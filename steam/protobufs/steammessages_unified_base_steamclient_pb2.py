# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steam/protobufs/steammessages_unified_base_steamclient.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steam/protobufs/steammessages_unified_base_steamclient.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('H\001\200\001\000'),
  serialized_pb=_b('\n<steam/protobufs/steammessages_unified_base_steamclient.proto\x1a google/protobuf/descriptor.proto\"\x0c\n\nNoResponse*]\n\x13\x45ProtoExecutionSite\x12 \n\x1ck_EProtoExecutionSiteUnknown\x10\x00\x12$\n k_EProtoExecutionSiteSteamClient\x10\x02:4\n\x0b\x64\x65scription\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\t:>\n\x13service_description\x12\x1f.google.protobuf.ServiceOptions\x18\xd0\x86\x03 \x01(\t:u\n\x16service_execution_site\x12\x1f.google.protobuf.ServiceOptions\x18\xd8\x86\x03 \x01(\x0e\x32\x14.EProtoExecutionSite:\x1ck_EProtoExecutionSiteUnknown:<\n\x12method_description\x12\x1e.google.protobuf.MethodOptions\x18\xd0\x86\x03 \x01(\t:8\n\x10\x65num_description\x12\x1c.google.protobuf.EnumOptions\x18\xd0\x86\x03 \x01(\t:C\n\x16\x65num_value_description\x12!.google.protobuf.EnumValueOptions\x18\xd0\x86\x03 \x01(\tB\x05H\x01\x80\x01\x00')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_EPROTOEXECUTIONSITE = _descriptor.EnumDescriptor(
  name='EProtoExecutionSite',
  full_name='EProtoExecutionSite',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_EProtoExecutionSiteUnknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EProtoExecutionSiteSteamClient', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=112,
  serialized_end=205,
)
_sym_db.RegisterEnumDescriptor(_EPROTOEXECUTIONSITE)

EProtoExecutionSite = enum_type_wrapper.EnumTypeWrapper(_EPROTOEXECUTIONSITE)
k_EProtoExecutionSiteUnknown = 0
k_EProtoExecutionSiteSteamClient = 2

DESCRIPTION_FIELD_NUMBER = 50000
description = _descriptor.FieldDescriptor(
  name='description', full_name='description', index=0,
  number=50000, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
SERVICE_DESCRIPTION_FIELD_NUMBER = 50000
service_description = _descriptor.FieldDescriptor(
  name='service_description', full_name='service_description', index=1,
  number=50000, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
SERVICE_EXECUTION_SITE_FIELD_NUMBER = 50008
service_execution_site = _descriptor.FieldDescriptor(
  name='service_execution_site', full_name='service_execution_site', index=2,
  number=50008, type=14, cpp_type=8, label=1,
  has_default_value=True, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
METHOD_DESCRIPTION_FIELD_NUMBER = 50000
method_description = _descriptor.FieldDescriptor(
  name='method_description', full_name='method_description', index=3,
  number=50000, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ENUM_DESCRIPTION_FIELD_NUMBER = 50000
enum_description = _descriptor.FieldDescriptor(
  name='enum_description', full_name='enum_description', index=4,
  number=50000, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ENUM_VALUE_DESCRIPTION_FIELD_NUMBER = 50000
enum_value_description = _descriptor.FieldDescriptor(
  name='enum_value_description', full_name='enum_value_description', index=5,
  number=50000, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_NORESPONSE = _descriptor.Descriptor(
  name='NoResponse',
  full_name='NoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=98,
  serialized_end=110,
)

DESCRIPTOR.message_types_by_name['NoResponse'] = _NORESPONSE
DESCRIPTOR.enum_types_by_name['EProtoExecutionSite'] = _EPROTOEXECUTIONSITE
DESCRIPTOR.extensions_by_name['description'] = description
DESCRIPTOR.extensions_by_name['service_description'] = service_description
DESCRIPTOR.extensions_by_name['service_execution_site'] = service_execution_site
DESCRIPTOR.extensions_by_name['method_description'] = method_description
DESCRIPTOR.extensions_by_name['enum_description'] = enum_description
DESCRIPTOR.extensions_by_name['enum_value_description'] = enum_value_description
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoResponse = _reflection.GeneratedProtocolMessageType('NoResponse', (_message.Message,), dict(
  DESCRIPTOR = _NORESPONSE,
  __module__ = 'steam.protobufs.steammessages_unified_base_steamclient_pb2'
  # @@protoc_insertion_point(class_scope:NoResponse)
  ))
_sym_db.RegisterMessage(NoResponse)

google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(description)
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(service_description)
service_execution_site.enum_type = _EPROTOEXECUTIONSITE
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(service_execution_site)
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(method_description)
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_description)
google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enum_value_description)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
