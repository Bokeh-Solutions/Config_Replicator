# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/users/mercolino/PycharmProjects/Config_Replicator/ui/reports.ui'
#
# Created: Thu May 15 18:07:10 2014
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

class Ui_ReportsWindow(object):
    def setupUi(self, ReportsWindow):
        ReportsWindow.setObjectName(_fromUtf8("ReportsWindow"))
        ReportsWindow.resize(640, 480)
        ReportsWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(ReportsWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(611, 0))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.summary_report = QtGui.QWidget()
        self.summary_report.setObjectName(_fromUtf8("summary_report"))
        self.gridLayout_3 = QtGui.QGridLayout(self.summary_report)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.summaryTextEdit = QtGui.QTextEdit(self.summary_report)
        self.summaryTextEdit.setMinimumSize(QtCore.QSize(570, 0))
        self.summaryTextEdit.setObjectName(_fromUtf8("summaryTextEdit"))
        self.gridLayout_3.addWidget(self.summaryTextEdit, 1, 0, 1, 1)
        self.summaryLabel = QtGui.QLabel(self.summary_report)
        self.summaryLabel.setObjectName(_fromUtf8("summaryLabel"))
        self.gridLayout_3.addWidget(self.summaryLabel, 0, 0, 1, 1)
        self.tabWidget.addTab(self.summary_report, _fromUtf8(""))
        self.output_report = QtGui.QWidget()
        self.output_report.setObjectName(_fromUtf8("output_report"))
        self.gridLayout_2 = QtGui.QGridLayout(self.output_report)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.outputTextEdit = QtGui.QTextEdit(self.output_report)
        self.outputTextEdit.setMinimumSize(QtCore.QSize(570, 0))
        self.outputTextEdit.setObjectName(_fromUtf8("outputTextEdit"))
        self.gridLayout_2.addWidget(self.outputTextEdit, 1, 0, 1, 1)
        self.outputLabel = QtGui.QLabel(self.output_report)
        self.outputLabel.setObjectName(_fromUtf8("outputLabel"))
        self.gridLayout_2.addWidget(self.outputLabel, 0, 0, 1, 1)
        self.tabWidget.addTab(self.output_report, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        ReportsWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(ReportsWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        ReportsWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClose = QtGui.QAction(ReportsWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ui/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(ReportsWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), ReportsWindow.close)
        QtCore.QMetaObject.connectSlotsByName(ReportsWindow)

    def retranslateUi(self, ReportsWindow):
        ReportsWindow.setWindowTitle(_translate("ReportsWindow", "Reports", None))
        self.summaryLabel.setText(_translate("ReportsWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summary_report), _translate("ReportsWindow", "Summary Report", None))
        self.outputLabel.setText(_translate("ReportsWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.output_report), _translate("ReportsWindow", "Output Report", None))
        self.toolBar.setWindowTitle(_translate("ReportsWindow", "toolBar", None))
        self.actionClose.setText(_translate("ReportsWindow", "Close", None))
        self.actionClose.setToolTip(_translate("ReportsWindow", "Close", None))

