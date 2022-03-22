# Command Keyword Library Documentation for Ssh
This feature is located in this file: `ssh.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_enable(device_name )

	Robot API Call: 

		ssh_enable  device_name  

UUID: 19268327-5b64-4b96-ae69-92538ef45c4f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable ssh2

----------------------------------------------


## REST
## SNMP
# API Function: enable_client
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_enable_client(device_name )

	Robot API Call: 

		ssh_enable_client  device_name  

UUID: c4691b4a-c544-47bf-b72f-ec34e9743aab
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ssh client enable

----------------------------------------------


## REST
## SNMP
# API Function: disable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_disable(device_name )

	Robot API Call: 

		ssh_disable  device_name  

UUID: 3a8fb625-5da1-4534-a716-32896dd5b63d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable ssh2

----------------------------------------------


## REST
## SNMP
# API Function: disable_client
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_disable_client(device_name )

	Robot API Call: 

		ssh_disable_client  device_name  

UUID: efcc8ea4-695d-4272-b325-fb416a42f991
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ssh client enable

----------------------------------------------


## REST
## SNMP
# API Function: set_version
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_set_version(device_name )

	Robot API Call: 

		ssh_set_version  device_name  

UUID: ce297f32-03ea-4a22-8288-8e4b3262bcd0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ssh version {version}

----------------------------------------------


## REST
## SNMP
# API Function: set_client_source_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_set_client_source_interface(device_name )

	Robot API Call: 

		ssh_set_client_source_interface  device_name  

UUID: a640fe7f-d4c0-4ae8-8d09-8d44e8a07d4e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ssh client source-interface {interface}

----------------------------------------------


## REST
## SNMP
# API Function: set_tcp_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_set_tcp_port(device_name )

	Robot API Call: 

		ssh_set_tcp_port  device_name  

UUID: f1650dc0-93b2-43f3-a95d-62d0e6c8cab8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ssh port {tcp_port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ssh server port {tcp_port}

----------------------------------------------


## REST
## SNMP
# API Function: clear_client_source_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_clear_client_source_interface(device_name )

	Robot API Call: 

		ssh_clear_client_source_interface  device_name  

UUID: b3492f28-5da3-4aef-bc73-e95016a55d23
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ssh client source-interface {interface}

----------------------------------------------


## REST
## SNMP
