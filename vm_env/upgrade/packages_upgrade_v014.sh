#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "13.0.0" ]
then
   mkdir /automation/tests
   cd /automation/tests
   git clone git@github.com:extremenetworks/extreme_automation_tests.git
   export PYTHONPATH=$PYTHONPATH:/automation/tests/extreme_automation_tests

   echo "Please add the new extreme_automation_tests to pycharm projects by attaching it to the main project."

   echo "Update the VM Version"
   sed -i 's/13.0.0/14.0.0/g' /automation/version.txt
   more /automation/version.txt 
   echo "Completed VM version update"
else
    echo "Skipping because of version"
    echo $line
fi
