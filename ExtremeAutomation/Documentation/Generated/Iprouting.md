# Command Keyword Library Documentation for Iprouting
This feature is located in this file: `iprouting.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: create_static_route
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_create_static_route(device_name, route, nexthop)

	Robot API Call: 

		iprouting_create_static_route  device_name  route  nexthop

UUID: ae2bcfeb-eb32-4a9c-a98c-10dd40a7527f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip route {route} {nexthop}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure iproute add {route} {nexthop}

----------------------------------------------


## REST
## SNMP
# API Function: delete_static_route
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_delete_static_route(device_name, route, nexthop)

	Robot API Call: 

		iprouting_delete_static_route  device_name  route  nexthop

UUID: cbc5ea79-a20b-4553-ac1f-60b32d1516d5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip route {route} {nexthop}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure iproute delete {route} {nexthop}

----------------------------------------------


## REST
## SNMP
# API Function: enable_ipmcforwarding_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_enable_ipmcforwarding_global(device_name )

	Robot API Call: 

		iprouting_enable_ipmcforwarding_global  device_name  

UUID: f69ae499-5b57-4e24-8987-a14d44cd3481
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable ipmcforwarding

----------------------------------------------


## REST
## SNMP
# API Function: enable_ipmcforwarding_ipv4_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_enable_ipmcforwarding_ipv4_global(device_name )

	Robot API Call: 

		iprouting_enable_ipmcforwarding_ipv4_global  device_name  

UUID: 32e171b5-6551-4db1-8ee2-0f6a864d50fc
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable ipmcforwarding ipv4

----------------------------------------------


## REST
## SNMP
# API Function: enable_ipmcforwarding_ipv6_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_enable_ipmcforwarding_ipv6_global(device_name )

	Robot API Call: 

		iprouting_enable_ipmcforwarding_ipv6_global  device_name  

UUID: 392d0585-b01e-4d9f-8142-02372f1cc973
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable ipmcforwarding ipv6

----------------------------------------------


## REST
## SNMP
# API Function: enable_ipmcforwarding_ipv4_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_enable_ipmcforwarding_ipv4_vlan(device_name )

	Robot API Call: 

		iprouting_enable_ipmcforwarding_ipv4_vlan  device_name  

UUID: 0ae7168d-3108-4462-b0e7-94f3b8f38310
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable ipmcforwarding ipv4 vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: enable_ipmcforwarding_ipv6_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_enable_ipmcforwarding_ipv6_vlan(device_name )

	Robot API Call: 

		iprouting_enable_ipmcforwarding_ipv6_vlan  device_name  

UUID: 16e0d041-734c-4eb9-a721-9a4ba9ff1279
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable ipmcforwarding ipv6 vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: disable_ipmcforwarding_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_disable_ipmcforwarding_global(device_name )

	Robot API Call: 

		iprouting_disable_ipmcforwarding_global  device_name  

UUID: debea284-1bd3-4f2f-995e-9a4b3763b3b1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable ipmcforwarding

----------------------------------------------


## REST
## SNMP
# API Function: disable_ipmcforwarding_ipv4_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_disable_ipmcforwarding_ipv4_global(device_name )

	Robot API Call: 

		iprouting_disable_ipmcforwarding_ipv4_global  device_name  

UUID: b82960d4-7270-4d1c-b212-0cefcaa26d93
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable ipmcforwarding ipv4

----------------------------------------------


## REST
## SNMP
# API Function: disable_ipmcforwarding_ipv6_global
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_disable_ipmcforwarding_ipv6_global(device_name )

	Robot API Call: 

		iprouting_disable_ipmcforwarding_ipv6_global  device_name  

UUID: e9b994c9-9b5e-4f22-88b3-014c36d5a7d8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable ipmcforwarding ipv6

----------------------------------------------


## REST
## SNMP
# API Function: disable_ipmcforwarding_ipv4_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_disable_ipmcforwarding_ipv4_vlan(device_name )

	Robot API Call: 

		iprouting_disable_ipmcforwarding_ipv4_vlan  device_name  

UUID: 8a8946e9-5ac9-433a-be25-b5a9bdd8d02a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable ipmcforwarding ipv4 vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: disable_ipmcforwarding_ipv6_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_disable_ipmcforwarding_ipv6_vlan(device_name )

	Robot API Call: 

		iprouting_disable_ipmcforwarding_ipv6_vlan  device_name  

UUID: 545b5ccb-1043-46e1-925a-35a934e7dae1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable ipmcforwarding ipv6 vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: iprouting_verify_and_store_default_gateway_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_verify_and_store_default_gateway_ip(device_name, destination_ip, gateway_name)

	Robot API Call: 

		iprouting_verify_and_store_default_gateway_ip  device_name  destination_ip  gateway_name

# API Function: iprouting_verify_route_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_verify_route_interface(device_name, interface)

	Robot API Call: 

		iprouting_verify_route_interface  device_name  interface

# API Function: iprouting_verify_route_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_verify_route_exists(device_name, route, mask, nexthop, vrf_name, isid, cost, interface, protocol, age, route_type, preference)

	Robot API Call: 

		iprouting_verify_route_exists  device_name  route  mask  nexthop  vrf_name  isid  cost  interface  protocol  age  route_type  preference

# API Function: iprouting_verify_route_does_not_exist
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_verify_route_does_not_exist(device_name, route, mask, nexthop, vrf_name, isid, cost, interface, protocol, age, route_type, preference)

	Robot API Call: 

		iprouting_verify_route_does_not_exist  device_name  route  mask  nexthop  vrf_name  isid  cost  interface  protocol  age  route_type  preference

# API Function: iprouting_verify_ipv6_route_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_verify_ipv6_route_exists(device_name, route, nexthop, interface, protocol, cost, age, route_type, preference)

	Robot API Call: 

		iprouting_verify_ipv6_route_exists  device_name  route  nexthop  interface  protocol  cost  age  route_type  preference

# API Function: iprouting_verify_vrf_route_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_verify_vrf_route_exists(device_name, route, mask, nexthop, vrf_name, cost, interface, protocol, age, route_type, preference)

	Robot API Call: 

		iprouting_verify_vrf_route_exists  device_name  route  mask  nexthop  vrf_name  cost  interface  protocol  age  route_type  preference

# API Function: iprouting_verify_vrf_ipv6_route_exists
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.iprouting.iprouting_verify_vrf_ipv6_route_exists(device_name, route, nexthop, vrf_name, isid, cost, interface, protocol, age, route_type, preference)

	Robot API Call: 

		iprouting_verify_vrf_ipv6_route_exists  device_name  route  nexthop  vrf_name  isid  cost  interface  protocol  age  route_type  preference

