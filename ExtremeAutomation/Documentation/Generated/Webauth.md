# Command Keyword Library Documentation for Webauth
This feature is located in this file: `webauth.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_enable_global(device_name )

	Robot API Call: 

		webauth_enable_global  device_name  

UUID: 8605577b-fe15-4664-baa7-6e84ac4421c1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable netlogin web-based

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set pwa enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_disable_global(device_name )

	Robot API Call: 

		webauth_disable_global  device_name  

UUID: 58c01afb-4532-4b08-bbe8-f44f0e54bda6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable netlogin web-based

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set pwa disable

----------------------------------------------


## REST
## SNMP
# API Function: enable_control_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_enable_control_port(device_name )

	Robot API Call: 

		webauth_enable_control_port  device_name  

UUID: 475f2a85-c938-46de-b2b1-da36b8114e43
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable netlogin ports {port} web-based

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set pwa portcontrol enable {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_control_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_disable_control_port(device_name )

	Robot API Call: 

		webauth_disable_control_port  device_name  

UUID: 93383c86-d287-4126-b217-16b639fa2b52
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable netlogin ports {port} web-based

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set pwa portcontrol disable {port}

----------------------------------------------


## REST
## SNMP
# API Function: enable_redirect_page
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_enable_redirect_page(device_name )

	Robot API Call: 

		webauth_enable_redirect_page  device_name  

UUID: ee9523ba-ceb5-433c-b27b-932152cb4fdb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable netlogin redirect-page

----------------------------------------------


## REST
## SNMP
# API Function: disable_redirect_page
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_disable_redirect_page(device_name )

	Robot API Call: 

		webauth_disable_redirect_page  device_name  

UUID: f82a024e-faaf-483a-81eb-aa56eebaa87f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable netlogin redirect-page

----------------------------------------------


## REST
## SNMP
# API Function: enable_logout_page
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_enable_logout_page(device_name )

	Robot API Call: 

		webauth_enable_logout_page  device_name  

UUID: 0157c81a-3fdf-4044-86b1-bbfb86d4ab48
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable netlogin logout-privilege

----------------------------------------------


## REST
## SNMP
# API Function: disable_logout_page
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_disable_logout_page(device_name )

	Robot API Call: 

		webauth_disable_logout_page  device_name  

UUID: c5a90167-b800-4730-9599-8eedbb64671d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable netlogin logout-privilege

----------------------------------------------


## REST
## SNMP
# API Function: enable_session_refresh
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_enable_session_refresh(device_name )

	Robot API Call: 

		webauth_enable_session_refresh  device_name  

UUID: eb5e5732-eb51-4387-8349-5b520c99af74
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

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_disable_session_refresh(device_name )

	Robot API Call: 

		webauth_disable_session_refresh  device_name  

UUID: 17fcbd87-7b7b-4027-992b-072260cf8179
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
# API Function: enable_reauthentication_on_refresh
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_enable_reauthentication_on_refresh(device_name )

	Robot API Call: 

		webauth_enable_reauthentication_on_refresh  device_name  

UUID: 4d2f44e4-954c-4e88-be77-9c232aaa442e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable netlogin reauthenticate-on-refresh

----------------------------------------------


## REST
## SNMP
# API Function: disable_reauthentication_on_refresh
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_disable_reauthentication_on_refresh(device_name )

	Robot API Call: 

		webauth_disable_reauthentication_on_refresh  device_name  

UUID: 276c579b-ed6c-43eb-8fbd-c03b4306afd9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable netlogin reauthenticate-on-refresh

----------------------------------------------


## REST
## SNMP
# API Function: set_hostname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_hostname(device_name )

	Robot API Call: 

		webauth_set_hostname  device_name  

UUID: d8f21304-c087-4894-ab2f-8b00b90f21a6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin base-url {url_name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set pwa hostname {url_name}

----------------------------------------------


## REST
## SNMP
# API Function: set_init_mac_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_init_mac_port(device_name )

	Robot API Call: 

		webauth_set_init_mac_port  device_name  

UUID: 19ce2e26-de9c-4974-af06-726750d8daaf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear netlogin state mac-address {mac} port {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_init_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_init_port(device_name )

	Robot API Call: 

		webauth_set_init_port  device_name  

UUID: 9155b2cb-6093-4f7d-b82b-32858ddf63b5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear netlogin state agent web-based port {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set pwa initialize {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_init_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_init_mac(device_name )

	Robot API Call: 

		webauth_set_init_mac  device_name  

UUID: 12cbca5e-67a7-4b96-8834-6fc0790a0fb5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear netlogin state agent web-based mac-address {mac}

----------------------------------------------


## REST
## SNMP
# API Function: set_init_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_init_all(device_name )

	Robot API Call: 

		webauth_set_init_all  device_name  

UUID: 909e163d-aa1c-4e10-b95d-c69fc92fae88
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear netlogin state agent web-based

----------------------------------------------


## REST
## SNMP
# API Function: set_redirect_page
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_redirect_page(device_name )

	Robot API Call: 

		webauth_set_redirect_page  device_name  

UUID: ee1a4441-587d-48da-aa1e-edb66bc1dd88
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin redirect-page {redirect_page}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set pwa ipaddress {redirect_page}

----------------------------------------------


## REST
## SNMP
# API Function: set_session_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_session_timeout(device_name )

	Robot API Call: 

		webauth_set_session_timeout  device_name  

UUID: 3919fec3-b919-40ee-9266-3ffff001771d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin session-timeout web-based {session_timeout}

----------------------------------------------


## REST
## SNMP
# API Function: set_idle_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_idle_timeout(device_name )

	Robot API Call: 

		webauth_set_idle_timeout  device_name  

UUID: 1a0f1eb2-33a4-431f-818f-8ae0b4c748e5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin idle-timeout web-based {idle_timeout}

----------------------------------------------


## REST
## SNMP
# API Function: set_lease_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_lease_time(device_name, vlan_name, lease_time)

	Robot API Call: 

		webauth_set_lease_time  device_name  vlan_name  lease_time

UUID: d8f32a89-1e25-4f90-8cd9-c504da005213
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} netlogin-lease-timer {lease_time}

----------------------------------------------


## REST
## SNMP
# API Function: set_session_refresh
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_session_refresh(device_name )

	Robot API Call: 

		webauth_set_session_refresh  device_name  

UUID: 73c3d442-1863-446e-ad0f-a6bb6639b7d2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin session-refresh {session_refresh}

----------------------------------------------


## REST
## SNMP
# API Function: set_allowed_refresh_failures
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_allowed_refresh_failures(device_name )

	Robot API Call: 

		webauth_set_allowed_refresh_failures  device_name  

UUID: aa8fac1c-6e03-4357-ae88-11d5f22f7d8b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin allowed-refresh-failures {num_failures}

----------------------------------------------


## REST
## SNMP
# API Function: set_protocol_order
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_protocol_order(device_name )

	Robot API Call: 

		webauth_set_protocol_order  device_name  

UUID: 85cc0d41-59fc-4685-aaaa-759bac2dae56
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin authentication protocol-order {order}

----------------------------------------------


## REST
## SNMP
# API Function: set_protocol_order_web_dot1x_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_protocol_order_web_dot1x_mac(device_name )

	Robot API Call: 

		webauth_set_protocol_order_web_dot1x_mac  device_name  

UUID: 5fed7b5a-4fc1-4dab-bcc8-7a65461e6192
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin authentication protocol-order web-based dot1x mac

----------------------------------------------


## REST
## SNMP
# API Function: set_protocol_order_web_mac_dot1x
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_protocol_order_web_mac_dot1x(device_name )

	Robot API Call: 

		webauth_set_protocol_order_web_mac_dot1x  device_name  

UUID: 884b221f-c28a-4e50-acbe-c0b5fdd0f739
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin authentication protocol-order web-based mac dot1x

----------------------------------------------


## REST
## SNMP
# API Function: set_db_order_local
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_db_order_local(device_name )

	Robot API Call: 

		webauth_set_db_order_local  device_name  

UUID: 73697d07-91d5-4fe4-a6d5-4a870269eed7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin web-based authentication database-order local

----------------------------------------------


## REST
## SNMP
# API Function: set_db_order_local_radius
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_db_order_local_radius(device_name )

	Robot API Call: 

		webauth_set_db_order_local_radius  device_name  

UUID: 15afc978-0a35-408e-945c-648561a2db2c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin web-based authentication database-order local radius

----------------------------------------------


## REST
## SNMP
# API Function: set_db_order_radius
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_db_order_radius(device_name )

	Robot API Call: 

		webauth_set_db_order_radius  device_name  

UUID: a766710f-c829-4315-bf44-a3851e3d4e89
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin web-based authentication database-order radius

----------------------------------------------


## REST
## SNMP
# API Function: set_db_order_radius_local
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_set_db_order_radius_local(device_name )

	Robot API Call: 

		webauth_set_db_order_radius_local  device_name  

UUID: beaebe2c-ab03-460b-bb97-8021cec0db01
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin web-based authentication database-order radius local

----------------------------------------------


## REST
## SNMP
# API Function: clear_hostname
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_clear_hostname(device_name )

	Robot API Call: 

		webauth_clear_hostname  device_name  

UUID: dba32dfa-85b2-4888-b3b4-ef9e48548c64
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin base-url network-access.com

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear pwa hostname

----------------------------------------------


## REST
## SNMP
# API Function: clear_redirect_page
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_clear_redirect_page(device_name )

	Robot API Call: 

		webauth_clear_redirect_page  device_name  

UUID: 671068c9-e516-4210-a488-8a63011c75d5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin redirect-page http://www.extremenetworks.com

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear pwa ipaddress

----------------------------------------------


## REST
## SNMP
# API Function: clear_session_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_clear_session_timeout(device_name )

	Robot API Call: 

		webauth_clear_session_timeout  device_name  

UUID: 8b536a06-86f6-4753-b7ed-7ba1f265128d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure netlogin session-timeout web-based

----------------------------------------------


## REST
## SNMP
# API Function: clear_idle_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_clear_idle_timeout(device_name )

	Robot API Call: 

		webauth_clear_idle_timeout  device_name  

UUID: b2827e2d-a25a-4580-8442-d1dd78585451
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure netlogin idle-timeout web-based

----------------------------------------------


## REST
## SNMP
# API Function: clear_lease_time
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_clear_lease_time(device_name )

	Robot API Call: 

		webauth_clear_lease_time  device_name  

UUID: 49537bd8-9618-4d7d-918f-b0bbbafacc40
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure vlan {vlan_name} netlogin-lease-timer 10

----------------------------------------------


## REST
## SNMP
# API Function: clear_session_refresh
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_clear_session_refresh(device_name )

	Robot API Call: 

		webauth_clear_session_refresh  device_name  

UUID: 5317e740-0148-4c5d-882c-154533d14dd6
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
# API Function: clear_allowed_refresh_failures
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_clear_allowed_refresh_failures(device_name )

	Robot API Call: 

		webauth_clear_allowed_refresh_failures  device_name  

UUID: 3d21c5c4-0cc0-4504-8eae-d8f1c75b4809
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure netlogin allowed-refresh-failures

----------------------------------------------


## REST
## SNMP
# API Function: clear_protocol_order
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_clear_protocol_order(device_name, mac)

	Robot API Call: 

		webauth_clear_protocol_order  device_name  mac

UUID: af54254b-7d49-4107-91c9-2b8df0ad5b39
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure netlogin authentication protocol-order dot1x mac web-based

----------------------------------------------


## REST
## SNMP
# API Function: clear_db_order
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.webauth.webauth_clear_db_order(device_name )

	Robot API Call: 

		webauth_clear_db_order  device_name  

UUID: 4aaa8f88-5d2c-47cc-9f8f-df2a90073548
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure netlogin web-based authentication database-order

----------------------------------------------


## REST
## SNMP
