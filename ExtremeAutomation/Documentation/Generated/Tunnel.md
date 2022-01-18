# Keyword Library Documentation for Tunnel
This feature is located in this file: `tunnel.yaml` (in this directory: econ-automation-framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /econ-automation-framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/econ-automation-framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: create_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_create_interface(device_name )

	Robot API Call: 

		tunnel_create_interface  device_name  

UUID: 5e4d2dce-a324-4288-85fa-b3986c94a5ec
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: tun.0.{tunnel}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		shutdown

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create tunnel {<str_utils.exos_tunnel_interface>tunnel}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface tunnel {tunnel}

----------------------------------------------


## REST
## SNMP
# API Function: delete_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_delete_interface(device_name )

	Robot API Call: 

		tunnel_delete_interface  device_name  

UUID: e8a1c3ea-06bf-4bc3-809f-477f1da53742
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no interface tunnel tun.0.{tunnel}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete tunnel {<str_utils.exos_tunnel_interface>tunnel}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no interface tunnel {tunnel}

----------------------------------------------


## REST
## SNMP
# API Function: enable_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_enable_interface(device_name )

	Robot API Call: 

		tunnel_enable_interface  device_name  

UUID: 3fcc3372-4257-4c27-ba06-9bd2f92bb76e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: tun.0.{tunnel}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no shutdown

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable tunnel {<str_utils.exos_tunnel_interface>tunnel}

----------------------------------------------


## REST
## SNMP
# API Function: disable_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_disable_interface(device_name )

	Robot API Call: 

		tunnel_disable_interface  device_name  

UUID: 75d9f71a-0d75-4b0b-b23c-644e421c6280
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: tun.0.{tunnel}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		shutdown

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable tunnel {<str_utils.exos_tunnel_interface>tunnel}

----------------------------------------------


## REST
## SNMP
# API Function: set_mode_gre
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_set_mode_gre(device_name )

	Robot API Call: 

		tunnel_set_mode_gre  device_name  

UUID: 7189ce0d-7a04-4abb-84c9-7d1f6a6f21b4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: tun.0.{tunnel}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		tunnel mode gre

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mode gre ip

----------------------------------------------


## REST
## SNMP
# API Function: set_mode_vxlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_set_mode_vxlan(device_name )

	Robot API Call: 

		tunnel_set_mode_vxlan  device_name  

UUID: b0e26563-c285-4f8b-b979-a8fefbd19217
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: tun.0.{tunnel}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		tunnel mode vxlan

----------------------------------------------


## REST
## SNMP
# API Function: set_mode_vxlan_l2tb_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_set_mode_vxlan_l2tb_port(device_name, tunnel, port)

	Robot API Call: 

		tunnel_set_mode_vxlan_l2tb_port  device_name  tunnel  port

UUID: b097d007-1522-42d1-9dc3-2539e52177fe
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: tun.0.{tunnel}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		tunnel mode vxlan l2 {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_mode_gre_l2_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_set_mode_gre_l2_port(device_name, tunnel, port)

	Robot API Call: 

		tunnel_set_mode_gre_l2_port  device_name  tunnel  port

UUID: 944976e1-5c22-4144-8891-1364fe6b4d37
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: tun.0.{tunnel}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		tunnel mode gre l2 {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_source_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_set_source_ip(device_name, tunnel, ip_address)

	Robot API Call: 

		tunnel_set_source_ip  device_name  tunnel  ip_address

UUID: ed130690-92dc-4748-8729-259d5b8c2858
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: tun.0.{tunnel}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		tunnel source {ip_address}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		source {ip_address}

----------------------------------------------


## REST
## SNMP
# API Function: set_dest_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_set_dest_ip(device_name, tunnel, ip_address)

	Robot API Call: 

		tunnel_set_dest_ip  device_name  tunnel  ip_address

UUID: 9eba98f9-cb29-45b6-aace-101b08753f60
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: tun.0.{tunnel}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		tunnel destination {ip_address}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		destination {ip_address}

----------------------------------------------


## REST
## SNMP
# API Function: clear_source_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_clear_source_ip(device_name, tunnel, ip_address)

	Robot API Call: 

		tunnel_clear_source_ip  device_name  tunnel  ip_address

UUID: 2feabea2-ad4d-4d86-89e8-d3bc5c44d8e6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no source

----------------------------------------------


## REST
## SNMP
# API Function: clear_dest_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_clear_dest_ip(device_name, tunnel, ip_address)

	Robot API Call: 

		tunnel_clear_dest_ip  device_name  tunnel  ip_address

UUID: fc21d27d-a6e4-49f3-9887-3e6c2330fd7c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no destination

----------------------------------------------


## REST
## SNMP
# API Function: clear_mode_gre
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_clear_mode_gre(device_name, tunnel, ip_address)

	Robot API Call: 

		tunnel_clear_mode_gre  device_name  tunnel  ip_address

UUID: 5efab2db-71ff-4999-bee6-0ee3c80407ea
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no tunnel mode gre ip

----------------------------------------------


## REST
## SNMP
# API Function: show_tunnel
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_show_tunnel(device_name )

	Robot API Call: 

		tunnel_show_tunnel  device_name  

UUID: bb5a6d27-f8bd-4338-afa2-e97330929747
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show tunnel {tunnel}

----------------------------------------------


## REST
## SNMP
# API Function: show_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementTunnelGenKeywords.tunnel_show_all(device_name )

	Robot API Call: 

		tunnel_show_all  device_name  

UUID: 51405cc7-f7f3-4911-8061-66bf00c1f0a4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show tunnel

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show tunnel

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show tunnel brief

----------------------------------------------


## REST
## SNMP
