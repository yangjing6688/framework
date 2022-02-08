#!/bin/bash

line=$(head -n 1 /automation/version.txt)
if [ $line == "14.0.0" ]
then
    sudo apt-get install python3-tk
    wget https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip 
    unzip chromedriver_linux64.zip 
    sudo mv chromedriver /usr/local/bin/chromedriver 
    sudo chown root:root /usr/local/bin/chromedriver 
    sudo chmod +x /usr/local/bin/chromedriver 
    sudo rm chromedriver_linux64.zip

    pip install pysnmp
   

   echo "Update the VM Version"
   sed -i 's/14.0.0/15.0.0/g' /automation/version.txt
   more /automation/version.txt 
   echo "Completed VM version update"
else
    echo "Skipping because of version"
    echo $line
fi
