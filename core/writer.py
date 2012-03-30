#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 This file is part of Edd.

 Edd is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 Edd is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with Edd.  If not, see <http://www.gnu.org/licenses/>.
"""

from os import fstat
from time import time as now

class Writer(object):
    def __init__(self, source_file, destination_device, block_size=1024):
        """
        Initialise the writer object that can transfer to the device.
        @param source_file:a file object representing the resource to be read from.
        @param destination_device:a file obect representing the resource to be written to
        @param block_size:the number of bytes to be written in one go. The smaller the number the greater the CPU used, the higher the number the less accurate the stats are.
        """
        self._source_file = source_file
        self._destination_device = destination_device
        self.__block_size = block_size
        
        self.file_size = os.fstat(self.__source_file.fileno()).st_size
        
        self.transfered = 0
        self.complete = False
        
    def get_errors(self):
        """
        Performs some simple validation to determine if the process will complete.
        Need more tests.
        """
        errors = []
        if self._destination_device.mode is not "wb":
            errors.append("Cannot write to the destination device. The mode must be 'wb'.")
        if self._source_file.mode is not "rb":
            errors.append("Cannot read from the source file. The mode must be 'rb'.")
        return errors
        
    def has_errors(self):
        """
        A simpler boolean result based upon the results of self.get_errors.
        """
        return bool(self.get_errors())

    def start(self, transfered=None, complete=None):
        """
        Reads data from the source file object and writes it to the destination file object.
        @param transfered:a Value object (from multiprocessing) that will be used to pass back how much data has been read and written from the source and destination file objects.
        @param complete:a Value object (from multiprocessing) that is used to pass back if the transfer has finished.
        """
        while True:
            buff = self._source_file.read(self.__block_size)
            if not buff:
                break
            self._destination_device.write(buff)
            buffer_length = len(buff)
            if transfered:
                transfered.value += buffer_length
            self.transfered += buffer_length
        if complete:
            complete.value = True
        self.complete = True
