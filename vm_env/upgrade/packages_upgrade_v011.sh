#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "10.0.0" ]
then
    echo "Please Reconfigured PyCharm to load the extAuto libraries for the vm (delete and reload both extAuto and cwautomation and attach them to the current project) also updated the setup.py to support ed25519 keys."

    echo "Update the VM Version"
    sed -i 's/10.0.0/11.0.0/g' /automation/version.txt
    more /automation/version.txt
    echo "Completed VM version update"
else
    echo "Skipping because of version"
    echo $line
fi
