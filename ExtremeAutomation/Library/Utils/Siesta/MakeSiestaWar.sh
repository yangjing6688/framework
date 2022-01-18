#!/bin/bash
# This script copies the necessary files to the siesta directory. Then generates a war file, moves it to
# the http file folder.

cd /var/lib/jenkins/workspace/post_commit_unit_tests/ExtremeAutomation/Library/Utils/Siesta/SiestaHarness/

cp harness.js /home/administrator/siesta/harness.js
cp harness_case.js /home/administrator/siesta/harness_case.js
cp index.html /home/administrator/siesta/index.html
cp EmcUtils.js /home/administrator/siesta/EmcUtils.js

cd /home/administrator/siesta/

jar -cvf robot_siesta.war *

mv robot_siesta.war /var/www/html/files/DEV/robot_siesta.war
