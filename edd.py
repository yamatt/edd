#!/usr/bin/env python
import sys
from PyQt4 import QtCore, QtGui
from ui.edd_ui import EddMainWindow
 
class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = EddMainWindow()
        self.ui.setupUi(self)
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
