# Keyword Library Documentation for Port
This feature is located in this file: `port.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: enable_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_enable_state(device_name )

	Robot API Call: 

		port_enable_state  device_name  

UUID: 97f025f1-a7f6-44b9-a118-33ddff5ef15a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port enable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable ports {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no shutdown

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: Ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no shutdown

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SNAPROUTE

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /public/v1/config/Port

----------------------------------------------


## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.2.2.1.7.{port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.2.2.1.7.{port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.2.2.1.7.{port}

----------------------------------------------


# API Function: disable_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_disable_state(device_name )

	Robot API Call: 

		port_disable_state  device_name  

UUID: 62c8985e-e0eb-46fc-aaa1-409eaab3d702
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port disable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable ports {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		shutdown

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: Ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		shutdown

----------------------------------------------


## REST
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SNAPROUTE

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: REST

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: patch

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: /public/v1/config/Port

----------------------------------------------


## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.2.2.1.7.{port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.2.2.1.7.{port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.2.2.1.7.{port}

----------------------------------------------


# API Function: enable_jumbo
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_enable_jumbo(device_name )

	Robot API Call: 

		port_enable_jumbo  device_name  

UUID: b7eee19b-7245-4369-8778-1a8f4f3f0b29
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port jumbo enable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable jumbo-frame ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: disable_jumbo
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_disable_jumbo(device_name )

	Robot API Call: 

		port_disable_jumbo  device_name  

UUID: b2215268-4e83-4d0a-ba2d-75e40438e3fd
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port jumbo disable {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable jumbo-frame ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: set_speed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_speed(device_name, port, speed, duplex, state)

	Robot API Call: 

		port_set_speed  device_name  port  speed  duplex  state

UUID: 538ae084-d666-4980-ac02-2b6a17f3167c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		set port speed {port} {speed}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} auto {state} speed {speed} duplex {duplex}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: Ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		speed {speed}

----------------------------------------------


## REST
## SNMP
# API Function: clear_speed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_clear_speed(device_name )

	Robot API Call: 

		port_clear_speed  device_name  

UUID: 9b736e06-72a2-4bdc-bddf-1222c16ac04e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear port speed {port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} auto on

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: Ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no speed

----------------------------------------------


## REST
## SNMP
# API Function: set_rate_egress_mbps
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_rate_egress_mbps(device_name )

	Robot API Call: 

		port_set_rate_egress_mbps  device_name  

UUID: ee8358af-ab27-416c-83ae-038b6b9d2b60
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} rate-limit egress {rate} Mbps

----------------------------------------------


## REST
## SNMP
# API Function: set_rate_egress_gbps
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_rate_egress_gbps(device_name )

	Robot API Call: 

		port_set_rate_egress_gbps  device_name  

UUID: aece5b75-5a3f-4dd0-9898-ec02174656ff
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} rate-limit egress {rate} Gbps

----------------------------------------------


## REST
## SNMP
# API Function: set_rate_egress_kbps
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_rate_egress_kbps(device_name )

	Robot API Call: 

		port_set_rate_egress_kbps  device_name  

UUID: 54127682-0ec3-4a86-8ff2-7e6c9082d60a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} rate-limit egress {rate} Kbps

----------------------------------------------


## REST
## SNMP
# API Function: set_rate_egress_no_limit
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_rate_egress_no_limit(device_name )

	Robot API Call: 

		port_set_rate_egress_no_limit  device_name  

UUID: 093f13b2-e8a0-46dd-94e2-3abcfa11c450
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} rate-limit egress no-limit

----------------------------------------------


## REST
## SNMP
# API Function: set_rate_flood_bcast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_rate_flood_bcast(device_name )

	Robot API Call: 

		port_set_rate_flood_bcast  device_name  

UUID: c64ae3dc-01d2-4808-88b8-c17ba3838a9f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} rate-limit flood broadcast {rate}

----------------------------------------------


## REST
## SNMP
# API Function: set_rate_flood_mcast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_rate_flood_mcast(device_name )

	Robot API Call: 

		port_set_rate_flood_mcast  device_name  

UUID: be2c7b98-9550-45e2-9178-34259c288e1c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} rate-limit flood multicast {rate}

----------------------------------------------


## REST
## SNMP
# API Function: set_rate_flood_unknown
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_rate_flood_unknown(device_name )

	Robot API Call: 

		port_set_rate_flood_unknown  device_name  

UUID: 42289171-2ebc-4c10-b618-045961049356
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure port {port} rate-limit flood unknown-destmac {rate}

----------------------------------------------


## REST
## SNMP
# API Function: set_restart
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_restart(device_name )

	Robot API Call: 

		port_set_restart  device_name  

UUID: ab98d9fa-b817-4b98-8f10-e6c0abd11cb1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		restart ports {port}

----------------------------------------------


## REST
## SNMP
# API Function: enable_flex_uni
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_enable_flex_uni(device_name )

	Robot API Call: 

		port_enable_flex_uni  device_name  

UUID: 2b1c6baf-48a0-41b9-94a8-037e4dfd8d81
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		flex-uni enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.4.10.1.1.116.{port}

----------------------------------------------


# API Function: disable_flex_uni
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_disable_flex_uni(device_name )

	Robot API Call: 

		port_disable_flex_uni  device_name  

UUID: b5a2fb20-a78c-4321-a3d3-e9d362a54665
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no flex-uni enable

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.2272.1.4.10.1.1.116.{port}

----------------------------------------------


# API Function: set_alias
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_set_alias(device_name, port, name)

	Robot API Call: 

		port_set_alias  device_name  port  name

UUID: 26939b7a-06a4-4759-99fa-76dc9caf1515
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		name {name}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: SLX

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: Ethernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		description {name}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.31.1.1.1.18.{port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.31.1.1.1.18.{port}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.31.1.1.1.18.{port}

----------------------------------------------


# API Function: port_verify_jumbo_frame_reception_enabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_jumbo_frame_reception_enabled_on_port(device_name, ports)

	Robot API Call: 

		port_verify_jumbo_frame_reception_enabled_on_port  device_name  ports

# API Function: port_verify_jumbo_frame_reception_disabled_on_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_jumbo_frame_reception_disabled_on_port(device_name, ports)

	Robot API Call: 

		port_verify_jumbo_frame_reception_disabled_on_port  device_name  ports

# API Function: port_verify_admin_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_admin_enabled(device_name, port)

	Robot API Call: 

		port_verify_admin_enabled  device_name  port

# API Function: port_verify_admin_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_admin_disabled(device_name, port)

	Robot API Call: 

		port_verify_admin_disabled  device_name  port

# API Function: port_verify_operational
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_operational(device_name, port)

	Robot API Call: 

		port_verify_operational  device_name  port

# API Function: port_verify_not_operational
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_not_operational(device_name, port)

	Robot API Call: 

		port_verify_not_operational  device_name  port

# API Function: port_verify_flex_uni_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_flex_uni_enabled(device_name, port)

	Robot API Call: 

		port_verify_flex_uni_enabled  device_name  port

# API Function: port_verify_flex_uni_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_flex_uni_disabled(device_name, port)

	Robot API Call: 

		port_verify_flex_uni_disabled  device_name  port

# API Function: port_verify_alias
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_alias(device_name, port, alias)

	Robot API Call: 

		port_verify_alias  device_name  port  alias

# API Function: port_verify_not_alias
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_not_alias(device_name, port, alias)

	Robot API Call: 

		port_verify_not_alias  device_name  port  alias

# API Function: port_verify_mtu
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_mtu(device_name, port, mtu)

	Robot API Call: 

		port_verify_mtu  device_name  port  mtu

# API Function: port_verify_mac_address
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_mac_address(device_name, port, mac)

	Robot API Call: 

		port_verify_mac_address  device_name  port  mac

# API Function: port_verify_high_speed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_high_speed(device_name, port, speed)

	Robot API Call: 

		port_verify_high_speed  device_name  port  speed

# API Function: port_verify_in_octets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_in_octets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_in_octets  device_name  port  count  count_operator

# API Function: port_verify_in_unicast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_in_unicast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_in_unicast_packets  device_name  port  count  count_operator

# API Function: port_verify_in_discard_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_in_discard_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_in_discard_packets  device_name  port  count  count_operator

# API Function: port_verify_in_error_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_in_error_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_in_error_packets  device_name  port  count  count_operator

# API Function: port_verify_in_unknown_protocol_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_in_unknown_protocol_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_in_unknown_protocol_packets  device_name  port  count  count_operator

# API Function: port_verify_out_octets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_out_octets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_out_octets  device_name  port  count  count_operator

# API Function: port_verify_out_unicast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_out_unicast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_out_unicast_packets  device_name  port  count  count_operator

# API Function: port_verify_out_discard_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_out_discard_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_out_discard_packets  device_name  port  count  count_operator

# API Function: port_verify_out_error_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_out_error_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_out_error_packets  device_name  port  count  count_operator

# API Function: port_verify_in_multicast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_in_multicast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_in_multicast_packets  device_name  port  count  count_operator

# API Function: port_verify_in_broadcast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_in_broadcast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_in_broadcast_packets  device_name  port  count  count_operator

# API Function: port_verify_out_multicast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_out_multicast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_out_multicast_packets  device_name  port  count  count_operator

# API Function: port_verify_out_broadcast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_out_broadcast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_out_broadcast_packets  device_name  port  count  count_operator

# API Function: port_verify_64_bit_in_octets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_64_bit_in_octets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_64_bit_in_octets  device_name  port  count  count_operator

# API Function: port_verify_64_bit_in_unicast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_64_bit_in_unicast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_64_bit_in_unicast_packets  device_name  port  count  count_operator

# API Function: port_verify_64_bit_in_multicast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_64_bit_in_multicast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_64_bit_in_multicast_packets  device_name  port  count  count_operator

# API Function: port_verify_64_bit_in_broadcast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_64_bit_in_broadcast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_64_bit_in_broadcast_packets  device_name  port  count  count_operator

# API Function: port_verify_64_bit_out_octets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_64_bit_out_octets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_64_bit_out_octets  device_name  port  count  count_operator

# API Function: port_verify_64_bit_out_unicast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_64_bit_out_unicast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_64_bit_out_unicast_packets  device_name  port  count  count_operator

# API Function: port_verify_64_bit_out_multicast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_64_bit_out_multicast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_64_bit_out_multicast_packets  device_name  port  count  count_operator

# API Function: port_verify_64_bit_out_broadcast_packets
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_64_bit_out_broadcast_packets(device_name, port, count, count_operator)

	Robot API Call: 

		port_verify_64_bit_out_broadcast_packets  device_name  port  count  count_operator

# API Function: port_verify_rate_egress
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_rate_egress(device_name, port, rate)

	Robot API Call: 

		port_verify_rate_egress  device_name  port  rate

# API Function: port_verify_rate_broadcast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_rate_broadcast(device_name, port, rate)

	Robot API Call: 

		port_verify_rate_broadcast  device_name  port  rate

# API Function: port_verify_rate_broadcast_none
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_rate_broadcast_none(device_name, port)

	Robot API Call: 

		port_verify_rate_broadcast_none  device_name  port

# API Function: port_verify_rate_multicast
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_rate_multicast(device_name, port, rate)

	Robot API Call: 

		port_verify_rate_multicast  device_name  port  rate

# API Function: port_verify_rate_multicast_none
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_rate_multicast_none(device_name, port)

	Robot API Call: 

		port_verify_rate_multicast_none  device_name  port

# API Function: port_verify_rate_unknown_destmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_rate_unknown_destmac(device_name, port, rate)

	Robot API Call: 

		port_verify_rate_unknown_destmac  device_name  port  rate

# API Function: port_verify_rate_unknown_destmac_none
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_rate_unknown_destmac_none(device_name, port)

	Robot API Call: 

		port_verify_rate_unknown_destmac_none  device_name  port

# API Function: port_verify_advertised_speed_and_duplex
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_advertised_speed_and_duplex(device_name, port, speed, duplex, flags)

	Robot API Call: 

		port_verify_advertised_speed_and_duplex  device_name  port  speed  duplex  flags

# API Function: port_verify_attributes
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.port.port_verify_attributes(admin_state, oper_state, jumbo_state, alias_state, mtu, high_speed, in_octets, in_ucast, in_discard, in_error, out_octets, out_ucast, out_discard, out_error, in_mcast, in_bcast, out_mcast, out_bcast, in_64_octets, in_64_ucast, in_64_mcast, in_64_bcast, out_64_octets, out_64_ucast, out_64_mcast, out_64_bcast, "admin_state", "admin_state", "oper_state", "oper_state", "jumbo_state", "jumbo_state", "alias", "alias", "flex_uni_state", "flex_uni_state", "mtu", "mac_addr", "high_speed", "in_octets", "in_ucast", "in_discard", "in_error", "out_octets", "out_ucast", "out_discard", "out_error", "in_mcast", "in_bcast", "out_mcast", "out_bcast", "in_64_octets", "in_64_ucast", "in_64_mcast", "in_64_bcast", "out_64_octets", "out_64_ucast", "out_64_mcast", "out_64_bcast")

	Robot API Call: 

		port_verify_attributes  admin_state  oper_state  jumbo_state  alias_state  mtu  high_speed  in_octets  in_ucast  in_discard  in_error  out_octets  out_ucast  out_discard  out_error  in_mcast  in_bcast  out_mcast  out_bcast  in_64_octets  in_64_ucast  in_64_mcast  in_64_bcast  out_64_octets  out_64_ucast  out_64_mcast  out_64_bcast  "admin_state"  "admin_state"  "oper_state"  "oper_state"  "jumbo_state"  "jumbo_state"  "alias"  "alias"  "flex_uni_state"  "flex_uni_state"  "mtu"  "mac_addr"  "high_speed"  "in_octets"  "in_ucast"  "in_discard"  "in_error"  "out_octets"  "out_ucast"  "out_discard"  "out_error"  "in_mcast"  "in_bcast"  "out_mcast"  "out_bcast"  "in_64_octets"  "in_64_ucast"  "in_64_mcast"  "in_64_bcast"  "out_64_octets"  "out_64_ucast"  "out_64_mcast"  "out_64_bcast"

