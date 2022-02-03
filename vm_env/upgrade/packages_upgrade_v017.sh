#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "16.0.0" ]
then
   cd /automation/tests
   git clone git@github.com:extremenetworks/extreme_automation_framework.git
   export PYTHONPATH=$PYTHONPATH:/automation/extreme_automation_framework/extauto:/automation/extreme_automation_framework
   
   echo "Update the VM Version"
   sed -i 's/16.0.0/17.0.0/g' /automation/version.txt
   more /automation/version.txt 
   echo "Completed VM version update"
else
    echo "Skipping because of version"
    echo $line
fi