package lnd

import (
	"time"
	"github.com/lightningnetwork/lnd/lnrpc"
	"sync"
	"github.com/go-errors/errors"
	"google.golang.org/grpc"
	"sync/atomic"
	"google.golang.org/grpc/credentials"
	"strconv"
	"net"
	"context"
	"strings"
	"github.com/bitlum/hub/manager/metrics/crypto"
	"github.com/bitlum/hub/manager/metrics"
	"github.com/bitlum/hub/manager/router"
)

// Config is a connector config.
type Config struct {
	// Asset name of the asset with which operates the router.
	Asset string

	// Port is gRPC port of lnd daemon.
	Port string

	// Host is gRPC host of lnd daemon.
	Host string

	// TlsCertPath is a path to certificate, which is needed to have a secure
	// gRPC connection with lnd daemon.
	TlsCertPath string

	// DB is used to store all data which needs to be persistent,
	// exact implementation of database backend is unknown for the hub,
	// in the simplest case it might be in-memory storage.
	DB DB

	// MetricsBackend...
	MetricsBackend crypto.MetricsBackend
}

func (c *Config) validate() error {
	if c.Asset == "" {
		return errors.Errorf("asset should be specified")
	}

	if c.Port == "" {
		return errors.Errorf("port should be specified")
	}

	if c.Host == "" {
		return errors.Errorf("host should be specified")
	}

	if c.TlsCertPath == "" {
		return errors.Errorf("tlc cert path should be specified")
	}

	if c.DB == nil {
		return errors.Errorf("db should be specified")
	}

	if c.MetricsBackend == nil {
		return errors.Errorf("metrics backend should be specified")
	}

	return nil
}

// Router is the lightning network daemon gRPC client wrapper which makes it
// compatible with our internal router interface.
type Router struct {
	started  int32
	shutdown int32
	wg       sync.WaitGroup
	quit     chan struct{}

	client lnrpc.LightningClient
	conn   *grpc.ClientConn

	cfg      *Config
	nodeAddr string

	// broadcaster is used to broadcast router updates in the non-blocking
	// manner. If one of receiver would not read te update write wouldn't stuck.
	broadcaster router.Broadcaster
}

// Runtime check to ensure that Connector implements common.LightningConnector
// interface.
var _ router.Router = (*Router)(nil)

func NewRouter(cfg *Config) (*Router, error) {
	if err := cfg.validate(); err != nil {
		return nil, errors.Errorf("config is invalid: %v", err)
	}

	return &Router{
		cfg:         cfg,
		quit:        make(chan struct{}),
		broadcaster: router.NewBroadcaster(),
	}, nil
}

// Start...
func (r *Router) Start() error {
	if !atomic.CompareAndSwapInt32(&r.started, 0, 1) {
		log.Warn("Lnd router already started")
		return nil
	}

	m := crypto.NewMetric(r.cfg.Asset, "Start",
		r.cfg.MetricsBackend)
	defer m.Finish()

	creds, err := credentials.NewClientTLSFromFile(r.cfg.TlsCertPath, "")
	if err != nil {
		m.AddError(metrics.HighSeverity)
		return errors.Errorf("unable to load credentials: %v", err)
	}

	opts := []grpc.DialOption{
		grpc.WithTransportCredentials(creds),
	}

	target := net.JoinHostPort(r.cfg.Host, r.cfg.Port)
	log.Infof("Lightning client connects to lnd: %v", target)

	conn, err := grpc.Dial(target, opts...)
	if err != nil {
		m.AddError(metrics.HighSeverity)
		return errors.Errorf("unable to to dial grpc: %v", err)
	}
	r.conn = conn
	r.client = lnrpc.NewLightningClient(r.conn)

	reqInfo := &lnrpc.GetInfoRequest{}
	respInfo, err := r.client.GetInfo(context.Background(), reqInfo)
	if err != nil {
		m.AddError(metrics.HighSeverity)
		return errors.Errorf("unable get lnd node info: %v", err)
	}

	log.Infof("Init lnd router with pub key: %v", respInfo.IdentityPubkey)
	r.nodeAddr = respInfo.IdentityPubkey

	r.listenLocalTopologyUpdates()
	r.listenForwardingUpdates()
	r.listenInvoiceUpdates()

	log.Info("Lnd router started")
	return nil
}

