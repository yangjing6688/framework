from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: emulation_ospf_network_group_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class EmulationOspfNetworkGroupConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(EmulationOspfNetworkGroupConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_network_group_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ACTIVE_ROUTER_ID_CMD] = "dummyValue1" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ALLOW_PROPAGATE_CMD] = "dummyValue2" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.AUTO_SELECT_FORWARDING_ADDRESS_CMD] = "dummyValue3" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.CONNECTED_TO_HANDLE_CMD] = "dummyValue4" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.CUSTOM_FROM_NODE_INDEX_CMD] = "dummyValue5" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.CUSTOM_LINK_MULTIPLIER_CMD] = "dummyValue6" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.CUSTOM_TO_NODE_INDEX_CMD] = "dummyValue7" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ENABLE_ADVERTISE_AS_STUB_NETWORK_CMD] = "dummyValue8" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ENABLE_DEVICE_CMD] = "dummyValue9" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ENABLE_IP_CMD] = "dummyValue10" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_ACTIVE_CMD] = "dummyValue11" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_METRIC_CMD] = "dummyValue12" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_NETWORK_ADDRESS_CMD] = "dummyValue13" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_NETWORK_ADDRESS_STEP_CMD] = "dummyValue14" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_NUMBER_OF_ROUTES_CMD] = "dummyValue15" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_PREFIX_CMD] = "dummyValue16" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_ACTIVE_CMD] = "dummyValue17" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_METRIC_CMD] = "dummyValue18" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_NETWORK_ADDRESS_CMD] = "dummyValue19" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_NETWORK_ADDRESS_STEP_CMD] = "dummyValue20" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_NUMBER_OF_ROUTES_CMD] = "dummyValue21" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_PREFIX_CMD] = "dummyValue22" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_ACTIVE_CMD] = "dummyValue23" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_E_BIT_CMD] = "dummyValue24" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_EXTERNAL_ROUTE_TAG_CMD] = "dummyValue25" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_F_BIT_CMD] = "dummyValue26" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_FORWARDING_ADDRESS_CMD] = "dummyValue27" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_IPV6_NETWORK_ADDRESS_CMD] = "dummyValue28" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_IPV6_NETWORK_ADDRESS_STEP_CMD] = "dummyValue29" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_L_A_BIT_CMD] = "dummyValue30" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_NETWORK_GROUP_HANDLE_CMD] = "dummyValue31" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_ROUTER_DESTINATION_CMD] = "dummyValue32" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_ROUTER_SOURCE_CMD] = "dummyValue33" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_STATE_ID_CMD] = "dummyValue34" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_STATE_ID_PREFIX_CMD] = "dummyValue35" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_M_C_BIT_CMD] = "dummyValue36" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_METRIC_CMD] = "dummyValue37" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_N_U_BIT_CMD] = "dummyValue38" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_P_BIT_CMD] = "dummyValue39" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_PREFIX_CMD] = "dummyValue40" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_PREFIX_COUNT_CMD] = "dummyValue41" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_REFERENCE_LS_TYPE_CMD] = EmulationOspfNetworkGroupConfigConstants.EXTERNAL_REFERENCE_LS_TYPE_IGNORE # constant value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_REFERENCED_LINK_STATE_ID_CMD] = "dummyValue43" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_T_BIT_CMD] = "dummyValue44" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT4_CMD] = "dummyValue45" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT5_CMD] = "dummyValue46" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT6_CMD] = "dummyValue47" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT7_CMD] = "dummyValue48" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.FAT_TREE_LEVEL_COUNT_CMD] = "dummyValue49" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.FAT_TREE_LINK_MULTIPLIER_CMD] = "dummyValue50" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.FAT_TREE_NODE_COUNT_CMD] = "dummyValue51" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.FORWARDING_ADDRESS_CMD] = "dummyValue52" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.FORWARDING_ADDRESS_STEP_CMD] = "dummyValue53" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.FROM_IP_CMD] = "dummyValue54" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.FROM_IP_STEP_CMD] = "dummyValue55" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.FROM_IPV6_CMD] = "dummyValue56" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.FROM_IPV6_STEP_CMD] = "dummyValue57" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.GRID_COL_CMD] = "dummyValue58" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.GRID_INCLUDE_EMULATED_DEVICE_CMD] = "dummyValue59" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.GRID_LINK_MULTIPLIER_CMD] = "dummyValue60" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.GRID_ROW_CMD] = "dummyValue61" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.HANDLE_CMD] = "dummyValue62" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_ENABLE_LEVEL_2_CMD] = "dummyValue63" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_LINK_MULTIPLIER_CMD] = "dummyValue64" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_NUMBER_OF_FIRST_LEVEL_CMD] = "dummyValue65" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_NUMBER_OF_SECOND_LEVEL_CMD] = "dummyValue66" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_ACTIVE_CMD] = "dummyValue67" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_D_C_BIT_CMD] = "dummyValue68" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_DESTINATION_ROUTER_ID_CMD] = "dummyValue69" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_DESTINATION_ROUTER_ID_STEP_CMD] = "dummyValue70" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_E_BIT_CMD] = "dummyValue71" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_LINK_STATE_ID_CMD] = "dummyValue72" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_LINK_STATE_ID_STEP_CMD] = "dummyValue73" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_M_C_BIT_CMD] = "dummyValue74" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_METRIC_CMD] = "dummyValue75" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_N_BIT_CMD] = "dummyValue76" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_ACTIVE_CMD] = "dummyValue77" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_COUNT_CMD] = "dummyValue78" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_L_A_BIT_CMD] = "dummyValue79" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_LINK_STATE_ID_CMD] = "dummyValue80" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_LINK_STATE_ID_PREFIX_CMD] = "dummyValue81" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_M_C_BIT_CMD] = "dummyValue82" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_METRIC_CMD] = "dummyValue83" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_N_U_BIT_CMD] = "dummyValue84" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_NETWORK_ADDRESS_CMD] = "dummyValue85" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_P_BIT_CMD] = "dummyValue86" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_PREFIX_CMD] = "dummyValue87" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_PREFIX_COUNT_CMD] = "dummyValue88" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT4_CMD] = "dummyValue89" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT5_CMD] = "dummyValue90" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT6_CMD] = "dummyValue91" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT7_CMD] = "dummyValue92" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_R_BIT_CMD] = "dummyValue93" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_RESERVED_BIT6_CMD] = "dummyValue94" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_RESERVED_BIT7_CMD] = "dummyValue95" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTER_AREA_V6_BIT_CMD] = "dummyValue96" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_ACTIVE_CMD] = "dummyValue97" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_L_A_BIT_CMD] = "dummyValue98" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_LINK_STATE_ID_CMD] = "dummyValue99" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_LINK_STATE_ID_PREFIX_CMD] = "dummyValue100" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_M_C_BIT_CMD] = "dummyValue101" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_METRIC_CMD] = "dummyValue102" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_N_U_BIT_CMD] = "dummyValue103" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_NETWORK_ADDRESS_CMD] = "dummyValue104" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_NETWORK_ADDRESS_STEP_CMD] = "dummyValue105" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_P_BIT_CMD] = "dummyValue106" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_PREFIX_COUNT_CMD] = "dummyValue107" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCE_LS_TYPE_CMD] = EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCE_LS_TYPE_NETWORK # constant value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCED_LINK_STATE_ID_CMD] = "dummyValue109" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCED_ROUTER_ID_CMD] = "dummyValue110" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT4_CMD] = "dummyValue111" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT5_CMD] = "dummyValue112" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT6_CMD] = "dummyValue113" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT7_CMD] = "dummyValue114" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ACTIVE_CMD] = "dummyValue115" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ALLOW_PROPAGATE_CMD] = "dummyValue116" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_LENGTH_CMD] = "dummyValue117" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_METRIC_CMD] = "dummyValue118" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_NETWORK_ADDRESS_CMD] = "dummyValue119" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_NETWORK_ADDRESS_STEP_CMD] = "dummyValue120" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_NUMBER_OF_ADDRESSES_CMD] = "dummyValue121" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ROUTE_ORIGIN_CMD] = EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ROUTE_ORIGIN_ANOTHER_AREA # constant value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_ACTIVE_CMD] = "dummyValue123" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_LENGTH_CMD] = "dummyValue124" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_METRIC_CMD] = "dummyValue125" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_NETWORK_ADDRESS_CMD] = "dummyValue126" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_NETWORK_ADDRESS_STEP_CMD] = "dummyValue127" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_NUMBER_OF_ADDRESSES_CMD] = "dummyValue128" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_ROUTE_ORIGIN_CMD] = EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_ROUTE_ORIGIN_ANOTHERAREA # constant value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINEAR_LINK_MULTIPLIER_CMD] = "dummyValue130" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINEAR_NODES_CMD] = "dummyValue131" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_METRIC_CMD] = "dummyValue132" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_CMD] = "dummyValue133" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_ADMINISTRATOR_GROUP_CMD] = "dummyValue134" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_MAX_BW_CMD] = "dummyValue135" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_MAX_RESV_BW_CMD] = "dummyValue136" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_METRIC_CMD] = "dummyValue137" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY0_CMD] = "dummyValue138" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY1_CMD] = "dummyValue139" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY2_CMD] = "dummyValue140" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY3_CMD] = "dummyValue141" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY4_CMD] = "dummyValue142" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY5_CMD] = "dummyValue143" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY6_CMD] = "dummyValue144" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY7_CMD] = "dummyValue145" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_ACTIVE_CMD] = "dummyValue146" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_D_C_BIT_CMD] = "dummyValue147" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_E_BIT_CMD] = "dummyValue148" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_L_A_BIT_CMD] = "dummyValue149" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_LINK_LOCAL_ADDRESS_CMD] = "dummyValue150" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_LINK_STATE_ID_CMD] = "dummyValue151" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_LINK_STATE_ID_PREFIX_CMD] = "dummyValue152" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_M_C_BIT_CMD] = "dummyValue153" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_METRIC_CMD] = "dummyValue154" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_N_BIT_CMD] = "dummyValue155" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_N_U_BIT_CMD] = "dummyValue156" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_NETWORK_ADDRESS_CMD] = "dummyValue157" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_P_BIT_CMD] = "dummyValue158" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_PREFIX_CMD] = "dummyValue159" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_PREFIX_COUNT_CMD] = "dummyValue160" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_R_BIT_CMD] = "dummyValue161" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_RESERVED_BIT6_CMD] = "dummyValue162" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_RESERVED_BIT7_CMD] = "dummyValue163" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_ROUTER_PRIORITY_CMD] = "dummyValue164" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT4_CMD] = "dummyValue165" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT5_CMD] = "dummyValue166" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT6_CMD] = "dummyValue167" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT7_CMD] = "dummyValue168" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_V6_BIT_CMD] = "dummyValue169" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.LINKLSA_X_BIT_CMD] = "dummyValue170" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.MESH_INCLUDE_EMULATED_DEVICE_CMD] = "dummyValue171" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.MESH_LINK_MULTIPLIER_CMD] = "dummyValue172" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.MESH_NUMBER_OF_NODES_CMD] = "dummyValue173" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.MODE_CMD] = EmulationOspfNetworkGroupConfigConstants.MODE_CREATE # constant value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.MULTIPLIER_CMD] = "dummyValue175" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_ACTIVE_CMD] = "dummyValue176" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_INCLUDE_FORWARDING_ADDRESS_CMD] = "dummyValue177" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_LINK_STATE_ID_CMD] = "dummyValue178" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_LINK_STATE_ID_STEP_CMD] = "dummyValue179" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_METRIC_CMD] = "dummyValue180" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_NETWORK_ADDRESS_CMD] = "dummyValue181" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_NETWORK_ADDRESS_STEP_CMD] = "dummyValue182" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_NUMBER_OF_ROUTES_CMD] = "dummyValue183" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_PREFIX_CMD] = "dummyValue184" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.NSSA_PROPAGATE_CMD] = "dummyValue185" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.PREFIX_CMD] = "dummyValue186" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.PROTOCOL_NAME_CMD] = "dummyValue187" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.RETURN_DETAILED_HANDLES_CMD] = "dummyValue188" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.RING_INCLUDE_EMULATED_DEVICE_CMD] = "dummyValue189" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.RING_LINK_MULTIPLIER_CMD] = "dummyValue190" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.RING_NUMBER_OF_NODES_CMD] = "dummyValue191" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ROUTER_ABR_CMD] = "dummyValue192" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ROUTER_ACTIVE_CMD] = "dummyValue193" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ROUTER_ASBR_CMD] = "dummyValue194" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ROUTER_ID_CMD] = "dummyValue195" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ROUTER_ID_STEP_CMD] = "dummyValue196" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.ROUTER_SYSTEM_ID_CMD] = "dummyValue197" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.STUB_ACTIVE_CMD] = "dummyValue198" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.STUB_METRIC_CMD] = "dummyValue199" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.STUB_NETWORK_ADDRESS_CMD] = "dummyValue200" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.STUB_NETWORK_ADDRESS_STEP_CMD] = "dummyValue201" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.STUB_NUMBER_OF_ROUTES_CMD] = "dummyValue202" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.STUB_PREFIX_CMD] = "dummyValue203" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.SUBNET_PREFIX_LENGTH_CMD] = "dummyValue204" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.SUMMARY_ACTIVE_CMD] = "dummyValue205" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.SUMMARY_METRIC_CMD] = "dummyValue206" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.SUMMARY_NETWORK_ADDRESS_CMD] = "dummyValue207" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.SUMMARY_NETWORK_ADDRESS_STEP_CMD] = "dummyValue208" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.SUMMARY_NUMBER_OF_ROUTES_CMD] = "dummyValue209" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.SUMMARY_PREFIX_CMD] = "dummyValue210" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TO_IP_CMD] = "dummyValue211" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TO_IP_STEP_CMD] = "dummyValue212" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TO_IPV6_CMD] = "dummyValue213" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TO_IPV6_STEP_CMD] = "dummyValue214" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TREE_DEPTH_CMD] = "dummyValue215" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TREE_INCLUDE_EMULATED_DEVICE_CMD] = "dummyValue216" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TREE_LINK_MULTIPLIER_CMD] = "dummyValue217" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TREE_MAX_CHILDREN_PER_NODE_CMD] = "dummyValue218" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TREE_NUMBER_OF_NODES_CMD] = "dummyValue219" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TREE_USE_TREE_DEPTH_CMD] = "dummyValue220" # static value
        dummyDict[EmulationOspfNetworkGroupConfigConstants.TYPE_CMD] = EmulationOspfNetworkGroupConfigConstants.TYPE_CUSTOM # constant value

        api = device.getApi(EmulationOspfNetworkGroupConfigConstants.EMULATION_OSPF_NETWORK_GROUP_CONFIG_API)
        assert isinstance(api, EmulationOspfNetworkGroupConfigApi)
        api.emulation_ospf_network_group_config(dummyDict)
    """
    def emulation_ospf_network_group_config(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::emulation_ospf_network_group_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_network_group_config_active_router_id(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_allow_propagate(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_auto_select_forwarding_address(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_connected_to_handle(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_custom_from_node_index(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_custom_link_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_custom_to_node_index(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_enable_advertise_as_stub_network(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_enable_device(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_enable_ip(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external1_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external1_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external1_network_address(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external1_network_address_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external1_number_of_routes(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external1_prefix(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external2_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external2_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external2_network_address(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external2_network_address_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external2_number_of_routes(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external2_prefix(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_e_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_external_route_tag(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_f_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_forwarding_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_ipv6_network_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_ipv6_network_address_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_l_a_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_link_network_group_handle(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_link_router_destination(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_link_router_source(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_link_state_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_link_state_id_prefix(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_m_c_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_n_u_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_p_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_prefix(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_prefix_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_reference_ls_type(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_referenced_link_state_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_t_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_unused_bit4(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_unused_bit5(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_unused_bit6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_external_unused_bit7(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_fat_tree_level_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_fat_tree_link_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_fat_tree_node_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_forwarding_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_forwarding_address_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_from_ip(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_from_ip_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_from_ipv6(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_from_ipv6_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_grid_col(self, range):
        """
        This is the method the command: emulation_ospf_network_group_config option grid_col
        Description:Defines number of columns in a grid. This option is valid only when
            -type is grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT

            2
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_COL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.GRID_COL_CMD : range})

    def emulation_ospf_network_group_config_grid_include_emulated_device(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_grid_link_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_grid_row(self, range):
        """
        This is the method the command: emulation_ospf_network_group_config option grid_row
        Description:Defines number of rows in a grid. This option is valid only when -type
            is grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT

            2
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_ROW_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.GRID_ROW_CMD : range})

    def emulation_ospf_network_group_config_handle(self, any):
        """
        This is the method the command: emulation_ospf_network_group_config option handle
        Description:This option represents the handle the user *must* pass to the
            'emulation_ospf_network_group_config' procedure. This option specifies
            on which OSPF router to configure the OSPF route range. The OSPF router
            handle(s) are returned by the procedure 'emulation_ospf_config' when
            configuring OSPF routers on the Ixia interface.
            DEFAULT
                None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork-NGPF[M]
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.HANDLE_CMD : any})

    def emulation_ospf_network_group_config_hub_spoke_enable_level_2(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_hub_spoke_link_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_hub_spoke_number_of_first_level(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_hub_spoke_number_of_second_level(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_d_c_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_destination_router_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_destination_router_id_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_e_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_link_state_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_link_state_id_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_m_c_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_n_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_l_a_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_link_state_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_link_state_id_prefix(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_m_c_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_n_u_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_network_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_p_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_prefix(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_prefix_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_unused_bit4(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_unused_bit5(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_unused_bit6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_prefix_unused_bit7(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_r_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_reserved_bit6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_reserved_bit7(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_inter_area_v6_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_l_a_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_link_state_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_link_state_id_prefix(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_m_c_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_n_u_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_network_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_network_address_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_p_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_prefix_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_reference_ls_type(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_referenced_link_state_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_referenced_router_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_unused_bit4(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_unused_bit5(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_unused_bit6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_intra_area_unused_bit7(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv4_prefix_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv4_prefix_allow_propagate(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv4_prefix_length(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv4_prefix_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv4_prefix_network_address(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv4_prefix_network_address_step(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv4_prefix_number_of_addresses(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv4_prefix_route_origin(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv6_prefix_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv6_prefix_length(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv6_prefix_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv6_prefix_network_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv6_prefix_network_address_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv6_prefix_number_of_addresses(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ipv6_prefix_route_origin(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linear_link_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linear_nodes(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_link_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_link_te(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te
        Description:This parameter enables Traffic Engineering on the link to the virtual
            ospf network Range topology. This field is applicable only when the
            -type is grid. This option is available with IxTclNetwork.
            DEFAULT
                None
        Constants Available: LINK_TE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_CMD : bool_opt})

    def emulation_ospf_network_group_config_link_te_administrator_group(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_link_te_max_bw(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_max_bw
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_MAX_BW_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_MAX_BW_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_max_resv_bw(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_max_resv_bw
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_MAX_RESV_BW_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_MAX_RESV_BW_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_metric(self, range):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_metric
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            10
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_METRIC_CMD : range})

    def emulation_ospf_network_group_config_link_te_unresv_bw_priority0(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_unresv_bw_priority0
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY0_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY0_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_unresv_bw_priority1(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_unresv_bw_priority1
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY1_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY1_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_unresv_bw_priority2(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_unresv_bw_priority2
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY2_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY2_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_unresv_bw_priority3(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_unresv_bw_priority3
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY3_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY3_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_unresv_bw_priority4(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_unresv_bw_priority4
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY4_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY4_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_unresv_bw_priority5(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_unresv_bw_priority5
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY5_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY5_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_unresv_bw_priority6(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_unresv_bw_priority6
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY6_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_unresv_bw_priority7(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_unresv_bw_priority7
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY7_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY7_CMD : numeric})

    def emulation_ospf_network_group_config_linklsa_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_d_c_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_e_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_l_a_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_link_local_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_link_state_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_link_state_id_prefix(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_m_c_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_n_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_n_u_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_network_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_p_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_prefix(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_prefix_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_r_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_reserved_bit6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_reserved_bit7(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_router_priority(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_unused_bit4(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_unused_bit5(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_unused_bit6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_unused_bit7(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_v6_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_linklsa_x_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_mesh_include_emulated_device(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_mesh_link_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_mesh_number_of_nodes(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_mode(self, opt):
        """
        This is the method the command: emulation_ospf_network_group_config option mode
        Description:Mode of the procedure call. Valid options are: create modify delete
            Valid options are:
            create

            modify

            delete

            DEFAULT

            create
        Constants Available: MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.MODE_CMD : opt})

    def emulation_ospf_network_group_config_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_include_forwarding_address(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_link_state_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_link_state_id_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_network_address(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_network_address_step(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_number_of_routes(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_prefix(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_nssa_propagate(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_prefix(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_protocol_name(self, alpha):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_return_detailed_handles(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ring_include_emulated_device(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ring_link_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_ring_number_of_nodes(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_router_abr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option router_abr
        Description:If true (1), set router to be an area boundary router (ABR). Correspond
            to E (external) bit in router LSA. This option is valid only when -type
            is router or grid, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: ROUTER_ABR_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ROUTER_ABR_CMD : bool_opt})

    def emulation_ospf_network_group_config_router_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_router_asbr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option router_asbr
        Description:If true (1), set router to be an AS boundary router (ASBR). Correspond
            to B (Border) bit in router LSA. This option is valid only when -type is
            router or grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: ROUTER_ASBR_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ROUTER_ASBR_CMD : bool_opt})

    def emulation_ospf_network_group_config_router_id(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_router_id_step(self, ip):
        """
        This is the method the command: emulation_ospf_network_group_config option router_id_step
        Description:The ID associated with the router.
            DEFAULT

            0.0.0.0
        Constants Available: ROUTER_ID_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ROUTER_ID_STEP_CMD : ip})

    def emulation_ospf_network_group_config_router_system_id(self, hex8withspaces):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_stub_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_stub_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_stub_network_address(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_stub_network_address_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_stub_number_of_routes(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_stub_prefix(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_subnet_prefix_length(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_summary_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_summary_metric(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_summary_network_address(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_summary_network_address_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_summary_number_of_routes(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_summary_prefix(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_to_ip(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_to_ip_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_to_ipv6(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_to_ipv6_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_tree_depth(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_tree_include_emulated_device(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_tree_link_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_tree_max_children_per_node(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_tree_number_of_nodes(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_tree_use_tree_depth(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_type(self, opt):
        """
        This is the method the command: emulation_ospf_network_group_config option type
        Description:The type of topology route to create.
            Valid options are:
            grid

            mesh

            custom

            ring

            hub-and-spoke

            tree

            ipv4-prefix

            fat-tree

            linear

            ipv6-prefix

            DEFAULT
                None
        Constants Available: TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TYPE_CMD : opt})


"""
    This is the Constants class for the command: emulation_ospf_network_group_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationOspfNetworkGroupConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    EMULATION_OSPF_NETWORK_GROUP_CONFIG_API = "EMULATION_OSPF_NETWORK_GROUP_CONFIG_API"

    ACTIVE_ROUTER_ID_CMD = "active_router_id"

    ALLOW_PROPAGATE_CMD = "allow_propagate"

    AUTO_SELECT_FORWARDING_ADDRESS_CMD = "auto_select_forwarding_address"

    CONNECTED_TO_HANDLE_CMD = "connected_to_handle"

    CUSTOM_FROM_NODE_INDEX_CMD = "custom_from_node_index"

    CUSTOM_LINK_MULTIPLIER_CMD = "custom_link_multiplier"

    CUSTOM_TO_NODE_INDEX_CMD = "custom_to_node_index"

    ENABLE_ADVERTISE_AS_STUB_NETWORK_CMD = "enable_advertise_as_stub_network"

    ENABLE_DEVICE_CMD = "enable_device"

    ENABLE_IP_CMD = "enable_ip"

    EXTERNAL1_ACTIVE_CMD = "external1_active"

    EXTERNAL1_METRIC_CMD = "external1_metric"

    EXTERNAL1_NETWORK_ADDRESS_CMD = "external1_network_address"

    EXTERNAL1_NETWORK_ADDRESS_STEP_CMD = "external1_network_address_step"

    EXTERNAL1_NUMBER_OF_ROUTES_CMD = "external1_number_of_routes"

    EXTERNAL1_PREFIX_CMD = "external1_prefix"

    EXTERNAL2_ACTIVE_CMD = "external2_active"

    EXTERNAL2_METRIC_CMD = "external2_metric"

    EXTERNAL2_NETWORK_ADDRESS_CMD = "external2_network_address"

    EXTERNAL2_NETWORK_ADDRESS_STEP_CMD = "external2_network_address_step"

    EXTERNAL2_NUMBER_OF_ROUTES_CMD = "external2_number_of_routes"

    EXTERNAL2_PREFIX_CMD = "external2_prefix"

    EXTERNAL_ACTIVE_CMD = "external_active"

    EXTERNAL_E_BIT_CMD = "external_e_bit"

    EXTERNAL_EXTERNAL_ROUTE_TAG_CMD = "external_external_route_tag"

    EXTERNAL_F_BIT_CMD = "external_f_bit"

    EXTERNAL_FORWARDING_ADDRESS_CMD = "external_forwarding_address"

    EXTERNAL_IPV6_NETWORK_ADDRESS_CMD = "external_ipv6_network_address"

    EXTERNAL_IPV6_NETWORK_ADDRESS_STEP_CMD = "external_ipv6_network_address_step"

    EXTERNAL_L_A_BIT_CMD = "external_l_a_bit"

    EXTERNAL_LINK_NETWORK_GROUP_HANDLE_CMD = "external_link_network_group_handle"

    EXTERNAL_LINK_ROUTER_DESTINATION_CMD = "external_link_router_destination"

    EXTERNAL_LINK_ROUTER_SOURCE_CMD = "external_link_router_source"

    EXTERNAL_LINK_STATE_ID_CMD = "external_link_state_id"

    EXTERNAL_LINK_STATE_ID_PREFIX_CMD = "external_link_state_id_prefix"

    EXTERNAL_M_C_BIT_CMD = "external_m_c_bit"

    EXTERNAL_METRIC_CMD = "external_metric"

    EXTERNAL_N_U_BIT_CMD = "external_n_u_bit"

    EXTERNAL_P_BIT_CMD = "external_p_bit"

    EXTERNAL_PREFIX_CMD = "external_prefix"

    EXTERNAL_PREFIX_COUNT_CMD = "external_prefix_count"

    EXTERNAL_REFERENCE_LS_TYPE_CMD = "external_reference_ls_type"
    # Constant values for EXTERNAL_REFERENCE_LS_TYPE_CMD
    EXTERNAL_REFERENCE_LS_TYPE_IGNORE = "ignore"
    EXTERNAL_REFERENCE_LS_TYPE_NETWORK = "network"
    EXTERNAL_REFERENCE_LS_TYPE_ROUTER = "router"

    EXTERNAL_REFERENCED_LINK_STATE_ID_CMD = "external_referenced_link_state_id"

    EXTERNAL_T_BIT_CMD = "external_t_bit"

    EXTERNAL_UNUSED_BIT4_CMD = "external_unused_bit4"

    EXTERNAL_UNUSED_BIT5_CMD = "external_unused_bit5"

    EXTERNAL_UNUSED_BIT6_CMD = "external_unused_bit6"

    EXTERNAL_UNUSED_BIT7_CMD = "external_unused_bit7"

    FAT_TREE_LEVEL_COUNT_CMD = "fat_tree_level_count"

    FAT_TREE_LINK_MULTIPLIER_CMD = "fat_tree_link_multiplier"

    FAT_TREE_NODE_COUNT_CMD = "fat_tree_node_count"

    FORWARDING_ADDRESS_CMD = "forwarding_address"

    FORWARDING_ADDRESS_STEP_CMD = "forwarding_address_step"

    FROM_IP_CMD = "from_ip"

    FROM_IP_STEP_CMD = "from_ip_step"

    FROM_IPV6_CMD = "from_ipv6"

    FROM_IPV6_STEP_CMD = "from_ipv6_step"

    GRID_COL_CMD = "grid_col"

    GRID_INCLUDE_EMULATED_DEVICE_CMD = "grid_include_emulated_device"

    GRID_LINK_MULTIPLIER_CMD = "grid_link_multiplier"

    GRID_ROW_CMD = "grid_row"

    HANDLE_CMD = "handle"

    HUB_SPOKE_ENABLE_LEVEL_2_CMD = "hub_spoke_enable_level_2"

    HUB_SPOKE_LINK_MULTIPLIER_CMD = "hub_spoke_link_multiplier"

    HUB_SPOKE_NUMBER_OF_FIRST_LEVEL_CMD = "hub_spoke_number_of_first_level"

    HUB_SPOKE_NUMBER_OF_SECOND_LEVEL_CMD = "hub_spoke_number_of_second_level"

    INTER_AREA_ACTIVE_CMD = "inter_area_active"

    INTER_AREA_D_C_BIT_CMD = "inter_area_d_c_bit"

    INTER_AREA_DESTINATION_ROUTER_ID_CMD = "inter_area_destination_router_id"

    INTER_AREA_DESTINATION_ROUTER_ID_STEP_CMD = "inter_area_destination_router_id_step"

    INTER_AREA_E_BIT_CMD = "inter_area_e_bit"

    INTER_AREA_LINK_STATE_ID_CMD = "inter_area_link_state_id"

    INTER_AREA_LINK_STATE_ID_STEP_CMD = "inter_area_link_state_id_step"

    INTER_AREA_M_C_BIT_CMD = "inter_area_m_c_bit"

    INTER_AREA_METRIC_CMD = "inter_area_metric"

    INTER_AREA_N_BIT_CMD = "inter_area_n_bit"

    INTER_AREA_PREFIX_ACTIVE_CMD = "inter_area_prefix_active"

    INTER_AREA_PREFIX_COUNT_CMD = "inter_area_prefix_count"

    INTER_AREA_PREFIX_L_A_BIT_CMD = "inter_area_prefix_l_a_bit"

    INTER_AREA_PREFIX_LINK_STATE_ID_CMD = "inter_area_prefix_link_state_id"

    INTER_AREA_PREFIX_LINK_STATE_ID_PREFIX_CMD = "inter_area_prefix_link_state_id_prefix"

    INTER_AREA_PREFIX_M_C_BIT_CMD = "inter_area_prefix_m_c_bit"

    INTER_AREA_PREFIX_METRIC_CMD = "inter_area_prefix_metric"

    INTER_AREA_PREFIX_N_U_BIT_CMD = "inter_area_prefix_n_u_bit"

    INTER_AREA_PREFIX_NETWORK_ADDRESS_CMD = "inter_area_prefix_network_address"

    INTER_AREA_PREFIX_P_BIT_CMD = "inter_area_prefix_p_bit"

    INTER_AREA_PREFIX_PREFIX_CMD = "inter_area_prefix_prefix"

    INTER_AREA_PREFIX_PREFIX_COUNT_CMD = "inter_area_prefix_prefix_count"

    INTER_AREA_PREFIX_UNUSED_BIT4_CMD = "inter_area_prefix_unused_bit4"

    INTER_AREA_PREFIX_UNUSED_BIT5_CMD = "inter_area_prefix_unused_bit5"

    INTER_AREA_PREFIX_UNUSED_BIT6_CMD = "inter_area_prefix_unused_bit6"

    INTER_AREA_PREFIX_UNUSED_BIT7_CMD = "inter_area_prefix_unused_bit7"

    INTER_AREA_R_BIT_CMD = "inter_area_r_bit"

    INTER_AREA_RESERVED_BIT6_CMD = "inter_area_reserved_bit6"

    INTER_AREA_RESERVED_BIT7_CMD = "inter_area_reserved_bit7"

    INTER_AREA_V6_BIT_CMD = "inter_area_v6_bit"

    INTRA_AREA_ACTIVE_CMD = "intra_area_active"

    INTRA_AREA_L_A_BIT_CMD = "intra_area_l_a_bit"

    INTRA_AREA_LINK_STATE_ID_CMD = "intra_area_link_state_id"

    INTRA_AREA_LINK_STATE_ID_PREFIX_CMD = "intra_area_link_state_id_prefix"

    INTRA_AREA_M_C_BIT_CMD = "intra_area_m_c_bit"

    INTRA_AREA_METRIC_CMD = "intra_area_metric"

    INTRA_AREA_N_U_BIT_CMD = "intra_area_n_u_bit"

    INTRA_AREA_NETWORK_ADDRESS_CMD = "intra_area_network_address"

    INTRA_AREA_NETWORK_ADDRESS_STEP_CMD = "intra_area_network_address_step"

    INTRA_AREA_P_BIT_CMD = "intra_area_p_bit"

    INTRA_AREA_PREFIX_COUNT_CMD = "intra_area_prefix_count"

    INTRA_AREA_REFERENCE_LS_TYPE_CMD = "intra_area_reference_ls_type"
    # Constant values for INTRA_AREA_REFERENCE_LS_TYPE_CMD
    INTRA_AREA_REFERENCE_LS_TYPE_NETWORK = "network"
    INTRA_AREA_REFERENCE_LS_TYPE_ROUTER = "router"

    INTRA_AREA_REFERENCED_LINK_STATE_ID_CMD = "intra_area_referenced_link_state_id"

    INTRA_AREA_REFERENCED_ROUTER_ID_CMD = "intra_area_referenced_router_id"

    INTRA_AREA_UNUSED_BIT4_CMD = "intra_area_unused_bit4"

    INTRA_AREA_UNUSED_BIT5_CMD = "intra_area_unused_bit5"

    INTRA_AREA_UNUSED_BIT6_CMD = "intra_area_unused_bit6"

    INTRA_AREA_UNUSED_BIT7_CMD = "intra_area_unused_bit7"

    IPV4_PREFIX_ACTIVE_CMD = "ipv4_prefix_active"

    IPV4_PREFIX_ALLOW_PROPAGATE_CMD = "ipv4_prefix_allow_propagate"

    IPV4_PREFIX_LENGTH_CMD = "ipv4_prefix_length"

    IPV4_PREFIX_METRIC_CMD = "ipv4_prefix_metric"

    IPV4_PREFIX_NETWORK_ADDRESS_CMD = "ipv4_prefix_network_address"

    IPV4_PREFIX_NETWORK_ADDRESS_STEP_CMD = "ipv4_prefix_network_address_step"

    IPV4_PREFIX_NUMBER_OF_ADDRESSES_CMD = "ipv4_prefix_number_of_addresses"

    IPV4_PREFIX_ROUTE_ORIGIN_CMD = "ipv4_prefix_route_origin"
    # Constant values for IPV4_PREFIX_ROUTE_ORIGIN_CMD
    IPV4_PREFIX_ROUTE_ORIGIN_ANOTHER_AREA = "another_area"
    IPV4_PREFIX_ROUTE_ORIGIN_EXTERNAL_TYPE_1 = "external_type_1"
    IPV4_PREFIX_ROUTE_ORIGIN_EXTERNAL_TYPE_2 = "external_type_2"
    IPV4_PREFIX_ROUTE_ORIGIN_NSSA = "nssa"
    IPV4_PREFIX_ROUTE_ORIGIN_SAME_AREA = "same_area"

    IPV6_PREFIX_ACTIVE_CMD = "ipv6_prefix_active"

    IPV6_PREFIX_LENGTH_CMD = "ipv6_prefix_length"

    IPV6_PREFIX_METRIC_CMD = "ipv6_prefix_metric"

    IPV6_PREFIX_NETWORK_ADDRESS_CMD = "ipv6_prefix_network_address"

    IPV6_PREFIX_NETWORK_ADDRESS_STEP_CMD = "ipv6_prefix_network_address_step"

    IPV6_PREFIX_NUMBER_OF_ADDRESSES_CMD = "ipv6_prefix_number_of_addresses"

    IPV6_PREFIX_ROUTE_ORIGIN_CMD = "ipv6_prefix_route_origin"
    # Constant values for IPV6_PREFIX_ROUTE_ORIGIN_CMD
    IPV6_PREFIX_ROUTE_ORIGIN_ANOTHERAREA = "anotherarea"
    IPV6_PREFIX_ROUTE_ORIGIN_EXTERNALTYPE1 = "externaltype1"
    IPV6_PREFIX_ROUTE_ORIGIN_EXTERNALTYPE2 = "externaltype2"
    IPV6_PREFIX_ROUTE_ORIGIN_NSSA = "nssa"
    IPV6_PREFIX_ROUTE_ORIGIN_SAMEAREA = "samearea"

    LINEAR_LINK_MULTIPLIER_CMD = "linear_link_multiplier"

    LINEAR_NODES_CMD = "linear_nodes"

    LINK_METRIC_CMD = "link_metric"

    LINK_TE_CMD = "link_te"

    LINK_TE_ADMINISTRATOR_GROUP_CMD = "link_te_administrator_group"

    LINK_TE_MAX_BW_CMD = "link_te_max_bw"

    LINK_TE_MAX_RESV_BW_CMD = "link_te_max_resv_bw"

    LINK_TE_METRIC_CMD = "link_te_metric"

    LINK_TE_UNRESV_BW_PRIORITY0_CMD = "link_te_unresv_bw_priority0"

    LINK_TE_UNRESV_BW_PRIORITY1_CMD = "link_te_unresv_bw_priority1"

    LINK_TE_UNRESV_BW_PRIORITY2_CMD = "link_te_unresv_bw_priority2"

    LINK_TE_UNRESV_BW_PRIORITY3_CMD = "link_te_unresv_bw_priority3"

    LINK_TE_UNRESV_BW_PRIORITY4_CMD = "link_te_unresv_bw_priority4"

    LINK_TE_UNRESV_BW_PRIORITY5_CMD = "link_te_unresv_bw_priority5"

    LINK_TE_UNRESV_BW_PRIORITY6_CMD = "link_te_unresv_bw_priority6"

    LINK_TE_UNRESV_BW_PRIORITY7_CMD = "link_te_unresv_bw_priority7"

    LINKLSA_ACTIVE_CMD = "linklsa_active"

    LINKLSA_D_C_BIT_CMD = "linklsa_d_c_bit"

    LINKLSA_E_BIT_CMD = "linklsa_e_bit"

    LINKLSA_L_A_BIT_CMD = "linklsa_l_a_bit"

    LINKLSA_LINK_LOCAL_ADDRESS_CMD = "linklsa_link_local_address"

    LINKLSA_LINK_STATE_ID_CMD = "linklsa_link_state_id"

    LINKLSA_LINK_STATE_ID_PREFIX_CMD = "linklsa_link_state_id_prefix"

    LINKLSA_M_C_BIT_CMD = "linklsa_m_c_bit"

    LINKLSA_METRIC_CMD = "linklsa_metric"

    LINKLSA_N_BIT_CMD = "linklsa_n_bit"

    LINKLSA_N_U_BIT_CMD = "linklsa_n_u_bit"

    LINKLSA_NETWORK_ADDRESS_CMD = "linklsa_network_address"

    LINKLSA_P_BIT_CMD = "linklsa_p_bit"

    LINKLSA_PREFIX_CMD = "linklsa_prefix"

    LINKLSA_PREFIX_COUNT_CMD = "linklsa_prefix_count"

    LINKLSA_R_BIT_CMD = "linklsa_r_bit"

    LINKLSA_RESERVED_BIT6_CMD = "linklsa_reserved_bit6"

    LINKLSA_RESERVED_BIT7_CMD = "linklsa_reserved_bit7"

    LINKLSA_ROUTER_PRIORITY_CMD = "linklsa_router_priority"

    LINKLSA_UNUSED_BIT4_CMD = "linklsa_unused_bit4"

    LINKLSA_UNUSED_BIT5_CMD = "linklsa_unused_bit5"

    LINKLSA_UNUSED_BIT6_CMD = "linklsa_unused_bit6"

    LINKLSA_UNUSED_BIT7_CMD = "linklsa_unused_bit7"

    LINKLSA_V6_BIT_CMD = "linklsa_v6_bit"

    LINKLSA_X_BIT_CMD = "linklsa_x_bit"

    MESH_INCLUDE_EMULATED_DEVICE_CMD = "mesh_include_emulated_device"

    MESH_LINK_MULTIPLIER_CMD = "mesh_link_multiplier"

    MESH_NUMBER_OF_NODES_CMD = "mesh_number_of_nodes"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CREATE = "create"
    MODE_DELETE = "delete"
    MODE_MODIFY = "modify"

    MULTIPLIER_CMD = "multiplier"

    NSSA_ACTIVE_CMD = "nssa_active"

    NSSA_INCLUDE_FORWARDING_ADDRESS_CMD = "nssa_include_forwarding_address"

    NSSA_LINK_STATE_ID_CMD = "nssa_link_state_id"

    NSSA_LINK_STATE_ID_STEP_CMD = "nssa_link_state_id_step"

    NSSA_METRIC_CMD = "nssa_metric"

    NSSA_NETWORK_ADDRESS_CMD = "nssa_network_address"

    NSSA_NETWORK_ADDRESS_STEP_CMD = "nssa_network_address_step"

    NSSA_NUMBER_OF_ROUTES_CMD = "nssa_number_of_routes"

    NSSA_PREFIX_CMD = "nssa_prefix"

    NSSA_PROPAGATE_CMD = "nssa_propagate"

    PREFIX_CMD = "prefix"

    PROTOCOL_NAME_CMD = "protocol_name"

    RETURN_DETAILED_HANDLES_CMD = "return_detailed_handles"

    RING_INCLUDE_EMULATED_DEVICE_CMD = "ring_include_emulated_device"

    RING_LINK_MULTIPLIER_CMD = "ring_link_multiplier"

    RING_NUMBER_OF_NODES_CMD = "ring_number_of_nodes"

    ROUTER_ABR_CMD = "router_abr"

    ROUTER_ACTIVE_CMD = "router_active"

    ROUTER_ASBR_CMD = "router_asbr"

    ROUTER_ID_CMD = "router_id"

    ROUTER_ID_STEP_CMD = "router_id_step"

    ROUTER_SYSTEM_ID_CMD = "router_system_id"

    STUB_ACTIVE_CMD = "stub_active"

    STUB_METRIC_CMD = "stub_metric"

    STUB_NETWORK_ADDRESS_CMD = "stub_network_address"

    STUB_NETWORK_ADDRESS_STEP_CMD = "stub_network_address_step"

    STUB_NUMBER_OF_ROUTES_CMD = "stub_number_of_routes"

    STUB_PREFIX_CMD = "stub_prefix"

    SUBNET_PREFIX_LENGTH_CMD = "subnet_prefix_length"

    SUMMARY_ACTIVE_CMD = "summary_active"

    SUMMARY_METRIC_CMD = "summary_metric"

    SUMMARY_NETWORK_ADDRESS_CMD = "summary_network_address"

    SUMMARY_NETWORK_ADDRESS_STEP_CMD = "summary_network_address_step"

    SUMMARY_NUMBER_OF_ROUTES_CMD = "summary_number_of_routes"

    SUMMARY_PREFIX_CMD = "summary_prefix"

    TO_IP_CMD = "to_ip"

    TO_IP_STEP_CMD = "to_ip_step"

    TO_IPV6_CMD = "to_ipv6"

    TO_IPV6_STEP_CMD = "to_ipv6_step"

    TREE_DEPTH_CMD = "tree_depth"

    TREE_INCLUDE_EMULATED_DEVICE_CMD = "tree_include_emulated_device"

    TREE_LINK_MULTIPLIER_CMD = "tree_link_multiplier"

    TREE_MAX_CHILDREN_PER_NODE_CMD = "tree_max_children_per_node"

    TREE_NUMBER_OF_NODES_CMD = "tree_number_of_nodes"

    TREE_USE_TREE_DEPTH_CMD = "tree_use_tree_depth"

    TYPE_CMD = "type"
    # Constant values for TYPE_CMD
    TYPE_CUSTOM = "custom"
    TYPE_FATTREE = "fattree"
    TYPE_GRID = "grid"
    TYPE_HUBANDSPOKE = "hubandspoke"
    TYPE_IPV4PREFIX = "ipv4prefix"
    TYPE_IPV6PREFIX = "ipv6prefix"
    TYPE_LINEAR = "linear"
    TYPE_MESH = "mesh"
    TYPE_RING = "ring"
    TYPE_TREE = "tree"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -active_router_id
    -allow_propagate
    -auto_select_forwarding_address
    -connected_to_handle
    -custom_from_node_index
    -custom_link_multiplier
    -custom_to_node_index
    -enable_advertise_as_stub_network
    -enable_device
    -enable_ip
    -external1_active
    -external1_metric
    -external1_network_address
    -external1_network_address_step
    -external1_number_of_routes
    -external1_prefix
    -external2_active
    -external2_metric
    -external2_network_address
    -external2_network_address_step
    -external2_number_of_routes
    -external2_prefix
    -external_active
    -external_e_bit
    -external_external_route_tag
    -external_f_bit
    -external_forwarding_address
    -external_ipv6_network_address
    -external_ipv6_network_address_step
    -external_l_a_bit
    -external_link_network_group_handle
    -external_link_router_destination
    -external_link_router_source
    -external_link_state_id
    -external_link_state_id_prefix
    -external_m_c_bit
    -external_metric
    -external_n_u_bit
    -external_p_bit
    -external_prefix
    -external_prefix_count
    -external_reference_ls_type
    -external_referenced_link_state_id
    -external_t_bit
    -external_unused_bit4
    -external_unused_bit5
    -external_unused_bit6
    -external_unused_bit7
    -fat_tree_level_count
    -fat_tree_link_multiplier
    -fat_tree_node_count
    -forwarding_address
    -forwarding_address_step
    -from_ip
    -from_ip_step
    -from_ipv6
    -from_ipv6_step
    -grid_col
    -grid_include_emulated_device
    -grid_link_multiplier
    -grid_row
    -handle
    -hub_spoke_enable_level_2
    -hub_spoke_link_multiplier
    -hub_spoke_number_of_first_level
    -hub_spoke_number_of_second_level
    -inter_area_active
    -inter_area_d_c_bit
    -inter_area_destination_router_id
    -inter_area_destination_router_id_step
    -inter_area_e_bit
    -inter_area_link_state_id
    -inter_area_link_state_id_step
    -inter_area_m_c_bit
    -inter_area_metric
    -inter_area_n_bit
    -inter_area_prefix_active
    -inter_area_prefix_count
    -inter_area_prefix_l_a_bit
    -inter_area_prefix_link_state_id
    -inter_area_prefix_link_state_id_prefix
    -inter_area_prefix_m_c_bit
    -inter_area_prefix_metric
    -inter_area_prefix_n_u_bit
    -inter_area_prefix_network_address
    -inter_area_prefix_p_bit
    -inter_area_prefix_prefix
    -inter_area_prefix_prefix_count
    -inter_area_prefix_unused_bit4
    -inter_area_prefix_unused_bit5
    -inter_area_prefix_unused_bit6
    -inter_area_prefix_unused_bit7
    -inter_area_r_bit
    -inter_area_reserved_bit6
    -inter_area_reserved_bit7
    -inter_area_v6_bit
    -intra_area_active
    -intra_area_l_a_bit
    -intra_area_link_state_id
    -intra_area_link_state_id_prefix
    -intra_area_m_c_bit
    -intra_area_metric
    -intra_area_n_u_bit
    -intra_area_network_address
    -intra_area_network_address_step
    -intra_area_p_bit
    -intra_area_prefix_count
    -intra_area_reference_ls_type
    -intra_area_referenced_link_state_id
    -intra_area_referenced_router_id
    -intra_area_unused_bit4
    -intra_area_unused_bit5
    -intra_area_unused_bit6
    -intra_area_unused_bit7
    -ipv4_prefix_active
    -ipv4_prefix_allow_propagate
    -ipv4_prefix_length
    -ipv4_prefix_metric
    -ipv4_prefix_network_address
    -ipv4_prefix_network_address_step
    -ipv4_prefix_number_of_addresses
    -ipv4_prefix_route_origin
    -ipv6_prefix_active
    -ipv6_prefix_length
    -ipv6_prefix_metric
    -ipv6_prefix_network_address
    -ipv6_prefix_network_address_step
    -ipv6_prefix_number_of_addresses
    -ipv6_prefix_route_origin
    -linear_link_multiplier
    -linear_nodes
    -link_metric
    -link_te
    -link_te_administrator_group
    -link_te_max_bw
    -link_te_max_resv_bw
    -link_te_metric
    -link_te_unresv_bw_priority0
    -link_te_unresv_bw_priority1
    -link_te_unresv_bw_priority2
    -link_te_unresv_bw_priority3
    -link_te_unresv_bw_priority4
    -link_te_unresv_bw_priority5
    -link_te_unresv_bw_priority6
    -link_te_unresv_bw_priority7
    -linklsa_active
    -linklsa_d_c_bit
    -linklsa_e_bit
    -linklsa_l_a_bit
    -linklsa_link_local_address
    -linklsa_link_state_id
    -linklsa_link_state_id_prefix
    -linklsa_m_c_bit
    -linklsa_metric
    -linklsa_n_bit
    -linklsa_n_u_bit
    -linklsa_network_address
    -linklsa_p_bit
    -linklsa_prefix
    -linklsa_prefix_count
    -linklsa_r_bit
    -linklsa_reserved_bit6
    -linklsa_reserved_bit7
    -linklsa_router_priority
    -linklsa_unused_bit4
    -linklsa_unused_bit5
    -linklsa_unused_bit6
    -linklsa_unused_bit7
    -linklsa_v6_bit
    -linklsa_x_bit
    -mesh_include_emulated_device
    -mesh_link_multiplier
    -mesh_number_of_nodes
    -mode
    -multiplier
    -nssa_active
    -nssa_include_forwarding_address
    -nssa_link_state_id
    -nssa_link_state_id_step
    -nssa_metric
    -nssa_network_address
    -nssa_network_address_step
    -nssa_number_of_routes
    -nssa_prefix
    -nssa_propagate
    -prefix
    -protocol_name
    -return_detailed_handles
    -ring_include_emulated_device
    -ring_link_multiplier
    -ring_number_of_nodes
    -router_abr
    -router_active
    -router_asbr
    -router_id
    -router_id_step
    -router_system_id
    -stub_active
    -stub_metric
    -stub_network_address
    -stub_network_address_step
    -stub_number_of_routes
    -stub_prefix
    -subnet_prefix_length
    -summary_active
    -summary_metric
    -summary_network_address
    -summary_network_address_step
    -summary_number_of_routes
    -summary_prefix
    -to_ip
    -to_ip_step
    -to_ipv6
    -to_ipv6_step
    -tree_depth
    -tree_include_emulated_device
    -tree_link_multiplier
    -tree_max_children_per_node
    -tree_number_of_nodes
    -tree_use_tree_depth
    -type
If you want to update this file, look in the CSV
"""
