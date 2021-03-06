# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: categorizer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='categorizer.proto',
  package='categorizer',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x63\x61tegorizer.proto\x12\x0b\x63\x61tegorizer\"\'\n\x15\x43\x61tegorizationRequest\x12\x0e\n\x06offers\x18\x01 \x01(\t\"\xf2\x02\n\x16\x43\x61tegorizationResponse\x12O\n\x0e\x63\x61tegorization\x18\x01 \x03(\x0b\x32\x37.categorizer.CategorizationResponse.CategorizationEntry\x1a\x9b\x01\n\x0e\x43\x61tegorization\x12V\n\ncategories\x18\x01 \x03(\x0b\x32\x42.categorizer.CategorizationResponse.Categorization.CategoriesEntry\x1a\x31\n\x0f\x43\x61tegoriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1ai\n\x13\x43\x61tegorizationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.categorizer.CategorizationResponse.Categorization:\x02\x38\x01\x32\x66\n\x0b\x43\x61tegorizer\x12W\n\nCategorize\x12\".categorizer.CategorizationRequest\x1a#.categorizer.CategorizationResponse\"\x00\x62\x06proto3'
)




_CATEGORIZATIONREQUEST = _descriptor.Descriptor(
  name='CategorizationRequest',
  full_name='categorizer.CategorizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offers', full_name='categorizer.CategorizationRequest.offers', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=73,
)


_CATEGORIZATIONRESPONSE_CATEGORIZATION_CATEGORIESENTRY = _descriptor.Descriptor(
  name='CategoriesEntry',
  full_name='categorizer.CategorizationResponse.Categorization.CategoriesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='categorizer.CategorizationResponse.Categorization.CategoriesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='categorizer.CategorizationResponse.Categorization.CategoriesEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=339,
)

_CATEGORIZATIONRESPONSE_CATEGORIZATION = _descriptor.Descriptor(
  name='Categorization',
  full_name='categorizer.CategorizationResponse.Categorization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='categories', full_name='categorizer.CategorizationResponse.Categorization.categories', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CATEGORIZATIONRESPONSE_CATEGORIZATION_CATEGORIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=339,
)

_CATEGORIZATIONRESPONSE_CATEGORIZATIONENTRY = _descriptor.Descriptor(
  name='CategorizationEntry',
  full_name='categorizer.CategorizationResponse.CategorizationEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='categorizer.CategorizationResponse.CategorizationEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='categorizer.CategorizationResponse.CategorizationEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=446,
)

_CATEGORIZATIONRESPONSE = _descriptor.Descriptor(
  name='CategorizationResponse',
  full_name='categorizer.CategorizationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='categorization', full_name='categorizer.CategorizationResponse.categorization', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CATEGORIZATIONRESPONSE_CATEGORIZATION, _CATEGORIZATIONRESPONSE_CATEGORIZATIONENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=446,
)

_CATEGORIZATIONRESPONSE_CATEGORIZATION_CATEGORIESENTRY.containing_type = _CATEGORIZATIONRESPONSE_CATEGORIZATION
_CATEGORIZATIONRESPONSE_CATEGORIZATION.fields_by_name['categories'].message_type = _CATEGORIZATIONRESPONSE_CATEGORIZATION_CATEGORIESENTRY
_CATEGORIZATIONRESPONSE_CATEGORIZATION.containing_type = _CATEGORIZATIONRESPONSE
_CATEGORIZATIONRESPONSE_CATEGORIZATIONENTRY.fields_by_name['value'].message_type = _CATEGORIZATIONRESPONSE_CATEGORIZATION
_CATEGORIZATIONRESPONSE_CATEGORIZATIONENTRY.containing_type = _CATEGORIZATIONRESPONSE
_CATEGORIZATIONRESPONSE.fields_by_name['categorization'].message_type = _CATEGORIZATIONRESPONSE_CATEGORIZATIONENTRY
DESCRIPTOR.message_types_by_name['CategorizationRequest'] = _CATEGORIZATIONREQUEST
DESCRIPTOR.message_types_by_name['CategorizationResponse'] = _CATEGORIZATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CategorizationRequest = _reflection.GeneratedProtocolMessageType('CategorizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORIZATIONREQUEST,
  '__module__' : 'categorizer_pb2'
  # @@protoc_insertion_point(class_scope:categorizer.CategorizationRequest)
  })
_sym_db.RegisterMessage(CategorizationRequest)

CategorizationResponse = _reflection.GeneratedProtocolMessageType('CategorizationResponse', (_message.Message,), {

  'Categorization' : _reflection.GeneratedProtocolMessageType('Categorization', (_message.Message,), {

    'CategoriesEntry' : _reflection.GeneratedProtocolMessageType('CategoriesEntry', (_message.Message,), {
      'DESCRIPTOR' : _CATEGORIZATIONRESPONSE_CATEGORIZATION_CATEGORIESENTRY,
      '__module__' : 'categorizer_pb2'
      # @@protoc_insertion_point(class_scope:categorizer.CategorizationResponse.Categorization.CategoriesEntry)
      })
    ,
    'DESCRIPTOR' : _CATEGORIZATIONRESPONSE_CATEGORIZATION,
    '__module__' : 'categorizer_pb2'
    # @@protoc_insertion_point(class_scope:categorizer.CategorizationResponse.Categorization)
    })
  ,

  'CategorizationEntry' : _reflection.GeneratedProtocolMessageType('CategorizationEntry', (_message.Message,), {
    'DESCRIPTOR' : _CATEGORIZATIONRESPONSE_CATEGORIZATIONENTRY,
    '__module__' : 'categorizer_pb2'
    # @@protoc_insertion_point(class_scope:categorizer.CategorizationResponse.CategorizationEntry)
    })
  ,
  'DESCRIPTOR' : _CATEGORIZATIONRESPONSE,
  '__module__' : 'categorizer_pb2'
  # @@protoc_insertion_point(class_scope:categorizer.CategorizationResponse)
  })
_sym_db.RegisterMessage(CategorizationResponse)
_sym_db.RegisterMessage(CategorizationResponse.Categorization)
_sym_db.RegisterMessage(CategorizationResponse.Categorization.CategoriesEntry)
_sym_db.RegisterMessage(CategorizationResponse.CategorizationEntry)


_CATEGORIZATIONRESPONSE_CATEGORIZATION_CATEGORIESENTRY._options = None
_CATEGORIZATIONRESPONSE_CATEGORIZATIONENTRY._options = None

_CATEGORIZER = _descriptor.ServiceDescriptor(
  name='Categorizer',
  full_name='categorizer.Categorizer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=448,
  serialized_end=550,
  methods=[
  _descriptor.MethodDescriptor(
    name='Categorize',
    full_name='categorizer.Categorizer.Categorize',
    index=0,
    containing_service=None,
    input_type=_CATEGORIZATIONREQUEST,
    output_type=_CATEGORIZATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CATEGORIZER)

DESCRIPTOR.services_by_name['Categorizer'] = _CATEGORIZER

# @@protoc_insertion_point(module_scope)
