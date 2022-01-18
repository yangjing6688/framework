from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: interface_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class InterfaceConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(InterfaceConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: interface_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[InterfaceConfigConstants.ADDITIONAL_FCOE_STAT_1_CMD] = InterfaceConfigConstants.ADDITIONAL_FCOE_STAT_1_FCOE_INVALID_DELIMITER # constant value
        dummyDict[InterfaceConfigConstants.ADDITIONAL_FCOE_STAT_2_CMD] = InterfaceConfigConstants.ADDITIONAL_FCOE_STAT_2_FCOE_INVALID_DELIMITER # constant value
        dummyDict[InterfaceConfigConstants.ADDRESSES_PER_SVLAN_CMD] = "dummyValue3" # static value
        dummyDict[InterfaceConfigConstants.ADDRESSES_PER_VCI_CMD] = "dummyValue4" # static value
        dummyDict[InterfaceConfigConstants.ADDRESSES_PER_VLAN_CMD] = "dummyValue5" # static value
        dummyDict[InterfaceConfigConstants.ADDRESSES_PER_VPI_CMD] = "dummyValue6" # static value
        dummyDict[InterfaceConfigConstants.ARP_CMD] = "dummyValue7" # static value
        dummyDict[InterfaceConfigConstants.ARP_ON_LINKUP_CMD] = "dummyValue8" # static value
        dummyDict[InterfaceConfigConstants.ARP_REFRESH_INTERVAL_CMD] = "dummyValue9" # static value
        dummyDict[InterfaceConfigConstants.ARP_REQ_RETRIES_CMD] = "dummyValue10" # static value
        dummyDict[InterfaceConfigConstants.ARP_REQ_TIMER_CMD] = "dummyValue11" # static value
        dummyDict[InterfaceConfigConstants.ARP_SEND_REQ_CMD] = "dummyValue12" # static value
        dummyDict[InterfaceConfigConstants.ATM_ENABLE_COSET_CMD] = "dummyValue13" # static value
        dummyDict[InterfaceConfigConstants.ATM_ENABLE_PATTERN_MATCHING_CMD] = "dummyValue14" # static value
        dummyDict[InterfaceConfigConstants.ATM_ENCAPSULATION_CMD] = InterfaceConfigConstants.ATM_ENCAPSULATION_VCCMUXIPV4ROUTED # constant value
        dummyDict[InterfaceConfigConstants.ATM_FILLER_CELL_CMD] = InterfaceConfigConstants.ATM_FILLER_CELL_IDLE # constant value
        dummyDict[InterfaceConfigConstants.ATM_INTERFACE_TYPE_CMD] = InterfaceConfigConstants.ATM_INTERFACE_TYPE_UNI # constant value
        dummyDict[InterfaceConfigConstants.ATM_PACKET_DECODE_MODE_CMD] = InterfaceConfigConstants.ATM_PACKET_DECODE_MODE_FRAME # constant value
        dummyDict[InterfaceConfigConstants.ATM_REASSEMBLY_TIMEOUT_CMD] = "dummyValue19" # static value
        dummyDict[InterfaceConfigConstants.AUTO_DETECT_INSTRUMENTATION_TYPE_CMD] = InterfaceConfigConstants.AUTO_DETECT_INSTRUMENTATION_TYPE_END_OF_FRAME # constant value
        dummyDict[InterfaceConfigConstants.AUTONEGOTIATION_CMD] = "dummyValue21" # static value
        dummyDict[InterfaceConfigConstants.BAD_BLOCKS_NUMBER_CMD] = "dummyValue22" # static value
        dummyDict[InterfaceConfigConstants.BERT_CONFIGURATION_CMD] = "dummyValue23" # static value
        dummyDict[InterfaceConfigConstants.BERT_ERROR_INSERTION_CMD] = "dummyValue24" # static value
        dummyDict[InterfaceConfigConstants.CHECK_GATEWAY_EXISTS_CMD] = "dummyValue25" # static value
        dummyDict[InterfaceConfigConstants.CHECK_OPPOSITE_IP_VERSION_CMD] = "dummyValue26" # static value
        dummyDict[InterfaceConfigConstants.CLOCKSOURCE_CMD] = InterfaceConfigConstants.CLOCKSOURCE_INTERNAL # constant value
        dummyDict[InterfaceConfigConstants.CONNECTED_COUNT_CMD] = "dummyValue28" # static value
        dummyDict[InterfaceConfigConstants.CONNECTED_TO_HANDLE_CMD] = "dummyValue29" # static value
        dummyDict[InterfaceConfigConstants.DATA_INTEGRITY_CMD] = "dummyValue30" # static value
        dummyDict[InterfaceConfigConstants.DUPLEX_CMD] = InterfaceConfigConstants.DUPLEX_HALF # constant value
        dummyDict[InterfaceConfigConstants.ENABLE_DATA_CENTER_SHARED_STATS_CMD] = "dummyValue32" # static value
        dummyDict[InterfaceConfigConstants.ENABLE_FLOW_CONTROL_CMD] = "dummyValue33" # static value
        dummyDict[InterfaceConfigConstants.ENABLE_LOOPBACK_CMD] = "dummyValue34" # static value
        dummyDict[InterfaceConfigConstants.ENABLE_NDP_CMD] = "dummyValue35" # static value
        dummyDict[InterfaceConfigConstants.ENABLE_RS_FEC_CMD] = "dummyValue36" # static value
        dummyDict[InterfaceConfigConstants.ENABLE_RS_FEC_STATISTICS_CMD] = "dummyValue37" # static value
        dummyDict[InterfaceConfigConstants.ETHERNET_ATTEMPT_ENABLED_CMD] = "dummyValue38" # static value
        dummyDict[InterfaceConfigConstants.ETHERNET_ATTEMPT_INTERVAL_CMD] = "dummyValue39" # static value
        dummyDict[InterfaceConfigConstants.ETHERNET_ATTEMPT_RATE_CMD] = "dummyValue40" # static value
        dummyDict[InterfaceConfigConstants.ETHERNET_ATTEMPT_SCALE_MODE_CMD] = InterfaceConfigConstants.ETHERNET_ATTEMPT_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.ETHERNET_DICONNECT_ENABLED_CMD] = "dummyValue42" # static value
        dummyDict[InterfaceConfigConstants.ETHERNET_DISCONNECT_INTERVAL_CMD] = "dummyValue43" # static value
        dummyDict[InterfaceConfigConstants.ETHERNET_DISCONNECT_RATE_CMD] = "dummyValue44" # static value
        dummyDict[InterfaceConfigConstants.ETHERNET_DISCONNECT_SCALE_MODE_CMD] = InterfaceConfigConstants.ETHERNET_DISCONNECT_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.FC_CREDIT_STARVATION_VALUE_CMD] = "dummyValue46" # static value
        dummyDict[InterfaceConfigConstants.FC_FIXED_DELAY_VALUE_CMD] = "dummyValue47" # static value
        dummyDict[InterfaceConfigConstants.FC_FORCE_ERRORS_CMD] = InterfaceConfigConstants.FC_FORCE_ERRORS_NO_ERRORS # constant value
        dummyDict[InterfaceConfigConstants.FC_MAX_DELAY_FOR_RANDOM_VALUE_CMD] = "dummyValue49" # static value
        dummyDict[InterfaceConfigConstants.FC_MIN_DELAY_FOR_RANDOM_VALUE_CMD] = "dummyValue50" # static value
        dummyDict[InterfaceConfigConstants.FC_NO_RRDY_AFTER_CMD] = "dummyValue51" # static value
        dummyDict[InterfaceConfigConstants.FC_RRDY_RESPONSE_DELAYS_CMD] = InterfaceConfigConstants.FC_RRDY_RESPONSE_DELAYS_CREDIT_STARVATION # constant value
        dummyDict[InterfaceConfigConstants.FC_TX_IGNORE_AVAILABLE_CREDITS_CMD] = "dummyValue53" # static value
        dummyDict[InterfaceConfigConstants.FC_TX_IGNORE_RX_LINK_FAULTS_CMD] = "dummyValue54" # static value
        dummyDict[InterfaceConfigConstants.FCOE_FLOW_CONTROL_TYPE_CMD] = InterfaceConfigConstants.FCOE_FLOW_CONTROL_TYPE_IEEE802_3X # constant value
        dummyDict[InterfaceConfigConstants.FCOE_PRIORITY_GROUP_SIZE_CMD] = InterfaceConfigConstants.FCOE_PRIORITY_GROUP_SIZE_OPT_4 # constant value
        dummyDict[InterfaceConfigConstants.FCOE_PRIORITY_GROUPS_CMD] = "dummyValue57" # static value
        dummyDict[InterfaceConfigConstants.FCOE_SUPPORT_DATA_CENTER_MODE_CMD] = "dummyValue58" # static value
        dummyDict[InterfaceConfigConstants.FLOW_CONTROL_DIRECTED_ADDR_CMD] = "dummyValue59" # static value
        dummyDict[InterfaceConfigConstants.FRAMING_CMD] = InterfaceConfigConstants.FRAMING_SONET # constant value
        dummyDict[InterfaceConfigConstants.GATEWAY_CMD] = "dummyValue61" # static value
        dummyDict[InterfaceConfigConstants.GATEWAY_INCR_MODE_CMD] = InterfaceConfigConstants.GATEWAY_INCR_MODE_EVERY_SUBNET # constant value
        dummyDict[InterfaceConfigConstants.GATEWAY_STEP_CMD] = "dummyValue63" # static value
        dummyDict[InterfaceConfigConstants.GOOD_BLOCKS_NUMBER_CMD] = "dummyValue64" # static value
        dummyDict[InterfaceConfigConstants.GRE_CHECKSUM_ENABLE_CMD] = "dummyValue65" # static value
        dummyDict[InterfaceConfigConstants.GRE_COUNT_CMD] = "dummyValue66" # static value
        dummyDict[InterfaceConfigConstants.GRE_DST_IP_ADDR_CMD] = "dummyValue67" # static value
        dummyDict[InterfaceConfigConstants.GRE_DST_IP_ADDR_STEP_CMD] = "dummyValue68" # static value
        dummyDict[InterfaceConfigConstants.GRE_IP_ADDR_CMD] = "dummyValue69" # static value
        dummyDict[InterfaceConfigConstants.GRE_IP_ADDR_STEP_CMD] = "dummyValue70" # static value
        dummyDict[InterfaceConfigConstants.GRE_IP_PREFIX_LENGTH_CMD] = "dummyValue71" # static value
        dummyDict[InterfaceConfigConstants.GRE_IPV6_ADDR_CMD] = "dummyValue72" # static value
        dummyDict[InterfaceConfigConstants.GRE_IPV6_ADDR_STEP_CMD] = "dummyValue73" # static value
        dummyDict[InterfaceConfigConstants.GRE_IPV6_PREFIX_LENGTH_CMD] = "dummyValue74" # static value
        dummyDict[InterfaceConfigConstants.GRE_KEY_ENABLE_CMD] = "dummyValue75" # static value
        dummyDict[InterfaceConfigConstants.GRE_KEY_IN_CMD] = "dummyValue76" # static value
        dummyDict[InterfaceConfigConstants.GRE_KEY_OUT_CMD] = "dummyValue77" # static value
        dummyDict[InterfaceConfigConstants.GRE_SEQ_ENABLE_CMD] = "dummyValue78" # static value
        dummyDict[InterfaceConfigConstants.IEEE_MEDIA_DEFAULTS_CMD] = "dummyValue79" # static value
        dummyDict[InterfaceConfigConstants.IGNORE_LINK_CMD] = "dummyValue80" # static value
        dummyDict[InterfaceConfigConstants.INTEGRITY_SIGNATURE_CMD] = "dummyValue81" # static value
        dummyDict[InterfaceConfigConstants.INTEGRITY_SIGNATURE_OFFSET_CMD] = "dummyValue82" # static value
        dummyDict[InterfaceConfigConstants.INTERFACE_HANDLE_CMD] = "dummyValue83" # static value
        dummyDict[InterfaceConfigConstants.INTERNAL_PPM_ADJUST_CMD] = "dummyValue84" # static value
        dummyDict[InterfaceConfigConstants.INTF_IP_ADDR_CMD] = "dummyValue85" # static value
        dummyDict[InterfaceConfigConstants.INTF_IP_ADDR_STEP_CMD] = "dummyValue86" # static value
        dummyDict[InterfaceConfigConstants.INTF_MODE_CMD] = InterfaceConfigConstants.INTF_MODE_ATM # constant value
        dummyDict[InterfaceConfigConstants.INTRINSIC_LATENCY_ADJUSTMENT_CMD] = "dummyValue88" # static value
        dummyDict[InterfaceConfigConstants.IPV4_ATTEMPT_ENABLED_CMD] = "dummyValue89" # static value
        dummyDict[InterfaceConfigConstants.IPV4_ATTEMPT_INTERVAL_CMD] = "dummyValue90" # static value
        dummyDict[InterfaceConfigConstants.IPV4_ATTEMPT_RATE_CMD] = "dummyValue91" # static value
        dummyDict[InterfaceConfigConstants.IPV4_ATTEMPT_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV4_ATTEMPT_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.IPV4_DICONNECT_ENABLED_CMD] = "dummyValue93" # static value
        dummyDict[InterfaceConfigConstants.IPV4_DISCONNECT_INTERVAL_CMD] = "dummyValue94" # static value
        dummyDict[InterfaceConfigConstants.IPV4_DISCONNECT_RATE_CMD] = "dummyValue95" # static value
        dummyDict[InterfaceConfigConstants.IPV4_DISCONNECT_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV4_DISCONNECT_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.IPV4_MANUAL_GATEWAY_MAC_CMD] = "dummyValue97" # static value
        dummyDict[InterfaceConfigConstants.IPV4_MANUAL_GATEWAY_MAC_STEP_CMD] = "dummyValue98" # static value
        dummyDict[InterfaceConfigConstants.IPV4_RE_SEND_ARP_ON_LINK_UP_CMD] = "dummyValue99" # static value
        dummyDict[InterfaceConfigConstants.IPV4_RESOLVE_GATEWAY_CMD] = "dummyValue100" # static value
        dummyDict[InterfaceConfigConstants.IPV4_SEND_ARP_INTERVAL_CMD] = "dummyValue101" # static value
        dummyDict[InterfaceConfigConstants.IPV4_SEND_ARP_MAX_OUTSTANDING_CMD] = "dummyValue102" # static value
        dummyDict[InterfaceConfigConstants.IPV4_SEND_ARP_RATE_CMD] = "dummyValue103" # static value
        dummyDict[InterfaceConfigConstants.IPV4_SEND_ARP_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV4_SEND_ARP_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.IPV6_ADDR_MODE_CMD] = InterfaceConfigConstants.IPV6_ADDR_MODE_STATIC # constant value
        dummyDict[InterfaceConfigConstants.IPV6_ATTEMPT_ENABLED_CMD] = "dummyValue106" # static value
        dummyDict[InterfaceConfigConstants.IPV6_ATTEMPT_INTERVAL_CMD] = "dummyValue107" # static value
        dummyDict[InterfaceConfigConstants.IPV6_ATTEMPT_RATE_CMD] = "dummyValue108" # static value
        dummyDict[InterfaceConfigConstants.IPV6_ATTEMPT_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV6_ATTEMPT_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_ENABLED_CMD] = "dummyValue110" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_INTERVAL_CMD] = "dummyValue111" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_MAX_OUTSTANDING_CMD] = "dummyValue112" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_RATE_CMD] = "dummyValue113" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_ATTEMPT_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_ENABLED_CMD] = "dummyValue115" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_INTERVAL_CMD] = "dummyValue116" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_MAX_OUTSTANDING_CMD] = "dummyValue117" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_RATE_CMD] = "dummyValue118" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_DISCONNECT_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_ENABLED_CMD] = "dummyValue120" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_MAX_OUTSTANDING_CMD] = "dummyValue121" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_RATE_CMD] = "dummyValue122" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_NS_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_ENABLED_CMD] = "dummyValue124" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_INTERVAL_CMD] = "dummyValue125" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_MAX_OUTSTANDING_CMD] = "dummyValue126" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_RATE_CMD] = "dummyValue127" # static value
        dummyDict[InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV6_AUTOCONFIGURATION_SEND_RS_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.IPV6_DICONNECT_ENABLED_CMD] = "dummyValue129" # static value
        dummyDict[InterfaceConfigConstants.IPV6_DISCONNECT_INTERVAL_CMD] = "dummyValue130" # static value
        dummyDict[InterfaceConfigConstants.IPV6_DISCONNECT_RATE_CMD] = "dummyValue131" # static value
        dummyDict[InterfaceConfigConstants.IPV6_DISCONNECT_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV6_DISCONNECT_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.IPV6_GATEWAY_CMD] = "dummyValue133" # static value
        dummyDict[InterfaceConfigConstants.IPV6_GATEWAY_STEP_CMD] = "dummyValue134" # static value
        dummyDict[InterfaceConfigConstants.IPV6_INTF_ADDR_CMD] = "dummyValue135" # static value
        dummyDict[InterfaceConfigConstants.IPV6_INTF_ADDR_STEP_CMD] = "dummyValue136" # static value
        dummyDict[InterfaceConfigConstants.IPV6_LOOPBACK_MULTIPLIER_CMD] = "dummyValue137" # static value
        dummyDict[InterfaceConfigConstants.IPV6_MANUAL_GATEWAY_MAC_CMD] = "dummyValue138" # static value
        dummyDict[InterfaceConfigConstants.IPV6_MANUAL_GATEWAY_MAC_STEP_CMD] = "dummyValue139" # static value
        dummyDict[InterfaceConfigConstants.IPV6_MULTIPLIER_CMD] = "dummyValue140" # static value
        dummyDict[InterfaceConfigConstants.IPV6_PREFIX_LENGTH_CMD] = "dummyValue141" # static value
        dummyDict[InterfaceConfigConstants.IPV6_RE_SEND_NS_ON_LINK_UP_CMD] = "dummyValue142" # static value
        dummyDict[InterfaceConfigConstants.IPV6_RESOLVE_GATEWAY_CMD] = "dummyValue143" # static value
        dummyDict[InterfaceConfigConstants.IPV6_SEND_NS_INTERVAL_CMD] = "dummyValue144" # static value
        dummyDict[InterfaceConfigConstants.IPV6_SEND_NS_MAX_OUTSTANDING_CMD] = "dummyValue145" # static value
        dummyDict[InterfaceConfigConstants.IPV6_SEND_NS_RATE_CMD] = "dummyValue146" # static value
        dummyDict[InterfaceConfigConstants.IPV6_SEND_NS_SCALE_MODE_CMD] = InterfaceConfigConstants.IPV6_SEND_NS_SCALE_MODE_PORT # constant value
        dummyDict[InterfaceConfigConstants.L23_CONFIG_TYPE_CMD] = InterfaceConfigConstants.L23_CONFIG_TYPE_PROTOCOL_INTERFACE # constant value
        dummyDict[InterfaceConfigConstants.LASER_ON_CMD] = "dummyValue149" # static value
        dummyDict[InterfaceConfigConstants.LINK_TRAINING_CMD] = "dummyValue150" # static value
        dummyDict[InterfaceConfigConstants.LOOP_CONTINUOUSLY_CMD] = "dummyValue151" # static value
        dummyDict[InterfaceConfigConstants.LOOP_COUNT_NUMBER_CMD] = "dummyValue152" # static value
        dummyDict[InterfaceConfigConstants.MASTER_SLAVE_MODE_CMD] = InterfaceConfigConstants.MASTER_SLAVE_MODE_AUTO # constant value
        dummyDict[InterfaceConfigConstants.MODE_CMD] = InterfaceConfigConstants.MODE_CONFIG # constant value
        dummyDict[InterfaceConfigConstants.MSS_CMD] = "dummyValue155" # static value
        dummyDict[InterfaceConfigConstants.MTU_CMD] = "dummyValue156" # static value
        dummyDict[InterfaceConfigConstants.NDP_SEND_REQ_CMD] = "dummyValue157" # static value
        dummyDict[InterfaceConfigConstants.NETMASK_CMD] = "dummyValue158" # static value
        dummyDict[InterfaceConfigConstants.NO_WRITE_CMD] = "dummyValue159" # static value
        dummyDict[InterfaceConfigConstants.NOTIFY_MAC_MOVE_CMD] = "dummyValue160" # static value
        dummyDict[InterfaceConfigConstants.NS_ON_LINKUP_CMD] = "dummyValue161" # static value
        dummyDict[InterfaceConfigConstants.OP_MODE_CMD] = InterfaceConfigConstants.OP_MODE_LOOPBACK # constant value
        dummyDict[InterfaceConfigConstants.OVERRIDE_EXISTENCE_CHECK_CMD] = "dummyValue163" # static value
        dummyDict[InterfaceConfigConstants.OVERRIDE_TRACKING_CMD] = "dummyValue164" # static value
        dummyDict[InterfaceConfigConstants.PCS_COUNT_CMD] = "dummyValue165" # static value
        dummyDict[InterfaceConfigConstants.PCS_ENABLED_CONTINUOUS_CMD] = "dummyValue166" # static value
        dummyDict[InterfaceConfigConstants.PCS_LANE_CMD] = "dummyValue167" # static value
        dummyDict[InterfaceConfigConstants.PCS_MARKER_FIELDS_CMD] = "dummyValue168" # static value
        dummyDict[InterfaceConfigConstants.PCS_PERIOD_CMD] = "dummyValue169" # static value
        dummyDict[InterfaceConfigConstants.PCS_PERIOD_TYPE_CMD] = "dummyValue170" # static value
        dummyDict[InterfaceConfigConstants.PCS_REPEAT_CMD] = "dummyValue171" # static value
        dummyDict[InterfaceConfigConstants.PCS_SYNC_BITS_CMD] = "dummyValue172" # static value
        dummyDict[InterfaceConfigConstants.PGID_128K_BIN_ENABLE_CMD] = "dummyValue173" # static value
        dummyDict[InterfaceConfigConstants.PGID_ENCAP_CMD] = InterfaceConfigConstants.PGID_ENCAP_LLCROUTEDCLIP # constant value
        dummyDict[InterfaceConfigConstants.PGID_MASK_CMD] = "dummyValue175" # static value
        dummyDict[InterfaceConfigConstants.PGID_MODE_CMD] = InterfaceConfigConstants.PGID_MODE_CUSTOM # constant value
        dummyDict[InterfaceConfigConstants.PGID_OFFSET_CMD] = "dummyValue177" # static value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT1_MASK_CMD] = "dummyValue178" # static value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT1_OFFSET_CMD] = "dummyValue179" # static value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT1_OFFSET_FROM_CMD] = InterfaceConfigConstants.PGID_SPLIT1_OFFSET_FROM_START_OF_FRAME # constant value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT1_WIDTH_CMD] = "dummyValue181" # static value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT2_MASK_CMD] = "dummyValue182" # static value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT2_OFFSET_CMD] = "dummyValue183" # static value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT2_OFFSET_FROM_CMD] = InterfaceConfigConstants.PGID_SPLIT2_OFFSET_FROM_START_OF_FRAME # constant value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT2_WIDTH_CMD] = "dummyValue185" # static value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT3_MASK_CMD] = "dummyValue186" # static value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT3_OFFSET_CMD] = "dummyValue187" # static value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT3_OFFSET_FROM_CMD] = InterfaceConfigConstants.PGID_SPLIT3_OFFSET_FROM_START_OF_FRAME # constant value
        dummyDict[InterfaceConfigConstants.PGID_SPLIT3_WIDTH_CMD] = "dummyValue189" # static value
        dummyDict[InterfaceConfigConstants.PHY_MODE_CMD] = InterfaceConfigConstants.PHY_MODE_COPPER # constant value
        dummyDict[InterfaceConfigConstants.PING_DST_CMD] = "dummyValue191" # static value
        dummyDict[InterfaceConfigConstants.PORT_HANDLE_CMD] = "dummyValue192" # static value
        dummyDict[InterfaceConfigConstants.PORT_RX_MODE_CMD] = InterfaceConfigConstants.PORT_RX_MODE_CAPTURE # constant value
        dummyDict[InterfaceConfigConstants.PPP_IPV4_ADDRESS_CMD] = "dummyValue194" # static value
        dummyDict[InterfaceConfigConstants.PPP_IPV4_NEGOTIATION_CMD] = "dummyValue195" # static value
        dummyDict[InterfaceConfigConstants.PPP_IPV6_NEGOTIATION_CMD] = "dummyValue196" # static value
        dummyDict[InterfaceConfigConstants.PPP_MPLS_NEGOTIATION_CMD] = "dummyValue197" # static value
        dummyDict[InterfaceConfigConstants.PPP_OSI_NEGOTIATION_CMD] = InterfaceConfigConstants.PPP_OSI_NEGOTIATION_ENABLE # constant value
        dummyDict[InterfaceConfigConstants.PROTOCOL_HANDLE_CMD] = "dummyValue199" # static value
        dummyDict[InterfaceConfigConstants.PROTOCOL_NAME_CMD] = "dummyValue200" # static value
        dummyDict[InterfaceConfigConstants.PVC_INCR_MODE_CMD] = InterfaceConfigConstants.PVC_INCR_MODE_VCI # constant value
        dummyDict[InterfaceConfigConstants.QINQ_INCR_MODE_CMD] = InterfaceConfigConstants.QINQ_INCR_MODE_INNER # constant value
        dummyDict[InterfaceConfigConstants.QOS_BYTE_OFFSET_CMD] = "dummyValue203" # static value
        dummyDict[InterfaceConfigConstants.QOS_PACKET_TYPE_CMD] = InterfaceConfigConstants.QOS_PACKET_TYPE_ETHERNET # constant value
        dummyDict[InterfaceConfigConstants.QOS_PATTERN_MASK_CMD] = "dummyValue205" # static value
        dummyDict[InterfaceConfigConstants.QOS_PATTERN_MATCH_CMD] = "dummyValue206" # static value
        dummyDict[InterfaceConfigConstants.QOS_PATTERN_OFFSET_CMD] = "dummyValue207" # static value
        dummyDict[InterfaceConfigConstants.QOS_STATS_CMD] = "dummyValue208" # static value
        dummyDict[InterfaceConfigConstants.ROUTER_SOLICITATION_RETRIES_CMD] = "dummyValue209" # static value
        dummyDict[InterfaceConfigConstants.RPR_HEC_SEED_CMD] = "dummyValue210" # static value
        dummyDict[InterfaceConfigConstants.RX_C2_CMD] = "dummyValue211" # static value
        dummyDict[InterfaceConfigConstants.RX_FCS_CMD] = InterfaceConfigConstants.RX_FCS_OPT_16 # constant value
        dummyDict[InterfaceConfigConstants.RX_SCRAMBLING_CMD] = "dummyValue213" # static value
        dummyDict[InterfaceConfigConstants.SEND_PING_CMD] = "dummyValue214" # static value
        dummyDict[InterfaceConfigConstants.SEND_ROUTER_SOLICITATION_CMD] = "dummyValue215" # static value
        dummyDict[InterfaceConfigConstants.SEND_SETS_MODE_CMD] = InterfaceConfigConstants.SEND_SETS_MODE_ALTERNATE # constant value
        dummyDict[InterfaceConfigConstants.SEQUENCE_CHECKING_CMD] = "dummyValue217" # static value
        dummyDict[InterfaceConfigConstants.SEQUENCE_NUM_OFFSET_CMD] = "dummyValue218" # static value
        dummyDict[InterfaceConfigConstants.SIGNATURE_CMD] = "dummyValue219" # static value
        dummyDict[InterfaceConfigConstants.SIGNATURE_MASK_CMD] = "dummyValue220" # static value
        dummyDict[InterfaceConfigConstants.SIGNATURE_OFFSET_CMD] = "dummyValue221" # static value
        dummyDict[InterfaceConfigConstants.SIGNATURE_START_OFFSET_CMD] = "dummyValue222" # static value
        dummyDict[InterfaceConfigConstants.SINGLE_ARP_PER_GATEWAY_CMD] = "dummyValue223" # static value
        dummyDict[InterfaceConfigConstants.SINGLE_NS_PER_GATEWAY_CMD] = "dummyValue224" # static value
        dummyDict[InterfaceConfigConstants.SITE_ID_CMD] = "dummyValue225" # static value
        dummyDict[InterfaceConfigConstants.SPEED_CMD] = InterfaceConfigConstants.SPEED_ETHER10 # constant value
        dummyDict[InterfaceConfigConstants.SRC_MAC_ADDR_CMD] = "dummyValue227" # static value
        dummyDict[InterfaceConfigConstants.SRC_MAC_ADDR_STEP_CMD] = "dummyValue228" # static value
        dummyDict[InterfaceConfigConstants.START_ERROR_INSERTION_CMD] = "dummyValue229" # static value
        dummyDict[InterfaceConfigConstants.STATIC_ATM_HEADER_ENCAPSULATION_CMD] = InterfaceConfigConstants.STATIC_ATM_HEADER_ENCAPSULATION_LLC_BRIDGED_ETH_FCS # constant value
        dummyDict[InterfaceConfigConstants.STATIC_ATM_RANGE_COUNT_CMD] = "dummyValue231" # static value
        dummyDict[InterfaceConfigConstants.STATIC_DLCI_COUNT_MODE_CMD] = InterfaceConfigConstants.STATIC_DLCI_COUNT_MODE_FIXED # constant value
        dummyDict[InterfaceConfigConstants.STATIC_DLCI_REPEAT_COUNT_CMD] = "dummyValue233" # static value
        dummyDict[InterfaceConfigConstants.STATIC_DLCI_VALUE_CMD] = "dummyValue234" # static value
        dummyDict[InterfaceConfigConstants.STATIC_DLCI_VALUE_STEP_CMD] = "dummyValue235" # static value
        dummyDict[InterfaceConfigConstants.STATIC_ENABLE_CMD] = "dummyValue236" # static value
        dummyDict[InterfaceConfigConstants.STATIC_FR_RANGE_COUNT_CMD] = "dummyValue237" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IG_ATM_ENCAP_CMD] = InterfaceConfigConstants.STATIC_IG_ATM_ENCAP_LLCROUTEDCLIP # constant value
        dummyDict[InterfaceConfigConstants.STATIC_IG_INTERFACE_ENABLE_LIST_CMD] = "dummyValue239" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IG_INTERFACE_HANDLE_LIST_CMD] = "dummyValue240" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IG_IP_TYPE_CMD] = InterfaceConfigConstants.STATIC_IG_IP_TYPE_IPV4 # constant value
        dummyDict[InterfaceConfigConstants.STATIC_IG_RANGE_COUNT_CMD] = "dummyValue242" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IG_VLAN_ENABLE_CMD] = "dummyValue243" # static value
        dummyDict[InterfaceConfigConstants.STATIC_INDIRECT_CMD] = "dummyValue244" # static value
        dummyDict[InterfaceConfigConstants.STATIC_INTF_HANDLE_CMD] = "dummyValue245" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IP_DST_ADDR_CMD] = "dummyValue246" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IP_DST_COUNT_CMD] = "dummyValue247" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IP_DST_COUNT_STEP_CMD] = "dummyValue248" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IP_DST_INCREMENT_CMD] = "dummyValue249" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IP_DST_INCREMENT_STEP_CMD] = "dummyValue250" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IP_DST_PREFIX_LEN_CMD] = "dummyValue251" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IP_DST_PREFIX_LEN_STEP_CMD] = "dummyValue252" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IP_DST_RANGE_STEP_CMD] = "dummyValue253" # static value
        dummyDict[InterfaceConfigConstants.STATIC_IP_RANGE_COUNT_CMD] = "dummyValue254" # static value
        dummyDict[InterfaceConfigConstants.STATIC_L3_PROTOCOL_CMD] = InterfaceConfigConstants.STATIC_L3_PROTOCOL_IPV4 # constant value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_COUNT_PER_VC_CMD] = "dummyValue256" # static value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_INCR_PER_VC_VLAN_MODE_CMD] = InterfaceConfigConstants.STATIC_LAN_INCR_PER_VC_VLAN_MODE_FIXED # constant value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_INTERMEDIATE_OBJREF_CMD] = "dummyValue258" # static value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_MAC_RANGE_MODE_CMD] = InterfaceConfigConstants.STATIC_LAN_MAC_RANGE_MODE_NORMAL # constant value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_NUMBER_OF_VCS_CMD] = "dummyValue260" # static value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_RANGE_COUNT_CMD] = "dummyValue261" # static value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_SKIP_VLAN_ID_ZERO_CMD] = "dummyValue262" # static value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_TPID_CMD] = InterfaceConfigConstants.STATIC_LAN_TPID_0X8100 # constant value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_VLAN_PRIORITY_CMD] = "dummyValue264" # static value
        dummyDict[InterfaceConfigConstants.STATIC_LAN_VLAN_STACK_COUNT_CMD] = "dummyValue265" # static value
        dummyDict[InterfaceConfigConstants.STATIC_MAC_DST_CMD] = "dummyValue266" # static value
        dummyDict[InterfaceConfigConstants.STATIC_MAC_DST_COUNT_CMD] = "dummyValue267" # static value
        dummyDict[InterfaceConfigConstants.STATIC_MAC_DST_COUNT_STEP_CMD] = "dummyValue268" # static value
        dummyDict[InterfaceConfigConstants.STATIC_MAC_DST_MODE_CMD] = InterfaceConfigConstants.STATIC_MAC_DST_MODE_FIXED # constant value
        dummyDict[InterfaceConfigConstants.STATIC_MAC_DST_STEP_CMD] = "dummyValue270" # static value
        dummyDict[InterfaceConfigConstants.STATIC_PVC_COUNT_CMD] = "dummyValue271" # static value
        dummyDict[InterfaceConfigConstants.STATIC_PVC_COUNT_STEP_CMD] = "dummyValue272" # static value
        dummyDict[InterfaceConfigConstants.STATIC_RANGE_PER_SPOKE_CMD] = "dummyValue273" # static value
        dummyDict[InterfaceConfigConstants.STATIC_SITE_ID_CMD] = "dummyValue274" # static value
        dummyDict[InterfaceConfigConstants.STATIC_SITE_ID_ENABLE_CMD] = "dummyValue275" # static value
        dummyDict[InterfaceConfigConstants.STATIC_SITE_ID_STEP_CMD] = "dummyValue276" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VCI_CMD] = "dummyValue277" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VCI_INCREMENT_CMD] = "dummyValue278" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VCI_INCREMENT_STEP_CMD] = "dummyValue279" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VCI_STEP_CMD] = "dummyValue280" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VLAN_ENABLE_CMD] = "dummyValue281" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VLAN_ID_CMD] = "dummyValue282" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VLAN_ID_MODE_CMD] = InterfaceConfigConstants.STATIC_VLAN_ID_MODE_FIXED # constant value
        dummyDict[InterfaceConfigConstants.STATIC_VLAN_ID_STEP_CMD] = "dummyValue284" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VPI_CMD] = "dummyValue285" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VPI_INCREMENT_CMD] = "dummyValue286" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VPI_INCREMENT_STEP_CMD] = "dummyValue287" # static value
        dummyDict[InterfaceConfigConstants.STATIC_VPI_STEP_CMD] = "dummyValue288" # static value
        dummyDict[InterfaceConfigConstants.TARGET_LINK_LAYER_ADDRESS_CMD] = "dummyValue289" # static value
        dummyDict[InterfaceConfigConstants.TRANSMIT_CLOCK_SOURCE_CMD] = InterfaceConfigConstants.TRANSMIT_CLOCK_SOURCE_INTERNAL # constant value
        dummyDict[InterfaceConfigConstants.TRANSMIT_MODE_CMD] = InterfaceConfigConstants.TRANSMIT_MODE_ADVANCED # constant value
        dummyDict[InterfaceConfigConstants.TX_C2_CMD] = "dummyValue292" # static value
        dummyDict[InterfaceConfigConstants.TX_FCS_CMD] = InterfaceConfigConstants.TX_FCS_OPT_16 # constant value
        dummyDict[InterfaceConfigConstants.TX_GAP_CONTROL_MODE_CMD] = InterfaceConfigConstants.TX_GAP_CONTROL_MODE_FIXED # constant value
        dummyDict[InterfaceConfigConstants.TX_IGNORE_RX_LINK_FAULTS_CMD] = "dummyValue295" # static value
        dummyDict[InterfaceConfigConstants.TX_LANES_CMD] = "dummyValue296" # static value
        dummyDict[InterfaceConfigConstants.TX_RX_SYNC_STATS_ENABLE_CMD] = "dummyValue297" # static value
        dummyDict[InterfaceConfigConstants.TX_RX_SYNC_STATS_INTERVAL_CMD] = "dummyValue298" # static value
        dummyDict[InterfaceConfigConstants.TX_SCRAMBLING_CMD] = "dummyValue299" # static value
        dummyDict[InterfaceConfigConstants.TYPE_A_ORDERED_SETS_CMD] = InterfaceConfigConstants.TYPE_A_ORDERED_SETS_LOCAL_FAULT # constant value
        dummyDict[InterfaceConfigConstants.TYPE_B_ORDERED_SETS_CMD] = InterfaceConfigConstants.TYPE_B_ORDERED_SETS_LOCAL_FAULT # constant value
        dummyDict[InterfaceConfigConstants.USE_VPN_PARAMETERS_CMD] = "dummyValue302" # static value
        dummyDict[InterfaceConfigConstants.VCI_CMD] = "dummyValue303" # static value
        dummyDict[InterfaceConfigConstants.VCI_COUNT_CMD] = "dummyValue304" # static value
        dummyDict[InterfaceConfigConstants.VCI_STEP_CMD] = "dummyValue305" # static value
        dummyDict[InterfaceConfigConstants.VLAN_CMD] = "dummyValue306" # static value
        dummyDict[InterfaceConfigConstants.VLAN_ID_CMD] = "dummyValue307" # static value
        dummyDict[InterfaceConfigConstants.VLAN_ID_COUNT_CMD] = "dummyValue308" # static value
        dummyDict[InterfaceConfigConstants.VLAN_ID_INNER_CMD] = "dummyValue309" # static value
        dummyDict[InterfaceConfigConstants.VLAN_ID_INNER_COUNT_CMD] = "dummyValue310" # static value
        dummyDict[InterfaceConfigConstants.VLAN_ID_INNER_MODE_CMD] = InterfaceConfigConstants.VLAN_ID_INNER_MODE_FIXED # constant value
        dummyDict[InterfaceConfigConstants.VLAN_ID_INNER_STEP_CMD] = "dummyValue312" # static value
        dummyDict[InterfaceConfigConstants.VLAN_ID_LIST_CMD] = "dummyValue313" # static value
        dummyDict[InterfaceConfigConstants.VLAN_ID_MODE_CMD] = InterfaceConfigConstants.VLAN_ID_MODE_FIXED # constant value
        dummyDict[InterfaceConfigConstants.VLAN_ID_STEP_CMD] = "dummyValue315" # static value
        dummyDict[InterfaceConfigConstants.VLAN_PROTOCOL_ID_CMD] = InterfaceConfigConstants.VLAN_PROTOCOL_ID_0X8100 # constant value
        dummyDict[InterfaceConfigConstants.VLAN_TPID_CMD] = InterfaceConfigConstants.VLAN_TPID_0X8100 # constant value
        dummyDict[InterfaceConfigConstants.VLAN_USER_PRIORITY_CMD] = "dummyValue318" # static value
        dummyDict[InterfaceConfigConstants.VLAN_USER_PRIORITY_STEP_CMD] = "dummyValue319" # static value
        dummyDict[InterfaceConfigConstants.VPI_CMD] = "dummyValue320" # static value
        dummyDict[InterfaceConfigConstants.VPI_COUNT_CMD] = "dummyValue321" # static value
        dummyDict[InterfaceConfigConstants.VPI_STEP_CMD] = "dummyValue322" # static value

        api = device.getApi(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        api.interface_config(dummyDict)
    """
    def interface_config(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::interface_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def interface_config_additional_fcoe_stat_1(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_additional_fcoe_stat_2(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_addresses_per_svlan(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_addresses_per_vci(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_addresses_per_vlan(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_addresses_per_vpi(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_arp(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_arp_on_linkup(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_arp_refresh_interval(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_arp_req_retries(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_arp_req_timer(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_arp_send_req(self, bool_opt):
        """
        This is the method the command: interface_config option arp_send_req
        Description:Whether sending an ARP request to the DUT is enabled. You can use this basic function to ensure correct addressing of the interfaces. By default, the ARP is sent on the Ethernet port. For IPv4 interfaces the arp request is sent to the gateway. For IPv6 interfaces a router solicitation is sent to 'all routers' multicast address. This option takes a list of values when -port_handle is a list of port handles. Valid options are: 0 - Disable (DEFAULT). 1 - Enable
        Constants Available: ARP_SEND_REQ_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.ARP_SEND_REQ_CMD : bool_opt})

    def interface_config_atm_enable_coset(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_enable_pattern_matching(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_encapsulation(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_filler_cell(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_interface_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_packet_decode_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_reassembly_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_auto_detect_instrumentation_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_autonegotiation(self, opt):
        """
        This is the method the command: interface_config option autonegotiation
        Description:Whether to enable auto-negotiation on each interface. When the new IxNetwork TCL API is used and the autonegotiation is enabled, the autonegotiation is performed using all the existing Ethernet speed/duplex combinations: 1000, 100full, 100half, 10full and 10half. The feature from HLTAPI 2.90, which allowed the user to select only a subset of speed/duplex combinations to be used in the autonegotiation process, is not supported by IxNetwork at this moment. If the autonegotition is enabled, the speed and duplex options are ignored. This option takes a list of values when -port_handle is a list of port handles. Valid options are: 0 - Disable 1 - Enable (DEFAULT)
        Constants Available: AUTONEGOTIATION_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.AUTONEGOTIATION_CMD : opt})

    def interface_config_bad_blocks_number(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_bert_configuration(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_bert_error_insertion(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_check_gateway_exists(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_check_opposite_ip_version(self, bool_opt):
        """
        This is the method the command: interface_config option check_opposite_ip_version
        Description:This parameter is used when trying to configure dual stack interfaces. For example, if an interface_config with ipv4 parameters is called, the procedure will search for an existing interface with the same MAC address and ipv6 settings. If such an interface is found and check_opposite_ip_version is set to 1 this interface will have the ipv4 settings created or modified if ipv4 settings already exists. In case check_opposite_ip_version is set to 0, an error specifying that the MAC address is unique per port will be thrown.
        Constants Available: CHECK_OPPOSITE_IP_VERSION_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.CHECK_OPPOSITE_IP_VERSION_CMD : bool_opt})

    def interface_config_clocksource(self, opt):
        """
        This is the method the command: interface_config option clocksource
        Description:Clock source for SONET interfaces at which each interface is configured. This option takes a list of values when -port_handle is a list of port handles.
            Valid options are:
            internal: Transmit Clocking Internal
            loop: Transmit Clocking Recovered
            external: Transmit Clocking External (77.76MHz)
        Constants Available: CLOCKSOURCE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.CLOCKSOURCE_CMD : opt})

    def interface_config_connected_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_connected_to_handle(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_data_integrity(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_duplex(self, opt):
        """
        This is the method the command: interface_config option duplex
        Description:Whether duplex is full or half. This option takes a list of values when -port_handle is a list of port handlesValid options are:
            half: half duplex
            full: full duplex
            auto: selects both full and half duplex
        Constants Available: DUPLEX_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.DUPLEX_CMD : opt})

    def interface_config_enable_data_center_shared_stats(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_flow_control(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_loopback(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_ndp(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_rs_fec(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_rs_fec_statistics(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_attempt_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_attempt_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_attempt_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_attempt_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_diconnect_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_disconnect_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_disconnect_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_disconnect_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_credit_starvation_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_fixed_delay_value(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_force_errors(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_max_delay_for_random_value(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_min_delay_for_random_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_no_rrdy_after(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_rrdy_response_delays(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_tx_ignore_available_credits(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_tx_ignore_rx_link_faults(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fcoe_flow_control_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fcoe_priority_group_size(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fcoe_priority_groups(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fcoe_support_data_center_mode(self, bool_opt):
        """
        This is the method the command: interface_config option fcoe_support_data_center_mode
        Description:Not defined
        Constants Available: FCOE_SUPPORT_DATA_CENTER_MODE_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FCOE_SUPPORT_DATA_CENTER_MODE_CMD : bool_opt})

    def interface_config_flow_control_directed_addr(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_framing(self, opt):
        """
        This is the method the command: interface_config option framing
        Description:POS interface type. This option takes a list of values when -port_handle is a list of port handles. Valid options are: sonet sdh
            Valid options are:
            sonet
            sdh
        Constants Available: FRAMING_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.FRAMING_CMD : opt})

    def interface_config_gateway(self, ipv4):
        """
        This is the method the command: interface_config option gateway
        Description:List of IP addresses that configure the addresses of the gateway (that is, the DUT interface IP addresses). This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: GATEWAY_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.GATEWAY_CMD : ipv4})

    def interface_config_gateway_incr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_gateway_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def interface_config_good_blocks_number(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_checksum_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_dst_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_dst_ip_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ip_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ip_addr_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ip_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ipv6_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ipv6_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ipv6_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_key_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_key_in(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_key_out(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_seq_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ieee_media_defaults(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ignore_link(self, bool_opt):
        """
        This is the method the command: interface_config option ignore_link
        Description:Transmit ignores the link status on Ethernet, POS or ATM port if set to true.This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: IGNORE_LINK_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IGNORE_LINK_CMD : bool_opt})

    def interface_config_integrity_signature(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_integrity_signature_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_interface_handle(self, opt):
        """
        This is the method the command: interface_config option interface_handle
        Description:This parameter takes a list of interface handles. It is used with -mode modify in order to modify L2-3 settings when -l23_config_type is protocol_interface. Parameter valid only with IxTclNetwork. If the interface handle represents a routed interface, the interface cannot be modified into a connected interface (it can only be routed to another connected interface).
        Constants Available: INTERFACE_HANDLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.INTERFACE_HANDLE_CMD : opt})

    def interface_config_internal_ppm_adjust(self, opt):
        """
        This is the method the command: interface_config option internal_ppm_adjust
        Description:Parameter valid only when transmit_clock_source is set on internal_ppm_adj. Specifies the PPM value to adjust the IEEE clock frequency tolerance.
        Constants Available: INTERNAL_PPM_ADJUST_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.INTERNAL_PPM_ADJUST_CMD : opt})

    def interface_config_intf_ip_addr(self, ip):
        """
        This is the method the command: interface_config option intf_ip_addr
        Description:List of IP addresses that configure each of the traffic generation tool interfaces.This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: INTF_IP_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.INTF_IP_ADDR_CMD : ip})

    def interface_config_intf_ip_addr_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def interface_config_intf_mode(self, opt):
        """
        This is the method the command: interface_config option intf_mode
        Description:SONET header type. This option takes a list of values when -port_handle is a list of port handles. Please check Ixia Hardware and Reference Manual for the list of cards that support this feature.
            Valid options are:
            atm
            pos_hdlc
            pos_ppp: The default value for cards that support ATM and POS is pos_ppp.
            ethernet_vm: This is specific for IxVM cards.
            ethernet
            ethernet_fcoe: If speed is configured to ether10000lan the port mode will be tenGigLanFcoe. If speed is configured to ether10000wan tenGigWanFcoe. Otherwise the port mode will be ethernetFcoe. Valid only with ixnetwork API.
            multis: This is specific for Multis cards (10G/40G/100G).Valid only with ixnetwork new API.
            multis_fcoe: FCoE for Multis cards (10G/40G/100G).Valid only with ixnetwork new API.
            rame_relay1490
            frame_relay2427
            frame_relay_cisco
            srp
            srp_cisco
            rpr
            fc: Fiber Channel
            gfp
            bert: The bert option is valid only for 40Gig/100Gig cards.
        Constants Available: INTF_MODE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.INTF_MODE_CMD : opt})

    def interface_config_intrinsic_latency_adjustment(self, opt):
        """
        This is the method the command: interface_config option intrinsic_latency_adjustment
        Description:This option enables the Intrinsic Latency Adjustment for poets that support this feature. Valid values are:0 - Not enabled (DEFAULT)1 - Enabled
        Constants Available: INTRINSIC_LATENCY_ADJUSTMENT_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.INTRINSIC_LATENCY_ADJUSTMENT_CMD : opt})

    def interface_config_ipv4_attempt_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_attempt_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_attempt_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_attempt_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_diconnect_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_disconnect_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_disconnect_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_disconnect_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_manual_gateway_mac(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_manual_gateway_mac_step(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_re_send_arp_on_link_up(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_resolve_gateway(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_send_arp_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_send_arp_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_send_arp_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_send_arp_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_attempt_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_attempt_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_attempt_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_attempt_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_ns_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_ns_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_ns_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_ns_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_diconnect_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_disconnect_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_disconnect_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_disconnect_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_gateway(self, ip):
        """
        This is the method the command: interface_config option ipv6_gateway
        Description:List of IPV6 addresses that configure the addresses of the gateway (that is, the DUT interface IP addresses). This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: IPV6_GATEWAY_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_GATEWAY_CMD : ip})

    def interface_config_ipv6_gateway_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_intf_addr(self, ip):
        """
        This is the method the command: interface_config option ipv6_intf_addr
        Description:List of IPv6 addresses that configure each of the traffic generation tool interfaces.This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: IPV6_INTF_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_INTF_ADDR_CMD : ip})

    def interface_config_ipv6_intf_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_loopback_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_manual_gateway_mac(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_manual_gateway_mac_step(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_prefix_length(self, opt):
        """
        This is the method the command: interface_config option ipv6_prefix_length
        Description:The mask width of the IPv6 address in an interface. This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: IPV6_PREFIX_LENGTH_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.IPV6_PREFIX_LENGTH_CMD : opt})

    def interface_config_ipv6_re_send_ns_on_link_up(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_resolve_gateway(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_send_ns_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_send_ns_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_send_ns_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_send_ns_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_l23_config_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_laser_on(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_link_training(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_loop_continuously(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_loop_count_number(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_master_slave_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_mode(self, mode):
        """
        This is the method the command: interface_config option mode
        Description:Action to be taken on the interface selected. This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs. Valid options are:configdestroy - clear all interfaces before configuring new ones.modify - Valid only when using IxTclNetwork. When ::::interface_config is provided with -port_handle parameter, -mode modify and other supported parameters, except -interface_handle, the modification is supported for L1 parameters only. When ::::interface_config is provided with -port_handle parameter, -mode modify and other supported parameters, including -interface_handle, the modification is supported for L2-L3 parameters also, but only for protocol interfaces (-l23_config_type protocol_interface). Action to be taken on the interface selected. This option takes a list of values when -port_handle is a list of port handles.
            Valid options are:
            config
            modify: Valid only when using IxTclNetwork. When ::ixia::interface_config is provided with -port_handle parameter, -mode modify and other supported parameters, except -interface_handle, the modification is supported for L1 parameters only. When ::ixia::interface_config is provided with -port_handle parameter, -mode modify and other supported parameters, including -interface_handle, the modification is supported for L2-L3 parameters also, but only for protocol interfaces (-l23_config_type protocol_interface).
            destroy: clear all interfaces before configuring new ones.
        Constants Available: MODE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        mode --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.MODE_CMD : mode})

    def interface_config_mss(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_mtu(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ndp_send_req(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_netmask(self, ip):
        """
        This is the method the command: interface_config option netmask
        Description:Network mask used for IP address configuration of the traffic generation tool interfaces. This option is valid for the old and the new APIs.
        Constants Available: NETMASK_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.NETMASK_CMD : ip})

    def interface_config_no_write(self, flag):
        return self.logger.log_unimplemented_method()

    def interface_config_notify_mac_move(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ns_on_linkup(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_op_mode(self, opt):
        """
        This is the method the command: interface_config option op_mode
        Description:Operational mode on the interface. This option takes a list of values when -port_handle is a list of port handles. Valid options are: loopback normal monitor sim_disconnect
            Valid options are:
            loopback
            normal
            monitor
            sim_disconnect
        Constants Available: OP_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.OP_MODE_CMD : opt})

    def interface_config_override_existence_check(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_override_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_enabled_continuous(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_lane(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_marker_fields(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_period(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_period_type(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_repeat(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_sync_bits(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_128k_bin_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_encap(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split1_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split1_offset(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split1_offset_from(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split1_width(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split2_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split2_offset(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split2_offset_from(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split2_width(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split3_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split3_offset(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split3_offset_from(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split3_width(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_phy_mode(self, opt):
        """
        This is the method the command: interface_config option phy_mode
        Description:For dual mode ethernet interfaces only. This option takes a list of values when -port_handle is a list of port handles. Valid options are: copper fiber sgmii (valid only for IxNetwork)
        Constants Available: PHY_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config(opt)

    def interface_config_ping_dst(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_port_handle(self, port_list):
        """
        This is the method the command: interface_config option port_handle
        Description:List of ports of which to take ownership and perform configuration. This option takes a list of port handles.
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork [M], IxNetwork-NGPF
        Keyword arguments:
        port_list --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.PORT_HANDLE_CMD : port_list})

    def interface_config_port_rx_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_ipv4_address(self, ip):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_ipv4_negotiation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_ipv6_negotiation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_mpls_negotiation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_osi_negotiation(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_protocol_handle(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_protocol_name(self, name):
        return self.logger.log_unimplemented_method()

    def interface_config_pvc_incr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qinq_incr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_byte_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_packet_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_pattern_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_pattern_match(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_pattern_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_stats(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_router_solicitation_retries(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_rpr_hec_seed(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_rx_c2(self, opt):
        """
        This is the method the command: interface_config option rx_c2
        Description:Receive Path Signal Label for the Ixia interface. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: RX_C2_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.RX_C2_CMD : opt})

    def interface_config_rx_fcs(self, opt):
        """
        This is the method the command: interface_config option rx_fcs
        Description:FCS value (16 or 32) for the receiving side of each interfaces. This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs. Valid options are:16 32
        Constants Available: RX_FCS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.RX_FCS_CMD : opt})

    def interface_config_rx_scrambling(self, bool_opt):
        """
        This is the method the command: interface_config option rx_scrambling
        Description:Whether to enable data scrambling in the SONET framer of the Ixia interface. (SPE Scrambling = X^43+1). This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs. Valid options are:0 - Disable1 - Enable (DEFAULT)
        Constants Available: RX_SCRAMBLING_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.RX_SCRAMBLING_CMD : bool_opt})

    def interface_config_send_ping(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_send_router_solicitation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_send_sets_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_sequence_checking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_sequence_num_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_signature(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_signature_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_signature_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_signature_start_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_single_arp_per_gateway(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_single_ns_per_gateway(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_site_id(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_speed(self, opt):
        """
        This is the method the command: interface_config option speed
        Description:Speed at which each interface is configured. This option takes a list of values when -port_handle is a list of port handles.
        Constants Available: SPEED_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SPEED_CMD : opt})

    def interface_config_src_mac_addr(self, mac):
        """
        This is the method the command: interface_config option src_mac_addr
        Description:MAC address of the port. This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs. Valid formats are:{00 00 00 00 00 00}, 00:00:00:00:00:00, 0000.0000.0000, 00.00.00.00.00.00, {0000 0000 0000}
        Constants Available: SRC_MAC_ADDR_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.SRC_MAC_ADDR_CMD : mac})

    def interface_config_src_mac_addr_step(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_start_error_insertion(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_static_atm_header_encapsulation(self, opt):
        """
        This is the method the command: interface_config option static_atm_header_encapsulation
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0.
        Constants Available: STATIC_ATM_HEADER_ENCAPSULATION_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_ATM_HEADER_ENCAPSULATION_CMD : opt})

    def interface_config_static_atm_range_count(self, numeric):
        """
        This is the method the command: interface_config option static_atm_range_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. Configure the number of ATM static endpoints to create.
        Constants Available: STATIC_ATM_RANGE_COUNT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_ATM_RANGE_COUNT_CMD : numeric})

    def interface_config_static_dlci_count_mode(self, opt):
        """
        This is the method the command: interface_config option static_dlci_count_mode
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1
        Constants Available: STATIC_DLCI_COUNT_MODE_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_DLCI_COUNT_MODE_CMD : opt})

    def interface_config_static_dlci_repeat_count(self, numeric):
        """
        This is the method the command: interface_config option static_dlci_repeat_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_fr_range_count > 0. Step of dlci_repeat_count between ranges.
        Constants Available: STATIC_DLCI_REPEAT_COUNT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_DLCI_REPEAT_COUNT_CMD : numeric})

    def interface_config_static_dlci_value(self, range):
        """
        This is the method the command: interface_config option static_dlci_value
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_fr_range_count > 0. The Data Link Connection Identifier (DLCI) value.
        Constants Available: STATIC_DLCI_VALUE_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_DLCI_VALUE_CMD : range})

    def interface_config_static_dlci_value_step(self, numeric):
        """
        This is the method the command: interface_config option static_dlci_value_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_fr_range_count > 0. Step of dlci values between ranges.
        Constants Available: STATIC_DLCI_VALUE_STEP_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_DLCI_VALUE_STEP_CMD : numeric})

    def interface_config_static_enable(self, bool_opt):
        """
        This is the method the command: interface_config option static_enable
        Description:Enables creation of IxNetwork static endpoints. If this parameter is 1, only IxNetwork static endpoints will be created. All other parameters that configure protocol interfaces (-l23_config_type protocol_interface) and SM static endpoints (-l23_config_type static_endpoint) will be ignored. Valid choices are: 0 - disable (DEFAULT) 1 - enable
        Constants Available: STATIC_ENABLE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_ENABLE_CMD : bool_opt})

    def interface_config_static_fr_range_count(self, numeric):
        """
        This is the method the command: interface_config option static_fr_range_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1. Number of Frame Relay static endpoint ranges to be created.
        Constants Available: STATIC_FR_RANGE_COUNT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_FR_RANGE_COUNT_CMD : numeric})

    def interface_config_static_ig_atm_encap(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_interface_enable_list(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_interface_handle_list(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_ip_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_range_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_vlan_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_indirect(self, bool_opt):
        """
        This is the method the command: interface_config option static_indirect
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. Enables/Disables creation atm/fr ranges that will be mapped to the lan static endpoint. The atm_range_count /fr_range_count parameter will must be at least equal to $static_lan_range_count divided by $static_range_per_spoke . If -static_lan_intermediate_objref is specified, the atm/fr ranges specified in static_lan_intermediate_objref will be used.
            Valid options are:
            0: disable
            1: enable (DEFAULT)
        Constants Available: STATIC_INDIRECT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_INDIRECT_CMD : bool_opt})

    def interface_config_static_intf_handle(self, opt):
        """
        This is the method the command: interface_config option static_intf_handle
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. Interface handles to be used by IP type. These handles are returned by interface_config when - l23_config_type is protocol_interface and -static_enable is 0. In order for an interface to be a valid handle it must have the same encapsulations as the static endpoint ip range (same IP type, number of vlans if any).
        Constants Available: STATIC_INTF_HANDLE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_INTF_HANDLE_CMD : opt})

    def interface_config_static_ip_dst_addr(self, ip):
        """
        This is the method the command: interface_config option static_ip_dst_addr
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. The first IP address in the range.
        Constants Available: STATIC_IP_DST_ADDR_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IP_DST_ADDR_CMD : ip})

    def interface_config_static_ip_dst_count(self, range):
        """
        This is the method the command: interface_config option static_ip_dst_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. Number of IPs to be generated on an IP range.
        Constants Available: STATIC_IP_DST_COUNT_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IP_DST_COUNT_CMD : range})

    def interface_config_static_ip_dst_count_step(self, numeric):
        """
        This is the method the command: interface_config option static_ip_dst_count_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. Step to increment - static_ip_dst_count between ranges.
        Constants Available: STATIC_IP_DST_COUNT_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IP_DST_COUNT_STEP_CMD : numeric})

    def interface_config_static_ip_dst_increment(self, ip):
        """
        This is the method the command: interface_config option static_ip_dst_increment
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. IP step used between IP on same IP range.
        Constants Available: STATIC_IP_DST_INCREMENT_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IP_DST_INCREMENT_CMD : ip})

    def interface_config_static_ip_dst_increment_step(self, ip):
        """
        This is the method the command: interface_config option static_ip_dst_increment_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. Step to increment -static_ip_dst_increment between ranges.
        Constants Available: STATIC_IP_DST_INCREMENT_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IP_DST_INCREMENT_STEP_CMD : ip})

    def interface_config_static_ip_dst_prefix_len(self, range):
        """
        This is the method the command: interface_config option static_ip_dst_prefix_len
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. The numbers of bits in the network mask
        Constants Available: STATIC_IP_DST_PREFIX_LEN_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IP_DST_PREFIX_LEN_CMD : range})

    def interface_config_static_ip_dst_prefix_len_step(self, numeric):
        """
        This is the method the command: interface_config option static_ip_dst_prefix_len_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. Step to increment the number of bits in the network masks to be used with the IP address between ranges.
        Constants Available: STATIC_IP_DST_PREFIX_LEN_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IP_DST_PREFIX_LEN_STEP_CMD : numeric})

    def interface_config_static_ip_dst_range_step(self, ip):
        """
        This is the method the command: interface_config option static_ip_dst_range_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. IP step between IP ranges.
        Constants Available: STATIC_IP_DST_RANGE_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IP_DST_RANGE_STEP_CMD : ip})

    def interface_config_static_ip_range_count(self, numeric):
        """
        This is the method the command: interface_config option static_ip_range_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. Number of IP static endpoint ranges to be created.
        Constants Available: STATIC_IP_RANGE_COUNT_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_IP_RANGE_COUNT_CMD : numeric})

    def interface_config_static_l3_protocol(self, opt):
        """
        This is the method the command: interface_config option static_l3_protocol
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_ip_range_count > 0. The IP version number. Valid choices are: ipv4 (DEFAULT) ipv6
        Constants Available: STATIC_L3_PROTOCOL_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_L3_PROTOCOL_CMD : opt})

    def interface_config_static_lan_count_per_vc(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_incr_per_vc_vlan_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_intermediate_objref(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_mac_range_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_number_of_vcs(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_range_count(self, numeric):
        """
        This is the method the command: interface_config option static_lan_range_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1. Number of LAN static endpoint ranges to be created. If any of the following parameters -static_mac_dst, -static_mac_dst_count, -static_mac_dst_mode, -static_site_id, -static_site_id_enable, -static_vlan_enable, -static_vlan_id or -static_vlan_id_mode is present the default value is set to 1.
        Constants Available: STATIC_LAN_RANGE_COUNT_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_LAN_RANGE_COUNT_CMD : numeric})

    def interface_config_static_lan_skip_vlan_id_zero(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_tpid(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_vlan_priority(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_vlan_stack_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_static_mac_dst(self, mac):
        """
        This is the method the command: interface_config option static_mac_dst
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. MAC address used in LAN ranges.
        Constants Available: STATIC_MAC_DST_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_MAC_DST_CMD : mac})

    def interface_config_static_mac_dst_count(self, range):
        """
        This is the method the command: interface_config option static_mac_dst_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. Number of MAC addresses to be generated by an LAN range.
        Constants Available: STATIC_MAC_DST_COUNT_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_MAC_DST_COUNT_CMD : range})

    def interface_config_static_mac_dst_count_step(self, numeric):
        """
        This is the method the command: interface_config option static_mac_dst_count_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. The step to increment static_mac_dst_count between ranges.
        Constants Available: STATIC_MAC_DST_COUNT_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_MAC_DST_COUNT_STEP_CMD : numeric})

    def interface_config_static_mac_dst_mode(self, opt):
        """
        This is the method the command: interface_config option static_mac_dst_mode
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. Valid choices are: increment (DEFAULT) fixed For increment MAC address from LAN range will be incremented.
        Constants Available: STATIC_MAC_DST_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_MAC_DST_MODE_CMD : opt})

    def interface_config_static_mac_dst_step(self, numeric):
        """
        This is the method the command: interface_config option static_mac_dst_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. MAC step between LAN ranges.
        Constants Available: STATIC_MAC_DST_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_MAC_DST_STEP_CMD : numeric})

    def interface_config_static_pvc_count(self, range):
        """
        This is the method the command: interface_config option static_pvc_count
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. Number of ATM PVC to create in a range.
        Constants Available: STATIC_PVC_COUNT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_PVC_COUNT_CMD : range})

    def interface_config_static_pvc_count_step(self, numeric):
        """
        This is the method the command: interface_config option static_pvc_count_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. Step of Permanent Virtual Circuits count (-static_pvc_count) between ATM ranges.
        Constants Available: STATIC_PVC_COUNT_STEP_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_PVC_COUNT_STEP_CMD : numeric})

    def interface_config_static_range_per_spoke(self, range):
        """
        This is the method the command: interface_config option static_range_per_spoke
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. Configure how many lan ranges will use the same atm/fr range. For example: if this parameter is 3, lan ranges 1, 2 and 3 will use atm range 1, lan ranges 4,5 and 6 will use atm range 2 and so on. The atm/fr ranges are taken from static_lan_intermediate_objref if it is specified or created if static_indirect is 1.
        Constants Available: STATIC_RANGE_PER_SPOKE_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_RANGE_PER_SPOKE_CMD : range})

    def interface_config_static_site_id(self, range):
        """
        This is the method the command: interface_config option static_site_id
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_site_id_enable 0 and -static_lan_mac_range_mode normal. The Site ID is implemented for static (and dynamic) routes, including the Static Lan end point. Users can configure traffic streams by grouping routes belonging to the same Site ID.
        Constants Available: STATIC_SITE_ID_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_SITE_ID_CMD : range})

    def interface_config_static_site_id_enable(self, bool_opt):
        """
        This is the method the command: interface_config option static_site_id_enable
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_lan_mac_range_mode normal. Enable site id value for LAN range(s). Valid choices are: 0 (DEFAULT) 1
        Constants Available: STATIC_SITE_ID_ENABLE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_SITE_ID_ENABLE_CMD : bool_opt})

    def interface_config_static_site_id_step(self, numeric):
        """
        This is the method the command: interface_config option static_site_id_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_site_id_enable 0 and -static_lan_mac_range_mode normal. Step of site_id between LAN ranges.
        Constants Available: STATIC_SITE_ID_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_SITE_ID_STEP_CMD : numeric})

    def interface_config_static_vci(self, range):
        """
        This is the method the command: interface_config option static_vci
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. The value for the first ATM Virtual Circuit Identifier (VCI). The VCI value is used with a VPI value - a VPI/VCI pair - to identify a specific ATM link.
        Constants Available: STATIC_VCI_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VCI_CMD : range})

    def interface_config_static_vci_increment(self, range):
        """
        This is the method the command: interface_config option static_vci_increment
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. Increment step used inside an ATM range for vci.
        Constants Available: STATIC_VCI_INCREMENT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VCI_INCREMENT_CMD : range})

    def interface_config_static_vci_increment_step(self, numeric):
        """
        This is the method the command: interface_config option static_vci_increment_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. Step to increment -static_vci_increment between ATM static endpoint ranges.
        Constants Available: STATIC_VCI_INCREMENT_STEP_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VCI_INCREMENT_STEP_CMD : numeric})

    def interface_config_static_vci_step(self, numeric):
        """
        This is the method the command: interface_config option static_vci_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. Step of vci between ATM ranges.
        Constants Available: STATIC_VCI_STEP_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VCI_STEP_CMD : numeric})

    def interface_config_static_vlan_enable(self, bool_opt):
        """
        This is the method the command: interface_config option static_vlan_enable
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. Enable VLAN for LAN ranges. Valid choices are: 1 - enable 0 - disable (DEFAULT)
        Constants Available: STATIC_VLAN_ENABLE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VLAN_ENABLE_CMD : bool_opt})

    def interface_config_static_vlan_id(self, range):
        """
        This is the method the command: interface_config option static_vlan_id
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0. Configure first VLAN ID. If stacked vlans need to be created, a list of values separated by the colon(:) character must be provided to this parameter.
        Constants Available: STATIC_VLAN_ID_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VLAN_ID_CMD : range})

    def interface_config_static_vlan_id_mode(self, opt):
        """
        This is the method the command: interface_config option static_vlan_id_mode
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_vlan_enable 1 and -static_lan_mac_range_mode normal. Select increment or fixed mode for vlan_id value.
            Valid options are:
            fixed: not increment (DEFAULT)
            increment: increment inner and outer
            inner: increment inner
            outer: increment outer
            DEFAULT: fixed
            DEPENDENCIES: Valid in combination with parameter(s)
            'static_enable' | value= '1' |
            'static_vlan_enable' | value= '1' |
            'static_lan_mac_range_mode' | value= 'normal' |
        Constants Available: STATIC_VLAN_ID_MODE_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VLAN_ID_MODE_CMD : opt})

    def interface_config_static_vlan_id_step(self, numeric):
        """
        This is the method the command: interface_config option static_vlan_id_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_lan_range_count > 0 and -static_vlan_enable 1. Step of start VLAN ID between LAN ranges. If stacked vlans need to be created then this parameter must be a list of values separated through the colon(:) character. Each vlan ID will be incremented with coresponding values in this parameter. Example: If static_vlan_id is 1:2:3, static_lan_range_count is 4 and static_vlan_id_step is 2:4:6, four LAN ranges will be created with the following VLAN IDs: 1,2,3, 3,6,9, 5,10,15, 7,14,21.
        Constants Available: STATIC_VLAN_ID_STEP_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VLAN_ID_STEP_CMD : numeric})

    def interface_config_static_vpi(self, range):
        """
        This is the method the command: interface_config option static_vpi
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. The value for the first ATM Virtual Port Identifier (VPI). The VPI value is used with a VCI value - a VPI/VCI pair - to identify a specific ATM virtual link.
        Constants Available: STATIC_VPI_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VPI_CMD : range})

    def interface_config_static_vpi_increment(self, range):
        """
        This is the method the command: interface_config option static_vpi_increment
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. Increment step used inside an ATM range for vpi.
        Constants Available: STATIC_VPI_INCREMENT_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VPI_INCREMENT_CMD : range})

    def interface_config_static_vpi_increment_step(self, numeric):
        """
        This is the method the command: interface_config option static_vpi_increment_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. Step to increment -static_vpi_increment between ATM static endpoint ranges.
        Constants Available: STATIC_VPI_INCREMENT_STEP_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VPI_INCREMENT_STEP_CMD : numeric})

    def interface_config_static_vpi_step(self, numeric):
        """
        This is the method the command: interface_config option static_vpi_step
        Description:Parameter valid only for IxNetwork static endpoints when -static_enable 1 and -static_atm_range_count > 0. Step of vpi between ATM static endpoint ranges.
        Constants Available: STATIC_VPI_STEP_CMD
        Supported:IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.STATIC_VPI_STEP_CMD : numeric})

    def interface_config_target_link_layer_address(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_transmit_clock_source(self, opt):
        """
        This is the method the command: interface_config option transmit_clock_source
        Description:Specifies the clock source for synchronous transmissions. You can set the transmit clock source for Ethernet 10/100/1000/100Gig interfaces. Options internal, bits, loop, external are not supported.
            Valid options are:
            internal: Specifies that a crystal on the interface provides the transmit clock
            bits: Specifies that a Building Integrated Timing Supply is used as the transmit
            loop: Specifies that a clock recovered from the received data is used as the
            external: Specifies that the transmit clock signals are provided by external
            internal_ppm_adj: Adjust the clock PPM within the IEEE clock frequency.
        Constants Available: TRANSMIT_CLOCK_SOURCE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TRANSMIT_CLOCK_SOURCE_CMD : opt})

    def interface_config_transmit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_tx_c2(self, opt):
        """
        This is the method the command: interface_config option tx_c2
        Description:Transmit Path Signal Label for the Ixia interface.This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.
        Constants Available: TX_C2_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TX_C2_CMD : opt})

    def interface_config_tx_fcs(self, opt):
        """
        This is the method the command: interface_config option tx_fcs
        Description:FCS value (16 or 32) for the transmitting side of each interfaces. This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs.Valid options are:16 32
        Constants Available: TX_FCS_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TX_FCS_CMD : opt})

    def interface_config_tx_gap_control_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_tx_ignore_rx_link_faults(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_tx_lanes(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_tx_rx_sync_stats_enable(self, bool_opt):
        """
        This is the method the command: interface_config option tx_rx_sync_stats_enable
        Description:This option starts / stops collecting Tx/Rx Sync stats.Valid options are:0 - stop collecting Sync stats (DEFAULT)1 - start collecting Sync stats
        Constants Available: TX_RX_SYNC_STATS_ENABLE_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TX_RX_SYNC_STATS_ENABLE_CMD : bool_opt})

    def interface_config_tx_rx_sync_stats_interval(self, numeric):
        """
        This is the method the command: interface_config option tx_rx_sync_stats_interval
        Description:This option represents the interval (ms) at which to synchronously freeze TX and RX PGID stats.
        Constants Available: TX_RX_SYNC_STATS_INTERVAL_CMD
        Supported:IxOS/IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TX_RX_SYNC_STATS_INTERVAL_CMD : numeric})

    def interface_config_tx_scrambling(self, bool_opt):
        """
        This is the method the command: interface_config option tx_scrambling
        Description:Whether to enable data scrambling in the SONET framer of the Ixia interface. (SPE Scrambling = X^43+1). This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs. Valid options are:0 - Disable1 - Enable (DEFAULT)
        Constants Available: TX_SCRAMBLING_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.TX_SCRAMBLING_CMD : bool_opt})

    def interface_config_type_a_ordered_sets(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_type_b_ordered_sets(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_use_vpn_parameters(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vci(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vci_count(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vci_step(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan(self, bool_opt):
        """
        This is the method the command: interface_config option vlan
        Description:Whether to enable VLAN on the traffic generation tool interfaces. This option takes a list of values when -port_handle is a list of port handles. This option is valid for the old and the new APIs. Valid options are:1 - Enable0 - Disable (DEFAULT)
        Constants Available: VLAN_CMD
        Supported:IxNetwork-FT, IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.interface_config({InterfaceConfigConstants.VLAN_CMD : bool_opt})

    def interface_config_vlan_id(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_count(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_inner(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_inner_count(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_inner_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_inner_step(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_list(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_protocol_id(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_tpid(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_user_priority(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_user_priority_step(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vpi(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vpi_count(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vpi_step(self, range):
        return self.logger.log_unimplemented_method()


"""
    This is the Constants class for the command: interface_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class InterfaceConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    INTERFACE_CONFIG_API = "INTERFACE_CONFIG_API"

    ADDITIONAL_FCOE_STAT_1_CMD = "additional_fcoe_stat_1"
    # Constant values for ADDITIONAL_FCOE_STAT_1_CMD
    ADDITIONAL_FCOE_STAT_1_FCOE_INVALID_DELIMITER = "fcoe_invalid_delimiter"
    ADDITIONAL_FCOE_STAT_1_FCOE_INVALID_FRAMES = "fcoe_invalid_frames"
    ADDITIONAL_FCOE_STAT_1_FCOE_INVALID_SIZE = "fcoe_invalid_size"
    ADDITIONAL_FCOE_STAT_1_FCOE_NORMAL_SIZE_BAD_FC_CRC = "fcoe_normal_size_bad_fc_crc"
    ADDITIONAL_FCOE_STAT_1_FCOE_NORMAL_SIZE_GOOD_FC_CRC = "fcoe_normal_size_good_fc_crc"
    ADDITIONAL_FCOE_STAT_1_FCOE_UNDERSIZE_BAD_FC_CRC = "fcoe_undersize_bad_fc_crc"
    ADDITIONAL_FCOE_STAT_1_FCOE_UNDERSIZE_GOOD_FC_CRC = "fcoe_undersize_good_fc_crc"
    ADDITIONAL_FCOE_STAT_1_FCOE_VALID_FRAMES = "fcoe_valid_frames"

    ADDITIONAL_FCOE_STAT_2_CMD = "additional_fcoe_stat_2"
    # Constant values for ADDITIONAL_FCOE_STAT_2_CMD
    ADDITIONAL_FCOE_STAT_2_FCOE_INVALID_DELIMITER = "fcoe_invalid_delimiter"
    ADDITIONAL_FCOE_STAT_2_FCOE_INVALID_FRAMES = "fcoe_invalid_frames"
    ADDITIONAL_FCOE_STAT_2_FCOE_INVALID_SIZE = "fcoe_invalid_size"
    ADDITIONAL_FCOE_STAT_2_FCOE_NORMAL_SIZE_BAD_FC_CRC = "fcoe_normal_size_bad_fc_crc"
    ADDITIONAL_FCOE_STAT_2_FCOE_NORMAL_SIZE_GOOD_FC_CRC = "fcoe_normal_size_good_fc_crc"
    ADDITIONAL_FCOE_STAT_2_FCOE_UNDERSIZE_BAD_FC_CRC = "fcoe_undersize_bad_fc_crc"
    ADDITIONAL_FCOE_STAT_2_FCOE_UNDERSIZE_GOOD_FC_CRC = "fcoe_undersize_good_fc_crc"
    ADDITIONAL_FCOE_STAT_2_FCOE_VALID_FRAMES = "fcoe_valid_frames"

    ADDRESSES_PER_SVLAN_CMD = "addresses_per_svlan"

    ADDRESSES_PER_VCI_CMD = "addresses_per_vci"

    ADDRESSES_PER_VLAN_CMD = "addresses_per_vlan"

    ADDRESSES_PER_VPI_CMD = "addresses_per_vpi"

    ARP_CMD = "arp"

    ARP_ON_LINKUP_CMD = "arp_on_linkup"

    ARP_REFRESH_INTERVAL_CMD = "arp_refresh_interval"

    ARP_REQ_RETRIES_CMD = "arp_req_retries"

    ARP_REQ_TIMER_CMD = "arp_req_timer"

    ARP_SEND_REQ_CMD = "arp_send_req"

    ATM_ENABLE_COSET_CMD = "atm_enable_coset"

    ATM_ENABLE_PATTERN_MATCHING_CMD = "atm_enable_pattern_matching"

    ATM_ENCAPSULATION_CMD = "atm_encapsulation"
    # Constant values for ATM_ENCAPSULATION_CMD
    ATM_ENCAPSULATION_VCCMUXIPV4ROUTED = "VccMuxIPV4Routed"
    ATM_ENCAPSULATION_VCCMUXBRIDGEDETHERNETFCS = "VccMuxBridgedEthernetFCS"
    ATM_ENCAPSULATION_VCCMUXBRIDGEDETHERNETNOFCS = "VccMuxBridgedEthernetNoFCS"
    ATM_ENCAPSULATION_VCCMUXIPV6ROUTED = "VccMuxIPV6Routed"
    ATM_ENCAPSULATION_VCCMUXMPLSROUTED = "VccMuxMPLSRouted"
    ATM_ENCAPSULATION_LLCROUTEDCLIP = "LLCRoutedCLIP"
    ATM_ENCAPSULATION_LLCBRIDGEDETHERNETFCS = "LLCBridgedEthernetFCS"
    ATM_ENCAPSULATION_LLCBRIDGEDETHERNETNOFCS = "LLCBridgedEthernetNoFCS"
    ATM_ENCAPSULATION_LLCPPPOA = "LLCPPPoA"
    ATM_ENCAPSULATION_VCCMUXPPPOA = "VccMuxPPPoA"
    ATM_ENCAPSULATION_LLCNLPIDROUTED = "LLCNLPIDRouted"

    ATM_FILLER_CELL_CMD = "atm_filler_cell"
    # Constant values for ATM_FILLER_CELL_CMD
    ATM_FILLER_CELL_IDLE = "idle"
    ATM_FILLER_CELL_UNASSIGNED = "unassigned"

    ATM_INTERFACE_TYPE_CMD = "atm_interface_type"
    # Constant values for ATM_INTERFACE_TYPE_CMD
    ATM_INTERFACE_TYPE_UNI = "uni"
    ATM_INTERFACE_TYPE_NNI = "nni"

    ATM_PACKET_DECODE_MODE_CMD = "atm_packet_decode_mode"
    # Constant values for ATM_PACKET_DECODE_MODE_CMD
    ATM_PACKET_DECODE_MODE_FRAME = "frame"
    ATM_PACKET_DECODE_MODE_CELL = "cell"

    ATM_REASSEMBLY_TIMEOUT_CMD = "atm_reassembly_timeout"

    AUTO_DETECT_INSTRUMENTATION_TYPE_CMD = "auto_detect_instrumentation_type"
    # Constant values for AUTO_DETECT_INSTRUMENTATION_TYPE_CMD
    AUTO_DETECT_INSTRUMENTATION_TYPE_END_OF_FRAME = "end_of_frame"
    AUTO_DETECT_INSTRUMENTATION_TYPE_FLOATING = "floating"

    AUTONEGOTIATION_CMD = "autonegotiation"

    BAD_BLOCKS_NUMBER_CMD = "bad_blocks_number"

    BERT_CONFIGURATION_CMD = "bert_configuration"

    BERT_ERROR_INSERTION_CMD = "bert_error_insertion"

    CHECK_GATEWAY_EXISTS_CMD = "check_gateway_exists"

    CHECK_OPPOSITE_IP_VERSION_CMD = "check_opposite_ip_version"

    CLOCKSOURCE_CMD = "clocksource"
    # Constant values for CLOCKSOURCE_CMD
    CLOCKSOURCE_INTERNAL = "internal"
    CLOCKSOURCE_LOOP = "loop"
    CLOCKSOURCE_EXTERNAL = "external"

    CONNECTED_COUNT_CMD = "connected_count"

    CONNECTED_TO_HANDLE_CMD = "connected_to_handle"

    DATA_INTEGRITY_CMD = "data_integrity"

    DUPLEX_CMD = "duplex"
    # Constant values for DUPLEX_CMD
    DUPLEX_HALF = "half"
    DUPLEX_FULL = "full"
    DUPLEX_AUTO = "auto"

    ENABLE_DATA_CENTER_SHARED_STATS_CMD = "enable_data_center_shared_stats"

    ENABLE_FLOW_CONTROL_CMD = "enable_flow_control"

    ENABLE_LOOPBACK_CMD = "enable_loopback"

    ENABLE_NDP_CMD = "enable_ndp"

    ENABLE_RS_FEC_CMD = "enable_rs_fec"

    ENABLE_RS_FEC_STATISTICS_CMD = "enable_rs_fec_statistics"

    ETHERNET_ATTEMPT_ENABLED_CMD = "ethernet_attempt_enabled"

    ETHERNET_ATTEMPT_INTERVAL_CMD = "ethernet_attempt_interval"

    ETHERNET_ATTEMPT_RATE_CMD = "ethernet_attempt_rate"

    ETHERNET_ATTEMPT_SCALE_MODE_CMD = "ethernet_attempt_scale_mode"
    # Constant values for ETHERNET_ATTEMPT_SCALE_MODE_CMD
    ETHERNET_ATTEMPT_SCALE_MODE_PORT = "port"
    ETHERNET_ATTEMPT_SCALE_MODE_DEVICE_GROUP = "device_group"

    ETHERNET_DICONNECT_ENABLED_CMD = "ethernet_diconnect_enabled"

    ETHERNET_DISCONNECT_INTERVAL_CMD = "ethernet_disconnect_interval"

    ETHERNET_DISCONNECT_RATE_CMD = "ethernet_disconnect_rate"

    ETHERNET_DISCONNECT_SCALE_MODE_CMD = "ethernet_disconnect_scale_mode"
    # Constant values for ETHERNET_DISCONNECT_SCALE_MODE_CMD
    ETHERNET_DISCONNECT_SCALE_MODE_PORT = "port"
    ETHERNET_DISCONNECT_SCALE_MODE_DEVICE_GROUP = "device_group"

    FC_CREDIT_STARVATION_VALUE_CMD = "fc_credit_starvation_value"

    FC_FIXED_DELAY_VALUE_CMD = "fc_fixed_delay_value"

    FC_FORCE_ERRORS_CMD = "fc_force_errors"
    # Constant values for FC_FORCE_ERRORS_CMD
    FC_FORCE_ERRORS_NO_ERRORS = "no_errors"
    FC_FORCE_ERRORS_NO_RRDY = "no_rrdy"
    FC_FORCE_ERRORS_NO_RRDY_EVERY = "no_rrdy_every"

    FC_MAX_DELAY_FOR_RANDOM_VALUE_CMD = "fc_max_delay_for_random_value"

    FC_MIN_DELAY_FOR_RANDOM_VALUE_CMD = "fc_min_delay_for_random_value"

    FC_NO_RRDY_AFTER_CMD = "fc_no_rrdy_after"

    FC_RRDY_RESPONSE_DELAYS_CMD = "fc_rrdy_response_delays"
    # Constant values for FC_RRDY_RESPONSE_DELAYS_CMD
    FC_RRDY_RESPONSE_DELAYS_CREDIT_STARVATION = "credit_starvation"
    FC_RRDY_RESPONSE_DELAYS_FIXED_DELAY = "fixed_delay"
    FC_RRDY_RESPONSE_DELAYS_NO_DELAY = "no_delay"
    FC_RRDY_RESPONSE_DELAYS_RANDOM_DELAY = "random_delay"

    FC_TX_IGNORE_AVAILABLE_CREDITS_CMD = "fc_tx_ignore_available_credits"

    FC_TX_IGNORE_RX_LINK_FAULTS_CMD = "fc_tx_ignore_rx_link_faults"

    FCOE_FLOW_CONTROL_TYPE_CMD = "fcoe_flow_control_type"
    # Constant values for FCOE_FLOW_CONTROL_TYPE_CMD
    FCOE_FLOW_CONTROL_TYPE_IEEE802_3X = "ieee802.3x"
    FCOE_FLOW_CONTROL_TYPE_IEEE802_1QBB = "ieee802.1Qbb"

    FCOE_PRIORITY_GROUP_SIZE_CMD = "fcoe_priority_group_size"
    # Constant values for FCOE_PRIORITY_GROUP_SIZE_CMD
    FCOE_PRIORITY_GROUP_SIZE_OPT_4 = "opt_4"
    FCOE_PRIORITY_GROUP_SIZE_OPT_8 = "opt_8"

    FCOE_PRIORITY_GROUPS_CMD = "fcoe_priority_groups"

    FCOE_SUPPORT_DATA_CENTER_MODE_CMD = "fcoe_support_data_center_mode"

    FLOW_CONTROL_DIRECTED_ADDR_CMD = "flow_control_directed_addr"

    FRAMING_CMD = "framing"
    # Constant values for FRAMING_CMD
    FRAMING_SONET = "sonet"
    FRAMING_SDH = "sdh"

    GATEWAY_CMD = "gateway"

    GATEWAY_INCR_MODE_CMD = "gateway_incr_mode"
    # Constant values for GATEWAY_INCR_MODE_CMD
    GATEWAY_INCR_MODE_EVERY_SUBNET = "every_subnet"
    GATEWAY_INCR_MODE_EVERY_INTERFACE = "every_interface"

    GATEWAY_STEP_CMD = "gateway_step"

    GOOD_BLOCKS_NUMBER_CMD = "good_blocks_number"

    GRE_CHECKSUM_ENABLE_CMD = "gre_checksum_enable"

    GRE_COUNT_CMD = "gre_count"

    GRE_DST_IP_ADDR_CMD = "gre_dst_ip_addr"

    GRE_DST_IP_ADDR_STEP_CMD = "gre_dst_ip_addr_step"

    GRE_IP_ADDR_CMD = "gre_ip_addr"

    GRE_IP_ADDR_STEP_CMD = "gre_ip_addr_step"

    GRE_IP_PREFIX_LENGTH_CMD = "gre_ip_prefix_length"

    GRE_IPV6_ADDR_CMD = "gre_ipv6_addr"

    GRE_IPV6_ADDR_STEP_CMD = "gre_ipv6_addr_step"

    GRE_IPV6_PREFIX_LENGTH_CMD = "gre_ipv6_prefix_length"

    GRE_KEY_ENABLE_CMD = "gre_key_enable"

    GRE_KEY_IN_CMD = "gre_key_in"

    GRE_KEY_OUT_CMD = "gre_key_out"

    GRE_SEQ_ENABLE_CMD = "gre_seq_enable"

    IEEE_MEDIA_DEFAULTS_CMD = "ieee_media_defaults"

    IGNORE_LINK_CMD = "ignore_link"

    INTEGRITY_SIGNATURE_CMD = "integrity_signature"

    INTEGRITY_SIGNATURE_OFFSET_CMD = "integrity_signature_offset"

    INTERFACE_HANDLE_CMD = "interface_handle"

    INTERNAL_PPM_ADJUST_CMD = "internal_ppm_adjust"

    INTF_IP_ADDR_CMD = "intf_ip_addr"

    INTF_IP_ADDR_STEP_CMD = "intf_ip_addr_step"

    INTF_MODE_CMD = "intf_mode"
    # Constant values for INTF_MODE_CMD
    INTF_MODE_ATM = "atm"
    INTF_MODE_POS_HDLC = "pos_hdlc"
    INTF_MODE_POS_PPP = "pos_ppp"
    INTF_MODE_ETHERNET = "ethernet"
    INTF_MODE_ETHERNET_VM = "ethernet_vm"
    INTF_MODE_MULTIS = "multis"
    INTF_MODE_MULTIS_FCOE = "multis_fcoe"
    INTF_MODE_RAME_RELAY1490 = "rame_relay1490"
    INTF_MODE_BERT = "bert"
    INTF_MODE_FRAME_RELAY2427 = "frame_relay2427"
    INTF_MODE_FRAME_RELAY_CISCO = "frame_relay_cisco"
    INTF_MODE_SRP = "srp"
    INTF_MODE_SRP_CISCO = "srp_cisco"
    INTF_MODE_RPR = "rpr"
    INTF_MODE_GFP = "gfp"
    INTF_MODE_ETHERNET_FCOE = "ethernet_fcoe"
    INTF_MODE_FC = "fc"

    INTRINSIC_LATENCY_ADJUSTMENT_CMD = "intrinsic_latency_adjustment"

    IPV4_ATTEMPT_ENABLED_CMD = "ipv4_attempt_enabled"

    IPV4_ATTEMPT_INTERVAL_CMD = "ipv4_attempt_interval"

    IPV4_ATTEMPT_RATE_CMD = "ipv4_attempt_rate"

    IPV4_ATTEMPT_SCALE_MODE_CMD = "ipv4_attempt_scale_mode"
    # Constant values for IPV4_ATTEMPT_SCALE_MODE_CMD
    IPV4_ATTEMPT_SCALE_MODE_PORT = "port"
    IPV4_ATTEMPT_SCALE_MODE_DEVICE_GROUP = "device_group"

    IPV4_DICONNECT_ENABLED_CMD = "ipv4_diconnect_enabled"

    IPV4_DISCONNECT_INTERVAL_CMD = "ipv4_disconnect_interval"

    IPV4_DISCONNECT_RATE_CMD = "ipv4_disconnect_rate"

    IPV4_DISCONNECT_SCALE_MODE_CMD = "ipv4_disconnect_scale_mode"
    # Constant values for IPV4_DISCONNECT_SCALE_MODE_CMD
    IPV4_DISCONNECT_SCALE_MODE_PORT = "port"
    IPV4_DISCONNECT_SCALE_MODE_DEVICE_GROUP = "device_group"

    IPV4_MANUAL_GATEWAY_MAC_CMD = "ipv4_manual_gateway_mac"

    IPV4_MANUAL_GATEWAY_MAC_STEP_CMD = "ipv4_manual_gateway_mac_step"

    IPV4_RE_SEND_ARP_ON_LINK_UP_CMD = "ipv4_re_send_arp_on_link_up"

    IPV4_RESOLVE_GATEWAY_CMD = "ipv4_resolve_gateway"

    IPV4_SEND_ARP_INTERVAL_CMD = "ipv4_send_arp_interval"

    IPV4_SEND_ARP_MAX_OUTSTANDING_CMD = "ipv4_send_arp_max_outstanding"

    IPV4_SEND_ARP_RATE_CMD = "ipv4_send_arp_rate"

    IPV4_SEND_ARP_SCALE_MODE_CMD = "ipv4_send_arp_scale_mode"
    # Constant values for IPV4_SEND_ARP_SCALE_MODE_CMD
    IPV4_SEND_ARP_SCALE_MODE_PORT = "port"
    IPV4_SEND_ARP_SCALE_MODE_DEVICE_GROUP = "device_group"

    IPV6_ADDR_MODE_CMD = "ipv6_addr_mode"
    # Constant values for IPV6_ADDR_MODE_CMD
    IPV6_ADDR_MODE_STATIC = "static"
    IPV6_ADDR_MODE_AUTOCONFIG = "autoconfig"

    IPV6_ATTEMPT_ENABLED_CMD = "ipv6_attempt_enabled"

    IPV6_ATTEMPT_INTERVAL_CMD = "ipv6_attempt_interval"

    IPV6_ATTEMPT_RATE_CMD = "ipv6_attempt_rate"

    IPV6_ATTEMPT_SCALE_MODE_CMD = "ipv6_attempt_scale_mode"
    # Constant values for IPV6_ATTEMPT_SCALE_MODE_CMD
    IPV6_ATTEMPT_SCALE_MODE_PORT = "port"
    IPV6_ATTEMPT_SCALE_MODE_DEVICE_GROUP = "device_group"

    IPV6_AUTOCONFIGURATION_ATTEMPT_ENABLED_CMD = "ipv6_autoconfiguration_attempt_enabled"

    IPV6_AUTOCONFIGURATION_ATTEMPT_INTERVAL_CMD = "ipv6_autoconfiguration_attempt_interval"

    IPV6_AUTOCONFIGURATION_ATTEMPT_MAX_OUTSTANDING_CMD = "ipv6_autoconfiguration_attempt_max_outstanding"

    IPV6_AUTOCONFIGURATION_ATTEMPT_RATE_CMD = "ipv6_autoconfiguration_attempt_rate"

    IPV6_AUTOCONFIGURATION_ATTEMPT_SCALE_MODE_CMD = "ipv6_autoconfiguration_attempt_scale_mode"
    # Constant values for IPV6_AUTOCONFIGURATION_ATTEMPT_SCALE_MODE_CMD
    IPV6_AUTOCONFIGURATION_ATTEMPT_SCALE_MODE_PORT = "port"
    IPV6_AUTOCONFIGURATION_ATTEMPT_SCALE_MODE_DEVICE_GROUP = "device_group"

    IPV6_AUTOCONFIGURATION_DISCONNECT_ENABLED_CMD = "ipv6_autoconfiguration_disconnect_enabled"

    IPV6_AUTOCONFIGURATION_DISCONNECT_INTERVAL_CMD = "ipv6_autoconfiguration_disconnect_interval"

    IPV6_AUTOCONFIGURATION_DISCONNECT_MAX_OUTSTANDING_CMD = "ipv6_autoconfiguration_disconnect_max_outstanding"

    IPV6_AUTOCONFIGURATION_DISCONNECT_RATE_CMD = "ipv6_autoconfiguration_disconnect_rate"

    IPV6_AUTOCONFIGURATION_DISCONNECT_SCALE_MODE_CMD = "ipv6_autoconfiguration_disconnect_scale_mode"
    # Constant values for IPV6_AUTOCONFIGURATION_DISCONNECT_SCALE_MODE_CMD
    IPV6_AUTOCONFIGURATION_DISCONNECT_SCALE_MODE_PORT = "port"
    IPV6_AUTOCONFIGURATION_DISCONNECT_SCALE_MODE_DEVICE_GROUP = "device_group"

    IPV6_AUTOCONFIGURATION_SEND_NS_ENABLED_CMD = "ipv6_autoconfiguration_send_ns_enabled"

    IPV6_AUTOCONFIGURATION_SEND_NS_MAX_OUTSTANDING_CMD = "ipv6_autoconfiguration_send_ns_max_outstanding"

    IPV6_AUTOCONFIGURATION_SEND_NS_RATE_CMD = "ipv6_autoconfiguration_send_ns_rate"

    IPV6_AUTOCONFIGURATION_SEND_NS_SCALE_MODE_CMD = "ipv6_autoconfiguration_send_ns_scale_mode"
    # Constant values for IPV6_AUTOCONFIGURATION_SEND_NS_SCALE_MODE_CMD
    IPV6_AUTOCONFIGURATION_SEND_NS_SCALE_MODE_PORT = "port"
    IPV6_AUTOCONFIGURATION_SEND_NS_SCALE_MODE_DEVICE_GROUP = "device_group"

    IPV6_AUTOCONFIGURATION_SEND_RS_ENABLED_CMD = "ipv6_autoconfiguration_send_rs_enabled"

    IPV6_AUTOCONFIGURATION_SEND_RS_INTERVAL_CMD = "ipv6_autoconfiguration_send_rs_interval"

    IPV6_AUTOCONFIGURATION_SEND_RS_MAX_OUTSTANDING_CMD = "ipv6_autoconfiguration_send_rs_max_outstanding"

    IPV6_AUTOCONFIGURATION_SEND_RS_RATE_CMD = "ipv6_autoconfiguration_send_rs_rate"

    IPV6_AUTOCONFIGURATION_SEND_RS_SCALE_MODE_CMD = "ipv6_autoconfiguration_send_rs_scale_mode"
    # Constant values for IPV6_AUTOCONFIGURATION_SEND_RS_SCALE_MODE_CMD
    IPV6_AUTOCONFIGURATION_SEND_RS_SCALE_MODE_PORT = "port"
    IPV6_AUTOCONFIGURATION_SEND_RS_SCALE_MODE_DEVICE_GROUP = "device_group"

    IPV6_DICONNECT_ENABLED_CMD = "ipv6_diconnect_enabled"

    IPV6_DISCONNECT_INTERVAL_CMD = "ipv6_disconnect_interval"

    IPV6_DISCONNECT_RATE_CMD = "ipv6_disconnect_rate"

    IPV6_DISCONNECT_SCALE_MODE_CMD = "ipv6_disconnect_scale_mode"
    # Constant values for IPV6_DISCONNECT_SCALE_MODE_CMD
    IPV6_DISCONNECT_SCALE_MODE_PORT = "port"
    IPV6_DISCONNECT_SCALE_MODE_DEVICE_GROUP = "device_group"

    IPV6_GATEWAY_CMD = "ipv6_gateway"

    IPV6_GATEWAY_STEP_CMD = "ipv6_gateway_step"

    IPV6_INTF_ADDR_CMD = "ipv6_intf_addr"

    IPV6_INTF_ADDR_STEP_CMD = "ipv6_intf_addr_step"

    IPV6_LOOPBACK_MULTIPLIER_CMD = "ipv6_loopback_multiplier"

    IPV6_MANUAL_GATEWAY_MAC_CMD = "ipv6_manual_gateway_mac"

    IPV6_MANUAL_GATEWAY_MAC_STEP_CMD = "ipv6_manual_gateway_mac_step"

    IPV6_MULTIPLIER_CMD = "ipv6_multiplier"

    IPV6_PREFIX_LENGTH_CMD = "ipv6_prefix_length"

    IPV6_RE_SEND_NS_ON_LINK_UP_CMD = "ipv6_re_send_ns_on_link_up"

    IPV6_RESOLVE_GATEWAY_CMD = "ipv6_resolve_gateway"

    IPV6_SEND_NS_INTERVAL_CMD = "ipv6_send_ns_interval"

    IPV6_SEND_NS_MAX_OUTSTANDING_CMD = "ipv6_send_ns_max_outstanding"

    IPV6_SEND_NS_RATE_CMD = "ipv6_send_ns_rate"

    IPV6_SEND_NS_SCALE_MODE_CMD = "ipv6_send_ns_scale_mode"
    # Constant values for IPV6_SEND_NS_SCALE_MODE_CMD
    IPV6_SEND_NS_SCALE_MODE_PORT = "port"
    IPV6_SEND_NS_SCALE_MODE_DEVICE_GROUP = "device_group"

    L23_CONFIG_TYPE_CMD = "l23_config_type"
    # Constant values for L23_CONFIG_TYPE_CMD
    L23_CONFIG_TYPE_PROTOCOL_INTERFACE = "protocol_interface"
    L23_CONFIG_TYPE_STATIC_ENDPOINT = "static_endpoint"

    LASER_ON_CMD = "laser_on"

    LINK_TRAINING_CMD = "link_training"

    LOOP_CONTINUOUSLY_CMD = "loop_continuously"

    LOOP_COUNT_NUMBER_CMD = "loop_count_number"

    MASTER_SLAVE_MODE_CMD = "master_slave_mode"
    # Constant values for MASTER_SLAVE_MODE_CMD
    MASTER_SLAVE_MODE_AUTO = "auto"
    MASTER_SLAVE_MODE_MASTER = "master"
    MASTER_SLAVE_MODE_SLAVE = "slave"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CONFIG = "config"
    MODE_MODIFY = "modify"
    MODE_DESTROY = "destroy"

    MSS_CMD = "mss"

    MTU_CMD = "mtu"

    NDP_SEND_REQ_CMD = "ndp_send_req"

    NETMASK_CMD = "netmask"

    NO_WRITE_CMD = "no_write"

    NOTIFY_MAC_MOVE_CMD = "notify_mac_move"

    NS_ON_LINKUP_CMD = "ns_on_linkup"

    OP_MODE_CMD = "op_mode"
    # Constant values for OP_MODE_CMD
    OP_MODE_LOOPBACK = "loopback"
    OP_MODE_NORMAL = "normal"
    OP_MODE_MONITOR = "monitor"
    OP_MODE_SIM_DISCONNECT = "sim_disconnect"

    OVERRIDE_EXISTENCE_CHECK_CMD = "override_existence_check"

    OVERRIDE_TRACKING_CMD = "override_tracking"

    PCS_COUNT_CMD = "pcs_count"

    PCS_ENABLED_CONTINUOUS_CMD = "pcs_enabled_continuous"

    PCS_LANE_CMD = "pcs_lane"

    PCS_MARKER_FIELDS_CMD = "pcs_marker_fields"

    PCS_PERIOD_CMD = "pcs_period"

    PCS_PERIOD_TYPE_CMD = "pcs_period_type"

    PCS_REPEAT_CMD = "pcs_repeat"

    PCS_SYNC_BITS_CMD = "pcs_sync_bits"

    PGID_128K_BIN_ENABLE_CMD = "pgid_128k_bin_enable"

    PGID_ENCAP_CMD = "pgid_encap"
    # Constant values for PGID_ENCAP_CMD
    PGID_ENCAP_LLCROUTEDCLIP = "LLCRoutedCLIP"
    PGID_ENCAP_LLCPPPOA = "LLCPPPoA"
    PGID_ENCAP_LLCBRIDGEDETHERNETFCS = "LLCBridgedEthernetFCS"
    PGID_ENCAP_LLCBRIDGEDETHERNETNOFCS = "LLCBridgedEthernetNoFCS"
    PGID_ENCAP_VCCMUXPPPOA = "VccMuxPPPoA"
    PGID_ENCAP_VCCMUXIPV4ROUTED = "VccMuxIPV4Routed"
    PGID_ENCAP_VCCMUXBRIDGEDETHERNETFCS = "VccMuxBridgedEthernetFCS"
    PGID_ENCAP_VCCMUXBRIDGEDETHERNETNOFCS = "VccMuxBridgedEthernetNoFCS"

    PGID_MASK_CMD = "pgid_mask"

    PGID_MODE_CMD = "pgid_mode"
    # Constant values for PGID_MODE_CMD
    PGID_MODE_CUSTOM = "custom"
    PGID_MODE_DSCP = "dscp"
    PGID_MODE_IPV6TC = "ipv6TC"
    PGID_MODE_MPLSEXP = "mplsExp"
    PGID_MODE_SPLIT = "split"
    PGID_MODE_OUTER_VLAN_PRIORITY = "outer_vlan_priority"
    PGID_MODE_OUTER_VLAN_ID_4 = "outer_vlan_id_4"
    PGID_MODE_OUTER_VLAN_ID_6 = "outer_vlan_id_6"
    PGID_MODE_OUTER_VLAN_ID_8 = "outer_vlan_id_8"
    PGID_MODE_OUTER_VLAN_ID_10 = "outer_vlan_id_10"
    PGID_MODE_OUTER_VLAN_ID_12 = "outer_vlan_id_12"
    PGID_MODE_INNER_VLAN_PRIORITY = "inner_vlan_priority"
    PGID_MODE_INNER_VLAN_ID_4 = "inner_vlan_id_4"
    PGID_MODE_INNER_VLAN_ID_6 = "inner_vlan_id_6"
    PGID_MODE_INNER_VLAN_ID_8 = "inner_vlan_id_8"
    PGID_MODE_INNER_VLAN_ID_10 = "inner_vlan_id_10"
    PGID_MODE_INNER_VLAN_ID_12 = "inner_vlan_id_12"
    PGID_MODE_TOS_PRECEDENCE = "tos_precedence"
    PGID_MODE_IPV6TC_BITS_0_2 = "ipv6TC_bits_0_2"
    PGID_MODE_IPV6TC_BITS_0_5 = "ipv6TC_bits_0_5"

    PGID_OFFSET_CMD = "pgid_offset"

    PGID_SPLIT1_MASK_CMD = "pgid_split1_mask"

    PGID_SPLIT1_OFFSET_CMD = "pgid_split1_offset"

    PGID_SPLIT1_OFFSET_FROM_CMD = "pgid_split1_offset_from"
    # Constant values for PGID_SPLIT1_OFFSET_FROM_CMD
    PGID_SPLIT1_OFFSET_FROM_START_OF_FRAME = "start_of_frame"

    PGID_SPLIT1_WIDTH_CMD = "pgid_split1_width"

    PGID_SPLIT2_MASK_CMD = "pgid_split2_mask"

    PGID_SPLIT2_OFFSET_CMD = "pgid_split2_offset"

    PGID_SPLIT2_OFFSET_FROM_CMD = "pgid_split2_offset_from"
    # Constant values for PGID_SPLIT2_OFFSET_FROM_CMD
    PGID_SPLIT2_OFFSET_FROM_START_OF_FRAME = "start_of_frame"

    PGID_SPLIT2_WIDTH_CMD = "pgid_split2_width"

    PGID_SPLIT3_MASK_CMD = "pgid_split3_mask"

    PGID_SPLIT3_OFFSET_CMD = "pgid_split3_offset"

    PGID_SPLIT3_OFFSET_FROM_CMD = "pgid_split3_offset_from"
    # Constant values for PGID_SPLIT3_OFFSET_FROM_CMD
    PGID_SPLIT3_OFFSET_FROM_START_OF_FRAME = "start_of_frame"

    PGID_SPLIT3_WIDTH_CMD = "pgid_split3_width"

    PHY_MODE_CMD = "phy_mode"
    # Constant values for PHY_MODE_CMD
    PHY_MODE_COPPER = "copper"
    PHY_MODE_FIBER = "fiber"
    PHY_MODE_SGMII = "sgmii"

    PING_DST_CMD = "ping_dst"

    PORT_HANDLE_CMD = "port_handle"

    PORT_RX_MODE_CMD = "port_rx_mode"
    # Constant values for PORT_RX_MODE_CMD
    PORT_RX_MODE_CAPTURE = "capture"
    PORT_RX_MODE_PACKET_GROUP = "packet_group"
    PORT_RX_MODE_DATA_INTEGRITY = "data_integrity"
    PORT_RX_MODE_SEQUENCE_CHECKING = "sequence_checking"
    PORT_RX_MODE_WIDE_PACKET_GROUP = "wide_packet_group"
    PORT_RX_MODE_ECHO = "echo"
    PORT_RX_MODE_AUTO_DETECT_INSTRUMENTATION = "auto_detect_instrumentation"
    PORT_RX_MODE_CAPTURE_AND_MEASURE = "capture_and_measure"

    PPP_IPV4_ADDRESS_CMD = "ppp_ipv4_address"

    PPP_IPV4_NEGOTIATION_CMD = "ppp_ipv4_negotiation"

    PPP_IPV6_NEGOTIATION_CMD = "ppp_ipv6_negotiation"

    PPP_MPLS_NEGOTIATION_CMD = "ppp_mpls_negotiation"

    PPP_OSI_NEGOTIATION_CMD = "ppp_osi_negotiation"
    # Constant values for PPP_OSI_NEGOTIATION_CMD
    PPP_OSI_NEGOTIATION_ENABLE = "enable"
    PPP_OSI_NEGOTIATION_DISABLE = "disable"

    PROTOCOL_HANDLE_CMD = "protocol_handle"

    PROTOCOL_NAME_CMD = "protocol_name"

    PVC_INCR_MODE_CMD = "pvc_incr_mode"
    # Constant values for PVC_INCR_MODE_CMD
    PVC_INCR_MODE_VCI = "vci"
    PVC_INCR_MODE_VPI = "vpi"
    PVC_INCR_MODE_BOTH = "both"

    QINQ_INCR_MODE_CMD = "qinq_incr_mode"
    # Constant values for QINQ_INCR_MODE_CMD
    QINQ_INCR_MODE_INNER = "inner"
    QINQ_INCR_MODE_OUTER = "outer"
    QINQ_INCR_MODE_BOTH = "both"

    QOS_BYTE_OFFSET_CMD = "qos_byte_offset"

    QOS_PACKET_TYPE_CMD = "qos_packet_type"
    # Constant values for QOS_PACKET_TYPE_CMD
    QOS_PACKET_TYPE_ETHERNET = "ethernet"
    QOS_PACKET_TYPE_IP_SNAP = "ip_snap"
    QOS_PACKET_TYPE_VLAN = "vlan"
    QOS_PACKET_TYPE_CUSTOM = "custom"
    QOS_PACKET_TYPE_IP_PPP = "ip_ppp"
    QOS_PACKET_TYPE_IP_CISCO_HDLC = "ip_cisco_hdlc"
    QOS_PACKET_TYPE_IP_ATM = "ip_atm"

    QOS_PATTERN_MASK_CMD = "qos_pattern_mask"

    QOS_PATTERN_MATCH_CMD = "qos_pattern_match"

    QOS_PATTERN_OFFSET_CMD = "qos_pattern_offset"

    QOS_STATS_CMD = "qos_stats"

    ROUTER_SOLICITATION_RETRIES_CMD = "router_solicitation_retries"

    RPR_HEC_SEED_CMD = "rpr_hec_seed"

    RX_C2_CMD = "rx_c2"

    RX_FCS_CMD = "rx_fcs"
    # Constant values for RX_FCS_CMD
    RX_FCS_OPT_16 = "opt_16"
    RX_FCS_OPT_32 = "opt_32"

    RX_SCRAMBLING_CMD = "rx_scrambling"

    SEND_PING_CMD = "send_ping"

    SEND_ROUTER_SOLICITATION_CMD = "send_router_solicitation"

    SEND_SETS_MODE_CMD = "send_sets_mode"
    # Constant values for SEND_SETS_MODE_CMD
    SEND_SETS_MODE_ALTERNATE = "alternate"
    SEND_SETS_MODE_TYPE_A_ONLY = "type_a_only"
    SEND_SETS_MODE_TYPE_B_ONLY = "type_b_only"

    SEQUENCE_CHECKING_CMD = "sequence_checking"

    SEQUENCE_NUM_OFFSET_CMD = "sequence_num_offset"

    SIGNATURE_CMD = "signature"

    SIGNATURE_MASK_CMD = "signature_mask"

    SIGNATURE_OFFSET_CMD = "signature_offset"

    SIGNATURE_START_OFFSET_CMD = "signature_start_offset"

    SINGLE_ARP_PER_GATEWAY_CMD = "single_arp_per_gateway"

    SINGLE_NS_PER_GATEWAY_CMD = "single_ns_per_gateway"

    SITE_ID_CMD = "site_id"

    SPEED_CMD = "speed"
    # Constant values for SPEED_CMD
    SPEED_ETHER10 = "ether10"
    SPEED_ETHER100 = "ether100"
    SPEED_ETHER1000 = "ether1000"
    SPEED_OC3 = "oc3"
    SPEED_OC12 = "oc12"
    SPEED_OC48 = "oc48"
    SPEED_OC192 = "oc192"
    SPEED_ETHER10000WAN = "ether10000wan"
    SPEED_ETHER10000LAN = "ether10000lan"
    SPEED_ETHER40000LAN = "ether40000lan"
    SPEED_ETHER100000LAN = "ether100000lan"
    SPEED_ETHER10GIG = "ether10Gig"
    SPEED_ETHER25GIG = "ether25Gig"
    SPEED_ETHER40GIG = "ether40Gig"
    SPEED_ETHER100GIG = "ether100Gig"
    SPEED_AUTO = "auto"
    SPEED_FC2000 = "fc2000"
    SPEED_FC4000 = "fc4000"
    SPEED_FC8000 = "fc8000"
    SPEED_ETHER100VM = "ether100vm"
    SPEED_ETHER1000VM = "ether1000vm"
    SPEED_ETHER2000VM = "ether2000vm"
    SPEED_ETHER3000VM = "ether3000vm"
    SPEED_ETHER4000VM = "ether4000vm"
    SPEED_ETHER5000VM = "ether5000vm"
    SPEED_ETHER6000VM = "ether6000vm"
    SPEED_ETHER7000VM = "ether7000vm"
    SPEED_ETHER8000VM = "ether8000vm"
    SPEED_ETHER9000VM = "ether9000vm"
    SPEED_ETHER10000VM = "ether10000vm"

    SRC_MAC_ADDR_CMD = "src_mac_addr"

    SRC_MAC_ADDR_STEP_CMD = "src_mac_addr_step"

    START_ERROR_INSERTION_CMD = "start_error_insertion"

    STATIC_ATM_HEADER_ENCAPSULATION_CMD = "static_atm_header_encapsulation"
    # Constant values for STATIC_ATM_HEADER_ENCAPSULATION_CMD
    STATIC_ATM_HEADER_ENCAPSULATION_LLC_BRIDGED_ETH_FCS = "llc_bridged_eth_fcs"

    STATIC_ATM_RANGE_COUNT_CMD = "static_atm_range_count"

    STATIC_DLCI_COUNT_MODE_CMD = "static_dlci_count_mode"
    # Constant values for STATIC_DLCI_COUNT_MODE_CMD
    STATIC_DLCI_COUNT_MODE_FIXED = "fixed"
    STATIC_DLCI_COUNT_MODE_INCREMENT = "increment"

    STATIC_DLCI_REPEAT_COUNT_CMD = "static_dlci_repeat_count"

    STATIC_DLCI_VALUE_CMD = "static_dlci_value"

    STATIC_DLCI_VALUE_STEP_CMD = "static_dlci_value_step"

    STATIC_ENABLE_CMD = "static_enable"

    STATIC_FR_RANGE_COUNT_CMD = "static_fr_range_count"

    STATIC_IG_ATM_ENCAP_CMD = "static_ig_atm_encap"
    # Constant values for STATIC_IG_ATM_ENCAP_CMD
    STATIC_IG_ATM_ENCAP_LLCROUTEDCLIP = "LLCRoutedCLIP"

    STATIC_IG_INTERFACE_ENABLE_LIST_CMD = "static_ig_interface_enable_list"

    STATIC_IG_INTERFACE_HANDLE_LIST_CMD = "static_ig_interface_handle_list"

    STATIC_IG_IP_TYPE_CMD = "static_ig_ip_type"
    # Constant values for STATIC_IG_IP_TYPE_CMD
    STATIC_IG_IP_TYPE_IPV4 = "ipv4"
    STATIC_IG_IP_TYPE_IPV6 = "ipv6"

    STATIC_IG_RANGE_COUNT_CMD = "static_ig_range_count"

    STATIC_IG_VLAN_ENABLE_CMD = "static_ig_vlan_enable"

    STATIC_INDIRECT_CMD = "static_indirect"

    STATIC_INTF_HANDLE_CMD = "static_intf_handle"

    STATIC_IP_DST_ADDR_CMD = "static_ip_dst_addr"

    STATIC_IP_DST_COUNT_CMD = "static_ip_dst_count"

    STATIC_IP_DST_COUNT_STEP_CMD = "static_ip_dst_count_step"

    STATIC_IP_DST_INCREMENT_CMD = "static_ip_dst_increment"

    STATIC_IP_DST_INCREMENT_STEP_CMD = "static_ip_dst_increment_step"

    STATIC_IP_DST_PREFIX_LEN_CMD = "static_ip_dst_prefix_len"

    STATIC_IP_DST_PREFIX_LEN_STEP_CMD = "static_ip_dst_prefix_len_step"

    STATIC_IP_DST_RANGE_STEP_CMD = "static_ip_dst_range_step"

    STATIC_IP_RANGE_COUNT_CMD = "static_ip_range_count"

    STATIC_L3_PROTOCOL_CMD = "static_l3_protocol"
    # Constant values for STATIC_L3_PROTOCOL_CMD
    STATIC_L3_PROTOCOL_IPV4 = "ipv4"
    STATIC_L3_PROTOCOL_IPV6 = "ipv6"

    STATIC_LAN_COUNT_PER_VC_CMD = "static_lan_count_per_vc"

    STATIC_LAN_INCR_PER_VC_VLAN_MODE_CMD = "static_lan_incr_per_vc_vlan_mode"
    # Constant values for STATIC_LAN_INCR_PER_VC_VLAN_MODE_CMD
    STATIC_LAN_INCR_PER_VC_VLAN_MODE_FIXED = "fixed"
    STATIC_LAN_INCR_PER_VC_VLAN_MODE_INCREMENT = "increment"
    STATIC_LAN_INCR_PER_VC_VLAN_MODE_INNER = "inner"
    STATIC_LAN_INCR_PER_VC_VLAN_MODE_OUTER = "outer"

    STATIC_LAN_INTERMEDIATE_OBJREF_CMD = "static_lan_intermediate_objref"

    STATIC_LAN_MAC_RANGE_MODE_CMD = "static_lan_mac_range_mode"
    # Constant values for STATIC_LAN_MAC_RANGE_MODE_CMD
    STATIC_LAN_MAC_RANGE_MODE_NORMAL = "normal"
    STATIC_LAN_MAC_RANGE_MODE_BUNDLED = "bundled"

    STATIC_LAN_NUMBER_OF_VCS_CMD = "static_lan_number_of_vcs"

    STATIC_LAN_RANGE_COUNT_CMD = "static_lan_range_count"

    STATIC_LAN_SKIP_VLAN_ID_ZERO_CMD = "static_lan_skip_vlan_id_zero"

    STATIC_LAN_TPID_CMD = "static_lan_tpid"
    # Constant values for STATIC_LAN_TPID_CMD
    STATIC_LAN_TPID_0X8100 = "0x8100"
    STATIC_LAN_TPID_0X88A8 = "0x88a8"
    STATIC_LAN_TPID_0X88A8 = "0x88A8"
    STATIC_LAN_TPID_0X9100 = "0x9100"
    STATIC_LAN_TPID_0X9200 = "0x9200"

    STATIC_LAN_VLAN_PRIORITY_CMD = "static_lan_vlan_priority"

    STATIC_LAN_VLAN_STACK_COUNT_CMD = "static_lan_vlan_stack_count"

    STATIC_MAC_DST_CMD = "static_mac_dst"

    STATIC_MAC_DST_COUNT_CMD = "static_mac_dst_count"

    STATIC_MAC_DST_COUNT_STEP_CMD = "static_mac_dst_count_step"

    STATIC_MAC_DST_MODE_CMD = "static_mac_dst_mode"
    # Constant values for STATIC_MAC_DST_MODE_CMD
    STATIC_MAC_DST_MODE_FIXED = "fixed"
    STATIC_MAC_DST_MODE_INCREMENT = "increment"

    STATIC_MAC_DST_STEP_CMD = "static_mac_dst_step"

    STATIC_PVC_COUNT_CMD = "static_pvc_count"

    STATIC_PVC_COUNT_STEP_CMD = "static_pvc_count_step"

    STATIC_RANGE_PER_SPOKE_CMD = "static_range_per_spoke"

    STATIC_SITE_ID_CMD = "static_site_id"

    STATIC_SITE_ID_ENABLE_CMD = "static_site_id_enable"

    STATIC_SITE_ID_STEP_CMD = "static_site_id_step"

    STATIC_VCI_CMD = "static_vci"

    STATIC_VCI_INCREMENT_CMD = "static_vci_increment"

    STATIC_VCI_INCREMENT_STEP_CMD = "static_vci_increment_step"

    STATIC_VCI_STEP_CMD = "static_vci_step"

    STATIC_VLAN_ENABLE_CMD = "static_vlan_enable"

    STATIC_VLAN_ID_CMD = "static_vlan_id"

    STATIC_VLAN_ID_MODE_CMD = "static_vlan_id_mode"
    # Constant values for STATIC_VLAN_ID_MODE_CMD
    STATIC_VLAN_ID_MODE_FIXED = "fixed"
    STATIC_VLAN_ID_MODE_INCREMENT = "increment"
    STATIC_VLAN_ID_MODE_INNER = "inner"
    STATIC_VLAN_ID_MODE_OUTER = "outer"

    STATIC_VLAN_ID_STEP_CMD = "static_vlan_id_step"

    STATIC_VPI_CMD = "static_vpi"

    STATIC_VPI_INCREMENT_CMD = "static_vpi_increment"

    STATIC_VPI_INCREMENT_STEP_CMD = "static_vpi_increment_step"

    STATIC_VPI_STEP_CMD = "static_vpi_step"

    TARGET_LINK_LAYER_ADDRESS_CMD = "target_link_layer_address"

    TRANSMIT_CLOCK_SOURCE_CMD = "transmit_clock_source"
    # Constant values for TRANSMIT_CLOCK_SOURCE_CMD
    TRANSMIT_CLOCK_SOURCE_INTERNAL = "internal"
    TRANSMIT_CLOCK_SOURCE_BITS = "bits"
    TRANSMIT_CLOCK_SOURCE_LOOP = "loop"
    TRANSMIT_CLOCK_SOURCE_EXTERNAL = "external"
    TRANSMIT_CLOCK_SOURCE_INTERNAL_PPM_ADJ = "internal_ppm_adj"

    TRANSMIT_MODE_CMD = "transmit_mode"
    # Constant values for TRANSMIT_MODE_CMD
    TRANSMIT_MODE_ADVANCED = "advanced"
    TRANSMIT_MODE_STREAM = "stream"
    TRANSMIT_MODE_ADVANCED_COARSE = "advanced_coarse"
    TRANSMIT_MODE_STREAM_COARSE = "stream_coarse"

    TX_C2_CMD = "tx_c2"

    TX_FCS_CMD = "tx_fcs"
    # Constant values for TX_FCS_CMD
    TX_FCS_OPT_16 = "opt_16"
    TX_FCS_OPT_32 = "opt_32"

    TX_GAP_CONTROL_MODE_CMD = "tx_gap_control_mode"
    # Constant values for TX_GAP_CONTROL_MODE_CMD
    TX_GAP_CONTROL_MODE_FIXED = "fixed"
    TX_GAP_CONTROL_MODE_AVERAGE = "average"

    TX_IGNORE_RX_LINK_FAULTS_CMD = "tx_ignore_rx_link_faults"

    TX_LANES_CMD = "tx_lanes"

    TX_RX_SYNC_STATS_ENABLE_CMD = "tx_rx_sync_stats_enable"

    TX_RX_SYNC_STATS_INTERVAL_CMD = "tx_rx_sync_stats_interval"

    TX_SCRAMBLING_CMD = "tx_scrambling"

    TYPE_A_ORDERED_SETS_CMD = "type_a_ordered_sets"
    # Constant values for TYPE_A_ORDERED_SETS_CMD
    TYPE_A_ORDERED_SETS_LOCAL_FAULT = "local_fault"
    TYPE_A_ORDERED_SETS_REMOTE_FAULT = "remote_fault"

    TYPE_B_ORDERED_SETS_CMD = "type_b_ordered_sets"
    # Constant values for TYPE_B_ORDERED_SETS_CMD
    TYPE_B_ORDERED_SETS_LOCAL_FAULT = "local_fault"
    TYPE_B_ORDERED_SETS_REMOTE_FAULT = "remote_fault"

    USE_VPN_PARAMETERS_CMD = "use_vpn_parameters"

    VCI_CMD = "vci"

    VCI_COUNT_CMD = "vci_count"

    VCI_STEP_CMD = "vci_step"

    VLAN_CMD = "vlan"

    VLAN_ID_CMD = "vlan_id"

    VLAN_ID_COUNT_CMD = "vlan_id_count"

    VLAN_ID_INNER_CMD = "vlan_id_inner"

    VLAN_ID_INNER_COUNT_CMD = "vlan_id_inner_count"

    VLAN_ID_INNER_MODE_CMD = "vlan_id_inner_mode"
    # Constant values for VLAN_ID_INNER_MODE_CMD
    VLAN_ID_INNER_MODE_FIXED = "fixed"
    VLAN_ID_INNER_MODE_INCREMENT = "increment"

    VLAN_ID_INNER_STEP_CMD = "vlan_id_inner_step"

    VLAN_ID_LIST_CMD = "vlan_id_list"

    VLAN_ID_MODE_CMD = "vlan_id_mode"
    # Constant values for VLAN_ID_MODE_CMD
    VLAN_ID_MODE_FIXED = "fixed"
    VLAN_ID_MODE_INCREMENT = "increment"

    VLAN_ID_STEP_CMD = "vlan_id_step"

    VLAN_PROTOCOL_ID_CMD = "vlan_protocol_id"
    # Constant values for VLAN_PROTOCOL_ID_CMD
    VLAN_PROTOCOL_ID_0X8100 = "0x8100"
    VLAN_PROTOCOL_ID_0X88A8 = "0x88A8"
    VLAN_PROTOCOL_ID_0X9100 = "0x9100"
    VLAN_PROTOCOL_ID_0X9200 = "0x9200"
    VLAN_PROTOCOL_ID_0X9300 = "0x9300"

    VLAN_TPID_CMD = "vlan_tpid"
    # Constant values for VLAN_TPID_CMD
    VLAN_TPID_0X8100 = "0x8100"
    VLAN_TPID_0X88A8 = "0x88a8"
    VLAN_TPID_0X88A8 = "0x88A8"
    VLAN_TPID_0X9100 = "0x9100"
    VLAN_TPID_0X9200 = "0x9200"
    VLAN_TPID_0X9300 = "0x9300"

    VLAN_USER_PRIORITY_CMD = "vlan_user_priority"

    VLAN_USER_PRIORITY_STEP_CMD = "vlan_user_priority_step"

    VPI_CMD = "vpi"

    VPI_COUNT_CMD = "vpi_count"

    VPI_STEP_CMD = "vpi_step"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -additional_fcoe_stat_1
    -additional_fcoe_stat_2
    -addresses_per_svlan
    -addresses_per_vci
    -addresses_per_vlan
    -addresses_per_vpi
    -arp
    -arp_on_linkup
    -arp_refresh_interval
    -arp_req_retries
    -arp_req_timer
    -arp_send_req
    -atm_enable_coset
    -atm_enable_pattern_matching
    -atm_encapsulation
    -atm_filler_cell
    -atm_interface_type
    -atm_packet_decode_mode
    -atm_reassembly_timeout
    -auto_detect_instrumentation_type
    -autonegotiation
    -bad_blocks_number
    -bert_configuration
    -bert_error_insertion
    -check_gateway_exists
    -check_opposite_ip_version
    -clocksource
    -connected_count
    -connected_to_handle
    -data_integrity
    -duplex
    -enable_data_center_shared_stats
    -enable_flow_control
    -enable_loopback
    -enable_ndp
    -enable_rs_fec
    -enable_rs_fec_statistics
    -ethernet_attempt_enabled
    -ethernet_attempt_interval
    -ethernet_attempt_rate
    -ethernet_attempt_scale_mode
    -ethernet_diconnect_enabled
    -ethernet_disconnect_interval
    -ethernet_disconnect_rate
    -ethernet_disconnect_scale_mode
    -fc_credit_starvation_value
    -fc_fixed_delay_value
    -fc_force_errors
    -fc_max_delay_for_random_value
    -fc_min_delay_for_random_value
    -fc_no_rrdy_after
    -fc_rrdy_response_delays
    -fc_tx_ignore_available_credits
    -fc_tx_ignore_rx_link_faults
    -fcoe_flow_control_type
    -fcoe_priority_group_size
    -fcoe_priority_groups
    -fcoe_support_data_center_mode
    -flow_control_directed_addr
    -framing
    -gateway
    -gateway_incr_mode
    -gateway_step
    -good_blocks_number
    -gre_checksum_enable
    -gre_count
    -gre_dst_ip_addr
    -gre_dst_ip_addr_step
    -gre_ip_addr
    -gre_ip_addr_step
    -gre_ip_prefix_length
    -gre_ipv6_addr
    -gre_ipv6_addr_step
    -gre_ipv6_prefix_length
    -gre_key_enable
    -gre_key_in
    -gre_key_out
    -gre_seq_enable
    -ieee_media_defaults
    -ignore_link
    -integrity_signature
    -integrity_signature_offset
    -interface_handle
    -internal_ppm_adjust
    -intf_ip_addr
    -intf_ip_addr_step
    -intf_mode
    -intrinsic_latency_adjustment
    -ipv4_attempt_enabled
    -ipv4_attempt_interval
    -ipv4_attempt_rate
    -ipv4_attempt_scale_mode
    -ipv4_diconnect_enabled
    -ipv4_disconnect_interval
    -ipv4_disconnect_rate
    -ipv4_disconnect_scale_mode
    -ipv4_manual_gateway_mac
    -ipv4_manual_gateway_mac_step
    -ipv4_re_send_arp_on_link_up
    -ipv4_resolve_gateway
    -ipv4_send_arp_interval
    -ipv4_send_arp_max_outstanding
    -ipv4_send_arp_rate
    -ipv4_send_arp_scale_mode
    -ipv6_addr_mode
    -ipv6_attempt_enabled
    -ipv6_attempt_interval
    -ipv6_attempt_rate
    -ipv6_attempt_scale_mode
    -ipv6_autoconfiguration_attempt_enabled
    -ipv6_autoconfiguration_attempt_interval
    -ipv6_autoconfiguration_attempt_max_outstanding
    -ipv6_autoconfiguration_attempt_rate
    -ipv6_autoconfiguration_attempt_scale_mode
    -ipv6_autoconfiguration_disconnect_enabled
    -ipv6_autoconfiguration_disconnect_interval
    -ipv6_autoconfiguration_disconnect_max_outstanding
    -ipv6_autoconfiguration_disconnect_rate
    -ipv6_autoconfiguration_disconnect_scale_mode
    -ipv6_autoconfiguration_send_ns_enabled
    -ipv6_autoconfiguration_send_ns_max_outstanding
    -ipv6_autoconfiguration_send_ns_rate
    -ipv6_autoconfiguration_send_ns_scale_mode
    -ipv6_autoconfiguration_send_rs_enabled
    -ipv6_autoconfiguration_send_rs_interval
    -ipv6_autoconfiguration_send_rs_max_outstanding
    -ipv6_autoconfiguration_send_rs_rate
    -ipv6_autoconfiguration_send_rs_scale_mode
    -ipv6_diconnect_enabled
    -ipv6_disconnect_interval
    -ipv6_disconnect_rate
    -ipv6_disconnect_scale_mode
    -ipv6_gateway
    -ipv6_gateway_step
    -ipv6_intf_addr
    -ipv6_intf_addr_step
    -ipv6_loopback_multiplier
    -ipv6_manual_gateway_mac
    -ipv6_manual_gateway_mac_step
    -ipv6_multiplier
    -ipv6_prefix_length
    -ipv6_re_send_ns_on_link_up
    -ipv6_resolve_gateway
    -ipv6_send_ns_interval
    -ipv6_send_ns_max_outstanding
    -ipv6_send_ns_rate
    -ipv6_send_ns_scale_mode
    -l23_config_type
    -laser_on
    -link_training
    -loop_continuously
    -loop_count_number
    -master_slave_mode
    -mode
    -mss
    -mtu
    -ndp_send_req
    -netmask
    -no_write
    -notify_mac_move
    -ns_on_linkup
    -op_mode
    -override_existence_check
    -override_tracking
    -pcs_count
    -pcs_enabled_continuous
    -pcs_lane
    -pcs_marker_fields
    -pcs_period
    -pcs_period_type
    -pcs_repeat
    -pcs_sync_bits
    -pgid_128k_bin_enable
    -pgid_encap
    -pgid_mask
    -pgid_mode
    -pgid_offset
    -pgid_split1_mask
    -pgid_split1_offset
    -pgid_split1_offset_from
    -pgid_split1_width
    -pgid_split2_mask
    -pgid_split2_offset
    -pgid_split2_offset_from
    -pgid_split2_width
    -pgid_split3_mask
    -pgid_split3_offset
    -pgid_split3_offset_from
    -pgid_split3_width
    -phy_mode
    -ping_dst
    -port_handle
    -port_rx_mode
    -ppp_ipv4_address
    -ppp_ipv4_negotiation
    -ppp_ipv6_negotiation
    -ppp_mpls_negotiation
    -ppp_osi_negotiation
    -protocol_handle
    -protocol_name
    -pvc_incr_mode
    -qinq_incr_mode
    -qos_byte_offset
    -qos_packet_type
    -qos_pattern_mask
    -qos_pattern_match
    -qos_pattern_offset
    -qos_stats
    -router_solicitation_retries
    -rpr_hec_seed
    -rx_c2
    -rx_fcs
    -rx_scrambling
    -send_ping
    -send_router_solicitation
    -send_sets_mode
    -sequence_checking
    -sequence_num_offset
    -signature
    -signature_mask
    -signature_offset
    -signature_start_offset
    -single_arp_per_gateway
    -single_ns_per_gateway
    -site_id
    -speed
    -src_mac_addr
    -src_mac_addr_step
    -start_error_insertion
    -static_atm_header_encapsulation
    -static_atm_range_count
    -static_dlci_count_mode
    -static_dlci_repeat_count
    -static_dlci_value
    -static_dlci_value_step
    -static_enable
    -static_fr_range_count
    -static_ig_atm_encap
    -static_ig_interface_enable_list
    -static_ig_interface_handle_list
    -static_ig_ip_type
    -static_ig_range_count
    -static_ig_vlan_enable
    -static_indirect
    -static_intf_handle
    -static_ip_dst_addr
    -static_ip_dst_count
    -static_ip_dst_count_step
    -static_ip_dst_increment
    -static_ip_dst_increment_step
    -static_ip_dst_prefix_len
    -static_ip_dst_prefix_len_step
    -static_ip_dst_range_step
    -static_ip_range_count
    -static_l3_protocol
    -static_lan_count_per_vc
    -static_lan_incr_per_vc_vlan_mode
    -static_lan_intermediate_objref
    -static_lan_mac_range_mode
    -static_lan_number_of_vcs
    -static_lan_range_count
    -static_lan_skip_vlan_id_zero
    -static_lan_tpid
    -static_lan_vlan_priority
    -static_lan_vlan_stack_count
    -static_mac_dst
    -static_mac_dst_count
    -static_mac_dst_count_step
    -static_mac_dst_mode
    -static_mac_dst_step
    -static_pvc_count
    -static_pvc_count_step
    -static_range_per_spoke
    -static_site_id
    -static_site_id_enable
    -static_site_id_step
    -static_vci
    -static_vci_increment
    -static_vci_increment_step
    -static_vci_step
    -static_vlan_enable
    -static_vlan_id
    -static_vlan_id_mode
    -static_vlan_id_step
    -static_vpi
    -static_vpi_increment
    -static_vpi_increment_step
    -static_vpi_step
    -target_link_layer_address
    -transmit_clock_source
    -transmit_mode
    -tx_c2
    -tx_fcs
    -tx_gap_control_mode
    -tx_ignore_rx_link_faults
    -tx_lanes
    -tx_rx_sync_stats_enable
    -tx_rx_sync_stats_interval
    -tx_scrambling
    -type_a_ordered_sets
    -type_b_ordered_sets
    -use_vpn_parameters
    -vci
    -vci_count
    -vci_step
    -vlan
    -vlan_id
    -vlan_id_count
    -vlan_id_inner
    -vlan_id_inner_count
    -vlan_id_inner_mode
    -vlan_id_inner_step
    -vlan_id_list
    -vlan_id_mode
    -vlan_id_step
    -vlan_protocol_id
    -vlan_tpid
    -vlan_user_priority
    -vlan_user_priority_step
    -vpi
    -vpi_count
    -vpi_step
If you want to update this file, look in the CSV
"""
