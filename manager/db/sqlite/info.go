package sqlite

import (
	"github.com/bitlum/hub/manager/router"
)

// Runtime check to ensure that DB implements lnd.RouterStorage interface.
var _ router.InfoStorage = (*DB)(nil)

// UpdateInfo updates information about the hub lightning network node.
func (d *DB) UpdateInfo(info *router.Info) error {
	d.nodeInfo = info
	return nil
}

// Info returns hub lighting network node information.
func (d *DB) Info() (*router.Info, error) {
	return d.nodeInfo, nil
}
