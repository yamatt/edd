#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 This file is part of PROJECT NAME.

 PROJECT NAME is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 PROJECT NAME is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with PROJECT NAME.  If not, see <http://www.gnu.org/licenses/>.
"""

from core import Writer
from multiprocessing import Process, Value
from time import sleep, time as now
from argparse import ArgumentParser

class WriterProcess(object):
    output_format = "Progress: %(pc).1f%% at [%(bits_per_second)d] b/s"
    def __init__(self, source_path, destination_path, block_size, interval_delay=1):
        self.interval_delay = float(interval_delay)
        
        # used for getting process progress
        self.transfered = Value("d", 0.0)
        self.complete = Value("b", False)
        
        # attempt to open specified files
        try:
            source_file = open(source_path, 'rb')
            destination_file = open(destination_path, 'wb')
            self.writer = Writer(source_file, destination_file, block_size)
        except IOError as e:
            print "This process could not complete. %s" % e
        
    def _start_process(self):
        self.process = Process(target=self.writer.start_process, args=(self.transfered, self.complete))
        self.process.start()
        
    def process(self):
        self._start_process()
        last_size = self.total_downloaded
        time_started = now()
        while not self.complete.value:
            sleep(self.interval_delay)
            
            # collate stats
            data = dict()
            data['file_size'] = float(self.writer.file_size)
            data['downloaded'] = self.transfered.value
            data['diff'] = self.transfered.value - last_size
            data['bits_per_second'] = data['diff'] / self.interval_delay
            data['percent_complete'] =  (data['downloaded'] / data['file_size']) * 100
            data['time_taken'] = now() - time_started
            output_string = self.output_format % data
            print "\r", output_string # the \r resets to the first column
        
    def start(self):
        try:
            self.process()
            print "Complete."
        except KeyboardInterrupt:
            self.process.terminate()
            print "Aborted."
        finally:
            time_taken = now() - time_started
            bytes_per_second = self.transfered.value / time_taken
            print "%d bytes transfered in %.1f seconds. (%d bps)" % (self.transfered.value, time_taken, bytes_per_second)
            
def get_args():
    parser = ArgumentParser()
    parser.add_argument('-i', '--in', help='Specify source file')
    parser.add_argument('-o', '--out', help='Specify destination device')
    parser.add_argument('-b', '--blocksize', help='Specify how many bits of data to write in one go')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    wp = WriterProcess(args['i'], args['o'], args['b'])
    wp.start()