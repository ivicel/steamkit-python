import abc
import struct

from .emsg import EMsg
from steam.utils.util import add_proto_mask
from steam.protobufs.steammessages_base_pb2 import CMsgProtoBufHeader


class BaseMsgHdr(abc.ABC):
    emsg = EMsg.Invalid

    def __init__(self, emsg, data=None):
        self.emsg = emsg
        if data is not None:
            self.deserialize(data)

    @abc.abstractmethod
    def serialize(self):
        """serialize header to bytes"""

    @abc.abstractmethod
    def deserialize(self, data):
        """deserialize header from bytes"""


class MsgHdr(BaseMsgHdr):
    channel_msg_fmt = "<Iqq"
    size = struct.calcsize(channel_msg_fmt)

    target_job_id = -1
    source_job_id = -1
    payload = None

    def serialize(self):
        try:
            buf = struct.pack(MsgHdr.channel_msg_fmt, self.emsg.value,
                              self.target_job_id, self.source_job_id)
        except Exception:
            raise ValueError("'%s' is not initialized." % self)

        return buf

    def deserialize(self, data):
        _, self.target_job_id, self.source_job_id = \
                struct.unpack_from(MsgHdr.channel_msg_fmt, data)
        self.payload = data[MsgHdr.size:]


class ExtendedMsgHdr(BaseMsgHdr):
    extended_msg_fmt = "<IBHqqB"
    size = struct.calcsize(extended_msg_fmt)

    header_size = 36
    header_version = 2
    target_job_id = -1
    source_job_id = -1
    header_canary = 239
    steamid = 0
    client_sessionid = 0
    payload = None

    def serialize(self):
        try:
            buf = struct.pack(ExtendedMsgHdr.extended_msg_fmt,
                              self.emsg.value,
                              self.header_size,
                              self.header_version,
                              self.target_job_id,
                              self.source_job_id,
                              self.header_canary,
                              self.steamid,
                              self.client_sessionid)
        except Exception:
            raise ValueError("'%s' is not initialized." % self)

        return buf

    def deserialize(self, data):
        # _, self.header_size, self.header_version, self.target_job_id, \
        #         self.source_job_id, self.header_canary, self.steam_id, \
        #         self.session_id = struct.unpack_from(ExtendedMsgHdr.extended_msg_fmt, data)
        self.payload = data[ExtendedMsgHdr.size:]


class ProtoMsgHdr(BaseMsgHdr):
    proto_msg_fmt = "<II"
    size = struct.calcsize(proto_msg_fmt)

    proto = None
    payload = None

    def __init__(self, emsg, data=None):
        self.proto = CMsgProtoBufHeader()
        BaseMsgHdr.__init__(self, emsg, data)

        if data:
            self.deserialize(data)

    def __getattr__(self, name):
        return self.__dict__.get(name, None) or getattr(self.proto, name)

    def __setattr__(self, key, value):
        if key in ('payload', 'proto', 'emsg'):
            self.__dict__[key] = value
        else:
            setattr(self.proto, key, value)

    def serialize(self):
        try:
            proto = self.proto.SerializeToString()
            buf = struct.pack(ProtoMsgHdr.proto_msg_fmt,
                              add_proto_mask(self.emsg.value),
                              len(proto)) + proto
        except Exception:
            raise ValueError("'%s' is not initialized." % self)

        return buf

    def deserialize(self, data):
        _, proto_length = struct.unpack_from(ProtoMsgHdr.proto_msg_fmt, data)
        proto_header_size = ProtoMsgHdr.size + proto_length
        self.proto.ParseFromString(data[ProtoMsgHdr.size:proto_header_size])
        self.payload = data[proto_header_size:]
