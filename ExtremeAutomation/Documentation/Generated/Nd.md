# Command Keyword Library Documentation for Nd
This feature is located in this file: `nd.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: set_v6_neighbor
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.nd.nd_set_v6_neighbor(device_name, ipv6_addr, hw_addr, interface, port)

	Robot API Call: 

		nd_set_v6_neighbor  device_name  ipv6_addr  hw_addr  interface  port

UUID: ebb0dced-7ea7-47c8-b14b-40d357f3ec6a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure neighbor-discovery add {ipv6_addr} {hw_addr}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ipv6 neighbor {ipv6_addr} {hw_addr} interface vlan.0.{interface}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ipv6 neighbor {ipv6_addr} port {port} mac {hw_addr} vlan {interface}

----------------------------------------------


## REST
## SNMP
# API Function: clear_v6_neighbor
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.nd.nd_clear_v6_neighbor(device_name, ipv6_addr, interface)

	Robot API Call: 

		nd_clear_v6_neighbor  device_name  ipv6_addr  interface

UUID: 79d7c87e-effc-42e0-a1e0-70e0313bbbf7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure neighbor-discovery delete {ipv6_addr}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ipv6 neighbor {ipv6_addr}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ipv6 neighbor {ipv6_addr} vlan {interface}

----------------------------------------------


## REST
## SNMP
# API Function: clear_v6_neighbor_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.nd.nd_clear_v6_neighbor_port(device_name )

	Robot API Call: 

		nd_clear_v6_neighbor_port  device_name  

UUID: 5d2a9bd2-cb72-463d-aaa1-08dd326ed63d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ipv6 neighbor {ipv6_addr} port {port}

----------------------------------------------


## REST
## SNMP
# API Function: nd_verify_neighbor_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.nd.nd_verify_neighbor_entry(device_name, ipv6_addr, hw_addr, interface)

	Robot API Call: 

		nd_verify_neighbor_entry  device_name  ipv6_addr  hw_addr  interface

# API Function: nd_verify_neighbor_entry_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.nd.nd_verify_neighbor_entry_does_not_exist(device_name, ipv6_addr, hw_addr, interface)

	Robot API Call: 

		nd_verify_neighbor_entry_does_not_exist  device_name  ipv6_addr  hw_addr  interface

