Report Files
============

Config Replicator generate two types of output reports, the first one it is always generated after each run of the program
and are called Summary Reports, he second ones are only generated when the script file has the directive !output configured.
The name format of the files are:

SummaryReportMMDDYYYYHHMM.txt and OutputReportMMDDYYYYHHMM.txt where:

- **MM:** Month when the report was generated
- **DD:** Day when the report was generated
- **YYYY:** Year when the report was generated
- **HH:** Hour when the report was generated
- **MM:** Minute when the report was generated

----

Summary Reports
---------------

The Summary Reports contains three sections that are described below:

Information
~~~~~~~~~~~

On this section you wil find general information of the run made, there is a subsection that give you the time statistics,
like:

- **Date:** It is the Date when the program was ran
- **Begin Time:** When the program begin the connection attempts to the devices on the destination list
- **End Time:** When he program end the connection attempts
- **Elapsed Time:** How much time it takes to run the program under the parameters specified

The second subsection gives you information about the parameters used to ru the program:

- **Script:** The name and description of the script used to run the program
- **Destination List:** The name and description of the destination list used
- **Number of Threads:** The number of threads used to connect to the devices
- **Username:** The username used to connect to the devices

The third subsection gives you the information of the connections:

- **Total Devices processed:** The total number of devices processed
- **Connections with errors:** The Number of devices with errors, a successful connection but an error in the commands sent increment this counter also a no response from the device
- **Successful Connections:** The number of successful connections, this counter is incremented only when the program made a successful connection via telnet or ssh to the router, the successfulness of the commands sent are not taking into consideration

Error Stats
~~~~~~~~~~~

Here are presented teh statistics about how many routers have the same problem

Error Details
~~~~~~~~~~~~~

On this section each connection error accounted on the "Connections with errors:" are presented, here you could check in detail
which was the error in the connection.

Error Connection Lists
~~~~~~~~~~~~~~~~~~~~~~

On this section are presented the list of the routers that had a specific problem in the format:

ip_address name_of_device connection_method

For Example:

192.168.1.100 Denver_Router telnet

This format will allow you to copy and paste this items on a list file in order to run another batch with the new list

Successful Connections
~~~~~~~~~~~~~~~~~~~~~~

On this section you will be presented with the successful connection attempts to the routers, the format of this section is:

IP_Address --> Name_of_the_device

For Example:

192.168.10.183	-->	R1-Router

----

Output Reports
--------------

The Output Reports contains two sections that are described below:

Information
~~~~~~~~~~~

Only the following information is presented:

- **Date:** It is the Date when the program was ran
- **Script:** The name and description of the script used to run the program
- **Destination List:** The name and description of the destination list used

Output Details
~~~~~~~~~~~~~~

On this section it is presented the output of each command on the script divided by device: