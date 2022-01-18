# Keyword Library Documentation for Cfm
This feature is located in this file: `cfm.yaml` (in this directory: econ-automation-framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /econ-automation-framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/econ-automation-framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py`

# API Function: enable_spbm
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_enable_spbm(device_name )

	Robot API Call: 

		cfm_enable_spbm  device_name  

UUID: 8f60226a-aad9-4e26-82ce-3d38ef7f5114
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm spbm enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.10.8.0

----------------------------------------------


# API Function: disable_spbm
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_disable_spbm(device_name )

	Robot API Call: 

		cfm_disable_spbm  device_name  

UUID: 59e45f05-83fe-4fe1-9ec9-13bf8c8c86b1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no cfm spbm enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.10.8.0

----------------------------------------------


# API Function: enable_maintenance_endpoint
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_enable_maintenance_endpoint(device_name )

	Robot API Call: 

		cfm_enable_maintenance_endpoint  device_name  

UUID: 456725b9-99ed-4f6e-a09b-f8d95f7516fe
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm maintenance-endpoint {md_name} {ma_name} {mep_id} enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.3.1.6.{mep_id}

----------------------------------------------


# API Function: disable_maintenance_endpoint
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_disable_maintenance_endpoint(device_name )

	Robot API Call: 

		cfm_disable_maintenance_endpoint  device_name  

UUID: 470e0bea-8107-4a05-9809-7b9f0cf1dcd4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no cfm maintenance-endpoint {md_name} {ma_name} {mep_id} enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.3.1.6.{mep_id}

----------------------------------------------


# API Function: set_spbm_mepid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_set_spbm_mepid(device_name )

	Robot API Call: 

		cfm_set_spbm_mepid  device_name  

UUID: c0b7c2f3-d0eb-4cba-9343-572403bd1418
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm spbm mepid {mep_id}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.10.10.0

----------------------------------------------


# API Function: set_spbm_level
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_set_spbm_level(device_name )

	Robot API Call: 

		cfm_set_spbm_level  device_name  

UUID: 77e98ce5-147f-4ef3-a17e-344d6d5f109d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm spbm level {spbm_level}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.10.9.0

----------------------------------------------


# API Function: set_maintenance_domain
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_set_maintenance_domain(device_name, md_name, md_index, md_level)

	Robot API Call: 

		cfm_set_maintenance_domain  device_name  md_name  md_index  md_level

UUID: 4c5bcd94-1569-4c2c-a7e8-f3e81994c441
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm maintenance-domain {md_name} index {md_index} maintenance-level {md_level}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.1.1.2.{md_index}||1.3.6.1.4.1.2272.1.69.1.1.3.{md_index}||1.3.6.1.4.1.2272.1.69.1.1.6.{md_index}

----------------------------------------------


# API Function: set_maintenance_domain_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_set_maintenance_domain_name(device_name, md_name, md_index)

	Robot API Call: 

		cfm_set_maintenance_domain_name  device_name  md_name  md_index

UUID: a3c647d2-6ab7-495f-b746-9168baec8557
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm maintenance-domain {md_name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.1.1.2.{md_index}||1.3.6.1.4.1.2272.1.69.1.1.3.{md_index}

----------------------------------------------


# API Function: set_maintenance_domain_index
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_set_maintenance_domain_index(device_name, md_name, md_index)

	Robot API Call: 

		cfm_set_maintenance_domain_index  device_name  md_name  md_index

UUID: 897ddb76-a82b-4bf9-b272-c3760286dd68
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm maintenance-domain {md_name} index {md_index}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.1.1.2.{md_index}||1.3.6.1.4.1.2272.1.69.1.1.3.{md_index}

----------------------------------------------


# API Function: set_maintenance_domain_level
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_set_maintenance_domain_level(device_name, md_name, md_level, md_index)

	Robot API Call: 

		cfm_set_maintenance_domain_level  device_name  md_name  md_level  md_index

UUID: d17b5590-19b5-401e-81e9-cb83a5759828
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm maintenance-domain {md_name} level {md_level}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.1.1.2.{md_index}||1.3.6.1.4.1.2272.1.69.1.1.3.{md_index}||1.3.6.1.4.1.2272.1.69.1.1.6.{md_index}

----------------------------------------------


# API Function: set_maintenance_association
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_set_maintenance_association(device_name )

	Robot API Call: 

		cfm_set_maintenance_association  device_name  

UUID: 7642f15a-cbe6-48cd-9c0b-efbb8e419580
## CLI
## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.2.1.4.{md_index}||1.3.6.1.4.1.2272.1.69.2.1.5.{md_index}||1.3.6.1.4.1.2272.1.69.2.1.6.{md_index}

----------------------------------------------


# API Function: set_maintenance_endpoint
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_set_maintenance_endpoint(device_name )

	Robot API Call: 

		cfm_set_maintenance_endpoint  device_name  

UUID: 260e8c48-0108-4f46-8890-fff920b95fd5
## CLI
## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.3.1.7.0

----------------------------------------------


# API Function: clear_spbm_mepid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_clear_spbm_mepid(device_name )

	Robot API Call: 

		cfm_clear_spbm_mepid  device_name  

UUID: 8b63fbe9-b7ac-475f-b6fd-eb3a97d17be8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm spbm mepid 1

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.10.10.0

----------------------------------------------


# API Function: clear_spbm_level
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_clear_spbm_level(device_name )

	Robot API Call: 

		cfm_clear_spbm_level  device_name  

UUID: 3025081e-cc13-4f6c-9c66-525d310a9447
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		cfm spbm level 4

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.10.9.0

----------------------------------------------


# API Function: clear_maintenance_domain
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_clear_maintenance_domain(device_name, md_name, md_index)

	Robot API Call: 

		cfm_clear_maintenance_domain  device_name  md_name  md_index

UUID: 1c620dbd-f86b-4928-9d60-967d1f2e3660
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no cfm maintenance-domain {md_name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.1.1.3.{md_index}

----------------------------------------------


# API Function: clear_maintenance_association
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_clear_maintenance_association(device_name )

	Robot API Call: 

		cfm_clear_maintenance_association  device_name  

UUID: 5a5dd2c6-4794-482a-8707-53fc61557799
## CLI
## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.2.1.6.0

----------------------------------------------


# API Function: clear_maintenance_endpoint
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_clear_maintenance_endpoint(device_name )

	Robot API Call: 

		cfm_clear_maintenance_endpoint  device_name  

UUID: e28efc19-5192-4972-89dd-eb92bc17e614
## CLI
## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.3.1.7.0

----------------------------------------------


# API Function: show_cmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_show_cmac(device_name )

	Robot API Call: 

		cfm_show_cmac  device_name  

UUID: 5173ced0-99dc-495f-acdf-20472e39d547
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show cfm cmac

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: get

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.10.15.0

----------------------------------------------


# API Function: show_spbm
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_show_spbm(device_name )

	Robot API Call: 

		cfm_show_spbm  device_name  

UUID: c8cfba3f-68dc-48b0-9cf0-36abedb1c93a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show cfm spbm

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.10

----------------------------------------------


# API Function: show_maintenance_endpoint
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_show_maintenance_endpoint(device_name )

	Robot API Call: 

		cfm_show_maintenance_endpoint  device_name  

UUID: 3bc56ed5-76fc-4683-b72c-2c5862a502e2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show cfm maintenance-endpoint

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.3

----------------------------------------------


# API Function: show_maintenance_association
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_show_maintenance_association(device_name )

	Robot API Call: 

		cfm_show_maintenance_association  device_name  

UUID: 6037e58d-02b2-4e93-ae76-32e28d89845a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show cfm maintenance-association

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.2

----------------------------------------------


# API Function: show_maintenance_domain
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_show_maintenance_domain(device_name )

	Robot API Call: 

		cfm_show_maintenance_domain  device_name  

UUID: 2927d7eb-8576-4c8b-9af5-015a2a39fc2f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show cfm maintenance-domain

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.1

----------------------------------------------


# API Function: show_association_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_show_association_name(device_name )

	Robot API Call: 

		cfm_show_association_name  device_name  

UUID: 672c0a91-5e52-4a98-a48c-0465860acf50
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show cfm maintenance-association

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.2.1.4

----------------------------------------------


# API Function: show_domain_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.NetworkElementCfmGenKeywords.cfm_show_domain_name(device_name )

	Robot API Call: 

		cfm_show_domain_name  device_name  

UUID: 24ec9c2f-94b7-4cea-80ec-6c04250cf980
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		show cfm maintenance-domain

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: walk

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.69.1.1.2

----------------------------------------------


