#!/bin/bash

cd /var/lib/jenkins/workspace/post_commit_unit_tests/ExtremeAutomation/Library/Utils/Siesta/

zip -r NetSightUtilities.zip NetSightInstaller.py NetSightResetRedeploy.py NetSightScriptCopy.py  NetSightLogCopy.py

mv NetSightUtilities.zip /var/www/html/files/DEV/NetSightUtilities.zip

mv NetSightStartupBatch.bat /var/www/html/files/DEV/NetSightStartupBatch.bat