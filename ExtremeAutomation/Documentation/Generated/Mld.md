# Command Keyword Library Documentation for Mld
This feature is located in this file: `mld.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_enable_vlan(device_name )

	Robot API Call: 

		mld_enable_vlan  device_name  

UUID: fdf9ef13-b6e0-4e40-9778-b37009e57b73
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set mld enable {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable mld {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_disable_vlan(device_name )

	Robot API Call: 

		mld_disable_vlan  device_name  

UUID: ac01e9f9-216e-4148-b8d9-9c814f561fca
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set mld disable {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable mld {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping enable

----------------------------------------------


## REST
## SNMP
# API Function: set_version
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_set_version(device_name, version, vlan, vlan_name)

	Robot API Call: 

		mld_set_version  device_name  version  vlan  vlan_name

UUID: c5dafbcc-5015-4322-9fd1-6a56cadbedde
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set mld config {vlan} mld-version {version}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable mld {vlan_name} {version}

----------------------------------------------


## REST
## SNMP
# API Function: enable_snooping
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_enable_snooping(device_name )

	Robot API Call: 

		mld_enable_snooping  device_name  

UUID: 2dbb6f6e-5680-4f48-b9e2-0c1f898c96a4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable mld snooping vlan {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_snooping
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_disable_snooping(device_name )

	Robot API Call: 

		mld_disable_snooping  device_name  

UUID: 2b2e306b-3c94-498b-b9c2-13b8c0ae10b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable mld snooping vlan {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_snooping_querier
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_enable_snooping_querier(device_name )

	Robot API Call: 

		mld_enable_snooping_querier  device_name  

UUID: 65b02f61-2516-4d37-9afa-13a16a609a97
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping querier enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_snooping_querier
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_disable_snooping_querier(device_name )

	Robot API Call: 

		mld_disable_snooping_querier  device_name  

UUID: 3a36fffa-9295-490b-80bf-e000d805714a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping querier enable

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_fast_leave
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_set_snooping_fast_leave(device_name )

	Robot API Call: 

		mld_set_snooping_fast_leave  device_name  

UUID: f9b1733d-6159-4597-826d-dff13ad888da
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping fast-leave

----------------------------------------------


## REST
## SNMP
# API Function: clear_snooping_fast_leave
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_clear_snooping_fast_leave(device_name )

	Robot API Call: 

		mld_clear_snooping_fast_leave  device_name  

UUID: b732ffd3-870e-40fe-87cb-572820e35061
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping fast-leave

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_last_member_query_count
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_set_snooping_last_member_query_count(device_name )

	Robot API Call: 

		mld_set_snooping_last_member_query_count  device_name  

UUID: 30168a49-720f-488b-add4-79faa0e1ec88
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping last-member-query-count {value}

----------------------------------------------


## REST
## SNMP
# API Function: clear_snooping_last_member_query_count
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_clear_snooping_last_member_query_count(device_name )

	Robot API Call: 

		mld_clear_snooping_last_member_query_count  device_name  

UUID: 01ea4117-bcb2-4926-a0f9-157ff3ed1142
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping last-member-query-count

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_last_member_query_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_set_snooping_last_member_query_interval(device_name )

	Robot API Call: 

		mld_set_snooping_last_member_query_interval  device_name  

UUID: 058cc38d-7123-4aa2-8967-17944d9f34f5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping last-member-query-interval {value}

----------------------------------------------


## REST
## SNMP
# API Function: clear_snooping_last_member_query_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_clear_snooping_last_member_query_interval(device_name )

	Robot API Call: 

		mld_clear_snooping_last_member_query_interval  device_name  

UUID: 40827e1e-d06b-47f3-909e-e50b18aa9f1b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping last-member-query-interval

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_robustness_variable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_set_snooping_robustness_variable(device_name )

	Robot API Call: 

		mld_set_snooping_robustness_variable  device_name  

UUID: 2144237d-6c46-4bbc-9948-e4bb1b274f7a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping robustness-variable {value}

----------------------------------------------


## REST
## SNMP
# API Function: clear_snooping_robustness_variable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_clear_snooping_robustness_variable(device_name )

	Robot API Call: 

		mld_clear_snooping_robustness_variable  device_name  

UUID: e2caa83e-dcfc-4081-acfc-c2528eddc8aa
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping robustness-variable

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_startup_query_count
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_set_snooping_startup_query_count(device_name )

	Robot API Call: 

		mld_set_snooping_startup_query_count  device_name  

UUID: d9564fc5-60cc-44b0-8cfe-840bc9a4ec63
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping startup-query-count {value}

----------------------------------------------


## REST
## SNMP
# API Function: clear_snooping_startup_query_count
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_clear_snooping_startup_query_count(device_name )

	Robot API Call: 

		mld_clear_snooping_startup_query_count  device_name  

UUID: 379c3a65-3448-4bc5-be33-c6d03c954d2a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping startup-query-count

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_startup_query_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_set_snooping_startup_query_interval(device_name )

	Robot API Call: 

		mld_set_snooping_startup_query_interval  device_name  

UUID: 92e59bff-c3f0-40a2-ac3b-2d7380251cbf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping startup-query-interval {value}

----------------------------------------------


## REST
## SNMP
# API Function: clear_snooping_startup_query_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_clear_snooping_startup_query_interval(device_name )

	Robot API Call: 

		mld_clear_snooping_startup_query_interval  device_name  

UUID: c2051e4c-d158-4d14-9ba3-a0564a05a79c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping startup-query-interval

----------------------------------------------


## REST
## SNMP
# API Function: set_snooping_mrouter
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_set_snooping_mrouter(device_name )

	Robot API Call: 

		mld_set_snooping_mrouter  device_name  

UUID: 2ced3098-8888-4ef5-8cc9-783664497def
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||ipv6 mld snooping mrouter interface ethernet {port}

----------------------------------------------


## REST
## SNMP
# API Function: clear_snooping_mrouter
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mld.mld_clear_snooping_mrouter(device_name )

	Robot API Call: 

		mld_clear_snooping_mrouter  device_name  

UUID: 0bbca321-7d96-4f9e-a96a-2a0256e5ee8e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan {vlan}||no ipv6 mld snooping mrouter interface ethernet

----------------------------------------------


## REST
## SNMP
