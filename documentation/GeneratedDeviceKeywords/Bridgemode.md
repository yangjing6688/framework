# Keyword Library Documentation for Bridgemode
This feature is located in this file: `bridgemode.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: set_mode
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bridgemode.bridgemode_set_mode(device_name )

	Robot API Call: 

		bridgemode_set_mode  device_name  

UUID: 0aedb73e-9436-4b17-b1c4-79440118b1c8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set bridge mode {mode}

----------------------------------------------


## REST
## SNMP
# API Function: bridgemode_verify_customer_bridge
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bridgemode.bridgemode_verify_customer_bridge(device_name)

	Robot API Call: 

		bridgemode_verify_customer_bridge  device_name

# API Function: bridgemode_verify_provider_bridge
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bridgemode.bridgemode_verify_provider_bridge(device_name)

	Robot API Call: 

		bridgemode_verify_provider_bridge  device_name

