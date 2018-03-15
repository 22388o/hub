package main

import (
	"io"
	"github.com/bitlum/hub/manager/logger"
	"time"
	"github.com/bitlum/hub/manager/router"
	"github.com/go-errors/errors"
)

// getState...
func getState(r router.Router) (*logger.Log, error) {
	// Get the router local network in order to write it on log file,
	// so that external optimisation program could sync it state.
	routerChannels, err := r.Network()
	if err != nil {
		return nil, err
	}

	// TODO(andrew.shvv) As far we have gap between those two operations
	// the free balance might actually change, need to cope with that.

	// Get the number of money under control of router in order to write
	// in the log.
	freeBalance, err := r.FreeBalance()
	if err != nil {
		return nil, err
	}

	channels := make([]*logger.Channel, len(routerChannels))
	for i, c := range routerChannels {
		channels[i] = &logger.Channel{
			ChannelId:     uint64(c.ChannelID),
			UserId:        uint64(c.UserID),
			UserBalance:   uint64(c.UserBalance),
			RouterBalance: uint64(c.RouterBalance),
		}
	}

	return &logger.Log{
		Time: time.Now().UnixNano(),
		Data: &logger.Log_State{
			State: &logger.RouterState{
				FreeBalance: uint64(freeBalance),
				Channels:    channels,
			},
		},
	}, nil
}

// updateLogFile subscribe on routers topology update and update the log with
// the current router state and channel updates.
//
// NOTE: Should be run as goroutine.
func updateLogFileGoroutine(r router.Router, w io.Writer, errChan chan error) {
	mainLog.Info("Write initial log state of the router in log file")

	var logEntry *logger.Log

	logEntry, err := getState(r)
	if err != nil {
		fail(errChan, "unable to get state: %v", err)
		return
	}

	for {
		if err := logger.WriteLog(w, logEntry); err != nil {
			fail(errChan, "unable to write new log entry: %v", err)
			return
		}

		select {
		case update, ok := <-r.ReceiveUpdates():
			if ok {
				mainLog.Info("Router update channel close, " +
					"exiting log update goroutine")
				return
			}

			switch u := update.(type) {
			case *router.UpdateChannelClosed:
				logEntry = &logger.Log{
					Time: time.Now().UnixNano(),
					Data: &logger.Log_ChannelChange{
						ChannelChange: &logger.ChannelChange{
							Type:          logger.ChannelChangeType_close,
							ChannelId:     uint64(u.ChannelID),
							UserId:        uint64(u.UserID),
							UserBalance:   0,
							RouterBalance: 0,
							Fee:           uint64(u.Fee),
						},
					},
				}
			case *router.UpdateChannelOpened:
				logEntry = &logger.Log{
					Time: time.Now().UnixNano(),
					Data: &logger.Log_ChannelChange{
						ChannelChange: &logger.ChannelChange{
							Type:          logger.ChannelChangeType_open,
							ChannelId:     uint64(u.ChannelID),
							UserId:        uint64(u.UserID),
							UserBalance:   uint64(u.UserBalance),
							RouterBalance: uint64(u.RouterBalance),
							Fee:           uint64(u.Fee),
						},
					},
				}
			case *router.UpdateChannelUpdated:
				logEntry = &logger.Log{
					Time: time.Now().UnixNano(),
					Data: &logger.Log_ChannelChange{
						ChannelChange: &logger.ChannelChange{
							Type:          logger.ChannelChangeType_udpate,
							ChannelId:     uint64(u.ChannelID),
							UserId:        uint64(u.UserID),
							UserBalance:   uint64(u.UserBalance),
							RouterBalance: uint64(u.RouterBalance),
							Fee:           uint64(u.Fee),
						},
					},
				}
			case *router.UpdatePayment:
				var status logger.PaymentStatus
				switch u.Status {
				case router.InsufficientFunds:
					status = logger.PaymentStatus_unsufficient_funds
				case router.Successful:
					status = logger.PaymentStatus_success
				case router.ExternalFail:
					status = logger.PaymentStatus_external_fail
				default:
					fail(errChan, "unknown status: %v", u.Status)
					return
				}

				logEntry = &logger.Log{
					Time: time.Now().UnixNano(),
					Data: &logger.Log_Payment{
						Payment: &logger.Payment{
							Status:   status,
							Sender:   u.Sender,
							Receiver: u.Receiver,
							Amount:   u.Amount,
							Earned:   u.Earned,
						},
					},
				}
			}

		case <-time.After(10 * time.Second):
			mainLog.Info("Synchronise state of the router and write state in the log")

			logEntry, err = getState(r)
			if err != nil {
				fail(errChan, "unable to get state: %v", err)
				return
			}
		}
	}
}

func fail(errChan chan error, format string, params ...interface{}) {
	err := errors.Errorf(format, params...)
	errChan <- err
}