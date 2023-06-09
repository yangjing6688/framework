# Keyword Library Documentation for Isis
This feature is located in this file: `isis.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_global(device_name )

	Robot API Call: 

		isis_enable_global  device_name  

UUID: 5e8b2b77-f570-4a1c-b139-c933c7547bd6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable isis

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1.1.8.0

----------------------------------------------


# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_global(device_name )

	Robot API Call: 

		isis_disable_global  device_name  

UUID: 695b2829-e1be-4156-878a-46a23c9ee9b9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable isis

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no router isis enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1.1.8.0

----------------------------------------------


# API Function: set_system_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_system_id(device_name )

	Robot API Call: 

		isis_set_system_id  device_name  

UUID: e822f7ac-4816-4653-9a92-8e9407962160
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||system-id {sys_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1.1.3.0

----------------------------------------------


# API Function: clear_system_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_system_id(device_name )

	Robot API Call: 

		isis_clear_system_id  device_name  

UUID: 7ea7fdb1-bfe2-42da-8034-04396957f7ba
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no system-id

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1.1.3.0

----------------------------------------------


# API Function: set_manual_area
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_manual_area(device_name )

	Robot API Call: 

		isis_set_manual_area  device_name  

UUID: f3d86c30-2ecd-4ce4-afca-1b3c59cb5757
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||manual-area {manual_area}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1.2.1.2.{manual_area}

----------------------------------------------


# API Function: clear_manual_area
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_manual_area(device_name )

	Robot API Call: 

		isis_clear_manual_area  device_name  

UUID: 9d3f74cd-aa7c-40a6-84dc-5090ab1821f3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no manual-area {manual_area}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1.2.1.2.{manual_area}

----------------------------------------------


# API Function: set_sys_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_sys_name(device_name )

	Robot API Call: 

		isis_set_sys_name  device_name  

UUID: 16686ac8-176a-40e9-9844-fade015600e5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||sys-name {name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.1.10.0

----------------------------------------------


# API Function: clear_sys_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_sys_name(device_name )

	Robot API Call: 

		isis_clear_sys_name  device_name  

UUID: 6ecbe2df-faf8-4ea0-b952-99405a04f618
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no sys-name

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.1.10.0

----------------------------------------------


# API Function: set_ipv4_source_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_ipv4_source_address(device_name )

	Robot API Call: 

		isis_set_ipv4_source_address  device_name  

UUID: 7e1e2500-a337-4c22-8923-6d86af2baa7d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||ip-source-address {ip}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.1.13.0

----------------------------------------------


# API Function: clear_ipv4_source_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_ipv4_source_address(device_name )

	Robot API Call: 

		isis_clear_ipv4_source_address  device_name  

UUID: f519f5e3-fea8-4b48-a10c-2b3c9d0a56b5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no ip-source-address||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.1.13.0

----------------------------------------------


# API Function: set_ipv6_source_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_ipv6_source_address(device_name )

	Robot API Call: 

		isis_set_ipv6_source_address  device_name  

UUID: 20b845c4-0d34-4048-9c90-f919c9ffd485
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||ipv6-source-address {ipv6_addr}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.1.15.0

----------------------------------------------


# API Function: clear_ipv6_source_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_ipv6_source_address(device_name )

	Robot API Call: 

		isis_clear_ipv6_source_address  device_name  

UUID: c95faa61-10c5-4f0b-a7fa-4e15cafab5c3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no ipv6-source-address||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.1.15.0

----------------------------------------------


# API Function: set_ipv4_tunnel_source_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_ipv4_tunnel_source_address(device_name )

	Robot API Call: 

		isis_set_ipv4_tunnel_source_address  device_name  

UUID: 496e1ece-fba0-4acf-8850-fdba99593a44
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||ip-tunnel-source-address {ip}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.1.17.0

----------------------------------------------


# API Function: clear_ipv4_tunnel_source_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_ipv4_tunnel_source_address(device_name )

	Robot API Call: 

		isis_clear_ipv4_tunnel_source_address  device_name  

UUID: 76e25363-c4ea-4d8a-9bab-e8b73138b869
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no ip-tunnel-source-address||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.1.17.0

----------------------------------------------


# API Function: set_inband_mgmt_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_inband_mgmt_ip(device_name )

	Robot API Call: 

		isis_set_inband_mgmt_ip  device_name  

UUID: b198e339-a35f-460e-bb1d-e33b67b27722
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||inband-mgmt-ip {ip}

----------------------------------------------


## REST
## SNMP
# API Function: clear_inband_mgmt_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_inband_mgmt_ip(device_name )

	Robot API Call: 

		isis_clear_inband_mgmt_ip  device_name  

UUID: a3ba0f4b-ca67-4422-89f9-2c20e76f61dc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no inband-mgmt-ip

----------------------------------------------


## REST
## SNMP
# API Function: set_metric_narrow
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_metric_narrow(device_name )

	Robot API Call: 

		isis_set_metric_narrow  device_name  

UUID: 1c5d648c-872d-43e8-b429-933c306cc815
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||metric narrow

----------------------------------------------


## REST
## SNMP
# API Function: clear_metric_narrow
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_metric_narrow(device_name )

	Robot API Call: 

		isis_clear_metric_narrow  device_name  

UUID: 1791f449-aaad-4d21-8db0-88214147709e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no metric

----------------------------------------------


## REST
## SNMP
# API Function: set_metric_wide
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_metric_wide(device_name )

	Robot API Call: 

		isis_set_metric_wide  device_name  

UUID: 76da7bee-e0bf-484d-b26d-8c5a88263b5e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||metric wide

----------------------------------------------


## REST
## SNMP
# API Function: clear_metric_wide
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_metric_wide(device_name )

	Robot API Call: 

		isis_clear_metric_wide  device_name  

UUID: c0fcf7c7-632a-4ad7-9a3f-22113bd9da38
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no metric

----------------------------------------------


## REST
## SNMP
# API Function: set_overload
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_overload(device_name )

	Robot API Call: 

		isis_set_overload  device_name  

UUID: dd0b7750-44a2-4fb7-bc26-89442f3b03d4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||overload

----------------------------------------------


## REST
## SNMP
# API Function: clear_overload
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_overload(device_name )

	Robot API Call: 

		isis_clear_overload  device_name  

UUID: ad2a98c5-e61e-424c-8673-42af44212485
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no overload

----------------------------------------------


## REST
## SNMP
# API Function: set_redistribute_bgp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_redistribute_bgp(device_name )

	Robot API Call: 

		isis_set_redistribute_bgp  device_name  

UUID: d64e0783-f82d-47aa-8b9c-fb1228323d6b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute bgp||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.{oid_index}

----------------------------------------------


# API Function: clear_redistribute_bgp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_redistribute_bgp(device_name )

	Robot API Call: 

		isis_clear_redistribute_bgp  device_name  

UUID: 19e03588-ec5e-4322-b59a-93a73c1deea9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute bgp||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.{oid_index}

----------------------------------------------


# API Function: enable_redistribute_bgp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_redistribute_bgp(device_name )

	Robot API Call: 

		isis_enable_redistribute_bgp  device_name  

UUID: d0a806dc-dec4-4261-8665-bec6ad3d2f24
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute bgp enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.{oid_index}

----------------------------------------------


# API Function: disable_redistribute_bgp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_redistribute_bgp(device_name )

	Robot API Call: 

		isis_disable_redistribute_bgp  device_name  

UUID: e8d423aa-74c0-430c-9326-87be7dc41b18
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute bgp enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.{oid_index}

----------------------------------------------


# API Function: set_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_redistribute_direct(device_name )

	Robot API Call: 

		isis_set_redistribute_direct  device_name  

UUID: 20aefb6c-0894-4e13-a3a3-ff1541343dad
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute direct||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.0.3.0.1

----------------------------------------------


# API Function: clear_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_redistribute_direct(device_name )

	Robot API Call: 

		isis_clear_redistribute_direct  device_name  

UUID: f37c174b-1650-4ae7-b20d-0af748785751
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute direct||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.0.3.0.1

----------------------------------------------


# API Function: enable_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_redistribute_direct(device_name )

	Robot API Call: 

		isis_enable_redistribute_direct  device_name  

UUID: 09f6db17-41c7-4533-8a9f-2ac452f6173c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute direct enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.0.3.0.1

----------------------------------------------


# API Function: disable_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_redistribute_direct(device_name )

	Robot API Call: 

		isis_disable_redistribute_direct  device_name  

UUID: 0ea31ada-4642-41ba-89cf-64b70d432b2b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute direct enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.0.3.0.1

----------------------------------------------


# API Function: enable_redistribute_direct_ipv6
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_redistribute_direct_ipv6(device_name )

	Robot API Call: 

		isis_enable_redistribute_direct_ipv6  device_name  

UUID: 495d343f-d8a9-492c-a1f4-d746dbd25fda
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||ipv6 redistribute direct enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.0.12.0.1

----------------------------------------------


# API Function: disable_redistribute_direct_ipv6
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_redistribute_direct_ipv6(device_name )

	Robot API Call: 

		isis_disable_redistribute_direct_ipv6  device_name  

UUID: 9b128fb6-ff78-4a70-b70c-6df61e6f4a95
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no ipv6 redistribute direct enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.0.12.0.1

----------------------------------------------


# API Function: set_redistribute_direct_apply
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_redistribute_direct_apply(device_name )

	Robot API Call: 

		isis_set_redistribute_direct_apply  device_name  

UUID: c5c6d7b8-c182-484f-a328-246031a1284f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis apply redistribute direct

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.0.3.0.1||1.3.6.1.4.1.2272.1.8.100.15.0

----------------------------------------------


# API Function: set_redistribute_direct_route_map_policy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_redistribute_direct_route_map_policy(device_name )

	Robot API Call: 

		isis_set_redistribute_direct_route_map_policy  device_name  

UUID: 3bd8cad2-55a6-4775-9d84-1a1dd0c5bc53
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute direct route-map {policy_name}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.11.0.3.0.1

----------------------------------------------


# API Function: clear_redistribute_direct_route_map_policy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_redistribute_direct_route_map_policy(device_name )

	Robot API Call: 

		isis_clear_redistribute_direct_route_map_policy  device_name  

UUID: cffea40d-754d-4b00-b803-3265f345afb0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute direct route-map ||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.11.0.3.0.1

----------------------------------------------


# API Function: set_redistribute_ospf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_redistribute_ospf(device_name )

	Robot API Call: 

		isis_set_redistribute_ospf  device_name  

UUID: 6a9af17b-8fe4-49e4-8e13-3c9c4c915dca
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute ospf||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.{oid_index}

----------------------------------------------


# API Function: clear_redistribute_ospf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_redistribute_ospf(device_name )

	Robot API Call: 

		isis_clear_redistribute_ospf  device_name  

UUID: 448c323c-e460-444d-afd9-c9797714c37f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute ospf||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.{oid_index}

----------------------------------------------


# API Function: enable_redistribute_ospf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_redistribute_ospf(device_name )

	Robot API Call: 

		isis_enable_redistribute_ospf  device_name  

UUID: edb590f7-7bae-43c8-91ac-1e81d05bac91
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute ospf enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.{oid_index}

----------------------------------------------


# API Function: disable_redistribute_ospf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_redistribute_ospf(device_name )

	Robot API Call: 

		isis_disable_redistribute_ospf  device_name  

UUID: 8d67a62b-5750-46aa-965f-70971738de7b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute ospf enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.{oid_index}

----------------------------------------------


# API Function: set_redistribute_rip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_redistribute_rip(device_name )

	Robot API Call: 

		isis_set_redistribute_rip  device_name  

UUID: 571889fe-477c-46a4-980f-fc68c9c07945
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute rip||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.{oid_index}

----------------------------------------------


# API Function: clear_redistribute_rip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_redistribute_rip(device_name )

	Robot API Call: 

		isis_clear_redistribute_rip  device_name  

UUID: e67af810-a0cc-499e-ae8e-782c9a553547
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute rip||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.{oid_index}

----------------------------------------------


# API Function: enable_redistribute_rip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_redistribute_rip(device_name )

	Robot API Call: 

		isis_enable_redistribute_rip  device_name  

UUID: 16611f69-56cf-4fa8-b09f-ea599503cb57
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute rip enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.{oid_index}

----------------------------------------------


# API Function: disable_redistribute_rip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_redistribute_rip(device_name )

	Robot API Call: 

		isis_disable_redistribute_rip  device_name  

UUID: adf56f6a-4266-44a5-a38d-5e05300a41db
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute rip enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.{oid_index}

----------------------------------------------


# API Function: set_redistribute_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_redistribute_static(device_name )

	Robot API Call: 

		isis_set_redistribute_static  device_name  

UUID: 63cdc549-5245-46f9-b5cd-3c50cd399d44
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute static||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.{oid_index}

----------------------------------------------


# API Function: clear_redistribute_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_redistribute_static(device_name )

	Robot API Call: 

		isis_clear_redistribute_static  device_name  

UUID: e03c7d05-b7e0-4149-b875-ea08c9156d03
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute static||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.15.{oid_index}

----------------------------------------------


# API Function: enable_redistribute_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_redistribute_static(device_name )

	Robot API Call: 

		isis_enable_redistribute_static  device_name  

UUID: e74e23c1-2c91-47b4-8e83-ecfb889f8ada
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||redistribute static enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.{oid_index}

----------------------------------------------


# API Function: disable_redistribute_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_redistribute_static(device_name )

	Robot API Call: 

		isis_disable_redistribute_static  device_name  

UUID: 3513c128-ad24-41f4-a6df-12338b62dc6d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no redistribute static enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22.1.5.{oid_index}

----------------------------------------------


# API Function: set_redistribute_apply
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_redistribute_apply(device_name )

	Robot API Call: 

		isis_set_redistribute_apply  device_name  

UUID: 6306c6cd-5828-4f83-87fc-f8e2196a8dcb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis apply redistribute||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.15.{oid_index}

----------------------------------------------


# API Function: set_spf_delay
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_spf_delay(device_name )

	Robot API Call: 

		isis_set_spf_delay  device_name  

UUID: 710ce659-c09c-4f29-9dc9-7ecba7e6c078
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spf-delay {delay}

----------------------------------------------


## REST
## SNMP
# API Function: clear_spf_delay
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_spf_delay(device_name )

	Robot API Call: 

		isis_clear_spf_delay  device_name  

UUID: 75a848f5-f768-402c-9d72-fb28adec3f5f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spf-delay

----------------------------------------------


## REST
## SNMP
# API Function: set_circuit_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_circuit_on_port(device_name )

	Robot API Call: 

		isis_set_circuit_on_port  device_name  

UUID: 6fb5a6ce-d257-4aa6-9b6b-218064622469
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.2.{isis_circuit}||1.3.6.1.3.37.1.3.2.1.3.{isis_circuit}||1.3.6.1.3.37.1.3.2.1.4.{isis_circuit}

----------------------------------------------


# API Function: enable_circuit_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_circuit_on_port(device_name )

	Robot API Call: 

		isis_enable_circuit_on_port  device_name  

UUID: 81736c7f-0658-423c-ac8a-804632dfeeb4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.3.{port}

----------------------------------------------


# API Function: disable_circuit_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_circuit_on_port(device_name )

	Robot API Call: 

		isis_disable_circuit_on_port  device_name  

UUID: 63620079-ea8b-44d6-8a30-d50c1b3771fc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no isis enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.3.{port}

----------------------------------------------


# API Function: clear_circuit_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_circuit_on_port(device_name )

	Robot API Call: 

		isis_clear_circuit_on_port  device_name  

UUID: a507ebbd-9d73-4db5-bce9-966c29e42954
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no isis

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.4.{port}

----------------------------------------------


# API Function: set_circuit_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_circuit_on_mlt(device_name )

	Robot API Call: 

		isis_set_circuit_on_mlt  device_name  

UUID: 73f4e284-3f73-4faf-b3de-72bf65186267
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.2.{isis_circuit}||1.3.6.1.3.37.1.3.2.1.3.{isis_circuit}||1.3.6.1.3.37.1.3.2.1.4.{isis_circuit}

----------------------------------------------


# API Function: enable_circuit_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_circuit_on_mlt(device_name )

	Robot API Call: 

		isis_enable_circuit_on_mlt  device_name  

UUID: fe1f3a9a-2ba5-4653-bb89-d961ba397eac
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.3.{mlt_id}

----------------------------------------------


# API Function: disable_circuit_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_circuit_on_mlt(device_name )

	Robot API Call: 

		isis_disable_circuit_on_mlt  device_name  

UUID: a7cd4661-5a80-476b-a5f2-ca98f8a66eb4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no isis enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.3.{mlt_id}

----------------------------------------------


# API Function: clear_circuit_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_circuit_on_mlt(device_name )

	Robot API Call: 

		isis_clear_circuit_on_mlt  device_name  

UUID: ff807daf-f443-4d1c-9d8b-e30f200d4b36
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no isis

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.4.{mlt_id}

----------------------------------------------


# API Function: set_auth_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_auth_on_port(device_name, port, auth_type, key_id, auth_key)

	Robot API Call: 

		isis_set_auth_on_port  device_name  port  auth_type  key_id  auth_key

UUID: 041f1993-d357-4926-9d14-efb8acbe5c68
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis hello-auth type {auth_type} key {auth_key} key-id {key_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.2.1.3.{port}||1.3.6.1.4.1.2272.1.63.2.1.4.{port}||1.3.6.1.4.1.2272.1.63.2.1.5.{port}

----------------------------------------------


# API Function: set_auth_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_auth_on_mlt(device_name, mlt_id, auth_type, key_id, auth_key)

	Robot API Call: 

		isis_set_auth_on_mlt  device_name  mlt_id  auth_type  key_id  auth_key

UUID: a2e60ffb-9f97-4bf0-9864-37f5e333c6bf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis hello-auth type {auth_type} key {auth_key} key-id {key_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.2.1.3.{mlt_id}||1.3.6.1.4.1.2272.1.63.2.1.4.{mlt_id}||1.3.6.1.4.1.2272.1.63.2.1.5.{mlt_id}

----------------------------------------------


# API Function: clear_auth_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_auth_on_port(device_name )

	Robot API Call: 

		isis_clear_auth_on_port  device_name  

UUID: 1e95c189-151e-439d-a953-fc1d7f81bf8c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no isis hello-auth

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.2.1.3.{port}

----------------------------------------------


# API Function: clear_auth_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_auth_on_mlt(device_name )

	Robot API Call: 

		isis_clear_auth_on_mlt  device_name  

UUID: 6e813614-15bc-4ce9-b5cd-f898942a1d00
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no isis hello-auth

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.2.1.3.{mlt_id}

----------------------------------------------


# API Function: set_l1_dr_priority_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_l1_dr_priority_on_port(device_name )

	Robot API Call: 

		isis_set_l1_dr_priority_on_port  device_name  

UUID: 8e30408c-7b97-4c58-9de1-5203240f5c14
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis l1-dr-priority {priority}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1.1.4.{port}

----------------------------------------------


# API Function: set_l1_dr_priority_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_l1_dr_priority_on_mlt(device_name )

	Robot API Call: 

		isis_set_l1_dr_priority_on_mlt  device_name  

UUID: 33aca53f-ca4b-473e-a0a4-e3524c9e6652
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis l1-dr-priority {priority}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1.1.4.{mlt_id}

----------------------------------------------


# API Function: set_l1_hello_interval_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_l1_hello_interval_on_port(device_name, port, interval)

	Robot API Call: 

		isis_set_l1_hello_interval_on_port  device_name  port  interval

UUID: b9cd3f50-d847-4f00-b3bf-226aeaa3e1a7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis l1-hello-interval {interval}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1.1.9.{port}

----------------------------------------------


# API Function: set_l1_hello_interval_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_l1_hello_interval_on_mlt(device_name, mlt_id, interval)

	Robot API Call: 

		isis_set_l1_hello_interval_on_mlt  device_name  mlt_id  interval

UUID: 915d4fb3-893c-48ca-ad79-cdb3b4f55fb8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis l1-hello-interval {interval}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1.1.9.{mlt_id}

----------------------------------------------


# API Function: set_l1_hello_multiplier_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_l1_hello_multiplier_on_port(device_name, port, multiplier)

	Robot API Call: 

		isis_set_l1_hello_multiplier_on_port  device_name  port  multiplier

UUID: 7cf5fb00-5403-484c-9c55-a8b210f08794
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis l1-hello-multiplier {multiplier}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1.1.8.{port}

----------------------------------------------


# API Function: set_l1_hello_multiplier_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_l1_hello_multiplier_on_mlt(device_name, mlt_id, multiplier)

	Robot API Call: 

		isis_set_l1_hello_multiplier_on_mlt  device_name  mlt_id  multiplier

UUID: 04e62c21-8b5e-49ef-8bd9-d17504b9d267
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis l1-hello-multiplier {multiplier}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1.1.8.{mlt_id}

----------------------------------------------


# API Function: set_logical_interface_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_logical_interface_port(device_name, isis_id, primary_vlan, secondary_vlan, port)

	Robot API Call: 

		isis_set_logical_interface_port  device_name  isis_id  primary_vlan  secondary_vlan  port

UUID: ebb09810-b864-434e-a1b2-71182d98a5e7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id} vid {primary_vlan},{secondary_vlan} primary-vid {primary_vlan} port {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.26.1.5.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.6.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.7.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.9.{isis_id}

----------------------------------------------


# API Function: set_logical_interface_port_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_logical_interface_port_name(device_name, isis_id, primary_vlan, secondary_vlan, port, name)

	Robot API Call: 

		isis_set_logical_interface_port_name  device_name  isis_id  primary_vlan  secondary_vlan  port  name

UUID: ecbfd0cf-38c3-40f8-bd28-2f8ba6b5d046
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id} vid {primary_vlan},{secondary_vlan} primary-vid {primary_vlan} port {port} name {name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.26.1.5.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.6.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.7.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.8.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.9.{isis_id}

----------------------------------------------


# API Function: set_logical_interface_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_logical_interface_mlt(device_name, isis_id, primary_vlan, secondary_vlan, mlt_id)

	Robot API Call: 

		isis_set_logical_interface_mlt  device_name  isis_id  primary_vlan  secondary_vlan  mlt_id

UUID: b6950cc9-9864-4cbf-b6eb-41b42073a2b7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id} vid {primary_vlan},{secondary_vlan} primary-vid {primary_vlan} mlt {mlt_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.26.1.5.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.6.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.7.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.9.{isis_id}

----------------------------------------------


# API Function: set_logical_interface_mlt_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_logical_interface_mlt_name(device_name, isis_id, primary_vlan, secondary_vlan, mlt_id, name)

	Robot API Call: 

		isis_set_logical_interface_mlt_name  device_name  isis_id  primary_vlan  secondary_vlan  mlt_id  name

UUID: 65b86f45-faaf-42b0-b402-4270611fec81
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id} vid {primary_vlan},{secondary_vlan} primary-vid {primary_vlan} mlt {mlt_id} name {name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.26.1.5.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.6.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.7.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.8.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.9.{isis_id}

----------------------------------------------


# API Function: set_logical_interface_ipv4
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_logical_interface_ipv4(device_name, isis_id, ip)

	Robot API Call: 

		isis_set_logical_interface_ipv4  device_name  isis_id  ip

UUID: b516f64c-ea7a-4bc9-b06b-b7e48ea7d233
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id} dest-ip {ip}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.26.1.4.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.9.{isis_id}

----------------------------------------------


# API Function: set_logical_interface_ipv4_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_logical_interface_ipv4_name(device_name, isis_id, ip, name)

	Robot API Call: 

		isis_set_logical_interface_ipv4_name  device_name  isis_id  ip  name

UUID: 4787609a-74d8-473a-91a9-c23ed2f93f16
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id} dest-ip {ip} name {name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.26.1.4.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.8.{isis_id}||1.3.6.1.4.1.2272.1.63.26.1.9.{isis_id}

----------------------------------------------


# API Function: clear_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_logical_interface(device_name )

	Robot API Call: 

		isis_clear_logical_interface  device_name  

UUID: 147e596b-0eae-4a4b-8aba-8c30f685ede9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no logical-intf isis {isis_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.26.1.9.{isis_id}

----------------------------------------------


# API Function: set_circuit_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_circuit_on_logical_interface(device_name )

	Robot API Call: 

		isis_set_circuit_on_logical_interface  device_name  

UUID: d59abe65-4e7d-4fdf-9dc7-60aeba11b38f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.2.{isis_id}||1.3.6.1.3.37.1.3.2.1.3.{isis_id}||1.3.6.1.3.37.1.3.2.1.4.{isis_id}

----------------------------------------------


# API Function: enable_circuit_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_enable_circuit_on_logical_interface(device_name )

	Robot API Call: 

		isis_enable_circuit_on_logical_interface  device_name  

UUID: fdf2b144-ed15-4231-8bb6-e936d4051830
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.3.{isis_id}

----------------------------------------------


# API Function: disable_circuit_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_disable_circuit_on_logical_interface(device_name )

	Robot API Call: 

		isis_disable_circuit_on_logical_interface  device_name  

UUID: 2f340493-ed7f-4743-bd1b-014006864256
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||no isis enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.3.{isis_id}

----------------------------------------------


# API Function: clear_circuit_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_circuit_on_logical_interface(device_name )

	Robot API Call: 

		isis_clear_circuit_on_logical_interface  device_name  

UUID: 5f0e7037-a1c3-46ca-8bfc-fd0ec2841299
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||no isis||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.4.{isis_id}

----------------------------------------------


# API Function: set_auth_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_auth_on_logical_interface(device_name, isis_id, auth_type, key_id, auth_key)

	Robot API Call: 

		isis_set_auth_on_logical_interface  device_name  isis_id  auth_type  key_id  auth_key

UUID: 6dbef1fc-ea72-4854-9594-52ccc0109429
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis hello-auth type {auth_type} key {auth_key} key-id {key_id}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.2.1.3.{isis_id}||1.3.6.1.4.1.2272.1.63.2.1.4.{isis_id}||1.3.6.1.4.1.2272.1.63.2.1.5.{isis_id}

----------------------------------------------


# API Function: clear_auth_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_clear_auth_on_logical_interface(device_name )

	Robot API Call: 

		isis_clear_auth_on_logical_interface  device_name  

UUID: 69035712-e13e-4b00-af19-c0e77699aee9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||no isis hello-auth||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.2.1.3.{isis_id}

----------------------------------------------


# API Function: set_l1_dr_priority_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_l1_dr_priority_on_logical_interface(device_name )

	Robot API Call: 

		isis_set_l1_dr_priority_on_logical_interface  device_name  

UUID: 4938f0c5-c7ba-47f4-8891-31d58293f376
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis l1-dr-priority {priority}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1.1.4.{isis_id}

----------------------------------------------


# API Function: set_l1_hello_interval_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_l1_hello_interval_on_logical_interface(device_name, isis_id, interval)

	Robot API Call: 

		isis_set_l1_hello_interval_on_logical_interface  device_name  isis_id  interval

UUID: b9be7b04-0cbb-4d58-a6e5-36d3dd3ac3e1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis l1-hello-interval {interval}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1.1.9.{isis_id}

----------------------------------------------


# API Function: set_l1_hello_multiplier_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_set_l1_hello_multiplier_on_logical_interface(device_name, isis_id, multiplier)

	Robot API Call: 

		isis_set_l1_hello_multiplier_on_logical_interface  device_name  isis_id  multiplier

UUID: 28ca259c-6215-4fbc-9311-f3863b53e501
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis l1-hello-multiplier {multiplier}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1.1.8.{isis_id}

----------------------------------------------


# API Function: isis_verify_enabled_globally
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_enabled_globally(device_name)

	Robot API Call: 

		isis_verify_enabled_globally  device_name

# API Function: isis_verify_disabled_globally
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_disabled_globally(device_name)

	Robot API Call: 

		isis_verify_disabled_globally  device_name

# API Function: isis_verify_system_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_system_id(device_name, sysid)

	Robot API Call: 

		isis_verify_system_id  device_name  sysid

# API Function: isis_verify_system_id_is_not
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_system_id_is_not(device_name, sysid)

	Robot API Call: 

		isis_verify_system_id_is_not  device_name  sysid

# API Function: isis_verify_manual_area_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_manual_area_exists(device_name, area)

	Robot API Call: 

		isis_verify_manual_area_exists  device_name  area

# API Function: isis_verify_manual_area_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_manual_area_does_not_exist(device_name, area)

	Robot API Call: 

		isis_verify_manual_area_does_not_exist  device_name  area

# API Function: isis_verify_system_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_system_name(device_name, sys_name)

	Robot API Call: 

		isis_verify_system_name  device_name  sys_name

# API Function: isis_verify_system_name_is_not
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_system_name_is_not(device_name, sys_name)

	Robot API Call: 

		isis_verify_system_name_is_not  device_name  sys_name

# API Function: isis_verify_circuit_on_port_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_port_exists(device_name, ports)

	Robot API Call: 

		isis_verify_circuit_on_port_exists  device_name  ports

# API Function: isis_verify_circuit_on_port_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_port_does_not_exist(device_name, ports)

	Robot API Call: 

		isis_verify_circuit_on_port_does_not_exist  device_name  ports

# API Function: isis_verify_circuit_on_port_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_port_enabled(device_name, ports)

	Robot API Call: 

		isis_verify_circuit_on_port_enabled  device_name  ports

# API Function: isis_verify_circuit_on_port_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_port_disabled(device_name, ports)

	Robot API Call: 

		isis_verify_circuit_on_port_disabled  device_name  ports

# API Function: isis_verify_circuit_on_mlt_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_mlt_exists(device_name, mlt_ids)

	Robot API Call: 

		isis_verify_circuit_on_mlt_exists  device_name  mlt_ids

# API Function: isis_verify_circuit_on_mlt_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_mlt_does_not_exist(device_name, mlt_ids)

	Robot API Call: 

		isis_verify_circuit_on_mlt_does_not_exist  device_name  mlt_ids

# API Function: isis_verify_circuit_on_mlt_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_mlt_enabled(device_name, mlt_ids)

	Robot API Call: 

		isis_verify_circuit_on_mlt_enabled  device_name  mlt_ids

# API Function: isis_verify_circuit_on_mlt_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_mlt_disabled(device_name, mlt_ids)

	Robot API Call: 

		isis_verify_circuit_on_mlt_disabled  device_name  mlt_ids

# API Function: isis_verify_circuit_on_logical_interface_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_logical_interface_exists(device_name, isis_id)

	Robot API Call: 

		isis_verify_circuit_on_logical_interface_exists  device_name  isis_id

# API Function: isis_verify_circuit_on_logical_interface_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_logical_interface_does_not_exist(device_name, isis_id)

	Robot API Call: 

		isis_verify_circuit_on_logical_interface_does_not_exist  device_name  isis_id

# API Function: isis_verify_circuit_on_logical_interface_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_logical_interface_enabled(device_name, isis_id)

	Robot API Call: 

		isis_verify_circuit_on_logical_interface_enabled  device_name  isis_id

# API Function: isis_verify_circuit_on_logical_interface_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_circuit_on_logical_interface_disabled(device_name, isis_id)

	Robot API Call: 

		isis_verify_circuit_on_logical_interface_disabled  device_name  isis_id

# API Function: isis_verify_auth_type_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_type_port(device_name, port, auth_type)

	Robot API Call: 

		isis_verify_auth_type_port  device_name  port  auth_type

# API Function: isis_verify_auth_type_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_type_mlt(device_name, mlt_id, auth_type)

	Robot API Call: 

		isis_verify_auth_type_mlt  device_name  mlt_id  auth_type

# API Function: isis_verify_auth_type_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_type_logical_interface(device_name, isis_id, auth_type)

	Robot API Call: 

		isis_verify_auth_type_logical_interface  device_name  isis_id  auth_type

# API Function: isis_verify_auth_key_id_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_key_id_port(device_name, port, key_id)

	Robot API Call: 

		isis_verify_auth_key_id_port  device_name  port  key_id

# API Function: isis_verify_auth_key_id_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_key_id_mlt(device_name, mlt_id, key_id)

	Robot API Call: 

		isis_verify_auth_key_id_mlt  device_name  mlt_id  key_id

# API Function: isis_verify_auth_key_id_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_key_id_logical_interface(device_name, isis_id, key_id)

	Robot API Call: 

		isis_verify_auth_key_id_logical_interface  device_name  isis_id  key_id

# API Function: isis_verify_auth_does_not_exist_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_does_not_exist_port(device_name, port)

	Robot API Call: 

		isis_verify_auth_does_not_exist_port  device_name  port

# API Function: isis_verify_auth_does_not_exist_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_does_not_exist_mlt(device_name, mlt_id)

	Robot API Call: 

		isis_verify_auth_does_not_exist_mlt  device_name  mlt_id

# API Function: isis_verify_auth_does_not_exist_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_does_not_exist_logical_interface(device_name, isis_id)

	Robot API Call: 

		isis_verify_auth_does_not_exist_logical_interface  device_name  isis_id

# API Function: isis_verify_adjacency_level_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_level_port(device_name, port, level, adj_index)

	Robot API Call: 

		isis_verify_adjacency_level_port  device_name  port  level  adj_index

# API Function: isis_verify_adjacency_level_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_level_mlt(device_name, mlt_id, level, adj_index)

	Robot API Call: 

		isis_verify_adjacency_level_mlt  device_name  mlt_id  level  adj_index

# API Function: isis_verify_adjacency_level_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_level_logical_interface(device_name, isis_id, level, adj_index)

	Robot API Call: 

		isis_verify_adjacency_level_logical_interface  device_name  isis_id  level  adj_index

# API Function: isis_verify_adjacency_state_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_state_port(device_name, port, state, adj_index)

	Robot API Call: 

		isis_verify_adjacency_state_port  device_name  port  state  adj_index

# API Function: isis_verify_adjacency_state_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_state_mlt(device_name, mlt_id, state, adj_index)

	Robot API Call: 

		isis_verify_adjacency_state_mlt  device_name  mlt_id  state  adj_index

# API Function: isis_verify_adjacency_state_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_state_logical_interface(device_name, isis_id, state, adj_index)

	Robot API Call: 

		isis_verify_adjacency_state_logical_interface  device_name  isis_id  state  adj_index

# API Function: isis_verify_adjacency_active_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_active_port(device_name, port, adj_index)

	Robot API Call: 

		isis_verify_adjacency_active_port  device_name  port  adj_index

# API Function: isis_verify_adjacency_active_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_active_mlt(device_name, mlt_id, adj_index)

	Robot API Call: 

		isis_verify_adjacency_active_mlt  device_name  mlt_id  adj_index

# API Function: isis_verify_adjacency_active_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_active_logical_interface(device_name, isis_id, adj_index)

	Robot API Call: 

		isis_verify_adjacency_active_logical_interface  device_name  isis_id  adj_index

# API Function: isis_verify_adjacency_inactive_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_inactive_port(device_name, port, adj_index)

	Robot API Call: 

		isis_verify_adjacency_inactive_port  device_name  port  adj_index

# API Function: isis_verify_adjacency_inactive_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_inactive_mlt(device_name, mlt_id, adj_index)

	Robot API Call: 

		isis_verify_adjacency_inactive_mlt  device_name  mlt_id  adj_index

# API Function: isis_verify_adjacency_inactive_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_inactive_logical_interface(device_name, isis_id, adj_index)

	Robot API Call: 

		isis_verify_adjacency_inactive_logical_interface  device_name  isis_id  adj_index

# API Function: isis_verify_adjacency_up_time_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_up_time_port(device_name, port, time, count_operator, adj_index)

	Robot API Call: 

		isis_verify_adjacency_up_time_port  device_name  port  time  count_operator  adj_index

# API Function: isis_verify_adjacency_up_time_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_up_time_mlt(device_name, mlt_id, time, count_operator, adj_index)

	Robot API Call: 

		isis_verify_adjacency_up_time_mlt  device_name  mlt_id  time  count_operator  adj_index

# API Function: isis_verify_adjacency_up_time_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_up_time_logical_interface(device_name, isis_id, time, count_operator, adj_index)

	Robot API Call: 

		isis_verify_adjacency_up_time_logical_interface  device_name  isis_id  time  count_operator  adj_index

# API Function: isis_verify_adjacency_priority_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_priority_port(device_name, port, priority, adj_index)

	Robot API Call: 

		isis_verify_adjacency_priority_port  device_name  port  priority  adj_index

# API Function: isis_verify_adjacency_priority_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_priority_mlt(device_name, mlt_id, priority, adj_index)

	Robot API Call: 

		isis_verify_adjacency_priority_mlt  device_name  mlt_id  priority  adj_index

# API Function: isis_verify_adjacency_priority_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_priority_logical_interface(device_name, isis_id, priority, adj_index)

	Robot API Call: 

		isis_verify_adjacency_priority_logical_interface  device_name  isis_id  priority  adj_index

# API Function: isis_verify_adjacency_hold_time_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_hold_time_port(device_name, port, holdtime, count_operator, adj_index)

	Robot API Call: 

		isis_verify_adjacency_hold_time_port  device_name  port  holdtime  count_operator  adj_index

# API Function: isis_verify_adjacency_hold_time_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_hold_time_mlt(device_name, mlt_id, holdtime, count_operator, adj_index)

	Robot API Call: 

		isis_verify_adjacency_hold_time_mlt  device_name  mlt_id  holdtime  count_operator  adj_index

# API Function: isis_verify_adjacency_hold_time_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_hold_time_logical_interface(device_name, isis_id, holdtime, count_operator, adj_index)

	Robot API Call: 

		isis_verify_adjacency_hold_time_logical_interface  device_name  isis_id  holdtime  count_operator  adj_index

# API Function: isis_verify_adjacency_system_id_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_system_id_port(device_name, port, sys_id, adj_index)

	Robot API Call: 

		isis_verify_adjacency_system_id_port  device_name  port  sys_id  adj_index

# API Function: isis_verify_adjacency_system_id_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_system_id_mlt(device_name, mlt_id, sys_id, adj_index)

	Robot API Call: 

		isis_verify_adjacency_system_id_mlt  device_name  mlt_id  sys_id  adj_index

# API Function: isis_verify_adjacency_system_id_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_system_id_logical_interface(device_name, isis_id, sys_id, adj_index)

	Robot API Call: 

		isis_verify_adjacency_system_id_logical_interface  device_name  isis_id  sys_id  adj_index

# API Function: isis_verify_adjacency_host_name_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_host_name_port(device_name, port, hostname, adj_index)

	Robot API Call: 

		isis_verify_adjacency_host_name_port  device_name  port  hostname  adj_index

# API Function: isis_verify_adjacency_host_name_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_host_name_mlt(device_name, mlt_id, hostname, adj_index)

	Robot API Call: 

		isis_verify_adjacency_host_name_mlt  device_name  mlt_id  hostname  adj_index

# API Function: isis_verify_adjacency_host_name_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_adjacency_host_name_logical_interface(device_name, isis_id, hostname, adj_index)

	Robot API Call: 

		isis_verify_adjacency_host_name_logical_interface  device_name  isis_id  hostname  adj_index

# API Function: isis_verify_l1_hello_interval_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_hello_interval_port(device_name, port, interval)

	Robot API Call: 

		isis_verify_l1_hello_interval_port  device_name  port  interval

# API Function: isis_verify_l1_hello_interval_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_hello_interval_mlt(device_name, mlt_id, interval)

	Robot API Call: 

		isis_verify_l1_hello_interval_mlt  device_name  mlt_id  interval

# API Function: isis_verify_l1_hello_interval_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_hello_interval_logical_interface(device_name, isis_id, interval)

	Robot API Call: 

		isis_verify_l1_hello_interval_logical_interface  device_name  isis_id  interval

# API Function: isis_verify_l1_hello_multiplier_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_hello_multiplier_port(device_name, port, multiplier)

	Robot API Call: 

		isis_verify_l1_hello_multiplier_port  device_name  port  multiplier

# API Function: isis_verify_l1_hello_multiplier_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_hello_multiplier_mlt(device_name, mlt_id, multiplier)

	Robot API Call: 

		isis_verify_l1_hello_multiplier_mlt  device_name  mlt_id  multiplier

# API Function: isis_verify_l1_hello_multiplier_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_hello_multiplier_logical_interface(device_name, isis_id, multiplier)

	Robot API Call: 

		isis_verify_l1_hello_multiplier_logical_interface  device_name  isis_id  multiplier

# API Function: isis_verify_l1_dr_hello_interval_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_dr_hello_interval_port(device_name, port, interval)

	Robot API Call: 

		isis_verify_l1_dr_hello_interval_port  device_name  port  interval

# API Function: isis_verify_l1_dr_hello_interval_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_dr_hello_interval_mlt(device_name, mlt_id, interval)

	Robot API Call: 

		isis_verify_l1_dr_hello_interval_mlt  device_name  mlt_id  interval

# API Function: isis_verify_l1_dr_hello_interval_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_dr_hello_interval_logical_interface(device_name, isis_id, interval)

	Robot API Call: 

		isis_verify_l1_dr_hello_interval_logical_interface  device_name  isis_id  interval

# API Function: isis_verify_lsdb_unicast_ip_and_hostname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_lsdb_unicast_ip_and_hostname(device_name, address, host_name)

	Robot API Call: 

		isis_verify_lsdb_unicast_ip_and_hostname  device_name  address  host_name

# API Function: isis_verify_corrupted_lsps
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_corrupted_lsps(device_name, count, count_operator, level)

	Robot API Call: 

		isis_verify_corrupted_lsps  device_name  count  count_operator  level

# API Function: isis_verify_auth_key_fails
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_auth_key_fails(device_name, count, count_operator, level)

	Robot API Call: 

		isis_verify_auth_key_fails  device_name  count  count_operator  level

# API Function: isis_verify_manual_addresses_dropped_from_area
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_manual_addresses_dropped_from_area(device_name, count, count_operator, level)

	Robot API Call: 

		isis_verify_manual_addresses_dropped_from_area  device_name  count  count_operator  level

# API Function: isis_verify_maximum_sequence_number_exceeded_attempts
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_maximum_sequence_number_exceeded_attempts(device_name, count, count_operator, level)

	Robot API Call: 

		isis_verify_maximum_sequence_number_exceeded_attempts  device_name  count  count_operator  level

# API Function: isis_verify_sequence_number_skips
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_sequence_number_skips(device_name, count, count_operator, level)

	Robot API Call: 

		isis_verify_sequence_number_skips  device_name  count  count_operator  level

# API Function: isis_verify_own_lsp_purges
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_own_lsp_purges(device_name, count, count_operator, level)

	Robot API Call: 

		isis_verify_own_lsp_purges  device_name  count  count_operator  level

# API Function: isis_verify_id_length_mismatches
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_id_length_mismatches(device_name, count, count_operator, level)

	Robot API Call: 

		isis_verify_id_length_mismatches  device_name  count  count_operator  level

# API Function: isis_verify_partition_changes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_partition_changes(device_name, count, count_operator, level)

	Robot API Call: 

		isis_verify_partition_changes  device_name  count  count_operator  level

# API Function: isis_verify_lsp_database_overloads
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_lsp_database_overloads(device_name, count, count_operator, level)

	Robot API Call: 

		isis_verify_lsp_database_overloads  device_name  count  count_operator  level

# API Function: isis_verify_logical_interface_exists_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_exists_on_port(device_name, index, port)

	Robot API Call: 

		isis_verify_logical_interface_exists_on_port  device_name  index  port

# API Function: isis_verify_logical_interface_does_not_exist_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_does_not_exist_on_port(device_name, index, port)

	Robot API Call: 

		isis_verify_logical_interface_does_not_exist_on_port  device_name  index  port

# API Function: isis_verify_logical_interface_exists_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_exists_on_mlt(device_name, index, mlt_index)

	Robot API Call: 

		isis_verify_logical_interface_exists_on_mlt  device_name  index  mlt_index

# API Function: isis_verify_logical_interface_does_not_exist_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_does_not_exist_on_mlt(device_name, index, port)

	Robot API Call: 

		isis_verify_logical_interface_does_not_exist_on_mlt  device_name  index  port

# API Function: isis_verify_logical_interface_ipv4_destination_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_ipv4_destination_exists(device_name, index, ip)

	Robot API Call: 

		isis_verify_logical_interface_ipv4_destination_exists  device_name  index  ip

# API Function: isis_verify_logical_interface_ipv4_destination_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_ipv4_destination_does_not_exist(device_name, index, ip)

	Robot API Call: 

		isis_verify_logical_interface_ipv4_destination_does_not_exist  device_name  index  ip

# API Function: isis_verify_logical_interface_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_name(device_name, index, name)

	Robot API Call: 

		isis_verify_logical_interface_name  device_name  index  name

# API Function: isis_verify_logical_interface_name_is_not
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_name_is_not(device_name, index, name)

	Robot API Call: 

		isis_verify_logical_interface_name_is_not  device_name  index  name

# API Function: isis_verify_port_auth_fails
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_port_auth_fails(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_port_auth_fails  device_name  port  count  count_operator  level

# API Function: isis_verify_port_adjacency_changes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_port_adjacency_changes(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_port_adjacency_changes  device_name  port  count  count_operator  level

# API Function: isis_verify_port_init_fails
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_port_init_fails(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_port_init_fails  device_name  port  count  count_operator  level

# API Function: isis_verify_port_rejected_adjancencies
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_port_rejected_adjancencies(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_port_rejected_adjancencies  device_name  port  count  count_operator  level

# API Function: isis_verify_port_id_field_length_mismatches
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_port_id_field_length_mismatches(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_port_id_field_length_mismatches  device_name  port  count  count_operator  level

# API Function: isis_verify_port_max_area_address_mismatches
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_port_max_area_address_mismatches(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_port_max_area_address_mismatches  device_name  port  count  count_operator  level

# API Function: isis_verify_port_designated_is_changes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_port_designated_is_changes(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_port_designated_is_changes  device_name  port  count  count_operator  level

# API Function: isis_verify_l1_port_hellos_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_port_hellos_transmitted(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_port_hellos_transmitted  device_name  port  count  count_operator  level

# API Function: isis_verify_l1_port_hellos_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_port_hellos_received(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_port_hellos_received  device_name  port  count  count_operator  level

# API Function: isis_verify_l1_port_lsps_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_port_lsps_transmitted(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_port_lsps_transmitted  device_name  port  count  count_operator  level

# API Function: isis_verify_l1_port_lsps_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_port_lsps_received(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_port_lsps_received  device_name  port  count  count_operator  level

# API Function: isis_verify_l1_port_csnps_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_port_csnps_transmitted(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_port_csnps_transmitted  device_name  port  count  count_operator  level

# API Function: isis_verify_l1_port_csnps_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_port_csnps_received(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_port_csnps_received  device_name  port  count  count_operator  level

# API Function: isis_verify_l1_port_psnps_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_port_psnps_transmitted(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_port_psnps_transmitted  device_name  port  count  count_operator  level

# API Function: isis_verify_l1_port_psnps_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_port_psnps_received(device_name, port, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_port_psnps_received  device_name  port  count  count_operator  level

# API Function: isis_verify_mlt_auth_fails
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_mlt_auth_fails(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_mlt_auth_fails  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_mlt_adjacency_changes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_mlt_adjacency_changes(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_mlt_adjacency_changes  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_mlt_init_fails
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_mlt_init_fails(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_mlt_init_fails  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_mlt_rejected_adjancencies
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_mlt_rejected_adjancencies(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_mlt_rejected_adjancencies  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_mlt_id_field_length_mismatches
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_mlt_id_field_length_mismatches(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_mlt_id_field_length_mismatches  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_mlt_max_area_address_mismatches
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_mlt_max_area_address_mismatches(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_mlt_max_area_address_mismatches  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_mlt_designated_is_changes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_mlt_designated_is_changes(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_mlt_designated_is_changes  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_l1_mlt_hellos_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_mlt_hellos_transmitted(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_mlt_hellos_transmitted  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_l1_mlt_hellos_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_mlt_hellos_received(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_mlt_hellos_received  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_l1_mlt_lsps_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_mlt_lsps_transmitted(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_mlt_lsps_transmitted  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_l1_mlt_lsps_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_mlt_lsps_received(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_mlt_lsps_received  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_l1_mlt_csnps_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_mlt_csnps_transmitted(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_mlt_csnps_transmitted  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_l1_mlt_csnps_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_mlt_csnps_received(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_mlt_csnps_received  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_l1_mlt_psnps_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_mlt_psnps_transmitted(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_mlt_psnps_transmitted  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_l1_mlt_psnps_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_mlt_psnps_received(device_name, mlt_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_mlt_psnps_received  device_name  mlt_id  count  count_operator  level

# API Function: isis_verify_logical_interface_auth_fails
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_auth_fails(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_logical_interface_auth_fails  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_logical_interface_adjacency_changes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_adjacency_changes(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_logical_interface_adjacency_changes  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_logical_interface_init_fails
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_init_fails(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_logical_interface_init_fails  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_logical_interface_rejected_adjancencies
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_rejected_adjancencies(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_logical_interface_rejected_adjancencies  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_logical_interface_id_field_length_mismatches
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_id_field_length_mismatches(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_logical_interface_id_field_length_mismatches  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_logical_interface_max_area_address_mismatches
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_max_area_address_mismatches(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_logical_interface_max_area_address_mismatches  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_logical_interface_designated_is_changes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_logical_interface_designated_is_changes(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_logical_interface_designated_is_changes  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_l1_logical_interface_hellos_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_logical_interface_hellos_transmitted(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_logical_interface_hellos_transmitted  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_l1_logical_interface_hellos_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_logical_interface_hellos_received(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_logical_interface_hellos_received  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_l1_logical_interface_lsps_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_logical_interface_lsps_transmitted(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_logical_interface_lsps_transmitted  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_l1_logical_interface_lsps_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_logical_interface_lsps_received(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_logical_interface_lsps_received  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_l1_logical_interface_csnps_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_logical_interface_csnps_transmitted(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_logical_interface_csnps_transmitted  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_l1_logical_interface_csnps_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_logical_interface_csnps_received(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_logical_interface_csnps_received  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_l1_logical_interface_psnps_transmitted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_logical_interface_psnps_transmitted(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_logical_interface_psnps_transmitted  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_l1_logical_interface_psnps_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_l1_logical_interface_psnps_received(device_name, isis_id, count, count_operator, level)

	Robot API Call: 

		isis_verify_l1_logical_interface_psnps_received  device_name  isis_id  count  count_operator  level

# API Function: isis_verify_ipv4_source_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_ipv4_source_address(device_name, ip)

	Robot API Call: 

		isis_verify_ipv4_source_address  device_name  ip

# API Function: isis_verify_ipv4_source_address_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_ipv4_source_address_does_not_exist(device_name, ip)

	Robot API Call: 

		isis_verify_ipv4_source_address_does_not_exist  device_name  ip

# API Function: isis_verify_ipv6_source_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_ipv6_source_address(device_name, ipv6_addr)

	Robot API Call: 

		isis_verify_ipv6_source_address  device_name  ipv6_addr

# API Function: isis_verify_ipv6_source_address_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_ipv6_source_address_does_not_exist(device_name, ipv6_addr)

	Robot API Call: 

		isis_verify_ipv6_source_address_does_not_exist  device_name  ipv6_addr

# API Function: isis_verify_ipv4_tunnel_source_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_ipv4_tunnel_source_address(device_name, ip)

	Robot API Call: 

		isis_verify_ipv4_tunnel_source_address  device_name  ip

# API Function: isis_verify_ipv4_tunnel_source_address_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_ipv4_tunnel_source_address_does_not_exist(device_name, ip)

	Robot API Call: 

		isis_verify_ipv4_tunnel_source_address_does_not_exist  device_name  ip

# API Function: isis_verify_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_redistribute_direct(device_name)

	Robot API Call: 

		isis_verify_redistribute_direct  device_name

# API Function: isis_verify_redistribute_direct_not_set
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_redistribute_direct_not_set(device_name)

	Robot API Call: 

		isis_verify_redistribute_direct_not_set  device_name

# API Function: isis_verify_redistribute_direct_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_redistribute_direct_enabled(device_name)

	Robot API Call: 

		isis_verify_redistribute_direct_enabled  device_name

# API Function: isis_verify_redistribute_direct_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_redistribute_direct_disabled(device_name)

	Robot API Call: 

		isis_verify_redistribute_direct_disabled  device_name

# API Function: isis_verify_redistribute_direct_ipv6_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_redistribute_direct_ipv6_enabled(device_name)

	Robot API Call: 

		isis_verify_redistribute_direct_ipv6_enabled  device_name

# API Function: isis_verify_redistribute_direct_ipv6_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_redistribute_direct_ipv6_disabled(device_name)

	Robot API Call: 

		isis_verify_redistribute_direct_ipv6_disabled  device_name

# API Function: isis_verify_redistribute_direct_route_map_policy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_redistribute_direct_route_map_policy(device_name, policy_name)

	Robot API Call: 

		isis_verify_redistribute_direct_route_map_policy  device_name  policy_name

# API Function: isis_verify_redistribute_direct_route_map_policy_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.isis.isis_verify_redistribute_direct_route_map_policy_does_not_exist(device_name, policy_name)

	Robot API Call: 

		isis_verify_redistribute_direct_route_map_policy_does_not_exist  device_name  policy_name

