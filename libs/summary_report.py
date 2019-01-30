import os
import datetime
import collections

def summary_report(init_time, fin_time, user, script, lst, thr, tot_dev, q_err, q_succ):
    """
    Function to save the summary Report

    Arguments:

    init_time = Time when the script begun

    fin_time = Ending time of the script

    user = username used to connect to the devices

    script = Response of the Script Menu

    lst = Response of the list Menu

    thr = Number of threads spawned

    tot_dev = Total Number of devices processed

    q_err = Error queue

    q_succ = Successful Connection Queue
    """
    errors = []
    errors_stats = []
    os.chdir('reports')
    date = datetime.datetime.now()
    file_name = 'SummaryReport%02d%02d%04d%02d%02d.txt' % (date.month, date.day, date.year, date.hour, date.minute)
    with open(file_name, 'w') as fd:
        os.chdir('..')
        fd.write("""Summary Report
==============\n\n""")
        fd.write("""Information
-----------\n""")
        fd.write('Time Stats:\n\n')
        fd.write('- **Date:** %s\n' % date.date())
        fd.write('- **Begin Time:** %s\n' % init_time)
        fd.write('- **End Time:** %s\n' % fin_time)

        #Processing Elapsed Time
        diff = fin_time - init_time
        diff = diff.seconds
        diff_hours = diff // 3600
        diff -= diff_hours * 3600
        diff_minutes = diff // 60
        diff_seconds = diff - (diff_minutes * 60)

        fd.write('- **Elapsed Time:** %02d Hours, %02d Minutes and %02d Seconds\n' % (diff_hours, diff_minutes, diff_seconds))
        fd.write('\nParameters:\n\n')
        fd.write('- **Script:** %s (%s)\n' % (script[1], script[2]))
        fd.write('- **Destination List:** %s (%s)\n' % (lst[1], lst[2]))
        fd.write('- **Number of Threads:** %i\n' % thr)
        fd.write('- **Username:** %s\n' % user)

        fd.write('\nConnection Stats:\n\n')
        fd.write('- **Total Devices processed:** %i\n' % tot_dev)
        fd.write('- **Connections with errors:** %i\n' % q_err.qsize())
        fd.write('- **Successful Connections:** %i\n' % q_succ.qsize())
        fd.write('\n----------\n\n')

        while not q_err.empty():
            e = q_err.get()
            errors.append(e)
            errors_stats.append(e[3])

        if len(errors) != 0:
            fd.write("""Error Stats
-----------\n""")
            counter = collections.Counter(errors_stats)
            for count in counter.most_common():
                fd.write('There are %i devices with error: %s\n' % (count[1], count[0]))

            fd.write('\n----------\n\n')

            fd.write("""Error Details
-------------\n""")
            for err in errors:
                title = '*Device:* %s (%s) connecting via %s\n' % (err[0], err[1], err[2])
                underline = '~'*len(title) + '\n'
                fd.write(title)
                fd.write(underline)
                fd.write('\tError: %s\n' % err[3])
                fd.write('\n')

            fd.write('\n----------\n\n')

            for err in list(counter):
                title = 'Routers with error: %s\n' % err
                fd.write(title)
                fd.write('-' * len(title) + '\n')
                for e in errors:
                    if err == e[3]:
                        fd.write('%s %s %s\n' % (e[0], e[1], e[2]))
                fd.write('\n----------\n\n')

        if q_succ.qsize() != 0:
            fd.write("""Successful Connections
----------------------\n""")
            while not q_succ.empty():
                succ = q_succ.get()
                fd.write('%s\t-->\t%s\n' % (succ[0], succ[1]))
                fd.flush()
                os.fsync(fd.fileno())
            fd.close()



__author__ = 'Miguel Ercolino'
