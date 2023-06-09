# Keyword Library Documentation for Gvrp
This feature is located in this file: `gvrp.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.gvrp.gvrp_enable_global(device_name )

	Robot API Call: 

		gvrp_enable_global  device_name  

UUID: 437c86c5-9308-4907-9309-0d6ff78d3aa3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set gvrp enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable mvrp

----------------------------------------------


## REST
## SNMP
# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.gvrp.gvrp_disable_global(device_name )

	Robot API Call: 

		gvrp_disable_global  device_name  

UUID: 95e010f0-7318-4337-a1bf-e683fe046832
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set gvrp disable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable mvrp

----------------------------------------------


## REST
## SNMP
# API Function: enable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.gvrp.gvrp_enable_port(device_name )

	Robot API Call: 

		gvrp_enable_port  device_name  

UUID: 35afdcac-f547-4240-a938-78a57d4cc55c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set gvrp enable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable mvrp ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.gvrp.gvrp_disable_port(device_name )

	Robot API Call: 

		gvrp_disable_port  device_name  

UUID: d0e8f204-ea0e-4e76-94e2-9180ad6c9850
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set gvrp disable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable mvrp ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: gvrp_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.gvrp.gvrp_verify_enabled(device_names)

	Robot API Call: 

		gvrp_verify_enabled  device_names

# API Function: gvrp_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.gvrp.gvrp_verify_disabled(device_names)

	Robot API Call: 

		gvrp_verify_disabled  device_names

# API Function: gvrp_verify_port_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.gvrp.gvrp_verify_port_enabled(device_names)

	Robot API Call: 

		gvrp_verify_port_enabled  device_names

# API Function: gvrp_verify_port_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.gvrp.gvrp_verify_port_disabled(device_names)

	Robot API Call: 

		gvrp_verify_port_disabled  device_names

