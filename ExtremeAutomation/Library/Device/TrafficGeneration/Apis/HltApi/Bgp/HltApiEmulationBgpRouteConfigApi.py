from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi

"""
    This is the API class for the command: emulation_bgp_route_config
"""


class EmulationBgpRouteConfigApi(TrafficGenerationApi):
    """
    init function
    """

    def __init__(self, device):
        TrafficGenerationApi.__init__(self, device)

    """
    This is the "One Large Method" for the command: emulation_bgp_route_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationBgpRouteConfigConstants.ARGUMENTS_CMD] = EmulationBgpRouteConfigConstants.ARGUMENTS_CONSTANTS # constant value
        dummyDict[EmulationBgpRouteConfigConstants.ACTIVE_CMD] = "dummyValue2" # static value
        dummyDict[EmulationBgpRouteConfigConstants.AD_VPLS_NLRI_CMD] = "dummyValue3" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ADVERTISE_LABEL_BLOCK_CMD] = "dummyValue4" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ADVERTISE_NEXTHOP_AS_V4_CMD] = "dummyValue5" # static value
        dummyDict[EmulationBgpRouteConfigConstants.AGGREGATOR_CMD] = "dummyValue6" # static value
        dummyDict[EmulationBgpRouteConfigConstants.AGGREGATOR_AS_CMD] = "dummyValue7" # static value
        dummyDict[EmulationBgpRouteConfigConstants.AGGREGATOR_ID_CMD] = "dummyValue8" # static value
        dummyDict[EmulationBgpRouteConfigConstants.AGGREGATOR_ID_MODE_CMD] = EmulationBgpRouteConfigConstants.AGGREGATOR_ID_MODE_FIXED # constant value
        dummyDict[EmulationBgpRouteConfigConstants.AS_NUMBER_VPLS_ID_CMD] = "dummyValue10" # static value
        dummyDict[EmulationBgpRouteConfigConstants.AS_NUMBER_VPLS_RD_CMD] = "dummyValue11" # static value
        dummyDict[EmulationBgpRouteConfigConstants.AS_NUMBER_VPLS_RT_CMD] = "dummyValue12" # static value
        dummyDict[EmulationBgpRouteConfigConstants.AS_PATH_CMD] = "dummyValue13" # static value
        dummyDict[EmulationBgpRouteConfigConstants.AS_PATH_SEGMENT_NUMBERS_CMD] = EmulationBgpRouteConfigConstants.AS_PATH_SEGMENT_NUMBERS_ANY # constant value
        dummyDict[EmulationBgpRouteConfigConstants.AS_PATH_SEGMENT_TYPE_CMD] = EmulationBgpRouteConfigConstants.AS_PATH_SEGMENT_TYPE_AS_SET_AS_SEQ # constant value
        dummyDict[EmulationBgpRouteConfigConstants.AS_PATH_SET_MODE_CMD] = EmulationBgpRouteConfigConstants.AS_PATH_SET_MODE_INCLUDE_AS_SEQ # constant value
        dummyDict[EmulationBgpRouteConfigConstants.ASSIGNED_NUMBER_VPLS_ID_CMD] = "dummyValue17" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ASSIGNED_NUMBER_VPLS_RD_CMD] = "dummyValue18" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ASSIGNED_NUMBER_VPLS_RT_CMD] = "dummyValue19" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ATOMIC_AGGREGATE_CMD] = "dummyValue20" # static value
        dummyDict[EmulationBgpRouteConfigConstants.CLUSTER_LIST_CMD] = "dummyValue21" # static value
        dummyDict[EmulationBgpRouteConfigConstants.CLUSTER_LIST_ENABLE_CMD] = "dummyValue22" # static value
        dummyDict[EmulationBgpRouteConfigConstants.COMMUNITIES_CMD] = "dummyValue23" # static value
        dummyDict[EmulationBgpRouteConfigConstants.COMMUNITIES_AS_NUMBER_CMD] = "dummyValue24" # static value
        dummyDict[EmulationBgpRouteConfigConstants.COMMUNITIES_ENABLE_CMD] = "dummyValue25" # static value
        dummyDict[EmulationBgpRouteConfigConstants.COMMUNITIES_LAST_TWO_OCTETS_CMD] = "dummyValue26" # static value
        dummyDict[EmulationBgpRouteConfigConstants.COMMUNITIES_TYPE_CMD] = EmulationBgpRouteConfigConstants.COMMUNITIES_TYPE_NO_EXPORT_NO_ADVERTISED # constant value
        dummyDict[EmulationBgpRouteConfigConstants.CONTROL_WORD_ENABLE_CMD] = "dummyValue28" # static value
        dummyDict[EmulationBgpRouteConfigConstants.DEFAULT_MDT_IP_CMD] = "dummyValue29" # static value
        dummyDict[EmulationBgpRouteConfigConstants.DEFAULT_MDT_IP_INCR_CMD] = "dummyValue30" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ENABLE_AGGREGATOR_CMD] = "dummyValue31" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ENABLE_AS_PATH_CMD] = "dummyValue32" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ENABLE_GENERATE_UNIQUE_ROUTES_CMD] = "dummyValue33" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ENABLE_LOCAL_PREF_CMD] = "dummyValue34" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ENABLE_MED_CMD] = "dummyValue35" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ENABLE_PARTIAL_ROUTE_FLAP_CMD] = "dummyValue36" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ENABLE_ROUTE_FLAP_CMD] = "dummyValue37" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ENABLE_TRADITIONAL_NLRI_CMD] = "dummyValue38" # static value
        dummyDict[EmulationBgpRouteConfigConstants.END_OF_RIB_CMD] = "dummyValue39" # static value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_CMD] = "dummyValue40" # static value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_AS_FOUR_BYTES_CMD] = "dummyValue41" # static value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_AS_TWO_BYTES_CMD] = "dummyValue42" # static value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_ASSIGNED_FOUR_BYTES_CMD] = "dummyValue43" # static value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_ASSIGNED_TWO_BYTES_CMD] = "dummyValue44" # static value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_ENABLE_CMD] = "dummyValue45" # static value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_IP_CMD] = "dummyValue46" # static value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_OPAQUE_DATA_CMD] = "dummyValue47" # static value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_SUBTYPE_CMD] = EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_SUBTYPE_ROUTE_TARGET # constant value
        dummyDict[EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_TYPE_CMD] = EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_TYPE_ADMIN_AS_TWO_OCTET # constant value
        dummyDict[EmulationBgpRouteConfigConstants.FLAP_DELAY_CMD] = "dummyValue50" # static value
        dummyDict[EmulationBgpRouteConfigConstants.FLAP_DOWN_TIME_CMD] = "dummyValue51" # static value
        dummyDict[EmulationBgpRouteConfigConstants.FLAP_UP_TIME_CMD] = "dummyValue52" # static value
        dummyDict[EmulationBgpRouteConfigConstants.HANDLE_CMD] = "dummyValue53" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_RD_AS_RT_CMD] = "dummyValue54" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_RT_AS_EXPORT_RT_CMD] = "dummyValue55" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_TARGET_CMD] = "dummyValue56" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_TARGET_ASSIGN_CMD] = "dummyValue57" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_TARGET_ASSIGN_INNER_STEP_CMD] = "dummyValue58" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_TARGET_ASSIGN_STEP_CMD] = "dummyValue59" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_TARGET_COUNT_CMD] = "dummyValue60" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_TARGET_INNER_STEP_CMD] = "dummyValue61" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_TARGET_STEP_CMD] = "dummyValue62" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_TARGET_TYPE_CMD] = EmulationBgpRouteConfigConstants.IMPORT_TARGET_TYPE_AS # constant value
        dummyDict[EmulationBgpRouteConfigConstants.IMPORT_VPLS_ID_AS_RD_CMD] = "dummyValue64" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IP_ADDRESS_VPLS_ID_CMD] = "dummyValue65" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IP_ADDRESS_VPLS_RD_CMD] = "dummyValue66" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IP_ADDRESS_VPLS_RT_CMD] = "dummyValue67" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IP_VERSION_CMD] = EmulationBgpRouteConfigConstants.IP_VERSION_4 # constant value
        dummyDict[EmulationBgpRouteConfigConstants.IPV4_MPLS_NLRI_CMD] = "dummyValue69" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IPV4_MPLS_VPN_NLRI_CMD] = "dummyValue70" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IPV4_MULTICAST_NLRI_CMD] = "dummyValue71" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IPV4_UNICAST_NLRI_CMD] = "dummyValue72" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IPV6_MPLS_NLRI_CMD] = "dummyValue73" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IPV6_MPLS_VPN_NLRI_CMD] = "dummyValue74" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IPV6_MULTICAST_NLRI_CMD] = "dummyValue75" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IPV6_PREFIX_LENGTH_CMD] = "dummyValue76" # static value
        dummyDict[EmulationBgpRouteConfigConstants.IPV6_UNICAST_NLRI_CMD] = "dummyValue77" # static value
        dummyDict[EmulationBgpRouteConfigConstants.L2_ENABLE_VLAN_CMD] = "dummyValue78" # static value
        dummyDict[EmulationBgpRouteConfigConstants.L2_MAC_COUNT_CMD] = "dummyValue79" # static value
        dummyDict[EmulationBgpRouteConfigConstants.L2_MAC_INCR_CMD] = "dummyValue80" # static value
        dummyDict[EmulationBgpRouteConfigConstants.L2_START_MAC_ADDR_CMD] = "dummyValue81" # static value
        dummyDict[EmulationBgpRouteConfigConstants.L2_VLAN_ID_CMD] = "dummyValue82" # static value
        dummyDict[EmulationBgpRouteConfigConstants.L2_VLAN_ID_INCR_CMD] = "dummyValue83" # static value
        dummyDict[EmulationBgpRouteConfigConstants.L2_VLAN_INCR_CMD] = EmulationBgpRouteConfigConstants.L2_VLAN_INCR_0 # constant value
        dummyDict[EmulationBgpRouteConfigConstants.L2_VLAN_PRIORITY_CMD] = "dummyValue85" # static value
        dummyDict[EmulationBgpRouteConfigConstants.L2_VLAN_TPID_CMD] = EmulationBgpRouteConfigConstants.L2_VLAN_TPID_0X8100 # constant value
        dummyDict[EmulationBgpRouteConfigConstants.L3_SITE_HANDLE_CMD] = "dummyValue87" # static value
        dummyDict[EmulationBgpRouteConfigConstants.LABEL_BLOCK_OFFSET_CMD] = "dummyValue88" # static value
        dummyDict[EmulationBgpRouteConfigConstants.LABEL_BLOCK_OFFSET_TYPE_CMD] = EmulationBgpRouteConfigConstants.LABEL_BLOCK_OFFSET_TYPE_LIST # constant value
        dummyDict[EmulationBgpRouteConfigConstants.LABEL_ID_CMD] = "dummyValue90" # static value
        dummyDict[EmulationBgpRouteConfigConstants.LABEL_INCR_MODE_CMD] = EmulationBgpRouteConfigConstants.LABEL_INCR_MODE_FIXED # constant value
        dummyDict[EmulationBgpRouteConfigConstants.LABEL_STEP_CMD] = "dummyValue92" # static value
        dummyDict[EmulationBgpRouteConfigConstants.LABEL_VALUE_CMD] = EmulationBgpRouteConfigConstants.LABEL_VALUE_NUMERIC # constant value
        dummyDict[EmulationBgpRouteConfigConstants.LABEL_VALUE_END_CMD] = "dummyValue94" # static value
        dummyDict[EmulationBgpRouteConfigConstants.LABEL_VALUE_TYPE_CMD] = EmulationBgpRouteConfigConstants.LABEL_VALUE_TYPE_LIST # constant value
        dummyDict[EmulationBgpRouteConfigConstants.LOCAL_PREF_CMD] = "dummyValue96" # static value
        dummyDict[EmulationBgpRouteConfigConstants.MAX_ROUTE_RANGES_CMD] = "dummyValue97" # static value
        dummyDict[EmulationBgpRouteConfigConstants.MODE_CMD] = EmulationBgpRouteConfigConstants.MODE_ADD # constant value
        dummyDict[EmulationBgpRouteConfigConstants.MTU_CMD] = "dummyValue99" # static value
        dummyDict[EmulationBgpRouteConfigConstants.MULTI_EXIT_DISC_CMD] = "dummyValue100" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NETMASK_CMD] = "dummyValue101" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NEXT_HOP_CMD] = "dummyValue102" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NEXT_HOP_ENABLE_CMD] = "dummyValue103" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NEXT_HOP_IP_VERSION_CMD] = EmulationBgpRouteConfigConstants.NEXT_HOP_IP_VERSION_4 # constant value
        dummyDict[EmulationBgpRouteConfigConstants.NEXT_HOP_IPV4_CMD] = "dummyValue105" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NEXT_HOP_IPV6_CMD] = "dummyValue106" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NEXT_HOP_MODE_CMD] = EmulationBgpRouteConfigConstants.NEXT_HOP_MODE_FIXED # constant value
        dummyDict[EmulationBgpRouteConfigConstants.NEXT_HOP_SET_MODE_CMD] = EmulationBgpRouteConfigConstants.NEXT_HOP_SET_MODE_SAME # constant value
        dummyDict[EmulationBgpRouteConfigConstants.NO_WRITE_CMD] = "dummyValue109" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NUM_LABELS_CMD] = "dummyValue110" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NUM_LABELS_TYPE_CMD] = EmulationBgpRouteConfigConstants.NUM_LABELS_TYPE_LIST # constant value
        dummyDict[EmulationBgpRouteConfigConstants.NUM_ROUTES_CMD] = "dummyValue112" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NUM_SITES_CMD] = "dummyValue113" # static value
        dummyDict[EmulationBgpRouteConfigConstants.NUMBER_VSI_ID_CMD] = "dummyValue114" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ORIGIN_CMD] = EmulationBgpRouteConfigConstants.ORIGIN_IGP # constant value
        dummyDict[EmulationBgpRouteConfigConstants.ORIGIN_ROUTE_ENABLE_CMD] = "dummyValue116" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ORIGINATOR_ID_CMD] = "dummyValue117" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ORIGINATOR_ID_ENABLE_CMD] = "dummyValue118" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PACKING_FROM_CMD] = "dummyValue119" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PACKING_TO_CMD] = "dummyValue120" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PARTIAL_ROUTE_FLAP_FROM_ROUTE_INDEX_CMD] = "dummyValue121" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PARTIAL_ROUTE_FLAP_TO_ROUTE_INDEX_CMD] = "dummyValue122" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PREFIX_CMD] = EmulationBgpRouteConfigConstants.PREFIX_IP # constant value
        dummyDict[EmulationBgpRouteConfigConstants.PREFIX_FROM_CMD] = "dummyValue124" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PREFIX_STEP_CMD] = "dummyValue125" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PREFIX_STEP_ACCROSS_VRFS_CMD] = EmulationBgpRouteConfigConstants.PREFIX_STEP_ACCROSS_VRFS_IP # constant value
        dummyDict[EmulationBgpRouteConfigConstants.PREFIX_STEP_ACROSS_VRFS_CMD] = "dummyValue127" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PREFIX_TO_CMD] = "dummyValue128" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PROTOCOL_NAME_CMD] = "dummyValue129" # static value
        dummyDict[EmulationBgpRouteConfigConstants.PROTOCOL_ROUTE_NAME_CMD] = "dummyValue130" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_ADMIN_STEP_CMD] = "dummyValue131" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_ADMIN_VALUE_CMD] = "dummyValue132" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_ADMIN_VALUE_STEP_CMD] = "dummyValue133" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_ADMIN_VALUE_STEP_ACROSS_VRFS_CMD] = "dummyValue134" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_ASSIGN_STEP_CMD] = "dummyValue135" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_ASSIGN_VALUE_CMD] = "dummyValue136" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_ASSIGN_VALUE_STEP_CMD] = "dummyValue137" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_ASSIGN_VALUE_STEP_ACROSS_VRFS_CMD] = "dummyValue138" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_COUNT_CMD] = "dummyValue139" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_COUNT_PER_VRF_CMD] = "dummyValue140" # static value
        dummyDict[EmulationBgpRouteConfigConstants.RD_TYPE_CMD] = EmulationBgpRouteConfigConstants.RD_TYPE_0 # constant value
        dummyDict[EmulationBgpRouteConfigConstants.ROUTE_HANDLE_CMD] = "dummyValue142" # static value
        dummyDict[EmulationBgpRouteConfigConstants.ROUTE_IP_ADDR_STEP_CMD] = EmulationBgpRouteConfigConstants.ROUTE_IP_ADDR_STEP_IP # constant value
        dummyDict[EmulationBgpRouteConfigConstants.SEQ_DELIVERY_ENABLE_CMD] = "dummyValue144" # static value
        dummyDict[EmulationBgpRouteConfigConstants.SITE_ID_CMD] = "dummyValue145" # static value
        dummyDict[EmulationBgpRouteConfigConstants.SITE_ID_STEP_CMD] = "dummyValue146" # static value
        dummyDict[EmulationBgpRouteConfigConstants.TARGET_CMD] = "dummyValue147" # static value
        dummyDict[EmulationBgpRouteConfigConstants.TARGET_ASSIGN_CMD] = "dummyValue148" # static value
        dummyDict[EmulationBgpRouteConfigConstants.TARGET_ASSIGN_INNER_STEP_CMD] = "dummyValue149" # static value
        dummyDict[EmulationBgpRouteConfigConstants.TARGET_ASSIGN_STEP_CMD] = "dummyValue150" # static value
        dummyDict[EmulationBgpRouteConfigConstants.TARGET_COUNT_CMD] = "dummyValue151" # static value
        dummyDict[EmulationBgpRouteConfigConstants.TARGET_INNER_STEP_CMD] = "dummyValue152" # static value
        dummyDict[EmulationBgpRouteConfigConstants.TARGET_STEP_CMD] = "dummyValue153" # static value
        dummyDict[EmulationBgpRouteConfigConstants.TARGET_TYPE_CMD] = EmulationBgpRouteConfigConstants.TARGET_TYPE_AS # constant value
        dummyDict[EmulationBgpRouteConfigConstants.TYPE_VPLS_ID_CMD] = EmulationBgpRouteConfigConstants.TYPE_VPLS_ID_AS # constant value
        dummyDict[EmulationBgpRouteConfigConstants.TYPE_VPLS_RD_CMD] = EmulationBgpRouteConfigConstants.TYPE_VPLS_RD_AS # constant value
        dummyDict[EmulationBgpRouteConfigConstants.TYPE_VPLS_RT_CMD] = EmulationBgpRouteConfigConstants.TYPE_VPLS_RT_AS # constant value
        dummyDict[EmulationBgpRouteConfigConstants.TYPE_VSI_ID_CMD] = EmulationBgpRouteConfigConstants.TYPE_VSI_ID_CONCAT_PE_ADDR # constant value
        dummyDict[EmulationBgpRouteConfigConstants.VPLS_CMD] = "dummyValue159" # static value
        dummyDict[EmulationBgpRouteConfigConstants.VPLS_NLRI_CMD] = "dummyValue160" # static value
        dummyDict[EmulationBgpRouteConfigConstants.VPN_NAME_CMD] = EmulationBgpRouteConfigConstants.VPN_NAME_ALPHA # constant value

        api = device.getApi(EmulationBgpRouteConfigConstants.EMULATION_BGP_ROUTE_CONFIG_API)
        api.emulation_bgp_route_config(dummyDict)
    """

    def emulation_bgp_route_config(self, argdictionary):
        return self.send_command_args(self._nameSpace + "::emulation_bgp_route_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """

    def emulation_bgp_route_config_Arguments(self, parameter):
        """
        This is the method the command: emulation_bgp_route_config option Arguments
        Description:Description
        Constants Available: ARGUMENTS_CMD
        Supported:Supported
        Keyword arguments:
        parameter --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ARGUMENTS_CMD: parameter})

    def emulation_bgp_route_config_active(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option active
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Activates the item

            DEFAULT
             None
        Constants Available: ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ACTIVE_CMD: bool})

    def emulation_bgp_route_config_ad_vpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option ad_vpls_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            This BGP/BGP+ router/peer supports BGP/BGP+ AD VPLS. Does not take priority over other flags that enable L3 sites. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast.

            DEFAULT
             None
        Constants Available: AD_VPLS_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AD_VPLS_NLRI_CMD: flag})

    def emulation_bgp_route_config_advertise_label_block(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option advertise_label_block
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Advertise Label Block

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: ADVERTISE_LABEL_BLOCK_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ADVERTISE_LABEL_BLOCK_CMD: bool})

    def emulation_bgp_route_config_advertise_nexthop_as_v4(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option advertise_nexthop_as_v4
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Advertise Nexthop as V4

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ADVERTISE_NEXTHOP_AS_V4_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ADVERTISE_NEXTHOP_AS_V4_CMD: bool})

    def emulation_bgp_route_config_aggregator(self, any):
        """
        This is the method the command: emulation_bgp_route_config option aggregator
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            For the AGGREGATOR path attribute, specifies the last AS number that formed the aggregate route, and the IP address of the BGP speaker that formed the aggregate route. Format: :.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: AGGREGATOR_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AGGREGATOR_CMD: any})

    def emulation_bgp_route_config_aggregator_as(self, number):
        """
        This is the method the command: emulation_bgp_route_config option aggregator_as
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            For the AGGREGATOR path attribute, specifies the last AS number that formed the aggregate route. Has priority over the legacy -aggregator parameter.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: AGGREGATOR_AS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        number --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AGGREGATOR_AS_CMD: number})

    def emulation_bgp_route_config_aggregator_id(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option aggregator_id
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            For the AGGREGATOR path attribute, specifies the IP address of the BGP speaker that formed the aggregate route. Has priority over the legacy -aggregator parameter.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: AGGREGATOR_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AGGREGATOR_ID_CMD: ip})

    def emulation_bgp_route_config_aggregator_id_mode(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option aggregator_id_mode
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Aggregator ID Mode

            Valid options are:

            fixed


            Fixed mode

            increment


            Increment aggregator ID

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: AGGREGATOR_ID_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AGGREGATOR_ID_MODE_CMD: opt})

    def emulation_bgp_route_config_as_number_vpls_id(self, any):
        """
        This is the method the command: emulation_bgp_route_config option as_number_vpls_id
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            VPLS ID AS Number

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: AS_NUMBER_VPLS_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AS_NUMBER_VPLS_ID_CMD: any})

    def emulation_bgp_route_config_as_number_vpls_rd(self, any):
        """
        This is the method the command: emulation_bgp_route_config option as_number_vpls_rd
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Route Distinguisher AS Number

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: AS_NUMBER_VPLS_RD_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AS_NUMBER_VPLS_RD_CMD: any})

    def emulation_bgp_route_config_as_number_vpls_rt(self, any):
        """
        This is the method the command: emulation_bgp_route_config option as_number_vpls_rt
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Route Target AS Number

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: AS_NUMBER_VPLS_RT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AS_NUMBER_VPLS_RT_CMD: any})

    def emulation_bgp_route_config_as_path(self, path):
        """
        This is the method the command: emulation_bgp_route_config option as_path
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies the AS_PATH path attribute, which is a mandatory attribute composed of a sequence of AS path segments.Format: :{as_set|as_seq|as_confed_set|as_confed_seq}:<x,x,x,x>Example:as_set:1,2,3,4as_set - specifies an unordered set of autonomous systems though which a route in the UPDATE message has traversed.as_seq - specifies an ordered set of autonomous systems through which a route in the UPDATE message has traversed.as_confed_set - specifies an unordered set of autonomous systems in the local confederation that the UPDATE message has traversed.as_confed_seq - specifies an ordered set of autonomous systems in the local confederation that the UPDATE message has traversed.DEFAULT = as_set:, where is the AS of the router which advertises this route. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the AS_PATH path attribute, which is a mandatory attribute composed of a sequence of AS path segments. Format: : {as_set|as_seq|as_confed_set|as_confed_seq}:<x,x,x,x>. Example: as_set:1,2,3,4 as_set - specifies an unordered set of autonomous systems though which a route in the UPDATE message has traversed. as_seq - specifies an ordered set of autonomous systems through which a route in the UPDATE message has traversed. as_confed_set - specifies an unordered set of autonomous systems in the local confederation that the UPDATE message has traversed. as_confed_seq - specifies an ordered set of autonomous systems in the local confederation that the UPDATE message has traversed. DEFAULT = as_set:, where is the AS of the router which advertises this route.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: AS_PATH_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        path --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AS_PATH_CMD: path})

    def emulation_bgp_route_config_as_path_segment_numbers(self, any):
        """
        This is the method the command: emulation_bgp_route_config option as_path_segment_numbers
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            A list of lists of AS_PATH segment numbers. The outer list length needs to match as_path_segment_type list length.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: AS_PATH_SEGMENT_NUMBERS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AS_PATH_SEGMENT_NUMBERS_CMD: any})

    def emulation_bgp_route_config_as_path_segment_type(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option as_path_segment_type
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the segment type for the AS_PATH attribute. This may be a list of values with equal length to the as_path parameter list.

            Valid options are:

            as_set


            AS-SET

            as_seq


            AS-SEQ

            as_confed_set


            AS-SET-CONFEDERATION

            as_confed_seq


            AS-SEQ-CONFEDERATION

            DEFAULT


            as_set

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: AS_PATH_SEGMENT_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AS_PATH_SEGMENT_TYPE_CMD: opt})

    def emulation_bgp_route_config_as_path_set_mode(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option as_path_set_mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            For External routing only. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            Valid options are:

            no_include


            Don't include Local AS#

            include_as_seq


            Include Local AS# as AS-SEQ

            include_as_set


            Include Local AS# as AS-SET

            include_as_seq_conf


            Include Local AS# as AS-SEQ-Confederation

            include_as_set_conf


            Include Local AS# as AS-SET-Confederation

            prepend_as


            Prepend Local AS# to first segment

            DEFAULT


            include_as_seq

            IxNetwork-NGPF


            DESCRIPTION


            For External routing only. Optional setup for the AS-Path.

            Valid options are:

            include_as_seq


            Include Local AS as AS-SEQ

            include_as_seq_conf


            Include Local AS as AS-SEQ-Confederation

            include_as_set


            Include Local AS as AS-SET

            include_as_set_conf


            Include Local AS as AS-SET-Confederation

            no_include


            Don't include Local AS

            prepend_as


            Prepend Local AS to first segment

            DEFAULT


            include_as_seq

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: AS_PATH_SET_MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.AS_PATH_SET_MODE_CMD: opt})

    def emulation_bgp_route_config_assigned_number_vpls_id(self, any):
        """
        This is the method the command: emulation_bgp_route_config option assigned_number_vpls_id
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            VPLS ID Assigned Number

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: ASSIGNED_NUMBER_VPLS_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ASSIGNED_NUMBER_VPLS_ID_CMD: any})

    def emulation_bgp_route_config_assigned_number_vpls_rd(self, any):
        """
        This is the method the command: emulation_bgp_route_config option assigned_number_vpls_rd
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Route Distinguisher Assigned Number

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: ASSIGNED_NUMBER_VPLS_RD_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ASSIGNED_NUMBER_VPLS_RD_CMD: any})

    def emulation_bgp_route_config_assigned_number_vpls_rt(self, any):
        """
        This is the method the command: emulation_bgp_route_config option assigned_number_vpls_rt
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Route Target Assigned Number

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: ASSIGNED_NUMBER_VPLS_RT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ASSIGNED_NUMBER_VPLS_RT_CMD: any})

    def emulation_bgp_route_config_atomic_aggregate(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option atomic_aggregate
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies the ATOMIC_AGGREGATE path attribute, which is a discretionary attribute. If set to 1, informs other BGP speakers that the local system selected a less specific route without selecting a more specific route included in it. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the ATOMIC_AGGREGATE path attribute, which is a discretionary attribute. If set to 1, informs other BGP speakers that the local system selected a less specific route without selecting a more specific route included in it.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ATOMIC_AGGREGATE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ATOMIC_AGGREGATE_CMD: flag})

    def emulation_bgp_route_config_cluster_list(self, string):
        """
        This is the method the command: emulation_bgp_route_config option cluster_list
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies the CLUSTER_LIST path attribute, which is an optional, non-transitive BGP attribute. It is a sequence of CLUSTER_ID values representing the reflection path through which the route has passed. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the CLUSTER_LIST path attribute, which is an optional, non-transitive BGP attribute. It is a sequence of CLUSTER_ID values representing the reflection path through which the route has passed.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: CLUSTER_LIST_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        string --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.CLUSTER_LIST_CMD: string})

    def emulation_bgp_route_config_cluster_list_enable(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option cluster_list_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Enables or disables cluster list on BGP route range.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables or disables cluster list on BGP route range.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: CLUSTER_LIST_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.CLUSTER_LIST_ENABLE_CMD: flag})

    def emulation_bgp_route_config_communities(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option communities
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies the COMMUNITIES path attribute, which is an optional transitive attribute of variable length. All routes with this attribute belong to the communities listed in the attribute. This is a list of numbers. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the COMMUNITIES path attribute, which is an optional transitive attribute of variable length. All routes with this attribute belong to the communities listed in the attribute. This is a list of numbers.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: COMMUNITIES_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.COMMUNITIES_CMD: numeric})

    def emulation_bgp_route_config_communities_as_number(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option communities_as_number
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Communities AS #

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: COMMUNITIES_AS_NUMBER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.COMMUNITIES_AS_NUMBER_CMD: numeric})

    def emulation_bgp_route_config_communities_enable(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option communities_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Enables or disables communities. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables or disables communities.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: COMMUNITIES_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.COMMUNITIES_ENABLE_CMD: flag})

    def emulation_bgp_route_config_communities_last_two_octets(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option communities_last_two_octets
        Description:upported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Last Two Octets

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: COMMUNITIES_LAST_TWO_OCTETS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.COMMUNITIES_LAST_TWO_OCTETS_CMD: numeric})

    def emulation_bgp_route_config_communities_type(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option communities_type
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Type

            Valid options are:

            noexport


            No export

            noadvertised


            No advertised

            noexport_subconfed


            No export subconfed

            manual


            Manual AS number

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: COMMUNITIES_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.COMMUNITIES_TYPE_CMD: opt})

    def emulation_bgp_route_config_control_word_enable(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option control_word_enable
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Enable Control Word

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: CONTROL_WORD_ENABLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.CONTROL_WORD_ENABLE_CMD: bool})

    def emulation_bgp_route_config_default_mdt_ip(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option default_mdt_ip
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Defines the IP address of the default MDT for mVPN. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Defines the IP address of the default MDT for mVPN.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: DEFAULT_MDT_IP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.DEFAULT_MDT_IP_CMD: ip})

    def emulation_bgp_route_config_default_mdt_ip_incr(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option default_mdt_ip_incr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Defines the IP address increment for each default MDT. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Defines the IP address increment for each default MDT.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: DEFAULT_MDT_IP_INCR_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.DEFAULT_MDT_IP_INCR_CMD: ip})

    def emulation_bgp_route_config_enable_aggregator(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option enable_aggregator
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Enable Aggregator ID

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ENABLE_AGGREGATOR_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ENABLE_AGGREGATOR_CMD: bool})

    def emulation_bgp_route_config_enable_as_path(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option enable_as_path
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This parameter indicates that as_path attributes are to be generated. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            This parameter indicates that as_path attributes are to be generated.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ENABLE_AS_PATH_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ENABLE_AS_PATH_CMD: bool})

    def emulation_bgp_route_config_enable_generate_unique_routes(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option enable_generate_unique_routes
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            FLAG - When set to 1, each router generates a different IP address range. When set to 0, each router advertises the route range as is. When enabled, the first router advertises numRoutes routes starting at networkAddress, the next router advertises numRoutes routes starting at (networkAddress + numRoutes), and so on. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            FLAG - When set to 1, each router generates a different IP address range. When set to 0, each router advertises the route range as is. When enabled, the first router advertises numRoutes routes starting at networkAddress, the next router advertises numRoutes routes starting at (networkAddress + numRoutes), and so on.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ENABLE_GENERATE_UNIQUE_ROUTES_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.ENABLE_GENERATE_UNIQUE_ROUTES_CMD: flag})

    def emulation_bgp_route_config_enable_local_pref(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option enable_local_pref
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This attribute inserts a local_pref attribute with the indicated value. (internal bgp only) Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            This attribute inserts a local_pref attribute with the indicated value. (internal bgp only)

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ENABLE_LOCAL_PREF_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ENABLE_LOCAL_PREF_CMD: bool})

    def emulation_bgp_route_config_enable_med(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option enable_med
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Enable Multi Exit

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ENABLE_MED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ENABLE_MED_CMD: bool})

    def emulation_bgp_route_config_enable_partial_route_flap(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option enable_partial_route_flap
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            FLAG - Enable partial flapping functions. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            FLAG - Enable partial flapping functions.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ENABLE_PARTIAL_ROUTE_FLAP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ENABLE_PARTIAL_ROUTE_FLAP_CMD: flag})

    def emulation_bgp_route_config_enable_route_flap(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option enable_route_flap
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            FLAG - Enables the flapping functions described by route_flap_up_time, route_flap_down_time, routesToFlapFrom, and routesToFlapTo. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            FLAG - Enables the flapping functions described by route_flap_up_time, route_flap_down_time, routesToFlapFrom, and routesToFlapTo.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ENABLE_ROUTE_FLAP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ENABLE_ROUTE_FLAP_CMD: flag})

    def emulation_bgp_route_config_enable_traditional_nlri(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option enable_traditional_nlri
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If checked, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)Values: 0 1. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If checked, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ENABLE_TRADITIONAL_NLRI_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ENABLE_TRADITIONAL_NLRI_CMD: bool})

    def emulation_bgp_route_config_end_of_rib(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option end_of_rib
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Configures BGP End of RIB markerValid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Configures BGP End of RIB marker

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: END_OF_RIB_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.END_OF_RIB_CMD: bool})

    def emulation_bgp_route_config_ext_communities(self, string):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies the EXTENDED COMMUNITIES path attribute, which is a transitive optional BGP attribute. All routes with the EXTENDED COMMUNITIES attribute belong to the communities listed in the attribute.This is a list of numbers separated by comma char "","" as follows:

            The first number is the value of the low-order type byte.

            Possible values:

            0 - (default)
            2 - Route target community
            3 - Route origin community
            4 - Link bandwidth community

            The second number is the value of the high-order type byte.
            Possible values:
            128 - IANA bit: This bit may be or'd with any other values.
            0 indicates that this is an IANA assignable type using First Come First Serve policy.
            1 indicates that this is an IANA assignable type using the IETF Consensus policy.
            64 - Transitive bit: This bit may be ordered with any other values.
            0 indicates that the community is transitive across ASes and
            1 indicates that it is non-transitive.
            0 - Two-octet AS specific (default): Value holds a two-octet global ASN followed by a four-bytes local admin value.
            1 - IPv4 address specific: Value holds a four-octet IP address followed by a two-bytes local administrator value.
            2 - Four-octet AS specific: Value holds a four-octet global ASN followed by a two-bytes local admin value.
            3 - Generic: Value holds six-octets.

            The third number is the value associated with the extended community. (default = {00 00 00 00 00 00})
            Example value: {2,128,03 22 00 00 00 00}. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the EXTENDED COMMUNITIES path attribute, which is a transitive optional BGP attribute. All routes with the EXTENDED COMMUNITIES attribute belong to the communities listed in the attribute. This is a list of numbers separated by comma char "","" as follows: The first number is the value of the low-order type byte. Possible values: 0 - (default) 2 - Route target community 3 - Route origin community 4 - Link bandwidth community The second number is the value of the high-order type byte. Possible values: 128 - IANA bit: This bit may be or'd with any other values. 0 indicates that this is an IANA assignable type using First Come First Serve policy. 1 indicates that this is an IANA assignable type using the IETF Consensus policy. 64 - Transitive bit: This bit may be or'd with any other values. 0 indicates that the community is transitive across ASes and 1 indicates that it is non-transitive. 0 - Two-octet AS specific (default): Value holds a two-octet global ASN followed by a four-bytes local admin value. 1 - IPv4 address specific: Value holds a four-octet IP address followed by a two-bytes local administrator value. 2 - Four-octet AS specific: Value holds a four-octet global ASN followed by a two-bytes local admin value. 3 - Generic: Value holds six-octets. The third number is the value associated with the extended community. (default = {00 00 00 00 00 00}) Example value: {2,128,03 22 00 00 00 00}.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        string --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_CMD: string})

    def emulation_bgp_route_config_ext_communities_as_four_bytes(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities_as_four_bytes
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            AS 4-Bytes

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_AS_FOUR_BYTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_AS_FOUR_BYTES_CMD: numeric})

    def emulation_bgp_route_config_ext_communities_as_two_bytes(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities_as_two_bytes
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            AS 2-Bytes

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_AS_TWO_BYTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_AS_TWO_BYTES_CMD: numeric})

    def emulation_bgp_route_config_ext_communities_assigned_four_bytes(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities_assigned_four_bytes
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Assigned Number(4 Octets)

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_ASSIGNED_FOUR_BYTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_ASSIGNED_FOUR_BYTES_CMD: numeric})

    def emulation_bgp_route_config_ext_communities_assigned_two_bytes(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities_assigned_two_bytes
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Assigned Number(2 Octets)

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_ASSIGNED_TWO_BYTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_ASSIGNED_TWO_BYTES_CMD: numeric})

    def emulation_bgp_route_config_ext_communities_enable(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities_enable
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Enable Extended Community

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_ENABLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_ENABLE_CMD: bool})

    def emulation_bgp_route_config_ext_communities_ip(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities_ip
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            IP

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_IP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_IP_CMD: ip})

    def emulation_bgp_route_config_ext_communities_opaque_data(self, any):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities_opaque_data
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Opaque Data

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_OPAQUE_DATA_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_OPAQUE_DATA_CMD: any})

    def emulation_bgp_route_config_ext_communities_subtype(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities_subtype
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            SubType

            Valid options are:

            routetarget


            Route target

            origin


            Origin

            extendedbandwidth


            Extended bandwidth

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_SUBTYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_SUBTYPE_CMD: opt})

    def emulation_bgp_route_config_ext_communities_type(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option ext_communities_type
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Type

            Valid options are:

            administratoras2octet


            Admin AS number 2 octet

            administratorip


            Admin IP address

            administratoras4octet


            Admin AS number 4 octet

            opaque


            Opaque data

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: EXT_COMMUNITIES_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.EXT_COMMUNITIES_TYPE_CMD: opt})

    def emulation_bgp_route_config_flap_delay(self, number):
        """
        This is the method the command: emulation_bgp_route_config option flap_delay
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Flapping delay

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: FLAP_DELAY_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        number --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.FLAP_DELAY_CMD: number})

    def emulation_bgp_route_config_flap_down_time(self, number):
        """
        This is the method the command: emulation_bgp_route_config option flap_down_time
        Description:Supported platforms  Details
            RANGE 1  1000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            During flapping operation, the period expressed in seconds during which the route is withdrawn from its neighbors. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            During flapping operation, the period expressed in seconds during which the route is withdrawn from its neighbors.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: FLAP_DOWN_TIME_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        number --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.FLAP_DOWN_TIME_CMD: number})

    def emulation_bgp_route_config_flap_up_time(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option flap_up_time
        Description:Supported platforms  Details
            RANGE 1  1000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            During flapping operation, the time between flap cycles, expressed in seconds. During this period, the route range will be up. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            During flapping operation, the time between flap cycles, expressed in seconds. During this period, the route range will be up.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: FLAP_UP_TIME_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.FLAP_UP_TIME_CMD: numeric})

    def emulation_bgp_route_config_handle(self, any):
        """
        This is the method the command: emulation_bgp_route_config option handle
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Valid values are:BGP router handle - handle is returned by procedure emulation_bgp_config. A new route will be added when -mode is add.BGP route handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. Valid only for mode remove. The object will be removed.BGP L2Site handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. When mode is remove the L2Site will be removed. When mode is add a new label block will be added to the provided L2Site.BGP L3Site handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. When mode is remove the L3Site will be removed. When mode is add a new vpn route range will be added to the provided L3Site.

            DEFAULT
             None

            IxNetwork-NGPF [M]


            DESCRIPTION


            Valid values are: BGP router handle - handle is returned by procedure emulation_bgp_config. A new route will be added when -mode is add. BGP route handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. Valid only for mode remove. The object will be removed. BGP L2Site handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. When mode is remove the L2Site will be removed. When mode is add a new label block will be added to the provided L2Site. BGP L3Site handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. When mode is remove the L3Site will be removed. When mode is add a new vpn route range will be added to the provided L3Site.

            DEFAULT
             None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.HANDLE_CMD: any})

    def emulation_bgp_route_config_import_rd_as_rt(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option import_rd_as_rt
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Use RD As RT

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: IMPORT_RD_AS_RT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IMPORT_RD_AS_RT_CMD: bool})

    def emulation_bgp_route_config_import_rt_as_export_rt(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option import_rt_as_export_rt
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Import RT List Same As Export RT List

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IMPORT_RT_AS_EXPORT_RT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IMPORT_RT_AS_EXPORT_RT_CMD: bool})

    def emulation_bgp_route_config_import_target(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option import_target
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            AS number or IP address list based on the -import_target_type list. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            AS number or IP address list based on the -import_target_type list.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IMPORT_TARGET_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IMPORT_TARGET_CMD: ip_or_numeric})

    def emulation_bgp_route_config_import_target_assign(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option import_target_assign
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The assigned number subfield of the value field of the import target. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the import target. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The assigned number subfield of the value field of the import target. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the import target.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IMPORT_TARGET_ASSIGN_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IMPORT_TARGET_ASSIGN_CMD: numeric})

    def emulation_bgp_route_config_import_target_assign_inner_step(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option import_target_assign_inner_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base import target assigned number field when -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base import target assigned number field when -target_count is greater than 1.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IMPORT_TARGET_ASSIGN_INNER_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.IMPORT_TARGET_ASSIGN_INNER_STEP_CMD: numeric})

    def emulation_bgp_route_config_import_target_assign_step(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option import_target_assign_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base import target assigned number field. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base import target assigned number field. Not supported reason: legacy item

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IMPORT_TARGET_ASSIGN_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.IMPORT_TARGET_ASSIGN_STEP_CMD: numeric})

    def emulation_bgp_route_config_import_target_count(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option import_target_count
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Number of RTs in Import Route Target List

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IMPORT_TARGET_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IMPORT_TARGET_COUNT_CMD: numeric})

    def emulation_bgp_route_config_import_target_inner_step(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option import_target_inner_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base import target field when -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base import target field when -target_count is greater than 1.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IMPORT_TARGET_INNER_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.IMPORT_TARGET_INNER_STEP_CMD: ip_or_numeric})

    def emulation_bgp_route_config_import_target_step(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option import_target_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base import target field. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base import target field. Not supported reason: legacy item

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IMPORT_TARGET_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IMPORT_TARGET_STEP_CMD: ip_or_numeric})

    def emulation_bgp_route_config_import_target_type(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option import_target_type
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            List of the import target type. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            List of the import target type.

            Valid options are:

            as


            Import target type is AS

            ip


            Import target type is IP

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IMPORT_TARGET_TYPE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IMPORT_TARGET_TYPE_CMD: opt})

    def emulation_bgp_route_config_import_vpls_id_as_rd(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option import_vpls_id_as_rd
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Use VPLS ID As Route Distinguisher

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: IMPORT_VPLS_ID_AS_RD_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IMPORT_VPLS_ID_AS_RD_CMD: bool})

    def emulation_bgp_route_config_ip_address_vpls_id(self, any):
        """
        This is the method the command: emulation_bgp_route_config option ip_address_vpls_id
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            VPLS ID IP Address

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: IP_ADDRESS_VPLS_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IP_ADDRESS_VPLS_ID_CMD: any})

    def emulation_bgp_route_config_ip_address_vpls_rd(self, any):
        """
        This is the method the command: emulation_bgp_route_config option ip_address_vpls_rd
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Route Distinguisher IP Address

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: IP_ADDRESS_VPLS_RD_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IP_ADDRESS_VPLS_RD_CMD: any})

    def emulation_bgp_route_config_ip_address_vpls_rt(self, any):
        """
        This is the method the command: emulation_bgp_route_config option ip_address_vpls_rt
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Route Target IP Address

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: IP_ADDRESS_VPLS_RT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IP_ADDRESS_VPLS_RT_CMD: any})

    def emulation_bgp_route_config_ip_version(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option ip_version
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The IP version of the BGP route to be created. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            Valid options are:

            4


            IPv4

            6


            IPv6

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The IP version of the BGP route to be created.

            Valid options are:

            4


            Bgp version 4

            6


            Bgp version 6

            DEFAULT


            4

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IP_VERSION_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IP_VERSION_CMD: opt})

    def emulation_bgp_route_config_ipv4_mpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option ipv4_mpls_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Enables the emulation of routes for IPv4 MPLS. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables the emulation of routes for IPv4 MPLS. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None
        Constants Available: IPV4_MPLS_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IPV4_MPLS_NLRI_CMD: flag})

    def emulation_bgp_route_config_ipv4_mpls_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option ipv4_mpls_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Enables the emulation of routes for IPv4 MPLS VPNs. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority. Requires parameter num_sites to be present in order to create VPN route ranges.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables the emulation of routes for IPv4 MPLS VPNs. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority. Requires parameter num_sites to be present in order to create VPN route ranges.

            DEFAULT
             None
        Constants Available: IPV4_MPLS_VPN_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IPV4_MPLS_VPN_NLRI_CMD: flag})

    def emulation_bgp_route_config_ipv4_multicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option ipv4_multicast_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Enables the emulation of routes for IPv4 multicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables the emulation of routes for IPv4 multicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None
        Constants Available: IPV4_MULTICAST_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IPV4_MULTICAST_NLRI_CMD: flag})

    def emulation_bgp_route_config_ipv4_unicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option ipv4_unicast_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Enables the emulation of routes for IPv4 unicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables the emulation of routes for IPv4 unicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None
        Constants Available: IPV4_UNICAST_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IPV4_UNICAST_NLRI_CMD: flag})

    def emulation_bgp_route_config_ipv6_mpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option ipv6_mpls_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Enables the emulation of routes for IPv6 MPLS. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables the emulation of routes for IPv6 MPLS. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None
        Constants Available: IPV6_MPLS_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IPV6_MPLS_NLRI_CMD: flag})

    def emulation_bgp_route_config_ipv6_mpls_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option ipv6_mpls_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Enables the emulation of routes for IPv6 MPLS VPNs. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority. Requires parameter num_sites to be present in order to create VPN route ranges.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables the emulation of routes for IPv6 MPLS VPNs. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority. Requires parameter num_sites to be present in order to create VPN route ranges.

            DEFAULT
             None
        Constants Available: IPV6_MPLS_VPN_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IPV6_MPLS_VPN_NLRI_CMD: flag})

    def emulation_bgp_route_config_ipv6_multicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option ipv6_multicast_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Enables the emulation of routes for IPv6 multicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables the emulation of routes for IPv6 multicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None
        Constants Available: IPV6_MULTICAST_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IPV6_MULTICAST_NLRI_CMD: flag})

    def emulation_bgp_route_config_ipv6_prefix_length(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option ipv6_prefix_length
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.
            RANGE 1  128
            IxNetwork


            DESCRIPTION


            IPv6 mask for the IPv6 routes advertised. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            IPv6 mask for the IPv6 routes advertised.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: IPV6_PREFIX_LENGTH_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IPV6_PREFIX_LENGTH_CMD: numeric})

    def emulation_bgp_route_config_ipv6_unicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option ipv6_unicast_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Enables the emulation of routes for IPv6 unicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables the emulation of routes for IPv6 unicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

            DEFAULT
             None
        Constants Available: IPV6_UNICAST_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.IPV6_UNICAST_NLRI_CMD: flag})

    def emulation_bgp_route_config_l2_enable_vlan(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option l2_enable_vlan
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Enable or disable vlan on this mac range. Valid for route type: VPLS (vpls flag enabled).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enable or disable vlan on this mac range.

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: L2_ENABLE_VLAN_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L2_ENABLE_VLAN_CMD: bool})

    def emulation_bgp_route_config_l2_mac_count(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option l2_mac_count
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Number of mac addresses for this range. Valid for route type: VPLS (vpls flag enabled).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Number of mac addresses for this range.

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: L2_MAC_COUNT_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L2_MAC_COUNT_CMD: numeric})

    def emulation_bgp_route_config_l2_mac_incr(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option l2_mac_incr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Indicates whether the initial mac address gets incremented across the range. Valid for route type: VPLS (vpls flag enabled).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Indicates whether the initial mac address gets incremented across the range. Not supported reason: legacy item

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: L2_MAC_INCR_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L2_MAC_INCR_CMD: bool})

    def emulation_bgp_route_config_l2_start_mac_addr(self, mac):
        """
        This is the method the command: emulation_bgp_route_config option l2_start_mac_addr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Start address for the MAC range. Valid for route type: VPLS (vpls flag enabled).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Start address for the MAC range.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: L2_START_MAC_ADDR_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L2_START_MAC_ADDR_CMD: mac})

    def emulation_bgp_route_config_l2_vlan_id(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option l2_vlan_id
        Description:Supported platforms  Details
            RANGE 0  65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Current vlan id. Valid for route type: VPLS (vpls flag enabled).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Current vlan id.

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: L2_VLAN_ID_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L2_VLAN_ID_CMD: numeric})

    def emulation_bgp_route_config_l2_vlan_id_incr(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option l2_vlan_id_incr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This parameter represents the increment step for vlan id across the ranges.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            This parameter represents the increment step for vlan id across the ranges.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: L2_VLAN_ID_INCR_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L2_VLAN_ID_INCR_CMD: numeric})

    def emulation_bgp_route_config_l2_vlan_incr(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option l2_vlan_incr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Indicates whether the vlan id gets incremented inside the same range.Valid for route type: VPLS (vpls flag enabled).

            Valid options are:

            0 or no_increment


            No Imcrement

            1 or parallel_increment


            Parallel Increment

            2 or inner_first


            Inner First

            3 or outer_first


            Outer First

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Indicates whether the vlan id gets incremented inside the same range.

            Valid options are:

            0


            No increment

            1


            Parallel increment

            2


            Inner first increment

            3


            Outer first increment

            no_increment


            No increment

            parallel_increment


            Parallel increment

            inner_first


            Inner first increment

            outer_first


            Outer first increment

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: L2_VLAN_INCR_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L2_VLAN_INCR_CMD: opt})

    def emulation_bgp_route_config_l2_vlan_priority(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option l2_vlan_priority
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            3-bit user priority field in the VLAN tag.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: L2_VLAN_PRIORITY_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L2_VLAN_PRIORITY_CMD: numeric})

    def emulation_bgp_route_config_l2_vlan_tpid(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option l2_vlan_tpid
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            16-bit Tag Protocol Identifier (TPID) or EtherType in the VLAN tag.

            Valid options are:

            0x8100


            Tunneling vlan protocol id is 0x8100

            0x88a8


            Tunneling vlan protocol id is 0x88a8

            0x9100


            Tunneling vlan protocol id is 0x9100

            0x9200


            Tunneling vlan protocol id is 0x9200

            0x9300


            Tunneling vlan protocol id is 0x9300

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: L2_VLAN_TPID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L2_VLAN_TPID_CMD: opt})

    def emulation_bgp_route_config_l3_site_handle(self, any):
        """
        This is the method the command: emulation_bgp_route_config option l3_site_handle
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The handle of the L3 VPN Site where to take action. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri); and mode remove.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The handle of the L3 VPN Site where to take action.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'mode' | value= 'remove' |
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: L3_SITE_HANDLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.L3_SITE_HANDLE_CMD: any})

    def emulation_bgp_route_config_label_block_offset(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option label_block_offset
        Description:Supported platforms  Details
            RANGE 0  65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The offset of the label block. Valid for route type: VPLS (vpls flag enabled).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The offset of the label block.

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: LABEL_BLOCK_OFFSET_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.LABEL_BLOCK_OFFSET_CMD: numeric})

    def emulation_bgp_route_config_label_block_offset_type(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option label_block_offset_type
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Type of the -label_block_offset parameter. Default value is single_value.Valid for route type: vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Type of the -label_block_offset parameter. Default value is single_value.

            Valid options are:

            list


            Specifies that the label_block_offset parameter is a list and shouldnt be multiplied

            single_value


            Specifies that the label_block_offset parameter is a single value and should be used a number of times equal to max_route_ranges

            DEFAULT


            single_value

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: LABEL_BLOCK_OFFSET_TYPE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.LABEL_BLOCK_OFFSET_TYPE_CMD: opt})

    def emulation_bgp_route_config_label_id(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option label_id
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            The identifier for the label space. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The identifier for the label space.

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: LABEL_ID_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.LABEL_ID_CMD: numeric})

    def emulation_bgp_route_config_label_incr_mode(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option label_incr_mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Method in which the MPLS label of an IPv4 MPLS-VPN route will be Valid for route type: mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            Valid options are:

            fixed


            Fixed MPLS label for all RDs

            rd


            Increment label per RD

            prefix


            Increment label per prefix advertised

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Method in which the MPLS label of an IPv4 MPLS-VPN route will be incremented.

            Valid options are:

            fixed


            Fixed MPLS label for all RDs

            rd


            Increment label per RD. Not used in NGPF

            prefix


            Increment label per prefix advertised

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: LABEL_INCR_MODE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.LABEL_INCR_MODE_CMD: opt})

    def emulation_bgp_route_config_label_step(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option label_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value used to step the base label. Valid for route type: mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value used to step the base label.

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: LABEL_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.LABEL_STEP_CMD: numeric})

    def emulation_bgp_route_config_label_value(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option label_value
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Starting value for the label of the BGP route. Default is 16. Valid for route type: mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Starting value for the label of the BGP route. Default is 16.

            DEFAULT


            16

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: LABEL_VALUE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.LABEL_VALUE_CMD: numeric})

    def emulation_bgp_route_config_label_value_end(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option label_value_end
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Ending value for the label of the BGP route. If this parameter is not provided it will be calculated as label_value + num_routes * label_step. Valid for route type: mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).Valid only for IxTclNetwork.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Ending value for the label of the BGP route. If this parameter is not provided it will be calculated as label_value + num_routes * label_step.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: LABEL_VALUE_END_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.LABEL_VALUE_END_CMD: numeric})

    def emulation_bgp_route_config_label_value_type(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option label_value_type
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Type of the -label_value parameter. If this parameter is set to list ""-label_value_step"" is ignored. Default value is single_value.Valid for route type: vpls (vpls)

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Type of the -label_value parameter. If this parameter is set to list ""-label_value_step"" is ignored. Default value is single_value.

            Valid options are:

            list


            Specifies that the label_value parameter is a list and shouldnt be multiplied

            single_value


            Specifies that the label_value parameter is a single value and should be used a number of times equal to max_route_ranges

            DEFAULT


            single_value

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: LABEL_VALUE_TYPE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.LABEL_VALUE_TYPE_CMD: opt})

    def emulation_bgp_route_config_local_pref(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option local_pref
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies the LOCAL_PREF path attribute, which is a discretionary attribute used by a BGP speaker to inform other BGP speakers in its own AS of the originating speakers degree of preference for an advertised route. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the LOCAL_PREF path attribute, which is a discretionary attribute used by a BGP speaker to inform other BGP speakers in its own AS of the originating speakers degree of preference for an advertised route.

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: LOCAL_PREF_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.LOCAL_PREF_CMD: numeric})

    def emulation_bgp_route_config_max_route_ranges(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option max_route_ranges
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The number of route ranges, mpls route ranges, vpn routes to create under the BGP neighbor or the number of label blocks to create under the BGP neighbor when VPLS is enabled.Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The number of route ranges, mpls route ranges, vpn routes to create under the BGP neighbor or the number of label blocks to create under the BGP neighbor when VPLS is enabled.

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: MAX_ROUTE_RANGES_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.MAX_ROUTE_RANGES_CMD: numeric})

    def emulation_bgp_route_config_mode(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT [M]


            Same as IxNetwork.

            IxNetwork [M]


            DESCRIPTION


            Specifies either addition or removal of routes from emulated nodes BGP table.Valid for all route types.

            DEFAULT
             None

            IxNetwork-NGPF [M]


            DESCRIPTION


            Specifies either addition or removal of routes from emulated nodes BGP table.

            Valid options are:

            add


            Add a new unicast, vpn or ip BGP route. Can also add L3 Sites, L2 Sites, L2 Site LabelBlocks, AD VPLS. (legacy alias)

            create


            Add a new unicast, vpn or ip BGP route. Can also add L3 Sites, L2 Sites, L2 Site LabelBlocks, AD VPLS.

            enable


            Enables the given BGP route handle.

            disable


            Disables the given BGP route handle.

            modify


            Modify the given BGP route handle.

            remove


            Remove the given BGP route handle. (legacy alias)

            delete


            Remove the given BGP route handle.

            DEFAULT
             None
        Constants Available: MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.MODE_CMD: opt})

    def emulation_bgp_route_config_mtu(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option mtu
        Description:Supported platforms  Details
            RANGE 0  65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Maximum transmit unit. Has to be in concordance with the DUT settings. Valid for route type: VPLS (vpls flag enabled).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Maximum transmit unit. Has to be in concordance with the DUT settings.

            DEFAULT


            1500

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: MTU_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.MTU_CMD: numeric})

    def emulation_bgp_route_config_multi_exit_disc(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option multi_exit_disc
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies the multi-exit discriminator, which is an optional non-transitive path attribute. The value of this attribute may be used by a BGP speakers decision process to discriminate among multiple exit points to a neighboring AS. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the multi-exit discriminator, which is an optional non-transitive path attribute. The value of this attribute may be used by a BGP speakers decision process to discriminate among multiple exit points to a neighboring AS.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: MULTI_EXIT_DISC_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.MULTI_EXIT_DISC_CMD: numeric})

    def emulation_bgp_route_config_netmask(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option netmask
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Netmask of the advertised routes. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Netmask of the advertised routes.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: NETMASK_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NETMASK_CMD: ip})

    def emulation_bgp_route_config_next_hop(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option next_hop
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies a mandatory path attribute that defines the IP address of the border router that should be used as the next hop to the destinations listed in the Network Layer Reachability field of the UPDATE message. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies a mandatory path attribute that defines the IP address of the border router that should be used as the next hop to the destinations listed in the Network Layer Reachability field of the UPDATE message.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: NEXT_HOP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NEXT_HOP_CMD: ip})

    def emulation_bgp_route_config_next_hop_enable(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option next_hop_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            A flag to enable the generation of a NEXT HOP attribute. Can be used as a flag of a choice of 0 or 1. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            A flag to enable the generation of a NEXT HOP attribute. Can be used as a flag of a choice of 0 or 1.

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: NEXT_HOP_ENABLE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NEXT_HOP_ENABLE_CMD: bool})

    def emulation_bgp_route_config_next_hop_ip_version(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option next_hop_ip_version
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The type of IP address in nextHopIpAddress. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            Valid options are:

            4


            IPv4

            6


            IPv6

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The type of IP address in nextHopIpAddress.

            Valid options are:

            4


            Ipv4 next hop address

            6


            Ipv6 next hop address

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: NEXT_HOP_IP_VERSION_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NEXT_HOP_IP_VERSION_CMD: opt})

    def emulation_bgp_route_config_next_hop_ipv4(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option next_hop_ipv4
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Specifies a mandatory path attribute that defines the IP address of the border router that should be used as the next hop to the destinations listed in the Network Layer Reachability field of the UPDATE message. Has priority over the legacy -next_hop parameter.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: NEXT_HOP_IPV4_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NEXT_HOP_IPV4_CMD: ip})

    def emulation_bgp_route_config_next_hop_ipv6(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option next_hop_ipv6
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Specifies a mandatory path attribute that defines the IP address of the border router that should be used as the next hop to the destinations listed in the Network Layer Reachability field of the UPDATE message. Has priority over the legacy -next_hop parameter.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: NEXT_HOP_IPV6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NEXT_HOP_IPV6_CMD: ip})

    def emulation_bgp_route_config_next_hop_mode(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option next_hop_mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.

            Valid options are:

            fixed


            Fixed next hop mode

            increment


            Increment next hop mode

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: NEXT_HOP_MODE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NEXT_HOP_MODE_CMD: opt})

    def emulation_bgp_route_config_next_hop_set_mode(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option next_hop_set_mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Indicates how to set the next hop IP address. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            Valid options are:

            same


            (default) Will set the value as the local IP address.

            manual


            The value is read from -next_hop_ip_address.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Indicates how to set the next hop IP address.

            Valid options are:

            same


            Will set the value as the local IP address

            manual


            The value is read from -next_hop_ip_address

            DEFAULT


            same

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: NEXT_HOP_SET_MODE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NEXT_HOP_SET_MODE_CMD: opt})

    def emulation_bgp_route_config_no_write(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option no_write
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            DESCRIPTION


            If this option is present, the configuration is not written to the hardware. This option can be used to queue up multiple configurations before writing to the hardware. The option is valid only for IxTclProtocol API.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If this option is present, the configuration is not written to the hardware. This option can be used to queue up multiple configurations before writing to the hardware.

            DEFAULT
             None
        Constants Available: NO_WRITE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NO_WRITE_CMD: flag})

    def emulation_bgp_route_config_num_labels(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option num_labels
        Description:Supported platforms  Details
            RANGE 1  65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies the number of labels to be created for the current label block. Valid for route type: vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the number of labels to be created for the current label block.

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: NUM_LABELS_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NUM_LABELS_CMD: numeric})

    def emulation_bgp_route_config_num_labels_type(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option num_labels_type
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Type of the -num_labels parameter. Default value is single_value.Valid for route type: vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Type of the -num_labels parameter. Default value is single_value.

            Valid options are:

            list


            Specifies that the num_labels parameter is a list and shouldnt be multiplied

            single_value


            Specifies that the num_labels parameter is a single value and should be used a number of times equal to max_route_ranges

            DEFAULT


            single_value

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: NUM_LABELS_TYPE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NUM_LABELS_TYPE_CMD: opt})

    def emulation_bgp_route_config_num_routes(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option num_routes
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Number of routes to advertise, using the prefix as the starting prefix and incrementing based upon the -prefix_step and the -netmask arguments. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Number of routes to advertise, using the prefix as the starting prefix and incrementing based upon the -prefix_step and the -netmask arguments.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: NUM_ROUTES_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NUM_ROUTES_CMD: numeric})

    def emulation_bgp_route_config_num_sites(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option num_sites
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Number of L2/L3 VPN sites (PEs) to be created on a BGP neighbor. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Number of L2/L3 VPN sites (PEs) to be created on a BGP neighbor.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: NUM_SITES_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NUM_SITES_CMD: numeric})

    def emulation_bgp_route_config_number_vsi_id(self, any):
        """
        This is the method the command: emulation_bgp_route_config option number_vsi_id
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            VSI ID Number

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: NUMBER_VSI_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.NUMBER_VSI_ID_CMD: any})

    def emulation_bgp_route_config_origin(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option origin
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Selects the value for the ORIGIN path attribute. Note that specifying a path attribute forces the advertised route to be a node route as opposed to a global route.

            Valid options are:igp, egp, incomplete

            Valid for route type:

            unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri),

            mpls (ipv4/6_mpls_nlri),

            vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Selects the value for the ORIGIN path attribute. Note that specifying a path attribute forces the advertised route to be a node route as opposed to a global route.

            Valid options are:

            igp


            Internal

            egp


            External

            incomplete


            Incomplete

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ORIGIN_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ORIGIN_CMD: opt})

    def emulation_bgp_route_config_origin_route_enable(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option origin_route_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            A flag to define whether to enable the origin route or not. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            A flag to define whether to enable the origin route or not.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ORIGIN_ROUTE_ENABLE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ORIGIN_ROUTE_ENABLE_CMD: flag})

    def emulation_bgp_route_config_originator_id(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option originator_id
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Specifies the ORIGINATOR_ID path attribute, which is an optional, non-transitive BGP attribute. It is created by a Route Reflector and carries the ROUTER_ID of the originator of the route in the local AS. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Specifies the ORIGINATOR_ID path attribute, which is an optional, non-transitive BGP attribute. It is created by a Route Reflector and carries the ROUTER_ID of the originator of the route in the local AS.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ORIGINATOR_ID_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ORIGINATOR_ID_CMD: ip})

    def emulation_bgp_route_config_originator_id_enable(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option originator_id_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Enables or disables originator ID on BGP route range. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables or disables originator ID on BGP route range.

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ORIGINATOR_ID_ENABLE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ORIGINATOR_ID_ENABLE_CMD: bool})

    def emulation_bgp_route_config_packing_from(self, nuber):
        """
        This is the method the command: emulation_bgp_route_config option packing_from
        Description:Supported platforms  Details
            RANGE 0  65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range -packing_from to -packing_to. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range -packing_from to -packing_to.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PACKING_FROM_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        nuber --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PACKING_FROM_CMD: nuber})

    def emulation_bgp_route_config_packing_to(self, number):
        """
        This is the method the command: emulation_bgp_route_config option packing_to
        Description:Supported platforms  Details
            RANGE 0  65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range -packing_from to -packing_to. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range -packing_from to -packing_to.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PACKING_TO_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        number --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PACKING_TO_CMD: number})

    def emulation_bgp_route_config_partial_route_flap_from_route_index(self, number):
        """
        This is the method the command: emulation_bgp_route_config option partial_route_flap_from_route_index
        Description:Supported platforms  Details
            RANGE 0  1000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            When partial route flapping is enabled, gives the index of the route from which to start. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            When partial route flapping is enabled, gives the index of the route from which to start.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PARTIAL_ROUTE_FLAP_FROM_ROUTE_INDEX_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        number --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.PARTIAL_ROUTE_FLAP_FROM_ROUTE_INDEX_CMD: number})

    def emulation_bgp_route_config_partial_route_flap_to_route_index(self, number):
        """
        This is the method the command: emulation_bgp_route_config option partial_route_flap_to_route_index
        Description:Supported platforms  Details
            RANGE 0  1000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            When partial route flapping is enabled, gives the index of the route which to end the flap. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            When partial route flapping is enabled, gives the index of the route which to end the flap.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PARTIAL_ROUTE_FLAP_TO_ROUTE_INDEX_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        number --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.PARTIAL_ROUTE_FLAP_TO_ROUTE_INDEX_CMD: number})

    def emulation_bgp_route_config_prefix(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option prefix
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Route prefix to be advertised / removed by emulated BGP node. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Route prefix to be advertised / removed by emulated BGP node.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PREFIX_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PREFIX_CMD: opt})

    def emulation_bgp_route_config_prefix_from(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option prefix_from
        Description:Supported platforms  Details
            RANGE 0  128
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The first prefix length to generate based on the -prefix. -num_routes. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The first prefix length to generate based on the -prefix.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PREFIX_FROM_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PREFIX_FROM_CMD: numeric})

    def emulation_bgp_route_config_prefix_step(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option prefix_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If -num_routes is greater than one, the step interval for the next incremented prefix. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If -num_routes is greater than one, the step interval for the next incremented prefix. Not supported reason: legacy item

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PREFIX_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PREFIX_STEP_CMD: numeric})

    def emulation_bgp_route_config_prefix_step_accross_vrfs(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option prefix_step_accross_vrfs
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            If -target_count is greater than one, the step interval for the next incremented prefix. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If -target_count is greater than one, the step interval for the next incremented prefix. Not supported reason: legacy item

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PREFIX_STEP_ACCROSS_VRFS_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PREFIX_STEP_ACCROSS_VRFS_CMD: ip})

    def emulation_bgp_route_config_prefix_step_across_vrfs(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option prefix_step_across_vrfs
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            The step interval for the next increment prefix when crossing vrfs. Not supported reason: legacy item

            DEFAULT
             Not supported

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PREFIX_STEP_ACROSS_VRFS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PREFIX_STEP_ACROSS_VRFS_CMD: ip})

    def emulation_bgp_route_config_prefix_to(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option prefix_to
        Description:Supported platforms  Details
            RANGE 0  128
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The last prefix length to generate based on the -prefix. -num_routes. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The last prefix length to generate based on the -prefix. Not supported reason: legacy item

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: PREFIX_TO_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PREFIX_TO_CMD: numeric})

    def emulation_bgp_route_config_protocol_name(self, string):
        """
        This is the method the command: emulation_bgp_route_config option protocol_name
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            This is the name of the protocol stack as it appears in the GUI.

            DEFAULT
             None
        Constants Available: PROTOCOL_NAME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        string --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PROTOCOL_NAME_CMD: string})

    def emulation_bgp_route_config_protocol_route_name(self, string):
        """
        This is the method the command: emulation_bgp_route_config option protocol_route_name
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            This is the name of the protocol stack as it appears in the GUI.

            DEFAULT
             None
        Constants Available: PROTOCOL_ROUTE_NAME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        string --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.PROTOCOL_ROUTE_NAME_CMD: string})

    def emulation_bgp_route_config_rd_admin_step(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_admin_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base route distinguisher administrator field.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base route distinguisher administrator field. Not supported reason: legacy item

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: RD_ADMIN_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.RD_ADMIN_STEP_CMD: ip_or_numeric})

    def emulation_bgp_route_config_rd_admin_value(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_admin_value
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Starting value of the administrator field of the route distinguisher.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Starting value of the administrator field of the route distinguisher.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: RD_ADMIN_VALUE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.RD_ADMIN_VALUE_CMD: ip_or_numeric})

    def emulation_bgp_route_config_rd_admin_value_step(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_admin_value_step
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Inner increment value to step the base route distinguisher administrator field. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Inner increment value to step the base route distinguisher administrator field.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: RD_ADMIN_VALUE_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.RD_ADMIN_VALUE_STEP_CMD: ip_or_numeric})

    def emulation_bgp_route_config_rd_admin_value_step_across_vrfs(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_admin_value_step_across_vrfs
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Outer increment value to step the base route distinguisher administrator field if -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Outer increment value to step the base route distinguisher administrator field if -target_count is greater than 1. Not supported reason: legacy item

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: RD_ADMIN_VALUE_STEP_ACROSS_VRFS_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.RD_ADMIN_VALUE_STEP_ACROSS_VRFS_CMD: ip_or_numeric})

    def emulation_bgp_route_config_rd_assign_step(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_assign_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base route distinguisher assigned number field.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base route distinguisher assigned number field. Not supported reason: legacy item

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: RD_ASSIGN_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.RD_ASSIGN_STEP_CMD: numeric})

    def emulation_bgp_route_config_rd_assign_value(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_assign_value
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Starting value of the assigned number field of the route distinguisher.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Starting value of the assigned number field of the route distinguisher.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: RD_ASSIGN_VALUE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.RD_ASSIGN_VALUE_CMD: numeric})

    def emulation_bgp_route_config_rd_assign_value_step(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_assign_value_step
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Inner increment value to step the base route distinguisher assigned number field if -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Inner increment value to step the base route distinguisher assigned number field if -target_count is greater than 1.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: RD_ASSIGN_VALUE_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.RD_ASSIGN_VALUE_STEP_CMD: numeric})

    def emulation_bgp_route_config_rd_assign_value_step_across_vrfs(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_assign_value_step_across_vrfs
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Outer increment value to step the base route distinguisher assigned number field if -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Outer increment value to step the base route distinguisher assigned number field if -target_count is greater than 1. Not supported reason: legacy item

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: RD_ASSIGN_VALUE_STEP_ACROSS_VRFS_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config(
            {EmulationBgpRouteConfigConstants.RD_ASSIGN_VALUE_STEP_ACROSS_VRFS_CMD: numeric})

    def emulation_bgp_route_config_rd_count(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_count
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            The number of route distinguisher values in a VRF range. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

            DEFAULT


            1

            IxNetwork-NGPF


            DESCRIPTION


            The number of route distinguisher values in a VRF range. Not supported reason: legacy item

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: RD_COUNT_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.RD_COUNT_CMD: numeric})

    def emulation_bgp_route_config_rd_count_per_vrf(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option rd_count_per_vrf
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            The number of times that the increment step is used per VRF.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

            DEFAULT


            1

            IxNetwork-NGPF


            DESCRIPTION


            The number of times that the increment step is used per VRF. Not supported reason: legacy item

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: RD_COUNT_PER_VRF_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.RD_COUNT_PER_VRF_CMD: numeric})

    def emulation_bgp_route_config_rd_type(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option rd_type
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Route distinguisher type. The meaning of the indexes is:0 - AS ; 1 - IP ; 2 - 4 byte AS.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Route distinguisher type.

            Valid options are:

            0


            2 byte AS route distinguisher type

            1


            IP route distinguisher type

            2


            4 byte AS route distinguisher type

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: RD_TYPE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.RD_TYPE_CMD: opt})

    def emulation_bgp_route_config_route_handle(self, any):
        """
        This is the method the command: emulation_bgp_route_config option route_handle
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The handle of the BGP route where to take action. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The handle of the BGP route where to take action.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ROUTE_HANDLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ROUTE_HANDLE_CMD: any})

    def emulation_bgp_route_config_route_ip_addr_step(self, ip):
        """
        This is the method the command: emulation_bgp_route_config option route_ip_addr_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            IP address increment step between the multiple route ranges created under the BGP neighbor, based on -max_route_ranges. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            IP address increment step between the multiple route ranges created under the BGP neighbor, based on -max_route_ranges.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: ROUTE_IP_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.ROUTE_IP_ADDR_STEP_CMD: ip})

    def emulation_bgp_route_config_seq_delivery_enable(self, bool):
        """
        This is the method the command: emulation_bgp_route_config option seq_delivery_enable
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Enable Sequenced Delivery

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: SEQ_DELIVERY_ENABLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.SEQ_DELIVERY_ENABLE_CMD: bool})

    def emulation_bgp_route_config_site_id(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option site_id
        Description:Supported platforms  Details
            RANGE 0  65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The current L2 site identifier. Valid for route type: vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The current L2 site identifier.

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: SITE_ID_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.SITE_ID_CMD: numeric})

    def emulation_bgp_route_config_site_id_step(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option site_id_step
        Description:Supported platforms  Details
            RANGE 0  65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment for the L2 site identifier.Valid for route type: vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment for the L2 site identifier.

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: SITE_ID_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.SITE_ID_STEP_CMD: numeric})

    def emulation_bgp_route_config_target(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option target
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            AS number or IP address list based on the -target_type list.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            AS number or IP address list based on the -target_type list.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: TARGET_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TARGET_CMD: ip_or_numeric})

    def emulation_bgp_route_config_target_assign(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option target_assign
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The assigned number subfield of the value field of the target. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the target.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The assigned number subfield of the value field of the target. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the target.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: TARGET_ASSIGN_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TARGET_ASSIGN_CMD: numeric})

    def emulation_bgp_route_config_target_assign_inner_step(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option target_assign_inner_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base target assigned number field when -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base target assigned number field when -target_count is greater than 1.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: TARGET_ASSIGN_INNER_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TARGET_ASSIGN_INNER_STEP_CMD: numeric})

    def emulation_bgp_route_config_target_assign_step(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option target_assign_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base target assigned number field.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base target assigned number field.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: TARGET_ASSIGN_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TARGET_ASSIGN_STEP_CMD: numeric})

    def emulation_bgp_route_config_target_count(self, numeric):
        """
        This is the method the command: emulation_bgp_route_config option target_count
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Number of AS number or IP address list based on the -target_type list. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Number of AS number or IP address list based on the -target_type list.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: TARGET_COUNT_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TARGET_COUNT_CMD: numeric})

    def emulation_bgp_route_config_target_inner_step(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option target_inner_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base target field when -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base target field when -target_count is greater than 1.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri' | value= '1' |
        Constants Available: TARGET_INNER_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TARGET_INNER_STEP_CMD: ip_or_numeric})

    def emulation_bgp_route_config_target_step(self, ip_or_numeric):
        """
        This is the method the command: emulation_bgp_route_config option target_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Increment value to step the base target field.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Increment value to step the base target field.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: TARGET_STEP_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        ip_or_numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TARGET_STEP_CMD: ip_or_numeric})

    def emulation_bgp_route_config_target_type(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option target_type
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            List of the target type.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            List of the target type.

            Valid options are:

            as


            AS target type

            ip


            IP target type

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |
        Constants Available: TARGET_TYPE_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TARGET_TYPE_CMD: opt})

    def emulation_bgp_route_config_type_vpls_id(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option type_vpls_id
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            VPLS ID Type

            Valid options are:

            as


            AS VPLS ID type

            ip


            IP VPLS ID type

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: TYPE_VPLS_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TYPE_VPLS_ID_CMD: opt})

    def emulation_bgp_route_config_type_vpls_rd(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option type_vpls_rd
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            RD Type

            Valid options are:

            as


            AS route distinguisher type

            ip


            IP route distinguisher type

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: TYPE_VPLS_RD_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TYPE_VPLS_RD_CMD: opt})

    def emulation_bgp_route_config_type_vpls_rt(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option type_vpls_rt
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            RT Type

            Valid options are:

            as


            AS route target type

            ip


            IP route target type

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: TYPE_VPLS_RT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TYPE_VPLS_RT_CMD: opt})

    def emulation_bgp_route_config_type_vsi_id(self, opt):
        """
        This is the method the command: emulation_bgp_route_config option type_vsi_id
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            VSI ID

            Valid options are:

            concat_pe_addr


            Concatenate PE address

            concat_num


            Concatenate number

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ad_vpls_nlri' | value= '1' |
        Constants Available: TYPE_VSI_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.TYPE_VSI_ID_CMD: opt})

    def emulation_bgp_route_config_vpls(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option vpls
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft.This will enable the L2 Sites.Does not take priority over other flags that enable L3 sites. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            (deprecated) This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. Does not take priority over other flags that enable L3 sites and AD VPLS. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast.

            DEFAULT
             None
        Constants Available: VPLS_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.VPLS_CMD: flag})

    def emulation_bgp_route_config_vpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_route_config option vpls_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. Does not take priority over other flags that enable L3 sites and AD VPLS. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast.

            DEFAULT
             None
        Constants Available: VPLS_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.VPLS_NLRI_CMD: flag})

    def emulation_bgp_route_config_vpn_name(self, alpha):
        """
        This is the method the command: emulation_bgp_route_config option vpn_name
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            VPN Name

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vpls_nlri' | value= '1' |
        Constants Available: VPN_NAME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        alpha --
        return -- pass/fail
        """
        return self.emulation_bgp_route_config({EmulationBgpRouteConfigConstants.VPN_NAME_CMD: alpha})


"""
    This is the Constants class for the command: emulation_bgp_route_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationBgpRouteConfigConstants:
    """
    init function
    """

    def __init__(self):
        pass

    # api reference constant for this api to get it from the device
    EMULATION_BGP_ROUTE_CONFIG_API = "EMULATION_BGP_ROUTE_CONFIG_API"

    ARGUMENTS_CMD = "Arguments"
    # Constant values for ARGUMENTS_CMD
    ARGUMENTS_CONSTANTS = "Constants"

    ACTIVE_CMD = "active"

    AD_VPLS_NLRI_CMD = "ad_vpls_nlri"

    ADVERTISE_LABEL_BLOCK_CMD = "advertise_label_block"

    ADVERTISE_NEXTHOP_AS_V4_CMD = "advertise_nexthop_as_v4"

    AGGREGATOR_CMD = "aggregator"

    AGGREGATOR_AS_CMD = "aggregator_as"

    AGGREGATOR_ID_CMD = "aggregator_id"

    AGGREGATOR_ID_MODE_CMD = "aggregator_id_mode"
    # Constant values for AGGREGATOR_ID_MODE_CMD
    AGGREGATOR_ID_MODE_FIXED = "fixed"
    AGGREGATOR_ID_MODE_INCREMENT = "increment"

    AS_NUMBER_VPLS_ID_CMD = "as_number_vpls_id"

    AS_NUMBER_VPLS_RD_CMD = "as_number_vpls_rd"

    AS_NUMBER_VPLS_RT_CMD = "as_number_vpls_rt"

    AS_PATH_CMD = "as_path"

    AS_PATH_SEGMENT_NUMBERS_CMD = "as_path_segment_numbers"
    # Constant values for AS_PATH_SEGMENT_NUMBERS_CMD
    AS_PATH_SEGMENT_NUMBERS_ANY = "ANY"

    AS_PATH_SEGMENT_TYPE_CMD = "as_path_segment_type"
    # Constant values for AS_PATH_SEGMENT_TYPE_CMD
    AS_PATH_SEGMENT_TYPE_AS_SET_AS_SEQ = "as_set as_seq"
    AS_PATH_SEGMENT_TYPE_AS_CONFED_SET = "as_confed_set"
    AS_PATH_SEGMENT_TYPE_AS_CONFED_SEQ = "as_confed_seq"

    AS_PATH_SET_MODE_CMD = "as_path_set_mode"
    # Constant values for AS_PATH_SET_MODE_CMD
    AS_PATH_SET_MODE_INCLUDE_AS_SEQ = "include_as_seq"
    AS_PATH_SET_MODE_INCLUDE_AS_SEQ_CONF = "include_as_seq_conf"
    AS_PATH_SET_MODE_INCLUDE_AS_SET = "include_as_set"
    AS_PATH_SET_MODE_INCLUDE_AS_SET_CONF = "include_as_set_conf"
    AS_PATH_SET_MODE_NO_INCLUDE = "no_include"
    AS_PATH_SET_MODE_PREPEND_AS = "prepend_as"

    ASSIGNED_NUMBER_VPLS_ID_CMD = "assigned_number_vpls_id"

    ASSIGNED_NUMBER_VPLS_RD_CMD = "assigned_number_vpls_rd"

    ASSIGNED_NUMBER_VPLS_RT_CMD = "assigned_number_vpls_rt"

    ATOMIC_AGGREGATE_CMD = "atomic_aggregate"

    CLUSTER_LIST_CMD = "cluster_list"

    CLUSTER_LIST_ENABLE_CMD = "cluster_list_enable"

    COMMUNITIES_CMD = "communities"

    COMMUNITIES_AS_NUMBER_CMD = "communities_as_number"

    COMMUNITIES_ENABLE_CMD = "communities_enable"

    COMMUNITIES_LAST_TWO_OCTETS_CMD = "communities_last_two_octets"

    COMMUNITIES_TYPE_CMD = "communities_type"
    # Constant values for COMMUNITIES_TYPE_CMD
    COMMUNITIES_TYPE_NO_EXPORT_NO_ADVERTISED = "no_export no_advertised"
    COMMUNITIES_TYPE_NO_EXPORT_SUBCONFED = "no_export_subconfed"
    COMMUNITIES_TYPE_MANUAL = "manual"

    CONTROL_WORD_ENABLE_CMD = "control_word_enable"

    DEFAULT_MDT_IP_CMD = "default_mdt_ip"

    DEFAULT_MDT_IP_INCR_CMD = "default_mdt_ip_incr"

    ENABLE_AGGREGATOR_CMD = "enable_aggregator"

    ENABLE_AS_PATH_CMD = "enable_as_path"

    ENABLE_GENERATE_UNIQUE_ROUTES_CMD = "enable_generate_unique_routes"

    ENABLE_LOCAL_PREF_CMD = "enable_local_pref"

    ENABLE_MED_CMD = "enable_med"

    ENABLE_PARTIAL_ROUTE_FLAP_CMD = "enable_partial_route_flap"

    ENABLE_ROUTE_FLAP_CMD = "enable_route_flap"

    ENABLE_TRADITIONAL_NLRI_CMD = "enable_traditional_nlri"

    END_OF_RIB_CMD = "end_of_rib"

    EXT_COMMUNITIES_CMD = "ext_communities"

    EXT_COMMUNITIES_AS_FOUR_BYTES_CMD = "ext_communities_as_four_bytes"

    EXT_COMMUNITIES_AS_TWO_BYTES_CMD = "ext_communities_as_two_bytes"

    EXT_COMMUNITIES_ASSIGNED_FOUR_BYTES_CMD = "ext_communities_assigned_four_bytes"

    EXT_COMMUNITIES_ASSIGNED_TWO_BYTES_CMD = "ext_communities_assigned_two_bytes"

    EXT_COMMUNITIES_ENABLE_CMD = "ext_communities_enable"

    EXT_COMMUNITIES_IP_CMD = "ext_communities_ip"

    EXT_COMMUNITIES_OPAQUE_DATA_CMD = "ext_communities_opaque_data"

    EXT_COMMUNITIES_SUBTYPE_CMD = "ext_communities_subtype"
    # Constant values for EXT_COMMUNITIES_SUBTYPE_CMD
    EXT_COMMUNITIES_SUBTYPE_ROUTE_TARGET = "route_target"
    EXT_COMMUNITIES_SUBTYPE_ORIGIN = "origin"
    EXT_COMMUNITIES_SUBTYPE_EXTENDED_BANDWIDTH = "extended_bandwidth"

    EXT_COMMUNITIES_TYPE_CMD = "ext_communities_type"
    # Constant values for EXT_COMMUNITIES_TYPE_CMD
    EXT_COMMUNITIES_TYPE_ADMIN_AS_TWO_OCTET = "admin_as_two_octet"
    EXT_COMMUNITIES_TYPE_ADMIN_IP = "admin_ip"
    EXT_COMMUNITIES_TYPE_ADMIN_AS_FOUR_OCTET = "admin_as_four_octet"
    EXT_COMMUNITIES_TYPE_OPAQUE = "opaque"

    FLAP_DELAY_CMD = "flap_delay"

    FLAP_DOWN_TIME_CMD = "flap_down_time"

    FLAP_UP_TIME_CMD = "flap_up_time"

    HANDLE_CMD = "handle"

    IMPORT_RD_AS_RT_CMD = "import_rd_as_rt"

    IMPORT_RT_AS_EXPORT_RT_CMD = "import_rt_as_export_rt"

    IMPORT_TARGET_CMD = "import_target"

    IMPORT_TARGET_ASSIGN_CMD = "import_target_assign"

    IMPORT_TARGET_ASSIGN_INNER_STEP_CMD = "import_target_assign_inner_step"

    IMPORT_TARGET_ASSIGN_STEP_CMD = "import_target_assign_step"

    IMPORT_TARGET_COUNT_CMD = "import_target_count"

    IMPORT_TARGET_INNER_STEP_CMD = "import_target_inner_step"

    IMPORT_TARGET_STEP_CMD = "import_target_step"

    IMPORT_TARGET_TYPE_CMD = "import_target_type"
    # Constant values for IMPORT_TARGET_TYPE_CMD
    IMPORT_TARGET_TYPE_AS = "as"
    IMPORT_TARGET_TYPE_IP = "ip"

    IMPORT_VPLS_ID_AS_RD_CMD = "import_vpls_id_as_rd"

    IP_ADDRESS_VPLS_ID_CMD = "ip_address_vpls_id"

    IP_ADDRESS_VPLS_RD_CMD = "ip_address_vpls_rd"

    IP_ADDRESS_VPLS_RT_CMD = "ip_address_vpls_rt"

    IP_VERSION_CMD = "ip_version"
    # Constant values for IP_VERSION_CMD
    IP_VERSION_4 = "4"
    IP_VERSION_6 = "6"

    IPV4_MPLS_NLRI_CMD = "ipv4_mpls_nlri"

    IPV4_MPLS_VPN_NLRI_CMD = "ipv4_mpls_vpn_nlri"

    IPV4_MULTICAST_NLRI_CMD = "ipv4_multicast_nlri"

    IPV4_UNICAST_NLRI_CMD = "ipv4_unicast_nlri"

    IPV6_MPLS_NLRI_CMD = "ipv6_mpls_nlri"

    IPV6_MPLS_VPN_NLRI_CMD = "ipv6_mpls_vpn_nlri"

    IPV6_MULTICAST_NLRI_CMD = "ipv6_multicast_nlri"

    IPV6_PREFIX_LENGTH_CMD = "ipv6_prefix_length"

    IPV6_UNICAST_NLRI_CMD = "ipv6_unicast_nlri"

    L2_ENABLE_VLAN_CMD = "l2_enable_vlan"

    L2_MAC_COUNT_CMD = "l2_mac_count"

    L2_MAC_INCR_CMD = "l2_mac_incr"

    L2_START_MAC_ADDR_CMD = "l2_start_mac_addr"

    L2_VLAN_ID_CMD = "l2_vlan_id"

    L2_VLAN_ID_INCR_CMD = "l2_vlan_id_incr"

    L2_VLAN_INCR_CMD = "l2_vlan_incr"
    # Constant values for L2_VLAN_INCR_CMD
    L2_VLAN_INCR_0 = "0"
    L2_VLAN_INCR_1 = "1"
    L2_VLAN_INCR_2 = "2"
    L2_VLAN_INCR_3 = "3"
    L2_VLAN_INCR_NO_INCREMENT = "no_increment"
    L2_VLAN_INCR_PARALLEL_INCREMENT = "parallel_increment"
    L2_VLAN_INCR_INNER_FIRST = "inner_first"
    L2_VLAN_INCR_OUTER_FIRST = "outer_first"

    L2_VLAN_PRIORITY_CMD = "l2_vlan_priority"

    L2_VLAN_TPID_CMD = "l2_vlan_tpid"
    # Constant values for L2_VLAN_TPID_CMD
    L2_VLAN_TPID_0X8100 = "0x8100"
    L2_VLAN_TPID_0X88A8 = "0x88a8"
    L2_VLAN_TPID_0X9100 = "0x9100"
    L2_VLAN_TPID_0X9200 = "0x9200"
    L2_VLAN_TPID_0X9300 = "0x9300"

    L3_SITE_HANDLE_CMD = "l3_site_handle"

    LABEL_BLOCK_OFFSET_CMD = "label_block_offset"

    LABEL_BLOCK_OFFSET_TYPE_CMD = "label_block_offset_type"
    # Constant values for LABEL_BLOCK_OFFSET_TYPE_CMD
    LABEL_BLOCK_OFFSET_TYPE_LIST = "list"
    LABEL_BLOCK_OFFSET_TYPE_SINGLE_VALUE = "single_value"

    LABEL_ID_CMD = "label_id"

    LABEL_INCR_MODE_CMD = "label_incr_mode"
    # Constant values for LABEL_INCR_MODE_CMD
    LABEL_INCR_MODE_FIXED = "fixed"
    LABEL_INCR_MODE_RD = "rd"
    LABEL_INCR_MODE_PREFIX = "prefix"

    LABEL_STEP_CMD = "label_step"

    LABEL_VALUE_CMD = "label_value"
    # Constant values for LABEL_VALUE_CMD
    LABEL_VALUE_NUMERIC = "NUMERIC"

    LABEL_VALUE_END_CMD = "label_value_end"

    LABEL_VALUE_TYPE_CMD = "label_value_type"
    # Constant values for LABEL_VALUE_TYPE_CMD
    LABEL_VALUE_TYPE_LIST = "list"
    LABEL_VALUE_TYPE_SINGLE_VALUE = "single_value"

    LOCAL_PREF_CMD = "local_pref"

    MAX_ROUTE_RANGES_CMD = "max_route_ranges"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_ADD = "add"
    MODE_CREATE = "create"
    MODE_MODIFY = "modify"
    MODE_REMOVE = "remove"
    MODE_DELETE = "delete"
    MODE_ENABLE = "enable"
    MODE_DISABLE = "disable"

    MTU_CMD = "mtu"

    MULTI_EXIT_DISC_CMD = "multi_exit_disc"

    NETMASK_CMD = "netmask"

    NEXT_HOP_CMD = "next_hop"

    NEXT_HOP_ENABLE_CMD = "next_hop_enable"

    NEXT_HOP_IP_VERSION_CMD = "next_hop_ip_version"
    # Constant values for NEXT_HOP_IP_VERSION_CMD
    NEXT_HOP_IP_VERSION_4 = "4"
    NEXT_HOP_IP_VERSION_6 = "6"

    NEXT_HOP_IPV4_CMD = "next_hop_ipv4"

    NEXT_HOP_IPV6_CMD = "next_hop_ipv6"

    NEXT_HOP_MODE_CMD = "next_hop_mode"
    # Constant values for NEXT_HOP_MODE_CMD
    NEXT_HOP_MODE_FIXED = "fixed"
    NEXT_HOP_MODE_INCREMENT = "increment"
    NEXT_HOP_MODE_INCREMENTPERPREFIX = "incrementPerPrefix"

    NEXT_HOP_SET_MODE_CMD = "next_hop_set_mode"
    # Constant values for NEXT_HOP_SET_MODE_CMD
    NEXT_HOP_SET_MODE_SAME = "same"
    NEXT_HOP_SET_MODE_MANUAL = "manual"

    NO_WRITE_CMD = "no_write"

    NUM_LABELS_CMD = "num_labels"

    NUM_LABELS_TYPE_CMD = "num_labels_type"
    # Constant values for NUM_LABELS_TYPE_CMD
    NUM_LABELS_TYPE_LIST = "list"
    NUM_LABELS_TYPE_SINGLE_VALUE = "single_value"

    NUM_ROUTES_CMD = "num_routes"

    NUM_SITES_CMD = "num_sites"

    NUMBER_VSI_ID_CMD = "number_vsi_id"

    ORIGIN_CMD = "origin"
    # Constant values for ORIGIN_CMD
    ORIGIN_IGP = "igp"
    ORIGIN_EGP = "egp"
    ORIGIN_INCOMPLETE = "incomplete"

    ORIGIN_ROUTE_ENABLE_CMD = "origin_route_enable"

    ORIGINATOR_ID_CMD = "originator_id"

    ORIGINATOR_ID_ENABLE_CMD = "originator_id_enable"

    PACKING_FROM_CMD = "packing_from"

    PACKING_TO_CMD = "packing_to"

    PARTIAL_ROUTE_FLAP_FROM_ROUTE_INDEX_CMD = "partial_route_flap_from_route_index"

    PARTIAL_ROUTE_FLAP_TO_ROUTE_INDEX_CMD = "partial_route_flap_to_route_index"

    PREFIX_CMD = "prefix"
    # Constant values for PREFIX_CMD
    PREFIX_IP = "IP"
    PREFIX_ALL = "all"

    PREFIX_FROM_CMD = "prefix_from"

    PREFIX_STEP_CMD = "prefix_step"

    PREFIX_STEP_ACCROSS_VRFS_CMD = "prefix_step_accross_vrfs"
    # Constant values for PREFIX_STEP_ACCROSS_VRFS_CMD
    PREFIX_STEP_ACCROSS_VRFS_IP = "IP"

    PREFIX_STEP_ACROSS_VRFS_CMD = "prefix_step_across_vrfs"

    PREFIX_TO_CMD = "prefix_to"

    PROTOCOL_NAME_CMD = "protocol_name"

    PROTOCOL_ROUTE_NAME_CMD = "protocol_route_name"

    RD_ADMIN_STEP_CMD = "rd_admin_step"

    RD_ADMIN_VALUE_CMD = "rd_admin_value"

    RD_ADMIN_VALUE_STEP_CMD = "rd_admin_value_step"

    RD_ADMIN_VALUE_STEP_ACROSS_VRFS_CMD = "rd_admin_value_step_across_vrfs"

    RD_ASSIGN_STEP_CMD = "rd_assign_step"

    RD_ASSIGN_VALUE_CMD = "rd_assign_value"

    RD_ASSIGN_VALUE_STEP_CMD = "rd_assign_value_step"

    RD_ASSIGN_VALUE_STEP_ACROSS_VRFS_CMD = "rd_assign_value_step_across_vrfs"

    RD_COUNT_CMD = "rd_count"

    RD_COUNT_PER_VRF_CMD = "rd_count_per_vrf"

    RD_TYPE_CMD = "rd_type"
    # Constant values for RD_TYPE_CMD
    RD_TYPE_0 = "0"
    RD_TYPE_1 = "1"
    RD_TYPE_2 = "2"

    ROUTE_HANDLE_CMD = "route_handle"

    ROUTE_IP_ADDR_STEP_CMD = "route_ip_addr_step"
    # Constant values for ROUTE_IP_ADDR_STEP_CMD
    ROUTE_IP_ADDR_STEP_IP = "IP"

    SEQ_DELIVERY_ENABLE_CMD = "seq_delivery_enable"

    SITE_ID_CMD = "site_id"

    SITE_ID_STEP_CMD = "site_id_step"

    TARGET_CMD = "target"

    TARGET_ASSIGN_CMD = "target_assign"

    TARGET_ASSIGN_INNER_STEP_CMD = "target_assign_inner_step"

    TARGET_ASSIGN_STEP_CMD = "target_assign_step"

    TARGET_COUNT_CMD = "target_count"

    TARGET_INNER_STEP_CMD = "target_inner_step"

    TARGET_STEP_CMD = "target_step"

    TARGET_TYPE_CMD = "target_type"
    # Constant values for TARGET_TYPE_CMD
    TARGET_TYPE_AS = "as"
    TARGET_TYPE_IP = "ip"

    TYPE_VPLS_ID_CMD = "type_vpls_id"
    # Constant values for TYPE_VPLS_ID_CMD
    TYPE_VPLS_ID_AS = "as"
    TYPE_VPLS_ID_IP = "ip"

    TYPE_VPLS_RD_CMD = "type_vpls_rd"
    # Constant values for TYPE_VPLS_RD_CMD
    TYPE_VPLS_RD_AS = "as"
    TYPE_VPLS_RD_IP = "ip"

    TYPE_VPLS_RT_CMD = "type_vpls_rt"
    # Constant values for TYPE_VPLS_RT_CMD
    TYPE_VPLS_RT_AS = "as"
    TYPE_VPLS_RT_IP = "ip"

    TYPE_VSI_ID_CMD = "type_vsi_id"
    # Constant values for TYPE_VSI_ID_CMD
    TYPE_VSI_ID_CONCAT_PE_ADDR = "concat_pe_addr"
    TYPE_VSI_ID_CONCAT_NUM = "concat_num"

    VPLS_CMD = "vpls"

    VPLS_NLRI_CMD = "vpls_nlri"

    VPN_NAME_CMD = "vpn_name"
    # Constant values for VPN_NAME_CMD
    VPN_NAME_ALPHA = "ALPHA"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


