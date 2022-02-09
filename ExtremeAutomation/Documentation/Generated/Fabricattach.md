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


# API Function: show_agent
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_agent(device_name )

	Robot API Call: 

		fabricattach_show_agent  device_name  

UUID: 4567a871-654b-4bef-9539-7e221e1e7537
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa agent

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
# API Function: show_service_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_service_state(device_name )

	Robot API Call: 

		fabricattach_show_service_state  device_name  

UUID: a51e7285-3506-49dd-a482-045cd766d3a4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.1.0

----------------------------------------------


# API Function: show_element_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_element_type(device_name )

	Robot API Call: 

		fabricattach_show_element_type  device_name  

UUID: 67ea1813-fdc0-45a3-8496-2ff556f71576
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.2.0

----------------------------------------------


# API Function: show_provision_mode
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_provision_mode(device_name )

	Robot API Call: 

		fabricattach_show_provision_mode  device_name  

UUID: 3075c202-b569-42d7-aada-e89093b62c81
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.13.0

----------------------------------------------


# API Function: show_global_timeouts
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_global_timeouts(device_name )

	Robot API Call: 

		fabricattach_show_global_timeouts  device_name  

UUID: 3e9b00a0-978e-4d30-94f4-3b2c0a402d71
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.22.0||1.3.6.1.4.1.45.5.46.1.26.0

----------------------------------------------


# API Function: show_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_port(device_name )

	Robot API Call: 

		fabricattach_show_port  device_name  

