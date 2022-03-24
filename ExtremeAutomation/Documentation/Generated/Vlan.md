# Command Keyword Library Documentation for Vlan
This feature is located in this file: `vlan.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: create_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_create_vlan(device_name, vlan)

	Robot API Call: 

		vlan_create_vlan  device_name  vlan

UUID: 2e07dc6a-2f52-4bdd-b814-6a3fd6afc666
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan create {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create vlan {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan create {vlan} type port-mstprstp 0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||exit

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: post

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-vlan:vlans

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SNAPROUTE

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: post

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /public/v1/config/Vlan

----------------------------------------------


## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.2.1.9.{vlan}||1.3.6.1.4.1.2272.1.3.2.1.10.{vlan}||1.3.6.1.4.1.2272.1.3.2.1.20.{vlan}

----------------------------------------------


# API Function: delete_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_delete_vlan(device_name, vlan)

	Robot API Call: 

		vlan_delete_vlan  device_name  vlan

UUID: eaccd886-b51c-409d-9daa-703133a964e5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear vlan {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete vlan {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan delete {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: topologyPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete {topology_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no vlan {vlan}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: delete

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-vlan:vlans/vlan={vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SNAPROUTE

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: delete

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /public/v1/config/Vlan

----------------------------------------------


## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.2.1.20.{vlan}

----------------------------------------------


# API Function: create_vman
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_create_vman(device_name, vman)

	Robot API Call: 

		vlan_create_vman  device_name  vman

UUID: 88e93a18-aa67-42a4-920c-03d4b57d43a5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan create {vman}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create vman {vman}

----------------------------------------------


## REST
## SNMP
# API Function: delete_vman
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_delete_vman(device_name, vman)

	Robot API Call: 

		vlan_delete_vman  device_name  vman

UUID: c1034622-3df6-43ac-bfa9-4cd8a7d15073
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear vlan {vman}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete vman {vman}

----------------------------------------------


## REST
## SNMP
# API Function: enable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_enable_vlan(device_name, vlan)

	Robot API Call: 

		vlan_enable_vlan  device_name  vlan

UUID: 8f1d1665-b71b-45ee-bcb3-062106d5c14e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan enable {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: disable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_disable_vlan(device_name, vlan)

	Robot API Call: 

		vlan_disable_vlan  device_name  vlan

UUID: 0e76a4c3-41d3-4405-a5c2-040c75793e40
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan disable {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: enable_dynamic_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_enable_dynamic_egress(device_name, vlan)

	Robot API Call: 

		vlan_enable_dynamic_egress  device_name  vlan

UUID: 25943c13-2b66-42fb-9a65-21c384ecdd57
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan dynamicegress {vlan} enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_dynamic_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_disable_dynamic_egress(device_name, vlan)

	Robot API Call: 

		vlan_disable_dynamic_egress  device_name  vlan

UUID: 688ba73b-d326-4b4e-8dea-ebd4fb7a260f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan dynamicegress {vlan} disable

----------------------------------------------


## REST
## SNMP
# API Function: set_egress_untagged
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_egress_untagged(device_name, vlan, port)

	Robot API Call: 

		vlan_set_egress_untagged  device_name  vlan  port

UUID: 1455236d-3899-476e-a333-93fcff7ed6ad
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan egress {vlan} {port} untagged

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan} add ports {port} untagged

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan ports {port} tagging tagAll||vlan members add {vlan} {port}||interface GigabitEthernet {port}||default-vlan-id {vlan}||untag-port-default-vlan enable||exit

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		switchport||switchport mode trunk||switchport trunk allowed vlan add {vlan}||switchport trunk native-vlan {vlan}||no switchport trunk tag native-vlan

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SNAPROUTE

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /public/v1/config/Vlan

----------------------------------------------


## SNMP
# API Function: set_egress_tagged
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_egress_tagged(device_name, vlan, port)

	Robot API Call: 

		vlan_set_egress_tagged  device_name  vlan  port

UUID: 8fb45945-51d5-43b8-b469-84d4cfc3f546
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan egress {vlan} {port} tagged

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan} add ports {port} tagged

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan ports {port} tagging tagAll||vlan members add {vlan} {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		switchport||switchport mode trunk||switchport trunk allowed vlan add {vlan}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SNAPROUTE

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /public/v1/config/Vlan

----------------------------------------------


## SNMP
# API Function: set_egress_forbidden
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_egress_forbidden(device_name, vlan, port)

	Robot API Call: 

		vlan_set_egress_forbidden  device_name  vlan  port

UUID: b75aade1-939c-4c43-b73d-c14250537fed
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan egress {vlan} {port} forbidden

----------------------------------------------


## REST
## SNMP
# API Function: clear_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_clear_egress  device_name  vlan  port

UUID: aaca0f2c-01a7-48d1-8b68-f113d9711a23
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear vlan egress {vlan} {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan} delete ports {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		switchport trunk allowed vlan remove {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: clear_egress_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_egress_type(device_name )

	Robot API Call: 

		vlan_clear_egress_type  device_name  

UUID: 51de2778-983c-462e-b205-29d1b6454bc6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear vlan egress {vlan} {port} {egress_type}

----------------------------------------------


## REST
## SNMP
# API Function: set_description
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_description(device_name, vlan, name)

	Robot API Call: 

		vlan_set_description  device_name  vlan  name

UUID: 5e31f606-0a42-473b-906e-651b1fdabebc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan name {vlan} "{name}"

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan} description "{name}"

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||description "{name}"||exit

----------------------------------------------


## REST
## SNMP
# API Function: clear_description
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_description(device_name )

	Robot API Call: 

		vlan_clear_description  device_name  

UUID: c5b9a551-a137-41af-aa7b-c283c9f9f12e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear vlan name {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure vlan {vlan} description

----------------------------------------------


## REST
## SNMP
# API Function: set_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_name(device_name, vlan, name)

	Robot API Call: 

		vlan_set_name  device_name  vlan  name

UUID: b5132db1-ed57-4b19-a129-13bf3cf6efbe
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set vlan name {vlan} "{name}"

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan} name "{name}"

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan name {vlan} {name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||name "{name}"||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.2.1.2.{vlan}

----------------------------------------------


# API Function: clear_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_name(device_name )

	Robot API Call: 

		vlan_clear_name  device_name  

UUID: a435b6bd-7aec-4705-81b0-af0bc59ffaeb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear vlan name {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: set_pvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_pvid(device_name, port, vlan, modify_egress)

	Robot API Call: 

		vlan_set_pvid  device_name  port  vlan  modify_egress

UUID: b4477fa8-5f9e-449e-bc9f-c88a87add7b6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port vlan {port} {vlan} {modify_egress}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		default-vlan-id {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		switchport trunk native-vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: clear_pvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_pvid(device_name, port)

	Robot API Call: 

		vlan_clear_pvid  device_name  port

UUID: 04479df7-6ad7-4db6-8410-9bda5e8458d9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear port vlan {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		default-vlan-id 1

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no switchport trunk native-vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: create_vlan_with_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_create_vlan_with_name(device_name, vlan, tag, topology_name, mode)

	Robot API Call: 

		vlan_create_vlan_with_name  device_name  vlan  tag  topology_name  mode

UUID: b86d2d18-f68a-4a9a-8ad1-1cdb08fe5b12
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create vlan {vlan} tag {tag}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: topologyPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create {topology_name} {mode} {vlan} {tag}

----------------------------------------------


## REST
## SNMP
# API Function: set_vman_egress_untagged
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_vman_egress_untagged(device_name, vman, port)

	Robot API Call: 

		vlan_set_vman_egress_untagged  device_name  vman  port

UUID: 04fbd352-383e-4c39-893e-dda530bd3503
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vman {vman} add ports {port} untagged

----------------------------------------------


## REST
## SNMP
# API Function: set_vman_egress_tagged
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_vman_egress_tagged(device_name, vman, port)

	Robot API Call: 

		vlan_set_vman_egress_tagged  device_name  vman  port

UUID: 407229d5-b7f8-4000-b3df-d72b175b5ff5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vman {vman} add ports {port} tagged

----------------------------------------------


## REST
## SNMP
# API Function: clear_vman_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_vman_egress(device_name, vman, port)

	Robot API Call: 

		vlan_clear_vman_egress  device_name  vman  port

UUID: 6a69ee23-2396-4360-84a1-a6e1ba89800a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vman {vman} delete ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_nsi
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_nsi(device_name, vlan, nsi)

	Robot API Call: 

		vlan_set_nsi  device_name  vlan  nsi

UUID: 610c3185-468f-4904-8271-907e501cf8cb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan} add nsi {nsi}

----------------------------------------------


## REST
## SNMP
# API Function: clear_nsi
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_nsi(device_name, vlan, nsi)

	Robot API Call: 

		vlan_clear_nsi  device_name  vlan  nsi

UUID: f0948db0-40b0-401c-ae27-1ec4f2b41dc1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan} delete nsi {nsi}

----------------------------------------------


## REST
## SNMP
# API Function: set_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_isid(device_name, vlan, i_sid)

	Robot API Call: 

		vlan_set_isid  device_name  vlan  i_sid

UUID: 294d7f0f-df09-4d6e-9270-7c0828f55389
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan} add isid {i_sid}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan i-sid {vlan} {i_sid}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.2.1.61.{vlan}

----------------------------------------------


# API Function: clear_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_isid(device_name, vlan, i_sid)

	Robot API Call: 

		vlan_clear_isid  device_name  vlan  i_sid

UUID: 46694b6b-a900-4efa-a601-ee598aa753ec
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan} delete isid {i_sid}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no vlan i-sid {vlan}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.2.1.61.{vlan}

----------------------------------------------


# API Function: create_spbm
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_create_spbm(device_name )

	Robot API Call: 

		vlan_create_spbm  device_name  

UUID: 6b27e129-327c-49c4-aab5-c2867715e0bd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan create {vlan} type spbm-bvlan

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.2.1.9.{vlan}||1.3.6.1.4.1.2272.1.3.2.1.10.{vlan}||1.3.6.1.4.1.2272.1.3.2.1.20.{vlan}

----------------------------------------------


# API Function: set_member
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_member(device_name )

	Robot API Call: 

		vlan_set_member  device_name  

UUID: c639c0ad-4fce-423f-ace9-15fe887fb325
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan members add {vlan} {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.2.1.11.{vlan}

----------------------------------------------


# API Function: clear_member
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_member(device_name )

	Robot API Call: 

		vlan_clear_member  device_name  

UUID: 2d7fb185-5133-4fb8-8d98-19e72eb05776
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan members remove {vlan} {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.2.1.11.{vlan}

----------------------------------------------


# API Function: set_port_encapsulation_dot1q
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_set_port_encapsulation_dot1q(device_name )

	Robot API Call: 

		vlan_set_port_encapsulation_dot1q  device_name  

UUID: 345acff8-3752-4fa5-bede-4a40de99cadf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		encapsulation dot1q

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.3.1.4.{port}

----------------------------------------------


# API Function: clear_port_encapsulation_dot1q
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_clear_port_encapsulation_dot1q(device_name )

	Robot API Call: 

		vlan_clear_port_encapsulation_dot1q  device_name  

UUID: 7c4d0acd-43c6-4374-9863-49b5ebaac0a2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no encapsulation dot1q

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.3.3.1.4.{port}

----------------------------------------------


# API Function: vlan_verify_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_exists(device_name, vlan)

	Robot API Call: 

		vlan_verify_exists  device_name  vlan

# API Function: vlan_verify_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_does_not_exist(device_name, vlan)

	Robot API Call: 

		vlan_verify_does_not_exist  device_name  vlan

# API Function: vlan_verify_vman_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_vman_exists(device_name, vman)

	Robot API Call: 

		vlan_verify_vman_exists  device_name  vman

# API Function: vlan_verify_vman_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_vman_does_not_exist(device_name, vman)

	Robot API Call: 

		vlan_verify_vman_does_not_exist  device_name  vman

# API Function: vlan_verify_port_on_untagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_on_untagged_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_on_untagged_egress  device_name  vlan  port

# API Function: vlan_verify_port_not_on_untagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_not_on_untagged_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_not_on_untagged_egress  device_name  vlan  port

# API Function: vlan_verify_port_not_on_operational_untagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_not_on_operational_untagged_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_not_on_operational_untagged_egress  device_name  vlan  port

# API Function: vlan_verify_port_on_tagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_on_tagged_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_on_tagged_egress  device_name  vlan  port

# API Function: vlan_verify_port_not_on_tagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_not_on_tagged_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_not_on_tagged_egress  device_name  vlan  port

# API Function: vlan_verify_port_not_on_operational_tagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_not_on_operational_tagged_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_not_on_operational_tagged_egress  device_name  vlan  port

# API Function: vlan_verify_port_on_forbidden_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_on_forbidden_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_on_forbidden_egress  device_name  vlan  port

# API Function: vlan_verify_port_on_static_forbidden_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_on_static_forbidden_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_on_static_forbidden_egress  device_name  vlan  port

# API Function: vlan_verify_port_on_static_untagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_on_static_untagged_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_on_static_untagged_egress  device_name  vlan  port

# API Function: vlan_verify_port_on_static_tagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_on_static_tagged_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_on_static_tagged_egress  device_name  vlan  port

# API Function: vlan_verify_port_not_on_static_tagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_not_on_static_tagged_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_not_on_static_tagged_egress  device_name  vlan  port

# API Function: vlan_verify_port_not_on_forbidden_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_not_on_forbidden_egress(device_name, vlan, port)

	Robot API Call: 

		vlan_verify_port_not_on_forbidden_egress  device_name  vlan  port

# API Function: vlan_verify_port_on_vman_untagged
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_on_vman_untagged(device_name, vman, port)

	Robot API Call: 

		vlan_verify_port_on_vman_untagged  device_name  vman  port

# API Function: vlan_verify_port_not_on_vman_untagged
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_not_on_vman_untagged(device_name, vman, port)

	Robot API Call: 

		vlan_verify_port_not_on_vman_untagged  device_name  vman  port

# API Function: vlan_verify_port_on_vman_tagged
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_on_vman_tagged(device_name, vman, port)

	Robot API Call: 

		vlan_verify_port_on_vman_tagged  device_name  vman  port

# API Function: vlan_verify_port_not_on_vman_tagged
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_not_on_vman_tagged(device_name, vman, port)

	Robot API Call: 

		vlan_verify_port_not_on_vman_tagged  device_name  vman  port

# API Function: vlan_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_enabled(device_name, vlan)

	Robot API Call: 

		vlan_verify_enabled  device_name  vlan

# API Function: vlan_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_disabled(device_name, vlan)

	Robot API Call: 

		vlan_verify_disabled  device_name  vlan

# API Function: vlan_verify_port_pvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_pvid(device_name, port, pvid)

	Robot API Call: 

		vlan_verify_port_pvid  device_name  port  pvid

# API Function: vlan_verify_port_does_not_have_pvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_does_not_have_pvid(device_name, port, pvid)

	Robot API Call: 

		vlan_verify_port_does_not_have_pvid  device_name  port  pvid

# API Function: vlan_verify_tag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_tag(device_name, vlan, tag)

	Robot API Call: 

		vlan_verify_tag  device_name  vlan  tag

# API Function: vlan_verify_tag_not_equal
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_tag_not_equal(device_name, vlan, tag)

	Robot API Call: 

		vlan_verify_tag_not_equal  device_name  vlan  tag

# API Function: vlan_verify_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_name(device_name, vlan, name)

	Robot API Call: 

		vlan_verify_name  device_name  vlan  name

# API Function: vlan_verify_name_is_not
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_name_is_not(device_name, vlan, name)

	Robot API Call: 

		vlan_verify_name_is_not  device_name  vlan  name

# API Function: vlan_verify_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_name_and_id(device_name, vlan_name)

	Robot API Call: 

		vlan_verify_name_and_id  device_name  vlan_name

# API Function: vlan_verify_description
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_description(device_name, vlan, description)

	Robot API Call: 

		vlan_verify_description  device_name  vlan  description

# API Function: vlan_verify_description_is_not
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_description_is_not(device_name, vlan, description)

	Robot API Call: 

		vlan_verify_description_is_not  device_name  vlan  description

# API Function: vlan_verify_port_tagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_tagged_egress(device_name, vlan)

	Robot API Call: 

		vlan_verify_port_tagged_egress  device_name  vlan

# API Function: vlan_verify_port_untagged_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_untagged_egress(device_name, vlan)

	Robot API Call: 

		vlan_verify_port_untagged_egress  device_name  vlan

# API Function: vlan_verify_isid_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_isid_exists(device_name, vlan, i_sid)

	Robot API Call: 

		vlan_verify_isid_exists  device_name  vlan  i_sid

# API Function: vlan_verify_isid_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_isid_does_not_exist(device_name, vlan, i_sid)

	Robot API Call: 

		vlan_verify_isid_does_not_exist  device_name  vlan  i_sid

# API Function: vlan_verify_nsi_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_nsi_exists(device_name, vlan, nsi)

	Robot API Call: 

		vlan_verify_nsi_exists  device_name  vlan  nsi

# API Function: vlan_verify_nsi_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_nsi_does_not_exist(device_name, vlan, nsi)

	Robot API Call: 

		vlan_verify_nsi_does_not_exist  device_name  vlan  nsi

# API Function: vlan_verify_port_encapsulation_dot1q
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_encapsulation_dot1q(device_name, port)

	Robot API Call: 

		vlan_verify_port_encapsulation_dot1q  device_name  port

# API Function: vlan_verify_port_encapsulation_not_dot1q
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_encapsulation_not_dot1q(device_name, port)

	Robot API Call: 

		vlan_verify_port_encapsulation_not_dot1q  device_name  port

# API Function: vlan_verify_port_is_member_of_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_is_member_of_vlan(device_name, ports, vlan)

	Robot API Call: 

		vlan_verify_port_is_member_of_vlan  device_name  ports  vlan

# API Function: vlan_verify_port_is_not_member_of_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vlan.vlan_verify_port_is_not_member_of_vlan(device_name, ports, vlan)

	Robot API Call: 

		vlan_verify_port_is_not_member_of_vlan  device_name  ports  vlan

