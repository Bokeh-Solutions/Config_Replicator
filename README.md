# Config Replicator

Config Replicator is a tool that allows you to send script files (.src) to a list file that contains the information of
devices where you want to send the configuration file.

This tool was originally designed to interact with Cisco devices, but it is flexible enough to interact with other devices too.
This can be achieved by modifying the configuration file "config.ini"

This tool can use telnet or ssh protocols to connect to the devices and send the script files, this script files can also
gather data if needed and present a report with the data gathered. Config Replicator perform this tasks by leveraging the
threading library to spawn multiple threads and connect to different devices "simultaneously"

There are two different versions of this tool, a text based tool called config_replicator.py that only needs a terminal 
to run, and the gui version called config_replicator_gui.py that uses PyQT.

This tool was developed in Python 2.7 and the gui is using PyQT4, while telnetlib and paramiko are used to connect to the
devices with telnet and ssh respectively.

## Pre-Requisites
If the gui is needed, then PyQT5 should be installed. PyQT5 can be installed easily with "pip install pyqt5"
Also paramiko should be installed if ssh is needed to connect to the devices, in linux is easy to install the library,
but in Windows can pose a challenge, Google search can help you to find some information about this.

Because the libraries used by this tool are multiplatform the tool is multiplatform

## How it works
The process flow is really simple and can be divided in the following steps:
    - Select the script file with the commands to send to the devices
    - Select the list file with the files where the script file need to be sent
    - Specify the number of threads to use, this will speed up the process because it can use the waiting times while 
    connecting
    or waiting for output from the device efficiently
    - Specify the credentials to use 
    - Wait until the process is complete
    - Read the Reports generated, there could be different reports generated explained below:
        - **Summary Report**: Is teh report generated indicating, how many devices where contacted successfuly and how many had erros,
        which errors the script encountered and other useful statistics
        - **Output Report**: If the script file indicate that the output from the commands needs to be gathered then this report is created
        with all the output generated organized by device.

## Limitations
There are some limitations on this script that can be summarized as follow:
    - The credentials should be teh same for all the devices in the list
    - Telnet and SSH connections can be mixed together in the same list


**_Note:_**: This tool is provided as_is, no support comes with it and you are responsible to run it on your systems, if something breaks you are the only one to blame...
