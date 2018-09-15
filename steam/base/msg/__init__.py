import abc

from steam.protobufs import steammessages_base_pb2
from steam.protobufs import steammessages_clientserver_login_pb2
from steam.protobufs import steammessages_clientserver_2_pb2
from steam.protobufs import steammessages_clientserver_friends_pb2
from steam.protobufs import steammessages_clientserver_pb2
from .emsg import EMsg
from .headers import MsgHdr, ExtendedMsgHdr, ProtoMsgHdr
from .structs import get_channel


defined_msg = {
    EMsg.Multi: steammessages_base_pb2.CMsgMulti,
    EMsg.ClientLogon: steammessages_clientserver_login_pb2.CMsgClientLogon,
    EMsg.ClientHeartBeat: steammessages_clientserver_login_pb2.CMsgClientHeartBeat,
    EMsg.ClientLogOnResponse: steammessages_clientserver_login_pb2.CMsgClientLogonResponse
}


cmsg_list = dict()
for cmsg_module in [steammessages_clientserver_pb2,
                    steammessages_base_pb2,
                    steammessages_clientserver_2_pb2,
                    steammessages_clientserver_friends_pb2,
                    steammessages_clientserver_login_pb2]:
    cmsg_names = list(filter(lambda s: s.startswith('CMsg'), cmsg_module.__dict__))
    for n in cmsg_names:
        cmsg_list.update({n: cmsg_module.__dict__[n]})


def get_cmsg(msg):
    if msg in defined_msg:
        return defined_msg[msg]

    if msg in cmsg_list:
        return cmsg_list[msg]

    return None


class BaseMsg(abc.ABC):
    header = None
    body = None

    @abc.abstractmethod
    def serialize(self):
        """serialize message to bytes"""

    @abc.abstractmethod
    def deserialize(self, data=None):
        """deserialize message from bytes"""

    @property
    def emsg(self):
        return self.header and self.header.emsg


class ChannelMsg(BaseMsg):
    def __init__(self, emsg, data=None):
        self.header = MsgHdr(emsg, data)
        self.body = get_channel(emsg, self.header.payload)

    def serialize(self):
        return self.header.serialize() + self.body.serialize()

    def deserialize(self, data=None):
        raise NotImplementedError()


class ExtendedMsg(BaseMsg):
    def __init__(self, emsg, data=None):
        self.header = ExtendedMsgHdr(emsg, data)

        if data:
            self.deserialize(self.header.payload)

    def serialize(self):
        pass

    def deserialize(self, data=None):
        pass

    @property
    def target_job_id(self):
        return self.header.target_job_id

    @property
    def source_job_id(self):
        return self.header.source_job_id


class ProtoMsg(BaseMsg):
    def __init__(self, emsg, data=None):
        self.header = ProtoMsgHdr(emsg, data)
        proto = get_cmsg(emsg)

        if proto:
            self.body = proto()

            if data:
                self.deserialize(self.header.payload)

    def serialize(self):
        return self.header.serialize() + self.body.SerializeToString()

    def deserialize(self, data=None):
        self.body.ParseFromString(data)
