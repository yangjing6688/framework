# Command Keyword Library Documentation for Snmp
This feature is located in this file: `snmp.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: create_all_trap_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_all_trap_server(device_name, ip_address, server_name, param_name, tag_list)

	Robot API Call: 

		snmp_create_all_trap_server  device_name  ip_address  server_name  param_name  tag_list

UUID: 937890fb-dc59-4f13-a87c-c4e718fc9990
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmp add trapreceiver {ip_address} community {community}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set snmp targetaddr {server_name} {ip_address} param {param_name} taglist {tag_list}

----------------------------------------------


## REST
## SNMP
# API Function: delete_trap_servers
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_trap_servers(device_name )

	Robot API Call: 

		snmp_delete_trap_servers  device_name  

UUID: 380d633f-5653-4917-bafb-2bed364f74eb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmp delete trapreceiver {ip_address}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear snmp targetaddr {server_name}

----------------------------------------------


## REST
## SNMP
# API Function: create_readonly_community
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_readonly_community(device_name, community_index, community_name, security_name, context)

	Robot API Call: 

		snmp_create_readonly_community  device_name  community_index  community_name  security_name  context

UUID: 3a7cc49b-7100-4584-9f62-ad1646c91afe
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 add community {community_index} name {community_name} user {security_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server community {community_name} index {community_index} secname {security_name} context {context}

----------------------------------------------


## REST
## SNMP
# API Function: create_readwrite_community
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_readwrite_community(device_name, community_index, community_name, security_name, context)

	Robot API Call: 

		snmp_create_readwrite_community  device_name  community_index  community_name  security_name  context

UUID: 967de9e7-3ced-40a1-ad0d-c89ab4b5177d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 add community {community_index} name {community_name} user {security_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server community {community_name} index {community_index} secname {security_name} context {context}

----------------------------------------------


## REST
## SNMP
# API Function: delete_community
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_community(device_name )

	Robot API Call: 

		snmp_delete_community  device_name  

UUID: c8579c62-a6a4-4e03-9bea-89fd8b50c5b3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 del community {community_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server community {community_name}

----------------------------------------------


## REST
## SNMP
# API Function: delete_user
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_user(device_name )

	Robot API Call: 

		snmp_delete_user  device_name  

UUID: 282ee4e9-601d-4c42-b69a-1965fe2a66e7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 delete user {user_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server user {user_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_user_no_authentication
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_set_user_no_authentication(device_name, user_name, group)

	Robot API Call: 

		snmp_set_user_no_authentication  device_name  user_name  group

UUID: 86b262b8-fc15-4c68-be86-1ca3ef0bc457
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 add user {user_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server user {user_name} group {group}

----------------------------------------------


## REST
## SNMP
# API Function: set_user_authentication
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_set_user_authentication(device_name, user_name, auth_proto, auth_password, group)

	Robot API Call: 

		snmp_set_user_authentication  device_name  user_name  auth_proto  auth_password  group

UUID: 83cad0e6-f50c-4897-a587-7fdb393dc513
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 add user {user_name} authentication {auth_proto} {auth_password}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server user {user_name}  group {group} {auth_proto} {auth_password}

----------------------------------------------


## REST
## SNMP
# API Function: set_user_privacy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_set_user_privacy(device_name, user_name, auth_proto, auth_password, priv_proto, priv_password, group)

	Robot API Call: 

		snmp_set_user_privacy  device_name  user_name  auth_proto  auth_password  priv_proto  priv_password  group

UUID: 2715b88c-a9de-41c0-8605-2900d2be9f33
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 add user {user_name} authentication {auth_proto} {auth_password} privacy {priv_proto} {priv_password}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server user {user_name} group {group} {auth_proto} {auth_password} {priv_proto} {priv_password}

----------------------------------------------


## REST
## SNMP
# API Function: set_user_no_authentication_engine_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_set_user_no_authentication_engine_id(device_name, engine_id, user_name, group)

	Robot API Call: 

		snmp_set_user_no_authentication_engine_id  device_name  engine_id  user_name  group

UUID: 5351d630-450c-4fa4-9a26-8c685b6ac119
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 add user {user_name} engine-id {engine_id}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server user engine-id {engine_id} {user_name} group {group}

----------------------------------------------


## REST
## SNMP
# API Function: set_user_authentication_engine_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_set_user_authentication_engine_id(device_name, auth_password, auth_proto, engine_id, user_name, group)

	Robot API Call: 

		snmp_set_user_authentication_engine_id  device_name  auth_password  auth_proto  engine_id  user_name  group

UUID: f75c5703-adac-4c4e-9885-5d73a91fbae9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 add user {user_name} authentication {auth_proto} {auth_password} engine-id {engine_id}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server user engine-id {engine_id} {user_name} group {group} {auth_proto} {auth_password}

----------------------------------------------


## REST
## SNMP
# API Function: set_user_privacy_engine_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_set_user_privacy_engine_id(device_name, auth_password, auth_proto, engine_id, priv_password, priv_proto, user_name, group)

	Robot API Call: 

		snmp_set_user_privacy_engine_id  device_name  auth_password  auth_proto  engine_id  priv_password  priv_proto  user_name  group

UUID: 9d182ff5-016a-42e3-a16a-e1fbbd96c461
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure snmpv3 add user {user_name} authentication {auth_proto} {auth_password} privacy {priv_proto} {priv_password} engine-id {engine_id}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server user engine-id {engine_id} {user_name} group {group} {auth_proto} {auth_password} {priv_proto} {priv_password}

----------------------------------------------


## REST
## SNMP
# API Function: enable_access_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_enable_access_global(device_name )

	Robot API Call: 

		snmp_enable_access_global  device_name  

UUID: acd52df8-7550-404d-8cd9-e757fabab7c2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable snmp access

----------------------------------------------


## REST
## SNMP
# API Function: disable_access_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_disable_access_global(device_name )

	Robot API Call: 

		snmp_disable_access_global  device_name  

UUID: 4ae2e419-faec-4a79-8d5b-c5475ea946a8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable snmp access

----------------------------------------------


## REST
## SNMP
# API Function: set_trap_param
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_set_trap_param(device_name, param_name, community, version)

	Robot API Call: 

		snmp_set_trap_param  device_name  param_name  community  version

UUID: 9911ac50-36b0-46eb-95c3-9e128d042a82
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set snmp targetparams {param_name} user {community} security {version} message {version}

----------------------------------------------


## REST
## SNMP
# API Function: clear_trap_param
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_clear_trap_param(device_name )

	Robot API Call: 

		snmp_clear_trap_param  device_name  

UUID: 502a9f4e-4cee-42a8-9689-5da899ad1bb8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear snmp targetparams {param_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_notify
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_set_notify(device_name )

	Robot API Call: 

		snmp_set_notify  device_name  

UUID: fa526bb7-d1fc-4196-8a0c-80dcf7cd84f7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set snmp notify {notify_name} tag {notify_name} {type}

----------------------------------------------


## REST
## SNMP
# API Function: clear_notify
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_clear_notify(device_name )

	Robot API Call: 

		snmp_clear_notify  device_name  

UUID: d945dbb4-92ab-4f69-b810-97fbdd8d9a2b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear snmp notify {notify_name}

----------------------------------------------


## REST
## SNMP
# API Function: enable_authentication_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_enable_authentication_trap(device_name )

	Robot API Call: 

		snmp_enable_authentication_trap  device_name  

UUID: 82570981-b4ba-4d40-8fe9-3868f9a706c7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server authentication-trap enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_authentication_trap
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_disable_authentication_trap(device_name )

	Robot API Call: 

		snmp_disable_authentication_trap  device_name  

UUID: 1af11b3a-7b17-4173-80ee-8b0075ee8a6f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server authentication-trap

----------------------------------------------


## REST
## SNMP
# API Function: enable_same_snmp_and_ip_sender_flag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_enable_same_snmp_and_ip_sender_flag(device_name )

	Robot API Call: 

		snmp_enable_same_snmp_and_ip_sender_flag  device_name  

UUID: 5a069297-79af-4ce3-b42a-057f33874574
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server force-iphdr-sender enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_same_snmp_and_ip_sender_flag
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_disable_same_snmp_and_ip_sender_flag(device_name )

	Robot API Call: 

		snmp_disable_same_snmp_and_ip_sender_flag  device_name  

UUID: b22d72e2-458b-4f59-a4ad-484bb7d29ad0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server force-iphdr-sender

----------------------------------------------


## REST
## SNMP
# API Function: enable_same_snmp_trap_sender_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_enable_same_snmp_trap_sender_ip(device_name )

	Robot API Call: 

		snmp_enable_same_snmp_trap_sender_ip  device_name  

UUID: 103819d3-297a-4504-b03e-ae75b124b56b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server force-trap-sender enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_same_snmp_trap_sender_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_disable_same_snmp_trap_sender_ip(device_name )

	Robot API Call: 

		snmp_disable_same_snmp_trap_sender_ip  device_name  

UUID: 82f99f99-a12a-4765-b0c4-ef5a14932855
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server force-trap-sender

----------------------------------------------


## REST
## SNMP
# API Function: create_v1_trap_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_v1_trap_server(device_name, ip_addr, security_name, port)

	Robot API Call: 

		snmp_create_v1_trap_server  device_name  ip_addr  security_name  port

UUID: 65155113-aca6-401f-9523-d24e265742af
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server host {ip_addr} port {port} v1 {security_name}

----------------------------------------------


## REST
## SNMP
# API Function: delete_v1_trap_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_v1_trap_server(device_name, ip_addr, security_name, port)

	Robot API Call: 

		snmp_delete_v1_trap_server  device_name  ip_addr  security_name  port

UUID: a2fc0df6-ba11-4600-aaa7-2b310e3137fd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server host {ip_addr} port {port} v1 {security_name}

----------------------------------------------


## REST
## SNMP
# API Function: create_v2c_trap_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_v2c_trap_server(device_name, ip_addr, security_name, port)

	Robot API Call: 

		snmp_create_v2c_trap_server  device_name  ip_addr  security_name  port

UUID: ab9bc27d-48a7-49e8-8060-a2d05523c403
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server host {ip_addr} port {port} v2c {security_name}

----------------------------------------------


## REST
## SNMP
# API Function: delete_v2c_trap_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_v2c_trap_server(device_name, ip_addr, security_name, port)

	Robot API Call: 

		snmp_delete_v2c_trap_server  device_name  ip_addr  security_name  port

UUID: 32c795f8-1d58-49fc-8546-175dea332fde
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server host {ip_addr} port {port} v2c {security_name}

----------------------------------------------


## REST
## SNMP
# API Function: create_v2c_inform_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_v2c_inform_server(device_name, ip_addr, security_name, port, timeout, retries, mms)

	Robot API Call: 

		snmp_create_v2c_inform_server  device_name  ip_addr  security_name  port  timeout  retries  mms

UUID: 262425cb-ecba-4def-ab78-92bef8d53265
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server host {ip_addr} port {port} v2c {security_name} inform timeout {timeout} retries {retries} mms {mms}

----------------------------------------------


## REST
## SNMP
# API Function: delete_v2c_inform_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_v2c_inform_server(device_name, ip_addr, security_name)

	Robot API Call: 

		snmp_delete_v2c_inform_server  device_name  ip_addr  security_name

UUID: 7b190c70-f885-4be0-afa8-7d02a752781e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server host {ip_addr} v2c {security_name}

----------------------------------------------


## REST
## SNMP
# API Function: create_v3_trap_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_v3_trap_server(device_name, ip_addr, security_name, security_level, port)

	Robot API Call: 

		snmp_create_v3_trap_server  device_name  ip_addr  security_name  security_level  port

UUID: 5c45efe6-41f2-4aca-bbc5-c2c58a4aa086
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server host {ip_addr} port {port} v3 {security_level} {security_name}

----------------------------------------------


## REST
## SNMP
# API Function: delete_v3_trap_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_v3_trap_server(device_name, ip_addr, security_name, port)

	Robot API Call: 

		snmp_delete_v3_trap_server  device_name  ip_addr  security_name  port

UUID: 27309891-ea40-41ce-8f00-63492aa8db80
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server host {ip_addr} port {port} v3 {security_name}

----------------------------------------------


## REST
## SNMP
# API Function: create_v3_inform_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_v3_inform_server(device_name, ip_addr, security_name, security_level, port, timeout, retries)

	Robot API Call: 

		snmp_create_v3_inform_server  device_name  ip_addr  security_name  security_level  port  timeout  retries

UUID: 60d292ee-8aa6-420e-8f61-9e5d94cf3c4b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server host {ip_addr} port {port} v3 {security_level} {security_name} inform timeout {timeout} retries {retries}

----------------------------------------------


## REST
## SNMP
# API Function: delete_v3_inform_server
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_v3_inform_server(device_name )

	Robot API Call: 

		snmp_delete_v3_inform_server  device_name  

UUID: 8410645f-c725-4937-8f93-ed97ec5c6d72
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server host {ip_addr} v3 {security_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_notify_filter
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_set_notify_filter(device_name, profile_name, oid_tree)

	Robot API Call: 

		snmp_set_notify_filter  device_name  profile_name  oid_tree

UUID: dc2296ba-a156-49a2-9584-59b971ca9756
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server notify-filter {profile_name} {oid_tree}

----------------------------------------------


## REST
## SNMP
# API Function: clear_notify_filter
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_clear_notify_filter(device_name, profile_name, oid_tree)

	Robot API Call: 

		snmp_clear_notify_filter  device_name  profile_name  oid_tree

UUID: 50c0c14a-8374-4114-859c-c7ffb10cb66c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server notify-filter {profile_name} {oid_tree}

----------------------------------------------


## REST
## SNMP
# API Function: delete_user_engine_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_user_engine_id(device_name )

	Robot API Call: 

		snmp_delete_user_engine_id  device_name  

UUID: e3dd38d3-79c0-4829-9a51-da0a58af052b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server user engine-id {engine_id} {user_name}

----------------------------------------------


## REST
## SNMP
# API Function: create_group_and_access
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_group_and_access(device_name, group, security_level, read_view, write_view, notify_view, context)

	Robot API Call: 

		snmp_create_group_and_access  device_name  group  security_level  read_view  write_view  notify_view  context

UUID: 8d68eddb-86bc-4b21-85a7-40ce75c3815d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server group {group} {context} {security_level} read-view {read_view} write-view {write_view} notify-view {notify_view}

----------------------------------------------


## REST
## SNMP
# API Function: delete_group_and_access
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_group_and_access(device_name, group, context)

	Robot API Call: 

		snmp_delete_group_and_access  device_name  group  context

UUID: 453baa15-3319-46ad-8851-3b75ea6dab78
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server group {group} {context}

----------------------------------------------


## REST
## SNMP
# API Function: create_view
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_create_view(device_name, view_name, oid_tree)

	Robot API Call: 

		snmp_create_view  device_name  view_name  oid_tree

UUID: e714befc-dc0d-4293-8ab7-108d34aee8ef
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server view {view_name} {oid_tree}

----------------------------------------------


## REST
## SNMP
# API Function: delete_view
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_delete_view(device_name, view_name, oid_tree)

	Robot API Call: 

		snmp_delete_view  device_name  view_name  oid_tree

UUID: 47f6342b-af6f-4346-b3cf-83e093410bbf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no snmp-server view {view_name} {oid_tree}

----------------------------------------------


## REST
## SNMP
# API Function: snmp_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_enabled(device_name, vr)

	Robot API Call: 

		snmp_verify_enabled  device_name  vr

# API Function: snmp_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_disabled(device_name, vr)

	Robot API Call: 

		snmp_verify_disabled  device_name  vr

# API Function: snmp_verify_notify_filter
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_notify_filter(device_name, profile_name, oid_tree)

	Robot API Call: 

		snmp_verify_notify_filter  device_name  profile_name  oid_tree

# API Function: snmp_verify_authentication_trap_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_authentication_trap_enabled(device_name)

	Robot API Call: 

		snmp_verify_authentication_trap_enabled  device_name

# API Function: snmp_verify_authentication_trap_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_authentication_trap_disabled(device_name)

	Robot API Call: 

		snmp_verify_authentication_trap_disabled  device_name

# API Function: snmp_verify_same_ip_as_ip_sender_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_same_ip_as_ip_sender_enabled(device_name)

	Robot API Call: 

		snmp_verify_same_ip_as_ip_sender_enabled  device_name

# API Function: snmp_verify_same_ip_as_ip_sender_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_same_ip_as_ip_sender_disabled(device_name)

	Robot API Call: 

		snmp_verify_same_ip_as_ip_sender_disabled  device_name

# API Function: snmp_verify_same_trap_ip_as_ip_sender_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_same_trap_ip_as_ip_sender_enabled(device_name)

	Robot API Call: 

		snmp_verify_same_trap_ip_as_ip_sender_enabled  device_name

# API Function: snmp_verify_same_trap_ip_as_ip_sender_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_same_trap_ip_as_ip_sender_disabled(device_name)

	Robot API Call: 

		snmp_verify_same_trap_ip_as_ip_sender_disabled  device_name

# API Function: snmp_verify_v1_trap_server_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v1_trap_server_exists(device_name, ip_addr, security_name, port)

	Robot API Call: 

		snmp_verify_v1_trap_server_exists  device_name  ip_addr  security_name  port

# API Function: snmp_verify_v1_trap_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v1_trap_server_does_not_exist(device_name, ip_addr, security_name, port)

	Robot API Call: 

		snmp_verify_v1_trap_server_does_not_exist  device_name  ip_addr  security_name  port

# API Function: snmp_verify_v2c_trap_server_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v2c_trap_server_exists(device_name, ip_addr, security_name, port)

	Robot API Call: 

		snmp_verify_v2c_trap_server_exists  device_name  ip_addr  security_name  port

# API Function: snmp_verify_v2c_trap_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v2c_trap_server_does_not_exist(device_name, ip_addr, security_name, port)

	Robot API Call: 

		snmp_verify_v2c_trap_server_does_not_exist  device_name  ip_addr  security_name  port

# API Function: snmp_verify_v2c_inform_server_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v2c_inform_server_exists(device_name, ip_addr, security_name, timeout, port)

	Robot API Call: 

		snmp_verify_v2c_inform_server_exists  device_name  ip_addr  security_name  timeout  port

# API Function: snmp_verify_v2c_inform_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v2c_inform_server_does_not_exist(device_name, ip_addr, security_name, timeout, port)

	Robot API Call: 

		snmp_verify_v2c_inform_server_does_not_exist  device_name  ip_addr  security_name  timeout  port

# API Function: snmp_verify_v3_trap_server_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v3_trap_server_exists(device_name, ip_addr, security_name, security_level, port)

	Robot API Call: 

		snmp_verify_v3_trap_server_exists  device_name  ip_addr  security_name  security_level  port

# API Function: snmp_verify_v3_trap_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v3_trap_server_does_not_exist(device_name, ip_addr, security_name, security_level, port)

	Robot API Call: 

		snmp_verify_v3_trap_server_does_not_exist  device_name  ip_addr  security_name  security_level  port

# API Function: snmp_verify_v3_inform_server_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v3_inform_server_exists(device_name, ip_addr, security_name, security_level, timeout, port)

	Robot API Call: 

		snmp_verify_v3_inform_server_exists  device_name  ip_addr  security_name  security_level  timeout  port

# API Function: snmp_verify_v3_inform_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_v3_inform_server_does_not_exist(device_name, ip_addr, security_name, security_level, timeout, port)

	Robot API Call: 

		snmp_verify_v3_inform_server_does_not_exist  device_name  ip_addr  security_name  security_level  timeout  port

# API Function: snmp_verify_community_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_community_exists(device_name, community_index, community_name, security_name)

	Robot API Call: 

		snmp_verify_community_exists  device_name  community_index  community_name  security_name

# API Function: snmp_verify_community_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_community_does_not_exist(device_name, community_index, community_name, security_name)

	Robot API Call: 

		snmp_verify_community_does_not_exist  device_name  community_index  community_name  security_name

# API Function: snmp_verify_user_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_user_exists(device_name, user_name)

	Robot API Call: 

		snmp_verify_user_exists  device_name  user_name

# API Function: snmp_verify_user_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_user_does_not_exist(device_name, user_name)

	Robot API Call: 

		snmp_verify_user_does_not_exist  device_name  user_name

# API Function: snmp_verify_group_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_group_exists(device_name, group)

	Robot API Call: 

		snmp_verify_group_exists  device_name  group

# API Function: snmp_verify_group_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_group_does_not_exist(device_name, group)

	Robot API Call: 

		snmp_verify_group_does_not_exist  device_name  group

# API Function: snmp_verify_access_for_group_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_access_for_group_exists(device_name, group, security_level)

	Robot API Call: 

		snmp_verify_access_for_group_exists  device_name  group  security_level

# API Function: snmp_verify_access_for_group_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_access_for_group_does_not_exist(device_name, group, security_level)

	Robot API Call: 

		snmp_verify_access_for_group_does_not_exist  device_name  group  security_level

# API Function: snmp_verify_view_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_view_exists(device_name, view_name, oid_tree)

	Robot API Call: 

		snmp_verify_view_exists  device_name  view_name  oid_tree

# API Function: snmp_verify_view_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.snmp.snmp_verify_view_does_not_exist(device_name, view_name, oid_tree)

	Robot API Call: 

		snmp_verify_view_does_not_exist  device_name  view_name  oid_tree

