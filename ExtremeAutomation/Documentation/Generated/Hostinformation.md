# Keyword Library Documentation for Hostinformation
This feature is located in this file: `hostinformation.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: set_prompt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_set_prompt(device_name )

	Robot API Call: 

		hostinformation_set_prompt  device_name  

UUID: 8570be79-7439-4139-bd18-5a986b3389bd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		prompt {prompt_name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.5.0

----------------------------------------------


# API Function: set_host_contact
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_set_host_contact(device_name )

	Robot API Call: 

		hostinformation_set_host_contact  device_name  

UUID: 783d173e-6609-4b01-a7c5-2030c6c54b0a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server contact {contact}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.4.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.4.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.4.0

----------------------------------------------


# API Function: set_host_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_set_host_name(device_name )

	Robot API Call: 

		hostinformation_set_host_name  device_name  

UUID: c7f45f88-cc06-4a62-981d-275f6fa8983f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server name {name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.5.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.5.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.5.0

----------------------------------------------


# API Function: set_host_location
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_set_host_location(device_name )

	Robot API Call: 

		hostinformation_set_host_location  device_name  

UUID: 162acbb4-0e6f-43c9-8211-9b83e34bfc6b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		snmp-server location {location}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.6.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.6.0

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.1.6.0

----------------------------------------------


# API Function: clear_prompt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_clear_prompt(device_name )

	Robot API Call: 

		hostinformation_clear_prompt  device_name  

UUID: 2ff11f67-fb26-45a2-bfda-0afbd69fcae9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no prompt

----------------------------------------------


## REST
## SNMP
# API Function: disable_iqagent
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_disable_iqagent(device_name )

	Robot API Call: 

		hostinformation_disable_iqagent  device_name  

UUID: 79c60845-a209-4a66-905c-8214679c2d23
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure terminal || application || no iqagent enable || show application iqagent

----------------------------------------------


## REST
## SNMP
# API Function: enable_iqagent
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_enable_iqagent(device_name )

	Robot API Call: 

		hostinformation_enable_iqagent  device_name  

UUID: 704c185e-7ca8-4601-a04f-f3c5454cb5ad
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure terminal || application || iqagent enable || show application iqagent

----------------------------------------------


## REST
## SNMP
# API Function: hostinformation_verify_system_prompt
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_verify_system_prompt(device_name, prompt_name)

	Robot API Call: 

		hostinformation_verify_system_prompt  device_name  prompt_name

# API Function: hostinformation_verify_host_location
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_verify_host_location(device_name, location)

	Robot API Call: 

		hostinformation_verify_host_location  device_name  location

# API Function: hostinformation_verify_host_contact
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_verify_host_contact(device_name, contact)

	Robot API Call: 

		hostinformation_verify_host_contact  device_name  contact

# API Function: hostinformation_verify_host_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_verify_host_name(device_name, name)

	Robot API Call: 

		hostinformation_verify_host_name  device_name  name

# API Function: hostinformation_verify_host_system_id
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_verify_host_system_id(device_name, system_id)

	Robot API Call: 

		hostinformation_verify_host_system_id  device_name  system_id

# API Function: hostinformation_verify_iqagent_version
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_verify_iqagent_version(device_name, iqagent_version)

	Robot API Call: 

		hostinformation_verify_iqagent_version  device_name  iqagent_version

# API Function: hostinformation_verify_host_nos_version
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostinformation.hostinformation_verify_host_nos_version(device_name, nos_version)

	Robot API Call: 

		hostinformation_verify_host_nos_version  device_name  nos_version

