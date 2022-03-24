# Command Keyword Library Documentation for Macsec
This feature is located in this file: `macsec.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable_ca_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_enable_ca_port(device_name )

	Robot API Call: 

		macsec_enable_ca_port  device_name  

UUID: 233d8332-a5cf-4fa2-837c-410dd31e62f2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec connectivity-association {ca_name} ports {port} enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_ca_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_disable_ca_port(device_name )

	Robot API Call: 

		macsec_disable_ca_port  device_name  

UUID: cd3c1607-b1dc-4495-832f-a2f20b2977c7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec connectivity-association {ca_name} ports {port} disable

----------------------------------------------


## REST
## SNMP
# API Function: create_ca
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_create_ca(device_name, ca_name, key_name, key)

	Robot API Call: 

		macsec_create_ca  device_name  ca_name  key_name  key

UUID: a04e7d1e-b39d-4cad-a245-60db991ba1b7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create macsec connectivity-association {ca_name} pre-shared-key ckn {key_name} cak {key}

----------------------------------------------


## REST
## SNMP
# API Function: create_ca_encrypted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_create_ca_encrypted(device_name, ca_name, key_name, key)

	Robot API Call: 

		macsec_create_ca_encrypted  device_name  ca_name  key_name  key

UUID: a0ca20f4-aea0-49a2-a8fd-00a39e56ad49
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create macsec connectivity-association {ca_name} pre-shared-key ckn {key_name} cak encrypted {key}

----------------------------------------------


## REST
## SNMP
# API Function: set_cipher_suite_128
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_cipher_suite_128(device_name )

	Robot API Call: 

		macsec_set_cipher_suite_128  device_name  

UUID: bbd3da5f-92d3-4afe-8b25-607855ae6440
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec cipher-suite gcm-aes-128 ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_cipher_suite_256
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_cipher_suite_256(device_name )

	Robot API Call: 

		macsec_set_cipher_suite_256  device_name  

UUID: a7b9178d-d85a-4693-b99f-5a6b1f8d3782
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec cipher-suite gcm-aes-256 ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_confidentiality_offset_0
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_confidentiality_offset_0(device_name )

	Robot API Call: 

		macsec_set_confidentiality_offset_0  device_name  

UUID: 5304635f-dfcf-41a7-b3db-f1d493fd572b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec confidentiality-offset 0 ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_confidentiality_offset_30
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_confidentiality_offset_30(device_name )

	Robot API Call: 

		macsec_set_confidentiality_offset_30  device_name  

UUID: e9182628-08d6-4e6a-820f-70858c15b917
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec confidentiality-offset 30 ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_confidentiality_offset_50
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_confidentiality_offset_50(device_name )

	Robot API Call: 

		macsec_set_confidentiality_offset_50  device_name  

UUID: 34499cc9-cf80-446a-88fd-083d70d7b8ab
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec confidentiality-offset 50 ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_hw_mode_half_duplex_mode
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_hw_mode_half_duplex_mode(device_name )

	Robot API Call: 

		macsec_set_hw_mode_half_duplex_mode  device_name  

UUID: 7b9b0748-794e-441b-9c97-886179b8f54e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec hw-mode half-duplex-mode ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_hw_mode_macsec_mode
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_hw_mode_macsec_mode(device_name )

	Robot API Call: 

		macsec_set_hw_mode_macsec_mode  device_name  

UUID: 749d5636-1cdd-4d82-abaf-58a3968aa4e6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec hw-mode macsec-mode ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_include_sci_enable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_include_sci_enable(device_name )

	Robot API Call: 

		macsec_set_include_sci_enable  device_name  

UUID: 4475d65a-3621-40d9-bb60-c2157f344669
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec include-sci enable ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_include_sci_disable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_include_sci_disable(device_name )

	Robot API Call: 

		macsec_set_include_sci_disable  device_name  

UUID: c1d00df9-5e3b-4fef-b8c7-df599f5b3c7d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec include-sci disable ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_initialize_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_initialize_ports(device_name )

	Robot API Call: 

		macsec_set_initialize_ports  device_name  

UUID: 3676756d-e07b-4357-b6f9-c5cbb106a208
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec initialize ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_mka_actor_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_mka_actor_priority(device_name, priority, port)

	Robot API Call: 

		macsec_set_mka_actor_priority  device_name  priority  port

UUID: 3db645df-a1a1-40ab-bb40-6549a7f6c324
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec mka actor-priority {priority} ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_replay_protect
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_replay_protect(device_name )

	Robot API Call: 

		macsec_set_replay_protect  device_name  

UUID: b63cf63e-1884-4b26-a7b0-ddcf0626f629
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec replay-protect {window_size} ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_replay_protect_disable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_set_replay_protect_disable(device_name )

	Robot API Call: 

		macsec_set_replay_protect_disable  device_name  

UUID: 0a11905d-a90b-4604-ab23-7bdcd0a7aabd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure macsec replay-protect disable ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: clear_counters_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_clear_counters_all(device_name )

	Robot API Call: 

		macsec_clear_counters_all  device_name  

UUID: ba7a6602-7e7d-4f3f-801a-1062113d739e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear macsec counters

----------------------------------------------


## REST
## SNMP
# API Function: clear_counters_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_clear_counters_on_port(device_name )

	Robot API Call: 

		macsec_clear_counters_on_port  device_name  

UUID: e6e8de1d-81b2-4c87-8679-a69b4f4dc48e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear macsec counters ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: delete_ca
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_delete_ca(device_name )

	Robot API Call: 

		macsec_delete_ca  device_name  

UUID: ae4bf96e-121f-4c57-a716-a7eede466818
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete macsec connectivity-association {ca_name}

----------------------------------------------


## REST
## SNMP
# API Function: macsec_verify_enabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_enabled_on_port(device_name, port)

	Robot API Call: 

		macsec_verify_enabled_on_port  device_name  port

# API Function: macsec_verify_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_disabled_on_port(device_name, port)

	Robot API Call: 

		macsec_verify_disabled_on_port  device_name  port

# API Function: macsec_verify_ca_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_ca_port(device_name, ca_name, port)

	Robot API Call: 

		macsec_verify_ca_port  device_name  ca_name  port

# API Function: macsec_verify_ca_ckn
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_ca_ckn(device_name, ca_name, ckn_name)

	Robot API Call: 

		macsec_verify_ca_ckn  device_name  ca_name  ckn_name

# API Function: macsec_verify_ca_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_ca_exists(device_name, ca_name)

	Robot API Call: 

		macsec_verify_ca_exists  device_name  ca_name

# API Function: macsec_verify_ca_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_ca_does_not_exist(device_name, ca_name)

	Robot API Call: 

		macsec_verify_ca_does_not_exist  device_name  ca_name

# API Function: macsec_verify_port_actor_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_port_actor_priority(device_name, priority)

	Robot API Call: 

		macsec_verify_port_actor_priority  device_name  priority

# API Function: macsec_verify_port_removed_from_ca
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_port_removed_from_ca(device_name, ca_name, port)

	Robot API Call: 

		macsec_verify_port_removed_from_ca  device_name  ca_name  port

# API Function: macsec_verify_port_cipher_suite
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_port_cipher_suite(device_name, port, cipher_value)

	Robot API Call: 

		macsec_verify_port_cipher_suite  device_name  port  cipher_value

# API Function: macsec_verify_port_connection_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_port_connection_status(device_name, port, status)

	Robot API Call: 

		macsec_verify_port_connection_status  device_name  port  status

# API Function: macsec_verify_port_cipher_suite_admin
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_port_cipher_suite_admin(device_name, port, suite)

	Robot API Call: 

		macsec_verify_port_cipher_suite_admin  device_name  port  suite

# API Function: macsec_verify_port_cipher_suite_oper
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_port_cipher_suite_oper(device_name, port, suite)

	Robot API Call: 

		macsec_verify_port_cipher_suite_oper  device_name  port  suite

# API Function: macsec_verify_port_confidentiality_offset_admin
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_port_confidentiality_offset_admin(device_name, port, offset)

	Robot API Call: 

		macsec_verify_port_confidentiality_offset_admin  device_name  port  offset

# API Function: macsec_verify_port_confidentiality_offset_oper
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_port_confidentiality_offset_oper(device_name, port, offset)

	Robot API Call: 

		macsec_verify_port_confidentiality_offset_oper  device_name  port  offset

# API Function: macsec_verify_tx_port_key_number
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_tx_port_key_number(device_name, port, tx_key_num)

	Robot API Call: 

		macsec_verify_tx_port_key_number  device_name  port  tx_key_num

# API Function: macsec_verify_rx_port_key_number
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_rx_port_key_number(device_name, port, rx_key_num)

	Robot API Call: 

		macsec_verify_rx_port_key_number  device_name  port  rx_key_num

# API Function: macsec_verify_tx_port_association_number
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_tx_port_association_number(device_name, port, tx_assoc_num)

	Robot API Call: 

		macsec_verify_tx_port_association_number  device_name  port  tx_assoc_num

# API Function: macsec_verify_rx_port_association_number
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_rx_port_association_number(device_name, port, rx_assoc_num)

	Robot API Call: 

		macsec_verify_rx_port_association_number  device_name  port  rx_assoc_num

# API Function: macsec_verify_self_elected_key_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_self_elected_key_server(device_name, port)

	Robot API Call: 

		macsec_verify_self_elected_key_server  device_name  port

# API Function: macsec_verify_peer_elected_key_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_peer_elected_key_server(device_name, port)

	Robot API Call: 

		macsec_verify_peer_elected_key_server  device_name  port

# API Function: macsec_verify_tx_port_no_errors
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_tx_port_no_errors(device_name, port)

	Robot API Call: 

		macsec_verify_tx_port_no_errors  device_name  port

# API Function: macsec_verify_rx_port_no_errors
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_rx_port_no_errors(device_name, port)

	Robot API Call: 

		macsec_verify_rx_port_no_errors  device_name  port

# API Function: macsec_verify_tx_sc_octets_encrypted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_tx_sc_octets_encrypted(device_name, port, count, count_max)

	Robot API Call: 

		macsec_verify_tx_sc_octets_encrypted  device_name  port  count  count_max

# API Function: macsec_verify_tx_sc_encrypted_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_tx_sc_encrypted_packets(device_name, port, count, count_max)

	Robot API Call: 

		macsec_verify_tx_sc_encrypted_packets  device_name  port  count  count_max

# API Function: macsec_verify_tx_sa_encrypted_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_tx_sa_encrypted_packets(device_name, port, count, count_max)

	Robot API Call: 

		macsec_verify_tx_sa_encrypted_packets  device_name  port  count  count_max

# API Function: macsec_verify_rx_sc_octets_decrypted
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_rx_sc_octets_decrypted(device_name, port, count, count_max)

	Robot API Call: 

		macsec_verify_rx_sc_octets_decrypted  device_name  port  count  count_max

# API Function: macsec_verify_rx_sc_ok_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_rx_sc_ok_packets(device_name, port, count, count_max)

	Robot API Call: 

		macsec_verify_rx_sc_ok_packets  device_name  port  count  count_max

# API Function: macsec_verify_rx_sa_ok_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_verify_rx_sa_ok_packets(device_name, port, count, count_max)

	Robot API Call: 

		macsec_verify_rx_sa_ok_packets  device_name  port  count  count_max

