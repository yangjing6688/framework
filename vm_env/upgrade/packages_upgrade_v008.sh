#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "6.0.0" ]
then
    echo "Install Curl"
    sudo apt install -y curl
    echo "Completed Installing Curl"

    echo "Installing Allure"
    curl -o allure-2.13.8.tgz -OLs https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz
    sudo tar -zxvf allure-2.13.8.tgz -C /opt/
    sudo ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure
    allure --version
    rm -rf allure-2.13.8.tgz
    echo "Completed installing Allure"

    echo "Update the VM Version"
    sed -i 's/6.0.0/8.0.0/g' /automation/version.txt
    more /automation/version.txt
    echo "Completed VM version update"
else
    echo "Skipping because of version"
    echo $line
fi
