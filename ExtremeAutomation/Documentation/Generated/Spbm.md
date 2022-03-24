# Command Keyword Library Documentation for Spbm
This feature is located in this file: `spbm.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: set_ethertype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_ethertype(device_name )

	Robot API Call: 

		spbm_set_ethertype  device_name  

UUID: c136f8ab-cc0c-4550-b157-14943892b971
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		spbm ethertype {ethertype}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.78.1.4.0

----------------------------------------------


# API Function: clear_ethertype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_ethertype(device_name )

	Robot API Call: 

		spbm_clear_ethertype  device_name  

UUID: a3ccaba0-b9f5-4a61-9069-77da2ffd4ce7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		spbm ethertype 0x8100

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.78.1.4.0

----------------------------------------------


# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_enable_global(device_name )

	Robot API Call: 

		spbm_enable_global  device_name  

UUID: 78fe268a-16fd-4bb1-8364-18e2d22d09c0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		spbm

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.78.1.2.0

----------------------------------------------


# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_disable_global(device_name )

	Robot API Call: 

		spbm_disable_global  device_name  

UUID: 39d9011e-4241-496a-959d-34ffb37fd6af
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no spbm

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.78.1.2.0

----------------------------------------------


# API Function: enable_ip_shortcut
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_enable_ip_shortcut(device_name )

	Robot API Call: 

		spbm_enable_ip_shortcut  device_name  

UUID: 5a85377b-4858-4507-a4d8-60aa9bf085f8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id} ip enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.7.{spbm_id}

----------------------------------------------


# API Function: disable_ip_shortcut
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_disable_ip_shortcut(device_name )

	Robot API Call: 

		spbm_disable_ip_shortcut  device_name  

UUID: a11b78c4-42a0-4a47-a525-952db7cb3108
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id} ip enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.7.{spbm_id}

----------------------------------------------


# API Function: enable_ipv6_shortcut
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_enable_ipv6_shortcut(device_name )

	Robot API Call: 

		spbm_enable_ipv6_shortcut  device_name  

UUID: c6574c76-301b-41f9-8c33-a098e8756360
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id} ipv6 enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.14.{spbm_id}

----------------------------------------------


# API Function: disable_ipv6_shortcut
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_disable_ipv6_shortcut(device_name )

	Robot API Call: 

		spbm_disable_ipv6_shortcut  device_name  

UUID: 90574270-cc2f-4bdd-b312-cbea48df779f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id} ipv6 enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.14.{spbm_id}

----------------------------------------------


# API Function: enable_lsdb_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_enable_lsdb_trap(device_name )

	Robot API Call: 

		spbm_enable_lsdb_trap  device_name  

UUID: 8ca085e9-24b2-4751-a584-e6a399327607
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id} lsdb-trap enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.5.{spbm_id}

----------------------------------------------


# API Function: disable_lsdb_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_disable_lsdb_trap(device_name )

	Robot API Call: 

		spbm_disable_lsdb_trap  device_name  

UUID: 01e46e45-6aaa-40e1-9fb1-d450ab581c9d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id} lsdb-trap enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.5.{spbm_id}

----------------------------------------------


# API Function: set_isis_instance_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_isis_instance_id(device_name )

	Robot API Call: 

		spbm_set_isis_instance_id  device_name  

UUID: ce70f188-0c68-4c9e-a499-cc09aad52c3f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.2.{spbm_id}

----------------------------------------------


# API Function: clear_isis_instance_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_isis_instance_id(device_name )

	Robot API Call: 

		spbm_clear_isis_instance_id  device_name  

UUID: 81819efc-1e95-4272-a8ad-a69cc382a529
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.2.{spbm_id}

----------------------------------------------


# API Function: set_isis_nickname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_isis_nickname(device_name, spbm_id, nickname)

	Robot API Call: 

		spbm_set_isis_nickname  device_name  spbm_id  nickname

UUID: 5825a7d7-957a-4ef1-9dfe-4f68e69e5f57
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id} nick-name {nickname}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.3.{spbm_id}

----------------------------------------------


# API Function: clear_isis_nickname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_isis_nickname(device_name )

	Robot API Call: 

		spbm_clear_isis_nickname  device_name  

UUID: 8389ed74-dbb8-4d6d-8e10-6ffdd4e0ad4d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id} nick-name||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.3.{spbm_id}

----------------------------------------------


# API Function: set_isis_bvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_isis_bvid(device_name, spbm_id, pri_vlan, sec_vlan)

	Robot API Call: 

		spbm_set_isis_bvid  device_name  spbm_id  pri_vlan  sec_vlan

UUID: 9033b7a0-92fb-4a58-b047-2c5c3bccec6c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id} b-vid {pri_vlan},{sec_vlan} primary {pri_vlan}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.4.{spbm_id}||1.3.6.1.4.1.2272.1.63.4.1.8.{spbm_id}

----------------------------------------------


# API Function: clear_isis_bvid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_isis_bvid(device_name, spbm_id, pri_vlan, sec_vlan)

	Robot API Call: 

		spbm_clear_isis_bvid  device_name  spbm_id  pri_vlan  sec_vlan

UUID: 64c86061-df56-4766-bf61-a9a130e2394f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id} b-vid {pri_vlan},{sec_vlan}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.4.{spbm_id}

----------------------------------------------


# API Function: enable_isis_multicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_enable_isis_multicast(device_name )

	Robot API Call: 

		spbm_enable_isis_multicast  device_name  

UUID: 43378da1-621e-4a13-9373-b74a0cb3ee28
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id} multicast enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.12.{spbm_id}

----------------------------------------------


# API Function: disable_isis_multicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_disable_isis_multicast(device_name )

	Robot API Call: 

		spbm_disable_isis_multicast  device_name  

UUID: f8f6903f-34c3-4496-bcda-9c940f3ebf6a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id} multicast enable||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.12.{spbm_id}

----------------------------------------------


# API Function: set_isis_multicast_fwd_cache_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_isis_multicast_fwd_cache_timeout(device_name )

	Robot API Call: 

		spbm_set_isis_multicast_fwd_cache_timeout  device_name  

UUID: 03473550-1e69-4362-a42e-3310392d4c36
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id} multicast fwd-cache-timeout {timeout}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.13.{spbm_id}

----------------------------------------------


# API Function: clear_isis_multicast_fwd_cache_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_isis_multicast_fwd_cache_timeout(device_name )

	Robot API Call: 

		spbm_clear_isis_multicast_fwd_cache_timeout  device_name  

UUID: de7738f1-f145-421e-97f6-3889870c4e08
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id} multicast fwd-cache-timeout||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.13.{spbm_id}

----------------------------------------------


# API Function: set_isis_smlt_virtual_bmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_isis_smlt_virtual_bmac(device_name, spbm_id, bmac)

	Robot API Call: 

		spbm_set_isis_smlt_virtual_bmac  device_name  spbm_id  bmac

UUID: 0875014c-78b5-40ec-a015-4a6419985d1b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id} smlt-virtual-bmac {bmac}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.10.{spbm_id}

----------------------------------------------


# API Function: clear_isis_smlt_virtual_bmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_isis_smlt_virtual_bmac(device_name )

	Robot API Call: 

		spbm_clear_isis_smlt_virtual_bmac  device_name  

UUID: 8e860b4d-187f-4b1a-8624-10cf14f75845
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id} smlt-virtual-bmac||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.10.{spbm_id}

----------------------------------------------


# API Function: set_isis_smlt_peer_system_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_isis_smlt_peer_system_id(device_name, spbm_id, peer_id)

	Robot API Call: 

		spbm_set_isis_smlt_peer_system_id  device_name  spbm_id  peer_id

UUID: c2730f12-5a57-4b2c-a89c-918a93ff7b96
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||spbm {spbm_id} smlt-peer-system-id {peer_id}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.11.{spbm_id}

----------------------------------------------


# API Function: clear_isis_smlt_peer_system_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_isis_smlt_peer_system_id(device_name )

	Robot API Call: 

		spbm_clear_isis_smlt_peer_system_id  device_name  

UUID: 0eb30dfe-5354-42dc-b17c-e8fa8edeff30
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		router isis||no spbm {spbm_id} smlt-peer-system-id||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.11.{spbm_id}

----------------------------------------------


# API Function: set_port_isis_instance_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_port_isis_instance_id(device_name )

	Robot API Call: 

		spbm_set_port_isis_instance_id  device_name  

UUID: a0337bcb-f440-43ff-862a-4472a9992f3b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.3.{port}.{spbm_id}||1.3.6.1.4.1.2272.1.63.5.1.4.{port}.{spbm_id}

----------------------------------------------


# API Function: clear_port_isis_instance_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_port_isis_instance_id(device_name )

	Robot API Call: 

		spbm_clear_port_isis_instance_id  device_name  

UUID: a0478d48-a84c-4783-b92a-f8292ccd0d15
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no isis spbm {spbm_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.3.{port}.{spbm_id}

----------------------------------------------


# API Function: set_mlt_isis_instance_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_mlt_isis_instance_id(device_name )

	Robot API Call: 

		spbm_set_mlt_isis_instance_id  device_name  

UUID: ce782566-ba3a-4dfb-b2e5-1c7664d58888
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.3.{mlt_id}.{spbm_id}||1.3.6.1.4.1.2272.1.63.5.1.4.{mlt_id}.{spbm_id}

----------------------------------------------


# API Function: clear_mlt_isis_instance_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_mlt_isis_instance_id(device_name )

	Robot API Call: 

		spbm_clear_mlt_isis_instance_id  device_name  

UUID: 5eda73f9-ee72-41a8-8570-d35c7040a610
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`:  mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no isis spbm {spbm_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.3.{mlt_id}.{spbm_id}

----------------------------------------------


# API Function: set_port_isis_interface_type_broadcast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_port_isis_interface_type_broadcast(device_name )

	Robot API Call: 

		spbm_set_port_isis_interface_type_broadcast  device_name  

UUID: c7d6f404-b060-4a5e-ba12-57c44106aad3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} interface-type broadcast

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.5.{port}.{spbm_id}

