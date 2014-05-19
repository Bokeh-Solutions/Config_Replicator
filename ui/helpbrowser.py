# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/users/mercolino/PycharmProjects/Config_Replicator/ui/helpbrowser.ui'
#
# Created: Mon May 19 13:19:10 2014
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

class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        helpWindow.setObjectName(_fromUtf8("helpWindow"))
        helpWindow.resize(640, 480)
        helpWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(helpWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.helpWebView = QtWebKit.QWebView(self.centralwidget)
        self.helpWebView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.helpWebView.setObjectName(_fromUtf8("helpWebView"))
        self.gridLayout.addWidget(self.helpWebView, 0, 0, 1, 1)
        helpWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(helpWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        helpWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClose = QtGui.QAction(helpWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ui/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(helpWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), helpWindow.close)
        QtCore.QMetaObject.connectSlotsByName(helpWindow)

    def retranslateUi(self, helpWindow):
        helpWindow.setWindowTitle(_translate("helpWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("helpWindow", "toolBar", None))
        self.actionClose.setText(_translate("helpWindow", "Close", None))
        self.actionClose.setToolTip(_translate("helpWindow", "Close", None))

from PyQt4 import QtWebKit
