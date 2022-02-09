# Keyword Library Documentation for Mlag
This feature is located in this file: `mlag.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: enable_port_peer_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_enable_port_peer_id(device_name, port, peer, pid)

	Robot API Call: 

		mlag_enable_port_peer_id  device_name  port  peer  pid

UUID: 0b8e33d5-a856-431c-b6af-08773902b814
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable mlag port {port} peer {peer} id {pid}

----------------------------------------------


## REST
## SNMP
# API Function: enable_port_reload_delay
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_enable_port_reload_delay(device_name )

	Robot API Call: 

		mlag_enable_port_reload_delay  device_name  

UUID: 3baa4d4e-76db-4630-b6d1-66b762d8e99b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable mlag port reload-delay

----------------------------------------------


## REST
## SNMP
# API Function: disable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_disable_port(device_name )

	Robot API Call: 

		mlag_disable_port  device_name  

UUID: 1ba93bc2-e255-4189-85da-38546cd52484
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable mlag port {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_port_reload_delay
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_disable_port_reload_delay(device_name )

	Robot API Call: 

		mlag_disable_port_reload_delay  device_name  

UUID: f9d7e823-ee46-436a-8525-6e42abd57292
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable mlag port reload-delay

----------------------------------------------


## REST
## SNMP
# API Function: create_peer
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_create_peer(device_name )

	Robot API Call: 

		mlag_create_peer  device_name  

UUID: d6090d24-851a-4809-a2d0-c5de13f07719
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create mlag peer {peer}

----------------------------------------------


## REST
## SNMP
# API Function: create_peer_auth_md5_key
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_create_peer_auth_md5_key(device_name )

	Robot API Call: 

		mlag_create_peer_auth_md5_key  device_name  

UUID: 6078f6fa-eb08-4508-a326-1d1b7282842a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create mlag peer {peer} authentication md5 key

----------------------------------------------


## REST
## SNMP
# API Function: create_peer_auth_md5_key_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_create_peer_auth_md5_key_name(device_name )

	Robot API Call: 

		mlag_create_peer_auth_md5_key_name  device_name  

UUID: 728b7687-90f1-4750-9558-a420850486b2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create mlag peer {peer} authentication md5 key {key}

----------------------------------------------


## REST
## SNMP
# API Function: create_peer_auth_md5_key_encrypted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_create_peer_auth_md5_key_encrypted(device_name )

	Robot API Call: 

		mlag_create_peer_auth_md5_key_encrypted  device_name  

UUID: 83442bb1-ee4a-414c-ad3a-ef70cde3634e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create mlag peer {peer} authentication md5 key encrypted {key}

----------------------------------------------


## REST
## SNMP
# API Function: delete_peer
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_delete_peer(device_name )

	Robot API Call: 

		mlag_delete_peer  device_name  

UUID: 8419a4eb-1be3-48f2-82d0-3284815a2de9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete mlag peer {peer}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer(device_name )

	Robot API Call: 

		mlag_set_peer  device_name  

UUID: d12c0189-3659-41ef-90ca-6a3d776775d1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_alternate_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_alternate_ip(device_name )

	Robot API Call: 

		mlag_set_peer_alternate_ip  device_name  

UUID: c4fe5069-51eb-40d9-9215-408154383cd7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} alternate ipaddress {ip}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_alternate_ip_none
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_alternate_ip_none(device_name )

	Robot API Call: 

		mlag_set_peer_alternate_ip_none  device_name  

UUID: dc20052e-7934-445c-a61f-56911277d22d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} alternate ipaddress none

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_alternate_ip_vr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_alternate_ip_vr(device_name )

	Robot API Call: 

		mlag_set_peer_alternate_ip_vr  device_name  

UUID: 2554033b-28e7-4acc-8f31-8a2134ae5150
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} alternate ipaddress {ip} vr {vr}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_auth_none
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_auth_none(device_name )

	Robot API Call: 

		mlag_set_peer_auth_none  device_name  

UUID: cf428def-4046-4837-aea3-52789a6181be
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} authentication none

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_auth_md5_key
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_auth_md5_key(device_name )

	Robot API Call: 

		mlag_set_peer_auth_md5_key  device_name  

UUID: 2a38a015-79ad-4f94-b2ac-e577a5821c93
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} authentication md5 key

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_auth_md5_key_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_auth_md5_key_name(device_name )

	Robot API Call: 

		mlag_set_peer_auth_md5_key_name  device_name  

UUID: 88183926-ddef-45dd-9d17-6e9ac74f48b2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} authentication md5 key {key}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_auth_md5_key_encrypted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_auth_md5_key_encrypted(device_name )

	Robot API Call: 

		mlag_set_peer_auth_md5_key_encrypted  device_name  

UUID: eea9d78d-99cf-4ce8-90e2-e4d619d2df37
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} authentication md5 key encrypted {key}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_interval(device_name )

	Robot API Call: 

		mlag_set_peer_interval  device_name  

UUID: 3c8d7a3c-4d90-4bf3-96f9-3221055bdbe7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} interval {interval}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_ipaddress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_ipaddress(device_name, peer, ip)

	Robot API Call: 

		mlag_set_peer_ipaddress  device_name  peer  ip

UUID: 14c2e6cf-1e10-4a24-b460-175714cbd854
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} ipaddress {ip}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_ipaddress_vr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_ipaddress_vr(device_name, peer, ip, vr)

	Robot API Call: 

		mlag_set_peer_ipaddress_vr  device_name  peer  ip  vr

UUID: f0a99314-5fd4-4de2-97a4-2bf2d12a1b64
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} ipaddress {ip} vr {vr}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_lacp_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_lacp_mac(device_name )

	Robot API Call: 

		mlag_set_peer_lacp_mac  device_name  

UUID: e4d3e1e5-002e-42ca-877e-00c031076cc0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} lacp-mac {mac}

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_lacp_mac_auto
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_lacp_mac_auto(device_name )

	Robot API Call: 

		mlag_set_peer_lacp_mac_auto  device_name  

UUID: 5467213f-ae96-4762-bd87-e01435a68c11
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} lacp-mac auto

----------------------------------------------


## REST
## SNMP
# API Function: set_peer_new_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_set_peer_new_name(device_name, peer, name)

	Robot API Call: 

		mlag_set_peer_new_name  device_name  peer  name

UUID: 5ee749cf-6635-4b08-8009-904a5692bd98
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mlag peer {peer} name {name}

----------------------------------------------


## REST
## SNMP
# API Function: show_peer
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_show_peer(device_name )

	Robot API Call: 

		mlag_show_peer  device_name  

UUID: 18c01586-d6ad-49c2-8dc5-d5c94e2e4343
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show mlag peer {peer}

----------------------------------------------


## REST
## SNMP
# API Function: show_peer_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_show_peer_all(device_name )

	Robot API Call: 

		mlag_show_peer_all  device_name  

UUID: e9f85c68-c116-4539-a42e-440172315425
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show mlag peer

----------------------------------------------


## REST
## SNMP
# API Function: show_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_show_ports(device_name )

	Robot API Call: 

		mlag_show_ports  device_name  

UUID: 13a9eb43-00e9-4f9e-ba20-e43295a0d37e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show mlag ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: show_ports_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mlag.mlag_show_ports_all(device_name )

	Robot API Call: 

		mlag_show_ports_all  device_name  

UUID: bf864b86-2ae1-43b4-b3b2-d976b017cbae
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show mlag ports

----------------------------------------------


## REST
## SNMP
