# Command Keyword Library Documentation for Macauth
This feature is located in this file: `macauth.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_enable(device_name )

	Robot API Call: 

		macauth_enable  device_name  

UUID: f2f65c83-6b78-416f-9da0-ce91a8fdd90c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set macauth enable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable netlogin mac

----------------------------------------------


## REST
## SNMP
# API Function: disable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_disable(device_name )

	Robot API Call: 

		macauth_disable  device_name  

UUID: d9ddd942-7c57-4736-b409-553c04fc2b41
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set macauth disable

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable netlogin mac

----------------------------------------------


## REST
## SNMP
# API Function: enable_port_reauthentication
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_enable_port_reauthentication(device_name )

	Robot API Call: 

		macauth_enable_port_reauthentication  device_name  

UUID: 395b1bb6-11c5-4d30-a119-7a0b3eee5a9f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set macauthentication reauthentication enable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin mac ports {port} timers reauthentication on

----------------------------------------------


## REST
## SNMP
# API Function: disable_port_reauthentication
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_disable_port_reauthentication(device_name )

	Robot API Call: 

		macauth_disable_port_reauthentication  device_name  

UUID: d37a9da1-aa27-4025-949f-2b129c472ae1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set macauthentication reauthentication disable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin mac ports {port} timers reauthentication off

----------------------------------------------


## REST
## SNMP
# API Function: set_password
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_set_password(device_name )

	Robot API Call: 

		macauth_set_password  device_name  

UUID: d0055eb3-42e5-4708-a5d5-54f1aa980922
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set macauth password {password}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin add mac-list default password {password}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_set_port_state(device_name )

	Robot API Call: 

		macauth_set_port_state  device_name  

UUID: ab8fafa9-3f90-4174-9b16-3a3e7fd83a6f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set macauth port {<api_utils.state_enable_disable>state} {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		{<api_utils.state_enable_disable>state} netlogin port {port} mac

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		{<api_utils.state_no_empty>state} endpoint-tracking enable

----------------------------------------------


## REST
## SNMP
# API Function: set_port_reauthperiod
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_set_port_reauthperiod(device_name, port, interval)

	Robot API Call: 

		macauth_set_port_reauthperiod  device_name  port  interval

UUID: fd91672c-7db0-488e-9ce6-2e7ae0e5b96d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set macauth reauthperiod {interval} {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin mac ports {port} timers reauth-period {interval}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		endpoint-tracking timeout reauth-period {interval}

----------------------------------------------


## REST
## SNMP
# API Function: set_port_quietperiod
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_set_port_quietperiod(device_name )

	Robot API Call: 

		macauth_set_port_quietperiod  device_name  

UUID: 786b6a37-d736-4d98-bd54-0b57bd046e9e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set macauth quietperiod {sec} {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin mac ports {port} timers delay {sec}

----------------------------------------------


## REST
## SNMP
# API Function: clear_password
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_clear_password(device_name, EXOS will simply have no MAC Auth default password))

	Robot API Call: 

		macauth_clear_password  device_name  EXOS will simply have no MAC Auth default password)

UUID: 135bdb30-0b17-4c8d-a2e7-7984dce2336d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear macauth password 

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin delete mac-list default

----------------------------------------------


## REST
## SNMP
# API Function: clear_port_reauthperiod
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_clear_port_reauthperiod(device_name )

	Robot API Call: 

		macauth_clear_port_reauthperiod  device_name  

UUID: 9dd7a148-6bb3-43f1-b332-673a0737ea8a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear macauth reauthperiod {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin mac ports {port} timers reauth-period 3600

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no endpoint-tracking timeout reauth-period

----------------------------------------------


## REST
## SNMP
# API Function: clear_port_quietperiod
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_clear_port_quietperiod(device_name )

	Robot API Call: 

		macauth_clear_port_quietperiod  device_name  

UUID: 5f084e54-30c8-49e8-ae95-8bc4532991da
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear macauth quietperiod {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin mac ports {port} timers delay 0

----------------------------------------------


## REST
## SNMP
# API Function: set_mac_format_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_set_mac_format_type(device_name )

	Robot API Call: 

		macauth_set_mac_format_type  device_name  

UUID: da655f5c-3d52-4885-a016-8b5c84d5a3b4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin mac username format_type {format_type}

----------------------------------------------


## REST
## SNMP
# API Function: set_mac_user
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_set_mac_user(device_name, mac_addr, password, mask)

	Robot API Call: 

		macauth_set_mac_user  device_name  mac_addr  password  mask

UUID: 723f1833-4212-484a-a564-59ab7230c267
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin add mac-list {<str_utils.normalize_mac>mac_addr} {mask} password {password}

----------------------------------------------


## REST
## SNMP
# API Function: set_mac_user_nopass
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_set_mac_user_nopass(device_name )

	Robot API Call: 

		macauth_set_mac_user_nopass  device_name  

UUID: b4508d75-bc40-4a1a-8d53-8506c8db5abc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin add mac-list {<str_utils.normalize_mac>mac_addr} {mask}

----------------------------------------------


## REST
## SNMP
# API Function: set_reauthperiod
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_set_reauthperiod(device_name )

	Robot API Call: 

		macauth_set_reauthperiod  device_name  

UUID: 75dc4abd-f611-4221-982d-f7f16c7c70d6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin mac timers reauth-period {interval}

----------------------------------------------


## REST
## SNMP
# API Function: clear_mac_user
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_clear_mac_user(device_name )

	Robot API Call: 

		macauth_clear_mac_user  device_name  

UUID: 7cc9a61d-9629-486e-abaf-2c2d4e076b0b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin delete mac-list {<str_utils.normalize_mac>mac_addr} {mask}

----------------------------------------------


## REST
## SNMP
# API Function: macauth_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_enabled(device_name)

	Robot API Call: 

		macauth_verify_enabled  device_name

# API Function: macauth_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_disabled(device_name)

	Robot API Call: 

		macauth_verify_disabled  device_name

# API Function: macauth_verify_enabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_enabled_on_port(device_name, port)

	Robot API Call: 

		macauth_verify_enabled_on_port  device_name  port

# API Function: macauth_verify_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_disabled_on_port(device_name, port)

	Robot API Call: 

		macauth_verify_disabled_on_port  device_name  port

# API Function: macauth_verify_reauth_period
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_reauth_period(device_name, interval)

	Robot API Call: 

		macauth_verify_reauth_period  device_name  interval

# API Function: macauth_verify_port_reauth_period
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_port_reauth_period(device_name, port, interval)

	Robot API Call: 

		macauth_verify_port_reauth_period  device_name  port  interval

# API Function: macauth_verify_port_reauth_period_default
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_port_reauth_period_default(device_name, port, interval)

	Robot API Call: 

		macauth_verify_port_reauth_period_default  device_name  port  interval

# API Function: macauth_verify_reauth_state_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_reauth_state_enabled(device_name, port)

	Robot API Call: 

		macauth_verify_reauth_state_enabled  device_name  port

# API Function: macauth_verify_reauth_state_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_reauth_state_disabled(device_name, port)

	Robot API Call: 

		macauth_verify_reauth_state_disabled  device_name  port

# API Function: macauth_verify_port_reauth_delay
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_port_reauth_delay(device_name, port, interval)

	Robot API Call: 

		macauth_verify_port_reauth_delay  device_name  port  interval

# API Function: macauth_verify_mac_list_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_mac_list_exists(device_name, mac_addrs, mask)

	Robot API Call: 

		macauth_verify_mac_list_exists  device_name  mac_addrs  mask

# API Function: macauth_verify_mac_list_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_mac_list_does_not_exist(device_name, mac_addrs, mask)

	Robot API Call: 

		macauth_verify_mac_list_does_not_exist  device_name  mac_addrs  mask

# API Function: macauth_verify_session_exists_by_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_session_exists_by_port(device_name, port, mac_addr, vlanid, mac_type, state)

	Robot API Call: 

		macauth_verify_session_exists_by_port  device_name  port  mac_addr  vlanid  mac_type  state

# API Function: macauth_verify_session_does_not_exist_by_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.macauth.macauth_verify_session_does_not_exist_by_port(device_name, port, mac_addr, vlanid, mac_type, state)

	Robot API Call: 

		macauth_verify_session_does_not_exist_by_port  device_name  port  mac_addr  vlanid  mac_type  state

