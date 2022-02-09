# Keyword Library Documentation for Ipsecurity
This feature is located in this file: `ipsecurity.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

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
# API Function: show_snooping_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ipsecurity.ipsecurity_show_snooping_vlan(device_name )

	Robot API Call: 

		ipsecurity_show_snooping_vlan  device_name  

UUID: 78dac202-30b3-4926-80fd-86573120adb6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip-security dhcp-snooping vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_snooping_vlan_entries
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ipsecurity.ipsecurity_show_snooping_vlan_entries(device_name )

	Robot API Call: 

		ipsecurity_show_snooping_vlan_entries  device_name  

UUID: 222cc1ba-091a-4eb0-8f5b-6e7d7521ad38
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip-security dhcp-snooping entries vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_snooping_vlan_violations
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ipsecurity.ipsecurity_show_snooping_vlan_violations(device_name )

	Robot API Call: 

		ipsecurity_show_snooping_vlan_violations  device_name  

UUID: 4e7517f1-29e4-4f7d-9803-de48ecc02914
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip-security dhcp-snooping violations vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_trusted_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ipsecurity.ipsecurity_show_trusted_ports(device_name )

	Robot API Call: 

		ipsecurity_show_trusted_ports  device_name  

UUID: c6308292-b9f3-4434-99fe-ed7d362d246d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show config | grep trusted

----------------------------------------------


## REST
## SNMP
