# Keyword Library Documentation for Vpex
This feature is located in this file: `vpex.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_enable_global(device_name )

	Robot API Call: 

		vpex_enable_global  device_name  

UUID: ad5e8fd5-07f8-4894-a55a-66207c4141ad
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable vpex

----------------------------------------------


## REST
## SNMP
# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_disable_global(device_name )

	Robot API Call: 

		vpex_disable_global  device_name  

UUID: 3a292f45-5876-478a-b74d-d77acdbb1899
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable vpex

----------------------------------------------


## REST
## SNMP
# API Function: enable_auto_configuration
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_enable_auto_configuration(device_name )

	Robot API Call: 

		vpex_enable_auto_configuration  device_name  

UUID: 457451ee-6dfc-4c54-8188-a8dd65cab4aa
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable vpex auto-configuration

----------------------------------------------


## REST
## SNMP
# API Function: disable_auto_configuration
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_disable_auto_configuration(device_name )

	Robot API Call: 

		vpex_disable_auto_configuration  device_name  

UUID: ac3de84b-ca95-4ade-ad84-d0a5ccce75ed
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable vpex auto-configuration

----------------------------------------------


## REST
## SNMP
# API Function: set_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_set_ports(device_name )

	Robot API Call: 

		vpex_set_ports  device_name  

UUID: fcd6f07b-9815-49cd-902c-8037df898def
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vpex ports {port} slot {slot}

----------------------------------------------


## REST
## SNMP
# API Function: clear_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_clear_ports(device_name )

	Robot API Call: 

		vpex_clear_ports  device_name  

UUID: c93965cf-c7c6-4699-a240-fb69d14c0e72
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure vpex ports {port} slot

----------------------------------------------


## REST
## SNMP
# API Function: set_ring_rebalancing_auto
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_set_ring_rebalancing_auto(device_name )

	Robot API Call: 

		vpex_set_ring_rebalancing_auto  device_name  

UUID: 38d8b33b-d2d7-4551-a008-af9dbcc390c4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vpex ring rebalancing auto

----------------------------------------------


## REST
## SNMP
# API Function: set_ring_rebalancing_off
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_set_ring_rebalancing_off(device_name )

	Robot API Call: 

		vpex_set_ring_rebalancing_off  device_name  

UUID: e86cc601-ec3c-4e0e-b84e-be7957d7bb7b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vpex ring rebalancing off

----------------------------------------------


## REST
## SNMP
# API Function: show_info
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_info(device_name )

	Robot API Call: 

		vpex_show_info  device_name  

UUID: ecdf3468-4f27-458b-a3d8-6991cc1058a3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe(device_name )

	Robot API Call: 

		vpex_show_bpe  device_name  

UUID: 81e59da1-f439-484c-9eb6-1c0d87ef8f8c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_cpu_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_cpu_utilization(device_name )

	Robot API Call: 

		vpex_show_bpe_cpu_utilization  device_name  

UUID: 947ebd0f-f016-409c-8335-0ddf1a9c29ca
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe cpu-utilization

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_environment
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_environment(device_name )

	Robot API Call: 

		vpex_show_bpe_environment  device_name  

UUID: ff52a45c-fc43-4278-b1a8-40e0ea6930d5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe environment

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_version_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_version_detail(device_name )

	Robot API Call: 

		vpex_show_bpe_version_detail  device_name  

UUID: 25b07336-d377-4829-9af7-2a99708cd7d3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe version detail

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_slot
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_slot(device_name )

	Robot API Call: 

		vpex_show_bpe_slot  device_name  

UUID: 0d74db1c-fb40-4f02-a0b1-0b50c710c1c9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe slot {slot}

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_slot_cpu_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_slot_cpu_utilization(device_name )

	Robot API Call: 

		vpex_show_bpe_slot_cpu_utilization  device_name  

UUID: c54304ee-306a-4eab-a4c8-de90af1cfb05
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe slot {slot} cpu-utilization

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_slot_environment
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_slot_environment(device_name )

	Robot API Call: 

		vpex_show_bpe_slot_environment  device_name  

UUID: 732ab290-1c9d-49fe-b914-636100d7a955
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe slot {slot} environment

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_slot_statistics
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_slot_statistics(device_name )

	Robot API Call: 

		vpex_show_bpe_slot_statistics  device_name  

UUID: af6062d7-c305-4906-a534-dfb50525f3c1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe slot {slot} statistics

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_slot_statistics_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_slot_statistics_detail(device_name )

	Robot API Call: 

		vpex_show_bpe_slot_statistics_detail  device_name  

UUID: 962d7438-5b93-43f5-acc4-94207b5fc057
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe slot {slot} statistics detail

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_slot_version_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_slot_version_detail(device_name )

	Robot API Call: 

		vpex_show_bpe_slot_version_detail  device_name  

UUID: 67b838a9-c612-442a-b6d0-894430f3b7ba
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe slot {slot} version detail

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_statistics
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_statistics(device_name )

	Robot API Call: 

		vpex_show_bpe_statistics  device_name  

UUID: eacb83c3-d0df-4e4a-8870-bc10aeddf7c3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe statistics

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_statistics_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_statistics_detail(device_name )

	Robot API Call: 

		vpex_show_bpe_statistics_detail  device_name  

UUID: 7b0432d1-3248-4741-9e22-0d41ce332e66
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe statistics detail

----------------------------------------------


## REST
## SNMP
# API Function: show_bpe_statistics_detail_slot
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_bpe_statistics_detail_slot(device_name )

	Robot API Call: 

		vpex_show_bpe_statistics_detail_slot  device_name  

UUID: 8e7e3dc3-9ae6-41d4-a52e-dd5dd6c542d7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex bpe statistics detail slot {slot}

----------------------------------------------


## REST
## SNMP
# API Function: show_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_ports(device_name )

	Robot API Call: 

		vpex_show_ports  device_name  

UUID: 13c1c7fe-de4a-4ce6-931b-43fa7a982ab5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex ports

----------------------------------------------


## REST
## SNMP
# API Function: show_ports_ecp_statistics
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_ports_ecp_statistics(device_name )

	Robot API Call: 

		vpex_show_ports_ecp_statistics  device_name  

UUID: 9e1ce645-6cef-4936-8f9d-866c02141a27
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex ports ecp statistics

----------------------------------------------


## REST
## SNMP
# API Function: show_ports_statistics
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_ports_statistics(device_name )

	Robot API Call: 

		vpex_show_ports_statistics  device_name  

UUID: 14b44ec3-2c7e-418f-bd6b-a8badc78487e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex ports statistics

----------------------------------------------


## REST
## SNMP
# API Function: show_ports_statistics_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_ports_statistics_detail(device_name )

	Robot API Call: 

		vpex_show_ports_statistics_detail  device_name  

UUID: ac0b9010-0ff0-4832-b87e-c85270bc1328
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex ports statistics detail

----------------------------------------------


## REST
## SNMP
# API Function: show_topology
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_topology(device_name )

	Robot API Call: 

		vpex_show_topology  device_name  

UUID: 65347b7e-7b26-42a5-9ac2-deee0ca4b633
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex topology

----------------------------------------------


## REST
## SNMP
# API Function: show_topology_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_topology_detail(device_name )

	Robot API Call: 

		vpex_show_topology_detail  device_name  

UUID: 7409021b-1d64-48ba-9686-b41a0778ec59
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex topology detail

----------------------------------------------


## REST
## SNMP
# API Function: show_topology_detail_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_topology_detail_port(device_name )

	Robot API Call: 

		vpex_show_topology_detail_port  device_name  

UUID: a232b920-dddc-4fe0-bb3c-0538dee1b353
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex topology detail port {port}

----------------------------------------------


## REST
## SNMP
# API Function: show_topology_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_topology_port(device_name )

	Robot API Call: 

		vpex_show_topology_port  device_name  

UUID: 00c5c177-da18-4803-8685-d8812613fa6f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex topology port {port}

----------------------------------------------


## REST
## SNMP
# API Function: show_topology_port_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_topology_port_detail(device_name )

	Robot API Call: 

		vpex_show_topology_port_detail  device_name  

UUID: 07630d62-e451-4c60-ada5-46f6cdcfa80e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex topology port {port} detail

----------------------------------------------


## REST
## SNMP
# API Function: show_topology_port_summary
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_topology_port_summary(device_name )

	Robot API Call: 

		vpex_show_topology_port_summary  device_name  

UUID: df64854b-5837-4bd0-81e2-98b0864c4704
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex topology port {port} summary

----------------------------------------------


## REST
## SNMP
# API Function: show_topology_summary
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_topology_summary(device_name )

	Robot API Call: 

		vpex_show_topology_summary  device_name  

UUID: 359e087e-ae2c-439e-9382-69f0ab9ec8a4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex topology summary

----------------------------------------------


## REST
## SNMP
# API Function: show_topology_summary_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.vpex.vpex_show_topology_summary_port(device_name )

	Robot API Call: 

		vpex_show_topology_summary_port  device_name  

UUID: 24b2b1b3-3f53-40f3-a272-f63dd7e9c45a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show vpex topology summary port {port}

----------------------------------------------


## REST
## SNMP
