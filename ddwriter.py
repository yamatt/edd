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
from multiprocessing import Process
from time import sleep
from argparse import ArgumentParser

class WriterProcess(Writer):
    output_format = "Progress: %(pc)s%% at [%(kbps)d]kbps"
    def __init__(self, source_path, destination_path, block_size, interval_delay=1):
        self.interval_delay = float(interval_delay)
        try:
            source_file = open(source_path, 'rb')
            destination_file = open(destination_path, 'wb')
        except IOError as e:
            print "This process could not complete. %s" % e
        super(WriterProcess, self).__init__(source_file, destination_file, block_size)
        
    def _start_process(self):
        self.__process = Process(target=self.start)
        self.__process.start()
        
    def process(self):
        self._start_process()
        last_size = self.total_downloaded
        while not self.complete:
            sleep(self.interval_delay)
            # collate data
            data = dict()
            data['file_size'] = float(self.file_size)
            data['downloaded'] = float(self.total_downloaded)
            data['diff'] = self.total_downloaded - last_size
            data['diff_kbytes'] = data['diff'] * (8 * 1024)
            data['bits_per_delay'] = data['diff'] / self.interval_delay
            data['kbytes_per_delay'] = data['diff_kbytes'] / self.interval_delay
            data['percent_complete'] =  (data['downloaded'] / data['file_size']) * 100
            output_string = self.output_format % data
            print output_string, "\r" # the \r is used so the next line is written on the same line
        print "\nComplete."
        
    def start(self):
        try:
            self.process()
        except KeyboardInterrupt:
            if self.__process.is_alive():
                self.__process.terminate()
            print "Forced exit."
            
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
