# Keyword Library Documentation for Macsec
This feature is located in this file: `macsec.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

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
# API Function: show
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show(device_name )

	Robot API Call: 

		macsec_show  device_name  

UUID: 74b4a151-0750-4a8a-a517-2d38020705c9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec

----------------------------------------------


## REST
## SNMP
# API Function: show_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show_port(device_name )

	Robot API Call: 

		macsec_show_port  device_name  

UUID: 37d44773-2324-41d4-8f0b-f9598032bb1f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: show_port_configuration
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show_port_configuration(device_name )

	Robot API Call: 

		macsec_show_port_configuration  device_name  

UUID: 226173dd-ee7b-400a-bef1-b0596a0e1f43
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec ports {port} configuration

----------------------------------------------


## REST
## SNMP
# API Function: show_port_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show_port_detail(device_name )

	Robot API Call: 

		macsec_show_port_detail  device_name  

UUID: b71624f5-cf44-4ada-b5fb-30d9db0fb416
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec ports {port} detail

----------------------------------------------


## REST
## SNMP
# API Function: show_port_counters
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show_port_counters(device_name )

	Robot API Call: 

		macsec_show_port_counters  device_name  

UUID: 84da5599-b18b-408e-9e94-d6851a2f5989
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec ports {port} detail | begin "SecY Interface Statistics"

----------------------------------------------


## REST
## SNMP
# API Function: show_port_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show_port_all(device_name )

	Robot API Call: 

		macsec_show_port_all  device_name  

UUID: 98724d26-bf74-4ac8-a968-2464089fe8c9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec ports all

----------------------------------------------


## REST
## SNMP
# API Function: show_port_all_config
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show_port_all_config(device_name )

	Robot API Call: 

		macsec_show_port_all_config  device_name  

UUID: 2da424eb-8975-4468-b929-52aa754c9948
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec ports all configuration

----------------------------------------------


## REST
## SNMP
# API Function: show_port_all_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show_port_all_detail(device_name )

	Robot API Call: 

		macsec_show_port_all_detail  device_name  

UUID: a81825d5-5fff-48ca-9e60-2ba8d00b3ee7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec ports all detail

----------------------------------------------


## REST
## SNMP
# API Function: show_connectivity_association
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show_connectivity_association(device_name )

	Robot API Call: 

		macsec_show_connectivity_association  device_name  

UUID: d9de53c4-5be3-43cd-b8d4-33052a211c74
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec connectivity-association {ca_name}

----------------------------------------------


## REST
## SNMP
# API Function: show_connectivity_association_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macsec.macsec_show_connectivity_association_all(device_name )

	Robot API Call: 

		macsec_show_connectivity_association_all  device_name  

UUID: 3a2df81f-d76c-49e1-9d88-d2256b6b26cf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show macsec connectivity-association

----------------------------------------------


## REST
## SNMP
