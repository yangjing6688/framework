#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "15.0.0" ]
then
   cd /automation/tests
   git clone git@github.com:extremenetworks/extreme_automation_framework.git
   export PYTHONPATH=$PYTHONPATH:/automation/tests/extreme_automation_framework

   echo "Please add the new extreme_automation_framework to pycharm projects by attaching it to the main project."
   
   echo "Update the VM Version"
   sed -i 's/15.0.0/16.0.0/g' /automation/version.txt
   more /automation/version.txt 
   echo "Completed VM version update"
else
    echo "Skipping because of version"
    echo $line
fi