# Keyword Library Documentation for Upm
This feature is located in this file: `upm.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: set_auth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_set_auth(device_name )

	Robot API Call: 

		upm_set_auth  device_name  

UUID: c6cbce2b-2f91-4a4a-931a-6042c77eb9fe
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure upm event user-authenticate profile {auth_profile} ports {ports}

----------------------------------------------


## REST
## SNMP
# API Function: set_unauth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_set_unauth(device_name )

	Robot API Call: 

		upm_set_unauth  device_name  

UUID: e7482fb1-174d-420b-a7b5-3a36763cf8e9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure upm event user-unauthenticated profile {auth_profile} ports {ports}

----------------------------------------------


## REST
## SNMP
# API Function: set_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_set_profile(device_name, profile, lines)

	Robot API Call: 

		upm_set_profile  device_name  profile  lines

UUID: bd69c272-33e8-431b-9be4-16d635825744
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create upm profile {profile}||{[<api_utils.exos_upm_profile>lines]}

----------------------------------------------


## REST
## SNMP
# API Function: clear_auth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_clear_auth(device_name )

	Robot API Call: 

		upm_clear_auth  device_name  

UUID: 95f379bd-be9f-4ae1-83ac-c23737a2b94c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure upm event user-authenticate profile {auth_profile} ports {ports}

----------------------------------------------


## REST
## SNMP
# API Function: clear_unauth
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_clear_unauth(device_name, UnConfigures all unauthenticated UPM events on specified profile)

	Robot API Call: 

		upm_clear_unauth  device_name  UnConfigures all unauthenticated UPM events on specified profile

UUID: 939cd1ba-fbc5-40f5-90dd-c6044e80764f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure upm event user-unauthenticated profile {auth_profile} ports {ports}

----------------------------------------------


## REST
## SNMP
# API Function: clear_auth_all_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_clear_auth_all_ports(device_name )

	Robot API Call: 

		upm_clear_auth_all_ports  device_name  

UUID: c3c20c34-ed79-4c78-83cf-5b65455c5ec1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure upm event user-authenticate profile {auth_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_unauth_all_ports
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_clear_unauth_all_ports(device_name )

	Robot API Call: 

		upm_clear_unauth_all_ports  device_name  

UUID: 002a0aa5-e20f-451e-8554-5e49c875255f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure upm event user-unauthenticated profile {auth_profile}

----------------------------------------------


## REST
## SNMP
# API Function: clear_profile
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_clear_profile(device_name )

	Robot API Call: 

		upm_clear_profile  device_name  

UUID: 0d164f68-612b-4ecc-be4e-983749106921
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete upm profile {profile}

----------------------------------------------


## REST
## SNMP
# API Function: show_event_authenticate
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_show_event_authenticate(device_name )

	Robot API Call: 

		upm_show_event_authenticate  device_name  

UUID: 4470ffb8-a43f-46ef-adf3-c92df8012cc6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show upm event user-authenticate

----------------------------------------------


## REST
## SNMP
# API Function: show_event_unauthenticated
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.upm.upm_show_event_unauthenticated(device_name )

	Robot API Call: 

		upm_show_event_unauthenticated  device_name  

UUID: 32c36576-7b50-4278-9f26-588024d10204
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show upm event user-unauthenticated

----------------------------------------------


## REST
## SNMP
