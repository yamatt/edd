from edd_main import Ui_main_window
from edd_process import Ui_progress

"""
The purpose of this module is to add the events and triggers to the basic ui template.
Looks like there will need to be something done about the translations too.
"""

class EddMainWindow(Ui_main_window):
    def setupUi(self, main_window):
        super(EddMainWindow, self).setupUi(main_window)
        # add event triggers
    
class EddProgressWindow(Ui_progress):
    def setupUi(self, main_window):
        super(EddMainWindow, self).setupUi(main_window)
        # add event triggers
