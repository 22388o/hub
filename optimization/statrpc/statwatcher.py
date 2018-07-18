from watchdog.events import PatternMatchingEventHandler as PattMatchEvHand
from threading import Thread
import time
import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from watcher.protologutills import split_path_name
from samples.smartlog import SmartLog
from watcher.logreader import LogReader
from statrpc.statserver import stat_serve
from statrpc.statparams import StatParams


class StatServerThread(Thread):
    def __init__(self, stat_params, setts):
        Thread.__init__(self)
        self.stat_params = stat_params
        self.setts = setts

    def run(self):
        stat_serve(self.stat_params, self.setts)


class WatcherStat(PattMatchEvHand):

    def __init__(self, setts, log_file_name):
        super().__init__(
            patterns='*' + split_path_name(log_file_name)['name'],
            ignore_directories=True, case_sensitive=False)
        self.setts = setts
        self.velocity_period = self.setts.velocity_period
        self.velocity_period /= self.setts.acceleration
        self.smart_log = SmartLog()
        self.log_reader = LogReader(log_file_name, self.smart_log, setts)
        self.time_stat_start = time.time()
        self.stat_params = StatParams(self.smart_log, self.setts)
        self.stat_server_thread = StatServerThread(self.stat_params, setts)
        self.stat_server_thread.start()

    def process(self, event):
        if (event.event_type == 'modified') and (
                event.src_path == self.log_reader.file_name):
            self.log_reader.process_log()

            delta_time = time.time() - self.time_stat_start
            if delta_time >= self.velocity_period:
                self.time_stat_start = time.time()
                self.stat_params.process()

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def on_moved(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)
