// Code generated by protoc-gen-go. DO NOT EDIT.
// source: log.proto

/*
Package logs is a generated protocol buffer package.

It is generated from these files:
	log.proto

It has these top-level messages:
	Log
	RouterState
	Channel
	Payment
	ChannelChange
	UserChange
*/
package logs

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type PaymentStatus int32

const (
	// Null is used to catch that field wasn't initialised.
	PaymentStatus_status_null PaymentStatus = 0
	PaymentStatus_success     PaymentStatus = 1
	// UnsufficientFunds means that router haven't posses/locked enough funds
	// with receiver user to route thouth the payment.
	PaymentStatus_unsufficient_funds PaymentStatus = 2
	// ExternalFail means that receiver failed to receive payment because of
	// the unknown to us reason.
	PaymentStatus_external_fail PaymentStatus = 3
	// UserLocalFail means that from user's side all channel are in
	// pending states or not exist at all, or number of funds from user side
	// is not enough.
	PaymentStatus_user_local_fail PaymentStatus = 4
)

var PaymentStatus_name = map[int32]string{
	0: "status_null",
	1: "success",
	2: "unsufficient_funds",
	3: "external_fail",
	4: "user_local_fail",
}
var PaymentStatus_value = map[string]int32{
	"status_null":        0,
	"success":            1,
	"unsufficient_funds": 2,
	"external_fail":      3,
	"user_local_fail":    4,
}

func (x PaymentStatus) String() string {
	return proto.EnumName(PaymentStatus_name, int32(x))
}
func (PaymentStatus) EnumDescriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

// ChannelChangeType represent the type of action which were attempted to
// apply to the channel.
type ChannelChangeType int32

const (
	// ChangeNull identifies the null state of channel change, so that
	// receiver could identify that some mistake has happened.
	ChannelChangeType_change_null ChannelChangeType = 0
	ChannelChangeType_openning    ChannelChangeType = 1
	// Opened is used when this channel was just created, and haven't been in
	// local network before.
	ChannelChangeType_opened ChannelChangeType = 2
	// ...
	ChannelChangeType_closing ChannelChangeType = 3
	// Closed is used when number locked funds / balances of both channel
	// participant equal to zero.
	ChannelChangeType_closed ChannelChangeType = 4
	// ...
	ChannelChangeType_updating ChannelChangeType = 5
	// Updated is used when one of the participants decides to update its
	// channel balance.
	ChannelChangeType_updated ChannelChangeType = 6
)

var ChannelChangeType_name = map[int32]string{
	0: "change_null",
	1: "openning",
	2: "opened",
	3: "closing",
	4: "closed",
	5: "updating",
	6: "updated",
}
var ChannelChangeType_value = map[string]int32{
	"change_null": 0,
	"openning":    1,
	"opened":      2,
	"closing":     3,
	"closed":      4,
	"updating":    5,
	"updated":     6,
}

func (x ChannelChangeType) String() string {
	return proto.EnumName(ChannelChangeType_name, int32(x))
}
func (ChannelChangeType) EnumDescriptor() ([]byte, []int) { return fileDescriptor0, []int{1} }

// Log is the main object in the file which represent the log entry in the
// log file.
type Log struct {
	Time int64 `protobuf:"varint,1,opt,name=time" json:"time,omitempty"`
	// Types that are valid to be assigned to Data:
	//	*Log_State
	//	*Log_Payment
	//	*Log_ChannelChange
	//	*Log_UserChange
	Data isLog_Data `protobuf_oneof:"data"`
}

func (m *Log) Reset()                    { *m = Log{} }
func (m *Log) String() string            { return proto.CompactTextString(m) }
func (*Log) ProtoMessage()               {}
func (*Log) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

type isLog_Data interface{ isLog_Data() }

type Log_State struct {
	State *RouterState `protobuf:"bytes,2,opt,name=state,oneof"`
}
type Log_Payment struct {
	Payment *Payment `protobuf:"bytes,3,opt,name=payment,oneof"`
}
type Log_ChannelChange struct {
	ChannelChange *ChannelChange `protobuf:"bytes,4,opt,name=channel_change,json=channelChange,oneof"`
}
type Log_UserChange struct {
	UserChange *UserChange `protobuf:"bytes,5,opt,name=user_change,json=userChange,oneof"`
}

