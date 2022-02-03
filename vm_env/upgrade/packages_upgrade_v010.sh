#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "9.0.0" ]
then
    echo "Please configuration NIS support for the vm"
else
    echo "Skipping because of version"
    echo $line
fi
