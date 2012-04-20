from edd_main import Ui_main_window as edd_main
from edd_process import Ui_progress as edd_progress

class Edd_ui(object):
    def __init__(self, assign=True):
        if assign:
            self.assign()
        
    def assign(self):
        """
        Creates assignments for events and triggers
        """
        pass
        
    def start(self):
        """
        Create the window
        """
        pass 
