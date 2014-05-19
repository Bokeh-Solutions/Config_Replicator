Multithreading and Queues
=========================

Config Replicator uses multithreading to speed up three processes in the code, the first one is the connection flow to each device,
the second one is the Output Report and the last one is the Progress Printing. The Summary Report is processed by the main program after the all the threads are finished.

The task flow to the different threads are controlled by queues, there are 4 queues used:

- **Destination Queue:** The destination queue is filled before spawning the connection threads, and it is filled with a tuple (ip_address, connection_mode), where connection mode could be a "telnet" or "ssh"
- **Error Queue:** This queue is used to accumulate errors found trying to connect, authenticate or sending commands to the device, it is filled in the connection process and is a tuple of the form (ip_address, name_of_the_device, connection_mode, error_string)
- **Success Queue:** This is a queue used to register when a successful connection is made, even if after there was any error sending commands, it is formed by a tuple (ip_address, name_of_the_address) and it is filled in the connection process
- **Output Queue:** The Output access is used to save the output of the commands send when the directive !output is present on the script, it has a format (ip_address, name_of_the_device, Output) where Output is the output of all the commands send to the device.

You could only specify the number of threads that should be spawned for the connection process and it is asked on the interactive section, the number of threads
depends on many factors and it is wise to do some tests, to see how many threads your computer could handle, normally you could spawn 20 threads without any problem,
but there are also some systems that could handle 100 threads without a glitch, so make your tests on your system.

With the number of threads and the timeout of telnet and ssh found in the file "config.cfg" you could process a large quantity of devices in a short period of time,
take into account that the larger the number of threads is more devices are processed at the same time, so if there is a problem with the configuration script more devices will be affected,
also if your connection is slow and the timeouts are not set correctly you could find some undesirable results, so be conservative.

For example if you could connect to a device but the authentication is managed by a server (tacacs or radius) and there is no reachability, then the timeout value for the authentication server could
be high, and if the timeout configured on the configuration file is lower than the timeout on the server you will found always an error trying to authenticate to the device.

On the contrary there is only one thread for the output process and for the progress printing, that means that an output write to the Output file each time that there is a task on the output queue and the output queue
is filled by the connection process.

The error queue is processed once all the threads finished to process the queues, and is processed sequentially to fill out the Summary Report.
