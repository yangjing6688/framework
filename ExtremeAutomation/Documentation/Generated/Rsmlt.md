# Command Keyword Library Documentation for Rsmlt
This feature is located in this file: `rsmlt.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable_edge_support
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.rsmlt.rsmlt_enable_edge_support(device_name )

	Robot API Call: 

		rsmlt_enable_edge_support  device_name  

UUID: 1cd191b8-4663-4daf-a172-43367ef3f08a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip rsmlt edge-support

----------------------------------------------


## REST
## SNMP
# API Function: disable_edge_support
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.rsmlt.rsmlt_disable_edge_support(device_name )

	Robot API Call: 

		rsmlt_disable_edge_support  device_name  

UUID: 55d26d95-87cf-4f12-a0ad-ba272e1ba705
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip rsmlt edge-support

----------------------------------------------


## REST
## SNMP
# API Function: enable_vlan_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.rsmlt.rsmlt_enable_vlan_interface(device_name )

	Robot API Call: 

		rsmlt_enable_vlan_interface  device_name  

UUID: 9a19e49e-ff41-4d35-bb56-b9af088a99e2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip rsmlt

----------------------------------------------


## REST
## SNMP
# API Function: disable_vlan_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.rsmlt.rsmlt_disable_vlan_interface(device_name )

	Robot API Call: 

		rsmlt_disable_vlan_interface  device_name  

UUID: ccff1e1c-83e4-4033-a8e2-02920585166c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip rsmlt

----------------------------------------------


## REST
## SNMP
# API Function: set_interface_holddown_timer
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.rsmlt.rsmlt_set_interface_holddown_timer(device_name )

	Robot API Call: 

		rsmlt_set_interface_holddown_timer  device_name  

UUID: 0096a4a2-a456-4713-8e24-8b0c353a3126
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip rsmlt holddown-timer {timer}

----------------------------------------------


## REST
## SNMP
# API Function: set_interface_holdup_timer
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.rsmlt.rsmlt_set_interface_holdup_timer(device_name )

	Robot API Call: 

		rsmlt_set_interface_holdup_timer  device_name  

UUID: 1c71b9f6-7d6e-411a-bbed-3fbd81e8de87
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip rsmlt holdup-timer {timer}

----------------------------------------------


## REST
## SNMP