----------------------------------------------


# API Function: set_port_isis_interface_type_p2p
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_port_isis_interface_type_p2p(device_name )

	Robot API Call: 

		spbm_set_port_isis_interface_type_p2p  device_name  

UUID: 2e8a85c0-0b45-434b-bd73-8cf9f34661cc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} interface-type pt-pt

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.5.{port}.{spbm_id}

----------------------------------------------


# API Function: clear_port_isis_interface_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_port_isis_interface_type(device_name )

	Robot API Call: 

		spbm_clear_port_isis_interface_type  device_name  

UUID: 44c01d4f-a214-42b8-9e90-c9ec26bdf4a4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} interface-type pt-pt

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.5.{port}.{spbm_id}

----------------------------------------------


# API Function: set_mlt_isis_interface_type_broadcast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_mlt_isis_interface_type_broadcast(device_name )

	Robot API Call: 

		spbm_set_mlt_isis_interface_type_broadcast  device_name  

UUID: 78613ac3-c70b-4ef7-a63f-9f0d232ff9f0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} interface-type broadcast

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.5.{mlt_id}.{spbm_id}

----------------------------------------------


# API Function: set_mlt_isis_interface_type_p2p
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_mlt_isis_interface_type_p2p(device_name )

	Robot API Call: 

		spbm_set_mlt_isis_interface_type_p2p  device_name  

