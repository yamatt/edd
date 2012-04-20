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

from stat import S_ISBLK as is_block_device

class UnixDeviceList(object):
    def __init__(self, find=True):
        self.__devices = []
        if find:
            self.find_devices()
        
    def find_devices(self):
        pass
        
    def get_devices(self):
        pass

class UnixDevice(file):
    def __init__(self, device_path, mode="wb"):
        if is_block_device(device_path):
            file.__init__(self, device_path, mode)
        else:
            raise IOError("The device path is not a block device.")

class UnknownDevice(file):
    def __init__(self, device_path, mode="wb"):
        file.__init__(self, device_path, mode)

if __name__ == "__main__":
    pass
