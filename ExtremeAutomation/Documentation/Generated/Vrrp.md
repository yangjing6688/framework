# Keyword Library Documentation for Vrrp
This feature is located in this file: `vrrp.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_enable_global(device_name )

	Robot API Call: 

		vrrp_enable_global  device_name  

UUID: c223e23c-297b-49fe-9326-77ddc3aa2697
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable vrrp

----------------------------------------------


## REST
## SNMP
# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_disable_global(device_name )

	Robot API Call: 

		vrrp_disable_global  device_name  

UUID: a5e2343b-bd31-4eb9-ad6d-4859df19b1ed
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable vrrp

----------------------------------------------


## REST
## SNMP
# API Function: enable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_enable_vlan(device_name )

	Robot API Call: 

		vrrp_enable_vlan  device_name  

UUID: ebb63174-a777-4bf0-81ba-feaee1d47d0a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable vrrp vlan {vlan} vrid {vrid}

----------------------------------------------


## REST
## SNMP
# API Function: disable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_disable_vlan(device_name )

	Robot API Call: 

		vrrp_disable_vlan  device_name  

UUID: ef0bb4d4-408a-4fdd-a5f8-70749a0f4f6e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable vrrp vlan {vlan} vrid {vrid}

----------------------------------------------


## REST
## SNMP
# API Function: enable_vlan_fabric_routing
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_enable_vlan_fabric_routing(device_name )

	Robot API Call: 

		vrrp_enable_vlan_fabric_routing  device_name  

UUID: 1aea17a3-64f3-4174-9c57-46944575a884
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vrrp vlan {vlan} vrid {vrid} fabric-routing on

----------------------------------------------


## REST
## SNMP
# API Function: disable_vlan_fabric_routing
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_disable_vlan_fabric_routing(device_name )

	Robot API Call: 

		vrrp_disable_vlan_fabric_routing  device_name  

UUID: cd972247-68b0-4348-8f34-fa286fd19cc5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vrrp vlan {vlan} vrid {vrid} fabric-routing off

----------------------------------------------


## REST
## SNMP
# API Function: create_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_create_vlan(device_name )

	Robot API Call: 

		vrrp_create_vlan  device_name  

UUID: 95df1aca-795a-4b87-b1d4-a6bd1fafd49b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create vrrp vlan {vlan} vrid {vrid}

----------------------------------------------


## REST
## SNMP
# API Function: clear_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_clear_vlan(device_name )

	Robot API Call: 

		vrrp_clear_vlan  device_name  

UUID: 0d2169e2-7c17-4e23-ae3e-127676e1370e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete vrrp vlan {vlan} vrid {vrid}

----------------------------------------------


## REST
## SNMP
# API Function: create_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_create_group(device_name )

	Robot API Call: 

		vrrp_create_group  device_name  

UUID: 5a97b9ae-459b-4920-ad52-0e0022067e98
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create vrrp group {name}

----------------------------------------------


## REST
## SNMP
# API Function: clear_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_clear_group(device_name )

	Robot API Call: 

		vrrp_clear_group  device_name  

UUID: 5aaeb0e1-bfbf-47fd-b007-34a5ba7abb4c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete vrrp group {name}

----------------------------------------------


## REST
## SNMP
# API Function: set_vlan_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_set_vlan_priority(device_name, vlan, vrid, priority)

	Robot API Call: 

		vrrp_set_vlan_priority  device_name  vlan  vrid  priority

UUID: 6eba5c94-5f6a-4618-b15b-b1fd8780050d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vrrp vlan {vlan} vrid {vrid} priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: set_vlan_ipaddress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_set_vlan_ipaddress(device_name, vlan, vrid, ip)

	Robot API Call: 

		vrrp_set_vlan_ipaddress  device_name  vlan  vrid  ip

UUID: 059235e6-51ad-4ccf-a7c8-6d9d704244ef
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vrrp vlan {vlan} vrid {vrid} add {ip}

----------------------------------------------


## REST
## SNMP
# API Function: show_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_show_all(device_name )

	Robot API Call: 

		vrrp_show_all  device_name  

UUID: 2fbb4647-b867-4879-bf9f-2396a31f2f26
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vrrp

----------------------------------------------


## REST
## SNMP
# API Function: show_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_show_detail(device_name )

	Robot API Call: 

		vrrp_show_detail  device_name  

UUID: e0e5da77-7d20-4f32-bcb0-098d7d8738d1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vrrp detail

----------------------------------------------


## REST
## SNMP
# API Function: show_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_show_group(device_name )

	Robot API Call: 

		vrrp_show_group  device_name  

UUID: 30b95afc-6bb0-4b95-a010-98512a2f240f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vrrp group {name}

----------------------------------------------


## REST
## SNMP
# API Function: show_group_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_show_group_all(device_name )

	Robot API Call: 

		vrrp_show_group_all  device_name  

UUID: d6566d08-8827-4deb-9854-b0385e36eb25
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vrrp group

----------------------------------------------


## REST
## SNMP
# API Function: show_virtual_router
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_show_virtual_router(device_name )

	Robot API Call: 

		vrrp_show_virtual_router  device_name  

UUID: e7fa2cb7-bf6a-4545-9f3e-7ff0213ef03b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vrrp virtual-router {vr}

----------------------------------------------


## REST
## SNMP
# API Function: show_virtual_router_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_show_virtual_router_all(device_name )

	Robot API Call: 

		vrrp_show_virtual_router_all  device_name  

UUID: 6b1813fa-e46c-41a6-b598-3e95b2843322
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vrrp virtual-router

----------------------------------------------


## REST
## SNMP
# API Function: show_vr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_show_vr(device_name )

	Robot API Call: 

		vrrp_show_vr  device_name  

UUID: f4a84284-c695-4d6f-ac5e-6ec621e73fa9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vrrp vr {vr}

----------------------------------------------


## REST
## SNMP
# API Function: show_vr_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_show_vr_all(device_name )

	Robot API Call: 

		vrrp_show_vr_all  device_name  

UUID: 8c5cfc15-1800-42e6-8b4d-ffd299d703f8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vrrp vr

----------------------------------------------


## REST
## SNMP
# API Function: show_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrrp.vrrp_show_vlan(device_name )

	Robot API Call: 

		vrrp_show_vlan  device_name  

UUID: 4940f28d-6bef-432d-9160-a29a28c80b07
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vrrp vlan {vlan}

----------------------------------------------


## REST
## SNMP
