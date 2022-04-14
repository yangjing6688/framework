#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "11.0.0" ]
then
    sudo su
    echo "KexAlgorithms diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1" >>/etc/ssh/ssh_config.d/weak.conf
    echo "Please configuration VPN support for the vm: https://extremenetworks.service-now.com/kb_view.do?sysparm_article=KB0010650"

    echo "Update the VM Version"
    sed -i 's/11.0.0/12.0.0/g' /automation/version.txt
    more /automation/version.txt
    echo "Completed VM version update"
else
    echo "Skipping because of version"
    echo $line
fi
