# Keyword Library Documentation for Vxlan
This feature is located in this file: `vxlan.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: create_logical_switch
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vxlan.vxlan_create_logical_switch(device_name )

	Robot API Call: 

		vxlan_create_logical_switch  device_name  

UUID: 49ef7ff1-d0e9-413e-94e5-b70d34b9fb39
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set tunnel logical-switch create name {name}

----------------------------------------------


## REST
## SNMP
# API Function: delete_logical_switch
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vxlan.vxlan_delete_logical_switch(device_name )

	Robot API Call: 

		vxlan_delete_logical_switch  device_name  

UUID: 54da38b2-c9e7-4491-9394-2b20965d3a25
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear tunnel logical-switch name {name}

----------------------------------------------


## REST
## SNMP
# API Function: create_logical_switch_to_vni_map
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vxlan.vxlan_create_logical_switch_to_vni_map(device_name )

	Robot API Call: 

		vxlan_create_logical_switch_to_vni_map  device_name  

UUID: 9314a29d-4bc0-467a-a64e-be6a87d2314d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set tunnel map logical-switch {name} keyword {vni}

----------------------------------------------


## REST
## SNMP
# API Function: create_logical_switch_to_vlan_map
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vxlan.vxlan_create_logical_switch_to_vlan_map(device_name )

	Robot API Call: 

		vxlan_create_logical_switch_to_vlan_map  device_name  

UUID: cccd83dc-7199-466c-9d60-b2dfcc80bc2e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set tunnel map logical-switch {name} vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: create_logical_switch_vni_vlan_map
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vxlan.vxlan_create_logical_switch_vni_vlan_map(device_name )

	Robot API Call: 

		vxlan_create_logical_switch_vni_vlan_map  device_name  

UUID: 68836667-af69-476d-b61c-9b89159eb618
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set tunnel map logical-switch {name} keyword {vni} vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: set_remote_vtep
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vxlan.vxlan_set_remote_vtep(device_name, name, ip_address)

	Robot API Call: 

		vxlan_set_remote_vtep  device_name  name  ip_address

UUID: 103d42de-427b-4ab8-9ceb-efba0c3080df
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set tunnel remote-vtep logical-switch {name} ip-address {ip_address}

----------------------------------------------


## REST
## SNMP
# API Function: clear_remote_vtep
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vxlan.vxlan_clear_remote_vtep(device_name )

	Robot API Call: 

		vxlan_clear_remote_vtep  device_name  

UUID: c3a92a89-a07e-4647-8249-c73cf068ea7a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear tunnel remote-vtep logical-switch {name}

----------------------------------------------


## REST
## SNMP
# API Function: vxlan_verify_logical_switch_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vxlan.vxlan_verify_logical_switch_exists(device_name, name)

	Robot API Call: 

		vxlan_verify_logical_switch_exists  device_name  name

# API Function: vxlan_verify_logical_switch_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vxlan.vxlan_verify_logical_switch_does_not_exist(device_name, name)

	Robot API Call: 

		vxlan_verify_logical_switch_does_not_exist  device_name  name

