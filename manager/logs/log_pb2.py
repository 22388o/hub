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
  package='logs',
  syntax='proto3',
  serialized_pb=_b('\n\tlog.proto\x12\x04logs\"\x90\x01\n\x03Log\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\"\n\x05state\x18\x03 \x01(\x0b\x32\x11.logs.RouterStateH\x00\x12 \n\x07payment\x18\x04 \x01(\x0b\x32\r.logs.PaymentH\x00\x12-\n\x0e\x63hannel_change\x18\x05 \x01(\x0b\x32\x13.logs.ChannelChangeH\x00\x42\x06\n\x04\x64\x61ta\"D\n\x0bRouterState\x12\x1f\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\r.logs.Channel\x12\x14\n\x0c\x66ree_balance\x18\x02 \x01(\x04\"H\n\x07\x43hannel\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x14\n\x0cuser_balance\x18\x02 \x01(\x04\x12\x16\n\x0erouter_balance\x18\x03 \x01(\x04\"\x81\x01\n\x07Payment\x12#\n\x06status\x18\x01 \x01(\x0e\x32\x13.logs.PaymentStatus\x12\x0e\n\x06sender\x18\x02 \x01(\x04\x12\x10\n\x08receiver\x18\x03 \x01(\x04\x12\x0f\n\x07\x63han_id\x18\x04 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x04\x12\x0e\n\x06\x65\x61rned\x18\x06 \x01(\x03\"\xbe\x01\n\rChannelChange\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.logs.ChannelChangeType\x12\x0f\n\x07user_id\x18\x02 \x01(\x04\x12\x1b\n\x13\x63hange_user_balance\x18\x03 \x01(\x04\x12\x1d\n\x15\x63hange_router_balance\x18\x04 \x01(\x04\x12\x14\n\x0cuser_balance\x18\x05 \x01(\x04\x12\x16\n\x0erouter_balance\x18\x06 \x01(\x04\x12\x0b\n\x03\x66\x65\x65\x18\x07 \x01(\x04*G\n\rPaymentStatus\x12\x0b\n\x07success\x10\x00\x12\x16\n\x12unsufficient_funds\x10\x01\x12\x11\n\rexternal_fail\x10\x02*4\n\x11\x43hannelChangeType\x12\x08\n\x04open\x10\x00\x12\t\n\x05\x63lose\x10\x01\x12\n\n\x06udpate\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PAYMENTSTATUS = _descriptor.EnumDescriptor(
  name='PaymentStatus',
  full_name='logs.PaymentStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='success', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='unsufficient_funds', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='external_fail', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=635,
  serialized_end=706,
)
_sym_db.RegisterEnumDescriptor(_PAYMENTSTATUS)

PaymentStatus = enum_type_wrapper.EnumTypeWrapper(_PAYMENTSTATUS)
_CHANNELCHANGETYPE = _descriptor.EnumDescriptor(
  name='ChannelChangeType',
  full_name='logs.ChannelChangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='open', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='close', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='udpate', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=708,
  serialized_end=760,
)
_sym_db.RegisterEnumDescriptor(_CHANNELCHANGETYPE)

ChannelChangeType = enum_type_wrapper.EnumTypeWrapper(_CHANNELCHANGETYPE)
success = 0
unsufficient_funds = 1
external_fail = 2
open = 0
close = 1
udpate = 2



_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='logs.Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='logs.Log.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='logs.Log.state', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment', full_name='logs.Log.payment', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_change', full_name='logs.Log.channel_change', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
      name='data', full_name='logs.Log.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=20,
  serialized_end=164,
)


_ROUTERSTATE = _descriptor.Descriptor(
  name='RouterState',
  full_name='logs.RouterState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='logs.RouterState.channels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='free_balance', full_name='logs.RouterState.free_balance', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=166,
  serialized_end=234,
)


_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='logs.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='logs.Channel.user_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_balance', full_name='logs.Channel.user_balance', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='router_balance', full_name='logs.Channel.router_balance', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=236,
  serialized_end=308,
)


_PAYMENT = _descriptor.Descriptor(
  name='Payment',
  full_name='logs.Payment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='logs.Payment.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender', full_name='logs.Payment.sender', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='logs.Payment.receiver', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chan_id', full_name='logs.Payment.chan_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='logs.Payment.amount', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='earned', full_name='logs.Payment.earned', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=311,
  serialized_end=440,
)


_CHANNELCHANGE = _descriptor.Descriptor(
  name='ChannelChange',
  full_name='logs.ChannelChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='logs.ChannelChange.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='logs.ChannelChange.user_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_user_balance', full_name='logs.ChannelChange.change_user_balance', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_router_balance', full_name='logs.ChannelChange.change_router_balance', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_balance', full_name='logs.ChannelChange.user_balance', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='router_balance', full_name='logs.ChannelChange.router_balance', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fee', full_name='logs.ChannelChange.fee', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=443,
  serialized_end=633,
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

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), dict(
  DESCRIPTOR = _LOG,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logs.Log)
  ))
_sym_db.RegisterMessage(Log)

RouterState = _reflection.GeneratedProtocolMessageType('RouterState', (_message.Message,), dict(
  DESCRIPTOR = _ROUTERSTATE,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logs.RouterState)
  ))
_sym_db.RegisterMessage(RouterState)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), dict(
  DESCRIPTOR = _CHANNEL,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logs.Channel)
  ))
_sym_db.RegisterMessage(Channel)

Payment = _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENT,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logs.Payment)
  ))
_sym_db.RegisterMessage(Payment)

ChannelChange = _reflection.GeneratedProtocolMessageType('ChannelChange', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELCHANGE,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:logs.ChannelChange)
  ))
_sym_db.RegisterMessage(ChannelChange)


# @@protoc_insertion_point(module_scope)
