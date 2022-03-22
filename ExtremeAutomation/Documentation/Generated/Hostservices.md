# Command Keyword Library Documentation for Hostservices
This feature is located in this file: `hostservices.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable_sys_force_topology_ip_flag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostservices.hostservices_enable_sys_force_topology_ip_flag(device_name )

	Robot API Call: 

		hostservices_enable_sys_force_topology_ip_flag  device_name  

UUID: 44ae2093-7a32-4200-9f6b-c76d9048a8a8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		sys force-topology-ip-flag

----------------------------------------------


## REST
## SNMP
# API Function: disable_sys_force_topology_ip_flag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostservices.hostservices_disable_sys_force_topology_ip_flag(device_name )

	Robot API Call: 

		hostservices_disable_sys_force_topology_ip_flag  device_name  

UUID: 0ed942d2-10cd-489d-804e-4e0ff39a37e7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no sys force-topology-ip-flag

----------------------------------------------


## REST
## SNMP
# API Function: set_sys_clipid_topology_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostservices.hostservices_set_sys_clipid_topology_ip(device_name )

	Robot API Call: 

		hostservices_set_sys_clipid_topology_ip  device_name  

UUID: 7dafa48c-20c4-4179-9a54-b6f6cc54e735
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		sys clipId-topology-ip {clip_id}

----------------------------------------------


## REST
## SNMP
# API Function: clear_sys_clipid_topology_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostservices.hostservices_clear_sys_clipid_topology_ip(device_name )

	Robot API Call: 

		hostservices_clear_sys_clipid_topology_ip  device_name  

UUID: ee66147e-6a71-43b9-b73a-4cd7defa0dc7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no sys clipId-topology-ip

----------------------------------------------


## REST
## SNMP