// Stop gracefully stops the connection with lnd daemon.
func (r *Router) Stop(reason string) error {
	if !atomic.CompareAndSwapInt32(&r.shutdown, 0, 1) {
		log.Warn("lnd router already shutdown")
		return nil
	}

	close(r.quit)
	if err := r.conn.Close(); err != nil {
		return errors.Errorf("unable to close connection to lnd: %v", err)
	}

	r.wg.Wait()

	log.Infof("lnd router shutdown, reason(%v)", reason)
	return nil
}

// SendPayment makes the payment on behalf of router. In the context of
// lightning network hub manager this hook might be used for future
// off-chain channel re-balancing tactics.
//
// NOTE: Part of the router.Router interface.
func (r *Router) SendPayment(userID router.UserID, amount router.BalanceUnit) error {
	// TODO(andrew.shvv) Add implementation when rebalancing strategy will be
	// needed.
	return nil
}

// OpenChannel opens the channel with the given user.
//
// NOTE: Part of the router.Router interface.
func (r *Router) OpenChannel(id router.UserID, funds router.BalanceUnit) error {
	m := crypto.NewMetric(r.cfg.Asset, "OpenChannel",
		r.cfg.MetricsBackend)
	defer m.Finish()

	req := &lnrpc.OpenChannelRequest{
		NodePubkeyString:   string(id),
		LocalFundingAmount: int64(funds),

		// TODO(andrew.shvv) We have to make a subsystem for optimising this
		// ration.
		SatPerByte: 0,

		// TODO(andrew.shvv) Should we make is equal to minimum exchange amount?
		MinHtlcMsat: 0,

		// TODO(andrew.shvv) Does the Jack wallet supports private channels?
		Private: false,
	}

	_, err := r.client.OpenChannelSync(context.Background(), req)
	if err != nil {
		return err
	}

	return nil
}

// CloseChannel closes the specified channel.
//
// NOTE: Part of the router.Router interface.
func (r *Router) CloseChannel(id router.ChannelID) error {
	m := crypto.NewMetric(r.cfg.Asset, "CloseChannel",
		r.cfg.MetricsBackend)
	defer m.Finish()

	parts := strings.Split(string(id), ":")
	if len(parts) != 2 {
		m.AddError(metrics.HighSeverity)
		log.Error("unable to split chan point("+
			"%v) on funding tx id and output index", id)
		return errors.New("unable decode channel point")
	}

	index, err := strconv.ParseUint(parts[1], 10, 32)
	if err != nil {
		m.AddError(metrics.HighSeverity)
		log.Error("unable to parse index", parts[1])
		return errors.Errorf("unable decode tx index: %v", err)
	}

	fundingTx := &lnrpc.ChannelPoint_FundingTxidStr{
		FundingTxidStr: parts[0],
	}

	req := &lnrpc.CloseChannelRequest{
		ChannelPoint: &lnrpc.ChannelPoint{
			FundingTxid: fundingTx,
			OutputIndex: uint32(index),
		},
		Force: false,
	}

	if _, err = r.client.CloseChannel(context.Background(), req); err != nil {
		m.AddError(metrics.HighSeverity)
		log.Errorf("unable close the channel: %v", err)
		return err
	}

	return nil
}

// UpdateChannel updates the number of locked funds in the specified
// channel.
//
// NOTE: Part of the router.Router interface.
func (r *Router) UpdateChannel(id router.ChannelID,
	funds router.BalanceUnit) error {

	// TODO(andrew.shvv) Implement
	// This hook would require splice-out splice-in mechanism to be
	// implemented in lnd.

	return nil
}

// SetFee updates the fee which router takes for routing the users
// payments.
//
// NOTE: Part of the router.Router interface.
func (r *Router) SetFee(fee uint64) error {
	// TODO(andrew.shvv) Implement
	return nil
}

// RegisterOnUpdates returns updates about router local network topology
// changes, about attempts of propagating the payment through the
// router, about fee changes etc.
//
// NOTE: Part of the router.Router interface.
func (r *Router) RegisterOnUpdates() *router.Receiver {
	return r.broadcaster.Listen()
}

