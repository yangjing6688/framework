# Keyword Library Documentation for Spbm
This feature is located in this file: `spbm.yaml` (in this directory: econ-automation-framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /econ-automation-framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/econ-automation-framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: set_ethertype
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_ethertype(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_ethertype(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_enable_global(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_disable_global(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_enable_ip_shortcut(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_disable_ip_shortcut(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_enable_ipv6_shortcut(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_disable_ipv6_shortcut(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_enable_lsdb_trap(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_disable_lsdb_trap(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_isis_instance_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_isis_instance_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_isis_nickname(device_name, spbm_id, nickname)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_isis_nickname(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_isis_bvid(device_name, spbm_id, pri_vlan, sec_vlan)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_isis_bvid(device_name, spbm_id, pri_vlan, sec_vlan)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_enable_isis_multicast(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_disable_isis_multicast(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_isis_multicast_fwd_cache_timeout(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_isis_multicast_fwd_cache_timeout(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_isis_smlt_virtual_bmac(device_name, spbm_id, bmac)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_isis_smlt_virtual_bmac(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_isis_smlt_peer_system_id(device_name, spbm_id, peer_id)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_isis_smlt_peer_system_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_port_isis_instance_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_port_isis_instance_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_mlt_isis_instance_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_mlt_isis_instance_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_port_isis_interface_type_broadcast(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_port_isis_interface_type_p2p(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_port_isis_interface_type(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_mlt_isis_interface_type_broadcast(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_mlt_isis_interface_type_p2p(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_mlt_isis_interface_type(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_port_isis_l1_metric(device_name, port, spbm_id, metric)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_port_isis_l1_metric(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_mlt_isis_l1_metric(device_name, mlt_id, spbm_id, metric)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_mlt_isis_l1_metric(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_logical_interface_isis_instance_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_logical_interface_isis_instance_id(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_logical_interface_isis_interface_type_broadcast(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_logical_interface_isis_interface_type_p2p(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_logical_interface_isis_interface_type(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_logical_interface_isis_l1_metric(device_name, isis_id, spbm_id, metric)

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_logical_interface_isis_l1_metric(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_set_virtual_ist_peer_ip(device_name )

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

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_clear_virtual_ist_peer_ip(device_name )

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
# API Function: show_virtual_ist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_virtual_ist(device_name )

	Robot API Call: 

		spbm_show_virtual_ist  device_name  

UUID: 85f347a1-7907-402c-800c-31d34824ff74
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show virtual-ist

----------------------------------------------


## REST
## SNMP
# API Function: show_virtual_ist_stat
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_virtual_ist_stat(device_name )

	Robot API Call: 

		spbm_show_virtual_ist_stat  device_name  

UUID: ddd852a4-e745-49c6-97fb-89dc8c3580e2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show virtual-ist stat

----------------------------------------------


## REST
## SNMP
# API Function: show_info
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_info(device_name )

	Robot API Call: 

		spbm_show_info  device_name  

UUID: 20304340-d70a-41d6-9b92-b3605cca7ce1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show spbm

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.78.1.2.0||1.3.6.1.4.1.2272.1.78.1.4.0

----------------------------------------------


# API Function: show_isis_info
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_info(device_name )

	Robot API Call: 

		spbm_show_isis_info  device_name  

UUID: f38a8fa5-adea-49fc-9e5a-d9d6888ba7a8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4

----------------------------------------------


# API Function: show_isis_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_interface(device_name )

	Robot API Call: 

		spbm_show_isis_interface  device_name  

UUID: cda4da94-7df5-480e-b115-0e20fec130d0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis interface

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.2.1||1.3.6.1.4.1.2272.1.63.5.1

----------------------------------------------


# API Function: show_isis_isid_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_all(device_name )

	Robot API Call: 

		spbm_show_isis_isid_all  device_name  

UUID: 6aaff610-ed87-4cb8-86db-48f2415a152b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid all

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_all_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_all_id(device_name )

	Robot API Call: 

		spbm_show_isis_isid_all_id  device_name  

UUID: 84ba13a6-f186-4072-9051-68d54d3868f4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid all id {isid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_all_nickname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_all_nickname(device_name )

	Robot API Call: 

		spbm_show_isis_isid_all_nickname  device_name  

UUID: ca4cd2d9-8234-4d14-8561-52040825bbb9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid all nick-name {nickname}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_all_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_all_vlan(device_name )

	Robot API Call: 

		spbm_show_isis_isid_all_vlan  device_name  

UUID: 4a199aa8-de33-436a-bfe3-934e12312a5e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid all vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_config
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_config(device_name )

	Robot API Call: 

		spbm_show_isis_isid_config  device_name  

UUID: 546c48b6-3aa9-4d21-b202-d7e68e45d879
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid config

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_config_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_config_id(device_name )

	Robot API Call: 

		spbm_show_isis_isid_config_id  device_name  

UUID: a813f307-4ee7-47f0-8224-0e88062d5a75
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid config id {isid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_config_nickname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_config_nickname(device_name )

	Robot API Call: 

		spbm_show_isis_isid_config_nickname  device_name  

UUID: aa02b940-4107-41c1-83fb-a6408b6f7b0b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid config nick_name {nickname}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_config_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_config_vlan(device_name )

	Robot API Call: 

		spbm_show_isis_isid_config_vlan  device_name  

UUID: f98ff251-fb5e-4bf5-8855-0b8612e4b49a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid config vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_discover
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_discover(device_name )

	Robot API Call: 

		spbm_show_isis_isid_discover  device_name  

UUID: 7ba509bd-1c56-4426-a02e-08a62e309e58
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid discover

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_discover_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_discover_id(device_name )

	Robot API Call: 

		spbm_show_isis_isid_discover_id  device_name  

UUID: 3d46862a-521f-4823-9ff2-2dd5f6013538
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid discover id {isid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_discover_nickname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_discover_nickname(device_name )

	Robot API Call: 

		spbm_show_isis_isid_discover_nickname  device_name  

UUID: f03943bc-66c5-4d1e-b8a8-dfb039e4afee
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid discover nick_name {nickname}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_isid_discover_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_isid_discover_vlan(device_name )

	Robot API Call: 

		spbm_show_isis_isid_discover_vlan  device_name  

UUID: 9fb77ae6-311e-46ef-840f-f9a1f44a332c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm i-sid discover vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_fib
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_fib(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_fib  device_name  

UUID: 688d8188-b637-42a7-9bee-cbcb0f3355d7
## CLI
## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.27

----------------------------------------------


# API Function: show_isis_ip_multicast_route
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route  device_name  

UUID: b1e56535-cb34-4439-8906-6a8c787c669d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.24

----------------------------------------------


# API Function: show_isis_ip_multicast_route_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_all(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_all  device_name  

UUID: 25a8be76-e467-4adc-b670-85e569849602
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route all

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.24

----------------------------------------------


# API Function: show_isis_ip_multicast_route_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_detail(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_detail  device_name  

UUID: d47d1372-a1bd-41c7-8469-2d7b39b2c40e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route detail

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.24

----------------------------------------------


# API Function: show_isis_ip_multicast_route_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_group(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_group  device_name  

UUID: e255b177-0af9-423c-97ce-7cf7bbbb7657
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route group {ip}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_group_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_group_detail(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_group_detail  device_name  

UUID: 09df1e63-0560-4fd1-b2eb-6580a1027d62
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route group {ip} detail

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_group_source
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_group_source(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_group_source  device_name  

UUID: 97285fd3-343c-4298-919d-3c9a38cfa5bd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route group {ip} source {sip}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_group_source_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_group_source_detail(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_group_source_detail  device_name  

UUID: 2f1f1cee-b388-4787-a1b9-859ab2a97d62
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route group {ip} source {sip} detail

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_group_source_beb
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_group_source_beb(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_group_source_beb  device_name  

UUID: 28c0a5e2-8a50-4b15-ab3a-7285412eed48
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route group {ip} source {sip} source-beb {name}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vlan(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vlan  device_name  

UUID: ed61f828-c8e0-4ab9-b3b6-96353a285041
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vlan_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vlan_detail(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vlan_detail  device_name  

UUID: 9a1cfa34-00d0-43cf-8dfd-001b48f391e9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vlan {vlan} detail

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vlan_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vlan_group(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vlan_group  device_name  

UUID: 6e571d88-0455-4f55-9f2e-8ba41ecbbdca
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vlan {vlan} group {ip}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vlan_group_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vlan_group_detail(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vlan_group_detail  device_name  

UUID: 75e5d20c-3889-47ce-b796-e6299cebd287
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vlan {vlan} group {ip} detail

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vlan_group_source
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vlan_group_source(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vlan_group_source  device_name  

UUID: d7401950-0ee9-4729-aa87-2a5eccd91a60
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vlan {vlan} group {ip} source {sip}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vlan_group_source_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vlan_group_source_detail(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vlan_group_source_detail  device_name  

UUID: 6a9efcb3-93f6-4f6a-911b-4c4d0a1bdb10
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vlan {vlan} group {ip} source {sip} detail

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vlan_group_source_beb
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vlan_group_source_beb(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vlan_group_source_beb  device_name  

UUID: 36bb3f43-08d5-4962-8f59-2b3d40e8b348
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vlan {vlan} group {ip} source {sip} source-beb {name}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vrf(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vrf  device_name  

UUID: 500c4a72-076b-47d9-b016-e68d5649aef6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vrf_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vrf_detail(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vrf_detail  device_name  

UUID: c79a9a5c-bb12-4d1a-8250-8594604fcb7a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vrf {vrf} detail

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vrf_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vrf_group(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vrf_group  device_name  

UUID: 2ea4ba67-33e5-4ffa-bfd3-ccf0e2d37353
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vrf {vrf} group {ip}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vsn_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vsn_isid(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vsn_isid  device_name  

UUID: 45dee8c1-2d37-4080-bd8c-222f660260ac
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vsn-isid {isid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vsn_isid_etail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vsn_isid_etail(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vsn_isid_etail  device_name  

UUID: fc40c6f8-b252-495a-98bb-204740ea3965
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vsn-isid {isid} detail

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_multicast_route_vsn_isid_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_multicast_route_vsn_isid_group(device_name )

	Robot API Call: 

		spbm_show_isis_ip_multicast_route_vsn_isid_group  device_name  

UUID: 021e1b78-cda4-4711-af84-f9e83a17c3c7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-multicast-route vsn-isid {isid} group {ip}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_unicast_fib
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_unicast_fib(device_name )

	Robot API Call: 

		spbm_show_isis_ip_unicast_fib  device_name  

UUID: 74b7ecbf-7afc-4886-9020-21d6dd2717bf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-unicast-fib

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.21

----------------------------------------------


# API Function: show_isis_ipv6_unicast_fib
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ipv6_unicast_fib(device_name )

	Robot API Call: 

		spbm_show_isis_ipv6_unicast_fib  device_name  

UUID: 86c0e7c0-4cb7-4b8f-9bca-8f38b18a79dc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ipv6-unicast-fib

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ipv6_unicast_fib_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ipv6_unicast_fib_id(device_name )

	Robot API Call: 

		spbm_show_isis_ipv6_unicast_fib_id  device_name  

UUID: 974e07ad-f503-4eaa-afe9-d465c40bb535
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ipv6-unicast-fib id {isid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_unicast_fib_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_unicast_fib_id(device_name )

	Robot API Call: 

		spbm_show_isis_ip_unicast_fib_id  device_name  

UUID: 2aacd9a0-b2ef-47f1-b2b3-0be284497eee
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-unicast-fib id {isid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_ip_unicast_fib_spbm_nh_as_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_ip_unicast_fib_spbm_nh_as_mac(device_name )

	Robot API Call: 

		spbm_show_isis_ip_unicast_fib_spbm_nh_as_mac  device_name  

UUID: 6abe888e-0778-4441-92ad-8b73a3f565e4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm ip-unicast-fib spbm-nh-as-mac

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.21

----------------------------------------------


# API Function: show_isis_multicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_multicast(device_name )

	Robot API Call: 

		spbm_show_isis_multicast  device_name  

UUID: 700ffaea-223f-4e77-947e-15cb876d70e5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm multicast

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.4.1.12.0||1.3.6.1.4.1.2272.1.63.4.1.13.0

----------------------------------------------


# API Function: show_isis_multicast_fib
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_multicast_fib(device_name )

	Robot API Call: 

		spbm_show_isis_multicast_fib  device_name  

UUID: f380acb6-ea96-4678-962b-534b49184b25
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm multicast-fib

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.14.1

----------------------------------------------


# API Function: show_isis_multicast_fib_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_multicast_fib_detail(device_name )

	Robot API Call: 

		spbm_show_isis_multicast_fib_detail  device_name  

UUID: 94a0acb9-7f92-4a90-bb02-2bec71405305
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm multicast-fib detail

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.27

----------------------------------------------


# API Function: show_isis_multicast_fib_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_multicast_fib_isid(device_name )

	Robot API Call: 

		spbm_show_isis_multicast_fib_isid  device_name  

UUID: 8f7e88a9-8577-4d18-b334-befd18aec1ef
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm multicast-fib i-sid {isid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_multicast_fib_nickname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_multicast_fib_nickname(device_name )

	Robot API Call: 

		spbm_show_isis_multicast_fib_nickname  device_name  

UUID: 01897b97-ee9f-44f6-b8a1-bc97966343eb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm multicast-fib nick-name {nickname}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_multicast_fib_summary
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_multicast_fib_summary(device_name )

	Robot API Call: 

		spbm_show_isis_multicast_fib_summary  device_name  

UUID: 58279390-2ac9-43c0-b937-369e4924ff90
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm multicast-fib summary

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_multicast_fib_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_multicast_fib_vlan(device_name )

	Robot API Call: 

		spbm_show_isis_multicast_fib_vlan  device_name  

UUID: dc0b4750-adc6-42a6-a353-4acbc4e52f66
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm multicast-fib vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_nickname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_nickname(device_name )

	Robot API Call: 

		spbm_show_isis_nickname  device_name  

UUID: c5bae896-780c-4af7-bccb-d92d4eca20c2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm nick-name {nickname}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_nickname_smlt_virtual_bmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_nickname_smlt_virtual_bmac(device_name )

	Robot API Call: 

		spbm_show_isis_nickname_smlt_virtual_bmac  device_name  

UUID: 484ce639-0c92-438a-8b32-e54d2688911e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm nick-name smlt-virtual-bmac {bmac}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_nickname_sysid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_nickname_sysid(device_name )

	Robot API Call: 

		spbm_show_isis_nickname_sysid  device_name  

UUID: efcaaa77-8512-4d3b-9ed2-2fc46f736d38
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm nick-name sysid {sysid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_unicast_fib
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_unicast_fib(device_name )

	Robot API Call: 

		spbm_show_isis_unicast_fib  device_name  

UUID: d81f45ec-39a7-47fb-a6a5-f75eeadf0e8b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm unicast-fib

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.63.13

----------------------------------------------


# API Function: show_isis_unicast_fib_bmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_unicast_fib_bmac(device_name )

	Robot API Call: 

		spbm_show_isis_unicast_fib_bmac  device_name  

UUID: 6905d0f9-1a1c-4d1c-bdac-c36e78b53744
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm unicast-fib b-mac {bmac}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_unicast_fib_summary
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_unicast_fib_summary(device_name )

	Robot API Call: 

		spbm_show_isis_unicast_fib_summary  device_name  

UUID: aebace63-c304-4635-9050-e2200854284e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm unicast-fib summary

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_unicast_fib_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_unicast_fib_vlan(device_name )

	Robot API Call: 

		spbm_show_isis_unicast_fib_vlan  device_name  

UUID: 9afe47bf-98e0-409e-80a5-66e25e7d50f4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm unicast-fib vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_unicast_tree
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_unicast_tree(device_name )

	Robot API Call: 

		spbm_show_isis_unicast_tree  device_name  

UUID: f199dac4-9c45-4f7b-8ccd-798b2d0b576f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm unicast-tree {bvlan}

----------------------------------------------


## REST
## SNMP
# API Function: show_isis_unicast_tree_destination
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isis_unicast_tree_destination(device_name )

	Robot API Call: 

		spbm_show_isis_unicast_tree_destination  device_name  

UUID: 1b724108-2b98-4356-a79b-bf1af8befb8a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show isis spbm unicast-tree {bvlan} destination {sysid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isid(device_name )

	Robot API Call: 

		spbm_show_isid  device_name  

UUID: 8227f5c7-3bc4-48d9-b7cc-fa40f3cf4b79
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid {isid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isid_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isid_all(device_name )

	Robot API Call: 

		spbm_show_isid_all  device_name  

UUID: 7881482f-6e66-44b6-85e3-da76313cb7f2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid

----------------------------------------------


## REST
## SNMP
# API Function: show_isid_elan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isid_elan(device_name )

	Robot API Call: 

		spbm_show_isid_elan  device_name  

UUID: a7f6dbcb-c532-4317-965d-7bf6b78383f7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid elan

----------------------------------------------


## REST
## SNMP
# API Function: show_isid_elan_transparent
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isid_elan_transparent(device_name )

	Robot API Call: 

		spbm_show_isid_elan_transparent  device_name  

UUID: 9e150c48-0151-4e77-b17c-988475c44bf4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid elan-transparent

----------------------------------------------


## REST
## SNMP
# API Function: show_isid_mac_address_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isid_mac_address_entry(device_name )

	Robot API Call: 

		spbm_show_isid_mac_address_entry  device_name  

UUID: be027d23-b56f-48a3-8f69-455f18b892d9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid mac-address-entry {isid}

----------------------------------------------


## REST
## SNMP
# API Function: show_isid_mac_address_entry_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isid_mac_address_entry_all(device_name )

	Robot API Call: 

		spbm_show_isid_mac_address_entry_all  device_name  

UUID: 6f2ea73f-b0cd-48b5-bad9-bc4cf20d9244
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid mac-address-entry

----------------------------------------------


## REST
## SNMP
# API Function: show_isid_mac_address_entry_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isid_mac_address_entry_mac(device_name )

	Robot API Call: 

		spbm_show_isid_mac_address_entry_mac  device_name  

UUID: 81993a78-2287-40a1-81ec-675a3338cff3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid mac-address-entry mac {mac}

----------------------------------------------


## REST
## SNMP
# API Function: show_isid_mac_address_entry_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isid_mac_address_entry_port(device_name )

	Robot API Call: 

		spbm_show_isid_mac_address_entry_port  device_name  

UUID: ef151f57-2e54-4593-a9b3-96706e8d3a42
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid mac-address-entry port {port}

----------------------------------------------


## REST
## SNMP
# API Function: show_isid_mac_address_entry_remote
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSpbmGenKeywords.spbm_show_isid_mac_address_entry_remote(device_name )

	Robot API Call: 

		spbm_show_isid_mac_address_entry_remote  device_name  

UUID: dc0bfd0a-155a-4a07-b3d0-fc59676c4210
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show i-sid mac-address-entry remote

----------------------------------------------


## REST
## SNMP
