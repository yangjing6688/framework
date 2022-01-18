from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: traffic_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class TrafficConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(TrafficConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[TrafficConfigConstants.ADJUST_RATE_CMD] = "dummyValue1" # static value
        dummyDict[TrafficConfigConstants.ALLOW_SELF_DESTINED_CMD] = "dummyValue2" # static value
        dummyDict[TrafficConfigConstants.APP_PROFILE_TYPE_CMD] = "dummyValue3" # static value
        dummyDict[TrafficConfigConstants.ARP_DST_HW_ADDR_CMD] = "dummyValue4" # static value
        dummyDict[TrafficConfigConstants.ARP_DST_HW_COUNT_CMD] = "dummyValue5" # static value
        dummyDict[TrafficConfigConstants.ARP_DST_HW_MODE_CMD] = TrafficConfigConstants.ARP_DST_HW_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ARP_DST_HW_STEP_CMD] = "dummyValue7" # static value
        dummyDict[TrafficConfigConstants.ARP_DST_HW_TRACKING_CMD] = "dummyValue8" # static value
        dummyDict[TrafficConfigConstants.ARP_HW_ADDRESS_LENGTH_CMD] = "dummyValue9" # static value
        dummyDict[TrafficConfigConstants.ARP_HW_ADDRESS_LENGTH_COUNT_CMD] = "dummyValue10" # static value
        dummyDict[TrafficConfigConstants.ARP_HW_ADDRESS_LENGTH_MODE_CMD] = TrafficConfigConstants.ARP_HW_ADDRESS_LENGTH_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ARP_HW_ADDRESS_LENGTH_STEP_CMD] = "dummyValue12" # static value
        dummyDict[TrafficConfigConstants.ARP_HW_ADDRESS_LENGTH_TRACKING_CMD] = "dummyValue13" # static value
        dummyDict[TrafficConfigConstants.ARP_HW_TYPE_CMD] = "dummyValue14" # static value
        dummyDict[TrafficConfigConstants.ARP_HW_TYPE_COUNT_CMD] = "dummyValue15" # static value
        dummyDict[TrafficConfigConstants.ARP_HW_TYPE_MODE_CMD] = TrafficConfigConstants.ARP_HW_TYPE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ARP_HW_TYPE_STEP_CMD] = "dummyValue17" # static value
        dummyDict[TrafficConfigConstants.ARP_HW_TYPE_TRACKING_CMD] = "dummyValue18" # static value
        dummyDict[TrafficConfigConstants.ARP_OPERATION_CMD] = TrafficConfigConstants.ARP_OPERATION_ARPREQUEST # constant value
        dummyDict[TrafficConfigConstants.ARP_OPERATION_MODE_CMD] = TrafficConfigConstants.ARP_OPERATION_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ARP_OPERATION_TRACKING_CMD] = "dummyValue21" # static value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_ADDR_LENGTH_CMD] = "dummyValue22" # static value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_ADDR_LENGTH_COUNT_CMD] = "dummyValue23" # static value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_ADDR_LENGTH_MODE_CMD] = TrafficConfigConstants.ARP_PROTOCOL_ADDR_LENGTH_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_ADDR_LENGTH_STEP_CMD] = "dummyValue25" # static value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_ADDR_LENGTH_TRACKING_CMD] = "dummyValue26" # static value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_TYPE_CMD] = "dummyValue27" # static value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_TYPE_COUNT_CMD] = "dummyValue28" # static value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_TYPE_MODE_CMD] = TrafficConfigConstants.ARP_PROTOCOL_TYPE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_TYPE_STEP_CMD] = "dummyValue30" # static value
        dummyDict[TrafficConfigConstants.ARP_PROTOCOL_TYPE_TRACKING_CMD] = "dummyValue31" # static value
        dummyDict[TrafficConfigConstants.ARP_SRC_HW_ADDR_CMD] = "dummyValue32" # static value
        dummyDict[TrafficConfigConstants.ARP_SRC_HW_COUNT_CMD] = "dummyValue33" # static value
        dummyDict[TrafficConfigConstants.ARP_SRC_HW_MODE_CMD] = TrafficConfigConstants.ARP_SRC_HW_MODE_DECREMENT # constant value
        dummyDict[TrafficConfigConstants.ARP_SRC_HW_STEP_CMD] = "dummyValue35" # static value
        dummyDict[TrafficConfigConstants.ARP_SRC_HW_TRACKING_CMD] = "dummyValue36" # static value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VCI_DATA_ITEM_LIST_CMD] = "dummyValue37" # static value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VCI_MASK_SELECT_CMD] = "dummyValue38" # static value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VCI_MASK_VALUE_CMD] = "dummyValue39" # static value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VCI_MODE_CMD] = TrafficConfigConstants.ATM_COUNTER_VCI_MODE_CONT_DECR # constant value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VCI_TYPE_CMD] = TrafficConfigConstants.ATM_COUNTER_VCI_TYPE_RANDOM # constant value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VPI_DATA_ITEM_LIST_CMD] = "dummyValue42" # static value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VPI_MASK_SELECT_CMD] = "dummyValue43" # static value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VPI_MASK_VALUE_CMD] = "dummyValue44" # static value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VPI_MODE_CMD] = TrafficConfigConstants.ATM_COUNTER_VPI_MODE_CONT_DECR # constant value
        dummyDict[TrafficConfigConstants.ATM_COUNTER_VPI_TYPE_CMD] = TrafficConfigConstants.ATM_COUNTER_VPI_TYPE_RANDOM # constant value
        dummyDict[TrafficConfigConstants.ATM_HEADER_AAL5ERROR_CMD] = TrafficConfigConstants.ATM_HEADER_AAL5ERROR_BAD_CRC # constant value
        dummyDict[TrafficConfigConstants.ATM_HEADER_CELL_LOSS_PRIORITY_CMD] = "dummyValue48" # static value
        dummyDict[TrafficConfigConstants.ATM_HEADER_CPCS_LENGTH_CMD] = "dummyValue49" # static value
        dummyDict[TrafficConfigConstants.ATM_HEADER_ENABLE_AUTO_VPI_VCI_CMD] = "dummyValue50" # static value
        dummyDict[TrafficConfigConstants.ATM_HEADER_ENABLE_CL_CMD] = "dummyValue51" # static value
        dummyDict[TrafficConfigConstants.ATM_HEADER_ENABLE_CPCS_LENGTH_CMD] = "dummyValue52" # static value
        dummyDict[TrafficConfigConstants.ATM_HEADER_ENCAPSULATION_CMD] = TrafficConfigConstants.ATM_HEADER_ENCAPSULATION_LLC_NLPID_ROUTED # constant value
        dummyDict[TrafficConfigConstants.ATM_HEADER_GENERIC_FLOW_CTRL_CMD] = "dummyValue54" # static value
        dummyDict[TrafficConfigConstants.ATM_HEADER_HEC_ERRORS_CMD] = "dummyValue55" # static value
        dummyDict[TrafficConfigConstants.ATM_RANGE_COUNT_CMD] = "dummyValue56" # static value
        dummyDict[TrafficConfigConstants.BECN_CMD] = "dummyValue57" # static value
        dummyDict[TrafficConfigConstants.BIDIRECTIONAL_CMD] = "dummyValue58" # static value
        dummyDict[TrafficConfigConstants.BURST_LOOP_COUNT_CMD] = "dummyValue59" # static value
        dummyDict[TrafficConfigConstants.CIRCUIT_ENDPOINT_TYPE_CMD] = TrafficConfigConstants.CIRCUIT_ENDPOINT_TYPE_IPV6_APPLICATION_TRAFFIC # constant value
        dummyDict[TrafficConfigConstants.CIRCUIT_TYPE_CMD] = TrafficConfigConstants.CIRCUIT_TYPE_6PE # constant value
        dummyDict[TrafficConfigConstants.COMMAND_RESPONSE_CMD] = "dummyValue62" # static value
        dummyDict[TrafficConfigConstants.CONVERT_TO_RAW_CMD] = "dummyValue63" # static value
        dummyDict[TrafficConfigConstants.CSRC_LIST_CMD] = "dummyValue64" # static value
        dummyDict[TrafficConfigConstants.CUSTOM_OFFSET_CMD] = "dummyValue65" # static value
        dummyDict[TrafficConfigConstants.CUSTOM_VALUES_CMD] = "dummyValue66" # static value
        dummyDict[TrafficConfigConstants.DATA_PATTERN_CMD] = "dummyValue67" # static value
        dummyDict[TrafficConfigConstants.DATA_PATTERN_MODE_CMD] = TrafficConfigConstants.DATA_PATTERN_MODE_INCR_WORD # constant value
        dummyDict[TrafficConfigConstants.DATA_TOS_CMD] = "dummyValue69" # static value
        dummyDict[TrafficConfigConstants.DATA_TOS_COUNT_CMD] = "dummyValue70" # static value
        dummyDict[TrafficConfigConstants.DATA_TOS_MODE_CMD] = TrafficConfigConstants.DATA_TOS_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DATA_TOS_STEP_CMD] = "dummyValue72" # static value
        dummyDict[TrafficConfigConstants.DATA_TOS_TRACKING_CMD] = "dummyValue73" # static value
        dummyDict[TrafficConfigConstants.DESTINATION_FILTER_CMD] = TrafficConfigConstants.DESTINATION_FILTER_6PE # constant value
        dummyDict[TrafficConfigConstants.DHCP_BOOT_FILENAME_CMD] = "dummyValue75" # static value
        dummyDict[TrafficConfigConstants.DHCP_BOOT_FILENAME_TRACKING_CMD] = "dummyValue76" # static value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_HW_ADDR_CMD] = "dummyValue77" # static value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_HW_ADDR_COUNT_CMD] = "dummyValue78" # static value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_HW_ADDR_MODE_CMD] = TrafficConfigConstants.DHCP_CLIENT_HW_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_HW_ADDR_STEP_CMD] = "dummyValue80" # static value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_HW_ADDR_TRACKING_CMD] = "dummyValue81" # static value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_CMD] = "dummyValue82" # static value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_COUNT_CMD] = "dummyValue83" # static value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_MODE_CMD] = TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_STEP_CMD] = "dummyValue85" # static value
        dummyDict[TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_TRACKING_CMD] = "dummyValue86" # static value
        dummyDict[TrafficConfigConstants.DHCP_FLAGS_CMD] = TrafficConfigConstants.DHCP_FLAGS_BROADCAST # constant value
        dummyDict[TrafficConfigConstants.DHCP_FLAGS_MODE_CMD] = TrafficConfigConstants.DHCP_FLAGS_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.DHCP_FLAGS_TRACKING_CMD] = "dummyValue89" # static value
        dummyDict[TrafficConfigConstants.DHCP_HOPS_CMD] = "dummyValue90" # static value
        dummyDict[TrafficConfigConstants.DHCP_HOPS_COUNT_CMD] = "dummyValue91" # static value
        dummyDict[TrafficConfigConstants.DHCP_HOPS_MODE_CMD] = TrafficConfigConstants.DHCP_HOPS_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_HOPS_STEP_CMD] = "dummyValue93" # static value
        dummyDict[TrafficConfigConstants.DHCP_HOPS_TRACKING_CMD] = "dummyValue94" # static value
        dummyDict[TrafficConfigConstants.DHCP_HW_LEN_CMD] = "dummyValue95" # static value
        dummyDict[TrafficConfigConstants.DHCP_HW_LEN_COUNT_CMD] = "dummyValue96" # static value
        dummyDict[TrafficConfigConstants.DHCP_HW_LEN_MODE_CMD] = TrafficConfigConstants.DHCP_HW_LEN_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_HW_LEN_STEP_CMD] = "dummyValue98" # static value
        dummyDict[TrafficConfigConstants.DHCP_HW_LEN_TRACKING_CMD] = "dummyValue99" # static value
        dummyDict[TrafficConfigConstants.DHCP_HW_TYPE_CMD] = "dummyValue100" # static value
        dummyDict[TrafficConfigConstants.DHCP_HW_TYPE_COUNT_CMD] = "dummyValue101" # static value
        dummyDict[TrafficConfigConstants.DHCP_HW_TYPE_MODE_CMD] = TrafficConfigConstants.DHCP_HW_TYPE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_HW_TYPE_STEP_CMD] = "dummyValue103" # static value
        dummyDict[TrafficConfigConstants.DHCP_HW_TYPE_TRACKING_CMD] = "dummyValue104" # static value
        dummyDict[TrafficConfigConstants.DHCP_MAGIC_COOKIE_CMD] = "dummyValue105" # static value
        dummyDict[TrafficConfigConstants.DHCP_MAGIC_COOKIE_COUNT_CMD] = "dummyValue106" # static value
        dummyDict[TrafficConfigConstants.DHCP_MAGIC_COOKIE_MODE_CMD] = TrafficConfigConstants.DHCP_MAGIC_COOKIE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_MAGIC_COOKIE_STEP_CMD] = "dummyValue108" # static value
        dummyDict[TrafficConfigConstants.DHCP_MAGIC_COOKIE_TRACKING_CMD] = "dummyValue109" # static value
        dummyDict[TrafficConfigConstants.DHCP_OPERATION_CODE_CMD] = TrafficConfigConstants.DHCP_OPERATION_CODE_REPLY # constant value
        dummyDict[TrafficConfigConstants.DHCP_OPERATION_CODE_MODE_CMD] = TrafficConfigConstants.DHCP_OPERATION_CODE_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.DHCP_OPERATION_CODE_TRACKING_CMD] = "dummyValue112" # static value
        dummyDict[TrafficConfigConstants.DHCP_OPTION_CMD] = TrafficConfigConstants.DHCP_OPTION_DHCP_SUBNET_MASK # constant value
        dummyDict[TrafficConfigConstants.DHCP_OPTION_DATA_CMD] = "dummyValue114" # static value
        dummyDict[TrafficConfigConstants.DHCP_RELAY_AGENT_IP_ADDR_CMD] = "dummyValue115" # static value
        dummyDict[TrafficConfigConstants.DHCP_RELAY_AGENT_IP_ADDR_COUNT_CMD] = "dummyValue116" # static value
        dummyDict[TrafficConfigConstants.DHCP_RELAY_AGENT_IP_ADDR_MODE_CMD] = TrafficConfigConstants.DHCP_RELAY_AGENT_IP_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_RELAY_AGENT_IP_ADDR_STEP_CMD] = "dummyValue118" # static value
        dummyDict[TrafficConfigConstants.DHCP_RELAY_AGENT_IP_ADDR_TRACKING_CMD] = "dummyValue119" # static value
        dummyDict[TrafficConfigConstants.DHCP_SECONDS_CMD] = "dummyValue120" # static value
        dummyDict[TrafficConfigConstants.DHCP_SECONDS_COUNT_CMD] = "dummyValue121" # static value
        dummyDict[TrafficConfigConstants.DHCP_SECONDS_MODE_CMD] = TrafficConfigConstants.DHCP_SECONDS_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_SECONDS_STEP_CMD] = "dummyValue123" # static value
        dummyDict[TrafficConfigConstants.DHCP_SECONDS_TRACKING_CMD] = "dummyValue124" # static value
        dummyDict[TrafficConfigConstants.DHCP_SERVER_HOST_NAME_CMD] = "dummyValue125" # static value
        dummyDict[TrafficConfigConstants.DHCP_SERVER_HOST_NAME_TRACKING_CMD] = "dummyValue126" # static value
        dummyDict[TrafficConfigConstants.DHCP_SERVER_IP_ADDR_CMD] = "dummyValue127" # static value
        dummyDict[TrafficConfigConstants.DHCP_SERVER_IP_ADDR_COUNT_CMD] = "dummyValue128" # static value
        dummyDict[TrafficConfigConstants.DHCP_SERVER_IP_ADDR_MODE_CMD] = TrafficConfigConstants.DHCP_SERVER_IP_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_SERVER_IP_ADDR_STEP_CMD] = "dummyValue130" # static value
        dummyDict[TrafficConfigConstants.DHCP_SERVER_IP_ADDR_TRACKING_CMD] = "dummyValue131" # static value
        dummyDict[TrafficConfigConstants.DHCP_TRANSACTION_ID_CMD] = "dummyValue132" # static value
        dummyDict[TrafficConfigConstants.DHCP_TRANSACTION_ID_COUNT_CMD] = "dummyValue133" # static value
        dummyDict[TrafficConfigConstants.DHCP_TRANSACTION_ID_MODE_CMD] = TrafficConfigConstants.DHCP_TRANSACTION_ID_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_TRANSACTION_ID_STEP_CMD] = "dummyValue135" # static value
        dummyDict[TrafficConfigConstants.DHCP_TRANSACTION_ID_TRACKING_CMD] = "dummyValue136" # static value
        dummyDict[TrafficConfigConstants.DHCP_YOUR_IP_ADDR_CMD] = "dummyValue137" # static value
        dummyDict[TrafficConfigConstants.DHCP_YOUR_IP_ADDR_COUNT_CMD] = "dummyValue138" # static value
        dummyDict[TrafficConfigConstants.DHCP_YOUR_IP_ADDR_MODE_CMD] = TrafficConfigConstants.DHCP_YOUR_IP_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.DHCP_YOUR_IP_ADDR_STEP_CMD] = "dummyValue140" # static value
        dummyDict[TrafficConfigConstants.DHCP_YOUR_IP_ADDR_TRACKING_CMD] = "dummyValue141" # static value
        dummyDict[TrafficConfigConstants.DISCARD_ELIGIBLE_CMD] = "dummyValue142" # static value
        dummyDict[TrafficConfigConstants.DLCI_CORE_ENABLE_CMD] = "dummyValue143" # static value
        dummyDict[TrafficConfigConstants.DLCI_CORE_VALUE_CMD] = "dummyValue144" # static value
        dummyDict[TrafficConfigConstants.DLCI_COUNT_MODE_CMD] = TrafficConfigConstants.DLCI_COUNT_MODE_RANDOM # constant value
        dummyDict[TrafficConfigConstants.DLCI_EXTENDED_ADDRESS0_CMD] = "dummyValue146" # static value
        dummyDict[TrafficConfigConstants.DLCI_EXTENDED_ADDRESS1_CMD] = "dummyValue147" # static value
        dummyDict[TrafficConfigConstants.DLCI_EXTENDED_ADDRESS2_CMD] = "dummyValue148" # static value
        dummyDict[TrafficConfigConstants.DLCI_EXTENDED_ADDRESS3_CMD] = "dummyValue149" # static value
        dummyDict[TrafficConfigConstants.DLCI_MASK_SELECT_CMD] = "dummyValue150" # static value
        dummyDict[TrafficConfigConstants.DLCI_MASK_VALUE_CMD] = "dummyValue151" # static value
        dummyDict[TrafficConfigConstants.DLCI_REPEAT_COUNT_CMD] = "dummyValue152" # static value
        dummyDict[TrafficConfigConstants.DLCI_REPEAT_COUNT_STEP_CMD] = "dummyValue153" # static value
        dummyDict[TrafficConfigConstants.DLCI_SIZE_CMD] = "dummyValue154" # static value
        dummyDict[TrafficConfigConstants.DLCI_VALUE_CMD] = "dummyValue155" # static value
        dummyDict[TrafficConfigConstants.DLCI_VALUE_STEP_CMD] = "dummyValue156" # static value
        dummyDict[TrafficConfigConstants.DURATION_CMD] = "dummyValue157" # static value
        dummyDict[TrafficConfigConstants.DYNAMIC_UPDATE_FIELDS_CMD] = TrafficConfigConstants.DYNAMIC_UPDATE_FIELDS_PPP # constant value
        dummyDict[TrafficConfigConstants.EGRESS_CUSTOM_FIELD_OFFSET_CMD] = "dummyValue159" # static value
        dummyDict[TrafficConfigConstants.EGRESS_CUSTOM_OFFSET_CMD] = TrafficConfigConstants.EGRESS_CUSTOM_OFFSET_NA # constant value
        dummyDict[TrafficConfigConstants.EGRESS_CUSTOM_WIDTH_CMD] = TrafficConfigConstants.EGRESS_CUSTOM_WIDTH_NA # constant value
        dummyDict[TrafficConfigConstants.EGRESS_TRACKING_CMD] = TrafficConfigConstants.EGRESS_TRACKING_OUTER_VLAN_PRIORITY # constant value
        dummyDict[TrafficConfigConstants.EGRESS_TRACKING_ENCAP_CMD] = TrafficConfigConstants.EGRESS_TRACKING_ENCAP_POS_PPP # constant value
        dummyDict[TrafficConfigConstants.EMULATION_DST_HANDLE_CMD] = "dummyValue164" # static value
        dummyDict[TrafficConfigConstants.EMULATION_DST_VLAN_PROTOCOL_TAG_ID_CMD] = "dummyValue165" # static value
        dummyDict[TrafficConfigConstants.EMULATION_MULTICAST_DST_HANDLE_CMD] = "dummyValue166" # static value
        dummyDict[TrafficConfigConstants.EMULATION_MULTICAST_DST_HANDLE_TYPE_CMD] = "dummyValue167" # static value
        dummyDict[TrafficConfigConstants.EMULATION_MULTICAST_RCVR_HANDLE_CMD] = "dummyValue168" # static value
        dummyDict[TrafficConfigConstants.EMULATION_MULTICAST_RCVR_HOST_INDEX_CMD] = "dummyValue169" # static value
        dummyDict[TrafficConfigConstants.EMULATION_MULTICAST_RCVR_MCAST_INDEX_CMD] = "dummyValue170" # static value
        dummyDict[TrafficConfigConstants.EMULATION_MULTICAST_RCVR_PORT_INDEX_CMD] = "dummyValue171" # static value
        dummyDict[TrafficConfigConstants.EMULATION_OVERRIDE_PPP_IP_ADDR_CMD] = TrafficConfigConstants.EMULATION_OVERRIDE_PPP_IP_ADDR_BOTH # constant value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_DST_HANDLE_CMD] = "dummyValue173" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_DST_INTF_COUNT_CMD] = "dummyValue174" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_DST_INTF_START_CMD] = "dummyValue175" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_DST_PORT_COUNT_CMD] = "dummyValue176" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_DST_PORT_START_CMD] = "dummyValue177" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_SRC_HANDLE_CMD] = "dummyValue178" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_SRC_INTF_COUNT_CMD] = "dummyValue179" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_SRC_INTF_START_CMD] = "dummyValue180" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_SRC_PORT_COUNT_CMD] = "dummyValue181" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SCALABLE_SRC_PORT_START_CMD] = "dummyValue182" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SRC_HANDLE_CMD] = "dummyValue183" # static value
        dummyDict[TrafficConfigConstants.EMULATION_SRC_VLAN_PROTOCOL_TAG_ID_CMD] = "dummyValue184" # static value
        dummyDict[TrafficConfigConstants.ENABLE_AUTO_DETECT_INSTRUMENTATION_CMD] = "dummyValue185" # static value
        dummyDict[TrafficConfigConstants.ENABLE_CE_TO_PE_TRAFFIC_CMD] = "dummyValue186" # static value
        dummyDict[TrafficConfigConstants.ENABLE_DATA_INTEGRITY_CMD] = "dummyValue187" # static value
        dummyDict[TrafficConfigConstants.ENABLE_DYNAMIC_MPLS_LABELS_CMD] = "dummyValue188" # static value
        dummyDict[TrafficConfigConstants.ENABLE_OVERRIDE_VALUE_CMD] = "dummyValue189" # static value
        dummyDict[TrafficConfigConstants.ENABLE_PGID_CMD] = "dummyValue190" # static value
        dummyDict[TrafficConfigConstants.ENABLE_TEST_OBJECTIVE_CMD] = "dummyValue191" # static value
        dummyDict[TrafficConfigConstants.ENABLE_TIME_STAMP_CMD] = "dummyValue192" # static value
        dummyDict[TrafficConfigConstants.ENABLE_UDF1_CMD] = "dummyValue193" # static value
        dummyDict[TrafficConfigConstants.ENABLE_UDF2_CMD] = "dummyValue194" # static value
        dummyDict[TrafficConfigConstants.ENABLE_UDF3_CMD] = "dummyValue195" # static value
        dummyDict[TrafficConfigConstants.ENABLE_UDF4_CMD] = "dummyValue196" # static value
        dummyDict[TrafficConfigConstants.ENABLE_UDF5_CMD] = "dummyValue197" # static value
        dummyDict[TrafficConfigConstants.ENDPOINTSET_COUNT_CMD] = "dummyValue198" # static value
        dummyDict[TrafficConfigConstants.ENFORCE_MIN_GAP_CMD] = "dummyValue199" # static value
        dummyDict[TrafficConfigConstants.ETHERNET_TYPE_CMD] = TrafficConfigConstants.ETHERNET_TYPE_ETHERNETII # constant value
        dummyDict[TrafficConfigConstants.ETHERNET_VALUE_CMD] = "dummyValue201" # static value
        dummyDict[TrafficConfigConstants.ETHERNET_VALUE_COUNT_CMD] = "dummyValue202" # static value
        dummyDict[TrafficConfigConstants.ETHERNET_VALUE_MODE_CMD] = TrafficConfigConstants.ETHERNET_VALUE_MODE_DEFAULT # constant value
        dummyDict[TrafficConfigConstants.ETHERNET_VALUE_STEP_CMD] = "dummyValue204" # static value
        dummyDict[TrafficConfigConstants.ETHERNET_VALUE_TRACKING_CMD] = "dummyValue205" # static value
        dummyDict[TrafficConfigConstants.FCS_CMD] = "dummyValue206" # static value
        dummyDict[TrafficConfigConstants.FCS_TYPE_CMD] = TrafficConfigConstants.FCS_TYPE_BAD_CRC # constant value
        dummyDict[TrafficConfigConstants.FECN_CMD] = "dummyValue208" # static value
        dummyDict[TrafficConfigConstants.FIELD_ACTIVEFIELDCHOICE_CMD] = "dummyValue209" # static value
        dummyDict[TrafficConfigConstants.FIELD_AUTO_CMD] = "dummyValue210" # static value
        dummyDict[TrafficConfigConstants.FIELD_COUNTVALUE_CMD] = "dummyValue211" # static value
        dummyDict[TrafficConfigConstants.FIELD_FIELDVALUE_CMD] = "dummyValue212" # static value
        dummyDict[TrafficConfigConstants.FIELD_FULLMESH_CMD] = "dummyValue213" # static value
        dummyDict[TrafficConfigConstants.FIELD_HANDLE_CMD] = "dummyValue214" # static value
        dummyDict[TrafficConfigConstants.FIELD_LINKED_CMD] = "dummyValue215" # static value
        dummyDict[TrafficConfigConstants.FIELD_LINKED_TO_CMD] = "dummyValue216" # static value
        dummyDict[TrafficConfigConstants.FIELD_OPTIONALENABLED_CMD] = "dummyValue217" # static value
        dummyDict[TrafficConfigConstants.FIELD_SINGLEVALUE_CMD] = "dummyValue218" # static value
        dummyDict[TrafficConfigConstants.FIELD_STARTVALUE_CMD] = "dummyValue219" # static value
        dummyDict[TrafficConfigConstants.FIELD_STEPVALUE_CMD] = "dummyValue220" # static value
        dummyDict[TrafficConfigConstants.FIELD_TRACKINGENABLED_CMD] = "dummyValue221" # static value
        dummyDict[TrafficConfigConstants.FIELD_VALUELIST_CMD] = "dummyValue222" # static value
        dummyDict[TrafficConfigConstants.FIELD_VALUETYPE_CMD] = "dummyValue223" # static value
        dummyDict[TrafficConfigConstants.FR_RANGE_COUNT_CMD] = "dummyValue224" # static value
        dummyDict[TrafficConfigConstants.FRAME_RATE_DISTRIBUTION_PORT_CMD] = TrafficConfigConstants.FRAME_RATE_DISTRIBUTION_PORT_APPLY_TO_ALL # constant value
        dummyDict[TrafficConfigConstants.FRAME_RATE_DISTRIBUTION_STREAM_CMD] = TrafficConfigConstants.FRAME_RATE_DISTRIBUTION_STREAM_APPLY_TO_ALL # constant value
        dummyDict[TrafficConfigConstants.FRAME_SEQUENCING_CMD] = TrafficConfigConstants.FRAME_SEQUENCING_ENABLE # constant value
        dummyDict[TrafficConfigConstants.FRAME_SEQUENCING_MODE_CMD] = TrafficConfigConstants.FRAME_SEQUENCING_MODE_RX_SWITCHED_PATH_FIXED # constant value
        dummyDict[TrafficConfigConstants.FRAME_SEQUENCING_OFFSET_CMD] = "dummyValue229" # static value
        dummyDict[TrafficConfigConstants.FRAME_SIZE_CMD] = "dummyValue230" # static value
        dummyDict[TrafficConfigConstants.FRAME_SIZE_DISTRIBUTION_CMD] = TrafficConfigConstants.FRAME_SIZE_DISTRIBUTION_CISCO # constant value
        dummyDict[TrafficConfigConstants.FRAME_SIZE_GAUSS_CMD] = "dummyValue232" # static value
        dummyDict[TrafficConfigConstants.FRAME_SIZE_IMIX_CMD] = "dummyValue233" # static value
        dummyDict[TrafficConfigConstants.FRAME_SIZE_MAX_CMD] = "dummyValue234" # static value
        dummyDict[TrafficConfigConstants.FRAME_SIZE_MIN_CMD] = "dummyValue235" # static value
        dummyDict[TrafficConfigConstants.FRAME_SIZE_STEP_CMD] = "dummyValue236" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_DEST_MAC_RETRY_COUNT_CMD] = "dummyValue237" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_DEST_MAC_RETRY_DELAY_CMD] = "dummyValue238" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_DISPLAY_MPLS_CURRENT_LABEL_VALUE_CMD] = "dummyValue239" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_ENABLE_DEST_MAC_RETRY_CMD] = "dummyValue240" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_ENABLE_MAC_CHANGE_ON_FLY_CMD] = "dummyValue241" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_ENABLE_MIN_FRAME_SIZE_CMD] = "dummyValue242" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_ENABLE_STAGGERED_TRANSMIT_CMD] = "dummyValue243" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_ENABLE_STREAM_ORDERING_CMD] = "dummyValue244" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_FRAME_ORDERING_CMD] = TrafficConfigConstants.GLOBAL_FRAME_ORDERING_NONE # constant value
        dummyDict[TrafficConfigConstants.GLOBAL_LARGE_ERROR_THRESHHOLD_CMD] = "dummyValue246" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_MAX_TRAFFIC_GENERATION_QUERIES_CMD] = "dummyValue247" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_MPLS_LABEL_LEARNING_TIMEOUT_CMD] = "dummyValue248" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_PEAK_LOADING_REPLICATION_COUNT_CMD] = "dummyValue249" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_REFRESH_LEARNED_INFO_BEFORE_APPLY_CMD] = "dummyValue250" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_STREAM_CONTROL_CMD] = TrafficConfigConstants.GLOBAL_STREAM_CONTROL_CONTINUOUS # constant value
        dummyDict[TrafficConfigConstants.GLOBAL_STREAM_CONTROL_ITERATIONS_CMD] = "dummyValue252" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_USE_TX_RX_SYNC_CMD] = "dummyValue253" # static value
        dummyDict[TrafficConfigConstants.GLOBAL_WAIT_TIME_CMD] = "dummyValue254" # static value
        dummyDict[TrafficConfigConstants.GRE_CHECKSUM_CMD] = "dummyValue255" # static value
        dummyDict[TrafficConfigConstants.GRE_CHECKSUM_COUNT_CMD] = "dummyValue256" # static value
        dummyDict[TrafficConfigConstants.GRE_CHECKSUM_ENABLE_CMD] = "dummyValue257" # static value
        dummyDict[TrafficConfigConstants.GRE_CHECKSUM_ENABLE_MODE_CMD] = TrafficConfigConstants.GRE_CHECKSUM_ENABLE_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.GRE_CHECKSUM_ENABLE_TRACKING_CMD] = "dummyValue259" # static value
        dummyDict[TrafficConfigConstants.GRE_CHECKSUM_MODE_CMD] = TrafficConfigConstants.GRE_CHECKSUM_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.GRE_CHECKSUM_STEP_CMD] = "dummyValue261" # static value
        dummyDict[TrafficConfigConstants.GRE_CHECKSUM_TRACKING_CMD] = "dummyValue262" # static value
        dummyDict[TrafficConfigConstants.GRE_KEY_CMD] = "dummyValue263" # static value
        dummyDict[TrafficConfigConstants.GRE_KEY_COUNT_CMD] = "dummyValue264" # static value
        dummyDict[TrafficConfigConstants.GRE_KEY_ENABLE_CMD] = "dummyValue265" # static value
        dummyDict[TrafficConfigConstants.GRE_KEY_ENABLE_MODE_CMD] = TrafficConfigConstants.GRE_KEY_ENABLE_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.GRE_KEY_ENABLE_TRACKING_CMD] = "dummyValue267" # static value
        dummyDict[TrafficConfigConstants.GRE_KEY_MODE_CMD] = TrafficConfigConstants.GRE_KEY_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.GRE_KEY_STEP_CMD] = "dummyValue269" # static value
        dummyDict[TrafficConfigConstants.GRE_KEY_TRACKING_CMD] = "dummyValue270" # static value
        dummyDict[TrafficConfigConstants.GRE_RESERVED0_CMD] = "dummyValue271" # static value
        dummyDict[TrafficConfigConstants.GRE_RESERVED0_COUNT_CMD] = "dummyValue272" # static value
        dummyDict[TrafficConfigConstants.GRE_RESERVED0_MODE_CMD] = TrafficConfigConstants.GRE_RESERVED0_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.GRE_RESERVED0_STEP_CMD] = "dummyValue274" # static value
        dummyDict[TrafficConfigConstants.GRE_RESERVED0_TRACKING_CMD] = "dummyValue275" # static value
        dummyDict[TrafficConfigConstants.GRE_RESERVED1_CMD] = "dummyValue276" # static value
        dummyDict[TrafficConfigConstants.GRE_RESERVED1_COUNT_CMD] = "dummyValue277" # static value
        dummyDict[TrafficConfigConstants.GRE_RESERVED1_MODE_CMD] = TrafficConfigConstants.GRE_RESERVED1_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.GRE_RESERVED1_STEP_CMD] = "dummyValue279" # static value
        dummyDict[TrafficConfigConstants.GRE_RESERVED1_TRACKING_CMD] = "dummyValue280" # static value
        dummyDict[TrafficConfigConstants.GRE_SEQ_ENABLE_CMD] = "dummyValue281" # static value
        dummyDict[TrafficConfigConstants.GRE_SEQ_ENABLE_MODE_CMD] = TrafficConfigConstants.GRE_SEQ_ENABLE_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.GRE_SEQ_ENABLE_TRACKING_CMD] = "dummyValue283" # static value
        dummyDict[TrafficConfigConstants.GRE_SEQ_NUMBER_CMD] = "dummyValue284" # static value
        dummyDict[TrafficConfigConstants.GRE_SEQ_NUMBER_COUNT_CMD] = "dummyValue285" # static value
        dummyDict[TrafficConfigConstants.GRE_SEQ_NUMBER_MODE_CMD] = TrafficConfigConstants.GRE_SEQ_NUMBER_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.GRE_SEQ_NUMBER_STEP_CMD] = "dummyValue287" # static value
        dummyDict[TrafficConfigConstants.GRE_SEQ_NUMBER_TRACKING_CMD] = "dummyValue288" # static value
        dummyDict[TrafficConfigConstants.GRE_VALID_CHECKSUM_ENABLE_CMD] = "dummyValue289" # static value
        dummyDict[TrafficConfigConstants.GRE_VERSION_CMD] = "dummyValue290" # static value
        dummyDict[TrafficConfigConstants.GRE_VERSION_COUNT_CMD] = "dummyValue291" # static value
        dummyDict[TrafficConfigConstants.GRE_VERSION_MODE_CMD] = TrafficConfigConstants.GRE_VERSION_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.GRE_VERSION_STEP_CMD] = "dummyValue293" # static value
        dummyDict[TrafficConfigConstants.GRE_VERSION_TRACKING_CMD] = "dummyValue294" # static value
        dummyDict[TrafficConfigConstants.HEADER_HANDLE_CMD] = "dummyValue295" # static value
        dummyDict[TrafficConfigConstants.HOSTS_PER_NET_CMD] = "dummyValue296" # static value
        dummyDict[TrafficConfigConstants.ICMP_CHECKSUM_CMD] = "dummyValue297" # static value
        dummyDict[TrafficConfigConstants.ICMP_CHECKSUM_COUNT_CMD] = "dummyValue298" # static value
        dummyDict[TrafficConfigConstants.ICMP_CHECKSUM_MODE_CMD] = TrafficConfigConstants.ICMP_CHECKSUM_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_CHECKSUM_STEP_CMD] = "dummyValue300" # static value
        dummyDict[TrafficConfigConstants.ICMP_CHECKSUM_TRACKING_CMD] = "dummyValue301" # static value
        dummyDict[TrafficConfigConstants.ICMP_CODE_CMD] = "dummyValue302" # static value
        dummyDict[TrafficConfigConstants.ICMP_CODE_COUNT_CMD] = "dummyValue303" # static value
        dummyDict[TrafficConfigConstants.ICMP_CODE_MODE_CMD] = TrafficConfigConstants.ICMP_CODE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_CODE_STEP_CMD] = "dummyValue305" # static value
        dummyDict[TrafficConfigConstants.ICMP_CODE_TRACKING_CMD] = "dummyValue306" # static value
        dummyDict[TrafficConfigConstants.ICMP_ID_CMD] = "dummyValue307" # static value
        dummyDict[TrafficConfigConstants.ICMP_ID_COUNT_CMD] = "dummyValue308" # static value
        dummyDict[TrafficConfigConstants.ICMP_ID_MODE_CMD] = TrafficConfigConstants.ICMP_ID_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_ID_STEP_CMD] = "dummyValue310" # static value
        dummyDict[TrafficConfigConstants.ICMP_ID_TRACKING_CMD] = "dummyValue311" # static value
        dummyDict[TrafficConfigConstants.ICMP_MAX_RESPONSE_DELAY_MS_CMD] = "dummyValue312" # static value
        dummyDict[TrafficConfigConstants.ICMP_MAX_RESPONSE_DELAY_MS_COUNT_CMD] = "dummyValue313" # static value
        dummyDict[TrafficConfigConstants.ICMP_MAX_RESPONSE_DELAY_MS_MODE_CMD] = TrafficConfigConstants.ICMP_MAX_RESPONSE_DELAY_MS_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_MAX_RESPONSE_DELAY_MS_STEP_CMD] = "dummyValue315" # static value
        dummyDict[TrafficConfigConstants.ICMP_MAX_RESPONSE_DELAY_MS_TRACKING_CMD] = "dummyValue316" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_INTERVAL_CODE_CMD] = "dummyValue317" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_INTERVAL_CODE_COUNT_CMD] = "dummyValue318" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_INTERVAL_CODE_MODE_CMD] = TrafficConfigConstants.ICMP_MC_QUERY_V2_INTERVAL_CODE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_INTERVAL_CODE_STEP_CMD] = "dummyValue320" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_INTERVAL_CODE_TRACKING_CMD] = "dummyValue321" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_CMD] = "dummyValue322" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_COUNT_CMD] = "dummyValue323" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_MODE_CMD] = TrafficConfigConstants.ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_STEP_CMD] = "dummyValue325" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_TRACKING_CMD] = "dummyValue326" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_S_FLAG_CMD] = "dummyValue327" # static value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_S_FLAG_MODE_CMD] = TrafficConfigConstants.ICMP_MC_QUERY_V2_S_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ICMP_MC_QUERY_V2_S_FLAG_TRACKING_CMD] = "dummyValue329" # static value
        dummyDict[TrafficConfigConstants.ICMP_MOBILE_PAM_M_BIT_CMD] = "dummyValue330" # static value
        dummyDict[TrafficConfigConstants.ICMP_MOBILE_PAM_M_BIT_MODE_CMD] = TrafficConfigConstants.ICMP_MOBILE_PAM_M_BIT_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ICMP_MOBILE_PAM_M_BIT_TRACKING_CMD] = "dummyValue332" # static value
        dummyDict[TrafficConfigConstants.ICMP_MOBILE_PAM_O_BIT_CMD] = "dummyValue333" # static value
        dummyDict[TrafficConfigConstants.ICMP_MOBILE_PAM_O_BIT_MODE_CMD] = TrafficConfigConstants.ICMP_MOBILE_PAM_O_BIT_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ICMP_MOBILE_PAM_O_BIT_TRACKING_CMD] = "dummyValue335" # static value
        dummyDict[TrafficConfigConstants.ICMP_MULTICAST_ADDRESS_CMD] = "dummyValue336" # static value
        dummyDict[TrafficConfigConstants.ICMP_MULTICAST_ADDRESS_COUNT_CMD] = "dummyValue337" # static value
        dummyDict[TrafficConfigConstants.ICMP_MULTICAST_ADDRESS_MODE_CMD] = TrafficConfigConstants.ICMP_MULTICAST_ADDRESS_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_MULTICAST_ADDRESS_STEP_CMD] = "dummyValue339" # static value
        dummyDict[TrafficConfigConstants.ICMP_MULTICAST_ADDRESS_TRACKING_CMD] = "dummyValue340" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_NAM_O_FLAG_CMD] = "dummyValue341" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_NAM_O_FLAG_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_NAM_O_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_NAM_O_FLAG_TRACKING_CMD] = "dummyValue343" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_NAM_R_FLAG_CMD] = "dummyValue344" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_NAM_R_FLAG_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_NAM_R_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_NAM_R_FLAG_TRACKING_CMD] = "dummyValue346" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_NAM_S_FLAG_CMD] = "dummyValue347" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_NAM_S_FLAG_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_NAM_S_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_NAM_S_FLAG_TRACKING_CMD] = "dummyValue349" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_H_FLAG_CMD] = "dummyValue350" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_H_FLAG_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_RAM_H_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_H_FLAG_TRACKING_CMD] = "dummyValue352" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_HOP_LIMIT_CMD] = "dummyValue353" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_HOP_LIMIT_COUNT_CMD] = "dummyValue354" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_HOP_LIMIT_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_RAM_HOP_LIMIT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_HOP_LIMIT_STEP_CMD] = "dummyValue356" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_HOP_LIMIT_TRACKING_CMD] = "dummyValue357" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_M_FLAG_CMD] = "dummyValue358" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_M_FLAG_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_RAM_M_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_M_FLAG_TRACKING_CMD] = "dummyValue360" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_O_FLAG_CMD] = "dummyValue361" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_O_FLAG_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_RAM_O_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_O_FLAG_TRACKING_CMD] = "dummyValue363" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_REACHABLE_TIME_CMD] = "dummyValue364" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_REACHABLE_TIME_COUNT_CMD] = "dummyValue365" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_REACHABLE_TIME_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_RAM_REACHABLE_TIME_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_REACHABLE_TIME_STEP_CMD] = "dummyValue367" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_REACHABLE_TIME_TRACKING_CMD] = "dummyValue368" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_RETRANSMIT_TIMER_CMD] = "dummyValue369" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_RETRANSMIT_TIMER_COUNT_CMD] = "dummyValue370" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_RETRANSMIT_TIMER_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_RAM_RETRANSMIT_TIMER_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_RETRANSMIT_TIMER_STEP_CMD] = "dummyValue372" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_RETRANSMIT_TIMER_TRACKING_CMD] = "dummyValue373" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_ROUTER_LIFETIME_CMD] = "dummyValue374" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_ROUTER_LIFETIME_COUNT_CMD] = "dummyValue375" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_ROUTER_LIFETIME_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_RAM_ROUTER_LIFETIME_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_ROUTER_LIFETIME_STEP_CMD] = "dummyValue377" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RAM_ROUTER_LIFETIME_TRACKING_CMD] = "dummyValue378" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RM_DEST_ADDR_CMD] = "dummyValue379" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RM_DEST_ADDR_COUNT_CMD] = "dummyValue380" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RM_DEST_ADDR_MODE_CMD] = TrafficConfigConstants.ICMP_NDP_RM_DEST_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RM_DEST_ADDR_STEP_CMD] = "dummyValue382" # static value
        dummyDict[TrafficConfigConstants.ICMP_NDP_RM_DEST_ADDR_TRACKING_CMD] = "dummyValue383" # static value
        dummyDict[TrafficConfigConstants.ICMP_PARAM_PROBLEM_MESSAGE_POINTER_CMD] = "dummyValue384" # static value
        dummyDict[TrafficConfigConstants.ICMP_PARAM_PROBLEM_MESSAGE_POINTER_COUNT_CMD] = "dummyValue385" # static value
        dummyDict[TrafficConfigConstants.ICMP_PARAM_PROBLEM_MESSAGE_POINTER_MODE_CMD] = TrafficConfigConstants.ICMP_PARAM_PROBLEM_MESSAGE_POINTER_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_PARAM_PROBLEM_MESSAGE_POINTER_STEP_CMD] = "dummyValue387" # static value
        dummyDict[TrafficConfigConstants.ICMP_PARAM_PROBLEM_MESSAGE_POINTER_TRACKING_CMD] = "dummyValue388" # static value
        dummyDict[TrafficConfigConstants.ICMP_PKT_TOO_BIG_MTU_CMD] = "dummyValue389" # static value
        dummyDict[TrafficConfigConstants.ICMP_PKT_TOO_BIG_MTU_COUNT_CMD] = "dummyValue390" # static value
        dummyDict[TrafficConfigConstants.ICMP_PKT_TOO_BIG_MTU_MODE_CMD] = TrafficConfigConstants.ICMP_PKT_TOO_BIG_MTU_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_PKT_TOO_BIG_MTU_STEP_CMD] = "dummyValue392" # static value
        dummyDict[TrafficConfigConstants.ICMP_PKT_TOO_BIG_MTU_TRACKING_CMD] = "dummyValue393" # static value
        dummyDict[TrafficConfigConstants.ICMP_SEQ_CMD] = "dummyValue394" # static value
        dummyDict[TrafficConfigConstants.ICMP_SEQ_COUNT_CMD] = "dummyValue395" # static value
        dummyDict[TrafficConfigConstants.ICMP_SEQ_MODE_CMD] = TrafficConfigConstants.ICMP_SEQ_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_SEQ_STEP_CMD] = "dummyValue397" # static value
        dummyDict[TrafficConfigConstants.ICMP_SEQ_TRACKING_CMD] = "dummyValue398" # static value
        dummyDict[TrafficConfigConstants.ICMP_TARGET_ADDR_CMD] = "dummyValue399" # static value
        dummyDict[TrafficConfigConstants.ICMP_TARGET_ADDR_COUNT_CMD] = "dummyValue400" # static value
        dummyDict[TrafficConfigConstants.ICMP_TARGET_ADDR_MODE_CMD] = TrafficConfigConstants.ICMP_TARGET_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_TARGET_ADDR_STEP_CMD] = "dummyValue402" # static value
        dummyDict[TrafficConfigConstants.ICMP_TARGET_ADDR_TRACKING_CMD] = "dummyValue403" # static value
        dummyDict[TrafficConfigConstants.ICMP_TYPE_CMD] = "dummyValue404" # static value
        dummyDict[TrafficConfigConstants.ICMP_TYPE_COUNT_CMD] = "dummyValue405" # static value
        dummyDict[TrafficConfigConstants.ICMP_TYPE_MODE_CMD] = TrafficConfigConstants.ICMP_TYPE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_TYPE_STEP_CMD] = "dummyValue407" # static value
        dummyDict[TrafficConfigConstants.ICMP_TYPE_TRACKING_CMD] = "dummyValue408" # static value
        dummyDict[TrafficConfigConstants.ICMP_UNUSED_CMD] = "dummyValue409" # static value
        dummyDict[TrafficConfigConstants.ICMP_UNUSED_COUNT_CMD] = "dummyValue410" # static value
        dummyDict[TrafficConfigConstants.ICMP_UNUSED_MODE_CMD] = TrafficConfigConstants.ICMP_UNUSED_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ICMP_UNUSED_STEP_CMD] = "dummyValue412" # static value
        dummyDict[TrafficConfigConstants.ICMP_UNUSED_TRACKING_CMD] = "dummyValue413" # static value
        dummyDict[TrafficConfigConstants.IGMP_AUX_DATA_LENGTH_CMD] = "dummyValue414" # static value
        dummyDict[TrafficConfigConstants.IGMP_AUX_DATA_LENGTH_COUNT_CMD] = "dummyValue415" # static value
        dummyDict[TrafficConfigConstants.IGMP_AUX_DATA_LENGTH_MODE_CMD] = TrafficConfigConstants.IGMP_AUX_DATA_LENGTH_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_AUX_DATA_LENGTH_STEP_CMD] = "dummyValue417" # static value
        dummyDict[TrafficConfigConstants.IGMP_AUX_DATA_LENGTH_TRACKING_CMD] = "dummyValue418" # static value
        dummyDict[TrafficConfigConstants.IGMP_CHECKSUM_CMD] = "dummyValue419" # static value
        dummyDict[TrafficConfigConstants.IGMP_CHECKSUM_COUNT_CMD] = "dummyValue420" # static value
        dummyDict[TrafficConfigConstants.IGMP_CHECKSUM_MODE_CMD] = TrafficConfigConstants.IGMP_CHECKSUM_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_CHECKSUM_STEP_CMD] = "dummyValue422" # static value
        dummyDict[TrafficConfigConstants.IGMP_CHECKSUM_TRACKING_CMD] = "dummyValue423" # static value
        dummyDict[TrafficConfigConstants.IGMP_DATA_V3R_CMD] = "dummyValue424" # static value
        dummyDict[TrafficConfigConstants.IGMP_DATA_V3R_COUNT_CMD] = "dummyValue425" # static value
        dummyDict[TrafficConfigConstants.IGMP_DATA_V3R_MODE_CMD] = TrafficConfigConstants.IGMP_DATA_V3R_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_DATA_V3R_STEP_CMD] = "dummyValue427" # static value
        dummyDict[TrafficConfigConstants.IGMP_DATA_V3R_TRACKING_CMD] = "dummyValue428" # static value
        dummyDict[TrafficConfigConstants.IGMP_GROUP_ADDR_CMD] = "dummyValue429" # static value
        dummyDict[TrafficConfigConstants.IGMP_GROUP_COUNT_CMD] = "dummyValue430" # static value
        dummyDict[TrafficConfigConstants.IGMP_GROUP_MODE_CMD] = TrafficConfigConstants.IGMP_GROUP_MODE_DECREMENT # constant value
        dummyDict[TrafficConfigConstants.IGMP_GROUP_STEP_CMD] = "dummyValue432" # static value
        dummyDict[TrafficConfigConstants.IGMP_GROUP_TRACKING_CMD] = "dummyValue433" # static value
        dummyDict[TrafficConfigConstants.IGMP_LENGTH_V3R_CMD] = "dummyValue434" # static value
        dummyDict[TrafficConfigConstants.IGMP_LENGTH_V3R_COUNT_CMD] = "dummyValue435" # static value
        dummyDict[TrafficConfigConstants.IGMP_LENGTH_V3R_MODE_CMD] = TrafficConfigConstants.IGMP_LENGTH_V3R_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_LENGTH_V3R_STEP_CMD] = "dummyValue437" # static value
        dummyDict[TrafficConfigConstants.IGMP_LENGTH_V3R_TRACKING_CMD] = "dummyValue438" # static value
        dummyDict[TrafficConfigConstants.IGMP_MAX_RESPONSE_TIME_CMD] = "dummyValue439" # static value
        dummyDict[TrafficConfigConstants.IGMP_MAX_RESPONSE_TIME_COUNT_CMD] = "dummyValue440" # static value
        dummyDict[TrafficConfigConstants.IGMP_MAX_RESPONSE_TIME_MODE_CMD] = TrafficConfigConstants.IGMP_MAX_RESPONSE_TIME_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_MAX_RESPONSE_TIME_STEP_CMD] = "dummyValue442" # static value
        dummyDict[TrafficConfigConstants.IGMP_MAX_RESPONSE_TIME_TRACKING_CMD] = "dummyValue443" # static value
        dummyDict[TrafficConfigConstants.IGMP_MSG_TYPE_CMD] = "dummyValue444" # static value
        dummyDict[TrafficConfigConstants.IGMP_MSG_TYPE_TRACKING_CMD] = "dummyValue445" # static value
        dummyDict[TrafficConfigConstants.IGMP_MULTICAST_SRC_CMD] = "dummyValue446" # static value
        dummyDict[TrafficConfigConstants.IGMP_MULTICAST_SRC_COUNT_CMD] = "dummyValue447" # static value
        dummyDict[TrafficConfigConstants.IGMP_MULTICAST_SRC_MODE_CMD] = "dummyValue448" # static value
        dummyDict[TrafficConfigConstants.IGMP_MULTICAST_SRC_STEP_CMD] = "dummyValue449" # static value
        dummyDict[TrafficConfigConstants.IGMP_MULTICAST_SRC_TRACKING_CMD] = "dummyValue450" # static value
        dummyDict[TrafficConfigConstants.IGMP_QQIC_CMD] = "dummyValue451" # static value
        dummyDict[TrafficConfigConstants.IGMP_QQIC_COUNT_CMD] = "dummyValue452" # static value
        dummyDict[TrafficConfigConstants.IGMP_QQIC_MODE_CMD] = TrafficConfigConstants.IGMP_QQIC_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_QQIC_STEP_CMD] = "dummyValue454" # static value
        dummyDict[TrafficConfigConstants.IGMP_QQIC_TRACKING_CMD] = "dummyValue455" # static value
        dummyDict[TrafficConfigConstants.IGMP_QRV_CMD] = "dummyValue456" # static value
        dummyDict[TrafficConfigConstants.IGMP_QRV_COUNT_CMD] = "dummyValue457" # static value
        dummyDict[TrafficConfigConstants.IGMP_QRV_MODE_CMD] = TrafficConfigConstants.IGMP_QRV_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_QRV_STEP_CMD] = "dummyValue459" # static value
        dummyDict[TrafficConfigConstants.IGMP_QRV_TRACKING_CMD] = "dummyValue460" # static value
        dummyDict[TrafficConfigConstants.IGMP_RECORD_TYPE_CMD] = TrafficConfigConstants.IGMP_RECORD_TYPE_MODE_IS_EXCLUDE # constant value
        dummyDict[TrafficConfigConstants.IGMP_RECORD_TYPE_MODE_CMD] = TrafficConfigConstants.IGMP_RECORD_TYPE_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IGMP_RECORD_TYPE_TRACKING_CMD] = "dummyValue463" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3Q_CMD] = "dummyValue464" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3Q_COUNT_CMD] = "dummyValue465" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3Q_MODE_CMD] = TrafficConfigConstants.IGMP_RESERVED_V3Q_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3Q_STEP_CMD] = "dummyValue467" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3Q_TRACKING_CMD] = "dummyValue468" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R1_CMD] = "dummyValue469" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R1_COUNT_CMD] = "dummyValue470" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R1_MODE_CMD] = TrafficConfigConstants.IGMP_RESERVED_V3R1_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R1_STEP_CMD] = "dummyValue472" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R1_TRACKING_CMD] = "dummyValue473" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R2_CMD] = "dummyValue474" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R2_COUNT_CMD] = "dummyValue475" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R2_MODE_CMD] = TrafficConfigConstants.IGMP_RESERVED_V3R2_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R2_STEP_CMD] = "dummyValue477" # static value
        dummyDict[TrafficConfigConstants.IGMP_RESERVED_V3R2_TRACKING_CMD] = "dummyValue478" # static value
        dummyDict[TrafficConfigConstants.IGMP_S_FLAG_CMD] = "dummyValue479" # static value
        dummyDict[TrafficConfigConstants.IGMP_S_FLAG_MODE_CMD] = TrafficConfigConstants.IGMP_S_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IGMP_S_FLAG_TRACKING_CMD] = "dummyValue481" # static value
        dummyDict[TrafficConfigConstants.IGMP_TYPE_CMD] = TrafficConfigConstants.IGMP_TYPE_MEMBERSHIP_REPORT # constant value
        dummyDict[TrafficConfigConstants.IGMP_UNUSED_CMD] = "dummyValue483" # static value
        dummyDict[TrafficConfigConstants.IGMP_UNUSED_COUNT_CMD] = "dummyValue484" # static value
        dummyDict[TrafficConfigConstants.IGMP_UNUSED_MODE_CMD] = TrafficConfigConstants.IGMP_UNUSED_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IGMP_UNUSED_STEP_CMD] = "dummyValue486" # static value
        dummyDict[TrafficConfigConstants.IGMP_UNUSED_TRACKING_CMD] = "dummyValue487" # static value
        dummyDict[TrafficConfigConstants.IGMP_VALID_CHECKSUM_CMD] = "dummyValue488" # static value
        dummyDict[TrafficConfigConstants.IGMP_VERSION_CMD] = TrafficConfigConstants.IGMP_VERSION_1 # constant value
        dummyDict[TrafficConfigConstants.INDIRECT_CMD] = "dummyValue490" # static value
        dummyDict[TrafficConfigConstants.INNER_IP_DST_ADDR_CMD] = "dummyValue491" # static value
        dummyDict[TrafficConfigConstants.INNER_IP_DST_COUNT_CMD] = "dummyValue492" # static value
        dummyDict[TrafficConfigConstants.INNER_IP_DST_MODE_CMD] = TrafficConfigConstants.INNER_IP_DST_MODE_RANDOM # constant value
        dummyDict[TrafficConfigConstants.INNER_IP_DST_STEP_CMD] = "dummyValue494" # static value
        dummyDict[TrafficConfigConstants.INNER_IP_DST_TRACKING_CMD] = "dummyValue495" # static value
        dummyDict[TrafficConfigConstants.INNER_IP_SRC_ADDR_CMD] = "dummyValue496" # static value
        dummyDict[TrafficConfigConstants.INNER_IP_SRC_COUNT_CMD] = "dummyValue497" # static value
        dummyDict[TrafficConfigConstants.INNER_IP_SRC_MODE_CMD] = TrafficConfigConstants.INNER_IP_SRC_MODE_RANDOM # constant value
        dummyDict[TrafficConfigConstants.INNER_IP_SRC_STEP_CMD] = "dummyValue499" # static value
        dummyDict[TrafficConfigConstants.INNER_IP_SRC_TRACKING_CMD] = "dummyValue500" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_DST_ADDR_CMD] = "dummyValue501" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_DST_COUNT_CMD] = "dummyValue502" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_DST_MASK_CMD] = "dummyValue503" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_DST_MODE_CMD] = TrafficConfigConstants.INNER_IPV6_DST_MODE_INCR_HOST # constant value
        dummyDict[TrafficConfigConstants.INNER_IPV6_DST_STEP_CMD] = "dummyValue505" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_DST_TRACKING_CMD] = "dummyValue506" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FLOW_LABEL_CMD] = "dummyValue507" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FLOW_LABEL_COUNT_CMD] = "dummyValue508" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FLOW_LABEL_MODE_CMD] = TrafficConfigConstants.INNER_IPV6_FLOW_LABEL_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FLOW_LABEL_STEP_CMD] = "dummyValue510" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FLOW_LABEL_TRACKING_CMD] = "dummyValue511" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_ID_CMD] = "dummyValue512" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_ID_COUNT_CMD] = "dummyValue513" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_ID_MODE_CMD] = TrafficConfigConstants.INNER_IPV6_FRAG_ID_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_ID_STEP_CMD] = "dummyValue515" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_ID_TRACKING_CMD] = "dummyValue516" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_MORE_FLAG_CMD] = "dummyValue517" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_MORE_FLAG_MODE_CMD] = TrafficConfigConstants.INNER_IPV6_FRAG_MORE_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_MORE_FLAG_TRACKING_CMD] = "dummyValue519" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_OFFSET_CMD] = "dummyValue520" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_OFFSET_COUNT_CMD] = "dummyValue521" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_OFFSET_MODE_CMD] = TrafficConfigConstants.INNER_IPV6_FRAG_OFFSET_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_OFFSET_STEP_CMD] = "dummyValue523" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_FRAG_OFFSET_TRACKING_CMD] = "dummyValue524" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_HOP_LIMIT_CMD] = "dummyValue525" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_HOP_LIMIT_COUNT_CMD] = "dummyValue526" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_HOP_LIMIT_MODE_CMD] = TrafficConfigConstants.INNER_IPV6_HOP_LIMIT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.INNER_IPV6_HOP_LIMIT_STEP_CMD] = "dummyValue528" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_HOP_LIMIT_TRACKING_CMD] = "dummyValue529" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_SRC_ADDR_CMD] = "dummyValue530" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_SRC_COUNT_CMD] = "dummyValue531" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_SRC_MASK_CMD] = "dummyValue532" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_SRC_MODE_CMD] = TrafficConfigConstants.INNER_IPV6_SRC_MODE_INCR_HOST # constant value
        dummyDict[TrafficConfigConstants.INNER_IPV6_SRC_STEP_CMD] = "dummyValue534" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_SRC_TRACKING_CMD] = "dummyValue535" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_TRAFFIC_CLASS_CMD] = "dummyValue536" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_TRAFFIC_CLASS_COUNT_CMD] = "dummyValue537" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_TRAFFIC_CLASS_MODE_CMD] = TrafficConfigConstants.INNER_IPV6_TRAFFIC_CLASS_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.INNER_IPV6_TRAFFIC_CLASS_STEP_CMD] = "dummyValue539" # static value
        dummyDict[TrafficConfigConstants.INNER_IPV6_TRAFFIC_CLASS_TRACKING_CMD] = "dummyValue540" # static value
        dummyDict[TrafficConfigConstants.INNER_PROTOCOL_CMD] = TrafficConfigConstants.INNER_PROTOCOL_HEX # constant value
        dummyDict[TrafficConfigConstants.INNER_PROTOCOL_COUNT_CMD] = "dummyValue542" # static value
        dummyDict[TrafficConfigConstants.INNER_PROTOCOL_MODE_CMD] = TrafficConfigConstants.INNER_PROTOCOL_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.INNER_PROTOCOL_STEP_CMD] = "dummyValue544" # static value
        dummyDict[TrafficConfigConstants.INNER_PROTOCOL_TRACKING_CMD] = "dummyValue545" # static value
        dummyDict[TrafficConfigConstants.INTEGRITY_SIGNATURE_CMD] = "dummyValue546" # static value
        dummyDict[TrafficConfigConstants.INTEGRITY_SIGNATURE_OFFSET_CMD] = "dummyValue547" # static value
        dummyDict[TrafficConfigConstants.INTER_BURST_GAP_CMD] = "dummyValue548" # static value
        dummyDict[TrafficConfigConstants.INTER_FRAME_GAP_CMD] = "dummyValue549" # static value
        dummyDict[TrafficConfigConstants.INTER_FRAME_GAP_UNIT_CMD] = TrafficConfigConstants.INTER_FRAME_GAP_UNIT_NS # constant value
        dummyDict[TrafficConfigConstants.INTER_STREAM_GAP_CMD] = "dummyValue551" # static value
        dummyDict[TrafficConfigConstants.INTF_HANDLE_CMD] = "dummyValue552" # static value
        dummyDict[TrafficConfigConstants.IP_BIT_FLAGS_CMD] = "dummyValue553" # static value
        dummyDict[TrafficConfigConstants.IP_CHECKSUM_CMD] = "dummyValue554" # static value
        dummyDict[TrafficConfigConstants.IP_CHECKSUM_COUNT_CMD] = "dummyValue555" # static value
        dummyDict[TrafficConfigConstants.IP_CHECKSUM_MODE_CMD] = TrafficConfigConstants.IP_CHECKSUM_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IP_CHECKSUM_STEP_CMD] = "dummyValue557" # static value
        dummyDict[TrafficConfigConstants.IP_CHECKSUM_TRACKING_CMD] = "dummyValue558" # static value
        dummyDict[TrafficConfigConstants.IP_COST_CMD] = "dummyValue559" # static value
        dummyDict[TrafficConfigConstants.IP_COST_MODE_CMD] = TrafficConfigConstants.IP_COST_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_COST_TRACKING_CMD] = "dummyValue561" # static value
        dummyDict[TrafficConfigConstants.IP_CU_CMD] = "dummyValue562" # static value
        dummyDict[TrafficConfigConstants.IP_CU_COUNT_CMD] = "dummyValue563" # static value
        dummyDict[TrafficConfigConstants.IP_CU_MODE_CMD] = TrafficConfigConstants.IP_CU_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IP_CU_STEP_CMD] = "dummyValue565" # static value
        dummyDict[TrafficConfigConstants.IP_CU_TRACKING_CMD] = "dummyValue566" # static value
        dummyDict[TrafficConfigConstants.IP_DELAY_CMD] = "dummyValue567" # static value
        dummyDict[TrafficConfigConstants.IP_DELAY_MODE_CMD] = TrafficConfigConstants.IP_DELAY_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_DELAY_TRACKING_CMD] = "dummyValue569" # static value
        dummyDict[TrafficConfigConstants.IP_DSCP_CMD] = "dummyValue570" # static value
        dummyDict[TrafficConfigConstants.IP_DSCP_COUNT_CMD] = "dummyValue571" # static value
        dummyDict[TrafficConfigConstants.IP_DSCP_MODE_CMD] = TrafficConfigConstants.IP_DSCP_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IP_DSCP_STEP_CMD] = "dummyValue573" # static value
        dummyDict[TrafficConfigConstants.IP_DSCP_TRACKING_CMD] = "dummyValue574" # static value
        dummyDict[TrafficConfigConstants.IP_DST_ADDR_CMD] = "dummyValue575" # static value
        dummyDict[TrafficConfigConstants.IP_DST_COUNT_CMD] = "dummyValue576" # static value
        dummyDict[TrafficConfigConstants.IP_DST_COUNT_STEP_CMD] = "dummyValue577" # static value
        dummyDict[TrafficConfigConstants.IP_DST_INCREMENT_CMD] = "dummyValue578" # static value
        dummyDict[TrafficConfigConstants.IP_DST_INCREMENT_STEP_CMD] = "dummyValue579" # static value
        dummyDict[TrafficConfigConstants.IP_DST_MODE_CMD] = TrafficConfigConstants.IP_DST_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_DST_PREFIX_LEN_CMD] = "dummyValue581" # static value
        dummyDict[TrafficConfigConstants.IP_DST_PREFIX_LEN_STEP_CMD] = "dummyValue582" # static value
        dummyDict[TrafficConfigConstants.IP_DST_RANGE_STEP_CMD] = "dummyValue583" # static value
        dummyDict[TrafficConfigConstants.IP_DST_SKIP_BROADCAST_CMD] = "dummyValue584" # static value
        dummyDict[TrafficConfigConstants.IP_DST_SKIP_MULTICAST_CMD] = "dummyValue585" # static value
        dummyDict[TrafficConfigConstants.IP_DST_STEP_CMD] = "dummyValue586" # static value
        dummyDict[TrafficConfigConstants.IP_DST_TRACKING_CMD] = "dummyValue587" # static value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_CMD] = "dummyValue588" # static value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_LAST_CMD] = "dummyValue589" # static value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_LAST_MODE_CMD] = TrafficConfigConstants.IP_FRAGMENT_LAST_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_LAST_TRACKING_CMD] = "dummyValue591" # static value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_MODE_CMD] = TrafficConfigConstants.IP_FRAGMENT_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_OFFSET_CMD] = "dummyValue593" # static value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_OFFSET_COUNT_CMD] = "dummyValue594" # static value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_OFFSET_MODE_CMD] = TrafficConfigConstants.IP_FRAGMENT_OFFSET_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_OFFSET_STEP_CMD] = "dummyValue596" # static value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_OFFSET_TRACKING_CMD] = "dummyValue597" # static value
        dummyDict[TrafficConfigConstants.IP_FRAGMENT_TRACKING_CMD] = "dummyValue598" # static value
        dummyDict[TrafficConfigConstants.IP_HDR_LENGTH_CMD] = "dummyValue599" # static value
        dummyDict[TrafficConfigConstants.IP_HDR_LENGTH_COUNT_CMD] = "dummyValue600" # static value
        dummyDict[TrafficConfigConstants.IP_HDR_LENGTH_MODE_CMD] = TrafficConfigConstants.IP_HDR_LENGTH_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IP_HDR_LENGTH_STEP_CMD] = "dummyValue602" # static value
        dummyDict[TrafficConfigConstants.IP_HDR_LENGTH_TRACKING_CMD] = "dummyValue603" # static value
        dummyDict[TrafficConfigConstants.IP_ID_CMD] = "dummyValue604" # static value
        dummyDict[TrafficConfigConstants.IP_ID_COUNT_CMD] = "dummyValue605" # static value
        dummyDict[TrafficConfigConstants.IP_ID_MODE_CMD] = TrafficConfigConstants.IP_ID_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IP_ID_STEP_CMD] = "dummyValue607" # static value
        dummyDict[TrafficConfigConstants.IP_ID_TRACKING_CMD] = "dummyValue608" # static value
        dummyDict[TrafficConfigConstants.IP_LENGTH_OVERRIDE_CMD] = "dummyValue609" # static value
        dummyDict[TrafficConfigConstants.IP_LENGTH_OVERRIDE_MODE_CMD] = TrafficConfigConstants.IP_LENGTH_OVERRIDE_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_LENGTH_OVERRIDE_TRACKING_CMD] = "dummyValue611" # static value
        dummyDict[TrafficConfigConstants.IP_MBZ_CMD] = "dummyValue612" # static value
        dummyDict[TrafficConfigConstants.IP_OPT_LOOSE_ROUTING_CMD] = "dummyValue613" # static value
        dummyDict[TrafficConfigConstants.IP_OPT_SECURITY_CMD] = "dummyValue614" # static value
        dummyDict[TrafficConfigConstants.IP_OPT_STRICT_ROUTING_CMD] = "dummyValue615" # static value
        dummyDict[TrafficConfigConstants.IP_OPT_TIMESTAMP_CMD] = "dummyValue616" # static value
        dummyDict[TrafficConfigConstants.IP_PRECEDENCE_CMD] = "dummyValue617" # static value
        dummyDict[TrafficConfigConstants.IP_PRECEDENCE_COUNT_CMD] = "dummyValue618" # static value
        dummyDict[TrafficConfigConstants.IP_PRECEDENCE_MODE_CMD] = TrafficConfigConstants.IP_PRECEDENCE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IP_PRECEDENCE_STEP_CMD] = "dummyValue620" # static value
        dummyDict[TrafficConfigConstants.IP_PRECEDENCE_TRACKING_CMD] = "dummyValue621" # static value
        dummyDict[TrafficConfigConstants.IP_PROTOCOL_CMD] = "dummyValue622" # static value
        dummyDict[TrafficConfigConstants.IP_PROTOCOL_COUNT_CMD] = "dummyValue623" # static value
        dummyDict[TrafficConfigConstants.IP_PROTOCOL_MODE_CMD] = TrafficConfigConstants.IP_PROTOCOL_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IP_PROTOCOL_STEP_CMD] = "dummyValue625" # static value
        dummyDict[TrafficConfigConstants.IP_PROTOCOL_TRACKING_CMD] = "dummyValue626" # static value
        dummyDict[TrafficConfigConstants.IP_RANGE_COUNT_CMD] = "dummyValue627" # static value
        dummyDict[TrafficConfigConstants.IP_RELIABILITY_CMD] = "dummyValue628" # static value
        dummyDict[TrafficConfigConstants.IP_RELIABILITY_MODE_CMD] = TrafficConfigConstants.IP_RELIABILITY_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_RELIABILITY_TRACKING_CMD] = "dummyValue630" # static value
        dummyDict[TrafficConfigConstants.IP_RESERVED_CMD] = "dummyValue631" # static value
        dummyDict[TrafficConfigConstants.IP_RESERVED_MODE_CMD] = TrafficConfigConstants.IP_RESERVED_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_RESERVED_TRACKING_CMD] = "dummyValue633" # static value
        dummyDict[TrafficConfigConstants.IP_SRC_ADDR_CMD] = "dummyValue634" # static value
        dummyDict[TrafficConfigConstants.IP_SRC_COUNT_CMD] = "dummyValue635" # static value
        dummyDict[TrafficConfigConstants.IP_SRC_MODE_CMD] = TrafficConfigConstants.IP_SRC_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_SRC_SKIP_BROADCAST_CMD] = "dummyValue637" # static value
        dummyDict[TrafficConfigConstants.IP_SRC_SKIP_MULTICAST_CMD] = "dummyValue638" # static value
        dummyDict[TrafficConfigConstants.IP_SRC_STEP_CMD] = "dummyValue639" # static value
        dummyDict[TrafficConfigConstants.IP_SRC_TRACKING_CMD] = "dummyValue640" # static value
        dummyDict[TrafficConfigConstants.IP_THROUGHPUT_CMD] = "dummyValue641" # static value
        dummyDict[TrafficConfigConstants.IP_THROUGHPUT_MODE_CMD] = TrafficConfigConstants.IP_THROUGHPUT_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IP_THROUGHPUT_TRACKING_CMD] = "dummyValue643" # static value
        dummyDict[TrafficConfigConstants.IP_TOS_COUNT_CMD] = "dummyValue644" # static value
        dummyDict[TrafficConfigConstants.IP_TOS_FIELD_CMD] = "dummyValue645" # static value
        dummyDict[TrafficConfigConstants.IP_TOS_STEP_CMD] = "dummyValue646" # static value
        dummyDict[TrafficConfigConstants.IP_TOTAL_LENGTH_CMD] = "dummyValue647" # static value
        dummyDict[TrafficConfigConstants.IP_TOTAL_LENGTH_COUNT_CMD] = "dummyValue648" # static value
        dummyDict[TrafficConfigConstants.IP_TOTAL_LENGTH_MODE_CMD] = TrafficConfigConstants.IP_TOTAL_LENGTH_MODE_AUTO # constant value
        dummyDict[TrafficConfigConstants.IP_TOTAL_LENGTH_STEP_CMD] = "dummyValue650" # static value
        dummyDict[TrafficConfigConstants.IP_TOTAL_LENGTH_TRACKING_CMD] = "dummyValue651" # static value
        dummyDict[TrafficConfigConstants.IP_TTL_CMD] = "dummyValue652" # static value
        dummyDict[TrafficConfigConstants.IP_TTL_COUNT_CMD] = "dummyValue653" # static value
        dummyDict[TrafficConfigConstants.IP_TTL_MODE_CMD] = TrafficConfigConstants.IP_TTL_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IP_TTL_STEP_CMD] = "dummyValue655" # static value
        dummyDict[TrafficConfigConstants.IP_TTL_TRACKING_CMD] = "dummyValue656" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_MD5SHA1_STRING_CMD] = "dummyValue657" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_MD5SHA1_STRING_COUNT_CMD] = "dummyValue658" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_MD5SHA1_STRING_MODE_CMD] = TrafficConfigConstants.IPV6_AUTH_MD5SHA1_STRING_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_MD5SHA1_STRING_STEP_CMD] = "dummyValue660" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_MD5SHA1_STRING_TRACKING_CMD] = "dummyValue661" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_NEXT_HEADER_CMD] = "dummyValue662" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_NEXT_HEADER_COUNT_CMD] = "dummyValue663" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_NEXT_HEADER_MODE_CMD] = TrafficConfigConstants.IPV6_AUTH_NEXT_HEADER_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_NEXT_HEADER_STEP_CMD] = "dummyValue665" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_NEXT_HEADER_TRACKING_CMD] = "dummyValue666" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PADDING_CMD] = "dummyValue667" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PADDING_COUNT_CMD] = "dummyValue668" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PADDING_MODE_CMD] = TrafficConfigConstants.IPV6_AUTH_PADDING_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PADDING_STEP_CMD] = "dummyValue670" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PADDING_TRACKING_CMD] = "dummyValue671" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PAYLOAD_LEN_CMD] = "dummyValue672" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PAYLOAD_LEN_COUNT_CMD] = "dummyValue673" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PAYLOAD_LEN_MODE_CMD] = TrafficConfigConstants.IPV6_AUTH_PAYLOAD_LEN_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PAYLOAD_LEN_STEP_CMD] = "dummyValue675" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_PAYLOAD_LEN_TRACKING_CMD] = "dummyValue676" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_RESERVED_CMD] = "dummyValue677" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_RESERVED_COUNT_CMD] = "dummyValue678" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_RESERVED_MODE_CMD] = TrafficConfigConstants.IPV6_AUTH_RESERVED_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_RESERVED_STEP_CMD] = "dummyValue680" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_RESERVED_TRACKING_CMD] = "dummyValue681" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SEQ_NUM_CMD] = "dummyValue682" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SEQ_NUM_COUNT_CMD] = "dummyValue683" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SEQ_NUM_MODE_CMD] = TrafficConfigConstants.IPV6_AUTH_SEQ_NUM_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SEQ_NUM_STEP_CMD] = "dummyValue685" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SEQ_NUM_TRACKING_CMD] = "dummyValue686" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SPI_CMD] = "dummyValue687" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SPI_COUNT_CMD] = "dummyValue688" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SPI_MODE_CMD] = TrafficConfigConstants.IPV6_AUTH_SPI_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SPI_STEP_CMD] = "dummyValue690" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_SPI_TRACKING_CMD] = "dummyValue691" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_STRING_CMD] = "dummyValue692" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_STRING_COUNT_CMD] = "dummyValue693" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_STRING_MODE_CMD] = TrafficConfigConstants.IPV6_AUTH_STRING_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_STRING_STEP_CMD] = "dummyValue695" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_STRING_TRACKING_CMD] = "dummyValue696" # static value
        dummyDict[TrafficConfigConstants.IPV6_AUTH_TYPE_CMD] = TrafficConfigConstants.IPV6_AUTH_TYPE_SHA1 # constant value
        dummyDict[TrafficConfigConstants.IPV6_CHECKSUM_CMD] = "dummyValue698" # static value
        dummyDict[TrafficConfigConstants.IPV6_DST_ADDR_CMD] = "dummyValue699" # static value
        dummyDict[TrafficConfigConstants.IPV6_DST_COUNT_CMD] = "dummyValue700" # static value
        dummyDict[TrafficConfigConstants.IPV6_DST_MASK_CMD] = "dummyValue701" # static value
        dummyDict[TrafficConfigConstants.IPV6_DST_MODE_CMD] = TrafficConfigConstants.IPV6_DST_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IPV6_DST_STEP_CMD] = "dummyValue703" # static value
        dummyDict[TrafficConfigConstants.IPV6_DST_TRACKING_CMD] = "dummyValue704" # static value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SEQ_NUMBER_CMD] = "dummyValue705" # static value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SEQ_NUMBER_COUNT_CMD] = "dummyValue706" # static value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SEQ_NUMBER_MODE_CMD] = TrafficConfigConstants.IPV6_ENCAP_SEQ_NUMBER_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SEQ_NUMBER_STEP_CMD] = "dummyValue708" # static value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SEQ_NUMBER_TRACKING_CMD] = "dummyValue709" # static value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SPI_CMD] = "dummyValue710" # static value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SPI_COUNT_CMD] = "dummyValue711" # static value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SPI_MODE_CMD] = TrafficConfigConstants.IPV6_ENCAP_SPI_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SPI_STEP_CMD] = "dummyValue713" # static value
        dummyDict[TrafficConfigConstants.IPV6_ENCAP_SPI_TRACKING_CMD] = "dummyValue714" # static value
        dummyDict[TrafficConfigConstants.IPV6_EXTENSION_HEADER_CMD] = TrafficConfigConstants.IPV6_EXTENSION_HEADER_NONE # constant value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_LABEL_CMD] = "dummyValue716" # static value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_LABEL_COUNT_CMD] = "dummyValue717" # static value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_LABEL_MODE_CMD] = TrafficConfigConstants.IPV6_FLOW_LABEL_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_LABEL_STEP_CMD] = "dummyValue719" # static value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_LABEL_TRACKING_CMD] = "dummyValue720" # static value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_VERSION_CMD] = "dummyValue721" # static value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_VERSION_COUNT_CMD] = "dummyValue722" # static value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_VERSION_MODE_CMD] = TrafficConfigConstants.IPV6_FLOW_VERSION_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_VERSION_STEP_CMD] = "dummyValue724" # static value
        dummyDict[TrafficConfigConstants.IPV6_FLOW_VERSION_TRACKING_CMD] = "dummyValue725" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_ID_CMD] = "dummyValue726" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_ID_COUNT_CMD] = "dummyValue727" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_ID_MODE_CMD] = TrafficConfigConstants.IPV6_FRAG_ID_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_ID_STEP_CMD] = "dummyValue729" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_ID_TRACKING_CMD] = "dummyValue730" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_MORE_FLAG_CMD] = "dummyValue731" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_MORE_FLAG_MODE_CMD] = TrafficConfigConstants.IPV6_FRAG_MORE_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_MORE_FLAG_TRACKING_CMD] = "dummyValue733" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_NEXT_HEADER_CMD] = "dummyValue734" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_OFFSET_CMD] = "dummyValue735" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_OFFSET_COUNT_CMD] = "dummyValue736" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_OFFSET_MODE_CMD] = TrafficConfigConstants.IPV6_FRAG_OFFSET_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_OFFSET_STEP_CMD] = "dummyValue738" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_OFFSET_TRACKING_CMD] = "dummyValue739" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_2BIT_CMD] = "dummyValue740" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_2BIT_COUNT_CMD] = "dummyValue741" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_2BIT_MODE_CMD] = TrafficConfigConstants.IPV6_FRAG_RES_2BIT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_2BIT_STEP_CMD] = "dummyValue743" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_2BIT_TRACKING_CMD] = "dummyValue744" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_8BIT_CMD] = "dummyValue745" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_8BIT_COUNT_CMD] = "dummyValue746" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_8BIT_MODE_CMD] = TrafficConfigConstants.IPV6_FRAG_RES_8BIT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_8BIT_STEP_CMD] = "dummyValue748" # static value
        dummyDict[TrafficConfigConstants.IPV6_FRAG_RES_8BIT_TRACKING_CMD] = "dummyValue749" # static value
        dummyDict[TrafficConfigConstants.IPV6_HOP_BY_HOP_OPTIONS_CMD] = "dummyValue750" # static value
        dummyDict[TrafficConfigConstants.IPV6_HOP_LIMIT_CMD] = "dummyValue751" # static value
        dummyDict[TrafficConfigConstants.IPV6_HOP_LIMIT_COUNT_CMD] = "dummyValue752" # static value
        dummyDict[TrafficConfigConstants.IPV6_HOP_LIMIT_MODE_CMD] = TrafficConfigConstants.IPV6_HOP_LIMIT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_HOP_LIMIT_STEP_CMD] = "dummyValue754" # static value
        dummyDict[TrafficConfigConstants.IPV6_HOP_LIMIT_TRACKING_CMD] = "dummyValue755" # static value
        dummyDict[TrafficConfigConstants.IPV6_LENGTH_CMD] = "dummyValue756" # static value
        dummyDict[TrafficConfigConstants.IPV6_NEXT_HEADER_CMD] = "dummyValue757" # static value
        dummyDict[TrafficConfigConstants.IPV6_NEXT_HEADER_COUNT_CMD] = "dummyValue758" # static value
        dummyDict[TrafficConfigConstants.IPV6_NEXT_HEADER_MODE_CMD] = TrafficConfigConstants.IPV6_NEXT_HEADER_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_NEXT_HEADER_STEP_CMD] = "dummyValue760" # static value
        dummyDict[TrafficConfigConstants.IPV6_NEXT_HEADER_TRACKING_CMD] = "dummyValue761" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_DST_ADDR_CMD] = "dummyValue762" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_DST_ADDR_COUNT_CMD] = "dummyValue763" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_DST_ADDR_MODE_CMD] = TrafficConfigConstants.IPV6_PSEUDO_DST_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_DST_ADDR_STEP_CMD] = "dummyValue765" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_DST_ADDR_TRACKING_CMD] = "dummyValue766" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_SRC_ADDR_CMD] = "dummyValue767" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_SRC_ADDR_COUNT_CMD] = "dummyValue768" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_SRC_ADDR_MODE_CMD] = TrafficConfigConstants.IPV6_PSEUDO_SRC_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_SRC_ADDR_STEP_CMD] = "dummyValue770" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_SRC_ADDR_TRACKING_CMD] = "dummyValue771" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_CMD] = "dummyValue772" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_COUNT_CMD] = "dummyValue773" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_MODE_CMD] = TrafficConfigConstants.IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_STEP_CMD] = "dummyValue775" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_TRACKING_CMD] = "dummyValue776" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_ZERO_NUMBER_CMD] = "dummyValue777" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_ZERO_NUMBER_COUNT_CMD] = "dummyValue778" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_ZERO_NUMBER_MODE_CMD] = TrafficConfigConstants.IPV6_PSEUDO_ZERO_NUMBER_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_ZERO_NUMBER_STEP_CMD] = "dummyValue780" # static value
        dummyDict[TrafficConfigConstants.IPV6_PSEUDO_ZERO_NUMBER_TRACKING_CMD] = "dummyValue781" # static value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_NODE_LIST_CMD] = "dummyValue782" # static value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_RES_CMD] = "dummyValue783" # static value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_RES_COUNT_CMD] = "dummyValue784" # static value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_RES_MODE_CMD] = TrafficConfigConstants.IPV6_ROUTING_RES_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_RES_STEP_CMD] = "dummyValue786" # static value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_RES_TRACKING_CMD] = "dummyValue787" # static value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_TYPE_CMD] = "dummyValue788" # static value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_TYPE_COUNT_CMD] = "dummyValue789" # static value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_TYPE_MODE_CMD] = TrafficConfigConstants.IPV6_ROUTING_TYPE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_TYPE_STEP_CMD] = "dummyValue791" # static value
        dummyDict[TrafficConfigConstants.IPV6_ROUTING_TYPE_TRACKING_CMD] = "dummyValue792" # static value
        dummyDict[TrafficConfigConstants.IPV6_SRC_ADDR_CMD] = "dummyValue793" # static value
        dummyDict[TrafficConfigConstants.IPV6_SRC_COUNT_CMD] = "dummyValue794" # static value
        dummyDict[TrafficConfigConstants.IPV6_SRC_MASK_CMD] = "dummyValue795" # static value
        dummyDict[TrafficConfigConstants.IPV6_SRC_MODE_CMD] = TrafficConfigConstants.IPV6_SRC_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.IPV6_SRC_STEP_CMD] = "dummyValue797" # static value
        dummyDict[TrafficConfigConstants.IPV6_SRC_TRACKING_CMD] = "dummyValue798" # static value
        dummyDict[TrafficConfigConstants.IPV6_TRAFFIC_CLASS_CMD] = "dummyValue799" # static value
        dummyDict[TrafficConfigConstants.IPV6_TRAFFIC_CLASS_COUNT_CMD] = "dummyValue800" # static value
        dummyDict[TrafficConfigConstants.IPV6_TRAFFIC_CLASS_MODE_CMD] = TrafficConfigConstants.IPV6_TRAFFIC_CLASS_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.IPV6_TRAFFIC_CLASS_STEP_CMD] = "dummyValue802" # static value
        dummyDict[TrafficConfigConstants.IPV6_TRAFFIC_CLASS_TRACKING_CMD] = "dummyValue803" # static value
        dummyDict[TrafficConfigConstants.ISL_CMD] = "dummyValue804" # static value
        dummyDict[TrafficConfigConstants.ISL_BPDU_CMD] = "dummyValue805" # static value
        dummyDict[TrafficConfigConstants.ISL_BPDU_COUNT_CMD] = "dummyValue806" # static value
        dummyDict[TrafficConfigConstants.ISL_BPDU_MODE_CMD] = TrafficConfigConstants.ISL_BPDU_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ISL_BPDU_STEP_CMD] = "dummyValue808" # static value
        dummyDict[TrafficConfigConstants.ISL_BPDU_TRACKING_CMD] = "dummyValue809" # static value
        dummyDict[TrafficConfigConstants.ISL_FRAME_TYPE_CMD] = TrafficConfigConstants.ISL_FRAME_TYPE_ETHERNET # constant value
        dummyDict[TrafficConfigConstants.ISL_FRAME_TYPE_MODE_CMD] = TrafficConfigConstants.ISL_FRAME_TYPE_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.ISL_FRAME_TYPE_TRACKING_CMD] = "dummyValue812" # static value
        dummyDict[TrafficConfigConstants.ISL_INDEX_CMD] = "dummyValue813" # static value
        dummyDict[TrafficConfigConstants.ISL_INDEX_COUNT_CMD] = "dummyValue814" # static value
        dummyDict[TrafficConfigConstants.ISL_INDEX_MODE_CMD] = TrafficConfigConstants.ISL_INDEX_MODE_DEFAULT # constant value
        dummyDict[TrafficConfigConstants.ISL_INDEX_STEP_CMD] = "dummyValue816" # static value
        dummyDict[TrafficConfigConstants.ISL_INDEX_TRACKING_CMD] = "dummyValue817" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_DST_CMD] = "dummyValue818" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_DST_COUNT_CMD] = "dummyValue819" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_DST_MODE_CMD] = TrafficConfigConstants.ISL_MAC_DST_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ISL_MAC_DST_STEP_CMD] = "dummyValue821" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_DST_TRACKING_CMD] = "dummyValue822" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_HIGH_CMD] = "dummyValue823" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_HIGH_COUNT_CMD] = "dummyValue824" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_HIGH_MODE_CMD] = TrafficConfigConstants.ISL_MAC_SRC_HIGH_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_HIGH_STEP_CMD] = "dummyValue826" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_HIGH_TRACKING_CMD] = "dummyValue827" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_LOW_CMD] = "dummyValue828" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_LOW_COUNT_CMD] = "dummyValue829" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_LOW_MODE_CMD] = TrafficConfigConstants.ISL_MAC_SRC_LOW_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_LOW_STEP_CMD] = "dummyValue831" # static value
        dummyDict[TrafficConfigConstants.ISL_MAC_SRC_LOW_TRACKING_CMD] = "dummyValue832" # static value
        dummyDict[TrafficConfigConstants.ISL_USER_PRIORITY_CMD] = "dummyValue833" # static value
        dummyDict[TrafficConfigConstants.ISL_USER_PRIORITY_COUNT_CMD] = "dummyValue834" # static value
        dummyDict[TrafficConfigConstants.ISL_USER_PRIORITY_MODE_CMD] = TrafficConfigConstants.ISL_USER_PRIORITY_MODE_DEFAULT # constant value
        dummyDict[TrafficConfigConstants.ISL_USER_PRIORITY_STEP_CMD] = "dummyValue836" # static value
        dummyDict[TrafficConfigConstants.ISL_USER_PRIORITY_TRACKING_CMD] = "dummyValue837" # static value
        dummyDict[TrafficConfigConstants.ISL_VLAN_ID_CMD] = "dummyValue838" # static value
        dummyDict[TrafficConfigConstants.ISL_VLAN_ID_COUNT_CMD] = "dummyValue839" # static value
        dummyDict[TrafficConfigConstants.ISL_VLAN_ID_MODE_CMD] = TrafficConfigConstants.ISL_VLAN_ID_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.ISL_VLAN_ID_STEP_CMD] = "dummyValue841" # static value
        dummyDict[TrafficConfigConstants.ISL_VLAN_ID_TRACKING_CMD] = "dummyValue842" # static value
        dummyDict[TrafficConfigConstants.L2_ENCAP_CMD] = TrafficConfigConstants.L2_ENCAP_HDLC_MULTICAST_MPLS # constant value
        dummyDict[TrafficConfigConstants.L3_GAUS1_AVG_CMD] = "dummyValue844" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS1_HALFBW_CMD] = "dummyValue845" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS1_WEIGHT_CMD] = "dummyValue846" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS2_AVG_CMD] = "dummyValue847" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS2_HALFBW_CMD] = "dummyValue848" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS2_WEIGHT_CMD] = "dummyValue849" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS3_AVG_CMD] = "dummyValue850" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS3_HALFBW_CMD] = "dummyValue851" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS3_WEIGHT_CMD] = "dummyValue852" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS4_AVG_CMD] = "dummyValue853" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS4_HALFBW_CMD] = "dummyValue854" # static value
        dummyDict[TrafficConfigConstants.L3_GAUS4_WEIGHT_CMD] = "dummyValue855" # static value
        dummyDict[TrafficConfigConstants.L3_IMIX1_RATIO_CMD] = "dummyValue856" # static value
        dummyDict[TrafficConfigConstants.L3_IMIX1_SIZE_CMD] = "dummyValue857" # static value
        dummyDict[TrafficConfigConstants.L3_IMIX2_RATIO_CMD] = "dummyValue858" # static value
        dummyDict[TrafficConfigConstants.L3_IMIX2_SIZE_CMD] = "dummyValue859" # static value
        dummyDict[TrafficConfigConstants.L3_IMIX3_RATIO_CMD] = "dummyValue860" # static value
        dummyDict[TrafficConfigConstants.L3_IMIX3_SIZE_CMD] = "dummyValue861" # static value
        dummyDict[TrafficConfigConstants.L3_IMIX4_RATIO_CMD] = "dummyValue862" # static value
        dummyDict[TrafficConfigConstants.L3_IMIX4_SIZE_CMD] = "dummyValue863" # static value
        dummyDict[TrafficConfigConstants.L3_LENGTH_CMD] = "dummyValue864" # static value
        dummyDict[TrafficConfigConstants.L3_LENGTH_MAX_CMD] = "dummyValue865" # static value
        dummyDict[TrafficConfigConstants.L3_LENGTH_MIN_CMD] = "dummyValue866" # static value
        dummyDict[TrafficConfigConstants.L3_LENGTH_STEP_CMD] = "dummyValue867" # static value
        dummyDict[TrafficConfigConstants.L3_PROTOCOL_CMD] = TrafficConfigConstants.L3_PROTOCOL_IPV4 # constant value
        dummyDict[TrafficConfigConstants.L4_PROTOCOL_CMD] = TrafficConfigConstants.L4_PROTOCOL_ICMP # constant value
        dummyDict[TrafficConfigConstants.LAN_RANGE_COUNT_CMD] = "dummyValue870" # static value
        dummyDict[TrafficConfigConstants.LATENCY_BINS_CMD] = "dummyValue871" # static value
        dummyDict[TrafficConfigConstants.LATENCY_BINS_ENABLE_CMD] = "dummyValue872" # static value
        dummyDict[TrafficConfigConstants.LATENCY_VALUES_CMD] = "dummyValue873" # static value
        dummyDict[TrafficConfigConstants.LENGTH_MODE_CMD] = TrafficConfigConstants.LENGTH_MODE_AUTO # constant value
        dummyDict[TrafficConfigConstants.LOOP_COUNT_CMD] = "dummyValue875" # static value
        dummyDict[TrafficConfigConstants.MAC_DISCOVERY_GW_CMD] = "dummyValue876" # static value
        dummyDict[TrafficConfigConstants.MAC_DST_CMD] = "dummyValue877" # static value
        dummyDict[TrafficConfigConstants.MAC_DST2_CMD] = "dummyValue878" # static value
        dummyDict[TrafficConfigConstants.MAC_DST2_COUNT_CMD] = "dummyValue879" # static value
        dummyDict[TrafficConfigConstants.MAC_DST2_MODE_CMD] = "dummyValue880" # static value
        dummyDict[TrafficConfigConstants.MAC_DST2_STEP_CMD] = "dummyValue881" # static value
        dummyDict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = "dummyValue882" # static value
        dummyDict[TrafficConfigConstants.MAC_DST_COUNT_STEP_CMD] = "dummyValue883" # static value
        dummyDict[TrafficConfigConstants.MAC_DST_MASK_CMD] = "dummyValue884" # static value
        dummyDict[TrafficConfigConstants.MAC_DST_MODE_CMD] = TrafficConfigConstants.MAC_DST_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.MAC_DST_SEED_CMD] = "dummyValue886" # static value
        dummyDict[TrafficConfigConstants.MAC_DST_STEP_CMD] = "dummyValue887" # static value
        dummyDict[TrafficConfigConstants.MAC_DST_TRACKING_CMD] = "dummyValue888" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC_CMD] = "dummyValue889" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC2_CMD] = "dummyValue890" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC2_COUNT_CMD] = "dummyValue891" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC2_MODE_CMD] = "dummyValue892" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC2_STEP_CMD] = "dummyValue893" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC_COUNT_CMD] = "dummyValue894" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC_MASK_CMD] = "dummyValue895" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC_MODE_CMD] = TrafficConfigConstants.MAC_SRC_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.MAC_SRC_SEED_CMD] = "dummyValue897" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC_STEP_CMD] = "dummyValue898" # static value
        dummyDict[TrafficConfigConstants.MAC_SRC_TRACKING_CMD] = "dummyValue899" # static value
        dummyDict[TrafficConfigConstants.MERGE_DESTINATIONS_CMD] = "dummyValue900" # static value
        dummyDict[TrafficConfigConstants.MIN_GAP_BYTES_CMD] = "dummyValue901" # static value
        dummyDict[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE # constant value
        dummyDict[TrafficConfigConstants.MPLS_CMD] = TrafficConfigConstants.MPLS_ENABLE # constant value
        dummyDict[TrafficConfigConstants.MPLS_BOTTOM_STACK_BIT_CMD] = "dummyValue904" # static value
        dummyDict[TrafficConfigConstants.MPLS_BOTTOM_STACK_BIT_COUNT_CMD] = "dummyValue905" # static value
        dummyDict[TrafficConfigConstants.MPLS_BOTTOM_STACK_BIT_MODE_CMD] = TrafficConfigConstants.MPLS_BOTTOM_STACK_BIT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.MPLS_BOTTOM_STACK_BIT_STEP_CMD] = "dummyValue907" # static value
        dummyDict[TrafficConfigConstants.MPLS_BOTTOM_STACK_BIT_TRACKING_CMD] = "dummyValue908" # static value
        dummyDict[TrafficConfigConstants.MPLS_EXP_BIT_CMD] = "dummyValue909" # static value
        dummyDict[TrafficConfigConstants.MPLS_EXP_BIT_COUNT_CMD] = "dummyValue910" # static value
        dummyDict[TrafficConfigConstants.MPLS_EXP_BIT_MODE_CMD] = TrafficConfigConstants.MPLS_EXP_BIT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.MPLS_EXP_BIT_STEP_CMD] = "dummyValue912" # static value
        dummyDict[TrafficConfigConstants.MPLS_EXP_BIT_TRACKING_CMD] = "dummyValue913" # static value
        dummyDict[TrafficConfigConstants.MPLS_LABELS_CMD] = "dummyValue914" # static value
        dummyDict[TrafficConfigConstants.MPLS_LABELS_COUNT_CMD] = "dummyValue915" # static value
        dummyDict[TrafficConfigConstants.MPLS_LABELS_MODE_CMD] = TrafficConfigConstants.MPLS_LABELS_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.MPLS_LABELS_STEP_CMD] = "dummyValue917" # static value
        dummyDict[TrafficConfigConstants.MPLS_LABELS_TRACKING_CMD] = "dummyValue918" # static value
        dummyDict[TrafficConfigConstants.MPLS_TTL_CMD] = "dummyValue919" # static value
        dummyDict[TrafficConfigConstants.MPLS_TTL_COUNT_CMD] = "dummyValue920" # static value
        dummyDict[TrafficConfigConstants.MPLS_TTL_MODE_CMD] = TrafficConfigConstants.MPLS_TTL_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.MPLS_TTL_STEP_CMD] = "dummyValue922" # static value
        dummyDict[TrafficConfigConstants.MPLS_TTL_TRACKING_CMD] = "dummyValue923" # static value
        dummyDict[TrafficConfigConstants.MPLS_TYPE_CMD] = TrafficConfigConstants.MPLS_TYPE_UNICAST # constant value
        dummyDict[TrafficConfigConstants.MULTIPLE_QUEUES_CMD] = "dummyValue925" # static value
        dummyDict[TrafficConfigConstants.NAME_CMD] = "dummyValue926" # static value
        dummyDict[TrafficConfigConstants.NO_WRITE_CMD] = "dummyValue927" # static value
        dummyDict[TrafficConfigConstants.NUM_DST_PORTS_CMD] = "dummyValue928" # static value
        dummyDict[TrafficConfigConstants.NUMBER_OF_PACKETS_PER_STREAM_CMD] = "dummyValue929" # static value
        dummyDict[TrafficConfigConstants.NUMBER_OF_PACKETS_TX_CMD] = "dummyValue930" # static value
        dummyDict[TrafficConfigConstants.OVERRIDE_VALUE_LIST_CMD] = "dummyValue931" # static value
        dummyDict[TrafficConfigConstants.PAUSE_CONTROL_TIME_CMD] = "dummyValue932" # static value
        dummyDict[TrafficConfigConstants.PENDING_OPERATIONS_TIMEOUT_CMD] = "dummyValue933" # static value
        dummyDict[TrafficConfigConstants.PGID_OFFSET_CMD] = "dummyValue934" # static value
        dummyDict[TrafficConfigConstants.PGID_VALUE_CMD] = "dummyValue935" # static value
        dummyDict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = "dummyValue936" # static value
        dummyDict[TrafficConfigConstants.PORT_HANDLE_CMD] = "dummyValue937" # static value
        dummyDict[TrafficConfigConstants.PORT_HANDLE2_CMD] = "dummyValue938" # static value
        dummyDict[TrafficConfigConstants.PPP_SESSION_ID_CMD] = "dummyValue939" # static value
        dummyDict[TrafficConfigConstants.PREAMBLE_CUSTOM_SIZE_CMD] = "dummyValue940" # static value
        dummyDict[TrafficConfigConstants.PREAMBLE_SIZE_MODE_CMD] = "dummyValue941" # static value
        dummyDict[TrafficConfigConstants.PT_HANDLE_CMD] = "dummyValue942" # static value
        dummyDict[TrafficConfigConstants.PUBLIC_PORT_IP_CMD] = "dummyValue943" # static value
        dummyDict[TrafficConfigConstants.PVC_COUNT_CMD] = "dummyValue944" # static value
        dummyDict[TrafficConfigConstants.PVC_COUNT_STEP_CMD] = "dummyValue945" # static value
        dummyDict[TrafficConfigConstants.QOS_BYTE_CMD] = "dummyValue946" # static value
        dummyDict[TrafficConfigConstants.QOS_BYTE_COUNT_CMD] = "dummyValue947" # static value
        dummyDict[TrafficConfigConstants.QOS_BYTE_MODE_CMD] = TrafficConfigConstants.QOS_BYTE_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.QOS_BYTE_STEP_CMD] = "dummyValue949" # static value
        dummyDict[TrafficConfigConstants.QOS_BYTE_TRACKING_CMD] = "dummyValue950" # static value
        dummyDict[TrafficConfigConstants.QOS_IPV6_FLOW_LABEL_CMD] = "dummyValue951" # static value
        dummyDict[TrafficConfigConstants.QOS_IPV6_TRAFFIC_CLASS_CMD] = "dummyValue952" # static value
        dummyDict[TrafficConfigConstants.QOS_TYPE_IXN_CMD] = TrafficConfigConstants.QOS_TYPE_IXN_TOS # constant value
        dummyDict[TrafficConfigConstants.QOS_VALUE_IXN_CMD] = "dummyValue954" # static value
        dummyDict[TrafficConfigConstants.QOS_VALUE_IXN_COUNT_CMD] = "dummyValue955" # static value
        dummyDict[TrafficConfigConstants.QOS_VALUE_IXN_MODE_CMD] = TrafficConfigConstants.QOS_VALUE_IXN_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.QOS_VALUE_IXN_STEP_CMD] = "dummyValue957" # static value
        dummyDict[TrafficConfigConstants.QOS_VALUE_IXN_TRACKING_CMD] = "dummyValue958" # static value
        dummyDict[TrafficConfigConstants.QUEUE_ID_CMD] = "dummyValue959" # static value
        dummyDict[TrafficConfigConstants.RAMP_UP_PERCENTAGE_CMD] = "dummyValue960" # static value
        dummyDict[TrafficConfigConstants.RANGE_PER_SPOKE_CMD] = "dummyValue961" # static value
        dummyDict[TrafficConfigConstants.RATE_BPS_CMD] = "dummyValue962" # static value
        dummyDict[TrafficConfigConstants.RATE_BYTEPS_CMD] = "dummyValue963" # static value
        dummyDict[TrafficConfigConstants.RATE_FRAME_GAP_CMD] = "dummyValue964" # static value
        dummyDict[TrafficConfigConstants.RATE_KBPS_CMD] = "dummyValue965" # static value
        dummyDict[TrafficConfigConstants.RATE_KBYTEPS_CMD] = "dummyValue966" # static value
        dummyDict[TrafficConfigConstants.RATE_MBPS_CMD] = "dummyValue967" # static value
        dummyDict[TrafficConfigConstants.RATE_MBYTEPS_CMD] = "dummyValue968" # static value
        dummyDict[TrafficConfigConstants.RATE_MODE_CMD] = "dummyValue969" # static value
        dummyDict[TrafficConfigConstants.RATE_PERCENT_CMD] = "dummyValue970" # static value
        dummyDict[TrafficConfigConstants.RATE_PPS_CMD] = "dummyValue971" # static value
        dummyDict[TrafficConfigConstants.RETURN_TO_ID_CMD] = "dummyValue972" # static value
        dummyDict[TrafficConfigConstants.RIP_COMMAND_CMD] = TrafficConfigConstants.RIP_COMMAND_TRACE_ON # constant value
        dummyDict[TrafficConfigConstants.RIP_COMMAND_MODE_CMD] = TrafficConfigConstants.RIP_COMMAND_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.RIP_COMMAND_TRACKING_CMD] = "dummyValue975" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_ADDR_FAMILY_ID_CMD] = "dummyValue976" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_ADDR_FAMILY_ID_COUNT_CMD] = "dummyValue977" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_ADDR_FAMILY_ID_MODE_CMD] = TrafficConfigConstants.RIP_RTE_ADDR_FAMILY_ID_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_RTE_ADDR_FAMILY_ID_STEP_CMD] = "dummyValue979" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_ADDR_FAMILY_ID_TRACKING_CMD] = "dummyValue980" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_IPV4_ADDR_CMD] = "dummyValue981" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_IPV4_ADDR_COUNT_CMD] = "dummyValue982" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_IPV4_ADDR_MODE_CMD] = TrafficConfigConstants.RIP_RTE_IPV4_ADDR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_RTE_IPV4_ADDR_STEP_CMD] = "dummyValue984" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_IPV4_ADDR_TRACKING_CMD] = "dummyValue985" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_METRIC_CMD] = "dummyValue986" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_METRIC_COUNT_CMD] = "dummyValue987" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_METRIC_MODE_CMD] = TrafficConfigConstants.RIP_RTE_METRIC_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_RTE_METRIC_STEP_CMD] = "dummyValue989" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_METRIC_TRACKING_CMD] = "dummyValue990" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED2_CMD] = "dummyValue991" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED2_COUNT_CMD] = "dummyValue992" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED2_MODE_CMD] = TrafficConfigConstants.RIP_RTE_V1_UNUSED2_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED2_STEP_CMD] = "dummyValue994" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED2_TRACKING_CMD] = "dummyValue995" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED3_CMD] = "dummyValue996" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED3_COUNT_CMD] = "dummyValue997" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED3_MODE_CMD] = TrafficConfigConstants.RIP_RTE_V1_UNUSED3_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED3_STEP_CMD] = "dummyValue999" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED3_TRACKING_CMD] = "dummyValue1000" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED4_CMD] = "dummyValue1001" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED4_COUNT_CMD] = "dummyValue1002" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED4_MODE_CMD] = TrafficConfigConstants.RIP_RTE_V1_UNUSED4_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED4_STEP_CMD] = "dummyValue1004" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V1_UNUSED4_TRACKING_CMD] = "dummyValue1005" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_NEXT_HOP_CMD] = "dummyValue1006" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_NEXT_HOP_COUNT_CMD] = "dummyValue1007" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_NEXT_HOP_MODE_CMD] = TrafficConfigConstants.RIP_RTE_V2_NEXT_HOP_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_NEXT_HOP_STEP_CMD] = "dummyValue1009" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_NEXT_HOP_TRACKING_CMD] = "dummyValue1010" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_ROUTE_TAG_CMD] = "dummyValue1011" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_ROUTE_TAG_COUNT_CMD] = "dummyValue1012" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_ROUTE_TAG_MODE_CMD] = TrafficConfigConstants.RIP_RTE_V2_ROUTE_TAG_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_ROUTE_TAG_STEP_CMD] = "dummyValue1014" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_ROUTE_TAG_TRACKING_CMD] = "dummyValue1015" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_SUBNET_MASK_CMD] = "dummyValue1016" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_SUBNET_MASK_COUNT_CMD] = "dummyValue1017" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_SUBNET_MASK_MODE_CMD] = TrafficConfigConstants.RIP_RTE_V2_SUBNET_MASK_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_SUBNET_MASK_STEP_CMD] = "dummyValue1019" # static value
        dummyDict[TrafficConfigConstants.RIP_RTE_V2_SUBNET_MASK_TRACKING_CMD] = "dummyValue1020" # static value
        dummyDict[TrafficConfigConstants.RIP_UNUSED_CMD] = "dummyValue1021" # static value
        dummyDict[TrafficConfigConstants.RIP_UNUSED_COUNT_CMD] = "dummyValue1022" # static value
        dummyDict[TrafficConfigConstants.RIP_UNUSED_MODE_CMD] = TrafficConfigConstants.RIP_UNUSED_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.RIP_UNUSED_STEP_CMD] = "dummyValue1024" # static value
        dummyDict[TrafficConfigConstants.RIP_UNUSED_TRACKING_CMD] = "dummyValue1025" # static value
        dummyDict[TrafficConfigConstants.RIP_VERSION_CMD] = TrafficConfigConstants.RIP_VERSION_1 # constant value
        dummyDict[TrafficConfigConstants.ROUTE_MESH_CMD] = TrafficConfigConstants.ROUTE_MESH_FULLY # constant value
        dummyDict[TrafficConfigConstants.RTP_CSRC_COUNT_CMD] = "dummyValue1028" # static value
        dummyDict[TrafficConfigConstants.RTP_PAYLOAD_TYPE_CMD] = "dummyValue1029" # static value
        dummyDict[TrafficConfigConstants.SESSION_AWARE_TRAFFIC_CMD] = TrafficConfigConstants.SESSION_AWARE_TRAFFIC_PPP # constant value
        dummyDict[TrafficConfigConstants.SIGNATURE_CMD] = "dummyValue1031" # static value
        dummyDict[TrafficConfigConstants.SIGNATURE_OFFSET_CMD] = "dummyValue1032" # static value
        dummyDict[TrafficConfigConstants.SITE_ID_CMD] = "dummyValue1033" # static value
        dummyDict[TrafficConfigConstants.SITE_ID_ENABLE_CMD] = "dummyValue1034" # static value
        dummyDict[TrafficConfigConstants.SITE_ID_STEP_CMD] = "dummyValue1035" # static value
        dummyDict[TrafficConfigConstants.SKIP_FRAME_SIZE_VALIDATION_CMD] = "dummyValue1036" # static value
        dummyDict[TrafficConfigConstants.SOURCE_FILTER_CMD] = TrafficConfigConstants.SOURCE_FILTER_6PE # constant value
        dummyDict[TrafficConfigConstants.SRC_DEST_MESH_CMD] = TrafficConfigConstants.SRC_DEST_MESH_FULLY # constant value
        dummyDict[TrafficConfigConstants.SSRC_CMD] = "dummyValue1039" # static value
        dummyDict[TrafficConfigConstants.STACK_INDEX_CMD] = "dummyValue1040" # static value
        dummyDict[TrafficConfigConstants.STREAM_ID_CMD] = "dummyValue1041" # static value
        dummyDict[TrafficConfigConstants.STREAM_PACKING_CMD] = TrafficConfigConstants.STREAM_PACKING_ONE_STREAM_PER_ENDPOINT_PAIR # constant value
        dummyDict[TrafficConfigConstants.TABLE_UDF_COLUMN_NAME_CMD] = "dummyValue1043" # static value
        dummyDict[TrafficConfigConstants.TABLE_UDF_COLUMN_OFFSET_CMD] = "dummyValue1044" # static value
        dummyDict[TrafficConfigConstants.TABLE_UDF_COLUMN_SIZE_CMD] = "dummyValue1045" # static value
        dummyDict[TrafficConfigConstants.TABLE_UDF_COLUMN_TYPE_CMD] = TrafficConfigConstants.TABLE_UDF_COLUMN_TYPE_BINARY # constant value
        dummyDict[TrafficConfigConstants.TABLE_UDF_ROWS_CMD] = "dummyValue1047" # static value
        dummyDict[TrafficConfigConstants.TAG_FILTER_CMD] = "dummyValue1048" # static value
        dummyDict[TrafficConfigConstants.TCP_ACK_FLAG_CMD] = "dummyValue1049" # static value
        dummyDict[TrafficConfigConstants.TCP_ACK_FLAG_MODE_CMD] = TrafficConfigConstants.TCP_ACK_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.TCP_ACK_FLAG_TRACKING_CMD] = "dummyValue1051" # static value
        dummyDict[TrafficConfigConstants.TCP_ACK_NUM_CMD] = "dummyValue1052" # static value
        dummyDict[TrafficConfigConstants.TCP_ACK_NUM_COUNT_CMD] = "dummyValue1053" # static value
        dummyDict[TrafficConfigConstants.TCP_ACK_NUM_MODE_CMD] = TrafficConfigConstants.TCP_ACK_NUM_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.TCP_ACK_NUM_STEP_CMD] = "dummyValue1055" # static value
        dummyDict[TrafficConfigConstants.TCP_ACK_NUM_TRACKING_CMD] = "dummyValue1056" # static value
        dummyDict[TrafficConfigConstants.TCP_CHECKSUM_CMD] = "dummyValue1057" # static value
        dummyDict[TrafficConfigConstants.TCP_CHECKSUM_COUNT_CMD] = "dummyValue1058" # static value
        dummyDict[TrafficConfigConstants.TCP_CHECKSUM_MODE_CMD] = TrafficConfigConstants.TCP_CHECKSUM_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.TCP_CHECKSUM_STEP_CMD] = "dummyValue1060" # static value
        dummyDict[TrafficConfigConstants.TCP_CHECKSUM_TRACKING_CMD] = "dummyValue1061" # static value
        dummyDict[TrafficConfigConstants.TCP_CWR_FLAG_CMD] = "dummyValue1062" # static value
        dummyDict[TrafficConfigConstants.TCP_CWR_FLAG_MODE_CMD] = TrafficConfigConstants.TCP_CWR_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.TCP_CWR_FLAG_TRACKING_CMD] = "dummyValue1064" # static value
        dummyDict[TrafficConfigConstants.TCP_DATA_OFFSET_CMD] = "dummyValue1065" # static value
        dummyDict[TrafficConfigConstants.TCP_DATA_OFFSET_COUNT_CMD] = "dummyValue1066" # static value
        dummyDict[TrafficConfigConstants.TCP_DATA_OFFSET_MODE_CMD] = TrafficConfigConstants.TCP_DATA_OFFSET_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.TCP_DATA_OFFSET_STEP_CMD] = "dummyValue1068" # static value
        dummyDict[TrafficConfigConstants.TCP_DATA_OFFSET_TRACKING_CMD] = "dummyValue1069" # static value
        dummyDict[TrafficConfigConstants.TCP_DST_PORT_CMD] = "dummyValue1070" # static value
        dummyDict[TrafficConfigConstants.TCP_DST_PORT_COUNT_CMD] = "dummyValue1071" # static value
        dummyDict[TrafficConfigConstants.TCP_DST_PORT_MODE_CMD] = TrafficConfigConstants.TCP_DST_PORT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.TCP_DST_PORT_STEP_CMD] = "dummyValue1073" # static value
        dummyDict[TrafficConfigConstants.TCP_DST_PORT_TRACKING_CMD] = "dummyValue1074" # static value
        dummyDict[TrafficConfigConstants.TCP_ECN_ECHO_FLAG_CMD] = "dummyValue1075" # static value
        dummyDict[TrafficConfigConstants.TCP_ECN_ECHO_FLAG_MODE_CMD] = TrafficConfigConstants.TCP_ECN_ECHO_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.TCP_ECN_ECHO_FLAG_TRACKING_CMD] = "dummyValue1077" # static value
        dummyDict[TrafficConfigConstants.TCP_FIN_FLAG_CMD] = "dummyValue1078" # static value
        dummyDict[TrafficConfigConstants.TCP_FIN_FLAG_MODE_CMD] = TrafficConfigConstants.TCP_FIN_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.TCP_FIN_FLAG_TRACKING_CMD] = "dummyValue1080" # static value
        dummyDict[TrafficConfigConstants.TCP_NS_FLAG_CMD] = "dummyValue1081" # static value
        dummyDict[TrafficConfigConstants.TCP_NS_FLAG_MODE_CMD] = TrafficConfigConstants.TCP_NS_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.TCP_NS_FLAG_TRACKING_CMD] = "dummyValue1083" # static value
        dummyDict[TrafficConfigConstants.TCP_PSH_FLAG_CMD] = "dummyValue1084" # static value
        dummyDict[TrafficConfigConstants.TCP_PSH_FLAG_MODE_CMD] = TrafficConfigConstants.TCP_PSH_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.TCP_PSH_FLAG_TRACKING_CMD] = "dummyValue1086" # static value
        dummyDict[TrafficConfigConstants.TCP_RESERVED_CMD] = "dummyValue1087" # static value
        dummyDict[TrafficConfigConstants.TCP_RESERVED_COUNT_CMD] = "dummyValue1088" # static value
        dummyDict[TrafficConfigConstants.TCP_RESERVED_MODE_CMD] = TrafficConfigConstants.TCP_RESERVED_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.TCP_RESERVED_STEP_CMD] = "dummyValue1090" # static value
        dummyDict[TrafficConfigConstants.TCP_RESERVED_TRACKING_CMD] = "dummyValue1091" # static value
        dummyDict[TrafficConfigConstants.TCP_RST_FLAG_CMD] = "dummyValue1092" # static value
        dummyDict[TrafficConfigConstants.TCP_RST_FLAG_MODE_CMD] = TrafficConfigConstants.TCP_RST_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.TCP_RST_FLAG_TRACKING_CMD] = "dummyValue1094" # static value
        dummyDict[TrafficConfigConstants.TCP_SEQ_NUM_CMD] = "dummyValue1095" # static value
        dummyDict[TrafficConfigConstants.TCP_SEQ_NUM_COUNT_CMD] = "dummyValue1096" # static value
        dummyDict[TrafficConfigConstants.TCP_SEQ_NUM_MODE_CMD] = TrafficConfigConstants.TCP_SEQ_NUM_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.TCP_SEQ_NUM_STEP_CMD] = "dummyValue1098" # static value
        dummyDict[TrafficConfigConstants.TCP_SEQ_NUM_TRACKING_CMD] = "dummyValue1099" # static value
        dummyDict[TrafficConfigConstants.TCP_SRC_PORT_CMD] = "dummyValue1100" # static value
        dummyDict[TrafficConfigConstants.TCP_SRC_PORT_COUNT_CMD] = "dummyValue1101" # static value
        dummyDict[TrafficConfigConstants.TCP_SRC_PORT_MODE_CMD] = TrafficConfigConstants.TCP_SRC_PORT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.TCP_SRC_PORT_STEP_CMD] = "dummyValue1103" # static value
        dummyDict[TrafficConfigConstants.TCP_SRC_PORT_TRACKING_CMD] = "dummyValue1104" # static value
        dummyDict[TrafficConfigConstants.TCP_SYN_FLAG_CMD] = "dummyValue1105" # static value
        dummyDict[TrafficConfigConstants.TCP_SYN_FLAG_MODE_CMD] = TrafficConfigConstants.TCP_SYN_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.TCP_SYN_FLAG_TRACKING_CMD] = "dummyValue1107" # static value
        dummyDict[TrafficConfigConstants.TCP_URG_FLAG_CMD] = "dummyValue1108" # static value
        dummyDict[TrafficConfigConstants.TCP_URG_FLAG_MODE_CMD] = TrafficConfigConstants.TCP_URG_FLAG_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.TCP_URG_FLAG_TRACKING_CMD] = "dummyValue1110" # static value
        dummyDict[TrafficConfigConstants.TCP_URGENT_PTR_CMD] = "dummyValue1111" # static value
        dummyDict[TrafficConfigConstants.TCP_URGENT_PTR_COUNT_CMD] = "dummyValue1112" # static value
        dummyDict[TrafficConfigConstants.TCP_URGENT_PTR_MODE_CMD] = TrafficConfigConstants.TCP_URGENT_PTR_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.TCP_URGENT_PTR_STEP_CMD] = "dummyValue1114" # static value
        dummyDict[TrafficConfigConstants.TCP_URGENT_PTR_TRACKING_CMD] = "dummyValue1115" # static value
        dummyDict[TrafficConfigConstants.TCP_WINDOW_CMD] = "dummyValue1116" # static value
        dummyDict[TrafficConfigConstants.TCP_WINDOW_COUNT_CMD] = "dummyValue1117" # static value
        dummyDict[TrafficConfigConstants.TCP_WINDOW_MODE_CMD] = TrafficConfigConstants.TCP_WINDOW_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.TCP_WINDOW_STEP_CMD] = "dummyValue1119" # static value
        dummyDict[TrafficConfigConstants.TCP_WINDOW_TRACKING_CMD] = "dummyValue1120" # static value
        dummyDict[TrafficConfigConstants.TEST_OBJECTIVE_VALUE_CMD] = "dummyValue1121" # static value
        dummyDict[TrafficConfigConstants.TIMESTAMP_INITIAL_VALUE_CMD] = "dummyValue1122" # static value
        dummyDict[TrafficConfigConstants.TRACK_BY_CMD] = TrafficConfigConstants.TRACK_BY_I_TAG_ISID # constant value
        dummyDict[TrafficConfigConstants.TRAFFIC_GENERATE_CMD] = "dummyValue1124" # static value
        dummyDict[TrafficConfigConstants.TRAFFIC_GENERATOR_CMD] = TrafficConfigConstants.TRAFFIC_GENERATOR_IXNETWORK # constant value
        dummyDict[TrafficConfigConstants.TRANSMIT_DISTRIBUTION_CMD] = TrafficConfigConstants.TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_LS_RJT_FCF_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_OX_ID # constant value
        dummyDict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS # constant value
        dummyDict[TrafficConfigConstants.TX_DELAY_CMD] = "dummyValue1128" # static value
        dummyDict[TrafficConfigConstants.TX_DELAY_UNIT_CMD] = TrafficConfigConstants.TX_DELAY_UNIT_NS # constant value
        dummyDict[TrafficConfigConstants.TX_MODE_CMD] = TrafficConfigConstants.TX_MODE_STREAM # constant value
        dummyDict[TrafficConfigConstants.UDF1_CASCADE_TYPE_CMD] = "dummyValue1131" # static value
        dummyDict[TrafficConfigConstants.UDF1_CHAIN_FROM_CMD] = TrafficConfigConstants.UDF1_CHAIN_FROM_UDFNONE # constant value
        dummyDict[TrafficConfigConstants.UDF1_COUNTER_INIT_VALUE_CMD] = "dummyValue1133" # static value
        dummyDict[TrafficConfigConstants.UDF1_COUNTER_MODE_CMD] = "dummyValue1134" # static value
        dummyDict[TrafficConfigConstants.UDF1_COUNTER_REPEAT_COUNT_CMD] = "dummyValue1135" # static value
        dummyDict[TrafficConfigConstants.UDF1_COUNTER_STEP_CMD] = "dummyValue1136" # static value
        dummyDict[TrafficConfigConstants.UDF1_COUNTER_TYPE_CMD] = "dummyValue1137" # static value
        dummyDict[TrafficConfigConstants.UDF1_COUNTER_UP_DOWN_CMD] = "dummyValue1138" # static value
        dummyDict[TrafficConfigConstants.UDF1_ENABLE_CASCADE_CMD] = "dummyValue1139" # static value
        dummyDict[TrafficConfigConstants.UDF1_INNER_REPEAT_COUNT_CMD] = "dummyValue1140" # static value
        dummyDict[TrafficConfigConstants.UDF1_INNER_REPEAT_VALUE_CMD] = "dummyValue1141" # static value
        dummyDict[TrafficConfigConstants.UDF1_INNER_STEP_CMD] = "dummyValue1142" # static value
        dummyDict[TrafficConfigConstants.UDF1_MASK_SELECT_CMD] = "dummyValue1143" # static value
        dummyDict[TrafficConfigConstants.UDF1_MASK_VAL_CMD] = "dummyValue1144" # static value
        dummyDict[TrafficConfigConstants.UDF1_MODE_CMD] = TrafficConfigConstants.UDF1_MODE_COUNTER # constant value
        dummyDict[TrafficConfigConstants.UDF1_OFFSET_CMD] = "dummyValue1146" # static value
        dummyDict[TrafficConfigConstants.UDF1_SKIP_MASK_BITS_CMD] = "dummyValue1147" # static value
        dummyDict[TrafficConfigConstants.UDF1_SKIP_ZEROS_AND_ONES_CMD] = "dummyValue1148" # static value
        dummyDict[TrafficConfigConstants.UDF1_VALUE_LIST_CMD] = "dummyValue1149" # static value
        dummyDict[TrafficConfigConstants.UDF2_CASCADE_TYPE_CMD] = "dummyValue1150" # static value
        dummyDict[TrafficConfigConstants.UDF2_CHAIN_FROM_CMD] = TrafficConfigConstants.UDF2_CHAIN_FROM_UDFNONE # constant value
        dummyDict[TrafficConfigConstants.UDF2_COUNTER_INIT_VALUE_CMD] = "dummyValue1152" # static value
        dummyDict[TrafficConfigConstants.UDF2_COUNTER_MODE_CMD] = "dummyValue1153" # static value
        dummyDict[TrafficConfigConstants.UDF2_COUNTER_REPEAT_COUNT_CMD] = "dummyValue1154" # static value
        dummyDict[TrafficConfigConstants.UDF2_COUNTER_STEP_CMD] = "dummyValue1155" # static value
        dummyDict[TrafficConfigConstants.UDF2_COUNTER_TYPE_CMD] = "dummyValue1156" # static value
        dummyDict[TrafficConfigConstants.UDF2_COUNTER_UP_DOWN_CMD] = "dummyValue1157" # static value
        dummyDict[TrafficConfigConstants.UDF2_ENABLE_CASCADE_CMD] = "dummyValue1158" # static value
        dummyDict[TrafficConfigConstants.UDF2_INNER_REPEAT_COUNT_CMD] = "dummyValue1159" # static value
        dummyDict[TrafficConfigConstants.UDF2_INNER_REPEAT_VALUE_CMD] = "dummyValue1160" # static value
        dummyDict[TrafficConfigConstants.UDF2_INNER_STEP_CMD] = "dummyValue1161" # static value
        dummyDict[TrafficConfigConstants.UDF2_MASK_SELECT_CMD] = "dummyValue1162" # static value
        dummyDict[TrafficConfigConstants.UDF2_MASK_VAL_CMD] = "dummyValue1163" # static value
        dummyDict[TrafficConfigConstants.UDF2_MODE_CMD] = "dummyValue1164" # static value
        dummyDict[TrafficConfigConstants.UDF2_OFFSET_CMD] = "dummyValue1165" # static value
        dummyDict[TrafficConfigConstants.UDF2_SKIP_MASK_BITS_CMD] = "dummyValue1166" # static value
        dummyDict[TrafficConfigConstants.UDF2_SKIP_ZEROS_AND_ONES_CMD] = "dummyValue1167" # static value
        dummyDict[TrafficConfigConstants.UDF2_VALUE_LIST_CMD] = "dummyValue1168" # static value
        dummyDict[TrafficConfigConstants.UDF3_CASCADE_TYPE_CMD] = "dummyValue1169" # static value
        dummyDict[TrafficConfigConstants.UDF3_CHAIN_FROM_CMD] = TrafficConfigConstants.UDF3_CHAIN_FROM_UDFNONE # constant value
        dummyDict[TrafficConfigConstants.UDF3_COUNTER_INIT_VALUE_CMD] = "dummyValue1171" # static value
        dummyDict[TrafficConfigConstants.UDF3_COUNTER_MODE_CMD] = "dummyValue1172" # static value
        dummyDict[TrafficConfigConstants.UDF3_COUNTER_REPEAT_COUNT_CMD] = "dummyValue1173" # static value
        dummyDict[TrafficConfigConstants.UDF3_COUNTER_STEP_CMD] = "dummyValue1174" # static value
        dummyDict[TrafficConfigConstants.UDF3_COUNTER_TYPE_CMD] = "dummyValue1175" # static value
        dummyDict[TrafficConfigConstants.UDF3_COUNTER_UP_DOWN_CMD] = "dummyValue1176" # static value
        dummyDict[TrafficConfigConstants.UDF3_ENABLE_CASCADE_CMD] = "dummyValue1177" # static value
        dummyDict[TrafficConfigConstants.UDF3_INNER_REPEAT_COUNT_CMD] = "dummyValue1178" # static value
        dummyDict[TrafficConfigConstants.UDF3_INNER_REPEAT_VALUE_CMD] = "dummyValue1179" # static value
        dummyDict[TrafficConfigConstants.UDF3_INNER_STEP_CMD] = "dummyValue1180" # static value
        dummyDict[TrafficConfigConstants.UDF3_MASK_SELECT_CMD] = "dummyValue1181" # static value
        dummyDict[TrafficConfigConstants.UDF3_MASK_VAL_CMD] = "dummyValue1182" # static value
        dummyDict[TrafficConfigConstants.UDF3_MODE_CMD] = "dummyValue1183" # static value
        dummyDict[TrafficConfigConstants.UDF3_OFFSET_CMD] = "dummyValue1184" # static value
        dummyDict[TrafficConfigConstants.UDF3_SKIP_MASK_BITS_CMD] = "dummyValue1185" # static value
        dummyDict[TrafficConfigConstants.UDF3_SKIP_ZEROS_AND_ONES_CMD] = "dummyValue1186" # static value
        dummyDict[TrafficConfigConstants.UDF3_VALUE_LIST_CMD] = "dummyValue1187" # static value
        dummyDict[TrafficConfigConstants.UDF4_CASCADE_TYPE_CMD] = "dummyValue1188" # static value
        dummyDict[TrafficConfigConstants.UDF4_CHAIN_FROM_CMD] = TrafficConfigConstants.UDF4_CHAIN_FROM_UDFNONE # constant value
        dummyDict[TrafficConfigConstants.UDF4_COUNTER_INIT_VALUE_CMD] = "dummyValue1190" # static value
        dummyDict[TrafficConfigConstants.UDF4_COUNTER_MODE_CMD] = "dummyValue1191" # static value
        dummyDict[TrafficConfigConstants.UDF4_COUNTER_REPEAT_COUNT_CMD] = "dummyValue1192" # static value
        dummyDict[TrafficConfigConstants.UDF4_COUNTER_STEP_CMD] = "dummyValue1193" # static value
        dummyDict[TrafficConfigConstants.UDF4_COUNTER_TYPE_CMD] = "dummyValue1194" # static value
        dummyDict[TrafficConfigConstants.UDF4_COUNTER_UP_DOWN_CMD] = "dummyValue1195" # static value
        dummyDict[TrafficConfigConstants.UDF4_ENABLE_CASCADE_CMD] = "dummyValue1196" # static value
        dummyDict[TrafficConfigConstants.UDF4_INNER_REPEAT_COUNT_CMD] = "dummyValue1197" # static value
        dummyDict[TrafficConfigConstants.UDF4_INNER_REPEAT_VALUE_CMD] = "dummyValue1198" # static value
        dummyDict[TrafficConfigConstants.UDF4_INNER_STEP_CMD] = "dummyValue1199" # static value
        dummyDict[TrafficConfigConstants.UDF4_MASK_SELECT_CMD] = "dummyValue1200" # static value
        dummyDict[TrafficConfigConstants.UDF4_MASK_VAL_CMD] = "dummyValue1201" # static value
        dummyDict[TrafficConfigConstants.UDF4_MODE_CMD] = "dummyValue1202" # static value
        dummyDict[TrafficConfigConstants.UDF4_OFFSET_CMD] = "dummyValue1203" # static value
        dummyDict[TrafficConfigConstants.UDF4_SKIP_MASK_BITS_CMD] = "dummyValue1204" # static value
        dummyDict[TrafficConfigConstants.UDF4_SKIP_ZEROS_AND_ONES_CMD] = "dummyValue1205" # static value
        dummyDict[TrafficConfigConstants.UDF4_VALUE_LIST_CMD] = "dummyValue1206" # static value
        dummyDict[TrafficConfigConstants.UDF5_CASCADE_TYPE_CMD] = "dummyValue1207" # static value
        dummyDict[TrafficConfigConstants.UDF5_CHAIN_FROM_CMD] = TrafficConfigConstants.UDF5_CHAIN_FROM_UDFNONE # constant value
        dummyDict[TrafficConfigConstants.UDF5_COUNTER_INIT_VALUE_CMD] = "dummyValue1209" # static value
        dummyDict[TrafficConfigConstants.UDF5_COUNTER_MODE_CMD] = "dummyValue1210" # static value
        dummyDict[TrafficConfigConstants.UDF5_COUNTER_REPEAT_COUNT_CMD] = "dummyValue1211" # static value
        dummyDict[TrafficConfigConstants.UDF5_COUNTER_STEP_CMD] = "dummyValue1212" # static value
        dummyDict[TrafficConfigConstants.UDF5_COUNTER_TYPE_CMD] = "dummyValue1213" # static value
        dummyDict[TrafficConfigConstants.UDF5_COUNTER_UP_DOWN_CMD] = "dummyValue1214" # static value
        dummyDict[TrafficConfigConstants.UDF5_ENABLE_CASCADE_CMD] = "dummyValue1215" # static value
        dummyDict[TrafficConfigConstants.UDF5_INNER_REPEAT_COUNT_CMD] = "dummyValue1216" # static value
        dummyDict[TrafficConfigConstants.UDF5_INNER_REPEAT_VALUE_CMD] = "dummyValue1217" # static value
        dummyDict[TrafficConfigConstants.UDF5_INNER_STEP_CMD] = "dummyValue1218" # static value
        dummyDict[TrafficConfigConstants.UDF5_MASK_SELECT_CMD] = "dummyValue1219" # static value
        dummyDict[TrafficConfigConstants.UDF5_MASK_VAL_CMD] = "dummyValue1220" # static value
        dummyDict[TrafficConfigConstants.UDF5_MODE_CMD] = "dummyValue1221" # static value
        dummyDict[TrafficConfigConstants.UDF5_OFFSET_CMD] = "dummyValue1222" # static value
        dummyDict[TrafficConfigConstants.UDF5_SKIP_MASK_BITS_CMD] = "dummyValue1223" # static value
        dummyDict[TrafficConfigConstants.UDF5_SKIP_ZEROS_AND_ONES_CMD] = "dummyValue1224" # static value
        dummyDict[TrafficConfigConstants.UDF5_VALUE_LIST_CMD] = "dummyValue1225" # static value
        dummyDict[TrafficConfigConstants.UDP_CHECKSUM_CMD] = "dummyValue1226" # static value
        dummyDict[TrafficConfigConstants.UDP_CHECKSUM_VALUE_CMD] = "dummyValue1227" # static value
        dummyDict[TrafficConfigConstants.UDP_CHECKSUM_VALUE_TRACKING_CMD] = "dummyValue1228" # static value
        dummyDict[TrafficConfigConstants.UDP_DST_PORT_CMD] = "dummyValue1229" # static value
        dummyDict[TrafficConfigConstants.UDP_DST_PORT_COUNT_CMD] = "dummyValue1230" # static value
        dummyDict[TrafficConfigConstants.UDP_DST_PORT_MODE_CMD] = TrafficConfigConstants.UDP_DST_PORT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.UDP_DST_PORT_STEP_CMD] = "dummyValue1232" # static value
        dummyDict[TrafficConfigConstants.UDP_DST_PORT_TRACKING_CMD] = "dummyValue1233" # static value
        dummyDict[TrafficConfigConstants.UDP_LENGTH_CMD] = "dummyValue1234" # static value
        dummyDict[TrafficConfigConstants.UDP_LENGTH_COUNT_CMD] = "dummyValue1235" # static value
        dummyDict[TrafficConfigConstants.UDP_LENGTH_MODE_CMD] = TrafficConfigConstants.UDP_LENGTH_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.UDP_LENGTH_STEP_CMD] = "dummyValue1237" # static value
        dummyDict[TrafficConfigConstants.UDP_LENGTH_TRACKING_CMD] = "dummyValue1238" # static value
        dummyDict[TrafficConfigConstants.UDP_SRC_PORT_CMD] = "dummyValue1239" # static value
        dummyDict[TrafficConfigConstants.UDP_SRC_PORT_COUNT_CMD] = "dummyValue1240" # static value
        dummyDict[TrafficConfigConstants.UDP_SRC_PORT_MODE_CMD] = TrafficConfigConstants.UDP_SRC_PORT_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.UDP_SRC_PORT_STEP_CMD] = "dummyValue1242" # static value
        dummyDict[TrafficConfigConstants.UDP_SRC_PORT_TRACKING_CMD] = "dummyValue1243" # static value
        dummyDict[TrafficConfigConstants.USE_ALL_IP_SUBNETS_CMD] = "dummyValue1244" # static value
        dummyDict[TrafficConfigConstants.USE_CP_RATE_CMD] = "dummyValue1245" # static value
        dummyDict[TrafficConfigConstants.USE_CP_SIZE_CMD] = "dummyValue1246" # static value
        dummyDict[TrafficConfigConstants.VCI_CMD] = "dummyValue1247" # static value
        dummyDict[TrafficConfigConstants.VCI_COUNT_CMD] = "dummyValue1248" # static value
        dummyDict[TrafficConfigConstants.VCI_INCREMENT_CMD] = "dummyValue1249" # static value
        dummyDict[TrafficConfigConstants.VCI_INCREMENT_STEP_CMD] = "dummyValue1250" # static value
        dummyDict[TrafficConfigConstants.VCI_STEP_CMD] = "dummyValue1251" # static value
        dummyDict[TrafficConfigConstants.VLAN_CMD] = TrafficConfigConstants.VLAN_ENABLE # constant value
        dummyDict[TrafficConfigConstants.VLAN_CFI_CMD] = "dummyValue1253" # static value
        dummyDict[TrafficConfigConstants.VLAN_CFI_COUNT_CMD] = "dummyValue1254" # static value
        dummyDict[TrafficConfigConstants.VLAN_CFI_MODE_CMD] = TrafficConfigConstants.VLAN_CFI_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.VLAN_CFI_STEP_CMD] = "dummyValue1256" # static value
        dummyDict[TrafficConfigConstants.VLAN_CFI_TRACKING_CMD] = "dummyValue1257" # static value
        dummyDict[TrafficConfigConstants.VLAN_ENABLE_CMD] = "dummyValue1258" # static value
        dummyDict[TrafficConfigConstants.VLAN_ID_CMD] = "dummyValue1259" # static value
        dummyDict[TrafficConfigConstants.VLAN_ID_COUNT_CMD] = "dummyValue1260" # static value
        dummyDict[TrafficConfigConstants.VLAN_ID_MODE_CMD] = TrafficConfigConstants.VLAN_ID_MODE_FIXED # constant value
        dummyDict[TrafficConfigConstants.VLAN_ID_STEP_CMD] = "dummyValue1262" # static value
        dummyDict[TrafficConfigConstants.VLAN_ID_TRACKING_CMD] = "dummyValue1263" # static value
        dummyDict[TrafficConfigConstants.VLAN_PROTOCOL_TAG_ID_CMD] = "dummyValue1264" # static value
        dummyDict[TrafficConfigConstants.VLAN_PROTOCOL_TAG_ID_COUNT_CMD] = "dummyValue1265" # static value
        dummyDict[TrafficConfigConstants.VLAN_PROTOCOL_TAG_ID_MODE_CMD] = TrafficConfigConstants.VLAN_PROTOCOL_TAG_ID_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.VLAN_PROTOCOL_TAG_ID_STEP_CMD] = "dummyValue1267" # static value
        dummyDict[TrafficConfigConstants.VLAN_PROTOCOL_TAG_ID_TRACKING_CMD] = "dummyValue1268" # static value
        dummyDict[TrafficConfigConstants.VLAN_USER_PRIORITY_CMD] = "dummyValue1269" # static value
        dummyDict[TrafficConfigConstants.VLAN_USER_PRIORITY_COUNT_CMD] = "dummyValue1270" # static value
        dummyDict[TrafficConfigConstants.VLAN_USER_PRIORITY_MODE_CMD] = TrafficConfigConstants.VLAN_USER_PRIORITY_MODE_INCR # constant value
        dummyDict[TrafficConfigConstants.VLAN_USER_PRIORITY_STEP_CMD] = "dummyValue1272" # static value
        dummyDict[TrafficConfigConstants.VLAN_USER_PRIORITY_TRACKING_CMD] = "dummyValue1273" # static value
        dummyDict[TrafficConfigConstants.VPI_CMD] = "dummyValue1274" # static value
        dummyDict[TrafficConfigConstants.VPI_COUNT_CMD] = "dummyValue1275" # static value
        dummyDict[TrafficConfigConstants.VPI_INCREMENT_CMD] = "dummyValue1276" # static value
        dummyDict[TrafficConfigConstants.VPI_INCREMENT_STEP_CMD] = "dummyValue1277" # static value
        dummyDict[TrafficConfigConstants.VPI_STEP_CMD] = "dummyValue1278" # static value

        api = device.getApi(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        api.traffic_config(dummyDict)
    """
    def traffic_config(self, argdictionary, supported = None, suppressed_output = None):
        self.process_supported_hltapi_commands(argdictionary, supported, suppressed_output)
        return self.send_command_args(self._nameSpace +"::traffic_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_config_adjust_rate(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_allow_self_destined(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_app_profile_type(self):
        """
        This is the method the command: traffic_config option app_profile_type
        Description:Deprecated Argument. It was used for Legacy AppLib.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork' |
        Constants Available: APP_PROFILE_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.APP_PROFILE_TYPE_CMD : ""})

    def traffic_config_arp_dst_hw_addr(self, mac):
        """
        This is the method the command: traffic_config option arp_dst_hw_addr
        Description:Value of the destination MAC address for arp packets from a particular stream.
        Constants Available: ARP_DST_HW_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ARP_DST_HW_ADDR_CMD : mac})

    def traffic_config_arp_dst_hw_count(self, count):
        """
        This is the method the command: traffic_config option arp_dst_hw_count
        Description:Number of destination MAC addresses used in ARP packets in a particular stream.
        Constants Available: ARP_DST_HW_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        count --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ARP_DST_HW_COUNT_CMD : count})

    def traffic_config_arp_dst_hw_mode(self, count):
        """
        This is the method the command: traffic_config option arp_dst_hw_mode
        Description:This parameter configures the behavior for arp_dst_hw_addr.
            Valid options are:
            fixed: the value is left unchanged for all packets.
            increment: the value is incremented as specified with arp_dst_hw_step and arp_dst_hw_count.
            decrement: the value is decremented as specified with arp_dst_hw_step and arp_dst_hw_count.
            list: Parameter -arp_dst_hw contains a list of values. Each packet will use one of the values from the list.
        Constants Available: ARP_DST_HW_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        count --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ARP_DST_HW_MODE_CMD : count})

    def traffic_config_arp_dst_hw_step(self, mac):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_dst_hw_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_operation(self, opt):
        """
        This is the method the command: traffic_config option arp_operation
        Description:Type of ARP operation given to a particular ARP packet from a particular
            stream. Valid options are: arpRequestArp request.arpReplyArp
            reply.rarpRequestReverse Arp request.rarpReplyReverse Arp reply.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: ARP_OPERATION_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ARP_OPERATION_CMD : opt})

    def traffic_config_arp_operation_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_operation_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_src_hw_addr(self, mac):
        """
        This is the method the command: traffic_config option arp_src_hw_addr
        Description:Value of the source MAC address for arp packets from a particular stream.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: ARP_SRC_HW_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ARP_SRC_HW_ADDR_CMD : mac})

    def traffic_config_arp_src_hw_count(self, numeric):
        """
        This is the method the command: traffic_config option arp_src_hw_count
        Description:Number of source MAC addresses used in ARP packets in a particular stream.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: ARP_SRC_HW_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ARP_SRC_HW_COUNT_CMD : numeric})

    def traffic_config_arp_src_hw_mode(self, opt):
        """
        This is the method the command: traffic_config option arp_src_hw_mode
        Description:Behavior of the source MAC address for ARP packets from a particular
            stream. Valid options are: fixedDEFAULTincrementthe value is incremented
            as specified with arp_src_hw_step and arp_src_hw_count.decrementthe
            value is decremented as specified with arp_src_hw_step and
            arp_src_hw_count.listParameter -arp_src_hw contains a list of values.
            Each packet will use one of the values from the list.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos' |
        Constants Available: ARP_SRC_HW_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ARP_SRC_HW_MODE_CMD : opt})

    def traffic_config_arp_src_hw_step(self, mac):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_src_hw_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_data_item_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_mask_select(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_mask_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_data_item_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_mask_select(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_mask_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_aal5error(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_cell_loss_priority(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_cpcs_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_enable_auto_vpi_vci(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_enable_cl(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_enable_cpcs_length(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_encapsulation(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_generic_flow_ctrl(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_hec_errors(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_range_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_becn(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_bidirectional(self, flag):
        """
        This is the method the command: traffic_config option bidirectional
        Description:Whether traffic is setup to transmit in both directions. When
            -traffic_generator is set to ixos:
            The two ports receiving and transmitting are specified by options
            port_handle and port_handle2.
            Option 'l3_protocol' source and destination addresses are swapped to get
            the traffic flowing in both directions.
            The parameters are based on the port associated with port_handle and are
            swapped for the port associated with port_handle2.
            MAC addresses can be handled in two ways. First, if the MAC destination
            addresses are not provided, ARP is used to get the next hop MAC address
            based on the gateway IP address set in the command interface_config.
            Second, use option 'mac_dst' and 'mac_dst2' addresses provided by this
            command. Option 'mac_dst2' applies to the port associated with option
            'port_handle2'. Option 'stream_id' is the same for both directions. As
            for the source MAC, you can use option 'mac_src2' to configure the MAC
            on the second port, and option 'mac_dst2' to configure the destination
            MAC on the second port if you are not using L2 next hop.
            When using subports (this is valid only for PPP/L2TP emulations), the
            traffic flow direction (upstream or downstream) is set per port, not per
            subport. All the subports created must have the traffic flow set in the
            same direction (upstream or downstream). If subports have different
            traffic flow direction, the traffic will be bidirectional.
            When -traffic_generator is set to ixnetwork: Two traffic items will be
            configured. The first traffic item will have:
            source - the emulation specified by emulation_src_handle
            destination - the destination specified by emulation_dst_handle
            The second traffic item will have:
            source - the emulation specified by emulation_dst_handle
            destination - the destination specified by emulation_src_handle
            The rest of the specified options will be set on both traffic items.
            Valid options are:
            0 Disabled. 1 Enabled.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: BIDIRECTIONAL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.BIDIRECTIONAL_CMD : flag})

    def traffic_config_burst_loop_count(self, numeric):
        """
        This is the method the command: traffic_config option burst_loop_count
        Description:Number of times to transmit a burst.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: BURST_LOOP_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.BURST_LOOP_COUNT_CMD : numeric})

    def traffic_config_circuit_endpoint_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_circuit_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_command_response(self, flag):
        """
        This is the method the command: traffic_config option command_response
        Description:Set Command Response bit.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos' |
        Constants Available: COMMAND_RESPONSE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.COMMAND_RESPONSE_CMD : flag})

    def traffic_config_convert_to_raw(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_csrc_list(self):
        """
        This is the method the command: traffic_config option csrc_list
        Description:Specifies the CSRC list which identifies the contributing sources for
            the payload contained in this packet. The number of identifiers is given
            by the CC field. If there are more than 15 contributing sources, only 15
            may be identified. CSRC identifiers are inserted by mixers, using the
            SSRC identifiers of contributing sources. Note: 0 to 15 items, 32 bits
            each and is required if csrc_count is > 0
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: CSRC_LIST_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.CSRC_LIST_CMD : ""})

    def traffic_config_custom_offset(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_custom_values(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_pattern(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_pattern_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_tos(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_tos_count(self, numeric):
        """
        This is the method the command: traffic_config option data_tos_count
        Description:Numeric value which configures the number of times the data_tos is
            incremeneted or decremented when data_tos_mode is incr or decr.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: DATA_TOS_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.DATA_TOS_COUNT_CMD : numeric})

    def traffic_config_data_tos_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_tos_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_tos_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_destination_filter(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_boot_filename(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_boot_filename_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_ip_addr_count(self, numeric):
        """
        This is the method the command: traffic_config option dhcp_client_ip_addr_count
        Description:Numeric value which configures the number of times the
            dhcp_client_ip_addr is incremeneted or decremented when
            dhcp_client_ip_addr_mode is incr or decr.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: DHCP_CLIENT_IP_ADDR_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_COUNT_CMD : numeric})

    def traffic_config_dhcp_client_ip_addr_mode(self, opt):
        """
        This is the method the command: traffic_config option dhcp_client_ip_addr_mode
        Description:This parameter configures
            Valid options are:
            fixed

            the value is left unchanged for all packets.
            incr

            the value is incremented as specified with dhcp_client_ip_addr_step and
            dhcp_client_ip_addr_count.
            decr

            the value is decremented as specified with dhcp_client_ip_addr_step and
            dhcp_client_ip_addr_count.
            list

            Parameter -dhcp_client_ip_addr contains a list of values. Each packet
            will use one of the values from the list.
            DEFAULT

            fixed
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: DHCP_CLIENT_IP_ADDR_MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_MODE_CMD : opt})

    def traffic_config_dhcp_client_ip_addr_step(self, ip):
        """
        This is the method the command: traffic_config option dhcp_client_ip_addr_step
        Description:Step value used to modify dhcp_client_ip_addr when
            dhcp_client_ip_addr_mode is incr or decr.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: DHCP_CLIENT_IP_ADDR_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_STEP_CMD : ip})

    def traffic_config_dhcp_client_ip_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_flags(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_flags_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_flags_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_operation_code(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_operation_code_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_operation_code_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_option(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_option_data(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_host_name(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_host_name_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_discard_eligible(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_core_enable(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_core_value(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_count_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_extended_address0(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_extended_address1(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_extended_address2(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_extended_address3(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_mask_select(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_mask_value(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_repeat_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_repeat_count_step(self, numeric):
        """
        This is the method the command: traffic_config option dlci_repeat_count_step
        Description:Repeat count step for dlci_value. The valid range is 0-4294967295. Valid
            only for traffic_generator ixnetwork for L2VPN traffic, but is not
            supported in this release.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork' |
        Constants Available: DLCI_REPEAT_COUNT_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.DLCI_REPEAT_COUNT_STEP_CMD : numeric})

    def traffic_config_dlci_size(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_value_step(self, numeric):
        """
        This is the method the command: traffic_config option dlci_value_step
        Description:Data Link Connection Identifier step. Depending on the traffic_generator
            value, this option has different value ranges. Valid choices are ixos -
            Valid range is 0-65535.ixnetwork (not supported in this release) - Valid
            range is 0-4294967295. The option can only be used for L2VPN traffic.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork' |
        Constants Available: DLCI_VALUE_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.DLCI_VALUE_STEP_CMD : numeric})

    def traffic_config_duration(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dynamic_update_fields(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_custom_field_offset(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_custom_offset(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_custom_width(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_tracking(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_tracking_encap(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_dst_handle(self):
        """
        This is the method the command: traffic_config option emulation_dst_handle
        Description:The handle used to retrieve information for L2 or L3 dst addresses and
            use them to configure the destinations for traffic.
            This should be the emulation handle that was obtained after configuring
            PPP/L2TP protocols with IxTclAccess or routing protocols with
            IxTclNetwork (BGP, OSPF, ISIS, LDP, RSVP, etc). This parameter can be
            provided with a list or with a list of lists elements. The following
            list will create one endpointset with n elements: {<endpoint_1>
            <endpoint_2> ... <endpoint_n>}
            The following list of lists will create multiple endpointsets with
            m,n,...,p elements: { {endpointset <endpoint_1.1> <endpoint_1.2> ...
            <endpoint_1.m>} {endpointset <endpoint_2.1> <endpoint_2.2> ...
            <endpoint_1.n>} ...{endpointset <endpoint_2.1> <endpoint_2.2> ...
            <endpoint_1.p>} }
            Note that in this combination the first item in the list is endpointset.
            This string is optional. The parameter -endpointset_count should be
            equal to the number of list elements provided to -emulation_src_handle
            and -emulation_dst_handle. Example 1: endpointset_count 1
            emulation_src_handle {<endpoint_1.1> <endpoint_1.2> <endpoint_1.3>}
            emulation_dst_handle {<endpoint_2.1> <endpoint_2.2> <endpoint_2.3>}
            Example 2: endpointset_count 1 emulation_src_handle {{endpointset
            <endpoint_1.1> <endpoint_1.2> <endpoint_1.3>}} emulation_dst_handle
            {{endpointset <endpoint_2.1> <endpoint_2.2> <endpoint_2.3>}} Example 3:
            endpointset_count 3 emulation_src_handle { {endpointset
            <endpoint_src_1.1> <endpoint_src_1.2> <endpoint_src_1.3>
            <endpoint_src_1.4>} {endpointset <endpoint_src_2.1> <endpoint_src_2.2>
            <endpoint_src_2.3>} {endpointset <endpoint_src_3.1> <endpoint_src_3.2>
            <endpoint_src_3.3> <endpoint_src_3.4> <endpoint_src_3.5>} }
            emulation_src_handle { {endpointset <endpoint_dst_1.1>
            <endpoint_dst_1.2> <endpoint_dst_1.3> <endpoint_dst_1.4>} {endpointset
            <endpoint_dst_2.1> <endpoint_dst_2.2> <endpoint_dst_2.3>} {endpointset
            <endpoint_dst_3.1> <endpoint_dst_3.2> <endpoint_dst_3.3>
            <endpoint_dst_3.4> <endpoint_dst_3.5>} }
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: EMULATION_DST_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.EMULATION_DST_HANDLE_CMD : ""})

    def traffic_config_emulation_dst_vlan_protocol_tag_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_dst_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_dst_handle_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_rcvr_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_rcvr_host_index(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_rcvr_mcast_index(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_rcvr_port_index(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_override_ppp_ip_addr(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_intf_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_intf_start(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_port_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_port_start(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_intf_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_intf_start(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_port_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_port_start(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_src_handle(self):
        """
        This is the method the command: traffic_config option emulation_src_handle
        Description:The handle used to retrieve information for L2 or L3 src addresses and
            use them to configure the sources for traffic.
            This should be the emulation handle that was obtained after configuring
            PPP/L2TP protocols with IxTclAccess or routing protocols with
            IxTclNetwork (BGP, OSPF, ISIS, LDP, RSVP, etc). This parameter can be
            provided with a list or with a list of lists elements. The following
            list will create one endpointset with n elements: {<endpoint_1>
            <endpoint_2> ... <endpoint_n>}The following list of lists will create
            multiple endpointsets with m,n,...,p elements: { {endpointset
            <endpoint_1.1> <endpoint_1.2> ... <endpoint_1.m>} {endpointset
            <endpoint_2.1> <endpoint_2.2> ... <endpoint_1.n>} ...{endpointset
            <endpoint_q.1> <endpoint_q.2> ... <endpoint_q.p>} }
            Note that in this combination the first item in the list is endpointset.
            This string is optional. The parameter -endpointset_count should be
            equal to the number of list elements provided to -emulation_src_handle
            and -emulation_dst_handle. Example 1: endpointset_count1
            emulation_src_handle {<endpoint_1.1> <endpoint_1.2> <endpoint_1.3>}
            emulation_dst_handle {<endpoint_2.1> <endpoint_2.2> <endpoint_2.3>}
            Example 2: endpointset_count 1 emulation_src_handle {{endpointset
            <endpoint_1.1> <endpoint_1.2> <endpoint_1.3>}} emulation_dst_handle
            {{endpointset <endpoint_2.1> <endpoint_2.2> <endpoint_2.3>}} Example 3:
            endpointset_count 3 emulation_src_handle { {endpointset
            <endpoint_src_1.1> <endpoint_src_1.2> <endpoint_src_1.3>
            <endpoint_src_1.4>} {endpointset <endpoint_src_2.1> <endpoint_src_2.2>
            <endpoint_src_2.3>} {endpointset <endpoint_src_3.1> <endpoint_src_3.2>
            <endpoint_src_3.3> <endpoint_src_3.4> <endpoint_src_3.5>} }
            emulation_src_handle { {endpointset <endpoint_dst_1.1>
            <endpoint_dst_1.2> <endpoint_dst_1.3> <endpoint_dst_1.4>} {endpointset
            <endpoint_dst_2.1> <endpoint_dst_2.2> <endpoint_dst_2.3>} {endpointset
            <endpoint_dst_3.1> <endpoint_dst_3.2> <endpoint_dst_3.3>
            <endpoint_dst_3.4> <endpoint_dst_3.5>} }
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: EMULATION_SRC_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.EMULATION_SRC_HANDLE_CMD : ""})

    def traffic_config_emulation_src_vlan_protocol_tag_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_auto_detect_instrumentation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_ce_to_pe_traffic(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_data_integrity(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_dynamic_mpls_labels(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_override_value(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_pgid(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_test_objective(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_time_stamp(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf1(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf2(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf3(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf4(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf5(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_endpointset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_enforce_min_gap(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value(self, value):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value_step(self, hexdefault0x01):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_fcs(self, opt):
        """
        This is the method the command: traffic_config option fcs
        Description:Whether to insert an fcs error in the frame. Valid choices are: 0 - Disabled.1 - Enable. The fcs error type can be specified with -fcs_type option.
        Constants Available: FCS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.FCS_CMD : opt})

    def traffic_config_fcs_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_fecn(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_activeFieldChoice(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_auto(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_countValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_fieldValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_fullMesh(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_linked(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_linked_to(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_optionalEnabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_singleValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_startValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_stepValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_trackingEnabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_valueList(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_valueType(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_fr_range_count(self):
        """
        This is the method the command: traffic_config option fr_range_count
        Description:This option is used to specify the number of Frame relay static endpoint
            ranges. It can take any numeric value. This option is available only
            when using the ixnetwork traffic generator for L2VPN traffic, but is not
            supported in this release.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork' |
        Constants Available: FR_RANGE_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.FR_RANGE_COUNT_CMD : ""})

    def traffic_config_frame_rate_distribution_port(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_rate_distribution_stream(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_sequencing(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_sequencing_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_sequencing_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size(self, size):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_distribution(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_gauss(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_imix(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_max(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_min(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_dest_mac_retry_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_dest_mac_retry_delay(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_display_mpls_current_label_value(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_dest_mac_retry(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_mac_change_on_fly(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_min_frame_size(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_staggered_transmit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_stream_ordering(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_frame_ordering(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_large_error_threshhold(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_max_traffic_generation_queries(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_mpls_label_learning_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_peak_loading_replication_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_refresh_learned_info_before_apply(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_stream_control(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_stream_control_iterations(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_use_tx_rx_sync(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_wait_time(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_enable_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_enable_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_enable_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_enable_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_enable_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_enable_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_valid_checksum_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_header_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_hosts_per_net(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_checksum(self):
        """
        This is the method the command: traffic_config option icmp_checksum
        Description:Valid only for traffic_generator ixnetwork_540 and ICMPv4. Configure 2
            byte HEX 'Checksum' field.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: ICMP_CHECKSUM_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ICMP_CHECKSUM_CMD : ""})

    def traffic_config_icmp_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_checksum_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_code(self, numeric):
        """
        This is the method the command: traffic_config option icmp_code
        Description:Code for each ICMP message type. Valid choices are between 0 and 255, inclusive. Valid only for ICMPv4 with traffic_generator is ixos.
        Constants Available: ICMP_CODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ICMP_CODE_CMD : numeric})

    def traffic_config_icmp_code_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_code_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_code_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_code_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_id(self, numeric):
        """
        This is the method the command: traffic_config option icmp_id
        Description:ID for each ping command, i.e. echoRequest. Valid choices are between 0 and 65535, inclusive. Valid only for ICMPv4.
        Constants Available: ICMP_ID_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ICMP_ID_CMD : numeric})

    def traffic_config_icmp_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_s_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_s_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_s_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_m_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_m_bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_m_bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_o_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_o_bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_o_bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_o_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_o_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_o_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_r_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_r_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_r_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_s_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_s_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_s_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_h_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_h_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_h_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_m_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_m_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_m_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_o_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_o_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_o_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_seq(self, numeric):
        """
        This is the method the command: traffic_config option icmp_seq
        Description:Sequence number for each ping command, i.e. EchoRequest. Valid choices are between 0 and 65535, inclusive. Valid only for ICMPv4 when traffic_generator is 'ixos'.
        Constants Available: ICMP_SEQ_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ICMP_SEQ_CMD : numeric})

    def traffic_config_icmp_seq_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_seq_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_seq_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_seq_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_type(self, numeric):
        """
        This is the method the command: traffic_config option icmp_type
        Description:ICMP message type. Valid choices are between 0 and 255, inclusive.
        Constants Available: ICMP_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.ICMP_TYPE_CMD : numeric})

    def traffic_config_icmp_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_type_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_group_addr(self, ip):
        """
        This is the method the command: traffic_config option igmp_group_addr
        Description:IP Multicast group address of the group being joined or left. Use a list
            of values when configuring multiple Group Records on IGMPv3 Messages. In
            case of IGMPv3 Memebership Report messages, the number of addresses from
            the igmp_group_addr field must match the number of lists of addresses
            from igmp_multicast_src parameter.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_GROUP_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_GROUP_ADDR_CMD : ip})

    def traffic_config_igmp_group_count(self, range):
        """
        This is the method the command: traffic_config option igmp_group_count
        Description:Number of IGMP message to be sent. For option 'igmp_group_mode' set to
            increment or decrement, this is the address range of the IGMP message.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_GROUP_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_GROUP_COUNT_CMD : range})

    def traffic_config_igmp_group_mode(self, opt):
        """
        This is the method the command: traffic_config option igmp_group_mode
        Description:How the Group Address varies when the repeat count is greater than 1.
            Valid choices are: fixed Group IP address is the same for all
            packets.increment Group IP address increments.decrement Group IP address
            decrements.listParameter -igmp_group_addr contains a list of values.
            Each packet will use one of the values from the list.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_GROUP_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_GROUP_MODE_CMD : opt})

    def traffic_config_igmp_group_step(self):
        """
        This is the method the command: traffic_config option igmp_group_step
        Description:Step value used to modify igmp_group_addr when igmp_group_mode is incr
            or decr.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: IGMP_GROUP_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_GROUP_STEP_CMD : ""})

    def traffic_config_igmp_group_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_max_response_time(self, range):
        """
        This is the method the command: traffic_config option igmp_max_response_time
        Description:Maximum allowed time before sending a responding report in units of
            Valid only for traffic_generator ixos/ixnetwork_540 with IGMPv2 and
            IGMPv3 Membership Query messages.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_MAX_RESPONSE_TIME_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_MAX_RESPONSE_TIME_CMD : range})

    def traffic_config_igmp_max_response_time_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_max_response_time_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_max_response_time_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_max_response_time_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_msg_type(self):
        """
        This is the method the command: traffic_config option igmp_msg_type
        Description:This parameter takes priority over igmp_type parameter when igmp_version
            is 3.
            Valid options are:
            query

            Membership Query
            report

            Membership Report
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: IGMP_MSG_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_MSG_TYPE_CMD : ""})

    def traffic_config_igmp_msg_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_multicast_src(self, ip):
        """
        This is the method the command: traffic_config option igmp_multicast_src
        Description:(Only for IGMPv3 messages) A list of IPv4 source addresses for the group
            in the case of Membership Queries and a list of lists of IPv4 source
            addresses in the case of Membership Reports.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_MULTICAST_SRC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_MULTICAST_SRC_CMD : ip})

    def traffic_config_igmp_multicast_src_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_multicast_src_mode(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_multicast_src_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_multicast_src_tracking(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qqic(self, range):
        """
        This is the method the command: traffic_config option igmp_qqic
        Description:This option is only used for an IGMP v.3 group membership query. The
            querier's query interval code, expressed in second. Values from 0 to 127
            are represented exactly, values from 128 to 255 are encoded into a
            floating point number with three bits of exponent and 4 bits of
            mantissa. A value higher than 255 will be silently forced to 255.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_QQIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_QQIC_CMD : range})

    def traffic_config_igmp_qqic_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qqic_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qqic_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qqic_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qrv(self, range):
        """
        This is the method the command: traffic_config option igmp_qrv
        Description:This option is only used for an IGMP v.3 group membership queries. The
            querier's robustness value, as a value from 0 to 7.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_QRV_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_QRV_CMD : range})

    def traffic_config_igmp_qrv_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qrv_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qrv_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qrv_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_record_type(self, opt):
        """
        This is the method the command: traffic_config option igmp_record_type
        Description:The type of IGMP message to be sent. Valid choices are: mode_is_includeA
            current-state-record which indicates that the interface has a filter
            mode of INCLUDE for the specified multicast address. The Source Address
            fields in this Group Record contain the interface's source list for the
            multicast address.mode_is_excludeAs in mode_is_include, except that the
            filter mode is EXCLUDE.change_to_include_mode A filter-mode-change
            record that indicates that the interface has changed to INCLUDE filter
            mode for the specified multicast address. The Source Address fields in
            this Group Record contain the interface's new source list for the
            multicast address.change_to_exclude_modeAs in change_to_include_mode,
            except that the filter mode is EXCLUDE.allow_new_sourcesA
            source-list-change that indicates that the Source Address fields in this
            Group Record contain a list of the additional sources that the system
            wishes to hear from, for packets sent to the multicast address. If the
            change was to an INCLUDE source list, these are the addresses that were
            added to the list; otherwise these are the addresses that were deleted
            from the list.block_old_sources A source-list-change that indicates that
            the Source Address fields in this Group Record contain a list of the
            sources that the system no longer wishes to hear from, for packets sent
            to the multicast address. If the change was to an INCLUDE source list,
            these are the addresses that were deleted from the list; otherwise these
            are the addresses that were added to the list.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_RECORD_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_RECORD_TYPE_CMD : opt})

    def traffic_config_igmp_record_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_record_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_s_flag(self, bool_opt):
        """
        This is the method the command: traffic_config option igmp_s_flag
        Description:This option is only used for an IGMP v.3 group membership query. It is
            the suppress router-side processing flag. If set, receiving multicast
            routers will not send timer updates in the normal manner when a query is
            received.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_S_FLAG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_S_FLAG_CMD : bool_opt})

    def traffic_config_igmp_s_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_s_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_type(self, opt):
        """
        This is the method the command: traffic_config option igmp_type
        Description:The type of IGMP message to be sent. dvmrp - Distance-Vector Multicast
            Routing Protocol message. Not supported with traffic_generator
            ixnetwork_540 and will be silently set to membership_query.leave_group -
            An IGMPv2 message sent by client to inform the DUT of its interest to
            leave a group. Not supported with traffic_generator ixnetwork_540 for
            IGMPv1 and will be silently set to membership_query.membership_query -
            General or group specific query messages sent by the
            DUT.membership_report - Message sent by client to inform the DUT of its
            interest to join a group.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_TYPE_CMD : opt})

    def traffic_config_igmp_unused(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_unused_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_unused_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_unused_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_unused_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_valid_checksum(self, bool_opt):
        """
        This is the method the command: traffic_config option igmp_valid_checksum
        Description:If set, this causes a valid header checksum to be generated. If
            unchecked, then the one's complement of the correct checksum is generated.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_VALID_CHECKSUM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_VALID_CHECKSUM_CMD : bool_opt})

    def traffic_config_igmp_version(self, opt):
        """
        This is the method the command: traffic_config option igmp_version
        Description:Not defined
            Valid options are:
            1

            IGMPv1
            2

            IGMPv2
            3

            IGMPv3
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: IGMP_VERSION_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IGMP_VERSION_CMD : opt})

    def traffic_config_indirect(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_mask(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_more_flag(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_more_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_more_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_mask(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_integrity_signature(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_integrity_signature_offset(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inter_burst_gap(self, numeric):
        """
        This is the method the command: traffic_config option inter_burst_gap
        Description:Number of milliseconds between each burst in the loop count.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: INTER_BURST_GAP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.INTER_BURST_GAP_CMD : numeric})

    def traffic_config_inter_frame_gap(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inter_frame_gap_unit(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inter_stream_gap(self, numeric):
        """
        This is the method the command: traffic_config option inter_stream_gap
        Description:Number milliseconds between each stream configured.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: INTER_STREAM_GAP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.INTER_STREAM_GAP_CMD : numeric})

    def traffic_config_intf_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_bit_flags(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_checksum(self, checksum):
        """
        This is the method the command: traffic_config option ip_checksum
        Description:IxNetwork, IxOS/IxNetwork-FT
        Constants Available: IP_CHECKSUM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        checksum --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_CHECKSUM_CMD : checksum})

    def traffic_config_ip_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_checksum_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cost(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cost_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cost_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cu(self, num):
        """
        This is the method the command: traffic_config option ip_cu
        Description:Configures 2-bit Diff-serv currently unused field in IP header.
        Constants Available: IP_CU_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        num --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_CU_CMD : num})

    def traffic_config_ip_cu_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cu_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cu_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cu_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_delay(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_delay_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_delay_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_dscp(self, num):
        """
        This is the method the command: traffic_config option ip_dscp
        Description:and 63, inclusive.
        Constants Available: IP_DSCP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        num --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DSCP_CMD : num})

    def traffic_config_ip_dscp_count(self):
        """
        This is the method the command: traffic_config option ip_dscp_count
        Description:Numeric value which configures the number of times the ip_dscp is
            incremeneted or decremented when ip_dscp_mode is incr or decr.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: IP_DSCP_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DSCP_COUNT_CMD : ""})

    def traffic_config_ip_dscp_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_dscp_step(self):
        """
        This is the method the command: traffic_config option ip_dscp_step
        Description:Step value used to modify ip_dscp when ip_dscp_mode is incr or decr.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: IP_DSCP_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DSCP_STEP_CMD : ""})

    def traffic_config_ip_dscp_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_dst_addr(self, dip):
        """
        This is the method the command: traffic_config option ip_dst_addr
        Description:Depending on the traffic_generator value, this option has different meanings:
            ixos/ixnetwork_540: Destination IP address of the packet.
            ixnetwork: This option is used to specify the value of the first IP of the first IP static endpoint range for L2VPN traffic. (Not supported in this release.)
        Constants Available: IP_DST_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        dip --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_ADDR_CMD : dip})

    def traffic_config_ip_dst_count(self, range):
        """
        This is the method the command: traffic_config option ip_dst_count
        Description:Number of destination IP addresses when option ""ip_dst_mode"" is set to increment or decrement. When traffic_generator is ixos the maximum value is 4294967295. When traffic_generator is ixnetwork_540 the maximum value is 2147483647.
        Constants Available: IP_DST_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_COUNT_CMD : range})

    def traffic_config_ip_dst_count_step(self):
        """
        This is the method the command: traffic_config option ip_dst_count_step
        Description:This option is used to specify the step between the value of the first
            address count value of each the IP static endpoint range. It can take
            any numeric value. This option is available only when using the
            ixnetwork traffic generator for L2VPN traffic, but is not supported in
            this release.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork' |
        Constants Available: IP_DST_COUNT_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_COUNT_STEP_CMD : ""})

    def traffic_config_ip_dst_increment(self):
        """
        This is the method the command: traffic_config option ip_dst_increment
        Description:This option is used to specify the value of the increment of the first
            IP static endpoint range. It can take any numeric value in the
            1-4294967295 range. This option is available only when using the
            ixnetwork traffic generator for L2VPN traffic, but is not supported in
            this release.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork' |
        Constants Available: IP_DST_INCREMENT_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_INCREMENT_CMD : ""})

    def traffic_config_ip_dst_increment_step(self):
        """
        This is the method the command: traffic_config option ip_dst_increment_step
        Description:This option is used to specify the step between the value of the first
            address increment value of each the IP static endpoint range. It can
            take any numeric value. This option is available only when using the
            ixnetwork traffic generator for L2VPN traffic, but is not supported in
            this release.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork' |
        Constants Available: IP_DST_INCREMENT_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_INCREMENT_STEP_CMD : ""})

    def traffic_config_ip_dst_mode(self, opt):
        """
        This is the method the command: traffic_config option ip_dst_mode
        Description:Valid options are:
            fixed: The destination IP address is the same for all packets.
            increment: The destination IP address increments. Valid only for traffic_generator ixos/ixnetwork_540.
            decrement: The destination IP address decrements. Valid only for traffic_generator ixos/ixnetwork_540.
            random: The destination IP address is random. Valid only for traffic_generator ixos. With traffic_generator ixnetwork_540 this will be silently ignored and configured to 'fixed'.
            emulation: destination IP derived from the emulation handle. Valid only for traffic_generator ixos/ixnetwork_540.list Parameter -ip_src_addr contains a list of values. Each packet will use one of the values from the list. Valid only for traffic_generator ixnetwork_540.
        Constants Available: IP_DST_MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_MODE_CMD : opt})

    def traffic_config_ip_dst_prefix_len(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_dst_prefix_len_step(self):
        """
        This is the method the command: traffic_config option ip_dst_prefix_len_step
        Description:This option is used to specify the step between the value of the first
            prefix lenght of each the IP static endpoint range. It can take any an
            numeric value. This option is available only when using the ixnetwork
            traffic generator for L2VPN traffic, but is not supported in this release.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork' |
        Constants Available: IP_DST_PREFIX_LEN_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_PREFIX_LEN_STEP_CMD : ""})

    def traffic_config_ip_dst_range_step(self):
        """
        This is the method the command: traffic_config option ip_dst_range_step
        Description:This option is used to specify the step between the value of the first
            IP of each the IP static endpoint range. It can take an IP value. This
            option is available only when using the ixnetwork traffic generator for
            L2VPN traffic, but is not supported in this release.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork' |
        Constants Available: IP_DST_RANGE_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_RANGE_STEP_CMD : ""})

    def traffic_config_ip_dst_skip_broadcast(self):
        """
        This is the method the command: traffic_config option ip_dst_skip_broadcast
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IP_DST_SKIP_BROADCAST_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_SKIP_BROADCAST_CMD : ""})

    def traffic_config_ip_dst_skip_multicast(self):
        """
        This is the method the command: traffic_config option ip_dst_skip_multicast
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IP_DST_SKIP_MULTICAST_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_SKIP_MULTICAST_CMD : ""})

    def traffic_config_ip_dst_step(self, ip_mask):
        """
        This is the method the command: traffic_config option ip_dst_step
        Description:The modifier for the increment and decrement choices of -ip_dst_mode which requires that only one field contain a non-zero value. When the ip_src_mode is random, then this acts as a mask if traffic_generator is ixos.
        Constants Available: IP_DST_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip_mask --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_DST_STEP_CMD : ip_mask})

    def traffic_config_ip_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment(self, opt):
        """
        This is the method the command: traffic_config option ip_fragment
        Description:Whether this is a fragmented datagram. This option is used in conjuction with option ""ip_id"" and ""ip_fragment_last"". Valid choices are: 0This is not a fragmented datagram.1This is a fragmented datagram.
        Constants Available: IP_FRAGMENT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_FRAGMENT_CMD : opt})

    def traffic_config_ip_fragment_last(self, opt):
        """
        This is the method the command: traffic_config option ip_fragment_last
        Description:Controls whether there are additional fragments used to assemble this datagram. 0More fragments to come.1DEFAULT) No more fragments.
        Constants Available: IP_FRAGMENT_LAST_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_FRAGMENT_LAST_CMD : opt})

    def traffic_config_ip_fragment_last_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_last_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_offset(self, offset):
        """
        This is the method the command: traffic_config option ip_fragment_offset
        Description:Where in the datagram this fragment belongs. The offset is measured inclusive.
        Constants Available: IP_FRAGMENT_OFFSET_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        offset --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_FRAGMENT_OFFSET_CMD : offset})

    def traffic_config_ip_fragment_offset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_offset_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_offset_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_offset_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_hdr_length(self, len):
        """
        This is the method the command: traffic_config option ip_hdr_length
        Description:Configure header length field in IP header.
        Constants Available: IP_HDR_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        len --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_HDR_LENGTH_CMD : len})

    def traffic_config_ip_hdr_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_hdr_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_hdr_length_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_hdr_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_id(self, opt):
        """
        This is the method the command: traffic_config option ip_id
        Description:Identifying value assigned by the sender to aid in assembling the
        Constants Available: IP_ID_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_ID_CMD : opt})

    def traffic_config_ip_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_length_override(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_length_override_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_length_override_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_mbz(self):
        """
        This is the method the command: traffic_config option ip_mbz
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IP_MBZ_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_MBZ_CMD : ""})

    def traffic_config_ip_opt_loose_routing(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_opt_security(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_opt_strict_routing(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_opt_timestamp(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_precedence(self, prec):
        """
        This is the method the command: traffic_config option ip_precedence
        Description:Part of the Type of Service byte of the IP header datagram that 7, inclusive. With traffic_generator ixnetwork_540 this parameter configures QOS for IPv6 traffic only for ixaccess backwards compatibility mode (details in description for traffic_generator ixnetwork_540) and if qos_ipv6_traffic_class and ipv6_traffic_class parameters are missing.
        Constants Available: IP_PRECEDENCE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        prec --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_PRECEDENCE_CMD : prec})

    def traffic_config_ip_precedence_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_precedence_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_precedence_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_precedence_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_protocol(self, proto):
        """
        This is the method the command: traffic_config option ip_protocol
        Description:0 and 255.
        Constants Available: IP_PROTOCOL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        proto --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_PROTOCOL_CMD : proto})

    def traffic_config_ip_protocol_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_protocol_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_protocol_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_protocol_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_range_count(self):
        """
        This is the method the command: traffic_config option ip_range_count
        Description:This option is used to specify the number of IP static endpoint ranges.
            It can take any numeric value.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork' |
        Constants Available: IP_RANGE_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_RANGE_COUNT_CMD : ""})

    def traffic_config_ip_reliability(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reliability_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reliability_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reserved(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reserved_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reserved_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_src_addr(self, sip):
        """
        This is the method the command: traffic_config option ip_src_addr
        Description:Source IP address of the packet.
        Constants Available: IP_SRC_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        sip --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_SRC_ADDR_CMD : sip})

    def traffic_config_ip_src_count(self, range):
        """
        This is the method the command: traffic_config option ip_src_count
        Description:Number of source IP addresses when option ""ip_src_mode"" is set to increment or decrement. When traffic_generator is ixos the maximum value is 4294967295. When traffic_generator is ixnetwork_540 the maximum value is 2147483647.
        Constants Available: IP_SRC_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_SRC_COUNT_CMD : range})

    def traffic_config_ip_src_mode(self, opt):
        """
        This is the method the command: traffic_config option ip_src_mode
        Description:Valid options are:
            fixed: The source IP address is the same for all packets.
            increment: The source IP address increments. Valid only for traffic_generator ixos/ixnetwork_540.
            decrement: The source IP address decrements. Valid only for traffic_generator ixos/ixnetwork_540.
            random: The source IP address is random. Valid only for traffic_generator ixos. With traffic_generator ixnetwork_540 this will be silently ignored and configured to 'fixed'.
            emulation: Source IP derived from the emulation handle. Valid only for traffic_generator ixos/ixnetwork_540.list Parameter -ip_src_addr contains a list of values. Each packet will use one of the values from the list. Valid only for traffic_generator ixnetwork_540.
        Constants Available: IP_SRC_MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_SRC_MODE_CMD : opt})

    def traffic_config_ip_src_skip_broadcast(self):
        """
        This is the method the command: traffic_config option ip_src_skip_broadcast
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IP_SRC_SKIP_BROADCAST_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_SRC_SKIP_BROADCAST_CMD : ""})

    def traffic_config_ip_src_skip_multicast(self):
        """
        This is the method the command: traffic_config option ip_src_skip_multicast
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IP_SRC_SKIP_MULTICAST_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_SRC_SKIP_MULTICAST_CMD : ""})

    def traffic_config_ip_src_step(self, ip_mask):
        """
        This is the method the command: traffic_config option ip_src_step
        Description:The modifier for the increment and decrement choices of -ip_src_mode which requires that only one field contain a non-zero value. When the ip_src_mode is random, then this acts as a mask if traffic_generator is ixos.
        Constants Available: IP_SRC_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip_mask --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_SRC_STEP_CMD : ip_mask})

    def traffic_config_ip_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_throughput(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_throughput_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_throughput_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_tos_count(self):
        """
        This is the method the command: traffic_config option ip_tos_count
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IP_TOS_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_TOS_COUNT_CMD : ""})

    def traffic_config_ip_tos_field(self, opt):
        """
        This is the method the command: traffic_config option ip_tos_field
        Constants Available: IP_TOS_FIELD_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_TOS_FIELD_CMD : opt})

    def traffic_config_ip_tos_step(self):
        """
        This is the method the command: traffic_config option ip_tos_step
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IP_TOS_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_TOS_STEP_CMD : ""})

    def traffic_config_ip_total_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_total_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_total_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_total_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_total_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_ttl(self, ttl):
        """
        This is the method the command: traffic_config option ip_ttl
        Description:0 and 255.
        Constants Available: IP_TTL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ttl --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IP_TTL_CMD : ttl})

    def traffic_config_ip_ttl_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_ttl_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_ttl_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_ttl_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_checksum(self):
        """
        This is the method the command: traffic_config option ipv6_checksum
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IPV6_CHECKSUM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_CHECKSUM_CMD : ""})

    def traffic_config_ipv6_dst_addr(self, ipv6):
        """
        This is the method the command: traffic_config option ipv6_dst_addr
        Description:Destination IPv6 address of the packet.
        Constants Available: IPV6_DST_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_DST_ADDR_CMD : ipv6})

    def traffic_config_ipv6_dst_count(self, range):
        """
        This is the method the command: traffic_config option ipv6_dst_count
        Description:Number of destination IP address when option ""ipv6_dst_mode"" is set to increment or decrement. When traffic_generator is ixos the maximum value is 4294967295. When traffic_generator is ixnetwork_540 the maximum value is 2147483647.
        Constants Available: IPV6_DST_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_DST_COUNT_CMD : range})

    def traffic_config_ipv6_dst_mask(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_dst_mode(self, opt):
        """
        This is the method the command: traffic_config option ipv6_dst_mode
        Description:The following is valid only for traffic_generator ixnetwork_540:
            Valid options are:
            increment
            decrement
            fixed
            list
            For backwards compatibility all modes starting with 'incr' will be configured as increment and all modes starting with 'decr' will be configured as decrement. Incrementing and decrementing depends only on ipv6_dst_step and ipv6_dst_count.
            The following is valid only for traffic_generator ixos:
            destination IP address mode.
            ipv6_dst_mode specifies how and if the ipv6_dst_addr is incremented.
            The ipv6_dst_mode depends on the IPv6 address type specified with ipv6_dst_addr parameter.
            Each ipv6_dst_mode allows a mask from a Mask range to be configured.
            The mask is configured using the ipv6_dst_mask attribute
            The step used for incrementing or decrementing is configued using the ipv6_dst_step attribute which has the form of an IPv6 address.
            The ipv6_dst_mask attribute specifies which part of the ipv6_dst_step address is used for incrementing as follows:
            Mask range 4-4, incr_global_top_level decr_global_top_level: xxxx::0
            Mask range 24-24, incr_global_next_level decr_global_next_level: 0:0xx:xxxx::0
            Mask range 48-48, incr_global_site_level decr_global_site_level incr_local_site_subnet decr_local_site_subnet: 0:0:0:xxxx::0
            Mask range 96-96, incr_mcast_group decr_mcast_group: 0::xxxx:xxxx
            Mask range 96-128, incr_host decr_host incr_intf_id decr_intf_id: 0::xxxx:xxxx (when mask is 96)
            Mask range 96-128, incr_host decr_host incr_intf_id decr_intf_id: 0::xxxx (when mask is 112)
            Mask range 0-128, incr_network decr_network: 0::xxxx:xxxx:0:0 (when mask is 96)
            Mask range 0-128, incr_network decr_network: 0::xxxx:xxxx:0 (when mask is 112)
            HEX values marked with 'x' in the format above are the ipv6_dst_step HEX values that are used for increment or decrement; HEX values marked with '0' are ignored.
            Valid options are:
            type
            User Defined
            address
            Mask range 0-128
            value
            Mask range 0-128
            Reserved
            Allocation
            Addresses
            ID
            Mask range 96-128
        Constants Available: IPV6_DST_MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_DST_MODE_CMD : opt})

    def traffic_config_ipv6_dst_step(self, ipv6):
        """
        This is the method the command: traffic_config option ipv6_dst_step
        Description:Step size of the destination IP address. ipv6_dst_mode specifies how and if the ipv6_dst_addr is incremented.
            The following is valid only for traffic_generator ixnetwork_540:
            Any IPv6 step is accepted. Incrementing and decrementing depends only on ipv6_dst_step and ipv6_dst_count.
            The following is valid only for traffic_generator ixos:
            The ipv6_dst_mode depends on the IPv6 address type specified with ipv6_dst_addr parameter.
            Each ipv6_dst_mode allows a mask from a Mask range to be configured. The mask is configured using the ipv6_dst_mask attribute.
            The step used for incrementing or decrementing is configued using the ipv6_dst_step attribute which has the form of an IPv6 address.
            The ipv6_dst_mask attribute specifies which part of the ipv6_dst_step address is used for incrementing as follows:Mask range 4-4, incr_global_top_level decr_global_top_level: xxxx::0Mask range 24-24, incr_global_next_level decr_global_next_level: 0:0xx:xxxx::0Mask range 48-48, incr_global_site_level decr_global_site_level incr_local_site_subnet decr_local_site_subnet: 0:0:0:xxxx::0Mask range 96-96, incr_mcast_group decr_mcast_group: 0::xxxx:xxxxMask range 96-128, incr_host decr_host incr_intf_id decr_intf_id: 0::xxxx:xxxx (when mask is 96)Mask range 96-128, incr_host decr_host incr_intf_id decr_intf_id: 0::xxxx (when mask is 112)Mask range 0-128, incr_network decr_network: 0::xxxx:xxxx:0:0 (when mask is 96)Mask range 0-128, incr_network decr_network: 0::xxxx:xxxx:0 (when mask is 112)HEX values marked with 'x' in the format above are the ipv6_dst_step HEX values that are used for increment or decrement; HEX values marked with '0' are ignored.
        Constants Available: IPV6_DST_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_DST_STEP_CMD : ipv6})

    def traffic_config_ipv6_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_extension_header(self, header):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_label(self, numeric):
        """
        This is the method the command: traffic_config option ipv6_flow_label
        Description:Flow label value of the IPv6 stream.
        Constants Available: IPV6_FLOW_LABEL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_FLOW_LABEL_CMD : numeric})

    def traffic_config_ipv6_flow_label_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_label_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_label_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_label_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_id(self, numeric):
        """
        This is the method the command: traffic_config option ipv6_frag_id
        Description:This can be used in two ways. If ""-ipv6_extension_header fragment"" is present then an IPv6 extension frament is added along with other IPv6 extension headers mentioned in ipv6_extension_header list. Also these option can be a list. If -ipv6_extension_header is not present then only one IPv6 fragment can be added and these option can only have one element. Identification field in the fragment extension header of an IPv6 stream.
        Constants Available: IPV6_FRAG_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_FRAG_ID_CMD : numeric})

    def traffic_config_ipv6_frag_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_more_flag(self, opt):
        """
        This is the method the command: traffic_config option ipv6_frag_more_flag
        Description:This can be used in two ways. If ""-ipv6_extension_header fragment"" is present then an IPv6 extension frament is added along with other IPv6 extension headers mentioned in -ipv6_extension_header list. Also these option can be a list. If -ipv6_extension_header is not present then only one IPv6 fragment can be added and these option can only have one element. Whether the M Flag in the fragment extension header of an IPv6 stream is set.
        Constants Available: IPV6_FRAG_MORE_FLAG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_FRAG_MORE_FLAG_CMD : opt})

    def traffic_config_ipv6_frag_more_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_more_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_next_header(self):
        """
        This is the method the command: traffic_config option ipv6_frag_next_header
        Description:Next header in the fragmentation extention header.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IPV6_FRAG_NEXT_HEADER_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_FRAG_NEXT_HEADER_CMD : ""})

    def traffic_config_ipv6_frag_offset(self, numeric):
        """
        This is the method the command: traffic_config option ipv6_frag_offset
        Description:This can be used in two ways. If ""-ipv6_extension_header fragment"" is present then an IPv6 extension frament is added along with other IPv6 extension headers mentioned in -ipv6_extension_header list. Also these option can be a list. If -ipv6_extension_header is not present then only one IPv6 fragment can be added and these option can only have one element. Whether the M Flag in the fragment extension header of an IPv6 stream is set.
        Constants Available: IPV6_FRAG_OFFSET_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_FRAG_OFFSET_CMD : numeric})

    def traffic_config_ipv6_frag_offset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_offset_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_offset_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_offset_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_by_hop_options(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_limit(self, hop_limit):
        """
        This is the method the command: traffic_config option ipv6_hop_limit
        Description:Hop limit value of the IPv6 stream.
        Constants Available: IPV6_HOP_LIMIT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        hop_limit --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_HOP_LIMIT_CMD : hop_limit})

    def traffic_config_ipv6_hop_limit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_limit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_limit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_limit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_length(self):
        """
        This is the method the command: traffic_config option ipv6_length
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: IPV6_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_LENGTH_CMD : ""})

    def traffic_config_ipv6_next_header(self, range):
        """
        This is the method the command: traffic_config option ipv6_next_header
        Description:Configures the 1-byte next header field in the IPv6 header.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: IPV6_NEXT_HEADER_CMD
        Supported:IxNetwork
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_NEXT_HEADER_CMD : range})

    def traffic_config_ipv6_next_header_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_next_header_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_next_header_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_next_header_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_node_list(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_src_addr(self, ipv6):
        """
        This is the method the command: traffic_config option ipv6_src_addr
        Description:Source IPv6 address of the packet.
        Constants Available: IPV6_SRC_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_SRC_ADDR_CMD : ipv6})

    def traffic_config_ipv6_src_count(self, range):
        """
        This is the method the command: traffic_config option ipv6_src_count
        Description:Number of source IP address when option ""ipv6_src_mode"" is set to increment or decrement. When traffic_generator is ixos the maximum value is 4294967295. When traffic_generator is ixnetwork_540 the maximum value is 2147483647.
        Constants Available: IPV6_SRC_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_SRC_COUNT_CMD : range})

    def traffic_config_ipv6_src_mask(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_src_mode(self, opt):
        """
        This is the method the command: traffic_config option ipv6_src_mode
        Description:The following is valid only for traffic_generator ixnetwork_540:
            Valid options are:
            increment
            decrement
            fixed
            list
            For backwards compatibility all modes starting with 'incr' will be configured as increment and all modes starting with 'decr' will be configured as decrement. Incrementing and decrementing depends only on ipv6_src_step and ipv6_src_count.
            The following is valid only for traffic_generator ixos:
            Source IP address mode.
            ipv6_src_mode specifies how and if the ipv6_src_addr is incremented.
            The ipv6_src_mode depends on the IPv6 address type specified with ipv6_src_addr parameter.
            Each ipv6_src_mode allows a mask from a Mask range to be configured.
            The mask is configured using the ipv6_src_mask attribute
            The step used for incrementing or decrementing is configued using the ipv6_src_step attribute which has the form of an IPv6 address.
            The ipv6_src_mask attribute specifies which part of the ipv6_src_step address is used for incrementing as follows:
            Mask range 4-4, incr_global_top_level decr_global_top_level: xxxx::0
            Mask range 24-24, incr_global_next_level decr_global_next_level: 0:0xx:xxxx::0
            Mask range 48-48, incr_global_site_level decr_global_site_level incr_local_site_subnet decr_local_site_subnet: 0:0:0:xxxx::0
            Mask range 96-96, incr_mcast_group decr_mcast_group: 0::xxxx:xxxx
            Mask range 96-128, incr_host decr_host incr_intf_id decr_intf_id: 0::xxxx:xxxx (when mask is 96)
            Mask range 96-128, incr_host decr_host incr_intf_id decr_intf_id: 0::xxxx (when mask is 112)
            Mask range 0-128, incr_network decr_network: 0::xxxx:xxxx:0:0 (when mask is 96)
            Mask range 0-128, incr_network decr_network: 0::xxxx:xxxx:0 (when mask is 112)
            HEX values marked with 'x' in the format above are the ipv6_src_step HEX values that are used for increment or decrement; HEX values marked with '0' are ignored.
            Valid options are:
            type
            User Defined
            address
            Mask range 0-128
            value
            Mask range 0-128
            Reserved
            Allocation
            Addresses
            ID
            Mask range 96-128
        Constants Available: IPV6_SRC_MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_SRC_MODE_CMD : opt})

    def traffic_config_ipv6_src_step(self, ipv6):
        """
        This is the method the command: traffic_config option ipv6_src_step
        Description:Step size of the source IP address. ipv6_src_mode specifies how and if the ipv6_src_addr is incremented.
            The following is valid only for traffic_generator ixnetwork_540:
            Any IPv6 step is accepted. Incrementing and decrementing depends only on ipv6_src_step and ipv6_src_count.
            The following is valid only for traffic_generator ixos:
            The ipv6_src_mode depends on the IPv6 address type specified with ipv6_src_addr parameter.
            Each ipv6_src_mode allows a mask from a Mask range to be configured. The mask is configured using the ipv6_src_mask attribute.
            The step used for incrementing or decrementing is configued using the ipv6_src_step attribute which has the form of an IPv6 address.
            The ipv6_src_mask attribute specifies which part of the ipv6_src_step address is used for incrementing as follows:Mask range 4-4, incr_global_top_level decr_global_top_level: xxxx::0Mask range 24-24, incr_global_next_level decr_global_next_level: 0:0xx:xxxx::0Mask range 48-48, incr_global_site_level decr_global_site_level incr_local_site_subnet decr_local_site_subnet: 0:0:0:xxxx::0Mask range 96-96, incr_mcast_group decr_mcast_group: 0::xxxx:xxxxMask range 96-128, incr_host decr_host incr_intf_id decr_intf_id: 0::xxxx:xxxx (when mask is 96)Mask range 96-128, incr_host decr_host incr_intf_id decr_intf_id: 0::xxxx (when mask is 112)Mask range 0-128, incr_network decr_network: 0::xxxx:xxxx:0:0 (when mask is 96)Mask range 0-128, incr_network decr_network: 0::xxxx:xxxx:0 (when mask is 112)HEX values marked with 'x' in the format above are the ipv6_src_step HEX values that are used for increment or decrement; HEX values marked with '0' are ignored.
        Constants Available: IPV6_SRC_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_SRC_STEP_CMD : ipv6})

    def traffic_config_ipv6_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_traffic_class(self, traffic_class):
        """
        This is the method the command: traffic_config option ipv6_traffic_class
        Description:Traffic class value of the IPv6 stream.
        Constants Available: IPV6_TRAFFIC_CLASS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        traffic_class --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.IPV6_TRAFFIC_CLASS_CMD : traffic_class})

    def traffic_config_ipv6_traffic_class_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_traffic_class_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_traffic_class_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_traffic_class_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu_step(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_frame_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_frame_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_frame_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_l2_encap(self, opt):
        """
        This is the method the command: traffic_config option l2_encap
        Description:Set level 2 encapsulation. Valid only for traffic_generator ixos and
            ixnetwork_540. Valid options with traffic_generator ixos are:
            atm_vc_mux
            atm_vc_mux_ethernet_ii
            atm_vc_mux_802.3snap
            atm_vc_mux_802.3snap_nofcs
            atm_vc_mux_ppp
            atm_vc_mux_pppoe
            atm_snap
            atm_snap_ethernet_ii
            atm_snap_802.3snap
            atm_snap_802.3snap_nofcs
            atm_snap_ppp
            atm_snap_pppoe
            hdlc_unicast
            hdlc_broadcast
            hdlc_unicast_mpls
            hdlc_multicast_mpls
            ethernet_ii
            ethernet_ii_unicast_mpls
            ethernet_ii_multicast_mpls
            ethernet_ii_vlan
            ethernet_ii_vlan_unicast_mpls
            ethernet_ii_vlan_multicast_mpls12
            ethernet_ii_pppoe
            ethernet_ii_vlan_pppoe
            ppp_link
            ietf_framerelay
            cisco_framerelay
            Valid options with traffic_generator ixnetwork_540 are:
            ethernet_ii
            ethernet_ii_unicast_mpls
            ethernet_ii_vlaneth
            ernet_ii_vlan_unicast_mpls
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L2_ENCAP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L2_ENCAP_CMD : opt})

    def traffic_config_l3_gaus1_avg(self, decimaldecimal):
        """
        This is the method the command: traffic_config option l3_gaus1_avg
        Description:The center of the first curve. Used if length_mode is set to gaussian or
            quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS1_AVG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        decimaldecimal --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS1_AVG_CMD : decimaldecimal})

    def traffic_config_l3_gaus1_halfbw(self, decimaldecimal):
        """
        This is the method the command: traffic_config option l3_gaus1_halfbw
        Description:The width at half of the first curve. Used if length_mode is set to
            gaussian or quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS1_HALFBW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        decimaldecimal --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS1_HALFBW_CMD : decimaldecimal})

    def traffic_config_l3_gaus1_weight(self, numeric):
        """
        This is the method the command: traffic_config option l3_gaus1_weight
        Description:The weigth of the first curve. Used if length_mode is set to gaussian or
            quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS1_WEIGHT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS1_WEIGHT_CMD : numeric})

    def traffic_config_l3_gaus2_avg(self, decimaldecimal):
        """
        This is the method the command: traffic_config option l3_gaus2_avg
        Description:The center of the second curve. Used if length_mode is set to gaussian
            or quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS2_AVG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        decimaldecimal --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS2_AVG_CMD : decimaldecimal})

    def traffic_config_l3_gaus2_halfbw(self, decimaldecimal):
        """
        This is the method the command: traffic_config option l3_gaus2_halfbw
        Description:The width at half of the second curve. Used if length_mode is set to
            gaussian or quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS2_HALFBW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        decimaldecimal --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS2_HALFBW_CMD : decimaldecimal})

    def traffic_config_l3_gaus2_weight(self, numeric):
        """
        This is the method the command: traffic_config option l3_gaus2_weight
        Description:The weigth of the second curve. Used if length_mode is set to gaussian
            or quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS2_WEIGHT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS2_WEIGHT_CMD : numeric})

    def traffic_config_l3_gaus3_avg(self, decimaldecimal):
        """
        This is the method the command: traffic_config option l3_gaus3_avg
        Description:The center of the third curve. Used if length_mode is set to gaussian or
            quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS3_AVG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        decimaldecimal --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS3_AVG_CMD : decimaldecimal})

    def traffic_config_l3_gaus3_halfbw(self, decimaldecimal):
        """
        This is the method the command: traffic_config option l3_gaus3_halfbw
        Description:The width at half of the third curve. Used if length_mode is set to
            gaussian or quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS3_HALFBW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        decimaldecimal --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS3_HALFBW_CMD : decimaldecimal})

    def traffic_config_l3_gaus3_weight(self, numeric):
        """
        This is the method the command: traffic_config option l3_gaus3_weight
        Description:The weigth of the third curve. Used if length_mode is set to gaussian or
            quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS3_WEIGHT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS3_WEIGHT_CMD : numeric})

    def traffic_config_l3_gaus4_avg(self, decimaldecimal):
        """
        This is the method the command: traffic_config option l3_gaus4_avg
        Description:The center of the fourth curve. Used if length_mode is set to gaussian
            or quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS4_AVG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        decimaldecimal --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS4_AVG_CMD : decimaldecimal})

    def traffic_config_l3_gaus4_halfbw(self, decimaldecimal):
        """
        This is the method the command: traffic_config option l3_gaus4_halfbw
        Description:The width at half of the fourth curve. Used if length_mode is set to
            gaussian or quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS4_HALFBW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        decimaldecimal --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS4_HALFBW_CMD : decimaldecimal})

    def traffic_config_l3_gaus4_weight(self, numeric):
        """
        This is the method the command: traffic_config option l3_gaus4_weight
        Description:The weigth of the fourth curve. Used if length_mode is set to gaussian
            or quad.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_GAUS4_WEIGHT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_GAUS4_WEIGHT_CMD : numeric})

    def traffic_config_l3_imix1_ratio(self, range):
        """
        This is the method the command: traffic_config option l3_imix1_ratio
        Description:Ratio of first packet size. Used if length_mode set to imix.The sum of
            all ratio (l3_imix1_ratio, l3_imix2_ratio, l3_imix3_ratio,
            l3_imix4_ratio) must be between 0 and 262,144.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_IMIX1_RATIO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_IMIX1_RATIO_CMD : range})

    def traffic_config_l3_imix1_size(self, range):
        """
        This is the method the command: traffic_config option l3_imix1_size
        Description:First Packet size in bytes. Used if length_mode set to imix.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_IMIX1_SIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_IMIX1_SIZE_CMD : range})

    def traffic_config_l3_imix2_ratio(self, range):
        """
        This is the method the command: traffic_config option l3_imix2_ratio
        Description:Ratio of second packet size. Used if length_mode set to imix.The sum of
            all ratio (l3_imix1_ratio, l3_imix2_ratio, l3_imix3_ratio,
            l3_imix4_ratio) must be between 0 and 262,144.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_IMIX2_RATIO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_IMIX2_RATIO_CMD : range})

    def traffic_config_l3_imix2_size(self, range):
        """
        This is the method the command: traffic_config option l3_imix2_size
        Description:Second Packet size in bytes. Used if length_mode set to imix.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_IMIX2_SIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_IMIX2_SIZE_CMD : range})

    def traffic_config_l3_imix3_ratio(self, range):
        """
        This is the method the command: traffic_config option l3_imix3_ratio
        Description:Ratio of third packet size. Used if length_mode set to imix.The sum of
            all ratio (l3_imix1_ratio, l3_imix2_ratio, l3_imix3_ratio,
            l3_imix4_ratio) must be between 0 and 262,144.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_IMIX3_RATIO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_IMIX3_RATIO_CMD : range})

    def traffic_config_l3_imix3_size(self, range):
        """
        This is the method the command: traffic_config option l3_imix3_size
        Description:Third Packet size in bytes. Used if length_mode set to imix.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_IMIX3_SIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_IMIX3_SIZE_CMD : range})

    def traffic_config_l3_imix4_ratio(self, range):
        """
        This is the method the command: traffic_config option l3_imix4_ratio
        Description:Ratio of fourth packet size. Used if length_mode set to imix.The sum of
            all ratio (l3_imix1_ratio, l3_imix2_ratio, l3_imix3_ratio,
            l3_imix4_ratio) must be between 0 and 262,144.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_IMIX4_RATIO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_IMIX4_RATIO_CMD : range})

    def traffic_config_l3_imix4_size(self, range):
        """
        This is the method the command: traffic_config option l3_imix4_size
        Description:Fourth Packet size in bytes. Used if length_mode set to imix.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_IMIX4_SIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_IMIX4_SIZE_CMD : range})

    def traffic_config_l3_length(self, range):
        """
        This is the method the command: traffic_config option l3_length
        Description:Packet size in bytes. Use this option in conjunction with option
            inclusive. If frame_size parameter is used, this option is ignored.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_LENGTH_CMD : range})

    def traffic_config_l3_length_max(self, range):
        """
        This is the method the command: traffic_config option l3_length_max
        Description:Maximum packet size for the specified stream in bytes. Use this option
            in conjunction with option 'length_mode' set to increment.If
            frame_size_max parameter is used, this option is ignored.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_LENGTH_MAX_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_LENGTH_MAX_CMD : range})

    def traffic_config_l3_length_min(self, range):
        """
        This is the method the command: traffic_config option l3_length_min
        Description:Minimum packet size for the specified stream in bytes. Use this option
            in conjunction with option 'length_mode' set to increment.If
            frame_size_min parameter is used, this option is ignored.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: L3_LENGTH_MIN_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_LENGTH_MIN_CMD : range})

    def traffic_config_l3_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_l3_protocol(self, proto):
        """
        This is the method the command: traffic_config option l3_protocol
        Description:Configures a layer 3 protocol header. Depending on the traffic_generator ixos - ipv4, ipv6, arp, pause_control, ipx, noneixnetwork (not supported in this release) - ipv4, ipv6ixnetwork_540 - ipv4, ipv6, arp
        Constants Available: L3_PROTOCOL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        proto --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L3_PROTOCOL_CMD : proto})

    def traffic_config_l4_protocol(self, opt):
        """
        This is the method the command: traffic_config option l4_protocol
        Description:In the Layer4 header in the IP-based packet, the Layer4 protocol. l4_protocol parameter should be added in mode create or modify for l4 parameters to be considered. If -mode is modify and traffic_generator is ixnetwork_540, it is only possible to modify headers that already exist in the packet.To replace the entire l4 header one must use traffic_config -mode replace_header. Valid options are:
            Valid options are:
            gre: For IPv4 and IPv6 (IxNetwork and IxOS).
            icmp: For IPv4 and IPv6 (IxNetwork). For IxOS, only the IPv4 stack is valid.
            igmp: For IPv4 and IPv6 (IxNetwork). For IxOS, only the IPv4 stack is valid.
            tcp: For IPv4 and IPv6 (IxNetwork and IxOS).
            udp: For IPv4 and IPv6 (IxNetwork and IxOS).
            rip: For IPv4 and IPv6 (IxNetwork). For IxOS, only the IPv4 stack is valid.
            dhcp: For IPv4 and IPv6 (IxNetwork). For IxOS, only the IPv4 stack is valid.
            ospf: For IPv4 and IPv6 (IxNetwork). For IxOS, only the IPv4 stack is valid.
            ip: For IPv4 and IPv6 (IxNetwork). For IxOS, only the IPv4 stack is valid.
        Constants Available: L4_PROTOCOL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.L4_PROTOCOL_CMD : opt})

    def traffic_config_lan_range_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_latency_bins(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_latency_bins_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_latency_values(self, decimal):
        return self.logger.log_unimplemented_method()

    def traffic_config_length_mode(self, opt):
        """
        This is the method the command: traffic_config option length_mode
        Description:This parameter can be updated while the traffic is running with -mode
            'dynamic_update' and -stream_id . The choices that are supported for
            dynamic_update are 'fixed' and 'random'. Behavior of the frame/packet
            size for a particular stream. Parameters l3_length* are ignored when
            frame_size* parameters are used.fixed - The frame/packet size is fixed.
            Dependencies: l3_length/frame_size when traffic_generator is set to ixos
            and ixnetwork_540, and only through parameter frame_size when
            traffic_generator is set to ixnetwork. PPPoX with traffic_generator
            ixnetwork supports only -length_mode fixed. increment - The frame/packet
            size will be incremented using a step from a minimum size to a maximum
            size. Dependencies: The incrementing step and minimum/maximum
            framesize/packet size must be specified using:
            l3_length_step/frame_size_step, l3_length_min/frame_size_min,
            l3_length_max/frame_size_max when traffic_generator is set to ixos and
            ixnetwork_540, and only through parameters frame_size_step,
            frame_size_min, frame_size_max when traffic_generator is set to
            ixnetwork.random - The frame/packet size is random, but limited by a
            minimum and maximum value. Dependencies: The minimum and maximum
            framesize/packet size must be specified using:
            l3_length_min/frame_size_min, l3_length_max/frame_size_max when
            traffic_generator is set to ixos and ixnetwork_540, and only through
            parameters frame_size_min, frame_size_max when traffic_generator is set
            to ixnetwork.auto - The frame/packet size is set automatically in order
            to have a valid frame, without overlapping headers and fields.
            Dependencies: This choice is valid only when traffic_generator is set to
            ixos and ixnetwork_540.imix - Mix of frame/packet sizes are generated
            during transmission. Dependencies: Imix settings must be specified using
            parameters:traffic_generator ixos - l3_imix/_size, l3_imix/_ratio(/is
            from 1 to 4).traffic generator is ixnetwork_540 - l3_imix/_size,
            l3_imix/_ratio(/is from 1 to 4) or frame_size_imix. Parameter
            frame_size_imix has priority over l3_imix* parameters.traffic generator
            is ixnetwork - Imix settings must be specified using parameter
            frame_size_imix.gaussian, quad - Frame/packet sizes are specified as
            gaussian/quad curves. Dependencies: traffic_generator ixos - these
            curves must be specified using options l3_gaus/_avg, l3_gaus/_halfbw,
            l3_gaus/_weight, where /is a number from 1 to 4. traffic_generator
            ixnetwork - these curves must be specified using option
            frame_size_gauss.traffic_generator ixnetwork_540 - these curves must be
            specified using options l3_gaus/_avg, l3_gaus/_halfbw, l3_gaus/_weight,
            where /is a number from 1 to 4 OR frame_size_gauss. Parameter
            frame_size_gauss has priority over l3_gaus* parameters.distribution -
            Frame size is specified with a predefined distribution. Dependencies:
            For IxTclNetwork, this choice is valid only when traffic_generator is
            set to ixnetwork/ixnetwork_540 and the distribution must be set using
            option frame_size_distribution.//////////////
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: LENGTH_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.LENGTH_MODE_CMD : opt})

    def traffic_config_loop_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_mac_discovery_gw(self):
        """
        This is the method the command: traffic_config option mac_discovery_gw
        Description:Default for -mac_dst_mode discovery is to use the interface gateway.
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: MAC_DISCOVERY_GW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DISCOVERY_GW_CMD : ""})

    def traffic_config_mac_dst(self, mac_address):
        """
        This is the method the command: traffic_config option mac_dst
        Description:Destination MAC address for a particular stream. For traffic_generator ixnetwork, can only be used for L2VPN traffic, but is not supported in this release. Valid formats are:11:11:11:11:11:112222.2222.2222{33 33 33 33 33 33}
        Constants Available: MAC_DST_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac_address --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST_CMD : mac_address})

    def traffic_config_mac_dst2(self, mac):
        """
        This is the method the command: traffic_config option mac_dst2
        Description:Value of the destination MAC address for port_handle2. This option
            applies to bidirectional only. Valid MAC formats
            are:11:11:11:11:11:112222.2222.2222{33 33 33 33 33 33 }
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos' |
        Constants Available: MAC_DST2_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST2_CMD : mac})

    def traffic_config_mac_dst2_count(self):
        """
        This is the method the command: traffic_config option mac_dst2_count
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: MAC_DST2_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST2_COUNT_CMD : ""})

    def traffic_config_mac_dst2_mode(self):
        """
        This is the method the command: traffic_config option mac_dst2_mode
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: MAC_DST2_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST2_MODE_CMD : ""})

    def traffic_config_mac_dst2_step(self):
        """
        This is the method the command: traffic_config option mac_dst2_step
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: MAC_DST2_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST2_STEP_CMD : ""})

    def traffic_config_mac_dst_count(self, numeric):
        """
        This is the method the command: traffic_config option mac_dst_count
        Description:Depending on the traffic_generator value, this option has different ixos - Number of destination MAC addresses used in a particular stream. ixnetwork_540 - Number of destination MAC addresses used in a particular stream. ixnetwork - MAC address count in the first LAN static endpoint range. It can take decimal values in the 1-4294967295 range. Also, it can be used just for L2VPN traffic, but is not supported in this release.
        Constants Available: MAC_DST_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST_COUNT_CMD : numeric})

    def traffic_config_mac_dst_count_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_mac_dst_mask(self):
        """
        This is the method the command: traffic_config option mac_dst_mask
        Description:Select this attribute to use random mask bit values. This parameter is available only when -mac_dst_mode is repeatable_random.
        Constants Available: MAC_DST_MASK_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST_MASK_CMD : ""})

    def traffic_config_mac_dst_mode(self, opt):
        """
        This is the method the command: traffic_config option mac_dst_mode
        Description:Behavior of the destination MAC address for a particular stream. For traffic_generator ixnetwork, this option can only be used for L2VPN traffic, but is not supported in this release. For traffic_generator ixnetwork_540 will have the same behavior. Valid options are:
            Valid options are:
            fixed: The destination MAC will be idle (same for all packets). Valid only for all values of traffic_generator.
            increment: The Destination MAC will increment for all packets. Valid only for all values of traffic_generator.
            decrement: The Destination MAC will be decrement for all packets. Valid only for traffic_generator ixos and ixnetwork_540.
            random: The Destination MAC will be random far all packets. Valid only for traffic_generator ixos.
            discovery: The Destination MAC will match the MAC address received from the ARP request. Valid only for traffic_generator ixos.
            list: Parameter -mac_dst contains a list of values. The Destination MAC will be selected in order from the list passed with -mac_dst. Valid only for traffic_generator ixnetwork_540.
            repeatable_random: The Source MAC will be random for all packets, but you can use mac_dst_mask, mac_dst_seed and mac_dst_count.
        Constants Available: MAC_DST_MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST_MODE_CMD : opt})

    def traffic_config_mac_dst_seed(self, numeric):
        """
        This is the method the command: traffic_config option mac_dst_seed
        Description:Value for setting the seed attribute. This parameter is available only when -mac_dst_mode is repeatable_random.
        Constants Available: MAC_DST_SEED_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST_SEED_CMD : numeric})

    def traffic_config_mac_dst_step(self, mac):
        """
        This is the method the command: traffic_config option mac_dst_step
        Description:Value by which the destination MAC Address is incremented.For traffic_generator ixnetwork, this option is used to specify the step between the value of the first MAC address of each the LAN static endpoint range and can only be used for L2VPN traffic, but is not supported in this release.For traffic_generator ixos the value for this parameter can also be given as apositive integer number. For example, the values 1 and 00:00:00:00:00:01 areequivalent.
        Constants Available: MAC_DST_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_DST_STEP_CMD : mac})

    def traffic_config_mac_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mac_src(self, mac_address):
        """
        This is the method the command: traffic_config option mac_src
        Description:Source MAC address for a particular stream. Valid formats are:11:11:11:11:11:112222.2222.2222{33 33 33 33 33 33}
        Constants Available: MAC_SRC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mac_address --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC_CMD : mac_address})

    def traffic_config_mac_src2(self, mac):
        """
        This is the method the command: traffic_config option mac_src2
        Description:Value of the source MAC address for port_handle2. This option applies to
            bidirectional only. Valid MAC formats
            are:11:11:11:11:11:112222.2222.2222{33 33 33 33 33 33 }
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos' |
        Constants Available: MAC_SRC2_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC2_CMD : mac})

    def traffic_config_mac_src2_count(self):
        """
        This is the method the command: traffic_config option mac_src2_count
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: MAC_SRC2_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC2_COUNT_CMD : ""})

    def traffic_config_mac_src2_mode(self):
        """
        This is the method the command: traffic_config option mac_src2_mode
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: MAC_SRC2_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC2_MODE_CMD : ""})

    def traffic_config_mac_src2_step(self):
        """
        This is the method the command: traffic_config option mac_src2_step
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: MAC_SRC2_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC2_STEP_CMD : ""})

    def traffic_config_mac_src_count(self, numeric):
        """
        This is the method the command: traffic_config option mac_src_count
        Description:Depending on the traffic_generator value, this option has different ixos - Number of destination MAC addresses used in a particular stream. ixnetwork_540 - Number of destination MAC addresses used in a particular stream. ixnetwork - MAC address count in the first LAN static endpoint range. It can take decimal values in the 1-4294967295 range. Also, it can be used just for L2VPN traffic, but is not supported in this release.
        Constants Available: MAC_SRC_COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC_COUNT_CMD : numeric})

    def traffic_config_mac_src_mask(self):
        """
        This is the method the command: traffic_config option mac_src_mask
        Description:Select this attribute to use random mask bit values. This parameter is available only when -mac_src_mode is repeatable_random.
        Constants Available: MAC_SRC_MASK_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC_MASK_CMD : ""})

    def traffic_config_mac_src_mode(self, opt):
        """
        This is the method the command: traffic_config option mac_src_mode
        Description:Behavior of the destination MAC address for a particular stream. For traffic_generator ixnetwork, this option can only be used for L2VPN traffic, but is not supported in this release. For traffic_generator ixnetwork_540 will have the same behavior. Valid options are:
            Valid options are:
            fixed: The source MAC will be idle (same for all packets). Valid only for all values of traffic_generator.
            increment: The Source MAC will increment for all packets. Valid only for all values of traffic_generator.
            decrement: The Source MAC will be decrement for all packets. Valid only for traffic_generator ixos and ixnetwork_540.
            random: The Source MAC will be random far all packets. Valid only for traffic_generator ixos.
            discovery: The Source MAC will match the MAC address received from the ARP request. Valid only for traffic_generator ixos.
            list: Parameter -mac_dst contains a list of values. The Source MAC will be selected in order from the list passed with -mac_dst. Valid only for traffic_generator ixnetwork_540.
            repeatable_random: The Source MAC will be random for all packets, but you can use mac_src_mask, mac_src_seed and mac_src_count.
        Constants Available: MAC_SRC_MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC_MODE_CMD : opt})

    def traffic_config_mac_src_seed(self, numeric):
        """
        This is the method the command: traffic_config option mac_src_seed
        Description:Value for setting the seed attribute. This parameter is available only when -mac_src_mode is repeatable_random.
        Constants Available: MAC_SRC_SEED_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC_SEED_CMD : numeric})

    def traffic_config_mac_src_step(self, mac):
        """
        This is the method the command: traffic_config option mac_src_step
        Description:Value by which the source MAC Address is incremented.For traffic_generator ixnetwork, this option is used to specify the step between the value of the first MAC address of each the LAN static endpoint range and can only be used for L2VPN traffic, but is not supported in this release.For traffic_generator ixos the value for this parameter can also be given as apositive integer number. For example, the values 1 and 00:00:00:00:00:01 areequivalent.
        Constants Available: MAC_SRC_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MAC_SRC_STEP_CMD : mac})

    def traffic_config_mac_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_merge_destinations(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_min_gap_bytes(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mode(self, proto):
        """
        This is the method the command: traffic_config option mode
        Description:create Create only one stream/traffic item. Dependencies: When traffic_generator is ixos, the port_handle must also be provided when mode is create. modify Modify only one existing stream/traffic item. Dependencies: traffic_generator must be ixos/ixnetwork/ixnetwork_540 and stream_id must be provided. NOTE: modify mode is not supported for streams originating in PPPoX endpoints when -traffic_generator is ixos. When traffic_generator ixnetwork_540 is used stream_id can also be a header handle. remove Remove/disable an existing stream/traffic item. Dependencies: traffic_generator must be ixos/ixnetwork/ixnetwork_540 and stream_id must be provided. When traffic_generator is ixos, it disables the stream, when traffic_generator is ixnetwork it removes the traffic item. When traffic_generator is ixnetwork_540: if stream_id is a traffic_item it removes it; if stream_id is a high level stream it suspends it; if stream_id is a header handle it removes it. reset Remove all existing traffic setups. enable Enables an existing stream. Dependencies: traffic_generator must be ixos/ixnetwork/ixnetwork_540 and stream_id must be provided. disable Disables an existing stream/traffic item. Dependencies: traffic_generator must be ixnetwork/ixnetwork_540 and stream_id must be provided. append_header Append headers. Dependencies: traffic_generator must be ixnetwork_540 and stream_id must be a header handle. prepend_header Prepend headers. Dependencies: traffic_generator must be ixnetwork_540 and stream_id must be a header handle. replace_header Replace a header. Dependencies: traffic_generator must be ixnetwork_540 and stream_id must be a header handle. modify_or_insert modifies or inserts a header, using the -stack_index parameter. dynamic_update With traffic_generator 'ixnetwork_540' some rate and framesize parameters can be changed while the traffic is running. To do this use -mode 'dynamic_update' and -stream_id . The parameters that will be used for this mode are: frame_size, frame_size_max, frame_size_min, length_mode (only fixed or random), rate_bps, rate_kbps, rate_mbps, rate_byteps, rate_kbyteps, rate_mbyteps, rate_percent, rate_pps, inter_frame_gap, inter_frame_gap_unit and enforce_min_gap. Any other parameters will be silently ignored. Dependencies: traffic_generator must be ixnetwork_540 and stream_id must be a traffic item handle. get_available_protocol_templates Returns a list of all available protocol templates in a user-friendly format. The elements from the list (or the entire list) can be used as pt_handle object(s). Returns key ""pt_handle"". Dependencies: traffic_generator must be ixnetwork_540. get_available_fields Returns a list of all available fields specific to the provided header handle (in user friendly format). The ""header_handle"" must be a stack object over a high level stream or a config element. Returns key ""handle"". Dependencies: traffic_generator must be ixnetwork_540. get_available_dynamic_update_fields Returns a list of all available dynamic update fields for the provided stream_id.Returns key ""available_dynamic_update_fields""Dependencies: traffic_generator must be ixnetwork_540. get_available_session_aware_traffic Returns a list of all availablesession aware traffic fields for the provided stream_id.Returns key ""available_session_aware_traffic_fields"" Dependencies: traffic_generator must be ixnetwork_540. get_available_fields_for_link Returns a list of all availablevalid stack link fields for the provided stream_id.Returns key ""available_fields_for_link"". Valid only for IxNetwork greater than 7.0. Dependencies: traffic_generator must be ixnetwork_540. get_field_values Returns the values for the provided field handle. The field handle can be obtained using mode ""get_available_fields"". The header handle must also be provided. List of returned keys: field_activeFieldChoice field_auto field_countValue field_defaultValue field_displayName field_enumValues field_fieldChoice field_fieldValue field_fullMesh field_id field_length field_level field_name field_offset field_offsetFromRoot field_optional field_optionalEnabled field_rateVaried field_readOnly field_requiresUdf field_singleValue field_startValue field_stepValue field_trackingEnabled field_valueFormat field_valueList field_valueType Dependencies: traffic_generator must be ixnetwork_540. set_field_values Sets the specified values for the given field handle. Not all values provided by ""get_field_values"" are available for set. Some of them are read-only. Valid fields: field_activeFieldChoice field_auto field_countValue field_fieldValue field_fullMesh field_optionalEnabled field_singleValue field_startValue field_stepValue field_trackingEnabled field_valueList field_valueType Dependencies: traffic_generator must be ixnetwork_540. add_field_level Adds a new field level for the specified header if multiple levels are supported. The ""header_handle"" and the ""field_handle"" must be provided. Returns the new field handlers associated with the new level (key: handle). Dependencies: traffic_generator must be ixnetwork_540. remove_field_level Removed the specified field level on the given header. The ""header_handle"" and the ""field_handle"" must be provided. Dependencies: traffic_generator must be ixnetwork_540. get_available_egress_tracking_field_offset Returns a list of all availableegress tracking custom field offsets specific for the provided stream_id.Returns key ""available_egress_tracking_field_offset"".
        Constants Available: MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        proto --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MODE_CMD : proto})

    def traffic_config_mpls(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_labels(self):
        """
        This is the method the command: traffic_config option mpls_labels
        Description:MPLS labels in the packets for each stream. Ixia supports multiple MPLS
            labels in a single packet. For example, to stack three labels in one
            packet, use -mpls_labels {14 18 78}, where 14, 18 and 78 are the label
            IDs in the packet.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: MPLS_LABELS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.MPLS_LABELS_CMD : ""})

    def traffic_config_mpls_labels_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_labels_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_labels_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_labels_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_multiple_queues(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_name(self, name_string):
        return self.logger.log_unimplemented_method()

    def traffic_config_no_write(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_num_dst_ports(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_number_of_packets_per_stream(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_number_of_packets_tx(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_override_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_pause_control_time(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_pending_operations_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_pgid_offset(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_pgid_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_pkts_per_burst(self, num):
        """
        This is the method the command: traffic_config option pkts_per_burst
        Description:Number of packets to include in one burst.
        Constants Available: PKTS_PER_BURST_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        num --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.PKTS_PER_BURST_CMD : num})

    def traffic_config_port_handle(self, port):
        """
        This is the method the command: traffic_config option port_handle
        Description:Depending on the traffic_generator value, this option has different meanings. If traffic_generator ixnetwork_540 is used this parameter is used ixos/ixnetwork_540 - The port for which to configure traffic. Mandatory for -mode create/reset when -traffic_generator is set to ixos. For traffic_generator ixnetwork_540 this is mandatory on mode create only if parameter -emulation_src_handle is missing.ixnetwork/ixnetwork_540 - The port_handle parameter is not necessary anymore. When using IxNetwork, traffic configurations will be done using previously created handles (IP interfaces, PPP ranges, L2TP ranges, Protocol Route Ranges etc.) as sources (parameter -emulation_src_handle) and destinations (-emulation_dst_handle).
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.PORT_HANDLE_CMD : port})

    def traffic_config_port_handle2(self, any):
        """
        This is the method the command: traffic_config option port_handle2
        Description:A second port for which to configure traffic configuration when option
            'bidirectional' is enabled. For traffic_generator ixnetwork_540 this
            parameter is used only if emulation_src_handle and emulation_dst_handle
            parameters are missing. For traffic_generator ixnetwork_540 this
            parameter can be used as destination port for the unidirectional traffic
            too.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: PORT_HANDLE2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.PORT_HANDLE2_CMD : any})

    def traffic_config_ppp_session_id(self):
        """
        This is the method the command: traffic_config option ppp_session_id
        Description:Not supported
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: PPP_SESSION_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.PPP_SESSION_ID_CMD : ""})

    def traffic_config_preamble_custom_size(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_preamble_size_mode(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_pt_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_public_port_ip(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_pvc_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_pvc_count_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_ipv6_flow_label(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_ipv6_traffic_class(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_type_ixn(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_queue_id(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ramp_up_percentage(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_range_per_spoke(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_bps(self, rate):
        """
        This is the method the command: traffic_config option rate_bps
        Description:This parameter can be updated while the traffic is running with -mode 'dynamic_update' and -stream_id . Traffic rate to send in bps.
        Constants Available: RATE_BPS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        rate --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.RATE_BPS_CMD : rate})

    def traffic_config_rate_byteps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_frame_gap(self, range):
        """
        This is the method the command: traffic_config option rate_frame_gap
        Description:Traffic rate in percent for the specified stream using a frame/gap
            ratio. allowed.The frame/gap percentage is defined as ( (frame_size +
            preamble)/(frame_size + preamble + frame_gap) )*100.For ATM and POS
            ports the preamble will be 0.If the rate cannot be achieved then it will
            be rounded to the closest legal value and the user will be informed
            about the value that will be used.Limitations:1. rate_frame_gap cannot
            be used in conjunction with the following
            parameters:rate_bpsrate_percentrate_pps2. The following parameters can
            have limited choices:length_mode only fixedtraffic_generator only ixos3.
            Port must be configured with transmit mode packet_streams
            (::::interface_config - transmit_mode stream)4. Only supported with
            ports that implement minimumInterFrameGap and maximumInterFrameGap
            features. If the port does not support these features an error is
            returned. Refer to IxiaReferenceGuide.pdf for a list of ports and the
            supported features.5. Supported only with IxOS version 5.10 or higher.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos' |
        Constants Available: RATE_FRAME_GAP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.RATE_FRAME_GAP_CMD : range})

    def traffic_config_rate_kbps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_kbyteps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_mbps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_mbyteps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_percent(self, range):
        """
        This is the method the command: traffic_config option rate_percent
        Description:This parameter can be updated while the traffic is running with -mode
            'dynamic_update' and -stream_id . Traffic rate in percent of line rate
            for the specified stream. Valid choices are between 0.00 and 100.00,
            inclusive.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: RATE_PERCENT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.RATE_PERCENT_CMD : range})

    def traffic_config_rate_pps(self, rate):
        """
        This is the method the command: traffic_config option rate_pps
        Description:This parameter can be updated while the traffic is running with -mode 'dynamic_update' and -stream_id . Traffic rate to send in pps.
        Constants Available: RATE_PPS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        rate --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.RATE_PPS_CMD : rate})

    def traffic_config_return_to_id(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_command(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_command_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_command_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_version(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_route_mesh(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rtp_csrc_count(self):
        """
        This is the method the command: traffic_config option rtp_csrc_count
        Description:Specifies the CSRC count contains the number of CSRC identifiers that
            follow the fixed header: Note: 4 bits
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: RTP_CSRC_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.RTP_CSRC_COUNT_CMD : ""})

    def traffic_config_rtp_payload_type(self):
        """
        This is the method the command: traffic_config option rtp_payload_type
        Description:Specifies the format of the RTP payload and determines its
            interpretation by the application - Note: 7 bits, G.729 codec is payload
            type 18
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: RTP_PAYLOAD_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.RTP_PAYLOAD_TYPE_CMD : ""})

    def traffic_config_session_aware_traffic(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_signature(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_signature_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_site_id(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_site_id_enable(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_site_id_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_skip_frame_size_validation(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_source_filter(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_src_dest_mesh(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ssrc(self):
        """
        This is the method the command: traffic_config option ssrc
        Description:Specifies the synchronization source
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
        Constants Available: SSRC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.SSRC_CMD : ""})

    def traffic_config_stack_index(self):
        """
        This is the method the command: traffic_config option stack_index
        Description:Required for -mode modify_or_insert. It represents the stack index in
            the highLevelStream / configElement.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
            'mode' | value= 'modify_or_insert' |
        Constants Available: STACK_INDEX_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.STACK_INDEX_CMD : ""})

    def traffic_config_stream_id(self, stream_id):
        """
        This is the method the command: traffic_config option stream_id
        Description:Required for -mode modify/remove/enable/disable/append_header/prepend_header/replace_header/dynamic_update calls. Stream ID is not required for configuring a stream for the first time. In this case, the stream ID is returned from the call.
        Constants Available: STREAM_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        stream_id --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.STREAM_ID_CMD : stream_id})

    def traffic_config_stream_packing(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_column_name(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_column_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_column_size(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_column_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_rows(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_tag_filter(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_flag(self, bool_opt):
        """
        This is the method the command: traffic_config option tcp_ack_flag
        Description:Whether the 'acknowledge flag' in the TCP header is enabled. Valid
            choices are:
            Valid options are:
            0

            Disabled
            1

            Enabled
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_ACK_FLAG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_ACK_FLAG_CMD : bool_opt})

    def traffic_config_tcp_ack_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_num(self, range):
        """
        This is the method the command: traffic_config option tcp_ack_num
        Description:TCP tcp_window size field for this particular stream. Valid choices are
            between 0 and 65535, inclusive.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_ACK_NUM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_ACK_NUM_CMD : range})

    def traffic_config_tcp_ack_num_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_num_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_num_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_num_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_cwr_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_cwr_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_cwr_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_dst_port(self, port):
        """
        This is the method the command: traffic_config option tcp_dst_port
        Description:between 0 and 65535, inclusive.
        Constants Available: TCP_DST_PORT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_DST_PORT_CMD : port})

    def traffic_config_tcp_dst_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_dst_port_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_dst_port_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_dst_port_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ecn_echo_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ecn_echo_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ecn_echo_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_fin_flag(self, bool_opt):
        """
        This is the method the command: traffic_config option tcp_fin_flag
        Description:Whether the 'finished flag' in the TCP header is enabled. Valid choices are:
            Valid options are:
            0

            Disabled
            1

            Enabled
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_FIN_FLAG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_FIN_FLAG_CMD : bool_opt})

    def traffic_config_tcp_fin_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_fin_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ns_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ns_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ns_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_psh_flag(self, bool_opt):
        """
        This is the method the command: traffic_config option tcp_psh_flag
        Description:Whether the 'psh flag' in the TCP header is enabled. Valid choices are:
            Valid options are:
            0

            Disabled
            1

            Enabled
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_PSH_FLAG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_PSH_FLAG_CMD : bool_opt})

    def traffic_config_tcp_psh_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_psh_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_reserved(self):
        """
        This is the method the command: traffic_config option tcp_reserved
        Description:Configure the TCP reserved field (0-7).
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixnetwork_540' |
        Constants Available: TCP_RESERVED_CMD
        Supported:IxNetwork
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_RESERVED_CMD : ""})

    def traffic_config_tcp_reserved_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_reserved_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_reserved_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_reserved_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_rst_flag(self, bool_opt):
        """
        This is the method the command: traffic_config option tcp_rst_flag
        Description:Whether the 'reset flag' in the TCP header is enabled. Valid choices are:
            Valid options are:
            0

            Disabled
            1

            Enabled
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_RST_FLAG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_RST_FLAG_CMD : bool_opt})

    def traffic_config_tcp_rst_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_rst_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_seq_num(self, range):
        """
        This is the method the command: traffic_config option tcp_seq_num
        Description:between 0 and 4294967295, inclusive.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_SEQ_NUM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_SEQ_NUM_CMD : range})

    def traffic_config_tcp_seq_num_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_seq_num_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_seq_num_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_seq_num_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_src_port(self, port):
        """
        This is the method the command: traffic_config option tcp_src_port
        Description:between 0 and 65535, inclusive.
        Constants Available: TCP_SRC_PORT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_SRC_PORT_CMD : port})

    def traffic_config_tcp_src_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_src_port_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_src_port_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_src_port_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_syn_flag(self, bool_opt):
        """
        This is the method the command: traffic_config option tcp_syn_flag
        Description:Whether the 'synchronize flag' in the TCP header is enabled.
            Valid options are:
            0

            Disabled
            1

            Enabled
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_SYN_FLAG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_SYN_FLAG_CMD : bool_opt})

    def traffic_config_tcp_syn_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_syn_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urg_flag(self, bool_opt):
        """
        This is the method the command: traffic_config option tcp_urg_flag
        Description:Whether the 'urgent flag' in the TCP header is enabled. Valid choices are:
            Valid options are:
            0

            Disabled
            1

            Enabled
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_URG_FLAG_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_URG_FLAG_CMD : bool_opt})

    def traffic_config_tcp_urg_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urg_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urgent_ptr(self, range):
        """
        This is the method the command: traffic_config option tcp_urgent_ptr
        Description:TCP Urgent Pointer value for this particular stream. Valid choices are
            between 0 and 65535, inclusive.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_URGENT_PTR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_URGENT_PTR_CMD : range})

    def traffic_config_tcp_urgent_ptr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urgent_ptr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urgent_ptr_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urgent_ptr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_window(self, range):
        """
        This is the method the command: traffic_config option tcp_window
        Description:TCP tcp_window size field for this particular stream. Valid choices are
            between 0 and 65535, inclusive.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: TCP_WINDOW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TCP_WINDOW_CMD : range})

    def traffic_config_tcp_window_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_window_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_window_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_window_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_test_objective_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_timestamp_initial_value(self):
        """
        This is the method the command: traffic_config option timestamp_initial_value
        Description:Specifies the initial value of the timestamp
            DEFAULT
                Not supported
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= '' |
                    RETURN VALUES
            Supported Platform     Details
            ixNetwork540OrNewer and IxNetwork530OrEarlier and IxOS/IxNetwork-FT

            status

            $::SUCCESS | $::FAILURE
            log

            On status of failure, gives detailed information. On status of success,
            gives possible warnings.
            stream_id

            Stream identifier when not bidirectional. When traffic_generator is
            ixnetwork_540 this key returns the name of the traffic item created.
            ixNetwork540OrNewer

            traffic_item

            Valid only for traffic_generator ixnetwork_540. This key returns the
            object reference of the traffic item created.
            <traffic_item>.headers

            Valid only for traffic_generator ixnetwork_540. Returns the list of the
            packet headers configured in <traffic_item>. <traffic_item> is returned
            by key 'traffic_item'.
            <traffic_item>.stream_ids

            Valid only for traffic_generator ixnetwork_540. Returns the list of the
            flow groups created for <traffic_item>. <traffic_item> is returned by
            key 'traffic_item'.
            <traffic_item>.<flow_group>.headers

            Valid only for traffic_generator ixnetwork_540. Returns the list of the
            packet headers created for <flow_group>. <flow_group> is one of the flow
            groups returned by key '<traffic_item>.stream_ids'.
            pt_handle

            Protocol Template handle (or list) returned when mode is
            'get_available_protocol_templates'.
            handle

            Returns available fields or field handles when mode is
            'get_available_fields', 'add_field_level' or 'remove_field_level'.
            field_activeFieldChoice

            Specific value for this key when mode is 'get_field_values'.
            field_auto

            Specific value for this key when mode is 'get_field_values'.
            field_countValue

            Specific value for this key when mode is 'get_field_values'.
            field_defaultValue

            Specific value for this key when mode is 'get_field_values'.
            field_displayName

            Specific value for this key when mode is 'get_field_values'.
            field_enumValues

            Specific value for this key when mode is 'get_field_values'.
            field_fieldChoice

            Specific value for this key when mode is 'get_field_values'.
            field_fieldValue

            Specific value for this key when mode is 'get_field_values'.
            field_fullMesh

            Specific value for this key when mode is 'get_field_values'.
            field_id

            Specific value for this key when mode is 'get_field_values'.
            field_length

            Specific value for this key when mode is 'get_field_values'.
            field_level

            Specific value for this key when mode is 'get_field_values'.
            field_name

            Specific value for this key when mode is 'get_field_values'.
            field_offset

            Specific value for this key when mode is 'get_field_values'.
            field_offsetFromRoot

            Specific value for this key when mode is 'get_field_values'.
            field_optional

            Specific value for this key when mode is 'get_field_values'.
            field_optionalEnabled

            Specific value for this key when mode is 'get_field_values'.
            field_rateVaried

            Specific value for this key when mode is 'get_field_values'.
            field_readOnly

            Specific value for this key when mode is 'get_field_values'.
            field_requiresUdf

            Specific value for this key when mode is 'get_field_values'.
            field_singleValue

            Specific value for this key when mode is 'get_field_values'.
            field_startValue

            Specific value for this key when mode is 'get_field_values'.
            field_stepValue

            Specific value for this key when mode is 'get_field_values'.
            field_trackingEnabled

            Specific value for this key when mode is 'get_field_values'.
            field_valueFormat

            Specific value for this key when mode is 'get_field_values'.
            field_valueList

            Specific value for this key when mode is 'get_field_values'.
            field_valueType

            Specific value for this key when mode is 'get_field_values'.
            last_stack
        Constants Available: TIMESTAMP_INITIAL_VALUE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TIMESTAMP_INITIAL_VALUE_CMD : ""})

    def traffic_config_track_by(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_traffic_generate(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_traffic_generator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_transmit_distribution(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_transmit_mode(self, mode):
        """
        This is the method the command: traffic_config option transmit_mode
        Description:Depending on the traffic_generator value, this option has different meanings:
            ixos/ixnetwork_540: Destination IP address of the packet.
            ixnetwork: This option is used to specify the value of the first IP of the first IP static endpoint range for L2VPN traffic. (Not supported in this release.)
        Constants Available: TRANSMIT_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        mode --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.TRANSMIT_MODE_CMD : mode})

    def traffic_config_tx_delay(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tx_delay_unit(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tx_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_checksum(self, bool_opt):
        """
        This is the method the command: traffic_config option udp_checksum
        Description:1 - the UDP checksum is set as current checksum for UDP data0 - If
            parameter udp_checksum_value is specified, the UDP checksum will be
            overriten by the value supplied through udp_checksum_value. If
            udp_checksum_value is not present, an invalid checksum will be set as
            the UDP checksum.Valid only for traffic_generator ixos/ixnetwork_540 and
            when -l4_protocol is udp.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: UDP_CHECKSUM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.UDP_CHECKSUM_CMD : bool_opt})

    def traffic_config_udp_checksum_value(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_checksum_value_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_dst_port(self, port):
        """
        This is the method the command: traffic_config option udp_dst_port
        Description:between 0 and 65535, inclusive. The port number needs to be different than the port number used for RIP and DHCP. Valid only for traffic_generator ixos/ixnetwork_540 and when -l4_protocol is udp.
        Constants Available: UDP_DST_PORT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.UDP_DST_PORT_CMD : port})

    def traffic_config_udp_dst_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_dst_port_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_dst_port_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_dst_port_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_src_port(self, port):
        """
        This is the method the command: traffic_config option udp_src_port
        Description:between 0 and 65535, inclusive. The port number needs to be different than the port number used for RIP and DHCP. Valid only for traffic_generator ixos/ixnetwork_540 and when -l4_protocol is udp.
        Constants Available: UDP_SRC_PORT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.UDP_SRC_PORT_CMD : port})

    def traffic_config_udp_src_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_src_port_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_src_port_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_src_port_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_use_all_ip_subnets(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_use_cp_rate(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_use_cp_size(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vci(self, range):
        """
        This is the method the command: traffic_config option vci
        Description:The virtual circuit identifier. Depending on the traffic_generator
            value, this option has different ixnetwork - This option is used to
            specify the value of the first VCI of the first ATM static endpoint
            range. It can take any value in the 0-4294967295 range. Can be used only
            for L2VPN traffic, but is not supported in this release.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: VCI_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VCI_CMD : range})

    def traffic_config_vci_count(self, range):
        """
        This is the method the command: traffic_config option vci_count
        Description:If -atm_counter_vci_type is set to counter and atm_counter_vci_mode is
            set to incr or decr, then this is the number of times to increment the
            VCI value before repeating from the start value.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: VCI_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VCI_COUNT_CMD : range})

    def traffic_config_vci_increment(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_vci_increment_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_vci_step(self, range):
        """
        This is the method the command: traffic_config option vci_step
        Description:Depending on the traffic_generator value, this option has different
            ixos/ixnetwork_540 - If -atm_counter_vci_type is set to counter, then
            this is the value added/substracted between successive vci values
            ixnetwork - This option is used to specify the step between the value of
            the first VCI of each the ATM static endpoint range. It can take any
            numeric value. Can be used only for L2VPN traffic, but is not supported
            in this release.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: VCI_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VCI_STEP_CMD : range})

    def traffic_config_vlan(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_cfi(self, bool_opt):
        """
        This is the method the command: traffic_config option vlan_cfi
        Description:Whether VLAN CFI bit is set or unset for a particular stream. For
            stacked VLAN (QinQ) this parameter will be provided as a list of values,
            each of them representing whether VLAN CFI bit is set or unset for each
            VLAN from the stack. Example: {1 0 1 1}Valid options are:0 - Unset1 - Set
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: VLAN_CFI_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VLAN_CFI_CMD : bool_opt})

    def traffic_config_vlan_cfi_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_cfi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_cfi_step(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_cfi_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_enable(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_id(self, vid):
        """
        This is the method the command: traffic_config option vlan_id
        Description:4095, inclusive. For stacked VLAN (QinQ) this parameter will be provided as a list of values, each of them representing the id a VLAN from the stack.Example: {10 13 14 20}. If emulation_src_handle or emulation_dst_handle are present and traffic_generator argument is ""ixos"", the traffic will be configured over PPPoX sessions using IxOS. In this case the vlan parameters apply only to the downstream (traffic sent from IP/Network port to PPPoE access port). Upstream traffic will use vlan information from the PPPoE handle.Downstream traffic will use vlan information set through this parameter.For traffic generator ixnetwork is used only for L2VPN traffic, but is not supported in this release.
        Constants Available: VLAN_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        vid --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VLAN_ID_CMD : vid})

    def traffic_config_vlan_id_count(self, num):
        """
        This is the method the command: traffic_config option vlan_id_count
        Description:Number of VLANs to be used for a particular stream. Option ""vlan_id_mode"" must be set to increment or decrement. Valid choices are between 1 and 4096, inclusive.For stacked VLAN (QinQ) this parameter will be provided as a list of values, each of them representing the number of VLANs for each vlan_id from the stack.Example: {2 5 1 13}
        Constants Available: VLAN_ID_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        num --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VLAN_ID_COUNT_CMD : num})

    def traffic_config_vlan_id_mode(self, opt):
        """
        This is the method the command: traffic_config option vlan_id_mode
        Description:Behavior of the VLAN tag in packets for a particular stream. For stacked VLAN (QinQ) this parameter will be provided as a list of values, each of them representing the Behavior of each VLAN from the stack. Only the top two VLAN elements in a stacked VLAN may use values different from ""fixed"". For traffic_generator ixnetwork is used only for L2VPN traffic, but is not supported in this release.For traffic_generator ixnetwork_540 the behavior is the same as for traffic_generator ixos.Example: {increment nested_incr fixed fixed}. Valid options are: fixedWill set the VLAN tag to be in idle mode. Available when using traffic_generator ixnetwork and ixos and ixnetwork_540.increment Will set the VLAN tag to be in increment mode. Available when using traffic_generator ixnetwork and ixos and ixnetwork_540. It is the default when using the ixos/ixnetwork_540 traffic generator.decrementWill set the VLAN tag to be in decrement mode. Available when using traffic_generator ixos and ixnetwork_540.random Will set the VLAN tag to be in random mode. Available when using traffic_generator ixos.nested_incr For the second VLAN in a stackedVlan, this may be used to performed nested increment with respect to the first stack element. Available when using traffic_generator ixos.nested_decr - For the second VLAN in a stackedVlan, this may be used to performed nested decrement with respect to the first stack element. Available when using traffic_generator ixos.list Will set the VLAN tag to be a list of values. Available when using traffic_generator ixnetwork_540 with mode append_header/modify_header.
        Constants Available: VLAN_ID_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VLAN_ID_MODE_CMD : opt})

    def traffic_config_vlan_id_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id_step(self, hexdefault0x01):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_user_priority(self, priority):
        """
        This is the method the command: traffic_config option vlan_user_priority
        Description:inclusive.For stacked VLAN (QinQ) this parameter will be provided as a list of values, each of them representing the user priority for each VLAN ID from the stack.Example: {2 4 6 0}.
        Constants Available: VLAN_USER_PRIORITY_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        priority --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VLAN_USER_PRIORITY_CMD : priority})

    def traffic_config_vlan_user_priority_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_user_priority_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_user_priority_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_user_priority_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vpi(self, range):
        """
        This is the method the command: traffic_config option vpi
        Description:Depending on the traffic_generator value, this option has different
            ixnetwork - This option is used to specify the value of the first VPI of
            the first ATM static endpoint range. It can take any value in the
            0-4294967295 range. Can be used only for L2VPN traffic, but is not
            supported in this release.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: VPI_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VPI_CMD : range})

    def traffic_config_vpi_count(self, range):
        """
        This is the method the command: traffic_config option vpi_count
        Description:If -atm_counter_vpi_type is set to counter and atm_counter_vpi_mode is
            set to incr or decr, then this is the number of times to increment the
            VPI value before repeating from the start value.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork_540' |
        Constants Available: VPI_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VPI_COUNT_CMD : range})

    def traffic_config_vpi_increment(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_vpi_increment_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_vpi_step(self, range):
        """
        This is the method the command: traffic_config option vpi_step
        Description:Depending on the traffic_generator value, this option has different
            ixos/ixnetwork_540 - If -atm_counter_vpi_type is set to counter, then
            this is the value added/substracted between successive vpi values
            ixnetwork - This option is used to specify the step between the value of
            the first VPI of each the ATM static endpoint range. It can take any
            numeric value. Can be used only for L2VPN traffic, but is not supported
            in this release.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'traffic_generator' | value= 'ixos ixnetwork ixnetwork_540' |
        Constants Available: VPI_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.traffic_config({TrafficConfigConstants.VPI_STEP_CMD : range})


"""
    This is the Constants class for the command: traffic_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class TrafficConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    TRAFFIC_CONFIG_API = "TRAFFIC_CONFIG_API"

    ADJUST_RATE_CMD = "adjust_rate"

    ALLOW_SELF_DESTINED_CMD = "allow_self_destined"

    APP_PROFILE_TYPE_CMD = "app_profile_type"

    ARP_DST_HW_ADDR_CMD = "arp_dst_hw_addr"

    ARP_DST_HW_COUNT_CMD = "arp_dst_hw_count"

    ARP_DST_HW_MODE_CMD = "arp_dst_hw_mode"
    # Constant values for ARP_DST_HW_MODE_CMD
    ARP_DST_HW_MODE_FIXED = "fixed"
    ARP_DST_HW_MODE_INCREMENT = "increment"
    ARP_DST_HW_MODE_DECREMENT = "decrement"

    ARP_DST_HW_STEP_CMD = "arp_dst_hw_step"

    ARP_DST_HW_TRACKING_CMD = "arp_dst_hw_tracking"

    ARP_HW_ADDRESS_LENGTH_CMD = "arp_hw_address_length"

    ARP_HW_ADDRESS_LENGTH_COUNT_CMD = "arp_hw_address_length_count"

    ARP_HW_ADDRESS_LENGTH_MODE_CMD = "arp_hw_address_length_mode"
    # Constant values for ARP_HW_ADDRESS_LENGTH_MODE_CMD
    ARP_HW_ADDRESS_LENGTH_MODE_INCR = "incr"
    ARP_HW_ADDRESS_LENGTH_MODE_FIXED = "fixed"
    ARP_HW_ADDRESS_LENGTH_MODE_LIST = "list"
    ARP_HW_ADDRESS_LENGTH_MODE_DECR = "decr"

    ARP_HW_ADDRESS_LENGTH_STEP_CMD = "arp_hw_address_length_step"

    ARP_HW_ADDRESS_LENGTH_TRACKING_CMD = "arp_hw_address_length_tracking"

    ARP_HW_TYPE_CMD = "arp_hw_type"

    ARP_HW_TYPE_COUNT_CMD = "arp_hw_type_count"

    ARP_HW_TYPE_MODE_CMD = "arp_hw_type_mode"
    # Constant values for ARP_HW_TYPE_MODE_CMD
    ARP_HW_TYPE_MODE_INCR = "incr"
    ARP_HW_TYPE_MODE_FIXED = "fixed"
    ARP_HW_TYPE_MODE_LIST = "list"
    ARP_HW_TYPE_MODE_DECR = "decr"

    ARP_HW_TYPE_STEP_CMD = "arp_hw_type_step"

    ARP_HW_TYPE_TRACKING_CMD = "arp_hw_type_tracking"

    ARP_OPERATION_CMD = "arp_operation"
    # Constant values for ARP_OPERATION_CMD
    ARP_OPERATION_ARPREQUEST = "arpRequest"
    ARP_OPERATION_ARPREPLY = "arpReply"
    ARP_OPERATION_RARPREPLY = "rarpReply"
    ARP_OPERATION_RARPREQUEST = "rarpRequest"

    ARP_OPERATION_MODE_CMD = "arp_operation_mode"
    # Constant values for ARP_OPERATION_MODE_CMD
    ARP_OPERATION_MODE_FIXED = "fixed"
    ARP_OPERATION_MODE_LIST = "list"

    ARP_OPERATION_TRACKING_CMD = "arp_operation_tracking"

    ARP_PROTOCOL_ADDR_LENGTH_CMD = "arp_protocol_addr_length"

    ARP_PROTOCOL_ADDR_LENGTH_COUNT_CMD = "arp_protocol_addr_length_count"

    ARP_PROTOCOL_ADDR_LENGTH_MODE_CMD = "arp_protocol_addr_length_mode"
    # Constant values for ARP_PROTOCOL_ADDR_LENGTH_MODE_CMD
    ARP_PROTOCOL_ADDR_LENGTH_MODE_INCR = "incr"
    ARP_PROTOCOL_ADDR_LENGTH_MODE_FIXED = "fixed"
    ARP_PROTOCOL_ADDR_LENGTH_MODE_LIST = "list"
    ARP_PROTOCOL_ADDR_LENGTH_MODE_DECR = "decr"

    ARP_PROTOCOL_ADDR_LENGTH_STEP_CMD = "arp_protocol_addr_length_step"

    ARP_PROTOCOL_ADDR_LENGTH_TRACKING_CMD = "arp_protocol_addr_length_tracking"

    ARP_PROTOCOL_TYPE_CMD = "arp_protocol_type"

    ARP_PROTOCOL_TYPE_COUNT_CMD = "arp_protocol_type_count"

    ARP_PROTOCOL_TYPE_MODE_CMD = "arp_protocol_type_mode"
    # Constant values for ARP_PROTOCOL_TYPE_MODE_CMD
    ARP_PROTOCOL_TYPE_MODE_INCR = "incr"
    ARP_PROTOCOL_TYPE_MODE_FIXED = "fixed"
    ARP_PROTOCOL_TYPE_MODE_LIST = "list"
    ARP_PROTOCOL_TYPE_MODE_DECR = "decr"

    ARP_PROTOCOL_TYPE_STEP_CMD = "arp_protocol_type_step"

    ARP_PROTOCOL_TYPE_TRACKING_CMD = "arp_protocol_type_tracking"

    ARP_SRC_HW_ADDR_CMD = "arp_src_hw_addr"

    ARP_SRC_HW_COUNT_CMD = "arp_src_hw_count"

    ARP_SRC_HW_MODE_CMD = "arp_src_hw_mode"
    # Constant values for ARP_SRC_HW_MODE_CMD
    ARP_SRC_HW_MODE_DECREMENT = "decrement"
    ARP_SRC_HW_MODE_FIXED = "fixed"
    ARP_SRC_HW_MODE_INCREMENT = "increment"

    ARP_SRC_HW_STEP_CMD = "arp_src_hw_step"

    ARP_SRC_HW_TRACKING_CMD = "arp_src_hw_tracking"

    ATM_COUNTER_VCI_DATA_ITEM_LIST_CMD = "atm_counter_vci_data_item_list"

    ATM_COUNTER_VCI_MASK_SELECT_CMD = "atm_counter_vci_mask_select"

    ATM_COUNTER_VCI_MASK_VALUE_CMD = "atm_counter_vci_mask_value"

    ATM_COUNTER_VCI_MODE_CMD = "atm_counter_vci_mode"
    # Constant values for ATM_COUNTER_VCI_MODE_CMD
    ATM_COUNTER_VCI_MODE_CONT_DECR = "cont_decr"
    ATM_COUNTER_VCI_MODE_INCR = "incr"
    ATM_COUNTER_VCI_MODE_CONT_INCR = "cont_incr"
    ATM_COUNTER_VCI_MODE_DECR = "decr"

    ATM_COUNTER_VCI_TYPE_CMD = "atm_counter_vci_type"
    # Constant values for ATM_COUNTER_VCI_TYPE_CMD
    ATM_COUNTER_VCI_TYPE_RANDOM = "random"
    ATM_COUNTER_VCI_TYPE_TABLE = "table"
    ATM_COUNTER_VCI_TYPE_FIXED = "fixed"
    ATM_COUNTER_VCI_TYPE_COUNTER = "counter"

    ATM_COUNTER_VPI_DATA_ITEM_LIST_CMD = "atm_counter_vpi_data_item_list"

    ATM_COUNTER_VPI_MASK_SELECT_CMD = "atm_counter_vpi_mask_select"

    ATM_COUNTER_VPI_MASK_VALUE_CMD = "atm_counter_vpi_mask_value"

    ATM_COUNTER_VPI_MODE_CMD = "atm_counter_vpi_mode"
    # Constant values for ATM_COUNTER_VPI_MODE_CMD
    ATM_COUNTER_VPI_MODE_CONT_DECR = "cont_decr"
    ATM_COUNTER_VPI_MODE_INCR = "incr"
    ATM_COUNTER_VPI_MODE_CONT_INCR = "cont_incr"
    ATM_COUNTER_VPI_MODE_DECR = "decr"

    ATM_COUNTER_VPI_TYPE_CMD = "atm_counter_vpi_type"
    # Constant values for ATM_COUNTER_VPI_TYPE_CMD
    ATM_COUNTER_VPI_TYPE_RANDOM = "random"
    ATM_COUNTER_VPI_TYPE_TABLE = "table"
    ATM_COUNTER_VPI_TYPE_FIXED = "fixed"
    ATM_COUNTER_VPI_TYPE_COUNTER = "counter"

    ATM_HEADER_AAL5ERROR_CMD = "atm_header_aal5error"
    # Constant values for ATM_HEADER_AAL5ERROR_CMD
    ATM_HEADER_AAL5ERROR_BAD_CRC = "bad_crc"
    ATM_HEADER_AAL5ERROR_NO_ERROR = "no_error"

    ATM_HEADER_CELL_LOSS_PRIORITY_CMD = "atm_header_cell_loss_priority"

    ATM_HEADER_CPCS_LENGTH_CMD = "atm_header_cpcs_length"

    ATM_HEADER_ENABLE_AUTO_VPI_VCI_CMD = "atm_header_enable_auto_vpi_vci"

    ATM_HEADER_ENABLE_CL_CMD = "atm_header_enable_cl"

    ATM_HEADER_ENABLE_CPCS_LENGTH_CMD = "atm_header_enable_cpcs_length"

    ATM_HEADER_ENCAPSULATION_CMD = "atm_header_encapsulation"
    # Constant values for ATM_HEADER_ENCAPSULATION_CMD
    ATM_HEADER_ENCAPSULATION_LLC_NLPID_ROUTED = "llc_nlpid_routed"
    ATM_HEADER_ENCAPSULATION_VCC_MUX_BRIDGED_ETH_NO_FCS = "vcc_mux_bridged_eth_no_fcs"
    ATM_HEADER_ENCAPSULATION_VCC_MUX_IPV4_ROUTED = "vcc_mux_ipv4_routed"
    ATM_HEADER_ENCAPSULATION_LLC_BRIDGED_ETH_FCS = "llc_bridged_eth_fcs"
    ATM_HEADER_ENCAPSULATION_VCC_MUX_MPLS_ROUTED = "vcc_mux_mpls_routed"
    ATM_HEADER_ENCAPSULATION_LLC_ROUTED_CLIP = "llc_routed_clip"
    ATM_HEADER_ENCAPSULATION_VCC_MUX_BRIDGED_ETH_FCS = "vcc_mux_bridged_eth_fcs"
    ATM_HEADER_ENCAPSULATION_VCC_MUX_IPV6_ROUTED = "vcc_mux_ipv6_routed"
    ATM_HEADER_ENCAPSULATION_LLC_BRIDGED_ETH_NO_FCS = "llc_bridged_eth_no_fcs"
    ATM_HEADER_ENCAPSULATION_LLC_PPPOA = "llc_pppoa"
    ATM_HEADER_ENCAPSULATION_VCC_MUX_PPOA = "vcc_mux_ppoa"

    ATM_HEADER_GENERIC_FLOW_CTRL_CMD = "atm_header_generic_flow_ctrl"

    ATM_HEADER_HEC_ERRORS_CMD = "atm_header_hec_errors"

    ATM_RANGE_COUNT_CMD = "atm_range_count"

    BECN_CMD = "becn"

    BIDIRECTIONAL_CMD = "bidirectional"

    BURST_LOOP_COUNT_CMD = "burst_loop_count"

    CIRCUIT_ENDPOINT_TYPE_CMD = "circuit_endpoint_type"
    # Constant values for CIRCUIT_ENDPOINT_TYPE_CMD
    CIRCUIT_ENDPOINT_TYPE_IPV6_APPLICATION_TRAFFIC = "ipv6_application_traffic"
    CIRCUIT_ENDPOINT_TYPE_ATM = "atm"
    CIRCUIT_ENDPOINT_TYPE_FC = "fc"
    CIRCUIT_ENDPOINT_TYPE_ETHERNET_VLAN = "ethernet_vlan"
    CIRCUIT_ENDPOINT_TYPE_HDLC = "hdlc"
    CIRCUIT_ENDPOINT_TYPE_ETHERNET_VLAN_ARP = "ethernet_vlan_arp"
    CIRCUIT_ENDPOINT_TYPE_PPP = "ppp"
    CIRCUIT_ENDPOINT_TYPE_IPV4 = "ipv4"
    CIRCUIT_ENDPOINT_TYPE_IPV6 = "ipv6"
    CIRCUIT_ENDPOINT_TYPE_IPV4_ARP = "ipv4_arp"
    CIRCUIT_ENDPOINT_TYPE_IPV4_APPLICATION_TRAFFIC = "ipv4_application_traffic"
    CIRCUIT_ENDPOINT_TYPE_FRAME_RELAY = "frame_relay"
    CIRCUIT_ENDPOINT_TYPE_FCOE = "fcoe"

    CIRCUIT_TYPE_CMD = "circuit_type"
    # Constant values for CIRCUIT_TYPE_CMD
    CIRCUIT_TYPE_6PE = "6pe"
    CIRCUIT_TYPE_NONE = "none"
    CIRCUIT_TYPE_6VPE = "6vpe"
    CIRCUIT_TYPE_APPLICATION = "application"
    CIRCUIT_TYPE_QUICK_FLOWS = "quick_flows"
    CIRCUIT_TYPE_MPLS = "mpls"
    CIRCUIT_TYPE_L2VPN = "l2vpn"
    CIRCUIT_TYPE_L3VPN = "l3vpn"
    CIRCUIT_TYPE_RAW = "raw"
    CIRCUIT_TYPE_STP = "stp"
    CIRCUIT_TYPE_VPLS = "vpls"
    CIRCUIT_TYPE_MAC_IN_MAC = "mac_in_mac"

    COMMAND_RESPONSE_CMD = "command_response"

    CONVERT_TO_RAW_CMD = "convert_to_raw"

    CSRC_LIST_CMD = "csrc_list"

    CUSTOM_OFFSET_CMD = "custom_offset"

    CUSTOM_VALUES_CMD = "custom_values"

    DATA_PATTERN_CMD = "data_pattern"

    DATA_PATTERN_MODE_CMD = "data_pattern_mode"
    # Constant values for DATA_PATTERN_MODE_CMD
    DATA_PATTERN_MODE_INCR_WORD = "incr_word"
    DATA_PATTERN_MODE_RANDOM = "random"
    DATA_PATTERN_MODE_INCR_BYTE = "incr_byte"
    DATA_PATTERN_MODE_DECR_BYTE = "decr_byte"
    DATA_PATTERN_MODE_REPEATING = "repeating"
    DATA_PATTERN_MODE_FIXED = "fixed"
    DATA_PATTERN_MODE_DECR_WORD = "decr_word"

    DATA_TOS_CMD = "data_tos"

    DATA_TOS_COUNT_CMD = "data_tos_count"

    DATA_TOS_MODE_CMD = "data_tos_mode"
    # Constant values for DATA_TOS_MODE_CMD
    DATA_TOS_MODE_INCR = "incr"
    DATA_TOS_MODE_FIXED = "fixed"
    DATA_TOS_MODE_LIST = "list"
    DATA_TOS_MODE_DECR = "decr"

    DATA_TOS_STEP_CMD = "data_tos_step"

    DATA_TOS_TRACKING_CMD = "data_tos_tracking"

    DESTINATION_FILTER_CMD = "destination_filter"
    # Constant values for DESTINATION_FILTER_CMD
    DESTINATION_FILTER_6PE = "6pe"
    DESTINATION_FILTER_ALL = "all"
    DESTINATION_FILTER_6VPE = "6vpe"
    DESTINATION_FILTER_ATM = "atm"
    DESTINATION_FILTER_MPLS = "mpls"
    DESTINATION_FILTER_NONE = "none"
    DESTINATION_FILTER_HDLC = "hdlc"
    DESTINATION_FILTER_L3VPN = "l3vpn"
    DESTINATION_FILTER_PPP = "ppp"
    DESTINATION_FILTER_FRAMERELAY = "framerelay"
    DESTINATION_FILTER_DATA_CENTER_BRIDGING = "data_center_bridging"
    DESTINATION_FILTER_ETHERNET = "ethernet"
    DESTINATION_FILTER_L2VPN = "l2vpn"
    DESTINATION_FILTER_MAC_IN_MAC = "mac_in_mac"
    DESTINATION_FILTER_BGPVPLS = "bgpvpls"

    DHCP_BOOT_FILENAME_CMD = "dhcp_boot_filename"

    DHCP_BOOT_FILENAME_TRACKING_CMD = "dhcp_boot_filename_tracking"

    DHCP_CLIENT_HW_ADDR_CMD = "dhcp_client_hw_addr"

    DHCP_CLIENT_HW_ADDR_COUNT_CMD = "dhcp_client_hw_addr_count"

    DHCP_CLIENT_HW_ADDR_MODE_CMD = "dhcp_client_hw_addr_mode"
    # Constant values for DHCP_CLIENT_HW_ADDR_MODE_CMD
    DHCP_CLIENT_HW_ADDR_MODE_INCR = "incr"
    DHCP_CLIENT_HW_ADDR_MODE_FIXED = "fixed"
    DHCP_CLIENT_HW_ADDR_MODE_LIST = "list"
    DHCP_CLIENT_HW_ADDR_MODE_DECR = "decr"

    DHCP_CLIENT_HW_ADDR_STEP_CMD = "dhcp_client_hw_addr_step"

    DHCP_CLIENT_HW_ADDR_TRACKING_CMD = "dhcp_client_hw_addr_tracking"

    DHCP_CLIENT_IP_ADDR_CMD = "dhcp_client_ip_addr"

    DHCP_CLIENT_IP_ADDR_COUNT_CMD = "dhcp_client_ip_addr_count"

    DHCP_CLIENT_IP_ADDR_MODE_CMD = "dhcp_client_ip_addr_mode"
    # Constant values for DHCP_CLIENT_IP_ADDR_MODE_CMD
    DHCP_CLIENT_IP_ADDR_MODE_INCR = "incr"
    DHCP_CLIENT_IP_ADDR_MODE_FIXED = "fixed"
    DHCP_CLIENT_IP_ADDR_MODE_LIST = "list"
    DHCP_CLIENT_IP_ADDR_MODE_DECR = "decr"

    DHCP_CLIENT_IP_ADDR_STEP_CMD = "dhcp_client_ip_addr_step"

    DHCP_CLIENT_IP_ADDR_TRACKING_CMD = "dhcp_client_ip_addr_tracking"

    DHCP_FLAGS_CMD = "dhcp_flags"
    # Constant values for DHCP_FLAGS_CMD
    DHCP_FLAGS_BROADCAST = "broadcast"
    DHCP_FLAGS_NO_BROADCAST = "no_broadcast"

    DHCP_FLAGS_MODE_CMD = "dhcp_flags_mode"
    # Constant values for DHCP_FLAGS_MODE_CMD
    DHCP_FLAGS_MODE_FIXED = "fixed"
    DHCP_FLAGS_MODE_LIST = "list"

    DHCP_FLAGS_TRACKING_CMD = "dhcp_flags_tracking"

    DHCP_HOPS_CMD = "dhcp_hops"

    DHCP_HOPS_COUNT_CMD = "dhcp_hops_count"

    DHCP_HOPS_MODE_CMD = "dhcp_hops_mode"
    # Constant values for DHCP_HOPS_MODE_CMD
    DHCP_HOPS_MODE_INCR = "incr"
    DHCP_HOPS_MODE_FIXED = "fixed"
    DHCP_HOPS_MODE_LIST = "list"
    DHCP_HOPS_MODE_DECR = "decr"

    DHCP_HOPS_STEP_CMD = "dhcp_hops_step"

    DHCP_HOPS_TRACKING_CMD = "dhcp_hops_tracking"

    DHCP_HW_LEN_CMD = "dhcp_hw_len"

    DHCP_HW_LEN_COUNT_CMD = "dhcp_hw_len_count"

    DHCP_HW_LEN_MODE_CMD = "dhcp_hw_len_mode"
    # Constant values for DHCP_HW_LEN_MODE_CMD
    DHCP_HW_LEN_MODE_INCR = "incr"
    DHCP_HW_LEN_MODE_FIXED = "fixed"
    DHCP_HW_LEN_MODE_LIST = "list"
    DHCP_HW_LEN_MODE_DECR = "decr"

    DHCP_HW_LEN_STEP_CMD = "dhcp_hw_len_step"

    DHCP_HW_LEN_TRACKING_CMD = "dhcp_hw_len_tracking"

    DHCP_HW_TYPE_CMD = "dhcp_hw_type"

    DHCP_HW_TYPE_COUNT_CMD = "dhcp_hw_type_count"

    DHCP_HW_TYPE_MODE_CMD = "dhcp_hw_type_mode"
    # Constant values for DHCP_HW_TYPE_MODE_CMD
    DHCP_HW_TYPE_MODE_INCR = "incr"
    DHCP_HW_TYPE_MODE_FIXED = "fixed"
    DHCP_HW_TYPE_MODE_LIST = "list"
    DHCP_HW_TYPE_MODE_DECR = "decr"

    DHCP_HW_TYPE_STEP_CMD = "dhcp_hw_type_step"

    DHCP_HW_TYPE_TRACKING_CMD = "dhcp_hw_type_tracking"

    DHCP_MAGIC_COOKIE_CMD = "dhcp_magic_cookie"

    DHCP_MAGIC_COOKIE_COUNT_CMD = "dhcp_magic_cookie_count"

    DHCP_MAGIC_COOKIE_MODE_CMD = "dhcp_magic_cookie_mode"
    # Constant values for DHCP_MAGIC_COOKIE_MODE_CMD
    DHCP_MAGIC_COOKIE_MODE_INCR = "incr"
    DHCP_MAGIC_COOKIE_MODE_FIXED = "fixed"
    DHCP_MAGIC_COOKIE_MODE_LIST = "list"
    DHCP_MAGIC_COOKIE_MODE_DECR = "decr"

    DHCP_MAGIC_COOKIE_STEP_CMD = "dhcp_magic_cookie_step"

    DHCP_MAGIC_COOKIE_TRACKING_CMD = "dhcp_magic_cookie_tracking"

    DHCP_OPERATION_CODE_CMD = "dhcp_operation_code"
    # Constant values for DHCP_OPERATION_CODE_CMD
    DHCP_OPERATION_CODE_REPLY = "reply"
    DHCP_OPERATION_CODE_REQUEST = "request"

    DHCP_OPERATION_CODE_MODE_CMD = "dhcp_operation_code_mode"
    # Constant values for DHCP_OPERATION_CODE_MODE_CMD
    DHCP_OPERATION_CODE_MODE_FIXED = "fixed"
    DHCP_OPERATION_CODE_MODE_LIST = "list"

    DHCP_OPERATION_CODE_TRACKING_CMD = "dhcp_operation_code_tracking"

    DHCP_OPTION_CMD = "dhcp_option"
    # Constant values for DHCP_OPTION_CMD
    DHCP_OPTION_DHCP_SUBNET_MASK = "dhcp_subnet_mask"
    DHCP_OPTION_DHCP_NETWARE_IP_DOMAIN = "dhcp_netware_ip_domain"
    DHCP_OPTION_DHCP_NAME_SERVER = "dhcp_name_server"
    DHCP_OPTION_DHCP_POP3_SVR = "dhcp_pop3_svr"
    DHCP_OPTION_DHCP_NIS_DOMAIN = "dhcp_nis_domain"
    DHCP_OPTION_DHCP_NET_BIOS_SCOPE = "dhcp_net_bios_scope"
    DHCP_OPTION_DHCP_REQUESTED_IP_ADDR = "dhcp_requested_ip_addr"
    DHCP_OPTION_DHCP_IP_FORWARDING_ENABLE = "dhcp_ip_forwarding_enable"
    DHCP_OPTION_DHCP_BOOT_FILE_NAME = "dhcp_boot_file_name"
    DHCP_OPTION_DHCP_ALL_SUBNETS_ARE_LOCAL = "dhcp_all_subnets_are_local"
    DHCP_OPTION_DHCP_PERFORM_MASK_DISCOVERY = "dhcp_perform_mask_discovery"
    DHCP_OPTION_DHCP_STATIC_ROUTE = "dhcp_static_route"
    DHCP_OPTION_DHCP_TRAILER_ENCAPSULATION = "dhcp_trailer_encapsulation"
    DHCP_OPTION_DHCP_EXTENSION_PATH = "dhcp_extension_path"
    DHCP_OPTION_DHCP_MERIT_DUMP_FILE = "dhcp_merit_dump_file"
    DHCP_OPTION_DHCP_NON_LOCAL_SRC_ROUTING_ENABLE = "dhcp_non_local_src_routing_enable"
    DHCP_OPTION_DHCP_PERFORM_ROUTER_DISCOVERY = "dhcp_perform_router_discovery"
    DHCP_OPTION_DHCP_AGENT_INFORMATION_OPTION = "dhcp_agent_information_option"
    DHCP_OPTION_DHCP_TIME_OFFSET = "dhcp_time_offset"
    DHCP_OPTION_DHCP_OPTION_OVERLOAD = "dhcp_option_overload"
    DHCP_OPTION_DHCP_TCP_KEEP_ALIVE_INTERVAL = "dhcp_tcp_keep_alive_interval"
    DHCP_OPTION_DHCP_IMPRESS_SERVER = "dhcp_impress_server"
    DHCP_OPTION_DHCP_PATH_MTU_AGING_TIMEOUT = "dhcp_path_mtu_aging_timeout"
    DHCP_OPTION_DHCP_DEFAULT_IRC_SVR = "dhcp_default_irc_svr"
    DHCP_OPTION_DHCP_MASK_SUPPLIER = "dhcp_mask_supplier"
    DHCP_OPTION_DHCP_PAD = "dhcp_pad"
    DHCP_OPTION_DHCP_ETHERNET_ENCAPSULATION = "dhcp_ethernet_encapsulation"
    DHCP_OPTION_DHCP_IP_ADDR_LEASE_TIME = "dhcp_ip_addr_lease_time"
    DHCP_OPTION_DHCP_COOKIE_SERVER = "dhcp_cookie_server"
    DHCP_OPTION_DHCP_NIS_PLUS_DOMAIN = "dhcp_nis_plus_domain"
    DHCP_OPTION_DHCP_DEFAULT_IP_TTL = "dhcp_default_ip_ttl"
    DHCP_OPTION_DHCP_GATEWAYS = "dhcp_gateways"
    DHCP_OPTION_DHCP_BROADCAST_ADDRESS = "dhcp_broadcast_address"
    DHCP_OPTION_DHCP_PARAM_REQUEST_LIST = "dhcp_param_request_list"
    DHCP_OPTION_DHCP_TFTP_SVR_NAME = "dhcp_tftp_svr_name"
    DHCP_OPTION_DHCP_RENEWAL_TIME_VALUE = "dhcp_renewal_time_value"
    DHCP_OPTION_DHCP_TIME_SERVER = "dhcp_time_server"
    DHCP_OPTION_DHCP_XWIN_SYS_FONT_SVR = "dhcp_xwin_sys_font_svr"
    DHCP_OPTION_DHCP_NET_BIOS_NAME_SVR = "dhcp_net_bios_name_svr"
    DHCP_OPTION_DHCP_INTERFACE_MTU = "dhcp_interface_mtu"
    DHCP_OPTION_DHCP_SMTP_SVR = "dhcp_smtp_svr"
    DHCP_OPTION_DHCP_PATH_MTU_PLATEAU_TABLE = "dhcp_path_mtu_plateau_table"
    DHCP_OPTION_DHCP_END = "dhcp_end"
    DHCP_OPTION_DHCP_MESSAGE = "dhcp_message"
    DHCP_OPTION_DHCP_HOST_NAME = "dhcp_host_name"
    DHCP_OPTION_DHCP_MESSAGE_TYPE = "dhcp_message_type"
    DHCP_OPTION_DHCP_NIS_PLUS_SERVER = "dhcp_nis_plus_server"
    DHCP_OPTION_DHCP_ARP_CACHE_TIMEOUT = "dhcp_arp_cache_timeout"
    DHCP_OPTION_DHCP_MAX_MESSAGE_SIZE = "dhcp_max_message_size"
    DHCP_OPTION_DHCP_DEFAULT_FINGER_SVR = "dhcp_default_finger_svr"
    DHCP_OPTION_DHCP_NET_BIOS_DATAGRAM_DIST_SVR = "dhcp_net_bios_datagram_dist_svr"
    DHCP_OPTION_DHCP_MOBILE_IP_HOME_AGENT = "dhcp_mobile_ip_home_agent"
    DHCP_OPTION_DHCP_LOG_SERVER = "dhcp_log_server"
    DHCP_OPTION_DHCP_SWAP_SERVER = "dhcp_swap_server"
    DHCP_OPTION_DHCP_NTP_SERVER = "dhcp_ntp_server"
    DHCP_OPTION_DHCP_RESOURCE_LOCATION_SERVER = "dhcp_resource_location_server"
    DHCP_OPTION_DHCP_WWW_SVR = "dhcp_www_svr"
    DHCP_OPTION_DHCP_STREET_TALK_SVR = "dhcp_street_talk_svr"
    DHCP_OPTION_DHCP_MAX_DATAGRAM_REASSEMBLY_SIZE = "dhcp_max_datagram_reassembly_size"
    DHCP_OPTION_DHCP_VENDOR_SPECIFIC_INFO = "dhcp_vendor_specific_info"
    DHCP_OPTION_DHCP_LPR_SERVER = "dhcp_lpr_server"
    DHCP_OPTION_DHCP_TCP_KEEP_GARBAGE = "dhcp_tcp_keep_garbage"
    DHCP_OPTION_DHCP_XWIN_SYS_DISPLAY_MGR = "dhcp_xwin_sys_display_mgr"
    DHCP_OPTION_DHCP_NET_BIOS_NODE_TYPE = "dhcp_net_bios_node_type"
    DHCP_OPTION_DHCP_POLICY_FILTER = "dhcp_policy_filter"
    DHCP_OPTION_DHCP_NNTP_SVR = "dhcp_nntp_svr"
    DHCP_OPTION_DHCP_SVR_IDENTIFIER = "dhcp_svr_identifier"
    DHCP_OPTION_DHCP_REBINDING_TIME_VALUE = "dhcp_rebinding_time_value"
    DHCP_OPTION_DHCP_NETWORK_IP_OPTION = "dhcp_network_ip_option"
    DHCP_OPTION_DHCP_CLIENT_ID = "dhcp_client_id"
    DHCP_OPTION_DHCP_ROUTER_SOLICIT_ADDR = "dhcp_router_solicit_addr"
    DHCP_OPTION_DHCP_ROOT_PATH = "dhcp_root_path"
    DHCP_OPTION_DHCP_TCP_DEFAULT_TTL = "dhcp_tcp_default_ttl"
    DHCP_OPTION_HCP_STDA_SVR = "hcp_stda_svr"
    DHCP_OPTION_DHCP_NIS_SERVER = "dhcp_nis_server"
    DHCP_OPTION_DHCP_BOOT_FILE_SIZE = "dhcp_boot_file_size"
    DHCP_OPTION_DHCP_DOMAIN_NAME_SERVER = "dhcp_domain_name_server"
    DHCP_OPTION_DHCP_DOMAIN_NAME = "dhcp_domain_name"
    DHCP_OPTION_DHCP_VENDOR_CLASS_ID = "dhcp_vendor_class_id"

    DHCP_OPTION_DATA_CMD = "dhcp_option_data"

    DHCP_RELAY_AGENT_IP_ADDR_CMD = "dhcp_relay_agent_ip_addr"

    DHCP_RELAY_AGENT_IP_ADDR_COUNT_CMD = "dhcp_relay_agent_ip_addr_count"

    DHCP_RELAY_AGENT_IP_ADDR_MODE_CMD = "dhcp_relay_agent_ip_addr_mode"
    # Constant values for DHCP_RELAY_AGENT_IP_ADDR_MODE_CMD
    DHCP_RELAY_AGENT_IP_ADDR_MODE_INCR = "incr"
    DHCP_RELAY_AGENT_IP_ADDR_MODE_FIXED = "fixed"
    DHCP_RELAY_AGENT_IP_ADDR_MODE_LIST = "list"
    DHCP_RELAY_AGENT_IP_ADDR_MODE_DECR = "decr"

    DHCP_RELAY_AGENT_IP_ADDR_STEP_CMD = "dhcp_relay_agent_ip_addr_step"

    DHCP_RELAY_AGENT_IP_ADDR_TRACKING_CMD = "dhcp_relay_agent_ip_addr_tracking"

    DHCP_SECONDS_CMD = "dhcp_seconds"

    DHCP_SECONDS_COUNT_CMD = "dhcp_seconds_count"

    DHCP_SECONDS_MODE_CMD = "dhcp_seconds_mode"
    # Constant values for DHCP_SECONDS_MODE_CMD
    DHCP_SECONDS_MODE_INCR = "incr"
    DHCP_SECONDS_MODE_FIXED = "fixed"
    DHCP_SECONDS_MODE_LIST = "list"
    DHCP_SECONDS_MODE_DECR = "decr"

    DHCP_SECONDS_STEP_CMD = "dhcp_seconds_step"

    DHCP_SECONDS_TRACKING_CMD = "dhcp_seconds_tracking"

    DHCP_SERVER_HOST_NAME_CMD = "dhcp_server_host_name"

    DHCP_SERVER_HOST_NAME_TRACKING_CMD = "dhcp_server_host_name_tracking"

    DHCP_SERVER_IP_ADDR_CMD = "dhcp_server_ip_addr"

    DHCP_SERVER_IP_ADDR_COUNT_CMD = "dhcp_server_ip_addr_count"

    DHCP_SERVER_IP_ADDR_MODE_CMD = "dhcp_server_ip_addr_mode"
    # Constant values for DHCP_SERVER_IP_ADDR_MODE_CMD
    DHCP_SERVER_IP_ADDR_MODE_INCR = "incr"
    DHCP_SERVER_IP_ADDR_MODE_FIXED = "fixed"
    DHCP_SERVER_IP_ADDR_MODE_LIST = "list"
    DHCP_SERVER_IP_ADDR_MODE_DECR = "decr"

    DHCP_SERVER_IP_ADDR_STEP_CMD = "dhcp_server_ip_addr_step"

    DHCP_SERVER_IP_ADDR_TRACKING_CMD = "dhcp_server_ip_addr_tracking"

    DHCP_TRANSACTION_ID_CMD = "dhcp_transaction_id"

    DHCP_TRANSACTION_ID_COUNT_CMD = "dhcp_transaction_id_count"

    DHCP_TRANSACTION_ID_MODE_CMD = "dhcp_transaction_id_mode"
    # Constant values for DHCP_TRANSACTION_ID_MODE_CMD
    DHCP_TRANSACTION_ID_MODE_INCR = "incr"
    DHCP_TRANSACTION_ID_MODE_FIXED = "fixed"
    DHCP_TRANSACTION_ID_MODE_LIST = "list"
    DHCP_TRANSACTION_ID_MODE_DECR = "decr"

    DHCP_TRANSACTION_ID_STEP_CMD = "dhcp_transaction_id_step"

    DHCP_TRANSACTION_ID_TRACKING_CMD = "dhcp_transaction_id_tracking"

    DHCP_YOUR_IP_ADDR_CMD = "dhcp_your_ip_addr"

    DHCP_YOUR_IP_ADDR_COUNT_CMD = "dhcp_your_ip_addr_count"

    DHCP_YOUR_IP_ADDR_MODE_CMD = "dhcp_your_ip_addr_mode"
    # Constant values for DHCP_YOUR_IP_ADDR_MODE_CMD
    DHCP_YOUR_IP_ADDR_MODE_INCR = "incr"
    DHCP_YOUR_IP_ADDR_MODE_FIXED = "fixed"
    DHCP_YOUR_IP_ADDR_MODE_LIST = "list"
    DHCP_YOUR_IP_ADDR_MODE_DECR = "decr"

    DHCP_YOUR_IP_ADDR_STEP_CMD = "dhcp_your_ip_addr_step"

    DHCP_YOUR_IP_ADDR_TRACKING_CMD = "dhcp_your_ip_addr_tracking"

    DISCARD_ELIGIBLE_CMD = "discard_eligible"

    DLCI_CORE_ENABLE_CMD = "dlci_core_enable"

    DLCI_CORE_VALUE_CMD = "dlci_core_value"

    DLCI_COUNT_MODE_CMD = "dlci_count_mode"
    # Constant values for DLCI_COUNT_MODE_CMD
    DLCI_COUNT_MODE_RANDOM = "random"
    DLCI_COUNT_MODE_CONT_DECREMENT = "cont_decrement"
    DLCI_COUNT_MODE_IDLE = "idle"
    DLCI_COUNT_MODE_INCREMENT = "increment"
    DLCI_COUNT_MODE_DECREMENT = "decrement"
    DLCI_COUNT_MODE_CONT_INCREMENT = "cont_increment"

    DLCI_EXTENDED_ADDRESS0_CMD = "dlci_extended_address0"

    DLCI_EXTENDED_ADDRESS1_CMD = "dlci_extended_address1"

    DLCI_EXTENDED_ADDRESS2_CMD = "dlci_extended_address2"

    DLCI_EXTENDED_ADDRESS3_CMD = "dlci_extended_address3"

    DLCI_MASK_SELECT_CMD = "dlci_mask_select"

    DLCI_MASK_VALUE_CMD = "dlci_mask_value"

    DLCI_REPEAT_COUNT_CMD = "dlci_repeat_count"

    DLCI_REPEAT_COUNT_STEP_CMD = "dlci_repeat_count_step"

    DLCI_SIZE_CMD = "dlci_size"

    DLCI_VALUE_CMD = "dlci_value"

    DLCI_VALUE_STEP_CMD = "dlci_value_step"

    DURATION_CMD = "duration"

    DYNAMIC_UPDATE_FIELDS_CMD = "dynamic_update_fields"
    # Constant values for DYNAMIC_UPDATE_FIELDS_CMD
    DYNAMIC_UPDATE_FIELDS_PPP = "ppp"
    DYNAMIC_UPDATE_FIELDS_MPLS_LABEL_VALUE = "mpls_label_value"

    EGRESS_CUSTOM_FIELD_OFFSET_CMD = "egress_custom_field_offset"

    EGRESS_CUSTOM_OFFSET_CMD = "egress_custom_offset"
    # Constant values for EGRESS_CUSTOM_OFFSET_CMD
    EGRESS_CUSTOM_OFFSET_NA = "NA"
    EGRESS_CUSTOM_OFFSET_NUMERIC = "NUMERIC"

    EGRESS_CUSTOM_WIDTH_CMD = "egress_custom_width"
    # Constant values for EGRESS_CUSTOM_WIDTH_CMD
    EGRESS_CUSTOM_WIDTH_NA = "NA"
    EGRESS_CUSTOM_WIDTH_NUMERIC = "NUMERIC"

    EGRESS_TRACKING_CMD = "egress_tracking"
    # Constant values for EGRESS_TRACKING_CMD
    EGRESS_TRACKING_OUTER_VLAN_PRIORITY = "outer_vlan_priority"
    EGRESS_TRACKING_VNTAG_LOOPED_BIT = "vnTag_looped_bit"
    EGRESS_TRACKING_OUTER_VLAN_ID_8 = "outer_vlan_id_8"
    EGRESS_TRACKING_OUTER_VLAN_ID_6 = "outer_vlan_id_6"
    EGRESS_TRACKING_OUTER_VLAN_ID_4 = "outer_vlan_id_4"
    EGRESS_TRACKING_IPV6TC = "ipv6TC"
    EGRESS_TRACKING_VNTAG_POINTER_BIT = "vnTag_pointer_bit"
    EGRESS_TRACKING_CUSTOM = "custom"
    EGRESS_TRACKING_IPV6TC_BITS_0_2 = "ipv6TC_bits_0_2"
    EGRESS_TRACKING_INNER_VLAN_PRIORITY = "inner_vlan_priority"
    EGRESS_TRACKING_IPV6TC_BITS_0_5 = "ipv6TC_bits_0_5"
    EGRESS_TRACKING_INNER_VLAN_ID_8 = "inner_vlan_id_8"
    EGRESS_TRACKING_INNER_VLAN_ID_6 = "inner_vlan_id_6"
    EGRESS_TRACKING_INNER_VLAN_ID_4 = "inner_vlan_id_4"
    EGRESS_TRACKING_CUSTOM_BY_FIELD = "custom_by_field"
    EGRESS_TRACKING_DSCP = "dscp"
    EGRESS_TRACKING_OUTER_VLAN_ID_12 = "outer_vlan_id_12"
    EGRESS_TRACKING_OUTER_VLAN_ID_10 = "outer_vlan_id_10"
    EGRESS_TRACKING_TOS_PRECEDENCE = "tos_precedence"
    EGRESS_TRACKING_VNTAG_DIRECTION_BIT = "vnTag_direction_bit"
    EGRESS_TRACKING_MPLSEXP = "mplsExp"
    EGRESS_TRACKING_INNER_VLAN_ID_10 = "inner_vlan_id_10"
    EGRESS_TRACKING_NONE = "none"
    EGRESS_TRACKING_INNER_VLAN_ID_12 = "inner_vlan_id_12"

    EGRESS_TRACKING_ENCAP_CMD = "egress_tracking_encap"
    # Constant values for EGRESS_TRACKING_ENCAP_CMD
    EGRESS_TRACKING_ENCAP_POS_PPP = "pos_ppp"
    EGRESS_TRACKING_ENCAP_FRAME_RELAY2427 = "frame_relay2427"
    EGRESS_TRACKING_ENCAP_LLCBRIDGEDETHERNETFCS = "LLCBridgedEthernetFCS"
    EGRESS_TRACKING_ENCAP_POS_HDLC = "pos_hdlc"
    EGRESS_TRACKING_ENCAP_VCCMUXBRIDGEDETHERNETNOFCS = "VccMuxBridgedEthernetNoFCS"
    EGRESS_TRACKING_ENCAP_LLCBRIDGEDETHERNETNOFCS = "LLCBridgedEthernetNoFCS"
    EGRESS_TRACKING_ENCAP_FRAME_RELAY_CISCO = "frame_relay_cisco"
    EGRESS_TRACKING_ENCAP_LLCROUTEDCLIP = "LLCRoutedCLIP"
    EGRESS_TRACKING_ENCAP_VCCMUXBRIDGEDETHERNETFCS = "VccMuxBridgedEthernetFCS"
    EGRESS_TRACKING_ENCAP_LLCPPPOA = "LLCPPPoA"
    EGRESS_TRACKING_ENCAP_FRAME_RELAY1490 = "frame_relay1490"
    EGRESS_TRACKING_ENCAP_VCCMUXPPPOA = "VccMuxPPPoA"
    EGRESS_TRACKING_ENCAP_ETHERNET = "ethernet"
    EGRESS_TRACKING_ENCAP_CUSTOM = "custom"
    EGRESS_TRACKING_ENCAP_VCCMUXIPV4ROUTED = "VccMuxIPV4Routed"

    EMULATION_DST_HANDLE_CMD = "emulation_dst_handle"

    EMULATION_DST_VLAN_PROTOCOL_TAG_ID_CMD = "emulation_dst_vlan_protocol_tag_id"

    EMULATION_MULTICAST_DST_HANDLE_CMD = "emulation_multicast_dst_handle"

    EMULATION_MULTICAST_DST_HANDLE_TYPE_CMD = "emulation_multicast_dst_handle_type"

    EMULATION_MULTICAST_RCVR_HANDLE_CMD = "emulation_multicast_rcvr_handle"

    EMULATION_MULTICAST_RCVR_HOST_INDEX_CMD = "emulation_multicast_rcvr_host_index"

    EMULATION_MULTICAST_RCVR_MCAST_INDEX_CMD = "emulation_multicast_rcvr_mcast_index"

    EMULATION_MULTICAST_RCVR_PORT_INDEX_CMD = "emulation_multicast_rcvr_port_index"

    EMULATION_OVERRIDE_PPP_IP_ADDR_CMD = "emulation_override_ppp_ip_addr"
    # Constant values for EMULATION_OVERRIDE_PPP_IP_ADDR_CMD
    EMULATION_OVERRIDE_PPP_IP_ADDR_BOTH = "both"
    EMULATION_OVERRIDE_PPP_IP_ADDR_NONE = "none"
    EMULATION_OVERRIDE_PPP_IP_ADDR_DOWNSTREAM = "downstream"
    EMULATION_OVERRIDE_PPP_IP_ADDR_UPSTREAM = "upstream"

    EMULATION_SCALABLE_DST_HANDLE_CMD = "emulation_scalable_dst_handle"

    EMULATION_SCALABLE_DST_INTF_COUNT_CMD = "emulation_scalable_dst_intf_count"

    EMULATION_SCALABLE_DST_INTF_START_CMD = "emulation_scalable_dst_intf_start"

    EMULATION_SCALABLE_DST_PORT_COUNT_CMD = "emulation_scalable_dst_port_count"

    EMULATION_SCALABLE_DST_PORT_START_CMD = "emulation_scalable_dst_port_start"

    EMULATION_SCALABLE_SRC_HANDLE_CMD = "emulation_scalable_src_handle"

    EMULATION_SCALABLE_SRC_INTF_COUNT_CMD = "emulation_scalable_src_intf_count"

    EMULATION_SCALABLE_SRC_INTF_START_CMD = "emulation_scalable_src_intf_start"

    EMULATION_SCALABLE_SRC_PORT_COUNT_CMD = "emulation_scalable_src_port_count"

    EMULATION_SCALABLE_SRC_PORT_START_CMD = "emulation_scalable_src_port_start"

    EMULATION_SRC_HANDLE_CMD = "emulation_src_handle"

    EMULATION_SRC_VLAN_PROTOCOL_TAG_ID_CMD = "emulation_src_vlan_protocol_tag_id"

    ENABLE_AUTO_DETECT_INSTRUMENTATION_CMD = "enable_auto_detect_instrumentation"

    ENABLE_CE_TO_PE_TRAFFIC_CMD = "enable_ce_to_pe_traffic"

    ENABLE_DATA_INTEGRITY_CMD = "enable_data_integrity"

    ENABLE_DYNAMIC_MPLS_LABELS_CMD = "enable_dynamic_mpls_labels"

    ENABLE_OVERRIDE_VALUE_CMD = "enable_override_value"

    ENABLE_PGID_CMD = "enable_pgid"

    ENABLE_TEST_OBJECTIVE_CMD = "enable_test_objective"

    ENABLE_TIME_STAMP_CMD = "enable_time_stamp"

    ENABLE_UDF1_CMD = "enable_udf1"

    ENABLE_UDF2_CMD = "enable_udf2"

    ENABLE_UDF3_CMD = "enable_udf3"

    ENABLE_UDF4_CMD = "enable_udf4"

    ENABLE_UDF5_CMD = "enable_udf5"

    ENDPOINTSET_COUNT_CMD = "endpointset_count"

    ENFORCE_MIN_GAP_CMD = "enforce_min_gap"

    ETHERNET_TYPE_CMD = "ethernet_type"
    # Constant values for ETHERNET_TYPE_CMD
    ETHERNET_TYPE_ETHERNETII = "ethernetII"
    ETHERNET_TYPE_IEEE8023SNAP = "ieee8023snap"
    ETHERNET_TYPE_IEEE8023 = "ieee8023"
    ETHERNET_TYPE_IEEE8022 = "ieee8022"

    ETHERNET_VALUE_CMD = "ethernet_value"

    ETHERNET_VALUE_COUNT_CMD = "ethernet_value_count"

    ETHERNET_VALUE_MODE_CMD = "ethernet_value_mode"
    # Constant values for ETHERNET_VALUE_MODE_CMD
    ETHERNET_VALUE_MODE_DEFAULT = "DEFAULT"
    ETHERNET_VALUE_MODE_INCR = "incr"
    ETHERNET_VALUE_MODE_FIXED = "fixed"
    ETHERNET_VALUE_MODE_LIST = "list"
    ETHERNET_VALUE_MODE_DECR = "decr"

    ETHERNET_VALUE_STEP_CMD = "ethernet_value_step"

    ETHERNET_VALUE_TRACKING_CMD = "ethernet_value_tracking"

    FCS_CMD = "fcs"

    FCS_TYPE_CMD = "fcs_type"
    # Constant values for FCS_TYPE_CMD
    FCS_TYPE_BAD_CRC = "bad_CRC"
    FCS_TYPE_NO_CRC = "no_CRC"
    FCS_TYPE_DRIBBLE = "dribble"
    FCS_TYPE_ALIGNMENT = "alignment"

    FECN_CMD = "fecn"

    FIELD_ACTIVEFIELDCHOICE_CMD = "field_activeFieldChoice"

    FIELD_AUTO_CMD = "field_auto"

    FIELD_COUNTVALUE_CMD = "field_countValue"

    FIELD_FIELDVALUE_CMD = "field_fieldValue"

    FIELD_FULLMESH_CMD = "field_fullMesh"

    FIELD_HANDLE_CMD = "field_handle"

    FIELD_LINKED_CMD = "field_linked"

    FIELD_LINKED_TO_CMD = "field_linked_to"

    FIELD_OPTIONALENABLED_CMD = "field_optionalEnabled"

    FIELD_SINGLEVALUE_CMD = "field_singleValue"

    FIELD_STARTVALUE_CMD = "field_startValue"

    FIELD_STEPVALUE_CMD = "field_stepValue"

    FIELD_TRACKINGENABLED_CMD = "field_trackingEnabled"

    FIELD_VALUELIST_CMD = "field_valueList"

    FIELD_VALUETYPE_CMD = "field_valueType"

    FR_RANGE_COUNT_CMD = "fr_range_count"

    FRAME_RATE_DISTRIBUTION_PORT_CMD = "frame_rate_distribution_port"
    # Constant values for FRAME_RATE_DISTRIBUTION_PORT_CMD
    FRAME_RATE_DISTRIBUTION_PORT_APPLY_TO_ALL = "apply_to_all"
    FRAME_RATE_DISTRIBUTION_PORT_SPLIT_EVENLY = "split_evenly"

    FRAME_RATE_DISTRIBUTION_STREAM_CMD = "frame_rate_distribution_stream"
    # Constant values for FRAME_RATE_DISTRIBUTION_STREAM_CMD
    FRAME_RATE_DISTRIBUTION_STREAM_APPLY_TO_ALL = "apply_to_all"
    FRAME_RATE_DISTRIBUTION_STREAM_SPLIT_EVENLY = "split_evenly"

    FRAME_SEQUENCING_CMD = "frame_sequencing"
    # Constant values for FRAME_SEQUENCING_CMD
    FRAME_SEQUENCING_ENABLE = "enable"
    FRAME_SEQUENCING_DISABLE = "disable"

    FRAME_SEQUENCING_MODE_CMD = "frame_sequencing_mode"
    # Constant values for FRAME_SEQUENCING_MODE_CMD
    FRAME_SEQUENCING_MODE_RX_SWITCHED_PATH_FIXED = "rx_switched_path_fixed"
    FRAME_SEQUENCING_MODE_RX_THRESHOLD = "rx_threshold"
    FRAME_SEQUENCING_MODE_RX_SWITCHED_PATH = "rx_switched_path"
    FRAME_SEQUENCING_MODE_ADVANCED = "advanced"

    FRAME_SEQUENCING_OFFSET_CMD = "frame_sequencing_offset"

    FRAME_SIZE_CMD = "frame_size"

    FRAME_SIZE_DISTRIBUTION_CMD = "frame_size_distribution"
    # Constant values for FRAME_SIZE_DISTRIBUTION_CMD
    FRAME_SIZE_DISTRIBUTION_CISCO = "cisco"
    FRAME_SIZE_DISTRIBUTION_TOLLY = "tolly"
    FRAME_SIZE_DISTRIBUTION_IMIX_STD = "imix_std"
    FRAME_SIZE_DISTRIBUTION_IMIX_TCP = "imix_tcp"
    FRAME_SIZE_DISTRIBUTION_IMIX_IPV6 = "imix_ipv6"
    FRAME_SIZE_DISTRIBUTION_IMIX_IPSEC = "imix_ipsec"
    FRAME_SIZE_DISTRIBUTION_TRIMODAL = "trimodal"
    FRAME_SIZE_DISTRIBUTION_QUADMODAL = "quadmodal"
    FRAME_SIZE_DISTRIBUTION_IMIX = "imix"

    FRAME_SIZE_GAUSS_CMD = "frame_size_gauss"

    FRAME_SIZE_IMIX_CMD = "frame_size_imix"

    FRAME_SIZE_MAX_CMD = "frame_size_max"

    FRAME_SIZE_MIN_CMD = "frame_size_min"

    FRAME_SIZE_STEP_CMD = "frame_size_step"

    GLOBAL_DEST_MAC_RETRY_COUNT_CMD = "global_dest_mac_retry_count"

    GLOBAL_DEST_MAC_RETRY_DELAY_CMD = "global_dest_mac_retry_delay"

    GLOBAL_DISPLAY_MPLS_CURRENT_LABEL_VALUE_CMD = "global_display_mpls_current_label_value"

    GLOBAL_ENABLE_DEST_MAC_RETRY_CMD = "global_enable_dest_mac_retry"

    GLOBAL_ENABLE_MAC_CHANGE_ON_FLY_CMD = "global_enable_mac_change_on_fly"

    GLOBAL_ENABLE_MIN_FRAME_SIZE_CMD = "global_enable_min_frame_size"

    GLOBAL_ENABLE_STAGGERED_TRANSMIT_CMD = "global_enable_staggered_transmit"

    GLOBAL_ENABLE_STREAM_ORDERING_CMD = "global_enable_stream_ordering"

    GLOBAL_FRAME_ORDERING_CMD = "global_frame_ordering"
    # Constant values for GLOBAL_FRAME_ORDERING_CMD
    GLOBAL_FRAME_ORDERING_NONE = "none"
    GLOBAL_FRAME_ORDERING_PEAK_LOADING = "peak_loading"
    GLOBAL_FRAME_ORDERING_FLOW_GROUP_SETUP = "flow_group_setup"
    GLOBAL_FRAME_ORDERING_RFC2889 = "rfc2889"

    GLOBAL_LARGE_ERROR_THRESHHOLD_CMD = "global_large_error_threshhold"

    GLOBAL_MAX_TRAFFIC_GENERATION_QUERIES_CMD = "global_max_traffic_generation_queries"

    GLOBAL_MPLS_LABEL_LEARNING_TIMEOUT_CMD = "global_mpls_label_learning_timeout"

    GLOBAL_PEAK_LOADING_REPLICATION_COUNT_CMD = "global_peak_loading_replication_count"

    GLOBAL_REFRESH_LEARNED_INFO_BEFORE_APPLY_CMD = "global_refresh_learned_info_before_apply"

    GLOBAL_STREAM_CONTROL_CMD = "global_stream_control"
    # Constant values for GLOBAL_STREAM_CONTROL_CMD
    GLOBAL_STREAM_CONTROL_CONTINUOUS = "continuous"
    GLOBAL_STREAM_CONTROL_ITERATIONS = "iterations"

    GLOBAL_STREAM_CONTROL_ITERATIONS_CMD = "global_stream_control_iterations"

    GLOBAL_USE_TX_RX_SYNC_CMD = "global_use_tx_rx_sync"

    GLOBAL_WAIT_TIME_CMD = "global_wait_time"

    GRE_CHECKSUM_CMD = "gre_checksum"

    GRE_CHECKSUM_COUNT_CMD = "gre_checksum_count"

    GRE_CHECKSUM_ENABLE_CMD = "gre_checksum_enable"

    GRE_CHECKSUM_ENABLE_MODE_CMD = "gre_checksum_enable_mode"
    # Constant values for GRE_CHECKSUM_ENABLE_MODE_CMD
    GRE_CHECKSUM_ENABLE_MODE_FIXED = "fixed"
    GRE_CHECKSUM_ENABLE_MODE_LIST = "list"

    GRE_CHECKSUM_ENABLE_TRACKING_CMD = "gre_checksum_enable_tracking"

    GRE_CHECKSUM_MODE_CMD = "gre_checksum_mode"
    # Constant values for GRE_CHECKSUM_MODE_CMD
    GRE_CHECKSUM_MODE_INCR = "incr"
    GRE_CHECKSUM_MODE_FIXED = "fixed"
    GRE_CHECKSUM_MODE_LIST = "list"
    GRE_CHECKSUM_MODE_DECR = "decr"

    GRE_CHECKSUM_STEP_CMD = "gre_checksum_step"

    GRE_CHECKSUM_TRACKING_CMD = "gre_checksum_tracking"

    GRE_KEY_CMD = "gre_key"

    GRE_KEY_COUNT_CMD = "gre_key_count"

    GRE_KEY_ENABLE_CMD = "gre_key_enable"

    GRE_KEY_ENABLE_MODE_CMD = "gre_key_enable_mode"
    # Constant values for GRE_KEY_ENABLE_MODE_CMD
    GRE_KEY_ENABLE_MODE_FIXED = "fixed"
    GRE_KEY_ENABLE_MODE_LIST = "list"

    GRE_KEY_ENABLE_TRACKING_CMD = "gre_key_enable_tracking"

    GRE_KEY_MODE_CMD = "gre_key_mode"
    # Constant values for GRE_KEY_MODE_CMD
    GRE_KEY_MODE_INCR = "incr"
    GRE_KEY_MODE_FIXED = "fixed"
    GRE_KEY_MODE_LIST = "list"
    GRE_KEY_MODE_DECR = "decr"

    GRE_KEY_STEP_CMD = "gre_key_step"

    GRE_KEY_TRACKING_CMD = "gre_key_tracking"

    GRE_RESERVED0_CMD = "gre_reserved0"

    GRE_RESERVED0_COUNT_CMD = "gre_reserved0_count"

    GRE_RESERVED0_MODE_CMD = "gre_reserved0_mode"
    # Constant values for GRE_RESERVED0_MODE_CMD
    GRE_RESERVED0_MODE_INCR = "incr"
    GRE_RESERVED0_MODE_FIXED = "fixed"
    GRE_RESERVED0_MODE_LIST = "list"
    GRE_RESERVED0_MODE_DECR = "decr"

    GRE_RESERVED0_STEP_CMD = "gre_reserved0_step"

    GRE_RESERVED0_TRACKING_CMD = "gre_reserved0_tracking"

    GRE_RESERVED1_CMD = "gre_reserved1"

    GRE_RESERVED1_COUNT_CMD = "gre_reserved1_count"

    GRE_RESERVED1_MODE_CMD = "gre_reserved1_mode"
    # Constant values for GRE_RESERVED1_MODE_CMD
    GRE_RESERVED1_MODE_INCR = "incr"
    GRE_RESERVED1_MODE_FIXED = "fixed"
    GRE_RESERVED1_MODE_LIST = "list"
    GRE_RESERVED1_MODE_DECR = "decr"

    GRE_RESERVED1_STEP_CMD = "gre_reserved1_step"

    GRE_RESERVED1_TRACKING_CMD = "gre_reserved1_tracking"

    GRE_SEQ_ENABLE_CMD = "gre_seq_enable"

    GRE_SEQ_ENABLE_MODE_CMD = "gre_seq_enable_mode"
    # Constant values for GRE_SEQ_ENABLE_MODE_CMD
    GRE_SEQ_ENABLE_MODE_FIXED = "fixed"
    GRE_SEQ_ENABLE_MODE_LIST = "list"

    GRE_SEQ_ENABLE_TRACKING_CMD = "gre_seq_enable_tracking"

    GRE_SEQ_NUMBER_CMD = "gre_seq_number"

    GRE_SEQ_NUMBER_COUNT_CMD = "gre_seq_number_count"

    GRE_SEQ_NUMBER_MODE_CMD = "gre_seq_number_mode"
    # Constant values for GRE_SEQ_NUMBER_MODE_CMD
    GRE_SEQ_NUMBER_MODE_INCR = "incr"
    GRE_SEQ_NUMBER_MODE_FIXED = "fixed"
    GRE_SEQ_NUMBER_MODE_LIST = "list"
    GRE_SEQ_NUMBER_MODE_DECR = "decr"

    GRE_SEQ_NUMBER_STEP_CMD = "gre_seq_number_step"

    GRE_SEQ_NUMBER_TRACKING_CMD = "gre_seq_number_tracking"

    GRE_VALID_CHECKSUM_ENABLE_CMD = "gre_valid_checksum_enable"

    GRE_VERSION_CMD = "gre_version"

    GRE_VERSION_COUNT_CMD = "gre_version_count"

    GRE_VERSION_MODE_CMD = "gre_version_mode"
    # Constant values for GRE_VERSION_MODE_CMD
    GRE_VERSION_MODE_INCR = "incr"
    GRE_VERSION_MODE_FIXED = "fixed"
    GRE_VERSION_MODE_LIST = "list"
    GRE_VERSION_MODE_DECR = "decr"

    GRE_VERSION_STEP_CMD = "gre_version_step"

    GRE_VERSION_TRACKING_CMD = "gre_version_tracking"

    HEADER_HANDLE_CMD = "header_handle"

    HOSTS_PER_NET_CMD = "hosts_per_net"

    ICMP_CHECKSUM_CMD = "icmp_checksum"

    ICMP_CHECKSUM_COUNT_CMD = "icmp_checksum_count"

    ICMP_CHECKSUM_MODE_CMD = "icmp_checksum_mode"
    # Constant values for ICMP_CHECKSUM_MODE_CMD
    ICMP_CHECKSUM_MODE_INCR = "incr"
    ICMP_CHECKSUM_MODE_FIXED = "fixed"
    ICMP_CHECKSUM_MODE_LIST = "list"
    ICMP_CHECKSUM_MODE_DECR = "decr"

    ICMP_CHECKSUM_STEP_CMD = "icmp_checksum_step"

    ICMP_CHECKSUM_TRACKING_CMD = "icmp_checksum_tracking"

    ICMP_CODE_CMD = "icmp_code"

    ICMP_CODE_COUNT_CMD = "icmp_code_count"

    ICMP_CODE_MODE_CMD = "icmp_code_mode"
    # Constant values for ICMP_CODE_MODE_CMD
    ICMP_CODE_MODE_INCR = "incr"
    ICMP_CODE_MODE_FIXED = "fixed"
    ICMP_CODE_MODE_LIST = "list"
    ICMP_CODE_MODE_DECR = "decr"

    ICMP_CODE_STEP_CMD = "icmp_code_step"

    ICMP_CODE_TRACKING_CMD = "icmp_code_tracking"

    ICMP_ID_CMD = "icmp_id"

    ICMP_ID_COUNT_CMD = "icmp_id_count"

    ICMP_ID_MODE_CMD = "icmp_id_mode"
    # Constant values for ICMP_ID_MODE_CMD
    ICMP_ID_MODE_INCR = "incr"
    ICMP_ID_MODE_FIXED = "fixed"
    ICMP_ID_MODE_LIST = "list"
    ICMP_ID_MODE_DECR = "decr"

    ICMP_ID_STEP_CMD = "icmp_id_step"

    ICMP_ID_TRACKING_CMD = "icmp_id_tracking"

    ICMP_MAX_RESPONSE_DELAY_MS_CMD = "icmp_max_response_delay_ms"

    ICMP_MAX_RESPONSE_DELAY_MS_COUNT_CMD = "icmp_max_response_delay_ms_count"

    ICMP_MAX_RESPONSE_DELAY_MS_MODE_CMD = "icmp_max_response_delay_ms_mode"
    # Constant values for ICMP_MAX_RESPONSE_DELAY_MS_MODE_CMD
    ICMP_MAX_RESPONSE_DELAY_MS_MODE_INCR = "incr"
    ICMP_MAX_RESPONSE_DELAY_MS_MODE_FIXED = "fixed"
    ICMP_MAX_RESPONSE_DELAY_MS_MODE_LIST = "list"
    ICMP_MAX_RESPONSE_DELAY_MS_MODE_DECR = "decr"

    ICMP_MAX_RESPONSE_DELAY_MS_STEP_CMD = "icmp_max_response_delay_ms_step"

    ICMP_MAX_RESPONSE_DELAY_MS_TRACKING_CMD = "icmp_max_response_delay_ms_tracking"

    ICMP_MC_QUERY_V2_INTERVAL_CODE_CMD = "icmp_mc_query_v2_interval_code"

    ICMP_MC_QUERY_V2_INTERVAL_CODE_COUNT_CMD = "icmp_mc_query_v2_interval_code_count"

    ICMP_MC_QUERY_V2_INTERVAL_CODE_MODE_CMD = "icmp_mc_query_v2_interval_code_mode"
    # Constant values for ICMP_MC_QUERY_V2_INTERVAL_CODE_MODE_CMD
    ICMP_MC_QUERY_V2_INTERVAL_CODE_MODE_INCR = "incr"
    ICMP_MC_QUERY_V2_INTERVAL_CODE_MODE_FIXED = "fixed"
    ICMP_MC_QUERY_V2_INTERVAL_CODE_MODE_LIST = "list"
    ICMP_MC_QUERY_V2_INTERVAL_CODE_MODE_DECR = "decr"

    ICMP_MC_QUERY_V2_INTERVAL_CODE_STEP_CMD = "icmp_mc_query_v2_interval_code_step"

    ICMP_MC_QUERY_V2_INTERVAL_CODE_TRACKING_CMD = "icmp_mc_query_v2_interval_code_tracking"

    ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_CMD = "icmp_mc_query_v2_robustness_var"

    ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_COUNT_CMD = "icmp_mc_query_v2_robustness_var_count"

    ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_MODE_CMD = "icmp_mc_query_v2_robustness_var_mode"
    # Constant values for ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_MODE_CMD
    ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_MODE_INCR = "incr"
    ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_MODE_FIXED = "fixed"
    ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_MODE_LIST = "list"
    ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_MODE_DECR = "decr"

    ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_STEP_CMD = "icmp_mc_query_v2_robustness_var_step"

    ICMP_MC_QUERY_V2_ROBUSTNESS_VAR_TRACKING_CMD = "icmp_mc_query_v2_robustness_var_tracking"

    ICMP_MC_QUERY_V2_S_FLAG_CMD = "icmp_mc_query_v2_s_flag"

    ICMP_MC_QUERY_V2_S_FLAG_MODE_CMD = "icmp_mc_query_v2_s_flag_mode"
    # Constant values for ICMP_MC_QUERY_V2_S_FLAG_MODE_CMD
    ICMP_MC_QUERY_V2_S_FLAG_MODE_FIXED = "fixed"
    ICMP_MC_QUERY_V2_S_FLAG_MODE_LIST = "list"

    ICMP_MC_QUERY_V2_S_FLAG_TRACKING_CMD = "icmp_mc_query_v2_s_flag_tracking"

    ICMP_MOBILE_PAM_M_BIT_CMD = "icmp_mobile_pam_m_bit"

    ICMP_MOBILE_PAM_M_BIT_MODE_CMD = "icmp_mobile_pam_m_bit_mode"
    # Constant values for ICMP_MOBILE_PAM_M_BIT_MODE_CMD
    ICMP_MOBILE_PAM_M_BIT_MODE_FIXED = "fixed"
    ICMP_MOBILE_PAM_M_BIT_MODE_LIST = "list"

    ICMP_MOBILE_PAM_M_BIT_TRACKING_CMD = "icmp_mobile_pam_m_bit_tracking"

    ICMP_MOBILE_PAM_O_BIT_CMD = "icmp_mobile_pam_o_bit"

    ICMP_MOBILE_PAM_O_BIT_MODE_CMD = "icmp_mobile_pam_o_bit_mode"
    # Constant values for ICMP_MOBILE_PAM_O_BIT_MODE_CMD
    ICMP_MOBILE_PAM_O_BIT_MODE_FIXED = "fixed"
    ICMP_MOBILE_PAM_O_BIT_MODE_LIST = "list"

    ICMP_MOBILE_PAM_O_BIT_TRACKING_CMD = "icmp_mobile_pam_o_bit_tracking"

    ICMP_MULTICAST_ADDRESS_CMD = "icmp_multicast_address"

    ICMP_MULTICAST_ADDRESS_COUNT_CMD = "icmp_multicast_address_count"

    ICMP_MULTICAST_ADDRESS_MODE_CMD = "icmp_multicast_address_mode"
    # Constant values for ICMP_MULTICAST_ADDRESS_MODE_CMD
    ICMP_MULTICAST_ADDRESS_MODE_INCR = "incr"
    ICMP_MULTICAST_ADDRESS_MODE_FIXED = "fixed"
    ICMP_MULTICAST_ADDRESS_MODE_LIST = "list"
    ICMP_MULTICAST_ADDRESS_MODE_DECR = "decr"

    ICMP_MULTICAST_ADDRESS_STEP_CMD = "icmp_multicast_address_step"

    ICMP_MULTICAST_ADDRESS_TRACKING_CMD = "icmp_multicast_address_tracking"

    ICMP_NDP_NAM_O_FLAG_CMD = "icmp_ndp_nam_o_flag"

    ICMP_NDP_NAM_O_FLAG_MODE_CMD = "icmp_ndp_nam_o_flag_mode"
    # Constant values for ICMP_NDP_NAM_O_FLAG_MODE_CMD
    ICMP_NDP_NAM_O_FLAG_MODE_FIXED = "fixed"
    ICMP_NDP_NAM_O_FLAG_MODE_LIST = "list"

    ICMP_NDP_NAM_O_FLAG_TRACKING_CMD = "icmp_ndp_nam_o_flag_tracking"

    ICMP_NDP_NAM_R_FLAG_CMD = "icmp_ndp_nam_r_flag"

    ICMP_NDP_NAM_R_FLAG_MODE_CMD = "icmp_ndp_nam_r_flag_mode"
    # Constant values for ICMP_NDP_NAM_R_FLAG_MODE_CMD
    ICMP_NDP_NAM_R_FLAG_MODE_FIXED = "fixed"
    ICMP_NDP_NAM_R_FLAG_MODE_LIST = "list"

    ICMP_NDP_NAM_R_FLAG_TRACKING_CMD = "icmp_ndp_nam_r_flag_tracking"

    ICMP_NDP_NAM_S_FLAG_CMD = "icmp_ndp_nam_s_flag"

    ICMP_NDP_NAM_S_FLAG_MODE_CMD = "icmp_ndp_nam_s_flag_mode"
    # Constant values for ICMP_NDP_NAM_S_FLAG_MODE_CMD
    ICMP_NDP_NAM_S_FLAG_MODE_FIXED = "fixed"
    ICMP_NDP_NAM_S_FLAG_MODE_LIST = "list"

    ICMP_NDP_NAM_S_FLAG_TRACKING_CMD = "icmp_ndp_nam_s_flag_tracking"

    ICMP_NDP_RAM_H_FLAG_CMD = "icmp_ndp_ram_h_flag"

    ICMP_NDP_RAM_H_FLAG_MODE_CMD = "icmp_ndp_ram_h_flag_mode"
    # Constant values for ICMP_NDP_RAM_H_FLAG_MODE_CMD
    ICMP_NDP_RAM_H_FLAG_MODE_FIXED = "fixed"
    ICMP_NDP_RAM_H_FLAG_MODE_LIST = "list"

    ICMP_NDP_RAM_H_FLAG_TRACKING_CMD = "icmp_ndp_ram_h_flag_tracking"

    ICMP_NDP_RAM_HOP_LIMIT_CMD = "icmp_ndp_ram_hop_limit"

    ICMP_NDP_RAM_HOP_LIMIT_COUNT_CMD = "icmp_ndp_ram_hop_limit_count"

    ICMP_NDP_RAM_HOP_LIMIT_MODE_CMD = "icmp_ndp_ram_hop_limit_mode"
    # Constant values for ICMP_NDP_RAM_HOP_LIMIT_MODE_CMD
    ICMP_NDP_RAM_HOP_LIMIT_MODE_INCR = "incr"
    ICMP_NDP_RAM_HOP_LIMIT_MODE_FIXED = "fixed"
    ICMP_NDP_RAM_HOP_LIMIT_MODE_LIST = "list"
    ICMP_NDP_RAM_HOP_LIMIT_MODE_DECR = "decr"

    ICMP_NDP_RAM_HOP_LIMIT_STEP_CMD = "icmp_ndp_ram_hop_limit_step"

    ICMP_NDP_RAM_HOP_LIMIT_TRACKING_CMD = "icmp_ndp_ram_hop_limit_tracking"

    ICMP_NDP_RAM_M_FLAG_CMD = "icmp_ndp_ram_m_flag"

    ICMP_NDP_RAM_M_FLAG_MODE_CMD = "icmp_ndp_ram_m_flag_mode"
    # Constant values for ICMP_NDP_RAM_M_FLAG_MODE_CMD
    ICMP_NDP_RAM_M_FLAG_MODE_FIXED = "fixed"
    ICMP_NDP_RAM_M_FLAG_MODE_LIST = "list"

    ICMP_NDP_RAM_M_FLAG_TRACKING_CMD = "icmp_ndp_ram_m_flag_tracking"

    ICMP_NDP_RAM_O_FLAG_CMD = "icmp_ndp_ram_o_flag"

    ICMP_NDP_RAM_O_FLAG_MODE_CMD = "icmp_ndp_ram_o_flag_mode"
    # Constant values for ICMP_NDP_RAM_O_FLAG_MODE_CMD
    ICMP_NDP_RAM_O_FLAG_MODE_FIXED = "fixed"
    ICMP_NDP_RAM_O_FLAG_MODE_LIST = "list"

    ICMP_NDP_RAM_O_FLAG_TRACKING_CMD = "icmp_ndp_ram_o_flag_tracking"

    ICMP_NDP_RAM_REACHABLE_TIME_CMD = "icmp_ndp_ram_reachable_time"

    ICMP_NDP_RAM_REACHABLE_TIME_COUNT_CMD = "icmp_ndp_ram_reachable_time_count"

    ICMP_NDP_RAM_REACHABLE_TIME_MODE_CMD = "icmp_ndp_ram_reachable_time_mode"
    # Constant values for ICMP_NDP_RAM_REACHABLE_TIME_MODE_CMD
    ICMP_NDP_RAM_REACHABLE_TIME_MODE_INCR = "incr"
    ICMP_NDP_RAM_REACHABLE_TIME_MODE_FIXED = "fixed"
    ICMP_NDP_RAM_REACHABLE_TIME_MODE_LIST = "list"
    ICMP_NDP_RAM_REACHABLE_TIME_MODE_DECR = "decr"

    ICMP_NDP_RAM_REACHABLE_TIME_STEP_CMD = "icmp_ndp_ram_reachable_time_step"

    ICMP_NDP_RAM_REACHABLE_TIME_TRACKING_CMD = "icmp_ndp_ram_reachable_time_tracking"

    ICMP_NDP_RAM_RETRANSMIT_TIMER_CMD = "icmp_ndp_ram_retransmit_timer"

    ICMP_NDP_RAM_RETRANSMIT_TIMER_COUNT_CMD = "icmp_ndp_ram_retransmit_timer_count"

    ICMP_NDP_RAM_RETRANSMIT_TIMER_MODE_CMD = "icmp_ndp_ram_retransmit_timer_mode"
    # Constant values for ICMP_NDP_RAM_RETRANSMIT_TIMER_MODE_CMD
    ICMP_NDP_RAM_RETRANSMIT_TIMER_MODE_INCR = "incr"
    ICMP_NDP_RAM_RETRANSMIT_TIMER_MODE_FIXED = "fixed"
    ICMP_NDP_RAM_RETRANSMIT_TIMER_MODE_LIST = "list"
    ICMP_NDP_RAM_RETRANSMIT_TIMER_MODE_DECR = "decr"

    ICMP_NDP_RAM_RETRANSMIT_TIMER_STEP_CMD = "icmp_ndp_ram_retransmit_timer_step"

    ICMP_NDP_RAM_RETRANSMIT_TIMER_TRACKING_CMD = "icmp_ndp_ram_retransmit_timer_tracking"

    ICMP_NDP_RAM_ROUTER_LIFETIME_CMD = "icmp_ndp_ram_router_lifetime"

    ICMP_NDP_RAM_ROUTER_LIFETIME_COUNT_CMD = "icmp_ndp_ram_router_lifetime_count"

    ICMP_NDP_RAM_ROUTER_LIFETIME_MODE_CMD = "icmp_ndp_ram_router_lifetime_mode"
    # Constant values for ICMP_NDP_RAM_ROUTER_LIFETIME_MODE_CMD
    ICMP_NDP_RAM_ROUTER_LIFETIME_MODE_INCR = "incr"
    ICMP_NDP_RAM_ROUTER_LIFETIME_MODE_FIXED = "fixed"
    ICMP_NDP_RAM_ROUTER_LIFETIME_MODE_LIST = "list"
    ICMP_NDP_RAM_ROUTER_LIFETIME_MODE_DECR = "decr"

    ICMP_NDP_RAM_ROUTER_LIFETIME_STEP_CMD = "icmp_ndp_ram_router_lifetime_step"

    ICMP_NDP_RAM_ROUTER_LIFETIME_TRACKING_CMD = "icmp_ndp_ram_router_lifetime_tracking"

    ICMP_NDP_RM_DEST_ADDR_CMD = "icmp_ndp_rm_dest_addr"

    ICMP_NDP_RM_DEST_ADDR_COUNT_CMD = "icmp_ndp_rm_dest_addr_count"

    ICMP_NDP_RM_DEST_ADDR_MODE_CMD = "icmp_ndp_rm_dest_addr_mode"
    # Constant values for ICMP_NDP_RM_DEST_ADDR_MODE_CMD
    ICMP_NDP_RM_DEST_ADDR_MODE_INCR = "incr"
    ICMP_NDP_RM_DEST_ADDR_MODE_FIXED = "fixed"
    ICMP_NDP_RM_DEST_ADDR_MODE_LIST = "list"
    ICMP_NDP_RM_DEST_ADDR_MODE_DECR = "decr"

    ICMP_NDP_RM_DEST_ADDR_STEP_CMD = "icmp_ndp_rm_dest_addr_step"

    ICMP_NDP_RM_DEST_ADDR_TRACKING_CMD = "icmp_ndp_rm_dest_addr_tracking"

    ICMP_PARAM_PROBLEM_MESSAGE_POINTER_CMD = "icmp_param_problem_message_pointer"

    ICMP_PARAM_PROBLEM_MESSAGE_POINTER_COUNT_CMD = "icmp_param_problem_message_pointer_count"

    ICMP_PARAM_PROBLEM_MESSAGE_POINTER_MODE_CMD = "icmp_param_problem_message_pointer_mode"
    # Constant values for ICMP_PARAM_PROBLEM_MESSAGE_POINTER_MODE_CMD
    ICMP_PARAM_PROBLEM_MESSAGE_POINTER_MODE_INCR = "incr"
    ICMP_PARAM_PROBLEM_MESSAGE_POINTER_MODE_FIXED = "fixed"
    ICMP_PARAM_PROBLEM_MESSAGE_POINTER_MODE_LIST = "list"
    ICMP_PARAM_PROBLEM_MESSAGE_POINTER_MODE_DECR = "decr"

    ICMP_PARAM_PROBLEM_MESSAGE_POINTER_STEP_CMD = "icmp_param_problem_message_pointer_step"

    ICMP_PARAM_PROBLEM_MESSAGE_POINTER_TRACKING_CMD = "icmp_param_problem_message_pointer_tracking"

    ICMP_PKT_TOO_BIG_MTU_CMD = "icmp_pkt_too_big_mtu"

    ICMP_PKT_TOO_BIG_MTU_COUNT_CMD = "icmp_pkt_too_big_mtu_count"

    ICMP_PKT_TOO_BIG_MTU_MODE_CMD = "icmp_pkt_too_big_mtu_mode"
    # Constant values for ICMP_PKT_TOO_BIG_MTU_MODE_CMD
    ICMP_PKT_TOO_BIG_MTU_MODE_INCR = "incr"
    ICMP_PKT_TOO_BIG_MTU_MODE_FIXED = "fixed"
    ICMP_PKT_TOO_BIG_MTU_MODE_LIST = "list"
    ICMP_PKT_TOO_BIG_MTU_MODE_DECR = "decr"

    ICMP_PKT_TOO_BIG_MTU_STEP_CMD = "icmp_pkt_too_big_mtu_step"

    ICMP_PKT_TOO_BIG_MTU_TRACKING_CMD = "icmp_pkt_too_big_mtu_tracking"

    ICMP_SEQ_CMD = "icmp_seq"

    ICMP_SEQ_COUNT_CMD = "icmp_seq_count"

    ICMP_SEQ_MODE_CMD = "icmp_seq_mode"
    # Constant values for ICMP_SEQ_MODE_CMD
    ICMP_SEQ_MODE_INCR = "incr"
    ICMP_SEQ_MODE_FIXED = "fixed"
    ICMP_SEQ_MODE_LIST = "list"
    ICMP_SEQ_MODE_DECR = "decr"

    ICMP_SEQ_STEP_CMD = "icmp_seq_step"

    ICMP_SEQ_TRACKING_CMD = "icmp_seq_tracking"

    ICMP_TARGET_ADDR_CMD = "icmp_target_addr"

    ICMP_TARGET_ADDR_COUNT_CMD = "icmp_target_addr_count"

    ICMP_TARGET_ADDR_MODE_CMD = "icmp_target_addr_mode"
    # Constant values for ICMP_TARGET_ADDR_MODE_CMD
    ICMP_TARGET_ADDR_MODE_INCR = "incr"
    ICMP_TARGET_ADDR_MODE_FIXED = "fixed"
    ICMP_TARGET_ADDR_MODE_LIST = "list"
    ICMP_TARGET_ADDR_MODE_DECR = "decr"

    ICMP_TARGET_ADDR_STEP_CMD = "icmp_target_addr_step"

    ICMP_TARGET_ADDR_TRACKING_CMD = "icmp_target_addr_tracking"

    ICMP_TYPE_CMD = "icmp_type"

    ICMP_TYPE_COUNT_CMD = "icmp_type_count"

    ICMP_TYPE_MODE_CMD = "icmp_type_mode"
    # Constant values for ICMP_TYPE_MODE_CMD
    ICMP_TYPE_MODE_INCR = "incr"
    ICMP_TYPE_MODE_FIXED = "fixed"
    ICMP_TYPE_MODE_LIST = "list"
    ICMP_TYPE_MODE_DECR = "decr"

    ICMP_TYPE_STEP_CMD = "icmp_type_step"

    ICMP_TYPE_TRACKING_CMD = "icmp_type_tracking"

    ICMP_UNUSED_CMD = "icmp_unused"

    ICMP_UNUSED_COUNT_CMD = "icmp_unused_count"

    ICMP_UNUSED_MODE_CMD = "icmp_unused_mode"
    # Constant values for ICMP_UNUSED_MODE_CMD
    ICMP_UNUSED_MODE_INCR = "incr"
    ICMP_UNUSED_MODE_FIXED = "fixed"
    ICMP_UNUSED_MODE_LIST = "list"
    ICMP_UNUSED_MODE_DECR = "decr"

    ICMP_UNUSED_STEP_CMD = "icmp_unused_step"

    ICMP_UNUSED_TRACKING_CMD = "icmp_unused_tracking"

    IGMP_AUX_DATA_LENGTH_CMD = "igmp_aux_data_length"

    IGMP_AUX_DATA_LENGTH_COUNT_CMD = "igmp_aux_data_length_count"

    IGMP_AUX_DATA_LENGTH_MODE_CMD = "igmp_aux_data_length_mode"
    # Constant values for IGMP_AUX_DATA_LENGTH_MODE_CMD
    IGMP_AUX_DATA_LENGTH_MODE_INCR = "incr"
    IGMP_AUX_DATA_LENGTH_MODE_FIXED = "fixed"
    IGMP_AUX_DATA_LENGTH_MODE_LIST = "list"
    IGMP_AUX_DATA_LENGTH_MODE_DECR = "decr"

    IGMP_AUX_DATA_LENGTH_STEP_CMD = "igmp_aux_data_length_step"

    IGMP_AUX_DATA_LENGTH_TRACKING_CMD = "igmp_aux_data_length_tracking"

    IGMP_CHECKSUM_CMD = "igmp_checksum"

    IGMP_CHECKSUM_COUNT_CMD = "igmp_checksum_count"

    IGMP_CHECKSUM_MODE_CMD = "igmp_checksum_mode"
    # Constant values for IGMP_CHECKSUM_MODE_CMD
    IGMP_CHECKSUM_MODE_INCR = "incr"
    IGMP_CHECKSUM_MODE_FIXED = "fixed"
    IGMP_CHECKSUM_MODE_LIST = "list"
    IGMP_CHECKSUM_MODE_DECR = "decr"

    IGMP_CHECKSUM_STEP_CMD = "igmp_checksum_step"

    IGMP_CHECKSUM_TRACKING_CMD = "igmp_checksum_tracking"

    IGMP_DATA_V3R_CMD = "igmp_data_v3r"

    IGMP_DATA_V3R_COUNT_CMD = "igmp_data_v3r_count"

    IGMP_DATA_V3R_MODE_CMD = "igmp_data_v3r_mode"
    # Constant values for IGMP_DATA_V3R_MODE_CMD
    IGMP_DATA_V3R_MODE_INCR = "incr"
    IGMP_DATA_V3R_MODE_FIXED = "fixed"
    IGMP_DATA_V3R_MODE_LIST = "list"
    IGMP_DATA_V3R_MODE_DECR = "decr"

    IGMP_DATA_V3R_STEP_CMD = "igmp_data_v3r_step"

    IGMP_DATA_V3R_TRACKING_CMD = "igmp_data_v3r_tracking"

    IGMP_GROUP_ADDR_CMD = "igmp_group_addr"

    IGMP_GROUP_COUNT_CMD = "igmp_group_count"

    IGMP_GROUP_MODE_CMD = "igmp_group_mode"
    # Constant values for IGMP_GROUP_MODE_CMD
    IGMP_GROUP_MODE_DECREMENT = "decrement"
    IGMP_GROUP_MODE_FIXED = "fixed"
    IGMP_GROUP_MODE_INCREMENT = "increment"

    IGMP_GROUP_STEP_CMD = "igmp_group_step"

    IGMP_GROUP_TRACKING_CMD = "igmp_group_tracking"

    IGMP_LENGTH_V3R_CMD = "igmp_length_v3r"

    IGMP_LENGTH_V3R_COUNT_CMD = "igmp_length_v3r_count"

    IGMP_LENGTH_V3R_MODE_CMD = "igmp_length_v3r_mode"
    # Constant values for IGMP_LENGTH_V3R_MODE_CMD
    IGMP_LENGTH_V3R_MODE_INCR = "incr"
    IGMP_LENGTH_V3R_MODE_FIXED = "fixed"
    IGMP_LENGTH_V3R_MODE_LIST = "list"
    IGMP_LENGTH_V3R_MODE_DECR = "decr"

    IGMP_LENGTH_V3R_STEP_CMD = "igmp_length_v3r_step"

    IGMP_LENGTH_V3R_TRACKING_CMD = "igmp_length_v3r_tracking"

    IGMP_MAX_RESPONSE_TIME_CMD = "igmp_max_response_time"

    IGMP_MAX_RESPONSE_TIME_COUNT_CMD = "igmp_max_response_time_count"

    IGMP_MAX_RESPONSE_TIME_MODE_CMD = "igmp_max_response_time_mode"
    # Constant values for IGMP_MAX_RESPONSE_TIME_MODE_CMD
    IGMP_MAX_RESPONSE_TIME_MODE_INCR = "incr"
    IGMP_MAX_RESPONSE_TIME_MODE_FIXED = "fixed"
    IGMP_MAX_RESPONSE_TIME_MODE_LIST = "list"
    IGMP_MAX_RESPONSE_TIME_MODE_DECR = "decr"

    IGMP_MAX_RESPONSE_TIME_STEP_CMD = "igmp_max_response_time_step"

    IGMP_MAX_RESPONSE_TIME_TRACKING_CMD = "igmp_max_response_time_tracking"

    IGMP_MSG_TYPE_CMD = "igmp_msg_type"

    IGMP_MSG_TYPE_TRACKING_CMD = "igmp_msg_type_tracking"

    IGMP_MULTICAST_SRC_CMD = "igmp_multicast_src"

    IGMP_MULTICAST_SRC_COUNT_CMD = "igmp_multicast_src_count"

    IGMP_MULTICAST_SRC_MODE_CMD = "igmp_multicast_src_mode"

    IGMP_MULTICAST_SRC_STEP_CMD = "igmp_multicast_src_step"

    IGMP_MULTICAST_SRC_TRACKING_CMD = "igmp_multicast_src_tracking"

    IGMP_QQIC_CMD = "igmp_qqic"

    IGMP_QQIC_COUNT_CMD = "igmp_qqic_count"

    IGMP_QQIC_MODE_CMD = "igmp_qqic_mode"
    # Constant values for IGMP_QQIC_MODE_CMD
    IGMP_QQIC_MODE_INCR = "incr"
    IGMP_QQIC_MODE_FIXED = "fixed"
    IGMP_QQIC_MODE_LIST = "list"
    IGMP_QQIC_MODE_DECR = "decr"

    IGMP_QQIC_STEP_CMD = "igmp_qqic_step"

    IGMP_QQIC_TRACKING_CMD = "igmp_qqic_tracking"

    IGMP_QRV_CMD = "igmp_qrv"

    IGMP_QRV_COUNT_CMD = "igmp_qrv_count"

    IGMP_QRV_MODE_CMD = "igmp_qrv_mode"
    # Constant values for IGMP_QRV_MODE_CMD
    IGMP_QRV_MODE_INCR = "incr"
    IGMP_QRV_MODE_FIXED = "fixed"
    IGMP_QRV_MODE_LIST = "list"
    IGMP_QRV_MODE_DECR = "decr"

    IGMP_QRV_STEP_CMD = "igmp_qrv_step"

    IGMP_QRV_TRACKING_CMD = "igmp_qrv_tracking"

    IGMP_RECORD_TYPE_CMD = "igmp_record_type"
    # Constant values for IGMP_RECORD_TYPE_CMD
    IGMP_RECORD_TYPE_MODE_IS_EXCLUDE = "mode_is_exclude"
    IGMP_RECORD_TYPE_CHANGE_TO_EXCLUDE_MODE = "change_to_exclude_mode"
    IGMP_RECORD_TYPE_ALLOW_NEW_SOURCES = "allow_new_sources"
    IGMP_RECORD_TYPE_CHANGE_TO_INCLUDE_MODE = "change_to_include_mode"
    IGMP_RECORD_TYPE_MODE_IS_INCLUDE = "mode_is_include"
    IGMP_RECORD_TYPE_BLOCK_OLD_SOURCES = "block_old_sources"

    IGMP_RECORD_TYPE_MODE_CMD = "igmp_record_type_mode"
    # Constant values for IGMP_RECORD_TYPE_MODE_CMD
    IGMP_RECORD_TYPE_MODE_FIXED = "fixed"
    IGMP_RECORD_TYPE_MODE_LIST = "list"

    IGMP_RECORD_TYPE_TRACKING_CMD = "igmp_record_type_tracking"

    IGMP_RESERVED_V3Q_CMD = "igmp_reserved_v3q"

    IGMP_RESERVED_V3Q_COUNT_CMD = "igmp_reserved_v3q_count"

    IGMP_RESERVED_V3Q_MODE_CMD = "igmp_reserved_v3q_mode"
    # Constant values for IGMP_RESERVED_V3Q_MODE_CMD
    IGMP_RESERVED_V3Q_MODE_INCR = "incr"
    IGMP_RESERVED_V3Q_MODE_FIXED = "fixed"
    IGMP_RESERVED_V3Q_MODE_LIST = "list"
    IGMP_RESERVED_V3Q_MODE_DECR = "decr"

    IGMP_RESERVED_V3Q_STEP_CMD = "igmp_reserved_v3q_step"

    IGMP_RESERVED_V3Q_TRACKING_CMD = "igmp_reserved_v3q_tracking"

    IGMP_RESERVED_V3R1_CMD = "igmp_reserved_v3r1"

    IGMP_RESERVED_V3R1_COUNT_CMD = "igmp_reserved_v3r1_count"

    IGMP_RESERVED_V3R1_MODE_CMD = "igmp_reserved_v3r1_mode"
    # Constant values for IGMP_RESERVED_V3R1_MODE_CMD
    IGMP_RESERVED_V3R1_MODE_INCR = "incr"
    IGMP_RESERVED_V3R1_MODE_FIXED = "fixed"
    IGMP_RESERVED_V3R1_MODE_LIST = "list"
    IGMP_RESERVED_V3R1_MODE_DECR = "decr"

    IGMP_RESERVED_V3R1_STEP_CMD = "igmp_reserved_v3r1_step"

    IGMP_RESERVED_V3R1_TRACKING_CMD = "igmp_reserved_v3r1_tracking"

    IGMP_RESERVED_V3R2_CMD = "igmp_reserved_v3r2"

    IGMP_RESERVED_V3R2_COUNT_CMD = "igmp_reserved_v3r2_count"

    IGMP_RESERVED_V3R2_MODE_CMD = "igmp_reserved_v3r2_mode"
    # Constant values for IGMP_RESERVED_V3R2_MODE_CMD
    IGMP_RESERVED_V3R2_MODE_INCR = "incr"
    IGMP_RESERVED_V3R2_MODE_FIXED = "fixed"
    IGMP_RESERVED_V3R2_MODE_LIST = "list"
    IGMP_RESERVED_V3R2_MODE_DECR = "decr"

    IGMP_RESERVED_V3R2_STEP_CMD = "igmp_reserved_v3r2_step"

    IGMP_RESERVED_V3R2_TRACKING_CMD = "igmp_reserved_v3r2_tracking"

    IGMP_S_FLAG_CMD = "igmp_s_flag"

    IGMP_S_FLAG_MODE_CMD = "igmp_s_flag_mode"
    # Constant values for IGMP_S_FLAG_MODE_CMD
    IGMP_S_FLAG_MODE_FIXED = "fixed"
    IGMP_S_FLAG_MODE_LIST = "list"

    IGMP_S_FLAG_TRACKING_CMD = "igmp_s_flag_tracking"

    IGMP_TYPE_CMD = "igmp_type"
    # Constant values for IGMP_TYPE_CMD
    IGMP_TYPE_MEMBERSHIP_REPORT = "membership_report"
    IGMP_TYPE_MEMBERSHIP_QUERY = "membership_query"
    IGMP_TYPE_LEAVE_GROUP = "leave_group"
    IGMP_TYPE_DVMRP = "dvmrp"

    IGMP_UNUSED_CMD = "igmp_unused"

    IGMP_UNUSED_COUNT_CMD = "igmp_unused_count"

    IGMP_UNUSED_MODE_CMD = "igmp_unused_mode"
    # Constant values for IGMP_UNUSED_MODE_CMD
    IGMP_UNUSED_MODE_INCR = "incr"
    IGMP_UNUSED_MODE_FIXED = "fixed"
    IGMP_UNUSED_MODE_LIST = "list"
    IGMP_UNUSED_MODE_DECR = "decr"

    IGMP_UNUSED_STEP_CMD = "igmp_unused_step"

    IGMP_UNUSED_TRACKING_CMD = "igmp_unused_tracking"

    IGMP_VALID_CHECKSUM_CMD = "igmp_valid_checksum"

    IGMP_VERSION_CMD = "igmp_version"
    # Constant values for IGMP_VERSION_CMD
    IGMP_VERSION_1 = "1"
    IGMP_VERSION_3 = "3"
    IGMP_VERSION_2 = "2"

    INDIRECT_CMD = "indirect"

    INNER_IP_DST_ADDR_CMD = "inner_ip_dst_addr"

    INNER_IP_DST_COUNT_CMD = "inner_ip_dst_count"

    INNER_IP_DST_MODE_CMD = "inner_ip_dst_mode"
    # Constant values for INNER_IP_DST_MODE_CMD
    INNER_IP_DST_MODE_RANDOM = "random"
    INNER_IP_DST_MODE_DECREMENT = "decrement"
    INNER_IP_DST_MODE_FIXED = "fixed"
    INNER_IP_DST_MODE_INCREMENT = "increment"

    INNER_IP_DST_STEP_CMD = "inner_ip_dst_step"

    INNER_IP_DST_TRACKING_CMD = "inner_ip_dst_tracking"

    INNER_IP_SRC_ADDR_CMD = "inner_ip_src_addr"

    INNER_IP_SRC_COUNT_CMD = "inner_ip_src_count"

    INNER_IP_SRC_MODE_CMD = "inner_ip_src_mode"
    # Constant values for INNER_IP_SRC_MODE_CMD
    INNER_IP_SRC_MODE_RANDOM = "random"
    INNER_IP_SRC_MODE_DECREMENT = "decrement"
    INNER_IP_SRC_MODE_FIXED = "fixed"
    INNER_IP_SRC_MODE_INCREMENT = "increment"

    INNER_IP_SRC_STEP_CMD = "inner_ip_src_step"

    INNER_IP_SRC_TRACKING_CMD = "inner_ip_src_tracking"

    INNER_IPV6_DST_ADDR_CMD = "inner_ipv6_dst_addr"

    INNER_IPV6_DST_COUNT_CMD = "inner_ipv6_dst_count"

    INNER_IPV6_DST_MASK_CMD = "inner_ipv6_dst_mask"

    INNER_IPV6_DST_MODE_CMD = "inner_ipv6_dst_mode"
    # Constant values for INNER_IPV6_DST_MODE_CMD
    INNER_IPV6_DST_MODE_INCR_HOST = "incr_host"
    INNER_IPV6_DST_MODE_INCR_GLOBAL_SITE_LEVEL = "incr_global_site_level"
    INNER_IPV6_DST_MODE_DECR_MCAST_GROUP = "decr_mcast_group"
    INNER_IPV6_DST_MODE_DECR_INTF_ID = "decr_intf_id"
    INNER_IPV6_DST_MODE_DECR_HOST = "decr_host"
    INNER_IPV6_DST_MODE_DECR_GLOBAL_SITE_LEVEL = "decr_global_site_level"
    INNER_IPV6_DST_MODE_INCR_NETWORK = "incr_network"
    INNER_IPV6_DST_MODE_INCR_INTF_ID = "incr_intf_id"
    INNER_IPV6_DST_MODE_RANDOM = "random"
    INNER_IPV6_DST_MODE_DECR_LOCAL_SITE_SUBNET = "decr_local_site_subnet"
    INNER_IPV6_DST_MODE_INCR_MCAST_GROUP = "incr_mcast_group"
    INNER_IPV6_DST_MODE_DECR_NETWORK = "decr_network"
    INNER_IPV6_DST_MODE_INCREMENT = "increment"
    INNER_IPV6_DST_MODE_DECR_GLOBAL_NEXT_LEVEL = "decr_global_next_level"
    INNER_IPV6_DST_MODE_INCR_LOCAL_SITE_SUBNET = "incr_local_site_subnet"
    INNER_IPV6_DST_MODE_DECREMENT = "decrement"
    INNER_IPV6_DST_MODE_FIXED = "fixed"
    INNER_IPV6_DST_MODE_INCR_GLOBAL_TOP_LEVEL = "incr_global_top_level"
    INNER_IPV6_DST_MODE_DECR_GLOBAL_TOP_LEVEL = "decr_global_top_level"
    INNER_IPV6_DST_MODE_INCR_GLOBAL_NEXT_LEVEL = "incr_global_next_level"

    INNER_IPV6_DST_STEP_CMD = "inner_ipv6_dst_step"

    INNER_IPV6_DST_TRACKING_CMD = "inner_ipv6_dst_tracking"

    INNER_IPV6_FLOW_LABEL_CMD = "inner_ipv6_flow_label"

    INNER_IPV6_FLOW_LABEL_COUNT_CMD = "inner_ipv6_flow_label_count"

    INNER_IPV6_FLOW_LABEL_MODE_CMD = "inner_ipv6_flow_label_mode"
    # Constant values for INNER_IPV6_FLOW_LABEL_MODE_CMD
    INNER_IPV6_FLOW_LABEL_MODE_INCR = "incr"
    INNER_IPV6_FLOW_LABEL_MODE_FIXED = "fixed"
    INNER_IPV6_FLOW_LABEL_MODE_LIST = "list"
    INNER_IPV6_FLOW_LABEL_MODE_DECR = "decr"

    INNER_IPV6_FLOW_LABEL_STEP_CMD = "inner_ipv6_flow_label_step"

    INNER_IPV6_FLOW_LABEL_TRACKING_CMD = "inner_ipv6_flow_label_tracking"

    INNER_IPV6_FRAG_ID_CMD = "inner_ipv6_frag_id"

    INNER_IPV6_FRAG_ID_COUNT_CMD = "inner_ipv6_frag_id_count"

    INNER_IPV6_FRAG_ID_MODE_CMD = "inner_ipv6_frag_id_mode"
    # Constant values for INNER_IPV6_FRAG_ID_MODE_CMD
    INNER_IPV6_FRAG_ID_MODE_INCR = "incr"
    INNER_IPV6_FRAG_ID_MODE_FIXED = "fixed"
    INNER_IPV6_FRAG_ID_MODE_LIST = "list"
    INNER_IPV6_FRAG_ID_MODE_DECR = "decr"

    INNER_IPV6_FRAG_ID_STEP_CMD = "inner_ipv6_frag_id_step"

    INNER_IPV6_FRAG_ID_TRACKING_CMD = "inner_ipv6_frag_id_tracking"

    INNER_IPV6_FRAG_MORE_FLAG_CMD = "inner_ipv6_frag_more_flag"

    INNER_IPV6_FRAG_MORE_FLAG_MODE_CMD = "inner_ipv6_frag_more_flag_mode"
    # Constant values for INNER_IPV6_FRAG_MORE_FLAG_MODE_CMD
    INNER_IPV6_FRAG_MORE_FLAG_MODE_FIXED = "fixed"
    INNER_IPV6_FRAG_MORE_FLAG_MODE_LIST = "list"

    INNER_IPV6_FRAG_MORE_FLAG_TRACKING_CMD = "inner_ipv6_frag_more_flag_tracking"

    INNER_IPV6_FRAG_OFFSET_CMD = "inner_ipv6_frag_offset"

    INNER_IPV6_FRAG_OFFSET_COUNT_CMD = "inner_ipv6_frag_offset_count"

    INNER_IPV6_FRAG_OFFSET_MODE_CMD = "inner_ipv6_frag_offset_mode"
    # Constant values for INNER_IPV6_FRAG_OFFSET_MODE_CMD
    INNER_IPV6_FRAG_OFFSET_MODE_INCR = "incr"
    INNER_IPV6_FRAG_OFFSET_MODE_FIXED = "fixed"
    INNER_IPV6_FRAG_OFFSET_MODE_LIST = "list"
    INNER_IPV6_FRAG_OFFSET_MODE_DECR = "decr"

    INNER_IPV6_FRAG_OFFSET_STEP_CMD = "inner_ipv6_frag_offset_step"

    INNER_IPV6_FRAG_OFFSET_TRACKING_CMD = "inner_ipv6_frag_offset_tracking"

    INNER_IPV6_HOP_LIMIT_CMD = "inner_ipv6_hop_limit"

    INNER_IPV6_HOP_LIMIT_COUNT_CMD = "inner_ipv6_hop_limit_count"

    INNER_IPV6_HOP_LIMIT_MODE_CMD = "inner_ipv6_hop_limit_mode"
    # Constant values for INNER_IPV6_HOP_LIMIT_MODE_CMD
    INNER_IPV6_HOP_LIMIT_MODE_INCR = "incr"
    INNER_IPV6_HOP_LIMIT_MODE_FIXED = "fixed"
    INNER_IPV6_HOP_LIMIT_MODE_LIST = "list"
    INNER_IPV6_HOP_LIMIT_MODE_DECR = "decr"

    INNER_IPV6_HOP_LIMIT_STEP_CMD = "inner_ipv6_hop_limit_step"

    INNER_IPV6_HOP_LIMIT_TRACKING_CMD = "inner_ipv6_hop_limit_tracking"

    INNER_IPV6_SRC_ADDR_CMD = "inner_ipv6_src_addr"

    INNER_IPV6_SRC_COUNT_CMD = "inner_ipv6_src_count"

    INNER_IPV6_SRC_MASK_CMD = "inner_ipv6_src_mask"

    INNER_IPV6_SRC_MODE_CMD = "inner_ipv6_src_mode"
    # Constant values for INNER_IPV6_SRC_MODE_CMD
    INNER_IPV6_SRC_MODE_INCR_HOST = "incr_host"
    INNER_IPV6_SRC_MODE_INCR_GLOBAL_SITE_LEVEL = "incr_global_site_level"
    INNER_IPV6_SRC_MODE_DECR_MCAST_GROUP = "decr_mcast_group"
    INNER_IPV6_SRC_MODE_DECR_INTF_ID = "decr_intf_id"
    INNER_IPV6_SRC_MODE_DECR_HOST = "decr_host"
    INNER_IPV6_SRC_MODE_DECR_GLOBAL_SITE_LEVEL = "decr_global_site_level"
    INNER_IPV6_SRC_MODE_INCR_NETWORK = "incr_network"
    INNER_IPV6_SRC_MODE_INCR_INTF_ID = "incr_intf_id"
    INNER_IPV6_SRC_MODE_RANDOM = "random"
    INNER_IPV6_SRC_MODE_DECR_LOCAL_SITE_SUBNET = "decr_local_site_subnet"
    INNER_IPV6_SRC_MODE_INCR_MCAST_GROUP = "incr_mcast_group"
    INNER_IPV6_SRC_MODE_DECR_NETWORK = "decr_network"
    INNER_IPV6_SRC_MODE_INCREMENT = "increment"
    INNER_IPV6_SRC_MODE_DECR_GLOBAL_NEXT_LEVEL = "decr_global_next_level"
    INNER_IPV6_SRC_MODE_INCR_LOCAL_SITE_SUBNET = "incr_local_site_subnet"
    INNER_IPV6_SRC_MODE_DECREMENT = "decrement"
    INNER_IPV6_SRC_MODE_FIXED = "fixed"
    INNER_IPV6_SRC_MODE_INCR_GLOBAL_TOP_LEVEL = "incr_global_top_level"
    INNER_IPV6_SRC_MODE_DECR_GLOBAL_TOP_LEVEL = "decr_global_top_level"
    INNER_IPV6_SRC_MODE_INCR_GLOBAL_NEXT_LEVEL = "incr_global_next_level"

    INNER_IPV6_SRC_STEP_CMD = "inner_ipv6_src_step"

    INNER_IPV6_SRC_TRACKING_CMD = "inner_ipv6_src_tracking"

    INNER_IPV6_TRAFFIC_CLASS_CMD = "inner_ipv6_traffic_class"

    INNER_IPV6_TRAFFIC_CLASS_COUNT_CMD = "inner_ipv6_traffic_class_count"

    INNER_IPV6_TRAFFIC_CLASS_MODE_CMD = "inner_ipv6_traffic_class_mode"
    # Constant values for INNER_IPV6_TRAFFIC_CLASS_MODE_CMD
    INNER_IPV6_TRAFFIC_CLASS_MODE_INCR = "incr"
    INNER_IPV6_TRAFFIC_CLASS_MODE_FIXED = "fixed"
    INNER_IPV6_TRAFFIC_CLASS_MODE_LIST = "list"
    INNER_IPV6_TRAFFIC_CLASS_MODE_DECR = "decr"

    INNER_IPV6_TRAFFIC_CLASS_STEP_CMD = "inner_ipv6_traffic_class_step"

    INNER_IPV6_TRAFFIC_CLASS_TRACKING_CMD = "inner_ipv6_traffic_class_tracking"

    INNER_PROTOCOL_CMD = "inner_protocol"
    # Constant values for INNER_PROTOCOL_CMD
    INNER_PROTOCOL_HEX = "HEX"
    INNER_PROTOCOL_IPV4 = "ipv4"
    INNER_PROTOCOL_IPV6 = "ipv6"

    INNER_PROTOCOL_COUNT_CMD = "inner_protocol_count"

    INNER_PROTOCOL_MODE_CMD = "inner_protocol_mode"
    # Constant values for INNER_PROTOCOL_MODE_CMD
    INNER_PROTOCOL_MODE_INCR = "incr"
    INNER_PROTOCOL_MODE_FIXED = "fixed"
    INNER_PROTOCOL_MODE_DECR = "decr"

    INNER_PROTOCOL_STEP_CMD = "inner_protocol_step"

    INNER_PROTOCOL_TRACKING_CMD = "inner_protocol_tracking"

    INTEGRITY_SIGNATURE_CMD = "integrity_signature"

    INTEGRITY_SIGNATURE_OFFSET_CMD = "integrity_signature_offset"

    INTER_BURST_GAP_CMD = "inter_burst_gap"

    INTER_FRAME_GAP_CMD = "inter_frame_gap"

    INTER_FRAME_GAP_UNIT_CMD = "inter_frame_gap_unit"
    # Constant values for INTER_FRAME_GAP_UNIT_CMD
    INTER_FRAME_GAP_UNIT_NS = "ns"
    INTER_FRAME_GAP_UNIT_BYTES = "bytes"

    INTER_STREAM_GAP_CMD = "inter_stream_gap"

    INTF_HANDLE_CMD = "intf_handle"

    IP_BIT_FLAGS_CMD = "ip_bit_flags"

    IP_CHECKSUM_CMD = "ip_checksum"

    IP_CHECKSUM_COUNT_CMD = "ip_checksum_count"

    IP_CHECKSUM_MODE_CMD = "ip_checksum_mode"
    # Constant values for IP_CHECKSUM_MODE_CMD
    IP_CHECKSUM_MODE_INCR = "incr"
    IP_CHECKSUM_MODE_FIXED = "fixed"
    IP_CHECKSUM_MODE_LIST = "list"
    IP_CHECKSUM_MODE_DECR = "decr"

    IP_CHECKSUM_STEP_CMD = "ip_checksum_step"

    IP_CHECKSUM_TRACKING_CMD = "ip_checksum_tracking"

    IP_COST_CMD = "ip_cost"

    IP_COST_MODE_CMD = "ip_cost_mode"
    # Constant values for IP_COST_MODE_CMD
    IP_COST_MODE_FIXED = "fixed"
    IP_COST_MODE_LIST = "list"

    IP_COST_TRACKING_CMD = "ip_cost_tracking"

    IP_CU_CMD = "ip_cu"

    IP_CU_COUNT_CMD = "ip_cu_count"

    IP_CU_MODE_CMD = "ip_cu_mode"
    # Constant values for IP_CU_MODE_CMD
    IP_CU_MODE_INCR = "incr"
    IP_CU_MODE_FIXED = "fixed"
    IP_CU_MODE_LIST = "list"
    IP_CU_MODE_DECR = "decr"

    IP_CU_STEP_CMD = "ip_cu_step"

    IP_CU_TRACKING_CMD = "ip_cu_tracking"

    IP_DELAY_CMD = "ip_delay"

    IP_DELAY_MODE_CMD = "ip_delay_mode"
    # Constant values for IP_DELAY_MODE_CMD
    IP_DELAY_MODE_FIXED = "fixed"
    IP_DELAY_MODE_LIST = "list"

    IP_DELAY_TRACKING_CMD = "ip_delay_tracking"

    IP_DSCP_CMD = "ip_dscp"

    IP_DSCP_COUNT_CMD = "ip_dscp_count"

    IP_DSCP_MODE_CMD = "ip_dscp_mode"
    # Constant values for IP_DSCP_MODE_CMD
    IP_DSCP_MODE_INCR = "incr"
    IP_DSCP_MODE_FIXED = "fixed"
    IP_DSCP_MODE_LIST = "list"
    IP_DSCP_MODE_DECR = "decr"

    IP_DSCP_STEP_CMD = "ip_dscp_step"

    IP_DSCP_TRACKING_CMD = "ip_dscp_tracking"

    IP_DST_ADDR_CMD = "ip_dst_addr"

    IP_DST_COUNT_CMD = "ip_dst_count"

    IP_DST_COUNT_STEP_CMD = "ip_dst_count_step"

    IP_DST_INCREMENT_CMD = "ip_dst_increment"

    IP_DST_INCREMENT_STEP_CMD = "ip_dst_increment_step"

    IP_DST_MODE_CMD = "ip_dst_mode"
    # Constant values for IP_DST_MODE_CMD
    IP_DST_MODE_FIXED = "fixed"
    IP_DST_MODE_INCREMENT = "increment"
    IP_DST_MODE_DECREMENT = "decrement"
    IP_DST_MODE_RANDOM = "random"
    IP_DST_MODE_EMULATION = "emulation"

    IP_DST_PREFIX_LEN_CMD = "ip_dst_prefix_len"

    IP_DST_PREFIX_LEN_STEP_CMD = "ip_dst_prefix_len_step"

    IP_DST_RANGE_STEP_CMD = "ip_dst_range_step"

    IP_DST_SKIP_BROADCAST_CMD = "ip_dst_skip_broadcast"

    IP_DST_SKIP_MULTICAST_CMD = "ip_dst_skip_multicast"

    IP_DST_STEP_CMD = "ip_dst_step"
    IP_DST_MASK_CMD = "ip_dst_mask"

    IP_DST_TRACKING_CMD = "ip_dst_tracking"

    IP_FRAGMENT_CMD = "ip_fragment"

    IP_FRAGMENT_LAST_CMD = "ip_fragment_last"

    IP_FRAGMENT_LAST_MODE_CMD = "ip_fragment_last_mode"
    # Constant values for IP_FRAGMENT_LAST_MODE_CMD
    IP_FRAGMENT_LAST_MODE_FIXED = "fixed"
    IP_FRAGMENT_LAST_MODE_LIST = "list"

    IP_FRAGMENT_LAST_TRACKING_CMD = "ip_fragment_last_tracking"

    IP_FRAGMENT_MODE_CMD = "ip_fragment_mode"
    # Constant values for IP_FRAGMENT_MODE_CMD
    IP_FRAGMENT_MODE_FIXED = "fixed"
    IP_FRAGMENT_MODE_LIST = "list"

    IP_FRAGMENT_OFFSET_CMD = "ip_fragment_offset"

    IP_FRAGMENT_OFFSET_COUNT_CMD = "ip_fragment_offset_count"

    IP_FRAGMENT_OFFSET_MODE_CMD = "ip_fragment_offset_mode"
    # Constant values for IP_FRAGMENT_OFFSET_MODE_CMD
    IP_FRAGMENT_OFFSET_MODE_INCR = "incr"
    IP_FRAGMENT_OFFSET_MODE_FIXED = "fixed"
    IP_FRAGMENT_OFFSET_MODE_LIST = "list"
    IP_FRAGMENT_OFFSET_MODE_DECR = "decr"

    IP_FRAGMENT_OFFSET_STEP_CMD = "ip_fragment_offset_step"

    IP_FRAGMENT_OFFSET_TRACKING_CMD = "ip_fragment_offset_tracking"

    IP_FRAGMENT_TRACKING_CMD = "ip_fragment_tracking"

    IP_HDR_LENGTH_CMD = "ip_hdr_length"

    IP_HDR_LENGTH_COUNT_CMD = "ip_hdr_length_count"

    IP_HDR_LENGTH_MODE_CMD = "ip_hdr_length_mode"
    # Constant values for IP_HDR_LENGTH_MODE_CMD
    IP_HDR_LENGTH_MODE_INCR = "incr"
    IP_HDR_LENGTH_MODE_FIXED = "fixed"
    IP_HDR_LENGTH_MODE_LIST = "list"
    IP_HDR_LENGTH_MODE_DECR = "decr"

    IP_HDR_LENGTH_STEP_CMD = "ip_hdr_length_step"

    IP_HDR_LENGTH_TRACKING_CMD = "ip_hdr_length_tracking"

    IP_ID_CMD = "ip_id"

    IP_ID_COUNT_CMD = "ip_id_count"

    IP_ID_MODE_CMD = "ip_id_mode"
    # Constant values for IP_ID_MODE_CMD
    IP_ID_MODE_INCR = "incr"
    IP_ID_MODE_FIXED = "fixed"
    IP_ID_MODE_LIST = "list"
    IP_ID_MODE_DECR = "decr"

    IP_ID_STEP_CMD = "ip_id_step"

    IP_ID_TRACKING_CMD = "ip_id_tracking"

    IP_LENGTH_OVERRIDE_CMD = "ip_length_override"

    IP_LENGTH_OVERRIDE_MODE_CMD = "ip_length_override_mode"
    # Constant values for IP_LENGTH_OVERRIDE_MODE_CMD
    IP_LENGTH_OVERRIDE_MODE_FIXED = "fixed"
    IP_LENGTH_OVERRIDE_MODE_LIST = "list"

    IP_LENGTH_OVERRIDE_TRACKING_CMD = "ip_length_override_tracking"

    IP_MBZ_CMD = "ip_mbz"

    IP_OPT_LOOSE_ROUTING_CMD = "ip_opt_loose_routing"

    IP_OPT_SECURITY_CMD = "ip_opt_security"

    IP_OPT_STRICT_ROUTING_CMD = "ip_opt_strict_routing"

    IP_OPT_TIMESTAMP_CMD = "ip_opt_timestamp"

    IP_PRECEDENCE_CMD = "ip_precedence"

    IP_PRECEDENCE_COUNT_CMD = "ip_precedence_count"

    IP_PRECEDENCE_MODE_CMD = "ip_precedence_mode"
    # Constant values for IP_PRECEDENCE_MODE_CMD
    IP_PRECEDENCE_MODE_INCR = "incr"
    IP_PRECEDENCE_MODE_FIXED = "fixed"
    IP_PRECEDENCE_MODE_LIST = "list"
    IP_PRECEDENCE_MODE_DECR = "decr"

    IP_PRECEDENCE_STEP_CMD = "ip_precedence_step"

    IP_PRECEDENCE_TRACKING_CMD = "ip_precedence_tracking"

    IP_PROTOCOL_CMD = "ip_protocol"

    IP_PROTOCOL_COUNT_CMD = "ip_protocol_count"

    IP_PROTOCOL_MODE_CMD = "ip_protocol_mode"
    # Constant values for IP_PROTOCOL_MODE_CMD
    IP_PROTOCOL_MODE_INCR = "incr"
    IP_PROTOCOL_MODE_FIXED = "fixed"
    IP_PROTOCOL_MODE_LIST = "list"
    IP_PROTOCOL_MODE_DECR = "decr"

    IP_PROTOCOL_STEP_CMD = "ip_protocol_step"

    IP_PROTOCOL_TRACKING_CMD = "ip_protocol_tracking"

    IP_RANGE_COUNT_CMD = "ip_range_count"

    IP_RELIABILITY_CMD = "ip_reliability"

    IP_RELIABILITY_MODE_CMD = "ip_reliability_mode"
    # Constant values for IP_RELIABILITY_MODE_CMD
    IP_RELIABILITY_MODE_FIXED = "fixed"
    IP_RELIABILITY_MODE_LIST = "list"

    IP_RELIABILITY_TRACKING_CMD = "ip_reliability_tracking"

    IP_RESERVED_CMD = "ip_reserved"

    IP_RESERVED_MODE_CMD = "ip_reserved_mode"
    # Constant values for IP_RESERVED_MODE_CMD
    IP_RESERVED_MODE_FIXED = "fixed"
    IP_RESERVED_MODE_LIST = "list"

    IP_RESERVED_TRACKING_CMD = "ip_reserved_tracking"

    IP_SRC_ADDR_CMD = "ip_src_addr"

    IP_SRC_COUNT_CMD = "ip_src_count"

    IP_SRC_MODE_CMD = "ip_src_mode"
    # Constant values for IP_SRC_MODE_CMD
    IP_SRC_MODE_FIXED = "fixed"
    IP_SRC_MODE_INCREMENT = "increment"
    IP_SRC_MODE_DECREMENT = "decrement"
    IP_SRC_MODE_RANDOM = "random"
    IP_SRC_MODE_EMULATION = "emulation"

    IP_SRC_SKIP_BROADCAST_CMD = "ip_src_skip_broadcast"

    IP_SRC_SKIP_MULTICAST_CMD = "ip_src_skip_multicast"

    IP_SRC_STEP_CMD = "ip_src_step"
    IP_SRC_MASK_CMD = "ip_src_mask"

    IP_SRC_TRACKING_CMD = "ip_src_tracking"

    IP_THROUGHPUT_CMD = "ip_throughput"

    IP_THROUGHPUT_MODE_CMD = "ip_throughput_mode"
    # Constant values for IP_THROUGHPUT_MODE_CMD
    IP_THROUGHPUT_MODE_FIXED = "fixed"
    IP_THROUGHPUT_MODE_LIST = "list"

    IP_THROUGHPUT_TRACKING_CMD = "ip_throughput_tracking"

    IP_TOS_COUNT_CMD = "ip_tos_count"

    IP_TOS_FIELD_CMD = "ip_tos_field"

    IP_TOS_STEP_CMD = "ip_tos_step"

    IP_TOTAL_LENGTH_CMD = "ip_total_length"

    IP_TOTAL_LENGTH_COUNT_CMD = "ip_total_length_count"

    IP_TOTAL_LENGTH_MODE_CMD = "ip_total_length_mode"
    # Constant values for IP_TOTAL_LENGTH_MODE_CMD
    IP_TOTAL_LENGTH_MODE_AUTO = "auto"
    IP_TOTAL_LENGTH_MODE_INCR = "incr"
    IP_TOTAL_LENGTH_MODE_FIXED = "fixed"
    IP_TOTAL_LENGTH_MODE_LIST = "list"
    IP_TOTAL_LENGTH_MODE_DECR = "decr"

    IP_TOTAL_LENGTH_STEP_CMD = "ip_total_length_step"

    IP_TOTAL_LENGTH_TRACKING_CMD = "ip_total_length_tracking"

    IP_TTL_CMD = "ip_ttl"

    IP_TTL_COUNT_CMD = "ip_ttl_count"

    IP_TTL_MODE_CMD = "ip_ttl_mode"
    # Constant values for IP_TTL_MODE_CMD
    IP_TTL_MODE_INCR = "incr"
    IP_TTL_MODE_FIXED = "fixed"
    IP_TTL_MODE_LIST = "list"
    IP_TTL_MODE_DECR = "decr"

    IP_TTL_STEP_CMD = "ip_ttl_step"

    IP_TTL_TRACKING_CMD = "ip_ttl_tracking"

    IPV6_AUTH_MD5SHA1_STRING_CMD = "ipv6_auth_md5sha1_string"

    IPV6_AUTH_MD5SHA1_STRING_COUNT_CMD = "ipv6_auth_md5sha1_string_count"

    IPV6_AUTH_MD5SHA1_STRING_MODE_CMD = "ipv6_auth_md5sha1_string_mode"
    # Constant values for IPV6_AUTH_MD5SHA1_STRING_MODE_CMD
    IPV6_AUTH_MD5SHA1_STRING_MODE_INCR = "incr"
    IPV6_AUTH_MD5SHA1_STRING_MODE_FIXED = "fixed"
    IPV6_AUTH_MD5SHA1_STRING_MODE_LIST = "list"
    IPV6_AUTH_MD5SHA1_STRING_MODE_DECR = "decr"

    IPV6_AUTH_MD5SHA1_STRING_STEP_CMD = "ipv6_auth_md5sha1_string_step"

    IPV6_AUTH_MD5SHA1_STRING_TRACKING_CMD = "ipv6_auth_md5sha1_string_tracking"

    IPV6_AUTH_NEXT_HEADER_CMD = "ipv6_auth_next_header"

    IPV6_AUTH_NEXT_HEADER_COUNT_CMD = "ipv6_auth_next_header_count"

    IPV6_AUTH_NEXT_HEADER_MODE_CMD = "ipv6_auth_next_header_mode"
    # Constant values for IPV6_AUTH_NEXT_HEADER_MODE_CMD
    IPV6_AUTH_NEXT_HEADER_MODE_INCR = "incr"
    IPV6_AUTH_NEXT_HEADER_MODE_FIXED = "fixed"
    IPV6_AUTH_NEXT_HEADER_MODE_LIST = "list"
    IPV6_AUTH_NEXT_HEADER_MODE_DECR = "decr"

    IPV6_AUTH_NEXT_HEADER_STEP_CMD = "ipv6_auth_next_header_step"

    IPV6_AUTH_NEXT_HEADER_TRACKING_CMD = "ipv6_auth_next_header_tracking"

    IPV6_AUTH_PADDING_CMD = "ipv6_auth_padding"

    IPV6_AUTH_PADDING_COUNT_CMD = "ipv6_auth_padding_count"

    IPV6_AUTH_PADDING_MODE_CMD = "ipv6_auth_padding_mode"
    # Constant values for IPV6_AUTH_PADDING_MODE_CMD
    IPV6_AUTH_PADDING_MODE_INCR = "incr"
    IPV6_AUTH_PADDING_MODE_FIXED = "fixed"
    IPV6_AUTH_PADDING_MODE_LIST = "list"
    IPV6_AUTH_PADDING_MODE_DECR = "decr"

    IPV6_AUTH_PADDING_STEP_CMD = "ipv6_auth_padding_step"

    IPV6_AUTH_PADDING_TRACKING_CMD = "ipv6_auth_padding_tracking"

    IPV6_AUTH_PAYLOAD_LEN_CMD = "ipv6_auth_payload_len"

    IPV6_AUTH_PAYLOAD_LEN_COUNT_CMD = "ipv6_auth_payload_len_count"

    IPV6_AUTH_PAYLOAD_LEN_MODE_CMD = "ipv6_auth_payload_len_mode"
    # Constant values for IPV6_AUTH_PAYLOAD_LEN_MODE_CMD
    IPV6_AUTH_PAYLOAD_LEN_MODE_INCR = "incr"
    IPV6_AUTH_PAYLOAD_LEN_MODE_FIXED = "fixed"
    IPV6_AUTH_PAYLOAD_LEN_MODE_LIST = "list"
    IPV6_AUTH_PAYLOAD_LEN_MODE_DECR = "decr"

    IPV6_AUTH_PAYLOAD_LEN_STEP_CMD = "ipv6_auth_payload_len_step"

    IPV6_AUTH_PAYLOAD_LEN_TRACKING_CMD = "ipv6_auth_payload_len_tracking"

    IPV6_AUTH_RESERVED_CMD = "ipv6_auth_reserved"

    IPV6_AUTH_RESERVED_COUNT_CMD = "ipv6_auth_reserved_count"

    IPV6_AUTH_RESERVED_MODE_CMD = "ipv6_auth_reserved_mode"
    # Constant values for IPV6_AUTH_RESERVED_MODE_CMD
    IPV6_AUTH_RESERVED_MODE_INCR = "incr"
    IPV6_AUTH_RESERVED_MODE_FIXED = "fixed"
    IPV6_AUTH_RESERVED_MODE_LIST = "list"
    IPV6_AUTH_RESERVED_MODE_DECR = "decr"

    IPV6_AUTH_RESERVED_STEP_CMD = "ipv6_auth_reserved_step"

    IPV6_AUTH_RESERVED_TRACKING_CMD = "ipv6_auth_reserved_tracking"

    IPV6_AUTH_SEQ_NUM_CMD = "ipv6_auth_seq_num"

    IPV6_AUTH_SEQ_NUM_COUNT_CMD = "ipv6_auth_seq_num_count"

    IPV6_AUTH_SEQ_NUM_MODE_CMD = "ipv6_auth_seq_num_mode"
    # Constant values for IPV6_AUTH_SEQ_NUM_MODE_CMD
    IPV6_AUTH_SEQ_NUM_MODE_INCR = "incr"
    IPV6_AUTH_SEQ_NUM_MODE_FIXED = "fixed"
    IPV6_AUTH_SEQ_NUM_MODE_LIST = "list"
    IPV6_AUTH_SEQ_NUM_MODE_DECR = "decr"

    IPV6_AUTH_SEQ_NUM_STEP_CMD = "ipv6_auth_seq_num_step"

    IPV6_AUTH_SEQ_NUM_TRACKING_CMD = "ipv6_auth_seq_num_tracking"

    IPV6_AUTH_SPI_CMD = "ipv6_auth_spi"

    IPV6_AUTH_SPI_COUNT_CMD = "ipv6_auth_spi_count"

    IPV6_AUTH_SPI_MODE_CMD = "ipv6_auth_spi_mode"
    # Constant values for IPV6_AUTH_SPI_MODE_CMD
    IPV6_AUTH_SPI_MODE_INCR = "incr"
    IPV6_AUTH_SPI_MODE_FIXED = "fixed"
    IPV6_AUTH_SPI_MODE_LIST = "list"
    IPV6_AUTH_SPI_MODE_DECR = "decr"

    IPV6_AUTH_SPI_STEP_CMD = "ipv6_auth_spi_step"

    IPV6_AUTH_SPI_TRACKING_CMD = "ipv6_auth_spi_tracking"

    IPV6_AUTH_STRING_CMD = "ipv6_auth_string"

    IPV6_AUTH_STRING_COUNT_CMD = "ipv6_auth_string_count"

    IPV6_AUTH_STRING_MODE_CMD = "ipv6_auth_string_mode"
    # Constant values for IPV6_AUTH_STRING_MODE_CMD
    IPV6_AUTH_STRING_MODE_INCR = "incr"
    IPV6_AUTH_STRING_MODE_FIXED = "fixed"
    IPV6_AUTH_STRING_MODE_LIST = "list"
    IPV6_AUTH_STRING_MODE_DECR = "decr"

    IPV6_AUTH_STRING_STEP_CMD = "ipv6_auth_string_step"

    IPV6_AUTH_STRING_TRACKING_CMD = "ipv6_auth_string_tracking"

    IPV6_AUTH_TYPE_CMD = "ipv6_auth_type"
    # Constant values for IPV6_AUTH_TYPE_CMD
    IPV6_AUTH_TYPE_SHA1 = "sha1"
    IPV6_AUTH_TYPE_MD5 = "md5"

    IPV6_CHECKSUM_CMD = "ipv6_checksum"

    IPV6_DST_ADDR_CMD = "ipv6_dst_addr"

    IPV6_DST_COUNT_CMD = "ipv6_dst_count"

    IPV6_DST_MASK_CMD = "ipv6_dst_mask"

    IPV6_DST_MODE_CMD = "ipv6_dst_mode"
    # Constant values for IPV6_DST_MODE_CMD
    IPV6_DST_MODE_FIXED = "fixed"
    IPV6_DST_MODE_INCREMENT = "increment"
    IPV6_DST_MODE_DECREMENT = "decrement"
    IPV6_DST_MODE_LIST = "list"
    IPV6_DST_MODE_RANDOM = "random"
    IPV6_DST_MODE_INCR_HOST = "incr_host"
    IPV6_DST_MODE_DECR_HOST = "decr_host"
    IPV6_DST_MODE_INCR_NETWORK = "incr_network"
    IPV6_DST_MODE_DECR_NETWORK = "decr_network"
    IPV6_DST_MODE_INCR_INTF_ID = "incr_intf_id"
    IPV6_DST_MODE_DECR_INTF_ID = "decr_intf_id"
    IPV6_DST_MODE_INCR_GLOBAL_TOP_LEVEL = "incr_global_top_level"
    IPV6_DST_MODE_DECR_GLOBAL_TOP_LEVEL = "decr_global_top_level"
    IPV6_DST_MODE_INCR_GLOBAL_NEXT_LEVEL = "incr_global_next_level"
    IPV6_DST_MODE_DECR_GLOBAL_NEXT_LEVEL = "decr_global_next_level"
    IPV6_DST_MODE_INCR_GLOBAL_SITE_LEVEL = "incr_global_site_level"
    IPV6_DST_MODE_DECR_GLOBAL_SITE_LEVEL = "decr_global_site_level"
    IPV6_DST_MODE_INCR_LOCAL_SITE_SUBNET = "incr_local_site_subnet"
    IPV6_DST_MODE_DECR_LOCAL_SITE_SUBNET = "decr_local_site_subnet"
    IPV6_DST_MODE_INCR_MCAST_GROUP = "incr_mcast_group"
    IPV6_DST_MODE_DECR_MCAST_GROUP = "decr_mcast_group"

    IPV6_DST_STEP_CMD = "ipv6_dst_step"

    IPV6_DST_TRACKING_CMD = "ipv6_dst_tracking"

    IPV6_ENCAP_SEQ_NUMBER_CMD = "ipv6_encap_seq_number"

    IPV6_ENCAP_SEQ_NUMBER_COUNT_CMD = "ipv6_encap_seq_number_count"

    IPV6_ENCAP_SEQ_NUMBER_MODE_CMD = "ipv6_encap_seq_number_mode"
    # Constant values for IPV6_ENCAP_SEQ_NUMBER_MODE_CMD
    IPV6_ENCAP_SEQ_NUMBER_MODE_INCR = "incr"
    IPV6_ENCAP_SEQ_NUMBER_MODE_FIXED = "fixed"
    IPV6_ENCAP_SEQ_NUMBER_MODE_LIST = "list"
    IPV6_ENCAP_SEQ_NUMBER_MODE_DECR = "decr"

    IPV6_ENCAP_SEQ_NUMBER_STEP_CMD = "ipv6_encap_seq_number_step"

    IPV6_ENCAP_SEQ_NUMBER_TRACKING_CMD = "ipv6_encap_seq_number_tracking"

    IPV6_ENCAP_SPI_CMD = "ipv6_encap_spi"

    IPV6_ENCAP_SPI_COUNT_CMD = "ipv6_encap_spi_count"

    IPV6_ENCAP_SPI_MODE_CMD = "ipv6_encap_spi_mode"
    # Constant values for IPV6_ENCAP_SPI_MODE_CMD
    IPV6_ENCAP_SPI_MODE_INCR = "incr"
    IPV6_ENCAP_SPI_MODE_FIXED = "fixed"
    IPV6_ENCAP_SPI_MODE_LIST = "list"
    IPV6_ENCAP_SPI_MODE_DECR = "decr"

    IPV6_ENCAP_SPI_STEP_CMD = "ipv6_encap_spi_step"

    IPV6_ENCAP_SPI_TRACKING_CMD = "ipv6_encap_spi_tracking"

    IPV6_EXTENSION_HEADER_CMD = "ipv6_extension_header"
    # Constant values for IPV6_EXTENSION_HEADER_CMD
    IPV6_EXTENSION_HEADER_NONE = "none"
    IPV6_EXTENSION_HEADER_HOP_BY_HOP = "hop_by_hop"
    IPV6_EXTENSION_HEADER_ROUTING = "routing"
    IPV6_EXTENSION_HEADER_DESTINATION = "destination"
    IPV6_EXTENSION_HEADER_AUTHENTICATION = "authentication"
    IPV6_EXTENSION_HEADER_FRAGMENT = "fragment"
    IPV6_EXTENSION_HEADER_ENCAPSULATION = "encapsulation"
    IPV6_EXTENSION_HEADER_PSEUDO = "pseudo"

    IPV6_FLOW_LABEL_CMD = "ipv6_flow_label"

    IPV6_FLOW_LABEL_COUNT_CMD = "ipv6_flow_label_count"

    IPV6_FLOW_LABEL_MODE_CMD = "ipv6_flow_label_mode"
    # Constant values for IPV6_FLOW_LABEL_MODE_CMD
    IPV6_FLOW_LABEL_MODE_INCR = "incr"
    IPV6_FLOW_LABEL_MODE_FIXED = "fixed"
    IPV6_FLOW_LABEL_MODE_LIST = "list"
    IPV6_FLOW_LABEL_MODE_DECR = "decr"

    IPV6_FLOW_LABEL_STEP_CMD = "ipv6_flow_label_step"

    IPV6_FLOW_LABEL_TRACKING_CMD = "ipv6_flow_label_tracking"

    IPV6_FLOW_VERSION_CMD = "ipv6_flow_version"

    IPV6_FLOW_VERSION_COUNT_CMD = "ipv6_flow_version_count"

    IPV6_FLOW_VERSION_MODE_CMD = "ipv6_flow_version_mode"
    # Constant values for IPV6_FLOW_VERSION_MODE_CMD
    IPV6_FLOW_VERSION_MODE_INCR = "incr"
    IPV6_FLOW_VERSION_MODE_FIXED = "fixed"
    IPV6_FLOW_VERSION_MODE_LIST = "list"
    IPV6_FLOW_VERSION_MODE_DECR = "decr"

    IPV6_FLOW_VERSION_STEP_CMD = "ipv6_flow_version_step"

    IPV6_FLOW_VERSION_TRACKING_CMD = "ipv6_flow_version_tracking"

    IPV6_FRAG_ID_CMD = "ipv6_frag_id"

    IPV6_FRAG_ID_COUNT_CMD = "ipv6_frag_id_count"

    IPV6_FRAG_ID_MODE_CMD = "ipv6_frag_id_mode"
    # Constant values for IPV6_FRAG_ID_MODE_CMD
    IPV6_FRAG_ID_MODE_INCR = "incr"
    IPV6_FRAG_ID_MODE_FIXED = "fixed"
    IPV6_FRAG_ID_MODE_LIST = "list"
    IPV6_FRAG_ID_MODE_DECR = "decr"

    IPV6_FRAG_ID_STEP_CMD = "ipv6_frag_id_step"

    IPV6_FRAG_ID_TRACKING_CMD = "ipv6_frag_id_tracking"

    IPV6_FRAG_MORE_FLAG_CMD = "ipv6_frag_more_flag"

    IPV6_FRAG_MORE_FLAG_MODE_CMD = "ipv6_frag_more_flag_mode"
    # Constant values for IPV6_FRAG_MORE_FLAG_MODE_CMD
    IPV6_FRAG_MORE_FLAG_MODE_FIXED = "fixed"
    IPV6_FRAG_MORE_FLAG_MODE_LIST = "list"

    IPV6_FRAG_MORE_FLAG_TRACKING_CMD = "ipv6_frag_more_flag_tracking"

    IPV6_FRAG_NEXT_HEADER_CMD = "ipv6_frag_next_header"

    IPV6_FRAG_OFFSET_CMD = "ipv6_frag_offset"

    IPV6_FRAG_OFFSET_COUNT_CMD = "ipv6_frag_offset_count"

    IPV6_FRAG_OFFSET_MODE_CMD = "ipv6_frag_offset_mode"
    # Constant values for IPV6_FRAG_OFFSET_MODE_CMD
    IPV6_FRAG_OFFSET_MODE_INCR = "incr"
    IPV6_FRAG_OFFSET_MODE_FIXED = "fixed"
    IPV6_FRAG_OFFSET_MODE_LIST = "list"
    IPV6_FRAG_OFFSET_MODE_DECR = "decr"

    IPV6_FRAG_OFFSET_STEP_CMD = "ipv6_frag_offset_step"

    IPV6_FRAG_OFFSET_TRACKING_CMD = "ipv6_frag_offset_tracking"

    IPV6_FRAG_RES_2BIT_CMD = "ipv6_frag_res_2bit"

    IPV6_FRAG_RES_2BIT_COUNT_CMD = "ipv6_frag_res_2bit_count"

    IPV6_FRAG_RES_2BIT_MODE_CMD = "ipv6_frag_res_2bit_mode"
    # Constant values for IPV6_FRAG_RES_2BIT_MODE_CMD
    IPV6_FRAG_RES_2BIT_MODE_INCR = "incr"
    IPV6_FRAG_RES_2BIT_MODE_FIXED = "fixed"
    IPV6_FRAG_RES_2BIT_MODE_LIST = "list"
    IPV6_FRAG_RES_2BIT_MODE_DECR = "decr"

    IPV6_FRAG_RES_2BIT_STEP_CMD = "ipv6_frag_res_2bit_step"

    IPV6_FRAG_RES_2BIT_TRACKING_CMD = "ipv6_frag_res_2bit_tracking"

    IPV6_FRAG_RES_8BIT_CMD = "ipv6_frag_res_8bit"

    IPV6_FRAG_RES_8BIT_COUNT_CMD = "ipv6_frag_res_8bit_count"

    IPV6_FRAG_RES_8BIT_MODE_CMD = "ipv6_frag_res_8bit_mode"
    # Constant values for IPV6_FRAG_RES_8BIT_MODE_CMD
    IPV6_FRAG_RES_8BIT_MODE_INCR = "incr"
    IPV6_FRAG_RES_8BIT_MODE_FIXED = "fixed"
    IPV6_FRAG_RES_8BIT_MODE_LIST = "list"
    IPV6_FRAG_RES_8BIT_MODE_DECR = "decr"

    IPV6_FRAG_RES_8BIT_STEP_CMD = "ipv6_frag_res_8bit_step"

    IPV6_FRAG_RES_8BIT_TRACKING_CMD = "ipv6_frag_res_8bit_tracking"

    IPV6_HOP_BY_HOP_OPTIONS_CMD = "ipv6_hop_by_hop_options"

    IPV6_HOP_LIMIT_CMD = "ipv6_hop_limit"

    IPV6_HOP_LIMIT_COUNT_CMD = "ipv6_hop_limit_count"

    IPV6_HOP_LIMIT_MODE_CMD = "ipv6_hop_limit_mode"
    # Constant values for IPV6_HOP_LIMIT_MODE_CMD
    IPV6_HOP_LIMIT_MODE_INCR = "incr"
    IPV6_HOP_LIMIT_MODE_FIXED = "fixed"
    IPV6_HOP_LIMIT_MODE_LIST = "list"
    IPV6_HOP_LIMIT_MODE_DECR = "decr"

    IPV6_HOP_LIMIT_STEP_CMD = "ipv6_hop_limit_step"

    IPV6_HOP_LIMIT_TRACKING_CMD = "ipv6_hop_limit_tracking"

    IPV6_LENGTH_CMD = "ipv6_length"

    IPV6_NEXT_HEADER_CMD = "ipv6_next_header"

    IPV6_NEXT_HEADER_COUNT_CMD = "ipv6_next_header_count"

    IPV6_NEXT_HEADER_MODE_CMD = "ipv6_next_header_mode"
    # Constant values for IPV6_NEXT_HEADER_MODE_CMD
    IPV6_NEXT_HEADER_MODE_INCR = "incr"
    IPV6_NEXT_HEADER_MODE_FIXED = "fixed"
    IPV6_NEXT_HEADER_MODE_LIST = "list"
    IPV6_NEXT_HEADER_MODE_DECR = "decr"

    IPV6_NEXT_HEADER_STEP_CMD = "ipv6_next_header_step"

    IPV6_NEXT_HEADER_TRACKING_CMD = "ipv6_next_header_tracking"

    IPV6_PSEUDO_DST_ADDR_CMD = "ipv6_pseudo_dst_addr"

    IPV6_PSEUDO_DST_ADDR_COUNT_CMD = "ipv6_pseudo_dst_addr_count"

    IPV6_PSEUDO_DST_ADDR_MODE_CMD = "ipv6_pseudo_dst_addr_mode"
    # Constant values for IPV6_PSEUDO_DST_ADDR_MODE_CMD
    IPV6_PSEUDO_DST_ADDR_MODE_INCR = "incr"
    IPV6_PSEUDO_DST_ADDR_MODE_FIXED = "fixed"
    IPV6_PSEUDO_DST_ADDR_MODE_LIST = "list"
    IPV6_PSEUDO_DST_ADDR_MODE_DECR = "decr"

    IPV6_PSEUDO_DST_ADDR_STEP_CMD = "ipv6_pseudo_dst_addr_step"

    IPV6_PSEUDO_DST_ADDR_TRACKING_CMD = "ipv6_pseudo_dst_addr_tracking"

    IPV6_PSEUDO_SRC_ADDR_CMD = "ipv6_pseudo_src_addr"

    IPV6_PSEUDO_SRC_ADDR_COUNT_CMD = "ipv6_pseudo_src_addr_count"

    IPV6_PSEUDO_SRC_ADDR_MODE_CMD = "ipv6_pseudo_src_addr_mode"
    # Constant values for IPV6_PSEUDO_SRC_ADDR_MODE_CMD
    IPV6_PSEUDO_SRC_ADDR_MODE_INCR = "incr"
    IPV6_PSEUDO_SRC_ADDR_MODE_FIXED = "fixed"
    IPV6_PSEUDO_SRC_ADDR_MODE_LIST = "list"
    IPV6_PSEUDO_SRC_ADDR_MODE_DECR = "decr"

    IPV6_PSEUDO_SRC_ADDR_STEP_CMD = "ipv6_pseudo_src_addr_step"

    IPV6_PSEUDO_SRC_ADDR_TRACKING_CMD = "ipv6_pseudo_src_addr_tracking"

    IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_CMD = "ipv6_pseudo_uppper_layer_pkt_length"

    IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_COUNT_CMD = "ipv6_pseudo_uppper_layer_pkt_length_count"

    IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_MODE_CMD = "ipv6_pseudo_uppper_layer_pkt_length_mode"
    # Constant values for IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_MODE_CMD
    IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_MODE_INCR = "incr"
    IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_MODE_FIXED = "fixed"
    IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_MODE_LIST = "list"
    IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_MODE_DECR = "decr"

    IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_STEP_CMD = "ipv6_pseudo_uppper_layer_pkt_length_step"

    IPV6_PSEUDO_UPPPER_LAYER_PKT_LENGTH_TRACKING_CMD = "ipv6_pseudo_uppper_layer_pkt_length_tracking"

    IPV6_PSEUDO_ZERO_NUMBER_CMD = "ipv6_pseudo_zero_number"

    IPV6_PSEUDO_ZERO_NUMBER_COUNT_CMD = "ipv6_pseudo_zero_number_count"

    IPV6_PSEUDO_ZERO_NUMBER_MODE_CMD = "ipv6_pseudo_zero_number_mode"
    # Constant values for IPV6_PSEUDO_ZERO_NUMBER_MODE_CMD
    IPV6_PSEUDO_ZERO_NUMBER_MODE_INCR = "incr"
    IPV6_PSEUDO_ZERO_NUMBER_MODE_FIXED = "fixed"
    IPV6_PSEUDO_ZERO_NUMBER_MODE_LIST = "list"
    IPV6_PSEUDO_ZERO_NUMBER_MODE_DECR = "decr"

    IPV6_PSEUDO_ZERO_NUMBER_STEP_CMD = "ipv6_pseudo_zero_number_step"

    IPV6_PSEUDO_ZERO_NUMBER_TRACKING_CMD = "ipv6_pseudo_zero_number_tracking"

    IPV6_ROUTING_NODE_LIST_CMD = "ipv6_routing_node_list"

    IPV6_ROUTING_RES_CMD = "ipv6_routing_res"

    IPV6_ROUTING_RES_COUNT_CMD = "ipv6_routing_res_count"

    IPV6_ROUTING_RES_MODE_CMD = "ipv6_routing_res_mode"
    # Constant values for IPV6_ROUTING_RES_MODE_CMD
    IPV6_ROUTING_RES_MODE_INCR = "incr"
    IPV6_ROUTING_RES_MODE_FIXED = "fixed"
    IPV6_ROUTING_RES_MODE_LIST = "list"
    IPV6_ROUTING_RES_MODE_DECR = "decr"

    IPV6_ROUTING_RES_STEP_CMD = "ipv6_routing_res_step"

    IPV6_ROUTING_RES_TRACKING_CMD = "ipv6_routing_res_tracking"

    IPV6_ROUTING_TYPE_CMD = "ipv6_routing_type"

    IPV6_ROUTING_TYPE_COUNT_CMD = "ipv6_routing_type_count"

    IPV6_ROUTING_TYPE_MODE_CMD = "ipv6_routing_type_mode"
    # Constant values for IPV6_ROUTING_TYPE_MODE_CMD
    IPV6_ROUTING_TYPE_MODE_INCR = "incr"
    IPV6_ROUTING_TYPE_MODE_FIXED = "fixed"
    IPV6_ROUTING_TYPE_MODE_LIST = "list"
    IPV6_ROUTING_TYPE_MODE_DECR = "decr"

    IPV6_ROUTING_TYPE_STEP_CMD = "ipv6_routing_type_step"

    IPV6_ROUTING_TYPE_TRACKING_CMD = "ipv6_routing_type_tracking"

    IPV6_SRC_ADDR_CMD = "ipv6_src_addr"

    IPV6_SRC_COUNT_CMD = "ipv6_src_count"

    IPV6_SRC_MASK_CMD = "ipv6_src_mask"

    IPV6_SRC_MODE_CMD = "ipv6_src_mode"
    # Constant values for IPV6_SRC_MODE_CMD
    IPV6_SRC_MODE_FIXED = "fixed"
    IPV6_SRC_MODE_INCREMENT = "increment"
    IPV6_SRC_MODE_DECREMENT = "decrement"
    IPV6_SRC_MODE_LIST = "list"
    IPV6_SRC_MODE_RANDOM = "random"
    IPV6_SRC_MODE_INCR_HOST = "incr_host"
    IPV6_SRC_MODE_DECR_HOST = "decr_host"
    IPV6_SRC_MODE_INCR_NETWORK = "incr_network"
    IPV6_SRC_MODE_DECR_NETWORK = "decr_network"
    IPV6_SRC_MODE_INCR_INTF_ID = "incr_intf_id"
    IPV6_SRC_MODE_DECR_INTF_ID = "decr_intf_id"
    IPV6_SRC_MODE_INCR_GLOBAL_TOP_LEVEL = "incr_global_top_level"
    IPV6_SRC_MODE_DECR_GLOBAL_TOP_LEVEL = "decr_global_top_level"
    IPV6_SRC_MODE_INCR_GLOBAL_NEXT_LEVEL = "incr_global_next_level"
    IPV6_SRC_MODE_DECR_GLOBAL_NEXT_LEVEL = "decr_global_next_level"
    IPV6_SRC_MODE_INCR_GLOBAL_SITE_LEVEL = "incr_global_site_level"
    IPV6_SRC_MODE_DECR_GLOBAL_SITE_LEVEL = "decr_global_site_level"
    IPV6_SRC_MODE_INCR_LOCAL_SITE_SUBNET = "incr_local_site_subnet"
    IPV6_SRC_MODE_DECR_LOCAL_SITE_SUBNET = "decr_local_site_subnet"
    IPV6_SRC_MODE_INCR_MCAST_GROUP = "incr_mcast_group"
    IPV6_SRC_MODE_DECR_MCAST_GROUP = "decr_mcast_group"

    IPV6_SRC_STEP_CMD = "ipv6_src_step"

    IPV6_SRC_TRACKING_CMD = "ipv6_src_tracking"

    IPV6_TRAFFIC_CLASS_CMD = "ipv6_traffic_class"

    IPV6_TRAFFIC_CLASS_COUNT_CMD = "ipv6_traffic_class_count"

    IPV6_TRAFFIC_CLASS_MODE_CMD = "ipv6_traffic_class_mode"
    # Constant values for IPV6_TRAFFIC_CLASS_MODE_CMD
    IPV6_TRAFFIC_CLASS_MODE_INCR = "incr"
    IPV6_TRAFFIC_CLASS_MODE_FIXED = "fixed"
    IPV6_TRAFFIC_CLASS_MODE_LIST = "list"
    IPV6_TRAFFIC_CLASS_MODE_DECR = "decr"

    IPV6_TRAFFIC_CLASS_STEP_CMD = "ipv6_traffic_class_step"

    IPV6_TRAFFIC_CLASS_TRACKING_CMD = "ipv6_traffic_class_tracking"

    ISL_CMD = "isl"

    ISL_BPDU_CMD = "isl_bpdu"

    ISL_BPDU_COUNT_CMD = "isl_bpdu_count"

    ISL_BPDU_MODE_CMD = "isl_bpdu_mode"
    # Constant values for ISL_BPDU_MODE_CMD
    ISL_BPDU_MODE_INCR = "incr"
    ISL_BPDU_MODE_FIXED = "fixed"
    ISL_BPDU_MODE_LIST = "list"
    ISL_BPDU_MODE_DECR = "decr"

    ISL_BPDU_STEP_CMD = "isl_bpdu_step"

    ISL_BPDU_TRACKING_CMD = "isl_bpdu_tracking"

    ISL_FRAME_TYPE_CMD = "isl_frame_type"
    # Constant values for ISL_FRAME_TYPE_CMD
    ISL_FRAME_TYPE_ETHERNET = "ethernet"
    ISL_FRAME_TYPE_ATM = "atm"
    ISL_FRAME_TYPE_TOKEN_RING = "token_ring"
    ISL_FRAME_TYPE_FDDI = "fddi"

    ISL_FRAME_TYPE_MODE_CMD = "isl_frame_type_mode"
    # Constant values for ISL_FRAME_TYPE_MODE_CMD
    ISL_FRAME_TYPE_MODE_FIXED = "fixed"
    ISL_FRAME_TYPE_MODE_LIST = "list"

    ISL_FRAME_TYPE_TRACKING_CMD = "isl_frame_type_tracking"

    ISL_INDEX_CMD = "isl_index"

    ISL_INDEX_COUNT_CMD = "isl_index_count"

    ISL_INDEX_MODE_CMD = "isl_index_mode"
    # Constant values for ISL_INDEX_MODE_CMD
    ISL_INDEX_MODE_DEFAULT = "DEFAULT"
    ISL_INDEX_MODE_INCR = "incr"
    ISL_INDEX_MODE_FIXED = "fixed"
    ISL_INDEX_MODE_LIST = "list"
    ISL_INDEX_MODE_DECR = "decr"

    ISL_INDEX_STEP_CMD = "isl_index_step"

    ISL_INDEX_TRACKING_CMD = "isl_index_tracking"

    ISL_MAC_DST_CMD = "isl_mac_dst"

    ISL_MAC_DST_COUNT_CMD = "isl_mac_dst_count"

    ISL_MAC_DST_MODE_CMD = "isl_mac_dst_mode"
    # Constant values for ISL_MAC_DST_MODE_CMD
    ISL_MAC_DST_MODE_INCR = "incr"
    ISL_MAC_DST_MODE_FIXED = "fixed"
    ISL_MAC_DST_MODE_LIST = "list"
    ISL_MAC_DST_MODE_DECR = "decr"

    ISL_MAC_DST_STEP_CMD = "isl_mac_dst_step"

    ISL_MAC_DST_TRACKING_CMD = "isl_mac_dst_tracking"

    ISL_MAC_SRC_HIGH_CMD = "isl_mac_src_high"

    ISL_MAC_SRC_HIGH_COUNT_CMD = "isl_mac_src_high_count"

    ISL_MAC_SRC_HIGH_MODE_CMD = "isl_mac_src_high_mode"
    # Constant values for ISL_MAC_SRC_HIGH_MODE_CMD
    ISL_MAC_SRC_HIGH_MODE_INCR = "incr"
    ISL_MAC_SRC_HIGH_MODE_FIXED = "fixed"
    ISL_MAC_SRC_HIGH_MODE_LIST = "list"
    ISL_MAC_SRC_HIGH_MODE_DECR = "decr"

    ISL_MAC_SRC_HIGH_STEP_CMD = "isl_mac_src_high_step"

    ISL_MAC_SRC_HIGH_TRACKING_CMD = "isl_mac_src_high_tracking"

    ISL_MAC_SRC_LOW_CMD = "isl_mac_src_low"

    ISL_MAC_SRC_LOW_COUNT_CMD = "isl_mac_src_low_count"

    ISL_MAC_SRC_LOW_MODE_CMD = "isl_mac_src_low_mode"
    # Constant values for ISL_MAC_SRC_LOW_MODE_CMD
    ISL_MAC_SRC_LOW_MODE_INCR = "incr"
    ISL_MAC_SRC_LOW_MODE_FIXED = "fixed"
    ISL_MAC_SRC_LOW_MODE_LIST = "list"
    ISL_MAC_SRC_LOW_MODE_DECR = "decr"

    ISL_MAC_SRC_LOW_STEP_CMD = "isl_mac_src_low_step"

    ISL_MAC_SRC_LOW_TRACKING_CMD = "isl_mac_src_low_tracking"

    ISL_USER_PRIORITY_CMD = "isl_user_priority"

    ISL_USER_PRIORITY_COUNT_CMD = "isl_user_priority_count"

    ISL_USER_PRIORITY_MODE_CMD = "isl_user_priority_mode"
    # Constant values for ISL_USER_PRIORITY_MODE_CMD
    ISL_USER_PRIORITY_MODE_DEFAULT = "DEFAULT"
    ISL_USER_PRIORITY_MODE_INCR = "incr"
    ISL_USER_PRIORITY_MODE_FIXED = "fixed"
    ISL_USER_PRIORITY_MODE_LIST = "list"
    ISL_USER_PRIORITY_MODE_DECR = "decr"

    ISL_USER_PRIORITY_STEP_CMD = "isl_user_priority_step"

    ISL_USER_PRIORITY_TRACKING_CMD = "isl_user_priority_tracking"

    ISL_VLAN_ID_CMD = "isl_vlan_id"

    ISL_VLAN_ID_COUNT_CMD = "isl_vlan_id_count"

    ISL_VLAN_ID_MODE_CMD = "isl_vlan_id_mode"
    # Constant values for ISL_VLAN_ID_MODE_CMD
    ISL_VLAN_ID_MODE_INCR = "incr"
    ISL_VLAN_ID_MODE_FIXED = "fixed"
    ISL_VLAN_ID_MODE_LIST = "list"
    ISL_VLAN_ID_MODE_DECR = "decr"

    ISL_VLAN_ID_STEP_CMD = "isl_vlan_id_step"

    ISL_VLAN_ID_TRACKING_CMD = "isl_vlan_id_tracking"

    L2_ENCAP_CMD = "l2_encap"
    # Constant values for L2_ENCAP_CMD
    L2_ENCAP_HDLC_MULTICAST_MPLS = "hdlc_multicast_mpls"
    L2_ENCAP_ETHERNET_II = "ethernet_ii"
    L2_ENCAP_ATM_SNAP = "atm_snap"
    L2_ENCAP_ATM_VC_MUX_PPP = "atm_vc_mux_ppp"
    L2_ENCAP_ETHERNET_II_VLAN_PPPOE = "ethernet_ii_vlan_pppoe"
    L2_ENCAP_ETHERNET_8023_SNAP = "ethernet_8023_snap"
    L2_ENCAP_ETHERNET_8022_SAP = "ethernet_8022"
    L2_ENCAP_ATM_SNAP_802_3SNAP = "atm_snap_802.3snap"
    L2_ENCAP_ETHERNET_II_VLAN_UNICAST_MPLS = "ethernet_ii_vlan_unicast_mpls"
    L2_ENCAP_ETHERNET_II_UNICAST_MPLS = "ethernet_ii_unicast_mpls"
    L2_ENCAP_ETHERNET_II_MULTICAST_MPLS = "ethernet_ii_multicast_mpls"
    L2_ENCAP_CISCO_FRAMERELAY = "cisco_framerelay"
    L2_ENCAP_ATM_VC_MUX_802_3SNAP_NOFCS = "atm_vc_mux_802.3snap_nofcs"
    L2_ENCAP_PPP_LINK = "ppp_link"
    L2_ENCAP_HDLC_BROADCAST = "hdlc_broadcast"
    L2_ENCAP_ATM_SNAP_802_3SNAP_NOFCS = "atm_snap_802.3snap_nofcs"
    L2_ENCAP_ATM_SNAP_PPP = "atm_snap_ppp"
    L2_ENCAP_ATM_VC_MUX_802_3SNAP = "atm_vc_mux_802.3snap"
    L2_ENCAP_ATM_VC_MUX_ETHERNET_II = "atm_vc_mux_ethernet_ii"
    L2_ENCAP_ATM_SNAP_PPPOE = "atm_snap_pppoe"
    L2_ENCAP_ETHERNET_II_VLAN = "ethernet_ii_vlan"
    L2_ENCAP_IETF_FRAMERELAY = "ietf_framerelay"
    L2_ENCAP_HDLC_UNICAST_MPLS = "hdlc_unicast_mpls"
    L2_ENCAP_ETHERNET_II_VLAN_MULTICAST_MPLS = "ethernet_ii_vlan_multicast_mpls"
    L2_ENCAP_ATM_SNAP_ETHERNET_II = "atm_snap_ethernet_ii"
    L2_ENCAP_ETHERNET_II_PPPOE = "ethernet_ii_pppoe"
    L2_ENCAP_ATM_VC_MUX = "atm_vc_mux"
    L2_ENCAP_HDLC_UNICAST = "hdlc_unicast"
    L2_ENCAP_ATM_VC_MUX_PPPOE = "atm_vc_mux_pppoe"

    L3_GAUS1_AVG_CMD = "l3_gaus1_avg"

    L3_GAUS1_HALFBW_CMD = "l3_gaus1_halfbw"

    L3_GAUS1_WEIGHT_CMD = "l3_gaus1_weight"

    L3_GAUS2_AVG_CMD = "l3_gaus2_avg"

    L3_GAUS2_HALFBW_CMD = "l3_gaus2_halfbw"

    L3_GAUS2_WEIGHT_CMD = "l3_gaus2_weight"

    L3_GAUS3_AVG_CMD = "l3_gaus3_avg"

    L3_GAUS3_HALFBW_CMD = "l3_gaus3_halfbw"

    L3_GAUS3_WEIGHT_CMD = "l3_gaus3_weight"

    L3_GAUS4_AVG_CMD = "l3_gaus4_avg"

    L3_GAUS4_HALFBW_CMD = "l3_gaus4_halfbw"

    L3_GAUS4_WEIGHT_CMD = "l3_gaus4_weight"

    L3_IMIX1_RATIO_CMD = "l3_imix1_ratio"

    L3_IMIX1_SIZE_CMD = "l3_imix1_size"

    L3_IMIX2_RATIO_CMD = "l3_imix2_ratio"

    L3_IMIX2_SIZE_CMD = "l3_imix2_size"

    L3_IMIX3_RATIO_CMD = "l3_imix3_ratio"

    L3_IMIX3_SIZE_CMD = "l3_imix3_size"

    L3_IMIX4_RATIO_CMD = "l3_imix4_ratio"

    L3_IMIX4_SIZE_CMD = "l3_imix4_size"

    L3_LENGTH_CMD = "l3_length"

    L3_LENGTH_MAX_CMD = "l3_length_max"

    L3_LENGTH_MIN_CMD = "l3_length_min"

    L3_LENGTH_STEP_CMD = "l3_length_step"

    L3_PROTOCOL_CMD = "l3_protocol"
    # Constant values for L3_PROTOCOL_CMD
    L3_PROTOCOL_IPV4 = "ipv4"
    L3_PROTOCOL_IPV6 = "ipv6"
    L3_PROTOCOL_ARP = "arp"
    L3_PROTOCOL_PAUSE_CONTROL = "pause_control"
    L3_PROTOCOL_IPX = "ipx"
    L3_PROTOCOL_NONE = "none"

    L4_PROTOCOL_CMD = "l4_protocol"
    # Constant values for L4_PROTOCOL_CMD
    L4_PROTOCOL_ICMP = "icmp"
    L4_PROTOCOL_IGMP = "igmp"
    L4_PROTOCOL_GGP = "ggp"
    L4_PROTOCOL_GRE = "gre"
    L4_PROTOCOL_IP = "ip"
    L4_PROTOCOL_ST = "st"
    L4_PROTOCOL_TCP = "tcp"
    L4_PROTOCOL_UCL = "ucl"
    L4_PROTOCOL_EGP = "egp"
    L4_PROTOCOL_IGP = "igp"
    L4_PROTOCOL_BBN_RCC_MON = "bbn_rcc_mon"
    L4_PROTOCOL_NVP_II = "nvp_ii"
    L4_PROTOCOL_PUP = "pup"
    L4_PROTOCOL_ARGUS = "argus"
    L4_PROTOCOL_EMCON = "emcon"
    L4_PROTOCOL_XNET = "xnet"
    L4_PROTOCOL_CHAOS = "chaos"
    L4_PROTOCOL_UDP = "udp"
    L4_PROTOCOL_MUX = "mux"
    L4_PROTOCOL_DCN_MEAS = "dcn_meas"
    L4_PROTOCOL_HMP = "hmp"
    L4_PROTOCOL_PRM = "prm"
    L4_PROTOCOL_XNS_IDP = "xns_idp"
    L4_PROTOCOL_TRUNK_1 = "trunk_1"
    L4_PROTOCOL_TRUNK_2 = "trunk_2"
    L4_PROTOCOL_LEAF_1 = "leaf_1"
    L4_PROTOCOL_LEAF_2 = "leaf_2"
    L4_PROTOCOL_RDP = "rdp"
    L4_PROTOCOL_IRTP = "irtp"
    L4_PROTOCOL_ISO_TP4 = "iso_tp4"
    L4_PROTOCOL_NETBLT = "netblt"
    L4_PROTOCOL_MFE_NSP = "mfe_nsp"
    L4_PROTOCOL_MERIT_INP = "merit_inp"
    L4_PROTOCOL_SEP = "sep"
    L4_PROTOCOL_CFTP = "cftp"
    L4_PROTOCOL_SAT_EXPAK = "sat_expak"
    L4_PROTOCOL_MIT_SUBNET = "mit_subnet"
    L4_PROTOCOL_RVD = "rvd"
    L4_PROTOCOL_IPPC = "ippc"
    L4_PROTOCOL_SAT_MON = "sat_mon"
    L4_PROTOCOL_IPCV = "ipcv"
    L4_PROTOCOL_BR_SAT_MON = "br_sat_mon"
    L4_PROTOCOL_WB_MON = "wb_mon"
    L4_PROTOCOL_WB_EXPAK = "wb_expak"
    L4_PROTOCOL_RIP = "rip"
    L4_PROTOCOL_OSPF = "ospf"

    LAN_RANGE_COUNT_CMD = "lan_range_count"

    LATENCY_BINS_CMD = "latency_bins"

    LATENCY_BINS_ENABLE_CMD = "latency_bins_enable"

    LATENCY_VALUES_CMD = "latency_values"

    LENGTH_MODE_CMD = "length_mode"
    # Constant values for LENGTH_MODE_CMD
    LENGTH_MODE_AUTO = "auto"
    LENGTH_MODE_RANDOM = "random"
    LENGTH_MODE_GAUSSIAN = "gaussian"
    LENGTH_MODE_INCREMENT = "increment"
    LENGTH_MODE_QUAD = "quad"
    LENGTH_MODE_DISTRIBUTION = "distribution"
    LENGTH_MODE_FIXED = "fixed"
    LENGTH_MODE_IMIX = "imix"

    LOOP_COUNT_CMD = "loop_count"

    MAC_DISCOVERY_GW_CMD = "mac_discovery_gw"

    MAC_DST_CMD = "mac_dst"

    MAC_DST2_CMD = "mac_dst2"

    MAC_DST2_COUNT_CMD = "mac_dst2_count"

    MAC_DST2_MODE_CMD = "mac_dst2_mode"

    MAC_DST2_STEP_CMD = "mac_dst2_step"

    MAC_DST_COUNT_CMD = "mac_dst_count"

    MAC_DST_COUNT_STEP_CMD = "mac_dst_count_step"

    MAC_DST_MASK_CMD = "mac_dst_mask"

    MAC_DST_MODE_CMD = "mac_dst_mode"
    # Constant values for MAC_DST_MODE_CMD
    MAC_DST_MODE_FIXED = "fixed"
    MAC_DST_MODE_INCREMENT = "increment"
    MAC_DST_MODE_LIST = "list"
    MAC_DST_MODE_DECREMENT = "decrement"
    MAC_DST_MODE_DISCOVERY = "discovery"
    MAC_DST_MODE_RANDOM = "random"
    MAC_DST_MODE_REPEATABLE_RANDOM = "repeatable_random"

    MAC_DST_SEED_CMD = "mac_dst_seed"

    MAC_DST_STEP_CMD = "mac_dst_step"

    MAC_DST_TRACKING_CMD = "mac_dst_tracking"

    MAC_SRC_CMD = "mac_src"

    MAC_SRC2_CMD = "mac_src2"

    MAC_SRC2_COUNT_CMD = "mac_src2_count"

    MAC_SRC2_MODE_CMD = "mac_src2_mode"

    MAC_SRC2_STEP_CMD = "mac_src2_step"

    MAC_SRC_COUNT_CMD = "mac_src_count"

    MAC_SRC_MASK_CMD = "mac_src_mask"

    MAC_SRC_MODE_CMD = "mac_src_mode"
    # Constant values for MAC_SRC_MODE_CMD
    MAC_SRC_MODE_FIXED = "fixed"
    MAC_SRC_MODE_INCREMENT = "increment"
    MAC_SRC_MODE_LIST = "list"
    MAC_SRC_MODE_DECREMENT = "decrement"
    MAC_SRC_MODE_DISCOVERY = "discovery"
    MAC_SRC_MODE_RANDOM = "random"
    MAC_SRC_MODE_REPEATABLE_RANDOM = "repeatable_random"

    MAC_SRC_SEED_CMD = "mac_src_seed"

    MAC_SRC_STEP_CMD = "mac_src_step"

    MAC_SRC_TRACKING_CMD = "mac_src_tracking"

    MERGE_DESTINATIONS_CMD = "merge_destinations"

    MIN_GAP_BYTES_CMD = "min_gap_bytes"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CREATE = "create"
    MODE_MODIFY = "modify"
    MODE_REMOVE = "remove"
    MODE_RESET = "reset"
    MODE_ENABLE = "enable"
    MODE_DISABLE = "disable"
    MODE_APPEND_HEADER = "append_header"
    MODE_PREPEND_HEADER = "prepend_header"
    MODE_REPLACE_HEADER = "replace_header"
    MODE_MODIFY_OR_INSERT = "modify_or_insert"
    MODE_DYNAMIC_UPDATE = "dynamic_update"
    MODE_GET_AVAILABLE_PROTOCOL_TEMPLATES = "get_available_protocol_templates"
    MODE_GET_AVAILABLE_FIELDS = "get_available_fields"
    MODE_GET_FIELD_VALUES = "get_field_values"
    MODE_SET_FIELD_VALUES = "set_field_values"
    MODE_ADD_FIELD_LEVEL = "add_field_level"
    MODE_REMOVE_FIELD_LEVEL = "remove_field_level"
    MODE_GET_AVAILABLE_EGRESS_TRACKING_FIELD_OFFSET = "get_available_egress_tracking_field_offset"
    MODE_GET_AVAILABLE_DYNAMIC_UPDATE_FIELDS = "get_available_dynamic_update_fields"
    MODE_GET_AVAILABLE_SESSION_AWARE_TRAFFIC = "get_available_session_aware_traffic"
    MODE_GET_AVAILABLE_FIELD = "get_available_field"

    MPLS_CMD = "mpls"
    # Constant values for MPLS_CMD
    MPLS_ENABLE = "enable"
    MPLS_DISABLE = "disable"

    MPLS_BOTTOM_STACK_BIT_CMD = "mpls_bottom_stack_bit"

    MPLS_BOTTOM_STACK_BIT_COUNT_CMD = "mpls_bottom_stack_bit_count"

    MPLS_BOTTOM_STACK_BIT_MODE_CMD = "mpls_bottom_stack_bit_mode"
    # Constant values for MPLS_BOTTOM_STACK_BIT_MODE_CMD
    MPLS_BOTTOM_STACK_BIT_MODE_INCR = "incr"
    MPLS_BOTTOM_STACK_BIT_MODE_FIXED = "fixed"
    MPLS_BOTTOM_STACK_BIT_MODE_LIST = "list"
    MPLS_BOTTOM_STACK_BIT_MODE_DECR = "decr"

    MPLS_BOTTOM_STACK_BIT_STEP_CMD = "mpls_bottom_stack_bit_step"

    MPLS_BOTTOM_STACK_BIT_TRACKING_CMD = "mpls_bottom_stack_bit_tracking"

    MPLS_EXP_BIT_CMD = "mpls_exp_bit"

    MPLS_EXP_BIT_COUNT_CMD = "mpls_exp_bit_count"

    MPLS_EXP_BIT_MODE_CMD = "mpls_exp_bit_mode"
    # Constant values for MPLS_EXP_BIT_MODE_CMD
    MPLS_EXP_BIT_MODE_INCR = "incr"
    MPLS_EXP_BIT_MODE_FIXED = "fixed"
    MPLS_EXP_BIT_MODE_LIST = "list"
    MPLS_EXP_BIT_MODE_DECR = "decr"

    MPLS_EXP_BIT_STEP_CMD = "mpls_exp_bit_step"

    MPLS_EXP_BIT_TRACKING_CMD = "mpls_exp_bit_tracking"

    MPLS_LABELS_CMD = "mpls_labels"

    MPLS_LABELS_COUNT_CMD = "mpls_labels_count"

    MPLS_LABELS_MODE_CMD = "mpls_labels_mode"
    # Constant values for MPLS_LABELS_MODE_CMD
    MPLS_LABELS_MODE_INCR = "incr"
    MPLS_LABELS_MODE_FIXED = "fixed"
    MPLS_LABELS_MODE_DECR = "decr"

    MPLS_LABELS_STEP_CMD = "mpls_labels_step"

    MPLS_LABELS_TRACKING_CMD = "mpls_labels_tracking"

    MPLS_TTL_CMD = "mpls_ttl"

    MPLS_TTL_COUNT_CMD = "mpls_ttl_count"

    MPLS_TTL_MODE_CMD = "mpls_ttl_mode"
    # Constant values for MPLS_TTL_MODE_CMD
    MPLS_TTL_MODE_INCR = "incr"
    MPLS_TTL_MODE_FIXED = "fixed"
    MPLS_TTL_MODE_DECR = "decr"

    MPLS_TTL_STEP_CMD = "mpls_ttl_step"

    MPLS_TTL_TRACKING_CMD = "mpls_ttl_tracking"

    MPLS_TYPE_CMD = "mpls_type"
    # Constant values for MPLS_TYPE_CMD
    MPLS_TYPE_UNICAST = "unicast"
    MPLS_TYPE_MULTICAST = "multicast"

    MULTIPLE_QUEUES_CMD = "multiple_queues"

    NAME_CMD = "name"

    NO_WRITE_CMD = "no_write"

    NUM_DST_PORTS_CMD = "num_dst_ports"

    NUMBER_OF_PACKETS_PER_STREAM_CMD = "number_of_packets_per_stream"

    NUMBER_OF_PACKETS_TX_CMD = "number_of_packets_tx"

    OVERRIDE_VALUE_LIST_CMD = "override_value_list"

    PAUSE_CONTROL_TIME_CMD = "pause_control_time"

    PENDING_OPERATIONS_TIMEOUT_CMD = "pending_operations_timeout"

    PGID_OFFSET_CMD = "pgid_offset"

    PGID_VALUE_CMD = "pgid_value"

    PKTS_PER_BURST_CMD = "pkts_per_burst"

    PORT_HANDLE_CMD = "port_handle"

    PORT_HANDLE2_CMD = "port_handle2"

    PPP_SESSION_ID_CMD = "ppp_session_id"

    PREAMBLE_CUSTOM_SIZE_CMD = "preamble_custom_size"

    PREAMBLE_SIZE_MODE_CMD = "preamble_size_mode"

    PT_HANDLE_CMD = "pt_handle"

    PUBLIC_PORT_IP_CMD = "public_port_ip"

    PVC_COUNT_CMD = "pvc_count"

    PVC_COUNT_STEP_CMD = "pvc_count_step"

    QOS_BYTE_CMD = "qos_byte"

    QOS_BYTE_COUNT_CMD = "qos_byte_count"

    QOS_BYTE_MODE_CMD = "qos_byte_mode"
    # Constant values for QOS_BYTE_MODE_CMD
    QOS_BYTE_MODE_INCR = "incr"
    QOS_BYTE_MODE_FIXED = "fixed"
    QOS_BYTE_MODE_LIST = "list"
    QOS_BYTE_MODE_DECR = "decr"

    QOS_BYTE_STEP_CMD = "qos_byte_step"

    QOS_BYTE_TRACKING_CMD = "qos_byte_tracking"

    QOS_IPV6_FLOW_LABEL_CMD = "qos_ipv6_flow_label"

    QOS_IPV6_TRAFFIC_CLASS_CMD = "qos_ipv6_traffic_class"

    QOS_TYPE_IXN_CMD = "qos_type_ixn"
    # Constant values for QOS_TYPE_IXN_CMD
    QOS_TYPE_IXN_TOS = "tos"
    QOS_TYPE_IXN_IPV6 = "ipv6"
    QOS_TYPE_IXN_DSCP = "dscp"
    QOS_TYPE_IXN_CUSTOM = "custom"

    QOS_VALUE_IXN_CMD = "qos_value_ixn"

    QOS_VALUE_IXN_COUNT_CMD = "qos_value_ixn_count"

    QOS_VALUE_IXN_MODE_CMD = "qos_value_ixn_mode"
    # Constant values for QOS_VALUE_IXN_MODE_CMD
    QOS_VALUE_IXN_MODE_INCR = "incr"
    QOS_VALUE_IXN_MODE_FIXED = "fixed"
    QOS_VALUE_IXN_MODE_LIST = "list"
    QOS_VALUE_IXN_MODE_DECR = "decr"

    QOS_VALUE_IXN_STEP_CMD = "qos_value_ixn_step"

    QOS_VALUE_IXN_TRACKING_CMD = "qos_value_ixn_tracking"

    QUEUE_ID_CMD = "queue_id"

    RAMP_UP_PERCENTAGE_CMD = "ramp_up_percentage"

    RANGE_PER_SPOKE_CMD = "range_per_spoke"

    RATE_BPS_CMD = "rate_bps"

    RATE_BYTEPS_CMD = "rate_byteps"

    RATE_FRAME_GAP_CMD = "rate_frame_gap"

    RATE_KBPS_CMD = "rate_kbps"

    RATE_KBYTEPS_CMD = "rate_kbyteps"

    RATE_MBPS_CMD = "rate_mbps"

    RATE_MBYTEPS_CMD = "rate_mbyteps"

    RATE_MODE_CMD = "rate_mode"

    RATE_PERCENT_CMD = "rate_percent"

    RATE_PPS_CMD = "rate_pps"

    RETURN_TO_ID_CMD = "return_to_id"

    RIP_COMMAND_CMD = "rip_command"
    # Constant values for RIP_COMMAND_CMD
    RIP_COMMAND_TRACE_ON = "trace_on"
    RIP_COMMAND_RESERVED = "reserved"
    RIP_COMMAND_REQUEST = "request"
    RIP_COMMAND_RESPONSE = "response"
    RIP_COMMAND_TRACE_OFF = "trace_off"

    RIP_COMMAND_MODE_CMD = "rip_command_mode"
    # Constant values for RIP_COMMAND_MODE_CMD
    RIP_COMMAND_MODE_FIXED = "fixed"
    RIP_COMMAND_MODE_LIST = "list"

    RIP_COMMAND_TRACKING_CMD = "rip_command_tracking"

    RIP_RTE_ADDR_FAMILY_ID_CMD = "rip_rte_addr_family_id"

    RIP_RTE_ADDR_FAMILY_ID_COUNT_CMD = "rip_rte_addr_family_id_count"

    RIP_RTE_ADDR_FAMILY_ID_MODE_CMD = "rip_rte_addr_family_id_mode"
    # Constant values for RIP_RTE_ADDR_FAMILY_ID_MODE_CMD
    RIP_RTE_ADDR_FAMILY_ID_MODE_INCR = "incr"
    RIP_RTE_ADDR_FAMILY_ID_MODE_FIXED = "fixed"
    RIP_RTE_ADDR_FAMILY_ID_MODE_LIST = "list"
    RIP_RTE_ADDR_FAMILY_ID_MODE_DECR = "decr"

    RIP_RTE_ADDR_FAMILY_ID_STEP_CMD = "rip_rte_addr_family_id_step"

    RIP_RTE_ADDR_FAMILY_ID_TRACKING_CMD = "rip_rte_addr_family_id_tracking"

    RIP_RTE_IPV4_ADDR_CMD = "rip_rte_ipv4_addr"

    RIP_RTE_IPV4_ADDR_COUNT_CMD = "rip_rte_ipv4_addr_count"

    RIP_RTE_IPV4_ADDR_MODE_CMD = "rip_rte_ipv4_addr_mode"
    # Constant values for RIP_RTE_IPV4_ADDR_MODE_CMD
    RIP_RTE_IPV4_ADDR_MODE_INCR = "incr"
    RIP_RTE_IPV4_ADDR_MODE_FIXED = "fixed"
    RIP_RTE_IPV4_ADDR_MODE_DECR = "decr"

    RIP_RTE_IPV4_ADDR_STEP_CMD = "rip_rte_ipv4_addr_step"

    RIP_RTE_IPV4_ADDR_TRACKING_CMD = "rip_rte_ipv4_addr_tracking"

    RIP_RTE_METRIC_CMD = "rip_rte_metric"

    RIP_RTE_METRIC_COUNT_CMD = "rip_rte_metric_count"

    RIP_RTE_METRIC_MODE_CMD = "rip_rte_metric_mode"
    # Constant values for RIP_RTE_METRIC_MODE_CMD
    RIP_RTE_METRIC_MODE_INCR = "incr"
    RIP_RTE_METRIC_MODE_FIXED = "fixed"
    RIP_RTE_METRIC_MODE_DECR = "decr"

    RIP_RTE_METRIC_STEP_CMD = "rip_rte_metric_step"

    RIP_RTE_METRIC_TRACKING_CMD = "rip_rte_metric_tracking"

    RIP_RTE_V1_UNUSED2_CMD = "rip_rte_v1_unused2"

    RIP_RTE_V1_UNUSED2_COUNT_CMD = "rip_rte_v1_unused2_count"

    RIP_RTE_V1_UNUSED2_MODE_CMD = "rip_rte_v1_unused2_mode"
    # Constant values for RIP_RTE_V1_UNUSED2_MODE_CMD
    RIP_RTE_V1_UNUSED2_MODE_INCR = "incr"
    RIP_RTE_V1_UNUSED2_MODE_FIXED = "fixed"
    RIP_RTE_V1_UNUSED2_MODE_DECR = "decr"

    RIP_RTE_V1_UNUSED2_STEP_CMD = "rip_rte_v1_unused2_step"

    RIP_RTE_V1_UNUSED2_TRACKING_CMD = "rip_rte_v1_unused2_tracking"

    RIP_RTE_V1_UNUSED3_CMD = "rip_rte_v1_unused3"

    RIP_RTE_V1_UNUSED3_COUNT_CMD = "rip_rte_v1_unused3_count"

    RIP_RTE_V1_UNUSED3_MODE_CMD = "rip_rte_v1_unused3_mode"
    # Constant values for RIP_RTE_V1_UNUSED3_MODE_CMD
    RIP_RTE_V1_UNUSED3_MODE_INCR = "incr"
    RIP_RTE_V1_UNUSED3_MODE_FIXED = "fixed"
    RIP_RTE_V1_UNUSED3_MODE_DECR = "decr"

    RIP_RTE_V1_UNUSED3_STEP_CMD = "rip_rte_v1_unused3_step"

    RIP_RTE_V1_UNUSED3_TRACKING_CMD = "rip_rte_v1_unused3_tracking"

    RIP_RTE_V1_UNUSED4_CMD = "rip_rte_v1_unused4"

    RIP_RTE_V1_UNUSED4_COUNT_CMD = "rip_rte_v1_unused4_count"

    RIP_RTE_V1_UNUSED4_MODE_CMD = "rip_rte_v1_unused4_mode"
    # Constant values for RIP_RTE_V1_UNUSED4_MODE_CMD
    RIP_RTE_V1_UNUSED4_MODE_INCR = "incr"
    RIP_RTE_V1_UNUSED4_MODE_FIXED = "fixed"
    RIP_RTE_V1_UNUSED4_MODE_DECR = "decr"

    RIP_RTE_V1_UNUSED4_STEP_CMD = "rip_rte_v1_unused4_step"

    RIP_RTE_V1_UNUSED4_TRACKING_CMD = "rip_rte_v1_unused4_tracking"

    RIP_RTE_V2_NEXT_HOP_CMD = "rip_rte_v2_next_hop"

    RIP_RTE_V2_NEXT_HOP_COUNT_CMD = "rip_rte_v2_next_hop_count"

    RIP_RTE_V2_NEXT_HOP_MODE_CMD = "rip_rte_v2_next_hop_mode"
    # Constant values for RIP_RTE_V2_NEXT_HOP_MODE_CMD
    RIP_RTE_V2_NEXT_HOP_MODE_INCR = "incr"
    RIP_RTE_V2_NEXT_HOP_MODE_FIXED = "fixed"
    RIP_RTE_V2_NEXT_HOP_MODE_DECR = "decr"

    RIP_RTE_V2_NEXT_HOP_STEP_CMD = "rip_rte_v2_next_hop_step"

    RIP_RTE_V2_NEXT_HOP_TRACKING_CMD = "rip_rte_v2_next_hop_tracking"

    RIP_RTE_V2_ROUTE_TAG_CMD = "rip_rte_v2_route_tag"

    RIP_RTE_V2_ROUTE_TAG_COUNT_CMD = "rip_rte_v2_route_tag_count"

    RIP_RTE_V2_ROUTE_TAG_MODE_CMD = "rip_rte_v2_route_tag_mode"
    # Constant values for RIP_RTE_V2_ROUTE_TAG_MODE_CMD
    RIP_RTE_V2_ROUTE_TAG_MODE_INCR = "incr"
    RIP_RTE_V2_ROUTE_TAG_MODE_FIXED = "fixed"
    RIP_RTE_V2_ROUTE_TAG_MODE_DECR = "decr"

    RIP_RTE_V2_ROUTE_TAG_STEP_CMD = "rip_rte_v2_route_tag_step"

    RIP_RTE_V2_ROUTE_TAG_TRACKING_CMD = "rip_rte_v2_route_tag_tracking"

    RIP_RTE_V2_SUBNET_MASK_CMD = "rip_rte_v2_subnet_mask"

    RIP_RTE_V2_SUBNET_MASK_COUNT_CMD = "rip_rte_v2_subnet_mask_count"

    RIP_RTE_V2_SUBNET_MASK_MODE_CMD = "rip_rte_v2_subnet_mask_mode"
    # Constant values for RIP_RTE_V2_SUBNET_MASK_MODE_CMD
    RIP_RTE_V2_SUBNET_MASK_MODE_INCR = "incr"
    RIP_RTE_V2_SUBNET_MASK_MODE_FIXED = "fixed"
    RIP_RTE_V2_SUBNET_MASK_MODE_DECR = "decr"

    RIP_RTE_V2_SUBNET_MASK_STEP_CMD = "rip_rte_v2_subnet_mask_step"

    RIP_RTE_V2_SUBNET_MASK_TRACKING_CMD = "rip_rte_v2_subnet_mask_tracking"

    RIP_UNUSED_CMD = "rip_unused"

    RIP_UNUSED_COUNT_CMD = "rip_unused_count"

    RIP_UNUSED_MODE_CMD = "rip_unused_mode"
    # Constant values for RIP_UNUSED_MODE_CMD
    RIP_UNUSED_MODE_INCR = "incr"
    RIP_UNUSED_MODE_FIXED = "fixed"
    RIP_UNUSED_MODE_LIST = "list"
    RIP_UNUSED_MODE_DECR = "decr"

    RIP_UNUSED_STEP_CMD = "rip_unused_step"

    RIP_UNUSED_TRACKING_CMD = "rip_unused_tracking"

    RIP_VERSION_CMD = "rip_version"
    # Constant values for RIP_VERSION_CMD
    RIP_VERSION_1 = "1"
    RIP_VERSION_2 = "2"

    ROUTE_MESH_CMD = "route_mesh"
    # Constant values for ROUTE_MESH_CMD
    ROUTE_MESH_FULLY = "fully"
    ROUTE_MESH_ONE_TO_ONE = "one_to_one"

    RTP_CSRC_COUNT_CMD = "rtp_csrc_count"

    RTP_PAYLOAD_TYPE_CMD = "rtp_payload_type"

    SESSION_AWARE_TRAFFIC_CMD = "session_aware_traffic"
    # Constant values for SESSION_AWARE_TRAFFIC_CMD
    SESSION_AWARE_TRAFFIC_PPP = "ppp"

    SIGNATURE_CMD = "signature"

    SIGNATURE_OFFSET_CMD = "signature_offset"

    SITE_ID_CMD = "site_id"

    SITE_ID_ENABLE_CMD = "site_id_enable"

    SITE_ID_STEP_CMD = "site_id_step"

    SKIP_FRAME_SIZE_VALIDATION_CMD = "skip_frame_size_validation"

    SOURCE_FILTER_CMD = "source_filter"
    # Constant values for SOURCE_FILTER_CMD
    SOURCE_FILTER_6PE = "6pe"
    SOURCE_FILTER_ALL = "all"
    SOURCE_FILTER_6VPE = "6vpe"
    SOURCE_FILTER_ATM = "atm"
    SOURCE_FILTER_MPLS = "mpls"
    SOURCE_FILTER_NONE = "none"
    SOURCE_FILTER_HDLC = "hdlc"
    SOURCE_FILTER_L3VPN = "l3vpn"
    SOURCE_FILTER_PPP = "ppp"
    SOURCE_FILTER_FRAMERELAY = "framerelay"
    SOURCE_FILTER_DATA_CENTER_BRIDGING = "data_center_bridging"
    SOURCE_FILTER_ETHERNET = "ethernet"
    SOURCE_FILTER_L2VPN = "l2vpn"
    SOURCE_FILTER_MAC_IN_MAC = "mac_in_mac"
    SOURCE_FILTER_BGPVPLS = "bgpvpls"

    SRC_DEST_MESH_CMD = "src_dest_mesh"
    # Constant values for SRC_DEST_MESH_CMD
    SRC_DEST_MESH_FULLY = "fully"
    SRC_DEST_MESH_MANY_TO_MANY = "many_to_many"
    SRC_DEST_MESH_ONE_TO_ONE = "one_to_one"

    SSRC_CMD = "ssrc"

    STACK_INDEX_CMD = "stack_index"

    STREAM_ID_CMD = "stream_id"

    STREAM_PACKING_CMD = "stream_packing"
    # Constant values for STREAM_PACKING_CMD
    STREAM_PACKING_ONE_STREAM_PER_ENDPOINT_PAIR = "one_stream_per_endpoint_pair"
    STREAM_PACKING_MERGE_DESTINATION_RANGES = "merge_destination_ranges"
    STREAM_PACKING_OPTIMAL_PACKING = "optimal_packing"

    TABLE_UDF_COLUMN_NAME_CMD = "table_udf_column_name"

    TABLE_UDF_COLUMN_OFFSET_CMD = "table_udf_column_offset"

    TABLE_UDF_COLUMN_SIZE_CMD = "table_udf_column_size"

    TABLE_UDF_COLUMN_TYPE_CMD = "table_udf_column_type"
    # Constant values for TABLE_UDF_COLUMN_TYPE_CMD
    TABLE_UDF_COLUMN_TYPE_BINARY = "binary"

    TABLE_UDF_ROWS_CMD = "table_udf_rows"

    TAG_FILTER_CMD = "tag_filter"

    TCP_ACK_FLAG_CMD = "tcp_ack_flag"

    TCP_ACK_FLAG_MODE_CMD = "tcp_ack_flag_mode"
    # Constant values for TCP_ACK_FLAG_MODE_CMD
    TCP_ACK_FLAG_MODE_FIXED = "fixed"
    TCP_ACK_FLAG_MODE_LIST = "list"

    TCP_ACK_FLAG_TRACKING_CMD = "tcp_ack_flag_tracking"

    TCP_ACK_NUM_CMD = "tcp_ack_num"

    TCP_ACK_NUM_COUNT_CMD = "tcp_ack_num_count"

    TCP_ACK_NUM_MODE_CMD = "tcp_ack_num_mode"
    # Constant values for TCP_ACK_NUM_MODE_CMD
    TCP_ACK_NUM_MODE_INCR = "incr"
    TCP_ACK_NUM_MODE_FIXED = "fixed"
    TCP_ACK_NUM_MODE_LIST = "list"
    TCP_ACK_NUM_MODE_DECR = "decr"

    TCP_ACK_NUM_STEP_CMD = "tcp_ack_num_step"

    TCP_ACK_NUM_TRACKING_CMD = "tcp_ack_num_tracking"

    TCP_CHECKSUM_CMD = "tcp_checksum"

    TCP_CHECKSUM_COUNT_CMD = "tcp_checksum_count"

    TCP_CHECKSUM_MODE_CMD = "tcp_checksum_mode"
    # Constant values for TCP_CHECKSUM_MODE_CMD
    TCP_CHECKSUM_MODE_INCR = "incr"
    TCP_CHECKSUM_MODE_FIXED = "fixed"
    TCP_CHECKSUM_MODE_LIST = "list"
    TCP_CHECKSUM_MODE_DECR = "decr"

    TCP_CHECKSUM_STEP_CMD = "tcp_checksum_step"

    TCP_CHECKSUM_TRACKING_CMD = "tcp_checksum_tracking"

    TCP_CWR_FLAG_CMD = "tcp_cwr_flag"

    TCP_CWR_FLAG_MODE_CMD = "tcp_cwr_flag_mode"
    # Constant values for TCP_CWR_FLAG_MODE_CMD
    TCP_CWR_FLAG_MODE_FIXED = "fixed"
    TCP_CWR_FLAG_MODE_LIST = "list"

    TCP_CWR_FLAG_TRACKING_CMD = "tcp_cwr_flag_tracking"

    TCP_DATA_OFFSET_CMD = "tcp_data_offset"

    TCP_DATA_OFFSET_COUNT_CMD = "tcp_data_offset_count"

    TCP_DATA_OFFSET_MODE_CMD = "tcp_data_offset_mode"
    # Constant values for TCP_DATA_OFFSET_MODE_CMD
    TCP_DATA_OFFSET_MODE_INCR = "incr"
    TCP_DATA_OFFSET_MODE_FIXED = "fixed"
    TCP_DATA_OFFSET_MODE_LIST = "list"
    TCP_DATA_OFFSET_MODE_DECR = "decr"

    TCP_DATA_OFFSET_STEP_CMD = "tcp_data_offset_step"

    TCP_DATA_OFFSET_TRACKING_CMD = "tcp_data_offset_tracking"

    TCP_DST_PORT_CMD = "tcp_dst_port"

    TCP_DST_PORT_COUNT_CMD = "tcp_dst_port_count"

    TCP_DST_PORT_MODE_CMD = "tcp_dst_port_mode"
    # Constant values for TCP_DST_PORT_MODE_CMD
    TCP_DST_PORT_MODE_INCR = "incr"
    TCP_DST_PORT_MODE_FIXED = "fixed"
    TCP_DST_PORT_MODE_LIST = "list"
    TCP_DST_PORT_MODE_DECR = "decr"

    TCP_DST_PORT_STEP_CMD = "tcp_dst_port_step"

    TCP_DST_PORT_TRACKING_CMD = "tcp_dst_port_tracking"

    TCP_ECN_ECHO_FLAG_CMD = "tcp_ecn_echo_flag"

    TCP_ECN_ECHO_FLAG_MODE_CMD = "tcp_ecn_echo_flag_mode"
    # Constant values for TCP_ECN_ECHO_FLAG_MODE_CMD
    TCP_ECN_ECHO_FLAG_MODE_FIXED = "fixed"
    TCP_ECN_ECHO_FLAG_MODE_LIST = "list"

    TCP_ECN_ECHO_FLAG_TRACKING_CMD = "tcp_ecn_echo_flag_tracking"

    TCP_FIN_FLAG_CMD = "tcp_fin_flag"

    TCP_FIN_FLAG_MODE_CMD = "tcp_fin_flag_mode"
    # Constant values for TCP_FIN_FLAG_MODE_CMD
    TCP_FIN_FLAG_MODE_FIXED = "fixed"
    TCP_FIN_FLAG_MODE_LIST = "list"

    TCP_FIN_FLAG_TRACKING_CMD = "tcp_fin_flag_tracking"

    TCP_NS_FLAG_CMD = "tcp_ns_flag"

    TCP_NS_FLAG_MODE_CMD = "tcp_ns_flag_mode"
    # Constant values for TCP_NS_FLAG_MODE_CMD
    TCP_NS_FLAG_MODE_FIXED = "fixed"
    TCP_NS_FLAG_MODE_LIST = "list"

    TCP_NS_FLAG_TRACKING_CMD = "tcp_ns_flag_tracking"

    TCP_PSH_FLAG_CMD = "tcp_psh_flag"

    TCP_PSH_FLAG_MODE_CMD = "tcp_psh_flag_mode"
    # Constant values for TCP_PSH_FLAG_MODE_CMD
    TCP_PSH_FLAG_MODE_FIXED = "fixed"
    TCP_PSH_FLAG_MODE_LIST = "list"

    TCP_PSH_FLAG_TRACKING_CMD = "tcp_psh_flag_tracking"

    TCP_RESERVED_CMD = "tcp_reserved"

    TCP_RESERVED_COUNT_CMD = "tcp_reserved_count"

    TCP_RESERVED_MODE_CMD = "tcp_reserved_mode"
    # Constant values for TCP_RESERVED_MODE_CMD
    TCP_RESERVED_MODE_INCR = "incr"
    TCP_RESERVED_MODE_FIXED = "fixed"
    TCP_RESERVED_MODE_LIST = "list"
    TCP_RESERVED_MODE_DECR = "decr"

    TCP_RESERVED_STEP_CMD = "tcp_reserved_step"

    TCP_RESERVED_TRACKING_CMD = "tcp_reserved_tracking"

    TCP_RST_FLAG_CMD = "tcp_rst_flag"

    TCP_RST_FLAG_MODE_CMD = "tcp_rst_flag_mode"
    # Constant values for TCP_RST_FLAG_MODE_CMD
    TCP_RST_FLAG_MODE_FIXED = "fixed"
    TCP_RST_FLAG_MODE_LIST = "list"

    TCP_RST_FLAG_TRACKING_CMD = "tcp_rst_flag_tracking"

    TCP_SEQ_NUM_CMD = "tcp_seq_num"

    TCP_SEQ_NUM_COUNT_CMD = "tcp_seq_num_count"

    TCP_SEQ_NUM_MODE_CMD = "tcp_seq_num_mode"
    # Constant values for TCP_SEQ_NUM_MODE_CMD
    TCP_SEQ_NUM_MODE_INCR = "incr"
    TCP_SEQ_NUM_MODE_FIXED = "fixed"
    TCP_SEQ_NUM_MODE_LIST = "list"
    TCP_SEQ_NUM_MODE_DECR = "decr"

    TCP_SEQ_NUM_STEP_CMD = "tcp_seq_num_step"

    TCP_SEQ_NUM_TRACKING_CMD = "tcp_seq_num_tracking"

    TCP_SRC_PORT_CMD = "tcp_src_port"

    TCP_SRC_PORT_COUNT_CMD = "tcp_src_port_count"

    TCP_SRC_PORT_MODE_CMD = "tcp_src_port_mode"
    # Constant values for TCP_SRC_PORT_MODE_CMD
    TCP_SRC_PORT_MODE_INCR = "incr"
    TCP_SRC_PORT_MODE_FIXED = "fixed"
    TCP_SRC_PORT_MODE_LIST = "list"
    TCP_SRC_PORT_MODE_DECR = "decr"

    TCP_SRC_PORT_STEP_CMD = "tcp_src_port_step"

    TCP_SRC_PORT_TRACKING_CMD = "tcp_src_port_tracking"

    TCP_SYN_FLAG_CMD = "tcp_syn_flag"

    TCP_SYN_FLAG_MODE_CMD = "tcp_syn_flag_mode"
    # Constant values for TCP_SYN_FLAG_MODE_CMD
    TCP_SYN_FLAG_MODE_FIXED = "fixed"
    TCP_SYN_FLAG_MODE_LIST = "list"

    TCP_SYN_FLAG_TRACKING_CMD = "tcp_syn_flag_tracking"

    TCP_URG_FLAG_CMD = "tcp_urg_flag"

    TCP_URG_FLAG_MODE_CMD = "tcp_urg_flag_mode"
    # Constant values for TCP_URG_FLAG_MODE_CMD
    TCP_URG_FLAG_MODE_FIXED = "fixed"
    TCP_URG_FLAG_MODE_LIST = "list"

    TCP_URG_FLAG_TRACKING_CMD = "tcp_urg_flag_tracking"

    TCP_URGENT_PTR_CMD = "tcp_urgent_ptr"

    TCP_URGENT_PTR_COUNT_CMD = "tcp_urgent_ptr_count"

    TCP_URGENT_PTR_MODE_CMD = "tcp_urgent_ptr_mode"
    # Constant values for TCP_URGENT_PTR_MODE_CMD
    TCP_URGENT_PTR_MODE_INCR = "incr"
    TCP_URGENT_PTR_MODE_FIXED = "fixed"
    TCP_URGENT_PTR_MODE_LIST = "list"
    TCP_URGENT_PTR_MODE_DECR = "decr"

    TCP_URGENT_PTR_STEP_CMD = "tcp_urgent_ptr_step"

    TCP_URGENT_PTR_TRACKING_CMD = "tcp_urgent_ptr_tracking"

    TCP_WINDOW_CMD = "tcp_window"

    TCP_WINDOW_COUNT_CMD = "tcp_window_count"

    TCP_WINDOW_MODE_CMD = "tcp_window_mode"
    # Constant values for TCP_WINDOW_MODE_CMD
    TCP_WINDOW_MODE_INCR = "incr"
    TCP_WINDOW_MODE_FIXED = "fixed"
    TCP_WINDOW_MODE_LIST = "list"
    TCP_WINDOW_MODE_DECR = "decr"

    TCP_WINDOW_STEP_CMD = "tcp_window_step"

    TCP_WINDOW_TRACKING_CMD = "tcp_window_tracking"

    TEST_OBJECTIVE_VALUE_CMD = "test_objective_value"

    TIMESTAMP_INITIAL_VALUE_CMD = "timestamp_initial_value"

    TRACK_BY_CMD = "track_by"
    # Constant values for TRACK_BY_CMD
    TRACK_BY_I_TAG_ISID = "i_tag_isid"
    TRACK_BY_DEFAULT_PHB = "default_phb"
    TRACK_BY_CUSTOM_24BIT = "custom_24bit"
    TRACK_BY_ASSURED_FORWARDING_PHB = "assured_forwarding_phb"
    TRACK_BY_IPV6_DEST_IP = "ipv6_dest_ip"
    TRACK_BY_C_SRC_MAC = "c_src_mac"
    TRACK_BY_CLASS_SELECTOR_PHB = "class_selector_phb"
    TRACK_BY_IPV6_TRAFFICCLASS = "ipv6_trafficclass"
    TRACK_BY_B_SRC_MAC = "b_src_mac"
    TRACK_BY_C_VLAN = "c_vlan"
    TRACK_BY_MPLS_FLOW_DESCRIPTOR = "mpls_flow_descriptor"
    TRACK_BY_INNER_VLAN = "inner_vlan"
    TRACK_BY_TOS = "tos"
    TRACK_BY_MPLS_MPLS_EXP = "mpls_mpls_exp"
    TRACK_BY_DEST_MAC = "dest_mac"
    TRACK_BY_EXPEDITED_FORWARDING_PHB = "expedited_forwarding_phb"
    TRACK_BY_SRC_MAC = "src_mac"
    TRACK_BY_MPLS_LABEL = "mpls_label"
    TRACK_BY_S_VLAN = "s_vlan"
    TRACK_BY_DLCI = "dlci"
    TRACK_BY_CUSTOM_16BIT = "custom_16bit"
    TRACK_BY_B_VLAN = "b_vlan"
    TRACK_BY_B_DEST_MAC = "b_dest_mac"
    TRACK_BY_NONE = "none"
    TRACK_BY_ENDPOINT_PAIR = "endpoint_pair"
    TRACK_BY_C_DEST_MAC = "c_dest_mac"
    TRACK_BY_IPV6_FLOW_LABEL = "ipv6_flow_label"
    TRACK_BY_CUSTOM_8BIT = "custom_8bit"
    TRACK_BY_SOURCE_IP = "source_ip"
    TRACK_BY_RAW_PRIORITY = "raw_priority"
    TRACK_BY_IPV6_SOURCE_IP = "ipv6_source_ip"
    TRACK_BY_CUSTOM_32BIT = "custom_32bit"
    TRACK_BY_DEST_IP = "dest_ip"

    TRAFFIC_GENERATE_CMD = "traffic_generate"

    TRAFFIC_GENERATOR_CMD = "traffic_generator"
    # Constant values for TRAFFIC_GENERATOR_CMD
    TRAFFIC_GENERATOR_IXNETWORK = "ixnetwork"
    TRAFFIC_GENERATOR_IXOS = "ixos"
    TRAFFIC_GENERATOR_IXNETWORK_540 = "ixnetwork_540"

    TRANSMIT_DISTRIBUTION_CMD = "transmit_distribution"
    # Constant values for TRANSMIT_DISTRIBUTION_CMD
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_LS_RJT_FCF_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_OX_ID = "fip_npiv_fdisc_ls_rjt_fcf_fip_npiv_fdisc_descriptor_fibre_channel_ox_id"
    TRANSMIT_DISTRIBUTION_IPV4_DEST_IP = "ipv4_dest_ip"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_LS_RJT_FCF_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_CS_CTL_PRIORITY = "fip_npiv_fdisc_ls_rjt_fcf_fip_npiv_fdisc_descriptor_fibre_channel_cs_ctl_priority"
    TRANSMIT_DISTRIBUTION_IPV6_DEST_IP = "ipv6_dest_ip"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_LS_RJT_FCF_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_DID = "fip_npiv_fdisc_ls_rjt_fcf_fip_npiv_fdisc_descriptor_fibre_channel_did"
    TRANSMIT_DISTRIBUTION_DEFAULT_PHB = "default_phb"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_REQUEST_ENODE_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_DID = "fip_flogi_request_enode_fip_flogi_descriptor_fibre_channel_did"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_LS_ACC_FCF_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_DID = "fip_npiv_fdisc_ls_acc_fcf_fip_npiv_fdisc_descriptor_fibre_channel_did"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_LS_ACC_FCF_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_OX_ID = "fip_npiv_fdisc_ls_acc_fcf_fip_npiv_fdisc_descriptor_fibre_channel_ox_id"
    TRANSMIT_DISTRIBUTION_ETHERNET_II_ETHER_TYPE = "ethernet_ii_ether_type"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_REQUEST_ENODE_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_CS_CTL_PRIORITY = "fip_npiv_fdisc_request_enode_fip_npiv_fdisc_descriptor_fibre_channel_cs_ctl_priority"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_BSRC_ADDRESS = "mac_in_mac_v42_bsrc_address"
    TRANSMIT_DISTRIBUTION_FCOE_OX_ID = "fcoe_ox_id"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_CDEST_ADDRESS = "mac_in_mac_v42_cdest_address"
    TRANSMIT_DISTRIBUTION_ASSURED_FORWARDING_PHB = "assured_forwarding_phb"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_REQUEST_ENODE_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_SID = "fip_npiv_fdisc_request_enode_fip_npiv_fdisc_descriptor_fibre_channel_sid"
    TRANSMIT_DISTRIBUTION_I_TAG_ISID = "i_tag_isid"
    TRANSMIT_DISTRIBUTION_C_SRC_MAC = "c_src_mac"
    TRANSMIT_DISTRIBUTION_CLASS_SELECTOR_PHB = "class_selector_phb"
    TRANSMIT_DISTRIBUTION_IPV6_TRAFFICCLASS = "ipv6_trafficclass"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_LS_ACC_FCF_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_DID = "fip_flogi_ls_acc_fcf_fip_flogi_descriptor_fibre_channel_did"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_STAG_PCP = "mac_in_mac_v42_stag_pcp"
    TRANSMIT_DISTRIBUTION_B_SRC_MAC = "b_src_mac"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_STAG_VLAN_ID = "mac_in_mac_v42_stag_vlan_id"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_LS_RJT_FCF_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_CS_CTL_PRIORITY = "fip_flogi_ls_rjt_fcf_fip_flogi_descriptor_fibre_channel_cs_ctl_priority"
    TRANSMIT_DISTRIBUTION_B_DEST_MAC = "b_dest_mac"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_LS_ACC_FCF_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_SID = "fip_flogi_ls_acc_fcf_fip_flogi_descriptor_fibre_channel_sid"
    TRANSMIT_DISTRIBUTION_MPLS_FLOW_DESCRIPTOR = "mpls_flow_descriptor"
    TRANSMIT_DISTRIBUTION_INNER_VLAN = "inner_vlan"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_LS_RJT_FCF_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_SID = "fip_flogi_ls_rjt_fcf_fip_flogi_descriptor_fibre_channel_sid"
    TRANSMIT_DISTRIBUTION_TOS = "tos"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_VLAN_ID = "mac_in_mac_v42_vlan_id"
    TRANSMIT_DISTRIBUTION_ETHERNET_II_PFC_QUEUE = "ethernet_ii_pfc_queue"
    TRANSMIT_DISTRIBUTION_IPV6_FLOWLABEL = "ipv6_flowlabel"
    TRANSMIT_DISTRIBUTION_MPLS_MPLS_EXP = "mpls_mpls_exp"
    TRANSMIT_DISTRIBUTION_FCOE_CS_CTL = "fcoe_cs_ctl"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_REQUEST_ENODE_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_OX_ID = "fip_flogi_request_enode_fip_flogi_descriptor_fibre_channel_ox_id"
    TRANSMIT_DISTRIBUTION_DEST_MAC = "dest_mac"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_BDEST_ADDRESS = "mac_in_mac_v42_bdest_address"
    TRANSMIT_DISTRIBUTION_MPLS_LABEL = "mpls_label"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_LS_RJT_FCF_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_OX_ID = "fip_flogi_ls_rjt_fcf_fip_flogi_descriptor_fibre_channel_ox_id"
    TRANSMIT_DISTRIBUTION_SRC_MAC = "src_mac"
    TRANSMIT_DISTRIBUTION_EXPEDITED_FORWARDING_PHB = "expedited_forwarding_phb"
    TRANSMIT_DISTRIBUTION_RAW_PRIORITY = "raw_priority"
    TRANSMIT_DISTRIBUTION_DEST_IP = "dest_ip"
    TRANSMIT_DISTRIBUTION_UDP_UDP_DST_PRT = "udp_udp_dst_prt"
    TRANSMIT_DISTRIBUTION_S_VLAN = "s_vlan"
    TRANSMIT_DISTRIBUTION_PPPOE_SESSION_SESSIONID = "pppoe_session_sessionid"
    TRANSMIT_DISTRIBUTION_FCOE_SRC_ID = "fcoe_src_id"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_LS_ACC_FCF_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_SID = "fip_npiv_fdisc_ls_acc_fcf_fip_npiv_fdisc_descriptor_fibre_channel_sid"
    TRANSMIT_DISTRIBUTION_VLAN_VLAN_USER_PRIORITY = "vlan_vlan_user_priority"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_LS_RJT_FCF_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_SID = "fip_npiv_fdisc_ls_rjt_fcf_fip_npiv_fdisc_descriptor_fibre_channel_sid"
    TRANSMIT_DISTRIBUTION_FRAME_SIZE = "frame_size"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_LS_ACC_FCF_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_CS_CTL_PRIORITY = "fip_flogi_ls_acc_fcf_fip_flogi_descriptor_fibre_channel_cs_ctl_priority"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_PRIORITY = "mac_in_mac_v42_priority"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_BTAG_PCP = "mac_in_mac_v42_btag_pcp"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_LS_RJT_FCF_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_DID = "fip_flogi_ls_rjt_fcf_fip_flogi_descriptor_fibre_channel_did"
    TRANSMIT_DISTRIBUTION_ENDPOINT_PAIR = "endpoint_pair"
    TRANSMIT_DISTRIBUTION_FCOE_DEST_ID = "fcoe_dest_id"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_ISID = "mac_in_mac_v42_isid"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_LS_ACC_FCF_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_CS_CTL_PRIORITY = "fip_npiv_fdisc_ls_acc_fcf_fip_npiv_fdisc_descriptor_fibre_channel_cs_ctl_priority"
    TRANSMIT_DISTRIBUTION_B_VLAN = "b_vlan"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_REQUEST_ENODE_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_DID = "fip_npiv_fdisc_request_enode_fip_npiv_fdisc_descriptor_fibre_channel_did"
    TRANSMIT_DISTRIBUTION_C_VLAN = "c_vlan"
    TRANSMIT_DISTRIBUTION_FIP_NPIV_FDISC_REQUEST_ENODE_FIP_NPIV_FDISC_DESCRIPTOR_FIBRE_CHANNEL_OX_ID = "fip_npiv_fdisc_request_enode_fip_npiv_fdisc_descriptor_fibre_channel_ox_id"
    TRANSMIT_DISTRIBUTION_UDP_UDP_SRC_PRT = "udp_udp_src_prt"
    TRANSMIT_DISTRIBUTION_NONE = "none"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_PRIORITY = "mac_in_mac_priority"
    TRANSMIT_DISTRIBUTION_C_DEST_MAC = "c_dest_mac"
    TRANSMIT_DISTRIBUTION_IPV6_FLOW_LABEL = "ipv6_flow_label"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_REQUEST_ENODE_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_SID = "fip_flogi_request_enode_fip_flogi_descriptor_fibre_channel_sid"
    TRANSMIT_DISTRIBUTION_TCP_TCP_DST_PRT = "tcp_tcp_dst_prt"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_V42_CSRC_ADDRESS = "mac_in_mac_v42_csrc_address"
    TRANSMIT_DISTRIBUTION_IPV4_SOURCE_IP = "ipv4_source_ip"
    TRANSMIT_DISTRIBUTION_SOURCE_IP = "source_ip"
    TRANSMIT_DISTRIBUTION_RX_PORT = "rx_port"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_REQUEST_ENODE_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_CS_CTL_PRIORITY = "fip_flogi_request_enode_fip_flogi_descriptor_fibre_channel_cs_ctl_priority"
    TRANSMIT_DISTRIBUTION_FIP_FLOGI_LS_ACC_FCF_FIP_FLOGI_DESCRIPTOR_FIBRE_CHANNEL_OX_ID = "fip_flogi_ls_acc_fcf_fip_flogi_descriptor_fibre_channel_ox_id"
    TRANSMIT_DISTRIBUTION_TCP_TCP_SRC_PRT = "tcp_tcp_src_prt"
    TRANSMIT_DISTRIBUTION_IPV6_SOURCE_IP = "ipv6_source_ip"
    TRANSMIT_DISTRIBUTION_IPV4_PRECEDENCE = "ipv4_precedence"
    TRANSMIT_DISTRIBUTION_L2TPV2_DATA_MESSAGE_TUNNEL_ID = "l2tpv2_data_message_tunnel_id"
    TRANSMIT_DISTRIBUTION_MAC_IN_MAC_VLAN_USER_PRIORITY = "mac_in_mac_vlan_user_priority"

    TRANSMIT_MODE_CMD = "transmit_mode"
    # Constant values for TRANSMIT_MODE_CMD
    TRANSMIT_MODE_CONTINUOUS = "continuous"
    TRANSMIT_MODE_RANDOM_SPACED = "random_spaced"
    TRANSMIT_MODE_SINGLE_PKT = "single_pkt"
    TRANSMIT_MODE_SINGLE_BURST = "single_burst"
    TRANSMIT_MODE_MULTI_BURST = "multi_burst"
    TRANSMIT_MODE_CONTINUOUS_BURST = "continuous_burst"
    TRANSMIT_MODE_RETURN_TO_ID = "return_to_id"
    TRANSMIT_MODE_RETURN_TO_ID_FOR_COUNT = "return_to_id_for_count"
    TRANSMIT_MODE_ADVANCE = "advance"
    TRANSMIT_MODE_NEXT = "next"
    TRANSMIT_MODE_END = "end"

    TX_DELAY_CMD = "tx_delay"

    TX_DELAY_UNIT_CMD = "tx_delay_unit"
    # Constant values for TX_DELAY_UNIT_CMD
    TX_DELAY_UNIT_NS = "ns"
    TX_DELAY_UNIT_BYTES = "bytes"

    TX_MODE_CMD = "tx_mode"
    # Constant values for TX_MODE_CMD
    TX_MODE_STREAM = "stream"
    TX_MODE_ADVANCED = "advanced"

    UDF1_CASCADE_TYPE_CMD = "udf1_cascade_type"

    UDF1_CHAIN_FROM_CMD = "udf1_chain_from"
    # Constant values for UDF1_CHAIN_FROM_CMD
    UDF1_CHAIN_FROM_UDFNONE = "udfNone"
    UDF1_CHAIN_FROM_UDF1 = "udf1"
    UDF1_CHAIN_FROM_UDF3 = "udf3"
    UDF1_CHAIN_FROM_UDF2 = "udf2"
    UDF1_CHAIN_FROM_UDF5 = "udf5"
    UDF1_CHAIN_FROM_UDF4 = "udf4"

    UDF1_COUNTER_INIT_VALUE_CMD = "udf1_counter_init_value"

    UDF1_COUNTER_MODE_CMD = "udf1_counter_mode"

    UDF1_COUNTER_REPEAT_COUNT_CMD = "udf1_counter_repeat_count"

    UDF1_COUNTER_STEP_CMD = "udf1_counter_step"

    UDF1_COUNTER_TYPE_CMD = "udf1_counter_type"

    UDF1_COUNTER_UP_DOWN_CMD = "udf1_counter_up_down"

    UDF1_ENABLE_CASCADE_CMD = "udf1_enable_cascade"

    UDF1_INNER_REPEAT_COUNT_CMD = "udf1_inner_repeat_count"

    UDF1_INNER_REPEAT_VALUE_CMD = "udf1_inner_repeat_value"

    UDF1_INNER_STEP_CMD = "udf1_inner_step"

    UDF1_MASK_SELECT_CMD = "udf1_mask_select"

    UDF1_MASK_VAL_CMD = "udf1_mask_val"

    UDF1_MODE_CMD = "udf1_mode"
    # Constant values for UDF1_MODE_CMD
    UDF1_MODE_COUNTER = "counter"
    UDF1_MODE_RANGE_LIST = "range_list"
    UDF1_MODE_VALUE_LIST = "value_list"
    UDF1_MODE_RANDOM = "random"
    UDF1_MODE_NESTED = "nested"
    UDF1_MODE_IPV4 = "ipv4"

    UDF1_OFFSET_CMD = "udf1_offset"

    UDF1_SKIP_MASK_BITS_CMD = "udf1_skip_mask_bits"

    UDF1_SKIP_ZEROS_AND_ONES_CMD = "udf1_skip_zeros_and_ones"

    UDF1_VALUE_LIST_CMD = "udf1_value_list"

    UDF2_CASCADE_TYPE_CMD = "udf2_cascade_type"

    UDF2_CHAIN_FROM_CMD = "udf2_chain_from"
    # Constant values for UDF2_CHAIN_FROM_CMD
    UDF2_CHAIN_FROM_UDFNONE = "udfNone"
    UDF2_CHAIN_FROM_UDF1 = "udf1"
    UDF2_CHAIN_FROM_UDF3 = "udf3"
    UDF2_CHAIN_FROM_UDF2 = "udf2"
    UDF2_CHAIN_FROM_UDF5 = "udf5"
    UDF2_CHAIN_FROM_UDF4 = "udf4"

    UDF2_COUNTER_INIT_VALUE_CMD = "udf2_counter_init_value"

    UDF2_COUNTER_MODE_CMD = "udf2_counter_mode"

    UDF2_COUNTER_REPEAT_COUNT_CMD = "udf2_counter_repeat_count"

    UDF2_COUNTER_STEP_CMD = "udf2_counter_step"

    UDF2_COUNTER_TYPE_CMD = "udf2_counter_type"

    UDF2_COUNTER_UP_DOWN_CMD = "udf2_counter_up_down"

    UDF2_ENABLE_CASCADE_CMD = "udf2_enable_cascade"

    UDF2_INNER_REPEAT_COUNT_CMD = "udf2_inner_repeat_count"

    UDF2_INNER_REPEAT_VALUE_CMD = "udf2_inner_repeat_value"

    UDF2_INNER_STEP_CMD = "udf2_inner_step"

    UDF2_MASK_SELECT_CMD = "udf2_mask_select"

    UDF2_MASK_VAL_CMD = "udf2_mask_val"

    UDF2_MODE_CMD = "udf2_mode"

    UDF2_OFFSET_CMD = "udf2_offset"

    UDF2_SKIP_MASK_BITS_CMD = "udf2_skip_mask_bits"

    UDF2_SKIP_ZEROS_AND_ONES_CMD = "udf2_skip_zeros_and_ones"

    UDF2_VALUE_LIST_CMD = "udf2_value_list"

    UDF3_CASCADE_TYPE_CMD = "udf3_cascade_type"

    UDF3_CHAIN_FROM_CMD = "udf3_chain_from"
    # Constant values for UDF3_CHAIN_FROM_CMD
    UDF3_CHAIN_FROM_UDFNONE = "udfNone"
    UDF3_CHAIN_FROM_UDF1 = "udf1"
    UDF3_CHAIN_FROM_UDF3 = "udf3"
    UDF3_CHAIN_FROM_UDF2 = "udf2"
    UDF3_CHAIN_FROM_UDF5 = "udf5"
    UDF3_CHAIN_FROM_UDF4 = "udf4"

    UDF3_COUNTER_INIT_VALUE_CMD = "udf3_counter_init_value"

    UDF3_COUNTER_MODE_CMD = "udf3_counter_mode"

    UDF3_COUNTER_REPEAT_COUNT_CMD = "udf3_counter_repeat_count"

    UDF3_COUNTER_STEP_CMD = "udf3_counter_step"

    UDF3_COUNTER_TYPE_CMD = "udf3_counter_type"

    UDF3_COUNTER_UP_DOWN_CMD = "udf3_counter_up_down"

    UDF3_ENABLE_CASCADE_CMD = "udf3_enable_cascade"

    UDF3_INNER_REPEAT_COUNT_CMD = "udf3_inner_repeat_count"

    UDF3_INNER_REPEAT_VALUE_CMD = "udf3_inner_repeat_value"

    UDF3_INNER_STEP_CMD = "udf3_inner_step"

    UDF3_MASK_SELECT_CMD = "udf3_mask_select"

    UDF3_MASK_VAL_CMD = "udf3_mask_val"

    UDF3_MODE_CMD = "udf3_mode"

    UDF3_OFFSET_CMD = "udf3_offset"

    UDF3_SKIP_MASK_BITS_CMD = "udf3_skip_mask_bits"

    UDF3_SKIP_ZEROS_AND_ONES_CMD = "udf3_skip_zeros_and_ones"

    UDF3_VALUE_LIST_CMD = "udf3_value_list"

    UDF4_CASCADE_TYPE_CMD = "udf4_cascade_type"

    UDF4_CHAIN_FROM_CMD = "udf4_chain_from"
    # Constant values for UDF4_CHAIN_FROM_CMD
    UDF4_CHAIN_FROM_UDFNONE = "udfNone"
    UDF4_CHAIN_FROM_UDF1 = "udf1"
    UDF4_CHAIN_FROM_UDF3 = "udf3"
    UDF4_CHAIN_FROM_UDF2 = "udf2"
    UDF4_CHAIN_FROM_UDF5 = "udf5"
    UDF4_CHAIN_FROM_UDF4 = "udf4"

    UDF4_COUNTER_INIT_VALUE_CMD = "udf4_counter_init_value"

    UDF4_COUNTER_MODE_CMD = "udf4_counter_mode"

    UDF4_COUNTER_REPEAT_COUNT_CMD = "udf4_counter_repeat_count"

    UDF4_COUNTER_STEP_CMD = "udf4_counter_step"

    UDF4_COUNTER_TYPE_CMD = "udf4_counter_type"

    UDF4_COUNTER_UP_DOWN_CMD = "udf4_counter_up_down"

    UDF4_ENABLE_CASCADE_CMD = "udf4_enable_cascade"

    UDF4_INNER_REPEAT_COUNT_CMD = "udf4_inner_repeat_count"

    UDF4_INNER_REPEAT_VALUE_CMD = "udf4_inner_repeat_value"

    UDF4_INNER_STEP_CMD = "udf4_inner_step"

    UDF4_MASK_SELECT_CMD = "udf4_mask_select"

    UDF4_MASK_VAL_CMD = "udf4_mask_val"

    UDF4_MODE_CMD = "udf4_mode"

    UDF4_OFFSET_CMD = "udf4_offset"

    UDF4_SKIP_MASK_BITS_CMD = "udf4_skip_mask_bits"

    UDF4_SKIP_ZEROS_AND_ONES_CMD = "udf4_skip_zeros_and_ones"

    UDF4_VALUE_LIST_CMD = "udf4_value_list"

    UDF5_CASCADE_TYPE_CMD = "udf5_cascade_type"

    UDF5_CHAIN_FROM_CMD = "udf5_chain_from"
    # Constant values for UDF5_CHAIN_FROM_CMD
    UDF5_CHAIN_FROM_UDFNONE = "udfNone"
    UDF5_CHAIN_FROM_UDF1 = "udf1"
    UDF5_CHAIN_FROM_UDF3 = "udf3"
    UDF5_CHAIN_FROM_UDF2 = "udf2"
    UDF5_CHAIN_FROM_UDF5 = "udf5"
    UDF5_CHAIN_FROM_UDF4 = "udf4"

    UDF5_COUNTER_INIT_VALUE_CMD = "udf5_counter_init_value"

    UDF5_COUNTER_MODE_CMD = "udf5_counter_mode"

    UDF5_COUNTER_REPEAT_COUNT_CMD = "udf5_counter_repeat_count"

    UDF5_COUNTER_STEP_CMD = "udf5_counter_step"

    UDF5_COUNTER_TYPE_CMD = "udf5_counter_type"

    UDF5_COUNTER_UP_DOWN_CMD = "udf5_counter_up_down"

    UDF5_ENABLE_CASCADE_CMD = "udf5_enable_cascade"

    UDF5_INNER_REPEAT_COUNT_CMD = "udf5_inner_repeat_count"

    UDF5_INNER_REPEAT_VALUE_CMD = "udf5_inner_repeat_value"

    UDF5_INNER_STEP_CMD = "udf5_inner_step"

    UDF5_MASK_SELECT_CMD = "udf5_mask_select"

    UDF5_MASK_VAL_CMD = "udf5_mask_val"

    UDF5_MODE_CMD = "udf5_mode"

    UDF5_OFFSET_CMD = "udf5_offset"

    UDF5_SKIP_MASK_BITS_CMD = "udf5_skip_mask_bits"

    UDF5_SKIP_ZEROS_AND_ONES_CMD = "udf5_skip_zeros_and_ones"

    UDF5_VALUE_LIST_CMD = "udf5_value_list"

    UDP_CHECKSUM_CMD = "udp_checksum"

    UDP_CHECKSUM_VALUE_CMD = "udp_checksum_value"

    UDP_CHECKSUM_VALUE_TRACKING_CMD = "udp_checksum_value_tracking"

    UDP_DST_PORT_CMD = "udp_dst_port"

    UDP_DST_PORT_COUNT_CMD = "udp_dst_port_count"

    UDP_DST_PORT_MODE_CMD = "udp_dst_port_mode"
    # Constant values for UDP_DST_PORT_MODE_CMD
    UDP_DST_PORT_MODE_INCR = "incr"
    UDP_DST_PORT_MODE_FIXED = "fixed"
    UDP_DST_PORT_MODE_LIST = "list"
    UDP_DST_PORT_MODE_DECR = "decr"

    UDP_DST_PORT_STEP_CMD = "udp_dst_port_step"

    UDP_DST_PORT_TRACKING_CMD = "udp_dst_port_tracking"

    UDP_LENGTH_CMD = "udp_length"

    UDP_LENGTH_COUNT_CMD = "udp_length_count"

    UDP_LENGTH_MODE_CMD = "udp_length_mode"
    # Constant values for UDP_LENGTH_MODE_CMD
    UDP_LENGTH_MODE_INCR = "incr"
    UDP_LENGTH_MODE_FIXED = "fixed"
    UDP_LENGTH_MODE_LIST = "list"
    UDP_LENGTH_MODE_DECR = "decr"

    UDP_LENGTH_STEP_CMD = "udp_length_step"

    UDP_LENGTH_TRACKING_CMD = "udp_length_tracking"

    UDP_SRC_PORT_CMD = "udp_src_port"

    UDP_SRC_PORT_COUNT_CMD = "udp_src_port_count"

    UDP_SRC_PORT_MODE_CMD = "udp_src_port_mode"
    # Constant values for UDP_SRC_PORT_MODE_CMD
    UDP_SRC_PORT_MODE_INCR = "incr"
    UDP_SRC_PORT_MODE_FIXED = "fixed"
    UDP_SRC_PORT_MODE_LIST = "list"
    UDP_SRC_PORT_MODE_DECR = "decr"

    UDP_SRC_PORT_STEP_CMD = "udp_src_port_step"

    UDP_SRC_PORT_TRACKING_CMD = "udp_src_port_tracking"

    USE_ALL_IP_SUBNETS_CMD = "use_all_ip_subnets"

    USE_CP_RATE_CMD = "use_cp_rate"

    USE_CP_SIZE_CMD = "use_cp_size"

    VCI_CMD = "vci"

    VCI_COUNT_CMD = "vci_count"

    VCI_INCREMENT_CMD = "vci_increment"

    VCI_INCREMENT_STEP_CMD = "vci_increment_step"

    VCI_STEP_CMD = "vci_step"

    VLAN_CMD = "vlan"
    # Constant values for VLAN_CMD
    VLAN_ENABLE = "enable"
    VLAN_DISABLE = "disable"

    VLAN_CFI_CMD = "vlan_cfi"

    VLAN_CFI_COUNT_CMD = "vlan_cfi_count"

    VLAN_CFI_MODE_CMD = "vlan_cfi_mode"
    # Constant values for VLAN_CFI_MODE_CMD
    VLAN_CFI_MODE_INCR = "incr"
    VLAN_CFI_MODE_FIXED = "fixed"
    VLAN_CFI_MODE_DECR = "decr"

    VLAN_CFI_STEP_CMD = "vlan_cfi_step"

    VLAN_CFI_TRACKING_CMD = "vlan_cfi_tracking"

    VLAN_ENABLE_CMD = "vlan_enable"

    VLAN_ID_CMD = "vlan_id"

    VLAN_ID_COUNT_CMD = "vlan_id_count"

    VLAN_ID_MODE_CMD = "vlan_id_mode"
    # Constant values for VLAN_ID_MODE_CMD
    VLAN_ID_MODE_FIXED = "fixed"
    VLAN_ID_MODE_INCREMENT = "increment"
    VLAN_ID_MODE_DECREMENT = "decrement"
    VLAN_ID_MODE_NESTED_INCR = "nested_incr"
    VLAN_ID_MODE_NESTED_DECR = "nested_decr"
    VLAN_ID_MODE_RANDOM = "random"
    VLAN_ID_MODE_LIST = "list"

    VLAN_ID_STEP_CMD = "vlan_id_step"

    VLAN_ID_TRACKING_CMD = "vlan_id_tracking"

    VLAN_PROTOCOL_TAG_ID_CMD = "vlan_protocol_tag_id"

    VLAN_PROTOCOL_TAG_ID_COUNT_CMD = "vlan_protocol_tag_id_count"

    VLAN_PROTOCOL_TAG_ID_MODE_CMD = "vlan_protocol_tag_id_mode"
    # Constant values for VLAN_PROTOCOL_TAG_ID_MODE_CMD
    VLAN_PROTOCOL_TAG_ID_MODE_INCR = "incr"
    VLAN_PROTOCOL_TAG_ID_MODE_FIXED = "fixed"
    VLAN_PROTOCOL_TAG_ID_MODE_LIST = "list"
    VLAN_PROTOCOL_TAG_ID_MODE_DECR = "decr"

    VLAN_PROTOCOL_TAG_ID_STEP_CMD = "vlan_protocol_tag_id_step"

    VLAN_PROTOCOL_TAG_ID_TRACKING_CMD = "vlan_protocol_tag_id_tracking"

    VLAN_USER_PRIORITY_CMD = "vlan_user_priority"

    VLAN_USER_PRIORITY_COUNT_CMD = "vlan_user_priority_count"

    VLAN_USER_PRIORITY_MODE_CMD = "vlan_user_priority_mode"
    # Constant values for VLAN_USER_PRIORITY_MODE_CMD
    VLAN_USER_PRIORITY_MODE_INCR = "incr"
    VLAN_USER_PRIORITY_MODE_FIXED = "fixed"
    VLAN_USER_PRIORITY_MODE_LIST = "list"
    VLAN_USER_PRIORITY_MODE_DECR = "decr"

    VLAN_USER_PRIORITY_STEP_CMD = "vlan_user_priority_step"

    VLAN_USER_PRIORITY_TRACKING_CMD = "vlan_user_priority_tracking"

    VPI_CMD = "vpi"

    VPI_COUNT_CMD = "vpi_count"

    VPI_INCREMENT_CMD = "vpi_increment"

    VPI_INCREMENT_STEP_CMD = "vpi_increment_step"

    VPI_STEP_CMD = "vpi_step"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -adjust_rate
    -allow_self_destined
    -app_profile_type
    -arp_dst_hw_addr
    -arp_dst_hw_count
    -arp_dst_hw_mode
    -arp_dst_hw_step
    -arp_dst_hw_tracking
    -arp_hw_address_length
    -arp_hw_address_length_count
    -arp_hw_address_length_mode
    -arp_hw_address_length_step
    -arp_hw_address_length_tracking
    -arp_hw_type
    -arp_hw_type_count
    -arp_hw_type_mode
    -arp_hw_type_step
    -arp_hw_type_tracking
    -arp_operation
    -arp_operation_mode
    -arp_operation_tracking
    -arp_protocol_addr_length
    -arp_protocol_addr_length_count
    -arp_protocol_addr_length_mode
    -arp_protocol_addr_length_step
    -arp_protocol_addr_length_tracking
    -arp_protocol_type
    -arp_protocol_type_count
    -arp_protocol_type_mode
    -arp_protocol_type_step
    -arp_protocol_type_tracking
    -arp_src_hw_addr
    -arp_src_hw_count
    -arp_src_hw_mode
    -arp_src_hw_step
    -arp_src_hw_tracking
    -atm_counter_vci_data_item_list
    -atm_counter_vci_mask_select
    -atm_counter_vci_mask_value
    -atm_counter_vci_mode
    -atm_counter_vci_type
    -atm_counter_vpi_data_item_list
    -atm_counter_vpi_mask_select
    -atm_counter_vpi_mask_value
    -atm_counter_vpi_mode
    -atm_counter_vpi_type
    -atm_header_aal5error
    -atm_header_cell_loss_priority
    -atm_header_cpcs_length
    -atm_header_enable_auto_vpi_vci
    -atm_header_enable_cl
    -atm_header_enable_cpcs_length
    -atm_header_encapsulation
    -atm_header_generic_flow_ctrl
    -atm_header_hec_errors
    -atm_range_count
    -becn
    -bidirectional
    -burst_loop_count
    -circuit_endpoint_type
    -circuit_type
    -command_response
    -convert_to_raw
    -csrc_list
    -custom_offset
    -custom_values
    -data_pattern
    -data_pattern_mode
    -data_tos
    -data_tos_count
    -data_tos_mode
    -data_tos_step
    -data_tos_tracking
    -destination_filter
    -dhcp_boot_filename
    -dhcp_boot_filename_tracking
    -dhcp_client_hw_addr
    -dhcp_client_hw_addr_count
    -dhcp_client_hw_addr_mode
    -dhcp_client_hw_addr_step
    -dhcp_client_hw_addr_tracking
    -dhcp_client_ip_addr
    -dhcp_client_ip_addr_count
    -dhcp_client_ip_addr_mode
    -dhcp_client_ip_addr_step
    -dhcp_client_ip_addr_tracking
    -dhcp_flags
    -dhcp_flags_mode
    -dhcp_flags_tracking
    -dhcp_hops
    -dhcp_hops_count
    -dhcp_hops_mode
    -dhcp_hops_step
    -dhcp_hops_tracking
    -dhcp_hw_len
    -dhcp_hw_len_count
    -dhcp_hw_len_mode
    -dhcp_hw_len_step
    -dhcp_hw_len_tracking
    -dhcp_hw_type
    -dhcp_hw_type_count
    -dhcp_hw_type_mode
    -dhcp_hw_type_step
    -dhcp_hw_type_tracking
    -dhcp_magic_cookie
    -dhcp_magic_cookie_count
    -dhcp_magic_cookie_mode
    -dhcp_magic_cookie_step
    -dhcp_magic_cookie_tracking
    -dhcp_operation_code
    -dhcp_operation_code_mode
    -dhcp_operation_code_tracking
    -dhcp_option
    -dhcp_option_data
    -dhcp_relay_agent_ip_addr
    -dhcp_relay_agent_ip_addr_count
    -dhcp_relay_agent_ip_addr_mode
    -dhcp_relay_agent_ip_addr_step
    -dhcp_relay_agent_ip_addr_tracking
    -dhcp_seconds
    -dhcp_seconds_count
    -dhcp_seconds_mode
    -dhcp_seconds_step
    -dhcp_seconds_tracking
    -dhcp_server_host_name
    -dhcp_server_host_name_tracking
    -dhcp_server_ip_addr
    -dhcp_server_ip_addr_count
    -dhcp_server_ip_addr_mode
    -dhcp_server_ip_addr_step
    -dhcp_server_ip_addr_tracking
    -dhcp_transaction_id
    -dhcp_transaction_id_count
    -dhcp_transaction_id_mode
    -dhcp_transaction_id_step
    -dhcp_transaction_id_tracking
    -dhcp_your_ip_addr
    -dhcp_your_ip_addr_count
    -dhcp_your_ip_addr_mode
    -dhcp_your_ip_addr_step
    -dhcp_your_ip_addr_tracking
    -discard_eligible
    -dlci_core_enable
    -dlci_core_value
    -dlci_count_mode
    -dlci_extended_address0
    -dlci_extended_address1
    -dlci_extended_address2
    -dlci_extended_address3
    -dlci_mask_select
    -dlci_mask_value
    -dlci_repeat_count
    -dlci_repeat_count_step
    -dlci_size
    -dlci_value
    -dlci_value_step
    -duration
    -dynamic_update_fields
    -egress_custom_field_offset
    -egress_custom_offset
    -egress_custom_width
    -egress_tracking
    -egress_tracking_encap
    -emulation_dst_handle
    -emulation_dst_vlan_protocol_tag_id
    -emulation_multicast_dst_handle
    -emulation_multicast_dst_handle_type
    -emulation_multicast_rcvr_handle
    -emulation_multicast_rcvr_host_index
    -emulation_multicast_rcvr_mcast_index
    -emulation_multicast_rcvr_port_index
    -emulation_override_ppp_ip_addr
    -emulation_scalable_dst_handle
    -emulation_scalable_dst_intf_count
    -emulation_scalable_dst_intf_start
    -emulation_scalable_dst_port_count
    -emulation_scalable_dst_port_start
    -emulation_scalable_src_handle
    -emulation_scalable_src_intf_count
    -emulation_scalable_src_intf_start
    -emulation_scalable_src_port_count
    -emulation_scalable_src_port_start
    -emulation_src_handle
    -emulation_src_vlan_protocol_tag_id
    -enable_auto_detect_instrumentation
    -enable_ce_to_pe_traffic
    -enable_data_integrity
    -enable_dynamic_mpls_labels
    -enable_override_value
    -enable_pgid
    -enable_test_objective
    -enable_time_stamp
    -enable_udf1
    -enable_udf2
    -enable_udf3
    -enable_udf4
    -enable_udf5
    -endpointset_count
    -enforce_min_gap
    -ethernet_type
    -ethernet_value
    -ethernet_value_count
    -ethernet_value_mode
    -ethernet_value_step
    -ethernet_value_tracking
    -fcs
    -fcs_type
    -fecn
    -field_activeFieldChoice
    -field_auto
    -field_countValue
    -field_fieldValue
    -field_fullMesh
    -field_handle
    -field_linked
    -field_linked_to
    -field_optionalEnabled
    -field_singleValue
    -field_startValue
    -field_stepValue
    -field_trackingEnabled
    -field_valueList
    -field_valueType
    -fr_range_count
    -frame_rate_distribution_port
    -frame_rate_distribution_stream
    -frame_sequencing
    -frame_sequencing_mode
    -frame_sequencing_offset
    -frame_size
    -frame_size_distribution
    -frame_size_gauss
    -frame_size_imix
    -frame_size_max
    -frame_size_min
    -frame_size_step
    -global_dest_mac_retry_count
    -global_dest_mac_retry_delay
    -global_display_mpls_current_label_value
    -global_enable_dest_mac_retry
    -global_enable_mac_change_on_fly
    -global_enable_min_frame_size
    -global_enable_staggered_transmit
    -global_enable_stream_ordering
    -global_frame_ordering
    -global_large_error_threshhold
    -global_max_traffic_generation_queries
    -global_mpls_label_learning_timeout
    -global_peak_loading_replication_count
    -global_refresh_learned_info_before_apply
    -global_stream_control
    -global_stream_control_iterations
    -global_use_tx_rx_sync
    -global_wait_time
    -gre_checksum
    -gre_checksum_count
    -gre_checksum_enable
    -gre_checksum_enable_mode
    -gre_checksum_enable_tracking
    -gre_checksum_mode
    -gre_checksum_step
    -gre_checksum_tracking
    -gre_key
    -gre_key_count
    -gre_key_enable
    -gre_key_enable_mode
    -gre_key_enable_tracking
    -gre_key_mode
    -gre_key_step
    -gre_key_tracking
    -gre_reserved0
    -gre_reserved0_count
    -gre_reserved0_mode
    -gre_reserved0_step
    -gre_reserved0_tracking
    -gre_reserved1
    -gre_reserved1_count
    -gre_reserved1_mode
    -gre_reserved1_step
    -gre_reserved1_tracking
    -gre_seq_enable
    -gre_seq_enable_mode
    -gre_seq_enable_tracking
    -gre_seq_number
    -gre_seq_number_count
    -gre_seq_number_mode
    -gre_seq_number_step
    -gre_seq_number_tracking
    -gre_valid_checksum_enable
    -gre_version
    -gre_version_count
    -gre_version_mode
    -gre_version_step
    -gre_version_tracking
    -header_handle
    -hosts_per_net
    -icmp_checksum
    -icmp_checksum_count
    -icmp_checksum_mode
    -icmp_checksum_step
    -icmp_checksum_tracking
    -icmp_code
    -icmp_code_count
    -icmp_code_mode
    -icmp_code_step
    -icmp_code_tracking
    -icmp_id
    -icmp_id_count
    -icmp_id_mode
    -icmp_id_step
    -icmp_id_tracking
    -icmp_max_response_delay_ms
    -icmp_max_response_delay_ms_count
    -icmp_max_response_delay_ms_mode
    -icmp_max_response_delay_ms_step
    -icmp_max_response_delay_ms_tracking
    -icmp_mc_query_v2_interval_code
    -icmp_mc_query_v2_interval_code_count
    -icmp_mc_query_v2_interval_code_mode
    -icmp_mc_query_v2_interval_code_step
    -icmp_mc_query_v2_interval_code_tracking
    -icmp_mc_query_v2_robustness_var
    -icmp_mc_query_v2_robustness_var_count
    -icmp_mc_query_v2_robustness_var_mode
    -icmp_mc_query_v2_robustness_var_step
    -icmp_mc_query_v2_robustness_var_tracking
    -icmp_mc_query_v2_s_flag
    -icmp_mc_query_v2_s_flag_mode
    -icmp_mc_query_v2_s_flag_tracking
    -icmp_mobile_pam_m_bit
    -icmp_mobile_pam_m_bit_mode
    -icmp_mobile_pam_m_bit_tracking
    -icmp_mobile_pam_o_bit
    -icmp_mobile_pam_o_bit_mode
    -icmp_mobile_pam_o_bit_tracking
    -icmp_multicast_address
    -icmp_multicast_address_count
    -icmp_multicast_address_mode
    -icmp_multicast_address_step
    -icmp_multicast_address_tracking
    -icmp_ndp_nam_o_flag
    -icmp_ndp_nam_o_flag_mode
    -icmp_ndp_nam_o_flag_tracking
    -icmp_ndp_nam_r_flag
    -icmp_ndp_nam_r_flag_mode
    -icmp_ndp_nam_r_flag_tracking
    -icmp_ndp_nam_s_flag
    -icmp_ndp_nam_s_flag_mode
    -icmp_ndp_nam_s_flag_tracking
    -icmp_ndp_ram_h_flag
    -icmp_ndp_ram_h_flag_mode
    -icmp_ndp_ram_h_flag_tracking
    -icmp_ndp_ram_hop_limit
    -icmp_ndp_ram_hop_limit_count
    -icmp_ndp_ram_hop_limit_mode
    -icmp_ndp_ram_hop_limit_step
    -icmp_ndp_ram_hop_limit_tracking
    -icmp_ndp_ram_m_flag
    -icmp_ndp_ram_m_flag_mode
    -icmp_ndp_ram_m_flag_tracking
    -icmp_ndp_ram_o_flag
    -icmp_ndp_ram_o_flag_mode
    -icmp_ndp_ram_o_flag_tracking
    -icmp_ndp_ram_reachable_time
    -icmp_ndp_ram_reachable_time_count
    -icmp_ndp_ram_reachable_time_mode
    -icmp_ndp_ram_reachable_time_step
    -icmp_ndp_ram_reachable_time_tracking
    -icmp_ndp_ram_retransmit_timer
    -icmp_ndp_ram_retransmit_timer_count
    -icmp_ndp_ram_retransmit_timer_mode
    -icmp_ndp_ram_retransmit_timer_step
    -icmp_ndp_ram_retransmit_timer_tracking
    -icmp_ndp_ram_router_lifetime
    -icmp_ndp_ram_router_lifetime_count
    -icmp_ndp_ram_router_lifetime_mode
    -icmp_ndp_ram_router_lifetime_step
    -icmp_ndp_ram_router_lifetime_tracking
    -icmp_ndp_rm_dest_addr
    -icmp_ndp_rm_dest_addr_count
    -icmp_ndp_rm_dest_addr_mode
    -icmp_ndp_rm_dest_addr_step
    -icmp_ndp_rm_dest_addr_tracking
    -icmp_param_problem_message_pointer
    -icmp_param_problem_message_pointer_count
    -icmp_param_problem_message_pointer_mode
    -icmp_param_problem_message_pointer_step
    -icmp_param_problem_message_pointer_tracking
    -icmp_pkt_too_big_mtu
    -icmp_pkt_too_big_mtu_count
    -icmp_pkt_too_big_mtu_mode
    -icmp_pkt_too_big_mtu_step
    -icmp_pkt_too_big_mtu_tracking
    -icmp_seq
    -icmp_seq_count
    -icmp_seq_mode
    -icmp_seq_step
    -icmp_seq_tracking
    -icmp_target_addr
    -icmp_target_addr_count
    -icmp_target_addr_mode
    -icmp_target_addr_step
    -icmp_target_addr_tracking
    -icmp_type
    -icmp_type_count
    -icmp_type_mode
    -icmp_type_step
    -icmp_type_tracking
    -icmp_unused
    -icmp_unused_count
    -icmp_unused_mode
    -icmp_unused_step
    -icmp_unused_tracking
    -igmp_aux_data_length
    -igmp_aux_data_length_count
    -igmp_aux_data_length_mode
    -igmp_aux_data_length_step
    -igmp_aux_data_length_tracking
    -igmp_checksum
    -igmp_checksum_count
    -igmp_checksum_mode
    -igmp_checksum_step
    -igmp_checksum_tracking
    -igmp_data_v3r
    -igmp_data_v3r_count
    -igmp_data_v3r_mode
    -igmp_data_v3r_step
    -igmp_data_v3r_tracking
    -igmp_group_addr
    -igmp_group_count
    -igmp_group_mode
    -igmp_group_step
    -igmp_group_tracking
    -igmp_length_v3r
    -igmp_length_v3r_count
    -igmp_length_v3r_mode
    -igmp_length_v3r_step
    -igmp_length_v3r_tracking
    -igmp_max_response_time
    -igmp_max_response_time_count
    -igmp_max_response_time_mode
    -igmp_max_response_time_step
    -igmp_max_response_time_tracking
    -igmp_msg_type
    -igmp_msg_type_tracking
    -igmp_multicast_src
    -igmp_multicast_src_count
    -igmp_multicast_src_mode
    -igmp_multicast_src_step
    -igmp_multicast_src_tracking
    -igmp_qqic
    -igmp_qqic_count
    -igmp_qqic_mode
    -igmp_qqic_step
    -igmp_qqic_tracking
    -igmp_qrv
    -igmp_qrv_count
    -igmp_qrv_mode
    -igmp_qrv_step
    -igmp_qrv_tracking
    -igmp_record_type
    -igmp_record_type_mode
    -igmp_record_type_tracking
    -igmp_reserved_v3q
    -igmp_reserved_v3q_count
    -igmp_reserved_v3q_mode
    -igmp_reserved_v3q_step
    -igmp_reserved_v3q_tracking
    -igmp_reserved_v3r1
    -igmp_reserved_v3r1_count
    -igmp_reserved_v3r1_mode
    -igmp_reserved_v3r1_step
    -igmp_reserved_v3r1_tracking
    -igmp_reserved_v3r2
    -igmp_reserved_v3r2_count
    -igmp_reserved_v3r2_mode
    -igmp_reserved_v3r2_step
    -igmp_reserved_v3r2_tracking
    -igmp_s_flag
    -igmp_s_flag_mode
    -igmp_s_flag_tracking
    -igmp_type
    -igmp_unused
    -igmp_unused_count
    -igmp_unused_mode
    -igmp_unused_step
    -igmp_unused_tracking
    -igmp_valid_checksum
    -igmp_version
    -indirect
    -inner_ip_dst_addr
    -inner_ip_dst_count
    -inner_ip_dst_mode
    -inner_ip_dst_step
    -inner_ip_dst_tracking
    -inner_ip_src_addr
    -inner_ip_src_count
    -inner_ip_src_mode
    -inner_ip_src_step
    -inner_ip_src_tracking
    -inner_ipv6_dst_addr
    -inner_ipv6_dst_count
    -inner_ipv6_dst_mask
    -inner_ipv6_dst_mode
    -inner_ipv6_dst_step
    -inner_ipv6_dst_tracking
    -inner_ipv6_flow_label
    -inner_ipv6_flow_label_count
    -inner_ipv6_flow_label_mode
    -inner_ipv6_flow_label_step
    -inner_ipv6_flow_label_tracking
    -inner_ipv6_frag_id
    -inner_ipv6_frag_id_count
    -inner_ipv6_frag_id_mode
    -inner_ipv6_frag_id_step
    -inner_ipv6_frag_id_tracking
    -inner_ipv6_frag_more_flag
    -inner_ipv6_frag_more_flag_mode
    -inner_ipv6_frag_more_flag_tracking
    -inner_ipv6_frag_offset
    -inner_ipv6_frag_offset_count
    -inner_ipv6_frag_offset_mode
    -inner_ipv6_frag_offset_step
    -inner_ipv6_frag_offset_tracking
    -inner_ipv6_hop_limit
    -inner_ipv6_hop_limit_count
    -inner_ipv6_hop_limit_mode
    -inner_ipv6_hop_limit_step
    -inner_ipv6_hop_limit_tracking
    -inner_ipv6_src_addr
    -inner_ipv6_src_count
    -inner_ipv6_src_mask
    -inner_ipv6_src_mode
    -inner_ipv6_src_step
    -inner_ipv6_src_tracking
    -inner_ipv6_traffic_class
    -inner_ipv6_traffic_class_count
    -inner_ipv6_traffic_class_mode
    -inner_ipv6_traffic_class_step
    -inner_ipv6_traffic_class_tracking
    -inner_protocol
    -inner_protocol_count
    -inner_protocol_mode
    -inner_protocol_step
    -inner_protocol_tracking
    -integrity_signature
    -integrity_signature_offset
    -inter_burst_gap
    -inter_frame_gap
    -inter_frame_gap_unit
    -inter_stream_gap
    -intf_handle
    -ip_bit_flags
    -ip_checksum
    -ip_checksum_count
    -ip_checksum_mode
    -ip_checksum_step
    -ip_checksum_tracking
    -ip_cost
    -ip_cost_mode
    -ip_cost_tracking
    -ip_cu
    -ip_cu_count
    -ip_cu_mode
    -ip_cu_step
    -ip_cu_tracking
    -ip_delay
    -ip_delay_mode
    -ip_delay_tracking
    -ip_dscp
    -ip_dscp_count
    -ip_dscp_mode
    -ip_dscp_step
    -ip_dscp_tracking
    -ip_dst_addr
    -ip_dst_count
    -ip_dst_count_step
    -ip_dst_increment
    -ip_dst_increment_step
    -ip_dst_mode
    -ip_dst_prefix_len
    -ip_dst_prefix_len_step
    -ip_dst_range_step
    -ip_dst_skip_broadcast
    -ip_dst_skip_multicast
    -ip_dst_step
    -ip_dst_tracking
    -ip_fragment
    -ip_fragment_last
    -ip_fragment_last_mode
    -ip_fragment_last_tracking
    -ip_fragment_mode
    -ip_fragment_offset
    -ip_fragment_offset_count
    -ip_fragment_offset_mode
    -ip_fragment_offset_step
    -ip_fragment_offset_tracking
    -ip_fragment_tracking
    -ip_hdr_length
    -ip_hdr_length_count
    -ip_hdr_length_mode
    -ip_hdr_length_step
    -ip_hdr_length_tracking
    -ip_id
    -ip_id_count
    -ip_id_mode
    -ip_id_step
    -ip_id_tracking
    -ip_length_override
    -ip_length_override_mode
    -ip_length_override_tracking
    -ip_mbz
    -ip_opt_loose_routing
    -ip_opt_security
    -ip_opt_strict_routing
    -ip_opt_timestamp
    -ip_precedence
    -ip_precedence_count
    -ip_precedence_mode
    -ip_precedence_step
    -ip_precedence_tracking
    -ip_protocol
    -ip_protocol_count
    -ip_protocol_mode
    -ip_protocol_step
    -ip_protocol_tracking
    -ip_range_count
    -ip_reliability
    -ip_reliability_mode
    -ip_reliability_tracking
    -ip_reserved
    -ip_reserved_mode
    -ip_reserved_tracking
    -ip_src_addr
    -ip_src_count
    -ip_src_mode
    -ip_src_skip_broadcast
    -ip_src_skip_multicast
    -ip_src_step
    -ip_src_tracking
    -ip_throughput
    -ip_throughput_mode
    -ip_throughput_tracking
    -ip_tos_count
    -ip_tos_field
    -ip_tos_step
    -ip_total_length
    -ip_total_length_count
    -ip_total_length_mode
    -ip_total_length_step
    -ip_total_length_tracking
    -ip_ttl
    -ip_ttl_count
    -ip_ttl_mode
    -ip_ttl_step
    -ip_ttl_tracking
    -ipv6_auth_md5sha1_string
    -ipv6_auth_md5sha1_string_count
    -ipv6_auth_md5sha1_string_mode
    -ipv6_auth_md5sha1_string_step
    -ipv6_auth_md5sha1_string_tracking
    -ipv6_auth_next_header
    -ipv6_auth_next_header_count
    -ipv6_auth_next_header_mode
    -ipv6_auth_next_header_step
    -ipv6_auth_next_header_tracking
    -ipv6_auth_padding
    -ipv6_auth_padding_count
    -ipv6_auth_padding_mode
    -ipv6_auth_padding_step
    -ipv6_auth_padding_tracking
    -ipv6_auth_payload_len
    -ipv6_auth_payload_len_count
    -ipv6_auth_payload_len_mode
    -ipv6_auth_payload_len_step
    -ipv6_auth_payload_len_tracking
    -ipv6_auth_reserved
    -ipv6_auth_reserved_count
    -ipv6_auth_reserved_mode
    -ipv6_auth_reserved_step
    -ipv6_auth_reserved_tracking
    -ipv6_auth_seq_num
    -ipv6_auth_seq_num_count
    -ipv6_auth_seq_num_mode
    -ipv6_auth_seq_num_step
    -ipv6_auth_seq_num_tracking
    -ipv6_auth_spi
    -ipv6_auth_spi_count
    -ipv6_auth_spi_mode
    -ipv6_auth_spi_step
    -ipv6_auth_spi_tracking
    -ipv6_auth_string
    -ipv6_auth_string_count
    -ipv6_auth_string_mode
    -ipv6_auth_string_step
    -ipv6_auth_string_tracking
    -ipv6_auth_type
    -ipv6_checksum
    -ipv6_dst_addr
    -ipv6_dst_count
    -ipv6_dst_mask
    -ipv6_dst_mode
    -ipv6_dst_step
    -ipv6_dst_tracking
    -ipv6_encap_seq_number
    -ipv6_encap_seq_number_count
    -ipv6_encap_seq_number_mode
    -ipv6_encap_seq_number_step
    -ipv6_encap_seq_number_tracking
    -ipv6_encap_spi
    -ipv6_encap_spi_count
    -ipv6_encap_spi_mode
    -ipv6_encap_spi_step
    -ipv6_encap_spi_tracking
    -ipv6_extension_header
    -ipv6_flow_label
    -ipv6_flow_label_count
    -ipv6_flow_label_mode
    -ipv6_flow_label_step
    -ipv6_flow_label_tracking
    -ipv6_flow_version
    -ipv6_flow_version_count
    -ipv6_flow_version_mode
    -ipv6_flow_version_step
    -ipv6_flow_version_tracking
    -ipv6_frag_id
    -ipv6_frag_id_count
    -ipv6_frag_id_mode
    -ipv6_frag_id_step
    -ipv6_frag_id_tracking
    -ipv6_frag_more_flag
    -ipv6_frag_more_flag_mode
    -ipv6_frag_more_flag_tracking
    -ipv6_frag_next_header
    -ipv6_frag_offset
    -ipv6_frag_offset_count
    -ipv6_frag_offset_mode
    -ipv6_frag_offset_step
    -ipv6_frag_offset_tracking
    -ipv6_frag_res_2bit
    -ipv6_frag_res_2bit_count
    -ipv6_frag_res_2bit_mode
    -ipv6_frag_res_2bit_step
    -ipv6_frag_res_2bit_tracking
    -ipv6_frag_res_8bit
    -ipv6_frag_res_8bit_count
    -ipv6_frag_res_8bit_mode
    -ipv6_frag_res_8bit_step
    -ipv6_frag_res_8bit_tracking
    -ipv6_hop_by_hop_options
    -ipv6_hop_limit
    -ipv6_hop_limit_count
    -ipv6_hop_limit_mode
    -ipv6_hop_limit_step
    -ipv6_hop_limit_tracking
    -ipv6_length
    -ipv6_next_header
    -ipv6_next_header_count
    -ipv6_next_header_mode
    -ipv6_next_header_step
    -ipv6_next_header_tracking
    -ipv6_pseudo_dst_addr
    -ipv6_pseudo_dst_addr_count
    -ipv6_pseudo_dst_addr_mode
    -ipv6_pseudo_dst_addr_step
    -ipv6_pseudo_dst_addr_tracking
    -ipv6_pseudo_src_addr
    -ipv6_pseudo_src_addr_count
    -ipv6_pseudo_src_addr_mode
    -ipv6_pseudo_src_addr_step
    -ipv6_pseudo_src_addr_tracking
    -ipv6_pseudo_uppper_layer_pkt_length
    -ipv6_pseudo_uppper_layer_pkt_length_count
    -ipv6_pseudo_uppper_layer_pkt_length_mode
    -ipv6_pseudo_uppper_layer_pkt_length_step
    -ipv6_pseudo_uppper_layer_pkt_length_tracking
    -ipv6_pseudo_zero_number
    -ipv6_pseudo_zero_number_count
    -ipv6_pseudo_zero_number_mode
    -ipv6_pseudo_zero_number_step
    -ipv6_pseudo_zero_number_tracking
    -ipv6_routing_node_list
    -ipv6_routing_res
    -ipv6_routing_res_count
    -ipv6_routing_res_mode
    -ipv6_routing_res_step
    -ipv6_routing_res_tracking
    -ipv6_routing_type
    -ipv6_routing_type_count
    -ipv6_routing_type_mode
    -ipv6_routing_type_step
    -ipv6_routing_type_tracking
    -ipv6_src_addr
    -ipv6_src_count
    -ipv6_src_mask
    -ipv6_src_mode
    -ipv6_src_step
    -ipv6_src_tracking
    -ipv6_traffic_class
    -ipv6_traffic_class_count
    -ipv6_traffic_class_mode
    -ipv6_traffic_class_step
    -ipv6_traffic_class_tracking
    -isl
    -isl_bpdu
    -isl_bpdu_count
    -isl_bpdu_mode
    -isl_bpdu_step
    -isl_bpdu_tracking
    -isl_frame_type
    -isl_frame_type_mode
    -isl_frame_type_tracking
    -isl_index
    -isl_index_count
    -isl_index_mode
    -isl_index_step
    -isl_index_tracking
    -isl_mac_dst
    -isl_mac_dst_count
    -isl_mac_dst_mode
    -isl_mac_dst_step
    -isl_mac_dst_tracking
    -isl_mac_src_high
    -isl_mac_src_high_count
    -isl_mac_src_high_mode
    -isl_mac_src_high_step
    -isl_mac_src_high_tracking
    -isl_mac_src_low
    -isl_mac_src_low_count
    -isl_mac_src_low_mode
    -isl_mac_src_low_step
    -isl_mac_src_low_tracking
    -isl_user_priority
    -isl_user_priority_count
    -isl_user_priority_mode
    -isl_user_priority_step
    -isl_user_priority_tracking
    -isl_vlan_id
    -isl_vlan_id_count
    -isl_vlan_id_mode
    -isl_vlan_id_step
    -isl_vlan_id_tracking
    -l2_encap
    -l3_gaus1_avg
    -l3_gaus1_halfbw
    -l3_gaus1_weight
    -l3_gaus2_avg
    -l3_gaus2_halfbw
    -l3_gaus2_weight
    -l3_gaus3_avg
    -l3_gaus3_halfbw
    -l3_gaus3_weight
    -l3_gaus4_avg
    -l3_gaus4_halfbw
    -l3_gaus4_weight
    -l3_imix1_ratio
    -l3_imix1_size
    -l3_imix2_ratio
    -l3_imix2_size
    -l3_imix3_ratio
    -l3_imix3_size
    -l3_imix4_ratio
    -l3_imix4_size
    -l3_length
    -l3_length_max
    -l3_length_min
    -l3_length_step
    -l3_protocol
    -l4_protocol
    -lan_range_count
    -latency_bins
    -latency_bins_enable
    -latency_values
    -length_mode
    -loop_count
    -mac_discovery_gw
    -mac_dst
    -mac_dst2
    -mac_dst2_count
    -mac_dst2_mode
    -mac_dst2_step
    -mac_dst_count
    -mac_dst_count_step
    -mac_dst_mask
    -mac_dst_mode
    -mac_dst_seed
    -mac_dst_step
    -mac_dst_tracking
    -mac_src
    -mac_src2
    -mac_src2_count
    -mac_src2_mode
    -mac_src2_step
    -mac_src_count
    -mac_src_mask
    -mac_src_mode
    -mac_src_seed
    -mac_src_step
    -mac_src_tracking
    -merge_destinations
    -min_gap_bytes
    -mode
    -mpls
    -mpls_bottom_stack_bit
    -mpls_bottom_stack_bit_count
    -mpls_bottom_stack_bit_mode
    -mpls_bottom_stack_bit_step
    -mpls_bottom_stack_bit_tracking
    -mpls_exp_bit
    -mpls_exp_bit_count
    -mpls_exp_bit_mode
    -mpls_exp_bit_step
    -mpls_exp_bit_tracking
    -mpls_labels
    -mpls_labels_count
    -mpls_labels_mode
    -mpls_labels_step
    -mpls_labels_tracking
    -mpls_ttl
    -mpls_ttl_count
    -mpls_ttl_mode
    -mpls_ttl_step
    -mpls_ttl_tracking
    -mpls_type
    -multiple_queues
    -name
    -no_write
    -num_dst_ports
    -number_of_packets_per_stream
    -number_of_packets_tx
    -override_value_list
    -pause_control_time
    -pending_operations_timeout
    -pgid_offset
    -pgid_value
    -pkts_per_burst
    -port_handle
    -port_handle2
    -ppp_session_id
    -preamble_custom_size
    -preamble_size_mode
    -pt_handle
    -public_port_ip
    -pvc_count
    -pvc_count_step
    -qos_byte
    -qos_byte_count
    -qos_byte_mode
    -qos_byte_step
    -qos_byte_tracking
    -qos_ipv6_flow_label
    -qos_ipv6_traffic_class
    -qos_type_ixn
    -qos_value_ixn
    -qos_value_ixn_count
    -qos_value_ixn_mode
    -qos_value_ixn_step
    -qos_value_ixn_tracking
    -queue_id
    -ramp_up_percentage
    -range_per_spoke
    -rate_bps
    -rate_byteps
    -rate_frame_gap
    -rate_kbps
    -rate_kbyteps
    -rate_mbps
    -rate_mbyteps
    -rate_mode
    -rate_percent
    -rate_pps
    -return_to_id
    -rip_command
    -rip_command_mode
    -rip_command_tracking
    -rip_rte_addr_family_id
    -rip_rte_addr_family_id_count
    -rip_rte_addr_family_id_mode
    -rip_rte_addr_family_id_step
    -rip_rte_addr_family_id_tracking
    -rip_rte_ipv4_addr
    -rip_rte_ipv4_addr_count
    -rip_rte_ipv4_addr_mode
    -rip_rte_ipv4_addr_step
    -rip_rte_ipv4_addr_tracking
    -rip_rte_metric
    -rip_rte_metric_count
    -rip_rte_metric_mode
    -rip_rte_metric_step
    -rip_rte_metric_tracking
    -rip_rte_v1_unused2
    -rip_rte_v1_unused2_count
    -rip_rte_v1_unused2_mode
    -rip_rte_v1_unused2_step
    -rip_rte_v1_unused2_tracking
    -rip_rte_v1_unused3
    -rip_rte_v1_unused3_count
    -rip_rte_v1_unused3_mode
    -rip_rte_v1_unused3_step
    -rip_rte_v1_unused3_tracking
    -rip_rte_v1_unused4
    -rip_rte_v1_unused4_count
    -rip_rte_v1_unused4_mode
    -rip_rte_v1_unused4_step
    -rip_rte_v1_unused4_tracking
    -rip_rte_v2_next_hop
    -rip_rte_v2_next_hop_count
    -rip_rte_v2_next_hop_mode
    -rip_rte_v2_next_hop_step
    -rip_rte_v2_next_hop_tracking
    -rip_rte_v2_route_tag
    -rip_rte_v2_route_tag_count
    -rip_rte_v2_route_tag_mode
    -rip_rte_v2_route_tag_step
    -rip_rte_v2_route_tag_tracking
    -rip_rte_v2_subnet_mask
    -rip_rte_v2_subnet_mask_count
    -rip_rte_v2_subnet_mask_mode
    -rip_rte_v2_subnet_mask_step
    -rip_rte_v2_subnet_mask_tracking
    -rip_unused
    -rip_unused_count
    -rip_unused_mode
    -rip_unused_step
    -rip_unused_tracking
    -rip_version
    -route_mesh
    -rtp_csrc_count
    -rtp_payload_type
    -session_aware_traffic
    -signature
    -signature_offset
    -site_id
    -site_id_enable
    -site_id_step
    -skip_frame_size_validation
    -source_filter
    -src_dest_mesh
    -ssrc
    -stack_index
    -stream_id
    -stream_packing
    -table_udf_column_name
    -table_udf_column_offset
    -table_udf_column_size
    -table_udf_column_type
    -table_udf_rows
    -tag_filter
    -tcp_ack_flag
    -tcp_ack_flag_mode
    -tcp_ack_flag_tracking
    -tcp_ack_num
    -tcp_ack_num_count
    -tcp_ack_num_mode
    -tcp_ack_num_step
    -tcp_ack_num_tracking
    -tcp_checksum
    -tcp_checksum_count
    -tcp_checksum_mode
    -tcp_checksum_step
    -tcp_checksum_tracking
    -tcp_cwr_flag
    -tcp_cwr_flag_mode
    -tcp_cwr_flag_tracking
    -tcp_data_offset
    -tcp_data_offset_count
    -tcp_data_offset_mode
    -tcp_data_offset_step
    -tcp_data_offset_tracking
    -tcp_dst_port
    -tcp_dst_port_count
    -tcp_dst_port_mode
    -tcp_dst_port_step
    -tcp_dst_port_tracking
    -tcp_ecn_echo_flag
    -tcp_ecn_echo_flag_mode
    -tcp_ecn_echo_flag_tracking
    -tcp_fin_flag
    -tcp_fin_flag_mode
    -tcp_fin_flag_tracking
    -tcp_ns_flag
    -tcp_ns_flag_mode
    -tcp_ns_flag_tracking
    -tcp_psh_flag
    -tcp_psh_flag_mode
    -tcp_psh_flag_tracking
    -tcp_reserved
    -tcp_reserved_count
    -tcp_reserved_mode
    -tcp_reserved_step
    -tcp_reserved_tracking
    -tcp_rst_flag
    -tcp_rst_flag_mode
    -tcp_rst_flag_tracking
    -tcp_seq_num
    -tcp_seq_num_count
    -tcp_seq_num_mode
    -tcp_seq_num_step
    -tcp_seq_num_tracking
    -tcp_src_port
    -tcp_src_port_count
    -tcp_src_port_mode
    -tcp_src_port_step
    -tcp_src_port_tracking
    -tcp_syn_flag
    -tcp_syn_flag_mode
    -tcp_syn_flag_tracking
    -tcp_urg_flag
    -tcp_urg_flag_mode
    -tcp_urg_flag_tracking
    -tcp_urgent_ptr
    -tcp_urgent_ptr_count
    -tcp_urgent_ptr_mode
    -tcp_urgent_ptr_step
    -tcp_urgent_ptr_tracking
    -tcp_window
    -tcp_window_count
    -tcp_window_mode
    -tcp_window_step
    -tcp_window_tracking
    -test_objective_value
    -timestamp_initial_value
    -track_by
    -traffic_generate
    -traffic_generator
    -transmit_distribution
    -transmit_mode
    -tx_delay
    -tx_delay_unit
    -tx_mode
    -udf1_cascade_type
    -udf1_chain_from
    -udf1_counter_init_value
    -udf1_counter_mode
    -udf1_counter_repeat_count
    -udf1_counter_step
    -udf1_counter_type
    -udf1_counter_up_down
    -udf1_enable_cascade
    -udf1_inner_repeat_count
    -udf1_inner_repeat_value
    -udf1_inner_step
    -udf1_mask_select
    -udf1_mask_val
    -udf1_mode
    -udf1_offset
    -udf1_skip_mask_bits
    -udf1_skip_zeros_and_ones
    -udf1_value_list
    -udf2_cascade_type
    -udf2_chain_from
    -udf2_counter_init_value
    -udf2_counter_mode
    -udf2_counter_repeat_count
    -udf2_counter_step
    -udf2_counter_type
    -udf2_counter_up_down
    -udf2_enable_cascade
    -udf2_inner_repeat_count
    -udf2_inner_repeat_value
    -udf2_inner_step
    -udf2_mask_select
    -udf2_mask_val
    -udf2_mode
    -udf2_offset
    -udf2_skip_mask_bits
    -udf2_skip_zeros_and_ones
    -udf2_value_list
    -udf3_cascade_type
    -udf3_chain_from
    -udf3_counter_init_value
    -udf3_counter_mode
    -udf3_counter_repeat_count
    -udf3_counter_step
    -udf3_counter_type
    -udf3_counter_up_down
    -udf3_enable_cascade
    -udf3_inner_repeat_count
    -udf3_inner_repeat_value
    -udf3_inner_step
    -udf3_mask_select
    -udf3_mask_val
    -udf3_mode
    -udf3_offset
    -udf3_skip_mask_bits
    -udf3_skip_zeros_and_ones
    -udf3_value_list
    -udf4_cascade_type
    -udf4_chain_from
    -udf4_counter_init_value
    -udf4_counter_mode
    -udf4_counter_repeat_count
    -udf4_counter_step
    -udf4_counter_type
    -udf4_counter_up_down
    -udf4_enable_cascade
    -udf4_inner_repeat_count
    -udf4_inner_repeat_value
    -udf4_inner_step
    -udf4_mask_select
    -udf4_mask_val
    -udf4_mode
    -udf4_offset
    -udf4_skip_mask_bits
    -udf4_skip_zeros_and_ones
    -udf4_value_list
    -udf5_cascade_type
    -udf5_chain_from
    -udf5_counter_init_value
    -udf5_counter_mode
    -udf5_counter_repeat_count
    -udf5_counter_step
    -udf5_counter_type
    -udf5_counter_up_down
    -udf5_enable_cascade
    -udf5_inner_repeat_count
    -udf5_inner_repeat_value
    -udf5_inner_step
    -udf5_mask_select
    -udf5_mask_val
    -udf5_mode
    -udf5_offset
    -udf5_skip_mask_bits
    -udf5_skip_zeros_and_ones
    -udf5_value_list
    -udp_checksum
    -udp_checksum_value
    -udp_checksum_value_tracking
    -udp_dst_port
    -udp_dst_port_count
    -udp_dst_port_mode
    -udp_dst_port_step
    -udp_dst_port_tracking
    -udp_length
    -udp_length_count
    -udp_length_mode
    -udp_length_step
    -udp_length_tracking
    -udp_src_port
    -udp_src_port_count
    -udp_src_port_mode
    -udp_src_port_step
    -udp_src_port_tracking
    -use_all_ip_subnets
    -use_cp_rate
    -use_cp_size
    -vci
    -vci_count
    -vci_increment
    -vci_increment_step
    -vci_step
    -vlan
    -vlan_cfi
    -vlan_cfi_count
    -vlan_cfi_mode
    -vlan_cfi_step
    -vlan_cfi_tracking
    -vlan_enable
    -vlan_id
    -vlan_id_count
    -vlan_id_mode
    -vlan_id_step
    -vlan_id_tracking
    -vlan_protocol_tag_id
    -vlan_protocol_tag_id_count
    -vlan_protocol_tag_id_mode
    -vlan_protocol_tag_id_step
    -vlan_protocol_tag_id_tracking
    -vlan_user_priority
    -vlan_user_priority_count
    -vlan_user_priority_mode
    -vlan_user_priority_step
    -vlan_user_priority_tracking
    -vpi
    -vpi_count
    -vpi_increment
    -vpi_increment_step
    -vpi_step
If you want to update this file, look in the CSV
"""
