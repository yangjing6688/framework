from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import PacketConfigFilterApi, PacketConfigFilterConstants

"""
    This is the API class for the command: packet_config_filter

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaPacketConfigFilterApi(PacketConfigFilterApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaPacketConfigFilterApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_config_filter
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        api.packet_config_filter(dummyDict)
    """
    def packet_config_filter(self, argdictionary):
        return super(IxiaPacketConfigFilterApi, self).packet_config_filter(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_config_filter_DA1(self, mac):
        """
        This is the method the command: packet_config_filter option DA1
        Description:Supported with IxTclHal and IxTclNetwork. Only frames that contain this destination MAC address are filtered, captured or counted.
        Constants Available: DA1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.DA1_CMD : mac})

    def packet_config_filter_DA2(self, mac):
        """
        This is the method the command: packet_config_filter option DA2
        Description:Supported with IxTclHal and IxTclNetwork. Only frames that contain this destination MAC address are filtered, captured or counted.
        Constants Available: DA2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.DA2_CMD : mac})

    def packet_config_filter_DA_mask1(self, mac):
        """
        This is the method the command: packet_config_filter option DA_mask1
        Description:Supported with IxTclHal and IxTclNetwork. A bit mask that allows the user to specify which bits of the DA1 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter.
        Constants Available: DA_MASK1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.DA_MASK1_CMD : mac})

    def packet_config_filter_DA_mask2(self, mac):
        """
        This is the method the command: packet_config_filter option DA_mask2
        Description:Supported with IxTclHal and IxTclNetwork. A bit mask that allows the user to specify which bits of the DA2 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter.
        Constants Available: DA_MASK2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.DA_MASK2_CMD : mac})

    def packet_config_filter_SA1(self, mac):
        """
        This is the method the command: packet_config_filter option SA1
        Description:Supported with IxTclHal and IxTclNetwork. Only frames that contain this destination MAC address are filtered, captured or counted.
        Constants Available: SA1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.SA1_CMD : mac})

    def packet_config_filter_SA2(self, mac):
        """
        This is the method the command: packet_config_filter option SA2
        Description:Supported with IxTclHal and IxTclNetwork. Only frames that contain this destination MAC address are filtered, captured or counted.
        Constants Available: SA2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.SA2_CMD : mac})

    def packet_config_filter_SA_mask1(self, mac):
        """
        This is the method the command: packet_config_filter option SA_mask1
        Description:Supported with IxTclHal and IxTclNetwork. A bit mask that allows the user to specify which bits of the SA1 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter.
        Constants Available: SA_MASK1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.SA_MASK1_CMD : mac})

    def packet_config_filter_SA_mask2(self, mac):
        """
        This is the method the command: packet_config_filter option SA_mask2
        Description:Supported with IxTclHal and IxTclNetwork. A bit mask that allows the user to specify which bits of the SA2 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter.
        Constants Available: SA_MASK2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.SA_MASK2_CMD : mac})

    def packet_config_filter_gfp_bad_fcs_error(self, opt):
        """
        This is the method the command: packet_config_filter option gfp_bad_fcs_error
        Description:Supported with IxTclHal. If true, then GFP bad FCS errors are used in the filter. This condition is OR'd or AND'd with the other GFP errors based on the setting of the gfp_error_condition option.
        Constants Available: GFP_BAD_FCS_ERROR_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.GFP_BAD_FCS_ERROR_CMD : opt})

    def packet_config_filter_gfp_eHec_error(self, opt):
        """
        This is the method the command: packet_config_filter option gfp_eHec_error
        Description:Supported with IxTclHal. If true, then GFP extension header HEC errors are used in the filter. This condition is OR'd or AND'd with the other GFP errors based on the setting of the gfp_error_condition option.
        Constants Available: GFP_EHEC_ERROR_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.GFP_EHEC_ERROR_CMD : opt})

    def packet_config_filter_gfp_error_condition(self, opt):
        """
        This is the method the command: packet_config_filter option gfp_error_condition
        Description:Supported with IxTclHal. Indicates whether the enabled error conditions associated with enableGfptHecError, enableGfpeHecError, enableGfpPayloadCrcError and enableGfpBadFcsError must all be present (AND'd) or only one must be present (OR).
            Valid options are:
            0:(logic OR) - (default) Only one of the enabled error conditions must be present.
            1:(logic AND) - All of the enabled error conditions must be present.
        Constants Available: GFP_ERROR_CONDITION_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.GFP_ERROR_CONDITION_CMD : opt})

    def packet_config_filter_gfp_payload_crc(self, opt):
        """
        This is the method the command: packet_config_filter option gfp_payload_crc
        Description:Supported with IxTclHal. If true, then GFP payload CRC errors are used in the filter. This condition is OR'd or AND'd with the other GFP errors based on the setting of the gfp_error_condition option.
        Constants Available: GFP_PAYLOAD_CRC_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.GFP_PAYLOAD_CRC_CMD : opt})

    def packet_config_filter_gfp_tHec_error(self, opt):
        """
        This is the method the command: packet_config_filter option gfp_tHec_error
        Description:Supported with IxTclHal. If true, then GFP type header HEC errors are used in the filter. This condition is OR'd or AND'd with the other GFP errors based on the setting of the gfp_error_condition option.
        Constants Available: GFP_THEC_ERROR_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.GFP_THEC_ERROR_CMD : opt})

    def packet_config_filter_match_type1(self, opt):
        """
        This is the method the command: packet_config_filter option match_type1
        Description:Supported with IxTclHal and IxTclNetwork. Match type for pattern1 set in class member pattern1.
            Valid options are:
            IpEthernetII: an Ethernet II packet.
            Ip8023Snap: an 802.3 SNAP packet.
            Vlan: a VLAN tagged packet.
            User: (default) a value as specified by pattern1, pattern Mask1 and patternOffset1.
            IpPpp: a PPP format packet
            IpCiscoHdlc: a Cisco HDLC format packet.
            IpSAEthernetII: match the IP Source Address for an Ethernet II packet located at offset 26. pattern will become the source IP address and pattern_mask will become the netmask for the IP address
            IpDAEthernetII: match the IP Destination Address for an Ethernet II packet located at offset 30. pattern will become the destination IP address and pattern_mask will become the netmask for the IP address
            IpSADAEthernetII: match the IP Source and Destination Address for an Ethernet II packet located at offset 26. pattern represents the IP addresses of the source and destination (in this order) and pattern_mask represents the masks of the source and destination IP addresses
            IpSA8023Snap: match the IP Source Address for an 802.3 Snap packet located at offset 34.(same as IpSAEthernetII)
            IpDA8023Snap: match the IP Destination Address for an 802.3 Snap packet located at offset 38. (same as IpDAEthernetII)
            IpSADA8023Snap: match the IP Source and Destination Address for an 802.3 Snap packet located at offset 34. (same as IpSADAEthernetII)
            IpSAPos: match the IP Source Address for an POS packet located at offset 16.(same as IpSAEthernetII)
            IpDAPos: match the IP Destination Address for an POS packet located at offset 20. (same as IpDAEthernetII)
            IpSADAPos: match the IP Source and Destination Addresses for an POS packet located at offset 16. (same as IpSADAEthernetII)
            TcpSourcePortIPEthernetII: match the TCP Source Port for an Ethernet II packet located at offset 34. (pattern represents the source port and the default mask value 00 will always overrides pattern_mask).
            TcpDestPortIPEthernetII: match the TCP Destination Port for an Ethernet II packet located at offset 36. (pattern represents the dest port and the default mask value 00 will always overrides pattern_mask).
            UdpSourcePortIPEthernetII: match the UDP Source Port for an Ethernet II packet located at offset 34.(pattern represents the source port)
            UdpDestPortIPEthernetII: match the UDP Destination Port for an Ethernet II packet located at offset 36. (pattern represents the dest port)
            TcpSourcePortIP8023Snap: match the TCP Source Port for an 802.3 Snap packet located at offset 42. (pattern represents the source port)
            TcpDestPortIP8023Snap: match the TCP Destination Port for an 802.3 Snap packet located at offset 44. (pattern represents the dest port)
            UdpSourcePortIP8023Snap: match the UDP Source Port for an 802.3 Snap packet located at offset 42. (pattern represents the source port)
            UdpDestPortIP8023Snap: match the UDP Destination Port for an 802.3 Snap packet located at offset 44 (pattern represents the dest port)
            TcpSourcePortIPPos: match the TCP Source Port for a POS
            TcpDestPortIPPos: match the TCP Destination Port for a POS packet located at offset 26. (pattern represents the dest port)
            UdpSourcePortIPPos: match the UDP Source Port for a POS packet located at offset 24. (pattern represents the source port)
            UdpDestPortIPPos: match the UDP Source Port for a POS packet located at offset 26. (pattern represents the dest port)
            SrpModeReserved000: match an SRP packet whose mode is reserved 000.
            SrpModeReserved001: match an SRP packet whose mode is reserved 001.
            SrpModeReserved010: match an SRP packet whose mode is reserved 010.
            SrpModeAtmCell011: match an SRP packet whose mode is ATM cell.
            SrpControlMessagePassToHost100: match an SRP packet whose mode is control message 1.
            SrpControlMessageBufferForHost101: match an SRP packet whose mode is control message 2.
            SrpUsageMessage110: match an SRP packet which is an SRP usage message.
            SrpPacketData111: match an SRP packet which is a data packet.
            SrpAllControlMessages10x: match SRP control messages 1 and 2.
            SrpUsageMessageOrPacketData11x: match SRP usage message or data packet.
            SrpControlUsageOrPacketData1xx: match SRP usage message, control message 1 or 2, or data packet.
            SrpInnerRing: match an SRP packet whose ringIdentifier is set to inner.
            SrpOuterRing: match an SRP packet whose ringIdentifier is set to outer.
            SrpPriority0-7: match an SRP packet whose priority is set to 0-7.
            SrpParityOdd: match an SRP packet with odd parity.
            SrpParityEven: match an SRP packet with even parity.
            SrpDiscoveryFrame: match an SRP discovery packet.
            SrpIpsFrame: match an SRP IPS packet.
            RprRingId0: Match any RPR packet which specifies Ringlet 0. Originally transmitted on Ringlet 0 by the Source)
            RprRingId1: Match any RPR packet which specifies Ringlet 1. (Originally transmitted on Ringlet 1 by the Source)
            RprFairnessEligibility0: Match any RPR packet which specifies Fairness Eligibility 0. (0 = Not eligible for Fairness algorithm)
            RprFairnessEligibility1: Match any RPR packet which specifies Fairness Eligibility 1. (0 = Not eligible for Fairness algorithm)
            RprIdlePacket: Match any RPR Idle packet (Type = 00).
            RprControlPacket: Match any RPR Control packet. (Type = 01)
            RprFairnessPacket: Match any RPR Fairness packet. (Type = 10)
            RprDataPacket: Match any RPR Data packet. (Type = 11)
            RprServiceClassC: Match any RPR packet which specifies service Class C.
            RprServiceClassB: Match any RPR packet which specifies service Class B.
            RprServiceClassA1: Match any RPR packet which specifies service Class A1.
            RprServiceClassA0: Match any RPR packet which specifies service Class A0.
            RprWrapEligibility0: Match any RPR packet which specifies Wrap Eligibility 0. (0 = Steerable only)
            RprWrapEligibility1: Match any RPR packet which specifies Wrap Eligibility 1. (1 = Wrap Eligible)
            RprParityBit0: Match any RPR packet which specifies Parity Bit 0.
            RprParityBit1: Match any RPR packet which specifies Parity Bit 1.
            IpV6SAEthernetII: Match the IPv6 Source Address for an Ethernet II packet. (pattern represents the IPv6 source address)
            IpV6DAEthernetII: Match the IPv6 Destination Address for an Ethernet II packet. (pattern represents the IPv6 destination address)
            IpV6SA8023Snap: Match the IPv6 Source Address for an 802.3 packet. (pattern represents the IPv6 source address)
            IpV6DA8023Snap: Match the IPv6 Destination Address for an 802.3 packet. (pattern represents the IPv6 destination address)
            IpV6SAPos: Match the IPv6 Source Address for a POS packet. (pattern represents the IPv6 source address)
            IpV6DAPos: Match the IPv6 Destination Address for a POS packet. (pattern represents the IPv6 destination address)
            Ipv6TcpSourcePortEthernetII: Match the IPv6 TCP source port number for an Ethernet II packet. (pattern represents the source port)
            Ipv6TcpDestPortEthernetII: Match the IPv6 TCP destination port number for an Ethernet II packet. (pattern represents the destination port)
            Ipv6UdpSourcePortEthernetII: Match the IPv6 UDP source port number for an Ethernet II packet. (pattern represents the source port)
            Ipv6UdpDestPortEthernetII: Match the IPv6 UDP destination port number for an Ethernet II packet. (pattern represents the destination port)
            Ipv6TcpSourcePort8023Snap: Match the IPv6 TCP source port number for an 802.3 SNAP packet. (pattern represents the source port)
            Ipv6TcpDestPort8023Snap: Match the IPv6 TCP destination port number for an 802.3 Snap packet. (pattern represents the destination port)
            Ipv6UdpSourcePort8023Snap: Match the IPv6 UDP source port number for an 802.3 Snap packet. (pattern represents the source port)
            Ipv6UdpDestPort8023Snap: Match the IPv6 UDP destination port number for an 802.3 Snap packet. (pattern represents the destination port)
            Ipv6TcpSourcePortPos: Match the IPv6 TCP source port number for an pos packet. (pattern represents the source port)
            Ipv6TcpDestPortPos: Match the IPv6 TCP destination port number for an pos packet. (pattern represents the destination port)
            Ipv6UdpSourcePortPos: Match the IPv6 UDP source port number for an pos packet. (pattern represents the source port)
            Ipv6UdpDestPortPos: Match the IPv6 UDP destination port number for an pos packet. (pattern represents the destination port)
            Ipv6IpTcpSourcePortEthernetII: Match the TCP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an Ethernet II packet. (pattern represents the source port)
            Ipv6IpTcpDestPortEthernetII: Match the TCP destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an Ethernet II packet. (pattern represents the destination port)
            Ipv6IpUdpSourcePortEthernetII: Match the UDP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an Ethernet II packet. (pattern represents the source port)
            Ipv6IpUdpDestPortEthernetII: Match the UPD destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an Ethernet II packet. (pattern represents the destination port)
            Ipv6IpTcpSourcePort8023Snap: Match the TCP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an 802.3 Snap packet. (pattern represents the source port)
            Ipv6IpTcpDestPort8023Snap: Match the TCP destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an 802.3 Snap packet. (pattern represents the destination port)
            Ipv6IpUdpSourcePort8023Snap: Match the UDP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an 802.3 Snap packet. (pattern represents the source port)
            Ipv6IpUdpDestPort8023Snap: Match the UPD destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an 802.3 Snap packet. (pattern represents the destination port)
            Ipv6IpTcpSourcePortPos: Match the TCP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in a POS packet. (pattern represents the source port)
            Ipv6IpTcpDestPortPos: Match the TCP destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in a POS packet. (pattern represents the destination port)
            Ipv6IpUdpSourcePortPos: Match the UDP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in a POS packet. (pattern represents the source port)
            Ipv6IpUdpDestPortPos: Match the UPD destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in a POS packet. (pattern represents the destination port)
            IpOverIpv6IpSAEthernetII: Match the IPv4 source address in an IPv4 frame encapsulated in an IPv6 frame in an Ethernet II packet. (pattern represents the source IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpDAEthernetII: Match the IPv4 destination address in an IPv4 frame encapsulated in an IPv6 frame in an Ethernet II packet. (pattern represents the destination IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpSA8023Snap: Match the IPv4 source address in an IPv4 frame encapsulated in an IPv6 frame in an 802.3 Snap packet. (pattern represents the source IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpDA8023Snap: Match the IPv4 destination address in an IPv4 frame encapsulated in an IPv6 frame in an 802.3 Snap packet. (pattern represents the destination IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpSAPos: Match the IPv4 source address in an IPv4 frame encapsulated in an IPv6 frame in POS packet. (pattern represents the source IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpDAPos: Match the IPv4 destination address in an IPv4 frame encapsulated in an IPv6 frame in POS packet. (pattern represents the destination IP address and pattern_mask will become the netmask for the IP address)
            Ipv6OverIpIpv6SAEthernetII: Match the IPv6 source address in an IPv6 frame encapsulated in an IPv4 frame in an Ethernet II packet. (pattern represents the IPv6 source address)
            Ipv6OverIpIpv6DAEthernetII: Match the IPv6 destination address in an IPv6 frame encapsulated in anIPv4 frame in an Ethernet II packet. (pattern represents the IPv6 destination address)
            Ipv6OverIpIpv6SA8023Snap: Match the IPv6 source address in an IPv6 frame encapsulated in an IPv4 frame in an 802.3 Snap packet. (pattern represents the IPv6 source address)
            Ipv6OverIpIpv6DA8023Snap: Match the IPv6 destination address in an IPv6 frame encapsulated in an IPv4 frame in an 802.3 Snap packet. (pattern represents the IPv6 destination address)
            Ipv6OverIpIpv6SAPos: Match the IPv6 source address in an IPv6 frame encapsulated in an IPv4 frame in POS packet. (pattern represents the IPv6 source address)
            Ipv6OverIpIpv6DAPos: Match the IPv6 destination address in an IPv6 frame encapsulated in an IPv4 frame in POS packet. (pattern represents the IPv6 destination address)
            Ipv6Ppp: Match an IPv6 PPP packet.
            Ipv6CiscoHdlc: Match an IPv6 packet encapsulated with Cisco HDLC.
            GfpDataFcsNullExtEthernet: Match a user data GFP frame which includes an FCS and whose payload uses a null extension and indicates frame-mapped ethernet data.
            GfpDataNoFcsNullExtEthernet: Match a user data GFP frame which does not includes an FCS and whose payload uses a null extension and indicates frame-mapped Ethernet data.
            GfpDataFcsLinearExtEthernet: Match a user data GFP frame which includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped Ethernet data.
            GfpDataNoFcsLinearExtEthernet: Match a user data GFP frame which does not includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped Ethernet data.
            GfpMgmtFcsNullExtEthernet: Match a management GFP frame which includes an FCS and whose payload uses a null extension and indicates frame-mapped Ethernet data.
            GfpMgmtNoFcsNullExtEthernet: Match a management GFP frame which does not includes an FCS and whose payload uses a null extension and indicates frame-mapped Ethernet data.
            GfpMgmtFcsLinearExtEthernet: Match a management GFP frame which includes an FCS and whose payload uses a linear frame extenzion and indicates frame-mapped Ethernet data.
            GfpMgmtNoFcsLinearExtEthernet: Match a management GFP frame which does not includes an FCS and whose payload uses a linear frame extension and indicates framemapped ethernet data.
            GfpDataFcsNullExtPpp: Match a user data GFP frame which includes an FCS and whose payload uses a null extension and indicates frame-mapped PPP data.
            GfpDataNoFcsNullExtPpp: Match a user data GFP frame which does not includes an FCS and whose payload uses a null extension and indicates frame-mapped PPP data.
            GfpDataFcsLinearExtPpp: Match a user data GFP frame which includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped PPP data.
            GfpDataNoFcsLinearExtPpp: Match a user data GFP frame which does not includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped PPP data.
            GfpMgmtFcsNullExtPpp: Match a management GFP frame which includes an FCS and whose payload uses a null extension and indicates frame-mapped PPP data.
            GfpMgmtNoFcsNullExtPpp: Match a management GFP frame which does not includes an FCS and whose payload uses a null extension and indicates frame-mapped PPP data.
            GfpMgmtFcsLinearExtPpp: Match a management GFP frame which includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped PPP data.
            GfpMgmtNoFcsLinearExtPpp: Match a management GFP frame which does not includes an FCS and whose payload uses a linear frame extension and indicates framemapped PPP data.
        Constants Available: MATCH_TYPE1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.MATCH_TYPE1_CMD : opt})

    def packet_config_filter_match_type2(self, opt):
        """
        This is the method the command: packet_config_filter option match_type2
        Description:Supported with IxTclHal and IxTclNetwork. Match type for pattern2 set in class member pattern2.
            Valid options are:
            IpEthernetII: an Ethernet II packet.
            Ip8023Snap: an 802.3 SNAP packet.
            Vlan: a VLAN tagged packet.
            User: (default) a value as specified by pattern1, pattern Mask1 and patternOffset1.
            IpPpp: a PPP format packet
            IpCiscoHdlc: a Cisco HDLC format packet.
            IpSAEthernetII: match the IP Source Address for an Ethernet II packet located at offset 26. pattern will become the source IP address and pattern_mask will become the netmask for the IP address
            IpDAEthernetII: match the IP Destination Address for an Ethernet II packet located at offset 30. pattern will become the destination IP address and pattern_mask will become the netmask for the IP address
            IpSADAEthernetII: match the IP Source and Destination Address for an Ethernet II packet located at offset 26. pattern represents the IP addresses of the source and destination (in this order) and pattern_mask represents the masks of the source and destination IP addresses
            IpSA8023Snap: match the IP Source Address for an 802.3 Snap packet located at offset 34.(same as IpSAEthernetII)
            IpDA8023Snap: match the IP Destination Address for an 802.3 Snap packet located at offset 38. (same as IpDAEthernetII)
            IpSADA8023Snap: match the IP Source and Destination Address for an 802.3 Snap packet located at offset 34. (same as IpSADAEthernetII)
            IpSAPos: match the IP Source Address for an POS packet located at offset 16.(same as IpSAEthernetII)
            IpDAPos: match the IP Destination Address for an POS packet located at offset 20. (same as IpDAEthernetII)
            IpSADAPos: match the IP Source and Destination Addresses for an POS packet located at offset 16. (same as IpSADAEthernetII)
            TcpSourcePortIPEthernetII: match the TCP Source Port for an Ethernet II packet located at offset 34. (pattern represents the source port and the default mask value 00 will always overrides pattern_mask).
            TcpDestPortIPEthernetII: match the TCP Destination Port for an Ethernet II packet located at offset 36. (pattern represents the dest port and the default mask value 00 will always overrides pattern_mask).
            UdpSourcePortIPEthernetII: match the UDP Source Port for an Ethernet II packet located at offset 34.(pattern represents the source port)
            UdpDestPortIPEthernetII: match the UDP Destination Port for an Ethernet II packet located at offset 36. (pattern represents the dest port)
            TcpSourcePortIP8023Snap: match the TCP Source Port for an 802.3 Snap packet located at offset 42. (pattern represents the source port)
            TcpDestPortIP8023Snap: match the TCP Destination Port for an 802.3 Snap packet located at offset 44. (pattern represents the dest port)
            UdpSourcePortIP8023Snap: match the UDP Source Port for an 802.3 Snap packet located at offset 42. (pattern represents the source port)
            UdpDestPortIP8023Snap: match the UDP Destination Port for an 802.3 Snap packet located at offset 44 (pattern represents the dest port)
            TcpSourcePortIPPos: match the TCP Source Port for a POS
            TcpDestPortIPPos: match the TCP Destination Port for a POS packet located at offset 26. (pattern represents the dest port)
            UdpSourcePortIPPos: match the UDP Source Port for a POS packet located at offset 24. (pattern represents the source port)
            UdpDestPortIPPos: match the UDP Source Port for a POS packet located at offset 26. (pattern represents the dest port)
            SrpModeReserved000: match an SRP packet whose mode is reserved 000.
            SrpModeReserved001: match an SRP packet whose mode is reserved 001.
            SrpModeReserved010: match an SRP packet whose mode is reserved 010.
            SrpModeAtmCell011: match an SRP packet whose mode is ATM cell.
            SrpControlMessagePassToHost100: match an SRP packet whose mode is control message 1.
            SrpControlMessageBufferForHost101: match an SRP packet whose mode is control message 2.
            SrpUsageMessage110: match an SRP packet which is an SRP usage message.
            SrpPacketData111: match an SRP packet which is a data packet.
            SrpAllControlMessages10x: match SRP control messages 1 and 2.
            SrpUsageMessageOrPacketData11x: match SRP usage message or data packet.
            SrpControlUsageOrPacketData1xx: match SRP usage message, control message 1 or 2, or data packet.
            SrpInnerRing: match an SRP packet whose ringIdentifier is set to inner.
            SrpOuterRing: match an SRP packet whose ringIdentifier is set to outer.
            SrpPriority0-7: match an SRP packet whose priority is set to 0-7.
            SrpParityOdd: match an SRP packet with odd parity.
            SrpParityEven: match an SRP packet with even parity.
            SrpDiscoveryFrame: match an SRP discovery packet.
            SrpIpsFrame: match an SRP IPS packet.
            RprRingId0: Match any RPR packet which specifies Ringlet 0. Originally transmitted on Ringlet 0 by the Source)
            RprRingId1: Match any RPR packet which specifies Ringlet 1. (Originally transmitted on Ringlet 1 by the Source)
            RprFairnessEligibility0: Match any RPR packet which specifies Fairness Eligibility 0. (0 = Not eligible for Fairness algorithm)
            RprFairnessEligibility1: Match any RPR packet which specifies Fairness Eligibility 1. (0 = Not eligible for Fairness algorithm)
            RprIdlePacket: Match any RPR Idle packet (Type = 00).
            RprControlPacket: Match any RPR Control packet. (Type = 01)
            RprFairnessPacket: Match any RPR Fairness packet. (Type = 10)
            RprDataPacket: Match any RPR Data packet. (Type = 11)
            RprServiceClassC: Match any RPR packet which specifies service Class C.
            RprServiceClassB: Match any RPR packet which specifies service Class B.
            RprServiceClassA1: Match any RPR packet which specifies service Class A1.
            RprServiceClassA0: Match any RPR packet which specifies service Class A0.
            RprWrapEligibility0: Match any RPR packet which specifies Wrap Eligibility 0. (0 = Steerable only)
            RprWrapEligibility1: Match any RPR packet which specifies Wrap Eligibility 1. (1 = Wrap Eligible)
            RprParityBit0: Match any RPR packet which specifies Parity Bit 0.
            RprParityBit1: Match any RPR packet which specifies Parity Bit 1.
            IpV6SAEthernetII: Match the IPv6 Source Address for an Ethernet II packet. (pattern represents the IPv6 source address)
            IpV6DAEthernetII: Match the IPv6 Destination Address for an Ethernet II packet. (pattern represents the IPv6 destination address)
            IpV6SA8023Snap: Match the IPv6 Source Address for an 802.3 packet. (pattern represents the IPv6 source address)
            IpV6DA8023Snap: Match the IPv6 Destination Address for an 802.3 packet. (pattern represents the IPv6 destination address)
            IpV6SAPos: Match the IPv6 Source Address for a POS packet. (pattern represents the IPv6 source address)
            IpV6DAPos: Match the IPv6 Destination Address for a POS packet. (pattern represents the IPv6 destination address)
            Ipv6TcpSourcePortEthernetII: Match the IPv6 TCP source port number for an Ethernet II packet. (pattern represents the source port)
            Ipv6TcpDestPortEthernetII: Match the IPv6 TCP destination port number for an Ethernet II packet. (pattern represents the destination port)
            Ipv6UdpSourcePortEthernetII: Match the IPv6 UDP source port number for an Ethernet II packet. (pattern represents the source port)
            Ipv6UdpDestPortEthernetII: Match the IPv6 UDP destination port number for an Ethernet II packet. (pattern represents the destination port)
            Ipv6TcpSourcePort8023Snap: Match the IPv6 TCP source port number for an 802.3 SNAP packet. (pattern represents the source port)
            Ipv6TcpDestPort8023Snap: Match the IPv6 TCP destination port number for an 802.3 Snap packet. (pattern represents the destination port)
            Ipv6UdpSourcePort8023Snap: Match the IPv6 UDP source port number for an 802.3 Snap packet. (pattern represents the source port)
            Ipv6UdpDestPort8023Snap: Match the IPv6 UDP destination port number for an 802.3 Snap packet. (pattern represents the destination port)
            Ipv6TcpSourcePortPos: Match the IPv6 TCP source port number for an pos packet. (pattern represents the source port)
            Ipv6TcpDestPortPos: Match the IPv6 TCP destination port number for an pos packet. (pattern represents the destination port)
            Ipv6UdpSourcePortPos: Match the IPv6 UDP source port number for an pos packet. (pattern represents the source port)
            Ipv6UdpDestPortPos: Match the IPv6 UDP destination port number for an pos packet. (pattern represents the destination port)
            Ipv6IpTcpSourcePortEthernetII: Match the TCP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an Ethernet II packet. (pattern represents the source port)
            Ipv6IpTcpDestPortEthernetII: Match the TCP destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an Ethernet II packet. (pattern represents the destination port)
            Ipv6IpUdpSourcePortEthernetII: Match the UDP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an Ethernet II packet. (pattern represents the source port)
            Ipv6IpUdpDestPortEthernetII: Match the UPD destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an Ethernet II packet. (pattern represents the destination port)
            Ipv6IpTcpSourcePort8023Snap: Match the TCP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an 802.3 Snap packet. (pattern represents the source port)
            Ipv6IpTcpDestPort8023Snap: Match the TCP destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an 802.3 Snap packet. (pattern represents the destination port)
            Ipv6IpUdpSourcePort8023Snap: Match the UDP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an 802.3 Snap packet. (pattern represents the source port)
            Ipv6IpUdpDestPort8023Snap: Match the UPD destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in an 802.3 Snap packet. (pattern represents the destination port)
            Ipv6IpTcpSourcePortPos: Match the TCP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in a POS packet. (pattern represents the source port)
            Ipv6IpTcpDestPortPos: Match the TCP destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in a POS packet. (pattern represents the destination port)
            Ipv6IpUdpSourcePortPos: Match the UDP source port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in a POS packet. (pattern represents the source port)
            Ipv6IpUdpDestPortPos: Match the UPD destination port number for an IPv4 over IPv6 or IPv6 over IPv4 frame in a POS packet. (pattern represents the destination port)
            IpOverIpv6IpSAEthernetII: Match the IPv4 source address in an IPv4 frame encapsulated in an IPv6 frame in an Ethernet II packet. (pattern represents the source IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpDAEthernetII: Match the IPv4 destination address in an IPv4 frame encapsulated in an IPv6 frame in an Ethernet II packet. (pattern represents the destination IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpSA8023Snap: Match the IPv4 source address in an IPv4 frame encapsulated in an IPv6 frame in an 802.3 Snap packet. (pattern represents the source IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpDA8023Snap: Match the IPv4 destination address in an IPv4 frame encapsulated in an IPv6 frame in an 802.3 Snap packet. (pattern represents the destination IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpSAPos: Match the IPv4 source address in an IPv4 frame encapsulated in an IPv6 frame in POS packet. (pattern represents the source IP address and pattern_mask will become the netmask for the IP address)
            IpOverIpv6IpDAPos: Match the IPv4 destination address in an IPv4 frame encapsulated in an IPv6 frame in POS packet. (pattern represents the destination IP address and pattern_mask will become the netmask for the IP address)
            Ipv6OverIpIpv6SAEthernetII: Match the IPv6 source address in an IPv6 frame encapsulated in an IPv4 frame in an Ethernet II packet. (pattern represents the IPv6 source address)
            Ipv6OverIpIpv6DAEthernetII: Match the IPv6 destination address in an IPv6 frame encapsulated in anIPv4 frame in an Ethernet II packet. (pattern represents the IPv6 destination address)
            Ipv6OverIpIpv6SA8023Snap: Match the IPv6 source address in an IPv6 frame encapsulated in an IPv4 frame in an 802.3 Snap packet. (pattern represents the IPv6 source address)
            Ipv6OverIpIpv6DA8023Snap: Match the IPv6 destination address in an IPv6 frame encapsulated in an IPv4 frame in an 802.3 Snap packet. (pattern represents the IPv6 destination address)
            Ipv6OverIpIpv6SAPos: Match the IPv6 source address in an IPv6 frame encapsulated in an IPv4 frame in POS packet. (pattern represents the IPv6 source address)
            Ipv6OverIpIpv6DAPos: Match the IPv6 destination address in an IPv6 frame encapsulated in an IPv4 frame in POS packet. (pattern represents the IPv6 destination address)
            Ipv6Ppp: Match an IPv6 PPP packet.
            Ipv6CiscoHdlc: Match an IPv6 packet encapsulated with Cisco HDLC.
            GfpDataFcsNullExtEthernet: Match a user data GFP frame which includes an FCS and whose payload uses a null extension and indicates frame-mapped ethernet data.
            GfpDataNoFcsNullExtEthernet: Match a user data GFP frame which does not includes an FCS and whose payload uses a null extension and indicates frame-mapped Ethernet data.
            GfpDataFcsLinearExtEthernet: Match a user data GFP frame which includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped Ethernet data.
            GfpDataNoFcsLinearExtEthernet: Match a user data GFP frame which does not includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped Ethernet data.
            GfpMgmtFcsNullExtEthernet: Match a management GFP frame which includes an FCS and whose payload uses a null extension and indicates frame-mapped Ethernet data.
            GfpMgmtNoFcsNullExtEthernet: Match a management GFP frame which does not includes an FCS and whose payload uses a null extension and indicates frame-mapped Ethernet data.
            GfpMgmtFcsLinearExtEthernet: Match a management GFP frame which includes an FCS and whose payload uses a linear frame extenzion and indicates frame-mapped Ethernet data.
            GfpMgmtNoFcsLinearExtEthernet: Match a management GFP frame which does not includes an FCS and whose payload uses a linear frame extension and indicates framemapped ethernet data.
            GfpDataFcsNullExtPpp: Match a user data GFP frame which includes an FCS and whose payload uses a null extension and indicates frame-mapped PPP data.
            GfpDataNoFcsNullExtPpp: Match a user data GFP frame which does not includes an FCS and whose payload uses a null extension and indicates frame-mapped PPP data.
            GfpDataFcsLinearExtPpp: Match a user data GFP frame which includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped PPP data.
            GfpDataNoFcsLinearExtPpp: Match a user data GFP frame which does not includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped PPP data.
            GfpMgmtFcsNullExtPpp: Match a management GFP frame which includes an FCS and whose payload uses a null extension and indicates frame-mapped PPP data.
            GfpMgmtNoFcsNullExtPpp: Match a management GFP frame which does not includes an FCS and whose payload uses a null extension and indicates frame-mapped PPP data.
            GfpMgmtFcsLinearExtPpp: Match a management GFP frame which includes an FCS and whose payload uses a linear frame extension and indicates frame-mapped PPP data.
            GfpMgmtNoFcsLinearExtPpp: Match a management GFP frame which does not includes an FCS and whose payload uses a linear frame extension and indicates framemapped PPP data.
        Constants Available: MATCH_TYPE2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.MATCH_TYPE2_CMD : opt})

    def packet_config_filter_mode(self, opt):
        """
        This is the method the command: packet_config_filter option mode
        Description:Supported with IxTclHal and IxTclNetwork (addAtmFilter choice is not valid with IxTclNetwork). When mode is create ATM specific configurations and general configurations will be set.The user can set the same pattern_atm for more pairs vpi/vci pairs (see parameters -vpi and -vci).If the user wants to set different pattern_atm for some pairs, he has to call this procedure using -mode addAtmFilter.When using -mode addAtmFilter, only ATM specific configurations will be set and all the other configurations will be ignored. These ATM specific configurations will be appended to the previous ones.This procedure must be called only once with -mode create, otherwise it will overwrite the previous configurations.
        Constants Available: MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.MODE_CMD : opt})

    def packet_config_filter_no_write(self, opt):
        """
        This is the method the command: packet_config_filter option no_write
        Description:Supported with IxTclHal. Step to increment the VPI.
        Constants Available: NO_WRITE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.NO_WRITE_CMD : opt})

    def packet_config_filter_pattern1(self, hex):
        """
        This is the method the command: packet_config_filter option pattern1
        Description:Supported with IxTclHal and IxTclNetwork. Only frames that contain this pattern at offset pattern_offset1 are filtered, captured or counted. Must be provided as a HEX list less then 16 bytes (Example: {00 11 ff})
        Constants Available: PATTERN1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN1_CMD : hex})

    def packet_config_filter_pattern2(self, hex):
        """
        This is the method the command: packet_config_filter option pattern2
        Description:Supported with IxTclHal and IxTclNetwork. Only frames that contain this pattern at offset pattern_offset2 are filtered, captured or counted. Must be provided as a HEX list less then 16 bytes (Example: {00 22 ff aa dd ee aa dd aa dd ee ff ee 33 55 66})
        Constants Available: PATTERN2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN2_CMD : hex})

    def packet_config_filter_pattern_atm(self, hex):
        """
        This is the method the command: packet_config_filter option pattern_atm
        Description:Supported with IxTclHal. Only frames that contain this pattern at offset pattern_offset_atm are filtered, captured or counted. Must be provided as a HEX list less then 40 bytes (Example: {00 22 ff aa dd ee aa dd aa dd ee ff ee 33 55 66}). This can be used only for cards that support ATM feature. This parameter refers to the vpi/vci specified with -vpi -vci parameters.
        Constants Available: PATTERN_ATM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN_ATM_CMD : hex})

    def packet_config_filter_pattern_mask1(self, hex):
        """
        This is the method the command: packet_config_filter option pattern_mask1
        Description:Supported with IxTclHal and IxTclNetwork. A bit mask that allows the user to specify which bits of pattern1 should be used when filtering. If the mask bit is set low, the pattern bit will be used in the filter. Must be provided as a HEX list less then 16 bytes (Example: {00 00 ff})
        Constants Available: PATTERN_MASK1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN_MASK1_CMD : hex})

    def packet_config_filter_pattern_mask2(self, hex):
        """
        This is the method the command: packet_config_filter option pattern_mask2
        Description:Supported with IxTclHal and IxTclNetwork. A bit mask that allows the user to specify which bits of pattern2 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter. Must be provided as a HEX list less then 16 bytes (Example: {00 ff ff})
        Constants Available: PATTERN_MASK2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN_MASK2_CMD : hex})

    def packet_config_filter_pattern_mask_atm(self, hex):
        """
        This is the method the command: packet_config_filter option pattern_mask_atm
        Description:Supported with IxTclHal. A bit mask that allows the user to specify which bits of pattern_atm should be used when filtering. If the mask bit is set high, the pattern bit will be ignored. Must be provided as a HEX list less then 40 bytes (Example: {00 00 ff})
        Constants Available: PATTERN_MASK_ATM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN_MASK_ATM_CMD : hex})

    def packet_config_filter_pattern_offset1(self, num):
        """
        This is the method the command: packet_config_filter option pattern_offset1
        Description:Supported with IxTclHal and IxTclNetwork. Offset of pattern1 in the frame to be filtered, captured or counted.
        Constants Available: PATTERN_OFFSET1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        num --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN_OFFSET1_CMD : num})

    def packet_config_filter_pattern_offset2(self, num):
        """
        This is the method the command: packet_config_filter option pattern_offset2
        Description:Supported with IxTclHal and IxTclNetwork. Offset of pattern2 in the frame to be filtered, captured or counted.
        Constants Available: PATTERN_OFFSET2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        num --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN_OFFSET2_CMD : num})

    def packet_config_filter_pattern_offset_atm(self, num):
        """
        This is the method the command: packet_config_filter option pattern_offset_atm
        Description:Supported with IxTclHal. Offset of pattern_atm in the frame to be filtered, captured or counted.
        Constants Available: PATTERN_OFFSET_ATM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        num --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN_OFFSET_ATM_CMD : num})

    def packet_config_filter_pattern_offset_type1(self, num):
        """
        This is the method the command: packet_config_filter option pattern_offset_type1
        Description:Supported with IxTclHal and IxTclNetwork. For ports that support the portFeaturePatternOffsetFlexible feature, this option specifies the place that pattern_offset1 is relative
            Valid options are:
            startOfFrame: (default) Offset from the start of the frame.
            startOfIp: Offset from the start of the IP header
            startOfProtocol: Offset from the start of the protocol within the IP header.
            startOfSonet: Offset from the start of the SONET frame. This choice is not supported with IxTclNetwork
        Constants Available: PATTERN_OFFSET_TYPE1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        num --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_CMD : num})

    def packet_config_filter_pattern_offset_type2(self, num):
        """
        This is the method the command: packet_config_filter option pattern_offset_type2
        Description:Supported with IxTclHal and IxTclNetwork. For ports that support the portFeaturePatternOffsetFlexible feature, this option specifies the place that pattern_offset2 is relative
            Valid options are:
            startOfFrame: (default) Offset from the start of the frame.
            startOfIp: Offset from the start of the IP header
            startOfProtocol: Offset from the start of the protocol within the IP header.
            startOfSonet: Offset from the start of the SONET frame. This choice is not supported with IxTclNetwork
        Constants Available: PATTERN_OFFSET_TYPE2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        num --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PATTERN_OFFSET_TYPE2_CMD : num})

    def packet_config_filter_vci(self, opt):
        """
        This is the method the command: packet_config_filter option vci
        Description:Supported with IxTclHal. The vci with which the pattern_atm will be associated.
        Constants Available: VCI_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.VCI_CMD : opt})

    def packet_config_filter_vci_count(self, opt):
        """
        This is the method the command: packet_config_filter option vci_count
        Description:Supported with IxTclHal. Number of vci's for which the pattern_atm will apply.
        Constants Available: VCI_COUNT_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.VCI_COUNT_CMD : opt})

    def packet_config_filter_vci_step(self, opt):
        """
        This is the method the command: packet_config_filter option vci_step
        Description:Supported with IxTclHal. Step to increment the VPI.
        Constants Available: VCI_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.VCI_STEP_CMD : opt})

    def packet_config_filter_vpi(self, opt):
        """
        This is the method the command: packet_config_filter option vpi
        Description:Supported with IxTclHal. The vpi with which the pattern_atm will be associated.
        Constants Available: VPI_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.VPI_CMD : opt})

    def packet_config_filter_vpi_count(self, opt):
        """
        This is the method the command: packet_config_filter option vpi_count
        Description:Supported with IxTclHal. Number of vpi's for which the pattern_atm will apply.
        Constants Available: VPI_COUNT_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.VPI_COUNT_CMD : opt})

    def packet_config_filter_vpi_step(self, opt):
        """
        This is the method the command: packet_config_filter option vpi_step
        Description:Supported with IxTclHal. Step to increment the vpi.
        Constants Available: VPI_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.VPI_STEP_CMD : opt})


    supportedIxiaHltapiCommands = {PacketConfigFilterConstants.DA1_CMD, PacketConfigFilterConstants.DA2_CMD, PacketConfigFilterConstants.DA_MASK1_CMD, PacketConfigFilterConstants.DA_MASK2_CMD, PacketConfigFilterConstants.SA1_CMD, PacketConfigFilterConstants.SA2_CMD, PacketConfigFilterConstants.SA_MASK1_CMD, PacketConfigFilterConstants.SA_MASK2_CMD, PacketConfigFilterConstants.GFP_BAD_FCS_ERROR_CMD, PacketConfigFilterConstants.GFP_EHEC_ERROR_CMD, PacketConfigFilterConstants.GFP_ERROR_CONDITION_CMD, PacketConfigFilterConstants.GFP_PAYLOAD_CRC_CMD, PacketConfigFilterConstants.GFP_THEC_ERROR_CMD, PacketConfigFilterConstants.MATCH_TYPE1_CMD, PacketConfigFilterConstants.MATCH_TYPE2_CMD, PacketConfigFilterConstants.MODE_CMD, PacketConfigFilterConstants.NO_WRITE_CMD, PacketConfigFilterConstants.PATTERN1_CMD, PacketConfigFilterConstants.PATTERN2_CMD, PacketConfigFilterConstants.PATTERN_ATM_CMD, PacketConfigFilterConstants.PATTERN_MASK1_CMD, PacketConfigFilterConstants.PATTERN_MASK2_CMD, PacketConfigFilterConstants.PATTERN_MASK_ATM_CMD, PacketConfigFilterConstants.PATTERN_OFFSET1_CMD, PacketConfigFilterConstants.PATTERN_OFFSET2_CMD, PacketConfigFilterConstants.PATTERN_OFFSET_ATM_CMD, PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_CMD, PacketConfigFilterConstants.PATTERN_OFFSET_TYPE2_CMD, PacketConfigFilterConstants.PORT_HANDLE_CMD, PacketConfigFilterConstants.VCI_CMD, PacketConfigFilterConstants.VCI_COUNT_CMD, PacketConfigFilterConstants.VCI_STEP_CMD, PacketConfigFilterConstants.VPI_CMD, PacketConfigFilterConstants.VPI_COUNT_CMD, PacketConfigFilterConstants.VPI_STEP_CMD}
