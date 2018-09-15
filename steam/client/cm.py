import logging
import struct
import binascii
import gzip
import contextlib
import asyncio

from steam.utils.evenemitter import EventEmitter
from ..utils.crypto import generate_session_key, symmetric_encrypt, symmetric_decrypt
from .connection import TCPConnection, CMConnectionError
from ..utils import clear_proto_mask, is_proto_msg
from ..base.msg.emsg import EMsg
from ..base.msg.types import EResult
from ..base.msg import ChannelMsg, ExtendedMsg, ProtoMsg


LOG = logging.getLogger("CMClient")


class CMClient(EventEmitter):
    EVENT_CHANNEL_CONNECTED = 'event_channel_connected'
    server_addr = None
    connected = False
    connecting = False
    session_key = None
    hmac_key = None
    steamid = 0
    client_sessionid = 0
    connection = None
    msg_loop = None
    _heart_beat_loop = None

    def __init__(self, loop=None):
        EventEmitter.__init__(self, loop)
        self.connection = TCPConnection(loop)
        self._loop = loop

    async def connect(self, address):
        if self.connection.connected:
            LOG.info("We are already connected, nothing to do.")
            return False

        if self.connecting:
            LOG.info("Connecting now, ignore this.")
            return

        self.connecting = True
        LOG.info("Connecting to server (%s:%s)" % address)
        try:
            result = await self.connection.connect(address)
        except CMConnectionError as exc:
            LOG.exception(exc)
            self.disconnect()
            return False

        if result:
            self.connected = True
            self.connecting = False
            self.address = address
        else:
            self.connecting = False
            LOG.error("Failed to connect server(%s), retry it later", repr(address))
            return False

        LOG.info('Successful connected to server (%s:%s)' % address)
        self.msg_loop = asyncio.ensure_future(self.message_recv_loop(), loop=self._loop)
        return result

    async def message_recv_loop(self):
        while self.connected:
            message = await self.connection.recv_queue.get()
            if self.session_key:
                message = symmetric_decrypt(message, self.session_key, self.hmac_key)

            try:
                message = self.parse_message(message)
                self.on_msg_received(message)
            except Exception as exc:
                LOG.exception(exc)

    def parse_message(self, msg):
        raw_type, = struct.unpack_from("<I", msg)
        emsg = EMsg(clear_proto_mask(raw_type))
        LOG.info("<- Receive message: %s", repr(emsg))

        if emsg.value in (EMsg.ChannelEncryptRequest,
                          EMsg.ChannelEncryptResult):
            msg = ChannelMsg(emsg, msg)
        elif is_proto_msg(raw_type):
            msg = ProtoMsg(emsg, msg)
        else:
            msg = ExtendedMsg(emsg, msg)

        return msg

    def on_msg_received(self, msg):
        if msg.emsg == EMsg.ChannelEncryptRequest:
            self._handle_encrypt_request(msg)
        elif msg.emsg == EMsg.ChannelEncryptResult:
            self._handle_encrypt_result(msg)
        elif msg.emsg == EMsg.Multi:
            self._handle_mutil(msg)
        elif msg.emsg == EMsg.ClientLogOnResponse:
            self._handle_logon_response(msg)
        elif msg.emsg == EMsg.ClientLogOff:
            self._handle_logoff(msg)
        elif msg.emsg == EMsg.ClientServerList:
            self._handle_server_list(msg)

        self.emit(msg.emsg, msg)

    def _handle_encrypt_request(self, msg):
        resp = ChannelMsg(EMsg.ChannelEncryptResponse)
        self.tmp_challenge = msg.body.challenge
        self.tmp_key, resp.body.key = generate_session_key(msg.body.challenge)

        resp.body.crc = binascii.crc32(resp.body.key) & 0xffffffff
        self.send(resp)

    def _handle_encrypt_result(self, msg):
        if msg.body.result != EResult.OK:
            raise ValueError("Channel encrypt error: %s" % repr(msg.body.result))

        self.session_key = self.tmp_key
        if self.tmp_challenge:
            self.hmac_key = self.session_key[:16]
            LOG.debug("Secured Connection with hmac")
        else:
            LOG.debug("Secured Connection with legacy mode")

        self.emit(CMClient.EVENT_CHANNEL_CONNECTED)

        del self.tmp_key
        del self.tmp_challenge

    def _handle_mutil(self, msg):
        size = struct.calcsize("<I")
        if msg.body.size_unzipped > 0:
            data = gzip.decompress(msg.body.message_body)
        else:
            data = msg.body.message_body

        while data:
            msg_length, = struct.unpack_from("<I", data)
            self.on_msg_received(self.parse_message(data[size:msg_length + size]))
            data = data[msg_length + size:]

    def _handle_logon_response(self, msg):
        if msg.body.eresult == EResult.OK:
            self.steamid = msg.header.steamid
            self.client_sessionid = msg.header.client_sessionid
            self._heart_beat_loop = asyncio.ensure_future(self.start_heart_beat(
                msg.body.out_of_game_heartbeat_seconds))

    def _handle_logoff(self, msg):
        pass

    def _handle_server_list(self, msg):
        pass

    async def start_heart_beat(self, seconds):
        LOG.info('Start heartbeat after %d seconds', seconds)
        while self.connection.connected:
            delay = seconds
            await asyncio.sleep(delay, loop=self._loop)
            msg = ProtoMsg(EMsg.ClientHeartBeat)
            self.send(msg)

    def send(self, msg):
        if isinstance(msg, (ProtoMsg, ExtendedMsg)):
            if self.steamid:
                msg.header.steamid = self.steamid

            if self.client_sessionid:
                msg.header.client_sessionid = self.client_sessionid

        message = msg.serialize()
        if self.session_key:
            message = symmetric_encrypt(message, self.session_key, self.hmac_key)
        packet = struct.pack("<II", len(message), self.connection.MAGIC) + message
        LOG.info("-> Send message: %s" % (repr(msg.emsg)))
        self.connection.send_queue.put_nowait(packet)

    def disconnect(self):
        self.server_addr = None
        self.client_sessionid = None
        self.hmac_key = None
        self.session_key = None
        self.steamid = None
        self.connection.disconnect()
        if self._heart_beat_loop:
            self._heart_beat_loop.cancel()
        self.msg_loop.cancel()
