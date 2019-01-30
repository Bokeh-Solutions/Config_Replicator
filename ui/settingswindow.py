# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingswindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        path = os.path.dirname(os.path.abspath(__file__))
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(640, 475)
        SettingsWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.settingsTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.settingsTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.settingsTextEdit.setReadOnly(True)
        self.settingsTextEdit.setObjectName("settingsTextEdit")
        self.gridLayout.addWidget(self.settingsTextEdit, 0, 0, 1, 1)
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(SettingsWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea)
        self.toolBar.setObjectName("toolBar")
        SettingsWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionSettingsSave = QtWidgets.QAction(SettingsWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(path,"save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsSave.setIcon(icon)
        self.actionSettingsSave.setObjectName("actionSettingsSave")
        self.actionSettingsClose = QtWidgets.QAction(SettingsWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(path,"exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsClose.setIcon(icon1)
        self.actionSettingsClose.setObjectName("actionSettingsClose")
        self.actionSettingsEdit = QtWidgets.QAction(SettingsWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.join(path,"edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsEdit.setIcon(icon2)
        self.actionSettingsEdit.setObjectName("actionSettingsEdit")
        self.actionSettingsUndo = QtWidgets.QAction(SettingsWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.join(path,"undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsUndo.setIcon(icon3)
        self.actionSettingsUndo.setObjectName("actionSettingsUndo")
        self.actionSettingsRedo = QtWidgets.QAction(SettingsWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.path.join(path,"Redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsRedo.setIcon(icon4)
        self.actionSettingsRedo.setObjectName("actionSettingsRedo")
        self.toolBar.addAction(self.actionSettingsSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettingsEdit)
        self.toolBar.addAction(self.actionSettingsUndo)
        self.toolBar.addAction(self.actionSettingsRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettingsClose)

        self.retranslateUi(SettingsWindow)
        self.actionSettingsClose.triggered.connect(SettingsWindow.close)
        self.actionSettingsUndo.triggered.connect(self.settingsTextEdit.undo)
        self.actionSettingsRedo.triggered.connect(self.settingsTextEdit.redo)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.toolBar.setWindowTitle(_translate("SettingsWindow", "toolBar"))
        self.actionSettingsSave.setText(_translate("SettingsWindow", "Save"))
        self.actionSettingsSave.setToolTip(_translate("SettingsWindow", "Save"))
        self.actionSettingsClose.setText(_translate("SettingsWindow", "Close"))
        self.actionSettingsClose.setToolTip(_translate("SettingsWindow", "Close"))
        self.actionSettingsEdit.setText(_translate("SettingsWindow", "Edit"))
        self.actionSettingsEdit.setToolTip(_translate("SettingsWindow", "Edit"))
        self.actionSettingsUndo.setText(_translate("SettingsWindow", "Undo"))
        self.actionSettingsUndo.setToolTip(_translate("SettingsWindow", "Undo"))
        self.actionSettingsRedo.setText(_translate("SettingsWindow", "Redo"))
        self.actionSettingsRedo.setToolTip(_translate("SettingsWindow", "Redo"))

