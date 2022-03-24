# Command Keyword Library Documentation for Vpex
This feature is located in this file: `vpex.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_enable_global(device_name )

	Robot API Call: 

		vpex_enable_global  device_name  

UUID: ad5e8fd5-07f8-4894-a55a-66207c4141ad
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable vpex

----------------------------------------------


## REST
## SNMP
# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_disable_global(device_name )

	Robot API Call: 

		vpex_disable_global  device_name  

UUID: 3a292f45-5876-478a-b74d-d77acdbb1899
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable vpex

----------------------------------------------


## REST
## SNMP
# API Function: enable_auto_configuration
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_enable_auto_configuration(device_name )

	Robot API Call: 

		vpex_enable_auto_configuration  device_name  

UUID: 457451ee-6dfc-4c54-8188-a8dd65cab4aa
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable vpex auto-configuration

----------------------------------------------


## REST
## SNMP
# API Function: disable_auto_configuration
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_disable_auto_configuration(device_name )

	Robot API Call: 

		vpex_disable_auto_configuration  device_name  

UUID: ac3de84b-ca95-4ade-ad84-d0a5ccce75ed
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable vpex auto-configuration

----------------------------------------------


## REST
## SNMP
# API Function: set_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_set_ports(device_name )

	Robot API Call: 

		vpex_set_ports  device_name  

UUID: fcd6f07b-9815-49cd-902c-8037df898def
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vpex ports {port} slot {slot}

----------------------------------------------


## REST
## SNMP
# API Function: clear_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_clear_ports(device_name )

	Robot API Call: 

		vpex_clear_ports  device_name  

UUID: c93965cf-c7c6-4699-a240-fb69d14c0e72
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure vpex ports {port} slot

----------------------------------------------


## REST
## SNMP
# API Function: set_ring_rebalancing_auto
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_set_ring_rebalancing_auto(device_name )

	Robot API Call: 

		vpex_set_ring_rebalancing_auto  device_name  

UUID: 38d8b33b-d2d7-4551-a008-af9dbcc390c4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vpex ring rebalancing auto

----------------------------------------------


## REST
## SNMP
# API Function: set_ring_rebalancing_off
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_set_ring_rebalancing_off(device_name )

	Robot API Call: 

		vpex_set_ring_rebalancing_off  device_name  

UUID: e86cc601-ec3c-4e0e-b84e-be7957d7bb7b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vpex ring rebalancing off

----------------------------------------------


## REST
## SNMP
# API Function: vpex_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_verify_enabled(device_name)

	Robot API Call: 

		vpex_verify_enabled  device_name

# API Function: vpex_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_verify_disabled(device_name)

	Robot API Call: 

		vpex_verify_disabled  device_name

