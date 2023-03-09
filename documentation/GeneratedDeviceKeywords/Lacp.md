# Keyword Library Documentation for Lacp
This feature is located in this file: `lacp.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_enable_global(device_name )

	Robot API Call: 

		lacp_enable_global  device_name  

UUID: a3aab87a-4811-4a23-b823-a24e6dd3edb0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		lacp enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_disable_global(device_name )

	Robot API Call: 

		lacp_disable_global  device_name  

UUID: 7893b72a-32d1-4372-beac-c5599e185374
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no lacp enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_disable_port(device_name )

	Robot API Call: 

		lacp_disable_port  device_name  

UUID: 257a08f4-5e78-4a35-a853-35372913ec5c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface ethernet {main_lag_port}||channel-group {key} mode passive

----------------------------------------------


## REST
## SNMP
# API Function: enable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_enable_port(device_name )

	Robot API Call: 

		lacp_enable_port  device_name  

UUID: 8ce4b9f2-e3f0-4fde-8d60-204af927bfa9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface ethernet {main_lag_port}||channel-group {key} mode active

----------------------------------------------


## REST
## SNMP
# API Function: create_lag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_create_lag(device_name, main_lag_port, port, key)

	Robot API Call: 

		lacp_create_lag  device_name  main_lag_port  port  key

UUID: 6733e1f6-de56-41fd-ac2c-11de35c9a645
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface {main_lag_port}||lacp key {key} aggregation enable||lacp enable||exit

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set lacp enable||set lacp aadminkey {main_lag_port} {key}||set port lacp port {port} aadminkey {key}||set port lacp port {port} enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable sharing {main_lag_port} grouping {port} lacp

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface ethernet {main_lag_port}||channel-group {key} mode on

----------------------------------------------


## REST
## SNMP
# API Function: delete_lag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_delete_lag(device_name, main_lag_port, key, port)

	Robot API Call: 

		lacp_delete_lag  device_name  main_lag_port  key  port

UUID: 1b7b971a-1b19-44a3-939a-cf482658c94b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface {main_lag_port}||no lacp aggregation enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lacp aadminkey {main_lag_port}||set port lacp port {port} disable||clear port lacp port {port} aadminkey||set lacp disable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable sharing {main_lag_port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface ethernet {main_lag_port}||no channel-group {key}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_set_port_priority(device_name )

	Robot API Call: 

		lacp_set_port_priority  device_name  

UUID: 52f86761-45c0-4eac-9760-5ae60331f9ad
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface ethernet {main_lag_port}||lacp port-priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: set_system_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_set_system_priority(device_name )

	Robot API Call: 

		lacp_set_system_priority  device_name  

UUID: 375da013-e36e-427e-96f7-d3d1a93eae15
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		lacp system-priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: set_lag_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_set_lag_port(device_name, main_lag_port, port, key)

	Robot API Call: 

		lacp_set_lag_port  device_name  main_lag_port  port  key

UUID: f8f70a5c-2f8b-4c22-9086-818a010990a2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface {main_lag_port}||lacp aggregation enable||lacp enable||exit

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port lacp port {port} aadminkey {key}||set port lacp port {port} enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure sharing {main_lag_port} add ports {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface ethernet {main_lag_port}||channel-group {key} mode on

----------------------------------------------


## REST
## SNMP
# API Function: clear_lag_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_clear_lag_port(device_name )

	Robot API Call: 

		lacp_clear_lag_port  device_name  

UUID: e96bb2e6-e508-437f-92d3-9b5ce6b1c3f0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface {main_lag_port}||no lacp aggregation enable||no lacp enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear port lacp port {port} aadminkey||set port lacp port {port} disable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure sharing {main_lag_port} delete ports {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface ethernet {main_lag_port}||no channel-group {key}

----------------------------------------------


## REST
## SNMP
# API Function: set_mlt_actor_key
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_set_mlt_actor_key(device_name )

	Robot API Call: 

		lacp_set_mlt_actor_key  device_name  

UUID: 6a69d5fb-8cc8-4c35-94ea-22822b0a86ed
## CLI
## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.2.840.10006.300.43.1.1.1.1.6.{mlt_id}

----------------------------------------------


# API Function: set_mlt_actor_system_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_set_mlt_actor_system_priority(device_name )

	Robot API Call: 

		lacp_set_mlt_actor_system_priority  device_name  

UUID: de9d6279-e922-4ee0-8cd0-92811715126d
## CLI
## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.2.840.10006.300.43.1.1.1.1.3.{mlt_id}

----------------------------------------------


# API Function: clear_counters
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_clear_counters(device_name )

	Robot API Call: 

		lacp_clear_counters  device_name  

UUID: 6aa9f95c-0e55-4293-9a92-f434cade9f20
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lacp {port_channel} counters

----------------------------------------------


## REST
## SNMP
# API Function: clear_all_counters
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_clear_all_counters(device_name )

	Robot API Call: 

		lacp_clear_all_counters  device_name  

UUID: 5de1719c-872a-41d7-9013-8930edadad8d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear lacp counters

----------------------------------------------


## REST
## SNMP
# API Function: lacp_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_verify_enabled(device_name)

	Robot API Call: 

		lacp_verify_enabled  device_name

# API Function: lacp_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_verify_disabled(device_name)

	Robot API Call: 

		lacp_verify_disabled  device_name

# API Function: lacp_verify_group_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_verify_group_exists(device_name, main_lag_port, lag_port, key)

	Robot API Call: 

		lacp_verify_group_exists  device_name  main_lag_port  lag_port  key

# API Function: lacp_verify_group_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_verify_group_does_not_exist(device_name, main_lag_port, lag_port, key)

	Robot API Call: 

		lacp_verify_group_does_not_exist  device_name  main_lag_port  lag_port  key

# API Function: lacp_verify_port_in_lag_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_verify_port_in_lag_group(device_name, main_lag_port, lag_port)

	Robot API Call: 

		lacp_verify_port_in_lag_group  device_name  main_lag_port  lag_port

# API Function: lacp_verify_port_not_in_lag_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.lacp.lacp_verify_port_not_in_lag_group(device_name, main_lag_port, lag_port)

	Robot API Call: 

		lacp_verify_port_not_in_lag_group  device_name  main_lag_port  lag_port

