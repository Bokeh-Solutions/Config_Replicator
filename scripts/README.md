The script files should have a ".src" extension and it is a plain cisco script

Use the directive "!desc:" to add a description about the script

If you need to grab the output of the commands in the script use the directive "!output", the output will be saved on a
file called OutputReportMMDDYYYY.txt inside the directory /reports

If !output is present in the file before send commands to the device it will issue a "terminal length 0" command and
after sending all the commands in teh script it will issue a "terminal no length" command

Finish all the scripts with a "!"