UUID: 491b2ef5-3da5-47fd-ba16-03c7b7a46e74
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} interface-type pt-pt

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.5.{mlt_id}.{spbm_id}

----------------------------------------------


# API Function: clear_mlt_isis_interface_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_mlt_isis_interface_type(device_name )

	Robot API Call: 

		spbm_clear_mlt_isis_interface_type  device_name  

UUID: 8db6ac4d-ccde-4888-8a0c-f87fb988d674
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} interface-type pt-pt

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.5.{mlt_id}.{spbm_id}

----------------------------------------------


# API Function: set_port_isis_l1_metric
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_port_isis_l1_metric(device_name, port, spbm_id, metric)

	Robot API Call: 

		spbm_set_port_isis_l1_metric  device_name  port  spbm_id  metric

UUID: 192c93b3-a9c6-437a-ad7c-a394db290ecf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} l1-metric {metric}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.7.{port}.{spbm_id}

----------------------------------------------


# API Function: clear_port_isis_l1_metric
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_port_isis_l1_metric(device_name )

	Robot API Call: 

		spbm_clear_port_isis_l1_metric  device_name  

UUID: 118919a5-184c-48f3-b968-01263df60f94
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} l1-metric 10

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.7.{port}.{spbm_id}

----------------------------------------------


# API Function: set_mlt_isis_l1_metric
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_mlt_isis_l1_metric(device_name, mlt_id, spbm_id, metric)

	Robot API Call: 

		spbm_set_mlt_isis_l1_metric  device_name  mlt_id  spbm_id  metric

UUID: 4fe99065-df6e-47e4-b341-e3149e3a90d5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} l1-metric {metric}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.7.{mlt_id}.{spbm_id}

----------------------------------------------


# API Function: clear_mlt_isis_l1_metric
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_mlt_isis_l1_metric(device_name )

	Robot API Call: 

		spbm_clear_mlt_isis_l1_metric  device_name  

UUID: db58c4ab-d6d5-488c-a445-f3bdd4ac9994
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: mlt {mlt_id}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		isis spbm {spbm_id} l1-metric 10

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.7.{mlt_id}.{spbm_id}

----------------------------------------------


# API Function: set_logical_interface_isis_instance_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_logical_interface_isis_instance_id(device_name )

	Robot API Call: 

		spbm_set_logical_interface_isis_instance_id  device_name  

UUID: 102d76c8-b7ef-46d2-8676-02e680dd5b3e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis spbm {spbm_id}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.3.{isis_id}.{spbm_id}||1.3.6.1.4.1.2272.1.63.5.1.4.{isis_id}.{spbm_id}

----------------------------------------------


# API Function: clear_logical_interface_isis_instance_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_logical_interface_isis_instance_id(device_name )

	Robot API Call: 

		spbm_clear_logical_interface_isis_instance_id  device_name  

UUID: fc371754-1f33-49e2-ba2a-1b8e99285a86
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||no isis spbm {spbm_id}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.3.{isis_id}.{spbm_id}

----------------------------------------------


# API Function: set_logical_interface_isis_interface_type_broadcast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_logical_interface_isis_interface_type_broadcast(device_name )

	Robot API Call: 

		spbm_set_logical_interface_isis_interface_type_broadcast  device_name  

UUID: 7499a7ff-6e7a-4fd2-8016-c316b08543e6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis spbm {spbm_id} interface-type broadcast||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.5.{isis_id}.{spbm_id}

----------------------------------------------


# API Function: set_logical_interface_isis_interface_type_p2p
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_logical_interface_isis_interface_type_p2p(device_name )

	Robot API Call: 

		spbm_set_logical_interface_isis_interface_type_p2p  device_name  

UUID: 2e674775-61f4-4e42-a16e-2abd9233bbc9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis spbm {spbm_id} interface-type pt-pt||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.5.{isis_id}.{spbm_id}

----------------------------------------------


# API Function: clear_logical_interface_isis_interface_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_logical_interface_isis_interface_type(device_name )

	Robot API Call: 

		spbm_clear_logical_interface_isis_interface_type  device_name  