// Network returns the information about the current local network router
// topology.
//
// NOTE: Part of the router.Router interface.
func (r *Router) Network() ([]*router.Channel, error) {
	m := crypto.NewMetric(r.cfg.Asset, "Network", r.cfg.MetricsBackend)
	defer m.Finish()

	var channels []*router.Channel

	{
		req := &lnrpc.PendingChannelsRequest{}
		resp, err := r.client.PendingChannels(context.Background(), req)
		if err != nil {
			m.AddError(metrics.HighSeverity)
			log.Errorf("unable to fetch pending channels: %v", err)
			return nil, err
		}

		for _, entry := range resp.PendingOpenChannels {
			channels = append(channels, &router.Channel{
				ChannelID:     router.ChannelID(entry.Channel.ChannelPoint),
				UserID:        router.UserID(entry.Channel.RemoteNodePub),
				UserBalance:   router.BalanceUnit(entry.Channel.RemoteBalance),
				RouterBalance: router.BalanceUnit(entry.Channel.LocalBalance),
				IsPending:     true,
			})
		}

		for _, entry := range resp.PendingForceClosingChannels {
			channels = append(channels, &router.Channel{
				ChannelID:     router.ChannelID(entry.Channel.ChannelPoint),
				UserID:        router.UserID(entry.Channel.RemoteNodePub),
				UserBalance:   router.BalanceUnit(entry.Channel.RemoteBalance),
				RouterBalance: router.BalanceUnit(entry.Channel.LocalBalance),
				IsPending:     true,
			})
		}

		for _, entry := range resp.PendingClosingChannels {
			channels = append(channels, &router.Channel{
				ChannelID:     router.ChannelID(entry.Channel.ChannelPoint),
				UserID:        router.UserID(entry.Channel.RemoteNodePub),
				UserBalance:   router.BalanceUnit(entry.Channel.RemoteBalance),
				RouterBalance: router.BalanceUnit(entry.Channel.LocalBalance),
				IsPending:     true,
			})
		}
	}

	{
		req := &lnrpc.ListChannelsRequest{}
		resp, err := r.client.ListChannels(context.Background(), req)
		if err != nil {
			m.AddError(metrics.HighSeverity)
			log.Errorf("unable to fetch open channels: %v", err)
			return nil, err
		}

		for _, c := range resp.Channels {
			channels = append(channels, &router.Channel{
				ChannelID:     router.ChannelID(c.ChannelPoint),
				UserID:        router.UserID(c.RemotePubkey),
				UserBalance:   router.BalanceUnit(c.RemoteBalance),
				RouterBalance: router.BalanceUnit(c.LocalBalance),
				IsPending:     false,
				IsActive:      c.Active,
			})
		}
	}

	return channels, nil
}

// FreeBalance returns the amount of funds at router disposal.
//
// NOTE: Part of the router.Router interface.
func (r *Router) FreeBalance() (router.BalanceUnit, error) {
	m := crypto.NewMetric(r.cfg.Asset, "FreeBalance", r.cfg.MetricsBackend)
	defer m.Finish()

	req := &lnrpc.WalletBalanceRequest{}
	resp, err := r.client.WalletBalance(context.Background(), req)
	if err != nil {
		m.AddError(metrics.HighSeverity)
		log.Errorf("unable to get wallet balance channels: %v", err)
		return 0, err
	}

	return router.BalanceUnit(resp.ConfirmedBalance), nil
}

// PendingBalance returns the amount of funds which in the process of
// being accepted by blockchain.
//
// NOTE: Part of the router.Router interface.
func (r *Router) PendingBalance() (router.BalanceUnit, error) {
	m := crypto.NewMetric(r.cfg.Asset, "PendingBalance", r.cfg.MetricsBackend)
	defer m.Finish()

	req := &lnrpc.PendingChannelsRequest{}
	resp, err := r.client.PendingChannels(context.Background(), req)
	if err != nil {
		m.AddError(metrics.HighSeverity)
		log.Errorf("unable to fetch pending channels: %v", err)
		return 0, err
	}

	return router.BalanceUnit(resp.TotalLimboBalance), nil
}

// AverageChangeUpdateDuration average time which is needed the change of
// state to ba updated over blockchain.
//
// NOTE: Part of the router.Router interface.
func (r *Router) AverageChangeUpdateDuration() (time.Duration, error) {

	// TODO(andrew.shvv) Implement
	// This hook would require us to make some channel update registry,
	// probably this would require to write data in some persistent storage.

	return 0, nil
}

// Done returns error if router stopped working for some reason,
// and nil if it was stopped.
//
// NOTE: Part of the router.Router interface.
func (r *Router) Done() chan error {
	// TODO(andrew.shvv) Implement
	return nil
}

// Asset returns asset with which corresponds to this router.
//
// NOTE: Part of the router.Router interface.
func (r *Router) Asset() string {
	return r.cfg.Asset
}