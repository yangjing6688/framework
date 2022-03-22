# Command Keyword Library Documentation for Cos
This feature is located in this file: `cos.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: create_qos_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_create_qos_profile(device_name )

	Robot API Call: 

		cos_create_qos_profile  device_name  

UUID: 66687146-d2d8-4032-9ce3-e462bce8ff76
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create qosprofile {<api_utils.exos_qos_profile>name}

----------------------------------------------


## REST
## SNMP
# API Function: delete_qos_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_delete_qos_profile(device_name )

	Robot API Call: 

		cos_delete_qos_profile  device_name  

UUID: 3fd8faed-e141-4950-9052-0d39b43477ec
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete qosprofile {<api_utils.exos_qos_profile>name}

----------------------------------------------


## REST
## SNMP
# API Function: create_port_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_create_port_group(device_name, group, cos_type)

	Robot API Call: 

		cos_create_port_group  device_name  group  cos_type

UUID: 2b23f6de-6c28-4e8a-9d66-d10ea7062a2e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create ports group {group}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos port-config {cos_type} {group}

----------------------------------------------


## REST
## SNMP
# API Function: delete_port_group
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_delete_port_group(device_name, group, cos_type)

	Robot API Call: 

		cos_delete_port_group  device_name  group  cos_type

UUID: 59ce8d59-ddf9-4693-a2f2-383238ca76d8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete ports group {group}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos port-config {cos_type} {group} entry

----------------------------------------------


## REST
## SNMP
# API Function: set_port_group_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_port_group_port(device_name, group, port, cos_type)

	Robot API Call: 

		cos_set_port_group_port  device_name  group  port  cos_type

UUID: e2408845-64d2-4a97-88ea-40bfc874b99a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure ports group {group} add {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos port-config {cos_type} {group} append ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_txq_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_txq_settings(device_name, cos_index, txq_index, qos_profile)

	Robot API Call: 

		cos_set_txq_settings  device_name  cos_index  txq_index  qos_profile

UUID: 534ab29f-1519-4d51-8219-919c7a794f1f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure dot1p type {cos_index} qosprofile {qos_profile} ingress-meter ingmeter{txq_index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} txq-reference {txq_index}

----------------------------------------------


## REST
## SNMP
# API Function: set_txq_settings_cos_under_seven
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_txq_settings_cos_under_seven(device_name, cos_index, txq_index, qos_profile)

	Robot API Call: 

		cos_set_txq_settings_cos_under_seven  device_name  cos_index  txq_index  qos_profile

UUID: 26cf69ba-cd93-423c-b0a3-adafc1da5763
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure cos-index {cos_index} qosprofile {qos_profile} ingress-meter ingmeter{txq_index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} txq-reference {txq_index}

----------------------------------------------


## REST
## SNMP
# API Function: set_irl_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_irl_settings(device_name, cos_index, irl_index, priority, qos_profile)

	Robot API Call: 

		cos_set_irl_settings  device_name  cos_index  irl_index  priority  qos_profile

UUID: 3a0dda6f-e090-4863-a844-40dc73f84732
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure cos-index {cos_index} qosprofile {qos_profile} ingress-meter ingmeter{irl_index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} priority {priority} irl-reference {irl_index}

----------------------------------------------


## REST
## SNMP
# API Function: set_irl_settings_cos_under_seven
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_irl_settings_cos_under_seven(device_name, cos_index, irl_index, qos_profile)

	Robot API Call: 

		cos_set_irl_settings_cos_under_seven  device_name  cos_index  irl_index  qos_profile

UUID: ee82d3f5-dfe9-40ab-a217-6e1c6df5dbbd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure dot1p type {cos_index} qosprofile {qos_profile} ingress-meter ingmeter{irl_index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} irl-reference {irl_index}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_resource_irl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_port_resource_irl(device_name )

	Robot API Call: 

		cos_set_port_resource_irl  device_name  

UUID: 40d8cbfa-559d-4d14-bab3-d3e693d98be0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure meter ingmeter{irl_index} committed-rate {rate} {unit} ports {group}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos port-resource irl {group} {irl_index} unit {unit} rate {rate}|| set cos reference irl {group} {irl_index} rate-limit {irl_index}

----------------------------------------------


## REST
## SNMP
# API Function: set_orl_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_orl_settings(device_name )

	Robot API Call: 

		cos_set_orl_settings  device_name  

UUID: d597935e-f0d1-4e50-8a57-bf681bedb113
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure cos-index {cos_index} qosprofile {qos_profile} ingress-meter ingmeter{orl_index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} priority {priority} orl-reference {orl_index}

----------------------------------------------


## REST
## SNMP
# API Function: set_orl_settings_cos_under_seven
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_orl_settings_cos_under_seven(device_name )

	Robot API Call: 

		cos_set_orl_settings_cos_under_seven  device_name  

UUID: 47b5a9d7-ecd3-45c9-b34d-1e13f39ede5f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure dot1p type {cos_index} qosprofile {qos_profile} ingress-meter ingmeter{orl_index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} orl-reference {orl_index}

----------------------------------------------


## REST
## SNMP
# API Function: set_dot1p_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_dot1p_type(device_name )

	Robot API Call: 

		cos_set_dot1p_type  device_name  

UUID: 4fff49d4-25c8-44ac-99b0-25861d7e056c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure dot1p type {cos_index} qosprofile {qos_profile} ingress-meter ingmeter{cos_index}

----------------------------------------------


## REST
## SNMP
# API Function: set_dot1p_type_only
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_dot1p_type_only(device_name )

	Robot API Call: 

		cos_set_dot1p_type_only  device_name  

UUID: c32e7b5e-ef21-4cf1-bce9-8eef31d090aa
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure dot1p type {cos_index} qosprofile {qos_profile}

----------------------------------------------


## REST
## SNMP
# API Function: set_dot1p_port_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_dot1p_port_type(device_name )

	Robot API Call: 

		cos_set_dot1p_port_type  device_name  

UUID: 5eac757b-854e-49e8-8118-78200de11b1c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure ports {port} qosprofile {qos_profile}

----------------------------------------------


## REST
## SNMP
# API Function: set_qos_scheduler
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_qos_scheduler(device_name, mode, group)

	Robot API Call: 

		cos_set_qos_scheduler  device_name  mode  group

UUID: 6f5e0812-c128-4952-a8a0-f86e5ae28f39
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure qosscheduler {mode} ports {group}

----------------------------------------------


## REST
## SNMP
# API Function: set_txq_weights
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_txq_weights(device_name )

	Robot API Call: 

		cos_set_txq_weights  device_name  

UUID: 81961638-5dc2-4530-b986-10032653612e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure qosprofile {txq} weight {weight} ports {group}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos port-config txq {group} arb-percentage {weights}

----------------------------------------------


## REST
## SNMP
# API Function: set_tos_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_tos_settings(device_name )

	Robot API Call: 

		cos_set_tos_settings  device_name  

UUID: 9d20361c-ec50-46f6-bdc0-8c1d9b467fb2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure cos-index {cos_index} replace-tos {tos}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} tos-value {tos}

----------------------------------------------


## REST
## SNMP
# API Function: set_tos_settings_cos_under_seven
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_tos_settings_cos_under_seven(device_name, tos, cos_index, qos_profile)

	Robot API Call: 

		cos_set_tos_settings_cos_under_seven  device_name  tos  cos_index  qos_profile

UUID: 762aa767-837e-48a3-b9e3-677d64accb3e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure diffserv replacement {qos_profile} code-point {tos}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} tos-value {tos}

----------------------------------------------


## REST
## SNMP
# API Function: set_priority_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_priority_settings(device_name )

	Robot API Call: 

		cos_set_priority_settings  device_name  

UUID: 5b6beb6b-8a63-497d-8f32-75cd3b799a3d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure cos-index {cos_index} qosprofile {qos_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: set_priority_settings_cos_under_seven
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_priority_settings_cos_under_seven(device_name )

	Robot API Call: 

		cos_set_priority_settings_cos_under_seven  device_name  

UUID: e5139fe0-4335-413c-b3a1-b379e81b0b01
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure dot1p type {cos_index} qosprofile {qos_profile}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos settings {cos_index} priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: set_diff_serve_replacement
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_diff_serve_replacement(device_name )

	Robot API Call: 

		cos_set_diff_serve_replacement  device_name  

UUID: f335362a-746b-49f6-8944-943f068d9d16
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure diffserv replacement {qos_profile} code-point {tos}

----------------------------------------------


## REST
## SNMP
# API Function: clear_index
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_clear_index(device_name )

	Robot API Call: 

		cos_clear_index  device_name  

UUID: 4f88f1b6-0f76-4b46-a667-7b90779bf59e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure cos-index {cos_index}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos settings {cos_index} all

----------------------------------------------


## REST
## SNMP
# API Function: clear_irl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_clear_irl(device_name )

	Robot API Call: 

		cos_clear_irl  device_name  

UUID: 5e036414-f9be-4117-ac5e-be78c1127afc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure meter ingmeter{irl_index} ports {group}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos irl {group} {irl_index}

----------------------------------------------


## REST
## SNMP
# API Function: set_txq_shaping
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_txq_shaping(device_name, group, rate, unit, qos_profile, txq)

	Robot API Call: 

		cos_set_txq_shaping  device_name  group  rate  unit  qos_profile  txq

UUID: 2edc366b-6292-45e5-8a28-e89348077eae
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure qosprofile {qos_profile} peak_rate {rate} {unit} ports {group}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos port-resource txq {group} {txq} rate {rate} unit {unit}

----------------------------------------------


## REST
## SNMP
# API Function: clear_txq_shaping
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_clear_txq_shaping(device_name )

	Robot API Call: 

		cos_clear_txq_shaping  device_name  

UUID: 72640ec5-c0dc-487b-87ef-f249f84cc05c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure qosprofile ports {group}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos port-resource txq {group} {txq}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_port_priority(device_name )

	Robot API Call: 

		cos_set_port_priority  device_name  

UUID: aedcb0dc-f957-4b87-b815-65721c906e9a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure ports {port} dot1p {pri}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port priority {port} {pri}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_qos_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_port_qos_profile(device_name )

	Robot API Call: 

		cos_set_port_qos_profile  device_name  

UUID: 61d087d3-4505-4a89-bd0b-ecc413d463ce
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} qosprofile {<api_utils.exos_qos_profile>qos_profile}

----------------------------------------------


## REST
## SNMP
# API Function: enable_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_enable_state(device_name )

	Robot API Call: 

		cos_enable_state  device_name  

UUID: a4405432-6e50-48a2-ae3f-7188264bac9b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos state enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_disable_state(device_name )

	Robot API Call: 

		cos_disable_state  device_name  

UUID: 18a6c301-b0ad-4e01-b6bc-9c7c090a3b6d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos state disable

----------------------------------------------


## REST
## SNMP
# API Function: set_txq_reference
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_txq_reference(device_name, group, reference, queue)

	Robot API Call: 

		cos_set_txq_reference  device_name  group  reference  queue

UUID: f72a808d-5200-4422-8364-3bf5d683b12b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos reference txq {group} {reference} queue {queue}

----------------------------------------------


## REST
## SNMP
# API Function: clear_txq_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_clear_txq_settings(device_name )

	Robot API Call: 

		cos_clear_txq_settings  device_name  

UUID: f0586b7e-8d8c-4b21-a818-d9beace3192d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos settings {cos_index} txq-reference

----------------------------------------------


## REST
## SNMP
# API Function: set_irl_reference
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_irl_reference(device_name, group, reference, number)

	Robot API Call: 

		cos_set_irl_reference  device_name  group  reference  number

UUID: 340f5bfb-6f5e-4969-af93-38327ff4b428
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos reference irl {group} {reference} rate-limit {number}

----------------------------------------------


## REST
## SNMP
# API Function: clear_irl_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_clear_irl_settings(device_name )

	Robot API Call: 

		cos_clear_irl_settings  device_name  

UUID: 43b138cd-a7ed-48f4-af24-fe092573d725
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos settings {cos_index} irl-reference

----------------------------------------------


## REST
## SNMP
# API Function: set_orl_reference
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_orl_reference(device_name, group, reference, number)

	Robot API Call: 

		cos_set_orl_reference  device_name  group  reference  number

UUID: 89cc3486-532c-4aaa-a7bb-29f0f59b9d8a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos reference orl {group} {reference} rate-limit {number}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_resource_orl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_set_port_resource_orl(device_name )

	Robot API Call: 

		cos_set_port_resource_orl  device_name  

UUID: c612d698-6767-4b14-b06a-479d69987aa5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set cos port-resource orl {group} {orl_index} unit {unit} rate {rate}|| set cos reference orl {group} {orl_index} rate-limit {orl_index}

----------------------------------------------


## REST
## SNMP
# API Function: clear_orl_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_clear_orl_settings(device_name )

	Robot API Call: 

		cos_clear_orl_settings  device_name  

UUID: 9313c590-f148-4abe-87d0-fe5ffb2202b6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos settings {cos_index} orl-reference

----------------------------------------------


## REST
## SNMP
# API Function: clear_tos_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_clear_tos_settings(device_name )

	Robot API Call: 

		cos_clear_tos_settings  device_name  

UUID: 557f1555-5501-4215-a868-ee04fd7841d9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos settings {cos_index} tos-value

----------------------------------------------


## REST
## SNMP
# API Function: clear_flood_ctrl_settings
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_clear_flood_ctrl_settings(device_name )

	Robot API Call: 

		cos_clear_flood_ctrl_settings  device_name  

UUID: c4ffb22d-4229-44f7-ab5e-1402bced0123
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos settings {cos_index} flood-ctrl

----------------------------------------------


## REST
## SNMP
# API Function: clear_all_config
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.cos.cos_clear_all_config(device_name )

	Robot API Call: 

		cos_clear_all_config  device_name  

UUID: 6eb8182a-3f4e-4297-bdcb-91cf976a3b10
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear cos all-entries

----------------------------------------------


## REST
## SNMP