# instantiate the class to access the constants
#   example EmulationBgpRouteConfigConstants.ARGUMENTS
EmulationBgpRouteConfigConstants = EmulationBgpRouteConfigConstants()

"""
Implemented Commands (Alphabetical)
    -Arguments
    -active
    -ad_vpls_nlri
    -advertise_label_block
    -advertise_nexthop_as_v4
    -aggregator
    -aggregator_as
    -aggregator_id
    -aggregator_id_mode
    -as_number_vpls_id
    -as_number_vpls_rd
    -as_number_vpls_rt
    -as_path
    -as_path_segment_numbers
    -as_path_segment_type
    -as_path_set_mode
    -assigned_number_vpls_id
    -assigned_number_vpls_rd
    -assigned_number_vpls_rt
    -atomic_aggregate
    -cluster_list
    -cluster_list_enable
    -communities
    -communities_as_number
    -communities_enable
    -communities_last_two_octets
    -communities_type
    -control_word_enable
    -default_mdt_ip
    -default_mdt_ip_incr
    -enable_aggregator
    -enable_as_path
    -enable_generate_unique_routes
    -enable_local_pref
    -enable_med
    -enable_partial_route_flap
    -enable_route_flap
    -enable_traditional_nlri
    -end_of_rib
    -ext_communities
    -ext_communities_as_four_bytes
    -ext_communities_as_two_bytes
    -ext_communities_assigned_four_bytes
    -ext_communities_assigned_two_bytes
    -ext_communities_enable
    -ext_communities_ip
    -ext_communities_opaque_data
    -ext_communities_subtype
    -ext_communities_type
    -flap_delay
    -flap_down_time
    -flap_up_time
    -handle
    -import_rd_as_rt
    -import_rt_as_export_rt
    -import_target
    -import_target_assign
    -import_target_assign_inner_step
    -import_target_assign_step
    -import_target_count
    -import_target_inner_step
    -import_target_step
    -import_target_type
    -import_vpls_id_as_rd
    -ip_address_vpls_id
    -ip_address_vpls_rd
    -ip_address_vpls_rt
    -ip_version
    -ipv4_mpls_nlri
    -ipv4_mpls_vpn_nlri
    -ipv4_multicast_nlri
    -ipv4_unicast_nlri
    -ipv6_mpls_nlri
    -ipv6_mpls_vpn_nlri
    -ipv6_multicast_nlri
    -ipv6_prefix_length
    -ipv6_unicast_nlri
    -l2_enable_vlan
    -l2_mac_count
    -l2_mac_incr
    -l2_start_mac_addr
    -l2_vlan_id
    -l2_vlan_id_incr
    -l2_vlan_incr
    -l2_vlan_priority
    -l2_vlan_tpid
    -l3_site_handle
    -label_block_offset
    -label_block_offset_type
    -label_id
    -label_incr_mode
    -label_step
    -label_value
    -label_value_end
    -label_value_type
    -local_pref
    -max_route_ranges
    -mode
    -mtu
    -multi_exit_disc
    -netmask
    -next_hop
    -next_hop_enable
    -next_hop_ip_version
    -next_hop_ipv4
    -next_hop_ipv6
    -next_hop_mode
    -next_hop_set_mode
    -no_write
    -num_labels
    -num_labels_type
    -num_routes
    -num_sites
    -number_vsi_id
    -origin
    -origin_route_enable
    -originator_id
    -originator_id_enable
    -packing_from
    -packing_to
    -partial_route_flap_from_route_index
    -partial_route_flap_to_route_index
    -prefix
    -prefix_from
    -prefix_step
    -prefix_step_accross_vrfs
    -prefix_step_across_vrfs
    -prefix_to
    -protocol_name
    -protocol_route_name
    -rd_admin_step
    -rd_admin_value
    -rd_admin_value_step
    -rd_admin_value_step_across_vrfs
    -rd_assign_step
    -rd_assign_value
    -rd_assign_value_step
    -rd_assign_value_step_across_vrfs
    -rd_count
    -rd_count_per_vrf
    -rd_type
    -route_handle
    -route_ip_addr_step
    -seq_delivery_enable
    -site_id
    -site_id_step
    -target
    -target_assign
    -target_assign_inner_step
    -target_assign_step
    -target_count
    -target_inner_step
    -target_step
    -target_type
    -type_vpls_id
    -type_vpls_rd
    -type_vpls_rt
    -type_vsi_id
    -vpls
    -vpls_nlri
    -vpn_name

Use this to regenerate this class in the devhelper

<?xml version="1.0" encoding="UTF-8"?>
<xml feature="emulation_bgp_route_config">
  <cmd name="Arguments">
    <description>Description</description>
    <param>Parameter</param>
    <constantlist>Constants</constantlist>
    <supported>Supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="handle">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Valid values are:BGP router handle - handle is returned by procedure emulation_bgp_config. A new route will be added when -mode is add.BGP route handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. Valid only for mode remove. The object will be removed.BGP L2Site handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. When mode is remove the L2Site will be removed. When mode is add a new label block will be added to the provided L2Site.BGP L3Site handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. When mode is remove the L3Site will be removed. When mode is add a new vpn route range will be added to the provided L3Site.

DEFAULT
 None

IxNetwork-NGPF [M]


DESCRIPTION


Valid values are: BGP router handle - handle is returned by procedure emulation_bgp_config. A new route will be added when -mode is add. BGP route handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. Valid only for mode remove. The object will be removed. BGP L2Site handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. When mode is remove the L2Site will be removed. When mode is add a new label block will be added to the provided L2Site. BGP L3Site handle - Valid only for IxNetwork Tcl API (new api). Handle is returned by procedure emulation_bgp_route_config with 'bgp_routes' key. When mode is remove the L3Site will be removed. When mode is add a new vpn route range will be added to the provided L3Site.

DEFAULT
 None</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="route_handle">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The handle of the BGP route where to take action. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The handle of the BGP route where to take action.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="l3_site_handle">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The handle of the L3 VPN Site where to take action. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri); and mode remove.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The handle of the L3 VPN Site where to take action.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'mode' | value= 'remove' |
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT [M]


Same as IxNetwork.

IxNetwork [M]


DESCRIPTION


Specifies either addition or removal of routes from emulated nodes BGP table.Valid for all route types.

DEFAULT
 None

IxNetwork-NGPF [M]


DESCRIPTION


Specifies either addition or removal of routes from emulated nodes BGP table.

Valid options are:

add


Add a new unicast, vpn or ip BGP route. Can also add L3 Sites, L2 Sites, L2 Site LabelBlocks, AD VPLS. (legacy alias)

create


Add a new unicast, vpn or ip BGP route. Can also add L3 Sites, L2 Sites, L2 Site LabelBlocks, AD VPLS.

enable


Enables the given BGP route handle.

disable


Disables the given BGP route handle.

modify


Modify the given BGP route handle.

remove


Remove the given BGP route handle. (legacy alias)

delete


Remove the given BGP route handle.

DEFAULT
 None</description>
    <param>opt</param>
    <constantlist>add,create,modify,remove,delete,enable,disable</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="protocol_name">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


This is the name of the protocol stack as it appears in the GUI.

DEFAULT
 None</description>
    <param>STRING</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="protocol_route_name">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


This is the name of the protocol stack as it appears in the GUI.

DEFAULT
 None</description>
    <param>STRING</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="active">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Activates the item

DEFAULT
 None</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_unicast_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Enables the emulation of routes for IPv4 unicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables the emulation of routes for IPv4 unicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_multicast_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Enables the emulation of routes for IPv4 multicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables the emulation of routes for IPv4 multicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_mpls_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Enables the emulation of routes for IPv4 MPLS. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables the emulation of routes for IPv4 MPLS. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_mpls_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Enables the emulation of routes for IPv4 MPLS VPNs. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority. Requires parameter num_sites to be present in order to create VPN route ranges.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables the emulation of routes for IPv4 MPLS VPNs. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority. Requires parameter num_sites to be present in order to create VPN route ranges.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_unicast_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Enables the emulation of routes for IPv6 unicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables the emulation of routes for IPv6 unicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_multicast_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Enables the emulation of routes for IPv6 multicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables the emulation of routes for IPv6 multicast. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_mpls_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Enables the emulation of routes for IPv6 MPLS. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables the emulation of routes for IPv6 MPLS. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_mpls_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Enables the emulation of routes for IPv6 MPLS VPNs. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority. Requires parameter num_sites to be present in order to create VPN route ranges.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables the emulation of routes for IPv6 MPLS VPNs. Learned routes filter is enabled at neighbor level for IxTclProcol, for IxTclNetwork the filters are set in emulation_bgp_config. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast. Only one of the three route categories can be emulated in a single emulation_bgp_route_config call, the selection is made based on priority. Requires parameter num_sites to be present in order to create VPN route ranges.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="max_route_ranges">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The number of route ranges, mpls route ranges, vpn routes to create under the BGP neighbor or the number of label blocks to create under the BGP neighbor when VPLS is enabled.Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The number of route ranges, mpls route ranges, vpn routes to create under the BGP neighbor or the number of label blocks to create under the BGP neighbor when VPLS is enabled.

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ip_version">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The IP version of the BGP route to be created. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

Valid options are:

4


IPv4

6


IPv6

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The IP version of the BGP route to be created.

Valid options are:

4


Bgp version 4

6


Bgp version 6

DEFAULT


4

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>4,6</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="prefix">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Route prefix to be advertised / removed by emulated BGP node. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Route prefix to be advertised / removed by emulated BGP node.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>IP,all</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="route_ip_addr_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


IP address increment step between the multiple route ranges created under the BGP neighbor, based on -max_route_ranges. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


IP address increment step between the multiple route ranges created under the BGP neighbor, based on -max_route_ranges.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist>IP</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="prefix_step_accross_vrfs">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


If -target_count is greater than one, the step interval for the next incremented prefix. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If -target_count is greater than one, the step interval for the next incremented prefix. Not supported reason: legacy item

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist>IP</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="num_routes">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Number of routes to advertise, using the prefix as the starting prefix and incrementing based upon the -prefix_step and the -netmask arguments. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Number of routes to advertise, using the prefix as the starting prefix and incrementing based upon the -prefix_step and the -netmask arguments.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="num_sites">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Number of L2/L3 VPN sites (PEs) to be created on a BGP neighbor. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Number of L2/L3 VPN sites (PEs) to be created on a BGP neighbor.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="prefix_from">
    <description>Supported platforms  Details
RANGE 0  128
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The first prefix length to generate based on the -prefix. -num_routes. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The first prefix length to generate based on the -prefix.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="prefix_to">
    <description>Supported platforms  Details
RANGE 0  128
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The last prefix length to generate based on the -prefix. -num_routes. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The last prefix length to generate based on the -prefix. Not supported reason: legacy item

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="prefix_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If -num_routes is greater than one, the step interval for the next incremented prefix. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If -num_routes is greater than one, the step interval for the next incremented prefix. Not supported reason: legacy item

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="prefix_step_across_vrfs">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


The step interval for the next increment prefix when crossing vrfs. Not supported reason: legacy item

DEFAULT
 Not supported

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="netmask">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Netmask of the advertised routes. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Netmask of the advertised routes.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_prefix_length">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.
RANGE 1  128
IxNetwork


DESCRIPTION


IPv6 mask for the IPv6 routes advertised. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


IPv6 mask for the IPv6 routes advertised.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="advertise_nexthop_as_v4">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Advertise Nexthop as V4

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="aggregator">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


For the AGGREGATOR path attribute, specifies the last AS number that formed the aggregate route, and the IP address of the BGP speaker that formed the aggregate route. Format: :.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="aggregator_as">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


For the AGGREGATOR path attribute, specifies the last AS number that formed the aggregate route. Has priority over the legacy -aggregator parameter.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMBER</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="aggregator_id">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


For the AGGREGATOR path attribute, specifies the IP address of the BGP speaker that formed the aggregate route. Has priority over the legacy -aggregator parameter.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="aggregator_id_mode">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Aggregator ID Mode

Valid options are:

fixed


Fixed mode

increment


Increment aggregator ID

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>fixed,increment</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="as_path_set_mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


For External routing only. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

Valid options are:

no_include


Don't include Local AS#

include_as_seq


Include Local AS# as AS-SEQ

include_as_set


Include Local AS# as AS-SET

include_as_seq_conf


Include Local AS# as AS-SEQ-Confederation

include_as_set_conf


Include Local AS# as AS-SET-Confederation

prepend_as


Prepend Local AS# to first segment

DEFAULT


include_as_seq

IxNetwork-NGPF


DESCRIPTION


For External routing only. Optional setup for the AS-Path.

Valid options are:

include_as_seq


Include Local AS as AS-SEQ

include_as_seq_conf


Include Local AS as AS-SEQ-Confederation

include_as_set


Include Local AS as AS-SET

include_as_set_conf


Include Local AS as AS-SET-Confederation

no_include


Don't include Local AS

prepend_as


Prepend Local AS to first segment

DEFAULT


include_as_seq

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>include_as_seq,include_as_seq_conf,include_as_set,include_as_set_conf,no_include,prepend_as</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="flap_delay">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Flapping delay

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMBER</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="flap_down_time">
    <description>Supported platforms  Details
RANGE 1  1000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


During flapping operation, the period expressed in seconds during which the route is withdrawn from its neighbors. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


During flapping operation, the period expressed in seconds during which the route is withdrawn from its neighbors.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMBER</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="enable_aggregator">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Enable Aggregator ID

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="enable_as_path">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


This parameter indicates that as_path attributes are to be generated. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


This parameter indicates that as_path attributes are to be generated.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="atomic_aggregate">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies the ATOMIC_AGGREGATE path attribute, which is a discretionary attribute. If set to 1, informs other BGP speakers that the local system selected a less specific route without selecting a more specific route included in it. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies the ATOMIC_AGGREGATE path attribute, which is a discretionary attribute. If set to 1, informs other BGP speakers that the local system selected a less specific route without selecting a more specific route included in it.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="cluster_list_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Enables or disables cluster list on BGP route range.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables or disables cluster list on BGP route range.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="communities_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Enables or disables communities. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables or disables communities.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ext_communities_enable">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Enable Extended Community

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="enable_route_flap">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


FLAG - Enables the flapping functions described by route_flap_up_time, route_flap_down_time, routesToFlapFrom, and routesToFlapTo. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


FLAG - Enables the flapping functions described by route_flap_up_time, route_flap_down_time, routesToFlapFrom, and routesToFlapTo.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="enable_local_pref">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


This attribute inserts a local_pref attribute with the indicated value. (internal bgp only) Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


This attribute inserts a local_pref attribute with the indicated value. (internal bgp only)

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="enable_med">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Enable Multi Exit

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="next_hop_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


A flag to enable the generation of a NEXT HOP attribute. Can be used as a flag of a choice of 0 or 1. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


A flag to enable the generation of a NEXT HOP attribute. Can be used as a flag of a choice of 0 or 1.

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="origin_route_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


A flag to define whether to enable the origin route or not. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


A flag to define whether to enable the origin route or not.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="originator_id_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Enables or disables originator ID on BGP route range. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables or disables originator ID on BGP route range.

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="partial_route_flap_from_route_index">
    <description>Supported platforms  Details
RANGE 0  1000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


When partial route flapping is enabled, gives the index of the route from which to start. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


When partial route flapping is enabled, gives the index of the route from which to start.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMBER</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="partial_route_flap_to_route_index">
    <description>Supported platforms  Details
RANGE 0  1000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


When partial route flapping is enabled, gives the index of the route which to end the flap. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


When partial route flapping is enabled, gives the index of the route which to end the flap.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMBER</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="next_hop">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies a mandatory path attribute that defines the IP address of the border router that should be used as the next hop to the destinations listed in the Network Layer Reachability field of the UPDATE message. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies a mandatory path attribute that defines the IP address of the border router that should be used as the next hop to the destinations listed in the Network Layer Reachability field of the UPDATE message.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="next_hop_ipv4">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Specifies a mandatory path attribute that defines the IP address of the border router that should be used as the next hop to the destinations listed in the Network Layer Reachability field of the UPDATE message. Has priority over the legacy -next_hop parameter.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="next_hop_ipv6">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Specifies a mandatory path attribute that defines the IP address of the border router that should be used as the next hop to the destinations listed in the Network Layer Reachability field of the UPDATE message. Has priority over the legacy -next_hop parameter.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="local_pref">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies the LOCAL_PREF path attribute, which is a discretionary attribute used by a BGP speaker to inform other BGP speakers in its own AS of the originating speakers degree of preference for an advertised route. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies the LOCAL_PREF path attribute, which is a discretionary attribute used by a BGP speaker to inform other BGP speakers in its own AS of the originating speakers degree of preference for an advertised route.

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="multi_exit_disc">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies the multi-exit discriminator, which is an optional non-transitive path attribute. The value of this attribute may be used by a BGP speakers decision process to discriminate among multiple exit points to a neighboring AS. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies the multi-exit discriminator, which is an optional non-transitive path attribute. The value of this attribute may be used by a BGP speakers decision process to discriminate among multiple exit points to a neighboring AS.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="next_hop_mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.

Valid options are:

fixed


Fixed next hop mode

increment


Increment next hop mode

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>fixed,increment,incrementPerPrefix</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="next_hop_ip_version">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The type of IP address in nextHopIpAddress. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

Valid options are:

4


IPv4

6


IPv6

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The type of IP address in nextHopIpAddress.

Valid options are:

4


Ipv4 next hop address

6


Ipv6 next hop address

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>4,6</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="next_hop_set_mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Indicates how to set the next hop IP address. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

Valid options are:

same


(default) Will set the value as the local IP address.

manual


The value is read from -next_hop_ip_address.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Indicates how to set the next hop IP address.

Valid options are:

same


Will set the value as the local IP address

manual


The value is read from -next_hop_ip_address

DEFAULT


same

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>same,manual</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="origin">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Selects the value for the ORIGIN path attribute. Note that specifying a path attribute forces the advertised route to be a node route as opposed to a global route.

Valid options are:igp, egp, incomplete

Valid for route type:

unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri),

mpls (ipv4/6_mpls_nlri),

vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Selects the value for the ORIGIN path attribute. Note that specifying a path attribute forces the advertised route to be a node route as opposed to a global route.

Valid options are:

igp


Internal

egp


External

incomplete


Incomplete

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>igp,egp,incomplete</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="originator_id">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies the ORIGINATOR_ID path attribute, which is an optional, non-transitive BGP attribute. It is created by a Route Reflector and carries the ROUTER_ID of the originator of the route in the local AS. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies the ORIGINATOR_ID path attribute, which is an optional, non-transitive BGP attribute. It is created by a Route Reflector and carries the ROUTER_ID of the originator of the route in the local AS.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="packing_from">
    <description>Supported platforms  Details
RANGE 0  65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range -packing_from to -packing_to. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range -packing_from to -packing_to.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUBER</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="packing_to">
    <description>Supported platforms  Details
RANGE 0  65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range -packing_from to -packing_to. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range -packing_from to -packing_to.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMBER</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="enable_partial_route_flap">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


FLAG - Enable partial flapping functions. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


FLAG - Enable partial flapping functions.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="flap_up_time">
    <description>Supported platforms  Details
RANGE 1  1000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


During flapping operation, the time between flap cycles, expressed in seconds. During this period, the route range will be up. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


During flapping operation, the time between flap cycles, expressed in seconds. During this period, the route range will be up.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="enable_traditional_nlri">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If checked, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)Values: 0 1. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If checked, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="enable_generate_unique_routes">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


FLAG - When set to 1, each router generates a different IP address range. When set to 0, each router advertises the route range as is. When enabled, the first router advertises numRoutes routes starting at networkAddress, the next router advertises numRoutes routes starting at (networkAddress + numRoutes), and so on. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


FLAG - When set to 1, each router generates a different IP address range. When set to 0, each router advertises the route range as is. When enabled, the first router advertises numRoutes routes starting at networkAddress, the next router advertises numRoutes routes starting at (networkAddress + numRoutes), and so on.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="end_of_rib">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Configures BGP End of RIB markerValid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Configures BGP End of RIB marker

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="communities">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies the COMMUNITIES path attribute, which is an optional transitive attribute of variable length. All routes with this attribute belong to the communities listed in the attribute. This is a list of numbers. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies the COMMUNITIES path attribute, which is an optional transitive attribute of variable length. All routes with this attribute belong to the communities listed in the attribute. This is a list of numbers.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="communities_as_number">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Communities AS #

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="communities_last_two_octets">
    <description>upported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Last Two Octets

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="communities_type">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Type

Valid options are:

noexport


No export

noadvertised


No advertised

noexport_subconfed


No export subconfed

manual


Manual AS number

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>no_export no_advertised,no_export_subconfed,manual</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ext_communities">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies the EXTENDED COMMUNITIES path attribute, which is a transitive optional BGP attribute. All routes with the EXTENDED COMMUNITIES attribute belong to the communities listed in the attribute.This is a list of numbers separated by comma char "","" as follows:

The first number is the value of the low-order type byte.

Possible values:

0 - (default)
2 - Route target community
3 - Route origin community
4 - Link bandwidth community

The second number is the value of the high-order type byte.
Possible values:
128 - IANA bit: This bit may be or'd with any other values.
0 indicates that this is an IANA assignable type using First Come First Serve policy.
1 indicates that this is an IANA assignable type using the IETF Consensus policy.
64 - Transitive bit: This bit may be ordered with any other values.
0 indicates that the community is transitive across ASes and
1 indicates that it is non-transitive.
0 - Two-octet AS specific (default): Value holds a two-octet global ASN followed by a four-bytes local admin value.
1 - IPv4 address specific: Value holds a four-octet IP address followed by a two-bytes local administrator value.
2 - Four-octet AS specific: Value holds a four-octet global ASN followed by a two-bytes local admin value.
3 - Generic: Value holds six-octets.

The third number is the value associated with the extended community. (default = {00 00 00 00 00 00})
Example value: {2,128,03 22 00 00 00 00}. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies the EXTENDED COMMUNITIES path attribute, which is a transitive optional BGP attribute. All routes with the EXTENDED COMMUNITIES attribute belong to the communities listed in the attribute. This is a list of numbers separated by comma char "","" as follows: The first number is the value of the low-order type byte. Possible values: 0 - (default) 2 - Route target community 3 - Route origin community 4 - Link bandwidth community The second number is the value of the high-order type byte. Possible values: 128 - IANA bit: This bit may be or'd with any other values. 0 indicates that this is an IANA assignable type using First Come First Serve policy. 1 indicates that this is an IANA assignable type using the IETF Consensus policy. 64 - Transitive bit: This bit may be or'd with any other values. 0 indicates that the community is transitive across ASes and 1 indicates that it is non-transitive. 0 - Two-octet AS specific (default): Value holds a two-octet global ASN followed by a four-bytes local admin value. 1 - IPv4 address specific: Value holds a four-octet IP address followed by a two-bytes local administrator value. 2 - Four-octet AS specific: Value holds a four-octet global ASN followed by a two-bytes local admin value. 3 - Generic: Value holds six-octets. The third number is the value associated with the extended community. (default = {00 00 00 00 00 00}) Example value: {2,128,03 22 00 00 00 00}.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>STRING</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ext_communities_as_two_bytes">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


AS 2-Bytes

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ext_communities_as_four_bytes">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


AS 4-Bytes

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ext_communities_assigned_two_bytes">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Assigned Number(2 Octets)

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ext_communities_assigned_four_bytes">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Assigned Number(4 Octets)

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ext_communities_ip">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


IP

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ext_communities_opaque_data">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Opaque Data

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ext_communities_type">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Type

Valid options are:

administratoras2octet


Admin AS number 2 octet

administratorip


Admin IP address

administratoras4octet


Admin AS number 4 octet

opaque


Opaque data

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>admin_as_two_octet,admin_ip,admin_as_four_octet,opaque</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ext_communities_subtype">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


SubType

Valid options are:

routetarget


Route target

origin


Origin

extendedbandwidth


Extended bandwidth

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>route_target,origin,extended_bandwidth</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="as_path">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies the AS_PATH path attribute, which is a mandatory attribute composed of a sequence of AS path segments.Format: :{as_set|as_seq|as_confed_set|as_confed_seq}:&lt;x,x,x,x&gt;Example:as_set:1,2,3,4as_set - specifies an unordered set of autonomous systems though which a route in the UPDATE message has traversed.as_seq - specifies an ordered set of autonomous systems through which a route in the UPDATE message has traversed.as_confed_set - specifies an unordered set of autonomous systems in the local confederation that the UPDATE message has traversed.as_confed_seq - specifies an ordered set of autonomous systems in the local confederation that the UPDATE message has traversed.DEFAULT = as_set:, where is the AS of the router which advertises this route. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies the AS_PATH path attribute, which is a mandatory attribute composed of a sequence of AS path segments. Format: : {as_set|as_seq|as_confed_set|as_confed_seq}:&lt;x,x,x,x&gt;. Example: as_set:1,2,3,4 as_set - specifies an unordered set of autonomous systems though which a route in the UPDATE message has traversed. as_seq - specifies an ordered set of autonomous systems through which a route in the UPDATE message has traversed. as_confed_set - specifies an unordered set of autonomous systems in the local confederation that the UPDATE message has traversed. as_confed_seq - specifies an ordered set of autonomous systems in the local confederation that the UPDATE message has traversed. DEFAULT = as_set:, where is the AS of the router which advertises this route.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>path</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="as_path_segment_type">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Specifies the segment type for the AS_PATH attribute. This may be a list of values with equal length to the as_path parameter list.

Valid options are:

as_set


AS-SET

as_seq


AS-SEQ

as_confed_set


AS-SET-CONFEDERATION

as_confed_seq


AS-SEQ-CONFEDERATION

DEFAULT


as_set

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>as_set as_seq,as_confed_set,as_confed_seq</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="as_path_segment_numbers">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


A list of lists of AS_PATH segment numbers. The outer list length needs to match as_path_segment_type list length.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist>ANY</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="cluster_list">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies the CLUSTER_LIST path attribute, which is an optional, non-transitive BGP attribute. It is a sequence of CLUSTER_ID values representing the reflection path through which the route has passed. Valid for route type: unicast/multicast (ipv4/6_unicast_nlri, ipv4/6_multicast_nlri), mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies the CLUSTER_LIST path attribute, which is an optional, non-transitive BGP attribute. It is a sequence of CLUSTER_ID values representing the reflection path through which the route has passed.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>STRING</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="vpls">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft.This will enable the L2 Sites.Does not take priority over other flags that enable L3 sites. The priority of the flags is the following VPN (L3 Sites), VPLS (L2 Sites), MPLS, Unicast/Multicast.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


(deprecated) This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. Does not take priority over other flags that enable L3 sites and AD VPLS. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="vpls_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. Does not take priority over other flags that enable L3 sites and AD VPLS. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="rd_admin_value">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Starting value of the administrator field of the route distinguisher.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Starting value of the administrator field of the route distinguisher.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="rd_admin_value_step">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Inner increment value to step the base route distinguisher administrator field. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Inner increment value to step the base route distinguisher administrator field.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="rd_admin_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base route distinguisher administrator field.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base route distinguisher administrator field. Not supported reason: legacy item

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="rd_assign_value">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Starting value of the assigned number field of the route distinguisher.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Starting value of the assigned number field of the route distinguisher.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="rd_assign_value_step">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Inner increment value to step the base route distinguisher assigned number field if -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Inner increment value to step the base route distinguisher assigned number field if -target_count is greater than 1.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="rd_assign_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base route distinguisher assigned number field.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base route distinguisher assigned number field. Not supported reason: legacy item

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="control_word_enable">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Enable Control Word

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="seq_delivery_enable">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Enable Sequenced Delivery

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="mtu">
    <description>Supported platforms  Details
RANGE 0  65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Maximum transmit unit. Has to be in concordance with the DUT settings. Valid for route type: VPLS (vpls flag enabled).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Maximum transmit unit. Has to be in concordance with the DUT settings.

DEFAULT


1500

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="site_id">
    <description>Supported platforms  Details
RANGE 0  65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The current L2 site identifier. Valid for route type: vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The current L2 site identifier.

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="site_id_step">
    <description>Supported platforms  Details
RANGE 0  65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment for the L2 site identifier.Valid for route type: vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment for the L2 site identifier.

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="target">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


AS number or IP address list based on the -target_type list.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


AS number or IP address list based on the -target_type list.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="target_inner_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base target field when -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base target field when -target_count is greater than 1.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="target_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base target field.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base target field.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="target_assign">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The assigned number subfield of the value field of the target. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the target.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The assigned number subfield of the value field of the target. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the target.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="target_assign_inner_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base target assigned number field when -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base target assigned number field when -target_count is greater than 1.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="target_assign_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base target assigned number field.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base target assigned number field.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="rd_type">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Route distinguisher type. The meaning of the indexes is:0 - AS ; 1 - IP ; 2 - 4 byte AS.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Route distinguisher type.

Valid options are:

0


2 byte AS route distinguisher type

1


IP route distinguisher type

2


4 byte AS route distinguisher type

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>0,1,2</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="target_type">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


List of the target type.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


List of the target type.

Valid options are:

as


AS target type

ip


IP target type

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>as,ip</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="vpn_name">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


VPN Name

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>ALPHA</param>
    <constantlist>ALPHA</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="advertise_label_block">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Advertise Label Block

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="num_labels">
    <description>Supported platforms  Details
RANGE 1  65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Specifies the number of labels to be created for the current label block. Valid for route type: vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Specifies the number of labels to be created for the current label block.

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="num_labels_type">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Type of the -num_labels parameter. Default value is single_value.Valid for route type: vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Type of the -num_labels parameter. Default value is single_value.

Valid options are:

list


Specifies that the num_labels parameter is a list and shouldnt be multiplied

single_value


Specifies that the num_labels parameter is a single value and should be used a number of times equal to max_route_ranges

DEFAULT


single_value

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>list,single_value</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="label_block_offset">
    <description>Supported platforms  Details
RANGE 0  65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The offset of the label block. Valid for route type: VPLS (vpls flag enabled).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The offset of the label block.

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="label_block_offset_type">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Type of the -label_block_offset parameter. Default value is single_value.Valid for route type: vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Type of the -label_block_offset parameter. Default value is single_value.

Valid options are:

list


Specifies that the label_block_offset parameter is a list and shouldnt be multiplied

single_value


Specifies that the label_block_offset parameter is a single value and should be used a number of times equal to max_route_ranges

DEFAULT


single_value

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>list,single_value</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="label_value">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Starting value for the label of the BGP route. Default is 16. Valid for route type: mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Starting value for the label of the BGP route. Default is 16.

DEFAULT


16

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist>NUMERIC</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="label_value_type">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Type of the -label_value parameter. If this parameter is set to list ""-label_value_step"" is ignored. Default value is single_value.Valid for route type: vpls (vpls)

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Type of the -label_value parameter. If this parameter is set to list ""-label_value_step"" is ignored. Default value is single_value.

Valid options are:

list


Specifies that the label_value parameter is a list and shouldnt be multiplied

single_value


Specifies that the label_value parameter is a single value and should be used a number of times equal to max_route_ranges

DEFAULT


single_value

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>list,single_value</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="l2_start_mac_addr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Start address for the MAC range. Valid for route type: VPLS (vpls flag enabled).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Start address for the MAC range.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>MAC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="l2_mac_incr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Indicates whether the initial mac address gets incremented across the range. Valid for route type: VPLS (vpls flag enabled).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Indicates whether the initial mac address gets incremented across the range. Not supported reason: legacy item

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="l2_mac_count">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Number of mac addresses for this range. Valid for route type: VPLS (vpls flag enabled).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Number of mac addresses for this range.

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="l2_enable_vlan">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Enable or disable vlan on this mac range. Valid for route type: VPLS (vpls flag enabled).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enable or disable vlan on this mac range.

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_unicast_nlri or ipv4/6_multicast_nlri or ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="l2_vlan_priority">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


3-bit user priority field in the VLAN tag.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="l2_vlan_tpid">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


16-bit Tag Protocol Identifier (TPID) or EtherType in the VLAN tag.

Valid options are:

0x8100


Tunneling vlan protocol id is 0x8100

0x88a8


Tunneling vlan protocol id is 0x88a8

0x9100


Tunneling vlan protocol id is 0x9100

0x9200


Tunneling vlan protocol id is 0x9200

0x9300


Tunneling vlan protocol id is 0x9300

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>0x8100,0x88a8,0x9100,0x9200,0x9300</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="l2_vlan_id">
    <description>Supported platforms  Details
RANGE 0  65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Current vlan id. Valid for route type: VPLS (vpls flag enabled).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Current vlan id.

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="l2_vlan_id_incr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


This parameter represents the increment step for vlan id across the ranges.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


This parameter represents the increment step for vlan id across the ranges.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="l2_vlan_incr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Indicates whether the vlan id gets incremented inside the same range.Valid for route type: VPLS (vpls flag enabled).

Valid options are:

0 or no_increment


No Imcrement

1 or parallel_increment


Parallel Increment

2 or inner_first


Inner First

3 or outer_first


Outer First

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Indicates whether the vlan id gets incremented inside the same range.

Valid options are:

0


No increment

1


Parallel increment

2


Inner first increment

3


Outer first increment

no_increment


No increment

parallel_increment


Parallel increment

inner_first


Inner first increment

outer_first


Outer first increment

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>0,1,2,3,no_increment,parallel_increment,inner_first,outer_first</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="import_rt_as_export_rt">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Import RT List Same As Export RT List

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="target_count">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Number of AS number or IP address list based on the -target_type list. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Number of AS number or IP address list based on the -target_type list.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="import_target_count">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Number of RTs in Import Route Target List

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="default_mdt_ip">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Defines the IP address of the default MDT for mVPN. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Defines the IP address of the default MDT for mVPN.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="default_mdt_ip_incr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Defines the IP address increment for each default MDT. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Defines the IP address increment for each default MDT.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="import_target">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


AS number or IP address list based on the -import_target_type list. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


AS number or IP address list based on the -import_target_type list.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="import_target_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base import target field. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base import target field. Not supported reason: legacy item

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="import_target_inner_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base import target field when -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base import target field when -target_count is greater than 1.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="import_target_assign">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The assigned number subfield of the value field of the import target. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the import target. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The assigned number subfield of the value field of the import target. It is a number from a numbering space which is maintained by the enterprise administers for a given IP address or ASN space. It is the local part of the import target.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="import_target_type">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


List of the import target type. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


List of the import target type.

Valid options are:

as


Import target type is AS

ip


Import target type is IP

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>as,ip</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="import_target_assign_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base import target assigned number field. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base import target assigned number field. Not supported reason: legacy item

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="import_target_assign_inner_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value to step the base import target assigned number field when -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value to step the base import target assigned number field when -target_count is greater than 1.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="rd_count">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


The number of route distinguisher values in a VRF range. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

DEFAULT


1

IxNetwork-NGPF


DESCRIPTION


The number of route distinguisher values in a VRF range. Not supported reason: legacy item

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="rd_count_per_vrf">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


The number of times that the increment step is used per VRF.Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

DEFAULT


1

IxNetwork-NGPF


DESCRIPTION


The number of times that the increment step is used per VRF. Not supported reason: legacy item

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="rd_admin_value_step_across_vrfs">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Outer increment value to step the base route distinguisher administrator field if -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Outer increment value to step the base route distinguisher administrator field if -target_count is greater than 1. Not supported reason: legacy item

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>IP | NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="rd_assign_value_step_across_vrfs">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Outer increment value to step the base route distinguisher assigned number field if -target_count is greater than 1. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Outer increment value to step the base route distinguisher assigned number field if -target_count is greater than 1. Not supported reason: legacy item

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="label_value_end">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Ending value for the label of the BGP route. If this parameter is not provided it will be calculated as label_value + num_routes * label_step. Valid for route type: mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).Valid only for IxTclNetwork.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Ending value for the label of the BGP route. If this parameter is not provided it will be calculated as label_value + num_routes * label_step.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="label_incr_mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Method in which the MPLS label of an IPv4 MPLS-VPN route will be Valid for route type: mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri).

Valid options are:

fixed


Fixed MPLS label for all RDs

rd


Increment label per RD

prefix


Increment label per prefix advertised

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Method in which the MPLS label of an IPv4 MPLS-VPN route will be incremented.

Valid options are:

fixed


Fixed MPLS label for all RDs

rd


Increment label per RD. Not used in NGPF

prefix


Increment label per prefix advertised

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>fixed,rd,prefix</constantlist>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="label_id">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


The identifier for the label space. Valid for route type: vpn (ipv4/6_mpls_vpn_nlri). Valid only for IxTclNetwork.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The identifier for the label space.

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_vpn_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="label_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Increment value used to step the base label. Valid for route type: mpls (ipv4/6_mpls_nlri), vpn (ipv4/6_mpls_vpn_nlri), vpls (vpls).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Increment value used to step the base label.

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4/6_mpls_nlri or ipv4/6_mpls_vpn_nlri or vpls_nlri' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ad_vpls_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


This BGP/BGP+ router/peer supports BGP/BGP+ AD VPLS. Does not take priority over other flags that enable L3 sites. The priority of the flags is the following VPN (L3 Sites), AD VPLS (L2 VPN), VPLS (L2 Sites), MPLS, Unicast/Multicast.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="as_number_vpls_id">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


VPLS ID AS Number

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="as_number_vpls_rd">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Route Distinguisher AS Number

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="as_number_vpls_rt">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Route Target AS Number

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="assigned_number_vpls_id">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


VPLS ID Assigned Number

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="assigned_number_vpls_rd">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Route Distinguisher Assigned Number

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="assigned_number_vpls_rt">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Route Target Assigned Number

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="import_rd_as_rt">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Use RD As RT

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="import_vpls_id_as_rd">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Use VPLS ID As Route Distinguisher

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>BOOL</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ip_address_vpls_id">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


VPLS ID IP Address

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ip_address_vpls_rd">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Route Distinguisher IP Address

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ip_address_vpls_rt">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Route Target IP Address

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="number_vsi_id">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


VSI ID Number

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>ANY</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="type_vpls_id">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


VPLS ID Type

Valid options are:

as


AS VPLS ID type

ip


IP VPLS ID type

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>as, ip</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="type_vpls_rd">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


RD Type

Valid options are:

as


AS route distinguisher type

ip


IP route distinguisher type

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>as,ip</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="type_vpls_rt">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


RT Type

Valid options are:

as


AS route target type

ip


IP route target type

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>as,ip</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="type_vsi_id">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


VSI ID

Valid options are:

concat_pe_addr


Concatenate PE address

concat_num


Concatenate number

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ad_vpls_nlri' | value= '1' |</description>
    <param>opt</param>
    <constantlist>concat_pe_addr,concat_num</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="no_write">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


DESCRIPTION


If this option is present, the configuration is not written to the hardware. This option can be used to queue up multiple configurations before writing to the hardware. The option is valid only for IxTclProtocol API.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If this option is present, the configuration is not written to the hardware. This option can be used to queue up multiple configurations before writing to the hardware.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork, IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
</xml>

"""
