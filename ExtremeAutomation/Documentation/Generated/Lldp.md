# Command Keyword Library Documentation for Lldp
This feature is located in this file: `lldp.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable(device_name )

	Robot API Call: 

		lldp_enable  device_name  

UUID: 67f68e1a-af05-4d32-88a4-cc8e0f989c1d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		protocol lldp||no disable

----------------------------------------------


## REST
## SNMP
# API Function: disable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable(device_name )

	Robot API Call: 

		lldp_disable  device_name  

UUID: aeb4b061-2335-490b-8db6-3006da23f70c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		protocol lldp||disable

----------------------------------------------


## REST
## SNMP
# API Function: enable_tx
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tx(device_name )

	Robot API Call: 

		lldp_enable_tx  device_name  

UUID: f8731a63-99ec-43da-8014-df6422405b96
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		protocol lldp||mode tx

----------------------------------------------


## REST
## SNMP
# API Function: enable_rx
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_rx(device_name )

	Robot API Call: 

		lldp_enable_rx  device_name  

UUID: be159c63-7f03-4bb2-b299-78ecf619481f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		protocol lldp||mode rx

----------------------------------------------


## REST
## SNMP
# API Function: enable_port_tx
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_port_tx(device_name )

	Robot API Call: 

		lldp_enable_port_tx  device_name  

UUID: e6946508-8d34-4463-b62c-6c89f5fce29c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port status tx-enable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable lldp ports {port} transmit-only

----------------------------------------------


## REST
## SNMP
# API Function: enable_port_rx
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_port_rx(device_name )

	Robot API Call: 

		lldp_enable_port_rx  device_name  

UUID: b72e04e4-15c2-4027-a94c-2c6600bfc20a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port status rx-enable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable lldp ports {port} receive-only

----------------------------------------------


## REST
## SNMP
# API Function: enable_port_both
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_port_both(device_name )

	Robot API Call: 

		lldp_enable_port_both  device_name  

UUID: b674aaf4-2510-4811-9f2e-e11b1bc7a612
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port status both {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable lldp ports {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: interface ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no lldp disable 

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-lldp:lldp

----------------------------------------------


## SNMP
# API Function: disable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_port(device_name )

	Robot API Call: 

		lldp_disable_port  device_name  

UUID: 9e2d8119-4960-41d5-9bc6-252c40fc311b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port status disable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable lldp ports {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: interface ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		lldp disable

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /rest/restconf/data/openconfig-lldp:lldp

----------------------------------------------


## SNMP
# API Function: set_tx_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_set_tx_interval(device_name )

	Robot API Call: 

		lldp_set_tx_interval  device_name  

UUID: 6d9bd153-8795-4c40-95f3-2a06039393b9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp tx-interval {interval}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp transmit-interval {interval}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		lldp tx-interval {interval}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		protocol lldp||hello {interval}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.0.8802.1.1.2.1.1.1.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.0.8802.1.1.2.1.1.1.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.0.8802.1.1.2.1.1.1.0

----------------------------------------------


# API Function: set_sys_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_set_sys_name(device_name )

	Robot API Call: 

		lldp_set_sys_name  device_name  

UUID: fe626814-f3f4-42ac-944c-40400ddaa99f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		protocol lldp||system-name}

----------------------------------------------


## REST
## SNMP
# API Function: clear_sys_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_clear_sys_name(device_name )

	Robot API Call: 

		lldp_clear_sys_name  device_name  

UUID: 93ea05f4-ff67-417c-a8a9-4a783a235148
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		protocol lldp||no system-name {name}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_set_profile(device_name )

	Robot API Call: 

		lldp_set_profile  device_name  

UUID: a64f240a-088e-441c-84ce-af505854e62e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		protocol lldp||profile {profile}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_set_profile_interface(device_name )

	Robot API Call: 

		lldp_set_profile_interface  device_name  

UUID: 31de4be9-c656-4bd9-a8d0-6a0aa35b9827
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: interface ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		lldp profile {profile}

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_all(device_name )

	Robot API Call: 

		lldp_enable_tlv_all  device_name  

UUID: b87c2fc6-002d-4b4d-bc16-269649cecdf1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv all {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise all-tlvs

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_all(device_name )

	Robot API Call: 

		lldp_disable_tlv_all  device_name  

UUID: ea8c4361-a4d8-46cd-98d0-2883ddf8cda5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv all {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise all-tlvs

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_port_desc
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_port_desc(device_name )

	Robot API Call: 

		lldp_enable_tlv_port_desc  device_name  

UUID: 243e2cdd-76ec-4b10-8f24-56d1dade6b1e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv port-desc {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise port-description

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_port_desc
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_port_desc(device_name )

	Robot API Call: 

		lldp_disable_tlv_port_desc  device_name  

UUID: a2f0e913-05b3-4b17-8e87-8734ca8a4ce2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv port-desc {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise port-description

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_sys_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_sys_name(device_name )

	Robot API Call: 

		lldp_enable_tlv_sys_name  device_name  

UUID: 1f43c317-9cd6-4523-8a75-f672666fcc8a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv sys-name {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise system-name

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_sys_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_sys_name(device_name )

	Robot API Call: 

		lldp_disable_tlv_sys_name  device_name  

UUID: 5b05361b-96d9-4deb-b82c-7f1e2979c976
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv sys-name {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise system-name

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_sys_desc
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_sys_desc(device_name )

	Robot API Call: 

		lldp_enable_tlv_sys_desc  device_name  

UUID: 92eb5100-f65a-4596-8a20-73adb056d328
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv sys-desc {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise system-description

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_sys_desc
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_sys_desc(device_name )

	Robot API Call: 

		lldp_disable_tlv_sys_desc  device_name  

UUID: 6224f79f-4236-4161-8e60-1d3abb1fa87c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv sys-desc {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise system-description

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_sys_cap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_sys_cap(device_name )

	Robot API Call: 

		lldp_enable_tlv_sys_cap  device_name  

UUID: 8fabfec5-88d0-45ae-8f46-0a6d86b6a8e3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv sys-cap {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise system-capabilities

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_sys_cap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_sys_cap(device_name )

	Robot API Call: 

		lldp_disable_tlv_sys_cap  device_name  

UUID: 3c0cd7be-4edf-4816-8fed-62171d39d293
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv sys-cap {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise system-capabilities

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_mgmt_addr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_mgmt_addr(device_name )

	Robot API Call: 

		lldp_enable_tlv_mgmt_addr  device_name  

UUID: 7b4f3527-942b-4730-bffb-4a74bb673f83
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv mgmt-addr {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise management-address

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_mgmt_addr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_mgmt_addr(device_name )

	Robot API Call: 

		lldp_disable_tlv_mgmt_addr  device_name  

UUID: 7925caba-a530-4639-831d-57795d4a7c51
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv mgmt-addr {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise management-address

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_vlan_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_vlan_id(device_name )

	Robot API Call: 

		lldp_enable_tlv_vlan_id  device_name  

UUID: 0f0b8b56-beb6-4c81-afda-87ecc3aee353
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv vlan-id {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific dot1 port-vlan-id

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_vlan_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_vlan_id(device_name )

	Robot API Call: 

		lldp_disable_tlv_vlan_id  device_name  

UUID: 5cba4f56-6f30-4f85-a289-7ad1c77794c1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv vlan-id {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific dot1 port-vlan-id

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_stp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_stp(device_name )

	Robot API Call: 

		lldp_enable_tlv_stp  device_name  

UUID: bc2117f1-b152-4837-9dcb-5cef7486f8eb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv stp {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_stp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_stp(device_name )

	Robot API Call: 

		lldp_disable_tlv_stp  device_name  

UUID: e5b114b3-f94c-4711-9ded-047064dfb083
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv stp {port}

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_lacp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_lacp(device_name )

	Robot API Call: 

		lldp_enable_tlv_lacp  device_name  

UUID: 8953e640-7f5a-441b-8ef4-27ea2d027c74
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv lacp {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_lacp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_lacp(device_name )

	Robot API Call: 

		lldp_disable_tlv_lacp  device_name  

UUID: 7febd848-9247-45bf-9b7e-54335a947b96
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv lacp {port}

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_gvrp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_gvrp(device_name )

	Robot API Call: 

		lldp_enable_tlv_gvrp  device_name  

UUID: 5ede15e9-fc5e-402c-b5db-4f234218894b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv gvrp {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_gvrp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_gvrp(device_name )

	Robot API Call: 

		lldp_disable_tlv_gvrp  device_name  

UUID: 872228d2-f196-4f8e-812d-1a1c141e2c0e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv gvrp {port}

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_mac_phy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_mac_phy(device_name )

	Robot API Call: 

		lldp_enable_tlv_mac_phy  device_name  

UUID: 58cce8d3-d1e4-44ee-8d2c-93df254cb67c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv mac-phy {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific dot3 mac-phy

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_mac_phy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_mac_phy(device_name )

	Robot API Call: 

		lldp_disable_tlv_mac_phy  device_name  

UUID: 3026e5b5-721b-4e26-af59-092bee7db3e2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv mac-phy {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific dot3 mac-phy

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_poe
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_poe(device_name )

	Robot API Call: 

		lldp_enable_tlv_poe  device_name  

UUID: f690f55d-0899-4a4a-bf9e-9b6f5eddbb3e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv poe {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific dot3 power-via-midi

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_poe
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_poe(device_name )

	Robot API Call: 

		lldp_disable_tlv_poe  device_name  

UUID: 9d5ce203-14af-40df-ba2b-a1ec958fd9b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv poe {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific dot3 power-via-midi

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_link_aggr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_link_aggr(device_name )

	Robot API Call: 

		lldp_enable_tlv_link_aggr  device_name  

UUID: 4998957c-135b-475e-be63-8ce458785948
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv link-aggr {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific dot3 link-aggregation

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_link_aggr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_link_aggr(device_name )

	Robot API Call: 

		lldp_disable_tlv_link_aggr  device_name  

UUID: 76d7d5cd-5ddf-4113-9d77-58d84e87500e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv link-aggr {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific dot3 link-aggregation

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_max_frame
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_max_frame(device_name )

	Robot API Call: 

		lldp_enable_tlv_max_frame  device_name  

UUID: 3be2d985-95d5-49dc-b629-aee16614268c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv max-frame {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific dot3 max-frame-size

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_max_frame
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_max_frame(device_name )

	Robot API Call: 

		lldp_disable_tlv_max_frame  device_name  

UUID: 09945c31-ed11-4ff1-ac7a-7c4d864860b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv max-frame {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific dot3 max-frame-size

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_med_cap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_med_cap(device_name )

	Robot API Call: 

		lldp_enable_tlv_med_cap  device_name  

UUID: 552405ea-e481-40b1-95a6-a552f4510004
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv med-cap {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific med capabilities

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_med_cap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_med_cap(device_name )

	Robot API Call: 

		lldp_disable_tlv_med_cap  device_name  

UUID: 3cc242e9-6b38-4584-b7f3-0481c092e9a9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv med-cap {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific med capabilities

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_med_pol
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_med_pol(device_name )

	Robot API Call: 

		lldp_enable_tlv_med_pol  device_name  

UUID: d465bbdc-1a1d-4e99-a5d4-6a65050ddd8c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv med-pol {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific med policy

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_med_pol
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_med_pol(device_name )

	Robot API Call: 

		lldp_disable_tlv_med_pol  device_name  

UUID: 96f950c4-4fff-429e-90c6-6641d2b8d811
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv med-pol {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific med policy

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_med_loc
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_med_loc(device_name )

	Robot API Call: 

		lldp_enable_tlv_med_loc  device_name  

UUID: 8fa838ad-7193-4b74-8e09-da9083f5483a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv med-loc {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific med location-identification {type} {value}

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_med_loc
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_med_loc(device_name )

	Robot API Call: 

		lldp_disable_tlv_med_loc  device_name  

UUID: 8ca06470-435a-4f4c-8cc3-80623ffa9883
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv med-loc {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific med location-identification {type} {value}

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_med_poe
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_med_poe(device_name )

	Robot API Call: 

		lldp_enable_tlv_med_poe  device_name  

UUID: 9a5a8eb2-b647-4eba-b0cd-41259fca8ae5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv med-poe {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific med power-via-midi

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_med_poe
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_med_poe(device_name )

	Robot API Call: 

		lldp_disable_tlv_med_poe  device_name  

UUID: dda342f7-4bb8-478f-bbf5-cd2511ea3063
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv med-poe {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific med power-via-midi

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_enhanced_trans_config
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_enhanced_trans_config(device_name )

	Robot API Call: 

		lldp_enable_tlv_enhanced_trans_config  device_name  

UUID: abe67216-3fe5-4952-83c6-ccf4c0b802c4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv enhanced-trans-config {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific dcbx ieee

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_enhanced_trans_config
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_enhanced_trans_config(device_name )

	Robot API Call: 

		lldp_disable_tlv_enhanced_trans_config  device_name  

UUID: d58a86f9-c2de-4c79-afac-de230fbbe546
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv enhanced-trans-config {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific dcbx ieee

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_enhanced_trans_rec
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_enhanced_trans_rec(device_name )

	Robot API Call: 

		lldp_enable_tlv_enhanced_trans_rec  device_name  

UUID: 63d89deb-76ff-4f3f-b069-bbd8febe8f17
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv enhanced-trans-rec {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} advertise vendor-specific dcbx ieee

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_enhanced_trans_rec
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_enhanced_trans_rec(device_name )

	Robot API Call: 

		lldp_disable_tlv_enhanced_trans_rec  device_name  

UUID: 59e71132-ab0e-473b-8dbf-a243b6102559
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv enhanced-trans-rec {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure lldp ports {port} no-advertise vendor-specific dcbx ieee

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_priority_flowctrl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_priority_flowctrl(device_name )

	Robot API Call: 

		lldp_enable_tlv_priority_flowctrl  device_name  

UUID: 5e1ab984-d780-4447-ab3d-220c2bebf35a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv priority-flowctrl {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_priority_flowctrl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_priority_flowctrl(device_name )

	Robot API Call: 

		lldp_disable_tlv_priority_flowctrl  device_name  

UUID: deeddb93-b780-488c-b18a-0830b8c23800
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv priority-flowctrl {port}

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_application_pri
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_application_pri(device_name )

	Robot API Call: 

		lldp_enable_tlv_application_pri  device_name  

UUID: 8a7f77d1-2cfa-473d-943a-5cefdd286c46
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv application-pri {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_application_pri
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_application_pri(device_name )

	Robot API Call: 

		lldp_disable_tlv_application_pri  device_name  

UUID: 61ebed67-8ee2-45b2-9c7b-50b5b3dba5c5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv application-pri {port}

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_congestion_notif
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_congestion_notif(device_name )

	Robot API Call: 

		lldp_enable_tlv_congestion_notif  device_name  

UUID: a8408611-f3e6-4d15-93f6-bfa1463e9a72
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv congestion-notif {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_congestion_notif
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_congestion_notif(device_name )

	Robot API Call: 

		lldp_disable_tlv_congestion_notif  device_name  

UUID: fa7dd0f8-893d-420f-a3d7-1330333dba5c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv congestion-notif {port}

----------------------------------------------


## REST
## SNMP
# API Function: enable_tlv_energy_eff_eth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_enable_tlv_energy_eff_eth(device_name )

	Robot API Call: 

		lldp_enable_tlv_energy_eff_eth  device_name  

UUID: 174b1a07-724a-4859-87cb-c356c6cf5de1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lldp port tx-tlv energy-eff-eth {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_tlv_energy_eff_eth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_disable_tlv_energy_eff_eth(device_name )

	Robot API Call: 

		lldp_disable_tlv_energy_eff_eth  device_name  

UUID: 37c1b5b7-f2c4-4a11-8f71-6f71ddedec67
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lldp port tx-tlv energy-eff-eth {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_tx_hold_multiplier
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_set_tx_hold_multiplier(device_name )

	Robot API Call: 

		lldp_set_tx_hold_multiplier  device_name  

UUID: 66eb3cef-0c24-4f81-b8f4-123be3838a24
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		lldp tx-hold-multiplier {multiplier}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		protocol lldp||multiplier {multiplier}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.0.8802.1.1.2.1.1.2.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.0.8802.1.1.2.1.1.2.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.0.8802.1.1.2.1.1.2.0

----------------------------------------------


# API Function: lldp_verify_tx_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_tx_interval(device_name, interval)

	Robot API Call: 

		lldp_verify_tx_interval  device_name  interval

# API Function: lldp_verify_tx_hold_multiplier
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_tx_hold_multiplier(device_name, multiplier)

	Robot API Call: 

		lldp_verify_tx_hold_multiplier  device_name  multiplier

# API Function: lldp_verify_port_desc_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_port_desc_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_port_desc_tlv_enabled  device_name  port

# API Function: lldp_verify_port_desc_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_port_desc_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_port_desc_tlv_disabled  device_name  port

# API Function: lldp_verify_sys_name_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_sys_name_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_sys_name_tlv_enabled  device_name  port

# API Function: lldp_verify_sys_name_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_sys_name_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_sys_name_tlv_disabled  device_name  port

# API Function: lldp_verify_sys_desc_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_sys_desc_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_sys_desc_tlv_enabled  device_name  port

# API Function: lldp_verify_sys_desc_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_sys_desc_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_sys_desc_tlv_disabled  device_name  port

# API Function: lldp_verify_sys_cap_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_sys_cap_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_sys_cap_tlv_enabled  device_name  port

# API Function: lldp_verify_sys_cap_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_sys_cap_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_sys_cap_tlv_disabled  device_name  port

# API Function: lldp_verify_mgmt_addr_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_mgmt_addr_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_mgmt_addr_tlv_enabled  device_name  port

# API Function: lldp_verify_mgmt_addr_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_mgmt_addr_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_mgmt_addr_tlv_disabled  device_name  port

# API Function: lldp_verify_vlan_id_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_vlan_id_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_vlan_id_tlv_enabled  device_name  port

# API Function: lldp_verify_vlan_id_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_vlan_id_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_vlan_id_tlv_disabled  device_name  port

# API Function: lldp_verify_stp_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_stp_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_stp_tlv_enabled  device_name  port

# API Function: lldp_verify_stp_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_stp_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_stp_tlv_disabled  device_name  port

# API Function: lldp_verify_lacp_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_lacp_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_lacp_tlv_enabled  device_name  port

# API Function: lldp_verify_lacp_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_lacp_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_lacp_tlv_disabled  device_name  port

# API Function: lldp_verify_gvrp_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_gvrp_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_gvrp_tlv_enabled  device_name  port

# API Function: lldp_verify_gvrp_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_gvrp_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_gvrp_tlv_disabled  device_name  port

# API Function: lldp_verify_mac_phy_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_mac_phy_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_mac_phy_tlv_enabled  device_name  port

# API Function: lldp_verify_mac_phy_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_mac_phy_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_mac_phy_tlv_disabled  device_name  port

# API Function: lldp_verify_poe_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_poe_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_poe_tlv_enabled  device_name  port

# API Function: lldp_verify_poe_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_poe_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_poe_tlv_disabled  device_name  port

# API Function: lldp_verify_link_aggr_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_link_aggr_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_link_aggr_tlv_enabled  device_name  port

# API Function: lldp_verify_link_aggr_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_link_aggr_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_link_aggr_tlv_disabled  device_name  port

# API Function: lldp_verify_max_frame_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_max_frame_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_max_frame_tlv_enabled  device_name  port

# API Function: lldp_verify_max_frame_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_max_frame_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_max_frame_tlv_disabled  device_name  port

# API Function: lldp_verify_med_cap_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_med_cap_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_med_cap_tlv_enabled  device_name  port

# API Function: lldp_verify_med_cap_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_med_cap_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_med_cap_tlv_disabled  device_name  port

# API Function: lldp_verify_med_pol_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_med_pol_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_med_pol_tlv_enabled  device_name  port

# API Function: lldp_verify_med_pol_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_med_pol_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_med_pol_tlv_disabled  device_name  port

# API Function: lldp_verify_med_loc_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_med_loc_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_med_loc_tlv_enabled  device_name  port

# API Function: lldp_verify_med_loc_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_med_loc_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_med_loc_tlv_disabled  device_name  port

# API Function: lldp_verify_med_poe_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_med_poe_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_med_poe_tlv_enabled  device_name  port

# API Function: lldp_verify_med_poe_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_med_poe_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_med_poe_tlv_disabled  device_name  port

# API Function: lldp_verify_enhanced_trans_config_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_enhanced_trans_config_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_enhanced_trans_config_tlv_enabled  device_name  port

# API Function: lldp_verify_enhanced_trans_config_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_enhanced_trans_config_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_enhanced_trans_config_tlv_disabled  device_name  port

# API Function: lldp_verify_enhanced_trans_rec_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_enhanced_trans_rec_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_enhanced_trans_rec_tlv_enabled  device_name  port

# API Function: lldp_verify_enhanced_trans_rec_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_enhanced_trans_rec_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_enhanced_trans_rec_tlv_disabled  device_name  port

# API Function: lldp_verify_priority_flowctrl_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_priority_flowctrl_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_priority_flowctrl_tlv_enabled  device_name  port

# API Function: lldp_verify_priority_flowctrl_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_priority_flowctrl_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_priority_flowctrl_tlv_disabled  device_name  port

# API Function: lldp_verify_application_pri_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_application_pri_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_application_pri_tlv_enabled  device_name  port

# API Function: lldp_verify_application_pri_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_application_pri_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_application_pri_tlv_disabled  device_name  port

# API Function: lldp_verify_congestion_notif_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_congestion_notif_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_congestion_notif_tlv_enabled  device_name  port

# API Function: lldp_verify_congestion_notif_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_congestion_notif_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_congestion_notif_tlv_disabled  device_name  port

# API Function: lldp_verify_energy_eff_eth_tlv_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_energy_eff_eth_tlv_enabled(device_name, port)

	Robot API Call: 

		lldp_verify_energy_eff_eth_tlv_enabled  device_name  port

# API Function: lldp_verify_energy_eff_eth_tlv_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_energy_eff_eth_tlv_disabled(device_name, port)

	Robot API Call: 

		lldp_verify_energy_eff_eth_tlv_disabled  device_name  port

# API Function: lldp_verify_transmit_enabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_transmit_enabled_on_port(device_name, port)

	Robot API Call: 

		lldp_verify_transmit_enabled_on_port  device_name  port

# API Function: lldp_verify_transmit_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_transmit_disabled_on_port(device_name, port)

	Robot API Call: 

		lldp_verify_transmit_disabled_on_port  device_name  port

# API Function: lldp_verify_receive_enabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_receive_enabled_on_port(device_name, port)

	Robot API Call: 

		lldp_verify_receive_enabled_on_port  device_name  port

# API Function: lldp_verify_receive_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_receive_disabled_on_port(device_name, port)

	Robot API Call: 

		lldp_verify_receive_disabled_on_port  device_name  port

# API Function: lldp_verify_remote_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_remote_port(device_name, port, remote_port)

	Robot API Call: 

		lldp_verify_remote_port  device_name  port  remote_port

# API Function: lldp_verify_neighbor_sysname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lldp.lldp_verify_neighbor_sysname(device_name, port, neighbor_sysname)

	Robot API Call: 

		lldp_verify_neighbor_sysname  device_name  port  neighbor_sysname

