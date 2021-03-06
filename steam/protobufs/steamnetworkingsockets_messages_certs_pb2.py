# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steam/protobufs/steamnetworkingsockets_messages_certs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='steam/protobufs/steamnetworkingsockets_messages_certs.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\200\001\000'),
  serialized_pb=_b('\n;steam/protobufs/steamnetworkingsockets_messages_certs.proto\"\x89\x02\n\x1c\x43MsgSteamDatagramCertificate\x12\x41\n\x08key_type\x18\x01 \x01(\x0e\x32&.CMsgSteamDatagramCertificate.EKeyType:\x07INVALID\x12\x10\n\x08key_data\x18\x02 \x01(\x0c\x12\x10\n\x08steam_id\x18\x04 \x01(\x06\x12!\n\x19gameserver_datacenter_ids\x18\x05 \x03(\x07\x12\x14\n\x0ctime_created\x18\x08 \x01(\x07\x12\x13\n\x0btime_expiry\x18\t \x01(\x07\x12\x0e\n\x06\x61pp_id\x18\n \x01(\r\"$\n\x08\x45KeyType\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07\x45\x44\x32\x35\x35\x31\x39\x10\x01\"[\n\"CMsgSteamDatagramCertificateSigned\x12\x0c\n\x04\x63\x65rt\x18\x04 \x01(\x0c\x12\x11\n\tca_key_id\x18\x05 \x01(\x06\x12\x14\n\x0c\x63\x61_signature\x18\x06 \x01(\x0c\x42\x03\x80\x01\x00')
)



_CMSGSTEAMDATAGRAMCERTIFICATE_EKEYTYPE = _descriptor.EnumDescriptor(
  name='EKeyType',
  full_name='CMsgSteamDatagramCertificate.EKeyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ED25519', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=293,
  serialized_end=329,
)
_sym_db.RegisterEnumDescriptor(_CMSGSTEAMDATAGRAMCERTIFICATE_EKEYTYPE)


_CMSGSTEAMDATAGRAMCERTIFICATE = _descriptor.Descriptor(
  name='CMsgSteamDatagramCertificate',
  full_name='CMsgSteamDatagramCertificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_type', full_name='CMsgSteamDatagramCertificate.key_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_data', full_name='CMsgSteamDatagramCertificate.key_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steam_id', full_name='CMsgSteamDatagramCertificate.steam_id', index=2,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameserver_datacenter_ids', full_name='CMsgSteamDatagramCertificate.gameserver_datacenter_ids', index=3,
      number=5, type=7, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_created', full_name='CMsgSteamDatagramCertificate.time_created', index=4,
      number=8, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_expiry', full_name='CMsgSteamDatagramCertificate.time_expiry', index=5,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='CMsgSteamDatagramCertificate.app_id', index=6,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CMSGSTEAMDATAGRAMCERTIFICATE_EKEYTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=329,
)


_CMSGSTEAMDATAGRAMCERTIFICATESIGNED = _descriptor.Descriptor(
  name='CMsgSteamDatagramCertificateSigned',
  full_name='CMsgSteamDatagramCertificateSigned',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cert', full_name='CMsgSteamDatagramCertificateSigned.cert', index=0,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ca_key_id', full_name='CMsgSteamDatagramCertificateSigned.ca_key_id', index=1,
      number=5, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ca_signature', full_name='CMsgSteamDatagramCertificateSigned.ca_signature', index=2,
      number=6, type=12, cpp_type=9, label=1,
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
  serialized_start=331,
  serialized_end=422,
)

_CMSGSTEAMDATAGRAMCERTIFICATE.fields_by_name['key_type'].enum_type = _CMSGSTEAMDATAGRAMCERTIFICATE_EKEYTYPE
_CMSGSTEAMDATAGRAMCERTIFICATE_EKEYTYPE.containing_type = _CMSGSTEAMDATAGRAMCERTIFICATE
DESCRIPTOR.message_types_by_name['CMsgSteamDatagramCertificate'] = _CMSGSTEAMDATAGRAMCERTIFICATE
DESCRIPTOR.message_types_by_name['CMsgSteamDatagramCertificateSigned'] = _CMSGSTEAMDATAGRAMCERTIFICATESIGNED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CMsgSteamDatagramCertificate = _reflection.GeneratedProtocolMessageType('CMsgSteamDatagramCertificate', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMDATAGRAMCERTIFICATE,
  __module__ = 'steam.protobufs.steamnetworkingsockets_messages_certs_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamDatagramCertificate)
  ))
_sym_db.RegisterMessage(CMsgSteamDatagramCertificate)

CMsgSteamDatagramCertificateSigned = _reflection.GeneratedProtocolMessageType('CMsgSteamDatagramCertificateSigned', (_message.Message,), dict(
  DESCRIPTOR = _CMSGSTEAMDATAGRAMCERTIFICATESIGNED,
  __module__ = 'steam.protobufs.steamnetworkingsockets_messages_certs_pb2'
  # @@protoc_insertion_point(class_scope:CMsgSteamDatagramCertificateSigned)
  ))
_sym_db.RegisterMessage(CMsgSteamDatagramCertificateSigned)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
