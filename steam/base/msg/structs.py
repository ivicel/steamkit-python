import struct

from ..msg.emsg import EMsg
from ..msg.types import EResult
from .types import EUniverse


class ChannelEncryptRequest:
    fmt = "<II"
    emsg = EMsg.ChannelEncryptRequest
    protocol_version = 1
    universe = EUniverse.Invalid
    challenge = b''

    def __init__(self, data):
        self.protocol_version, self.universe = struct.unpack_from(ChannelEncryptRequest.fmt, data)
        size = struct.calcsize(ChannelEncryptRequest.fmt)
        self.challenge = data[size:]


class ChannelEncryptResponse:
    protocol_version = 1
    key_size = 128
    key = None
    crc = None
    end = 0

    def serialize(self):
        return struct.pack("<II128sII",
                           self.protocol_version,
                           self.key_size,
                           self.key,
                           self.crc,
                           self.end)


class ChannelEncryptResult:
    result = EResult.Invalid

    def __init__(self, data):
        r, = struct.unpack_from("<I", data)
        self.result = EResult(r)


channels = {
    EMsg.ChannelEncryptRequest: ChannelEncryptRequest,
    EMsg.ChannelEncryptResponse: ChannelEncryptResponse,
    EMsg.ChannelEncryptResult: ChannelEncryptResult
}


def get_channel(msg, *args):
    cls = channels.get(msg, None)
    if not cls:
        raise ValueError("EMsg doesn't match: %s" % repr(msg))

    return cls(*args) if len(args) > 0 and args[0] is not None else cls()
