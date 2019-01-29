import os
import re
import sys
import Queue
import logging
import getpass
import ConfigParser
import datetime

from libs import menu
from libs import summary_report as sr
from libs import connection as conn
from libs import progress as prog
from libs import output_report as out


def help_arg():
    """
    Function to print help
    """
    print 'To enable the debug use the directive -d, use --help for help'


def welcome():
    """
    Function to print the Welcome Screen
    """
    welcome_string = """
    Welcome to the Config Replicator
    ================================

    All the scripts should be saved with an \".src\" extension on the \"scripts\" directory, read the README.md file on the
    directory to know more about this files.

    All the destination lists should be saved with a \".lst\" extension on the \"lists\" directory, read the README.md file
    on the directory to know more about this files.

    You could find the reports on the \"reports\" directory with a format \"SummaryReportMMDDYYYYHHMM.txt\" and if your
    script needs output then it will be generated another report with the format \"OutputReportMMDDYYYYHHMM.txt\"

    This program uses multithreading to speed up the process when the destination list is big, you could select the number
    of threads to spawn just before to send the script to the destination list, please use a reasonable number here you could
    have undesirable results if this number is too big.

    The flow of the program could be resumed as:
        - Select the script to send to each device
        - Select the destination list where to send the script selected
        - Select the number of threads to use
        - Enter the Username and Password to use to connect to the devices
        ' Enter the Enable password if requested
    """
    clear()
    print welcome_string
    raw_input('Press any key to continue.')


def clear():
    """
    Function to Clear the terminal window, it should work on linux and windows
    """
    os.system('cls' if os.name == 'nt' else 'clear')


######################################################################################
#### Main
######################################################################################
if __name__ == "__main__":

    #Logging setup
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    debug = False
    handler = ''

    #Processing arguments
    try:
        if sys.argv[1] == '-d':
            date = datetime.datetime.now()
            debug_file = 'Debug_Output%02d%02d%04d%02d%02d.log' % (date.month, date.day, date.year, date.hour, date.minute)
            os.chdir('debugs')
            handler = logging.FileHandler(debug_file)
            os.chdir('..')
            handler.setLevel(logging.DEBUG)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)
            debug = True
        elif sys.argv[1] == '--help':
            help_arg()
            sys.exit(0)
        else:
            help_arg()
            sys.exit(0)
    except IndexError:
        pass

    #Welcome Screen
    welcome()

    #Parsing config file for the menus parameters
    logger.debug('Parsing the configuration file')
    configure = ConfigParser.ConfigParser()
    configure.read('config.cfg')
    #Use Enable?
    use_enable = configure.get('enable', 'use_enable').replace("\'", "").lower()
    #Scripts menu parameters
    script_menu_page_len = int(configure.get('menus', 'scripts_menu_len_page'))
    script_menu_title = configure.get('menus', 'scripts_menu_title').replace('\'', '')
    script_menu_subtitle = configure.get('menus', 'scripts_menu_subtitle').replace('\'', '')
    script_menu_prompt = configure.get('menus', 'scripts_menu_prompt').replace('\'', '')
    script_menu_col_number = int(configure.get('menus', 'scripts_menu_col_number'))
    script_menu_col_item = int(configure.get('menus', 'scripts_menu_col_item'))
    script_menu_col_desc = int(configure.get('menus', 'scripts_menu_col_desc'))

    #Lists menu parameters
    list_menu_page_len = int(configure.get('menus', 'lists_menu_len_page'))
    list_menu_title = configure.get('menus', 'lists_menu_title').replace('\'', '')
    list_menu_subtitle = configure.get('menus', 'lists_menu_subtitle').replace('\'', '')
    list_menu_prompt = configure.get('menus', 'lists_menu_prompt').replace('\'', '')
    list_menu_col_number = int(configure.get('menus', 'lists_menu_col_number'))
    list_menu_col_item = int(configure.get('menus', 'lists_menu_col_item'))
    list_menu_col_desc = int(configure.get('menus', 'lists_menu_col_desc'))


    #Creation of the Scripts Menu
    logger.debug('Creating Script Menu')
    script_menu = menu.Menu()
    script_menu.menu_title = script_menu_title
    script_menu.menu_subtitle = script_menu_subtitle
    script_menu.prompt = script_menu_prompt
    script_menu.len_page = script_menu_page_len
    script_menu.change_cols(script_menu_col_number, script_menu_col_item, script_menu_col_desc)

    #Creation of the List Menu
    logger.debug('Creating List Menu')
    list_menu = menu.Menu()
    list_menu.menu_title = list_menu_title
    list_menu.menu_subtitle = list_menu_subtitle
    list_menu.prompt = list_menu_prompt
    list_menu.len_page = list_menu_page_len
    list_menu.change_cols(list_menu_col_number, list_menu_col_item, list_menu_col_desc)

    #Change to the script directory
    os.chdir('scripts')
    desc = re.compile('(^![Dd][Ee][Ss][Cc]:\s*)(.+)\n')
    logger.debug('Searching all the files with .src extension to populate script menu')
    for f in os.listdir('.'):
        #Check if it has the .src extension
        if re.search('.+\.src$', f):
            logger.debug('Opening file: %s' % f)
            fd = open(f, 'r')
            lines = fd.readlines()
            fd.close()
            match = False
            for line in lines:
                #Search for the !desc: directive
                match = re.search(desc, line)
                if match:
                    #Add item to the script menu
                    logger.debug('Found Description directive on file: %s' % f)
                    script_menu.add_item(f, match.group(2))
                    break
            if not match:
                #Add Item to the script menu and use N/A if does not have teh directive description
                script_menu.add_item(f, 'N/A')
                logger.debug('Description directive not found on file: %s' % f)

    #return to the initial directory
    os.chdir('..')

    #Change to the lists directory
    os.chdir('lists')
    desc = re.compile('(^![Dd][Ee][Ss][Cc]:\s*)(.+)\n')
    logger.debug('Searching all the files with .lst extension to populate list menu')
    for f in os.listdir('.'):
        #Check if it has the .lst extension
        if re.search('.+\.lst$', f):
            logger.debug('Opening file: %s' % f)
            fd = open(f, 'r')
            lines = fd.readlines()
            fd.close()
            match = False
            for line in lines:
                #Search for the !desc: directive
                match = re.search(desc, line)
                if match:
                    #Add item to the list menu
                    logger.debug('Found Description directive on file: %s' % f)
                    list_menu.add_item(f, match.group(2))
                    break
            if not match:
                #Add Item to the list menu and use N/A if does not have teh directive description
                list_menu.add_item(f, 'N/A')
                logger.debug('Description directive not found on file: %s' % f)

    #return to the initial directory
    os.chdir('..')

    logger.debug('Entering in the script menu loop')
    while True:
        #Print and loop the script menu
        resp_script = script_menu.loop()

        r = ' '
        #Loop for the script action
        while r.lower() != 'r':
            #Clear the terminal window
            clear()

            #Take input user to take action over script
            print 'You selected the script \"%s\"' % resp_script[1]
            print 'What do you want to do next?'
            r = raw_input('(C)ontinue, (V)iew, (R)eturn, (Q)uit: ')

            #Make decision about selection
            if r.lower() == 'c':
                break
            elif r.lower() == 'v':
                clear()
                os.chdir('scripts')
                fd = open(resp_script[1], 'r')
                os.chdir('..')
                print resp_script[1]
                print "="*len(resp_script[1])
                for line in fd:
                    print line.strip('\n')
                print
                print '-'*70
                fd.close()
                raw_input('Press any key to continue')
            elif r.lower() == 'r':
                break
            elif r.lower() == 'q':
                sys.exit(0)

        #If continue was selected then break the script menu loop
        if r.lower() == 'c':
            break

    logger.debug('Entering in the list menu loop')
    while True:
        #Print and loop the list menu
        resp_list = list_menu.loop()

        threads = ' '
        #Loop for the list action
        while type(threads) != int:
            #Clear the terminal window
            clear()

            #Take input user to take action over list
            print 'The selected script \"%s\" will be send to the destination list \"%s\"' % (resp_script[1], resp_list[1])
            print 'How many threads do you want to have? '
            threads = raw_input('Enter a number or (R)eturn, (Q)uit: ')

            #Make a decision about the selection
            if threads.lower() == 'q':
                sys.exit(0)
            elif threads.lower() == 'r':
                break

            #Try to convert to integer
            try:
                threads = int(threads)
                if threads == 0:
                    threads = 1
            except ValueError:
                threads = ' '

        #If it is an integer break the list menu loop
        if type(threads) == int:
            break

    #Ask for username and password
    clear()
    print 'Enter the credentials to login into the devices.'
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')

    #Ask for enable password
    if use_enable == 'yes':
        clear()
        print 'You selected the use of enable password in the config.cfg section [enable]'
        print 'Enter the enable password'
        enable_password = getpass.getpass('Enable password: ')
    else:
        enable_password = ''

    #Last Warning before proceed
    r = ' '
    while r.lower() != 'y':
        clear()
        print """################
#   WARNING!   #
################
After this screen you will use the credentials entered before to send the script \"%s\" to each device saved on the
destination list \"%s\", using %i threads
        """ % (resp_script[1], resp_list[1], threads)
        print '-' * 70
        r = raw_input('Are you sure you want to continue? (Y)es/(N)o: ')

        if r.lower() == 'n':
            sys.exit(0)

    #Create all the queues
    logger.debug('Creating the queues')
    destination_queue = Queue.Queue()
    err_queue = Queue.Queue()
    succ_queue = Queue.Queue()
    output_queue = Queue.Queue()

    #Set the Beginning time
    begin_time = datetime.datetime.now()

    #Filling the Destination queue with tuple (ip_address, telnet/ssh)
    logger.debug('Filling the destination queue')
    os.chdir('lists')
    fd = open(resp_list[1], 'r')
    os.chdir('..')
    ip_regex = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
    for line in fd:
        if re.match(ip_regex, line):
            param = line.split(' ')
            #Processing IP Address
            ip_addr = param[0].strip('\n')
            #Processing Device name
            try:
                dev_name = param[1].strip('\n')
            except IndexError:
                dev_name = 'N/A'
            #processing Connection Mode
            try:
                conn_mode = param[2].lower().strip('\n')
                if conn_mode not in ['telnet', 'ssh']:
                    conn_mode = 'telnet'
            except IndexError:
                conn_mode = 'telnet'
            destination_queue.put((ip_addr, dev_name, conn_mode))
    fd.close()

    #Total devices
    total_devices = destination_queue.qsize()

    #Creating list with commands to send and output directive
    os.chdir('scripts')
    fd = open(resp_script[1], 'r')
    os.chdir('..')
    output_pattern = re.compile('(^![Oo][Uu][Tt][Pp][Uu][Tt])(.*)\n')
    output = False
    commands = []
    for line in fd:
        if not re.search('^!', line):
            commands.append(line)
        elif re.search(output_pattern, line):
            output = True
    fd.close()

    logger.debug('Starting %i connection threads' % threads)
    for i in range(threads):
        t = conn.Connection(destination_queue, err_queue, output_queue, succ_queue, username, password, enable_password, commands, output, debug, logger, handler)
        t.setDaemon(True)
        t.start()

    #Start printing progress
    logger.debug('Starting printing progress thread')
    t = prog.Progress(destination_queue, total_devices, logger)
    t.setDaemon(True)
    t.start()

    #Start an output report thread
    if output:
        logger.debug('Starting Output report thread')
        t = out.OutputReport(destination_queue, output_queue, resp_script, resp_list)
        t.setDaemon(True)
        t.start()

    destination_queue.join()
    output_queue.join()

    #Set the end time
    end_time = datetime.datetime.now()

    logger.info('Finished Connecting, creating Summary Report')
    sr.summary_report(begin_time, end_time, username, resp_script, resp_list, threads, total_devices, err_queue, succ_queue)

    __author__ = 'Miguel Ercolino'
