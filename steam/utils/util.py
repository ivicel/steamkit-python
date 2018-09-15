import socket
import struct

PROTO_MASK = 0x80000000
EMSG_MASK = ~PROTO_MASK


def clear_proto_mask(msg):
    return msg & EMSG_MASK


def add_proto_mask(msg):
    return (msg | PROTO_MASK) & 0xffffffff


def is_proto_msg(msg):
    return (msg & PROTO_MASK) > 1


def ip_to_int(ip):
    return struct.unpack(">L", socket.inet_pton(socket.AF_INET, ip))[0]
