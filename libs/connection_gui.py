import telnetlib
import ConfigParser
import logging
import re

from PyQt4.QtCore import *


try:
    import paramiko
    paramiko_error = False
except ImportError as e:
    paramiko_error = True

class connectDevices(QThread):
    """
    Class for Multithreading to connect to the devices

    Arguments:

    q_dest = Destination Queue

    q_error = Error Queue

    q_out = Output Queue

    q_succ = Successful Connection Queue

    user = username to login to the devices

    pwd = password to login to the devices

    en_pwd = enable password

    cmd = List with the commands to send to the devices

    out = Boolean to express that the scripts need an output report

    """

    def __init__(self, q_dest, q_error, q_out, q_succ, user, pwd, en_pwd, cmd, out, parent=None):
        """
        Initialization function
        """
        super(connectDevices, self).__init__(parent)
        self.q_dest = q_dest
        self.q_error = q_error
        self.q_out = q_out
        self.q_succ = q_succ
        self.user = user
        self.pwd = pwd
        self.en_pwd = en_pwd
        self.cmd = cmd
        self.out = out
        self.finish = False

    def run(self):
        """
        Connection Function
        """
        config = ConfigParser.ConfigParser()

        #Parse the configuration file
        config.read('config.ini')
        enable = config.get('enable', 'use_enable').replace("\'", "").lower()
        enable_command = config.get('enable', 'enable_command').replace("\'", "").lower()
        username_prompts = config.get('prompts', 'username_prompts').replace("\'", "").split(',')
        password_prompts = config.get('prompts', 'password_prompts').replace("\'", "").split(',')
        telnet_device_enable_prompts = config.get('prompts', 'telnet_device_enable_prompts').replace("\'", "").split(',')
        telnet_device_prompts = config.get('prompts', 'telnet_device_prompts').replace("\'", "").split(',')
        ssh_device_prompt = config.get('prompts', 'ssh_device_prompt').replace("\'", "")
        ssh_device_enable_prompt = config.get('prompts', 'ssh_device_enable_prompt').replace("\'", "")
        error_strings = config.get('errors', 'error').replace("\'", "").split(',')
        telnet_tout = int(config.get('telnet', 'timeout'))
        ssh_tout = int(config.get('ssh', 'timeout'))
        no_stop = config.get('output', 'no_stop').replace("\'", "")
        default_stop = config.get('output', 'default_stop').replace("\'", "")

        #Multiline Commands
        multiline = config.get('multiline', 'commands').replace('\'', '').split(',')

        while not self.q_dest.empty():
            error = False
            #Picking a device from the queue
            ip, name, mode = self.q_dest.get()
            #Processing a telnet device
            if mode == 'telnet':
                try:
                    telnet = telnetlib.Telnet(ip, 23, timeout=telnet_tout)
                except Exception as e:
                    self.q_error.put((ip, name, mode, e.message if len(e.args) == 1 else 'Error[' + str(e.errno) + '] ' + e.strerror))
                    self.q_dest.task_done()
                    self.emit(SIGNAL('err_conn'))
                    continue

                #Sending Username
                try:
                    if telnet.expect(username_prompts, timeout=telnet_tout)[0] >= 0:
                        telnet.write(self.user + '\n')
                    else:
                        self.q_error.put((ip, name, mode, 'Problem matching username prompt'))
                        telnet.close()
                        self.q_dest.task_done()
                        self.emit(SIGNAL('err_conn'))
                        continue
                except Exception as e:
                    self.q_error.put((ip, name, mode, e.message if len(e.args) == 1 else 'Error[' + str(e.errno) + '] ' + e.strerror))
                    self.q_dest.task_done()
                    self.emit(SIGNAL('err_conn'))
                    continue

                #Sending Password
                try:
                    if telnet.expect(password_prompts, timeout=telnet_tout)[0] >= 0:
                        telnet.write(self.pwd + '\n')
                    else:
                        self.q_error.put((ip, name, mode, 'Problem matching password prompt'))
                        telnet.close()
                        self.q_dest.task_done()
                        self.emit(SIGNAL('err_conn'))
                        continue
                except Exception as e:
                    self.q_error.put((ip, name, mode, e.message if len(e.args) == 1 else 'Error[' + str(e.errno) + '] ' + e.strerror))
                    telnet.close()
                    self.q_dest.task_done()
                    self.emit(SIGNAL('err_conn'))
                    continue

                if enable == 'yes':
                    #Sending enable command
                    try:
                        if telnet.expect(telnet_device_enable_prompts, timeout=telnet_tout)[0] >= 0:
                            telnet.write(enable_command + '\n')
                        else:
                            telnet.write('\n')
                    except Exception as e:
                        self.q_error.put((ip, name, mode, e.message if len(e.args) == 1 else 'Error[' + str(e.errno) + '] ' + e.strerror))
                        telnet.close()
                        self.q_dest.task_done()
                        self.emit(SIGNAL('err_conn'))
                        continue

                    #Sending password if ask for it
                    try:
                        if telnet.expect(password_prompts, timeout=telnet_tout)[0] >= 0:
                            telnet.write(self.en_pwd + '\n')
                        else:
                            telnet.write('\n')
                    except Exception as e:
                        self.q_error.put((ip, name, mode, e.message if len(e.args) == 1 else 'Error[' + str(e.errno) + '] ' + e.strerror))
                        telnet.close()
                        self.q_dest.task_done()
                        self.emit(SIGNAL('err_conn'))
                        continue

                    try:
                        resp_cmd = telnet.expect(telnet_device_prompts, timeout=telnet_tout)
                        for err in error_strings:
                            if re.search(re.compile(err), resp_cmd[2]):
                                self.q_error.put((ip, name, mode, "There was a problem with the enable password"))
                                error = True
                                break
                        if error:
                            telnet.close()
                            self.q_dest.task_done()
                            self.emit(SIGNAL('err_conn'))
                            continue
                    except Exception as e:
                        self.q_error.put((ip, name, mode, 'There was a problem matching the device prompt'))
                        telnet.close()
                        self.q_dest.task_done()
                        self.emit(SIGNAL('err_conn'))
                        continue

                else:
                    #Checking for problems with authentication
                    try:
                        resp_cmd = telnet.expect(telnet_device_prompts, timeout=telnet_tout)
                        for err in error_strings:
                            if re.search(re.compile(err), resp_cmd[2]):
                                self.q_error.put((ip, name, mode, "There was a problem with the authentication"))
                                error = True
                                break
                        if error:
                            telnet.close()
                            self.q_dest.task_done()
                            self.emit(SIGNAL('err_conn'))
                            continue
                    except Exception as e:
                        self.q_error.put((ip, name, mode, e.message if len(e.args) == 1 else 'Error[' + str(e.errno) + '] ' + e.strerror))
                        telnet.close()
                        self.q_dest.task_done()
                        self.emit(SIGNAL('err_conn'))
                        continue

                try:
                    #Sending a no stop command
                    if self.out:
                        telnet.write(no_stop + '\n')
                        telnet.expect(telnet_device_prompts, timeout=telnet_tout)

                    #Sending Commands
                    resp_out = ''
                    if resp_cmd[0] >= 0:
                        #Flag for multiline commands
                        ml = False
                        for cmd in self.cmd:
                            #loop to check if cmd is a multiline command
                            for rgx in multiline:
                                #Check if it is the first line of a multiline command
                                first_line = re.search(rgx, cmd)
                                escape_char = rgx[-2]
                                if first_line and not ml:
                                    #Check if a multiline command is written in a one line
                                    one_multiline = re.search(rgx + '.+' + escape_char + '$', cmd)
                                    if not one_multiline:
                                        ml = True
                                    break
                                else:
                                    #Check if it is the last line of the multiline command
                                    last_line = re.search('.*' + escape_char + '$', cmd)
                                    if last_line and ml:
                                        ml = False
                            #If it is a multiline send it without a prompt, if not send it with prompt
                            if ml:
                                telnet.write(cmd)
                            else:
                                #If it is not multiline command then wait for prompt
                                telnet.write(cmd)
                                resp_cmd = telnet.expect(telnet_device_prompts, timeout=telnet_tout)
                                if self.out:
                                    resp_out = resp_out + resp_cmd[2] + '\n' + '-' * 70 + '\n'
                                for err in error_strings:
                                    if re.search(re.compile(err), resp_cmd[2]):
                                        self.q_error.put((ip, name, mode,
                                                          "There was a problem with the command \"%s\"" % cmd.strip(
                                                              '\n')))
                                        error = True
                                        break
                                if error:
                                    break
                        #Sending a default terminal stop
                        if self.out:
                            telnet.write(default_stop + '\n')
                            telnet.expect(telnet_device_prompts, timeout=telnet_tout)
                            self.q_out.put((ip, name, resp_out))
                    else:
                        self.q_error.put((ip, name, mode, "There was a problem matching the device prompt"))
                        telnet.close()
                        self.q_dest.task_done()
                        self.emit(SIGNAL('err_conn'))
                        continue

                    self.q_succ.put((ip, name))
                    telnet.close()
                    self.q_dest.task_done()
                    self.emit(SIGNAL('succ_conn'))

                except Exception as e:
                    self.q_error.put((ip, name, mode, e.message if len(e.args) == 1 else 'Error[' + str(e.errno) + '] ' + e.strerror))
                    telnet.close()
                    self.q_dest.task_done()
                    self.emit(SIGNAL('err_conn'))
                    continue

            #Processing a ssh device
            elif mode == 'ssh':
                if not paramiko_error:
                    logging.getLogger("paramiko").setLevel(logging.CRITICAL)

                    client = paramiko.SSHClient()
                    #Auto accepting ssh key
                    client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
                    #Connecting via ssh to ip
                    try:
                        client.connect(ip, port=22, username=self.user, password=self.pwd, timeout=ssh_tout)
                    except Exception as e:
                        self.q_error.put((ip, name, mode, e.message if len(e.args) == 1 else 'Error[' + str(e.errno) +'] ' + e.strerror))
                        self.q_dest.task_done()
                        self.emit(SIGNAL('err_conn'))
                        continue

                    #Starting interactive shell
                    chan = client.invoke_shell()

                    #Capturing the initial buffer
                    buff = ''
                    enable_ssh = False
                    while True:
                        resp = chan.recv(9999)
                        buff += resp
                        if re.search(ssh_device_enable_prompt, buff):
                            enable_ssh = True
                            break
                        if re.search(ssh_device_prompt, buff):
                            break

                    if enable_ssh and enable != 'yes':
                        self.q_error.put((ip, name, mode, 'SSH Error device ask for enable password and enable not configured in config.ini section [enable]'))
                        client.close()
                        self.q_dest.task_done()
                        self.emit(SIGNAL('err_conn'))
                        continue

                    #Sending enable command
                    match = False
                    if enable == 'yes':
                        chan.send(enable_command + '\n')
                        buff = ''
                        #Capturing response buffer
                        while True:
                            resp = chan.recv(9999)
                            buff += resp
                            if re.search(ssh_device_prompt, buff):
                                break
                            for pwd_prompt in password_prompts:
                                if re.search(pwd_prompt, buff):
                                    chan.send(self.en_pwd + '\n')
                                    match = True
                                    #Capturing response buffer
                                    while not re.search(ssh_device_prompt, buff):
                                        resp = chan.recv(9999)
                                        buff += resp
                                    break
                            if match:
                                break

                    #Sending no stop command
                    if self.out:
                        chan.send(no_stop + '\n')
                        buff = ''
                        #Capturing response buffer
                        while not re.search(ssh_device_prompt, buff):
                            resp = chan.recv(9999)
                            buff += resp

                    resp_out = ''
                    #Sending Commands
                    for cmd in self.cmd:
                        chan.send(cmd)
                        buff = ''
                        #Capturing response buffer
                        while not re.search(ssh_device_prompt, buff):
                            resp = chan.recv(9999)
                            buff += resp
                        #Creating string with all result commands for output
                        if self.out:
                            resp_out = resp_out + buff + '\n' + '-' * 70 + '\n'
                        #Checking if there was not error in the command
                        for err in error_strings:
                            if re.search(re.compile(err), buff):
                                self.q_error.put((ip, name, mode, "There was a problem with the command \"%s\"" % cmd.strip('\n')))
                                error = True
                                break
                        if error:
                            break

                    #Sending a terminal default stop
                    if self.out:
                        chan.send(default_stop + '\n')
                        buff = ''
                        #Capturing response buffer
                        while not re.search(ssh_device_prompt, buff):
                            resp = chan.recv(9999)
                            buff += resp
                        self.q_out.put((ip, name, resp_out))

                    self.q_succ.put((ip, name))
                    client.close()
                    self.q_dest.task_done()
                    self.emit(SIGNAL('succ_conn'))
                else:
                    self.q_error.put((ip, name, mode, "Paramiko library not installed, SSH connections are not possible"))
                    self.q_dest.task_done()
                    self.emit(SIGNAL('err_conn'))
        self.finish = True

__author__ = 'Miguel Ercolino'
