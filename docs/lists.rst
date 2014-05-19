Destination List Files
======================

All the destination lists should be saved with a ".lst" extension on the "lists" directory. The format of this file is:

Ip_address Name_of_the device [telnet/ssh]

----

For example:

**10.10.10.1 Denver_Router telnet** --> it will connect to the Denver_Router with an ip address of 10.10.10.1 via telnet.

**10.10.10.1 Denver_Router** --> it is the same as the previous entry, the default method of connection is telnet, if no
method of connection is found or the name is not recognizable then telnet will always be used.

**10.10.10.1 Denver_Router ssh** --> it will connect to the Denver_Router with an ip address of 10.10.10.1 via ssh.

----

As in the scripts files the destination list files use also the "!desc:" directive to show the description of the list in the
Scripts Menu, each line of the Destination List Menu is formed with:

- **Number:** To identify the selection
- **List Name:** The name of the list i.e: name_script.lst
- **Description:** the description of the script file configured with the "!desc" directive, if the directive is not present then "N/A" is shown

On the scripts folder there are one example list files:

- *routers.lst:* This file send the commands to a different devices using different connection methods