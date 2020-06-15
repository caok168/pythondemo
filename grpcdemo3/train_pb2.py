# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: train.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='train.proto',
  package='pca',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0btrain.proto\x12\x03pca\"\'\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"D\n\x12\x44\x61taPrepareRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x0f\n\x07message\x18\x03 \x01(\t\"2\n\x13\x44\x61taPrepareResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0b\x32\x0b.pca.Status\"3\n\x0cTrainRequest\x12#\n\nparameters\x18\x01 \x01(\x0b\x32\x0f.pca.Parameters\"=\n\rTrainResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0b\x32\x0b.pca.Status\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\r\n\x0bTestRequest\"+\n\x0cTestResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0b\x32\x0b.pca.Status\"6\n\nParameters\x12\n\n\x02lr\x18\x01 \x01(\x02\x12\r\n\x05\x65poch\x18\x02 \x01(\x05\x12\r\n\x05\x62\x61tch\x18\x03 \x01(\x05\x32\xb5\x01\n\x0cTrainService\x12\x42\n\x0bLoadDataSet\x12\x17.pca.DataPrepareRequest\x1a\x18.pca.DataPrepareResponse\"\x00\x12\x32\n\x05Train\x12\x11.pca.TrainRequest\x1a\x12.pca.TrainResponse\"\x00\x30\x01\x12-\n\x04Test\x12\x10.pca.TestRequest\x1a\x11.pca.TestResponse\"\x00\x62\x06proto3'
)




_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='pca.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pca.Status.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pca.Status.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=59,
)


_DATAPREPAREREQUEST = _descriptor.Descriptor(
  name='DataPrepareRequest',
  full_name='pca.DataPrepareRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pca.DataPrepareRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='pca.DataPrepareRequest.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pca.DataPrepareRequest.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=129,
)


_DATAPREPARERESPONSE = _descriptor.Descriptor(
  name='DataPrepareResponse',
  full_name='pca.DataPrepareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pca.DataPrepareResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=181,
)


_TRAINREQUEST = _descriptor.Descriptor(
  name='TrainRequest',
  full_name='pca.TrainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters', full_name='pca.TrainRequest.parameters', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=234,
)


_TRAINRESPONSE = _descriptor.Descriptor(
  name='TrainResponse',
  full_name='pca.TrainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pca.TrainResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='pca.TrainResponse.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=297,
)


_TESTREQUEST = _descriptor.Descriptor(
  name='TestRequest',
  full_name='pca.TestRequest',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=312,
)


_TESTRESPONSE = _descriptor.Descriptor(
  name='TestResponse',
  full_name='pca.TestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pca.TestResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=357,
)


_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='pca.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lr', full_name='pca.Parameters.lr', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='pca.Parameters.epoch', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch', full_name='pca.Parameters.batch', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=413,
)

_DATAPREPARERESPONSE.fields_by_name['status'].message_type = _STATUS
_TRAINREQUEST.fields_by_name['parameters'].message_type = _PARAMETERS
_TRAINRESPONSE.fields_by_name['status'].message_type = _STATUS
_TESTRESPONSE.fields_by_name['status'].message_type = _STATUS
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['DataPrepareRequest'] = _DATAPREPAREREQUEST
DESCRIPTOR.message_types_by_name['DataPrepareResponse'] = _DATAPREPARERESPONSE
DESCRIPTOR.message_types_by_name['TrainRequest'] = _TRAINREQUEST
DESCRIPTOR.message_types_by_name['TrainResponse'] = _TRAINRESPONSE
DESCRIPTOR.message_types_by_name['TestRequest'] = _TESTREQUEST
DESCRIPTOR.message_types_by_name['TestResponse'] = _TESTRESPONSE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'train_pb2'
  # @@protoc_insertion_point(class_scope:pca.Status)
  })
_sym_db.RegisterMessage(Status)

DataPrepareRequest = _reflection.GeneratedProtocolMessageType('DataPrepareRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATAPREPAREREQUEST,
  '__module__' : 'train_pb2'
  # @@protoc_insertion_point(class_scope:pca.DataPrepareRequest)
  })
_sym_db.RegisterMessage(DataPrepareRequest)

DataPrepareResponse = _reflection.GeneratedProtocolMessageType('DataPrepareResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATAPREPARERESPONSE,
  '__module__' : 'train_pb2'
  # @@protoc_insertion_point(class_scope:pca.DataPrepareResponse)
  })
_sym_db.RegisterMessage(DataPrepareResponse)

TrainRequest = _reflection.GeneratedProtocolMessageType('TrainRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAINREQUEST,
  '__module__' : 'train_pb2'
  # @@protoc_insertion_point(class_scope:pca.TrainRequest)
  })
_sym_db.RegisterMessage(TrainRequest)

TrainResponse = _reflection.GeneratedProtocolMessageType('TrainResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRAINRESPONSE,
  '__module__' : 'train_pb2'
  # @@protoc_insertion_point(class_scope:pca.TrainResponse)
  })
_sym_db.RegisterMessage(TrainResponse)

TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTREQUEST,
  '__module__' : 'train_pb2'
  # @@protoc_insertion_point(class_scope:pca.TestRequest)
  })
_sym_db.RegisterMessage(TestRequest)

TestResponse = _reflection.GeneratedProtocolMessageType('TestResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESPONSE,
  '__module__' : 'train_pb2'
  # @@protoc_insertion_point(class_scope:pca.TestResponse)
  })
_sym_db.RegisterMessage(TestResponse)

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERS,
  '__module__' : 'train_pb2'
  # @@protoc_insertion_point(class_scope:pca.Parameters)
  })
_sym_db.RegisterMessage(Parameters)



_TRAINSERVICE = _descriptor.ServiceDescriptor(
  name='TrainService',
  full_name='pca.TrainService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=416,
  serialized_end=597,
  methods=[
  _descriptor.MethodDescriptor(
    name='LoadDataSet',
    full_name='pca.TrainService.LoadDataSet',
    index=0,
    containing_service=None,
    input_type=_DATAPREPAREREQUEST,
    output_type=_DATAPREPARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Train',
    full_name='pca.TrainService.Train',
    index=1,
    containing_service=None,
    input_type=_TRAINREQUEST,
    output_type=_TRAINRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Test',
    full_name='pca.TrainService.Test',
    index=2,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRAINSERVICE)

DESCRIPTOR.services_by_name['TrainService'] = _TRAINSERVICE

# @@protoc_insertion_point(module_scope)