UUID: 73db387e-a995-4b8d-bf52-ea999d1608fb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa interface port {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.2.{port}||1.3.6.1.4.1.45.5.46.1.6.1.4.{port}||1.3.6.1.4.1.45.5.46.1.6.1.5.{port}||1.3.6.1.4.1.45.5.46.1.6.1.6.{port}||1.3.6.1.4.1.45.5.46.1.6.1.7.{port}

----------------------------------------------


# API Function: show_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_mlt(device_name )

	Robot API Call: 

		fabricattach_show_mlt  device_name  

UUID: 38d80307-ef51-4c67-afa2-33f7b80a7389
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa interface mlt {mlt_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.6.1.2.{mlt_id}||1.3.6.1.4.1.45.5.46.1.6.1.4.{mlt_id}||1.3.6.1.4.1.45.5.46.1.6.1.5.{mlt_id}||1.3.6.1.4.1.45.5.46.1.6.1.6.{mlt_id}||1.3.6.1.4.1.45.5.46.1.6.1.7.{mlt_id}

----------------------------------------------


# API Function: show_elements_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_elements_port(device_name )

	Robot API Call: 

		fabricattach_show_elements_port  device_name  

UUID: d5cace34-fbdb-4b18-a6a9-3a4de157a722
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa elements {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.11.1.2.{port}||1.3.6.1.4.1.45.5.46.1.11.1.3.{port}||1.3.6.1.4.1.45.5.46.1.11.1.4.{port}||1.3.6.1.4.1.45.5.46.1.11.1.5.{port}||1.3.6.1.4.1.45.5.46.1.11.1.6.{port}||1.3.6.1.4.1.45.5.46.1.11.1.8.{port}||1.3.6.1.4.1.45.5.46.1.11.1.9.{port}||1.3.6.1.4.1.45.5.46.1.11.1.10.{port}

----------------------------------------------


# API Function: show_assignment_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_assignment_port(device_name )

	Robot API Call: 

		fabricattach_show_assignment_port  device_name  

UUID: 27d91f59-0ab0-4510-9dcc-7eeff2580340
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa assignment {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.5.1.4.{port}||1.3.6.1.4.1.45.5.46.1.5.1.6.{port}

----------------------------------------------


# API Function: show_stats_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_stats_global(device_name )

	Robot API Call: 

		fabricattach_show_stats_global  device_name  

UUID: fb8262da-696a-49d5-a3ec-e9e502880476
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa statistics summary

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach statistics

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.24

----------------------------------------------


# API Function: show_stats_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_stats_port(device_name )

	Robot API Call: 

		fabricattach_show_stats_port  device_name  

UUID: cfb8d976-77a3-429b-8da6-e22c44e79b50
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa statistics {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.23.1.2.{port}||1.3.6.1.4.1.45.5.46.1.23.1.3.{port}||1.3.6.1.4.1.45.5.46.1.23.1.4.{port}||1.3.6.1.4.1.45.5.46.1.23.1.5.{port}||1.3.6.1.4.1.45.5.46.1.23.1.6.{port}||1.3.6.1.4.1.45.5.46.1.23.1.7.{port}||1.3.6.1.4.1.45.5.46.1.23.1.8.{port}||1.3.6.1.4.1.45.5.46.1.23.1.9.{port}||1.3.6.1.4.1.45.5.46.1.23.1.10.{port}||1.3.6.1.4.1.45.5.46.1.23.1.11.{port}

----------------------------------------------


# API Function: show_zero_touch_client
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_zero_touch_client(device_name )

	Robot API Call: 

		fabricattach_show_zero_touch_client  device_name  

UUID: 07576a33-7963-499a-b59b-f648c20e13f5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fa zero-touch-client

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.46.1.29

----------------------------------------------


# API Function: show_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_isid(device_name )

	Robot API Call: 

		fabricattach_show_isid  device_name  

UUID: 430c3207-54ff-4e1b-a60e-0d1f766d17d0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid {isid}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.87.5.1.3.{port}||1.3.6.1.4.1.2272.1.87.5.1.4.{port}||1.3.6.1.4.1.2272.1.87.5.1.5.{port}||1.3.6.1.4.1.2272.1.87.5.1.6.{port}||1.3.6.1.4.1.2272.1.87.5.1.7.{port}

----------------------------------------------


# API Function: show_client_proxy_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_client_proxy_status(device_name )

	Robot API Call: 

		fabricattach_show_client_proxy_status  device_name  

UUID: 9e5cd2d7-d2be-4d89-aa1a-97531ab5e191
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
# API Function: show_standalone_proxy_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_standalone_proxy_status(device_name )

	Robot API Call: 

		fabricattach_show_standalone_proxy_status  device_name  

UUID: dd69da30-844f-4869-996c-24d1942c1bb2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
# API Function: show_agent_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_agent_timeout(device_name )

	Robot API Call: 

		fabricattach_show_agent_timeout  device_name  

UUID: 424a0a0b-e26b-439c-8535-e8d1f969bd01
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
# API Function: show_extended_logging_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_extended_logging_status(device_name )

	Robot API Call: 

		fabricattach_show_extended_logging_status  device_name  

UUID: d374d76e-30c3-4a14-afd5-8e042cff9e06
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
# API Function: show_primary_server_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_primary_server_id(device_name )

	Robot API Call: 

		fabricattach_show_primary_server_id  device_name  

UUID: 35bd30b6-9e4d-4627-9412-dc07baba7377
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
# API Function: show_server_description
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_server_description(device_name )

	Robot API Call: 

		fabricattach_show_server_description  device_name  

UUID: 70c5140c-03c8-4c37-b5cf-efb11a734224
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
# API Function: show_neighbors
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_neighbors(device_name )

	Robot API Call: 

		fabricattach_show_neighbors  device_name  

UUID: d4058dbc-aa04-476b-8250-dbd7ed3fa277
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach neighbors

----------------------------------------------


## REST
## SNMP
# API Function: show_elements
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_elements(device_name )

	Robot API Call: 

		fabricattach_show_elements  device_name  

UUID: df6dd63e-7c54-48fc-b83e-6a74983e546b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach elements

----------------------------------------------


## REST
## SNMP
# API Function: show_auto_provision_setting
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_auto_provision_setting(device_name )

	Robot API Call: 

		fabricattach_show_auto_provision_setting  device_name  

UUID: 2b427864-874f-45ee-84ef-3ce1fa7df180
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
# API Function: show_zero_touch_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fabricattach.fabricattach_show_zero_touch_status(device_name )

	Robot API Call: 

		fabricattach_show_zero_touch_status  device_name  

UUID: e34ddcc6-77d1-4c7a-a5a6-6c68f0a4e313
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show fabric attach agent

----------------------------------------------


## REST
## SNMP
