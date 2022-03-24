# Command Keyword Library Documentation for Dvr
This feature is located in this file: `dvr.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: set_domain_controller
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_domain_controller(device_name )

	Robot API Call: 

		dvr_set_domain_controller  device_name  

UUID: a9354712-f304-477b-ad23-6e9e42e13dfa
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr controller {domain_id}

----------------------------------------------


## REST
## SNMP
# API Function: clear_domain_controller
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_domain_controller(device_name )

	Robot API Call: 

		dvr_clear_domain_controller  device_name  

UUID: 0b080271-8fba-4eff-90ba-7c75c884eecc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no dvr controller

----------------------------------------------


## REST
## SNMP
# API Function: disable_domain_controller_inject_default_route_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_disable_domain_controller_inject_default_route_all(device_name )

	Robot API Call: 

		dvr_disable_domain_controller_inject_default_route_all  device_name  

UUID: a6241fde-5aad-4228-92b7-f58aefb50a1f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr controller inject-default-route-disable

----------------------------------------------


## REST
## SNMP
# API Function: disable_domain_controller_inject_default_route
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_disable_domain_controller_inject_default_route(device_name )

	Robot API Call: 

		dvr_disable_domain_controller_inject_default_route  device_name  

UUID: 5ad92c0d-527e-43b4-8ef2-7397d22d44f1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr controller {domain_id} inject-default-route-disable

----------------------------------------------


## REST
## SNMP
# API Function: set_leaf_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_leaf_id(device_name )

	Robot API Call: 

		dvr_set_leaf_id  device_name  

UUID: 912359c5-35e4-47f8-8493-60f314775716
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr leaf {domain_id}

----------------------------------------------


## REST
## SNMP
# API Function: set_leaf_virtual_ist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_leaf_virtual_ist(device_name, interface, local_ip, mask, peer_ip, cluster_id)

	Robot API Call: 

		dvr_set_leaf_virtual_ist  device_name  interface  local_ip  mask  peer_ip  cluster_id

UUID: 3ec2c0ab-0858-49cc-904b-dad9c3b31b94
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr leaf virtual-ist {local_ip} {mask} peer-ip {peer_ip} cluster-id {cluster_id}

----------------------------------------------


## REST
## SNMP
# API Function: clear_leaf_virtual_ist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_leaf_virtual_ist(device_name )

	Robot API Call: 

		dvr_clear_leaf_virtual_ist  device_name  

UUID: 04166cee-a168-4d87-be9a-a7066f89dd3d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no dvr leaf virtual-ist

----------------------------------------------


## REST
## SNMP
# API Function: set_interface_gateway_ipv4
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_interface_gateway_ipv4(device_name )

	Robot API Call: 

		dvr_set_interface_gateway_ipv4  device_name  

UUID: 7b57b57b-b8da-4b65-beb6-d6378e002fa3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr gw-ipv4 {ip}

----------------------------------------------


## REST
## SNMP
# API Function: clear_interface_gateway_ipv4
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_interface_gateway_ipv4(device_name )

	Robot API Call: 

		dvr_clear_interface_gateway_ipv4  device_name  

UUID: 0f24691c-49cf-4a99-9286-f6a55ade9a3a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no dvr gw-ipv4

----------------------------------------------


## REST
## SNMP
# API Function: enable_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_enable_interface(device_name )

	Robot API Call: 

		dvr_enable_interface  device_name  

UUID: 5ca6c2e3-261f-4af1-9e7b-f1a7fcd6928e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable dvr

----------------------------------------------


## REST
## SNMP
# API Function: disable_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_disable_interface(device_name )

	Robot API Call: 

		dvr_disable_interface  device_name  

UUID: 675309c2-4098-4849-bf6b-35112f847d19
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no enable dvr

----------------------------------------------


## REST
## SNMP
# API Function: set_redistribute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_redistribute(device_name )

	Robot API Call: 

		dvr_set_redistribute  device_name  

UUID: e276fd26-c1b6-4ff6-8f6a-de90d7d18a19
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr apply redistribute

----------------------------------------------


## REST
## SNMP
# API Function: set_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_redistribute_direct(device_name )

	Robot API Call: 

		dvr_set_redistribute_direct  device_name  

UUID: 8218d215-1b64-4859-83aa-9c6a24e5b500
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr apply redistribute direct

----------------------------------------------


## REST
## SNMP
# API Function: set_redistribute_direct_metric
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_redistribute_direct_metric(device_name )

	Robot API Call: 

		dvr_set_redistribute_direct_metric  device_name  

UUID: ee3ffa88-b799-48f3-9d8a-1b0d79133d3a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr redistribute direct metric {metric}

----------------------------------------------


## REST
## SNMP
# API Function: set_redistribute_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_redistribute_vrf(device_name )

	Robot API Call: 

		dvr_set_redistribute_vrf  device_name  

UUID: 772add6c-9ead-4a38-acc5-2e2a022ec026
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr apply redistribute vrf {vrf}

----------------------------------------------


## REST
## SNMP
# API Function: clear_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_redistribute_direct(device_name )

	Robot API Call: 

		dvr_clear_redistribute_direct  device_name  

UUID: 5fccb62e-e05c-48ec-bd98-52696f881319
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no dvr redistribute direct

----------------------------------------------


## REST
## SNMP
# API Function: enable_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_enable_redistribute_direct(device_name )

	Robot API Call: 

		dvr_enable_redistribute_direct  device_name  

UUID: f65ace22-c6d0-42a6-a806-806faad1a763
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr redistribute direct enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_redistribute_direct
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_disable_redistribute_direct(device_name )

	Robot API Call: 

		dvr_disable_redistribute_direct  device_name  

UUID: 97430b8d-49f6-4ea7-8b9d-80b7f3c1f86a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no dvr redistribute direct enable

----------------------------------------------


## REST
## SNMP
# API Function: set_redistribute_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_redistribute_static(device_name )

	Robot API Call: 

		dvr_set_redistribute_static  device_name  

UUID: 8580a1f9-ad78-44a7-b36a-f8dc0f0c8395
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr apply redistribute static

----------------------------------------------


## REST
## SNMP
# API Function: set_redistribute_static_metric
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_set_redistribute_static_metric(device_name )

	Robot API Call: 

		dvr_set_redistribute_static_metric  device_name  

UUID: 79131e5a-93e3-4e81-944f-041e50b5f6dc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr redistribute static metric {metric}

----------------------------------------------


## REST
## SNMP
# API Function: clear_redistribute_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_redistribute_static(device_name )

	Robot API Call: 

		dvr_clear_redistribute_static  device_name  

UUID: 649e982c-da7b-42d2-aa4e-611ccfd944f4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no dvr redistribute static

----------------------------------------------


## REST
## SNMP
# API Function: enable_redistribute_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_enable_redistribute_static(device_name )

	Robot API Call: 

		dvr_enable_redistribute_static  device_name  

UUID: f84d11b1-ad75-435a-baee-686c854b42a6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		dvr redistribute static enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_redistribute_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_disable_redistribute_static(device_name )

	Robot API Call: 

		dvr_disable_redistribute_static  device_name  

UUID: cc74db7b-4152-4fba-a553-b6cc47c83186
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no dvr redistribute static enable

----------------------------------------------


## REST
## SNMP
# API Function: clear_host_entries
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_host_entries(device_name )

	Robot API Call: 

		dvr_clear_host_entries  device_name  

UUID: 60738e0e-9974-4a7a-bc90-750dffd6d684
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear dvr host-entries

----------------------------------------------


## REST
## SNMP
# API Function: clear_host_entries_ipv4
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_host_entries_ipv4(device_name )

	Robot API Call: 

		dvr_clear_host_entries_ipv4  device_name  

UUID: 29bfcbbc-6451-4a34-8e3e-1d6eb7c45191
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear dvr host-entries {ip}

----------------------------------------------


## REST
## SNMP
# API Function: clear_host_entries_ipv4_l3isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_host_entries_ipv4_l3isid(device_name )

	Robot API Call: 

		dvr_clear_host_entries_ipv4_l3isid  device_name  

UUID: f4fc181e-2dd8-47ed-b1ca-bb3669c97cdf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear dvr host-entries {ip} l3isid {isid}

----------------------------------------------


## REST
## SNMP
# API Function: clear_host_entries_l2isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_host_entries_l2isid(device_name )

	Robot API Call: 

		dvr_clear_host_entries_l2isid  device_name  

UUID: a89a7127-50d7-482d-8324-6aacf96db0c0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear dvr host-entries l2isid {isid}

----------------------------------------------


## REST
## SNMP
# API Function: clear_host_entries_l3isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_clear_host_entries_l3isid(device_name )

	Robot API Call: 

		dvr_clear_host_entries_l3isid  device_name  

UUID: c8e41357-3e78-4751-9097-af9c99a8d357
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear dvr host-entries l3isid {isid}

----------------------------------------------


## REST
## SNMP
# API Function: dvr_verify_interface_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_verify_interface_enabled(device_name, interface)

	Robot API Call: 

		dvr_verify_interface_enabled  device_name  interface

# API Function: dvr_verify_interface_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_verify_interface_disabled(device_name, interface)

	Robot API Call: 

		dvr_verify_interface_disabled  device_name  interface

# API Function: dvr_verify_domain_controller_id_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_verify_domain_controller_id_exists(device_name, domain_id)

	Robot API Call: 

		dvr_verify_domain_controller_id_exists  device_name  domain_id

# API Function: dvr_verify_leaf_domain_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dvr.dvr_verify_leaf_domain_id(device_name, interface, domain_id)

	Robot API Call: 

		dvr_verify_leaf_domain_id  device_name  interface  domain_id

