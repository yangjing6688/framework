# Keyword Library Documentation for Radius
This feature is located in this file: `radius.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_enable_global(device_name )

	Robot API Call: 

		radius_enable_global  device_name  

UUID: 6a794411-17ce-44a1-b80f-5f467d25a8d6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius enable 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable radius

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.1.0

----------------------------------------------


# API Function: enable_acct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_enable_acct(device_name )

	Robot API Call: 

		radius_enable_acct  device_name  

UUID: d2154d3e-5129-4551-8e84-21fe67976ba5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius accounting enable 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable radius-accounting

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius enable||radius accounting enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.1.0||1.3.6.1.4.1.2272.1.29.1.5.0

----------------------------------------------


# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_disable_global(device_name )

	Robot API Call: 

		radius_disable_global  device_name  

UUID: 9f41adce-7e97-45c2-addc-1b3b23dcdd4c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius disable 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable radius

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no radius enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.1.0

----------------------------------------------


# API Function: disable_acct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_disable_acct(device_name )

	Robot API Call: 

		radius_disable_acct  device_name  

UUID: 55596503-345c-4584-9438-65aff18f58ea
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius accounting disable 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable radius-accounting

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no radius accounting enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.5.0

----------------------------------------------


# API Function: set_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_server(device_name, addr, secret, index, port, client_ip, vr)

	Robot API Call: 

		radius_set_server  device_name  addr  secret  index  port  client_ip  vr

UUID: 714d2b1e-d4bc-436a-8691-dbd3ac8209b6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius server {index} {addr} {port} {secret}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure radius {index} server {addr} {port} client-ip {client_ip} shared-secret {secret} vr {vr}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius server host {client_ip} key {secret} source-ip {addr}

----------------------------------------------


## REST
## SNMP
# API Function: set_acct_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_acct_server(device_name, addr, index, port, secret, client_ip, vr)

	Robot API Call: 

		radius_set_acct_server  device_name  addr  index  port  secret  client_ip  vr

UUID: c26d9e66-84f7-43c4-b51c-6b4a215fac5d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius accounting server {index} {addr} {port} {secret}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure radius-accounting {index} server {addr} {port} client-ip {client_ip} shared-secret {secret} vr {vr}

----------------------------------------------


## REST
## SNMP
# API Function: set_retries_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_retries_global(device_name )

	Robot API Call: 

		radius_set_retries_global  device_name  

UUID: 37ec7b4e-7453-456d-8567-6dc1c07c3813
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius retries {num}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure radius retries {num}

----------------------------------------------


## REST
## SNMP
# API Function: set_timeout_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_timeout_global(device_name )

	Robot API Call: 

		radius_set_timeout_global  device_name  

UUID: 3c29d965-525b-4e5b-82c0-ae90f35ac1d1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius timeout {sec}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure radius timeout {sec}

----------------------------------------------


## REST
## SNMP
# API Function: set_algorithm_global_std
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_algorithm_global_std(device_name )

	Robot API Call: 

		radius_set_algorithm_global_std  device_name  

UUID: 9bc592d8-0738-4dc3-8ac2-0ad11d54feec
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius algorithm standard 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure radius algorithm standard

----------------------------------------------


## REST
## SNMP
# API Function: set_algorithm_global_rr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_algorithm_global_rr(device_name )

	Robot API Call: 

		radius_set_algorithm_global_rr  device_name  

UUID: 9236cb3d-b0ef-46c2-9813-d3d209c31920
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius algorithm round-robin 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure radius algorithm round-robin

----------------------------------------------


## REST
## SNMP
# API Function: set_algorithm_global_srr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_algorithm_global_srr(device_name )

	Robot API Call: 

		radius_set_algorithm_global_srr  device_name  

UUID: cceb1fc6-b521-41dc-ae71-702da2578716
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius algorithm sticky-round-robin 

----------------------------------------------


## REST
## SNMP
# API Function: set_accounting_retries_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_accounting_retries_global(device_name )

	Robot API Call: 

		radius_set_accounting_retries_global  device_name  

UUID: 6b4efe4d-560b-478d-a8fd-3ded6d09ffbd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius accounting retries {num} all

----------------------------------------------


## REST
## SNMP
# API Function: set_accounting_timeout_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_accounting_timeout_global(device_name )

	Robot API Call: 

		radius_set_accounting_timeout_global  device_name  

UUID: 920d5343-c390-4865-b011-2a89384d6301
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set radius accounting timeout {sec} all

----------------------------------------------


## REST
## SNMP
# API Function: clear_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_clear_server(device_name )

	Robot API Call: 

		radius_clear_server  device_name  

UUID: 51c0947e-5037-40a8-b4da-20d97ff27f12
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear radius server {index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure radius server {index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no radius server host {client_ip} used-by cli

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.5624.1.2.4.1.5.1.8.{index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.5624.1.2.4.1.5.1.8.{index}

----------------------------------------------


# API Function: clear_acct_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_clear_acct_server(device_name )

	Robot API Call: 

		radius_clear_acct_server  device_name  

UUID: c1229a43-8988-4884-88a3-59da0add71a3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear radius accounting server {index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure radius-accounting server {index}

----------------------------------------------


## REST
## SNMP
# API Function: clear_acct_server_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_clear_acct_server_global(device_name )

	Robot API Call: 

		radius_clear_acct_server_global  device_name  

UUID: 605ebf72-b989-4a7e-bb47-5a3c5f477542
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear radius accounting server all

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure radius-accounting

----------------------------------------------


## REST
## SNMP
# API Function: clear_algorithm_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_clear_algorithm_global(device_name )

	Robot API Call: 

		radius_clear_algorithm_global  device_name  

UUID: 89723391-2765-4306-872f-e3007199182e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear radius algorithm 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure radius algorithm standard

----------------------------------------------


## REST
## SNMP
# API Function: clear_retries_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_clear_retries_global(device_name )

	Robot API Call: 

		radius_clear_retries_global  device_name  

UUID: f9a7b472-ee89-45b6-8260-e890d5a8b4c5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear radius retries 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure radius retries 3

----------------------------------------------


## REST
## SNMP
# API Function: clear_timeout_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_clear_timeout_global(device_name )

	Robot API Call: 

		radius_clear_timeout_global  device_name  

UUID: 2a17d732-4379-4e7c-83b7-7d1b6a4189c2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear radius timeout 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure radius timeout 3

----------------------------------------------


## REST
## SNMP
# API Function: clear_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_clear_state(device_name )

	Robot API Call: 

		radius_clear_state  device_name  

UUID: a6ad0a18-a989-4afc-a647-2188555afbd7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear radius state 

----------------------------------------------


## REST
## SNMP
# API Function: enable_mgmt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_enable_mgmt(device_name )

	Robot API Call: 

		radius_enable_mgmt  device_name  

UUID: 9057e14d-ac0c-4761-b94b-f3a2b910e18a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable radius mgmt-access

----------------------------------------------


## REST
## SNMP
# API Function: enable_netlogin
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_enable_netlogin(device_name )

	Robot API Call: 

		radius_enable_netlogin  device_name  

UUID: aee135e5-1ef4-44a7-9aa7-f08e6e866480
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable radius netlogin

----------------------------------------------


## REST
## SNMP
# API Function: disable_mgmt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_disable_mgmt(device_name )

	Robot API Call: 

		radius_disable_mgmt  device_name  

UUID: 8c1a1e0b-4474-4ed2-b0ba-5ca0719b65e1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable radius mgmt-access

----------------------------------------------


## REST
## SNMP
# API Function: disable_netlogin
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_disable_netlogin(device_name )

	Robot API Call: 

		radius_disable_netlogin  device_name  

UUID: 614343be-6e31-45ba-8e49-95f100ad7dde
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable radius netlogin

----------------------------------------------


## REST
## SNMP
# API Function: enable_include_cli_cmds
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_enable_include_cli_cmds(device_name )

	Robot API Call: 

		radius_enable_include_cli_cmds  device_name  

UUID: 47365281-4cf9-4edc-a300-c605dba1b82b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius accounting include-cli-commands

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.7.0

----------------------------------------------


# API Function: enable_cli_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_enable_cli_profile(device_name )

	Robot API Call: 

		radius_enable_cli_profile  device_name  

UUID: 174bcffc-fd8c-44e0-8819-b6467e53fcca
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius cli-profile

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.14.0

----------------------------------------------


# API Function: enable_src_ip_flag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_enable_src_ip_flag(device_name )

	Robot API Call: 

		radius_enable_src_ip_flag  device_name  

UUID: 65f9bf8e-afc4-4ba9-9524-2f6cba1014e4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius sourceip-flag

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.16.0

----------------------------------------------


# API Function: disable_include_cli_cmds
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_disable_include_cli_cmds(device_name )

	Robot API Call: 

		radius_disable_include_cli_cmds  device_name  

UUID: cdf8d306-4ecc-46a2-bb3c-c54e9e7e4bde
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no radius accounting include-cli-commands

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.7.0

----------------------------------------------


# API Function: disable_cli_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_disable_cli_profile(device_name )

	Robot API Call: 

		radius_disable_cli_profile  device_name  

UUID: d9ca9238-85ed-485a-a939-7687362b38d4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no radius cli-profile

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.14.0

----------------------------------------------


# API Function: disable_src_ip_flag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_disable_src_ip_flag(device_name )

	Robot API Call: 

		radius_disable_src_ip_flag  device_name  

UUID: 057b5f5e-0951-4e7d-8753-4bc8c689994d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no radius sourceip-flag

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.16.0

----------------------------------------------


# API Function: set_max_servers
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_max_servers(device_name )

	Robot API Call: 

		radius_set_max_servers  device_name  

UUID: 165af531-1f1e-4519-9f91-6c59f50e0cb5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius maxserver {max_servers}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.2.0

----------------------------------------------


# API Function: set_access_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_access_priority(device_name )

	Robot API Call: 

		radius_set_access_priority  device_name  

UUID: 69907b5f-f591-4374-830f-9db39180b440
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius access-priority-attribute {attr_value}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.3.0

----------------------------------------------


# API Function: set_acct_attr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_acct_attr(device_name )

	Robot API Call: 

		radius_set_acct_attr  device_name  

UUID: ff4888ac-a8c7-4635-97e9-c714020980d9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius accounting attribute-value {attr_value}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.6.0

----------------------------------------------


# API Function: set_mcast_addr_attr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_mcast_addr_attr(device_name )

	Robot API Call: 

		radius_set_mcast_addr_attr  device_name  

UUID: 3d1d1fbe-ba8d-4b2d-841f-5cc71b44a6ec
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius mcast-addr-attr-value {attr_value}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.9.0

----------------------------------------------


# API Function: set_auth_info_attr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_auth_info_attr(device_name )

	Robot API Call: 

		radius_set_auth_info_attr  device_name  

UUID: 2acf12a1-fa88-431e-ae57-05a286cbf7e4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius auth-info-attr-value {attr_value}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.10.0

----------------------------------------------


# API Function: set_cmd_access_attr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_cmd_access_attr(device_name )

	Robot API Call: 

		radius_set_cmd_access_attr  device_name  

UUID: 475ba50d-f042-41a2-a03f-e24928eb9aef
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius command-access-attribute {attr_value}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.11.0

----------------------------------------------


# API Function: set_cli_cmd_attr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_cli_cmd_attr(device_name )

	Robot API Call: 

		radius_set_cli_cmd_attr  device_name  

UUID: f2d03fd9-f2ac-4668-a737-26e2448a57fc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius cli-commands-attribute {attr_value}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.12.0

----------------------------------------------


# API Function: set_cli_cmd_count
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_cli_cmd_count(device_name )

	Robot API Call: 

		radius_set_cli_cmd_count  device_name  

UUID: 3a3728fc-4684-4532-87b3-7290b2a51fe0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius cli-cmd-count {value}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.18.0

----------------------------------------------


# API Function: set_server_for_cli
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_set_server_for_cli(device_name )

	Robot API Call: 

		radius_set_server_for_cli  device_name  

UUID: 80b929b7-de43-4258-a2ac-e1276374cc12
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius server host {addr} key {secret} port {auth_port} priority {priority} retry {max_retries} timeout {timeout} acct-port {acct_port} source-ip {source_ip}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.5.1.9.{addr}||1.3.6.1.4.1.2272.1.29.5.1.8.{addr}||1.3.6.1.4.1.2272.1.29.5.1.4.{addr}||1.3.6.1.4.1.2272.1.29.5.1.7.{addr}||1.3.6.1.4.1.2272.1.29.5.1.6.{addr}||1.3.6.1.4.1.2272.1.29.5.1.5.{addr}||1.3.6.1.4.1.2272.1.29.5.1.18.{addr}||1.3.6.1.4.1.2272.1.29.5.1.17.{addr}||1.3.6.1.4.1.2272.1.29.5.1.30.{addr}||1.3.6.1.4.1.2272.1.29.5.1.16.{addr}

----------------------------------------------


# API Function: clear_server_for_cli
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_clear_server_for_cli(device_name )

	Robot API Call: 

		radius_clear_server_for_cli  device_name  

UUID: 93acf6fd-8d47-4be8-90fb-ca762a0da238
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no radius server host {addr} used-by cli

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.5.1.16.{addr}

----------------------------------------------


# API Function: clear_stats_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_clear_stats_global(device_name )

	Robot API Call: 

		radius_clear_stats_global  device_name  

UUID: d5301bc9-f275-4b44-904d-62d24a4da49e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		radius clear-stat

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.29.1.8.0

----------------------------------------------


# API Function: radius_verify_server_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_exists(device_name, index, addr)

	Robot API Call: 

		radius_verify_server_exists  device_name  index  addr

# API Function: radius_verify_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_does_not_exist(device_name, index, addr)

	Robot API Call: 

		radius_verify_server_does_not_exist  device_name  index  addr

# API Function: radius_verify_server_active
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_active(device_name, index, addr)

	Robot API Call: 

		radius_verify_server_active  device_name  index  addr

# API Function: radius_verify_server_inactive
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_inactive(device_name, index, addr)

	Robot API Call: 

		radius_verify_server_inactive  device_name  index  addr

# API Function: radius_verify_accounting_server_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_accounting_server_exists(device_name, index, addr)

	Robot API Call: 

		radius_verify_accounting_server_exists  device_name  index  addr

# API Function: radius_verify_accounting_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_accounting_server_does_not_exist(device_name, index, addr)

	Robot API Call: 

		radius_verify_accounting_server_does_not_exist  device_name  index  addr

# API Function: radius_verify_state_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_state_enabled(device_name)

	Robot API Call: 

		radius_verify_state_enabled  device_name

# API Function: radius_verify_accounting_state_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_accounting_state_enabled(device_name)

	Robot API Call: 

		radius_verify_accounting_state_enabled  device_name

# API Function: radius_verify_state_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_state_disabled(device_name)

	Robot API Call: 

		radius_verify_state_disabled  device_name

# API Function: radius_verify_accounting_state_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_accounting_state_disabled(device_name)

	Robot API Call: 

		radius_verify_accounting_state_disabled  device_name

# API Function: radius_verify_retries
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_retries(device_name, num)

	Robot API Call: 

		radius_verify_retries  device_name  num

# API Function: radius_verify_retries_set_to_default
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_retries_set_to_default(device_name)

	Robot API Call: 

		radius_verify_retries_set_to_default  device_name

# API Function: radius_verify_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_timeout(device_name, sec)

	Robot API Call: 

		radius_verify_timeout  device_name  sec

# API Function: radius_verify_timeout_set_to_default
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_timeout_set_to_default(device_name)

	Robot API Call: 

		radius_verify_timeout_set_to_default  device_name

# API Function: radius_verify_algorithm_type_standard
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_algorithm_type_standard(device_name)

	Robot API Call: 

		radius_verify_algorithm_type_standard  device_name

# API Function: radius_verify_algorithm_type_round_robin
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_algorithm_type_round_robin(device_name)

	Robot API Call: 

		radius_verify_algorithm_type_round_robin  device_name

# API Function: radius_verify_algorithm_type_sticky_round_robin
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_algorithm_type_sticky_round_robin(device_name)

	Robot API Call: 

		radius_verify_algorithm_type_sticky_round_robin  device_name

# API Function: radius_verify_algorithm_set_to_default
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_algorithm_set_to_default(device_name)

	Robot API Call: 

		radius_verify_algorithm_set_to_default  device_name

# API Function: radius_verify_enabled_for_management
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_enabled_for_management(device_name)

	Robot API Call: 

		radius_verify_enabled_for_management  device_name

# API Function: radius_verify_disabled_for_management
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_disabled_for_management(device_name)

	Robot API Call: 

		radius_verify_disabled_for_management  device_name

# API Function: radius_verify_enabled_for_multiauth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_enabled_for_multiauth(device_name)

	Robot API Call: 

		radius_verify_enabled_for_multiauth  device_name

# API Function: radius_verify_disabled_for_multiauth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_disabled_for_multiauth(device_name)

	Robot API Call: 

		radius_verify_disabled_for_multiauth  device_name

# API Function: radius_verify_max_servers
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_max_servers(device_name, max_servers)

	Robot API Call: 

		radius_verify_max_servers  device_name  max_servers

# API Function: radius_verify_access_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_access_priority(device_name, attr_value)

	Robot API Call: 

		radius_verify_access_priority  device_name  attr_value

# API Function: radius_verify_accounting_attribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_accounting_attribute(device_name, attr_value)

	Robot API Call: 

		radius_verify_accounting_attribute  device_name  attr_value

# API Function: radius_verify_include_cli_cmds_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_include_cli_cmds_enabled(device_name)

	Robot API Call: 

		radius_verify_include_cli_cmds_enabled  device_name

# API Function: radius_verify_include_cli_cmds_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_include_cli_cmds_disabled(device_name)

	Robot API Call: 

		radius_verify_include_cli_cmds_disabled  device_name

# API Function: radius_verify_multicast_address_attribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_multicast_address_attribute(device_name, attr_value)

	Robot API Call: 

		radius_verify_multicast_address_attribute  device_name  attr_value

# API Function: radius_verify_authentication_information_attribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_authentication_information_attribute(device_name, attr_value)

	Robot API Call: 

		radius_verify_authentication_information_attribute  device_name  attr_value

# API Function: radius_verify_command_access_attribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_command_access_attribute(device_name, attr_value)

	Robot API Call: 

		radius_verify_command_access_attribute  device_name  attr_value

# API Function: radius_verify_command_attribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_command_attribute(device_name, attr_value)

	Robot API Call: 

		radius_verify_command_attribute  device_name  attr_value

# API Function: radius_verify_profiling_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_profiling_enabled(device_name)

	Robot API Call: 

		radius_verify_profiling_enabled  device_name

# API Function: radius_verify_profiling_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_profiling_disabled(device_name)

	Robot API Call: 

		radius_verify_profiling_disabled  device_name

# API Function: radius_verify_source_ip_flag_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_source_ip_flag_enabled(device_name)

	Robot API Call: 

		radius_verify_source_ip_flag_enabled  device_name

# API Function: radius_verify_source_ip_flag_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_source_ip_flag_disabled(device_name)

	Robot API Call: 

		radius_verify_source_ip_flag_disabled  device_name

# API Function: radius_verify_command_count
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_command_count(device_name, value)

	Robot API Call: 

		radius_verify_command_count  device_name  value

# API Function: radius_verify_server_host_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_priority(device_name, addr, priority)

	Robot API Call: 

		radius_verify_server_host_priority  device_name  addr  priority

# API Function: radius_verify_server_host_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_timeout(device_name, addr, timeout)

	Robot API Call: 

		radius_verify_server_host_timeout  device_name  addr  timeout

# API Function: radius_verify_server_host_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_enabled(device_name, addr)

	Robot API Call: 

		radius_verify_server_host_enabled  device_name  addr

# API Function: radius_verify_server_host_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_disabled(device_name, addr)

	Robot API Call: 

		radius_verify_server_host_disabled  device_name  addr

# API Function: radius_verify_server_host_retries
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_retries(device_name, addr, max_retries)

	Robot API Call: 

		radius_verify_server_host_retries  device_name  addr  max_retries

# API Function: radius_verify_server_host_auth_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_auth_port(device_name, addr, auth_port)

	Robot API Call: 

		radius_verify_server_host_auth_port  device_name  addr  auth_port

# API Function: radius_verify_server_host_accounting_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_accounting_enabled(device_name, addr)

	Robot API Call: 

		radius_verify_server_host_accounting_enabled  device_name  addr

# API Function: radius_verify_server_host_accounting_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_accounting_disabled(device_name, addr)

	Robot API Call: 

		radius_verify_server_host_accounting_disabled  device_name  addr

# API Function: radius_verify_server_host_accounting_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_accounting_port(device_name, addr, acct_port)

	Robot API Call: 

		radius_verify_server_host_accounting_port  device_name  addr  acct_port

# API Function: radius_verify_server_host_source_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.radius.radius_verify_server_host_source_ip(device_name, addr, source_ip)

	Robot API Call: 

		radius_verify_server_host_source_ip  device_name  addr  source_ip

