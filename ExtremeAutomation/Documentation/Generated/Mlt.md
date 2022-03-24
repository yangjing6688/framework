# Command Keyword Library Documentation for Mlt
This feature is located in this file: `mlt.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: create_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_create_id(device_name )

	Robot API Call: 

		mlt_create_id  device_name  

UUID: 61c7cf26-44c8-47eb-b0b1-344baf998f46
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mlt {mlt_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.7.{mlt_id}

----------------------------------------------


# API Function: delete_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_delete_id(device_name )

	Robot API Call: 

		mlt_delete_id  device_name  

UUID: 10cf289a-a38f-40ab-985a-e1edab663ebd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no mlt {mlt_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.7.{mlt_id}

----------------------------------------------


# API Function: enable_flex_uni
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_enable_flex_uni(device_name )

	Robot API Call: 

		mlt_enable_flex_uni  device_name  

UUID: 97c17a90-02d4-4b74-af4e-80bc48f5fa95
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		flex-uni enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.49.{mlt_id}

----------------------------------------------


# API Function: disable_flex_uni
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_disable_flex_uni(device_name )

	Robot API Call: 

		mlt_disable_flex_uni  device_name  

UUID: a9841ef0-3767-404f-84b5-a4125aa299a2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no flex-uni enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.49.{mlt_id}

----------------------------------------------


# API Function: enable_lacp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_enable_lacp(device_name )

	Robot API Call: 

		mlt_enable_lacp  device_name  

UUID: 1e1368d4-55d7-4507-a051-2b8a7752f43b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		lacp enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.18.{mlt_id}

----------------------------------------------


# API Function: disable_lacp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_disable_lacp(device_name )

	Robot API Call: 

		mlt_disable_lacp  device_name  

UUID: 68d147b8-0e4e-4ca6-9fb1-51cc995252ef
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no lacp enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.18.{mlt_id}

----------------------------------------------


# API Function: set_port_member
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_set_port_member(device_name )

	Robot API Call: 

		mlt_set_port_member  device_name  

UUID: 5932c3c8-ee1e-497e-84a9-0d359a20fb79
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mlt {mlt_id} member {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.3.{mlt_id}

----------------------------------------------


# API Function: clear_port_member
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_clear_port_member(device_name )

	Robot API Call: 

		mlt_clear_port_member  device_name  

UUID: 7e1bb41b-e957-4855-b711-a7165922d877
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no mlt {mlt_id} member {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.3.{mlt_id}

----------------------------------------------


# API Function: set_type_split_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_set_type_split_mlt(device_name )

	Robot API Call: 

		mlt_set_type_split_mlt  device_name  

UUID: 1b4685fe-bb79-40d1-9e07-52a4309e564c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		smlt

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.12.{mlt_id}

----------------------------------------------


# API Function: set_type_normal_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_set_type_normal_mlt(device_name )

	Robot API Call: 

		mlt_set_type_normal_mlt  device_name  

UUID: 42dad7ab-c2b1-47eb-968a-4770a759368e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no smlt

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.12.{mlt_id}

----------------------------------------------


# API Function: set_encapsulation_dot1q
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_set_encapsulation_dot1q(device_name )

	Robot API Call: 

		mlt_set_encapsulation_dot1q  device_name  

UUID: 4ce20ab9-ec4a-4726-8051-5afdb7c4d86c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mlt {mlt_id} encapsulation dot1q

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.4.{mlt_id}

----------------------------------------------


# API Function: clear_encapsulation_dot1q
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_clear_encapsulation_dot1q(device_name )

	Robot API Call: 

		mlt_clear_encapsulation_dot1q  device_name  

UUID: 29d08a66-c90a-4bbb-8e85-0393f2e372d9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no mlt {mlt_id} encapsulation dot1q

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.17.10.1.4.{mlt_id}

----------------------------------------------


# API Function: mlt_verify_id_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_id_exists(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_id_exists  device_name  mlt_id

# API Function: mlt_verify_id_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_id_does_not_exist(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_id_does_not_exist  device_name  mlt_id

# API Function: mlt_verify_admin_mode_split
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_admin_mode_split(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_admin_mode_split  device_name  mlt_id

# API Function: mlt_verify_admin_mode_normal
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_admin_mode_normal(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_admin_mode_normal  device_name  mlt_id

# API Function: mlt_verify_oper_mode_split
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_oper_mode_split(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_oper_mode_split  device_name  mlt_id

# API Function: mlt_verify_oper_mode_normal
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_oper_mode_normal(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_oper_mode_normal  device_name  mlt_id

# API Function: mlt_verify_flex_uni_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_flex_uni_enabled(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_flex_uni_enabled  device_name  mlt_id

# API Function: mlt_verify_flex_uni_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_flex_uni_disabled(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_flex_uni_disabled  device_name  mlt_id

# API Function: mlt_verify_lacp_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_lacp_enabled(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_lacp_enabled  device_name  mlt_id

# API Function: mlt_verify_lacp_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_lacp_disabled(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_lacp_disabled  device_name  mlt_id

# API Function: mlt_verify_lacp_oper_up
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_lacp_oper_up(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_lacp_oper_up  device_name  mlt_id

# API Function: mlt_verify_lacp_oper_down
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_lacp_oper_down(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_lacp_oper_down  device_name  mlt_id

# API Function: mlt_verify_port_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_port_exists(device_name, mlt_id, ports)

	Robot API Call: 

		mlt_verify_port_exists  device_name  mlt_id  ports

# API Function: mlt_verify_port_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_port_does_not_exist(device_name, mlt_id, ports)

	Robot API Call: 

		mlt_verify_port_does_not_exist  device_name  mlt_id  ports

# API Function: mlt_verify_encapsulation_dot1q
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_encapsulation_dot1q(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_encapsulation_dot1q  device_name  mlt_id

# API Function: mlt_verify_encapsulation_not_dot1q
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlt.mlt_verify_encapsulation_not_dot1q(device_name, mlt_id)

	Robot API Call: 

		mlt_verify_encapsulation_not_dot1q  device_name  mlt_id

