from ExtremeAutomation.Keywords.TrafficKeywords.TrafficCaptureKeywords import TrafficCaptureKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficGeneratorConnectionManager import TrafficGeneratorConnectionManager
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketCreationKeywords import TrafficPacketCreationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketInspectionKeywords import TrafficPacketInspectionKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStatisticsKeywords import TrafficStatisticsKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficTransmitKeywords import TrafficTransmitKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStreamConfigurationKeywords import TrafficStreamConfigurationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.EzTrafficValidation.TrafficValidationKeywords import TrafficValidationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.Constants.PacketTypeConstants import PacketTypeConstants
import time


class TrafficGenerationUdks():
    def __init__(self):
        self.trafficCaptureKeywords = TrafficCaptureKeywords()
        self.trafficGeneratorConnectionManager = TrafficGeneratorConnectionManager()
        self.trafficPacketCreationKeywords = TrafficPacketCreationKeywords()
        self.trafficPacketInspectionKeywords = TrafficPacketInspectionKeywords()
        self.trafficStatisticsKeywords = TrafficStatisticsKeywords()
        self.trafficStreamConfigurationKeywords = TrafficStreamConfigurationKeywords()
        self.trafficValidationKeywords = TrafficValidationKeywords()
        self.trafficTransmitKeywords = TrafficTransmitKeywords()
        self.packetTypeConstants = PacketTypeConstants()

    # Packet_Creation_Keywords

    def Create_Ethernet2_Packet(self, packet_name, dmac=None, smac=None, vlan_id=None,
                                vlan_prio=None, vlan_tpid=None, ether_type=None,
                                packet_len=None, **kwargs):

        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_PACKET, vlan_id, vlan_prio,  vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac, smac, ether_type, **kwargs)

    def Create_Ethernet2_VLAN_Stack_Packet(self,  packet_name, dmac=None, smac=None, vlan_ids=None,
                                           vlan_prio_list=None, vlan_tpid_list=None, ether_type=None,
                                           packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_VLAN_STACK_PACKET, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_vlan_stack_tag(packet_name, vlan_ids, vlan_prio_list, vlan_tpid_list, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac, smac, ether_type, **kwargs)

    def Create_ARP_Packet(self,  packet_name, dmac=None,            smac=None,              vlan_id=None,
                          vlan_prio=None,       vlan_tpid=None,         hardware_type=None,
                          proto_type=None,      hardware_size=None,     proto_size=None,
                          op_code=None,         sender_hardware=None,   sender_proto=None,
                          target_hardware=None, target_proto=None,      packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_ARP_PACKET, vlan_id, vlan_prio, vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac, smac, **kwargs)
        self.trafficPacketCreationKeywords.set_arp(packet_name, hardware_type,   proto_type,   hardware_size,   proto_size,
                                                   op_code, sender_hardware, sender_proto, target_hardware, target_proto, **kwargs)

    def Create_IPv4_Packet(self, packet_name, dmac=None,       smac=None,          vlan_id=None,
                           vlan_prio=None,  vlan_tpid=None,     dip=None,
                           sip=None,        header_len=None,    ttl=None,
                           proto=None,      tos=None,           total_len=None,
                           id=None,         flags=None,         frag_offset=None,
                           checksum=None,   packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV4_PACKET,   vlan_id,    vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,      smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip, sip, header_len, ttl, proto, 
                                                    tos, total_len, id, flags, frag_offset, checksum, **kwargs)

    def Create_IPv4_ICMP_Packet(self,  packet_name, dmac=None,       smac=None,          vlan_id=None,
                                vlan_prio=None,  vlan_tpid=None,     dip=None,
                                sip=None,        header_len=None,    ttl=None,
                                proto=None,      tos=None,           total_len=None,
                                id=None,         flags=None,         frag_offset=None,
                                icmp_type=None,  code=None,          icmp_id=None,
                                icmp_seq=None,   icmp_checksum=None, checksum=None,
                                packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV4_ICMP_PACKET, vlan_id,    vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,      smac,  **kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip,       sip,     header_len, ttl,         proto,
                                                    tos,         total_len, id,      flags,      frag_offset, checksum, **kwargs)
        self.trafficPacketCreationKeywords.set_icmp(packet_name, icmp_type, code,    icmp_id,    icmp_seq,    icmp_checksum,  **kwargs)

    def Create_IPv4_UDP_Packet(self, packet_name, dmac=None,       smac=None,          vlan_id=None,
                               vlan_prio=None,  vlan_tpid=None,     dip=None,
                               sip=None,        src_port=None,      dst_port=None,
                               header_len=None, ttl=None,           proto=None,
                               tos=None,        total_len=None,     id=None,
                               flags=None,      frag_offset=None,   checksum=None,
                               packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV4_UDP_PACKET,   vlan_id,    vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,      smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip, sip, header_len, ttl, proto,
                                                    tos, total_len, id, flags, frag_offset, checksum, **kwargs)
        self.trafficPacketCreationKeywords.set_udp(packet_name, src_port,  dst_port, **kwargs)

    def Create_IPv4_TCP_Packet(self, packet_name, dmac=None,       smac=None,          vlan_id=None,
                               vlan_prio=None,  vlan_tpid=None,     dip=None,
                               sip=None,        src_port=None,      dst_port=None,
                               header_len=None, ttl=None,           proto=None,
                               tos=None,        total_len=None,     id=None,
                               flags=None,      frag_offset=None,   checksum=None,
                               seq_num=None,    ack_num=None,       window=None,
                               ns_flag=0,          cwr_flag=0,            ece_flag=0,
                               urg_flag=0,         ack_flag=0,            psh_flag=0,
                               rst_flag=0,        syn_flag=0,            fin_flag=0,
                               packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV4_TCP_PACKET,   vlan_id,    vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,      smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip,       sip,      header_len, ttl,         proto,
                                                    tos,         total_len, id,       flags,      frag_offset, checksum, **kwargs)
        self.trafficPacketCreationKeywords.set_tcp(packet_name, src_port,  dst_port, seq_num,    ack_num,     window,
                                                   ns_flag,     cwr_flag,  ece_flag, urg_flag,   ack_flag,    psh_flag, 
                                                   rst_flag,    syn_flag,  fin_flag, **kwargs)

    def Create_IPv4_SNAP_Packet(self, packet_name, dmac=None,       smac=None,          vlan_id=None,
                                vlan_prio=None,  vlan_tpid=None,     dip=None,
                                sip=None,        src_port=None,      dst_port=None,
                                header_len=None, ttl=None,           proto=None,
                                tos=None,        total_len=None,     id=None,
                                flags=None,      frag_offset=None,   checksum=None,
                                packet_len=None, **kwargs):       
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH_SNAP_IPV4_PACKET,   vlan_id,    vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet(packet_name, dmac,      smac, *kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip,       sip,      header_len, ttl,         proto,
                                                    tos,         total_len, id,       flags,      frag_offset, checksum, *kwargs)

    def Create_Ethernet2_Over_IPv4_VXLAN_Packet(self, packet_name, inner_packet,        dmac=None,          smac=None,
                                                vlan_id=None,     vlan_prio=None,     vlan_tpid=None,
                                                dip=None,         sip=None,           header_len=None,
                                                ttl=None,         proto=None,         tos=None,
                                                total_len=None,   id=None,            flags=None,
                                                frag_offset=None, checksum=None,      src_port=None,
                                                dst_port=None,    vxlan_flags=None,   group_id=None,
                                                vni=None,         packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_VXLAN_UDP_IPV4_PACKET,   vlan_id,    
                                                         vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,         smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip,          sip,         header_len, ttl,         proto,
                                                    tos,         total_len,    id,          flags,      frag_offset, checksum, **kwargs)
        self.trafficPacketCreationKeywords.set_udp(packet_name, src_port,     dst_port, **kwargs)
        self.trafficPacketCreationKeywords.set_vxlan(packet_name, inner_packet, vxlan_flags, group_id,   vni, **kwargs)

    def Create_Ethernet2_Over_IPv4_L2TB_Packet(self, packet_name, inner_packet,        protocol,              dmac=None,
                                               smac=None,        vlan_id=None,       vlan_prio=None,
                                               vlan_tpid=None,   dip=None,           sip=None,
                                               header_len=None,  ttl=None,           proto=None,
                                               tos=None,         total_len=None,     id=None,
                                               flags=None,       frag_offset=None,   ip_checksum=None,
                                               packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_GRE_IPV4_PACKET,     vlan_id,      vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,         smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip,          sip,         header_len,   ttl,         proto,
                                                    tos,         total_len,    id,          flags,        frag_offset, ip_checksum, **kwargs)
        self.trafficPacketCreationKeywords.set_gre(packet_name, inner_packet, protocol, **kwargs)

    def Create_IPv6_Packet(self,  packet_name, dmac=None,       smac=None,          vlan_id=None,
                           vlan_prio=None,  vlan_tpid=None,     dip=None,
                           sip=None,        traffic_class=None, next_header=None,
                           hop_limit=None,  packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_PACKET, vlan_id, vlan_prio, vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac, smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip, sip, traffic_class, next_header, hop_limit, **kwargs)

    def Create_IPv6_ICMP_Packet(self, packet_name, dmac=None,       smac=None,          vlan_id=None,
                                vlan_prio=None,  vlan_tpid=None,     dip=None,
                                sip=None,        traffic_class=None, next_header=None,
                                hop_limit=None,  packet_len=None,    icmp_type=None,
                                code=None,       icmp_id=None,       icmp_seq=None,
                                icmp_checksum=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_ICMP_PACKET,    vlan_id, vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,      smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip,       sip,  traffic_class, next_header, hop_limit, **kwargs)
        self.trafficPacketCreationKeywords.set_icmpv6(packet_name, icmp_type, code, icmp_id,       icmp_seq,    icmp_checksum, **kwargs)

    def Create_IPv6_UDP_Packet(self, packet_name, dmac=None,          smac=None,          vlan_id=None,
                               vlan_prio=None,     vlan_tpid=None,     dip=None,
                               sip=None,           src_port=None,      dst_port=None,
                               traffic_class=None, next_header=None,   hop_limit=None,
                               packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_UDP_PACKET, vlan_id,       vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,      smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip,       sip,    traffic_class, next_header, hop_limit, **kwargs)
        self.trafficPacketCreationKeywords.set_udp(packet_name, src_port,  dst_port, **kwargs)

    def Create_IPv6_TCP_Packet(self, packet_name, dmac=None,          smac=None,          vlan_id=None,
                               vlan_prio=None,     vlan_tpid=None,     dip=None,
                               sip=None,           src_port=None,      dst_port=None,
                               traffic_class=None, next_header=None,   hop_limit=None,
                               seq_num=None,       ack_num=None,       window=None,
                               ns_flag=0,             cwr_flag=0,            ece_flag=0,
                               urg_flag=0,            ack_flag=0,            psh_flag=0,
                               rst_flag=0,            syn_flag=0,            fin_flag=0,
                               packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_TCP_PACKET,    vlan_id,       vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,      smac, **kwargs)
        self.trafficPacketCreationKeywords.Set_IPv6(packet_name, dip,       sip,       traffic_class, next_header, hop_limit, **kwargs)
        self.trafficPacketCreationKeywords.Set_TCP(packet_name, src_port,  dst_port,  seq_num,       ack_num,     window,
                                                   ns_flag,     cwr_flag,  ece_flag,  urg_flag,      ack_flag,    psh_flag,
                                                   rst_flag,    syn_flag,  fin_flag, **kwargs)

    def Create_IPv6_Fragment_Packet(self, packet_name, dmac=None,       smac=None,          vlan_id=None,
                                    vlan_prio=None,  vlan_tpid=None,     dip=None,
                                    sip=None,        traffic_class=None, next_header=None,
                                    hop_limit=None,  packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_PACKET, vlan_id,       vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,    smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip,      sip, traffic_class, next_header, hop_limit, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6_fragment(packet_name, **kwargs)

    def Create_IPv6_SNAP_Packet(self, packet_name, dmac=None,          smac=None,          vlan_id=None,
                                vlan_prio=None,     vlan_tpid=None,     dip=None,
                                sip=None,           src_port=None,      dst_port=None,
                                traffic_class=None, next_header=None,   hop_limit=None,
                                packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH_SNAP_IPV6_PACKET, vlan_id,      vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet(packet_name, dmac, smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip, sip,  traffic_class, next_header, hop_limit, **kwargs)

    def Create_Ethernet2_Over_IPv6_VXLAN_Packet(self, packet_name, dmac=None,          smac=None,          vlan_id=None,
                                                vlan_prio=None,     vlan_tpid=None,     dip=None,
                                                sip=None,           src_port=None,      dst_port=None,
                                                traffic_class=None, next_header=None,   hop_limit=None,
                                                vxlan_flags=None,   group_id=None,      vni=None,
                                                packet_len=None,    inner_packet=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_UDP_PACKET, vlan_id, vlan_prio,   vlan_tpid, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac, smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip,  sip, traffic_class,   next_header, hop_limit, **kwargs)
        self.trafficPacketCreationKeywords.set_udp(packet_name, src_port,     dst_port, **kwargs)
        self.trafficPacketCreationKeywords.set_vxlan(packet_name, inner_packet, vxlan_flags,     group_id,    vni, **kwargs)

    def Create_IPv4_Vlan_Stack_Packet(self, packet_name, dmac=None,           smac=None,          vlan_ids=None,
                                      vlan_prio_list=None, vlan_tpid_list=None,     dip=None,
                                      sip=None,            header_len=None,    ttl=None,
                                      proto=None,          tos=None,           total_len=None,
                                      id=None,             flags=None,         frag_offset=None,
                                      checksum=None,       packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV4_VLAN_STACK_PACKET, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_vlan_stack_tag(packet_name, vlan_ids, vlan_prio_list, vlan_tpid_list, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac, smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip, sip, header_len, ttl, proto, tos, total_len, id, flags, frag_offset, checksum, **kwargs)

    def Create_IPv4_Vlan_Stack_UDP_Packet(self, packet_name, dmac=None,            smac=None,          vlan_ids=None,
                                          vlan_prio_list=None,  vlan_tpid_list=None,     dip=None,
                                          sip=None,             src_port=None,      dst_port=None,
                                          header_len=None,      ttl=None,           proto=None,
                                          tos=None,             total_len=None,     id=None,
                                          flags=None,           frag_offset=None,   checksum=None,
                                          packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV4_UDP_VLAN_STACK_PACKET,  packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_vlan_stack_tag(packet_name, vlan_ids,  vlan_prio_list,     vlan_tpid_list, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,      smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip, sip, header_len, ttl, proto, tos, total_len, id,  flags, frag_offset, checksum, **kwargs)
        self.trafficPacketCreationKeywords.set_udp(packet_name, src_port,  dst_port, **kwargs)

    def Create_IPv4_Vlan_Stack_TCP_Packet(self, packet_name, dmac=None,            smac=None,          vlan_ids=None,
                                          vlan_prio_list=None,  vlan_tpid_list=None,     dip=None,
                                          sip=None,             src_port=None,      dst_port=None,
                                          header_len=None,      ttl=None,           proto=None,
                                          tos=None,             total_len=None,     id=None,
                                          flags=None,           frag_offset=None,   checksum=None,
                                          seq_num=None,         ack_num=None,       window=None,
                                          ns_flag=0,               cwr_flag=0,            ece_flag=0,
                                          urg_flag=0,              ack_flag=0,            psh_flag=0,
                                          rst_flag=0,              syn_flag=0,            fin_flag=0,
                                          packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV4_TCP_VLAN_STACK_PACKET, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_vlan_stack_tag(packet_name, vlan_ids,  vlan_prio_list,    vlan_tpid_list, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac, smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv4(packet_name, dip, sip, header_len, ttl, proto, tos, total_len, id, flags, frag_offset, checksum, **kwargs)
        self.trafficPacketCreationKeywords.Set_TCP(packet_name, src_port,  dst_port, seq_num, ack_num, window,
                                                   ns_flag, cwr_flag, ece_flag, urg_flag,  ack_flag, psh_flag,
                                                   rst_flag, syn_flag, fin_flag, **kwargs)

    def Create_IPv6_Vlan_Stack_Packet(self, packet_name, dmac=None,            smac=None,          vlan_ids=None,
                                      vlan_prio_list=None,  vlan_tpid_list=None,     dip=None,
                                      sip=None,             traffic_class=None, next_header=None,
                                      hop_limit=None,       packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_VLAN_STACK_PACKET,  packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_vlan_stack_tag(packet_name, vlan_ids,  vlan_prio_list, vlan_tpid_list,  **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac, smac,  **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip,       sip,  traffic_class, next_header, hop_limit,  **kwargs)

    def Create_IPv6_Vlan_Stack_UDP_Packet(self, packet_name, dmac=None,               smac=None,          vlan_ids=None,
                                          vlan_prio_list=None,     vlan_tpid_list=None,     dip=None,
                                          sip=None,                src_port=None,      dst_port=None,
                                          traffic_class=None,      next_header=None,   hop_limit=None,
                                          packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_UDP_VLAN_STACK_PACKET, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_vlan_stack_tag(packet_name, vlan_ids, vlan_prio_list, vlan_tpid_list, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac, smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip, sip, traffic_class, next_header, hop_limit, **kwargs)
        self.trafficPacketCreationKeywords.set_udp(packet_name, src_port,  dst_port, **kwargs)

    def Create_IPv6_Vlan_Stack_TCP_Packet(self, packet_name, dmac=None,               smac=None,          vlan_ids=None,
                                          vlan_prio_list=None,     vlan_tpid_list=None,     dip=None,
                                          sip=None,                src_port=None,      dst_port=None,
                                          traffic_class=None,      next_header=None,   hop_limit=None,
                                          seq_num=None,            ack_num=None,       window=None,
                                          ns_flag=0,                  cwr_flag=0,            ece_flag=0,
                                          urg_flag=0,                 ack_flag=0,            psh_flag=0,
                                          rst_flag=0,                 syn_flag=0,           fin_flag=0,
                                          packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_TCP_VLAN_STACK_PACKET, packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_vlan_stack_tag(packet_name, vlan_ids,  vlan_prio_list,    vlan_tpid_list, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,      smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip,       sip,       traffic_class, next_header, hop_limit, **kwargs)
        self.trafficPacketCreationKeywords.set_tcp(packet_name, src_port,  dst_port,  seq_num,       ack_num,     window,
                                                   ns_flag,     cwr_flag,  ece_flag,  urg_flag,      ack_flag,    psh_flag,
                                                   rst_flag,    syn_flag,  fin_flag, **kwargs)

    def Create_IPv6_Vlan_Stack_Fragment_Packet(self, packet_name, dmac=None,            smac=None,          vlan_ids=None,
                                               vlan_prio_list=None,  vlan_tpid_list=None,     dip=None,
                                               sip=None,             traffic_class=None, next_header=None,
                                               hop_limit=None,       packet_len=None, **kwargs):
        self.trafficPacketCreationKeywords.create_packet(packet_name, self.packetTypeConstants.ETH2_IPV6_VLAN_STACK_PACKET,  packet_len, **kwargs)
        self.trafficPacketCreationKeywords.set_vlan_stack_tag(packet_name, vlan_ids,  vlan_prio_list, vlan_tpid_list, **kwargs)
        self.trafficPacketCreationKeywords.set_ethernet2(packet_name, dmac,  smac, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6(packet_name, dip,   sip,    traffic_class, next_header, hop_limit, **kwargs)
        self.trafficPacketCreationKeywords.set_ipv6_fragment(packet_name, **kwargs)

    ########################################################################################################################
    #   Traffic_Stream_Configuration   #####################################################################################
    ########################################################################################################################
    def Configure_Packet_on_Port_Single_Burst(self, tgen_port, packet_name, stream_number=1, count=100, rate=100, unit='pps', **kwargs):
        self.trafficStreamConfigurationKeywords.remove_all_streams_from_port(tgen_port, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_packet(tgen_port, stream_number, packet_name, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_rate(tgen_port, stream_number, rate, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_unit(tgen_port, stream_number, unit, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_count(tgen_port, stream_number, count, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_mode_single_burst(tgen_port, stream_number, **kwargs)
        self.trafficStreamConfigurationKeywords.add_stream_to_port(tgen_port, stream_number, **kwargs)

    def Configure_Packet_on_Port_Continuous(self, tgen_port, packet_name, stream_number=1, count=100, rate=100, unit='pps', **kwargs):
        self.trafficStreamConfigurationKeywords.remove_all_streams_from_port(tgen_port, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_packet(tgen_port, stream_number, packet_name, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_rate(tgen_port, stream_number, rate, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_unit(tgen_port, stream_number, unit, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_count(tgen_port, stream_number, count, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_mode_continuous(tgen_port, stream_number, **kwargs)
        self.trafficStreamConfigurationKeywords.add_stream_to_port(tgen_port, stream_number, **kwargs)

    def Transmit_Packet_on_Port_Single_Burst(self, tgen_port,   packet_name, stream_number=1, count=100, rate=100, unit='pps', max_wait=60, **kwargs):
        self.trafficStreamConfigurationKeywords.remove_all_streams_from_port(tgen_port, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_packet(tgen_port, stream_number, packet_name, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_rate(tgen_port, stream_number, rate, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_unit(tgen_port, stream_number, unit, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_count(tgen_port, stream_number, count, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_mode_single_burst(tgen_port, stream_number, **kwargs)
        self.trafficStreamConfigurationKeywords.add_stream_to_port(tgen_port, stream_number, **kwargs)
        self.trafficTransmitKeywords.start_transmit_on_port_and_wait(tgen_port, max_wait, **kwargs)

    def Transmit_Packet_on_Port_Continuous(self, tgen_port, packet_name, stream_number=1, count=100, rate=100, unit='pps', **kwargs):
        self.trafficStreamConfigurationKeywords.remove_all_streams_from_port(tgen_port, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_packet(tgen_port, stream_number, packet_name, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_rate(tgen_port, stream_number, rate, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_unit(tgen_port, stream_number, unit, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_count(tgen_port, stream_number, count, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_mode_continuous(tgen_port, stream_number, **kwargs)
        self.trafficStreamConfigurationKeywords.add_stream_to_port(tgen_port, stream_number, **kwargs)
        self.trafficTransmitKeywords.start_transmit_on_port(tgen_port, **kwargs)

    def Stop_Transmit_and_Clear_all_Streams_on_Port(self, tgen_port, **kwargs):
        self.trafficTransmitKeywords.stop_transmit_on_port(tgen_port, **kwargs)
        self.trafficCaptureKeywords.clear_port_stats_and_filters(tgen_port, **kwargs)
        self.trafficStreamConfigurationKeywords.remove_all_streams_from_port(tgen_port, **kwargs)

    def send_stream_with_incrementing_smac(self, tgen_port, packet_name, stream_number=1, count=100, rate=100, unit='pps', sa_count=1, max_wait=120, **kwargs):
        self.trafficStreamConfigurationKeywords.remove_all_streams_from_port(tgen_port, **kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_packet(tgen_port,stream_number,packet_name,**kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_rate(tgen_port,stream_number,rate,**kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_unit(tgen_port,stream_number,unit,**kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_count(tgen_port,stream_number,count,**kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_mac_src_mode_increment(tgen_port,stream_number,sa_count,1,**kwargs)
        self.trafficStreamConfigurationKeywords.configure_stream_mode_single_burst(tgen_port,stream_number,**kwargs)
        self.trafficStreamConfigurationKeywords.add_stream_to_port(tgen_port,stream_number)
        self.trafficTransmitKeywords.start_transmit_on_port_and_wait(tgen_port,max_wait,**kwargs)
    ########################################################################################################################
    #   Traffic_Capture_Configuration   ####################################################################################
    ########################################################################################################################
    def Start_Capture(self, tgen_port, **kwargs):
        self.trafficCaptureKeywords.start_capture_on_port(tgen_port, **kwargs)
        self.trafficCaptureKeywords.clear_port_statistics(tgen_port, **kwargs)

    def Start_Capture_with_DMAC_Filter(self, tgen_port, dmac, mask=None, **kwargs):
        self.trafficCaptureKeywords.configure_capture_da1(tgen_port, dmac, mask, **kwargs)
        self.trafficCaptureKeywords.start_capture_on_port(tgen_port, **kwargs)
        self.trafficCaptureKeywords.clear_port_statistics(tgen_port, **kwargs)

    def Start_Capture_with_SMAC_Filter(self, tgen_port, smac, mask=None, **kwargs):
        self.trafficCaptureKeywords.configure_capture_sa1(tgen_port, smac, mask, **kwargs)
        self.trafficCaptureKeywords.start_capture_on_port(tgen_port, **kwargs)
        self.trafficCaptureKeywords.clear_port_statistics(tgen_port, **kwargs)

    def Start_Capture_with_DMAC_and_SMAC_Filter(self, tgen_port, dmac, smac, dmac_mask=None, smac_mask=None, **kwargs):
        self.trafficCaptureKeywords.configure_capture_da1(tgen_port, dmac, dmac_mask, **kwargs)
        self.trafficCaptureKeywords.configure_capture_sa1(tgen_port, smac, smac_mask, **kwargs)
        self.trafficCaptureKeywords.start_capture_on_port(tgen_port, **kwargs)
        self.trafficCaptureKeywords.clear_port_statistics(tgen_port, **kwargs)

    ########################################################################################################################
    #   Traffic_Verification_Keywords   ####################################################################################
    ########################################################################################################################
    def Transmit_Traffic_Unidirectionally_and_Verify_it_was_Received(self, tx_port, rx_port, tx_packet, rx_packet, tx_count=100, **kwargs):
        self.Configure_Packet_on_Port_Single_Burst(tx_port, tx_packet,  count=tx_count, **kwargs)
        tx_packet_a = self.trafficPacketCreationKeywords.get_packet(tx_packet)
        rx_packet_a = self.trafficPacketCreationKeywords.get_packet(rx_packet)
        if tx_packet_a and rx_packet_a:
            self.Start_Capture_with_DMAC_and_SMAC_Filter(tx_port, 
                                                         rx_packet_a.get_destination_mac(), 
                                                         rx_packet_a.get_source_mac(), 
                                                         rx_packet_a.get_destination_mac_mask(),
                                                         rx_packet_a.get_source_mac_mask())
            self.trafficTransmitKeywords.start_transmit_on_port_and_wait(tx_port, **kwargs)
            self.trafficStatisticsKeywords.get_captured_count(rx_port, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_equal(rx_port, tx_count, **kwargs)
            self.trafficStatisticsKeywords.get_tx_count(tx_port, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_equal(tx_port, tx_count, **kwargs)
            self.trafficPacketInspectionKeywords.capture_inspection_random_list(rx_port, rx_packet,  5, **kwargs)
        else:
            print("You must define the packets to use this keyword")

    def Prime_Traffic_Bidirectionally(self, port_a, port_b, tx_packet_a, tx_packet_b, tx_count=5,  tx_rate=5, **kwargs):
        self.Configure_Packet_on_Port_Single_Burst(port_a, tx_packet_a,  count=tx_count,  rate=tx_rate, **kwargs)
        self.Configure_Packet_on_Port_Single_Burst(port_b, tx_packet_b,  count=tx_count,  rate=tx_rate, **kwargs)
        self.trafficCaptureKeywords.clear_port_statistics(port_a, **kwargs)
        self.trafficCaptureKeywords.clear_port_statistics(port_b, **kwargs)
        self.trafficTransmitKeywords.start_transmit_on_port(port_a, **kwargs)
        self.trafficTransmitKeywords.start_transmit_on_port_and_wait(port_b, **kwargs)
        self.trafficStatisticsKeywords.get_tx_count(port_a, **kwargs)
        self.trafficStatisticsKeywords.stat_value_should_be_equal(port_a, tx_count, **kwargs)
        self.trafficStatisticsKeywords.get_tx_count(port_b, **kwargs)
        self.trafficStatisticsKeywords.stat_value_should_be_equal(port_b, tx_count, **kwargs)

    def Transmit_Traffic_Bidirectionally_and_Verify_it_was_Received(self, port_a, port_b, tx_packet_name_a, tx_packet_name_b, rx_packet_name_a, rx_packet_name_b,
                                                                    tx_count=100, tx_rate=100, **kwargs):
        self.Configure_Packet_on_Port_Single_Burst(port_a, tx_packet_name_a,  count=tx_count,  rate=tx_rate, **kwargs)
        self.Configure_Packet_on_Port_Single_Burst(port_b, tx_packet_name_b,  count=tx_count,  rate=tx_rate, **kwargs)
        rx_packet_a = self.trafficPacketCreationKeywords.get_packet(rx_packet_name_a)
        rx_packet_b = self.trafficPacketCreationKeywords.get_packet(rx_packet_name_b)
        if rx_packet_a and rx_packet_b:
            self.Start_Capture_with_DMAC_and_SMAC_Filter(port_a, 
                                                         rx_packet_a.get_destination_mac(), 
                                                         rx_packet_a.get_source_mac(), 
                                                         rx_packet_a.get_destination_mac_mask(),
                                                         rx_packet_a.get_source_mac_mask())
            self.Start_Capture_with_DMAC_and_SMAC_Filter(port_b, 
                                                         rx_packet_b.get_destination_mac(), 
                                                         rx_packet_b.get_source_mac(), 
                                                         rx_packet_b.get_destination_mac_mask(),
                                                         rx_packet_b.get_source_mac_mask())
            self.trafficTransmitKeywords.start_transmit_on_port(port_a, **kwargs)
            self.trafficTransmitKeywords.start_transmit_on_port_and_wait(port_b, **kwargs)
            self.trafficStatisticsKeywords.get_captured_count(port_a, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_equal(port_a, tx_count, **kwargs)
            self.trafficStatisticsKeywords.get_captured_count(port_b, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_equal(port_b, tx_count, **kwargs)
            self.trafficStatisticsKeywords.get_tx_count(port_a, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_equal(port_a, tx_count, **kwargs)
            self.trafficStatisticsKeywords.get_tx_count(port_b, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_equal(port_b, tx_count, **kwargs)
            self.trafficPacketInspectionKeywords.capture_inspection_random_list(port_a, rx_packet_name_a,  5, **kwargs)
            self.trafficPacketInspectionKeywords.capture_inspection_random_list(port_b, rx_packet_name_b,  5, **kwargs)
        else:
            print("You must define the packets to use this keyword")

    def Transmit_Traffic_Bidirectionally_and_Verify_it_was_Received_Routed(self, port_a, port_b, tx_packet_name_a, tx_packet_name_b, rx_packet_name_a, rx_packet_name_b,
                                                                           tx_count=100, tx_rate=100, **kwargs):
        self.Configure_Packet_on_Port_Single_Burst(port_a, tx_packet_name_a,  count=tx_count,  rate=tx_rate, **kwargs)
        self.Configure_Packet_on_Port_Single_Burst(port_b, tx_packet_name_b,  count=tx_count,  rate=tx_rate, **kwargs)
        tx_packet_a = self.trafficPacketCreationKeywords.get_packet(tx_packet_name_a)
        tx_packet_b = self.trafficPacketCreationKeywords.get_packet(tx_packet_name_b)
        if tx_packet_a and tx_packet_b:
            self.Start_Capture_with_DMAC_and_SMAC_Filter(port_a, 
                                                         tx_packet_b.get_destination_mac(), 
                                                         tx_packet_b.get_source_mac(), 
                                                         tx_packet_b.get_destination_mac_mask(),
                                                         tx_packet_b.get_source_mac_mask())
            self.Start_Capture_with_DMAC_and_SMAC_Filter(port_b, 
                                                         tx_packet_a.get_destination_mac(), 
                                                         tx_packet_a.get_source_mac(), 
                                                         tx_packet_a.get_destination_mac_mask(),
                                                         tx_packet_a.get_source_mac_mask())
            self.trafficTransmitKeywords.start_transmit_on_port(port_a, **kwargs)
            self.trafficTransmitKeywords.start_transmit_on_port_and_wait(port_b, **kwargs)
            self.trafficStatisticsKeywords.get_rx_count(port_a, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_greater_than_or_equal(port_a, tx_count, **kwargs)
            self.trafficStatisticsKeywords.get_rx_count(port_b, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_greater_than_or_equal(port_b, tx_count, **kwargs)
            self.trafficStatisticsKeywords.get_tx_count(port_a, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_equal(port_a, tx_count, **kwargs)
            self.trafficStatisticsKeywords.get_tx_count(port_b, **kwargs)
            self.trafficStatisticsKeywords.stat_value_should_be_equal(port_b, tx_count, **kwargs)
            self.trafficPacketInspectionKeywords.capture_inspection_random_list(port_a, rx_packet_name_a,  5, **kwargs)
            self.trafficPacketInspectionKeywords.capture_inspection_random_list(port_b, rx_packet_name_b,  5, **kwargs)
        else:
            print("You must define the packets to use this keyword")


    def send_source_macs_on_port_from_traffic_generator(self, mac_add_list, tgen_port):

        '''
         - This keyword will send a list of source macs on port from traffic generator
        :param mac_add_list: mac_add_list = ['00:00:00:00:00:01', '00:00:00:00:00:02', "..."]
        '''

        packet_a = 'packetA'
        #tgen_port_a = self.tb.createTgenPort(self.tb.tgen1_name, self.tb.tgen_dut1_port_a.ifname)

        for i in range(0, len(mac_add_list)):
            self.Create_Ethernet2_Packet(packet_a, smac=mac_add_list[i])
            self.send_stream_with_incrementing_smac(tgen_port, packet_a, stream_number=1, count=1,
                                                    rate=100, unit='pps', sa_count=1,  max_wait=120)
        #self.Start_Capture(tgen_port)


