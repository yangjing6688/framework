#!/bin/bash

cd /var/lib/jenkins/workspace/post_commit_unit_tests/ExtremeAutomation/Library/Utils/Siesta/

zip -r RestServer.zip RestServer.py RestServerConfig.py ssl.key ssl.cert

mv RestServer.zip /var/www/html/files/DEV/RestServer.zip

mv RestServerStart.py /var/www/html/files/DEV/RestServerStart.py