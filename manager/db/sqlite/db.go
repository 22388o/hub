package sqlite

import (
	"github.com/jinzhu/gorm"
	"path/filepath"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
	"github.com/bitlum/hub/manager/router"
)

// DB is the primary datastore.
type DB struct {
	*gorm.DB
	dbPath string

	// nodeInfo is a information about hub, which is stored in-memory.
	nodeInfo *router.DbInfo
}

// Open opens an existing db. Any necessary schemas migrations due to
// updates will take place as necessary.
func Open(dbPath string, dbName string) (*DB, error) {
	path := filepath.Join(dbPath, dbName)

	gdb, err := gorm.Open("sqlite3", path)
	if err != nil {
		return nil, err
	}

	gdb.CreateTable(
		&Counters{},
		&Channel{},
		&Payment{},
		&Peer{})
	if gdb.Error != nil {
		return nil, err
	}

	db := &DB{
		DB:     gdb,
		dbPath: dbPath,
	}

	return db, nil
}
