# Command Keyword Library Documentation for Bgp
This feature is located in this file: `bgp.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_global(device_name )

	Robot API Call: 

		bgp_enable_global  device_name  

UUID: 864baf6b-abcf-47ba-920d-856bb640e79c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable bgp

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp {asnum} enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_global(device_name )

	Robot API Call: 

		bgp_disable_global  device_name  

UUID: fe9d5af9-a437-4627-9fd1-df444da0f44e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable bgp

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no router bgp enable

----------------------------------------------


## REST
## SNMP
# API Function: create_as
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_create_as(device_name )

	Robot API Call: 

		bgp_create_as  device_name  

UUID: 5cb85d69-e9d2-4cf9-a87f-ad9173289ac6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure bgp as-number {asnum}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp {asnum}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/config

----------------------------------------------


## SNMP
# API Function: delete_as
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_delete_as(device_name )

	Robot API Call: 

		bgp_delete_as  device_name  

UUID: 2844c681-6679-4646-a94e-570082c8b85e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no router bgp {asnum}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure bgp as-number 0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp 0

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/config

----------------------------------------------


## SNMP
# API Function: set_router_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_router_id(device_name, rtrid, asnum)

	Robot API Call: 

		bgp_set_router_id  device_name  rtrid  asnum

UUID: 0cd0af1c-15cd-4a39-bc11-154744a4f502
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		bgp router-id {rtrid}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure bgp routerid {rtrid}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||router-id {rtrid}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/config

----------------------------------------------


## SNMP
# API Function: clear_router_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_router_id(device_name )

	Robot API Call: 

		bgp_clear_router_id  device_name  

UUID: 45788698-c46e-40e7-804f-221a7536bf93
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no bgp router-id

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure bgp routerid 0.0.0.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||no router-id

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/config

----------------------------------------------


## SNMP
# API Function: create_neighbor
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_create_neighbor(device_name, ip, remoteas, asnum)

	Robot API Call: 

		bgp_create_neighbor  device_name  ip  remoteas  asnum

UUID: 157a36a7-b911-4e1b-a16b-04bb52abf727
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		neighbor {ip} remote-as {remoteas}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create bgp neighbor {ip} remote-as-number {remoteas}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||neighbor {ip}||neighbor {ip} remote-as {remoteas}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: post

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/neighbors

----------------------------------------------


## SNMP
# API Function: create_neighbor_link_local
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_create_neighbor_link_local(device_name, ip, remoteas, asnum, vlan_eos, vlan_exos)

	Robot API Call: 

		bgp_create_neighbor_link_local  device_name  ip  remoteas  asnum  vlan_eos  vlan_exos

UUID: 7123f5e3-13e7-435d-b9dd-eb43664b7af2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		neighbor {ip}%{vlan_eos} remote-as {remoteas}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create bgp neighbor {ip}%{vlan_exos} remote-as-number {remoteas}

----------------------------------------------


## REST
## SNMP
# API Function: delete_neighbor
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_delete_neighbor(device_name, ip, asnum, remoteas)

	Robot API Call: 

		bgp_delete_neighbor  device_name  ip  asnum  remoteas

UUID: be1c7911-d5ae-4de3-940f-639373cad108
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no neighbor {ip} remote-as {remoteas}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete bgp neighbor {ip}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||no neighbor {ip}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: delete

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={ip}

----------------------------------------------


## SNMP
# API Function: delete_neighbor_link_local
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_delete_neighbor_link_local(device_name, ip, remoteas, asnum)

	Robot API Call: 

		bgp_delete_neighbor_link_local  device_name  ip  remoteas  asnum

UUID: b4e67dba-f36a-4a65-b973-3eb7e1f02739
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no neighbor {ip}%{vlan_eos} remote-as {remoteas}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete bgp neighbor {ip}%{vlan_exos}

----------------------------------------------


## REST
## SNMP
# API Function: enable_neighbor
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_neighbor(device_name, ip, asnum)

	Robot API Call: 

		bgp_enable_neighbor  device_name  ip  asnum

UUID: 5af49855-d323-4e88-aafa-25023a8541b8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		neighbor {ip} enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable bgp neighbor {ip}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||neighbor {ip} enable

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={ip}/config

----------------------------------------------


## SNMP
# API Function: enable_neighbor_link_local
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_neighbor_link_local(device_name, ip, asnum, vlan_eos, vlan_exos)

	Robot API Call: 

		bgp_enable_neighbor_link_local  device_name  ip  asnum  vlan_eos  vlan_exos

UUID: 37fc30fe-c52f-49f3-8b4a-aea3c076c403
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		neighbor {ip}%{vlan_eos} enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable bgp neighbor {ip}%{vlan_exos}

----------------------------------------------


## REST
## SNMP
# API Function: disable_neighbor
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_neighbor(device_name, ip, asnum)

	Robot API Call: 

		bgp_disable_neighbor  device_name  ip  asnum

UUID: 402dd380-b0c2-48c8-87af-77d1b99d617c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no neighbor {ip} enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable bgp neighbor {ip}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||no neighbor {ip} enable

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={ip}/config

----------------------------------------------


## SNMP
# API Function: disable_neighbor_link_local
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_neighbor_link_local(device_name, ip, asnum, vlan_eos, vlan_exos)

	Robot API Call: 

		bgp_disable_neighbor_link_local  device_name  ip  asnum  vlan_eos  vlan_exos

UUID: 1fcb4eba-f5fd-4d60-aeb0-32781e3e5b3e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no neighbor {ip}%{vlan_eos} enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable bgp neighbor {ip}%{vlan_exos}

----------------------------------------------


## REST
## SNMP
# API Function: set_redistribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_redistribute(device_name, protocol, asnum)

	Robot API Call: 

		bgp_set_redistribute  device_name  protocol  asnum

UUID: fd5a6676-3d4c-491e-a842-3234fd0d3154
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		redistribute {protocol}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable bgp export {protocol}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||redistribute {protocol}

----------------------------------------------


## REST
## SNMP
# API Function: clear_redistribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_redistribute(device_name, protocol, asnum)

	Robot API Call: 

		bgp_clear_redistribute  device_name  protocol  asnum

UUID: 314c6f26-9895-43e9-be5e-17615b1f3175
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no redistribute {protocol}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable bgp export {protocol}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||no redistribute {protocol}

----------------------------------------------


## REST
## SNMP
# API Function: set_neighbor_password
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_neighbor_password(device_name, ip, password, asnum)

	Robot API Call: 

		bgp_set_neighbor_password  device_name  ip  password  asnum

UUID: e48b6513-3b98-4cef-b33a-b5d6ca8d9987
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerProtoPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: bgp||{asnum}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		neighbor {ip} remote-as {asnum} password {password}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure bgp neighbor {ip} password {password}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||neighbor password {ip} {password}

----------------------------------------------


## REST
## SNMP
# API Function: clear_neighbor
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_neighbor(device_name )

	Robot API Call: 

		bgp_clear_neighbor  device_name  

UUID: dfb7288b-7a76-4b56-b23a-2961325450f6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear bgp neighbor {ip}

----------------------------------------------


## REST
## SNMP
# API Function: clear_neighbor_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_neighbor_all(device_name )

	Robot API Call: 

		bgp_clear_neighbor_all  device_name  

UUID: bb8bbcc1-6f96-48d1-981b-71a6477fc46e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear bgp neighbor all

----------------------------------------------


## REST
## SNMP
# API Function: enable_neighbor_capability
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_neighbor_capability(device_name, ip, capability, family)

	Robot API Call: 

		bgp_enable_neighbor_capability  device_name  ip  capability  family

UUID: e813f686-694b-49ca-8f0e-9da4531f2500
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable bgp neighbor {ip} capability {family}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||neighbor {ip} {capability}

----------------------------------------------


## REST
## SNMP
# API Function: disable_neighbor_capability
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_neighbor_capability(device_name, ip, capability, family)

	Robot API Call: 

		bgp_disable_neighbor_capability  device_name  ip  capability  family

UUID: 69328593-da48-4fe0-8c82-2c2d9f5d5576
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable bgp neighbor {ip} capability {family}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router bgp||no neighbor {ip} {capability}

----------------------------------------------


## REST
## SNMP
# API Function: set_auto_peering
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_auto_peering(device_name )

	Robot API Call: 

		bgp_set_auto_peering  device_name  

UUID: 96ee215d-50e6-440e-a347-d9a7ccbfe4d7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create auto-peering bgp routerid {rtrid} AS-number {asnum}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/config

----------------------------------------------


## SNMP
# API Function: clear_auto_peering
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_auto_peering(device_name )

	Robot API Call: 

		bgp_clear_auto_peering  device_name  

UUID: 0e63e4bf-7d6e-48e6-b339-327cced65e43
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete auto-peering

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/config

----------------------------------------------


## SNMP
# API Function: set_confederation_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_confederation_id(device_name )

	Robot API Call: 

		bgp_set_confederation_id  device_name  

UUID: 56b7b4e4-d115-41a8-9b5a-1cf3ac47ad94
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/confederation

----------------------------------------------


## SNMP
# API Function: clear_confederation_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_confederation_id(device_name )

	Robot API Call: 

		bgp_clear_confederation_id  device_name  

UUID: 051db196-8dfc-4840-be89-fa99f9ca61e5
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/confederation

----------------------------------------------


## SNMP
# API Function: set_confederation_peer_member_as
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_confederation_peer_member_as(device_name )

	Robot API Call: 

		bgp_set_confederation_peer_member_as  device_name  

UUID: 96eb8a17-1ace-4fcf-b58a-c75e410d4b92
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/confederation

----------------------------------------------


## SNMP
# API Function: clear_confederation_peer_member_as
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_confederation_peer_member_as(device_name )

	Robot API Call: 

		bgp_clear_confederation_peer_member_as  device_name  

UUID: c3d4462c-2a2e-4547-bea4-fc58eddbbe42
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: put

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/confederation/config

----------------------------------------------


## SNMP
# API Function: set_graceful_restart_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_graceful_restart_time(device_name )

	Robot API Call: 

		bgp_set_graceful_restart_time  device_name  

UUID: d690b5e2-3703-4a8c-80ea-27b38fc15e2f
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart

----------------------------------------------


## SNMP
# API Function: clear_graceful_restart_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_graceful_restart_time(device_name )

	Robot API Call: 

		bgp_clear_graceful_restart_time  device_name  

UUID: 9961287f-3900-4d9c-a6e4-09a51eb3c8c2
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart

----------------------------------------------


## SNMP
# API Function: set_graceful_stale_route_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_graceful_stale_route_time(device_name )

	Robot API Call: 

		bgp_set_graceful_stale_route_time  device_name  

UUID: 01b06852-3823-406d-b0a0-069c255fa592
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart

----------------------------------------------


## SNMP
# API Function: clear_graceful_stale_route_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_graceful_stale_route_time(device_name )

	Robot API Call: 

		bgp_clear_graceful_stale_route_time  device_name  

UUID: c0977793-99ef-4c23-80e6-be1e01bcaae9
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart

----------------------------------------------


## SNMP
# API Function: set_maximum_paths
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_maximum_paths(device_name )

	Robot API Call: 

		bgp_set_maximum_paths  device_name  

UUID: 73d88e2b-4ab9-4c20-8666-b57e12edf42a
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/use-multiple-paths

----------------------------------------------


## SNMP
# API Function: clear_maximum_paths
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_clear_maximum_paths(device_name )

	Robot API Call: 

		bgp_clear_maximum_paths  device_name  

UUID: fe16fd98-d64b-4092-9ee8-874000a28cbb
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/use-multiple-paths

----------------------------------------------


## SNMP
# API Function: set_neighbor_keep_alive_interval_and_hold_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_neighbor_keep_alive_interval_and_hold_time(device_name )

	Robot API Call: 

		bgp_set_neighbor_keep_alive_interval_and_hold_time  device_name  

UUID: dc0b405a-d443-4301-9169-4f19b07ba9f8
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={neighbor_ip}/timers/config

----------------------------------------------


## SNMP
# API Function: set_neighbor_transport_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_set_neighbor_transport_address(device_name )

	Robot API Call: 

		bgp_set_neighbor_transport_address  device_name  

UUID: 4cb300fe-9d8c-44c9-a946-43e09ffffad8
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/neighbors/neighbor={neighbor_ip}/transport/config

----------------------------------------------


## SNMP
# API Function: enable_graceful_restart
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_graceful_restart(device_name )

	Robot API Call: 

		bgp_enable_graceful_restart  device_name  

UUID: e2b047db-b25b-4b3b-904e-c23fe06eb7ab
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart

----------------------------------------------


## SNMP
# API Function: disable_graceful_restart
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_graceful_restart(device_name )

	Robot API Call: 

		bgp_disable_graceful_restart  device_name  

UUID: 9a58f084-68ce-473a-9365-46d48f557c4e
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/graceful-restart

----------------------------------------------


## SNMP
# API Function: enable_allow_multiple_as
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_allow_multiple_as(device_name )

	Robot API Call: 

		bgp_enable_allow_multiple_as  device_name  

UUID: 81c07919-1e9a-4b95-935e-5cd04020fc21
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/use-multiple-paths/ebgp/config

----------------------------------------------


## SNMP
# API Function: disable_allow_multiple_as
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_allow_multiple_as(device_name )

	Robot API Call: 

		bgp_disable_allow_multiple_as  device_name  

UUID: d45a68c6-8ba2-4ea4-b35e-0d12d3f2e2ea
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/use-multiple-paths/ebgp/config

----------------------------------------------


## SNMP
# API Function: enable_always_compare_med
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_always_compare_med(device_name )

	Robot API Call: 

		bgp_enable_always_compare_med  device_name  

UUID: a6ffb1b3-0979-4a9f-8dae-e70f954b3e67
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/route-selection-options

----------------------------------------------


## SNMP
# API Function: disable_always_compare_med
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_always_compare_med(device_name )

	Robot API Call: 

		bgp_disable_always_compare_med  device_name  

UUID: 47a68d38-b0bd-435f-9e3a-86ff53391fad
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/route-selection-options

----------------------------------------------


## SNMP
# API Function: enable_advertise_inactive_routes_ipv4_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_advertise_inactive_routes_ipv4_unicast(device_name )

	Robot API Call: 

		bgp_enable_advertise_inactive_routes_ipv4_unicast  device_name  

UUID: c71e06f9-6800-4243-bdfe-1e442f6c830c
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/afi-safis

----------------------------------------------


## SNMP
# API Function: disable_advertise_inactive_routes_ipv4_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_advertise_inactive_routes_ipv4_unicast(device_name )

	Robot API Call: 

		bgp_disable_advertise_inactive_routes_ipv4_unicast  device_name  

UUID: 7b9be6d0-cdef-4956-8351-da0b428d7d26
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/afi-safis

----------------------------------------------


## SNMP
# API Function: enable_advertise_inactive_routes_l3vpn_ipv4_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_advertise_inactive_routes_l3vpn_ipv4_unicast(device_name )

	Robot API Call: 

		bgp_enable_advertise_inactive_routes_l3vpn_ipv4_unicast  device_name  

UUID: 65319d27-fffd-4045-b6ef-ad6640fc98c1
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/afi-safis

----------------------------------------------


## SNMP
# API Function: disable_advertise_inactive_routes_l3vpn_ipv4_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_advertise_inactive_routes_l3vpn_ipv4_unicast(device_name )

	Robot API Call: 

		bgp_disable_advertise_inactive_routes_l3vpn_ipv4_unicast  device_name  

UUID: 60264893-2a4c-440f-a750-0341f8074f45
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/afi-safis

----------------------------------------------


## SNMP
# API Function: enable_advertise_inactive_routes_ipv6_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_enable_advertise_inactive_routes_ipv6_unicast(device_name )

	Robot API Call: 

		bgp_enable_advertise_inactive_routes_ipv6_unicast  device_name  

UUID: fd87f773-188a-4066-8e95-48c9bebcd16d
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/afi-safis

----------------------------------------------


## SNMP
# API Function: disable_advertise_inactive_routes_ipv6_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_disable_advertise_inactive_routes_ipv6_unicast(device_name )

	Robot API Call: 

		bgp_disable_advertise_inactive_routes_ipv6_unicast  device_name  

UUID: a3b1620a-94c4-43fc-8238-bd410c4325b0
## CLI
## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-bgp:bgp/global/afi-safis

----------------------------------------------


## SNMP
# API Function: bgp_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_enabled(device_name)

	Robot API Call: 

		bgp_verify_enabled  device_name

# API Function: bgp_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_disabled(device_name)

	Robot API Call: 

		bgp_verify_disabled  device_name

# API Function: bgp_verify_as
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_as(device_name, asnum)

	Robot API Call: 

		bgp_verify_as  device_name  asnum

# API Function: bgp_verify_as_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_as_does_not_exist(device_name, asnum)

	Robot API Call: 

		bgp_verify_as_does_not_exist  device_name  asnum

# API Function: bgp_verify_routerid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_routerid(device_name, rtrid, asnum)

	Robot API Call: 

		bgp_verify_routerid  device_name  rtrid  asnum

# API Function: bgp_verify_routerid_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_routerid_does_not_exist(device_name, rtrid, asnum)

	Robot API Call: 

		bgp_verify_routerid_does_not_exist  device_name  rtrid  asnum

# API Function: bgp_verify_auto_peering
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_auto_peering(device_name, peering_value)

	Robot API Call: 

		bgp_verify_auto_peering  device_name  peering_value

# API Function: bgp_verify_auto_peering_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_auto_peering_disabled(device_name)

	Robot API Call: 

		bgp_verify_auto_peering_disabled  device_name

# API Function: bgp_verify_neighbor_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_neighbor_exists(device_name, ip, asnum)

	Robot API Call: 

		bgp_verify_neighbor_exists  device_name  ip  asnum

# API Function: bgp_verify_neighbor_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_neighbor_does_not_exist(device_name, ip, asnum)

	Robot API Call: 

		bgp_verify_neighbor_does_not_exist  device_name  ip  asnum

# API Function: bgp_verify_route_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_route_exists(device_name, route, nexthop, intf)

	Robot API Call: 

		bgp_verify_route_exists  device_name  route  nexthop  intf

# API Function: bgp_verify_route_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_route_does_not_exist(device_name, route, nexthop, intf)

	Robot API Call: 

		bgp_verify_route_does_not_exist  device_name  route  nexthop  intf

# API Function: bgp_verify_neighbor_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_neighbor_state(device_name, neighbor, state)

	Robot API Call: 

		bgp_verify_neighbor_state  device_name  neighbor  state

# API Function: bgp_verify_linklocal_neighbor_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_linklocal_neighbor_state(device_name, neighbor, vlan, state)

	Robot API Call: 

		bgp_verify_linklocal_neighbor_state  device_name  neighbor  vlan  state

# API Function: bgp_verify_confederation_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_confederation_id(device_name, confed_id)

	Robot API Call: 

		bgp_verify_confederation_id  device_name  confed_id

# API Function: bgp_verify_confederation_peer_member_as_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_confederation_peer_member_as_exists(device_name, peer, exists)

	Robot API Call: 

		bgp_verify_confederation_peer_member_as_exists  device_name  peer  exists

# API Function: bgp_verify_graceful_restart
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_graceful_restart(device_name, graceful_restart)

	Robot API Call: 

		bgp_verify_graceful_restart  device_name  graceful_restart

# API Function: bgp_verify_graceful_restart_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_graceful_restart_time(device_name, restart_time)

	Robot API Call: 

		bgp_verify_graceful_restart_time  device_name  restart_time

# API Function: bgp_verify_graceful_stale_route_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_graceful_stale_route_time(device_name, stale_route_time)

	Robot API Call: 

		bgp_verify_graceful_stale_route_time  device_name  stale_route_time

# API Function: bgp_verify_allow_multiple_as
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_allow_multiple_as(device_name, allow_multiple_as)

	Robot API Call: 

		bgp_verify_allow_multiple_as  device_name  allow_multiple_as

# API Function: bgp_verify_maximum_paths
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_maximum_paths(device_name, maximum_paths)

	Robot API Call: 

		bgp_verify_maximum_paths  device_name  maximum_paths

# API Function: bgp_verify_always_compare_med
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_always_compare_med(device_name, always_compare_med)

	Robot API Call: 

		bgp_verify_always_compare_med  device_name  always_compare_med

# API Function: bgp_verify_advertise_inactive_routes_ipv4_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_advertise_inactive_routes_ipv4_unicast(device_name, advertise_inactive_routes)

	Robot API Call: 

		bgp_verify_advertise_inactive_routes_ipv4_unicast  device_name  advertise_inactive_routes

# API Function: bgp_verify_advertise_inactive_routes_ipv6_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_advertise_inactive_routes_ipv6_unicast(device_name, advertise_inactive_routes)

	Robot API Call: 

		bgp_verify_advertise_inactive_routes_ipv6_unicast  device_name  advertise_inactive_routes

# API Function: bgp_verify_advertise_inactive_routes_l3vpn_ipv4_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_advertise_inactive_routes_l3vpn_ipv4_unicast(device_name, advertise_inactive_routes)

	Robot API Call: 

		bgp_verify_advertise_inactive_routes_l3vpn_ipv4_unicast  device_name  advertise_inactive_routes

# API Function: bgp_verify_neighbor_keep_alive_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_neighbor_keep_alive_time(device_name, neighbor_ip, keep_alive_interval)

	Robot API Call: 

		bgp_verify_neighbor_keep_alive_time  device_name  neighbor_ip  keep_alive_interval

# API Function: bgp_verify_neighbor_hold_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.bgp.bgp_verify_neighbor_hold_time(device_name, neighbor_ip, hold_time)

	Robot API Call: 

		bgp_verify_neighbor_hold_time  device_name  neighbor_ip  hold_time

