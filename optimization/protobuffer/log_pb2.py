# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='log.proto',
  package='logger',
  syntax='proto3',
  serialized_pb=_b('\n\tlog.proto\x12\x06logger\"\x96\x01\n\x03Log\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12$\n\x05state\x18\x02 \x01(\x0b\x32\x13.logger.RouterStateH\x00\x12\"\n\x07payment\x18\x03 \x01(\x0b\x32\x0f.logger.PaymentH\x00\x12/\n\x0e\x63hannel_change\x18\x04 \x01(\x0b\x32\x15.logger.ChannelChangeH\x00\x42\x06\n\x04\x64\x61ta\"\x87\x01\n\x0bRouterState\x12!\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x0f.logger.Channel\x12\x14\n\x0c\x66ree_balance\x18\x02 \x01(\x04\x12\x17\n\x0fpending_balance\x18\x03 \x01(\x04\x12&\n\x1e\x61verage_change_update_duration\x18\x04 \x01(\x04\"p\n\x07\x43hannel\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x14\n\x0cuser_balance\x18\x03 \x01(\x04\x12\x16\n\x0erouter_balance\x18\x04 \x01(\x04\x12\x12\n\nis_pending\x18\x05 \x01(\x08\"r\n\x07Payment\x12%\n\x06status\x18\x01 \x01(\x0e\x32\x15.logger.PaymentStatus\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x10\n\x08receiver\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x04\x12\x0e\n\x06\x65\x61rned\x18\x06 \x01(\x03\"\x98\x01\n\rChannelChange\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.logger.ChannelChangeType\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x12\n\nchannel_id\x18\x03 \x01(\t\x12\x14\n\x0cuser_balance\x18\x04 \x01(\x04\x12\x16\n\x0erouter_balance\x18\x05 \x01(\x04\x12\x0b\n\x03\x66\x65\x65\x18\x06 \x01(\x04*X\n\rPaymentStatus\x12\x0f\n\x0bstatus_null\x10\x00\x12\x0b\n\x07success\x10\x01\x12\x16\n\x12unsufficient_funds\x10\x02\x12\x11\n\rexternal_fail\x10\x03*r\n\x11\x43hannelChangeType\x12\x0f\n\x0b\x63hange_null\x10\x00\x12\x0c\n\x08openning\x10\x01\x12\n\n\x06opened\x10\x02\x12\x0b\n\x07\x63losing\x10\x03\x12\n\n\x06\x63losed\x10\x04\x12\x0c\n\x08updating\x10\x05\x12\x0b\n\x07updated\x10\x06\x62\x06proto3')
)

_PAYMENTSTATUS = _descriptor.EnumDescriptor(
  name='PaymentStatus',
  full_name='logger.PaymentStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='status_null', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='success', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='unsufficient_funds', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='external_fail', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=697,
  serialized_end=785,
)
_sym_db.RegisterEnumDescriptor(_PAYMENTSTATUS)

PaymentStatus = enum_type_wrapper.EnumTypeWrapper(_PAYMENTSTATUS)
_CHANNELCHANGETYPE = _descriptor.EnumDescriptor(
  name='ChannelChangeType',
  full_name='logger.ChannelChangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='change_null', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='openning', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='opened', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='closing', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='closed', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='updating', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='updated', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=787,
  serialized_end=901,
)
_sym_db.RegisterEnumDescriptor(_CHANNELCHANGETYPE)

ChannelChangeType = enum_type_wrapper.EnumTypeWrapper(_CHANNELCHANGETYPE)
status_null = 0
success = 1
unsufficient_funds = 2
external_fail = 3
change_null = 0
openning = 1
opened = 2
closing = 3
closed = 4
updating = 5
updated = 6



_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='logger.Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='logger.Log.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='logger.Log.state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment', full_name='logger.Log.payment', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_change', full_name='logger.Log.channel_change', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='logger.Log.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=22,
  serialized_end=172,
)


