# Keyword Library Documentation for Site
This feature is located in this file: `site.yaml` (in this directory: econ-automation-framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /econ-automation-framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/econ-automation-framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: show_all
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSiteGenKeywords.site_show_all(device_name )

	Robot API Call: 

		site_show_all  device_name  

UUID: 66054fea-36d6-49b3-a59a-c64727a94ad6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show site

----------------------------------------------


## REST
## SNMP
# API Function: show_detail
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementSiteGenKeywords.site_show_detail(device_name )

	Robot API Call: 

		site_show_detail  device_name  

UUID: cb810be3-6e9d-48c1-878e-915722ddbf33
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXTRWIRELESS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show site "{site_name}"

----------------------------------------------


## REST
## SNMP
