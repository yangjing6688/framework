#!/bin/bash
cwd=$(pwd)
echo "Updating git to the lastest..."
cd /automation/econ/econ-automation-framework
git pull
cd /automation/econ/econ-automation-tests
git pull
cd /automation/xiq/cw_automation
git pull
cd /automation/xiq/extauto
git pull
cd /automation/econ/econ-automation-framework/vm_env
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
bash ./virtual_env_requirements.sh
