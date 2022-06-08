#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "8.0.0" ]
then
    echo "Update the VM Version"
    sed -i 's/8.0.0/9.0.0/g' /automation/version.txt
    more /automation/version.txt
    echo "Completed VM version update"

else
    echo "Skipping because of version"
    echo $line
fi
