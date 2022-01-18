# Keyword Library Documentation for Wlanservices
This feature is located in this file: `wlanservices.yaml` (in this directory: econ-automation-framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /econ-automation-framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/econ-automation-framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: show_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementWlanservicesGenKeywords.wlanservices_show_all(device_name )

	Robot API Call: 

		wlanservices_show_all  device_name  

UUID: 3b504f20-a9fe-4d6e-b8fc-1d6480f59dea
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show wlans

----------------------------------------------


## REST
## SNMP
# API Function: show_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementWlanservicesGenKeywords.wlanservices_show_detail(device_name )

	Robot API Call: 

		wlanservices_show_detail  device_name  

UUID: 99808fc2-1b5d-4693-ada6-523765211ee2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show wlans "{wlan_service_name}"

----------------------------------------------


## REST
## SNMP
