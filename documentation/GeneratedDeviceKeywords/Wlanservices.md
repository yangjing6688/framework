# Keyword Library Documentation for Wlanservices
This feature is located in this file: `wlanservices.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: wlanservices_verify_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.wlanservices.wlanservices_verify_exists(device_name, wlan_service_name)

	Robot API Call: 

		wlanservices_verify_exists  device_name  wlan_service_name

# API Function: wlanservices_verify_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.wlanservices.wlanservices_verify_does_not_exist(device_name, wlan_service_name)

	Robot API Call: 

		wlanservices_verify_does_not_exist  device_name  wlan_service_name

