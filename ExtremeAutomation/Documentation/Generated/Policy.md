# Keyword Library Documentation for Policy
This feature is located in this file: `policy.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: set_invalid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_invalid(device_name, action)

	Robot API Call: 

		policy_set_invalid  device_name  action

UUID: cbba64d9-3e6c-4e38-a947-df6845f9dc8a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy invalid action {action}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy invalid action {action}

----------------------------------------------


## REST
## SNMP
# API Function: clear_invalid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_invalid(device_name )

	Robot API Call: 

		policy_clear_invalid  device_name  

UUID: c0534d4e-6503-4a62-92c8-60982adfafc0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy invalid action

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy invalid action

----------------------------------------------


## REST
## SNMP
# API Function: set_port_admin_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_port_admin_profile(device_name, port, admin_id)

	Robot API Call: 

		policy_set_port_admin_profile  device_name  port  admin_id

UUID: 7cc7e155-0479-484c-96ec-a8588b67f12b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy port {port} admin-id {admin_id}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy port {port} {admin_id}

----------------------------------------------


## REST
## SNMP
# API Function: clear_port_admin_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_port_admin_profile(device_name, port)

	Robot API Call: 

		policy_clear_port_admin_profile  device_name  port

UUID: 05bc86ba-7e7e-46e7-ad5d-01e6eb12d87a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule admin-profile port {port} port-string {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule admin-profile port {port} port-string {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_mac_source_admin_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_mac_source_admin_profile(device_name, mac_source, port, profile_id, mask)

	Robot API Call: 

		policy_set_mac_source_admin_profile  device_name  mac_source  port  profile_id  mask

UUID: 1149cd7c-a45b-4d67-9a92-9b766b3be7a4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule admin-profile macsource {mac_source} mask {mask} port-string {port} admin-pid {profile_id}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule admin-profile macsource {mac_source} mask {mask} port-string {port} admin-pid {profile_id}

----------------------------------------------


## REST
## SNMP
# API Function: clear_mac_source_admin_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_mac_source_admin_profile(device_name, mac_source, port, mask)

	Robot API Call: 

		policy_clear_mac_source_admin_profile  device_name  mac_source  port  mask

UUID: 4a52d2b0-4aa9-413e-81f8-8b5259a52e76
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule admin-profile macsource {mac_source} mask {mask} port-string {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule admin-profile macsource {mac_source} mask {mask} port-string {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile(device_name, profile_id)

	Robot API Call: 

		policy_set_profile  device_name  profile_id

UUID: 186cd3f0-1c59-4c01-8d30-3469e618861d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewBaseRolePrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create {profile_id}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_with_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_with_name(device_name, profile_id, name)

	Robot API Call: 

		policy_set_profile_with_name  device_name  profile_id  name

UUID: a71c0e31-e2b3-4feb-b96e-409c4b70e2a8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} name {name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} name {name}

----------------------------------------------


## REST
## SNMP
# API Function: clear_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_profile(device_name, profile_id)

	Robot API Call: 

		policy_clear_profile  device_name  profile_id

UUID: 1b24bfee-47d4-4044-9312-3a5f8306faf2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy profile {profile_id}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy profile {profile_id}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewBaseRolePrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete {profile_id}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_name(device_name, profile_id, name)

	Robot API Call: 

		policy_set_profile_name  device_name  profile_id  name

UUID: 8d888968-eb15-4d19-8b95-f841a428a8c0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} name {name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} name {name}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_pvid_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_pvid_status(device_name, profile_id,  status)

	Robot API Call: 

		policy_set_profile_pvid_status  device_name  profile_id   status

UUID: 1fd26716-ee6f-4975-8341-0f128761bb42
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} pvid-status {status}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} pvid-status {status}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_pvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_pvid(device_name, profile_id,  pvid)

	Robot API Call: 

		policy_set_profile_pvid  device_name  profile_id   pvid

UUID: 8158885c-d39e-4179-8e32-fe37aaef85da
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} pvid {pvid}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} pvid {pvid}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_cos_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_cos_status(device_name, profile_id,  status)

	Robot API Call: 

		policy_set_profile_cos_status  device_name  profile_id   status

UUID: 0e7ef673-36cd-4430-b44e-cef0ca3cfe5d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} cos-status {status}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} cos-status {status}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_cos
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_cos(device_name, profile_id, cos_value)

	Robot API Call: 

		policy_set_profile_cos  device_name  profile_id  cos_value

UUID: 7ed1047d-4e70-4bf1-b876-8a528ae2d8ff
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} cos {cos_value}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} cos {cos_value}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewRolePrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		default-cos {cos_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_egress_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_egress_vlan(device_name, profile_id, vlan, append)

	Robot API Call: 

		policy_set_profile_egress_vlan  device_name  profile_id  vlan  append

UUID: 2df5030d-a802-4114-afd5-9a8438b02dc5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} {<api_utils.policy_vlan_append>append} egress-vlans {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} {<api_utils.policy_vlan_append>append} egress-vlans {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewRolePrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		egress-vlans enable {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_untagged_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_untagged_vlan(device_name, profile_id, vlan, append)

	Robot API Call: 

		policy_set_profile_untagged_vlan  device_name  profile_id  vlan  append

UUID: 37000051-e9e9-413a-8181-77f833f36cef
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} {<api_utils.policy_vlan_append>append} untagged-vlans {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} {<api_utils.policy_vlan_append>append} untagged-vlans {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_forbidden_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_forbidden_vlan(device_name, profile_id, vlan, append)

	Robot API Call: 

		policy_set_profile_forbidden_vlan  device_name  profile_id  vlan  append

UUID: 89b900e8-d445-4b48-8b0a-eb437c6cd184
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} {<api_utils.policy_vlan_append>append} forbidden-vlans {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} {<api_utils.policy_vlan_append>append} forbidden-vlans {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_tci_overwrite
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_tci_overwrite(device_name, profile_id,  status)

	Robot API Call: 

		policy_set_profile_tci_overwrite  device_name  profile_id   status

UUID: e5cc7a53-165c-4f27-83ba-f246fecb1a5e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} tci-overwrite {status}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} tci-overwrite {status}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_pvid_pvid_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_pvid_pvid_status(device_name, profile_id,  pvid,  pvid_status)

	Robot API Call: 

		policy_set_profile_pvid_pvid_status  device_name  profile_id   pvid   pvid_status

UUID: 53b7e3fe-5a56-4317-abfe-e0a3c34818e7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} pvid {pvid} pvid-status {pvid_status}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} pvid {pvid} pvid-status {pvid_status}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_untagged_pvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_untagged_pvid(device_name, profile_id,  pvid,  name,  vlan)

	Robot API Call: 

		policy_set_profile_untagged_pvid  device_name  profile_id   pvid   name   vlan

UUID: 9dcd19b0-ae53-4265-9de1-b3969bc333b6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_id} pvid {pvid} pvid-status enable name {name} untagged-vlans {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} pvid {pvid} pvid-status enable name {name} untagged-vlans {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule(device_name, profile_id,  options)

	Robot API Call: 

		policy_set_rule  device_name  profile_id   options

UUID: b6f4e66e-1598-4bf3-ad42-b0bf814bf9bd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} {options}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} {options}

----------------------------------------------


## REST
## SNMP
# API Function: clear_profile_rules
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_profile_rules(device_name, profile_id,  options)

	Robot API Call: 

		policy_clear_profile_rules  device_name  profile_id   options

UUID: 197a5c36-bac9-44be-a484-be9ecb69bbdc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} {options}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} {options}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ether
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ether(device_name, profile_id, ether_type, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ether  device_name  profile_id  ether_type  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 00dc62ac-48ee-43d1-9f2d-e641269cebb5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} ether {ether_type} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ether {ether_type} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ether
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ether(device_name, profile_id, ether_type, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ether  device_name  profile_id  ether_type  mask  port_string

UUID: a3ed88d2-6bfe-4a37-ae66-9c6bc359d155
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} ether {ether_type} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ether {ether_type} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ip6dest
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ip6dest(device_name, profile_id, ipv6_addr, l4_port, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ip6dest  device_name  profile_id  ipv6_addr  l4_port  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: b5a88d8d-6553-49ca-a2cc-44f8bc78d0fa
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} ip6dest {<api_utils.policy_gen_ip6dest>ipv6_addr.l4_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ip6dest {<api_utils.policy_gen_ip6dest>ipv6_addr.l4_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ip6dest
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ip6dest(device_name, profile_id, ipv6_addr, l4_port, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ip6dest  device_name  profile_id  ipv6_addr  l4_port  mask  port_string

UUID: 3d40333e-8cd9-4412-877a-b1c6beca869a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} ip6dest {<api_utils.policy_gen_ip6dest>ipv6_addr.l4_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ip6dest {<api_utils.policy_gen_ip6dest>ipv6_addr.l4_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipdestsocket
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipdestsocket(device_name, profile_id, ip_addr, l4_port, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipdestsocket  device_name  profile_id  ip_addr  l4_port  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 5b33c2df-1b7a-45d1-a4b9-36dd408479b8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} ipdestsocket {<api_utils.policy_gen_ipaddr>ip_addr.l4_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipdestsocket {<api_utils.policy_gen_ipaddr>ip_addr.l4_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipdestsocket
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipdestsocket(device_name, profile_id, ip_addr, l4_port, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipdestsocket  device_name  profile_id  ip_addr  l4_port  mask  port_string

UUID: 95004a55-e1c8-4123-8a49-ea9da45ffabb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} ipdestsocket {<api_utils.policy_gen_ipaddr>ip_addr.l4_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipdestsocket {<api_utils.policy_gen_ipaddr>ip_addr.l4_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipfrag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipfrag(device_name, profile_id, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipfrag  device_name  profile_id  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: df5ee88d-f686-4f49-8e83-20717c03414d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} ipfrag {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipfrag {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipfrag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipfrag(device_name, profile_id, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipfrag  device_name  profile_id  mask  port_string

UUID: fb57fc23-5306-453b-89ec-d01784c26e26
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} ipfrag {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipfrag {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipproto
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipproto(device_name, profile_id, ipproto, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipproto  device_name  profile_id  ipproto  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: b121e22f-f39a-4d29-9f27-24e52b0a34b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} ipproto {ipproto} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipproto {ipproto} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipproto
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipproto(device_name, profile_id, ip_proto, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipproto  device_name  profile_id  ip_proto  mask  port_string

UUID: 21ef32cc-449c-4473-9393-c90bf90fd5df
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} ipproto {ip_proto} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipproto {ip_proto} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipsourcesocket
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipsourcesocket(device_name, profile_id, ip_addr, l4_port, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipsourcesocket  device_name  profile_id  ip_addr  l4_port  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 47f84da2-31b0-4995-93cd-719fd56f9d95
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} ipsourcesocket {<api_utils.policy_gen_ipaddr>ip_addr.l4_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipsourcesocket {<api_utils.policy_gen_ipaddr>ip_addr.l4_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipsourcesocket
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipsourcesocket(device_name, profile_id, ip_addr, l4_port, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipsourcesocket  device_name  profile_id  ip_addr  l4_port  mask  port_string

UUID: 241d9ba8-b923-4685-bd9f-505489d1e170
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} ipsourcesocket {<api_utils.policy_gen_ipaddr>ip_addr.l4_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipsourcesocket {<api_utils.policy_gen_ipaddr>ip_addr.l4_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_iptos
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_iptos(device_name, profile_id, ip_tos, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_iptos  device_name  profile_id  ip_tos  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 498b751e-4e40-4fcf-9244-b62c85106bad
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} iptos {ip_tos} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} iptos {ip_tos} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_iptos
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_iptos(device_name, profile_id, ip_tos, mask, port_string)

	Robot API Call: 

		policy_clear_rule_iptos  device_name  profile_id  ip_tos  mask  port_string

UUID: 7ea42f76-f9d4-4eac-9f7d-c802d411dbde
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} iptos {ip_tos} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} iptos {ip_tos} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipttl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipttl(device_name, profile_id, ip_ttl, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipttl  device_name  profile_id  ip_ttl  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 15845486-fd51-4719-9681-962616403401
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} ipttl {ip_ttl} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipttl {ip_ttl} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipttl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipttl(device_name, profile_id, ip_ttl, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipttl  device_name  profile_id  ip_ttl  mask  port_string

UUID: 4565ecf5-cca2-4804-9135-f7c13485cb58
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} ipttl {ip_ttl} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipttl {ip_ttl} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_macdest
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_macdest(device_name, profile_id, mac_addr, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_macdest  device_name  profile_id  mac_addr  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: fcf4e5b4-cb65-4e83-96b1-652749767595
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} macdest {mac_addr} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} macdest {mac_addr} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_macdest
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_macdest(device_name, profile_id, mac_addr, mask, port_string)

	Robot API Call: 

		policy_clear_rule_macdest  device_name  profile_id  mac_addr  mask  port_string

UUID: 48e3bcd5-d239-444a-b804-0e1a80a99d08
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} macdest {mac_addr} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} macdest {mac_addr} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_macsource
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_macsource(device_name, profile_id, mac_addr, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_macsource  device_name  profile_id  mac_addr  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 05ed08cb-7843-4ce5-9402-e291469a6dac
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} macsource {mac_addr} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} macsource {mac_addr} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_macsource
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_macsource(device_name, profile_id, mac_addr, mask, port_string)

	Robot API Call: 

		policy_clear_rule_macsource  device_name  profile_id  mac_addr  mask  port_string

UUID: 6fa3f836-0f78-45c2-8f62-389d722b0ec5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} macsource {mac_addr} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} macsource {mac_addr} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_port(device_name, profile_id, port, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_port  device_name  profile_id  port  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: c6d16f77-2d5a-4ccb-9f92-5c4ae88b1202
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} port {port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} port {port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_port(device_name, profile_id, port, mask, port_string)

	Robot API Call: 

		policy_clear_rule_port  device_name  profile_id  port  mask  port_string

UUID: a3327bbf-b5a3-4f1e-9325-2a1ddb65138f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} port {port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} port {port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_tcpdestportip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_tcpdestportip(device_name, profile_id, tcp_port, ip_addr, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_tcpdestportip  device_name  profile_id  tcp_port  ip_addr  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: a3e4238e-1a35-4ce9-88cb-85e04170e482
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} tcpdestportip {<api_utils.policy_gen_tcpip>ip_addr.tcp_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} tcpdestportip {<api_utils.policy_gen_tcpip>ip_addr.tcp_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_tcpdestportip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_tcpdestportip(device_name, profile_id, tcp_port, ip_addr, mask, port_string)

	Robot API Call: 

		policy_clear_rule_tcpdestportip  device_name  profile_id  tcp_port  ip_addr  mask  port_string

UUID: 6e3721c8-8645-4899-b746-0e1d5f802195
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} tcpdestportip {<api_utils.policy_gen_tcpip>ip_addr.tcp_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} tcpdestportip {<api_utils.policy_gen_tcpip>ip_addr.tcp_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_tcpsourceportip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_tcpsourceportip(device_name, profile_id, tcp_port, ip_addr, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_tcpsourceportip  device_name  profile_id  tcp_port  ip_addr  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: a6f55f48-6dc0-4d77-97b4-172bf186e911
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} tcpsourceportip {<api_utils.policy_gen_tcpip>ip_addr.tcp_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} tcpsourceportip {<api_utils.policy_gen_tcpip>ip_addr.tcp_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_tcpsourceportip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_tcpsourceportip(device_name, profile_id, tcp_port, ip_addr, mask, port_string)

	Robot API Call: 

		policy_clear_rule_tcpsourceportip  device_name  profile_id  tcp_port  ip_addr  mask  port_string

UUID: 3b1c1584-9a85-4269-9e55-efac096723c4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} tcpsourceportip {<api_utils.policy_gen_tcpip>ip_addr.tcp_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} tcpsourceportip {<api_utils.policy_gen_tcpip>ip_addr.tcp_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_udpdestportip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_udpdestportip(device_name, profile_id, udp_port, ip_addr, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_udpdestportip  device_name  profile_id  udp_port  ip_addr  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 4449ead8-29c0-42bc-9634-4892b72c5fcd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} udpdestportip {<api_utils.policy_gen_tcpip>ip_addr.udp_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} udpdestportip {<api_utils.policy_gen_tcpip>ip_addr.udp_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_udpdestportip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_udpdestportip(device_name, profile_id, udp_port, ip_addr, mask, port_string)

	Robot API Call: 

		policy_clear_rule_udpdestportip  device_name  profile_id  udp_port  ip_addr  mask  port_string

UUID: 9c0a29d3-d851-4261-bbf7-4a81135446e8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} udpdestportip {<api_utils.policy_gen_tcpip>ip_addr.udp_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} udpdestportip {<api_utils.policy_gen_tcpip>ip_addr.udp_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_udpsourceportip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_udpsourceportip(device_name, profile_id, udp_port, ip_addr, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_udpsourceportip  device_name  profile_id  udp_port  ip_addr  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 35f5ab4b-f5d1-4bc4-be7a-7117ab47c080
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule {profile_id} udpsourceportip {<api_utils.policy_gen_tcpip>ip_addr.udp_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} udpsourceportip {<api_utils.policy_gen_tcpip>ip_addr.udp_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_udpsourceportip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_udpsourceportip(device_name, profile_id, udp_port, ip_addr, mask, port_string)

	Robot API Call: 

		policy_clear_rule_udpsourceportip  device_name  profile_id  udp_port  ip_addr  mask  port_string

UUID: 0ecb0b61-132c-412d-8321-0e15d66aec58
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy rule {profile_id} udpsourceportip {<api_utils.policy_gen_tcpip>ip_addr.udp_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} udpsourceportip {<api_utils.policy_gen_tcpip>ip_addr.udp_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_maptable_response
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_maptable_response(device_name )

	Robot API Call: 

		policy_set_maptable_response  device_name  

UUID: efe56dda-2ecc-4a1c-a6d3-27254842e983
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy maptable response {type}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy maptable response {type}

----------------------------------------------


## REST
## SNMP
# API Function: clear_maptable_response
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_maptable_response(device_name )

	Robot API Call: 

		policy_clear_maptable_response  device_name  

UUID: 68d2ad8d-f98f-4aa4-a719-6ca6c8774171
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy maptable response

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy maptable response

----------------------------------------------


## REST
## SNMP
# API Function: enable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_enable(device_name )

	Robot API Call: 

		policy_enable  device_name  

UUID: cda4d3d3-1e02-414c-8393-c8c81595f704
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable policy

----------------------------------------------


## REST
## SNMP
# API Function: disable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_disable(device_name )

	Robot API Call: 

		policy_disable  device_name  

UUID: 14033106-dd6a-4742-be0f-95de4284cf08
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable policy

----------------------------------------------


## REST
## SNMP
# API Function: set_vlanauthorization_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_vlanauthorization_state(device_name )

	Robot API Call: 

		policy_set_vlanauthorization_state  device_name  

UUID: 448045af-54a7-4217-8f8a-4aa53175f84e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy vlanauthorization {state}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_model_access_list
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_model_access_list(device_name )

	Robot API Call: 

		policy_set_rule_model_access_list  device_name  

UUID: e2a1fab3-273f-42d2-b308-281ce103a7f9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule-model access-list

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_model_hierarchical
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_model_hierarchical(device_name )

	Robot API Call: 

		policy_set_rule_model_hierarchical  device_name  

UUID: 20b65c48-acde-4718-b040-58a11ba07cf5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy rule-model hierarchical

----------------------------------------------


## REST
## SNMP
# API Function: set_access_list_profile_index
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list_profile_index(device_name, profile_index, list_name)

	Robot API Call: 

		policy_set_access_list_profile_index  device_name  profile_index  list_name

UUID: 96c9961e-89b9-453c-87a6-9c9a004605e6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_index} access-list {list_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_access_list_profile_none
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list_profile_none(device_name )

	Robot API Call: 

		policy_set_access_list_profile_none  device_name  

UUID: 71c4267e-2880-4fc4-bf2c-ea659db1fd3f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy profile {profile_index} access-list unassigned

----------------------------------------------


## REST
## SNMP
# API Function: set_access_list_profile_highest
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list_profile_highest(device_name )

	Robot API Call: 

		policy_set_access_list_profile_highest  device_name  

UUID: 30f0c730-1e43-4881-826a-2747adf81774
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy access-list profile highest-priority {list_name}.{rule}

----------------------------------------------


## REST
## SNMP
# API Function: set_access_list_profile_lowest
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list_profile_lowest(device_name )

	Robot API Call: 

		policy_set_access_list_profile_lowest  device_name  

UUID: 72a0ee34-e3ba-4769-81bd-9c6033ca4cc1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy access-list profile lowest-priority {list_name}.{rule}

----------------------------------------------


## REST
## SNMP
# API Function: set_access_list_rule_precedence_first
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list_rule_precedence_first(device_name )

	Robot API Call: 

		policy_set_access_list_rule_precedence_first  device_name  

UUID: e8082c13-8eca-4c72-89e9-0384ddd5e305
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy access-list rule-precedence {list_name}.{rule} first

----------------------------------------------


## REST
## SNMP
# API Function: set_access_list_rule_precedence_last
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list_rule_precedence_last(device_name )

	Robot API Call: 

		policy_set_access_list_rule_precedence_last  device_name  

UUID: 1c35d07c-08f3-4c16-8019-9c3faf18127c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy access-list rule-precedence {list_name}.{rule} last

----------------------------------------------


## REST
## SNMP
# API Function: set_access_list_rule_precedence_before
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list_rule_precedence_before(device_name, list1, rule1, list2, rule2)

	Robot API Call: 

		policy_set_access_list_rule_precedence_before  device_name  list1  rule1  list2  rule2

UUID: 5d2737f3-d279-48bf-b6c4-410c40864a09
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy access-list rule-precedence {list1}.{rule1} before {list2}.{rule2}

----------------------------------------------


## REST
## SNMP
# API Function: set_access_list_rule_precedence_after
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list_rule_precedence_after(device_name, list1, rule1, list2, rule2)

	Robot API Call: 

		policy_set_access_list_rule_precedence_after  device_name  list1  rule1  list2  rule2

UUID: 9026dadf-fad9-4e16-894f-e55ad622d846
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure policy access-list rule-precedence {list1}.{rule1} after {list2}.{rule2}

----------------------------------------------


## REST
## SNMP
# API Function: set_access_list
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list(device_name, list_name, rule, match_string, action_string)

	Robot API Call: 

		policy_set_access_list  device_name  list_name  rule  match_string  action_string

UUID: 1600e48f-bf9d-41cc-8168-6d1ba5587828
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create policy access-list {list_name}.{rule} matches {match_string} actions {action_string}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/ietf-access-control-list:acls

----------------------------------------------


## SNMP
# API Function: set_access_list_action_set
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_access_list_action_set(device_name, set_id, action_string)

	Robot API Call: 

		policy_set_access_list_action_set  device_name  set_id  action_string

UUID: efe6da8e-03d5-4654-8f8e-977a977510a8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create policy access-list action-set {set_id} {action_string}

----------------------------------------------


## REST
## SNMP
# API Function: clear_all_rules
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_all_rules(device_name )

	Robot API Call: 

		policy_clear_all_rules  device_name  

UUID: 538e5ddc-e2c8-4bd3-86bc-a1fb99a3af21
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure policy all-rules

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy all-rules

----------------------------------------------


## REST
## SNMP
# API Function: clear_access_list_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_access_list_all(device_name )

	Robot API Call: 

		policy_clear_access_list_all  device_name  

UUID: f16dcda3-7d22-4283-b09b-7402f8d1a03f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete policy access-list all-rules

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: delete

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/ietf-access-control-list:acls

----------------------------------------------


## SNMP
# API Function: clear_access_list
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_access_list(device_name )

	Robot API Call: 

		policy_clear_access_list  device_name  

UUID: 303ccc7d-9d3a-4fde-9337-319683debd11
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete policy access-list {list_name}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: delete

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/ietf-access-control-list:acls/acl={list_name}

----------------------------------------------


## SNMP
# API Function: clear_access_list_rule
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_access_list_rule(device_name )

	Robot API Call: 

		policy_clear_access_list_rule  device_name  

UUID: b7e80862-0e5e-4b80-b36e-8d276741a77f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete policy access-list {list_name}.{rule}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: delete

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/ietf-access-control-list:acls/acl={list_name}/aces/ace={rule}

----------------------------------------------


## SNMP
# API Function: clear_access_list_action_set
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_access_list_action_set(device_name )

	Robot API Call: 

		policy_clear_access_list_action_set  device_name  

UUID: ea3a4263-84d0-4e40-bff2-5cd51b294741
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete policy access-list action-set {set_id}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_precedence
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_precedence(device_name, profile_id, precedence)

	Robot API Call: 

		policy_set_profile_precedence  device_name  profile_id  precedence

UUID: bfd3bd78-7c3e-41f2-8e26-c1fd2435d5a5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} precedence {precedence}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_mirror_dest
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_mirror_dest(device_name, profile_id, index)

	Robot API Call: 

		policy_set_profile_mirror_dest  device_name  profile_id  index

UUID: 07de7f4b-c431-4105-8da7-84a787c2bd12
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} mirror-destination {index}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_syslog
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_syslog(device_name )

	Robot API Call: 

		policy_set_profile_syslog  device_name  

UUID: 5a3fac57-847b-4e3a-9dee-0f86709ab8b7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} syslog {state}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_trap(device_name )

	Robot API Call: 

		policy_set_profile_trap  device_name  

UUID: 256457b7-0d33-4d4a-9fa1-592345de38f6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} trap {state}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_disable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_disable_port(device_name )

	Robot API Call: 

		policy_set_profile_disable_port  device_name  

UUID: cf1aa1f0-1a6a-4a6f-bd64-eabb89fc654f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} disable-port {state}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_fst
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_fst(device_name, profile_id, index)

	Robot API Call: 

		policy_set_profile_fst  device_name  profile_id  index

UUID: 090f879d-7414-42f3-a552-27e15126c02f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} fst {index}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_web_redirect
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_web_redirect(device_name, profile_id, index)

	Robot API Call: 

		policy_set_profile_web_redirect  device_name  profile_id  index

UUID: d7557d56-5435-4ded-9d24-ca6fadbe08a2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy profile {profile_id} web-redirect {index}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_application
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_application(device_name, profile_id, application, application_type, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_application  device_name  profile_id  application  application_type  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: fa524d81-170b-44fc-9c88-9e8c378f7f52
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} application {application} {application_type} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_application
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_application(device_name, profile_id, application, application_type, mask, port_string)

	Robot API Call: 

		policy_clear_rule_application  device_name  profile_id  application  application_type  mask  port_string

UUID: fdcd9819-07d0-4da2-a8b2-d79c0ac2f0a8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} application {application} {application_type} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_icmp6type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_icmp6type(device_name, profile_id, icmp6type, icmp6code, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_icmp6type  device_name  profile_id  icmp6type  icmp6code  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: fcba0959-7643-460b-b132-16d2dde35319
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} icmp6type {<api_utils.policy_gen_icmp6>icmp6type.icmp6code} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_icmp6type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_icmp6type(device_name, profile_id, icmp6_type, icmp6_code, mask, port_string)

	Robot API Call: 

		policy_clear_rule_icmp6type  device_name  profile_id  icmp6_type  icmp6_code  mask  port_string

UUID: c239e306-7d15-4611-826a-7fd38a731cf5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} icmp6type {<api_utils.policy_gen_icmp6>icmp6_type.icmp6_code} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_icmptype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_icmptype(device_name, profile_id, icmptype, icmpcode, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_icmptype  device_name  profile_id  icmptype  icmpcode  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 5e4ea557-4950-4b71-9c20-3a43a0e3849f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} icmptype {<api_utils.policy_gen_icmp>icmptype.icmpcode} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_icmptype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_icmptype(device_name, profile_id, icmp_type, icmp_code, mask, port_string)

	Robot API Call: 

		policy_clear_rule_icmptype  device_name  profile_id  icmp_type  icmp_code  mask  port_string

UUID: af5fb0c8-8285-470a-a1ee-e5d6d440df6a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} icmptype {<api_utils.policy_gen_icmp>icmp_type.icmp_code} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ip6flowlabel
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ip6flowlabel(device_name, profile_id, ip6_flow_label, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ip6flowlabel  device_name  profile_id  ip6_flow_label  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: e5f1c36b-bcfe-4b13-b5f5-0d1a3308cbc2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ip6flowlabel {ip6_flow_label} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ip6flowlabel
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ip6flowlabel(device_name, profile_id, ip6_flow_label, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ip6flowlabel  device_name  profile_id  ip6_flow_label  mask  port_string

UUID: a2174339-6b3a-4367-b2cd-2e5ba72fdfe1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ip6flowlabel {ip6_flow_label} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ip6source
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ip6source(device_name, profile_id, ipv6_addr, l4_port, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ip6source  device_name  profile_id  ipv6_addr  l4_port  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: f4d89a0e-8b2e-4a07-862a-0238bd2febf5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ip6source {<api_utils.policy_gen_ip6dest>ipv6_addr.l4_port} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ip6source
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ip6source(device_name, profile_id, ipv6_addr, l4_port, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ip6source  device_name  profile_id  ipv6_addr  l4_port  mask  port_string

UUID: 16d20f97-556f-479d-8922-b363fc3cb3bc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ip6source {<api_utils.policy_gen_ip6dest>ipv6_addr.l4_port} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipxclass
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipxclass(device_name, profile_id, ipx_class, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipxclass  device_name  profile_id  ipx_class  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 4b7cbdc4-4522-4214-886c-b1185512998b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipxclass {ipx_class} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipxclass
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipxclass(device_name, profile_id, ipx_class, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipxclass  device_name  profile_id  ipx_class  mask  port_string

UUID: fa631379-9c32-4060-9807-25ea93ab4e4b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipxclass {ipx_class} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipxdest
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipxdest(device_name, profile_id, ipx_addr, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipxdest  device_name  profile_id  ipx_addr  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 75179bad-bb77-4bdf-97ab-56fd5531dc77
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipxdest {ipx_addr} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipxdest
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipxdest(device_name, profile_id, ipx_addr, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipxdest  device_name  profile_id  ipx_addr  mask  port_string

UUID: a2e72025-0ee1-41f2-a9ec-a30943fba1b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipxdest {ipx_addr} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipxdestsocket
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipxdestsocket(device_name, profile_id, ipx_socket, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipxdestsocket  device_name  profile_id  ipx_socket  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 01db00e6-9b07-4690-97eb-596c4e92aab2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipxdestsocket {ipx_socket} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipxdestsocket
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipxdestsocket(device_name, profile_id, ipx_socket, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipxdestsocket  device_name  profile_id  ipx_socket  mask  port_string

UUID: 9d3118bd-1002-4b7e-a815-b28d4bc033cd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipxdestsocket {ipx_socket} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipxsource
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipxsource(device_name, profile_id, ipx_addr, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipxsource  device_name  profile_id  ipx_addr  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 914b0351-2b35-4cc4-8c9a-dcbe13b583a9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipxsource {ipx_addr} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipxsource
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipxsource(device_name, profile_id, ipx_addr, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipxsource  device_name  profile_id  ipx_addr  mask  port_string

UUID: db18ee58-e235-491d-b8e0-af78803c07c4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipxsource {ipx_addr} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipxsourcesocket
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipxsourcesocket(device_name, profile_id, ipx_socket, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipxsourcesocket  device_name  profile_id  ipx_socket  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 32b8a6af-574e-4faf-940e-b9db30ea15cc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipxsourcesocket {ipx_socket} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipxsourcesocket
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipxsourcesocket(device_name, profile_id, ipx_socket, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipxsourcesocket  device_name  profile_id  ipx_socket  mask  port_string

UUID: e1518406-93ab-4025-8efa-197939be68cb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipxsourcesocket {ipx_socket} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_ipxtype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_ipxtype(device_name, profile_id, ipx_type, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_ipxtype  device_name  profile_id  ipx_type  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 34f0dd2c-57f4-43b6-a197-73d41a65126a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} ipxtype {ipx_type} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_ipxtype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_ipxtype(device_name, profile_id, ipx_type, mask, port_string)

	Robot API Call: 

		policy_clear_rule_ipxtype  device_name  profile_id  ipx_type  mask  port_string

UUID: c22d7e0a-2425-4f69-9db4-27ca2ae8cf1e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} ipxtype {ipx_type} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_llcdsapssap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_llcdsapssap(device_name, profile_id, llc_dsap_ssap, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_llcdsapssap  device_name  profile_id  llc_dsap_ssap  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: 82a219b6-f9e3-48e0-a2d8-1b3cafd60a7e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} llcdsapssap {llc_dsap_ssap} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_llcdsapssap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_llcdsapssap(device_name, profile_id, llc_dsap_ssap, mask, port_string)

	Robot API Call: 

		policy_clear_rule_llcdsapssap  device_name  profile_id  llc_dsap_ssap  mask  port_string

UUID: a4d02d47-eb78-4854-89b0-16508161dc20
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} llcdsapssap {llc_dsap_ssap} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_tci
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_tci(device_name, profile_id, tci_value, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_tci  device_name  profile_id  tci_value  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: b7bc6b10-59f5-4a0e-bafd-383c4d46e78b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} tci {tci_value} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_tci
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_tci(device_name, profile_id, tci_value, mask, port_string)

	Robot API Call: 

		policy_clear_rule_tci  device_name  profile_id  tci_value  mask  port_string

UUID: 1ebdd8b3-53a0-4840-bfdd-908d8462d991
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} tci {tci_value} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_vlantag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_vlantag(device_name, profile_id, vlan_tag, mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite, mirror_destination, syslog, trap, disable_port, quarantine_profile)

	Robot API Call: 

		policy_set_rule_vlantag  device_name  profile_id  vlan_tag  mask  port_string  storage_type  vlan  forward  drop  cos  tci_overwrite  mirror_destination  syslog  trap  disable_port  quarantine_profile

UUID: e9ea7542-fb2c-48d5-86b5-26f5a6f70e1f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set policy rule {profile_id} vlantag {vlan_tag} {<api_utils.policy_gen_rule>mask.port_string.storage_type.vlan.forward.drop.cos.tci_overwrite.mirror_destination.syslog.trap.disable_port.quarantine_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_vlantag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_vlantag(device_name, profile_id, vlan_tag, mask, port_string)

	Robot API Call: 

		policy_clear_rule_vlantag  device_name  profile_id  vlan_tag  mask  port_string

UUID: 5b5e373a-6d75-4e62-87fc-99cdbe34b1d7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear policy rule {profile_id} vlantag {vlan_tag} {<api_utils.policy_gen_rule_del>mask.port_string}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_access_control
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_access_control(device_name )

	Robot API Call: 

		policy_set_profile_access_control  device_name  

UUID: 58b7c94e-e02e-4ce8-be2a-34d987ec0667
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewRolePrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		access-control {state}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_traffic_mirror
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_profile_traffic_mirror(device_name )

	Robot API Call: 

		policy_set_profile_traffic_mirror  device_name  

UUID: 3444cb7b-7790-40a5-a7fa-bf6baeb90a70
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewRolePrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		traffic-mirror {mirror_state}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_l7
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_l7(device_name, profile_name, rule_id, group_name, app_name, in_filter_action, out_filter_action, access_control, cos_name, mirror_state)

	Robot API Call: 

		policy_set_rule_l7  device_name  profile_name  rule_id  group_name  app_name  in_filter_action  out_filter_action  access_control  cos_name  mirror_state

UUID: ce7cf52e-bbfa-4d6f-90bc-28ca12a83bbe
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewAcFiltersPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create {rule_id} app-signature group {group_name} name {app_name} in {in_filter_action} out {out_filter_action} {access_control} cos {cos_name} traffic-mirror {mirror_state}||apply {profile_name}

----------------------------------------------


## REST
## SNMP
# API Function: clear_rule_l7
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_clear_rule_l7(device_name )

	Robot API Call: 

		policy_clear_rule_l7  device_name  

UUID: 274f530c-7715-418e-932f-7482ad7cbf91
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewAcFiltersPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete {rule_id}||apply {profile_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_l7_configure
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_l7_configure(device_name )

	Robot API Call: 

		policy_set_rule_l7_configure  device_name  

UUID: 967f6656-1398-48ea-bcb6-c4e2e8c7186b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewAcFiltersPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		config {rule_id} app-signature group {group_name} name {app_name} in {in_filter_action} out {out_filter_action} {access_control} cos {cos_name} traffic-mirror {mirror_state}

----------------------------------------------


## REST
## SNMP
# API Function: set_rule_apply
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_set_rule_apply(device_name )

	Robot API Call: 

		policy_set_rule_apply  device_name  

UUID: 2f33e730-926b-4585-b011-2fa6537d21a6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: ewAcFiltersPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		apply {profile_name}

----------------------------------------------


## REST
## SNMP
# API Function: show_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_state(device_name )

	Robot API Call: 

		policy_show_state  device_name  

UUID: 871fd84a-db46-4ea5-931c-e4f4859c97d6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy state

----------------------------------------------


## REST
## SNMP
# API Function: show_map_response
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_map_response(device_name )

	Robot API Call: 

		policy_show_map_response  device_name  

UUID: 81343f8f-b126-4181-9d3e-53dfc8070538
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy maptable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy maptable

----------------------------------------------


## REST
## SNMP
# API Function: show_profiles
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_profiles(device_name )

	Robot API Call: 

		policy_show_profiles  device_name  

UUID: ee409148-6d7f-40cc-9ad6-33c490e4744b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy profile detail

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy profile -verbose

----------------------------------------------


## REST
## SNMP
# API Function: show_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_profile(device_name )

	Robot API Call: 

		policy_show_profile  device_name  

UUID: f4cc3445-c7d6-4131-9f3f-58f5aceb62c8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy profile {profile_index}

----------------------------------------------


## REST
## SNMP
# API Function: show_rules
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_rules(device_name )

	Robot API Call: 

		policy_show_rules  device_name  

UUID: e6c422c4-8307-4b49-800c-693b86ad4819
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy rule {rule_type} detail

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy rule {rule_type} -verbose

----------------------------------------------


## REST
## SNMP
# API Function: show_invalid_action
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_invalid_action(device_name )

	Robot API Call: 

		policy_show_invalid_action  device_name  

UUID: fb37f6cd-aa15-400c-b47b-6f1cf02e71c1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy invalid action

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy invalid action

----------------------------------------------


## REST
## SNMP
# API Function: show_vlanauthorization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_vlanauthorization(device_name )

	Robot API Call: 

		policy_show_vlanauthorization  device_name  

UUID: fc6bd614-b5b7-4624-ad95-62e32311bdee
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy vlanauthorization

----------------------------------------------


## REST
## SNMP
# API Function: show_allow_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_allow_type(device_name )

	Robot API Call: 

		policy_show_allow_type  device_name  

UUID: f09ee2b9-6d5c-40bd-8d6d-a2cb1ca2940f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy allowed-type {port} detail

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy allowed-type {port} -verbose

----------------------------------------------


## REST
## SNMP
# API Function: show_all_rules
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_all_rules(device_name )

	Robot API Call: 

		policy_show_all_rules  device_name  

UUID: 1fbc44c3-7b05-4234-b056-fc3bc876feeb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy rule detail

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy rule -verbose

----------------------------------------------


## REST
## SNMP
# API Function: show_all_profiles
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_all_profiles(device_name )

	Robot API Call: 

		policy_show_all_profiles  device_name  

UUID: 4cc7973d-623a-4ba9-a48a-3963adc44854
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy profile detail

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy profile -verbose

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		role show

----------------------------------------------


## REST
## SNMP
# API Function: show_rules_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_rules_profile(device_name )

	Robot API Call: 

		policy_show_rules_profile  device_name  

UUID: 5e757112-dbf2-46f6-98d3-c97d3966fcbe
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy rule profile-index {profile_id} detail

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy rule {profile_id} -verbose

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		role {profile_id} acfilters show

----------------------------------------------


## REST
## SNMP
# API Function: show_invalid_count
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_invalid_count(device_name )

	Robot API Call: 

		policy_show_invalid_count  device_name  

UUID: 4042d414-f795-40fe-ba31-5215c68b748b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy invalid count

----------------------------------------------


## REST
## SNMP
# API Function: show_admin_profiles
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_admin_profiles(device_name )

	Robot API Call: 

		policy_show_admin_profiles  device_name  

UUID: 35c5144b-815e-46b3-a13f-f07fee9e3557
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy rule admin-pid {profile_id} detail

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy rule admin-pid {profile_id} -verbose

----------------------------------------------


## REST
## SNMP
# API Function: show_access_list_rule_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_access_list_rule_name(device_name )

	Robot API Call: 

		policy_show_access_list_rule_name  device_name  

UUID: 352acacf-6fdb-4070-a7e3-0ef8baef9294
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy access-list {list_name}.{rule}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/ietf-access-control-list:acls/acl={list_name}/aces/ace={rule}

----------------------------------------------


## SNMP
# API Function: show_access_list_list_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_access_list_list_name(device_name )

	Robot API Call: 

		policy_show_access_list_list_name  device_name  

UUID: e5d08279-b58c-4b2f-9941-bec2c5f6bb66
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy access-list {list_name}

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/ietf-access-control-list:acls/acl={list_name}

----------------------------------------------


## SNMP
# API Function: show_access_list_action_set
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_access_list_action_set(device_name )

	Robot API Call: 

		policy_show_access_list_action_set  device_name  

UUID: 7d55818b-8301-4ef1-9574-0e6626056b81
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show policy access-list action-set {set_id}

----------------------------------------------


## REST
## SNMP
# API Function: show_profile_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.policy.policy_show_profile_detail(device_name )

	Robot API Call: 

		policy_show_profile_detail  device_name  

UUID: 49398e02-08d0-4cb0-997c-e333ac188cba
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		role {profile_name} show

----------------------------------------------


## REST
## SNMP
