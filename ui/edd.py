# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edd.ui'
#
# Created: Tue Mar 27 20:30:50 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(418, 180)
        main_window.setWindowTitle(QtGui.QApplication.translate("main_window", "Edd", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.device_label = QtGui.QLabel(self.centralwidget)
        self.device_label.setGeometry(QtCore.QRect(10, 10, 401, 21))
        self.device_label.setText(QtGui.QApplication.translate("main_window", "Select the device you would like to write to:", None, QtGui.QApplication.UnicodeUTF8))
        self.device_label.setObjectName(_fromUtf8("device_label"))
        self.device = QtGui.QComboBox(self.centralwidget)
        self.device.setGeometry(QtCore.QRect(10, 30, 351, 31))
        self.device.setObjectName(_fromUtf8("device"))
        self.reload = QtGui.QPushButton(self.centralwidget)
        self.reload.setGeometry(QtCore.QRect(370, 30, 31, 31))
        self.reload.setAccessibleName(QtGui.QApplication.translate("main_window", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.reload.setAccessibleDescription(_fromUtf8(""))
        self.reload.setText(_fromUtf8(""))
        self.reload.setObjectName(_fromUtf8("reload"))
        self.file_path_label = QtGui.QLabel(self.centralwidget)
        self.file_path_label.setGeometry(QtCore.QRect(10, 70, 391, 21))
        self.file_path_label.setText(QtGui.QApplication.translate("main_window", "Select the file you want to write to the device:", None, QtGui.QApplication.UnicodeUTF8))
        self.file_path_label.setObjectName(_fromUtf8("file_path_label"))
        self.file_path = QtGui.QLineEdit(self.centralwidget)
        self.file_path.setGeometry(QtCore.QRect(10, 90, 291, 31))
        self.file_path.setObjectName(_fromUtf8("file_path"))
        self.browse = QtGui.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(310, 90, 95, 31))
        self.browse.setText(QtGui.QApplication.translate("main_window", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.close = QtGui.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(310, 140, 95, 31))
        self.close.setText(QtGui.QApplication.translate("main_window", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setObjectName(_fromUtf8("close"))
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(200, 140, 95, 31))
        self.start.setText(QtGui.QApplication.translate("main_window", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.start.setObjectName(_fromUtf8("start"))
        main_window.setCentralWidget(self.centralwidget)
        self.device_label.setBuddy(self.device)
        self.file_path_label.setBuddy(self.file_path)

        self.retranslateUi(main_window)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL(_fromUtf8("clicked()")), main_window.close)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.setTabOrder(self.device, self.reload)
        main_window.setTabOrder(self.reload, self.file_path)
        main_window.setTabOrder(self.file_path, self.browse)
        main_window.setTabOrder(self.browse, self.start)
        main_window.setTabOrder(self.start, self.close)

    def retranslateUi(self, main_window):
        pass

