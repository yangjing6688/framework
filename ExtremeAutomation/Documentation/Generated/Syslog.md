# Keyword Library Documentation for Syslog
This feature is located in this file: `syslog.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: show_info
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.syslog.syslog_show_info(device_name )

	Robot API Call: 

		syslog_show_info  device_name  

UUID: c7bf4eb2-f6c7-4a44-9ce3-481f7dee8a91
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show log configuration

----------------------------------------------


## REST
## SNMP
# API Function: show_target_info
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.syslog.syslog_show_target_info(device_name )

	Robot API Call: 

		syslog_show_target_info  device_name  

UUID: 7624468f-99b7-4115-9a4e-498853e1787e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show log configuration target syslog

----------------------------------------------


## REST
## SNMP
