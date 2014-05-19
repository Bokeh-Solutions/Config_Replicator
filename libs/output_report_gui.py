from PyQt4.QtCore import *
import os
import datetime

class OutputReport (QThread):
    """
    Class for Multithreading to generate the Output Report for scripts with the directive !output

    Arguments:

    q_dest = Destination Queue

    q_out = Output Queue

    script = Response of the Script Menu

    lst = Response of the list Menu
    """
    def __init__(self, q_dest, q_out, script, lst, parent=None):
        """
        Initialization function
        """
        super(OutputReport, self).__init__(parent)
        self.q_dest = q_dest
        self.q_out = q_out
        self.script = script
        self.lst = lst
        self.finish = False

    def run(self):
        """
        Output report function
        """
        os.chdir('reports')
        date = datetime.datetime.now()
        file_name = 'OutputReport%02d%02d%04d%02d%02d.txt' % (date.month, date.day, date.year, date.hour, date.minute)
        fd = open(file_name, 'w')
        os.chdir('..')
        fd.write("""Output Report
=============\n\n""")
        fd.write("""Information
-----------\n""")
        fd.write('- **Date:** %s\n' % date.date())
        fd.write('- **Script:** %s\n' % self.script)
        fd.write('- **Destination List:** %s\n' % self.lst)
        fd.write('\n----------\n\n')
        fd.write("""Output Details
--------------\n""")
        out = ('', '', '')
        while out[2] != 'finish_task':
            out = self.q_out.get()
            if out[2] != 'finish_task':
                title = '*Device:* %s (%s)\n' % (out[0], out[1])
                underline = '~' * len(title) + '\n'
                fd.write(title)
                fd.write(underline)
                fd.write(out[2])
                fd.write('\n\n')
            self.q_out.task_done()
        fd.close()
        self.emit(SIGNAL('output_report(QString)'), file_name)
        self.finish = True

__author__ = 'Miguel Ercolino'
