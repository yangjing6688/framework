# Keyword Library Documentation for Fabricattach
This feature is located in this file: `fabricattach.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_enable_global(device_name )

	Robot API Call: 

		fabricattach_enable_global  device_name  

UUID: 2fadd54c-c514-4dd7-adc4-e14f861ecfe7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.1.0

----------------------------------------------


# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_disable_global(device_name )

	Robot API Call: 

		fabricattach_disable_global  device_name  

UUID: d44d2d2d-b35f-4bb6-87ea-69e45259f1f4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.1.0

----------------------------------------------


# API Function: enable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_enable_port(device_name )

	Robot API Call: 

		fabricattach_enable_port  device_name  

UUID: 014943bb-3d2c-4642-8369-8f4eda5db253
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.2.{port}||1.3.6.1.4.1.45.5.46.1.6.1.3.{port}

----------------------------------------------


# API Function: disable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_disable_port(device_name )

	Robot API Call: 

		fabricattach_disable_port  device_name  

UUID: 84ca75ea-abca-40b9-859e-a2e0334e760a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.2.{port}||1.3.6.1.4.1.45.5.46.1.6.1.3.{port}

----------------------------------------------


# API Function: delete_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_delete_port(device_name )

	Robot API Call: 

		fabricattach_delete_port  device_name  

UUID: fb9747d5-cc8a-4aec-bc0f-292609bf07ae
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.3.{port}

----------------------------------------------


# API Function: enable_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_enable_mlt(device_name )

	Robot API Call: 

		fabricattach_enable_mlt  device_name  

UUID: b56fce5c-2794-43b5-9402-ba257afa7fc2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.2.{mlt_id}||1.3.6.1.4.1.45.5.46.1.6.1.3.{mlt_id}

----------------------------------------------


# API Function: disable_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_disable_mlt(device_name )

	Robot API Call: 

		fabricattach_disable_mlt  device_name  

UUID: e1ff075d-a674-4319-8cad-c2027b1b42d6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.2.{mlt_id}||1.3.6.1.4.1.45.5.46.1.6.1.3.{mlt_id}

----------------------------------------------


# API Function: delete_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_delete_mlt(device_name )

	Robot API Call: 

		fabricattach_delete_mlt  device_name  

UUID: 1b87c519-cb3d-42f8-90fa-4702f613bac4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.3.{mlt_id}

----------------------------------------------


# API Function: enable_port_auth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_enable_port_auth(device_name )

	Robot API Call: 

		fabricattach_enable_port_auth  device_name  

UUID: ee77b7d6-1c80-4a45-8918-1d9f97420fbf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa message-authentication

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.4.{port}

----------------------------------------------


# API Function: disable_port_auth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_disable_port_auth(device_name )

	Robot API Call: 

		fabricattach_disable_port_auth  device_name  

UUID: b29e33ba-e609-46fc-a013-dbf0530d5cdd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa message-authentication

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.4.{port}

----------------------------------------------


# API Function: enable_mlt_auth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_enable_mlt_auth(device_name )

	Robot API Call: 

		fabricattach_enable_mlt_auth  device_name  

UUID: d9cf0399-b7d8-4b9c-89eb-aacfd59f7111
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa message-authentication

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.4.{mlt_id}

----------------------------------------------


# API Function: disable_mlt_auth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_disable_mlt_auth(device_name )

	Robot API Call: 

		fabricattach_disable_mlt_auth  device_name  

UUID: d3cb51c9-090b-4f79-b107-8c7cbc7de45d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa message-authentication

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.4.{mlt_id}

----------------------------------------------


# API Function: set_assignment_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_set_assignment_timeout(device_name )

	Robot API Call: 

		fabricattach_set_assignment_timeout  device_name  

UUID: 6e7549b9-7fbf-44fd-963f-ca316c7e6ab2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa assignment-timeout {timeout}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.22.0

----------------------------------------------


# API Function: set_discovery_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_set_discovery_timeout(device_name )

	Robot API Call: 

		fabricattach_set_discovery_timeout  device_name  

UUID: 4970b994-e328-4c88-8282-81b0af6b3219
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa discovery-timeout {timeout}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.26.0

----------------------------------------------


# API Function: set_port_auth_key
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_set_port_auth_key(device_name, port, auth_key)

	Robot API Call: 

		fabricattach_set_port_auth_key  device_name  port  auth_key

UUID: 967ecb22-20cc-4bc9-ab7a-f570616cfcb4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa authentication-key {auth_key}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.5.{port}

----------------------------------------------


# API Function: set_mlt_auth_key
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_set_mlt_auth_key(device_name, mlt_id, auth_key)

	Robot API Call: 

		fabricattach_set_mlt_auth_key  device_name  mlt_id  auth_key

UUID: 982e301b-0505-4832-8f3d-d09432fe3b9a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa authentication-key {auth_key}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.5.{mlt_id}

----------------------------------------------


# API Function: set_port_mgmt_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_set_port_mgmt_isid(device_name, port, i_sid)

	Robot API Call: 

		fabricattach_set_port_mgmt_isid  device_name  port  i_sid

UUID: 5d41fe78-26f5-417d-97f8-0218d063f5b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa management i-sid {i_sid}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.6.{port}

----------------------------------------------


# API Function: set_mlt_mgmt_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_set_mlt_mgmt_isid(device_name, mlt_id, i_sid)

	Robot API Call: 

		fabricattach_set_mlt_mgmt_isid  device_name  mlt_id  i_sid

UUID: 86cc40a1-774c-4175-8019-98c3051fe105
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa management i-sid {i_sid}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.6.{mlt_id}

----------------------------------------------


# API Function: set_port_mgmt_isid_and_cvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_set_port_mgmt_isid_and_cvid(device_name, port, i_sid, c_vid)

	Robot API Call: 

		fabricattach_set_port_mgmt_isid_and_cvid  device_name  port  i_sid  c_vid

UUID: 5609738c-9095-4e98-b168-6ef46b060ba0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa management i-sid {i_sid} c-vid {c_vid}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.6.{port}||1.3.6.1.4.1.45.5.46.1.6.1.7.{port}

----------------------------------------------


# API Function: set_mlt_mgmt_isid_and_cvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_set_mlt_mgmt_isid_and_cvid(device_name, mlt_id, i_sid, c_vid)

	Robot API Call: 

		fabricattach_set_mlt_mgmt_isid_and_cvid  device_name  mlt_id  i_sid  c_vid

UUID: 6ccb9ec6-f2d7-4d11-8031-54cf3a5130bc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa management i-sid {i_sid} c-vid {c_vid}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.6.{mlt_id}||1.3.6.1.4.1.45.5.46.1.6.1.7.{mlt_id}

----------------------------------------------


# API Function: clear_port_mgmt_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_clear_port_mgmt_isid(device_name )

	Robot API Call: 

		fabricattach_clear_port_mgmt_isid  device_name  

UUID: a3fd6b4e-cf1b-498f-8cc5-08d1c8491a80
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa management i-sid

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.6.{port}

----------------------------------------------


# API Function: clear_mlt_mgmt_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_clear_mlt_mgmt_isid(device_name )

	Robot API Call: 

		fabricattach_clear_mlt_mgmt_isid  device_name  

UUID: 980e1662-394f-4fea-b058-02fdfc152dae
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa management i-sid

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.6.{mlt_id}

----------------------------------------------


# API Function: set_zero_touch_client_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_set_zero_touch_client_isid(device_name, name, i_sid)

	Robot API Call: 

		fabricattach_set_zero_touch_client_isid  device_name  name  i_sid

UUID: fbb9689a-0c10-4f0d-b6ab-57179f88581c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		fa zero-touch-client standard {name} i-sid {i_sid}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.29.1.4.{name}||1.3.6.1.4.1.45.5.46.1.29.1.5.{name}

----------------------------------------------


# API Function: clear_zero_touch_client
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_clear_zero_touch_client(device_name )

	Robot API Call: 

		fabricattach_clear_zero_touch_client  device_name  

UUID: d666bda8-c763-4b2d-8e9e-c077b37cbba8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no fa zero-touch-client standard {name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.29.1.5.{name}

----------------------------------------------


# API Function: fabricattach_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_enabled(device_name)

	Robot API Call: 

		fabricattach_verify_enabled  device_name

# API Function: fabricattach_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_disabled(device_name)

	Robot API Call: 

		fabricattach_verify_disabled  device_name

# API Function: fabricattach_verify_element_is_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_is_server(device_name)

	Robot API Call: 

		fabricattach_verify_element_is_server  device_name

# API Function: fabricattach_verify_element_is_proxy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_is_proxy(device_name)

	Robot API Call: 

		fabricattach_verify_element_is_proxy  device_name

# API Function: fabricattach_verify_client_proxy_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_client_proxy_enabled(device_name)

	Robot API Call: 

		fabricattach_verify_client_proxy_enabled  device_name

# API Function: fabricattach_verify_mode_spbm
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_mode_spbm(device_name)

	Robot API Call: 

		fabricattach_verify_mode_spbm  device_name

# API Function: fabricattach_verify_assignment_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_assignment_timeout(device_name, timeout)

	Robot API Call: 

		fabricattach_verify_assignment_timeout  device_name  timeout

# API Function: fabricattach_verify_agent_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_agent_timeout(device_name, timeout)

	Robot API Call: 

		fabricattach_verify_agent_timeout  device_name  timeout

# API Function: fabricattach_verify_discovery_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_discovery_timeout(device_name, timeout)

	Robot API Call: 

		fabricattach_verify_discovery_timeout  device_name  timeout

# API Function: fabricattach_verify_attach_agent_service_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_attach_agent_service_enabled(device_name)

	Robot API Call: 

		fabricattach_verify_attach_agent_service_enabled  device_name

# API Function: fabricattach_verify_removed_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_removed_on_port(device_name, port)

	Robot API Call: 

		fabricattach_verify_removed_on_port  device_name  port

# API Function: fabricattach_verify_enabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_enabled_on_port(device_name, port)

	Robot API Call: 

		fabricattach_verify_enabled_on_port  device_name  port

# API Function: fabricattach_verify_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_disabled_on_port(device_name, port)

	Robot API Call: 

		fabricattach_verify_disabled_on_port  device_name  port

# API Function: fabricattach_verify_removed_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_removed_on_mlt(device_name, mlt_id)

	Robot API Call: 

		fabricattach_verify_removed_on_mlt  device_name  mlt_id

# API Function: fabricattach_verify_enabled_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_enabled_on_mlt(device_name, mlt_id)

	Robot API Call: 

		fabricattach_verify_enabled_on_mlt  device_name  mlt_id

# API Function: fabricattach_verify_disabled_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_disabled_on_mlt(device_name, mlt_id)

	Robot API Call: 

		fabricattach_verify_disabled_on_mlt  device_name  mlt_id

# API Function: fabricattach_verify_auth_enabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_auth_enabled_on_port(device_name, port)

	Robot API Call: 

		fabricattach_verify_auth_enabled_on_port  device_name  port

# API Function: fabricattach_verify_auth_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_auth_disabled_on_port(device_name, port)

	Robot API Call: 

		fabricattach_verify_auth_disabled_on_port  device_name  port

# API Function: fabricattach_verify_auth_enabled_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_auth_enabled_on_mlt(device_name, mlt_id)

	Robot API Call: 

		fabricattach_verify_auth_enabled_on_mlt  device_name  mlt_id

# API Function: fabricattach_verify_auth_disabled_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_auth_disabled_on_mlt(device_name, mlt_id)

	Robot API Call: 

		fabricattach_verify_auth_disabled_on_mlt  device_name  mlt_id

# API Function: fabricattach_verify_mgmt_isid_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_mgmt_isid_on_port(device_name, port, i_sid)

	Robot API Call: 

		fabricattach_verify_mgmt_isid_on_port  device_name  port  i_sid

# API Function: fabricattach_verify_mgmt_isid_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_mgmt_isid_on_mlt(device_name, mlt-id, i_sid)

	Robot API Call: 

		fabricattach_verify_mgmt_isid_on_mlt  device_name  mlt-id  i_sid

# API Function: fabricattach_verify_mgmt_isid_and_cvid_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_mgmt_isid_and_cvid_on_port(device_name, port, i_sid, c_vid)

	Robot API Call: 

		fabricattach_verify_mgmt_isid_and_cvid_on_port  device_name  port  i_sid  c_vid

# API Function: fabricattach_verify_mgmt_isid_and_cvid_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_mgmt_isid_and_cvid_on_mlt(device_name, mlt-id, i_sid, c_vid)

	Robot API Call: 

		fabricattach_verify_mgmt_isid_and_cvid_on_mlt  device_name  mlt-id  i_sid  c_vid

# API Function: fabricattach_verify_mgmt_isid_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_mgmt_isid_disabled_on_port(device_name, port)

	Robot API Call: 

		fabricattach_verify_mgmt_isid_disabled_on_port  device_name  port

# API Function: fabricattach_verify_mgmt_isid_disabled_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_mgmt_isid_disabled_on_mlt(device_name, port)

	Robot API Call: 

		fabricattach_verify_mgmt_isid_disabled_on_mlt  device_name  port

# API Function: fabricattach_verify_neighbor_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_neighbor_exists(device_name, neighbor)

	Robot API Call: 

		fabricattach_verify_neighbor_exists  device_name  neighbor

# API Function: fabricattach_verify_neighbor_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_neighbor_does_not_exist(device_name, neighbor)

	Robot API Call: 

		fabricattach_verify_neighbor_does_not_exist  device_name  neighbor

# API Function: fabricattach_verify_element_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_type(device_name, port, element_type)

	Robot API Call: 

		fabricattach_verify_element_type  device_name  port  element_type

# API Function: fabricattach_verify_element_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_vlan(device_name, port, vlan)

	Robot API Call: 

		fabricattach_verify_element_vlan  device_name  port  vlan

# API Function: fabricattach_verify_element_system_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_system_id(device_name, port, system_id)

	Robot API Call: 

		fabricattach_verify_element_system_id  device_name  port  system_id

# API Function: fabricattach_verify_primary_server_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_primary_server_id(device_name, server id)

	Robot API Call: 

		fabricattach_verify_primary_server_id  device_name  server id

# API Function: fabricattach_verify_element_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_state(device_name, port, state)

	Robot API Call: 

		fabricattach_verify_element_state  device_name  port  state

# API Function: fabricattach_verify_element_assigned_auth_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_assigned_auth_status(device_name, port, element_assign_auth)

	Robot API Call: 

		fabricattach_verify_element_assigned_auth_status  device_name  port  element_assign_auth

# API Function: fabricattach_verify_element_auth_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_auth_status(device_name, port, element_auth)

	Robot API Call: 

		fabricattach_verify_element_auth_status  device_name  port  element_auth

# API Function: fabricattach_verify_element_assigned_oper_auth_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_assigned_oper_auth_status(device_name, port, element_assigned_oper_auth)

	Robot API Call: 

		fabricattach_verify_element_assigned_oper_auth_status  device_name  port  element_assigned_oper_auth

# API Function: fabricattach_verify_element_oper_auth_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_element_oper_auth_status(device_name, port, element_oper_auth)

	Robot API Call: 

		fabricattach_verify_element_oper_auth_status  device_name  port  element_oper_auth

# API Function: fabricattach_verify_assigned_isid_to_vlan_map_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_assigned_isid_to_vlan_map_on_port(device_name, port, isid, vlan)

	Robot API Call: 

		fabricattach_verify_assigned_isid_to_vlan_map_on_port  device_name  port  isid  vlan

# API Function: fabricattach_verify_assigned_isid_to_vlan_map_not_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_assigned_isid_to_vlan_map_not_on_port(device_name, port, isid, vlan)

	Robot API Call: 

		fabricattach_verify_assigned_isid_to_vlan_map_not_on_port  device_name  port  isid  vlan

# API Function: fabricattach_verify_assigned_isid_to_vlan_map_state_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_assigned_isid_to_vlan_map_state_on_port(device_name, port, isid, vlan, state)

	Robot API Call: 

		fabricattach_verify_assigned_isid_to_vlan_map_state_on_port  device_name  port  isid  vlan  state

# API Function: fabricattach_verify_assigned_isid_to_vlan_map_origin_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_assigned_isid_to_vlan_map_origin_on_port(device_name, port, isid, vlan, origin)

	Robot API Call: 

		fabricattach_verify_assigned_isid_to_vlan_map_origin_on_port  device_name  port  isid  vlan  origin

# API Function: fabricattach_verify_global_stats_discovered_elements_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_discovered_elements_received(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_discovered_elements_received  device_name  count  count_operator

# API Function: fabricattach_verify_global_stats_assignments_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_assignments_received(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_assignments_received  device_name  count  count_operator

# API Function: fabricattach_verify_global_stats_assignments_accepted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_assignments_accepted(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_assignments_accepted  device_name  count  count_operator

# API Function: fabricattach_verify_global_stats_assignments_rejected
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_assignments_rejected(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_assignments_rejected  device_name  count  count_operator

# API Function: fabricattach_verify_global_stats_assignments_expired
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_assignments_expired(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_assignments_expired  device_name  count  count_operator

# API Function: fabricattach_verify_global_stats_discovered_auth_failed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_discovered_auth_failed(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_discovered_auth_failed  device_name  count  count_operator

# API Function: fabricattach_verify_global_stats_discovered_elements_expired
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_discovered_elements_expired(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_discovered_elements_expired  device_name  count  count_operator

# API Function: fabricattach_verify_global_stats_discovered_elements_deleted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_discovered_elements_deleted(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_discovered_elements_deleted  device_name  count  count_operator

# API Function: fabricattach_verify_global_stats_assignments_deleted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_assignments_deleted(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_assignments_deleted  device_name  count  count_operator

# API Function: fabricattach_verify_global_stats_assignment_auth_failed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_global_stats_assignment_auth_failed(device_name, count, count_operator)

	Robot API Call: 

		fabricattach_verify_global_stats_assignment_auth_failed  device_name  count  count_operator

# API Function: fabricattach_verify_port_stats_discovered_elements_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_discovered_elements_received(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_discovered_elements_received  device_name  port  count  count_operator

# API Function: fabricattach_verify_port_stats_assignments_received
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_assignments_received(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_assignments_received  device_name  port  count  count_operator

# API Function: fabricattach_verify_port_stats_assignments_accepted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_assignments_accepted(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_assignments_accepted  device_name  port  count  count_operator

# API Function: fabricattach_verify_port_stats_assignments_rejected
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_assignments_rejected(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_assignments_rejected  device_name  port  count  count_operator

# API Function: fabricattach_verify_port_stats_assignments_expired
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_assignments_expired(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_assignments_expired  device_name  port  count  count_operator

# API Function: fabricattach_verify_port_stats_discovered_auth_failed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_discovered_auth_failed(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_discovered_auth_failed  device_name  port  count  count_operator

# API Function: fabricattach_verify_port_stats_discovered_elements_expired
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_discovered_elements_expired(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_discovered_elements_expired  device_name  port  count  count_operator

# API Function: fabricattach_verify_port_stats_discovered_elements_deleted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_discovered_elements_deleted(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_discovered_elements_deleted  device_name  port  count  count_operator

# API Function: fabricattach_verify_port_stats_assignments_deleted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_assignments_deleted(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_assignments_deleted  device_name  port  count  count_operator

# API Function: fabricattach_verify_port_stats_assignment_auth_failed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_port_stats_assignment_auth_failed(device_name, port, count, count_operator)

	Robot API Call: 

		fabricattach_verify_port_stats_assignment_auth_failed  device_name  port  count  count_operator

# API Function: fabricattach_verify_zero_touch_client_to_isid_auto_attach_map
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_zero_touch_client_to_isid_auto_attach_map(device_name, i_sid, client_name)

	Robot API Call: 

		fabricattach_verify_zero_touch_client_to_isid_auto_attach_map  device_name  i_sid  client_name

# API Function: fabricattach_verify_zero_touch_client_to_vlan_auto_attach_map
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_zero_touch_client_to_vlan_auto_attach_map(device_name, vlan_or_untagged, client_name)

	Robot API Call: 

		fabricattach_verify_zero_touch_client_to_vlan_auto_attach_map  device_name  vlan_or_untagged  client_name

# API Function: fabricattach_verify_zero_touch_client_name_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_zero_touch_client_name_exists(device_name, client_name)

	Robot API Call: 

		fabricattach_verify_zero_touch_client_name_exists  device_name  client_name

# API Function: fabricattach_verify_zero_touch_client_name_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_zero_touch_client_name_does_not_exist(device_name, client_name)

	Robot API Call: 

		fabricattach_verify_zero_touch_client_name_does_not_exist  device_name  client_name

# API Function: fabricattach_verify_isid_port_platform_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_isid_port_platform_vlan(device_name, port, isid, vlan)

	Robot API Call: 

		fabricattach_verify_isid_port_platform_vlan  device_name  port  isid  vlan

# API Function: fabricattach_verify_isid_port_isid_cvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_isid_port_isid_cvid(device_name, port, isid, cvid)

	Robot API Call: 

		fabricattach_verify_isid_port_isid_cvid  device_name  port  isid  cvid

# API Function: fabricattach_verify_isid_port_isid_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_isid_port_isid_type(device_name, port, isid, i_type)

	Robot API Call: 

		fabricattach_verify_isid_port_isid_type  device_name  port  isid  i_type

# API Function: fabricattach_verify_isid_port_isid_origin
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_isid_port_isid_origin(device_name, port, isid, i_origin)

	Robot API Call: 

		fabricattach_verify_isid_port_isid_origin  device_name  port  isid  i_origin

# API Function: fabricattach_verify_isid_mlt_platform_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_isid_mlt_platform_vlan(device_name, mlt_id, isid, vlan)

	Robot API Call: 

		fabricattach_verify_isid_mlt_platform_vlan  device_name  mlt_id  isid  vlan

# API Function: fabricattach_verify_isid_mlt_isid_cvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_isid_mlt_isid_cvid(device_name, mlt_id, isid, cvid)

	Robot API Call: 

		fabricattach_verify_isid_mlt_isid_cvid  device_name  mlt_id  isid  cvid

# API Function: fabricattach_verify_isid_mlt_isid_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_isid_mlt_isid_type(device_name, mlt_id, isid, i_type)

	Robot API Call: 

		fabricattach_verify_isid_mlt_isid_type  device_name  mlt_id  isid  i_type

# API Function: fabricattach_verify_isid_mlt_isid_origin
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_verify_isid_mlt_isid_origin(device_name, mlt_id, isid, i_origin)

	Robot API Call: 

		fabricattach_verify_isid_mlt_isid_origin  device_name  mlt_id  isid  i_origin

