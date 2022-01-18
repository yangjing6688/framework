# Keyword Library Documentation for Hostservices
This feature is located in this file: `hostservices.yaml` (in this directory: econ-automation-framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /econ-automation-framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/econ-automation-framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: enable_sys_force_topology_ip_flag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementHostservicesGenKeywords.hostservices_enable_sys_force_topology_ip_flag(device_name )

	Robot API Call: 

		hostservices_enable_sys_force_topology_ip_flag  device_name  

UUID: 44ae2093-7a32-4200-9f6b-c76d9048a8a8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		sys force-topology-ip-flag

----------------------------------------------


## REST
## SNMP
# API Function: disable_sys_force_topology_ip_flag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementHostservicesGenKeywords.hostservices_disable_sys_force_topology_ip_flag(device_name )

	Robot API Call: 

		hostservices_disable_sys_force_topology_ip_flag  device_name  

UUID: 0ed942d2-10cd-489d-804e-4e0ff39a37e7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no sys force-topology-ip-flag

----------------------------------------------


## REST
## SNMP
# API Function: set_sys_clipid_topology_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementHostservicesGenKeywords.hostservices_set_sys_clipid_topology_ip(device_name )

	Robot API Call: 

		hostservices_set_sys_clipid_topology_ip  device_name  

UUID: 7dafa48c-20c4-4179-9a54-b6f6cc54e735
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		sys clipId-topology-ip {clip_id}

----------------------------------------------


## REST
## SNMP
# API Function: clear_sys_clipid_topology_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementHostservicesGenKeywords.hostservices_clear_sys_clipid_topology_ip(device_name )

	Robot API Call: 

		hostservices_clear_sys_clipid_topology_ip  device_name  

UUID: ee66147e-6a71-43b9-b73a-4cd7defa0dc7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no sys clipId-topology-ip

----------------------------------------------


## REST
## SNMP
# API Function: show_sys_setting
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementHostservicesGenKeywords.hostservices_show_sys_setting(device_name )

	Robot API Call: 

		hostservices_show_sys_setting  device_name  

UUID: f60ea537-ad29-4c8a-96bf-bfaa679d2433
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show sys setting

----------------------------------------------


## REST
## SNMP
# API Function: show_autotopology_nmm_table
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementHostservicesGenKeywords.hostservices_show_autotopology_nmm_table(device_name )

	Robot API Call: 

		hostservices_show_autotopology_nmm_table  device_name  

UUID: 99b9efa8-9d29-4288-80d3-d56a2cf16193
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show autotopology nmm-table

----------------------------------------------


## REST
## SNMP
