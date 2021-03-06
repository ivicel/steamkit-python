# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steam/protobufs/steammessages_clientlanp2p.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steam.protobufs import steammessages_base_pb2 as steam_dot_protobufs_dot_steammessages__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steam/protobufs/steammessages_clientlanp2p.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('H\001\200\001\000'),
  serialized_pb=_b('\n0steam/protobufs/steammessages_clientlanp2p.proto\x1a(steam/protobufs/steammessages_base.proto\"\x87\x01\n\x1d\x43MsgClientLANP2PRequestChunks\x12;\n\nchunk_keys\x18\x01 \x03(\x0b\x32\'.CMsgClientLANP2PRequestChunks.ChunkKey\x1a)\n\x08\x43hunkKey\x12\x10\n\x08\x64\x65pot_id\x18\x01 \x01(\r\x12\x0b\n\x03sha\x18\x02 \x01(\x0c\"\xe9\x01\n%CMsgClientLANP2PRequestChunksResponse\x12I\n\x0f\x63hunk_responses\x18\x01 \x03(\x0b\x32\x30.CMsgClientLANP2PRequestChunksResponse.ChunkData\x1au\n\tChunkData\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x10\n\x08\x64\x65pot_id\x18\x02 \x01(\r\x12\x0b\n\x03sha\x18\x03 \x01(\x0c\x12\x12\n\nchunk_data\x18\x04 \x01(\x0c\x12\x11\n\tencrypted\x18\x05 \x01(\x08\x12\x12\n\ncompressed\x18\x06 \x01(\x08\x42\x05H\x01\x80\x01\x00')
  ,
  dependencies=[steam_dot_protobufs_dot_steammessages__base__pb2.DESCRIPTOR,])




_CMSGCLIENTLANP2PREQUESTCHUNKS_CHUNKKEY = _descriptor.Descriptor(
  name='ChunkKey',
  full_name='CMsgClientLANP2PRequestChunks.ChunkKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='depot_id', full_name='CMsgClientLANP2PRequestChunks.ChunkKey.depot_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sha', full_name='CMsgClientLANP2PRequestChunks.ChunkKey.sha', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=230,
)

_CMSGCLIENTLANP2PREQUESTCHUNKS = _descriptor.Descriptor(
  name='CMsgClientLANP2PRequestChunks',
  full_name='CMsgClientLANP2PRequestChunks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_keys', full_name='CMsgClientLANP2PRequestChunks.chunk_keys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CMSGCLIENTLANP2PREQUESTCHUNKS_CHUNKKEY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=230,
)


_CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE_CHUNKDATA = _descriptor.Descriptor(
  name='ChunkData',
  full_name='CMsgClientLANP2PRequestChunksResponse.ChunkData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CMsgClientLANP2PRequestChunksResponse.ChunkData.result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depot_id', full_name='CMsgClientLANP2PRequestChunksResponse.ChunkData.depot_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sha', full_name='CMsgClientLANP2PRequestChunksResponse.ChunkData.sha', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_data', full_name='CMsgClientLANP2PRequestChunksResponse.ChunkData.chunk_data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encrypted', full_name='CMsgClientLANP2PRequestChunksResponse.ChunkData.encrypted', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compressed', full_name='CMsgClientLANP2PRequestChunksResponse.ChunkData.compressed', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=466,
)

_CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE = _descriptor.Descriptor(
  name='CMsgClientLANP2PRequestChunksResponse',
  full_name='CMsgClientLANP2PRequestChunksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_responses', full_name='CMsgClientLANP2PRequestChunksResponse.chunk_responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE_CHUNKDATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=466,
)

_CMSGCLIENTLANP2PREQUESTCHUNKS_CHUNKKEY.containing_type = _CMSGCLIENTLANP2PREQUESTCHUNKS
_CMSGCLIENTLANP2PREQUESTCHUNKS.fields_by_name['chunk_keys'].message_type = _CMSGCLIENTLANP2PREQUESTCHUNKS_CHUNKKEY
_CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE_CHUNKDATA.containing_type = _CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE
_CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE.fields_by_name['chunk_responses'].message_type = _CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE_CHUNKDATA
DESCRIPTOR.message_types_by_name['CMsgClientLANP2PRequestChunks'] = _CMSGCLIENTLANP2PREQUESTCHUNKS
DESCRIPTOR.message_types_by_name['CMsgClientLANP2PRequestChunksResponse'] = _CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CMsgClientLANP2PRequestChunks = _reflection.GeneratedProtocolMessageType('CMsgClientLANP2PRequestChunks', (_message.Message,), dict(

  ChunkKey = _reflection.GeneratedProtocolMessageType('ChunkKey', (_message.Message,), dict(
    DESCRIPTOR = _CMSGCLIENTLANP2PREQUESTCHUNKS_CHUNKKEY,
    __module__ = 'steam.protobufs.steammessages_clientlanp2p_pb2'
    # @@protoc_insertion_point(class_scope:CMsgClientLANP2PRequestChunks.ChunkKey)
    ))
  ,
  DESCRIPTOR = _CMSGCLIENTLANP2PREQUESTCHUNKS,
  __module__ = 'steam.protobufs.steammessages_clientlanp2p_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientLANP2PRequestChunks)
  ))
_sym_db.RegisterMessage(CMsgClientLANP2PRequestChunks)
_sym_db.RegisterMessage(CMsgClientLANP2PRequestChunks.ChunkKey)

CMsgClientLANP2PRequestChunksResponse = _reflection.GeneratedProtocolMessageType('CMsgClientLANP2PRequestChunksResponse', (_message.Message,), dict(

  ChunkData = _reflection.GeneratedProtocolMessageType('ChunkData', (_message.Message,), dict(
    DESCRIPTOR = _CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE_CHUNKDATA,
    __module__ = 'steam.protobufs.steammessages_clientlanp2p_pb2'
    # @@protoc_insertion_point(class_scope:CMsgClientLANP2PRequestChunksResponse.ChunkData)
    ))
  ,
  DESCRIPTOR = _CMSGCLIENTLANP2PREQUESTCHUNKSRESPONSE,
  __module__ = 'steam.protobufs.steammessages_clientlanp2p_pb2'
  # @@protoc_insertion_point(class_scope:CMsgClientLANP2PRequestChunksResponse)
  ))
_sym_db.RegisterMessage(CMsgClientLANP2PRequestChunksResponse)
_sym_db.RegisterMessage(CMsgClientLANP2PRequestChunksResponse.ChunkData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
