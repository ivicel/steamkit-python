import asyncio
import contextlib
import socket
import struct
import logging

LOG = logging.getLogger("Connection")


class TCPConnection:
    server_addr = None
    connected = False
    recv_queue = None
    send_queue = None
    _packet_header_fmt = "<II"
    _packet_header_size = struct.calcsize(_packet_header_fmt)
    MAGIC = 0x31305456

    def __init__(self, loop):
        self._loop = loop
        self.recv_loop = None
        self.send_loop = None
        self.init_queue()

    async def connect(self, address):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.settimeout(60)
        self._sock.setblocking(False)
        try:
            await self._loop.sock_connect(self._sock, address)
        except OSError:
            raise CMConnectionError("Error to connect CM server[%s]" % address)

        self.connected = True
        self.recv_loop = asyncio.ensure_future(self.read_packet(), loop=self._loop)
        self.send_loop = asyncio.ensure_future(self.send_packet(), loop=self._loop)
        return True

    @property
    def local_address(self):
        return self._sock.getsockname()[0]

    async def read_packet(self):
        # try:
        while self.connected:
            data = await self.read(8)
            if len(data) != 8:
                raise CMConnectionError("Got wrong length of packet header: %s" % repr(data))

            msg_length, magic = struct.unpack_from(TCPConnection._packet_header_fmt, data)

            if magic != TCPConnection.MAGIC:
                raise CMConnectionError("Error magic number, need '%s' but got '%s'" %
                                        (hex(TCPConnection.MAGIC), hex(magic)))

            message = await self.read(msg_length)
            await self.recv_queue.put(message)
        # except Exception as exc:
        #     LOG.error('Receive connection error: %s', exc)

    def disconnect(self):
        self.connected = False
        self.init_queue()
        self._sock.close()
        self.recv_loop.cancel()
        self.send_loop.cancel()

    def init_queue(self):
        self.recv_queue = asyncio.Queue(loop=self._loop)
        self.send_queue = asyncio.Queue(loop=self._loop)

    async def read(self, nlen):
        buf = b''
        need_to_read = nlen
        while need_to_read > 0:
            data = await self._loop.sock_recv(self._sock, need_to_read)
            if not data:
                break
            need_to_read -= len(data)
            buf += data

        return buf

    async def send_packet(self):
        await asyncio.sleep(.5)
        while self.connected:
            packet = await self.send_queue.get()
            await self._loop.sock_sendall(self._sock, packet)


class CMConnectionError(Exception):
    pass
