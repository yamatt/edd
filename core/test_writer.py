import unittest
from writer import Writer
from device_manager import UnknownDevice
from os import urandom, remove as delete
from hashlib import sha512

class TestWriter(unittest.TestCase):
    source_file_path = "test.source.file"
    destination_file_path = "test.destination.file"
    def setUp(self):
        with open(source_file_path, 'wb') as source_file:
            source_file.write(urandom(1024))
        
    def tearDown(self):
        delete(source_file_path)
        
    def test_file_writing(self):
        """
        create source file
        create destination file
        fill the source file with data
        start the process
        test that hash of source file is same as hash of destination file
        """
        with open(self.source_file_path, 'rb') as source_file:
            with UnknownDevice(self.destination_file_path) as destination_device:
                w = Writer(source_file, destination_device)
                w.start()
        self.assertEqual(self.get_hash(self.source_file_path, self.destination_file_path)
        
    def test_permissions(self):
        """
        Create a source file
        create a destination file
        set source file's permissions to not readable
        set destination file's permissions to not writable
        open writer
        test for errors
        """
        pass
        
    def test_device_writing(self):
        """
        ask to specify device to write to
        if answer:
            create source file with data
            write to device
            test device has same data
        """
        device_path = raw_input("""
Specify the path to the device you would like to overwrite.
WARNING: This has a high change of destroying the data on the device.
WARNING: This will most likely require root permissions on Linux machines.
RECOMMEND: Doing this in a virtual machine will reduce the chance of catastrophic damage to your machine.

## To stop this test just enter an empty value. ##

EXAMPLE UNIX: /dev/sdc
EXAMPLE WINDOWS: \\.\PhysicalDrive3
EXAMPLE OSX: /dev/disk3
:""")
        if device_path:
            with UnknownDevice(device_path) as destination_device:
                with open(self.source_file_path, 'rb') as source_file:
                    w = Writer(source_file, destination_device)
                    w.start()
            self.assertEqual(self.get_hash(self.source_file_path, device_path)
            
    def get_hash(self, file_path):
        with open(file_path, 'rb') as f:
            hash_result = sha512(f.read()).digest()
        return hash_result
        

if __name__ == "__main__":
    unittest.main()
