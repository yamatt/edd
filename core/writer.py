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

from os import fstat
from time import time as now

class Writer(object):
    def __init__(self, source_file, destination_device, block_size=1024):
        self._source_file = source_file
        self._destination_device = destination_device
        self.__block_size = block_size
        
        self.file_size = os.fstat(self.__source_file.fileno()).st_size
        self.current_transfered = 0
        self.complete = False
        
    def get_errors(self):
        errors = []
        if not hasattr(self._source_file, 'read'):
            errors.append("Source file does not have a read attribute.")
        if not hasattr(self._destination_device, 'write'):
            errors.append("Destination device does not have a write attribute.")
        return errors
        
    def has_errors(self):
        return bool(self.get_errors())
        
    def start(self):
        while True:
            buff = self._source_file.read(self.__block_size)
            if not buff:
                break
            self._destination_device.write(buff)
            buffer_length = len(buff)
            self.total_downloaded += buffer_length
        self.complete = True

    def start_process(self, transfered, complete):
        """
        Duplicate of start. Wondering if there is a better way.
        """
        while True:
            buff = self._source_file.read(self.__block_size)
            if not buff:
                break
            self._destination_device.write(buff)
            buffer_length = len(buff)
            transfered.value += buffer_length
        complete.value = True