func (*Log_State) isLog_Data()         {}
func (*Log_Payment) isLog_Data()       {}
func (*Log_ChannelChange) isLog_Data() {}
func (*Log_UserChange) isLog_Data()    {}

func (m *Log) GetData() isLog_Data {
	if m != nil {
		return m.Data
	}
	return nil
}

func (m *Log) GetTime() int64 {
	if m != nil {
		return m.Time
	}
	return 0
}

func (m *Log) GetState() *RouterState {
	if x, ok := m.GetData().(*Log_State); ok {
		return x.State
	}
	return nil
}

func (m *Log) GetPayment() *Payment {
	if x, ok := m.GetData().(*Log_Payment); ok {
		return x.Payment
	}
	return nil
}

func (m *Log) GetChannelChange() *ChannelChange {
	if x, ok := m.GetData().(*Log_ChannelChange); ok {
		return x.ChannelChange
	}
	return nil
}

func (m *Log) GetUserChange() *UserChange {
	if x, ok := m.GetData().(*Log_UserChange); ok {
		return x.UserChange
	}
	return nil
}

// XXX_OneofFuncs is for the internal use of the proto package.
func (*Log) XXX_OneofFuncs() (func(msg proto.Message, b *proto.Buffer) error, func(msg proto.Message, tag, wire int, b *proto.Buffer) (bool, error), func(msg proto.Message) (n int), []interface{}) {
	return _Log_OneofMarshaler, _Log_OneofUnmarshaler, _Log_OneofSizer, []interface{}{
		(*Log_State)(nil),
		(*Log_Payment)(nil),
		(*Log_ChannelChange)(nil),
		(*Log_UserChange)(nil),
	}
}

func _Log_OneofMarshaler(msg proto.Message, b *proto.Buffer) error {
	m := msg.(*Log)
	// data
	switch x := m.Data.(type) {
	case *Log_State:
		b.EncodeVarint(2<<3 | proto.WireBytes)
		if err := b.EncodeMessage(x.State); err != nil {
			return err
		}
	case *Log_Payment:
		b.EncodeVarint(3<<3 | proto.WireBytes)
		if err := b.EncodeMessage(x.Payment); err != nil {
			return err
		}
	case *Log_ChannelChange:
		b.EncodeVarint(4<<3 | proto.WireBytes)
		if err := b.EncodeMessage(x.ChannelChange); err != nil {
			return err
		}
	case *Log_UserChange:
		b.EncodeVarint(5<<3 | proto.WireBytes)
		if err := b.EncodeMessage(x.UserChange); err != nil {
			return err
		}
	case nil:
	default:
		return fmt.Errorf("Log.Data has unexpected type %T", x)
	}
	return nil
}

func _Log_OneofUnmarshaler(msg proto.Message, tag, wire int, b *proto.Buffer) (bool, error) {
	m := msg.(*Log)
	switch tag {
	case 2: // data.state
		if wire != proto.WireBytes {
			return true, proto.ErrInternalBadWireType
		}
		msg := new(RouterState)
		err := b.DecodeMessage(msg)
		m.Data = &Log_State{msg}
		return true, err
	case 3: // data.payment
		if wire != proto.WireBytes {
			return true, proto.ErrInternalBadWireType
		}
		msg := new(Payment)
		err := b.DecodeMessage(msg)
		m.Data = &Log_Payment{msg}
		return true, err
	case 4: // data.channel_change
		if wire != proto.WireBytes {
			return true, proto.ErrInternalBadWireType
		}
		msg := new(ChannelChange)
		err := b.DecodeMessage(msg)
		m.Data = &Log_ChannelChange{msg}
		return true, err
	case 5: // data.user_change
		if wire != proto.WireBytes {
			return true, proto.ErrInternalBadWireType
		}
		msg := new(UserChange)
		err := b.DecodeMessage(msg)
		m.Data = &Log_UserChange{msg}
		return true, err
	default:
		return false, nil
	}
}

func _Log_OneofSizer(msg proto.Message) (n int) {
	m := msg.(*Log)
	// data
	switch x := m.Data.(type) {
	case *Log_State:
		s := proto.Size(x.State)
		n += proto.SizeVarint(2<<3 | proto.WireBytes)
		n += proto.SizeVarint(uint64(s))
		n += s
	case *Log_Payment:
		s := proto.Size(x.Payment)
		n += proto.SizeVarint(3<<3 | proto.WireBytes)
		n += proto.SizeVarint(uint64(s))
		n += s
	case *Log_ChannelChange:
		s := proto.Size(x.ChannelChange)
		n += proto.SizeVarint(4<<3 | proto.WireBytes)
		n += proto.SizeVarint(uint64(s))
		n += s
	case *Log_UserChange:
		s := proto.Size(x.UserChange)
		n += proto.SizeVarint(5<<3 | proto.WireBytes)
		n += proto.SizeVarint(uint64(s))
		n += s
	case nil:
	default:
		panic(fmt.Sprintf("proto: unexpected type %T in oneof", x))
	}
	return n
}

