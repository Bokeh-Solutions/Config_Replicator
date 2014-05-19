import ConfigParser
import threading
import time

class Progress (threading.Thread):
    """
    Class for Multithreading to print the progress of the connections

    Arguments:

    q_dest = Destination Queue

    tot_dev = Total Number of devices processed

    logger = Logging object
    """
    def __init__(self, q_dest, tot_dev, logger):
        """
        Initialization function
        """
        threading.Thread.__init__(self)
        self.q_dest = q_dest
        self.tot_dev = tot_dev
        self.logger = logger

    def run(self):
        """
        Progress printing function
        """
        config = ConfigParser.ConfigParser()

        #Parse the configuration file
        self.logger.debug('Parsing the configuration file')
        config.read('config.cfg')
        interval = int(config.get('progress', 'interval'))

        while not self.q_dest.empty():
            time.sleep(interval)
            progress = (1 - (float(self.q_dest.qsize())/self.tot_dev)) * 100
            title = ' Progress:'
            content = ' Connecting Progress: %.2f%% ' % progress
            tot_len = len(content) + 2
            print
            print '+' + '-' * tot_len + '+'
            print '| ' + title + ' ' * (tot_len - len(title) - 1) + '|'
            print '| ' + content + ' |'
            print '+' + '-' * tot_len + '+'
            print

__author__ = 'Miguel Ercolino'
