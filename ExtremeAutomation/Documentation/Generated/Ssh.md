# Keyword Library Documentation for Ssh
This feature is located in this file: `ssh.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

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
# API Function: show
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_show(device_name )

	Robot API Call: 

		ssh_show  device_name  

UUID: 823e42ad-344c-4a2a-8d19-0ef08d30551c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ssh2

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ssh global

----------------------------------------------


## REST
## SNMP
# API Function: show_client_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_show_client_status(device_name )

	Robot API Call: 

		ssh_show_client_status  device_name  

UUID: 29b3463d-2b88-4f75-b3dc-74df4fce2bfb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ssh client status

----------------------------------------------


## REST
## SNMP
# API Function: show_server_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_show_server_status(device_name )

	Robot API Call: 

		ssh_show_server_status  device_name  

UUID: 5c6f721d-5043-41e0-976c-ef92fc3d3a7f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ssh server status

----------------------------------------------


## REST
## SNMP
# API Function: show_session
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_show_session(device_name )

	Robot API Call: 

		ssh_show_session  device_name  

UUID: 97c26e4e-1ed6-43a1-bed7-62b2c986b62c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ssh session

----------------------------------------------


## REST
## SNMP
# API Function: show_rekey
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.ssh.ssh_show_rekey(device_name )

	Robot API Call: 

		ssh_show_rekey  device_name  

UUID: afe63ae6-664e-4e8f-b386-9c6d3da7c584
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ssh rekey

----------------------------------------------


## REST
## SNMP
