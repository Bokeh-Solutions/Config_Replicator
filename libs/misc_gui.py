from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os

from ui import credentials
from ui import settingswindow
from ui import enable
from ui import helpbrowser
from ui import reports


class reportsWindow(QMainWindow, reports.Ui_ReportsWindow):
    """
    Class to create the Reports window

    Arguments:

    summary_report_file = Name of the created summary report

    output_report_file = Name of the output summary report
    """
    def __init__(self, summary_report_file='', output_report_file='', parent=None):
        """
        Initialization Function
        """
        super(reportsWindow, self).__init__(parent)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)
        self.summaryTextEdit.setReadOnly(True)
        self.outputTextEdit.setReadOnly(True)

        if summary_report_file == '':
            self.summaryLabel.setText('Summary report not found, connect to devices first.')
        else:
            self.summaryLabel.setText(summary_report_file)
            fd = open('reports/' + summary_report_file)
            self.summaryTextEdit.setPlainText(fd.read())

        if output_report_file == '':
            self.tabWidget.removeTab(1)
        else:
            self.outputLabel.setText(output_report_file)
            fd = open('reports/' + output_report_file)
            self.outputTextEdit.setPlainText(fd.read())


class helpWindow(QMainWindow, helpbrowser.Ui_helpWindow):
    """
    Class to create the Help Window
    """
    def __init__(self, parent=None):
        super(helpWindow, self).__init__(parent)
        self.setupUi(self)
        help_file = os.path.abspath("docs/_build/html/index.html")
        self.helpWebView.setUrl(QUrl('file:///' + help_file.replace('\\', '/')))


class enableDlg(QDialog, enable.Ui_enableDialog):
    """
    Class to create the enable Dialog
    """
    def __init__(self, parent=None):
        super(enableDlg, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_enableButtonBox_accepted(self):
        """
        Function to run when the Ok Button is clicked
        """
        self.emit(pyqtSignal('QString', name='enable'), self.enableLineEdit.text())


class settingsWindow(QMainWindow, settingswindow.Ui_SettingsWindow):
    """
    Class to create the Settings window
    """
    def __init__(self, parent=None):
        super(settingsWindow, self).__init__(parent)
        self.setupUi(self)
        f = open('config.ini', 'r')
        self.settingsTextEdit.setPlainText(f.read())
        self.settingsTextEdit.setReadOnly(True)
        f.close()
        self.statusbar.showMessage('config.ini')
        self.actionSettingsSave.setEnabled(False)

    @pyqtSlot()
    def on_actionSettingsEdit_triggered(self):
        """
        Function to run when the Edit button is pressed in the toolbar
        """
        self.actionSettingsEdit.setEnabled(False)
        self.settingsTextEdit.setReadOnly(False)
        self.statusbar.showMessage('Editing config.ini')

    @pyqtSlot()
    def on_actionSettingsSave_triggered(self):
        """
        Function to run when the Save button is pressed in the toolbar
        """
        f = open('config.ini', 'w')
        f.write(self.settingsTextEdit.toPlainText())
        f.close()
        self.actionSettingsEdit.setEnabled(True)
        self.settingsTextEdit.setReadOnly(True)
        self.statusbar.showMessage('config.ini Saved...')

    @pyqtSlot()
    def on_settingsTextEdit_textChanged(self):
        """
        Function to run when the text change
        """
        self.actionSettingsSave.setEnabled(True)


class credentialDlg(QDialog, credentials.Ui_Dialog):
    """
    Class to create the Credential dialog
    """
    def __init__(self, parent=None):
        super(credentialDlg, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """
        Function to run when the Ok Button is clicked
        """
        self.emit(pyqtSignal('QString', 'QString', name='credentials'), self.usernameLineEdit.text(), self.passwordLineEdit.text())
