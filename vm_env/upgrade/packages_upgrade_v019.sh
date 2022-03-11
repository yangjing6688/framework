#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "18.0.0" ]
then
   cd /automation/tests/extreme_automation_tests
   pip install -r requirements.txt
   
   echo "Update the VM Version"
   sed -i 's/18.0.0/19.0.0/g' /automation/version.txt
   more /automation/version.txt 
   echo "Completed VM version update"
else
    echo "Skipping because of version"
    echo $line
fi