.. Config Replicator documentation master file, created by
   sphinx-quickstart on Fri Apr 25 18:56:50 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Config Replicator's documentation!
=============================================

Config Replicator is a program written in Python 2.7.6 multiplatform and multithreaded created to help to the deployment
of the same configuration to a list of network devices, could be also used to grab the output of commands in a list of network
devices, until now it was only tested with Cisco Routers but through the "config.cfg" file could be used with other
devices too.

Config replicator grab a list of commands to send to the devices saved on a file with a ".src" extension saved in the
"scripts" directory, then grab the network device list from a destination list file with a ".lst' extension saved on the
"lists" directory. All he commands grabbed will be send to each one of the devices on the destination list.

The flow of the program could be resumed as:

    - Select the script to send to each device
    - Select the destination list where to send the script selected
    - Select the number of threads to use
    - Enter the Username and Password to use to connect to the devices
    - Enter the enable password if enable was configured in 'config.cfg'

In the following sections it is specified how the program works

Contents:

.. toctree::
   :maxdepth: 2

   installation
   start
   gui
   multithreading
   scripts
   lists
   reports
   configuration
   debugging
   license
   executable
   code


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

