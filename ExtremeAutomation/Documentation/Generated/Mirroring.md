# Command Keyword Library Documentation for Mirroring
This feature is located in this file: `mirroring.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: create_both
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_create_both(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_create_both  device_name  name  src_port  dst_port

UUID: 35ff8622-050d-45d8-bdcd-cb2d0f1d0b00
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port mirroring create {src_port} {dst_port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create mirror {name} to port {dst_port}||configure mirror {name} add port {src_port} ingress-and-egress

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mirror-by-port {name} in-port {src_port} out-port {dst_port} mode both

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		monitor session {name}|| source ethernet {src_port} destination ethernet {dst_port} direction both

----------------------------------------------


## REST
## SNMP
# API Function: create_ingress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_create_ingress(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_create_ingress  device_name  name  src_port  dst_port

UUID: 9c4fca35-e2b6-4795-9575-3dd9ff15beef
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port mirroring create {src_port} {dst_port} rx

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create mirror {name} to port {dst_port}||configure mirror {name} add port {src_port} ingress

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mirror-by-port {name} in-port {src_port} out-port {dst_port} mode rx

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		monitor session {name}|| source ethernet {src_port} destination ethernet {dst_port} direction rx

----------------------------------------------


## REST
## SNMP
# API Function: create_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_create_egress(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_create_egress  device_name  name  src_port  dst_port

UUID: e599fd8a-8124-4614-9442-34b1ed04b425
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port mirroring create {src_port} {dst_port} tx

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create mirror {name} to port {dst_port}||configure mirror {name} add port {src_port} egress

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mirror-by-port {name} in-port {src_port} out-port {dst_port} mode tx

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		monitor session {name}|| source ethernet {src_port} destination ethernet {dst_port} direction tx

----------------------------------------------


## REST
## SNMP
# API Function: delete_port_mirror
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_delete_port_mirror(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_delete_port_mirror  device_name  name  src_port  dst_port

UUID: 8318eb28-5773-4485-a296-4e58fd750979
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear port mirroring {src_port} {dst_port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		delete mirror {name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no mirror-by-port {name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no monitor session {name}

----------------------------------------------


## REST
## SNMP
# API Function: enable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_enable_port(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_enable_port  device_name  name  src_port  dst_port

UUID: 11727cab-c503-416e-bb6c-bbdc34b8df48
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port mirroring enable {src_port} {dst_port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable mirror {name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		mirror-by-port {name} enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_disable_port(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_disable_port  device_name  name  src_port  dst_port

UUID: 76c15bfb-dbac-4f97-88e2-303b7e1400e7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port mirroring disable {src_port} {dst_port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable mirror {name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no mirror-by-port {name} enable

----------------------------------------------


## REST
## SNMP
# API Function: create_remote_both
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_create_remote_both(device_name )

	Robot API Call: 

		mirroring_create_remote_both  device_name  

UUID: 86f6074b-6927-4104-86bb-8c0f6a32ae7b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create mirror {name} to remote-ip {ip}

----------------------------------------------


## REST
## SNMP
# API Function: create_portlist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_create_portlist(device_name )

	Robot API Call: 

		mirroring_create_portlist  device_name  

UUID: 67f7a017-2424-4570-9fb4-2072b7a3cae3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		create mirror {name} to port-list {port_list}

----------------------------------------------


## REST
## SNMP
# API Function: set_source_port_both
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_set_source_port_both(device_name )

	Robot API Call: 

		mirroring_set_source_port_both  device_name  

UUID: 36706790-6717-4eba-bff7-ab50276d95fb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mirror {name} add port {src_port} ingress-and-egress

----------------------------------------------


## REST
## SNMP
# API Function: set_source_port_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_set_source_port_vlan(device_name )

	Robot API Call: 

		mirroring_set_source_port_vlan  device_name  

UUID: 4c7b5043-1eb9-46dc-aefe-f3546e24a662
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mirror {name} add port {src_port} vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: set_source_port_ingress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_set_source_port_ingress(device_name )

	Robot API Call: 

		mirroring_set_source_port_ingress  device_name  

UUID: 056f8301-40d8-4252-b9a9-843000e960f4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mirror {name} add port {src_port} ingress

----------------------------------------------


## REST
## SNMP
# API Function: set_source_port_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_set_source_port_egress(device_name )

	Robot API Call: 

		mirroring_set_source_port_egress  device_name  

UUID: 77e707e2-1dc1-4a94-afd7-dc289bdaafa1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mirror {name} add port {src_port} egress

----------------------------------------------


## REST
## SNMP
# API Function: set_description
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_set_description(device_name )

	Robot API Call: 

		mirroring_set_description  device_name  

UUID: a85983a3-446c-4086-86c1-56881347b937
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		monitor session {name}||description {description}

----------------------------------------------


## REST
## SNMP
# API Function: clear_source_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_clear_source_port(device_name )

	Robot API Call: 

		mirroring_clear_source_port  device_name  

UUID: 8dd4f447-ca67-4415-857f-35d5bb131055
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mirror {name} delete port {src_port}

----------------------------------------------


## REST
## SNMP
# API Function: enable_remote_ping_check
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_enable_remote_ping_check(device_name, name, src_ip, dst_ip)

	Robot API Call: 

		mirroring_enable_remote_ping_check  device_name  name  src_ip  dst_ip

UUID: f2319f16-18ea-4819-bddc-60d9501568b6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mirror {name} ping-check on from {src_ip} to remote-ip {dst_ip}

----------------------------------------------


## REST
## SNMP
# API Function: disable_remote_ping_check
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_disable_remote_ping_check(device_name, name, src_ip, dst_ip)

	Robot API Call: 

		mirroring_disable_remote_ping_check  device_name  name  src_ip  dst_ip

UUID: 04077770-3b9f-4abf-88e0-2b7a2124a5dd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure mirror {name} ping-check off from {src_ip} to remote-ip {dst_ip}

----------------------------------------------


## REST
## SNMP
# API Function: mirroring_verify_port_mirror_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_port_mirror_exists(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_port_mirror_exists  device_name  name  src_port  dst_port

# API Function: mirroring_verify_port_mirror_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_port_mirror_does_not_exist(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_port_mirror_does_not_exist  device_name  name  src_port  dst_port

# API Function: mirroring_verify_ingress_mirror_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_ingress_mirror_exists(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_ingress_mirror_exists  device_name  name  src_port  dst_port

# API Function: mirroring_verify_ingress_mirror_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_ingress_mirror_does_not_exist(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_ingress_mirror_does_not_exist  device_name  name  src_port  dst_port

# API Function: mirroring_verify_egress_mirror_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_egress_mirror_exists(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_egress_mirror_exists  device_name  name  src_port  dst_port

# API Function: mirroring_verify_egress_mirror_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_egress_mirror_does_not_exist(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_egress_mirror_does_not_exist  device_name  name  src_port  dst_port

# API Function: mirroring_verify_ingress_egress_mirror_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_ingress_egress_mirror_exists(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_ingress_egress_mirror_exists  device_name  name  src_port  dst_port

# API Function: mirroring_verify_ingress_egress_mirror_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_ingress_egress_mirror_does_not_exist(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_ingress_egress_mirror_does_not_exist  device_name  name  src_port  dst_port

# API Function: mirroring_verify_port_mirror_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_port_mirror_enabled(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_port_mirror_enabled  device_name  name  src_port  dst_port

# API Function: mirroring_verify_port_mirror_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.mirroring.mirroring_verify_port_mirror_disabled(device_name, name, src_port, dst_port)

	Robot API Call: 

		mirroring_verify_port_mirror_disabled  device_name  name  src_port  dst_port

