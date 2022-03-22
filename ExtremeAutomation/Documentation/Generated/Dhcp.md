# Command Keyword Library Documentation for Dhcp
This feature is located in this file: `dhcp.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_enable_vlan(device_name )

	Robot API Call: 

		dhcp_enable_vlan  device_name  

UUID: 95e41821-4973-49cf-8312-981cbb3160cf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable dhcp vlan {vlan_name}

----------------------------------------------


## REST
## SNMP
# API Function: disable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_disable_vlan(device_name )

	Robot API Call: 

		dhcp_disable_vlan  device_name  

UUID: 44395079-d9af-4809-ae6d-0cd93722f7b9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable dhcp vlan {vlan_name}

----------------------------------------------


## REST
## SNMP
# API Function: enable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_enable_port(device_name, vlan_name, port)

	Robot API Call: 

		dhcp_enable_port  device_name  vlan_name  port

UUID: 4dfb6620-78ca-4385-b300-b25861893a72
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable dhcp ports {port} vlan {vlan_name}

----------------------------------------------


## REST
## SNMP
# API Function: disable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_disable_port(device_name, vlan_name, port)

	Robot API Call: 

		dhcp_disable_port  device_name  vlan_name  port

UUID: 48ab5fcb-082d-4ed6-b33e-219920b3f1a7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable dhcp ports {port} vlan {vlan_name}

----------------------------------------------


## REST
## SNMP
# API Function: enable_bootprelay_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_enable_bootprelay_vlan(device_name )

	Robot API Call: 

		dhcp_enable_bootprelay_vlan  device_name  

UUID: 66669dfd-e515-42ed-96a3-a91040ab81f6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable bootprelay ipv4 vlan {vlan_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_address_range
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_set_address_range(device_name, vlan_name, start_addr, end_addr)

	Robot API Call: 

		dhcp_set_address_range  device_name  vlan_name  start_addr  end_addr

UUID: 751f49d4-8fd5-4a9d-b177-bcbf1e8110bc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-address-range {start_addr} - {end_addr}

----------------------------------------------


## REST
## SNMP
# API Function: set_lease_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_set_lease_time(device_name, vlan_name, seconds)

	Robot API Call: 

		dhcp_set_lease_time  device_name  vlan_name  seconds

UUID: 74c693f6-a9f6-4e2c-8218-412df2631e82
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-lease-timer {seconds}

----------------------------------------------


## REST
## SNMP
# API Function: set_netlogin_lease_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_set_netlogin_lease_time(device_name, vlan_name, seconds)

	Robot API Call: 

		dhcp_set_netlogin_lease_time  device_name  vlan_name  seconds

UUID: d708d78b-4f60-4f47-92d7-a8878f97c96f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} netlogin-lease-timer {seconds}

----------------------------------------------


## REST
## SNMP
# API Function: set_options_gateway
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_set_options_gateway(device_name, vlan_name, gateway_addr)

	Robot API Call: 

		dhcp_set_options_gateway  device_name  vlan_name  gateway_addr

UUID: c53e256f-6efa-4c43-9579-b21d3ba4885a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-options default-gateway {gateway_addr}

----------------------------------------------


## REST
## SNMP
# API Function: set_options_dns
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_set_options_dns(device_name, vlan_name, dns_addr)

	Robot API Call: 

		dhcp_set_options_dns  device_name  vlan_name  dns_addr

UUID: 1bf8479f-6b23-418a-b64e-c1b607df125c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-options dns-server {dns_addr}

----------------------------------------------


## REST
## SNMP
# API Function: set_options_dns_pri
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_set_options_dns_pri(device_name, vlan_name, dns_addr)

	Robot API Call: 

		dhcp_set_options_dns_pri  device_name  vlan_name  dns_addr

UUID: b0ea2231-5950-43d8-90ae-b0e5e4624b86
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-options dns-server primary {dns_addr}

----------------------------------------------


## REST
## SNMP
# API Function: set_options_dns_sec
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_set_options_dns_sec(device_name, vlan_name, dns_addr)

	Robot API Call: 

		dhcp_set_options_dns_sec  device_name  vlan_name  dns_addr

UUID: ba87f7ba-07a7-447a-b8af-8d07af7b304e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-options dns-server secondary {dns_addr}

----------------------------------------------


## REST
## SNMP
# API Function: set_bootprelay_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_set_bootprelay_ip(device_name )

	Robot API Call: 

		dhcp_set_bootprelay_ip  device_name  

UUID: b21625a1-7eb3-4836-b7e7-7aec620729d5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure bootprelay add {ip} vr {vr}

----------------------------------------------


## REST
## SNMP
# API Function: clear_address_range
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_clear_address_range(device_name )

	Robot API Call: 

		dhcp_clear_address_range  device_name  

UUID: fe3e3c6c-e698-4384-b64f-658b68054f92
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure vlan {vlan_name} dhcp-address-range

----------------------------------------------


## REST
## SNMP
# API Function: clear_lease_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_clear_lease_time(device_name )

	Robot API Call: 

		dhcp_clear_lease_time  device_name  

UUID: c56985ed-e4d9-4ac8-9ca4-cdb304e912af
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-lease-timer 300

----------------------------------------------


## REST
## SNMP
# API Function: clear_netlogin_lease_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_clear_netlogin_lease_time(device_name )

	Robot API Call: 

		dhcp_clear_netlogin_lease_time  device_name  

UUID: 26aa9bb0-58d7-42ac-88c0-5f3b7865ec4a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} netlogin-lease-timer 10

----------------------------------------------


## REST
## SNMP
# API Function: clear_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_clear_global(device_name )

	Robot API Call: 

		dhcp_clear_global  device_name  

UUID: 5a3dc96a-b3f5-4a95-bea8-20afd1a27e27
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure vlan {vlan_name} dhcp

----------------------------------------------


## REST
## SNMP
# API Function: clear_options_gateway
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_clear_options_gateway(device_name )

	Robot API Call: 

		dhcp_clear_options_gateway  device_name  

UUID: eb990672-d516-471d-bc82-0a79136bc4e8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure vlan {vlan_name} dhcp-options default-gateway

----------------------------------------------


## REST
## SNMP
# API Function: clear_options_dns
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_clear_options_dns(device_name )

	Robot API Call: 

		dhcp_clear_options_dns  device_name  

UUID: 92351040-86fd-471d-bcec-1eedb2b37967
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-options dns-server

----------------------------------------------


## REST
## SNMP
# API Function: clear_options_dns_pri
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_clear_options_dns_pri(device_name )

	Robot API Call: 

		dhcp_clear_options_dns_pri  device_name  

UUID: 9035ed79-1b7d-48cc-b525-f8ddf589e889
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-options dns-server primary

----------------------------------------------


## REST
## SNMP
# API Function: clear_options_dns_sec
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dhcp.dhcp_clear_options_dns_sec(device_name )

	Robot API Call: 

		dhcp_clear_options_dns_sec  device_name  

UUID: 4bce6caf-0ce0-41eb-afcd-39331cb4b12c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} dhcp-options dns-server secondary

----------------------------------------------


## REST
## SNMP