// RouterState is a type of log entry which describes the state/view of the
// router local lightning network and number of free funds which exist under
// control router.
type RouterState struct {
	// Channels represent the local lightning network topology.
	Channels []*Channel `protobuf:"bytes,1,rep,name=channels" json:"channels,omitempty"`
	// FreeBalance it is free number of funds under router managment which
	// could be used to lock them in the channels.
	FreeBalance uint64 `protobuf:"varint,2,opt,name=free_balance,json=freeBalance" json:"free_balance,omitempty"`
	// PendingBalance is the amount of funds which in the process of
	// being accepted by blockchain.
	PendingBalance uint64 `protobuf:"varint,3,opt,name=pending_balance,json=pendingBalance" json:"pending_balance,omitempty"`
}

func (m *RouterState) Reset()                    { *m = RouterState{} }
func (m *RouterState) String() string            { return proto.CompactTextString(m) }
func (*RouterState) ProtoMessage()               {}
func (*RouterState) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{1} }

func (m *RouterState) GetChannels() []*Channel {
	if m != nil {
		return m.Channels
	}
	return nil
}

func (m *RouterState) GetFreeBalance() uint64 {
	if m != nil {
		return m.FreeBalance
	}
	return 0
}

func (m *RouterState) GetPendingBalance() uint64 {
	if m != nil {
		return m.PendingBalance
	}
	return 0
}

// Channel is used as the building block in describing of the lightning
// network topology.
type Channel struct {
	UserId        string `protobuf:"bytes,1,opt,name=user_id,json=userId" json:"user_id,omitempty"`
	ChannelId     string `protobuf:"bytes,2,opt,name=channel_id,json=channelId" json:"channel_id,omitempty"`
	UserBalance   uint64 `protobuf:"varint,3,opt,name=user_balance,json=userBalance" json:"user_balance,omitempty"`
	RouterBalance uint64 `protobuf:"varint,4,opt,name=router_balance,json=routerBalance" json:"router_balance,omitempty"`
	IsPending     bool   `protobuf:"varint,5,opt,name=is_pending,json=isPending" json:"is_pending,omitempty"`
}

func (m *Channel) Reset()                    { *m = Channel{} }
func (m *Channel) String() string            { return proto.CompactTextString(m) }
func (*Channel) ProtoMessage()               {}
func (*Channel) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{2} }

func (m *Channel) GetUserId() string {
	if m != nil {
		return m.UserId
	}
	return ""
}

func (m *Channel) GetChannelId() string {
	if m != nil {
		return m.ChannelId
	}
	return ""
}

func (m *Channel) GetUserBalance() uint64 {
	if m != nil {
		return m.UserBalance
	}
	return 0
}

func (m *Channel) GetRouterBalance() uint64 {
	if m != nil {
		return m.RouterBalance
	}
	return 0
}

func (m *Channel) GetIsPending() bool {
	if m != nil {
		return m.IsPending
	}
	return false
}

// Payment represent the attempt of peer in the local lightning network to
// send the payment to some another peer in the network.
type Payment struct {
	Status   PaymentStatus `protobuf:"varint,1,opt,name=status,enum=logs.PaymentStatus" json:"status,omitempty"`
	Sender   string        `protobuf:"bytes,2,opt,name=sender" json:"sender,omitempty"`
	Receiver string        `protobuf:"bytes,3,opt,name=receiver" json:"receiver,omitempty"`
	Amount   uint64        `protobuf:"varint,5,opt,name=amount" json:"amount,omitempty"`
	// Earned is the number of funds which router earned by making this payment.
	// In case of rebalncing router will pay the fee, for that reason this
	// number will be negative.
	Earned int64 `protobuf:"varint,6,opt,name=earned" json:"earned,omitempty"`
}

func (m *Payment) Reset()                    { *m = Payment{} }
func (m *Payment) String() string            { return proto.CompactTextString(m) }
func (*Payment) ProtoMessage()               {}
func (*Payment) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{3} }

