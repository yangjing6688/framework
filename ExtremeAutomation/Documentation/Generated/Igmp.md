# Command Keyword Library Documentation for Igmp
This feature is located in this file: `igmp.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: set_version
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_set_version(device_name )

	Robot API Call: 

		igmp_set_version  device_name  

UUID: 0aadf5bd-92a0-4eb4-808e-41d4b8cac082
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set igmp enable {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable igmp vlan {vlan_name} {igmp_ver}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||ip igmp version {igmp_ver}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping version {igmp_ver}

----------------------------------------------


## REST
## SNMP
# API Function: set_version_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_set_version_interface(device_name )

	Robot API Call: 

		igmp_set_version_interface  device_name  

UUID: 8aea0bc5-c952-4e2e-816c-e427b8517071
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: interface ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip igmp snooping version {igmp_ver}

----------------------------------------------


## REST
## SNMP
# API Function: enable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_enable_vlan(device_name )

	Robot API Call: 

		igmp_enable_vlan  device_name  

UUID: 641501ff-2725-4c7b-bd1b-d2712089faef
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set igmp enable {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable igmp vlan {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_disable_vlan(device_name )

	Robot API Call: 

		igmp_disable_vlan  device_name  

UUID: 8cf98d6c-2531-4707-8e13-610bbbe5b015
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set igmp disable {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable igmp vlan {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ip igmp snooping enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_snooping
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_enable_snooping(device_name )

	Robot API Call: 

		igmp_enable_snooping  device_name  

UUID: ad3dcd6a-80e3-4722-987c-c0cfe19a9cf0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable igmp snooping

----------------------------------------------


## REST
## SNMP
# API Function: disable_snooping
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_disable_snooping(device_name )

	Robot API Call: 

		igmp_disable_snooping  device_name  

UUID: 33b24c3b-bf5b-4bc3-ae3b-b40feeb4dd32
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable igmp snooping

----------------------------------------------


## REST
## SNMP
# API Function: enable_snooping_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_enable_snooping_vlan(device_name )

	Robot API Call: 

		igmp_enable_snooping_vlan  device_name  

UUID: 60d3ecc1-10ff-48e2-ae92-69fa5da82b0c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable igmp snooping vlan {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||ip igmp snooping

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_snooping_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_disable_snooping_vlan(device_name )

	Robot API Call: 

		igmp_disable_snooping_vlan  device_name  

UUID: 1631f48a-be31-4588-974f-c24c337c12f5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable igmp snooping vlan {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||no ip igmp snooping

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ip igmp snooping enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_snooping_proxy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_enable_snooping_proxy(device_name )

	Robot API Call: 

		igmp_enable_snooping_proxy  device_name  

UUID: 0196a404-68d8-4b0f-83f1-433fc6432474
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable igmp snooping with-proxy

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||ip igmp proxy

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping mrouter interface ethernet {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_snooping_proxy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_disable_snooping_proxy(device_name )

	Robot API Call: 

		igmp_disable_snooping_proxy  device_name  

UUID: 76d57f2c-571e-45b2-b5c0-0a207ba0d9dc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable igmp snooping with-proxy

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||no ip igmp proxy

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ip igmp snooping mrouter interface ethernet {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_querier
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_set_snooping_querier(device_name )

	Robot API Call: 

		igmp_set_snooping_querier  device_name  

UUID: e1aa66d9-a6f6-4b0a-8a7e-0fac3b8ce11a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||ip igmp snoop-querier

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping querier enable

----------------------------------------------


## REST
## SNMP
# API Function: clear_snooping_querier
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_clear_snooping_querier(device_name )

	Robot API Call: 

		igmp_clear_snooping_querier  device_name  

UUID: 3d678401-0b11-4825-b3c8-ed3f8a17ea08
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||no ip igmp snoop-querier

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ip igmp snooping querier enable

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_querier_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_set_snooping_querier_address(device_name, vlan, ip)

	Robot API Call: 

		igmp_set_snooping_querier_address  device_name  vlan  ip

UUID: da64ed04-80dd-4d0c-bf3a-7800e85e490f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||ip igmp snoop-querier-addr {ip}

----------------------------------------------


## REST
## SNMP
# API Function: clear_snooping_querier_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_clear_snooping_querier_address(device_name )

	Robot API Call: 

		igmp_clear_snooping_querier_address  device_name  

UUID: eb8d99c4-0eff-4747-8e35-ef20436b8dc0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||no ip igmp snoop-querier-addr

----------------------------------------------


## REST
## SNMP
# API Function: enable_snooping_compatibility_mode_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_enable_snooping_compatibility_mode_vlan(device_name )

	Robot API Call: 

		igmp_enable_snooping_compatibility_mode_vlan  device_name  

UUID: 9e528319-5811-48ba-8ef8-7c28815237da
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||ip igmp compatibility-mode

----------------------------------------------


## REST
## SNMP
# API Function: disable_snooping_compatibility_mode_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_disable_snooping_compatibility_mode_vlan(device_name )

	Robot API Call: 

		igmp_disable_snooping_compatibility_mode_vlan  device_name  

UUID: cbe934fa-704e-4d48-a21a-3f0d8b15d30e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||no ip igmp compatibility-mode

----------------------------------------------


## REST
## SNMP
# API Function: enable_snooping_dynamic_downgrade_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_enable_snooping_dynamic_downgrade_vlan(device_name )

	Robot API Call: 

		igmp_enable_snooping_dynamic_downgrade_vlan  device_name  

UUID: eda8b88f-e4a8-469e-b265-106c467192f8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||ip igmp dynamic-downgrade-version

----------------------------------------------


## REST
## SNMP
# API Function: disable_snooping_dynamic_downgrade_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_disable_snooping_dynamic_downgrade_vlan(device_name )

	Robot API Call: 

		igmp_disable_snooping_dynamic_downgrade_vlan  device_name  

UUID: a1a8ff37-78c9-403d-8037-aab70629a7da
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||no ip igmp dynamic-downgrade-version

----------------------------------------------


## REST
## SNMP
# API Function: enable_snooping_explicit_host_tracking_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_enable_snooping_explicit_host_tracking_vlan(device_name )

	Robot API Call: 

		igmp_enable_snooping_explicit_host_tracking_vlan  device_name  

UUID: 54ce7d01-39b1-42e6-b7e0-b5d4b39e93b1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}||ip igmp igmpv3-explicit-host-tracking

----------------------------------------------


## REST
## SNMP
# API Function: disable_snooping_explicit_host_tracking_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_disable_snooping_explicit_host_tracking_vlan(device_name )

	Robot API Call: 

		igmp_disable_snooping_explicit_host_tracking_vlan  device_name  

UUID: 9b6b1d1e-ce7a-4d65-a79e-0bf5d2e7d566
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		interface vlan {vlan}no ip igmp igmpv3-explicit-host-tracking

----------------------------------------------


## REST
## SNMP
# API Function: enable_snooping_fast_leave
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_enable_snooping_fast_leave(device_name )

	Robot API Call: 

		igmp_enable_snooping_fast_leave  device_name  

UUID: d2c72ecd-47e2-4f58-86cf-08f36f55b45b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping fast-leave

----------------------------------------------


## REST
## SNMP
# API Function: disable_snooping_fast_leave
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_disable_snooping_fast_leave(device_name )

	Robot API Call: 

		igmp_disable_snooping_fast_leave  device_name  

UUID: c6f3a98b-4179-4ea1-b7d7-468b79315034
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ip igmp snooping fast-leave

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_last_member_query_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_set_snooping_last_member_query_interval(device_name )

	Robot API Call: 

		igmp_set_snooping_last_member_query_interval  device_name  

UUID: 6949f5e5-5f42-4a72-acdf-c24982b417c1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping last-member-query-interval {interval}

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_last_member_query_count
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_set_snooping_last_member_query_count(device_name )

	Robot API Call: 

		igmp_set_snooping_last_member_query_count  device_name  

UUID: 1b1f42c4-3cd1-41c8-9be5-5e2adb9b6f29
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping last-member-query-count {value}

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_query_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_set_snooping_query_interval(device_name )

	Robot API Call: 

		igmp_set_snooping_query_interval  device_name  

UUID: 4e09522e-fdf2-4a99-93a9-58ad6ff39773
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping query-interval {interval}

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_query_max_response_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_set_snooping_query_max_response_time(device_name )

	Robot API Call: 

		igmp_set_snooping_query_max_response_time  device_name  

UUID: cd2a3cb1-3e0a-4fd3-adc2-6d23e9e5d52b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ip igmp snooping query-max-response-time {time}

----------------------------------------------


## REST
## SNMP
# API Function: igmp_verify_enabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_enabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_enabled_on_vlan  device_name  vlan

# API Function: igmp_verify_disabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_disabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_disabled_on_vlan  device_name  vlan

# API Function: igmp_verify_version
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_version(device_name, vlan, version)

	Robot API Call: 

		igmp_verify_version  device_name  vlan  version

# API Function: igmp_verify_snooping_enabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_enabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_enabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_disabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_disabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_disabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_querier_enabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_querier_enabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_querier_enabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_querier_disabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_querier_disabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_querier_disabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_querier_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_querier_address(device_name, vlan, ip)

	Robot API Call: 

		igmp_verify_snooping_querier_address  device_name  vlan  ip

# API Function: igmp_verify_snooping_querier_address_removed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_querier_address_removed(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_querier_address_removed  device_name  vlan

# API Function: igmp_verify_snooping_proxy_enabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_proxy_enabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_proxy_enabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_proxy_disabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_proxy_disabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_proxy_disabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_dynamic_downgrade_enabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_dynamic_downgrade_enabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_dynamic_downgrade_enabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_dynamic_downgrade_disabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_dynamic_downgrade_disabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_dynamic_downgrade_disabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_compatibility_mode_enabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_compatibility_mode_enabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_compatibility_mode_enabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_compatibility_mode_disabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_compatibility_mode_disabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_compatibility_mode_disabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_explicit_host_tracking_enabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_explicit_host_tracking_enabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_explicit_host_tracking_enabled_on_vlan  device_name  vlan

# API Function: igmp_verify_snooping_explicit_host_tracking_disabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_snooping_explicit_host_tracking_disabled_on_vlan(device_name, vlan)

	Robot API Call: 

		igmp_verify_snooping_explicit_host_tracking_disabled_on_vlan  device_name  vlan

# API Function: igmp_verify_group_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_group_exists(device_name, group, vlan, port)

	Robot API Call: 

		igmp_verify_group_exists  device_name  group  vlan  port

# API Function: igmp_verify_group_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.igmp.igmp_verify_group_does_not_exist(device_name, group, vlan, port)

	Robot API Call: 

		igmp_verify_group_does_not_exist  device_name  group  vlan  port

