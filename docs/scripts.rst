Scripts Files
=============

All the scripts files should be saved with an ".src" extension on the "scripts" directory, this files should be

The script files should have a ".src" extension and it is a plain device script as you were in front of a vty console
connected to it, for example if you are connecting to a Cisco Router then it should be commands as the ones you
will send when you are connected via telnet/ssh to the router.

There are other directives that could be configured on the scripts that tells the program some things, this directives are:
"!desc:" --> This directive without the quotes are used to add a Description comment in the Scripts Menu
"!output" --> This directive without the quotes are used to specify that the output of the commands should be grabbed.

----

For example, each line of the Script Menu is formed with:

- **Number:** To identify the selection
- **Script Name:** The name of the script i.e: name_script.src
- **Description:** the description of the script file configured with the "!desc" directive, if the directive is not present then "N/A" is shown

----

When the directive "!output" is used, the output will be saved on a file called *OutputReportMMDDYYYY.txt* inside the directory "/reports"

If "!output" is present in the script file, then the program send before the commands a command to not to stop for any user input
to the device and after the commands were sent then the program send the command to return the terminal to the defaults. This
commands could be configured in the "config.cfg" file with the "no_stop" and "default_stop" variables.

You should be sure that there is always a blank line at the end of the script to ensure that the last command is sent without
any problem, if the script is for Cisco devices it is recommended to finish all the script with teh character "!" without
the quotes

On the scripts folder there are two example script files:
- *loopback_config.src:* This file send the commands to a Cisco devices to configure two loopback interfaces
- *show_interfaces.src:* This file is an example of a script with output, it send the "show ip interface brief" to a cisco Device and grab the output