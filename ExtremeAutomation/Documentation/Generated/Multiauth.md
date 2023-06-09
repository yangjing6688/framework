# Keyword Library Documentation for Multiauth
This feature is located in this file: `multiauth.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: enable_session_refresh
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_enable_session_refresh(device_name )

	Robot API Call: 

		multiauth_enable_session_refresh  device_name  

UUID: f3eb09e3-5666-4313-ac3d-fbb864ea2476
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable netlogin session-refresh

----------------------------------------------


## REST
## SNMP
# API Function: disable_session_refresh
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_disable_session_refresh(device_name )

	Robot API Call: 

		multiauth_disable_session_refresh  device_name  

UUID: bf5c7ddd-7ddb-4969-b73c-21f3a626cd4e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable netlogin session-refresh

----------------------------------------------


## REST
## SNMP
# API Function: set_session_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_session_timeout(device_name )

	Robot API Call: 

		multiauth_set_session_timeout  device_name  

UUID: ad2d1a2b-1c05-46ca-9fb5-fe6ce27806b8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin session-timeout {timeout}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set multiauth session-timeout {timeout}

----------------------------------------------


## REST
## SNMP
# API Function: set_session_type_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_session_type_timeout(device_name )

	Robot API Call: 

		multiauth_set_session_type_timeout  device_name  

UUID: 3acfba85-52e1-4d2c-9959-88fdd081a2e6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin session-timeout {<api_utils.exos_ma_mode>mode} {timeout}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set multiauth session-timeout {<api_utils.eos_ma_mode>mode} {timeout}

----------------------------------------------


## REST
## SNMP
# API Function: clear_session_type_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_clear_session_type_timeout(device_name )

	Robot API Call: 

		multiauth_clear_session_type_timeout  device_name  

UUID: 25b27d24-41ba-408f-b670-d6a0a55918e5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure netlogin session-timeout {<api_utils.exos_ma_mode>mode}

----------------------------------------------


## REST
## SNMP
# API Function: set_session_refresh
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_session_refresh(device_name )

	Robot API Call: 

		multiauth_set_session_refresh  device_name  

UUID: f26cfaa0-c900-4839-9d43-3f6f9a10709d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin session-refresh {seconds}

----------------------------------------------


## REST
## SNMP
# API Function: clear_session_refresh
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_clear_session_refresh(device_name )

	Robot API Call: 

		multiauth_clear_session_refresh  device_name  

UUID: a16c13f3-5825-484b-9a84-9b823ea8fe1a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure netlogin session-refresh

----------------------------------------------


## REST
## SNMP
# API Function: set_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_vlan(device_name )

	Robot API Call: 

		multiauth_set_vlan  device_name  

UUID: 2b3308c0-27b9-48e0-9550-91d9af08dff1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin vlan {multiauth_vlan_name}

----------------------------------------------


## REST
## SNMP
# API Function: clear_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_clear_vlan(device_name )

	Robot API Call: 

		multiauth_clear_vlan  device_name  

UUID: 954d2698-9c1a-478e-888b-b4aea467b4a3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure netlogin vlan

----------------------------------------------


## REST
## SNMP
# API Function: set_idle_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_idle_timeout(device_name )

	Robot API Call: 

		multiauth_set_idle_timeout  device_name  

UUID: 796e0685-e341-454b-9f48-4e69b3008fe7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin idle-timeout {timeout}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set multiauth idle-timeout {timeout}

----------------------------------------------


## REST
## SNMP
# API Function: set_idle_type_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_idle_type_timeout(device_name )

	Robot API Call: 

		multiauth_set_idle_type_timeout  device_name  

UUID: 6af1773b-18c7-4bfa-ac39-fda93afa3608
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin idle-timeout {<api_utils.exos_ma_mode>mode} {timeout}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set multiauth idle-timeout {<api_utils.eos_ma_mode>mode} {timeout}

----------------------------------------------


## REST
## SNMP
# API Function: clear_idle_type_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_clear_idle_type_timeout(device_name )

	Robot API Call: 

		multiauth_clear_idle_type_timeout  device_name  

UUID: 05becf3a-3ebb-4fec-a4be-cc1a44177e9d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure netlogin idle-timeout {<api_utils.exos_ma_mode>mode}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_mode
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_port_mode(device_name )

	Robot API Call: 

		multiauth_set_port_mode  device_name  

UUID: 0cdfcb1c-ff0d-454e-904e-843d68779832
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin port {port} authentication mode {<api_utils.exos_ma_mode>mode}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set multiauth port mode {<api_utils.eos_ma_mode>mode} {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_numusers
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_port_numusers(device_name, port, num_users)

	Robot API Call: 

		multiauth_set_port_numusers  device_name  port  num_users

UUID: affaa376-34fb-4b1e-a6b9-83a4a41a77b1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin ports {port} allowed-users {num_users}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set multiauth port numusers {num_users} {port}

----------------------------------------------


## REST
## SNMP
# API Function: clear_station_mac_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_clear_station_mac_port(device_name )

	Robot API Call: 

		multiauth_clear_station_mac_port  device_name  

UUID: 395038b8-7e83-43ae-9ef4-789be298fad1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear netlogin state mac-address {mac} port {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear multiauth station mac {mac} port {port}

----------------------------------------------


## REST
## SNMP
# API Function: clear_station_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_clear_station_port(device_name )

	Robot API Call: 

		multiauth_clear_station_port  device_name  

UUID: 4c0206d2-7df7-4c17-bf25-b630cb366e01
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear netlogin state port {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear multiauth station port {port}

----------------------------------------------


## REST
## SNMP
# API Function: clear_station_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_clear_station_mac(device_name )

	Robot API Call: 

		multiauth_clear_station_mac  device_name  

UUID: 146f1262-e1c3-4df0-85b5-a2c31b423fde
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear netlogin state mac-address {mac}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear multiauth station mac {mac} port *.*.*

----------------------------------------------


## REST
## SNMP
# API Function: clear_station_agent
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_clear_station_agent(device_name )

	Robot API Call: 

		multiauth_clear_station_agent  device_name  

UUID: a98b62da-73b5-4a30-a12d-547a9a970f71
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear netlogin state agent {<api_utils.exos_ma_agent>agent}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear multiauth session {mac} *.*.* {<api_utils.eos_ma_agent>agent}

----------------------------------------------


## REST
## SNMP
# API Function: set_mode
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_mode(device_name )

	Robot API Call: 

		multiauth_set_mode  device_name  

UUID: e059d40a-d336-440e-8fa0-37bbc37f7de8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set multiauth mode {mode}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_force_auth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_set_port_force_auth(device_name )

	Robot API Call: 

		multiauth_set_port_force_auth  device_name  

UUID: 62f29872-ded8-4e28-9eef-50da69f83dea
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set multiauth port mode force-auth {port}

----------------------------------------------


## REST
## SNMP
# API Function: multiauth_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_enabled(device_name)

	Robot API Call: 

		multiauth_verify_enabled  device_name

# API Function: multiauth_verify_session_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_exists(device_name, station_address, port, auth_status, last_attempt, agent_type, session_applied, server_type, vlan_tun_attr, policy_index, policy_name, session_timeout, session_duration, idle_timeout, idle_time, termination_time, auth_server_ip, session_duration_operator, idle_time_operator)

	Robot API Call: 

		multiauth_verify_session_exists  device_name  station_address  port  auth_status  last_attempt  agent_type  session_applied  server_type  vlan_tun_attr  policy_index  policy_name  session_timeout  session_duration  idle_timeout  idle_time  termination_time  auth_server_ip  session_duration_operator  idle_time_operator

# API Function: multiauth_verify_session_exists_by_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_exists_by_port(device_name, station_address, port, auth_status, last_attempt, agent_type, session_applied, server_type, vlan_tun_attr, policy_index, policy_name, session_timeout, session_duration, idle_timeout, idle_time, termination_time, auth_server_ip, session_duration_operator, idle_time_operator)

	Robot API Call: 

		multiauth_verify_session_exists_by_port  device_name  station_address  port  auth_status  last_attempt  agent_type  session_applied  server_type  vlan_tun_attr  policy_index  policy_name  session_timeout  session_duration  idle_timeout  idle_time  termination_time  auth_server_ip  session_duration_operator  idle_time_operator

# API Function: multiauth_verify_session_exists_by_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_exists_by_mac(device_name, station_address, port, auth_status, last_attempt, agent_type, session_applied, server_type, vlan_tun_attr, policy_index, policy_name, session_timeout, session_duration, idle_timeout, idle_time, termination_time, auth_server_ip, session_duration_operator, idle_time_operator, last_attempt_operator)

	Robot API Call: 

		multiauth_verify_session_exists_by_mac  device_name  station_address  port  auth_status  last_attempt  agent_type  session_applied  server_type  vlan_tun_attr  policy_index  policy_name  session_timeout  session_duration  idle_timeout  idle_time  termination_time  auth_server_ip  session_duration_operator  idle_time_operator  last_attempt_operator

# API Function: multiauth_verify_session_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_does_not_exist(device_name, station_address, port, auth_status, last_attempt, agent_type, session_applied, server_type, vlan_tun_attr, policy_index, policy_name, session_timeout, session_duration, idle_timeout, idle_time, termination_time, auth_server_ip, session_duration_operator, idle_time_operator, last_attempt_operator)

	Robot API Call: 

		multiauth_verify_session_does_not_exist  device_name  station_address  port  auth_status  last_attempt  agent_type  session_applied  server_type  vlan_tun_attr  policy_index  policy_name  session_timeout  session_duration  idle_timeout  idle_time  termination_time  auth_server_ip  session_duration_operator  idle_time_operator  last_attempt_operator

# API Function: multiauth_verify_session_expired
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_expired(device_name, station_address, port, auth_status, last_attempt, agent_type, session_applied, server_type, vlan_tun_attr, policy_index, policy_name, session_timeout, session_duration, idle_timeout, idle_time, termination_time, auth_server_ip, session_duration_operator, idle_time_operator, last_attempt_operator)

	Robot API Call: 

		multiauth_verify_session_expired  device_name  station_address  port  auth_status  last_attempt  agent_type  session_applied  server_type  vlan_tun_attr  policy_index  policy_name  session_timeout  session_duration  idle_timeout  idle_time  termination_time  auth_server_ip  session_duration_operator  idle_time_operator  last_attempt_operator

# API Function: multiauth_verify_vlan_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_vlan_exist(device_names, vlan)

	Robot API Call: 

		multiauth_verify_vlan_exist  device_names  vlan

# API Function: multiauth_verify_vlan_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_vlan_does_not_exist(device_names, vlan)

	Robot API Call: 

		multiauth_verify_vlan_does_not_exist  device_names  vlan

# API Function: multiauth_verify_session_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_timeout(device_name, timeout)

	Robot API Call: 

		multiauth_verify_session_timeout  device_name  timeout

# API Function: multiauth_verify_mac_session_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_mac_session_timeout(device_name, timeout)

	Robot API Call: 

		multiauth_verify_mac_session_timeout  device_name  timeout

# API Function: multiauth_verify_dot1x_session_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_dot1x_session_timeout(device_name, timeout)

	Robot API Call: 

		multiauth_verify_dot1x_session_timeout  device_name  timeout

# API Function: multiauth_verify_web_session_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_web_session_timeout(device_name, timeout)

	Robot API Call: 

		multiauth_verify_web_session_timeout  device_name  timeout

# API Function: multiauth_verify_idle_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_idle_timeout(device_name, timeout)

	Robot API Call: 

		multiauth_verify_idle_timeout  device_name  timeout

# API Function: multiauth_verify_mac_idle_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_mac_idle_timeout(device_name, timeout)

	Robot API Call: 

		multiauth_verify_mac_idle_timeout  device_name  timeout

# API Function: multiauth_verify_dot1x_idle_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_dot1x_idle_timeout(device_name, timeout)

	Robot API Call: 

		multiauth_verify_dot1x_idle_timeout  device_name  timeout

# API Function: multiauth_verify_web_idle_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_web_idle_timeout(device_name, timeout)

	Robot API Call: 

		multiauth_verify_web_idle_timeout  device_name  timeout

# API Function: multiauth_verify_session_refresh_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_refresh_enabled(device_name)

	Robot API Call: 

		multiauth_verify_session_refresh_enabled  device_name

# API Function: multiauth_verify_session_refresh_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_refresh_interval(device_name, interval)

	Robot API Call: 

		multiauth_verify_session_refresh_interval  device_name  interval

# API Function: multiauth_verify_session_idle_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_idle_time(device_name, timer)

	Robot API Call: 

		multiauth_verify_session_idle_time  device_name  timer

# API Function: multiauth_verify_session_idle_time_greater_than
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_idle_time_greater_than(device_name, timer)

	Robot API Call: 

		multiauth_verify_session_idle_time_greater_than  device_name  timer

# API Function: multiauth_verify_session_idle_time_less_than
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_idle_time_less_than(device_name, timer)

	Robot API Call: 

		multiauth_verify_session_idle_time_less_than  device_name  timer

# API Function: multiauth_verify_session_duration_greater_than
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_duration_greater_than(device_name, timer)

	Robot API Call: 

		multiauth_verify_session_duration_greater_than  device_name  timer

# API Function: multiauth_verify_session_duration_less_than
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.multiauth.multiauth_verify_session_duration_less_than(device_name, timer)

	Robot API Call: 

		multiauth_verify_session_duration_less_than  device_name  timer

