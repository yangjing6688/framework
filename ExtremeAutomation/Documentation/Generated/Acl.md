# Keyword Library Documentation for Acl
This feature is located in this file: `acl.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: create_ipv4
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_create_ipv4(device_name, name, acl_id, acl_type, voss_acl_type)

	Robot API Call: 

		acl_create_ipv4  device_name  name  acl_id  acl_type  voss_acl_type

UUID: 46cc1e09-b77a-48f3-b471-b0460b965a05
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip access-list {acl_type} {name}|| exit

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl {acl_id} type {voss_acl_type} name {name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.11.{acl_id}||1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.13.{acl_id}||1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.3.{acl_id}||1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.4.{acl_id}

----------------------------------------------


# API Function: create_ipv6
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_create_ipv6(device_name, name, acl_id, acl_type, voss_acl_type)

	Robot API Call: 

		acl_create_ipv6  device_name  name  acl_id  acl_type  voss_acl_type

UUID: 8d98c3b6-3c38-41de-bbb9-7665d4fac2b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ipv6 access-list {acl_type} {name}|| exit

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl {acl_id} type {voss_acl_type} name {name} pktType ipv6

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.11.{acl_id}||1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.13.{acl_id}||1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.3.{acl_id}||1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.4.{acl_id}

----------------------------------------------


# API Function: delete_list
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_delete_list(device_name, name, acl_id, acl_type, ip_ver)

	Robot API Call: 

		acl_delete_list  device_name  name  acl_id  acl_type  ip_ver

UUID: 3d235e88-a2c4-4f09-961c-98f0600ef260
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no {ip_ver} access-list {acl_type} {name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no filter acl {acl_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.11.{acl_id}

----------------------------------------------


# API Function: set_standard_rule
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_set_standard_rule(device_name )

	Robot API Call: 

		acl_set_standard_rule  device_name  

UUID: fda50222-0089-4331-b760-a0be89989052
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		{ip_ver} access-list {acl_type} {name}|| {rule_type} {rule_info}|| exit

----------------------------------------------


## REST
## SNMP
# API Function: create_ace_index
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_create_ace_index(device_name, ace_name, acl_id, ace_index)

	Robot API Call: 

		acl_create_ace_index  device_name  ace_name  acl_id  ace_index

UUID: 91b19841-d175-4715-ad5e-762434c6dd5d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl ace {acl_id} {ace_index} name {ace_name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.19.{acl_id}||1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.3.{acl_id}

----------------------------------------------


# API Function: delete_ace_index
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_delete_ace_index(device_name, acl_id, ace_index)

	Robot API Call: 

		acl_delete_ace_index  device_name  acl_id  ace_index

UUID: ca55a68a-e092-4462-aaf9-42ce02793795
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no filter acl ace {acl_id} {ace_index}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.19.{acl_id}

----------------------------------------------


# API Function: enable_list
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_enable_list(device_name )

	Robot API Call: 

		acl_enable_list  device_name  

UUID: 57cd5339-9aa3-4b16-aa0d-a71ca66ace9b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl {acl_id} enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.8.{acl_id}

----------------------------------------------


# API Function: disable_list
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_disable_list(device_name )

	Robot API Call: 

		acl_disable_list  device_name  

UUID: 71c6c544-fa88-4dfa-be7b-4e87198e029b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no filter acl {acl_id} enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.8.{acl_id}

----------------------------------------------


# API Function: enable_ace
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_enable_ace(device_name, acl_id, ace_index)

	Robot API Call: 

		acl_enable_ace  device_name  acl_id  ace_index

UUID: 40e17139-f478-436f-bd1f-e7b7e251d857
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl ace {acl_id} {ace_index} enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.10.{acl_id}.{ace_index}

----------------------------------------------


# API Function: disable_ace
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_disable_ace(device_name, acl_id, ace_index)

	Robot API Call: 

		acl_disable_ace  device_name  acl_id  ace_index

UUID: 40e579c3-0a1b-4785-bb42-0f0a7930cf04
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no filter acl ace {acl_id} {ace_index} enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.10.{acl_id}.{ace_index}

----------------------------------------------


# API Function: set_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_set_name(device_name, name, acl_id)

	Robot API Call: 

		acl_set_name  device_name  name  acl_id

UUID: aa86a026-8284-4fd1-97ce-9be9826d4c30
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl {acl_id} name {name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.3.{acl_id}

----------------------------------------------


# API Function: set_default_action
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_set_default_action(device_name )

	Robot API Call: 

		acl_set_default_action  device_name  

UUID: 54ea9fc0-1ca1-476f-94a2-dfa4525a4bf7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl set {acl_id} default-action {action}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.6.{acl_id}

----------------------------------------------


# API Function: set_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_set_port(device_name )

	Robot API Call: 

		acl_set_port  device_name  

UUID: 0a1fae24-2a56-4607-ab8e-108277703e4f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl port {acl_id} {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.10.{acl_id}

----------------------------------------------


# API Function: clear_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_clear_port(device_name )

	Robot API Call: 

		acl_clear_port  device_name  

UUID: ecc0cb15-cdbb-4731-84fd-f54bef2a7c4b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no filter acl port {acl_id} {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.10.{acl_id}

----------------------------------------------


# API Function: set_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_set_vlan(device_name )

	Robot API Call: 

		acl_set_vlan  device_name  

UUID: 6c9f011e-c993-455b-a448-1fd505c3f1b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl vlan {acl_id} {vlan}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.9.{acl_id}

----------------------------------------------


# API Function: clear_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_clear_vlan(device_name )

	Robot API Call: 

		acl_clear_vlan  device_name  

UUID: cf9d5686-2128-4a94-8eb8-d45aebd55127
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no filter acl vlan {acl_id} {vlan}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.3.1.1.9.{acl_id}

----------------------------------------------


# API Function: set_ace_action
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_set_ace_action(device_name, acl_id, ace_index, ace_action)

	Robot API Call: 

		acl_set_ace_action  device_name  acl_id  ace_index  ace_action

UUID: 57b9120e-fe78-4259-803c-c5596a9e132e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl ace action {acl_id} {ace_index} {ace_action}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.4.{acl_id}.{ace_index}

----------------------------------------------


# API Function: set_ace_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_set_ace_name(device_name, acl_id, ace_index, ace_name)

	Robot API Call: 

		acl_set_ace_name  device_name  acl_id  ace_index  ace_name

UUID: 60841625-fe68-45df-807c-962bac8724ac
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl ace {acl_id} {ace_index} name {ace_name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.4.1.1.3.{acl_id}.{ace_index}

----------------------------------------------


# API Function: set_ace_ethernet_ethertype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_set_ace_ethernet_ethertype(device_name, acl_id, ace_index, ace_ethertype)

	Robot API Call: 

		acl_set_ace_ethernet_ethertype  device_name  acl_id  ace_index  ace_ethertype

UUID: ce925b7f-3e77-40cf-91de-6d09c99de6cd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		filter acl ace ethernet {acl_id} {ace_index} ether-type eq {ace_ethertype}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.4.4.1.3.{acl_id}.{ace_index}||1.3.6.1.4.1.2272.1.202.1.1.2.4.4.1.6.{acl_id}.{ace_index}||1.3.6.1.4.1.2272.1.202.1.1.2.4.4.1.5.{acl_id}.{ace_index}

----------------------------------------------


# API Function: clear_ace_ethernet_ethertype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_clear_ace_ethernet_ethertype(device_name, acl_id, ace_index)

	Robot API Call: 

		acl_clear_ace_ethernet_ethertype  device_name  acl_id  ace_index

UUID: 3505b71e-e11c-4f18-9560-077cbd35dac8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no filter acl ace ethernet {acl_id} {ace_index} ether-type

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.202.1.1.2.4.4.1.6.{acl_id}.{ace_index}

----------------------------------------------


# API Function: acl_verify_ipv4_standard_list_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ipv4_standard_list_exists(device_name, acl_name, acl_id)

	Robot API Call: 

		acl_verify_ipv4_standard_list_exists  device_name  acl_name  acl_id

# API Function: acl_verify_ipv4_standard_list_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ipv4_standard_list_does_not_exist(device_name, acl_name, acl_id)

	Robot API Call: 

		acl_verify_ipv4_standard_list_does_not_exist  device_name  acl_name  acl_id

# API Function: acl_verify_ipv6_standard_list_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ipv6_standard_list_exists(device_name, acl_name, acl_id)

	Robot API Call: 

		acl_verify_ipv6_standard_list_exists  device_name  acl_name  acl_id

# API Function: acl_verify_ipv6_standard_list_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ipv6_standard_list_does_not_exist(device_name, acl_name, acl_id)

	Robot API Call: 

		acl_verify_ipv6_standard_list_does_not_exist  device_name  acl_name  acl_id

# API Function: acl_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_enabled(device_name, acl_id, acl_name)

	Robot API Call: 

		acl_verify_enabled  device_name  acl_id  acl_name

# API Function: acl_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_disabled(device_name, acl_id, acl_name)

	Robot API Call: 

		acl_verify_disabled  device_name  acl_id  acl_name

# API Function: acl_verify_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_name(device_name, acl_id, acl_name)

	Robot API Call: 

		acl_verify_name  device_name  acl_id  acl_name

# API Function: acl_verify_default_action
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_default_action(device_name, acl_id, acl_name, action)

	Robot API Call: 

		acl_verify_default_action  device_name  acl_id  acl_name  action

# API Function: acl_verify_port_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_port_exists(device_name, acl_name, acl_id, ports)

	Robot API Call: 

		acl_verify_port_exists  device_name  acl_name  acl_id  ports

# API Function: acl_verify_port_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_port_does_not_exist(device_name, acl_name, acl_id, ports)

	Robot API Call: 

		acl_verify_port_does_not_exist  device_name  acl_name  acl_id  ports

# API Function: acl_verify_vlan_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_vlan_exists(device_name, acl_name, acl_id, vlan)

	Robot API Call: 

		acl_verify_vlan_exists  device_name  acl_name  acl_id  vlan

# API Function: acl_verify_vlan_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_vlan_does_not_exist(device_name, acl_name, acl_id, vlan)

	Robot API Call: 

		acl_verify_vlan_does_not_exist  device_name  acl_name  acl_id  vlan

# API Function: acl_verify_ace_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ace_exists(device_name, ace_name, acl_id, ace_index)

	Robot API Call: 

		acl_verify_ace_exists  device_name  ace_name  acl_id  ace_index

# API Function: acl_verify_ace_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ace_does_not_exist(device_name, ace_name, acl_id, ace_index)

	Robot API Call: 

		acl_verify_ace_does_not_exist  device_name  ace_name  acl_id  ace_index

# API Function: acl_verify_ace_oper_up
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ace_oper_up(device_name, ace_name, acl_id, ace_index)

	Robot API Call: 

		acl_verify_ace_oper_up  device_name  ace_name  acl_id  ace_index

# API Function: acl_verify_ace_oper_down
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ace_oper_down(device_name, ace_name, acl_id, ace_index)

	Robot API Call: 

		acl_verify_ace_oper_down  device_name  ace_name  acl_id  ace_index

# API Function: acl_verify_ace_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ace_name(device_name, ace_name, acl_id, ace_index)

	Robot API Call: 

		acl_verify_ace_name  device_name  ace_name  acl_id  ace_index

# API Function: acl_verify_ace_action
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ace_action(device_name, ace_name, acl_id, ace_index, ace_action)

	Robot API Call: 

		acl_verify_ace_action  device_name  ace_name  acl_id  ace_index  ace_action

# API Function: acl_verify_ace_ethernet_ethertype_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ace_ethernet_ethertype_exists(device_name, ace_name, acl_id, ace_index, ace_ethertype)

	Robot API Call: 

		acl_verify_ace_ethernet_ethertype_exists  device_name  ace_name  acl_id  ace_index  ace_ethertype

# API Function: acl_verify_ace_ethernet_ethertype_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.acl.acl_verify_ace_ethernet_ethertype_does_not_exist(device_name, ace_name, acl_id, ace_index, ace_ethertype)

	Robot API Call: 

		acl_verify_ace_ethernet_ethertype_does_not_exist  device_name  ace_name  acl_id  ace_index  ace_ethertype

