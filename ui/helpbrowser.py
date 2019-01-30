# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpbrowser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        helpWindow.setObjectName("helpWindow")
        helpWindow.resize(640, 480)
        helpWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(helpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.helpWebView = QtWebEngineWidgets.QWebView(self.centralwidget)
        self.helpWebView.setUrl(QtCore.QUrl("about:blank"))
        self.helpWebView.setObjectName("helpWebView")
        self.gridLayout.addWidget(self.helpWebView, 0, 0, 1, 1)
        helpWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(helpWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        helpWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClose = QtWidgets.QAction(helpWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon)
        self.actionClose.setObjectName("actionClose")
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(helpWindow)
        self.actionClose.triggered.connect(helpWindow.close)
        QtCore.QMetaObject.connectSlotsByName(helpWindow)

    def retranslateUi(self, helpWindow):
        _translate = QtCore.QCoreApplication.translate
        helpWindow.setWindowTitle(_translate("helpWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("helpWindow", "toolBar"))
        self.actionClose.setText(_translate("helpWindow", "Close"))
        self.actionClose.setToolTip(_translate("helpWindow", "Close"))

from PyQt5 import QtWebEngineWidgets
