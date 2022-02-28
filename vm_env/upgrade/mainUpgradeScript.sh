#!/bin/bash
cwd=$(pwd)
echo "Updating git to the lastest..."
cd /automation/tests/extreme_automation_tests
git checkout main
git pull
cd /automation/framework/extreme_automation_framework
git checkout main
git pull
echo "Completed updating git"
cd $cwd
bash ./packages_upgrade_v008.sh
bash ./packages_upgrade_v009.sh
bash ./packages_upgrade_v010.sh
bash ./packages_upgrade_v011.sh
bash ./packages_upgrade_v012.sh
bash ./packages_upgrade_v013.sh
bash ./packages_upgrade_v014.sh
bash ./packages_upgrade_v015.sh
bash ./packages_upgrade_v016.sh
bash ./packages_upgrade_v017.sh
bash ./packages_upgrade_v018.sh
