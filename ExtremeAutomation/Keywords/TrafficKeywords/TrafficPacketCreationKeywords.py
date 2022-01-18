from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
import ExtremeAutomation.Library.Net.Packet.PacketClassifier as pc
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.Constants.PacketTypeConstants import PacketTypeConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficCreationKeywordsBaseClass import TrafficCreationKeywordsBaseClass


class TrafficPacketCreationKeywords(TrafficCreationKeywordsBaseClass):
    def __init__(self):
        super(TrafficPacketCreationKeywords, self).__init__()

        self.pkt_types = self.__get_packet_types(PacketTypeConstants())
        self.pkt_classifier = pc.PacketClassifier

    def create_packet(self, packet_name, packet_type, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                      length=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name the packet should be stored under. This name will be used
                        to retrieve the packet later.
        [packet_type] - The type of packet to be created. Valid types can be found in
                        "/Keywords/TrafficKeywords/Utils/Constants/PacketTypeConstants.py"
        *[vlan_id] - The VLAN ID to apply to the packet.
        *[vlan_priority] - The VLAN priority to apply to the packet.
        *[vlan_tpid] - The VLAN TPID to apply to the packet.
        [length] - The length of the packet. If no length is passed the minimum valid length will be
                   calculated and used.

        * - If all of theses arguments are None then the packet will be untagged. If any of the values
            are set the packet will be tagged.

        Creates a base packet with a given name and packet type.
        """
        self._init_keyword(**kwargs)

        if packet_type in self.pkt_types:
            self.packet = self.pkt_classifier.get_packet(packet_type)

            if length is not None:
                self.packet.set_length(str(length))
                self.packet.user_set_length = True

            if isinstance(vlan_id, list) or isinstance(vlan_priority, list) or isinstance(vlan_tpid, list):
                self.packet = self.pkt_classifier.copy_to_vlanstack_packet(self.packet)
                self.pkt_dict.add_packet(packet_name, self.packet)
                self.set_vlan_stack_tag(packet_name, vlan_id, vlan_priority, vlan_tpid)
            elif vlan_id is not None or vlan_priority is not None or vlan_tpid is not None:
                self.packet = self.pkt_classifier.copy_to_tag_packet(self.packet)
                self.pkt_dict.add_packet(packet_name, self.packet)
                self.set_vlan_tag(packet_name, vlan_id, vlan_priority, vlan_tpid)

            if self.add_to_dict:
                self.pkt_dict.add_packet(packet_name, self.packet)

            self._keyword_cleanup()

            return self.packet
        else:
            self.logger.log_info("!!! Unable to create a packet with type " + packet_type + " !!!")
            self.logger.log_info("!!! Verify the specified packet type exists in the PacketTypeConstants file !!!")
            return False

    def create_packet_with_hex(self, packet_name, *hex_string, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name the packet will be stored with.
        [hex_string] - The hex string of the packet bytes. Can be formatted in any of the following ways.
                       "0x123456789ABCDEF", "123456789ABCDEF", or "01 23 45 67 89 AB CD EF". The
                       string is not case sensitive.
        [length] - The length of the packet. Must be passed as a named arg length=<length>.

        Creates a packet based of a string of hex characters.
        """
        _hex = "".join(hex_string)

        formatted_hex = _hex.lower().replace("0x", "").replace(" ", "")
        self.packet = self.pkt_classifier.classify_packet_bytes(formatted_hex)

        if "length" in kwargs:
            length = kwargs["length"]
        else:
            length = None

        if length is not None:
            self.packet.set_length(str(length))
            self.packet.user_set_length = True

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def clone_packet(self, packet_name, clone_packet_name, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The source packet to copy.
        [clone_packet_name] - The name the collection copy should be given.

        Clones an existing packet collection to a new collection.
        """
        self._init_keyword(packet_name, **kwargs)

        new_packet = pc.copy.deepcopy(self.packet)
        new_packet.cloned_packet = True
        self.pkt_dict.add_collection(clone_packet_name, new_packet)

        return self.packet

    def set_length(self, packet_name, length, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name the packet should be stored under. This name will be used
                        to retrieve the packet later.
        [length] - The length of the packet.

        Set's the given packets length.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.AbstractPacket):
            self.packet.set_length(length)
            self.packet.user_set_length = True
        else:
            self.logger.log_error("Packet " + packet_name + " does not exist, create it first.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_ethernet(self, packet_name, dmac=None, smac=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name of the packet
        [dmac]        - The Destination MAC address
        [smac]        - The Source MAC address

        Sets the Ethernet header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.EthernetPacketHeader):
            self.pkt_def.add_packet_info(self.packet.set_destination_mac, self.packet.get_destination_mac, dmac,
                                         self.pkt_defaults.DESTINATION_MAC)
            self.pkt_def.add_packet_info(self.packet.set_source_mac, self.packet.get_source_mac, smac,
                                         self.pkt_defaults.SOURCE_MAC)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an Ethernet2 header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_ethernet2(self, packet_name, dmac=None, smac=None, ether_type=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name of the packet
        [dmac]        - The Destination MAC address
        [smac]        - The Source MAC address
        [ether_type]  - The EtherType field

        Sets the Ethernet2 header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.Ethernet2PacketHeader):
            if isinstance(self.packet, pc.LldpPacketHeader):
                self.pkt_def.add_packet_info(self.packet.set_destination_mac, self.packet.get_destination_mac,
                                             self.pkt_defaults.LLDP_DEST_MAC, self.pkt_defaults.LLDP_DEST_MAC)
            else:
                self.pkt_def.add_packet_info(self.packet.set_destination_mac, self.packet.get_destination_mac, dmac,
                                             self.pkt_defaults.DESTINATION_MAC)
            self.pkt_def.add_packet_info(self.packet.set_source_mac, self.packet.get_source_mac, smac,
                                         self.pkt_defaults.SOURCE_MAC)
            self.pkt_def.add_packet_info(self.packet.set_ether_type, self.packet.get_ether_type, ether_type,
                                         self.pkt_defaults.ETHER_TYPE)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an Ethernet2 header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_vlan_tag(self, packet_name, vlan_id=None, vlan_priority=None, vlan_tpid=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name]   - The name of the packet
        [vlan_id]       - The value for the VLAN ID
        [vlan_priority] - The value for the VLAN Priority
        [vlan_tpid]     - The Tag Protocol ID for the VLAN header

        Sets the VLAN header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.TaggedPacketHeader):
            self.pkt_def.add_packet_info(self.packet.set_vlan_id, self.packet.get_vlan_id, vlan_id,
                                         self.pkt_defaults.VLAN_ID)
            self.pkt_def.add_packet_info(self.packet.set_vlan_tci, self.packet.get_vlan_tci, vlan_priority,
                                         self.pkt_defaults.VLAN_PRIORITY)
            self.pkt_def.add_packet_info(self.packet.set_vlan_protocol_id, self.packet.get_vlan_protocol_id, vlan_tpid,
                                         self.pkt_defaults.VLAN_TPID)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain a VLAN header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_sap(self, packet_name, dmac=None, smac=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name of the packet
        [dmac]        - The Destination MAC address
        [smac]        - The Source MAC address

        Sets the SAP header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.SapPacketHeader):
            self.pkt_def.add_packet_info(self.packet.set_destination_mac, self.packet.get_destination_mac, dmac,
                                         self.pkt_defaults.DESTINATION_MAC)
            self.pkt_def.add_packet_info(self.packet.set_source_mac, self.packet.get_source_mac, smac,
                                         self.pkt_defaults.SOURCE_MAC)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain a SAP header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_vlan_stack_tag(self, packet_name, vlan_id_list=None, vlan_priority_list=None, vlan_tpid_list=None,
                           **kwargs):
        """
        Keyword Arguments:
        [packet_name]        - The name of the packet
        [vlan_id_list]       - A list of values for the VLAN ID
        [vlan_priority_list] - A list of values for the VLAN Priority
        [vlan_tpid_list]     - A list of Tag Protocol IDs for the VLAN header

        Sets the Q-in-Q VLAN header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.VlanStackPacketHeader):
            vlan_stack_ids = ListUtils.convert_to_list(vlan_id_list)
            vlan_stack_pris = ListUtils.convert_to_list(vlan_priority_list)
            vlan_stack_tpids = ListUtils.convert_to_list(vlan_tpid_list)

            self.packet.num_tags = max(len(vlan_stack_ids) if vlan_stack_ids is not None else 0,
                                       len(vlan_stack_pris) if vlan_stack_pris is not None else 0,
                                       len(vlan_stack_tpids) if vlan_stack_tpids is not None else 0)

            for i in range(self.packet.num_tags):
                if vlan_stack_ids is not None:
                    vlan_id = vlan_stack_ids[i] if len(vlan_stack_ids) > i else self.pkt_defaults.VLAN_ID
                else:
                    vlan_id = None
                if vlan_stack_pris is not None:
                    vlan_pri = vlan_stack_pris[i] if len(vlan_stack_pris) > i else self.pkt_defaults.VLAN_PRIORITY
                else:
                    vlan_pri = None
                if vlan_stack_tpids is not None:
                    vlan_tpid = vlan_stack_tpids[i] if len(vlan_stack_tpids) > i else self.pkt_defaults.VLAN_TPID
                else:
                    vlan_tpid = None

                self.pkt_def.add_packet_info(self.packet.set_vlan_id, self.packet.get_vlan_id,
                                             vlan_id, self.pkt_defaults.VLAN_ID, [i + 1], [i + 1])
                self.pkt_def.add_packet_info(self.packet.set_vlan_tci, self.packet.get_vlan_tci,
                                             vlan_pri, self.pkt_defaults.VLAN_PRIORITY, [i + 1], [i + 1])
                self.pkt_def.add_packet_info(self.packet.set_vlan_protocol_id, self.packet.get_vlan_protocol_id,
                                             vlan_tpid, self.pkt_defaults.VLAN_TPID, [i + 1], [i + 1])

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain a VLAN stack header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_arp(self, packet_name, hardware_type=None, proto_type=None, hardware_size=None, proto_size=None,
                op_code=None, sender_hardware_address=None, sender_protocol_address=None,
                target_hardware_address=None, target_protocol_address=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name]             - The name of the packet
        [hardware_type]           - The sender's network link type
        [proto_type]              - The ARP protocol EtherType
        [hardware_size]           - The hardware address length
        [proto_size]              - The protocol address length
        [op_code]                 - The ARP operation type (request or reply)
        [sender_hardware_address] - The sender's source MAC address
        [sender_protocol_address] - The sender's IPv4 address
        [target_hardware_address] - The target's MAC address
        [target_protocol_address] - The target's IPv4 address

        Sets the ARP header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.ArpPacketHeader):
            self.pkt_def.add_packet_info(self.packet.set_ether_type, self.packet.get_ether_type,
                                         self.pkt_defaults.ARP_ETHER_PROTO, self.pkt_defaults.ARP_ETHER_PROTO)
            self.pkt_def.add_packet_info(self.packet.set_arp_proto, self.packet.get_arp_proto, proto_type,
                                         self.pkt_defaults.ARP_PROTO_TYPE)
            self.pkt_def.add_packet_info(self.packet.set_arp_id, self.packet.get_arp_id, hardware_size,
                                         self.pkt_defaults.ARP_HARDWARE_SIZE)
            self.pkt_def.add_packet_info(self.packet.set_arp_seq, self.packet.get_arp_seq, proto_size,
                                         self.pkt_defaults.ARP_PROTO_SIZE)
            self.pkt_def.add_packet_info(self.packet.set_arp_operation, self.packet.get_arp_operation, op_code,
                                         self.pkt_defaults.ARP_OPERATION)
            self.pkt_def.add_packet_info(self.packet.set_arp_hardware, self.packet.get_arp_hardware, hardware_type,
                                         self.pkt_defaults.ARP_HARDWARE_SIZE)
            self.pkt_def.add_packet_info(self.packet.set_arp_sender_hardware_address,
                                         self.packet.get_arp_sender_hardware_address, sender_hardware_address,
                                         self.pkt_defaults.ARP_SENDER_HARDWARE_ADDRESS)
            self.pkt_def.add_packet_info(self.packet.set_arp_source_protocol_address,
                                         self.packet.get_arp_source_protocol_address, sender_protocol_address,
                                         self.pkt_defaults.ARP_SOURCE_PROTOCOL_ADDRESS)
            self.pkt_def.add_packet_info(self.packet.set_arp_target_hardware_address,
                                         self.packet.get_arp_target_hardware_address, target_hardware_address,
                                         self.pkt_defaults.ARP_TARGET_HARDWARE_ADDRESS)
            self.pkt_def.add_packet_info(self.packet.set_arp_target_protocol_address,
                                         self.packet.get_arp_target_protocol_address, target_protocol_address,
                                         self.pkt_defaults.ARP_TARGET_PROTOCOL_ADDRESS)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an ARP header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_ipv4(self, packet_name, dip=None, sip=None, ip_hdr_len=None, ip_ttl=None, ip_proto=None, ip_tos=None,
                 ip_total_len=None, ip_id=None, ip_flags=None, ip_frag_offset=None, ip_chksum=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name]    - The name of the packet
        [dip]            - The value for the Destination IP
        [sip]            - The value for the Source IP
        [ip_hdr_len]     - The IPv4 Header length
        [ip_ttl]         - The IPv4 TTL
        [ip_proto]       - The IPv4 Protocol ID for the following header
        [ip_tos]         - The IPv4 ToS
        [ip_total_len]   - The IPv4 Total packet length field
        [ip_id]          - The IPv4 packet ID
        [ip_flags]       - The IPv4 flags field
        [ip_frag_offset] - The offset, for fragmented packets
        [ip_chksum]      - The IPv4 Header checksum (Leave blank for auto-calculation)

        Sets the IPv4 header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.IpV4PacketHeader):
            if ip_hdr_len is not None:
                self.pkt_def.add_packet_info(self.packet.set_ip_hdr_length, self.packet.get_ip_hdr_length, ip_hdr_len,
                                             None)
            if ip_total_len is not None:
                self.pkt_def.add_packet_info(self.packet.set_ip_length, self.packet.get_ip_length, ip_total_len,
                                             None)
            if ip_chksum is not None:
                self.pkt_def.add_packet_info(self.packet.set_ip_checksum, self.packet.get_ip_checksum, ip_chksum,
                                             None)
            if isinstance(self.packet, pc.SnapPacketHeader):
                self.pkt_def.add_packet_info(self.packet.set_snap_ether_type, self.packet.get_snap_ether_type,
                                             self.pkt_defaults.ETHER_TYPE_IP, None)
            else:
                self.pkt_def.add_packet_info(self.packet.set_ether_type, self.packet.get_ether_type,
                                             self.pkt_defaults.ETHER_TYPE_IP, None)
            self.pkt_def.add_packet_info(self.packet.set_destination_ip, self.packet.get_destination_ip, dip,
                                         self.pkt_defaults.IP_DIP)
            self.pkt_def.add_packet_info(self.packet.set_source_ip, self.packet.get_source_ip, sip,
                                         self.pkt_defaults.IP_SIP)
            self.pkt_def.add_packet_info(self.packet.set_ip_ttl, self.packet.get_ip_ttl, ip_ttl,
                                         self.pkt_defaults.IP_TTL)
            self.pkt_def.add_packet_info(self.packet.set_ip_protocol, self.packet.get_ip_protocol, ip_proto,
                                         self.pkt_defaults.IP_PROTOCOL)
            self.pkt_def.add_packet_info(self.packet.set_ip_tos, self.packet.get_ip_tos, ip_tos,
                                         self.pkt_defaults.IP_TOS)
            self.pkt_def.add_packet_info(self.packet.set_ip_id, self.packet.get_ip_id, ip_id,
                                         self.pkt_defaults.IP_ID)
            self.pkt_def.add_packet_info(self.packet.set_ip_flags, self.packet.get_ip_flags, ip_flags,
                                         self.pkt_defaults.IP_FLAGS)
            self.pkt_def.add_packet_info(self.packet.set_ip_fragment_offset, self.packet.get_ip_fragment_offset,
                                         ip_frag_offset, self.pkt_defaults.IP_FRAG_OFFSET)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet " + packet_name + " does not contain an IPv4 header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_ipv6(self, packet_name, dip=None, sip=None, ipv6_traffic_class=None, ipv6_next_header=None,
                 ipv6_hop_limit=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name]        - The name of the packet
        [dip]                - The value for the Destination IPv6 Address
        [sip]                - The value for the Source IPv6 Address
        [ipv6_traffic_class] - The IPv6 Traffic Class
        [ipv6_next_header]   - The IPv6 Next Header
        [ipv6_hop_limit]     - The IPv6 Hop Limit

        Sets the IPv6 header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.IpV6PacketHeader):
            if isinstance(self.packet, pc.SnapPacketHeader):
                self.pkt_def.add_packet_info(self.packet.set_snap_ether_type, self.packet.get_snap_ether_type,
                                             self.pkt_defaults.ETHER_TYPE_IPV6, None)
            else:
                self.pkt_def.add_packet_info(self.packet.set_ether_type, self.packet.get_ether_type,
                                             self.pkt_defaults.ETHER_TYPE_IPV6, None)
            self.pkt_def.add_packet_info(self.packet.set_ipv6_destination_address,
                                         self.packet.get_ipv6_destination_address, dip, self.pkt_defaults.IPV6_DIP)
            self.pkt_def.add_packet_info(self.packet.set_ipv6_source_address, self.packet.get_ipv6_source_address,
                                         sip, self.pkt_defaults.IPV6_SIP)
            self.pkt_def.add_packet_info(self.packet.set_ipv6_traffic_class, self.packet.get_ipv6_traffic_class,
                                         ipv6_traffic_class, self.pkt_defaults.IPV6_TRAFFIC_CLASS)
            self.pkt_def.add_packet_info(self.packet.set_ipv6_next_header, self.packet.get_ipv6_next_header,
                                         ipv6_next_header, self.pkt_defaults.IPV6_NEXT_HEADER)
            self.pkt_def.add_packet_info(self.packet.set_ipv6_hop_limit, self.packet.get_ipv6_hop_limit,
                                         ipv6_hop_limit, self.pkt_defaults.IPV6_HOP_LIMIT)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an IPv6 header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_udp(self, packet_name, src_port=None, dst_port=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name of the packet
        [src_port]   - The UDP source port
        [dst_port]   - The UDP destination port

        Sets the UDP header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.UdpPacketHeader):
            if self.packet.is_ipv4():
                self.pkt_def.add_packet_info(self.packet.set_ip_protocol, self.packet.get_ip_protocol,
                                             self.pkt_defaults.IP_PROTOCOL_UDP, None)
            elif self.packet.is_ipv6():
                self.pkt_def.add_packet_info(self.packet.set_ipv6_next_header, self.packet.get_ipv6_next_header,
                                             self.pkt_defaults.IPV6_NEXT_HEADER_UDP, None)

            self.pkt_def.add_packet_info(self.packet.set_source_port, self.packet.get_source_port, src_port,
                                         self.pkt_defaults.UDP_SRC_PORT)
            self.pkt_def.add_packet_info(self.packet.set_destination_port, self.packet.get_destination_port, dst_port,
                                         self.pkt_defaults.UDP_DST_PORT)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain a UDP header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_tcp(self, packet_name, src_port=None, dst_port=None, seq_num=None, ack_num=None, window=None,
                ns_flag="0", cwr_flag="0", ece_flag="0", urg_flag="0", ack_flag="0", psh_flag="0",
                rst_flag="0", syn_flag="0", fin_flag="0", **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name of the packet
        [src_port]    - The TCP source port
        [dst_port]    - The TCP destination port
        [seq_num]     - The TCP sequence number
        [ack_num]     - The TCP sequence number expected for a TCP ACK
        [window]      - The receive window size
        [ns_flag]     - The concealment protection flag
        [cwr_flag]    - The congestion window reduced flag
        [ece_flag]    - The ECN-Echo flag
        [urg_flag]    - The urgent pointer field flag
        [ack_flag]    - The acknowledgement flag
        [psh_flag]    - The push function flag
        [rst_flag]    - The reset flag
        [syn_flag]    - The synchronize flag
        [fin_flag]    - The last packet flag

        Sets the TCP header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.TcpPacketHeader):
            valid_flags = ["1", 1, "True", "true", True]

            flags = "".join(["1" if ns_flag in valid_flags else "0",
                             "1" if cwr_flag in valid_flags else "0",
                             "1" if ece_flag in valid_flags else "0",
                             "1" if urg_flag in valid_flags else "0",
                             "1" if ack_flag in valid_flags else "0",
                             "1" if psh_flag in valid_flags else "0",
                             "1" if rst_flag in valid_flags else "0",
                             "1" if syn_flag in valid_flags else "0",
                             "1" if fin_flag in valid_flags else "0"])

            if self.packet.is_ipv4():
                self.pkt_def.add_packet_info(self.packet.set_ip_protocol, self.packet.get_ip_protocol,
                                             self.pkt_defaults.IP_PROTOCOL_TCP, None)
            elif self.packet.is_ipv6():
                self.pkt_def.add_packet_info(self.packet.set_ipv6_next_header, self.packet.get_ipv6_next_header,
                                             self.pkt_defaults.IPV6_NEXT_HEADER_TCP, None)
            self.pkt_def.add_packet_info(self.packet.set_source_port, self.packet.get_source_port, src_port,
                                         self.pkt_defaults.TCP_SRC_PORT)
            self.pkt_def.add_packet_info(self.packet.set_destination_port, self.packet.get_destination_port, dst_port,
                                         self.pkt_defaults.TCP_DST_PORT)
            self.pkt_def.add_packet_info(self.packet.set_sequence_number, self.packet.get_sequence_number, seq_num,
                                         self.pkt_defaults.TCP_SEQ_NUM)
            self.pkt_def.add_packet_info(self.packet.set_acknowledgement_number, self.packet.get_acknowledgement_number,
                                         ack_num, self.pkt_defaults.TCP_ACK_NUM)
            self.pkt_def.add_packet_info(self.packet.set_window, self.packet.get_window, window,
                                         self.pkt_defaults.TCP_WINDOW)
            self.pkt_def.add_packet_info(self.packet.set_flags, self.packet.get_flags, "".join(flags),
                                         self.pkt_defaults.TCP_FLAGS)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain a TCP header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_icmp(self, packet_name, icmp_type=None, code=None, icmp_id=None, seq=None, checksum=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The packet name
        [icmp_type]   - The ICMP type
        [code]        - The ICMP code
        [icmp_id]     - The ICMP packet ID
        [seq]         - The ICMP sequence number
        [checksum]    - The ICMP header checksum

        Sets the ICMP header fields in the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.IcmpPacketHeader):
            self.pkt_def.add_packet_info(self.packet.set_ip_protocol, self.packet.get_ip_protocol,
                                         self.pkt_defaults.IP_PROTOCOL_ICMP, self.pkt_defaults.IP_PROTOCOL_ICMP)
            self.pkt_def.add_packet_info(self.packet.set_icmp_type, self.packet.get_icmp_type, icmp_type,
                                         self.pkt_defaults.ICMP_TYPE)
            self.pkt_def.add_packet_info(self.packet.set_icmp_code, self.packet.get_icmp_code, code,
                                         self.pkt_defaults.ICMP_CODE)
            self.pkt_def.add_packet_info(self.packet.set_icmp_id, self.packet.get_icmp_id, icmp_id,
                                         self.pkt_defaults.ICMP_ID)
            self.pkt_def.add_packet_info(self.packet.set_icmp_seq, self.packet.get_icmp_seq, seq,
                                         self.pkt_defaults.ICMP_SEQ)

            if checksum is not None:
                self.pkt_def.add_packet_info(self.packet.set_icmp_checksum, self.packet.get_icmp_checksum, checksum,
                                             None)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an ICMP header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_icmpv6(self, packet_name, icmp_type=None, code=None, icmp_id=None, seq=None, checksum=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The packet name
        [icmp_type]   - The ICMPv6 type
        [code]        - The ICMPv6 code
        [icmp_id]     - The ICMPv6 packet ID
        [seq]         - The ICMPv6 sequence number
        [checksum]    - The ICMPv6 header checksum

        Sets the ICMPv6 header fields in the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.IcmpPacketHeader):
            self.pkt_def.add_packet_info(self.packet.set_ipv6_next_header, self.packet.get_ipv6_next_header,
                                         self.pkt_defaults.IPV6_NEXT_HEADER_ICMP, None)
            self.pkt_def.add_packet_info(self.packet.set_icmp_type, self.packet.get_icmp_type, icmp_type,
                                         self.pkt_defaults.ICMP_TYPE)
            self.pkt_def.add_packet_info(self.packet.set_icmp_code, self.packet.get_icmp_code, code,
                                         self.pkt_defaults.ICMP_CODE)
            self.pkt_def.add_packet_info(self.packet.set_icmp_id, self.packet.get_icmp_id, icmp_id,
                                         self.pkt_defaults.ICMP_ID)
            self.pkt_def.add_packet_info(self.packet.set_icmp_seq, self.packet.get_icmp_seq, seq,
                                         self.pkt_defaults.ICMP_SEQ)

            if checksum is not None:
                self.pkt_def.add_packet_info(self.packet.set_icmp_checksum, self.packet.get_icmp_checksum, checksum,
                                             None)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an ICMPv6 header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_igmp(self, packet_name, igmp_type=None, group_address=None, max_response_time=None, checksum=None,
                 **kwargs):
        """
        Keyword Arguments:
        [packet_name]       - The packet name
        [igmp_type]         - The IGMP type                   Example:  "0x11"
        [group_address]     - The IGMP group address          Example:  "224.0.0.1"
        [max_response_time] - The IGMP max response time      Example:  "100"
        [checksum]          - The IGMP header checksum

        Sets the IGMP header fields in the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.IgmpPacketHeader):
            self.pkt_def.add_packet_info(self.packet.set_ip_protocol, self.packet.get_ip_protocol,
                                         self.pkt_defaults.IP_PROTOCOL_IGMP, self.pkt_defaults.IP_PROTOCOL_IGMP)
            self.pkt_def.add_packet_info(self.packet.set_igmp_type, self.packet.get_igmp_type, igmp_type,
                                         self.pkt_defaults.IGMP_TYPE)
            self.pkt_def.add_packet_info(self.packet.set_igmp_groupaddress, self.packet.get_igmp_groupaddress,
                                         group_address, self.pkt_defaults.GROUP_ADDRESS)
            self.pkt_def.add_packet_info(self.packet.set_igmp_maxresptime, self.packet.get_igmp_maxresptime,
                                         max_response_time, self.pkt_defaults.MAX_RESP_TIME)

            if checksum is not None:
                self.pkt_def.add_packet_info(self.packet.set_igmp_checksum, self.packet.get_igmp_checksum, checksum,
                                             None)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an IGMP header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_ipv6_fragment(self, packet_name, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name of the packet

        Adds the IPv6 fragment header to the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.IpV6PacketHeader):
            self.packet.add_ipv6_extension_headers_fragment()

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an IPv6 header to add a "
                                                              "Fragment header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_bpdu_header(self, packet_name, protocol_id=None, version=None, message_type=None, flags=None,
                        root_prio=None, root_mac=None, cost=None, bridge_prio=None, bridge_mac=None, port_id=None,
                        age=None, max_age=None, hello_time=None, forward_delay=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name]   - The name of the packet
        [protocol_id]   - The spanning tree protocol ID
        [version]       - The spanning tree version
        [message_type]  - The spanning tree message type
        [flags]         - The spanning tree flags field
        [root_prio]     - The Root bridge priority
        [root_mac]      - The Root bridge MAC address
        [cost]          - The Root path cost
        [bridge_prio]   - The Designated bridge priority
        [bridge_mac]    - The Designated bridge MAC address
        [port_id]       - The sender's port ID
        [age]           - The BPDU current age
        [max_age]       - The spanning tree max age
        [hello_time]    - The spanning tree hello interval
        [forward_delay] - The spanning tree forward delay

        Sets the Spanning Tree BPDU header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.BpduPacketHeader):
            if isinstance(self.packet, pc.RstpPacketHeader):
                conf_version = [version, self.pkt_defaults.RSTP_VERSION]
                conf_message_type = [message_type, self.pkt_defaults.RSTP_MESSAGE_TYPE]
                conf_flags = [flags, self.pkt_defaults.RSTP_FLAGS]
            elif isinstance(self.packet, pc.MstpPacketHeader):
                conf_version = [version, self.pkt_defaults.MSTP_VERSION]
                conf_message_type = [message_type, self.pkt_defaults.MSTP_MESSAGE_TYPE]
                conf_flags = [flags, self.pkt_defaults.MSTP_FLAGS]
            else:
                conf_version = [version, self.pkt_defaults.STP_VERSION]
                conf_message_type = [message_type, self.pkt_defaults.STP_MESSAGE_TYPE]
                conf_flags = [flags, self.pkt_defaults.STP_FLAGS]

            self.pkt_def.add_packet_info(self.packet.set_bpdu_protocol_id, self.packet.get_bpdu_protocol_id,
                                         protocol_id, self.pkt_defaults.STP_PROTOCOL_ID)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_version, self.packet.get_bpdu_version,
                                         *conf_version)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_message_type, self.packet.get_bpdu_message_type,
                                         *conf_message_type)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_flags, self.packet.get_bpdu_flags,
                                         *conf_flags)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_root_priority, self.packet.get_bpdu_root_priority,
                                         root_prio, self.pkt_defaults.STP_ROOT_PRIO)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_root_mac, self.packet.get_bpdu_root_mac,
                                         root_mac, self.pkt_defaults.STP_ROOT_MAC)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_cost, self.packet.get_bpdu_cost,
                                         cost, self.pkt_defaults.STP_COST)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_bridge_priority, self.packet.get_bpdu_bridge_priority,
                                         bridge_prio, self.pkt_defaults.STP_BRIDGE_PRIO)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_bridge_mac, self.packet.get_bpdu_bridge_mac,
                                         bridge_mac, self.pkt_defaults.STP_BRIDGE_MAC)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_port_id, self.packet.get_bpdu_port_id,
                                         port_id, self.pkt_defaults.STP_PORT_ID)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_age, self.packet.get_bpdu_age,
                                         age, self.pkt_defaults.STP_AGE)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_max_age, self.packet.get_bpdu_max_age,
                                         max_age, self.pkt_defaults.STP_MAX_AGE)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_hello_timer, self.packet.get_bpdu_hello_timer,
                                         hello_time, self.pkt_defaults.STP_HELLO_TIME)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_forward_delay, self.packet.get_bpdu_forward_delay,
                                         forward_delay, self.pkt_defaults.STP_FORWARD_DELAY)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet " + packet_name + " does not contain a BPDU header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_tcn_bpdu(self, packet_name, protocol_id=None, version=None, message_type=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name]  - The name of the packet
        [protocol_id]  - The spanning tree protocol ID
        [version]      - The spanning tree version
        [message_type] - The spanning tree message type

        Sets the Spanning Tree TCN BPDU header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.BpduPacketHeader):
            if not self.packet.user_set_length:
                self.packet.set_length(43)
                self.packet.user_set_length = True

            self.pkt_def.add_packet_info(self.packet.set_bpdu_protocol_id, self.packet.get_bpdu_protocol_id,
                                         protocol_id, self.pkt_defaults.STP_PROTOCOL_ID)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_version, self.packet.get_bpdu_version,
                                         version, self.pkt_defaults.STP_VERSION)
            self.pkt_def.add_packet_info(self.packet.set_bpdu_message_type, self.packet.get_bpdu_message_type,
                                         message_type, self.pkt_defaults.STP_MESSAGE_TYPE)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet " + packet_name + " does not contain a BPDU header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_mstp_bpdu_cist_header(self, packet_name, ver1_length=None, ver3_length=None, msti_name=None,
                                  msti_digest=None, cist_bridge_prio=None, cist_bridge_mac=None, cist_path_cost=None,
                                  cist_hops=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name]      - The name of the packet
        [ver1_length]      - The version 1 length
        [ver3_length]      - The version 3 length
        [msti_name]        - The MST region name
        [msti_digest]      - The MST configuration digest
        [cist_bridge_prio] - The CIST Root bridge priority
        [cist_bridge_mac]  - The CIST Root bridge MAC address
        [cist_path_cost]   - The CIST external path cost
        [cist_hops]        - The current hop count (message age)

        Sets the MST BPDU header CIST fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.MstpPacketHeader):
            self.pkt_def.add_packet_info(self.packet.set_mstp_version_1_length, self.packet.get_mstp_version_1_length,
                                         ver1_length, self.pkt_defaults.VER1_LENGTH)
            self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_length, self.packet.get_mstp_version_3_length,
                                         ver3_length, self.pkt_defaults.VER3_LENGTH)
            self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_name, self.packet.get_mstp_version_3_name,
                                         msti_name, self.pkt_defaults.MSTI_NAME)
            self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_digest, self.packet.get_mstp_version_3_digest,
                                         msti_digest, self.pkt_defaults.MSTI_DIGEST)
            self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_cist_bridge_internal_priority,
                                         self.packet.get_mstp_version_3_cist_bridge_internal_priority,
                                         cist_bridge_prio, self.pkt_defaults.STP_BRIDGE_PRIO)
            self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_cist_bridge_internal_system_id,
                                         self.packet.get_mstp_version_3_cist_bridge_internal_system_id,
                                         cist_bridge_mac, self.pkt_defaults.STP_BRIDGE_MAC)
            self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_cist_internal_root_path_cost,
                                         self.packet.get_mstp_version_3_cist_internal_root_path_cost,
                                         cist_path_cost, self.pkt_defaults.STP_COST)
            self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_cist_remaining_hops,
                                         self.packet.get_mstp_version_3_cist_remaining_hops,
                                         cist_hops, self.pkt_defaults.CIST_HOPS)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet " + packet_name + " does not contain an MSTP BPDU header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_msti_bpdu_extensions(self, packet_name, msti_list, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name of the packet
        [msti_list]   - A list of MST IDs

        Sets the MST BPDU header additional MST ID fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.MstpPacketHeader):
            for index, msti in enumerate(msti_list):
                sid = index + 1
                msti_flags = msti["msti_flags"] if "msti_flags" in msti else None
                msti_root_prio = msti["msti_root_prio"] if "msti_root_prio" in msti else None
                msti_id = msti["msti_id"] if "msti_id" in msti else None
                msti_root = msti["msti_root"] if "msti_root" in msti else None
                msti_path_cost = msti["msti_path_cost"] if "msti_path_cost" in msti else None
                msti_bridge_prio = msti["msti_bridge_prio"] if "msti_bridge_prio" in msti else None
                msti_port_prio = msti["msti_port_prio"] if "msti_port_prio" in msti else None
                msti_hops = msti["msti_hops"] if "msti_hops" in msti else None

                self.packet.add_mstid_entry()

                self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_mstid_flags,
                                             self.packet.get_mstp_version_3_mstid_flags,
                                             msti_flags, self.pkt_defaults.MSTP_FLAGS, [sid])
                self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_mstid_priority,
                                             self.packet.get_mstp_version_3_mstid_priority,
                                             msti_root_prio, self.pkt_defaults.MSTI_ROOT_PRIO, [sid])
                self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_mstid_mstid,
                                             self.packet.get_mstp_version_3_mstid_mstid,
                                             msti_id, self.pkt_defaults.MSTI_ID, [sid])
                self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_mstid_regional_root,
                                             self.packet.get_mstp_version_3_mstid_regional_root,
                                             msti_root, self.pkt_defaults.STP_ROOT_MAC, [sid])
                self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_mstid_internal_root_path_cost,
                                             self.packet.get_mstp_version_3_mstid_internal_root_path_cost,
                                             msti_path_cost, self.pkt_defaults.MSTI_PATH_COST, [sid])
                self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_mstid_bridge_identifier_priority,
                                             self.packet.get_mstp_version_3_mstid_bridge_identifier_priority,
                                             msti_bridge_prio, self.pkt_defaults.MSTI_BRIDGE_PRIO, [sid])
                self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_mstid_port_identifier_priority,
                                             self.packet.get_mstp_version_3_mstid_port_identifier_priority,
                                             msti_port_prio, self.pkt_defaults.MSTI_PORT_PRIO, [sid])
                self.pkt_def.add_packet_info(self.packet.set_mstp_version_3_mstid_remaining_hops,
                                             self.packet.get_mstp_version_3_mstid_remaining_hops,
                                             msti_hops, self.pkt_defaults.MSTI_HOPS, [sid])
                self._configure_packet()
                self.pkt_def.clear_packet_info()

            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an MSTP BPDU header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def add_lldp_tlv(self, packet_name, type_name, value=None, type_id=None, length=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name] - The name of the packet the TLV should be added to.
        [type_name]   - The type of TLV to add. Valid types are as follows.
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
        [value]       - The TLV's value.
        [type_id]     - If a custom TLV is added, the value the type field should be set to.
        [length]      - If a custom TLV is added, the value the length field should be set to.

        Adds the TLV to the LLDP packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.LldpPacketHeader):
            norm_type_name = type_name.lower().replace("_", "").replace(" ", "")

            if norm_type_name.lower() == "capabilities":
                self.packet.add_lldp_tlv_capabilities(value)
            elif norm_type_name.lower() == "chassissubtype":
                self.packet.add_lldp_tlv_chassis_subtype(value)
            elif norm_type_name.lower() == "portsubtype":
                self.packet.add_lldp_tlv_port_subtype(value)
            elif norm_type_name.lower() == "portdescription":
                self.packet.add_lldp_tlv_port_description(value)
            elif norm_type_name.lower() == "systemname":
                self.packet.add_lldp_tlv_system_name(value)
            elif norm_type_name.lower() == "systemdescription":
                self.packet.add_lldp_tlv_system_description(value)
            elif norm_type_name.lower() == "portvlan":
                self.packet.add_lldp_tlv_ieee_802_1_portvlan(value)
            elif norm_type_name.lower() == "macphy":
                self.packet.add_lldp_tlv_ieee_802_3_mc_phy_config(value)
            elif norm_type_name.lower() == "timetolive":
                self.packet.add_lldp_tlv_time_to_live(value)
            elif norm_type_name.lower() == "end":
                self.packet.add_lldp_tlv_end()
            elif norm_type_name.lower() == "custom":
                index = self.packet.add_lldp_entry(type_id)
                self.packet.set_lldp_tlv_length(length, index)
                self.packet.set_lldp_tlv_message(value, index)
            else:
                self.logger.log_error("Unknown TLV type! Use a known TLV type or 'custom'.")
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain an LLDP header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_vxlan(self, packet_name, inner_packet_name, flags, group_id, vni, **kwargs):
        """
        Keyword Arguments:
        [packet_name]       - The name of the packet
        [inner_packet_name] - The name of the packet to encapsulate
        [flags]             - The VXLAN flags field
        [group_id]          - The VXLAN group ID
        [vni]               - The VXLAN network identifier

        Sets the VXLAN header fields in the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.VxlanPacketHeader):
            if self.packet.cloned_packet:
                inner_packet = self.packet.get_vxlan_inner_packet()
            else:
                inner_packet = self.pkt_dict.get_packet(inner_packet_name)

            self.pkt_def.add_packet_info(self.packet.set_vxlan_inner_packet, self.packet.get_vxlan_inner_packet,
                                         inner_packet, None)
            self.pkt_def.add_packet_info(self.packet.set_vxlan_flags, self.packet.get_vxlan_flags,
                                         flags, self.pkt_defaults.VXLAN_FLAGS)
            self.pkt_def.add_packet_info(self.packet.set_vxlan_group_policy_id, self.packet.get_vxlan_group_policy_id,
                                         group_id, self.pkt_defaults.VXLAN_GROUP_ID)
            self.pkt_def.add_packet_info(self.packet.set_vxlan_vxlan_network_identifier,
                                         self.packet.get_vxlan_vxlan_network_identifier,
                                         vni, self.pkt_defaults.VXLAN_VNI)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet " + packet_name + " does not contain a VXLAN header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_gre(self, packet_name, inner_packet_name, protocol, checksum_bit=None, checksum=None, routing_bit=None,
                routing=None, key_bit=None, key=None, sequence_bit=None, sequence=None, src_route_bit=None,
                recursion_control=None, version=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name]       - The name of the packet
        [inner_packet_name] - The name of the packet to encapsulate
        [protocol]          - The ethertype of the encapsulated packet
        [checksum_bit]      - The checksum flag
        [checksum]          - The checksum value, if the flag is set
        [routing_bit]       - The routing flag
        [routing]           - The routing information, if the flag is set
        [key_bit]           - The key value flag
        [key]               - The application specific key value
        [sequence_bit]      - The sequence number flag
        [sequence]          - The sequence number, if the flag is set
        [src_route_bit]     - The source route flag
        [recursion_control] - The GRE recursion control
        [version]           - The GRE version number

        Sets the GRE header fields in the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.GrePacketHeader):
            if self.packet.cloned_packet:
                inner_packet = self.packet.get_gre_inner_packet()
            else:
                inner_packet = self.pkt_dict.get_packet(inner_packet_name)

            self.pkt_def.add_packet_info(self.packet.set_gre_inner_packet, self.packet.get_gre_inner_packet,
                                         inner_packet, None)
            self.pkt_def.add_packet_info(self.packet.set_gre_protocol_type, self.packet.get_gre_protocol_type,
                                         protocol, self.pkt_defaults.GRE_PROTOCOL_TYPE)
            self.pkt_def.add_packet_info(self.packet.set_gre_flag_checksum_present,
                                         self.packet.get_gre_flag_checksum_present,
                                         checksum_bit, self.pkt_defaults.GRE_CHECKSUM_BIT)
            self.pkt_def.add_packet_info(self.packet.set_gre_flag_routing_present,
                                         self.packet.get_gre_flag_routing_present,
                                         routing_bit, self.pkt_defaults.GRE_ROUTING_BIT)
            self.pkt_def.add_packet_info(self.packet.set_gre_flag_key_present,
                                         self.packet.get_gre_flag_key_present,
                                         key_bit, self.pkt_defaults.GRE_KEY_BIT)
            self.pkt_def.add_packet_info(self.packet.set_gre_flag_sequence_number_present,
                                         self.packet.get_gre_flag_sequence_number_present,
                                         sequence_bit, self.pkt_defaults.GRE_SEQUENCE_BIT)
            self.pkt_def.add_packet_info(self.packet.set_gre_flag_strict_source_route,
                                         self.packet.get_gre_flag_strict_source_route,
                                         src_route_bit, self.pkt_defaults.GRE_SOURCE_ROUTE_BIT)
            self.pkt_def.add_packet_info(self.packet.set_gre_flag_recursion_control_information,
                                         self.packet.get_gre_flag_recursion_control_information,
                                         recursion_control, self.pkt_defaults.GRE_RECURSION_CTRL)
            self.pkt_def.add_packet_info(self.packet.set_gre_flag_version_number,
                                         self.packet.get_gre_flag_version_number,
                                         version, self.pkt_defaults.GRE_VERSION)

            if checksum_bit is None:
                self.pkt_def.add_packet_info(self.packet.set_gre_checksum, self.packet.get_gre_checksum,
                                             checksum, self.pkt_defaults.GRE_CHECKSUM)
            if routing_bit is None:
                self.pkt_def.add_packet_info(self.packet.set_gre_routing, self.packet.get_gre_routing,
                                             routing, self.pkt_defaults.GRE_ROUTING)
            if key_bit is None:
                self.pkt_def.add_packet_info(self.packet.set_gre_key, self.packet.get_gre_key,
                                             key, self.pkt_defaults.GRE_KEY)
            if sequence_bit is None:
                self.pkt_def.add_packet_info(self.packet.set_gre_sequence, self.packet.get_gre_sequence,
                                             sequence, self.pkt_defaults.GRE_SEQUENCE)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet " + packet_name + " does not contain a GRE header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    def set_pim(self, packet_name, pim_version, pim_type, options=None, **kwargs):
        """
        Keyword Arguments:
        [packet_name]   - The name of the packet
        [pim_version]     - The IGMP packet type
        [grp_address]   - The multicast group address
        [max_resp_time] - The maximum time to wait for a response

        Sets the IGMP header fields for the packet.
        """
        self._init_keyword(packet_name, **kwargs)

        if isinstance(self.packet, pc.PimPacketHeader):
            if self.packet.is_ipv4():
                self.pkt_def.add_packet_info(self.packet.set_ip_protocol, self.packet.get_ip_protocol,
                                             self.pkt_defaults.IP_PROTOCOL_PIM, None)
            elif self.packet.is_ipv6():
                self.pkt_def.add_packet_info(self.packet.set_ipv6_next_header, self.packet.get_ipv6_next_header,
                                             self.pkt_defaults.IPV6_NEXT_HEADER_PIM, None)
            self.pkt_def.add_packet_info(self.packet.set_pim_version, self.packet.get_pim_version, pim_version,
                                         self.pkt_defaults.PIM_VERSION)
            self.pkt_def.add_packet_info(self.packet.set_pim_length, self.packet.get_pim_length, pim_type,
                                         self.pkt_defaults.PIM_TYPE)
            self.pkt_def.add_packet_info(self.packet.set_pim_options, self.packet.get_pim_options,
                                         options, None)

            self._configure_packet()
            self._validate_packet_length()
        else:
            self.logger.log_error("Packet + " + packet_name + " does not contain a PIM header.")

        if self.add_to_dict:
            self.pkt_dict.add_packet(packet_name, self.packet)

        self._keyword_cleanup()

        return self.packet

    @staticmethod
    def __get_packet_types(constants_obj):
        types = list()

        type_keys = [attr for attr in dir(constants_obj) if attr.find("__") == -1]

        for key in type_keys:
            types.append(getattr(constants_obj, key))

        return types

    def _configure_packet(self):
        for pkt_info in self.pkt_def.packet_info:
            val = (self._get_value(pkt_info.get_func, pkt_info.val, pkt_info.default_val, pkt_info.get_args)
                   if self.packet.cloned_packet else pkt_info.val)
            self._set_packet_attr(pkt_info.set_func, val, pkt_info.default_val, pkt_info.set_args)

    @staticmethod
    def _set_packet_attr(set_function, value, default_value, set_args):
        if len(set_args) == 0:
            set_function(value if value is not None else default_value,
                         ignore_check=True if value is None else False)
        else:
            args = [i for i in set_args] + [value if value is not None else default_value]
            kwargs = {"ignore_check": True if value is None else False}
            set_function(*args, **kwargs)

    @staticmethod
    def _get_value(get_function, value, default_value, get_args):
        if value is None:
            if len(get_args) == 0:
                if get_function() != default_value:
                    return get_function()
            else:
                if get_function(get_args) != default_value:
                    return get_function(*get_args)
        return value
    
    def get_packet(self, packet_name):
        if packet_name in self.pkt_dict.packet_dictionary:
            return self.pkt_dict.get_packet(packet_name)
        else:
            return None
