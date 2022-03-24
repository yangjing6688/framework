# Command Keyword Library Documentation for Logging
This feature is located in this file: `logging.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: clear_log
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.logging.logging_clear_log(device_name )

	Robot API Call: 

		logging_clear_log  device_name  

UUID: e98e0e13-4086-463d-8b5c-736ca7d20db5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear log static

----------------------------------------------


## REST
## SNMP
# API Function: clear_log_auditlog
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.logging.logging_clear_log_auditlog(device_name )

	Robot API Call: 

		logging_clear_log_auditlog  device_name  

UUID: a09f2853-a6c2-484b-a3e2-8dc45402c9e1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear logging auditlog

----------------------------------------------


## REST
## SNMP
# API Function: clear_log_raslog
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.logging.logging_clear_log_raslog(device_name )

	Robot API Call: 

		logging_clear_log_raslog  device_name  

UUID: c79f61db-d7e3-4a79-b661-2d989ac2e7a7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear logging raslog

----------------------------------------------


## REST
## SNMP
# API Function: logging_verify_string_in_log
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.logging.logging_verify_string_in_log(device_name, string)

	Robot API Call: 

		logging_verify_string_in_log  device_name  string

# API Function: logging_verify_regex_in_log
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.logging.logging_verify_regex_in_log(device_name, regex)

	Robot API Call: 

		logging_verify_regex_in_log  device_name  regex

