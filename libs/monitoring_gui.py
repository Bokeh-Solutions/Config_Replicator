from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import datetime
import queue

from libs import connection_gui as conn
from libs import summary_report_gui as sr
from libs import output_report_gui as out
import time
from ui import monitoring

class monitoringDlg(QDialog, monitoring.Ui_monitoringDialog):
    """
    Class to create the Monitoring window

    Arguments:

    script = Name of the script used
    list = Name of the destination list used
    th_number = Number of threads used
    com_list = Command List created from the script
    dest_list = Destination list created from the file
    user = username to login into the devices
    pwd = password used to login into the devices
    en_pwd = Enable Password
    out = Boolean to know if there is output
    """

    # Defining Signals
    getSummaryReport = pyqtSignal('QString', name='summary_report')
    getOutputReport = pyqtSignal('QString', name='output_report')

    def __init__(self, script, list, th_number, com_list, dest_list, user, pwd, en_pwd, out, parent=None):
        super(monitoringDlg, self).__init__(parent)
        self.setupUi(self)
        self.th_number = th_number
        self.com_list = com_list
        self.dest_list = dest_list
        self.monitoringOkPushButton.setEnabled(False)
        self.monitoringScriptLabel.setText(script)
        self.monitoringListLabel.setText(list)
        self.monitoringThreadsLabel.setText(str(th_number))
        self.monitoringProgressBar.setValue(0)
        self.TotalLcdNumber.display(len(self.dest_list))
        self.user = user
        self.pwd = pwd
        self.out = out
        self.en_pwd = en_pwd
        self.thread = ''
        self.threads = []
        self.summaryReport = ''
        self.outputReport = ''
        QTimer.singleShot(500, self.start_threads)

    def start_threads(self):
        """
        Function to start the Threads
        """
        destination_queue = queue.Queue()
        err_queue = queue.Queue()
        succ_queue = queue.Queue()
        output_queue = queue.Queue()

        for dest in self.dest_list:
            destination_queue.put(dest)

        for i in range(self.th_number):
            self.thread = conn.connectDevices(destination_queue, err_queue, output_queue, succ_queue, self.user, self.pwd, self.en_pwd, self.com_list, self.out, parent=self)
            self.threads.append(self.thread)
            self.thread.update_succ_conn.connect(self.update_succ_conn)
            self.thread.update_err_conn.connect(self.update_err_conn)
            self.thread.start()

         #Start an output report thread
        if self.out:
            output_thread = out.OutputReport(destination_queue, output_queue, self.monitoringScriptLabel.text(), self.monitoringListLabel.text())
            output_thread.sendOutputReport.connect(self.sendOutputReport)
            output_thread.start()
            time.sleep(.25)

        all_finished = False
        begin_time = datetime.datetime.now()
        while not all_finished:
            end_time = datetime.datetime.now()
            diff = end_time - begin_time
            diff = diff.seconds
            diff_hours = diff // 3600
            diff -= diff_hours * 3600
            diff_minutes = diff // 60
            diff_seconds = diff - (diff_minutes * 60)

            progress = int((1-(float(destination_queue.qsize())/len(self.dest_list)))*100)

            if progress == 100:
                progress = 99

            all_finished = True
            for thread in self.threads:
                if not thread.finish:
                    all_finished = False

            self.elapsedTimeLcdNumber.display('{:02d}:{:02d}:{:02d}'.format(diff_hours, diff_minutes, diff_seconds))
            self.monitoringProgressBar.setValue(progress)
            self.monitoringProgressLabel.setText(str(progress) + '%')
            QApplication.processEvents()
            time.sleep(0.5)

        if self.out:
            output_queue.put(('', '', 'finish_task'))

            while not output_thread.finish:
                pass

            output_thread.exit(0)

        self.monitoringProgressBar.setValue(100)
        self.monitoringProgressLabel.setText('100%')

        for thread in self.threads:
            thread.exit(0)

        #Creating Summary Report
        self.summaryReport = sr.summary_report(begin_time, end_time, self.user, self.monitoringScriptLabel.text(), self.monitoringListLabel.text(), self.th_number, len(self.dest_list), err_queue, succ_queue)

        self.monitoringOkPushButton.setEnabled(True)

        self.getSummaryReport.emit(self.summaryReport)

    def update_succ_conn(self):
        """
        Function to run when a signal succ conn arrives
        """
        self.SuccConnLcdNumber.display(self.SuccConnLcdNumber.value() + 1)

    def update_err_conn(self):
        """
        Function to run when a signal err conn arrives
        """
        self.errorConnLcdNumber.display(self.errorConnLcdNumber.value() + 1)

    def sendOutputReport(self, out_report):
        """
        Function to send the signal with the name of the output report
        """
        self.getOutputReport.emit(out_report)

    def closeEvent(self, evnt):
        """
        Function to avoid to close the monitor window while running
        """
        all_finished = True
        for thread in self.threads:
            if not thread.finish:
                all_finished = False
        QApplication.processEvents()
        time.sleep(1)
        if all_finished:
            super(monitoringDlg, self).closeEvent(evnt)
        else:
            evnt.ignore()

