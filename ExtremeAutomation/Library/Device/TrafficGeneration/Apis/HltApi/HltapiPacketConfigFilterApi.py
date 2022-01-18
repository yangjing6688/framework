from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: packet_config_filter

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class PacketConfigFilterApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(PacketConfigFilterApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_config_filter
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[PacketConfigFilterConstants.DA1_CMD] = "dummyValue1" # static value
        dummyDict[PacketConfigFilterConstants.DA2_CMD] = "dummyValue2" # static value
        dummyDict[PacketConfigFilterConstants.DA_MASK1_CMD] = "dummyValue3" # static value
        dummyDict[PacketConfigFilterConstants.DA_MASK2_CMD] = "dummyValue4" # static value
        dummyDict[PacketConfigFilterConstants.SA1_CMD] = "dummyValue5" # static value
        dummyDict[PacketConfigFilterConstants.SA2_CMD] = "dummyValue6" # static value
        dummyDict[PacketConfigFilterConstants.SA_MASK1_CMD] = "dummyValue7" # static value
        dummyDict[PacketConfigFilterConstants.SA_MASK2_CMD] = "dummyValue8" # static value
        dummyDict[PacketConfigFilterConstants.GFP_BAD_FCS_ERROR_CMD] = "dummyValue9" # static value
        dummyDict[PacketConfigFilterConstants.GFP_EHEC_ERROR_CMD] = "dummyValue10" # static value
        dummyDict[PacketConfigFilterConstants.GFP_ERROR_CONDITION_CMD] = "dummyValue11" # static value
        dummyDict[PacketConfigFilterConstants.GFP_PAYLOAD_CRC_CMD] = "dummyValue12" # static value
        dummyDict[PacketConfigFilterConstants.GFP_THEC_ERROR_CMD] = "dummyValue13" # static value
        dummyDict[PacketConfigFilterConstants.MATCH_TYPE1_CMD] = PacketConfigFilterConstants.MATCH_TYPE1_IPETHERNETII # constant value
        dummyDict[PacketConfigFilterConstants.MATCH_TYPE2_CMD] = PacketConfigFilterConstants.MATCH_TYPE2_IPETHERNETII # constant value
        dummyDict[PacketConfigFilterConstants.MODE_CMD] = PacketConfigFilterConstants.MODE_CREATE # constant value
        dummyDict[PacketConfigFilterConstants.NO_WRITE_CMD] = "dummyValue17" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN1_CMD] = "dummyValue18" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN2_CMD] = "dummyValue19" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN_ATM_CMD] = "dummyValue20" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN_MASK1_CMD] = "dummyValue21" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN_MASK2_CMD] = "dummyValue22" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN_MASK_ATM_CMD] = "dummyValue23" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN_OFFSET1_CMD] = "dummyValue24" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN_OFFSET2_CMD] = "dummyValue25" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN_OFFSET_ATM_CMD] = "dummyValue26" # static value
        dummyDict[PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_CMD] = PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_STARTOFFRAME # constant value
        dummyDict[PacketConfigFilterConstants.PATTERN_OFFSET_TYPE2_CMD] = PacketConfigFilterConstants.PATTERN_OFFSET_TYPE2_STARTOFFRAME # constant value
        dummyDict[PacketConfigFilterConstants.PORT_HANDLE_CMD] = "dummyValue29" # static value
        dummyDict[PacketConfigFilterConstants.VCI_CMD] = "dummyValue30" # static value
        dummyDict[PacketConfigFilterConstants.VCI_COUNT_CMD] = "dummyValue31" # static value
        dummyDict[PacketConfigFilterConstants.VCI_STEP_CMD] = "dummyValue32" # static value
        dummyDict[PacketConfigFilterConstants.VPI_CMD] = "dummyValue33" # static value
        dummyDict[PacketConfigFilterConstants.VPI_COUNT_CMD] = "dummyValue34" # static value
        dummyDict[PacketConfigFilterConstants.VPI_STEP_CMD] = "dummyValue35" # static value

        api = device.getApi(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        api.packet_config_filter(dummyDict)
    """
    def packet_config_filter(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::packet_config_filter", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_config_filter_DA1(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_DA2(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_DA_mask1(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_DA_mask2(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_SA1(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_SA2(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_SA_mask1(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_SA_mask2(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_bad_fcs_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_eHec_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_error_condition(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_payload_crc(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_tHec_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_match_type1(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_match_type2(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_mode(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_no_write(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern1(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern2(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_atm(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_mask1(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_mask2(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_mask_atm(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset1(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset2(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset_atm(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset_type1(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset_type2(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_port_handle(self, port):
        """
        This is the method the command: packet_config_filter option port_handle
        Description:Depending on the traffic_generator value, this option has different meanings. If traffic_generator ixnetwork_540 is used this parameter is used ixos/ixnetwork_540 - The port for which to configure traffic. Mandatory for -mode create/reset when -traffic_generator is set to ixos. For traffic_generator ixnetwork_540 this is mandatory on mode create only if parameter -emulation_src_handle is missing.ixnetwork/ixnetwork_540 - The port_handle parameter is not necessary anymore. When using IxNetwork, traffic configurations will be done using previously created handles (IP interfaces, PPP ranges, L2TP ranges, Protocol Route Ranges etc.) as sources (parameter -emulation_src_handle) and destinations (-emulation_dst_handle).
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.packet_config_filter({PacketConfigFilterConstants.PORT_HANDLE_CMD : port})

    def packet_config_filter_vci(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vci_count(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vci_step(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vpi(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vpi_count(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vpi_step(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


"""
    This is the Constants class for the command: packet_config_filter
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class PacketConfigFilterConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    PACKET_CONFIG_FILTER_API = "PACKET_CONFIG_FILTER_API"

    DA1_CMD = "DA1"

    DA2_CMD = "DA2"

    DA_MASK1_CMD = "DA_mask1"

    DA_MASK2_CMD = "DA_mask2"

    SA1_CMD = "SA1"

    SA2_CMD = "SA2"

    SA_MASK1_CMD = "SA_mask1"

    SA_MASK2_CMD = "SA_mask2"

    GFP_BAD_FCS_ERROR_CMD = "gfp_bad_fcs_error"

    GFP_EHEC_ERROR_CMD = "gfp_eHec_error"

    GFP_ERROR_CONDITION_CMD = "gfp_error_condition"

    GFP_PAYLOAD_CRC_CMD = "gfp_payload_crc"

    GFP_THEC_ERROR_CMD = "gfp_tHec_error"

    MATCH_TYPE1_CMD = "match_type1"
    # Constant values for MATCH_TYPE1_CMD
    MATCH_TYPE1_IPETHERNETII = "IpEthernetII"
    MATCH_TYPE1_IP8023SNAP = "Ip8023Snap"
    MATCH_TYPE1_VLAN = "Vlan"
    MATCH_TYPE1_USER = "User"
    MATCH_TYPE1_IPPPP = "IpPpp"
    MATCH_TYPE1_IPCISCOHDLC = "IpCiscoHdlc"
    MATCH_TYPE1_IPSAETHERNETII = "IpSAEthernetII"
    MATCH_TYPE1_IPDAETHERNETII = "IpDAEthernetII"
    MATCH_TYPE1_IPSADAETHERNETII = "IpSADAEthernetII"
    MATCH_TYPE1_IPSA8023SNAP = "IpSA8023Snap"
    MATCH_TYPE1_IPDA8023SNAP = "IpDA8023Snap"
    MATCH_TYPE1_IPSADA8023SNAP = "IpSADA8023Snap"
    MATCH_TYPE1_IPSAPOS = "IpSAPos"
    MATCH_TYPE1_IPDAPOS = "IpDAPos"
    MATCH_TYPE1_IPSADAPOS = "IpSADAPos"
    MATCH_TYPE1_TCPSOURCEPORTIPETHERNETII = "TcpSourcePortIPEthernetII"
    MATCH_TYPE1_TCPDESTPORTIPETHERNETII = "TcpDestPortIPEthernetII"
    MATCH_TYPE1_UDPSOURCEPORTIPETHERNETII = "UdpSourcePortIPEthernetII"
    MATCH_TYPE1_UDPDESTPORTIPETHERNETII = "UdpDestPortIPEthernetII"
    MATCH_TYPE1_TCPSOURCEPORTIP8023SNAP = "TcpSourcePortIP8023Snap"
    MATCH_TYPE1_TCPDESTPORTIP8023SNAP = "TcpDestPortIP8023Snap"
    MATCH_TYPE1_UDPSOURCEPORTIP8023SNAP = "UdpSourcePortIP8023Snap"
    MATCH_TYPE1_UDPDESTPORTIP8023SNAP = "UdpDestPortIP8023Snap"
    MATCH_TYPE1_TCPSOURCEPORTIPPOS = "TcpSourcePortIPPos"
    MATCH_TYPE1_TCPDESTPORTIPPOS = "TcpDestPortIPPos"
    MATCH_TYPE1_UDPSOURCEPORTIPPOS = "UdpSourcePortIPPos"
    MATCH_TYPE1_UDPDESTPORTIPPOS = "UdpDestPortIPPos"
    MATCH_TYPE1_SRPMODERESERVED000 = "SrpModeReserved000"
    MATCH_TYPE1_SRPMODERESERVED001 = "SrpModeReserved001"
    MATCH_TYPE1_SRPMODERESERVED010 = "SrpModeReserved010"
    MATCH_TYPE1_SRPMODEATMCELL011 = "SrpModeAtmCell011"
    MATCH_TYPE1_SRPCONTROLMESSAGEPASSTOHOST100 = "SrpControlMessagePassToHost100"
    MATCH_TYPE1_SRPCONTROLMESSAGEBUFFERFORHOST101 = "SrpControlMessageBufferForHost101"
    MATCH_TYPE1_SRPUSAGEMESSAGE110 = "SrpUsageMessage110"
    MATCH_TYPE1_SRPPACKETDATA111 = "SrpPacketData111"
    MATCH_TYPE1_SRPALLCONTROLMESSAGES10X = "SrpAllControlMessages10x"
    MATCH_TYPE1_SRPUSAGEMESSAGEORPACKETDATA11X = "SrpUsageMessageOrPacketData11x"
    MATCH_TYPE1_SRPCONTROLUSAGEORPACKETDATA1XX = "SrpControlUsageOrPacketData1xx"
    MATCH_TYPE1_SRPINNERRING = "SrpInnerRing"
    MATCH_TYPE1_SRPOUTERRING = "SrpOuterRing"
    MATCH_TYPE1_SRPPRIORITY0_7 = "SrpPriority0-7"
    MATCH_TYPE1_SRPPARITYODD = "SrpParityOdd"
    MATCH_TYPE1_SRPPARITYEVEN = "SrpParityEven"
    MATCH_TYPE1_SRPDISCOVERYFRAME = "SrpDiscoveryFrame"
    MATCH_TYPE1_SRPIPSFRAME = "SrpIpsFrame"
    MATCH_TYPE1_RPRRINGID0 = "RprRingId0"
    MATCH_TYPE1_RPRRINGID1 = "RprRingId1"
    MATCH_TYPE1_RPRFAIRNESSELIGIBILITY0 = "RprFairnessEligibility0"
    MATCH_TYPE1_RPRFAIRNESSELIGIBILITY1 = "RprFairnessEligibility1"
    MATCH_TYPE1_RPRIDLEPACKET = "RprIdlePacket"
    MATCH_TYPE1_RPRCONTROLPACKET = "RprControlPacket"
    MATCH_TYPE1_RPRFAIRNESSPACKET = "RprFairnessPacket"
    MATCH_TYPE1_RPRDATAPACKET = "RprDataPacket"
    MATCH_TYPE1_RPRSERVICECLASSC = "RprServiceClassC"
    MATCH_TYPE1_RPRSERVICECLASSB = "RprServiceClassB"
    MATCH_TYPE1_RPRSERVICECLASSA1 = "RprServiceClassA1"
    MATCH_TYPE1_RPRSERVICECLASSA0 = "RprServiceClassA0"
    MATCH_TYPE1_RPRWRAPELIGIBILITY0 = "RprWrapEligibility0"
    MATCH_TYPE1_RPRWRAPELIGIBILITY1 = "RprWrapEligibility1"
    MATCH_TYPE1_RPRPARITYBIT0 = "RprParityBit0"
    MATCH_TYPE1_RPRPARITYBIT1 = "RprParityBit1"
    MATCH_TYPE1_IPV6SAETHERNETII = "IpV6SAEthernetII"
    MATCH_TYPE1_IPV6DAETHERNETII = "IpV6DAEthernetII"
    MATCH_TYPE1_IPV6SA8023SNAP = "IpV6SA8023Snap"
    MATCH_TYPE1_IPV6DA8023SNAP = "IpV6DA8023Snap"
    MATCH_TYPE1_IPV6SAPOS = "IpV6SAPos"
    MATCH_TYPE1_IPV6DAPOS = "IpV6DAPos"
    MATCH_TYPE1_IPV6TCPSOURCEPORTETHERNETII = "Ipv6TcpSourcePortEthernetII"
    MATCH_TYPE1_IPV6TCPDESTPORTETHERNETII = "Ipv6TcpDestPortEthernetII"
    MATCH_TYPE1_IPV6UDPSOURCEPORTETHERNETII = "Ipv6UdpSourcePortEthernetII"
    MATCH_TYPE1_IPV6UDPDESTPORTETHERNETII = "Ipv6UdpDestPortEthernetII"
    MATCH_TYPE1_IPV6TCPSOURCEPORT8023SNAP = "Ipv6TcpSourcePort8023Snap"
    MATCH_TYPE1_IPV6TCPDESTPORT8023SNAP = "Ipv6TcpDestPort8023Snap"
    MATCH_TYPE1_IPV6UDPSOURCEPORT8023SNAP = "Ipv6UdpSourcePort8023Snap"
    MATCH_TYPE1_IPV6UDPDESTPORT8023SNAP = "Ipv6UdpDestPort8023Snap"
    MATCH_TYPE1_IPV6TCPSOURCEPORTPOS = "Ipv6TcpSourcePortPos"
    MATCH_TYPE1_IPV6TCPDESTPORTPOS = "Ipv6TcpDestPortPos"
    MATCH_TYPE1_IPV6UDPSOURCEPORTPOS = "Ipv6UdpSourcePortPos"
    MATCH_TYPE1_IPV6UDPDESTPORTPOS = "Ipv6UdpDestPortPos"
    MATCH_TYPE1_IPV6IPTCPSOURCEPORTETHERNETII = "Ipv6IpTcpSourcePortEthernetII"
    MATCH_TYPE1_IPV6IPTCPDESTPORTETHERNETII = "Ipv6IpTcpDestPortEthernetII"
    MATCH_TYPE1_IPV6IPUDPSOURCEPORTETHERNETII = "Ipv6IpUdpSourcePortEthernetII"
    MATCH_TYPE1_IPV6IPUDPDESTPORTETHERNETII = "Ipv6IpUdpDestPortEthernetII"
    MATCH_TYPE1_IPV6IPTCPSOURCEPORT8023SNAP = "Ipv6IpTcpSourcePort8023Snap"
    MATCH_TYPE1_IPV6IPTCPDESTPORT8023SNAP = "Ipv6IpTcpDestPort8023Snap"
    MATCH_TYPE1_IPV6IPUDPSOURCEPORT8023SNAP = "Ipv6IpUdpSourcePort8023Snap"
    MATCH_TYPE1_IPV6IPUDPDESTPORT8023SNAP = "Ipv6IpUdpDestPort8023Snap"
    MATCH_TYPE1_IPV6IPTCPSOURCEPORTPOS = "Ipv6IpTcpSourcePortPos"
    MATCH_TYPE1_IPV6IPTCPDESTPORTPOS = "Ipv6IpTcpDestPortPos"
    MATCH_TYPE1_IPV6IPUDPSOURCEPORTPOS = "Ipv6IpUdpSourcePortPos"
    MATCH_TYPE1_IPV6IPUDPDESTPORTPOS = "Ipv6IpUdpDestPortPos"
    MATCH_TYPE1_IPOVERIPV6IPSAETHERNETII = "IpOverIpv6IpSAEthernetII"
    MATCH_TYPE1_IPOVERIPV6IPDAETHERNETII = "IpOverIpv6IpDAEthernetII"
    MATCH_TYPE1_IPOVERIPV6IPSA8023SNAP = "IpOverIpv6IpSA8023Snap"
    MATCH_TYPE1_IPOVERIPV6IPDA8023SNAP = "IpOverIpv6IpDA8023Snap"
    MATCH_TYPE1_IPOVERIPV6IPSAPOS = "IpOverIpv6IpSAPos"
    MATCH_TYPE1_IPOVERIPV6IPDAPOS = "IpOverIpv6IpDAPos"
    MATCH_TYPE1_IPV6OVERIPIPV6SAETHERNETII = "Ipv6OverIpIpv6SAEthernetII"
    MATCH_TYPE1_IPV6OVERIPIPV6DAETHERNETII = "Ipv6OverIpIpv6DAEthernetII"
    MATCH_TYPE1_IPV6OVERIPIPV6SA8023SNAP = "Ipv6OverIpIpv6SA8023Snap"
    MATCH_TYPE1_IPV6OVERIPIPV6DA8023SNAP = "Ipv6OverIpIpv6DA8023Snap"
    MATCH_TYPE1_IPV6OVERIPIPV6SAPOS = "Ipv6OverIpIpv6SAPos"
    MATCH_TYPE1_IPV6OVERIPIPV6DAPOS = "Ipv6OverIpIpv6DAPos"
    MATCH_TYPE1_IPV6PPP = "Ipv6Ppp"
    MATCH_TYPE1_IPV6CISCOHDLC = "Ipv6CiscoHdlc"
    MATCH_TYPE1_GFPDATAFCSNULLEXTETHERNET = "GfpDataFcsNullExtEthernet"
    MATCH_TYPE1_GFPDATANOFCSNULLEXTETHERNET = "GfpDataNoFcsNullExtEthernet"
    MATCH_TYPE1_GFPDATAFCSLINEAREXTETHERNET = "GfpDataFcsLinearExtEthernet"
    MATCH_TYPE1_GFPDATANOFCSLINEAREXTETHERNET = "GfpDataNoFcsLinearExtEthernet"
    MATCH_TYPE1_GFPMGMTFCSNULLEXTETHERNET = "GfpMgmtFcsNullExtEthernet"
    MATCH_TYPE1_GFPMGMTNOFCSNULLEXTETHERNET = "GfpMgmtNoFcsNullExtEthernet"
    MATCH_TYPE1_GFPMGMTFCSLINEAREXTETHERNET = "GfpMgmtFcsLinearExtEthernet"
    MATCH_TYPE1_GFPMGMTNOFCSLINEAREXTETHERNET = "GfpMgmtNoFcsLinearExtEthernet"
    MATCH_TYPE1_GFPDATAFCSNULLEXTPPP = "GfpDataFcsNullExtPpp"
    MATCH_TYPE1_GFPDATANOFCSNULLEXTPPP = "GfpDataNoFcsNullExtPpp"
    MATCH_TYPE1_GFPDATAFCSLINEAREXTPPP = "GfpDataFcsLinearExtPpp"
    MATCH_TYPE1_GFPDATANOFCSLINEAREXTPPP = "GfpDataNoFcsLinearExtPpp"
    MATCH_TYPE1_GFPMGMTFCSNULLEXTPPP = "GfpMgmtFcsNullExtPpp"
    MATCH_TYPE1_GFPMGMTNOFCSNULLEXTPPP = "GfpMgmtNoFcsNullExtPpp"
    MATCH_TYPE1_GFPMGMTFCSLINEAREXTPPP = "GfpMgmtFcsLinearExtPpp"
    MATCH_TYPE1_GFPMGMTNOFCSLINEAREXTPPP = "GfpMgmtNoFcsLinearExtPpp"

    MATCH_TYPE2_CMD = "match_type2"
    # Constant values for MATCH_TYPE2_CMD
    MATCH_TYPE2_IPETHERNETII = "IpEthernetII"
    MATCH_TYPE2_IP8023SNAP = "Ip8023Snap"
    MATCH_TYPE2_VLAN = "Vlan"
    MATCH_TYPE2_USER = "User"
    MATCH_TYPE2_IPPPP = "IpPpp"
    MATCH_TYPE2_IPCISCOHDLC = "IpCiscoHdlc"
    MATCH_TYPE2_IPSAETHERNETII = "IpSAEthernetII"
    MATCH_TYPE2_IPDAETHERNETII = "IpDAEthernetII"
    MATCH_TYPE2_IPSADAETHERNETII = "IpSADAEthernetII"
    MATCH_TYPE2_IPSA8023SNAP = "IpSA8023Snap"
    MATCH_TYPE2_IPDA8023SNAP = "IpDA8023Snap"
    MATCH_TYPE2_IPSADA8023SNAP = "IpSADA8023Snap"
    MATCH_TYPE2_IPSAPOS = "IpSAPos"
    MATCH_TYPE2_IPDAPOS = "IpDAPos"
    MATCH_TYPE2_IPSADAPOS = "IpSADAPos"
    MATCH_TYPE2_TCPSOURCEPORTIPETHERNETII = "TcpSourcePortIPEthernetII"
    MATCH_TYPE2_TCPDESTPORTIPETHERNETII = "TcpDestPortIPEthernetII"
    MATCH_TYPE2_UDPSOURCEPORTIPETHERNETII = "UdpSourcePortIPEthernetII"
    MATCH_TYPE2_UDPDESTPORTIPETHERNETII = "UdpDestPortIPEthernetII"
    MATCH_TYPE2_TCPSOURCEPORTIP8023SNAP = "TcpSourcePortIP8023Snap"
    MATCH_TYPE2_TCPDESTPORTIP8023SNAP = "TcpDestPortIP8023Snap"
    MATCH_TYPE2_UDPSOURCEPORTIP8023SNAP = "UdpSourcePortIP8023Snap"
    MATCH_TYPE2_UDPDESTPORTIP8023SNAP = "UdpDestPortIP8023Snap"
    MATCH_TYPE2_TCPSOURCEPORTIPPOS = "TcpSourcePortIPPos"
    MATCH_TYPE2_TCPDESTPORTIPPOS = "TcpDestPortIPPos"
    MATCH_TYPE2_UDPSOURCEPORTIPPOS = "UdpSourcePortIPPos"
    MATCH_TYPE2_UDPDESTPORTIPPOS = "UdpDestPortIPPos"
    MATCH_TYPE2_SRPMODERESERVED000 = "SrpModeReserved000"
    MATCH_TYPE2_SRPMODERESERVED001 = "SrpModeReserved001"
    MATCH_TYPE2_SRPMODERESERVED010 = "SrpModeReserved010"
    MATCH_TYPE2_SRPMODEATMCELL011 = "SrpModeAtmCell011"
    MATCH_TYPE2_SRPCONTROLMESSAGEPASSTOHOST100 = "SrpControlMessagePassToHost100"
    MATCH_TYPE2_SRPCONTROLMESSAGEBUFFERFORHOST101 = "SrpControlMessageBufferForHost101"
    MATCH_TYPE2_SRPUSAGEMESSAGE110 = "SrpUsageMessage110"
    MATCH_TYPE2_SRPPACKETDATA111 = "SrpPacketData111"
    MATCH_TYPE2_SRPALLCONTROLMESSAGES10X = "SrpAllControlMessages10x"
    MATCH_TYPE2_SRPUSAGEMESSAGEORPACKETDATA11X = "SrpUsageMessageOrPacketData11x"
    MATCH_TYPE2_SRPCONTROLUSAGEORPACKETDATA1XX = "SrpControlUsageOrPacketData1xx"
    MATCH_TYPE2_SRPINNERRING = "SrpInnerRing"
    MATCH_TYPE2_SRPOUTERRING = "SrpOuterRing"
    MATCH_TYPE2_SRPPRIORITY0_7 = "SrpPriority0-7"
    MATCH_TYPE2_SRPPARITYODD = "SrpParityOdd"
    MATCH_TYPE2_SRPPARITYEVEN = "SrpParityEven"
    MATCH_TYPE2_SRPDISCOVERYFRAME = "SrpDiscoveryFrame"
    MATCH_TYPE2_SRPIPSFRAME = "SrpIpsFrame"
    MATCH_TYPE2_RPRRINGID0 = "RprRingId0"
    MATCH_TYPE2_RPRRINGID1 = "RprRingId1"
    MATCH_TYPE2_RPRFAIRNESSELIGIBILITY0 = "RprFairnessEligibility0"
    MATCH_TYPE2_RPRFAIRNESSELIGIBILITY1 = "RprFairnessEligibility1"
    MATCH_TYPE2_RPRIDLEPACKET = "RprIdlePacket"
    MATCH_TYPE2_RPRCONTROLPACKET = "RprControlPacket"
    MATCH_TYPE2_RPRFAIRNESSPACKET = "RprFairnessPacket"
    MATCH_TYPE2_RPRDATAPACKET = "RprDataPacket"
    MATCH_TYPE2_RPRSERVICECLASSC = "RprServiceClassC"
    MATCH_TYPE2_RPRSERVICECLASSB = "RprServiceClassB"
    MATCH_TYPE2_RPRSERVICECLASSA1 = "RprServiceClassA1"
    MATCH_TYPE2_RPRSERVICECLASSA0 = "RprServiceClassA0"
    MATCH_TYPE2_RPRWRAPELIGIBILITY0 = "RprWrapEligibility0"
    MATCH_TYPE2_RPRWRAPELIGIBILITY1 = "RprWrapEligibility1"
    MATCH_TYPE2_RPRPARITYBIT0 = "RprParityBit0"
    MATCH_TYPE2_RPRPARITYBIT1 = "RprParityBit1"
    MATCH_TYPE2_IPV6SAETHERNETII = "IpV6SAEthernetII"
    MATCH_TYPE2_IPV6DAETHERNETII = "IpV6DAEthernetII"
    MATCH_TYPE2_IPV6SA8023SNAP = "IpV6SA8023Snap"
    MATCH_TYPE2_IPV6DA8023SNAP = "IpV6DA8023Snap"
    MATCH_TYPE2_IPV6SAPOS = "IpV6SAPos"
    MATCH_TYPE2_IPV6DAPOS = "IpV6DAPos"
    MATCH_TYPE2_IPV6TCPSOURCEPORTETHERNETII = "Ipv6TcpSourcePortEthernetII"
    MATCH_TYPE2_IPV6TCPDESTPORTETHERNETII = "Ipv6TcpDestPortEthernetII"
    MATCH_TYPE2_IPV6UDPSOURCEPORTETHERNETII = "Ipv6UdpSourcePortEthernetII"
    MATCH_TYPE2_IPV6UDPDESTPORTETHERNETII = "Ipv6UdpDestPortEthernetII"
    MATCH_TYPE2_IPV6TCPSOURCEPORT8023SNAP = "Ipv6TcpSourcePort8023Snap"
    MATCH_TYPE2_IPV6TCPDESTPORT8023SNAP = "Ipv6TcpDestPort8023Snap"
    MATCH_TYPE2_IPV6UDPSOURCEPORT8023SNAP = "Ipv6UdpSourcePort8023Snap"
    MATCH_TYPE2_IPV6UDPDESTPORT8023SNAP = "Ipv6UdpDestPort8023Snap"
    MATCH_TYPE2_IPV6TCPSOURCEPORTPOS = "Ipv6TcpSourcePortPos"
    MATCH_TYPE2_IPV6TCPDESTPORTPOS = "Ipv6TcpDestPortPos"
    MATCH_TYPE2_IPV6UDPSOURCEPORTPOS = "Ipv6UdpSourcePortPos"
    MATCH_TYPE2_IPV6UDPDESTPORTPOS = "Ipv6UdpDestPortPos"
    MATCH_TYPE2_IPV6IPTCPSOURCEPORTETHERNETII = "Ipv6IpTcpSourcePortEthernetII"
    MATCH_TYPE2_IPV6IPTCPDESTPORTETHERNETII = "Ipv6IpTcpDestPortEthernetII"
    MATCH_TYPE2_IPV6IPUDPSOURCEPORTETHERNETII = "Ipv6IpUdpSourcePortEthernetII"
    MATCH_TYPE2_IPV6IPUDPDESTPORTETHERNETII = "Ipv6IpUdpDestPortEthernetII"
    MATCH_TYPE2_IPV6IPTCPSOURCEPORT8023SNAP = "Ipv6IpTcpSourcePort8023Snap"
    MATCH_TYPE2_IPV6IPTCPDESTPORT8023SNAP = "Ipv6IpTcpDestPort8023Snap"
    MATCH_TYPE2_IPV6IPUDPSOURCEPORT8023SNAP = "Ipv6IpUdpSourcePort8023Snap"
    MATCH_TYPE2_IPV6IPUDPDESTPORT8023SNAP = "Ipv6IpUdpDestPort8023Snap"
    MATCH_TYPE2_IPV6IPTCPSOURCEPORTPOS = "Ipv6IpTcpSourcePortPos"
    MATCH_TYPE2_IPV6IPTCPDESTPORTPOS = "Ipv6IpTcpDestPortPos"
    MATCH_TYPE2_IPV6IPUDPSOURCEPORTPOS = "Ipv6IpUdpSourcePortPos"
    MATCH_TYPE2_IPV6IPUDPDESTPORTPOS = "Ipv6IpUdpDestPortPos"
    MATCH_TYPE2_IPOVERIPV6IPSAETHERNETII = "IpOverIpv6IpSAEthernetII"
    MATCH_TYPE2_IPOVERIPV6IPDAETHERNETII = "IpOverIpv6IpDAEthernetII"
    MATCH_TYPE2_IPOVERIPV6IPSA8023SNAP = "IpOverIpv6IpSA8023Snap"
    MATCH_TYPE2_IPOVERIPV6IPDA8023SNAP = "IpOverIpv6IpDA8023Snap"
    MATCH_TYPE2_IPOVERIPV6IPSAPOS = "IpOverIpv6IpSAPos"
    MATCH_TYPE2_IPOVERIPV6IPDAPOS = "IpOverIpv6IpDAPos"
    MATCH_TYPE2_IPV6OVERIPIPV6SAETHERNETII = "Ipv6OverIpIpv6SAEthernetII"
    MATCH_TYPE2_IPV6OVERIPIPV6DAETHERNETII = "Ipv6OverIpIpv6DAEthernetII"
    MATCH_TYPE2_IPV6OVERIPIPV6SA8023SNAP = "Ipv6OverIpIpv6SA8023Snap"
    MATCH_TYPE2_IPV6OVERIPIPV6DA8023SNAP = "Ipv6OverIpIpv6DA8023Snap"
    MATCH_TYPE2_IPV6OVERIPIPV6SAPOS = "Ipv6OverIpIpv6SAPos"
    MATCH_TYPE2_IPV6OVERIPIPV6DAPOS = "Ipv6OverIpIpv6DAPos"
    MATCH_TYPE2_IPV6PPP = "Ipv6Ppp"
    MATCH_TYPE2_IPV6CISCOHDLC = "Ipv6CiscoHdlc"
    MATCH_TYPE2_GFPDATAFCSNULLEXTETHERNET = "GfpDataFcsNullExtEthernet"
    MATCH_TYPE2_GFPDATANOFCSNULLEXTETHERNET = "GfpDataNoFcsNullExtEthernet"
    MATCH_TYPE2_GFPDATAFCSLINEAREXTETHERNET = "GfpDataFcsLinearExtEthernet"
    MATCH_TYPE2_GFPDATANOFCSLINEAREXTETHERNET = "GfpDataNoFcsLinearExtEthernet"
    MATCH_TYPE2_GFPMGMTFCSNULLEXTETHERNET = "GfpMgmtFcsNullExtEthernet"
    MATCH_TYPE2_GFPMGMTNOFCSNULLEXTETHERNET = "GfpMgmtNoFcsNullExtEthernet"
    MATCH_TYPE2_GFPMGMTFCSLINEAREXTETHERNET = "GfpMgmtFcsLinearExtEthernet"
    MATCH_TYPE2_GFPMGMTNOFCSLINEAREXTETHERNET = "GfpMgmtNoFcsLinearExtEthernet"
    MATCH_TYPE2_GFPDATAFCSNULLEXTPPP = "GfpDataFcsNullExtPpp"
    MATCH_TYPE2_GFPDATANOFCSNULLEXTPPP = "GfpDataNoFcsNullExtPpp"
    MATCH_TYPE2_GFPDATAFCSLINEAREXTPPP = "GfpDataFcsLinearExtPpp"
    MATCH_TYPE2_GFPDATANOFCSLINEAREXTPPP = "GfpDataNoFcsLinearExtPpp"
    MATCH_TYPE2_GFPMGMTFCSNULLEXTPPP = "GfpMgmtFcsNullExtPpp"
    MATCH_TYPE2_GFPMGMTNOFCSNULLEXTPPP = "GfpMgmtNoFcsNullExtPpp"
    MATCH_TYPE2_GFPMGMTFCSLINEAREXTPPP = "GfpMgmtFcsLinearExtPpp"
    MATCH_TYPE2_GFPMGMTNOFCSLINEAREXTPPP = "GfpMgmtNoFcsLinearExtPpp"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CREATE = "create"
    MODE_ADDATMFILTER = "addAtmFilter"

    NO_WRITE_CMD = "no_write"

    PATTERN1_CMD = "pattern1"

    PATTERN2_CMD = "pattern2"

    PATTERN_ATM_CMD = "pattern_atm"

    PATTERN_MASK1_CMD = "pattern_mask1"

    PATTERN_MASK2_CMD = "pattern_mask2"

    PATTERN_MASK_ATM_CMD = "pattern_mask_atm"

    PATTERN_OFFSET1_CMD = "pattern_offset1"

    PATTERN_OFFSET2_CMD = "pattern_offset2"

    PATTERN_OFFSET_ATM_CMD = "pattern_offset_atm"

    PATTERN_OFFSET_TYPE1_CMD = "pattern_offset_type1"
    # Constant values for PATTERN_OFFSET_TYPE1_CMD
    PATTERN_OFFSET_TYPE1_STARTOFFRAME = "startOfFrame"
    PATTERN_OFFSET_TYPE1_STARTOFIP = "startOfIp"
    PATTERN_OFFSET_TYPE1_STARTOFPROTOCOL = "startOfProtocol"
    PATTERN_OFFSET_TYPE1_STARTOFSONET = "startOfSonet"

    PATTERN_OFFSET_TYPE2_CMD = "pattern_offset_type2"
    # Constant values for PATTERN_OFFSET_TYPE2_CMD
    PATTERN_OFFSET_TYPE2_STARTOFFRAME = "startOfFrame"
    PATTERN_OFFSET_TYPE2_STARTOFIP = "startOfIp"
    PATTERN_OFFSET_TYPE2_STARTOFPROTOCOL = "startOfProtocol"
    PATTERN_OFFSET_TYPE2_STARTOFSONET = "startOfSonet"

    PORT_HANDLE_CMD = "port_handle"

    VCI_CMD = "vci"

    VCI_COUNT_CMD = "vci_count"

    VCI_STEP_CMD = "vci_step"

    VPI_CMD = "vpi"

    VPI_COUNT_CMD = "vpi_count"

    VPI_STEP_CMD = "vpi_step"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -DA1
    -DA2
    -DA_mask1
    -DA_mask2
    -SA1
    -SA2
    -SA_mask1
    -SA_mask2
    -gfp_bad_fcs_error
    -gfp_eHec_error
    -gfp_error_condition
    -gfp_payload_crc
    -gfp_tHec_error
    -match_type1
    -match_type2
    -mode
    -no_write
    -pattern1
    -pattern2
    -pattern_atm
    -pattern_mask1
    -pattern_mask2
    -pattern_mask_atm
    -pattern_offset1
    -pattern_offset2
    -pattern_offset_atm
    -pattern_offset_type1
    -pattern_offset_type2
    -port_handle
    -vci
    -vci_count
    -vci_step
    -vpi
    -vpi_count
    -vpi_step
If you want to update this file, look in the CSV
"""