UUID: e69ab934-b0f6-4d59-b73a-8f0618030cdb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis spbm {spbm_id} interface-type pt-pt||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.5.{isis_id}.{spbm_id}

----------------------------------------------


# API Function: set_logical_interface_isis_l1_metric
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_logical_interface_isis_l1_metric(device_name, isis_id, spbm_id, metric)

	Robot API Call: 

		spbm_set_logical_interface_isis_l1_metric  device_name  isis_id  spbm_id  metric

UUID: cf049f1e-8540-4415-9bc9-655b87514d9a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis spbm {spbm_id} l1-metric {metric}||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.7.{isis_id}.{spbm_id}

----------------------------------------------


# API Function: clear_logical_interface_isis_l1_metric
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_logical_interface_isis_l1_metric(device_name )

	Robot API Call: 

		spbm_clear_logical_interface_isis_l1_metric  device_name  

UUID: efb270e6-bc64-48c7-a852-70bb9ad3941e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		logical-intf isis {isis_id}||isis spbm {spbm_id} l1-metric 1000||exit

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.5.1.7.{isis_id}.{spbm_id}

----------------------------------------------


# API Function: set_virtual_ist_peer_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_set_virtual_ist_peer_ip(device_name )

	Robot API Call: 

		spbm_set_virtual_ist_peer_ip  device_name  

UUID: be8d1e54-361c-42a8-a27a-4785671cdd5d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		virtual-ist peer-ip {ip} vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: clear_virtual_ist_peer_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_clear_virtual_ist_peer_ip(device_name )

	Robot API Call: 

		spbm_clear_virtual_ist_peer_ip  device_name  

UUID: d2d8ead0-8751-4d2b-9eba-b46ef94de674
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no virtual-ist peer-ip

----------------------------------------------


## REST
## SNMP
# API Function: spbm_verify_ethertype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_ethertype(device_name, ethertype)

	Robot API Call: 

		spbm_verify_ethertype  device_name  ethertype

# API Function: spbm_verify_globally_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_globally_enabled(device_name)

	Robot API Call: 

		spbm_verify_globally_enabled  device_name

# API Function: spbm_verify_globally_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_globally_disabled(device_name)

	Robot API Call: 

		spbm_verify_globally_disabled  device_name

# API Function: spbm_verify_ip_shortcut_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_ip_shortcut_enabled(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_ip_shortcut_enabled  device_name  spbm_id

# API Function: spbm_verify_ip_shortcut_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_ip_shortcut_disabled(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_ip_shortcut_disabled  device_name  spbm_id

# API Function: spbm_verify_ipv6_shortcut_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_ipv6_shortcut_enabled(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_ipv6_shortcut_enabled  device_name  spbm_id

# API Function: spbm_verify_ipv6_shortcut_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_ipv6_shortcut_disabled(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_ipv6_shortcut_disabled  device_name  spbm_id

# API Function: spbm_verify_instance_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_instance_exists(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_instance_exists  device_name  spbm_id

# API Function: spbm_verify_instance_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_instance_does_not_exist(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_instance_does_not_exist  device_name  spbm_id

# API Function: spbm_verify_nickname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_nickname(device_name, spbm_id, nickname)

	Robot API Call: 

		spbm_verify_nickname  device_name  spbm_id  nickname

# API Function: spbm_verify_vlan_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_vlan_exists(device_name, spbm_id, bvid)

	Robot API Call: 

		spbm_verify_vlan_exists  device_name  spbm_id  bvid

# API Function: spbm_verify_vlan_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_vlan_does_not_exist(device_name, spbm_id, bvid)

	Robot API Call: 

		spbm_verify_vlan_does_not_exist  device_name  spbm_id  bvid

# API Function: spbm_verify_multicast_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_multicast_enabled(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_multicast_enabled  device_name  spbm_id

# API Function: spbm_verify_multicast_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_multicast_disabled(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_multicast_disabled  device_name  spbm_id

# API Function: spbm_verify_lsdb_trap_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_lsdb_trap_enabled(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_lsdb_trap_enabled  device_name  spbm_id

# API Function: spbm_verify_lsdb_trap_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_lsdb_trap_disabled(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_lsdb_trap_disabled  device_name  spbm_id

# API Function: spbm_verify_smlt_bmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_smlt_bmac(device_name, spbm_id, bmac)

	Robot API Call: 

		spbm_verify_smlt_bmac  device_name  spbm_id  bmac

# API Function: spbm_verify_smlt_peer_system_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_smlt_peer_system_id(device_name, spbm_id, peer_sys_id)

	Robot API Call: 

		spbm_verify_smlt_peer_system_id  device_name  spbm_id  peer_sys_id

