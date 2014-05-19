# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/users/mercolino/PycharmProjects/Config_Replicator/ui/credentials.ui'
#
# Created: Tue May 13 17:30:46 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(428, 152)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(428, 152))
        Dialog.setMaximumSize(QtCore.QSize(428, 152))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 110, 411, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 421, 16))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 291, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.usernameLabel = QtGui.QLabel(self.layoutWidget)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)
        self.usernameLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.usernameLineEdit.setObjectName(_fromUtf8("usernameLineEdit"))
        self.gridLayout.addWidget(self.usernameLineEdit, 0, 1, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.layoutWidget)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)
        self.passwordLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.passwordLineEdit.setInputMask(_fromUtf8(""))
        self.passwordLineEdit.setText(_fromUtf8(""))
        self.passwordLineEdit.setMaxLength(32767)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)
        self.usernameLabel.setBuddy(self.usernameLineEdit)
        self.passwordLabel.setBuddy(self.passwordLineEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        Dialog.setTabOrder(self.passwordLineEdit, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Credentials", None))
        self.label.setText(_translate("Dialog", "Please enter the username and password to login to the devices.", None))
        self.usernameLabel.setText(_translate("Dialog", "&Username:", None))
        self.passwordLabel.setText(_translate("Dialog", "&Password:", None))

