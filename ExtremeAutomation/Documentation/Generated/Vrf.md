# Command Keyword Library Documentation for Vrf
This feature is located in this file: `vrf.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: create_router
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_create_router(device_name )

	Robot API Call: 

		vrf_create_router  device_name  

UUID: 79ad39b1-ea31-44e0-af58-0c820758655a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: create_router_with_vrfid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_create_router_with_vrfid(device_name )

	Robot API Call: 

		vrf_create_router_with_vrfid  device_name  

UUID: 0aba9a09-f599-42b7-89e2-45dbeec380dd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip vrf {vrf_name} vrfid {vrfid}

----------------------------------------------


## REST
## SNMP
# API Function: delete_router
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_delete_router(device_name )

	Robot API Call: 

		vrf_delete_router  device_name  

UUID: 8fca33fe-1a50-499a-8d9d-fa01eed835e3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: enable_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_enable_trap(device_name )

	Robot API Call: 

		vrf_enable_trap  device_name  

UUID: 57402ee0-6ae0-49d6-ac07-2a907c1f910e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip vrf {vrf_name} vrf-trap enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_disable_trap(device_name )

	Robot API Call: 

		vrf_disable_trap  device_name  

UUID: 1dce067a-6fe7-4069-a18c-8a30d7a9e09f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip vrf {vrf_name} vrf-trap enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_max_routes_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_enable_max_routes_trap(device_name )

	Robot API Call: 

		vrf_enable_max_routes_trap  device_name  

UUID: 8cfe1a37-1b6f-4df1-a762-3a171b9efa38
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip vrf {vrf_name} max-routes-trap enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_max_routes_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_disable_max_routes_trap(device_name )

	Robot API Call: 

		vrf_disable_max_routes_trap  device_name  

UUID: 213b5ab6-963d-49f0-8a32-f9da60698841
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip vrf {vrf_name} max-routes-trap enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_mvpn
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_enable_mvpn(device_name )

	Robot API Call: 

		vrf_enable_mvpn  device_name  

UUID: e6839ffc-2101-4399-b175-2f976cc4e41c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name} || mvpn enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_mvpn
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_disable_mvpn(device_name )

	Robot API Call: 

		vrf_disable_mvpn  device_name  

UUID: b6a526c3-3b87-4aae-8ebe-08ec636cfb64
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name} || no mvpn enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_ipv6_max_routes_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_enable_ipv6_max_routes_trap(device_name )

	Robot API Call: 

		vrf_enable_ipv6_max_routes_trap  device_name  

UUID: 87b358f0-068b-434f-8a02-910813c8b9c8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip vrf {vrf_name} ipv6-max-routes-trap enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_ipv6_max_routes_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_disable_ipv6_max_routes_trap(device_name )

	Robot API Call: 

		vrf_disable_ipv6_max_routes_trap  device_name  

UUID: 6f2d3dee-e0cc-4910-a42c-64c5b17bd684
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip vrf {vrf_name} ipv6-max-routes-trap enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_ipvpn
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_enable_ipvpn(device_name )

	Robot API Call: 

		vrf_enable_ipvpn  device_name  

UUID: 5c9afa7d-9ea0-4e98-8d38-0952e97c0ec7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name}||ipvpn enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_ipvpn
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_disable_ipvpn(device_name )

	Robot API Call: 

		vrf_disable_ipvpn  device_name  

UUID: bf2da38d-06f7-4ca1-aebe-d25a1f472ff6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name}||no ipvpn enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_isis_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_enable_isis_redistribute_direct(device_name )

	Robot API Call: 

		vrf_enable_isis_redistribute_direct  device_name  

UUID: ebb15783-390a-4eda-a807-68a1faddbbda
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name}||isis redistribute direct enable||exit

----------------------------------------------


## REST
## SNMP
# API Function: disable_isis_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_disable_isis_redistribute_direct(device_name )

	Robot API Call: 

		vrf_disable_isis_redistribute_direct  device_name  

UUID: 9eccfbc2-293c-426a-9814-28749746c015
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name}||no isis redistribute direct enable||exit

----------------------------------------------


## REST
## SNMP
# API Function: set_mvpn_fwd_cache_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_mvpn_fwd_cache_timeout(device_name, vrf_name, timeout)

	Robot API Call: 

		vrf_set_mvpn_fwd_cache_timeout  device_name  vrf_name  timeout

UUID: 562e7f2d-955e-4f3c-8804-0166234e9c6e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name}||mvpn fwd-cache-timeout {timeout}||exit

----------------------------------------------


## REST
## SNMP
# API Function: set_max_routes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_max_routes(device_name, vrf_name, num_max_routes)

	Robot API Call: 

		vrf_set_max_routes  device_name  vrf_name  num_max_routes

UUID: 9ccdaf91-17f5-4c9d-b925-0060d97a92af
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip vrf {vrf_name} max-routes {num_max_routes}

----------------------------------------------


## REST
## SNMP
# API Function: set_ipv6_max_routes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_ipv6_max_routes(device_name, vrf_name, num_max_routes)

	Robot API Call: 

		vrf_set_ipv6_max_routes  device_name  vrf_name  num_max_routes

UUID: 3456a4a9-c719-4988-8814-2bce7ac6f7f5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip vrf {vrf_name} ipv6-max-routes {num_max_routes}

----------------------------------------------


## REST
## SNMP
# API Function: set_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_name(device_name )

	Robot API Call: 

		vrf_set_name  device_name  

UUID: 6d3ef614-8bf1-4cd0-8dc2-31c07b418f32
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip vrf {vrf_name} {new_vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_vrfid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_vrfid(device_name )

	Robot API Call: 

		vrf_set_vrfid  device_name  

UUID: cc22e8fa-bc27-4a43-8e9a-d781f04af55b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip vrf {vrf_name} vrfid {vrfid}

----------------------------------------------


## REST
## SNMP
# API Function: set_interface_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_interface_vlan(device_name, vrf_name, interface)

	Robot API Call: 

		vrf_set_interface_vlan  device_name  vrf_name  interface

UUID: 47b48d3e-d7f5-4ac3-aaf1-aeb4d367b985
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: clear_interface_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_clear_interface_vlan(device_name, vrf_name, interface)

	Robot API Call: 

		vrf_clear_interface_vlan  device_name  vrf_name  interface

UUID: 814fff13-2c4d-461a-b91e-d6f5aaf1a6b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_ipvpn
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_ipvpn(device_name )

	Robot API Call: 

		vrf_set_ipvpn  device_name  

UUID: 7c72f65d-3b9d-4110-abc0-fb5c12b1e92e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name}||ipvpn

----------------------------------------------


## REST
## SNMP
# API Function: set_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_isid(device_name, vrf_name, i_sid)

	Robot API Call: 

		vrf_set_isid  device_name  vrf_name  i_sid

UUID: eab779d3-226a-4742-9d4f-0997b14350db
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name}||i-sid {i_sid}

----------------------------------------------


## REST
## SNMP
# API Function: set_isis_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_isis_redistribute_direct(device_name )

	Robot API Call: 

		vrf_set_isis_redistribute_direct  device_name  

UUID: 3f53d840-e837-4305-a1e1-fae3a510e5d9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name}||isis redistribute direct||exit

----------------------------------------------


## REST
## SNMP
# API Function: clear_isis_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_clear_isis_redistribute_direct(device_name )

	Robot API Call: 

		vrf_clear_isis_redistribute_direct  device_name  

UUID: 97f1fb35-755e-444b-8056-65a8c4a6512e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router vrf {vrf_name}||no isis redistribute direct||exit

----------------------------------------------


## REST
## SNMP
# API Function: set_isis_redistribute_direct_apply
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_set_isis_redistribute_direct_apply(device_name )

	Robot API Call: 

		vrf_set_isis_redistribute_direct_apply  device_name  

UUID: 64858983-7fc7-496e-a08f-fa9f39c061a3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis apply redistribute direct vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: vrf_verify_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_name(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_name  device_name  vrf_name

# API Function: vrf_verify_vrfid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_vrfid(device_name, vrf_name, vrfid)

	Robot API Call: 

		vrf_verify_vrfid  device_name  vrf_name  vrfid

# API Function: vrf_verify_mvpn_fwd_cache_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_mvpn_fwd_cache_timeout(device_name, vrf_name, timeout)

	Robot API Call: 

		vrf_verify_mvpn_fwd_cache_timeout  device_name  vrf_name  timeout

# API Function: vrf_verify_name_and_vrfid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_name_and_vrfid(device_name, vrf_name, vrfid)

	Robot API Call: 

		vrf_verify_name_and_vrfid  device_name  vrf_name  vrfid

# API Function: vrf_verify_name_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_name_does_not_exist(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_name_does_not_exist  device_name  vrf_name

# API Function: vrf_verify_vrfid_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_vrfid_does_not_exist(device_name, vrfid)

	Robot API Call: 

		vrf_verify_vrfid_does_not_exist  device_name  vrfid

# API Function: vrf_verify_trap_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_trap_enabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_trap_enabled  device_name  vrf_name

# API Function: vrf_verify_trap_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_trap_disabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_trap_disabled  device_name  vrf_name

# API Function: vrf_verify_mvpn_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_mvpn_enabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_mvpn_enabled  device_name  vrf_name

# API Function: vrf_verify_mvpn_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_mvpn_disabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_mvpn_disabled  device_name  vrf_name

# API Function: vrf_verify_max_routes_trap_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_max_routes_trap_enabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_max_routes_trap_enabled  device_name  vrf_name

# API Function: vrf_verify_max_routes_trap_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_max_routes_trap_disabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_max_routes_trap_disabled  device_name  vrf_name

# API Function: vrf_verify_ipv6_max_routes_trap_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_ipv6_max_routes_trap_enabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_ipv6_max_routes_trap_enabled  device_name  vrf_name

# API Function: vrf_verify_ipv6_max_routes_trap_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_ipv6_max_routes_trap_disabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_ipv6_max_routes_trap_disabled  device_name  vrf_name

# API Function: vrf_verify_max_routes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_max_routes(device_name, vrf_name, num_max_routes)

	Robot API Call: 

		vrf_verify_max_routes  device_name  vrf_name  num_max_routes

# API Function: vrf_verify_ipv6_max_routes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_ipv6_max_routes(device_name, vrf_name, num_max_routes)

	Robot API Call: 

		vrf_verify_ipv6_max_routes  device_name  vrf_name  num_max_routes

# API Function: vrf_verify_interface_vlan_assigned
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_interface_vlan_assigned(device_name, vrf_name, vlan)

	Robot API Call: 

		vrf_verify_interface_vlan_assigned  device_name  vrf_name  vlan

# API Function: vrf_verify_interface_vlan_not_assigned
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_interface_vlan_not_assigned(device_name, vrf_name, vlan)

	Robot API Call: 

		vrf_verify_interface_vlan_not_assigned  device_name  vrf_name  vlan

# API Function: vrf_verify_ipvpn
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_ipvpn(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_ipvpn  device_name  vrf_name

# API Function: vrf_verify_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_isid(device_name, vrf_name, i_sid)

	Robot API Call: 

		vrf_verify_isid  device_name  vrf_name  i_sid

# API Function: vrf_verify_ipvpn_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_ipvpn_enabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_ipvpn_enabled  device_name  vrf_name

# API Function: vrf_verify_ipvpn_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_ipvpn_disabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_ipvpn_disabled  device_name  vrf_name

# API Function: vrf_verify_isis_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_isis_redistribute_direct(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_isis_redistribute_direct  device_name  vrf_name

# API Function: vrf_verify_isis_redistribute_direct_cleared
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_isis_redistribute_direct_cleared(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_isis_redistribute_direct_cleared  device_name  vrf_name

# API Function: vrf_verify_isis_redistribute_direct_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_isis_redistribute_direct_enabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_isis_redistribute_direct_enabled  device_name  vrf_name

# API Function: vrf_verify_isis_redistribute_direct_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vrf.vrf_verify_isis_redistribute_direct_disabled(device_name, vrf_name)

	Robot API Call: 

		vrf_verify_isis_redistribute_direct_disabled  device_name  vrf_name

