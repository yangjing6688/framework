# TrafficPacketCollectionCreationKeywords
Library Scope: test suite<br>
Named Arguments: Supported

## Introduction
Documentation for test library TrafficPacketCollectionCreationKeywords.

## Shortcuts
[Add Lldp Tlv Collection](#Add_Lldp_Tlv_Collection) | [Clone Packet Collection](#Clone_Packet_Collection) | [Create Packet Collection](#Create_Packet_Collection) | [Set Arp Collection](#Set_Arp_Collection) | [Set Bpdu Header Collection](#Set_Bpdu_Header_Collection) | [Set Ethernet2 Collection](#Set_Ethernet2_Collection) | [Set Ethernet2 Range](#Set_Ethernet2_Range) | [Set Ipv4 Collection](#Set_Ipv4_Collection) | [Set Ipv4 Range](#Set_Ipv4_Range) | [Set Ipv6 Collection](#Set_Ipv6_Collection) | [Set Ipv6 Range](#Set_Ipv6_Range) | [Set Msti Bpdu Extensions Collection](#Set_Msti_Bpdu_Extensions_Collection) | [Set Mstp Bpdu Cist Header Collection](#Set_Mstp_Bpdu_Cist_Header_Collection) | [Set Sap Collection](#Set_Sap_Collection) | [Set Tcn Bpdu Collection](#Set_Tcn_Bpdu_Collection) | [Set Tcp Collection](#Set_Tcp_Collection) | [Set Udp Collection](#Set_Udp_Collection) | [Set Vlan Tag Collection](#Set_Vlan_Tag_Collection) | [Set Vlan Tag Range](#Set_Vlan_Tag_Range) | [Set Vlanstack Tag Collection](#Set_Vlanstack_Tag_Collection)
***

## Keywords
| Keyword | Arguments | Documentation |
|---------|-----------|---------------|
| <a name="Add_Lldp_Tlv_Collection"></a>Add Lldp Tlv Collection | collection_name, type_name, value=None, type_id=None, length=None, **kwargs |  |
| <a name="Clone_Packet_Collection"></a>Clone Packet Collection | collection_name, clone_collection_name, **kwargs | Keyword Arguments:<br>[collection_name] - The source collection to copy.<br>[clone_collection_name] - The name the collection copy should be given.<br><br>Clones an existing packet collection to a new collection. |
| <a name="Create_Packet_Collection"></a>Create Packet Collection | collection_name, number_of_packets, packet_type, packet_length=None, **kwargs | Keyword Arguments:<br>[collection_name] - The name to give to the packet collection.<br>[number_of_packets] - The number of packets within the collection.<br>[packet_type] - The type of packet that the collection will be made up of.<br>[packet_length] - The length of the packets within the collection.<br><br>Creates a collection of packets of a given packet type. |
| <a name="Set_Arp_Collection"></a>Set Arp Collection | collection_name, hardware_type=None, proto_type=None, hardware_size=None, proto_size=None, op_code=None, sender_hardware_address=None, sender_protocol_address=None, target_hardware_address=None, target_protocol_address=None, **kwargs |  |
| <a name="Set_Bpdu_Header_Collection"></a>Set Bpdu Header Collection | collection_name, protocol_id=None, version=None, message_type=None, flags=None, root_prio=None, root_mac=None, cost=None, bridge_prio=None, bridge_mac=None, port_id=None, age=None, max_age=None, hello_time=None, forward_delay=None, **kwargs |  |
| <a name="Set_Ethernet2_Collection"></a>Set Ethernet2 Collection | collection_name, dmac=None, smac=None, ether_type=None, **kwargs |  |
| <a name="Set_Ethernet2_Range"></a>Set Ethernet2 Range | collection_name, dmac_range_string=None, smac_range_string=None, ether_type=None, **kwargs |  |
| <a name="Set_Ipv4_Collection"></a>Set Ipv4 Collection | collection_name, dip=None, sip=None, ip_hdr_len=None, ip_ttl=None, ip_proto=None, ip_tos=None, ip_total_len=None, ip_id=None, ip_flags=None, ip_frag_offset=None, ip_chksum=None, **kwargs |  |
| <a name="Set_Ipv4_Range"></a>Set Ipv4 Range | collection_name, dip_range_string=None, sip_range_string=None, ip_hdr_len=None, ip_ttl=None, ip_proto=None, ip_tos=None, ip_total_len=None, ip_id=None, ip_flags=None, ip_frag_offset=None, ip_chksum=None, **kwargs |  |
| <a name="Set_Ipv6_Collection"></a>Set Ipv6 Collection | collection_name, sip=None, dip=None, ipv6_traffic_class=None, ipv6_next_header=None, ipv6_hop_limit=None, **kwargs |  |
| <a name="Set_Ipv6_Range"></a>Set Ipv6 Range | collection_name, dip_range_string=None, sip_range_string=None, ipv6_traffic_class=None, ipv6_next_header=None, ipv6_hop_limit=None, **kwargs |  |
| <a name="Set_Msti_Bpdu_Extensions_Collection"></a>Set Msti Bpdu Extensions Collection | collection_name, msti_list, **kwargs |  |
| <a name="Set_Mstp_Bpdu_Cist_Header_Collection"></a>Set Mstp Bpdu Cist Header Collection | collection_name, ver1_length=None, ver3_length=None, msti_name=None, msti_digest=None, cist_bridge_prio=None, cist_bridge_mac=None, cist_path_cost=None, cist_hops=None, **kwargs |  |
| <a name="Set_Sap_Collection"></a>Set Sap Collection | collection_name, dmac=None, smac=None, **kwargs |  |
| <a name="Set_Tcn_Bpdu_Collection"></a>Set Tcn Bpdu Collection | collection_name, protocol_id=None, version=None, message_type=None, **kwargs |  |
| <a name="Set_Tcp_Collection"></a>Set Tcp Collection | collection_name, src_port=None, dst_port=None, seq_num=None, ack_num=None, window=None, ns_flag=0, cwr_flag=0, ece_flag=0, urg_flag=0, ack_flag=0, psh_flag=0, rst_flag=0, syn_flag=0, fin_flag=0, **kwargs |  |
| <a name="Set_Udp_Collection"></a>Set Udp Collection | collection_name, src_port=None, dst_port=None, **kwargs |  |
| <a name="Set_Vlan_Tag_Collection"></a>Set Vlan Tag Collection | collection_name, vlan_id=None, vlan_priority=None, vlan_tpid=None, **kwargs |  |
| <a name="Set_Vlan_Tag_Range"></a>Set Vlan Tag Range | collection_name, vlan_tag_string=None, vlan_priority_string=None, vlan_tpid=None, **kwargs |  |
| <a name="Set_Vlanstack_Tag_Collection"></a>Set Vlanstack Tag Collection | collection_name, vlanstack_count, vlanstack_tpid=None, vlanstack_ids=None, vlanstack_priorities=None, **kwargs |  |
