# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reports.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_ReportsWindow(object):
    def setupUi(self, ReportsWindow):
        path = os.path.dirname(os.path.abspath(__file__))
        ReportsWindow.setObjectName("ReportsWindow")
        ReportsWindow.resize(640, 480)
        ReportsWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(ReportsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(611, 0))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.summary_report = QtWidgets.QWidget()
        self.summary_report.setObjectName("summary_report")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.summary_report)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.summaryTextEdit = QtWidgets.QTextEdit(self.summary_report)
        self.summaryTextEdit.setMinimumSize(QtCore.QSize(570, 0))
        self.summaryTextEdit.setObjectName("summaryTextEdit")
        self.gridLayout_3.addWidget(self.summaryTextEdit, 1, 0, 1, 1)
        self.summaryLabel = QtWidgets.QLabel(self.summary_report)
        self.summaryLabel.setObjectName("summaryLabel")
        self.gridLayout_3.addWidget(self.summaryLabel, 0, 0, 1, 1)
        self.tabWidget.addTab(self.summary_report, "")
        self.output_report = QtWidgets.QWidget()
        self.output_report.setObjectName("output_report")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.output_report)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.outputTextEdit = QtWidgets.QTextEdit(self.output_report)
        self.outputTextEdit.setMinimumSize(QtCore.QSize(570, 0))
        self.outputTextEdit.setObjectName("outputTextEdit")
        self.gridLayout_2.addWidget(self.outputTextEdit, 1, 0, 1, 1)
        self.outputLabel = QtWidgets.QLabel(self.output_report)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout_2.addWidget(self.outputLabel, 0, 0, 1, 1)
        self.tabWidget.addTab(self.output_report, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        ReportsWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(ReportsWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        ReportsWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClose = QtWidgets.QAction(ReportsWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(path, "exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon)
        self.actionClose.setObjectName("actionClose")
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(ReportsWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionClose.triggered.connect(ReportsWindow.close)
        QtCore.QMetaObject.connectSlotsByName(ReportsWindow)

    def retranslateUi(self, ReportsWindow):
        _translate = QtCore.QCoreApplication.translate
        ReportsWindow.setWindowTitle(_translate("ReportsWindow", "Reports"))
        self.summaryLabel.setText(_translate("ReportsWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summary_report), _translate("ReportsWindow", "Summary Report"))
        self.outputLabel.setText(_translate("ReportsWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.output_report), _translate("ReportsWindow", "Output Report"))
        self.toolBar.setWindowTitle(_translate("ReportsWindow", "toolBar"))
        self.actionClose.setText(_translate("ReportsWindow", "Close"))
        self.actionClose.setToolTip(_translate("ReportsWindow", "Close"))

