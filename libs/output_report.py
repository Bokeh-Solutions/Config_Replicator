import threading
import os
import datetime

class OutputReport (threading.Thread):
    """
    Class for Multithreading to generate the Output Report for scripts with the directive !output

    Arguments:

    q_dest = Destination Queue

    q_out = Output Queue

    script = Response of the Script Menu

    lst = Response of the list Menu
    """
    def __init__(self, q_dest, q_out, script, lst):
        """
        Initialization function
        """
        threading.Thread.__init__(self)
        self.q_dest = q_dest
        self.q_out = q_out
        self.script = script
        self.lst = lst

    def run(self):
        """
        Output report function
        """
        os.chdir('reports')
        date = datetime.datetime.now()
        file_name = 'OutputReport{month:02d}{day:02d}{year:04d}{hour:02d}{minute:02d}.txt'.format(month=date.month,
                                                                                                  day=date.day,
                                                                                                  year=date.year,
                                                                                                  hour=date.hour,
                                                                                                  minute=date.minute)
        with open(file_name, 'w') as fd:
            os.chdir('..')
            fd.write("""Output Report
=============\n\n""")
            fd.write("""Information
-----------\n""")
            fd.write('- **Date:** %s\n' % date.date())
            fd.write('- **Script:** %s (%s)\n' % (self.script[1], self.script[2]))
            fd.write('- **Destination List:** %s (%s)\n' % (self.lst[1], self.lst[2]))
            fd.write('\n----------\n\n')
            fd.write("""Output Details
--------------\n""")
            while True:
                out = self.q_out.get()
                title = '*Device:* %s (%s)\n' % (out[0], out[1])
                underline = '~' * len(title) + '\n'
                fd.write(title)
                fd.write(underline)
                fd.write(out[2])
                fd.write('\n\n')
                fd.flush()
                os.fsync(fd.fileno())
                self.q_out.task_done()


__author__ = 'Miguel Ercolino'
