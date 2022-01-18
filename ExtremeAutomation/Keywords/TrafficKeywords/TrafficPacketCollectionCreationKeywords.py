from ExtremeAutomation.Library.Utils.Lists.IntList import IntList
from ExtremeAutomation.Library.Utils.Lists.IpV4List import IpV4List
from ExtremeAutomation.Library.Utils.Lists.IpV6List import IpV6List
from ExtremeAutomation.Library.Utils.Lists.EnetAddressList import EnetAddressList
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketCreationKeywords import TrafficPacketCreationKeywords
from ExtremeAutomation.Keywords.BaseClasses.TrafficCreationKeywordsBaseClass import TrafficCreationKeywordsBaseClass


class TrafficPacketCollectionCreationKeywords(TrafficCreationKeywordsBaseClass):
    def __init__(self):
        super(TrafficPacketCollectionCreationKeywords, self).__init__()

        self.pkt_col = list()
        self.pkt_config = TrafficPacketCreationKeywords()

    def create_packet_collection(self, collection_name, number_of_packets, packet_type, packet_length=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name to give to the packet collection.
        [number_of_packets] - The number of packets within the collection.
        [packet_type] - The type of packet that the collection will be made up of.
        [packet_length] - The length of the packets within the collection.

        Creates a collection of packets of a given packet type.
        """
        self._init_keyword(**kwargs)

        number_of_packets = int(number_of_packets)
        packet_collection = list()

        # Creates <number_of_packets> packets of <packet_type> and stores them with the name
        # <collection_name>_<n>.
        for i in range(1, number_of_packets + 1):
            packet_collection.append(self.pkt_config.create_packet(collection_name + "_" + str(i), packet_type,
                                                                   packet_length, add_to_dict=False, log_keyword=False))

        # Stores the created collection under the collection name within the packet dictionary.
        self.pkt_dict.add_collection(collection_name, packet_collection)

        return packet_collection

    def clone_packet_collection(self, collection_name, clone_collection_name, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The source collection to copy.
        [clone_collection_name] - The name the collection copy should be given.

        Clones an existing packet collection to a new collection.
        """
        self._init_keyword(collection_name, **kwargs)

        self.pkt_dict.add_collection(clone_collection_name, self.pkt_col)

        return self.pkt_col

    ####################################################################################################################
    #   Packet Header Range Configuration   ############################################################################
    ####################################################################################################################
    def set_ethernet2_range(self, collection_name, dmac_range_string=None, smac_range_string=None, ether_type=None,
                            **kwargs):
        """
        Keyword Arguments:
        [collection_name]   - The name of the packet collection
        [dmac_range_string] - The range of Destination MACs to use
        [smac_range_string] - The range of Source MACs to use
        [ether_type]        - The EtherType for all packets in the collection

        Sets the Ethernet2 header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        dmac_list = (self.__verify_range_len(EnetAddressList(dmac_range_string).get_all())
                     if dmac_range_string is not None else None)
        smac_list = (self.__verify_range_len(EnetAddressList(smac_range_string).get_all())
                     if smac_range_string is not None else None)

        for i, packet in enumerate(self.pkt_col):
            dmac = dmac_list[i] if dmac_list is not None else None
            smac = smac_list[i] if smac_list is not None else None

            mod_pkt_col.append(self.pkt_config.set_ethernet2(packet, dmac, smac, ether_type, add_to_dict=False,
                                                             log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_vlan_tag_range(self, collection_name, vlan_tag_string=None, vlan_priority_string=None, vlan_tpid=None,
                           **kwargs):
        """
        Keyword Arguments:
        [collection_name]      - The name of the packet collection
        [vlan_tag_string]      - The value or range of values for the VLAN ID
        [vlan_priority_string] - The value or range of values for the VLAN Priority
        [vlan_tpid]            - The Tag Protocol ID for the VLAN header

        Sets the VLAN header fields for the packets in the collection.
        """
        self._init_keyword(collection_name)

        mod_pkt_col = list()

        vlan_tag_list = (self.__verify_range_len(IntList(vlan_tag_string).get_all())
                         if vlan_tag_string is not None else None)
        vlan_priority_list = (self.__verify_range_len(IntList(vlan_priority_string).get_all())
                              if vlan_priority_string is not None else None)

        for i, packet in enumerate(self.pkt_col):
            vlan_tag = vlan_tag_list[i] if vlan_tag_list is not None else None
            vlan_priority = vlan_priority_list[i] if vlan_priority_list is not None else None

            mod_pkt_col.append(self.pkt_config.set_vlan_tag(packet, vlan_tag, vlan_priority, vlan_tpid,
                                                            add_to_dict=False, log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_ipv4_range(self, collection_name, dip_range_string=None, sip_range_string=None, ip_hdr_len=None,
                       ip_ttl=None, ip_proto=None, ip_tos=None, ip_total_len=None, ip_id=None, ip_flags=None,
                       ip_frag_offset=None, ip_chksum=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name]  - The name of the packet collection
        [dip_range_string] - The value or range of values for the Destination IP
        [sip_range_string] - The value or range of values for the Source IP
        [ip_hdr_len]       - The IPv4 Header length
        [ip_ttl]           - The IPv4 TTL
        [ip_proto]         - The IPv4 Protocol ID for the following header
        [ip_tos]           - The IPv4 ToS
        [ip_total_len]     - The IPv4 Total packet length field
        [ip_id]            - The IPv4 packet ID
        [ip_flags]         - The IPv4 flags field
        [ip_frag_offset]   - The offset, for fragmented packets
        [ip_chksum]        - The IPv4 Header checksum (Leave blank for auto-calculation)

        Sets the IPv4 header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        dip_list = (self.__verify_range_len(IpV4List(dip_range_string).get_all())
                    if dip_range_string is not None else None)
        sip_list = (self.__verify_range_len(IpV4List(sip_range_string).get_all())
                    if sip_range_string is not None else None)

        for i, packet in enumerate(self.pkt_col):
            dip = dip_list[i] if dip_list is not None else None
            sip = sip_list[i] if sip_list is not None else None
            mod_pkt_col.append(self.pkt_config.set_ipv4(packet, dip, sip, ip_hdr_len, ip_ttl, ip_proto, ip_tos,
                                                        ip_total_len, ip_id, ip_flags, ip_frag_offset, ip_chksum,
                                                        add_to_dict=False, log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_ipv6_range(self, collection_name, dip_range_string=None, sip_range_string=None, ipv6_traffic_class=None,
                       ipv6_next_header=None, ipv6_hop_limit=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name]    - The name of the packet collection
        [dip_range_string]   - The value or range of values for the Destination IPv6 Address
        [sip_range_string]   - The value or range of values for the Source IPv6 Address
        [ipv6_traffic_class] - The IPv6 Traffic Class
        [ipv6_next_header]   - The IPv6 Next Header
        [ipv6_hop_limit]     - The IPv6 Hop Limit

        Sets the IPv6 header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        dip_list = (self.__verify_range_len(IpV6List(dip_range_string).get_all())
                    if dip_range_string is not None else None)
        sip_list = (self.__verify_range_len(IpV6List(sip_range_string).get_all())
                    if sip_range_string is not None else None)

        for i, packet in enumerate(self.pkt_col):
            dip = dip_list[i] if dip_list is not None else None
            sip = sip_list[i] if sip_list is not None else None

            mod_pkt_col.append(self.pkt_config.set_ipv6(packet, dip, sip, ipv6_traffic_class, ipv6_next_header,
                                                        ipv6_hop_limit, add_to_dict=False, log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    ####################################################################################################################
    #   Single Value Configuration   ###################################################################################
    ####################################################################################################################
    def set_ethernet2_collection(self, collection_name, dmac=None, smac=None, ether_type=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name of the packet collection
        [dmac]            - The Destination MAC address
        [smac]            - The Source MAC address
        [ether_type]      - The EtherType for all packets in the collection

        Sets the Ethernet2 header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_ethernet2(packet, dmac, smac, ether_type,
                                                             add_to_dict=False, log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_sap_collection(self, collection_name, dmac=None, smac=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name of the packet collection
        [dmac]            - The Destination MAC address
        [smac]            - The Source MAC address

        Sets the SAP header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_sap(packet, dmac, smac, add_to_dict=False,
                                                       log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_vlan_tag_collection(self, collection_name, vlan_id=None, vlan_priority=None, vlan_tpid=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name of the packet collection
        [vlan_id]         - The value for the VLAN ID
        [vlan_priority]   - The value for the VLAN Priority
        [vlan_tpid]       - The Tag Protocol ID for the VLAN header

        Sets the VLAN header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_vlan_tag(packet, vlan_id, vlan_priority, vlan_tpid,
                                                            add_to_dict=False, log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_vlanstack_tag_collection(self, collection_name, vlanstack_ids=None, vlanstack_priorities=None,
                                     vlanstack_tpid=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name]      - The name of the packet collection
        [vlanstack_ids]        - A list of values for the VLAN ID
        [vlanstack_priorities] - A list of values for the VLAN Priority
        [vlanstack_tpid]       - A list of Tag Protocol IDs for the VLAN header

        Sets the Q-in-Q VLAN header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_vlan_stack_tag(packet, vlanstack_ids, vlanstack_priorities,
                                                                  vlanstack_tpid, add_to_dict=False,
                                                                  log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_arp_collection(self, collection_name, hardware_type=None, proto_type=None, hardware_size=None,
                           proto_size=None, op_code=None, sender_hardware_address=None, sender_protocol_address=None,
                           target_hardware_address=None, target_protocol_address=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name]         - The name of the packet collection
        [hardware_type]           - The sender's network link type
        [proto_type]              - The ARP protocol EtherType
        [hardware_size]           - The hardware address length
        [proto_size]              - The protocol address length
        [op_code]                 - The ARP operation type (request or reply)
        [sender_hardware_address] - The sender's source MAC address
        [sender_protocol_address] - The sender's IPv4 address
        [target_hardware_address] - The target's MAC address
        [target_protocol_address] - The target's IPv4 address

        Sets the ARP header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_arp(packet, hardware_type, proto_type, hardware_size, proto_size,
                                                       op_code, sender_hardware_address, sender_protocol_address,
                                                       target_hardware_address, target_protocol_address,
                                                       add_to_dict=False, log_keyword=False, **kwargs))

            self.pkt_dict.add_collection(collection_name, mod_pkt_col)
            self._keyword_cleanup()

            return mod_pkt_col

    def set_ipv4_collection(self, collection_name, dip=None, sip=None, ip_hdr_len=None, ip_ttl=None, ip_proto=None,
                            ip_tos=None, ip_total_len=None, ip_id=None, ip_flags=None, ip_frag_offset=None,
                            ip_chksum=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name of the packet collection
        [dip]             - The value for the Destination IP
        [sip]             - The value for the Source IP
        [ip_hdr_len]      - The IPv4 Header length
        [ip_ttl]          - The IPv4 TTL
        [ip_proto]        - The IPv4 Protocol ID for the following header
        [ip_tos]          - The IPv4 ToS
        [ip_total_len]    - The IPv4 Total packet length field
        [ip_id]           - The IPv4 packet ID
        [ip_flags]        - The IPv4 flags field
        [ip_frag_offset]  - The offset, for fragmented packets
        [ip_chksum]       - The IPv4 Header checksum (Leave blank for auto-calculation)

        Sets the IPv4 header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_ipv4(packet, dip, sip, ip_hdr_len, ip_ttl, ip_proto, ip_tos,
                                                        ip_total_len, ip_id, ip_flags, ip_frag_offset, ip_chksum,
                                                        add_to_dict=False, log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_ipv6_collection(self, collection_name, sip=None, dip=None, ipv6_traffic_class=None, ipv6_next_header=None,
                            ipv6_hop_limit=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name]    - The name of the packet collection
        [dip]                - The value for the Destination IPv6 Address
        [sip]                - The value for the Source IPv6 Address
        [ipv6_traffic_class] - The IPv6 Traffic Class
        [ipv6_next_header]   - The IPv6 Next Header
        [ipv6_hop_limit]     - The IPv6 Hop Limit

        Sets the IPv6 header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_ipv6(packet, dip, sip, ipv6_traffic_class, ipv6_next_header,
                                                        ipv6_hop_limit, add_to_dict=False, log_keyword=False,
                                                        **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_udp_collection(self, collection_name, src_port=None, dst_port=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name of the packet collection
        [src_port]        - The UDP source port
        [dst_port]        - The UDP destination port

        Sets the UDP header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_udp(packet, src_port, dst_port, add_to_dict=False,
                                                       log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_tcp_collection(self, collection_name, src_port=None, dst_port=None, seq_num=None, ack_num=None, window=None,
                           ns_flag="0", cwr_flag="0", ece_flag="0", urg_flag="0", ack_flag="0", psh_flag="0",
                           rst_flag="0", syn_flag="0", fin_flag="0", **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name of the packet collection
        [src_port]        - The TCP source port
        [dst_port]        - The TCP destination port
        [seq_num]         - The TCP sequence number
        [ack_num]         - The TCP sequence number expected for a TCP ACK
        [window]          - The receive window size
        [ns_flag]         - The concealment protection flag
        [cwr_flag]        - The congestion window reduced flag
        [ece_flag]        - The ECN-Echo flag
        [urg_flag]        - The urgent pointer field flag
        [ack_flag]        - The acknowledgement flag
        [psh_flag]        - The push function flag
        [rst_flag]        - The reset flag
        [syn_flag]        - The synchronize flag
        [fin_flag]        - The last packet flag

        Sets the TCP header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_tcp(packet, src_port, dst_port, seq_num, ack_num, window,
                                                       ns_flag, cwr_flag, ece_flag, urg_flag, ack_flag, psh_flag,
                                                       rst_flag, syn_flag, fin_flag, add_to_dict=False,
                                                       log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_bpdu_header_collection(self, collection_name, protocol_id=None, version=None, message_type=None, flags=None,
                                   root_prio=None, root_mac=None, cost=None, bridge_prio=None, bridge_mac=None,
                                   port_id=None, age=None, max_age=None, hello_time=None, forward_delay=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name of the packet collection
        [protocol_id]     - The spanning tree protocol ID
        [version]         - The spanning tree version
        [message_type]    - The spanning tree message type
        [flags]           - The spanning tree flags field
        [root_prio]       - The Root bridge priority
        [root_mac]        - The Root bridge MAC address
        [cost]            - The Root path cost
        [bridge_prio]     - The Designated bridge priority
        [bridge_mac]      - The Designated bridge MAC address
        [port_id]         - The sender's port ID
        [age]             - The BPDU current age
        [max_age]         - The spanning tree max age
        [hello_time]      - The spanning tree hello interval
        [forward_delay]   - The spanning tree forward delay

        Sets the Spanning Tree BPDU header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_bpdu_header(packet, protocol_id, version, message_type, flags,
                                                               root_prio, root_mac, cost, bridge_prio, bridge_mac,
                                                               port_id, age, max_age, hello_time, forward_delay,
                                                               add_to_dict=False, log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_tcn_bpdu_collection_(self, collection_name, protocol_id=None, version=None, message_type=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name of the packet collection
        [protocol_id]     - The spanning tree protocol ID
        [version]         - The spanning tree version
        [message_type]    - The spanning tree message type

        Sets the Spanning Tree TCN BPDU header fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_tcn_bpdu(packet, protocol_id, version, message_type,
                                                            add_to_dict=False, log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_mstp_bpdu_cist_header_collection(self, collection_name, ver1_length=None, ver3_length=None, msti_name=None,
                                             msti_digest=None, cist_bridge_prio=None, cist_bridge_mac=None,
                                             cist_path_cost=None, cist_hops=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name]  - The name of the packet collection
        [ver1_length]      - The version 1 length
        [ver3_length]      - The version 3 length
        [msti_name]        - The MST region name
        [msti_digest]      - The MST configuration digest
        [cist_bridge_prio] - The CIST Root bridge priority
        [cist_bridge_mac]  - The CIST Root bridge MAC address
        [cist_path_cost]   - The CIST external path cost
        [cist_hops]        - The current hop count (message age)

        Sets the MST BPDU header CIST fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_mstp_bpdu_cist_header(packet, ver1_length, ver3_length, msti_name,
                                                                         msti_digest, cist_bridge_prio, cist_bridge_mac,
                                                                         cist_path_cost, cist_hops, add_to_dict=False,
                                                                         log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def set_msti_bpdu_extensions_collection(self, collection_name, msti_list, **kwargs):
        """
        Keyword Arguments:
        [collection_name]  - The name of the packet collection
        [msti_list]        - A list of MST IDs

        Sets the MST BPDU header additional MST ID fields for the packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.set_msti_bpdu_extensions(packet, msti_list, add_to_dict=False,
                                                                        log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def add_lldp_tlv_collection(self, collection_name, type_name, value=None, type_id=None, length=None, **kwargs):
        """
        Keyword Arguments:
        [collection_name] - The name of the packet the TLV should be added to.
        [type_name]       - The type of TLV to add. Valid types are as follows.
                              - Capabilities
                                  - Expected Value: 4 byte hex string (ex: 0x0004)
                              - Chassis Subtype
                                  - Expected Value: MAC Address
                              - Port Subtype
                                  - Expected Value: Port (ex: ge.3.2)
                              - Port Description
                                  - Expected Value: String (ex: ISL Port A)
                              - System Name
                                  - Expected Value: String (ex: EXOS_460G2)
                              - System Description
                                  - Expected Value: String (ex: S4, Version 8.42.01.0007)
                              - Port VLAN
                                  - Expected Value: VLAN ID (ex: 1234)
                              - MAC Phy
                                  - Expected Value: 6 byte hex string (0x123456)
                              - Time to Live
                                  - Expected Value: Number string (ex: 120)
                              - End
                                  - No value is provided
                              - Custom
                                  - Expected Value: N/A
        [value]           - The TLV's value.
        [type_id]         - If a custom TLV is added, the value the type field should be set to.
        [length]          - If a custom TLV is added, the value the length field should be set to.

        Adds the TLV to the LLDP packets in the collection.
        """
        self._init_keyword(collection_name, **kwargs)

        mod_pkt_col = list()

        for packet in self.pkt_col:
            mod_pkt_col.append(self.pkt_config.add_lldp_tlv(packet, type_name, value, type_id, length,
                                                            add_to_dict=False, log_keyword=False, **kwargs))

        self.pkt_dict.add_collection(collection_name, mod_pkt_col)
        self._keyword_cleanup()

        return mod_pkt_col

    def __verify_range_len(self, expanded_range_list):
        collection_length = len(self.pkt_col)
        if isinstance(expanded_range_list, list):
            if len(expanded_range_list) == 1:
                return list(expanded_range_list * collection_length)
            elif len(expanded_range_list) < collection_length:
                raise FailureException(str(len(expanded_range_list)) + " values provided at least " +
                                       str(collection_length) + " must be provided.")
            else:
                return expanded_range_list
        elif expanded_range_list is None:
            return list()
        else:
            raise Exception("Expected a list, got " + type(expanded_range_list) + " instead.")