_ROUTERSTATE = _descriptor.Descriptor(
  name='RouterState',
  full_name='logger.RouterState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='logger.RouterState.channels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_balance', full_name='logger.RouterState.free_balance', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending_balance', full_name='logger.RouterState.pending_balance', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_change_update_duration', full_name='logger.RouterState.average_change_update_duration', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=310,
)


_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='logger.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='logger.Channel.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='logger.Channel.channel_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_balance', full_name='logger.Channel.user_balance', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='router_balance', full_name='logger.Channel.router_balance', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_pending', full_name='logger.Channel.is_pending', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=424,
)


_PAYMENT = _descriptor.Descriptor(
  name='Payment',
  full_name='logger.Payment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='logger.Payment.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender', full_name='logger.Payment.sender', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='logger.Payment.receiver', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='logger.Payment.amount', index=3,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='earned', full_name='logger.Payment.earned', index=4,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=540,
)


_CHANNELCHANGE = _descriptor.Descriptor(
  name='ChannelChange',
  full_name='logger.ChannelChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='logger.ChannelChange.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='logger.ChannelChange.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='logger.ChannelChange.channel_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_balance', full_name='logger.ChannelChange.user_balance', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='router_balance', full_name='logger.ChannelChange.router_balance', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee', full_name='logger.ChannelChange.fee', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=543,
  serialized_end=695,
)

_LOG.fields_by_name['state'].message_type = _ROUTERSTATE
_LOG.fields_by_name['payment'].message_type = _PAYMENT
_LOG.fields_by_name['channel_change'].message_type = _CHANNELCHANGE
_LOG.oneofs_by_name['data'].fields.append(
  _LOG.fields_by_name['state'])
_LOG.fields_by_name['state'].containing_oneof = _LOG.oneofs_by_name['data']
_LOG.oneofs_by_name['data'].fields.append(
  _LOG.fields_by_name['payment'])
_LOG.fields_by_name['payment'].containing_oneof = _LOG.oneofs_by_name['data']
_LOG.oneofs_by_name['data'].fields.append(
  _LOG.fields_by_name['channel_change'])
_LOG.fields_by_name['channel_change'].containing_oneof = _LOG.oneofs_by_name['data']
_ROUTERSTATE.fields_by_name['channels'].message_type = _CHANNEL
_PAYMENT.fields_by_name['status'].enum_type = _PAYMENTSTATUS
_CHANNELCHANGE.fields_by_name['type'].enum_type = _CHANNELCHANGETYPE
DESCRIPTOR.message_types_by_name['Log'] = _LOG
DESCRIPTOR.message_types_by_name['RouterState'] = _ROUTERSTATE
DESCRIPTOR.message_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.message_types_by_name['Payment'] = _PAYMENT
DESCRIPTOR.message_types_by_name['ChannelChange'] = _CHANNELCHANGE
DESCRIPTOR.enum_types_by_name['PaymentStatus'] = _PAYMENTSTATUS
DESCRIPTOR.enum_types_by_name['ChannelChangeType'] = _CHANNELCHANGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), dict(
  DESCRIPTOR = _LOG,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logger.Log)
  ))
_sym_db.RegisterMessage(Log)

RouterState = _reflection.GeneratedProtocolMessageType('RouterState', (_message.Message,), dict(
  DESCRIPTOR = _ROUTERSTATE,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logger.RouterState)
  ))
_sym_db.RegisterMessage(RouterState)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), dict(
  DESCRIPTOR = _CHANNEL,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logger.Channel)
  ))
_sym_db.RegisterMessage(Channel)

Payment = _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENT,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logger.Payment)
  ))
_sym_db.RegisterMessage(Payment)

ChannelChange = _reflection.GeneratedProtocolMessageType('ChannelChange', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELCHANGE,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logger.ChannelChange)
  ))
_sym_db.RegisterMessage(ChannelChange)


# @@protoc_insertion_point(module_scope)
