# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/users/mercolino/PycharmProjects/Config_Replicator/ui/enable.ui'
#
# Created: Tue May 13 17:30:26 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_enableDialog(object):
    def setupUi(self, enableDialog):
        enableDialog.setObjectName(_fromUtf8("enableDialog"))
        enableDialog.resize(270, 104)
        enableDialog.setMinimumSize(QtCore.QSize(270, 104))
        enableDialog.setMaximumSize(QtCore.QSize(270, 104))
        self.enableButtonBox = QtGui.QDialogButtonBox(enableDialog)
        self.enableButtonBox.setGeometry(QtCore.QRect(10, 70, 251, 32))
        self.enableButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.enableButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.enableButtonBox.setObjectName(_fromUtf8("enableButtonBox"))
        self.label = QtGui.QLabel(enableDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(enableDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 62, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.enableLineEdit = QtGui.QLineEdit(enableDialog)
        self.enableLineEdit.setGeometry(QtCore.QRect(70, 40, 191, 21))
        self.enableLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.enableLineEdit.setObjectName(_fromUtf8("enableLineEdit"))
        self.label_2.setBuddy(self.enableLineEdit)

        self.retranslateUi(enableDialog)
        QtCore.QObject.connect(self.enableButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), enableDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(enableDialog)

    def retranslateUi(self, enableDialog):
        enableDialog.setWindowTitle(_translate("enableDialog", "Dialog", None))
        self.label.setText(_translate("enableDialog", "Enter your Enable Password:", None))
        self.label_2.setText(_translate("enableDialog", "&Enable:", None))