func (m *Payment) GetStatus() PaymentStatus {
	if m != nil {
		return m.Status
	}
	return PaymentStatus_status_null
}

func (m *Payment) GetSender() string {
	if m != nil {
		return m.Sender
	}
	return ""
}

func (m *Payment) GetReceiver() string {
	if m != nil {
		return m.Receiver
	}
	return ""
}

func (m *Payment) GetAmount() uint64 {
	if m != nil {
		return m.Amount
	}
	return 0
}

func (m *Payment) GetEarned() int64 {
	if m != nil {
		return m.Earned
	}
	return 0
}

type ChannelChange struct {
	Type          ChannelChangeType `protobuf:"varint,1,opt,name=type,enum=logs.ChannelChangeType" json:"type,omitempty"`
	UserId        string            `protobuf:"bytes,2,opt,name=user_id,json=userId" json:"user_id,omitempty"`
	ChannelId     string            `protobuf:"bytes,3,opt,name=channel_id,json=channelId" json:"channel_id,omitempty"`
	UserBalance   uint64            `protobuf:"varint,4,opt,name=user_balance,json=userBalance" json:"user_balance,omitempty"`
	RouterBalance uint64            `protobuf:"varint,5,opt,name=router_balance,json=routerBalance" json:"router_balance,omitempty"`
	// Fee which was taken by blockchain decentrilized computer /
	// mainers or some other form of smart contract manager.
	Fee uint64 `protobuf:"varint,6,opt,name=fee" json:"fee,omitempty"`
	// Duration which was taken by blockchain decentrilized computer to apply
	// this change (open, close, update).
	Duration int64 `protobuf:"varint,7,opt,name=duration" json:"duration,omitempty"`
}

func (m *ChannelChange) Reset()                    { *m = ChannelChange{} }
func (m *ChannelChange) String() string            { return proto.CompactTextString(m) }
func (*ChannelChange) ProtoMessage()               {}
func (*ChannelChange) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{4} }

func (m *ChannelChange) GetType() ChannelChangeType {
	if m != nil {
		return m.Type
	}
	return ChannelChangeType_change_null
}

func (m *ChannelChange) GetUserId() string {
	if m != nil {
		return m.UserId
	}
	return ""
}

func (m *ChannelChange) GetChannelId() string {
	if m != nil {
		return m.ChannelId
	}
	return ""
}

func (m *ChannelChange) GetUserBalance() uint64 {
	if m != nil {
		return m.UserBalance
	}
	return 0
}

func (m *ChannelChange) GetRouterBalance() uint64 {
	if m != nil {
		return m.RouterBalance
	}
	return 0
}

func (m *ChannelChange) GetFee() uint64 {
	if m != nil {
		return m.Fee
	}
	return 0
}

func (m *ChannelChange) GetDuration() int64 {
	if m != nil {
		return m.Duration
	}
	return 0
}

type UserChange struct {
	UserId      string `protobuf:"bytes,1,opt,name=user_id,json=userId" json:"user_id,omitempty"`
	IsConnected bool   `protobuf:"varint,2,opt,name=is_connected,json=isConnected" json:"is_connected,omitempty"`
}

func (m *UserChange) Reset()                    { *m = UserChange{} }
func (m *UserChange) String() string            { return proto.CompactTextString(m) }
func (*UserChange) ProtoMessage()               {}
func (*UserChange) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{5} }

func (m *UserChange) GetUserId() string {
	if m != nil {
		return m.UserId
	}
	return ""
}

func (m *UserChange) GetIsConnected() bool {
	if m != nil {
		return m.IsConnected
	}
	return false
}

func init() {
	proto.RegisterType((*Log)(nil), "logs.Log")
	proto.RegisterType((*RouterState)(nil), "logs.RouterState")
	proto.RegisterType((*Channel)(nil), "logs.Channel")
	proto.RegisterType((*Payment)(nil), "logs.Payment")
	proto.RegisterType((*ChannelChange)(nil), "logs.ChannelChange")
	proto.RegisterType((*UserChange)(nil), "logs.UserChange")
	proto.RegisterEnum("logs.PaymentStatus", PaymentStatus_name, PaymentStatus_value)
	proto.RegisterEnum("logs.ChannelChangeType", ChannelChangeType_name, ChannelChangeType_value)
}

