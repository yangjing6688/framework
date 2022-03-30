# Keyword Library Documentation for Dns
This feature is located in this file: `dns.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: create_domain_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_create_domain_name(device_name )

	Robot API Call: 

		dns_create_domain_name  device_name  

UUID: e52ebe68-5a1e-4318-b7eb-01f0165887db
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip domain-name {domain_name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.1.70.0

----------------------------------------------


# API Function: delete_domain_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_delete_domain_name(device_name )

	Robot API Call: 

		dns_delete_domain_name  device_name  

UUID: 24f37769-0d47-4a87-b6de-7ba2735d7daf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip domain-name

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.1.70.0

----------------------------------------------


# API Function: set_primary_server_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_set_primary_server_ip(device_name, ip_addr, ip_type)

	Robot API Call: 

		dns_set_primary_server_ip  device_name  ip_addr  ip_type

UUID: 1a4f6daf-b175-4fd8-826b-87f0ad9d8ef5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip name-server primary {ip_addr}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.1.64.1.6.0||1.3.6.1.4.1.2272.1.1.64.1.7.0||1.3.6.1.4.1.2272.1.1.64.1.8.0

----------------------------------------------


# API Function: set_secondary_server_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_set_secondary_server_ip(device_name, ip_addr, ip_type)

	Robot API Call: 

		dns_set_secondary_server_ip  device_name  ip_addr  ip_type

UUID: e309545c-f045-4ff1-b3b5-df236f6960bf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip name-server secondary {ip_addr}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.1.64.1.6.1||1.3.6.1.4.1.2272.1.1.64.1.7.1||1.3.6.1.4.1.2272.1.1.64.1.8.1

----------------------------------------------


# API Function: set_tertiary_server_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_set_tertiary_server_ip(device_name, ip_addr, ip_type)

	Robot API Call: 

		dns_set_tertiary_server_ip  device_name  ip_addr  ip_type

UUID: a7cfe8b1-4a4e-4c98-a4ee-00ccaaed6d61
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip name-server tertiary {ip_addr}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.1.64.1.6.2||1.3.6.1.4.1.2272.1.1.64.1.7.2||1.3.6.1.4.1.2272.1.1.64.1.8.2

----------------------------------------------


# API Function: clear_primary_server_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_clear_primary_server_ip(device_name )

	Robot API Call: 

		dns_clear_primary_server_ip  device_name  

UUID: ff9d10d1-2200-492f-a0bc-ef9a9aaa1b9d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip name-server primary

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.1.64.1.6.0

----------------------------------------------


# API Function: clear_secondary_server_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_clear_secondary_server_ip(device_name )

	Robot API Call: 

		dns_clear_secondary_server_ip  device_name  

UUID: efd8b04c-9820-463e-a4e1-1b90aa0cedc4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip name-server secondary

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.1.64.1.6.1

----------------------------------------------


# API Function: clear_tertiary_server_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_clear_tertiary_server_ip(device_name )

	Robot API Call: 

		dns_clear_tertiary_server_ip  device_name  

UUID: 44ad3310-2381-4b0f-87a9-0831a6b47c79
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip name-server tertiary

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.1.64.1.6.2

----------------------------------------------


# API Function: dns_verify_domain_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_domain_name(device_name, domain_name)

	Robot API Call: 

		dns_verify_domain_name  device_name  domain_name

# API Function: dns_verify_domain_name_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_domain_name_does_not_exist(device_name, domain_name)

	Robot API Call: 

		dns_verify_domain_name_does_not_exist  device_name  domain_name

# API Function: dns_verify_server_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_server_ip(device_name, ip_addr, pri_sec_or_ter)

	Robot API Call: 

		dns_verify_server_ip  device_name  ip_addr  pri_sec_or_ter

# API Function: dns_verify_server_status_active
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_server_status_active(device_name, pri_sec_or_ter)

	Robot API Call: 

		dns_verify_server_status_active  device_name  pri_sec_or_ter

# API Function: dns_verify_server_status_inactive
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_server_status_inactive(device_name, pri_sec_or_ter)

	Robot API Call: 

		dns_verify_server_status_inactive  device_name  pri_sec_or_ter

# API Function: dns_verify_server_sent_requests
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_server_sent_requests(device_name, ip_addr, count, count_operator, pri_sec_or_ter)

	Robot API Call: 

		dns_verify_server_sent_requests  device_name  ip_addr  count  count_operator  pri_sec_or_ter

# API Function: dns_verify_server_successful_requests
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_server_successful_requests(device_name, ip_addr, count, count_operator, pri_sec_or_ter)

	Robot API Call: 

		dns_verify_server_successful_requests  device_name  ip_addr  count  count_operator  pri_sec_or_ter

# API Function: dns_verify_server_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_server_does_not_exist(device_name, ip_addr, pri_sec_or_ter)

	Robot API Call: 

		dns_verify_server_does_not_exist  device_name  ip_addr  pri_sec_or_ter

# API Function: dns_verify_remote_host_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_remote_host_ip(device_name, host_ip, host_name)

	Robot API Call: 

		dns_verify_remote_host_ip  device_name  host_ip  host_name

# API Function: dns_verify_remote_host_name
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.dns.dns_verify_remote_host_name(device_name, host_ip, host_name)

	Robot API Call: 

		dns_verify_remote_host_name  device_name  host_ip  host_name

