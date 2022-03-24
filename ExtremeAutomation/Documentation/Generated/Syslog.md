# Command Keyword Library Documentation for Syslog
This feature is located in this file: `syslog.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: syslog_verify_server_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.syslog.syslog_verify_server_exists(ip, port, server_facility, vr)

	Robot API Call: 

		syslog_verify_server_exists  ip  port  server_facility  vr

# API Function: syslog_verify_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.syslog.syslog_verify_server_does_not_exist(ip, port, server_facility, vr)

	Robot API Call: 

		syslog_verify_server_does_not_exist  ip  port  server_facility  vr

