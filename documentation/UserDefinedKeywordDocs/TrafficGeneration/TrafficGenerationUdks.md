# TrafficGenerationUdks
Library Scope: N/A<br>
Named Arguments: Supported

## Introduction
Documentation for resource file TrafficGenerationUdks.

## Shortcuts
[Configure Packet on Port, Continuous](#Configure_Packet_on_Port,_Continuous) | [Configure Packet on Port, Single Burst](#Configure_Packet_on_Port,_Single_Burst) | [Create ARP Packet](#Create_ARP_Packet) | [Create Ethernet2 Packet](#Create_Ethernet2_Packet) | [Create IPv4 Packet](#Create_IPv4_Packet) | [Create IPv4 TCP Packet](#Create_IPv4_TCP_Packet) | [Create IPv4 UDP Packet](#Create_IPv4_UDP_Packet) | [Create IPv6 Packet](#Create_IPv6_Packet) | [Create IPv6 TCP Packet](#Create_IPv6_TCP_Packet) | [Create IPv6 UDP Packet](#Create_IPv6_UDP_Packet) | [Start Capture](#Start_Capture) | [Start Capture with DMAC and SMAC Filter](#Start_Capture_with_DMAC_and_SMAC_Filter) | [Start Capture with DMAC Filter](#Start_Capture_with_DMAC_Filter) | [Start Capture with SMAC Filter](#Start_Capture_with_SMAC_Filter) | [Stop Transmit and Clear all Streams on Port](#Stop_Transmit_and_Clear_all_Streams_on_Port) | [Transmit Packet on Port, Continuous](#Transmit_Packet_on_Port,_Continuous) | [Transmit Packet on Port, Single Burst](#Transmit_Packet_on_Port,_Single_Burst) | [Transmit Traffic Bidirectionally and Verify it was Received](#Transmit_Traffic_Bidirectionally_and_Verify_it_was_Received) | [Transmit Traffic Unidirectionally and Verify it was Received](#Transmit_Traffic_Unidirectionally_and_Verify_it_was_Received)
***

## Keywords
| Keyword | Arguments | Documentation |
|---------|-----------|---------------|
| <a name="Configure_Packet_on_Port,_Continuous"></a>Configure Packet on Port, Continuous | tgen_port, packet_name, stream_number=1, count=100, rate=100, unit=pps |  |
| <a name="Configure_Packet_on_Port,_Single_Burst"></a>Configure Packet on Port, Single Burst | tgen_port, packet_name, stream_number=1, count=100, rate=100, unit=pps |  |
| <a name="Create_ARP_Packet"></a>Create ARP Packet | packet_name, dmac=${NONE}, smac=${NONE}, vlan_id=${NONE}, vlan_prio=${NONE}, vlan_tpid=${NONE}, hardware_type=${NONE}, proto_type=${NONE}, hardware_size=${NONE}, proto_size=${NONE}, op_code=${NONE}, sender_hardware=${NONE}, sender_proto=${NONE}, target_hardware=${NONE}, target_proto=${NONE}, packet_len=${NONE} |  |
| <a name="Create_Ethernet2_Packet"></a>Create Ethernet2 Packet | packet_name, dmac=${NONE}, smac=${NONE}, vlan_id=${NONE}, vlan_prio=${NONE}, vlan_tpid=${NONE}, ether_type=${NONE}, packet_len=${NONE} |  |
| <a name="Create_IPv4_Packet"></a>Create IPv4 Packet | packet_name, dmac=${NONE}, smac=${NONE}, vlan_id=${NONE}, vlan_prio=${NONE}, vlan_tpid=${NONE}, dip=${NONE}, sip=${NONE}, header_len=${NONE}, ttl=${NONE}, proto=${NONE}, tos=${NONE}, total_len=${NONE}, id=${NONE}, flags=${NONE}, frag_offset=${NONE}, checksum=${NONE}, packet_len=${NONE} |  |
| <a name="Create_IPv4_TCP_Packet"></a>Create IPv4 TCP Packet | packet_name, dmac=${NONE}, smac=${NONE}, vlan_id=${NONE}, vlan_prio=${NONE}, vlan_tpid=${NONE}, dip=${NONE}, sip=${NONE}, src_port=${NONE}, dst_port=${NONE}, header_len=${NONE}, ttl=${NONE}, proto=${NONE}, tos=${NONE}, total_len=${NONE}, id=${NONE}, flags=${NONE}, frag_offset=${NONE}, checksum=${NONE}, seq_num=${NONE}, ack_num=${NONE}, window=${NONE}, ns_flag=0, cwr_flag=0, ece_flag=0, urg_flag=0, ack_flag=0, psh_flag=0, rst_flag=0, syn_flag=0, fin_flag=0, packet_len=${NONE} |  |
| <a name="Create_IPv4_UDP_Packet"></a>Create IPv4 UDP Packet | packet_name, dmac=${NONE}, smac=${NONE}, vlan_id=${NONE}, vlan_prio=${NONE}, vlan_tpid=${NONE}, dip=${NONE}, sip=${NONE}, src_port=${NONE}, dst_port=${NONE}, header_len=${NONE}, ttl=${NONE}, proto=${NONE}, tos=${NONE}, total_len=${NONE}, id=${NONE}, flags=${NONE}, frag_offset=${NONE}, checksum=${NONE}, packet_len=${NONE} |  |
| <a name="Create_IPv6_Packet"></a>Create IPv6 Packet | packet_name, dmac=${NONE}, smac=${NONE}, vlan_id=${NONE}, vlan_prio=${NONE}, vlan_tpid=${NONE}, dip=${NONE}, sip=${NONE}, traffic_class=${NONE}, next_header=${NONE}, hop_limit=${NONE}, packet_len=${NONE} |  |
| <a name="Create_IPv6_TCP_Packet"></a>Create IPv6 TCP Packet | packet_name, dmac=${NONE}, smac=${NONE}, vlan_id=${NONE}, vlan_prio=${NONE}, vlan_tpid=${NONE}, dip=${NONE}, sip=${NONE}, src_port=${NONE}, dst_port=${NONE}, traffic_class=${NONE}, next_header=${NONE}, hop_limit=${NONE}, seq_num=${NONE}, ack_num=${NONE}, window=${NONE}, ns_flag=0, cwr_flag=0, ece_flag=0, urg_flag=0, ack_flag=0, psh_flag=0, rst_flag=0, syn_flag=0, fin_flag=0, packet_len=${NONE} |  |
| <a name="Create_IPv6_UDP_Packet"></a>Create IPv6 UDP Packet | packet_name, dmac=${NONE}, smac=${NONE}, vlan_id=${NONE}, vlan_prio=${NONE}, vlan_tpid=${NONE}, dip=${NONE}, sip=${NONE}, src_port=${NONE}, dst_port=${NONE}, traffic_class=${NONE}, next_header=${NONE}, hop_limit=${NONE}, packet_len=${NONE} |  |
| <a name="Start_Capture"></a>Start Capture | tgen_port |  |
| <a name="Start_Capture_with_DMAC_and_SMAC_Filter"></a>Start Capture with DMAC and SMAC Filter | tgen_port, dmac, smac, dmac_mask=${NONE}, smac_mask=${NONE} |  |
| <a name="Start_Capture_with_DMAC_Filter"></a>Start Capture with DMAC Filter | tgen_port, dmac, mask=${NONE} |  |
| <a name="Start_Capture_with_SMAC_Filter"></a>Start Capture with SMAC Filter | tgen_port, smac, mask=${NONE} |  |
| <a name="Stop_Transmit_and_Clear_all_Streams_on_Port"></a>Stop Transmit and Clear all Streams on Port | tgen_port |  |
| <a name="Transmit_Packet_on_Port,_Continuous"></a>Transmit Packet on Port, Continuous | tgen_port, packet_name, stream_number=1, count=100, rate=100, unit=pps |  |
| <a name="Transmit_Packet_on_Port,_Single_Burst"></a>Transmit Packet on Port, Single Burst | tgen_port, packet_name, stream_number=1, count=100, rate=100, unit=pps, max_wait=60 |  |
| <a name="Transmit_Traffic_Bidirectionally_and_Verify_it_was_Received"></a>Transmit Traffic Bidirectionally and Verify it was Received | port_a, port_b, tx_packet_a, tx_packet_b, rx_packet_a, rx_packet_b, tx_count=100 |  |
| <a name="Transmit_Traffic_Unidirectionally_and_Verify_it_was_Received"></a>Transmit Traffic Unidirectionally and Verify it was Received | tx_port, rx_port, tx_packet, rx_packet, tx_count=100 |  |
