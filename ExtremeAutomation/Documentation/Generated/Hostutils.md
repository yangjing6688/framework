# Command Keyword Library Documentation for Hostutils
This feature is located in this file: `hostutils.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: ping_host
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_ping_host(device_name )

	Robot API Call: 

		hostutils_ping_host  device_name  

UUID: 57c52793-0d02-4f7f-b5b2-53bcd3024df4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ping -c {count} -i {timeout} {host_address}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ping count {count} interval {timeout} {host_address}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ping {host_address} count {count} -t {timeout}

----------------------------------------------


## REST
## SNMP
# API Function: enable_debug_mode
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_enable_debug_mode(device_name )

	Robot API Call: 

		hostutils_enable_debug_mode  device_name  

UUID: 561a3b82-0d6e-456c-9c21-e8732fff4e8c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable debug-mode

----------------------------------------------


## REST
## SNMP
# API Function: return_debug_creds
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_return_debug_creds(device_name )

	Robot API Call: 

		hostutils_return_debug_creds  device_name  

UUID: 1151e4ca-cb54-4aed-b89c-d6d3cb64661e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		{response}

----------------------------------------------


## REST
## SNMP
# API Function: enable_feature_license
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_enable_feature_license(device_name )

	Robot API Call: 

		hostutils_enable_feature_license  device_name  

UUID: 5c9acf86-b925-473a-b308-755ad8b516bb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable license {key}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_ipaddr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_ipaddr(device_name )

	Robot API Call: 

		hostutils_l2_ping_ipaddr  device_name  

UUID: b865ec88-e01c-47da-b928-d8cacd8278fb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping ip-address {ip_address}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_ipaddr_burst
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_ipaddr_burst(device_name )

	Robot API Call: 

		hostutils_l2_ping_ipaddr_burst  device_name  

UUID: e826a9f3-d167-4d9a-b4b2-e24b370bf180
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {ip_address} burst-count {burst_count}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_ipaddr_data_tlv_size
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_ipaddr_data_tlv_size(device_name )

	Robot API Call: 

		hostutils_l2_ping_ipaddr_data_tlv_size  device_name  

UUID: c03217f7-8d02-4761-82e7-3b34bac7f745
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {ip_address} data-tlv-size {tlv_size}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_ipaddr_frame_size
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_ipaddr_frame_size(device_name )

	Robot API Call: 

		hostutils_l2_ping_ipaddr_frame_size  device_name  

UUID: 623c47a7-9076-4190-adb5-81f2fbf456d9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {ip_address} frame-size {frame_size}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_ipaddr_time_out
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_ipaddr_time_out(device_name )

	Robot API Call: 

		hostutils_l2_ping_ipaddr_time_out  device_name  

UUID: e1f7fe5f-bcef-48f2-be42-169b60e75f74
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {ip_address} time-out {time_out}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_ipaddr_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_ipaddr_vrf(device_name )

	Robot API Call: 

		hostutils_l2_ping_ipaddr_vrf  device_name  

UUID: 84b7d926-79ed-4786-a361-cf64e19e291d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping ip-address {ip_address} vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_mac(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_mac  device_name  

UUID: e5e1cf1f-1bc4-429b-90e5-3e5b97f180f7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping vlan {vlan} mac {mac_address}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename  device_name  

UUID: 876087e1-0ccd-4062-9b8a-eafd8b806609
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_burst
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_burst(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_burst  device_name  

UUID: 2f5e3a17-79c6-45dd-a236-464eb043f19c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} burst-count {burst_count}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_data_tlv_size
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_data_tlv_size(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_data_tlv_size  device_name  

UUID: 3317ad1e-b519-441e-a82b-1fe05a4f4624
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} data-tlv-size {tlv_size}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_frame_size
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_frame_size(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_frame_size  device_name  

UUID: 03afaf76-43a1-4599-97e9-5122edaee6e5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} frame_size {frame_size}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_priority(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_priority  device_name  

UUID: a1e82a3d-52f1-418a-bda1-2ba2d7a063d0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_source_mode_nodal
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_source_mode_nodal(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_source_mode_nodal  device_name  

UUID: dd8b8868-c9e0-46e7-948b-666d60ac7683
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} source-mode nodal

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_source_mode_novlanmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_source_mode_novlanmac(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_source_mode_novlanmac  device_name  

UUID: 1bf7c148-23fd-4220-9961-7894422c0806
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} source-mode novlanmac

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_testfill_pattern_all_zero
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_testfill_pattern_all_zero(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_testfill_pattern_all_zero  device_name  

UUID: 66d4d1b0-9b11-4e0e-9c56-c6c35b5e96e6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} testfill-pattern all-zero

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_testfill_pattern_all_zero_crc
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_testfill_pattern_all_zero_crc(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_testfill_pattern_all_zero_crc  device_name  

UUID: 21bc24ec-1323-492a-a818-900f6fcc87ef
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} testfill-pattern all-zero-crc

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq  device_name  

UUID: 93f96795-4070-4447-b3c1-e3d58ce27937
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} testfill-pattern pseudo-random-bit-sequence

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq_crc
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq_crc(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq_crc  device_name  

UUID: 09e13a76-cb60-4905-82f8-3b3687353048
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} testfill-pattern pseudo-random-bit-sequence-crc

----------------------------------------------


## REST
## SNMP
# API Function: l2_ping_vlan_routernodename_timeout
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_ping_vlan_routernodename_timeout(device_name )

	Robot API Call: 

		hostutils_l2_ping_vlan_routernodename_timeout  device_name  

UUID: 71efee42-56ee-4485-915b-e9dc4bd99bb6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 ping {vlan} routernodename {node_name} time-out {timeout}

----------------------------------------------


## REST
## SNMP
# API Function: l2_traceroute_ipaddr
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_traceroute_ipaddr(device_name )

	Robot API Call: 

		hostutils_l2_traceroute_ipaddr  device_name  

UUID: b5249415-798c-409e-8847-f9ea9572540c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 traceroute ip-address {ip_address}

----------------------------------------------


## REST
## SNMP
# API Function: l2_traceroute_ipaddr_ttl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_traceroute_ipaddr_ttl(device_name )

	Robot API Call: 

		hostutils_l2_traceroute_ipaddr_ttl  device_name  

UUID: f0854239-db80-4193-9184-792ac5c1527f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 traceroute ip-address {ip_address} ttl-value {ttl}

----------------------------------------------


## REST
## SNMP
# API Function: l2_traceroute_ipaddr_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_traceroute_ipaddr_vrf(device_name )

	Robot API Call: 

		hostutils_l2_traceroute_ipaddr_vrf  device_name  

UUID: 206ff912-49f4-433d-93a0-93959427859d
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 traceroute ip-address {ip_address} vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: l2_traceroute_vlan_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_traceroute_vlan_mac(device_name )

	Robot API Call: 

		hostutils_l2_traceroute_vlan_mac  device_name  

UUID: 4609e598-4735-4f4d-93ed-93c2c645ba6f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 traceroute vlan {vlan} mac {mac}

----------------------------------------------


## REST
## SNMP
# API Function: l2_traceroute_vlan_routernodename_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_traceroute_vlan_routernodename_priority(device_name )

	Robot API Call: 

		hostutils_l2_traceroute_vlan_routernodename_priority  device_name  

UUID: 0587bdf3-05d3-4686-b780-0640a76a0fd1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 traceroute vlan {vlan} routernodename {name} priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: l2_traceroute_vlan_routernodename_source_mode_nodal
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_traceroute_vlan_routernodename_source_mode_nodal(device_name )

	Robot API Call: 

		hostutils_l2_traceroute_vlan_routernodename_source_mode_nodal  device_name  

UUID: 786dcc02-9baf-429f-99f5-c3202b4e8865
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 traceroute vlan {vlan} routernodename {name} source-mode nodal

----------------------------------------------


## REST
## SNMP
# API Function: l2_traceroute_vlan_routernodename_source_mode_novlanmac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_traceroute_vlan_routernodename_source_mode_novlanmac(device_name )

	Robot API Call: 

		hostutils_l2_traceroute_vlan_routernodename_source_mode_novlanmac  device_name  

UUID: 9dd77c84-6cc7-4673-aafa-4fdcd64ae983
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 traceroute vlan {vlan} routernodename {name} source-mode novlanmac

----------------------------------------------


## REST
## SNMP
# API Function: l2_traceroute_vlan_routernodename_ttl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_traceroute_vlan_routernodename_ttl(device_name )

	Robot API Call: 

		hostutils_l2_traceroute_vlan_routernodename_ttl  device_name  

UUID: 5dd27024-5a9a-4bec-9876-62490a39ea72
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 traceroute vlan {vlan} routernodename {name} ttl-value {ttl}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracetree_vlan_isid
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracetree_vlan_isid(device_name )

	Robot API Call: 

		hostutils_l2_tracetree_vlan_isid  device_name  

UUID: 81053d9a-5b3b-46a4-93b4-1de3c8954c87
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracetree vlan {vlan} isid {isid}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracetree_vlan_isid_mac
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracetree_vlan_isid_mac(device_name )

	Robot API Call: 

		hostutils_l2_tracetree_vlan_isid_mac  device_name  

UUID: 04cb12b5-4318-4a6c-8828-82cd43cfd723
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracetree vlan {vlan} isid mac {mac}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracetree_vlan_isid_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracetree_vlan_isid_priority(device_name )

	Robot API Call: 

		hostutils_l2_tracetree_vlan_isid_priority  device_name  

UUID: 44b28541-b559-4f40-b9ca-3175235e92eb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracetree vlan {vlan} isid priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracetree_vlan_isid_routernodename
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracetree_vlan_isid_routernodename(device_name )

	Robot API Call: 

		hostutils_l2_tracetree_vlan_isid_routernodename  device_name  

UUID: f67bb98f-1f9c-4107-ac78-495ddc15b4cf
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracetree vlan {vlan} isid {isid} routernodename {name}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracetree_vlan_isid_routernodename_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracetree_vlan_isid_routernodename_priority(device_name )

	Robot API Call: 

		hostutils_l2_tracetree_vlan_isid_routernodename_priority  device_name  

UUID: 170b5bf4-9943-4328-84a8-b0e2a9b46099
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracetree vlan {vlan} isid {isid} routernodename {name} priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracetree_vlan_isid_routernodename_source_mode_nodal
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracetree_vlan_isid_routernodename_source_mode_nodal(device_name )

	Robot API Call: 

		hostutils_l2_tracetree_vlan_isid_routernodename_source_mode_nodal  device_name  

UUID: e8f8e6bb-867f-4ce6-a0db-ac446df1dd52
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracetree vlan {vlan} isid {isid} routernodename {name} source-mode nodal

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracetree_vlan_isid_routernodename_ttl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracetree_vlan_isid_routernodename_ttl(device_name )

	Robot API Call: 

		hostutils_l2_tracetree_vlan_isid_routernodename_ttl  device_name  

UUID: 4eba03ce-76c2-46ee-bd04-415e3d2b93be
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracetree vlan {vlan} isid {isid} routernodename {name} ttl-value {ttl}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracetree_vlan_isid_source_mode_nodal
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracetree_vlan_isid_source_mode_nodal(device_name )

	Robot API Call: 

		hostutils_l2_tracetree_vlan_isid_source_mode_nodal  device_name  

UUID: ecbd065a-1d3b-4dbd-a56f-146a2e29ce7e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracetree vlan {vlan} isid {isid} source-mode nodal

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracetree_vlan_isid_ttl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracetree_vlan_isid_ttl(device_name )

	Robot API Call: 

		hostutils_l2_tracetree_vlan_isid_ttl  device_name  

UUID: cbb445d9-b372-4fc2-9a8c-8eea9233bb38
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracetree vlan {vlan} isid {isid} ttl-value {ttl}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracemroute
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracemroute(device_name )

	Robot API Call: 

		hostutils_l2_tracemroute  device_name  

UUID: 9ba90ce9-3030-4298-9a31-f35f7d39f872
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracemroute source {source_address} group {group_address}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracemroute_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracemroute_priority(device_name )

	Robot API Call: 

		hostutils_l2_tracemroute_priority  device_name  

UUID: fd70b7d6-72c3-4d62-bbb2-1ccc2b32d135
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracemroute source {source_address} group {group_address} priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracemroute_ttl
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracemroute_ttl(device_name )

	Robot API Call: 

		hostutils_l2_tracemroute_ttl  device_name  

UUID: 6a382043-bb0d-4def-bc3c-a51cb96632e3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracemroute source {source_address} group {group_address} ttl-value {ttl}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracemroute_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracemroute_vlan(device_name )

	Robot API Call: 

		hostutils_l2_tracemroute_vlan  device_name  

UUID: 7df24a03-94a9-4190-81ed-cd6e0154f12e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracemroute source {source_address} group {group_address} vlan {vlan}

----------------------------------------------


## REST
## SNMP
# API Function: l2_tracemroute_vrf
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_l2_tracemroute_vrf(device_name )

	Robot API Call: 

		hostutils_l2_tracemroute_vrf  device_name  

UUID: b5a1808c-2079-4ac7-a3b3-685d4fd4a0ec
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		l2 tracemroute source {source_address} group {group_address} vrf {vrf_name}

----------------------------------------------


## REST
## SNMP
# API Function: telnet_to_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_telnet_to_ip(device_name )

	Robot API Call: 

		hostutils_telnet_to_ip  device_name  

UUID: 653ec587-88c4-4a0f-bbb8-ff81c1990bb4
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		telnet {ip_address}

----------------------------------------------


## REST
## SNMP
# API Function: ssh_to_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostutils.hostutils_ssh_to_ip(device_name )

	Robot API Call: 

		hostutils_ssh_to_ip  device_name  

UUID: 23546501-3087-40dd-a754-f9e6355e9a49
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ssh user {username} {ip_address}

----------------------------------------------


## REST
## SNMP