func init() { proto.RegisterFile("log.proto", fileDescriptor0) }

var fileDescriptor0 = []byte{
	// 625 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x8c, 0x54, 0xcb, 0x6a, 0xdb, 0x40,
	0x14, 0xb5, 0x2c, 0x59, 0xb6, 0xaf, 0x62, 0x47, 0x99, 0x40, 0x22, 0x0a, 0x81, 0xc4, 0x50, 0x9a,
	0x07, 0x64, 0xd1, 0x6c, 0xbb, 0x4a, 0x36, 0x0e, 0x74, 0x11, 0x26, 0xed, 0x5a, 0x28, 0x9a, 0x6b,
	0x77, 0x40, 0x1e, 0x89, 0x99, 0x51, 0x69, 0xf6, 0xfd, 0x8a, 0x7e, 0x42, 0x3f, 0xad, 0xf4, 0x23,
	0xca, 0x3c, 0xa4, 0xc4, 0x34, 0x7d, 0xac, 0x3c, 0xf7, 0xdc, 0x73, 0x3c, 0x67, 0xce, 0xbd, 0x36,
	0x4c, 0xab, 0x7a, 0x7d, 0xd9, 0xc8, 0x5a, 0xd7, 0x24, 0xaa, 0xea, 0xb5, 0x5a, 0xfc, 0x08, 0x20,
	0x7c, 0x5f, 0xaf, 0x09, 0x81, 0x48, 0xf3, 0x0d, 0x66, 0xc1, 0x71, 0x70, 0x1a, 0x52, 0x7b, 0x26,
	0x67, 0x30, 0x52, 0xba, 0xd0, 0x98, 0x0d, 0x8f, 0x83, 0xd3, 0xe4, 0xed, 0xde, 0xa5, 0x51, 0x5c,
	0xd2, 0xba, 0xd5, 0x28, 0xef, 0x4d, 0x63, 0x39, 0xa0, 0x8e, 0x41, 0xce, 0x60, 0xdc, 0x14, 0x8f,
	0x1b, 0x14, 0x3a, 0x0b, 0x2d, 0x79, 0xe6, 0xc8, 0x77, 0x0e, 0x5c, 0x0e, 0x68, 0xd7, 0x27, 0xef,
	0x60, 0x5e, 0x7e, 0x2a, 0x84, 0xc0, 0x2a, 0x37, 0x9f, 0x6b, 0xcc, 0x22, 0xab, 0xd8, 0x77, 0x8a,
	0x1b, 0xd7, 0xbb, 0xb1, 0xad, 0xe5, 0x80, 0xce, 0xca, 0xe7, 0x00, 0xb9, 0x82, 0xa4, 0x55, 0x28,
	0x3b, 0xe9, 0xc8, 0x4a, 0x53, 0x27, 0xfd, 0xa8, 0x50, 0xf6, 0x3a, 0x68, 0xfb, 0xea, 0x3a, 0x86,
	0x88, 0x15, 0xba, 0x58, 0x7c, 0x0d, 0x20, 0x79, 0x66, 0x9f, 0x9c, 0xc1, 0xc4, 0x7f, 0xbb, 0xca,
	0x82, 0xe3, 0xf0, 0xc9, 0xb6, 0x37, 0x41, 0xfb, 0x36, 0x39, 0x81, 0x9d, 0x95, 0x44, 0xcc, 0x1f,
	0x8a, 0xaa, 0x10, 0xa5, 0x8b, 0x24, 0xa2, 0x89, 0xc1, 0xae, 0x1d, 0x44, 0xde, 0xc0, 0x6e, 0x83,
	0x82, 0x71, 0xb1, 0xee, 0x59, 0xa1, 0x65, 0xcd, 0x3d, 0xec, 0x89, 0x8b, 0xef, 0x01, 0x8c, 0xfd,
	0x0d, 0xe4, 0x10, 0xc6, 0xf6, 0x3d, 0x9c, 0xd9, 0xe8, 0xa7, 0x34, 0x36, 0xe5, 0x2d, 0x23, 0x47,
	0x00, 0x5d, 0x4c, 0x9c, 0xd9, 0xeb, 0xa6, 0x74, 0xea, 0x91, 0x5b, 0x66, 0xfc, 0x58, 0xdd, 0xf6,
	0x4d, 0x36, 0x9b, 0xce, 0xcf, 0x6b, 0x98, 0x4b, 0xfb, 0xd8, 0x9e, 0x14, 0x59, 0xd2, 0xcc, 0xa1,
	0x1d, 0xed, 0x08, 0x80, 0xab, 0xdc, 0x5b, 0xb4, 0x81, 0x4e, 0xe8, 0x94, 0xab, 0x3b, 0x07, 0x2c,
	0xbe, 0x05, 0x30, 0xf6, 0x53, 0x24, 0x17, 0x10, 0x9b, 0x71, 0xb7, 0xca, 0x7a, 0x9d, 0x77, 0x23,
	0xf3, 0xed, 0x7b, 0xdb, 0xa2, 0x9e, 0x42, 0x0e, 0x20, 0x56, 0x28, 0x18, 0x4a, 0x6f, 0xde, 0x57,
	0xe4, 0x15, 0x4c, 0x24, 0x96, 0xc8, 0x3f, 0xa3, 0xb4, 0xae, 0xa7, 0xb4, 0xaf, 0x8d, 0xa6, 0xd8,
	0xd4, 0xad, 0xd0, 0xd6, 0x47, 0x44, 0x7d, 0x65, 0x70, 0x2c, 0xa4, 0x40, 0x96, 0xc5, 0x76, 0x3f,
	0x7d, 0xb5, 0xf8, 0x19, 0xc0, 0x6c, 0x6b, 0x61, 0xc8, 0x05, 0x44, 0xfa, 0xb1, 0x41, 0x6f, 0xf0,
	0xf0, 0x85, 0x9d, 0xfa, 0xf0, 0xd8, 0x20, 0xb5, 0xa4, 0xe7, 0xe1, 0x0f, 0xff, 0x12, 0x7e, 0xf8,
	0xaf, 0xf0, 0xa3, 0xff, 0x09, 0x7f, 0xf4, 0x52, 0xf8, 0x29, 0x84, 0x2b, 0x44, 0xfb, 0xaa, 0x88,
	0x9a, 0xa3, 0x89, 0x87, 0xb5, 0xb2, 0xd0, 0xbc, 0x16, 0xd9, 0xd8, 0x3e, 0xb6, 0xaf, 0x17, 0x4b,
	0x80, 0xa7, 0x1d, 0xff, 0xf3, 0xea, 0x9c, 0xc0, 0x0e, 0x57, 0x79, 0x59, 0x0b, 0x81, 0xa5, 0x46,
	0xf7, 0xb6, 0x09, 0x4d, 0xb8, 0xba, 0xe9, 0xa0, 0xf3, 0x0d, 0xcc, 0xb6, 0xa6, 0x46, 0x76, 0x21,
	0x71, 0x73, 0xcb, 0x45, 0x5b, 0x55, 0xe9, 0x80, 0x24, 0x30, 0x56, 0x6d, 0x59, 0xa2, 0x52, 0x69,
	0x40, 0x0e, 0x80, 0xb4, 0x42, 0xb5, 0xab, 0x15, 0x2f, 0x39, 0x0a, 0x9d, 0xaf, 0x5a, 0xc1, 0x54,
	0x3a, 0x24, 0x7b, 0x30, 0xc3, 0x2f, 0x1a, 0xa5, 0x28, 0xaa, 0x7c, 0x55, 0xf0, 0x2a, 0x0d, 0xc9,
	0x3e, 0xec, 0x5a, 0x57, 0x55, 0x5d, 0x76, 0x60, 0x74, 0x2e, 0x61, 0xef, 0xb7, 0x19, 0x98, 0x2b,
	0xdd, 0xaf, 0xb8, 0xbb, 0x72, 0x07, 0x26, 0x75, 0x83, 0x42, 0x70, 0xb1, 0x4e, 0x03, 0x02, 0x10,
	0x9b, 0x0a, 0x59, 0x3a, 0x34, 0x66, 0xca, 0xaa, 0x56, 0xa6, 0x11, 0x9a, 0x86, 0x29, 0x90, 0xa5,
	0x91, 0x91, 0xb4, 0x0d, 0x2b, 0xb4, 0xe9, 0x8c, 0x0c, 0xcd, 0x56, 0xc8, 0xd2, 0xf8, 0x21, 0xb6,
	0x7f, 0x73, 0x57, 0xbf, 0x02, 0x00, 0x00, 0xff, 0xff, 0x01, 0xf5, 0x3e, 0x2f, 0xf3, 0x04, 0x00,
	0x00,
}
