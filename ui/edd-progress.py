# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edd-progress.ui'
#
# Created: Tue Mar 27 20:30:42 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_progress(object):
    def setupUi(self, progress):
        progress.setObjectName(_fromUtf8("progress"))
        progress.resize(402, 120)
        progress.setWindowTitle(QtGui.QApplication.translate("progress", "Progress...", None, QtGui.QApplication.UnicodeUTF8))
        self.progress_label = QtGui.QLabel(progress)
        self.progress_label.setGeometry(QtCore.QRect(10, 10, 381, 21))
        self.progress_label.setText(QtGui.QApplication.translate("progress", "Progress:", None, QtGui.QApplication.UnicodeUTF8))
        self.progress_label.setObjectName(_fromUtf8("progress_label"))
        self.progress_bar = QtGui.QProgressBar(progress)
        self.progress_bar.setGeometry(QtCore.QRect(10, 40, 381, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progress_bar.setOrientation(QtCore.Qt.Horizontal)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.cancel = QtGui.QPushButton(progress)
        self.cancel.setGeometry(QtCore.QRect(300, 80, 95, 31))
        self.cancel.setText(QtGui.QApplication.translate("progress", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.ok = QtGui.QPushButton(progress)
        self.ok.setGeometry(QtCore.QRect(190, 80, 95, 31))
        self.ok.setText(QtGui.QApplication.translate("progress", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.ok.setObjectName(_fromUtf8("ok"))

        self.retranslateUi(progress)
        QtCore.QMetaObject.connectSlotsByName(progress)

    def retranslateUi(self, progress):
        pass

