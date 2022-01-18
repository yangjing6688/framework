echo "Update the Econ-Automation Vitrual Environment"
source /automation/econ/venv/bin/activate
pip install -r /automation/econ/econ-automation-tests/requirements.txt
pip list
deactivate
echo "Completed the Econ-Automation Vitrual Environment"


echo "Update the xiq automation Vitrual Environment"
source /automation/xiq/venv/bin/activate
pip install -r ./xiq_requirements.txt
pip list
deactivate
echo "Completed the xiq automation Vitrual Environment"