# API Function: spbm_verify_split_beb_primary
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_split_beb_primary(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_split_beb_primary  device_name  spbm_id

# API Function: spbm_verify_split_beb_secondary
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_split_beb_secondary(device_name, spbm_id)

	Robot API Call: 

		spbm_verify_split_beb_secondary  device_name  spbm_id

# API Function: spbm_verify_isis_instance_exists_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_instance_exists_on_port(device_name, port, spbm_id)

	Robot API Call: 

		spbm_verify_isis_instance_exists_on_port  device_name  port  spbm_id

# API Function: spbm_verify_isis_instance_does_not_exist_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_instance_does_not_exist_on_port(device_name, port, spbm_id)

	Robot API Call: 

		spbm_verify_isis_instance_does_not_exist_on_port  device_name  port  spbm_id

# API Function: spbm_verify_isis_admin_status_enabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_admin_status_enabled_on_port(device_name, port, spbm_id)

	Robot API Call: 

		spbm_verify_isis_admin_status_enabled_on_port  device_name  port  spbm_id

# API Function: spbm_verify_isis_admin_status_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_admin_status_disabled_on_port(device_name, port, spbm_id)

	Robot API Call: 

		spbm_verify_isis_admin_status_disabled_on_port  device_name  port  spbm_id

# API Function: spbm_verify_isis_oper_status_enabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_oper_status_enabled_on_port(device_name, port, spbm_id)

	Robot API Call: 

		spbm_verify_isis_oper_status_enabled_on_port  device_name  port  spbm_id

# API Function: spbm_verify_isis_oper_status_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_oper_status_disabled_on_port(device_name, port, spbm_id)

	Robot API Call: 

		spbm_verify_isis_oper_status_disabled_on_port  device_name  port  spbm_id

# API Function: spbm_verify_isis_total_adjacencies_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_total_adjacencies_on_port(device_name, port, spbm_id, total_adj)

	Robot API Call: 

		spbm_verify_isis_total_adjacencies_on_port  device_name  port  spbm_id  total_adj

# API Function: spbm_verify_isis_up_adjacencies_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_up_adjacencies_on_port(device_name, port, spbm_id, up_adj)

	Robot API Call: 

		spbm_verify_isis_up_adjacencies_on_port  device_name  port  spbm_id  up_adj

# API Function: spbm_verify_isis_l1_metric_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_l1_metric_on_port(device_name, port, spbm_id, l1_metric)

	Robot API Call: 

		spbm_verify_isis_l1_metric_on_port  device_name  port  spbm_id  l1_metric

# API Function: spbm_verify_isis_type_broadcast_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_type_broadcast_on_port(device_name, port, spbm_id)

	Robot API Call: 

		spbm_verify_isis_type_broadcast_on_port  device_name  port  spbm_id

# API Function: spbm_verify_isis_type_point_to_point_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_type_point_to_point_on_port(device_name, port, spbm_id)

	Robot API Call: 

		spbm_verify_isis_type_point_to_point_on_port  device_name  port  spbm_id

# API Function: spbm_verify_isis_instance_exists_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_instance_exists_on_mlt(device_name, mlt_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_instance_exists_on_mlt  device_name  mlt_id  spbm_id

# API Function: spbm_verify_isis_instance_does_not_exist_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_instance_does_not_exist_on_mlt(device_name, mlt_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_instance_does_not_exist_on_mlt  device_name  mlt_id  spbm_id

# API Function: spbm_verify_isis_admin_status_enabled_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_admin_status_enabled_on_mlt(device_name, mlt_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_admin_status_enabled_on_mlt  device_name  mlt_id  spbm_id

# API Function: spbm_verify_isis_admin_status_disabled_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_admin_status_disabled_on_mlt(device_name, mlt_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_admin_status_disabled_on_mlt  device_name  mlt_id  spbm_id

# API Function: spbm_verify_isis_oper_status_enabled_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_oper_status_enabled_on_mlt(device_name, mlt_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_oper_status_enabled_on_mlt  device_name  mlt_id  spbm_id

# API Function: spbm_verify_isis_oper_status_disabled_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_oper_status_disabled_on_mlt(device_name, mlt_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_oper_status_disabled_on_mlt  device_name  mlt_id  spbm_id

# API Function: spbm_verify_isis_total_adjacencies_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_total_adjacencies_on_mlt(device_name, mlt_id, spbm_id, total_adj)

	Robot API Call: 

		spbm_verify_isis_total_adjacencies_on_mlt  device_name  mlt_id  spbm_id  total_adj

# API Function: spbm_verify_isis_up_adjacencies_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_up_adjacencies_on_mlt(device_name, mlt_id, spbm_id, up_adj)

	Robot API Call: 

		spbm_verify_isis_up_adjacencies_on_mlt  device_name  mlt_id  spbm_id  up_adj

# API Function: spbm_verify_isis_l1_metric_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_l1_metric_on_mlt(device_name, mlt_id, spbm_id, l1_metric)

	Robot API Call: 

		spbm_verify_isis_l1_metric_on_mlt  device_name  mlt_id  spbm_id  l1_metric

# API Function: spbm_verify_isis_type_broadcast_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_type_broadcast_on_mlt(device_name, mlt_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_type_broadcast_on_mlt  device_name  mlt_id  spbm_id

# API Function: spbm_verify_isis_type_point_to_point_on_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_type_point_to_point_on_mlt(device_name, mlt_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_type_point_to_point_on_mlt  device_name  mlt_id  spbm_id

# API Function: spbm_verify_isis_instance_exists_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_instance_exists_on_logical_interface(device_name, isis_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_instance_exists_on_logical_interface  device_name  isis_id  spbm_id

# API Function: spbm_verify_isis_instance_does_not_exist_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_instance_does_not_exist_on_logical_interface(device_name, isis_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_instance_does_not_exist_on_logical_interface  device_name  isis_id  spbm_id

# API Function: spbm_verify_isis_admin_status_enabled_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_admin_status_enabled_on_logical_interface(device_name, isis_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_admin_status_enabled_on_logical_interface  device_name  isis_id  spbm_id

# API Function: spbm_verify_isis_admin_status_disabled_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_admin_status_disabled_on_logical_interface(device_name, isis_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_admin_status_disabled_on_logical_interface  device_name  isis_id  spbm_id

# API Function: spbm_verify_isis_oper_status_enabled_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_oper_status_enabled_on_logical_interface(device_name, isis_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_oper_status_enabled_on_logical_interface  device_name  isis_id  spbm_id

# API Function: spbm_verify_isis_oper_status_disabled_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_oper_status_disabled_on_logical_interface(device_name, isis_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_oper_status_disabled_on_logical_interface  device_name  isis_id  spbm_id

# API Function: spbm_verify_isis_total_adjacencies_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_total_adjacencies_on_logical_interface(device_name, isis_id, spbm_id, total_adj)

	Robot API Call: 

		spbm_verify_isis_total_adjacencies_on_logical_interface  device_name  isis_id  spbm_id  total_adj

# API Function: spbm_verify_isis_up_adjacencies_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_up_adjacencies_on_logical_interface(device_name, isis_id, spbm_id, up_adj)

	Robot API Call: 

		spbm_verify_isis_up_adjacencies_on_logical_interface  device_name  isis_id  spbm_id  up_adj

# API Function: spbm_verify_isis_l1_metric_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_l1_metric_on_logical_interface(device_name, isis_id, spbm_id, l1_metric)

	Robot API Call: 

		spbm_verify_isis_l1_metric_on_logical_interface  device_name  isis_id  spbm_id  l1_metric

# API Function: spbm_verify_isis_type_broadcast_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_type_broadcast_on_logical_interface(device_name, isis_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_type_broadcast_on_logical_interface  device_name  isis_id  spbm_id

# API Function: spbm_verify_isis_type_point_to_point_on_logical_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_type_point_to_point_on_logical_interface(device_name, isis_id, spbm_id)

	Robot API Call: 

		spbm_verify_isis_type_point_to_point_on_logical_interface  device_name  isis_id  spbm_id

# API Function: spbm_verify_isis_unicast_fib_host_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_unicast_fib_host_name(device_name, sysid, bvlan, da, hostname)

	Robot API Call: 

		spbm_verify_isis_unicast_fib_host_name  device_name  sysid  bvlan  da  hostname

# API Function: spbm_verify_isis_unicast_fib_cost
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_unicast_fib_cost(device_name, sysid, bvlan, da, cost)

	Robot API Call: 

		spbm_verify_isis_unicast_fib_cost  device_name  sysid  bvlan  da  cost

# API Function: spbm_verify_isis_unicast_fib_outgoing_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_unicast_fib_outgoing_port(device_name, sysid, bvlan, da, port)

	Robot API Call: 

		spbm_verify_isis_unicast_fib_outgoing_port  device_name  sysid  bvlan  da  port

# API Function: spbm_verify_isis_multicast_fwd_cache_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_multicast_fwd_cache_timeout(device_name, spbm_id, timeout)

	Robot API Call: 

		spbm_verify_isis_multicast_fwd_cache_timeout  device_name  spbm_id  timeout

# API Function: spbm_verify_isis_multicast_fib_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_multicast_fib_isid(device_name, sysid, bvlan, da, isid)

	Robot API Call: 

		spbm_verify_isis_multicast_fib_isid  device_name  sysid  bvlan  da  isid

# API Function: spbm_verify_isis_multicast_fib_host_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_multicast_fib_host_name(device_name, sysid, bvlan, da, isid, hostname)

	Robot API Call: 

		spbm_verify_isis_multicast_fib_host_name  device_name  sysid  bvlan  da  isid  hostname

# API Function: spbm_verify_isis_multicast_fib_outbound_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_multicast_fib_outbound_port(device_name, sysid, bvlan, da, isid, port)

	Robot API Call: 

		spbm_verify_isis_multicast_fib_outbound_port  device_name  sysid  bvlan  da  isid  port

# API Function: spbm_verify_isis_multicast_fib_outbound_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_multicast_fib_outbound_mlt(device_name, sysid, bvlan, da, isid, mlt_id)

	Robot API Call: 

		spbm_verify_isis_multicast_fib_outbound_mlt  device_name  sysid  bvlan  da  isid  mlt_id

# API Function: spbm_verify_isis_multicast_fib_inbound_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_multicast_fib_inbound_port(device_name, sysid, bvlan, da, isid, port)

	Robot API Call: 

		spbm_verify_isis_multicast_fib_inbound_port  device_name  sysid  bvlan  da  isid  port

# API Function: spbm_verify_isis_multicast_fib_inbound_mlt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_multicast_fib_inbound_mlt(device_name, sysid, bvlan, da, isid, mlt_id)

	Robot API Call: 

		spbm_verify_isis_multicast_fib_inbound_mlt  device_name  sysid  bvlan  da  isid  mlt_id

# API Function: spbm_verify_isis_multicast_fib_cvlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_multicast_fib_cvlan(device_name, sysid, bvlan, da, isid, cvlan)

	Robot API Call: 

		spbm_verify_isis_multicast_fib_cvlan  device_name  sysid  bvlan  da  isid  cvlan

# API Function: spbm_verify_isis_ip_unicast_fib_destination_network
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_destination_network(device_name, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_destination_network  device_name  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ipv6_unicast_fib_destination_network
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_destination_network(device_name, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_destination_network  device_name  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_nh_beb
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_nh_beb(device_name, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_nh_beb  device_name  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ipv6_unicast_fib_nh_beb
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_nh_beb(device_name, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_nh_beb  device_name  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_bvlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_bvlan(device_name, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_bvlan  device_name  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ipv6_unicast_fib_bvlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_bvlan(device_name, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_bvlan  device_name  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_outgoing_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_outgoing_port(device_name, dest, nh_beb, bvlan, out_int)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_outgoing_port  device_name  dest  nh_beb  bvlan  out_int

# API Function: spbm_verify_isis_ipv6_unicast_fib_outgoing_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_outgoing_port(device_name, dest, nh_beb, bvlan, out_int)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_outgoing_port  device_name  dest  nh_beb  bvlan  out_int

# API Function: spbm_verify_isis_ip_unicast_fib_spbm_cost
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_spbm_cost(device_name, dest, nh_beb, bvlan, spbm_cost)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_spbm_cost  device_name  dest  nh_beb  bvlan  spbm_cost

# API Function: spbm_verify_isis_ipv6_unicast_fib_spbm_cost
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_spbm_cost(device_name, dest, nh_beb, bvlan, spbm_cost)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_spbm_cost  device_name  dest  nh_beb  bvlan  spbm_cost

# API Function: spbm_verify_isis_ip_unicast_fib_prefix_cost
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_prefix_cost(device_name, dest, nh_beb, bvlan, prefix_cost)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_prefix_cost  device_name  dest  nh_beb  bvlan  prefix_cost

# API Function: spbm_verify_isis_ipv6_unicast_fib_prefix_cost
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_prefix_cost(device_name, dest, nh_beb, bvlan, prefix_cost)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_prefix_cost  device_name  dest  nh_beb  bvlan  prefix_cost

# API Function: spbm_verify_isis_ip_unicast_fib_prefix_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_prefix_type(device_name, dest, nh_beb, bvlan, prefix_type)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_prefix_type  device_name  dest  nh_beb  bvlan  prefix_type

# API Function: spbm_verify_isis_ip_unicast_fib_metric_prefix_type_internal
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_metric_prefix_type_internal(device_name, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_metric_prefix_type_internal  device_name  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_metric_prefix_type_external
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_metric_prefix_type_external(device_name, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_metric_prefix_type_external  device_name  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_ip_route_preference
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_ip_route_preference(device_name, dest, nh_beb, bvlan, ip_route_pref)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_ip_route_preference  device_name  dest  nh_beb  bvlan  ip_route_pref

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_name(device_name, dest, nh_beb, bvlan, vrf_name)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_name  device_name  dest  nh_beb  bvlan  vrf_name

# API Function: spbm_verify_isis_ip_unicast_fib_nh_bmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_nh_bmac(device_name, dest, nh_bmac, bvlan, nh_mac)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_nh_bmac  device_name  dest  nh_bmac  bvlan  nh_mac

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid(device_name, dest, nh_beb, bvlan, isid)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid  device_name  dest  nh_beb  bvlan  isid

# API Function: spbm_verify_isis_ip_unicast_fib_destination_network_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_destination_network_isid(device_name, dest, nh_beb, bvlan, dest_isid)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_destination_network_isid  device_name  dest  nh_beb  bvlan  dest_isid

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_name(device_name, vrf_name, isid, dest_isid, dest)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_name  device_name  vrf_name  isid  dest_isid  dest

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_id(device_name, vrf_name, isid, dest_isid, dest)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_id  device_name  vrf_name  isid  dest_isid  dest

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_dest_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_dest_isid(device_name, vrf_name, isid, dest_isid, dest)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_dest_isid  device_name  vrf_name  isid  dest_isid  dest

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_dest_network
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_dest_network(device_name, vrf_name, isid, dest_isid, dest)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_dest_network  device_name  vrf_name  isid  dest_isid  dest

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_nh_beb
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_nh_beb(device_name, vrf_name, isid, dest_isid, dest, nh_beb)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_nh_beb  device_name  vrf_name  isid  dest_isid  dest  nh_beb

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_bvlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_bvlan(device_name, vrf_name, isid, dest_isid, dest, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_bvlan  device_name  vrf_name  isid  dest_isid  dest  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_out_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_out_port(device_name, vrf_name, isid, dest_isid, dest, out_int)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_out_port  device_name  vrf_name  isid  dest_isid  dest  out_int

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_spbm_cost
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_spbm_cost(device_name, vrf_name, isid, dest_isid, dest, spbm_cost)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_spbm_cost  device_name  vrf_name  isid  dest_isid  dest  spbm_cost

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_prefix_cost
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_prefix_cost(device_name, vrf_name, isid, dest_isid, dest, prefix_cost)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_prefix_cost  device_name  vrf_name  isid  dest_isid  dest  prefix_cost

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_ip_route_pref
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_ip_route_pref(device_name, vrf_name, isid, dest_isid, dest, ip_route_pref)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_ip_route_pref  device_name  vrf_name  isid  dest_isid  dest  ip_route_pref

# API Function: spbm_verify_isis_ip_unicast_fib_dest_network_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_dest_network_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_dest_network_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ipv6_unicast_fib_dest_network_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_dest_network_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_dest_network_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_nh_beb_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_nh_beb_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_nh_beb_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ipv6_unicast_fib_nh_beb_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_nh_beb_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_nh_beb_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_bvlan_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_bvlan_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_bvlan_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ipv6_unicast_fib_bvlan_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_bvlan_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_bvlan_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_out_int_port_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_out_int_port_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, out_int)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_out_int_port_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  out_int

# API Function: spbm_verify_isis_ipv6_unicast_fib_out_int_port_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_out_int_port_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, out_int)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_out_int_port_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  out_int

# API Function: spbm_verify_isis_ip_unicast_fib_spbm_cost_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_spbm_cost_by_vrf_name_and_id(vrf_name, isid, dest, nh_beb, bvlan, spbm_cost)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_spbm_cost_by_vrf_name_and_id  vrf_name  isid  dest  nh_beb  bvlan  spbm_cost

# API Function: spbm_verify_isis_ipv6_unicast_fib_spbm_cost_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_spbm_cost_by_vrf_name_and_id(vrf_name, isid, dest, nh_beb, bvlan, spbm_cost)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_spbm_cost_by_vrf_name_and_id  vrf_name  isid  dest  nh_beb  bvlan  spbm_cost

# API Function: spbm_verify_isis_ip_unicast_fib_prefix_cost_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_prefix_cost_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, prefix_cost)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_prefix_cost_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  prefix_cost

# API Function: spbm_verify_isis_ipv6_unicast_fib_prefix_cost_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_prefix_cost_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, prefix_cost)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_prefix_cost_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  prefix_cost

# API Function: spbm_verify_isis_ip_unicast_fib_prefix_type_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_prefix_type_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, prefix_type)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_prefix_type_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  prefix_type

# API Function: spbm_verify_isis_ipv6_unicast_fib_prefix_type_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_prefix_type_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, prefix_type)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_prefix_type_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  prefix_type

# API Function: spbm_verify_isis_ip_unicast_fib_ip_route_pref_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_ip_route_pref_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, ip_route_pref)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_ip_route_pref_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  ip_route_pref

# API Function: spbm_verify_isis_ipv6_unicast_fib_ip_route_pref_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_ip_route_pref_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, ip_route_pref)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_ip_route_pref_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  ip_route_pref

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_name_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_name_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_name_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ipv6_unicast_fib_vrf_name_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_vrf_name_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_vrf_name_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan

# API Function: spbm_verify_isis_ip_unicast_fib_vrf_isid_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_vrf_isid_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, vrf_isid)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_vrf_isid_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  vrf_isid

# API Function: spbm_verify_isis_ipv6_unicast_fib_vrf_isid_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_vrf_isid_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, vrf_isid)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_vrf_isid_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  vrf_isid

# API Function: spbm_verify_isis_ip_unicast_fib_dest_network_isid_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_dest_network_isid_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, dest_isid)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_dest_network_isid_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  dest_isid

# API Function: spbm_verify_isis_ipv6_unicast_fib_dest_network_isid_by_vrf_name_and_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ipv6_unicast_fib_dest_network_isid_by_vrf_name_and_id(device_name, vrf_name, isid, dest, nh_beb, bvlan, dest_isid)

	Robot API Call: 

		spbm_verify_isis_ipv6_unicast_fib_dest_network_isid_by_vrf_name_and_id  device_name  vrf_name  isid  dest  nh_beb  bvlan  dest_isid

# API Function: spbm_verify_isis_ip_unicast_fib_nh_bmac_by_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_unicast_fib_nh_bmac_by_id(device_name, dest, nh_bmac, bvlan, nh_mac, vrf_isid)

	Robot API Call: 

		spbm_verify_isis_ip_unicast_fib_nh_bmac_by_id  device_name  dest  nh_bmac  bvlan  nh_mac  vrf_isid

# API Function: spbm_verify_isis_ip_multicast_route_vrf_entries_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_isis_ip_multicast_route_vrf_entries_exist(device_name, vrf_name, mcast_source, mcast_group, data_isid, bvlan, source_beb)

	Robot API Call: 

		spbm_verify_isis_ip_multicast_route_vrf_entries_exist  device_name  vrf_name  mcast_source  mcast_group  data_isid  bvlan  source_beb

# API Function: spbm_verify_virtual_ist_peer_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_virtual_ist_peer_ip(device_name, ip, vlan)

	Robot API Call: 

		spbm_verify_virtual_ist_peer_ip  device_name  ip  vlan

# API Function: spbm_verify_virtual_ist_peer_ip_is_not
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.spbm.spbm_verify_virtual_ist_peer_ip_is_not(device_name, ip, vlan)

	Robot API Call: 

		spbm_verify_virtual_ist_peer_ip_is_not  device_name  ip  vlan

