# Keyword Library Documentation for Fdb
This feature is located in this file: `fdb.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: set_agetime
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_set_agetime(device_name )

	Robot API Call: 

		fdb_set_agetime  device_name  

UUID: 736ac064-ce1f-4dee-afca-fb6a4319bac4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set mac agetime {agetime}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure fdb agingtime {agetime}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mac-address-table aging-time {agetime}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mac-address-table aging-time {agetime}

----------------------------------------------


## REST
## SNMP
# API Function: set_agetime_conversational
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_set_agetime_conversational(device_name )

	Robot API Call: 

		fdb_set_agetime_conversational  device_name  

UUID: a492eead-986d-4e65-aa59-412dcc2f963e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mac-address-table aging-time conversational {agetime}

----------------------------------------------


## REST
## SNMP
# API Function: set_agetime_min
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_set_agetime_min(device_name )

	Robot API Call: 

		fdb_set_agetime_min  device_name  

UUID: b19aed04-3660-4ec2-a109-b0f1c570666e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set mac agetime {agetime}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure fdb agingtime {agetime}

----------------------------------------------


## REST
## SNMP
# API Function: clear_agetime
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_agetime(device_name )

	Robot API Call: 

		fdb_clear_agetime  device_name  

UUID: 66f14371-91fd-4033-8f27-ff150c64064f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac agetime

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure fdb agingtime 300

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		default mac-address-table aging-time

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no mac-address-table aging-time

----------------------------------------------


## REST
## SNMP
# API Function: clear_agetime_conversational
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_agetime_conversational(device_name )

	Robot API Call: 

		fdb_clear_agetime_conversational  device_name  

UUID: efbe4303-7299-4609-933e-e3cba7f5eff2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no mac-address-table aging-time conversational

----------------------------------------------


## REST
## SNMP
# API Function: set_fdb_learn_mode_conversational
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_set_fdb_learn_mode_conversational(device_name )

	Robot API Call: 

		fdb_set_fdb_learn_mode_conversational  device_name  

UUID: 0051f0b5-6ee6-4192-be05-c9f983a7921c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mac-address-table learning-mode conversational

----------------------------------------------


## REST
## SNMP
# API Function: clear_fdb_learn_mode
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_fdb_learn_mode(device_name )

	Robot API Call: 

		fdb_clear_fdb_learn_mode  device_name  

UUID: d8621faf-21ea-4ad5-9920-1258bdcf1701
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no mac-address-table learning-mode

----------------------------------------------


## REST
## SNMP
# API Function: enable_unicast_as_multicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_enable_unicast_as_multicast(device_name )

	Robot API Call: 

		fdb_enable_unicast_as_multicast  device_name  

UUID: 47b3a54d-ba99-476d-8c5d-b49a30be417b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set mac unicast-as-multicast enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_unicast_as_multicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_disable_unicast_as_multicast(device_name )

	Robot API Call: 

		fdb_disable_unicast_as_multicast  device_name  

UUID: c337fe5a-94e8-4bf2-8936-97395a846603
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set mac unicast-as-multicast disable

----------------------------------------------


## REST
## SNMP
# API Function: clear_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_all(device_name )

	Robot API Call: 

		fdb_clear_all  device_name  

UUID: 254dbcd8-83ed-4264-8cc8-2a3f9861e262
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac all

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear fdb

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac-address-table dynamic

----------------------------------------------


## REST
## SNMP
# API Function: clear_all_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_all_vlan(device_name )

	Robot API Call: 

		fdb_clear_all_vlan  device_name  

UUID: 102b660f-4c7f-4da0-9428-df884f789080
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac fid {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear fdb vlan {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan mac-address-entry {vlan} flush

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac-address-table dynamic vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: clear_all_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_all_port(device_name )

	Robot API Call: 

		fdb_clear_all_port  device_name  

UUID: f8a712ed-edd6-402f-8f72-233e9db3b554
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac port-string {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear fdb ports {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		action flushMacFdb

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac-address-table dynamic interface {port}

----------------------------------------------


## REST
## SNMP
# API Function: clear_all_linecard
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_all_linecard(device_name )

	Robot API Call: 

		fdb_clear_all_linecard  device_name  

UUID: 8858fcda-16c3-4834-9354-166ec6639f2c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac-address-table dynamic linecard {linecard}

----------------------------------------------


## REST
## SNMP
# API Function: clear_all_linecard_rbid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_all_linecard_rbid(device_name )

	Robot API Call: 

		fdb_clear_all_linecard_rbid  device_name  

UUID: 759183ec-93e6-428f-930f-ee5c6492a562
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac-address-table dynamic linecard {linecard} rbridge-id {rbid}

----------------------------------------------


## REST
## SNMP
# API Function: create_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_create_entry(device_name )

	Robot API Call: 

		fdb_create_entry  device_name  

UUID: ab3fbbd4-53b0-4e10-811e-a1e5a6177ffe
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set mac unicast {<str_utils.normalize_mac>mac} {vlan} {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create fdb {<str_utils.normalize_mac>mac} vlan {vlan_name} ports {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		vlan mac-address-static {vlan} {<str_utils.normalize_mac>mac} {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mac-address-table static {<str_utils.normalize_mac>mac} forward ethernet {port} vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: create_multicast_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_create_multicast_entry(device_name )

	Robot API Call: 

		fdb_create_multicast_entry  device_name  

UUID: fe3435c2-b44b-45fa-9ceb-ffc249c6b962
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set mac multicast {<str_utils.normalize_mac>mac} {vlan} {[<api_utils.eos_fdb_portlist>port]}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create fdb {<str_utils.normalize_mac>mac} vlan {vlan_name} ports {[<api_utils.exos_fdb_portlist>port]}

----------------------------------------------


## REST
## SNMP
# API Function: delete_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_delete_entry(device_name )

	Robot API Call: 

		fdb_delete_entry  device_name  

UUID: a7ffbe28-bdad-435e-8cc1-a8cd70494d91
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac address {<str_utils.normalize_mac>mac}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete fdb {<str_utils.normalize_mac>mac} vlan {vlan_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no vlan mac-address-static {vlan} {<str_utils.normalize_mac>mac}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac-address-table dynamic address {<str_utils.normalize_mac>mac}

----------------------------------------------


## REST
## SNMP
# API Function: create_blackhole_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_create_blackhole_entry(device_name )

	Robot API Call: 

		fdb_create_blackhole_entry  device_name  

UUID: d2e810e2-d4a5-4775-b7b2-dc087479edc7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create fdb {<str_utils.normalize_mac>mac} vlan {vlan_name} blackhole

----------------------------------------------


## REST
## SNMP
# API Function: enable_learning
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_enable_learning(device_name )

	Robot API Call: 

		fdb_enable_learning  device_name  

UUID: 1b7c9c68-7fb4-4ac9-bf13-672a4ccafc27
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no mac-learning disable

----------------------------------------------


## REST
## SNMP
# API Function: enable_learning_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_enable_learning_vlan(device_name )

	Robot API Call: 

		fdb_enable_learning_vlan  device_name  

UUID: e0863cc7-fd58-463e-9152-c041ab212648
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable learning vlan {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mac-learning disable vlan remove {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: enable_learning_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_enable_learning_port(device_name )

	Robot API Call: 

		fdb_enable_learning_port  device_name  

UUID: 8040411f-9a0b-4627-97a4-30145a1625f0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable learning port {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_learning
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_disable_learning(device_name )

	Robot API Call: 

		fdb_disable_learning  device_name  

UUID: 4be32eb9-a507-4cbb-89f3-a1161120e7e5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mac-learning disable

----------------------------------------------


## REST
## SNMP
# API Function: disable_learning_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_disable_learning_vlan(device_name )

	Robot API Call: 

		fdb_disable_learning_vlan  device_name  

UUID: 7a410a50-052d-4560-bd7d-974fb0e45cfb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable learning vlan {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mac-learning disable vlan add {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: disable_learning_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_disable_learning_port(device_name )

	Robot API Call: 

		fdb_disable_learning_port  device_name  

UUID: d49dc04a-9fcb-4e05-ac51-1a4107d6123f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable learning port {port}

----------------------------------------------


## REST
## SNMP
# API Function: clear_mac_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_mac_port(device_name )

	Robot API Call: 

		fdb_clear_mac_port  device_name  

UUID: 6e6956b8-7388-499d-9ad4-011889173bab
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac-address-table port {port} address {<str_utils.normalize_mac>mac}

----------------------------------------------


## REST
## SNMP
# API Function: clear_mac_port_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_mac_port_vlan(device_name )

	Robot API Call: 

		fdb_clear_mac_port_vlan  device_name  

UUID: 5a282653-5135-4c64-bce5-872b907725c0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac-address-table port {port} address {<str_utils.normalize_mac>mac} interface vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: clear_dynamic_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_clear_dynamic_entry(device_name )

	Robot API Call: 

		fdb_clear_dynamic_entry  device_name  

UUID: 8fa25d83-1e10-4208-8bb4-681351ac937e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear mac-address-table dynamic {<str_utils.normalize_mac>mac} {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: fdb_verify_agetime
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_verify_agetime(device_name)

	Robot API Call: 

		fdb_verify_agetime  device_name

# API Function: fdb_verify_entry_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_verify_entry_exists(device_name, mac, vlan, port)

	Robot API Call: 

		fdb_verify_entry_exists  device_name  mac  vlan  port

# API Function: fdb_verify_entry_has_only_one_instance
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_verify_entry_has_only_one_instance(device_name, mac)

	Robot API Call: 

		fdb_verify_entry_has_only_one_instance  device_name  mac

# API Function: fdb_verify_entry_has_only_two_instances
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_verify_entry_has_only_two_instances(device_name, mac)

	Robot API Call: 

		fdb_verify_entry_has_only_two_instances  device_name  mac

# API Function: fdb_verify_entry_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_verify_entry_does_not_exist(device_name, mac, vlan, port)

	Robot API Call: 

		fdb_verify_entry_does_not_exist  device_name  mac  vlan  port

# API Function: fdb_verify_entries_all_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_verify_entries_all_exist(device_name, mac, vlan, port)

	Robot API Call: 

		fdb_verify_entries_all_exist  device_name  mac  vlan  port

# API Function: fdb_verify_entry_exists_for_duration
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.fdb.fdb_verify_entry_exists_for_duration(device_name, mac, vlan, port, max_wait, interval)

	Robot API Call: 

		fdb_verify_entry_exists_for_duration  device_name  mac  vlan  port  max_wait  interval

