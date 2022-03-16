#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "10.0.0" ]
then
    echo "Please Reconfigured PyCharm to load the extAuto libraries for the vm (delete and reload both extAuto and cwautomation and attach them to the current project) also updated the setup.py to support ed25519 keys."
else
    echo "Skipping because of version"
    echo $line
fi
