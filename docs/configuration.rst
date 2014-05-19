Configuration File (config.cfg)
===============================

There is a configuration file used to fine tune the program and to change some options it is used by the text and GUI version of the program,
this configuration file is conformed by 6 sections that are described below:

[enable] Section
----------------

On this section you could configure tell the config replicator to wait for the enable password in the connection flow:

- **enable:** This parameter is used to use enable on the connection flow take the values 'yes' or 'no'
- **enable_command:** This parameter is used to specify the enable command to send to the devices

[prompts] Section
-----------------

On this section you could configure the different prompts that the program should match in order to proceed sending commands,
each parameter is discussed in detail below:

- **username_prompts:** This parameter is used to match the username prompts when connecting to a device via telnet, it accepts a list of REGEX prompts enclosed in a single quotes and separated by comma
- **password_prompts:** This parameter is used to match the password prompts when connecting to a device via telnet, it accepts a list of REGEX prompts enclosed in a single quotes and separated by comma
- **telnet_device_prompts:** This parameter is used to match the device prompt when connecting to a device via telnet, it accepts a list of REGEX prompts enclosed in a single quotes and separated by comma
- **ssh_device_prompt:** This parameter is used to match the device prompts when connecting to a device via ssh, it only accept a single value
- **telnet_device_enable_prompts:** This parameter is used to match the enable prompts when connecting to a device via telnet, it accepts a list of REGEX prompts enclosed in a single quotes and separated by comma
- **ssh_device_enable_prompt:** This parameter is used to match the device enable prompt when connecting to a device via ssh, it only accept a single value

[errors] Section
----------------

On this section you could configure the different errors that you could find when sending the commands to the device, each
time that a command is send to a device via telnet or ssh the program checks the output with this list, if a match is found
then an error is registered, the connection is considered successful but an error in the connection is raised.

- **error:** This parameter is used to match the errors when sending commands to a device via any method, it accepts a list of REGEX errors enclosed in a single quotes and separated by comma

[output] Section
----------------

On this section you could configure the different commands to send before and after the commands on a script file with the !output directive,
this commands should prevent the stop of the output to wait for an user input.

- **no_stop:** This parameter is used to configure the command to send to prevent the output setup to wait for a user input, i.e: In Cisco should be "terminal length 0"
- **default_stop:** This parameter is used to configure the command to send to cancel the previous command, i.e: In Cisco should be "terminal no length" or "terminal length 32"

[telnet] Section
----------------

On this section you could configure the different parameters for the telnet connections.

- **timeout:** This parameter is used to configure the timeout value for the telnet connections and to wait for the prompt after sending a command, it is recommended not to configure a low value, because could lead to undesirable results, the minimum recommended value is 5 seconds.

[ssh] Section
-------------

On this section you could configure the different parameters for the ssh connections.

- **timeout:** This parameter is used to configure the timeout for the ssh connections only

[menus] Section
---------------

On this section you could configure the different parameters for the Script and Destination List Menus, this parameters are not used by the gui version.

- **len_page:** Specify the length of each page of the menu, ie. if 3 is specified only 3 items per page will be shown
- **title:** Title of the Menu, it is always rendered on the menu
- **subtitle:** Subtitle of the menu, it is a field below the title, if none is specified is not rendered
- **prompt:** Prompt shown for user input
- **col_number:** Number of columns to reserve for the number column of the menu
- **col_item:** Number of columns to reserve for the item column of the menu (Scripts name or lists name)
- **col_desc:** Number of columns to reserve for the description column of the menu

[progress] Section
------------------

Config Replicator print the progress of the connections every "interval" seconds, this parameters are not used by the gui version.

- **interval:** Number of seconds before printing the progress of teh connection