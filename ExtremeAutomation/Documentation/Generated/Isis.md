# Keyword Library Documentation for Isis
This feature is located in this file: `isis.yaml` (in this directory: econ-automation-framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /econ-automation-framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/econ-automation-framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_global(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_global(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_system_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_system_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_manual_area(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_manual_area(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_sys_name(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_sys_name(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_ipv4_source_address(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_ipv4_source_address(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_ipv6_source_address(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_ipv6_source_address(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_ipv4_tunnel_source_address(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_ipv4_tunnel_source_address(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_inband_mgmt_ip(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_inband_mgmt_ip(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_metric_narrow(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_metric_narrow(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_metric_wide(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_metric_wide(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_overload(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_overload(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_redistribute_bgp(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_redistribute_bgp(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_redistribute_bgp(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_redistribute_bgp(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_redistribute_direct(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_redistribute_direct(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_redistribute_direct(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_redistribute_direct(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_redistribute_direct_ipv6(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_redistribute_direct_ipv6(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_redistribute_direct_apply(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_redistribute_direct_route_map_policy(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_redistribute_direct_route_map_policy(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_redistribute_ospf(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_redistribute_ospf(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_redistribute_ospf(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_redistribute_ospf(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_redistribute_rip(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_redistribute_rip(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_redistribute_rip(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_redistribute_rip(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_redistribute_static(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_redistribute_static(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_redistribute_static(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_redistribute_static(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_redistribute_apply(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_spf_delay(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_spf_delay(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_circuit_on_port(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_circuit_on_port(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_circuit_on_port(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_circuit_on_port(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_circuit_on_mlt(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_circuit_on_mlt(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_circuit_on_mlt(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_circuit_on_mlt(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_auth_on_port(device_name, port, auth_type, key_id, auth_key)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_auth_on_mlt(device_name, mlt_id, auth_type, key_id, auth_key)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_auth_on_port(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_auth_on_mlt(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_l1_dr_priority_on_port(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_l1_dr_priority_on_mlt(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_l1_hello_interval_on_port(device_name, port, interval)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_l1_hello_interval_on_mlt(device_name, mlt_id, interval)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_l1_hello_multiplier_on_port(device_name, port, multiplier)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_l1_hello_multiplier_on_mlt(device_name, mlt_id, multiplier)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_logical_interface_port(device_name, isis_id, primary_vlan, secondary_vlan, port)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_logical_interface_port_name(device_name, isis_id, primary_vlan, secondary_vlan, port, name)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_logical_interface_mlt(device_name, isis_id, primary_vlan, secondary_vlan, mlt_id)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_logical_interface_mlt_name(device_name, isis_id, primary_vlan, secondary_vlan, mlt_id, name)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_logical_interface_ipv4(device_name, isis_id, ip)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_logical_interface_ipv4_name(device_name, isis_id, ip, name)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_logical_interface(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_circuit_on_logical_interface(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_enable_circuit_on_logical_interface(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_disable_circuit_on_logical_interface(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_circuit_on_logical_interface(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_auth_on_logical_interface(device_name, isis_id, auth_type, key_id, auth_key)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_clear_auth_on_logical_interface(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_l1_dr_priority_on_logical_interface(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_l1_hello_interval_on_logical_interface(device_name, isis_id, interval)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_set_l1_hello_multiplier_on_logical_interface(device_name, isis_id, multiplier)

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


# API Function: show_circuit
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_circuit(device_name )

	Robot API Call: 

		isis_show_circuit  device_name  

UUID: fa0140f5-6c5c-496f-af68-3630be0f284e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.1.{isis_circuit}

----------------------------------------------


# API Function: show_circuit_interfaces
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_circuit_interfaces(device_name )

	Robot API Call: 

		isis_show_circuit_interfaces  device_name  

UUID: ec8e2aef-a43d-46f8-b78c-819f227e30f0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis int-ckt-level

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1.2

----------------------------------------------


# API Function: show_info
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_info(device_name )

	Robot API Call: 

		isis_show_info  device_name  

UUID: 1826c2f3-c01c-4da5-8c56-c21538da2331
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1||1.3.6.1.4.1.2272.1.63.1

----------------------------------------------


# API Function: show_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_interface(device_name )

	Robot API Call: 

		isis_show_interface  device_name  

UUID: c777e704-4043-4a2c-9b9d-4afb8d796f73
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis interface

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.3.2.1||1.3.6.1.4.1.2272.1.63.2.1

----------------------------------------------


# API Function: show_interface_l1
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_interface_l1(device_name )

	Robot API Call: 

		isis_show_interface_l1  device_name  

UUID: 3270ac3e-7cd1-4ecc-948a-0342954e2d7f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis interface l1

----------------------------------------------


## REST
## SNMP
# API Function: show_interface_l2
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_interface_l2(device_name )

	Robot API Call: 

		isis_show_interface_l2  device_name  

UUID: cdd357c7-9811-4a73-8e48-4626efc720de
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis interface l2

----------------------------------------------


## REST
## SNMP
# API Function: show_interface_l12
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_interface_l12(device_name )

	Robot API Call: 

		isis_show_interface_l12  device_name  

UUID: 70c576f5-4160-4f6e-868e-d481e14504ce
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis interface l12

----------------------------------------------


## REST
## SNMP
# API Function: show_area
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_area(device_name )

	Robot API Call: 

		isis_show_area  device_name  

UUID: 9f7194d9-1204-43b3-80f8-34c7e1d7960a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis area

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1.3.1.1

----------------------------------------------


# API Function: show_lsdb
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_lsdb(device_name )

	Robot API Call: 

		isis_show_lsdb  device_name  

UUID: f0ef2ee5-4617-4d8d-b767-2fbaf1a576b1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis lsdb

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.9

----------------------------------------------


# API Function: show_manual_area
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_manual_area(device_name )

	Robot API Call: 

		isis_show_manual_area  device_name  

UUID: 587dbeea-5f2c-448f-b305-31d4429f7afd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis manual-area

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1.2.1.2

----------------------------------------------


# API Function: show_net
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_net(device_name )

	Robot API Call: 

		isis_show_net  device_name  

UUID: 15e262ad-c217-41cb-ac39-469e95afb303
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis net

----------------------------------------------


## REST
## SNMP
# API Function: show_spb_mcast_summary
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_spb_mcast_summary(device_name )

	Robot API Call: 

		isis_show_spb_mcast_summary  device_name  

UUID: fa374b1a-c8b9-4a51-ad46-01a5332dfe28
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spb-mcast-summary

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.14||1.3.6.1.4.1.2272.1.63.24

----------------------------------------------


# API Function: show_statistics
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_statistics(device_name )

	Robot API Call: 

		isis_show_statistics  device_name  

UUID: ad804fc6-b117-45c2-afd6-2bf8eed49c9a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis statistics

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.5

----------------------------------------------


# API Function: show_sys_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_sys_id(device_name )

	Robot API Call: 

		isis_show_sys_id  device_name  

UUID: a7366f3d-a071-4250-9bad-75e339c290a8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis system-id

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.1.1.3.0

----------------------------------------------


# API Function: show_adjacencies
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_adjacencies(device_name )

	Robot API Call: 

		isis_show_adjacencies  device_name  

UUID: 6a1f17f2-f7bf-47c1-b0a8-91f887bc7448
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis adjacencies

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.10||1.3.6.1.3.37.1.6

----------------------------------------------


# API Function: show_interface_auth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_interface_auth(device_name )

	Robot API Call: 

		isis_show_interface_auth  device_name  

UUID: cd9d0273-3446-46b2-ae13-24fef1351b00
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis int-auth

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.2

----------------------------------------------


# API Function: show_interface_timers
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_interface_timers(device_name )

	Robot API Call: 

		isis_show_interface_timers  device_name  

UUID: 571b9c9e-0ef6-479f-bd01-92f201db29ab
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis int-timers

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.4.1

----------------------------------------------


# API Function: show_lsdb_ip_unicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_lsdb_ip_unicast(device_name )

	Robot API Call: 

		isis_show_lsdb_ip_unicast  device_name  

UUID: 1015aaee-1c15-4f93-8227-cb2a46b70620
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis lsdb ip-unicast

----------------------------------------------


## REST
## SNMP
# API Function: show_system_stats
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_system_stats(device_name )

	Robot API Call: 

		isis_show_system_stats  device_name  

UUID: f50ea600-252c-4654-aa21-403f27015b68
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis statistics

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.5.1

----------------------------------------------


# API Function: show_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_logical_interface(device_name )

	Robot API Call: 

		isis_show_logical_interface  device_name  

UUID: d5433420-d9b3-4d4b-884f-3029de321fa5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis logical-interface

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.26

----------------------------------------------


# API Function: show_logical_interface_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_logical_interface_name(device_name )

	Robot API Call: 

		isis_show_logical_interface_name  device_name  

UUID: 66e013fd-54e2-4b0c-b13f-62e93c7b50ff
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis logical-interface name

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.26.1.8

----------------------------------------------


# API Function: show_interface_stats
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_interface_stats(device_name )

	Robot API Call: 

		isis_show_interface_stats  device_name  

UUID: 6aa9eeb8-a02d-45ab-8da8-1c0f63568b02
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis int-counters

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.5.2

----------------------------------------------


# API Function: show_interface_l1_packet_stats
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_interface_l1_packet_stats(device_name )

	Robot API Call: 

		isis_show_interface_l1_packet_stats  device_name  

UUID: f9500aff-4ba2-4d02-899a-c40aa15b9250
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis int-l1-cntl-pkts

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.5.3

----------------------------------------------


# API Function: show_interface_l2_packet_stats
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_interface_l2_packet_stats(device_name )

	Robot API Call: 

		isis_show_interface_l2_packet_stats  device_name  

UUID: 42dd923e-ebff-4ca2-9325-9ffd25aff56c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis int-l2-cntl-pkts

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.3.37.1.5.3

----------------------------------------------


# API Function: show_ip_redistribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_ip_redistribute(device_name )

	Robot API Call: 

		isis_show_ip_redistribute  device_name  

UUID: 403df57b-93f9-4239-bf4f-5acacada817e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip isis redistribute

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.8.100.22

----------------------------------------------


# API Function: show_ipv6_redistribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementIsisGenKeywords.isis_show_ipv6_redistribute(device_name )

	Robot API Call: 

		isis_show_ipv6_redistribute  device_name  

UUID: ec788ef5-15d9-4ddb-ab3e-ea02bc9c0b71
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ipv6 isis redistribute

----------------------------------------------


## REST
## SNMP
