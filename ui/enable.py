# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_enableDialog(object):
    def setupUi(self, enableDialog):
        enableDialog.setObjectName("enableDialog")
        enableDialog.resize(270, 104)
        enableDialog.setMinimumSize(QtCore.QSize(270, 104))
        enableDialog.setMaximumSize(QtCore.QSize(270, 104))
        self.enableButtonBox = QtWidgets.QDialogButtonBox(enableDialog)
        self.enableButtonBox.setGeometry(QtCore.QRect(10, 70, 251, 32))
        self.enableButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.enableButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.enableButtonBox.setObjectName("enableButtonBox")
        self.label = QtWidgets.QLabel(enableDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(enableDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 62, 16))
        self.label_2.setObjectName("label_2")
        self.enableLineEdit = QtWidgets.QLineEdit(enableDialog)
        self.enableLineEdit.setGeometry(QtCore.QRect(70, 40, 191, 21))
        self.enableLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enableLineEdit.setObjectName("enableLineEdit")
        self.label_2.setBuddy(self.enableLineEdit)

        self.retranslateUi(enableDialog)
        self.enableButtonBox.accepted.connect(enableDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(enableDialog)

    def retranslateUi(self, enableDialog):
        _translate = QtCore.QCoreApplication.translate
        enableDialog.setWindowTitle(_translate("enableDialog", "Dialog"))
        self.label.setText(_translate("enableDialog", "Enter your Enable Password:"))
        self.label_2.setText(_translate("enableDialog", "&Enable:"))

