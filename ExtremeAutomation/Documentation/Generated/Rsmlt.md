# Keyword Library Documentation for Rsmlt
This feature is located in this file: `rsmlt.yaml` (in this directory: econ-automation-framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /econ-automation-framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/econ-automation-framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: enable_edge_support
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_enable_edge_support(device_name )

	Robot API Call: 

		rsmlt_enable_edge_support  device_name  

UUID: 1cd191b8-4663-4daf-a172-43367ef3f08a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip rsmlt edge-support

----------------------------------------------


## REST
## SNMP
# API Function: disable_edge_support
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_disable_edge_support(device_name )

	Robot API Call: 

		rsmlt_disable_edge_support  device_name  

UUID: 55d26d95-87cf-4f12-a0ad-ba272e1ba705
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip rsmlt edge-support

----------------------------------------------


## REST
## SNMP
# API Function: enable_vlan_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_enable_vlan_interface(device_name )

	Robot API Call: 

		rsmlt_enable_vlan_interface  device_name  

UUID: 9a19e49e-ff41-4d35-bb56-b9af088a99e2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip rsmlt

----------------------------------------------


## REST
## SNMP
# API Function: disable_vlan_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_disable_vlan_interface(device_name )

	Robot API Call: 

		rsmlt_disable_vlan_interface  device_name  

UUID: ccff1e1c-83e4-4033-a8e2-02920585166c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip rsmlt

----------------------------------------------


## REST
## SNMP
# API Function: set_interface_holddown_timer
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_set_interface_holddown_timer(device_name )

	Robot API Call: 

		rsmlt_set_interface_holddown_timer  device_name  

UUID: 0096a4a2-a456-4713-8e24-8b0c353a3126
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip rsmlt holddown-timer {timer}

----------------------------------------------


## REST
## SNMP
# API Function: set_interface_holdup_timer
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_set_interface_holdup_timer(device_name )

	Robot API Call: 

		rsmlt_set_interface_holdup_timer  device_name  

UUID: 1c71b9f6-7d6e-411a-bbed-3fbd81e8de87
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip rsmlt holdup-timer {timer}

----------------------------------------------


## REST
## SNMP
# API Function: show_info
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_info(device_name )

	Robot API Call: 

		rsmlt_show_info  device_name  

UUID: 2aeb7133-d9d9-4070-8ea5-fd4605f98726
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt

----------------------------------------------


## REST
## SNMP
# API Function: show_edge_support
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_edge_support(device_name )

	Robot API Call: 

		rsmlt_show_edge_support  device_name  

UUID: 076ea85d-774c-45f5-a63b-aad5dcfc44c6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt edge-support

----------------------------------------------


## REST
## SNMP
# API Function: show_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_vrf(device_name )

	Robot API Call: 

		rsmlt_show_vrf  device_name  

UUID: 5a775e8e-20a2-4a07-a5c4-156f29e1ae73
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: show_vrfid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_vrfid(device_name )

	Robot API Call: 

		rsmlt_show_vrfid  device_name  

UUID: 072e67f6-98ef-449c-b01a-dd3b178db6be
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt vrf {vrfid}

----------------------------------------------


## REST
## SNMP
# API Function: show_local
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_local(device_name )

	Robot API Call: 

		rsmlt_show_local  device_name  

UUID: 85b5667a-1dce-4d62-856f-378f1709a30f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt local

----------------------------------------------


## REST
## SNMP
# API Function: show_local_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_local_vrf(device_name )

	Robot API Call: 

		rsmlt_show_local_vrf  device_name  

UUID: b278e204-9ba8-4dac-a04a-ef509f21038b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt local vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: show_local_vrfid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_local_vrfid(device_name )

	Robot API Call: 

		rsmlt_show_local_vrfid  device_name  

UUID: 6849ddec-4e93-4ff3-9b80-fc7eaa1cba3b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt local vrf {vrfid}

----------------------------------------------


## REST
## SNMP
# API Function: show_peer
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_peer(device_name )

	Robot API Call: 

		rsmlt_show_peer  device_name  

UUID: dff6e248-9921-4c5f-b0c6-5e76535dac46
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt peer

----------------------------------------------


## REST
## SNMP
# API Function: show_peer_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_peer_vrf(device_name )

	Robot API Call: 

		rsmlt_show_peer_vrf  device_name  

UUID: ce5720d7-6383-4aa6-bafe-231c3d764097
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt peer vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: show_peer_vrfid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementRsmltGenKeywords.rsmlt_show_peer_vrfid(device_name )

	Robot API Call: 

		rsmlt_show_peer_vrfid  device_name  

UUID: e2ff2584-90fa-4814-b1b5-8559155efd61
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show ip rsmlt peer vrf {vrfid}

----------------------------------------------


## REST
## SNMP
