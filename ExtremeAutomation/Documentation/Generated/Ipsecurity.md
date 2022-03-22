# Command Keyword Library Documentation for Ipsecurity
This feature is located in this file: `ipsecurity.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: set_trusted_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ipsecurity.ipsecurity_set_trusted_port(device_name )

	Robot API Call: 

		ipsecurity_set_trusted_port  device_name  

UUID: b9ac8cef-938a-42b2-9f7c-89f05e973036
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure trusted-port {port} trust-for dhcp-server

----------------------------------------------


## REST
## SNMP
# API Function: enable_dhcp_snooping
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ipsecurity.ipsecurity_enable_dhcp_snooping(device_name, vlan, ports, violation_action, snmp_trap, block, duration)

	Robot API Call: 

		ipsecurity_enable_dhcp_snooping  device_name  vlan  ports  violation_action  snmp_trap  block  duration

UUID: 47d790b4-9278-4c6b-840b-cc492b777005
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable ip-security dhcp-snooping vlan {vlan} ports {ports} violation-action {violation_action} {<api_utils.exos_ipsec_trap>snmp_trap} {block} {<api_utils.exos_ipsec_duration>duration.snmp_trap.block}

----------------------------------------------


## REST
## SNMP
# API Function: disable_dhcp_snooping
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ipsecurity.ipsecurity_disable_dhcp_snooping(device_name, vlan, ports)

	Robot API Call: 

		ipsecurity_disable_dhcp_snooping  device_name  vlan  ports

UUID: 57f8930a-0e61-4148-a03c-10a9c233593c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable ip-security dhcp-snooping vlan {vlan} ports {ports}

----------------------------------------------


## REST
## SNMP
