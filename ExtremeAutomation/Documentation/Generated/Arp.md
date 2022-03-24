# Command Keyword Library Documentation for Arp
This feature is located in this file: `arp.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: create_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_create_entry(device_name, ip_address, mac)

	Robot API Call: 

		arp_create_entry  device_name  ip_address  mac

UUID: 9e145f7e-5188-4a1a-9293-6169429256ba
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		arp {ip_address} {mac}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure iparp add {ip_address} {mac}

----------------------------------------------


## REST
## SNMP
# API Function: create_entry_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_create_entry_interface(device_name, ip_address, mac, interface)

	Robot API Call: 

		arp_create_entry_interface  device_name  ip_address  mac  interface

UUID: 24a3e643-81cd-46e5-99ba-0e2aba2150ea
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		arp {ip_address} {mac} interface vlan.0.{interface}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure iparp add {ip_address} {mac}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip arp {ip_address} {mac} {interface} vid {interface}

----------------------------------------------


## REST
## SNMP
# API Function: delete_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_delete_entry(device_name )

	Robot API Call: 

		arp_delete_entry  device_name  

UUID: 78efc289-9630-4ce7-842e-f1927fab2fd6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no arp {ip_address}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure iparp delete {ip_address}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip arp {ip_address}

----------------------------------------------


## REST
## SNMP
# API Function: clear_all_entries
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_clear_all_entries(device_name )

	Robot API Call: 

		arp_clear_all_entries  device_name  

UUID: c7a01592-4d90-41dd-a9ce-04ec8a451c42
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear arp all

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear iparp

----------------------------------------------


## REST
## SNMP
# API Function: create_entry_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_create_entry_port(device_name, ip_address, mac, port)

	Robot API Call: 

		arp_create_entry_port  device_name  ip_address  mac  port

UUID: b18ddc94-cccb-498e-a1df-5ebb199f9e7c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip arp {ip_address} {mac} {port}

----------------------------------------------


## REST
## SNMP
# API Function: create_entry_port_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_create_entry_port_vlan(device_name, ip_address, mac, port, vlan)

	Robot API Call: 

		arp_create_entry_port_vlan  device_name  ip_address  mac  port  vlan

UUID: dbf72d3f-e00b-42af-b5ea-75d6d8ae223c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip arp {ip_address} {mac} {port} vid {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: arp_verify_entry_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_verify_entry_exists(device_name, ip_address, macaddr, intf, static)

	Robot API Call: 

		arp_verify_entry_exists  device_name  ip_address  macaddr  intf  static

# API Function: arp_verify_entry_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_verify_entry_does_not_exist(device_name, ip_address, macaddr, intf, static)

	Robot API Call: 

		arp_verify_entry_does_not_exist  device_name  ip_address  macaddr  intf  static

# API Function: arp_verify_entry_exists_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_verify_entry_exists_vrf(device_name, vrf_name, ip_address, macaddr, intf, static)

	Robot API Call: 

		arp_verify_entry_exists_vrf  device_name  vrf_name  ip_address  macaddr  intf  static

# API Function: arp_verify_entry_does_not_exist_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.arp.arp_verify_entry_does_not_exist_vrf(device_name, vrf_name, ip_address, macaddr, intf, static)

	Robot API Call: 

		arp_verify_entry_does_not_exist_vrf  device_name  vrf_name  ip_address  macaddr  intf  static

