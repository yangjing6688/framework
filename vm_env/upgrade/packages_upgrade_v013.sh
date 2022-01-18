#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "12.0.0" ]
then
   echo "Install the VPN software for ubuntu if this VM is not run in the VPN."
   echo "Update the VM Version"
   sed -i 's/12.0.0/13.0.0/g' /automation/version.txt
   more /automation/version.txt 
   echo "Completed VM version update"
else
    echo "Skipping because of version"
    echo $line
fi
