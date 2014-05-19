# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/users/mercolino/PycharmProjects/Config_Replicator/ui/settingswindow.ui'
#
# Created: Tue May 13 12:31:01 2014
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

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName(_fromUtf8("SettingsWindow"))
        SettingsWindow.resize(640, 475)
        SettingsWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(SettingsWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.settingsTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.settingsTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.settingsTextEdit.setReadOnly(True)
        self.settingsTextEdit.setObjectName(_fromUtf8("settingsTextEdit"))
        self.gridLayout.addWidget(self.settingsTextEdit, 0, 0, 1, 1)
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SettingsWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(SettingsWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        SettingsWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionSettingsSave = QtGui.QAction(SettingsWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ui/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsSave.setIcon(icon)
        self.actionSettingsSave.setObjectName(_fromUtf8("actionSettingsSave"))
        self.actionSettingsClose = QtGui.QAction(SettingsWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("ui/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsClose.setIcon(icon1)
        self.actionSettingsClose.setObjectName(_fromUtf8("actionSettingsClose"))
        self.actionSettingsEdit = QtGui.QAction(SettingsWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("ui/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsEdit.setIcon(icon2)
        self.actionSettingsEdit.setObjectName(_fromUtf8("actionSettingsEdit"))
        self.actionSettingsUndo = QtGui.QAction(SettingsWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("ui/undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsUndo.setIcon(icon3)
        self.actionSettingsUndo.setObjectName(_fromUtf8("actionSettingsUndo"))
        self.actionSettingsRedo = QtGui.QAction(SettingsWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("ui/Redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsRedo.setIcon(icon4)
        self.actionSettingsRedo.setObjectName(_fromUtf8("actionSettingsRedo"))
        self.toolBar.addAction(self.actionSettingsSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettingsEdit)
        self.toolBar.addAction(self.actionSettingsUndo)
        self.toolBar.addAction(self.actionSettingsRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettingsClose)

        self.retranslateUi(SettingsWindow)
        QtCore.QObject.connect(self.actionSettingsClose, QtCore.SIGNAL(_fromUtf8("triggered()")), SettingsWindow.close)
        QtCore.QObject.connect(self.actionSettingsUndo, QtCore.SIGNAL(_fromUtf8("triggered()")), self.settingsTextEdit.undo)
        QtCore.QObject.connect(self.actionSettingsRedo, QtCore.SIGNAL(_fromUtf8("triggered()")), self.settingsTextEdit.redo)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings", None))
        self.toolBar.setWindowTitle(_translate("SettingsWindow", "toolBar", None))
        self.actionSettingsSave.setText(_translate("SettingsWindow", "Save", None))
        self.actionSettingsSave.setToolTip(_translate("SettingsWindow", "Save", None))
        self.actionSettingsClose.setText(_translate("SettingsWindow", "Close", None))
        self.actionSettingsClose.setToolTip(_translate("SettingsWindow", "Close", None))
        self.actionSettingsEdit.setText(_translate("SettingsWindow", "Edit", None))
        self.actionSettingsEdit.setToolTip(_translate("SettingsWindow", "Edit", None))
        self.actionSettingsUndo.setText(_translate("SettingsWindow", "Undo", None))
        self.actionSettingsUndo.setToolTip(_translate("SettingsWindow", "Undo", None))
        self.actionSettingsRedo.setText(_translate("SettingsWindow", "Redo", None))
        self.actionSettingsRedo.setToolTip(_translate("SettingsWindow", "Redo", None))

