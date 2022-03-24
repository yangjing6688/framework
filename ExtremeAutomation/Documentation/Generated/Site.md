# Command Keyword Library Documentation for Site
This feature is located in this file: `site.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: site_verify_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.site.site_verify_exists(device_name, site_name)

	Robot API Call: 

		site_verify_exists  device_name  site_name

# API Function: site_verify_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.site.site_verify_does_not_exist(device_name, site_name)

	Robot API Call: 

		site_verify_does_not_exist  device_name  site_name

# API Function: site_verify_associated_ap_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.site.site_verify_associated_ap_exists(device_name, site_name, ap_name)

	Robot API Call: 

		site_verify_associated_ap_exists  device_name  site_name  ap_name

# API Function: site_verify_associated_ap_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.site.site_verify_associated_ap_does_not_exist(device_name, site_name, ap_name)

	Robot API Call: 

		site_verify_associated_ap_does_not_exist  device_name  site_name  ap_name

# API Function: site_verify_dns_server_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.site.site_verify_dns_server_exists(device_name, site_name, dns_server)

	Robot API Call: 

		site_verify_dns_server_exists  device_name  site_name  dns_server

# API Function: site_verify_dns_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.site.site_verify_dns_server_does_not_exist(device_name, site_name, dns_server)

	Robot API Call: 

		site_verify_dns_server_does_not_exist  device_name  site_name  dns_server

# API Function: site_verify_associated_wlan_radio_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.site.site_verify_associated_wlan_radio_exists(device_name, site_name, wlan_name, radio_mode)

	Robot API Call: 

		site_verify_associated_wlan_radio_exists  device_name  site_name  wlan_name  radio_mode

