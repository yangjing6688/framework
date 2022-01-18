from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi

"""
    This is the API class for the command: emulation_bgp_config
"""


class EmulationBgpConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        TrafficGenerationApi.__init__(self, device)

    """
    This is the "One Large Method" for the command: emulation_bgp_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationBgpConfigConstants.ARGUMENTS_CMD] = EmulationBgpConfigConstants.ARGUMENTS_CONSTANTS # constant value
        dummyDict[EmulationBgpConfigConstants.ACT_AS_RESTARTED_CMD] = EmulationBgpConfigConstants.ACT_AS_RESTARTED_0 # constant value
        dummyDict[EmulationBgpConfigConstants.ACTIVE_CMD] = EmulationBgpConfigConstants.ACTIVE_0 # constant value
        dummyDict[EmulationBgpConfigConstants.ACTIVE_CONNECT_ENABLE_CMD] = "dummyValue4" # static value
        dummyDict[EmulationBgpConfigConstants.ADVERTISE_END_OF_RIB_CMD] = EmulationBgpConfigConstants.ADVERTISE_END_OF_RIB_0 # constant value
        dummyDict[EmulationBgpConfigConstants.ADVERTISE_HOST_ROUTE_CMD] = "dummyValue6" # static value
        dummyDict[EmulationBgpConfigConstants.ATM_ENCAPSULATION_CMD] = EmulationBgpConfigConstants.ATM_ENCAPSULATION_VCCMUXIPV4ROUTED # constant value
        dummyDict[EmulationBgpConfigConstants.BFD_REGISTRATION_CMD] = EmulationBgpConfigConstants.BFD_REGISTRATION_0 # constant value
        dummyDict[EmulationBgpConfigConstants.BFD_REGISTRATION_MODE_CMD] = EmulationBgpConfigConstants.BFD_REGISTRATION_MODE_SINGLE_HOP # constant value
        dummyDict[EmulationBgpConfigConstants.CAPABILITY_ROUTE_CONSTRAINT_CMD] = EmulationBgpConfigConstants.CAPABILITY_ROUTE_CONSTRAINT_0 # constant value
        dummyDict[EmulationBgpConfigConstants.CAPABILITY_ROUTE_REFRESH_CMD] = EmulationBgpConfigConstants.CAPABILITY_ROUTE_REFRESH_0 # constant value
        dummyDict[EmulationBgpConfigConstants.CONFIGURE_KEEPALIVE_TIMER_CMD] = EmulationBgpConfigConstants.CONFIGURE_KEEPALIVE_TIMER_0 # constant value
        dummyDict[EmulationBgpConfigConstants.COUNT_CMD] = "dummyValue13" # static value
        dummyDict[EmulationBgpConfigConstants.DISABLE_RECEIVED_UPDATE_VALIDATION_CMD] = EmulationBgpConfigConstants.DISABLE_RECEIVED_UPDATE_VALIDATION_0 # constant value
        dummyDict[EmulationBgpConfigConstants.DISCARD_IXIA_GENERATED_ROUTES_CMD] = EmulationBgpConfigConstants.DISCARD_IXIA_GENERATED_ROUTES_0 # constant value
        dummyDict[EmulationBgpConfigConstants.ENABLE_4_BYTE_AS_CMD] = EmulationBgpConfigConstants.ENABLE_4_BYTE_AS_0 # constant value
        dummyDict[EmulationBgpConfigConstants.ENABLE_AD_VPLS_PREFIX_LENGTH_CMD] = EmulationBgpConfigConstants.ENABLE_AD_VPLS_PREFIX_LENGTH_0 # constant value
        dummyDict[EmulationBgpConfigConstants.ENABLE_FLAP_CMD] = EmulationBgpConfigConstants.ENABLE_FLAP_0 # constant value
        dummyDict[EmulationBgpConfigConstants.FLAP_DOWN_TIME_CMD] = "dummyValue19" # static value
        dummyDict[EmulationBgpConfigConstants.FLAP_UP_TIME_CMD] = "dummyValue20" # static value
        dummyDict[EmulationBgpConfigConstants.GATEWAY_IP_ADDR_CMD] = "dummyValue21" # static value
        dummyDict[EmulationBgpConfigConstants.GRACEFUL_RESTART_ENABLE_CMD] = EmulationBgpConfigConstants.GRACEFUL_RESTART_ENABLE_0 # constant value
        dummyDict[EmulationBgpConfigConstants.HANDLE_CMD] = EmulationBgpConfigConstants.HANDLE_DELETE # constant value
        dummyDict[EmulationBgpConfigConstants.HOLD_TIME_CMD] = "dummyValue24" # static value
        dummyDict[EmulationBgpConfigConstants.IBGP_TESTER_AS_FOUR_BYTES_CMD] = "dummyValue25" # static value
        dummyDict[EmulationBgpConfigConstants.IBGP_TESTER_AS_TWO_BYTES_CMD] = "dummyValue26" # static value
        dummyDict[EmulationBgpConfigConstants.INITIATE_EBGP_ACTIVE_CONNECTION_CMD] = EmulationBgpConfigConstants.INITIATE_EBGP_ACTIVE_CONNECTION_0 # constant value
        dummyDict[EmulationBgpConfigConstants.INITIATE_IBGP_ACTIVE_CONNECTION_CMD] = EmulationBgpConfigConstants.INITIATE_IBGP_ACTIVE_CONNECTION_0 # constant value
        dummyDict[EmulationBgpConfigConstants.INTERFACE_HANDLE_CMD] = "dummyValue29" # static value
        dummyDict[EmulationBgpConfigConstants.IP_VERSION_CMD] = EmulationBgpConfigConstants.IP_VERSION_4 # constant value
        dummyDict[EmulationBgpConfigConstants.IPV4_CAPABILITY_MDT_NLRI_CMD] = "dummyValue31" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_CAPABILITY_MPLS_NLRI_CMD] = "dummyValue32" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_CAPABILITY_MPLS_VPN_NLRI_CMD] = "dummyValue33" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_CAPABILITY_MULTICAST_NLRI_CMD] = "dummyValue34" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_CAPABILITY_MULTICAST_VPN_NLRI_CMD] = "dummyValue35" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_CAPABILITY_UNICAST_NLRI_CMD] = "dummyValue36" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_FILTER_MPLS_NLRI_CMD] = "dummyValue37" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_FILTER_MPLS_VPN_NLRI_CMD] = "dummyValue38" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_FILTER_MULTICAST_NLRI_CMD] = "dummyValue39" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_FILTER_MULTICAST_VPN_NLRI_CMD] = "dummyValue40" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_FILTER_UNICAST_NLRI_CMD] = "dummyValue41" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_MDT_NLRI_CMD] = "dummyValue42" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_MPLS_NLRI_CMD] = "dummyValue43" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_MPLS_VPN_NLRI_CMD] = "dummyValue44" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_MULTICAST_NLRI_CMD] = "dummyValue45" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_MULTICAST_VPN_NLRI_CMD] = "dummyValue46" # static value
        dummyDict[EmulationBgpConfigConstants.IPV4_UNICAST_NLRI_CMD] = "dummyValue47" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_CAPABILITY_MPLS_NLRI_CMD] = "dummyValue48" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_CAPABILITY_MPLS_VPN_NLRI_CMD] = "dummyValue49" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_CAPABILITY_MULTICAST_NLRI_CMD] = "dummyValue50" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_CAPABILITY_MULTICAST_VPN_NLRI_CMD] = "dummyValue51" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_CAPABILITY_UNICAST_NLRI_CMD] = "dummyValue52" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_FILTER_MPLS_NLRI_CMD] = "dummyValue53" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_FILTER_MPLS_VPN_NLRI_CMD] = "dummyValue54" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_FILTER_MULTICAST_NLRI_CMD] = "dummyValue55" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_FILTER_MULTICAST_VPN_NLRI_CMD] = "dummyValue56" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_FILTER_UNICAST_NLRI_CMD] = "dummyValue57" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_MPLS_NLRI_CMD] = "dummyValue58" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_MPLS_VPN_NLRI_CMD] = "dummyValue59" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_MULTICAST_NLRI_CMD] = "dummyValue60" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_MULTICAST_VPN_NLRI_CMD] = "dummyValue61" # static value
        dummyDict[EmulationBgpConfigConstants.IPV6_UNICAST_NLRI_CMD] = "dummyValue62" # static value
        dummyDict[EmulationBgpConfigConstants.KEEPALIVE_TIMER_CMD] = "dummyValue63" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_ADDR_STEP_CMD] = "dummyValue64" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_AS_CMD] = "dummyValue65" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_AS4_CMD] = "dummyValue66" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_AS_MODE_CMD] = EmulationBgpConfigConstants.LOCAL_AS_MODE_FIXED # constant value
        dummyDict[EmulationBgpConfigConstants.LOCAL_AS_STEP_CMD] = "dummyValue68" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_IP_ADDR_CMD] = "dummyValue69" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_IPV6_ADDR_CMD] = "dummyValue70" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_LOOPBACK_IP_ADDR_CMD] = "dummyValue71" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_LOOPBACK_IP_ADDR_STEP_CMD] = "dummyValue72" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_LOOPBACK_IP_PREFIX_LENGTH_CMD] = "dummyValue73" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_ROUTER_ID_CMD] = "dummyValue74" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_ROUTER_ID_ENABLE_CMD] = EmulationBgpConfigConstants.LOCAL_ROUTER_ID_ENABLE_0 # constant value
        dummyDict[EmulationBgpConfigConstants.LOCAL_ROUTER_ID_STEP_CMD] = "dummyValue76" # static value
        dummyDict[EmulationBgpConfigConstants.LOCAL_ROUTER_ID_TYPE_CMD] = EmulationBgpConfigConstants.LOCAL_ROUTER_ID_TYPE_SAME # constant value
        dummyDict[EmulationBgpConfigConstants.MAC_ADDRESS_START_CMD] = "dummyValue78" # static value
        dummyDict[EmulationBgpConfigConstants.MAC_ADDRESS_STEP_CMD] = "dummyValue79" # static value
        dummyDict[EmulationBgpConfigConstants.MD5_ENABLE_CMD] = EmulationBgpConfigConstants.MD5_ENABLE_0 # constant value
        dummyDict[EmulationBgpConfigConstants.MD5_KEY_CMD] = "dummyValue81" # static value
        dummyDict[EmulationBgpConfigConstants.MLDP_P2MP_FEC_TYPE_CMD] = "dummyValue82" # static value
        dummyDict[EmulationBgpConfigConstants.MODE_CMD] = EmulationBgpConfigConstants.MODE_DELETE # constant value
        dummyDict[EmulationBgpConfigConstants.MODIFY_OUTGOING_AS_PATH_CMD] = "dummyValue84" # static value
        dummyDict[EmulationBgpConfigConstants.NEIGHBOR_TYPE_CMD] = EmulationBgpConfigConstants.NEIGHBOR_TYPE_INTERNAL # constant value
        dummyDict[EmulationBgpConfigConstants.NETMASK_CMD] = "dummyValue86" # static value
        dummyDict[EmulationBgpConfigConstants.NEXT_HOP_ENABLE_CMD] = EmulationBgpConfigConstants.NEXT_HOP_ENABLE_FLAG # constant value
        dummyDict[EmulationBgpConfigConstants.NEXT_HOP_IP_CMD] = "dummyValue88" # static value
        dummyDict[EmulationBgpConfigConstants.NO_WRITE_CMD] = "dummyValue89" # static value
        dummyDict[EmulationBgpConfigConstants.OVERRIDE_EXISTENCE_CHECK_CMD] = EmulationBgpConfigConstants.OVERRIDE_EXISTENCE_CHECK_0 # constant value
        dummyDict[EmulationBgpConfigConstants.OVERRIDE_TRACKING_CMD] = EmulationBgpConfigConstants.OVERRIDE_TRACKING_0 # constant value
        dummyDict[EmulationBgpConfigConstants.PORT_HANDLE_CMD] = "dummyValue92" # static value
        dummyDict[EmulationBgpConfigConstants.REMOTE_ADDR_STEP_CMD] = "dummyValue93" # static value
        dummyDict[EmulationBgpConfigConstants.REMOTE_AS_CMD] = "dummyValue94" # static value
        dummyDict[EmulationBgpConfigConstants.REMOTE_CONFEDERATION_MEMBER_CMD] = "dummyValue95" # static value
        dummyDict[EmulationBgpConfigConstants.REMOTE_IP_ADDR_CMD] = "dummyValue96" # static value
        dummyDict[EmulationBgpConfigConstants.REMOTE_IPV6_ADDR_CMD] = "dummyValue97" # static value
        dummyDict[EmulationBgpConfigConstants.REMOTE_LOOPBACK_IP_ADDR_CMD] = "dummyValue98" # static value
        dummyDict[EmulationBgpConfigConstants.REMOTE_LOOPBACK_IP_ADDR_STEP_CMD] = "dummyValue99" # static value
        dummyDict[EmulationBgpConfigConstants.REQUEST_VPN_LABEL_EXCHANGE_OVER_LSP_CMD] = EmulationBgpConfigConstants.REQUEST_VPN_LABEL_EXCHANGE_OVER_LSP_0 # constant value
        dummyDict[EmulationBgpConfigConstants.RESET_CMD] = "dummyValue101" # static value
        dummyDict[EmulationBgpConfigConstants.RESTART_TIME_CMD] = "dummyValue102" # static value
        dummyDict[EmulationBgpConfigConstants.RETRIES_CMD] = "dummyValue103" # static value
        dummyDict[EmulationBgpConfigConstants.RETRY_TIME_CMD] = "dummyValue104" # static value
        dummyDict[EmulationBgpConfigConstants.ROUTE_REFRESH_CMD] = "dummyValue105" # static value
        dummyDict[EmulationBgpConfigConstants.ROUTES_PER_MSG_CMD] = "dummyValue106" # static value
        dummyDict[EmulationBgpConfigConstants.SEND_IXIA_SIGNATURE_WITH_ROUTES_CMD] = EmulationBgpConfigConstants.SEND_IXIA_SIGNATURE_WITH_ROUTES_0 # constant value
        dummyDict[EmulationBgpConfigConstants.STAGGERED_START_ENABLE_CMD] = "dummyValue108" # static value
        dummyDict[EmulationBgpConfigConstants.STAGGERED_START_TIME_CMD] = "dummyValue109" # static value
        dummyDict[EmulationBgpConfigConstants.STALE_TIME_CMD] = "dummyValue110" # static value
        dummyDict[EmulationBgpConfigConstants.START_RATE_CMD] = "dummyValue111" # static value
        dummyDict[EmulationBgpConfigConstants.START_RATE_ENABLE_CMD] = EmulationBgpConfigConstants.START_RATE_ENABLE_0 # constant value
        dummyDict[EmulationBgpConfigConstants.START_RATE_INTERVAL_CMD] = "dummyValue113" # static value
        dummyDict[EmulationBgpConfigConstants.START_RATE_SCALE_MODE_CMD] = EmulationBgpConfigConstants.START_RATE_SCALE_MODE_DEVICEGROUP # constant value
        dummyDict[EmulationBgpConfigConstants.STOP_RATE_CMD] = "dummyValue115" # static value
        dummyDict[EmulationBgpConfigConstants.STOP_RATE_ENABLE_CMD] = EmulationBgpConfigConstants.STOP_RATE_ENABLE_0 # constant value
        dummyDict[EmulationBgpConfigConstants.STOP_RATE_INTERVAL_CMD] = "dummyValue117" # static value
        dummyDict[EmulationBgpConfigConstants.STOP_RATE_SCALE_MODE_CMD] = EmulationBgpConfigConstants.STOP_RATE_SCALE_MODE_DEVICEGROUP # constant value
        dummyDict[EmulationBgpConfigConstants.SUPPRESS_NOTIFY_CMD] = "dummyValue119" # static value
        dummyDict[EmulationBgpConfigConstants.TCP_WINDOW_SIZE_CMD] = "dummyValue120" # static value
        dummyDict[EmulationBgpConfigConstants.TIMEOUT_CMD] = "dummyValue121" # static value
        dummyDict[EmulationBgpConfigConstants.TRIGGER_VPLS_PW_INITIATION_CMD] = EmulationBgpConfigConstants.TRIGGER_VPLS_PW_INITIATION_0 # constant value
        dummyDict[EmulationBgpConfigConstants.TTL_VALUE_CMD] = "dummyValue123" # static value
        dummyDict[EmulationBgpConfigConstants.UPDATE_INTERVAL_CMD] = "dummyValue124" # static value
        dummyDict[EmulationBgpConfigConstants.UPDATE_MSG_SIZE_CMD] = "dummyValue125" # static value
        dummyDict[EmulationBgpConfigConstants.UPDATES_PER_ITERATION_CMD] = "dummyValue126" # static value
        dummyDict[EmulationBgpConfigConstants.VCI_CMD] = "dummyValue127" # static value
        dummyDict[EmulationBgpConfigConstants.VCI_STEP_CMD] = "dummyValue128" # static value
        dummyDict[EmulationBgpConfigConstants.VLAN_CMD] = EmulationBgpConfigConstants.VLAN_0 # constant value
        dummyDict[EmulationBgpConfigConstants.VLAN_CFI_CMD] = "dummyValue130" # static value
        dummyDict[EmulationBgpConfigConstants.VLAN_ID_CMD] = "dummyValue131" # static value
        dummyDict[EmulationBgpConfigConstants.VLAN_ID_MODE_CMD] = EmulationBgpConfigConstants.VLAN_ID_MODE_FIXED # constant value
        dummyDict[EmulationBgpConfigConstants.VLAN_ID_STEP_CMD] = "dummyValue133" # static value
        dummyDict[EmulationBgpConfigConstants.VLAN_USER_PRIORITY_CMD] = "dummyValue134" # static value
        dummyDict[EmulationBgpConfigConstants.VPI_CMD] = "dummyValue135" # static value
        dummyDict[EmulationBgpConfigConstants.VPI_STEP_CMD] = "dummyValue136" # static value
        dummyDict[EmulationBgpConfigConstants.VPLS_CMD] = EmulationBgpConfigConstants.VPLS_0 # constant value
        dummyDict[EmulationBgpConfigConstants.VPLS_CAPABILITY_NLRI_CMD] = "dummyValue138" # static value
        dummyDict[EmulationBgpConfigConstants.VPLS_FILTER_NLRI_CMD] = "dummyValue139" # static value
        dummyDict[EmulationBgpConfigConstants.VPLS_NLRI_CMD] = "dummyValue140" # static value

        api = device.getApi(EmulationBgpConfigConstants.EMULATION_BGP_CONFIG_API)
        api.emulation_bgp_config(dummyDict)
    """
    def emulation_bgp_config(self, argdictionary):
        return self.send_command_args(self._nameSpace +"::emulation_bgp_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """

    def emulation_bgp_config_Arguments(self, parameter):
        """
        This is the method the command: emulation_bgp_config option Arguments
        Description:Description
        Constants Available: ARGUMENTS_CMD
        Supported:Supported
        Keyword arguments:
        parameter --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ARGUMENTS_CMD: parameter})

    def emulation_bgp_config_act_as_restarted(self, bool):
        """
        This is the method the command: emulation_bgp_config option act_as_restarted
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Act as restarted

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'graceful_restart_enable' | value= '1' |
        Constants Available: ACT_AS_RESTARTED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ACT_AS_RESTARTED_CMD : bool})

    def emulation_bgp_config_active(self, bool):
        """
        This is the method the command: emulation_bgp_config option active
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Activates the item

            DEFAULT


            1
        Constants Available: ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ACTIVE_CMD : bool})

    def emulation_bgp_config_active_connect_enable(self, flag):
        """
        This is the method the command: emulation_bgp_config option active_connect_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            For External BGP neighbor. If set, a HELLO message is actively sent when BGP testing starts. Otherwise, the port waits for the DUT to send its HELLO message.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            For External BGP neighbor. If set, a HELLO message is actively sent when BGP testing starts. Otherwise, the port waits for the DUT to send its HELLO message.

            DEFAULT
             None
        Constants Available: ACTIVE_CONNECT_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ACTIVE_CONNECT_ENABLE_CMD : flag})

    def emulation_bgp_config_advertise_end_of_rib(self, bool):
        """
        This is the method the command: emulation_bgp_config option advertise_end_of_rib
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Advertise End-Of-RIB

            DEFAULT


            0
        Constants Available: ADVERTISE_END_OF_RIB_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ADVERTISE_END_OF_RIB_CMD : bool})

    def emulation_bgp_config_advertise_host_route(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option advertise_host_route
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Not supported

            DEFAULT
             Not supported

            IxNetwork-NGPF


            DESCRIPTION


            Not supported

            DEFAULT
             Not supported
        Constants Available: ADVERTISE_HOST_ROUTE_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ADVERTISE_HOST_ROUTE_CMD : not_supported})

    def emulation_bgp_config_atm_encapsulation(self, opt):
        """
        This is the method the command: emulation_bgp_config option atm_encapsulation
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The encapsulation of the ATM protocol interface associated with the emulated router.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The encapsulation of the ATM protocol interface associated with the emulated router.

            Valid options are:

            VccMuxIPV4Routed


            VccMuxIPV6Routed


            VccMuxBridgedEthernetFCS


            VccMuxBridgedEthernetNoFCS


            LLCRoutedCLIP


            LLCBridgedEthernetFCS


            LLCBridgedEthernetNoFCS


            DEFAULT
             None
        Constants Available: ATM_ENCAPSULATION_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ATM_ENCAPSULATION_CMD : opt})

    def emulation_bgp_config_bfd_registration(self, bool):
        """
        This is the method the command: emulation_bgp_config option bfd_registration
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Enable or disable BFD registration.

            DEFAULT


            0

            IxNetwork-NGPF


            DESCRIPTION


            Enable or disable BFD registration.

            DEFAULT


            0
        Constants Available: BFD_REGISTRATION_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.BFD_REGISTRATION_CMD : bool})

    def emulation_bgp_config_bfd_registration_mode(self, opt):
        """
        This is the method the command: emulation_bgp_config option bfd_registration_mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Set BFD registration mode to single hop or multi hop.

            DEFAULT


            multi_hop

            IxNetwork-NGPF


            DESCRIPTION


            Set BFD registration mode to single hop or multi hop.

            Valid options are:

            single_hop


            multi_hop


            DEFAULT


            multi_hop
        Constants Available: BFD_REGISTRATION_MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.BFD_REGISTRATION_MODE_CMD : opt})

    def emulation_bgp_config_capability_route_constraint(self, bool):
        """
        This is the method the command: emulation_bgp_config option capability_route_constraint
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Route Constraint

            DEFAULT
             None
        Constants Available: CAPABILITY_ROUTE_CONSTRAINT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.CAPABILITY_ROUTE_CONSTRAINT_CMD : bool})

    def emulation_bgp_config_capability_route_refresh(self, bool):
        """
        This is the method the command: emulation_bgp_config option capability_route_refresh
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Route Refresh

            DEFAULT
             None
        Constants Available: CAPABILITY_ROUTE_REFRESH_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.CAPABILITY_ROUTE_REFRESH_CMD : bool})

    def emulation_bgp_config_configure_keepalive_timer(self, bool):
        """
        This is the method the command: emulation_bgp_config option configure_keepalive_timer
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Configure Keepalive Timer

            DEFAULT


            0
        Constants Available: CONFIGURE_KEEPALIVE_TIMER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.CONFIGURE_KEEPALIVE_TIMER_CMD : bool})

    def emulation_bgp_config_count(self, numeric):
        """
        This is the method the command: emulation_bgp_config option count
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Number of BGP nodes to create.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Number of BGP nodes to create.

            DEFAULT


            1
        Constants Available: COUNT_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.COUNT_CMD : numeric})

    def emulation_bgp_config_disable_received_update_validation(self, bool):
        """
        This is the method the command: emulation_bgp_config option disable_received_update_validation
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Disable Received Update Validation (Enabled for High Performance)

            DEFAULT
             None
        Constants Available: DISABLE_RECEIVED_UPDATE_VALIDATION_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.DISABLE_RECEIVED_UPDATE_VALIDATION_CMD : bool})

    def emulation_bgp_config_discard_ixia_generated_routes(self, bool):
        """
        This is the method the command: emulation_bgp_config option discard_ixia_generated_routes
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Discard Ixia Generated Routes

            DEFAULT


            0
        Constants Available: DISCARD_IXIA_GENERATED_ROUTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.DISCARD_IXIA_GENERATED_ROUTES_CMD : bool})

    def emulation_bgp_config_enable_4_byte_as(self, bool):
        """
        This is the method the command: emulation_bgp_config option enable_4_byte_as
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Allow 4 byte values for -local_as.

            DEFAULT


            0

            IxNetwork-NGPF


            DESCRIPTION


            Allow 4 byte values for -local_as.

            DEFAULT


            0
        Constants Available: ENABLE_4_BYTE_AS_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ENABLE_4_BYTE_AS_CMD : bool})

    def emulation_bgp_config_enable_ad_vpls_prefix_length(self, bool):
        """
        This is the method the command: emulation_bgp_config option enable_ad_vpls_prefix_length
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Enable AD VPLS Prefix Length in Bits

            DEFAULT
             None
        Constants Available: ENABLE_AD_VPLS_PREFIX_LENGTH_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ENABLE_AD_VPLS_PREFIX_LENGTH_CMD : bool})

    def emulation_bgp_config_enable_flap(self, bool):
        """
        This is the method the command: emulation_bgp_config option enable_flap
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Flap

            DEFAULT


            0
        Constants Available: ENABLE_FLAP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ENABLE_FLAP_CMD : bool})

    def emulation_bgp_config_flap_down_time(self, numeric):
        """
        This is the method the command: emulation_bgp_config option flap_down_time
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Downtime in Seconds

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'enable_flap' | value= '1' |
        Constants Available: FLAP_DOWN_TIME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.FLAP_DOWN_TIME_CMD : numeric})

    def emulation_bgp_config_flap_up_time(self, numeric):
        """
        This is the method the command: emulation_bgp_config option flap_up_time
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Uptime in Seconds

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'enable_flap' | value= '1' |
        Constants Available: FLAP_UP_TIME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.FLAP_UP_TIME_CMD : numeric})

    def emulation_bgp_config_gateway_ip_addr(self, ip):
        """
        This is the method the command: emulation_bgp_config option gateway_ip_addr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The gateway IPV4 or IPV6 address of the BGP4 neighbor interface. If this parameter is not provided it will be initialized to the remote_ip_addr value.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The gateway IPV4 or IPV6 address of the BGP4 neighbor interface. If this parameter is not provided it will be initialized to the remote_ip_addr value.

            DEFAULT
             None
        Constants Available: GATEWAY_IP_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.GATEWAY_IP_ADDR_CMD : ip})

    def emulation_bgp_config_graceful_restart_enable(self, bool):
        """
        This is the method the command: emulation_bgp_config option graceful_restart_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Will enable graceful restart (HA) on the BGP4 neighbor.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Will enable graceful restart (HA) on the BGP4 neighbor.

            DEFAULT


            0
        Constants Available: GRACEFUL_RESTART_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.GRACEFUL_RESTART_ENABLE_CMD : bool})

    def emulation_bgp_config_handle(self, opt):
        """
        This is the method the command: emulation_bgp_config option handle
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            BGP handle used for -mode modify/disable/delete.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            BGP handle used for -mode modify/disable/delete. When -handle is provided with the /globals value the arguments that configure global protocol setting accept both multivalue handles and simple values. When -handle is provided with a a protocol stack handle or a protocol session handle, the arguments that configure global settings will only accept simple values. In this situation, these arguments will configure only the settings of the parent device group or the ports associated with the parent topology.

            DEFAULT
             None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.HANDLE_CMD : opt})

    def emulation_bgp_config_hold_time(self, numeric):
        """
        This is the method the command: emulation_bgp_config option hold_time
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Configures the hold time for BGP sessions for this Neighbor. Keepalives are sent out every one-third of this interval. If the default value is 90, KeepAlive messages are sent every 30 seconds.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Configures the hold time for BGP sessions for this Neighbor. Keepalives are sent out every one-third of this interval. If the default value is 90, KeepAlive messages are sent every 30 seconds.

            DEFAULT
             None
        Constants Available: HOLD_TIME_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.HOLD_TIME_CMD : numeric})

    def emulation_bgp_config_ibgp_tester_as_four_bytes(self, numeric):
        """
        This is the method the command: emulation_bgp_config option ibgp_tester_as_four_bytes
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Tester 4 Byte AS# for iBGP

            DEFAULT
             None
        Constants Available: IBGP_TESTER_AS_FOUR_BYTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IBGP_TESTER_AS_FOUR_BYTES_CMD : numeric})

    def emulation_bgp_config_ibgp_tester_as_two_bytes(self, numeric):
        """
        This is the method the command: emulation_bgp_config option ibgp_tester_as_two_bytes
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Tester AS# for iBGP

            DEFAULT
             None
        Constants Available: IBGP_TESTER_AS_TWO_BYTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IBGP_TESTER_AS_TWO_BYTES_CMD : numeric})

    def emulation_bgp_config_initiate_ebgp_active_connection(self, bool):
        """
        This is the method the command: emulation_bgp_config option initiate_ebgp_active_connection
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Initiate eBGP Active Connection

            DEFAULT
             None
        Constants Available: INITIATE_EBGP_ACTIVE_CONNECTION_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.INITIATE_EBGP_ACTIVE_CONNECTION_CMD : bool})

    def emulation_bgp_config_initiate_ibgp_active_connection(self, bool):
        """
        This is the method the command: emulation_bgp_config option initiate_ibgp_active_connection
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Initiate iBGP Active Connection

            DEFAULT
             None
        Constants Available: INITIATE_IBGP_ACTIVE_CONNECTION_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.INITIATE_IBGP_ACTIVE_CONNECTION_CMD : bool})

    def emulation_bgp_config_interface_handle(self, string):
        """
        This is the method the command: emulation_bgp_config option interface_handle
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            This parameter is valid only for IxTclNetwork API and represents a list of interfaces previously created using interface_config or another emulation__config command that returns the interfacehandles (for example: BFD).

            Starting with IxNetwork 5.60 this parameter accepts handles returned by emulation_dhcp_group_config procedure in the following format: |,-, ... The DHCP ranges are separated from the Interface Index identifiers with the (|) character. The Interface Index identifiers are separated with comas (,). A range of Interface Index identifiers can be defined using the dash (-) character.

            Ranges along with the Interface Index identifiers are grouped together in TCL Lists. The lists can contain mixed items, protocol interface handles returned by interface_config and handles returned by emulation_dhcp_group_config along with the interface index.

            Example:count 10 (10 BGP neighbors). 3 DHCP range handles returned by ::::emulation_dhcp_group_config. Each DHCP range has 20 sessions (interfaces). If we pass -interface_handle in the following format: [list $dhcp_r1|1,5 $dhcp_r2|1-3 $dhcp_r3|1,3,5-9,13] The interfaces will be distributed to the routers in the following manner:

            BGP Neighbor 1: $dhcp_r1 -> interface 1
            BGP Neighbor 2: $dhcp_r1 -> interface 5
            BGP Neighbor 3: $dhcp_r2 -> interface 1
            BGP Neighbor 4: $dhcp_r2 -> interface 2
            BGP Neighbor 5: $dhcp_r2 -> interface 3
            BGP Neighbor 6: $dhcp_r3 -> interface 1
            BGP Neighbor 7: $dhcp_r3 -> interface 3
            BGP Neighbor 8: $dhcp_r3 -> interface 5
            BGP Neighbor 9: $dhcp_r3 -> interface 6
            BGP Neighbor 10: $dhcp_r3 -> interface 7
            BGP Neighbor 11: $dhcp_r3 -> interface 8
            BGP Neighbor 12: $dhcp_r3 -> interface 9
            BGP Neighbor 13 $dhcp_r3 -> interface 13

            Starting with IxNetwork 6.30SP1 this parameter accepts handles returned by interface_config procedure with -l23_config_type static_type setting in the following format: |,-, ... The IP ranges are separated from the Interface Index identifiers with the (|) character. The Interface Index identifiers are separated with comas (,). A range of Interface Index identifiers can be defined using the dash (-) character.

            Ranges along with the Interface Index identifiers are grouped together in TCL Lists. The lists can contain mixed items, protocol interface handles returned by interface_config with -l23_config_type protocol_interface and with -l23_config_type static_type.

            Example:count 10 (10 BGP neighbors). 3 IP range handles returned by ::::interface_config. Each IP range has 20 sessions (interfaces). If we pass -interface_handle in the following format: [list $ip_r1|1,5 $ip_r2|1-3 $ip_r3|1,3,5-9,13] The interfaces will be distributed to the routers in the following manner:


            BGP Neighbor 1: $ip_r1 -> interface 1
            BGP Neighbor 2: $ip_r1 -> interface 5
            BGP Neighbor 3: $ip_r2 -> interface 1
            BGP Neighbor 4: $ip_r2 -> interface 2
            BGP Neighbor 5: $ip_r2 -> interface 3
            BGP Neighbor 6: $ip_r3 -> interface 1
            BGP Neighbor 7: $ip_r3 -> interface 3
            BGP Neighbor 8: $ip_r3 -> interface 5
            BGP Neighbor 9: $ip_r3 -> interface 6
            BGP Neighbor 10: $ip_r3 -> interface 7
            BGP Neighbor 11: $ip_r3 -> interface 8
            BGP Neighbor 12: $ip_r3 -> interface 9
            BGP Neighbor 13 $ip_r3 -> interface 13

            Valid for mode create for IxTclNetwork only.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            This parameter is valid only for IxTclNetwork API and represents a list of interfaces previously created using interface_config or another emulation__config command that returns the interface handles (for example: BFD). Starting with IxNetwork 5.60 this parameter accepts handles returned by emulation_dhcp_group_config procedure in the following format: |,-, ... The DHCP ranges are separated from the Interface Index identifiers with the (|) character. The Interface Index identifiers are separated with comas (,). A range of Interface Index identifiers can be defined using the dash (-) character. Ranges along with the Interface Index identifiers are grouped together in TCL Lists. The lists can contain mixed items, protocol interface handles returned by interface_config and handles returned by emulation_dhcp_group_config along with the interface index. Example: count 10 (10 BGP neighbors). 3 DHCP range handles returned by ::::emulation_dhcp_group_config. Each DHCP range has 20 sessions (interfaces). If we pass a -interface_handle in the following format: [list $dhcp_r1|1,5 $dhcp_r2|1-3 $dhcp_r3|1,3,5-9,13] The interfaces will be distributed to the routers in the following manner: BGP Neighbor 1: $dhcp_r1 -> interface 1 BGP Neighbor 2: $dhcp_r1 -> interface 5 BGP Neighbor 3: $dhcp_r2 -> interface 1 BGP Neighbor 4: $dhcp_r2 -> interface 2 BGP Neighbor 5: $dhcp_r2 -> interface 3 BGP Neighbor 6: $dhcp_r3 -> interface 1 BGP Neighbor 7: $dhcp_r3 -> interface 3 BGP Neighbor 8: $dhcp_r3 -> interface 5 BGP Neighbor 9: $dhcp_r3 -> interface 6 BGP Neighbor 10: $dhcp_r3 -> interface 7 BGP Neighbor 11: $dhcp_r3 -> interface 8 BGP Neighbor 12: $dhcp_r3 -> interface 9 BGP Neighbor 13 $dhcp_r3 -> interface 13 Starting with IxNetwork 6.30SP1 this parameter accepts handles returned by interface_config procedure with -l23_config_type static_type setting in the following format: |,-, ... The IP ranges are separated from the Interface Index identifiers with the (|) character. The Interface Index identifiers are separated with comas (,). A range of Interface Index identifiers can be defined using the dash (-) character. Ranges along with the Interface Index identifiers are grouped together in TCL Lists. The lists can contain mixed items, protocol interface handles returned by interface_config with -l23_config_type protocol_interface and with -l23_config_type static_type. Example: count 10 (10 BGP neighbors). 3 IP range handles returned by ::::interface_config. Each IP range has 20 sessions (interfaces). If we pass a -interface_handle in the following format: [list $ip_r1|1,5 $ip_r2|1-3 $ip_r3|1,3,5-9,13] The interfaces will be distributed to the routers in the following manner: BGP Neighbor 1: $ip_r1 -> interface 1 BGP Neighbor 2: $ip_r1 -> interface 5 BGP Neighbor 3: $ip_r2 -> interface 1 BGP Neighbor 4: $ip_r2 -> interface 2 BGP Neighbor 5: $ip_r2 -> interface 3 BGP Neighbor 6: $ip_r3 -> interface 1 BGP Neighbor 7: $ip_r3 -> interface 3 BGP Neighbor 8: $ip_r3 -> interface 5 BGP Neighbor 9: $ip_r3 -> interface 6 BGP Neighbor 10: $ip_r3 -> interface 7 BGP Neighbor 11: $ip_r3 -> interface 8 BGP Neighbor 12: $ip_r3 -> interface 9 BGP Neighbor 13 $ip_r3 -> interface 13 Valid for mode create for IxTclNetwork only.

            DEFAULT
             None
        Constants Available: INTERFACE_HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        string --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.INTERFACE_HANDLE_CMD : string})

    def emulation_bgp_config_ip_version(self, opt):
        """
        This is the method the command: emulation_bgp_config option ip_version
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This option defines the IP version of the BGP4.

            Valid options are:

            4


            IPv4

            6


            IPv6

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            This option defines the IP version of the BGP4 neighbor to be configured on the Ixia interface.

            Valid options are:

            4


            IPv4

            6


            IPv6

            DEFAULT


            4
        Constants Available: IP_VERSION_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IP_VERSION_CMD : opt})

    def emulation_bgp_config_ipv4_capability_mdt_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_capability_mdt_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If checked, this BGP/BGP+ router/peer supports IPv4 MDT address family messages.

            DEFAULT
             None
        Constants Available: IPV4_CAPABILITY_MDT_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_CAPABILITY_MDT_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_capability_mpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_capability_mpls_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_CAPABILITY_MPLS_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_CAPABILITY_MPLS_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_capability_mpls_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_capability_mpls_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_CAPABILITY_MPLS_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_CAPABILITY_MPLS_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_capability_multicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_capability_multicast_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_CAPABILITY_MULTICAST_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_CAPABILITY_MULTICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_capability_multicast_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_capability_multicast_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            IPv4 Multicast VPN

            DEFAULT
             None
        Constants Available: IPV4_CAPABILITY_MULTICAST_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_CAPABILITY_MULTICAST_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_capability_unicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_capability_unicast_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_CAPABILITY_UNICAST_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_CAPABILITY_UNICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_filter_mpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_filter_mpls_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_FILTER_MPLS_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_FILTER_MPLS_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_filter_mpls_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_filter_mpls_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_FILTER_MPLS_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_FILTER_MPLS_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_filter_multicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_filter_multicast_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_FILTER_MULTICAST_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_FILTER_MULTICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_filter_multicast_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_filter_multicast_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            IPv4 Multicast VPN

            DEFAULT
             None
        Constants Available: IPV4_FILTER_MULTICAST_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_FILTER_MULTICAST_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_filter_unicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_filter_unicast_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_FILTER_UNICAST_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_FILTER_UNICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_mdt_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_mdt_nlri
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If checked, this BGP/BGP+ router/peer supports IPv4 MDT address family messages.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If checked, this BGP/BGP+ router/peer supports IPv4 MDT address family messages.

            DEFAULT
             None
        Constants Available: IPV4_MDT_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_MDT_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_mpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_mpls_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            If used, support for IPv4 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_MPLS_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_MPLS_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_mpls_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_mpls_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            If used, support for IPv4 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_MPLS_VPN_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_MPLS_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_multicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_multicast_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            If used, support for IPv4 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_MULTICAST_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_MULTICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_multicast_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_multicast_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            IPv4 Multicast VPN

            DEFAULT
             None
        Constants Available: IPV4_MULTICAST_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_MULTICAST_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv4_unicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv4_unicast_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            If used, support for IPv4 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv4 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV4_UNICAST_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV4_UNICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_capability_mpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_capability_mpls_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_CAPABILITY_MPLS_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_CAPABILITY_MPLS_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_capability_mpls_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_capability_mpls_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_CAPABILITY_MPLS_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_CAPABILITY_MPLS_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_capability_multicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_capability_multicast_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_CAPABILITY_MULTICAST_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_CAPABILITY_MULTICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_capability_multicast_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_capability_multicast_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            IPv6 Multicast VPN

            DEFAULT
             None
        Constants Available: IPV6_CAPABILITY_MULTICAST_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_CAPABILITY_MULTICAST_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_capability_unicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_capability_unicast_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_CAPABILITY_UNICAST_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_CAPABILITY_UNICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_filter_mpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_filter_mpls_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_FILTER_MPLS_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_FILTER_MPLS_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_filter_mpls_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_filter_mpls_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_FILTER_MPLS_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_FILTER_MPLS_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_filter_multicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_filter_multicast_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_FILTER_MULTICAST_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_FILTER_MULTICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_filter_multicast_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_filter_multicast_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            IPv6 Multicast VPN

            DEFAULT
             None
        Constants Available: IPV6_FILTER_MULTICAST_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_FILTER_MULTICAST_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_filter_unicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_filter_unicast_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_FILTER_UNICAST_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_FILTER_UNICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_mpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_mpls_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            If used, support for IPv6 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_MPLS_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_MPLS_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_mpls_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_mpls_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            If used, support for IPv6 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_MPLS_VPN_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_MPLS_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_multicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_multicast_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            If used, support for IPv6 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_MULTICAST_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_MULTICAST_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_multicast_vpn_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_multicast_vpn_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            IPv6 Multicast VPN

            DEFAULT
             None
        Constants Available: IPV6_MULTICAST_VPN_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_MULTICAST_VPN_NLRI_CMD : flag})

    def emulation_bgp_config_ipv6_unicast_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option ipv6_unicast_nlri
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            If used, support for IPv6 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If used, support for IPv6 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

            DEFAULT
             None
        Constants Available: IPV6_UNICAST_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.IPV6_UNICAST_NLRI_CMD : flag})

    def emulation_bgp_config_keepalive_timer(self, numeric):
        """
        This is the method the command: emulation_bgp_config option keepalive_timer
        Description:Supported platforms  Details
            RANGE 0 - 65535
            IxNetwork-NGPF


            DESCRIPTION


            Keepalive Timer

            DEFAULT


            30
        Constants Available: KEEPALIVE_TIMER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.KEEPALIVE_TIMER_CMD : numeric})

    def emulation_bgp_config_local_addr_step(self, ip):
        """
        This is the method the command: emulation_bgp_config option local_addr_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Defines the mask and increment step for the next -local_ip_addr or ""-local_ipv6_addr"".(DEFAULT = 0.1.0.0 | 0:0:0:0:1::0)

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Defines the mask and increment step for the next -local_ip_addr or ""-local_ipv6_addr"".

            DEFAULT
             None
        Constants Available: LOCAL_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_ADDR_STEP_CMD : ip})

    def emulation_bgp_config_local_as(self, numeric):
        """
        This is the method the command: emulation_bgp_config option local_as
        Description:Supported platforms  Details
            RANGE 0 - 4294967295
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The AS number of the BGP node to be emulated by the test port.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The AS number of the BGP node to be emulated by the test port.

            DEFAULT
             None
        Constants Available: LOCAL_AS_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_AS_CMD : numeric})

    def emulation_bgp_config_local_as4(self, numeric):
        """
        This is the method the command: emulation_bgp_config option local_as4
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            The 4 bytes AS number of the BGP node to be emulated by the test port.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'enable_4_byte_as' | value= '1' |
        Constants Available: LOCAL_AS4_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_AS4_CMD : numeric})

    def emulation_bgp_config_local_as_mode(self, opt):
        """
        This is the method the command: emulation_bgp_config option local_as_mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            For External BGP type only. This option controls the AS number (local_as) assigned to additional routers.

            Valid options are:

            fixed


            (default) the local_as remains fixed.

            increment


            increments the local_as.

            DEFAULT


            fixed

            IxNetwork-NGPF


            DESCRIPTION


            For External BGP type only. This option controls the AS number (local_as) assigned to additional routers.

            Valid options are:

            fixed


            (default) the local_as remains fixed

            increment


            increments the local_as

            DEFAULT


            fixed
        Constants Available: LOCAL_AS_MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_AS_MODE_CMD : opt})

    def emulation_bgp_config_local_as_step(self, numeric):
        """
        This is the method the command: emulation_bgp_config option local_as_step
        Description:Supported platforms  Details
            RANGE 0 - 4294967295
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If you configure more then 1 eBGP neighbor on the Ixia interface, and if you select the option local_as_mode to increment, the option local_as_step defines the step by which the AS number is incremented.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If you configure more then 1 eBGP neighbor on the Ixia interface, and if you select the option local_as_mode to increment, the option local_as_step defines the step by which the AS number is incremented.

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'local_as_mode' | value= 'increment' |
        Constants Available: LOCAL_AS_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_AS_STEP_CMD : numeric})

    def emulation_bgp_config_local_ip_addr(self, ipv4):
        """
        This is the method the command: emulation_bgp_config option local_ip_addr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The IPv4 address of the Ixia simulated BGP node to be emulated.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The IPv4 address of the Ixia simulated BGP node to be emulated.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ip_version' | value= '4' |
        Constants Available: LOCAL_IP_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_IP_ADDR_CMD : ipv4})

    def emulation_bgp_config_local_ipv6_addr(self, ipv6):
        """
        This is the method the command: emulation_bgp_config option local_ipv6_addr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The IPv6 address of the BGP node to be emulated by the test port.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The IPv6 address of the BGP node to be emulated by the test port.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ip_version' | value= '6' |
        Constants Available: LOCAL_IPV6_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_IPV6_ADDR_CMD : ipv6})

    def emulation_bgp_config_local_loopback_ip_addr(self, ip):
        """
        This is the method the command: emulation_bgp_config option local_loopback_ip_addr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Required when the -ipv4_mpls_vpn_nlri option is used.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Required when the -ipv4_mpls_vpn_nlri option is used.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4_mpls_vpn_nlri' | value= '' |
        Constants Available: LOCAL_LOOPBACK_IP_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_LOOPBACK_IP_ADDR_CMD : ip})

    def emulation_bgp_config_local_loopback_ip_addr_step(self, ip):
        """
        This is the method the command: emulation_bgp_config option local_loopback_ip_addr_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Required when the -ipv4_mpls_vpn_nlri option is used.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Required when the -ipv4_mpls_vpn_nlri option is used.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4_mpls_vpn_nlri' | value= '' |
        Constants Available: LOCAL_LOOPBACK_IP_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_LOOPBACK_IP_ADDR_STEP_CMD : ip})

    def emulation_bgp_config_local_loopback_ip_prefix_length(self, numeric):
        """
        This is the method the command: emulation_bgp_config option local_loopback_ip_prefix_length
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Prefix length for local_loopback_ip_addr.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Prefix length for local_loopback_ip_addr.

            DEFAULT
             None
        Constants Available: LOCAL_LOOPBACK_IP_PREFIX_LENGTH_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_LOOPBACK_IP_PREFIX_LENGTH_CMD : numeric})

    def emulation_bgp_config_local_router_id(self, ipv4):
        """
        This is the method the command: emulation_bgp_config option local_router_id
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            BGP4 router ID of the emulated node, must be in IPv4 format.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            BGP4 router ID of the emulated node, must be in IPv4 format.

            DEFAULT
             None
        Constants Available: LOCAL_ROUTER_ID_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_ROUTER_ID_CMD : ipv4})

    def emulation_bgp_config_local_router_id_enable(self, bool):
        """
        This is the method the command: emulation_bgp_config option local_router_id_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Enables the BGP4 local router id option.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables the BGP4 local router id option.

            DEFAULT


            0
        Constants Available: LOCAL_ROUTER_ID_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_ROUTER_ID_ENABLE_CMD : bool})

    def emulation_bgp_config_local_router_id_step(self, ipv4):
        """
        This is the method the command: emulation_bgp_config option local_router_id_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            BGP4 router ID step of the emulated node, must be in IPv4 format.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            BGP4 router ID step of the emulated node, must be in IPv4 format.

            DEFAULT


            0.0.0.1
        Constants Available: LOCAL_ROUTER_ID_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_ROUTER_ID_STEP_CMD : ipv4})

    def emulation_bgp_config_local_router_id_type(self, opt):
        """
        This is the method the command: emulation_bgp_config option local_router_id_type
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            BGP ID Same as Router ID

            Valid options are:

            same


            new


            DEFAULT


            new
        Constants Available: LOCAL_ROUTER_ID_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.LOCAL_ROUTER_ID_TYPE_CMD : opt})

    def emulation_bgp_config_mac_address_start(self, mac):
        """
        This is the method the command: emulation_bgp_config option mac_address_start
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Initial MAC address of the interfaces created for the BGP4 neighbor.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Initial MAC address of the interfaces created for the BGP4 neighbor.

            DEFAULT
             None
        Constants Available: MAC_ADDRESS_START_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.MAC_ADDRESS_START_CMD : mac})

    def emulation_bgp_config_mac_address_step(self, mac):
        """
        This is the method the command: emulation_bgp_config option mac_address_step
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            The incrementing step for thr MAC address of the dirrectly connected interfaces created for the BGP4 neighbor.This option is valid only when IxTclNetwork API is used.

            DEFAULT


            0000.0000.0001

            IxNetwork-NGPF


            DESCRIPTION


            The incrementing step for thr MAC address of the dirrectly connected interfaces created for the BGP4 neighbor. This option is valid only when IxTclNetwork API is used.

            DEFAULT


            0000.0000.0001
        Constants Available: MAC_ADDRESS_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.MAC_ADDRESS_STEP_CMD : mac})

    def emulation_bgp_config_md5_enable(self, bool):
        """
        This is the method the command: emulation_bgp_config option md5_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If set to 1, enables MD5 authentication for emulated BGP node.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If set to 1, enables MD5 authentication for emulated BGP node.

            Valid options are:

            0


            1


            DEFAULT
             None
        Constants Available: MD5_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.MD5_ENABLE_CMD : bool})

    def emulation_bgp_config_md5_key(self, string):
        """
        This is the method the command: emulation_bgp_config option md5_key
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The key used for md5 authentication.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The key used for md5 authentication.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'md5_enable' | value= '1' |
        Constants Available: MD5_KEY_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        string --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.MD5_KEY_CMD : string})

    def emulation_bgp_config_mldp_p2mp_fec_type(self, hex):
        """
        This is the method the command: emulation_bgp_config option mldp_p2mp_fec_type
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            MLDP P2MP FEC Type (Hex)

            DEFAULT
             None
        Constants Available: MLDP_P2MP_FEC_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.MLDP_P2MP_FEC_TYPE_CMD : hex})

    def emulation_bgp_config_mode(self, opt):
        """
        This is the method the command: emulation_bgp_config option mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This option defines the action to be taken on the BGP server.

            Valid options are:

            enable


            enable and/or create the BGP4 configuration. If -handle is specified, then it will be enabled, otherwise created.

            delete


            delete the BGP4 configuration, requires the use of -handle.

            disable


            disable the BGP4 configuration, requires the use of -handle.

            modify


            modify the BGP4 configuration, requires the use of -handle.

            reset


            deletes all BGP4 configurations from the -port_handle and then creates the provided BGP4 configuration.

            DEFAULT
             None

            IxNetwork-NGPF [M]


            DESCRIPTION


            This option defines the action to be taken on the BGP server.

            Valid options are:

            delete


            delete the BGP4 configuration, requires the use of -handle.

            disable


            disable the BGP4 configuration, requires the use of -handle.

            enable


            enable and/or create the BGP4 configuration. If -handle is specified, then it will be enabled, otherwise created.

            create


            create the BGP configuration

            modify


            modify the BGP4 configuration, requires the use of -handle.

            reset


            deletes all BGP4 configurations from the -port_handle and then creates the provided BGP4 configuration.

            DEFAULT
             None
        Constants Available: MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.MODE_CMD : opt})

    def emulation_bgp_config_modify_outgoing_as_path(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option modify_outgoing_as_path
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Moved to emulation_bgp_route_config under AS Path configuration.

            DEFAULT
             Not supported

            IxNetwork-NGPF


            DESCRIPTION


            Moved to emulation_bgp_route_config under AS Path configuration.

            DEFAULT
             Not supported
        Constants Available: MODIFY_OUTGOING_AS_PATH_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.MODIFY_OUTGOING_AS_PATH_CMD : not_supported})

    def emulation_bgp_config_neighbor_type(self, opt):
        """
        This is the method the command: emulation_bgp_config option neighbor_type
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Sets the BGP neighbor type.

            Valid options are:

            internal


            iBGP

            external


            eBGP

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Sets the BGP neighbor type.

            Valid options are:

            internal


            iBGP

            external


            eBGP

            DEFAULT
             None
        Constants Available: NEIGHBOR_TYPE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.NEIGHBOR_TYPE_CMD : opt})

    def emulation_bgp_config_netmask(self, numeric):
        """
        This is the method the command: emulation_bgp_config option netmask
        Description:Supported platforms  Details
            RANGE 1 - 128
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Mask of the IP address for the interface configuration.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Mask of the IP address for the interface configuration.

            DEFAULT
             None
        Constants Available: NETMASK_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.NETMASK_CMD : numeric})

    def emulation_bgp_config_next_hop_enable(self, opt):
        """
        This is the method the command: emulation_bgp_config option next_hop_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This option is used for IPv4 traffic, and enables the use of the BGP NEXT_HOP attributes. When enabled, the IP next hop must be configured (using the -next_hop_ip option).

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            This option is used for IPv4 traffic, and enables the use of the BGP NEXT_HOP attributes. When enabled, the IP next hop must be configured (using the -next_hop_ip option).

            Valid options are:

            0


            1


            DEFAULT


            1
        Constants Available: NEXT_HOP_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.NEXT_HOP_ENABLE_CMD : opt})

    def emulation_bgp_config_next_hop_ip(self, ip):
        """
        This is the method the command: emulation_bgp_config option next_hop_ip
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Defines the IP of the next hop. This option is used if the flag -next_hop_enable is set.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Defines the IP of the next hop. This option is used if the flag -next_hop_enable is set.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'next_hop_enable' | value= '1' |
        Constants Available: NEXT_HOP_IP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.NEXT_HOP_IP_CMD : ip})

    def emulation_bgp_config_no_write(self, flag):
        """
        This is the method the command: emulation_bgp_config option no_write
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If this option is present, the configuration is not written to the hardware. This option can be used to queue up multiple configurations before writing to the hardware.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If this option is present, the configuration is not written to the hardware. This option can be used to queue up multiple configurations before writing to the hardware.

            DEFAULT
             None
        Constants Available: NO_WRITE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.NO_WRITE_CMD : flag})

    def emulation_bgp_config_override_existence_check(self, bool):
        """
        This is the method the command: emulation_bgp_config option override_existence_check
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If this option is enabled, the interface existence check is skipped but the list of interfaces is still created and maintained in order to keep track of existing interfaces if required. Using this option will speed up the interfaces' creation.

            DEFAULT


            0

            IxNetwork-NGPF


            DESCRIPTION


            If this option is enabled, the interface existence check is skipped but the list of interfaces is still created and maintained in order to keep track of existing interfaces if required. Using this option will speed up the interfaces' creation.

            DEFAULT


            0
        Constants Available: OVERRIDE_EXISTENCE_CHECK_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.OVERRIDE_EXISTENCE_CHECK_CMD : bool})

    def emulation_bgp_config_override_tracking(self, bool):
        """
        This is the method the command: emulation_bgp_config option override_tracking
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If this option is enabled, the list of interfaces won't be created and maintained anymore, thus, speeding up the interfaces' creation even more. Also, it will enable -override_existence_check in case it wasn't already enabled because checking for interface existence becomes impossible if the the list of interfaces doesn't exist anymore.

            DEFAULT


            0

            IxNetwork-NGPF


            DESCRIPTION


            If this option is enabled, the list of interfaces won?t be created and maintained anymore, thus, speeding up the interfaces' creation even more. Also, it will enable -override_existence_check in case it wasn?t already enabled because checking for interface existence becomes impossible if the the list of interfaces doesn?t exist anymore.

            DEFAULT


            0
        Constants Available: OVERRIDE_TRACKING_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.OVERRIDE_TRACKING_CMD : bool})

    def emulation_bgp_config_port_handle(self, port):
        """
        This is the method the command: emulation_bgp_config option port_handle
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The port on which the BGP neighbor is to be created.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The port on which the BGP neighbor is to be created.

            DEFAULT
             None
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.PORT_HANDLE_CMD : port})

    def emulation_bgp_config_remote_addr_step(self, ip):
        """
        This is the method the command: emulation_bgp_config option remote_addr_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Defines the mask and increment step for the next -remote_ip_addr or ""-remote_ipv6_addr"".(DEFAULT = 0.1.0.0 | 0:0:0:0:1::0)

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Defines the mask and increment step for the next -remote_ip_addr or ""-remote_ipv6_addr"".

            DEFAULT
             None
        Constants Available: REMOTE_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.REMOTE_ADDR_STEP_CMD : ip})

    def emulation_bgp_config_remote_as(self, numeric):
        """
        This is the method the command: emulation_bgp_config option remote_as
        Description:Supported platforms  Details
            RANGE 0 - 4294967295

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The remote AS.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The remote AS. Not supported reason: not supported in NGPF, deprecated in legacy

            DEFAULT
             None
        Constants Available: REMOTE_AS_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.REMOTE_AS_CMD : numeric})

    def emulation_bgp_config_remote_confederation_member(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option remote_confederation_member
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Moved to emulation_bgp_route_config under AS Path configuration.

            DEFAULT
             Not supported

            IxNetwork-NGPF


            DESCRIPTION


            Moved to emulation_bgp_route_config under AS Path configuration.

            DEFAULT
             Not supported
        Constants Available: REMOTE_CONFEDERATION_MEMBER_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.REMOTE_CONFEDERATION_MEMBER_CMD : not_supported})

    def emulation_bgp_config_remote_ip_addr(self, ipv4):
        """
        This is the method the command: emulation_bgp_config option remote_ip_addr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The IPv4 address of the DUTs interface connected to the emulated BGP port.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The IPv4 address of the DUTs interface connected to the emulated BGP port.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ip_version' | value= '4' |
        Constants Available: REMOTE_IP_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.REMOTE_IP_ADDR_CMD : ipv4})

    def emulation_bgp_config_remote_ipv6_addr(self, ipv6):
        """
        This is the method the command: emulation_bgp_config option remote_ipv6_addr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The IPv6 address of the DUT interface connected to emulated BGP node.This parameter is mandatory when -mode is create, -ip_version is 6 and parameter -neighbor_type is external, or -neighbor_type is internal and ipv4_mpls_nlri, ipv6_mpls_nlri, ipv4_mpls_vpn_nlri, and ipv6_mpls_vpn_nlri are not enabled.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The IPv6 address of the DUT interface connected to emulated BGP node. This parameter is mandatory when -mode is create, -ip_version is 6 and parameter -neighbor_type is external, or -neighbor_type is internal and ipv4_mpls_nlri, ipv6_mpls_nlri, ipv4_mpls_vpn_nlri, and ipv6_mpls_vpn_nlri are not enabled.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ip_version' | value= '6' |
        Constants Available: REMOTE_IPV6_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.REMOTE_IPV6_ADDR_CMD : ipv6})

    def emulation_bgp_config_remote_loopback_ip_addr(self, ip):
        """
        This is the method the command: emulation_bgp_config option remote_loopback_ip_addr
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Required when the -ipv4_mpls_vpn_nlri option is used.This parameter is mandatory when -mode is create, and parameter -neighbor_type is internal and and ipv4_mpls_nlri, ipv6_mpls_nlri, ipv4_mpls_vpn_nlri, and ipv6_mpls_vpn_nlri are enabled.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Required when the -ipv4_mpls_vpn_nlri option is used. This parameter is mandatory when -mode is create, and parameter -neighbor_type is internal and and ipv4_mpls_nlri, ipv6_mpls_nlri, ipv4_mpls_vpn_nlri, and ipv6_mpls_vpn_nlri are enabled.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4_mpls_vpn_nlri' | value= '' |
        Constants Available: REMOTE_LOOPBACK_IP_ADDR_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.REMOTE_LOOPBACK_IP_ADDR_CMD : ip})

    def emulation_bgp_config_remote_loopback_ip_addr_step(self, ip):
        """
        This is the method the command: emulation_bgp_config option remote_loopback_ip_addr_step
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Required when the -ipv4_mpls_vpn_nlri option is used.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Required when the -ipv4_mpls_vpn_nlri option is used.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'ipv4_mpls_vpn_nlri' | value= '' |
        Constants Available: REMOTE_LOOPBACK_IP_ADDR_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.REMOTE_LOOPBACK_IP_ADDR_STEP_CMD : ip})

    def emulation_bgp_config_request_vpn_label_exchange_over_lsp(self, bool):
        """
        This is the method the command: emulation_bgp_config option request_vpn_label_exchange_over_lsp
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Request VPN Label Exchange over LSP

            DEFAULT
             None
        Constants Available: REQUEST_VPN_LABEL_EXCHANGE_OVER_LSP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.REQUEST_VPN_LABEL_EXCHANGE_OVER_LSP_CMD : bool})

    def emulation_bgp_config_reset(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option reset
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Clears any BGP4 configuration on the targeted port before configuring further.

            DEFAULT
             Not supported

            IxNetwork-NGPF


            DESCRIPTION


            Clears any BGP4 configuration on the targeted port before configuring further.

            DEFAULT
             Not supported
        Constants Available: RESET_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.RESET_CMD : not_supported})

    def emulation_bgp_config_restart_time(self, numeric):
        """
        This is the method the command: emulation_bgp_config option restart_time
        Description:Supported platforms  Details
            RANGE 0 - 10000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If -graceful_restart_enable is set, sets the amount of time following a restart operation allowed to re-establish a BGP session, in seconds.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If -graceful_restart_enable is set, sets the amount of time following a restart operation allowed to re-establish a BGP session, in seconds.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'graceful_restart_enable' | value= '1' |
        Constants Available: RESTART_TIME_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.RESTART_TIME_CMD : numeric})

    def emulation_bgp_config_retries(self, numeric):
        """
        This is the method the command: emulation_bgp_config option retries
        Description:Supported platforms  Details
            RANGE 0 - 10000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            For External BGP neighbor. The number of times to attempt an OPEN connection with the DUT routers before giving up.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            For External BGP neighbor. The number of times to attempt an OPEN connection with the DUT routers before giving up. Not supported reason: not supported in NGPF

            DEFAULT
             None
        Constants Available: RETRIES_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.RETRIES_CMD : numeric})

    def emulation_bgp_config_retry_time(self, numeric):
        """
        This is the method the command: emulation_bgp_config option retry_time
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            For External BGP neighbor. When retries are necessary, the delay in seconds between retries.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            For External BGP neighbor. When retries are necessary, the delay in seconds between retries. Not supported reason: not supported in NGPF

            DEFAULT
             None
        Constants Available: RETRY_TIME_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.RETRY_TIME_CMD : numeric})

    def emulation_bgp_config_route_refresh(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option route_refresh
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Details needed.

            DEFAULT
             Not supported

            IxNetwork-NGPF


            DESCRIPTION


            Details needed.

            DEFAULT
             Not supported
        Constants Available: ROUTE_REFRESH_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ROUTE_REFRESH_CMD : not_supported})

    def emulation_bgp_config_routes_per_msg(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option routes_per_msg
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Not supported

            DEFAULT
             Not supported

            IxNetwork-NGPF


            DESCRIPTION


            Not supported

            DEFAULT
             Not supported
        Constants Available: ROUTES_PER_MSG_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.ROUTES_PER_MSG_CMD : not_supported})

    def emulation_bgp_config_send_ixia_signature_with_routes(self, bool):
        """
        This is the method the command: emulation_bgp_config option send_ixia_signature_with_routes
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Send Ixia Signature With Routes

            DEFAULT


            0
        Constants Available: SEND_IXIA_SIGNATURE_WITH_ROUTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.SEND_IXIA_SIGNATURE_WITH_ROUTES_CMD : bool})

    def emulation_bgp_config_staggered_start_enable(self, flag):
        """
        This is the method the command: emulation_bgp_config option staggered_start_enable
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Enables staggered start of neighbors.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Enables staggered start of neighbors.

            DEFAULT
             None
        Constants Available: STAGGERED_START_ENABLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.STAGGERED_START_ENABLE_CMD : flag})

    def emulation_bgp_config_staggered_start_time(self, numeric):
        """
        This is the method the command: emulation_bgp_config option staggered_start_time
        Description:Supported platforms  Details
            RANGE 0 - 10000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            When the -staggered_start_enable flag is used, this is the duration of the start process in seconds.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            When the -staggered_start_enable flag is used, this is the duration of the start process in seconds.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'staggered_start_time' | value= '1' |
        Constants Available: STAGGERED_START_TIME_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.STAGGERED_START_TIME_CMD : numeric})

    def emulation_bgp_config_stale_time(self, numeric):
        """
        This is the method the command: emulation_bgp_config option stale_time
        Description:Supported platforms  Details
            RANGE 0 - 10000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If -graceful_restart_enable is set, sets the amount of time after which an End-Of-RIB marker is sent in an Update message to the peer to allow time for routing convergence via IGP and BGP selection, in seconds. Stale routing information for that address family is then deleted by the receiving peer.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            If -graceful_restart_enable is set, sets the amount of time after which an End-Of-RIB marker is sent in an Update message to the peer to allow time for routing convergence via IGP and BGP selection, in seconds. Stale routing information for that address family is then deleted by the receiving peer.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'graceful_restart_enable' | value= '1' |
        Constants Available: STALE_TIME_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.STALE_TIME_CMD : numeric})

    def emulation_bgp_config_start_rate(self, numeric):
        """
        This is the method the command: emulation_bgp_config option start_rate
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Number of times an action is triggered per time interval

            DEFAULT
             None
        Constants Available: START_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.START_RATE_CMD : numeric})

    def emulation_bgp_config_start_rate_enable(self, bool):
        """
        This is the method the command: emulation_bgp_config option start_rate_enable
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Enable bgp globals start rate

            DEFAULT
             None
        Constants Available: START_RATE_ENABLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.START_RATE_ENABLE_CMD : bool})

    def emulation_bgp_config_start_rate_interval(self, numeric):
        """
        This is the method the command: emulation_bgp_config option start_rate_interval
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Time interval used to calculate the rate for triggering an action (rate = count/interval)

            DEFAULT
             None
        Constants Available: START_RATE_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.START_RATE_INTERVAL_CMD : numeric})

    def emulation_bgp_config_start_rate_scale_mode(self, port):
        """
        This is the method the command: emulation_bgp_config option start_rate_scale_mode
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Indicates whether the control is specified per port or per device group

            Valid options are:

            deviceGroup


            The values regarding start rate are mapped per device group

            port


            The values regarding start rate are mapped per port

            DEFAULT
             None
        Constants Available: START_RATE_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.START_RATE_SCALE_MODE_CMD : port})

    def emulation_bgp_config_stop_rate(self, numeric):
        """
        This is the method the command: emulation_bgp_config option stop_rate
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Number of times an action is triggered per time interval

            DEFAULT
             None
        Constants Available: STOP_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.STOP_RATE_CMD : numeric})

    def emulation_bgp_config_stop_rate_enable(self, bool):
        """
        This is the method the command: emulation_bgp_config option stop_rate_enable
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Enable bgp globals stop rate

            DEFAULT
             None
        Constants Available: STOP_RATE_ENABLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.STOP_RATE_ENABLE_CMD : bool})

    def emulation_bgp_config_stop_rate_interval(self, numeric):
        """
        This is the method the command: emulation_bgp_config option stop_rate_interval
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Time interval used to calculate the rate for triggering an action (rate = count/interval)

            DEFAULT
             None
        Constants Available: STOP_RATE_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.STOP_RATE_INTERVAL_CMD : numeric})

    def emulation_bgp_config_stop_rate_scale_mode(self, port):
        """
        This is the method the command: emulation_bgp_config option stop_rate_scale_mode
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Indicates whether the control is specified per port or per device group

            Valid options are:

            deviceGroup


            The values regarding stop rate are mapped per device group

            port


            The values regarding stop rate are mapped per port

            DEFAULT
             None
        Constants Available: STOP_RATE_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.STOP_RATE_SCALE_MODE_CMD : port})

    def emulation_bgp_config_suppress_notify(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option suppress_notify
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            If set to 1, suppresses, the notification message sent to the peer. if set to 0, does not suppress the notification message sent to the peer.

            DEFAULT
             Not supported

            IxNetwork-NGPF


            DESCRIPTION


            If set to 1, suppresses, the notification message sent to the peer. if set to 0, does not suppress the notification message sent to the peer.

            DEFAULT
             Not supported
        Constants Available: SUPPRESS_NOTIFY_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.SUPPRESS_NOTIFY_CMD : not_supported})

    def emulation_bgp_config_tcp_window_size(self, numeric):
        """
        This is the method the command: emulation_bgp_config option tcp_window_size
        Description:Supported platforms  Details
            RANGE 0 - 10000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            For External BGP neighbor only. The TCP window used for communications from the neighbor.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            For External BGP neighbor only. The TCP window used for communications from the neighbor.

            DEFAULT
             None
        Constants Available: TCP_WINDOW_SIZE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.TCP_WINDOW_SIZE_CMD : numeric})

    def emulation_bgp_config_timeout(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option timeout
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Not supported

            DEFAULT
             Not supported

            IxNetwork-NGPF


            DESCRIPTION


            Not supported

            DEFAULT
             Not supported
        Constants Available: TIMEOUT_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.TIMEOUT_CMD : not_supported})

    def emulation_bgp_config_trigger_vpls_pw_initiation(self, bool):
        """
        This is the method the command: emulation_bgp_config option trigger_vpls_pw_initiation
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Trigger VPLS PW Initiation

            DEFAULT
             None
        Constants Available: TRIGGER_VPLS_PW_INITIATION_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.TRIGGER_VPLS_PW_INITIATION_CMD : bool})

    def emulation_bgp_config_ttl_value(self, numeric):
        """
        This is the method the command: emulation_bgp_config option ttl_value
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This attribute represents the limited number of iterations that a unit of data can experience before the data is discarded.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            This attribute represents the limited number of iterations that a unit of data can experience before the data is discarded.

            DEFAULT
             None
        Constants Available: TTL_VALUE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.TTL_VALUE_CMD : numeric})

    def emulation_bgp_config_update_interval(self, numeric):
        """
        This is the method the command: emulation_bgp_config option update_interval
        Description:Supported platforms  Details
            RANGE 0 - 65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The time intervals at which UPDATE messages are sent to the DUT, expressed in the number of milliseconds between UPDATE messages.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The time intervals at which UPDATE messages are sent to the DUT, expressed in the number of milliseconds between UPDATE messages.

            DEFAULT
             None
        Constants Available: UPDATE_INTERVAL_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.UPDATE_INTERVAL_CMD : numeric})

    def emulation_bgp_config_update_msg_size(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option update_msg_size
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Maximum size (bytes) of the UPDATE message transmitted by emulated router node.

            DEFAULT
             Not supported

            IxNetwork-NGPF


            DESCRIPTION


            Maximum size (bytes) of the UPDATE message transmitted by emulated router node.

            DEFAULT
             Not supported
        Constants Available: UPDATE_MSG_SIZE_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.UPDATE_MSG_SIZE_CMD : not_supported})

    def emulation_bgp_config_updates_per_iteration(self, numeric):
        """
        This is the method the command: emulation_bgp_config option updates_per_iteration
        Description:Supported platforms  Details
            RANGE 0 - 10000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            When the protocol server operates on older ports that do not possess a local processor, this tuning parameter controls how many UPDATE messages are sent at a time. When many routers are being simulated on such a port, changing this value may help to increase or decrease performance.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            When the protocol server operates on older ports that do not possess a local processor, this tuning parameter controls how many UPDATE messages are sent at a time. When many routers are being simulated on such a port, changing this value may help to increase or decrease performance.

            DEFAULT
             None
        Constants Available: UPDATES_PER_ITERATION_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.UPDATES_PER_ITERATION_CMD : numeric})

    def emulation_bgp_config_vci(self, numeric):
        """
        This is the method the command: emulation_bgp_config option vci
        Description:Supported platforms  Details
            RANGE 0 - 65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            VCI for emulated router node. RANGE 0-65535

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            VCI for emulated router node. RANGE 0-65535

            DEFAULT
             None
        Constants Available: VCI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VCI_CMD : numeric})

    def emulation_bgp_config_vci_step(self, numeric):
        """
        This is the method the command: emulation_bgp_config option vci_step
        Description:Supported platforms  Details
            RANGE 0 - 65535
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The step value used for incrementing the -vci option. RANGE 0-65535 When vci_step causes the vci value to exceed it's maximum value the increment will be done modulo .Examples: vci = 65534; vci_step = 2 -> new vci value = 0vci = 65535; vci_step = 11 -> new vci value = 10

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The step value used for incrementing the -vci option. RANGE 0-65535 When vci_step causes the vci value to exceed it's maximum value the increment will be done modulo . Examples: vci = 65534; vci_step = 2 -> new vci value = 0 vci = 65535; vci_step = 11 -> new vci value = 10

            DEFAULT
             None
        Constants Available: VCI_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VCI_STEP_CMD : numeric})

    def emulation_bgp_config_vlan(self, bool):
        """
        This is the method the command: emulation_bgp_config option vlan
        Description:Supported platforms  Details

            IxNetwork


            DESCRIPTION


            Enables vlan on the directly connected BGP router interface. Valid options are:

            Valid options are:

            0


            disable

            1


            enable.This option is valid only when -mode is create or -mode is modify and -handle is a BGP router handle.This option is available only when IxNetwork tcl API is used.

            DEFAULT


            0

            IxNetwork-NGPF


            DESCRIPTION


            Enables vlan on the directly connected BGP router interface. Valid options are: 0 - disable, 1 - enable. This option is valid only when -mode is create or -mode is modify and -handle is a BGP router handle. This option is available only when IxNetwork tcl API is used.

            DEFAULT


            0

            DEPENDENCIES


            Valid in combination with parameter(s)
            'mode' | value= 'create' |
            'mode' | value= 'modify' |
        Constants Available: VLAN_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        bool --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VLAN_CMD : bool})

    def emulation_bgp_config_vlan_cfi(self, not_supported):
        """
        This is the method the command: emulation_bgp_config option vlan_cfi
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            Canonical format indicator field in VLAN for emulated router node.

            DEFAULT
             Not supported
        Constants Available: VLAN_CFI_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VLAN_CFI_CMD : not_supported})

    def emulation_bgp_config_vlan_id(self, numeric):
        """
        This is the method the command: emulation_bgp_config option vlan_id
        Description:Supported platforms  Details
            RANGE 0 - 4095
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            VLAN ID for the emulated router node.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            VLAN ID for the emulated router node.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vlan' | value= '1' |
        Constants Available: VLAN_ID_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VLAN_ID_CMD : numeric})

    def emulation_bgp_config_vlan_id_mode(self, opt):
        """
        This is the method the command: emulation_bgp_config option vlan_id_mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            For multiple neighbor configuration, configurest the VLAN ID mode. Valid options are:fixedincrement

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            For multiple neighbor configuration, configurest the VLAN ID mode.

            Valid options are:

            fixed


            increment


            DEFAULT


            increment

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vlan' | value= '1' |
        Constants Available: VLAN_ID_MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VLAN_ID_MODE_CMD : opt})

    def emulation_bgp_config_vlan_id_step(self, numeric):
        """
        This is the method the command: emulation_bgp_config option vlan_id_step
        Description:Supported platforms  Details
            RANGE 0 - 4096
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            Defines the step for every VLAN When -vlan_id_mode is set to increment.When vlan_id_step causes the vlan_id value to exceed it's maximum value the increment will be done modulo .Examples: vlan_id = 4094; vlan_id_step = 2 -> new vlan_id value = 0vlan_id = 4095; vlan_id_step = 11 -> new vlan_id value = 10

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            Defines the step for every VLAN When -vlan_id_mode is set to increment. When vlan_id_step causes the vlan_id value to exceed it's maximum value the increment will be done modulo . Examples: vlan_id = 4094; vlan_id_step = 2 -> new vlan_id value = 0 vlan_id = 4095; vlan_id_step = 11 -> new vlan_id value = 10

            DEFAULT


            1

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vlan' | value= '1' |
            'vlan_id_mode' | value= 'increment' |
        Constants Available: VLAN_ID_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VLAN_ID_STEP_CMD : numeric})

    def emulation_bgp_config_vlan_user_priority(self, numeric):
        """
        This is the method the command: emulation_bgp_config option vlan_user_priority
        Description:Supported platforms  Details
            RANGE 0 - 7
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The VLAN user priority assigned to emulated router node.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The VLAN user priority assigned to emulated router node.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'vlan' | value= '1' |
        Constants Available: VLAN_USER_PRIORITY_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VLAN_USER_PRIORITY_CMD : numeric})

    def emulation_bgp_config_vpi(self, numeric):
        """
        This is the method the command: emulation_bgp_config option vpi
        Description:Supported platforms  Details
            RANGE 0 - 255
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            VPI for emulated router node. RANGE 0-255

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            VPI for emulated router node. RANGE 0-255

            DEFAULT
             None
        Constants Available: VPI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VPI_CMD : numeric})

    def emulation_bgp_config_vpi_step(self, numeric):
        """
        This is the method the command: emulation_bgp_config option vpi_step
        Description:Supported platforms  Details
            RANGE 0 - 255
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The step value used for incrementing the -vpi option. RANGE 0-255When vpi_step causes the vpi value to exceed it's maximum value the increment will be done modulo .Examples: vpi = 254; vpi_step = 2 -> new vpi value = 0vpi = 255; vpi_step = 11 -> new vpi value = 10

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The step value used for incrementing the -vpi option. RANGE 0-255 When vpi_step causes the vpi value to exceed it's maximum value the increment will be done modulo . Examples: vpi = 254; vpi_step = 2 -> new vpi value = 0 vpi = 255; vpi_step = 11 -> new vpi value = 10

            DEFAULT
             None
        Constants Available: VPI_STEP_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VPI_STEP_CMD : numeric})

    def emulation_bgp_config_vpls(self, opt):
        """
        This is the method the command: emulation_bgp_config option vpls
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

            Valid options are:

            0


            disabled

            1


            enabled

            DEFAULT


            0

            IxNetwork-NGPF


            DESCRIPTION


            (deprecated) This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled. Valid choices are: 0 - disabled 1 - enabled

            Valid options are:

            0


            1


            disabled


            vpn


            no_vpn


            DEFAULT


            0
        Constants Available: VPLS_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VPLS_CMD : opt})

    def emulation_bgp_config_vpls_capability_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option vpls_capability_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

            DEFAULT
             None
        Constants Available: VPLS_CAPABILITY_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VPLS_CAPABILITY_NLRI_CMD : flag})

    def emulation_bgp_config_vpls_filter_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option vpls_filter_nlri
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

            DEFAULT
             None
        Constants Available: VPLS_FILTER_NLRI_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VPLS_FILTER_NLRI_CMD : flag})

    def emulation_bgp_config_vpls_nlri(self, flag):
        """
        This is the method the command: emulation_bgp_config option vpls_nlri
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

            DEFAULT
             None
        Constants Available: VPLS_NLRI_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_bgp_config({EmulationBgpConfigConstants.VPLS_NLRI_CMD : flag})


"""
    This is the Constants class for the command: emulation_bgp_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationBgpConfigConstants:
    """
    init function
    """
    def __init__(self):
        pass
    # api reference constant for this api to get it from the device
    EMULATION_BGP_CONFIG_API = "EMULATION_BGP_CONFIG_API"

    ARGUMENTS_CMD = "Arguments"
    # Constant values for ARGUMENTS_CMD
    ARGUMENTS_CONSTANTS = "Constants"

    ACT_AS_RESTARTED_CMD = "act_as_restarted"
    # Constant values for ACT_AS_RESTARTED_CMD
    ACT_AS_RESTARTED_0 = "0"
    ACT_AS_RESTARTED_1 = "1"

    ACTIVE_CMD = "active"
    # Constant values for ACTIVE_CMD
    ACTIVE_0 = "0"
    ACTIVE_1 = "1"

    ACTIVE_CONNECT_ENABLE_CMD = "active_connect_enable"

    ADVERTISE_END_OF_RIB_CMD = "advertise_end_of_rib"
    # Constant values for ADVERTISE_END_OF_RIB_CMD
    ADVERTISE_END_OF_RIB_0 = "0"
    ADVERTISE_END_OF_RIB_1 = "1"

    ADVERTISE_HOST_ROUTE_CMD = "advertise_host_route"

    ATM_ENCAPSULATION_CMD = "atm_encapsulation"
    # Constant values for ATM_ENCAPSULATION_CMD
    ATM_ENCAPSULATION_VCCMUXIPV4ROUTED = "VccMuxIPV4Routed"
    ATM_ENCAPSULATION_VCCMUXIPV6ROUTED = "VccMuxIPV6Routed"
    ATM_ENCAPSULATION_VCCMUXBRIDGEDETHERNETFCS = "VccMuxBridgedEthernetFCS"
    ATM_ENCAPSULATION_VCCMUXBRIDGEDETHERNETNOFCS = "VccMuxBridgedEthernetNoFCS"
    ATM_ENCAPSULATION_LLCROUTEDCLIP = "LLCRoutedCLIP"
    ATM_ENCAPSULATION_LLCBRIDGEDETHERNETFCS = "LLCBridgedEthernetFCS"
    ATM_ENCAPSULATION_LLCBRIDGEDETHERNETNOFCS = "LLCBridgedEthernetNoFCS"

    BFD_REGISTRATION_CMD = "bfd_registration"
    # Constant values for BFD_REGISTRATION_CMD
    BFD_REGISTRATION_0 = "0"
    BFD_REGISTRATION_1 = "1"

    BFD_REGISTRATION_MODE_CMD = "bfd_registration_mode"
    # Constant values for BFD_REGISTRATION_MODE_CMD
    BFD_REGISTRATION_MODE_SINGLE_HOP = "single_hop"
    BFD_REGISTRATION_MODE_MULTI_HOP = "multi_hop"

    CAPABILITY_ROUTE_CONSTRAINT_CMD = "capability_route_constraint"
    # Constant values for CAPABILITY_ROUTE_CONSTRAINT_CMD
    CAPABILITY_ROUTE_CONSTRAINT_0 = "0"
    CAPABILITY_ROUTE_CONSTRAINT_1 = "1"

    CAPABILITY_ROUTE_REFRESH_CMD = "capability_route_refresh"
    # Constant values for CAPABILITY_ROUTE_REFRESH_CMD
    CAPABILITY_ROUTE_REFRESH_0 = "0"
    CAPABILITY_ROUTE_REFRESH_1 = "1"

    CONFIGURE_KEEPALIVE_TIMER_CMD = "configure_keepalive_timer"
    # Constant values for CONFIGURE_KEEPALIVE_TIMER_CMD
    CONFIGURE_KEEPALIVE_TIMER_0 = "0"
    CONFIGURE_KEEPALIVE_TIMER_1 = "1"

    COUNT_CMD = "count"

    DISABLE_RECEIVED_UPDATE_VALIDATION_CMD = "disable_received_update_validation"
    # Constant values for DISABLE_RECEIVED_UPDATE_VALIDATION_CMD
    DISABLE_RECEIVED_UPDATE_VALIDATION_0 = "0"
    DISABLE_RECEIVED_UPDATE_VALIDATION_1 = "1"

    DISCARD_IXIA_GENERATED_ROUTES_CMD = "discard_ixia_generated_routes"
    # Constant values for DISCARD_IXIA_GENERATED_ROUTES_CMD
    DISCARD_IXIA_GENERATED_ROUTES_0 = "0"
    DISCARD_IXIA_GENERATED_ROUTES_1 = "1"

    ENABLE_4_BYTE_AS_CMD = "enable_4_byte_as"
    # Constant values for ENABLE_4_BYTE_AS_CMD
    ENABLE_4_BYTE_AS_0 = "0"
    ENABLE_4_BYTE_AS_1 = "1"

    ENABLE_AD_VPLS_PREFIX_LENGTH_CMD = "enable_ad_vpls_prefix_length"
    # Constant values for ENABLE_AD_VPLS_PREFIX_LENGTH_CMD
    ENABLE_AD_VPLS_PREFIX_LENGTH_0 = "0"
    ENABLE_AD_VPLS_PREFIX_LENGTH_1 = "1"

    ENABLE_FLAP_CMD = "enable_flap"
    # Constant values for ENABLE_FLAP_CMD
    ENABLE_FLAP_0 = "0"
    ENABLE_FLAP_1 = "1"

    FLAP_DOWN_TIME_CMD = "flap_down_time"

    FLAP_UP_TIME_CMD = "flap_up_time"

    GATEWAY_IP_ADDR_CMD = "gateway_ip_addr"

    GRACEFUL_RESTART_ENABLE_CMD = "graceful_restart_enable"
    # Constant values for GRACEFUL_RESTART_ENABLE_CMD
    GRACEFUL_RESTART_ENABLE_0 = "0"
    GRACEFUL_RESTART_ENABLE_1 = "1"

    HANDLE_CMD = "handle"
    # Constant values for HANDLE_CMD
    HANDLE_DELETE = "delete"
    HANDLE_DISABLE = "disable"
    HANDLE_ENABLE = "enable"
    HANDLE_CREATE = "create"
    HANDLE_MODIFY = "modify"
    HANDLE_RESET = "reset"

    HOLD_TIME_CMD = "hold_time"

    IBGP_TESTER_AS_FOUR_BYTES_CMD = "ibgp_tester_as_four_bytes"

    IBGP_TESTER_AS_TWO_BYTES_CMD = "ibgp_tester_as_two_bytes"

    INITIATE_EBGP_ACTIVE_CONNECTION_CMD = "initiate_ebgp_active_connection"
    # Constant values for INITIATE_EBGP_ACTIVE_CONNECTION_CMD
    INITIATE_EBGP_ACTIVE_CONNECTION_0 = "0"
    INITIATE_EBGP_ACTIVE_CONNECTION_1 = "1"

    INITIATE_IBGP_ACTIVE_CONNECTION_CMD = "initiate_ibgp_active_connection"
    # Constant values for INITIATE_IBGP_ACTIVE_CONNECTION_CMD
    INITIATE_IBGP_ACTIVE_CONNECTION_0 = "0"
    INITIATE_IBGP_ACTIVE_CONNECTION_1 = "1"

    INTERFACE_HANDLE_CMD = "interface_handle"

    IP_VERSION_CMD = "ip_version"
    # Constant values for IP_VERSION_CMD
    IP_VERSION_4 = "4"
    IP_VERSION_6 = "6"

    IPV4_CAPABILITY_MDT_NLRI_CMD = "ipv4_capability_mdt_nlri"

    IPV4_CAPABILITY_MPLS_NLRI_CMD = "ipv4_capability_mpls_nlri"

    IPV4_CAPABILITY_MPLS_VPN_NLRI_CMD = "ipv4_capability_mpls_vpn_nlri"

    IPV4_CAPABILITY_MULTICAST_NLRI_CMD = "ipv4_capability_multicast_nlri"

    IPV4_CAPABILITY_MULTICAST_VPN_NLRI_CMD = "ipv4_capability_multicast_vpn_nlri"

    IPV4_CAPABILITY_UNICAST_NLRI_CMD = "ipv4_capability_unicast_nlri"

    IPV4_FILTER_MPLS_NLRI_CMD = "ipv4_filter_mpls_nlri"

    IPV4_FILTER_MPLS_VPN_NLRI_CMD = "ipv4_filter_mpls_vpn_nlri"

    IPV4_FILTER_MULTICAST_NLRI_CMD = "ipv4_filter_multicast_nlri"

    IPV4_FILTER_MULTICAST_VPN_NLRI_CMD = "ipv4_filter_multicast_vpn_nlri"

    IPV4_FILTER_UNICAST_NLRI_CMD = "ipv4_filter_unicast_nlri"

    IPV4_MDT_NLRI_CMD = "ipv4_mdt_nlri"

    IPV4_MPLS_NLRI_CMD = "ipv4_mpls_nlri"

    IPV4_MPLS_VPN_NLRI_CMD = "ipv4_mpls_vpn_nlri"

    IPV4_MULTICAST_NLRI_CMD = "ipv4_multicast_nlri"

    IPV4_MULTICAST_VPN_NLRI_CMD = "ipv4_multicast_vpn_nlri"

    IPV4_UNICAST_NLRI_CMD = "ipv4_unicast_nlri"

    IPV6_CAPABILITY_MPLS_NLRI_CMD = "ipv6_capability_mpls_nlri"

    IPV6_CAPABILITY_MPLS_VPN_NLRI_CMD = "ipv6_capability_mpls_vpn_nlri"

    IPV6_CAPABILITY_MULTICAST_NLRI_CMD = "ipv6_capability_multicast_nlri"

    IPV6_CAPABILITY_MULTICAST_VPN_NLRI_CMD = "ipv6_capability_multicast_vpn_nlri"

    IPV6_CAPABILITY_UNICAST_NLRI_CMD = "ipv6_capability_unicast_nlri"

    IPV6_FILTER_MPLS_NLRI_CMD = "ipv6_filter_mpls_nlri"

    IPV6_FILTER_MPLS_VPN_NLRI_CMD = "ipv6_filter_mpls_vpn_nlri"

    IPV6_FILTER_MULTICAST_NLRI_CMD = "ipv6_filter_multicast_nlri"

    IPV6_FILTER_MULTICAST_VPN_NLRI_CMD = "ipv6_filter_multicast_vpn_nlri"

    IPV6_FILTER_UNICAST_NLRI_CMD = "ipv6_filter_unicast_nlri"

    IPV6_MPLS_NLRI_CMD = "ipv6_mpls_nlri"

    IPV6_MPLS_VPN_NLRI_CMD = "ipv6_mpls_vpn_nlri"

    IPV6_MULTICAST_NLRI_CMD = "ipv6_multicast_nlri"

    IPV6_MULTICAST_VPN_NLRI_CMD = "ipv6_multicast_vpn_nlri"

    IPV6_UNICAST_NLRI_CMD = "ipv6_unicast_nlri"

    KEEPALIVE_TIMER_CMD = "keepalive_timer"

    LOCAL_ADDR_STEP_CMD = "local_addr_step"

    LOCAL_AS_CMD = "local_as"

    LOCAL_AS4_CMD = "local_as4"

    LOCAL_AS_MODE_CMD = "local_as_mode"
    # Constant values for LOCAL_AS_MODE_CMD
    LOCAL_AS_MODE_FIXED = "fixed"
    LOCAL_AS_MODE_INCREMENT = "increment"

    LOCAL_AS_STEP_CMD = "local_as_step"

    LOCAL_IP_ADDR_CMD = "local_ip_addr"

    LOCAL_IPV6_ADDR_CMD = "local_ipv6_addr"

    LOCAL_LOOPBACK_IP_ADDR_CMD = "local_loopback_ip_addr"

    LOCAL_LOOPBACK_IP_ADDR_STEP_CMD = "local_loopback_ip_addr_step"

    LOCAL_LOOPBACK_IP_PREFIX_LENGTH_CMD = "local_loopback_ip_prefix_length"

    LOCAL_ROUTER_ID_CMD = "local_router_id"

    LOCAL_ROUTER_ID_ENABLE_CMD = "local_router_id_enable"
    # Constant values for LOCAL_ROUTER_ID_ENABLE_CMD
    LOCAL_ROUTER_ID_ENABLE_0 = "0"
    LOCAL_ROUTER_ID_ENABLE_1 = "1"

    LOCAL_ROUTER_ID_STEP_CMD = "local_router_id_step"

    LOCAL_ROUTER_ID_TYPE_CMD = "local_router_id_type"
    # Constant values for LOCAL_ROUTER_ID_TYPE_CMD
    LOCAL_ROUTER_ID_TYPE_SAME = "same"
    LOCAL_ROUTER_ID_TYPE_NEW = "new"

    MAC_ADDRESS_START_CMD = "mac_address_start"

    MAC_ADDRESS_STEP_CMD = "mac_address_step"

    MD5_ENABLE_CMD = "md5_enable"
    # Constant values for MD5_ENABLE_CMD
    MD5_ENABLE_0 = "0"
    MD5_ENABLE_1 = "1"

    MD5_KEY_CMD = "md5_key"

    MLDP_P2MP_FEC_TYPE_CMD = "mldp_p2mp_fec_type"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_DELETE = "delete"
    MODE_DISABLE = "disable"
    MODE_ENABLE = "enable"
    MODE_CREATE = "create"
    MODE_MODIFY = "modify"
    MODE_RESET = "reset"

    MODIFY_OUTGOING_AS_PATH_CMD = "modify_outgoing_as_path"

    NEIGHBOR_TYPE_CMD = "neighbor_type"
    # Constant values for NEIGHBOR_TYPE_CMD
    NEIGHBOR_TYPE_INTERNAL = "internal"
    NEIGHBOR_TYPE_EXTERNAL = "external"

    NETMASK_CMD = "netmask"

    NEXT_HOP_ENABLE_CMD = "next_hop_enable"
    # Constant values for NEXT_HOP_ENABLE_CMD
    NEXT_HOP_ENABLE_FLAG = "FLAG"
    NEXT_HOP_ENABLE_0 = "0"
    NEXT_HOP_ENABLE_1 = "1"

    NEXT_HOP_IP_CMD = "next_hop_ip"

    NO_WRITE_CMD = "no_write"

    OVERRIDE_EXISTENCE_CHECK_CMD = "override_existence_check"
    # Constant values for OVERRIDE_EXISTENCE_CHECK_CMD
    OVERRIDE_EXISTENCE_CHECK_0 = "0"
    OVERRIDE_EXISTENCE_CHECK_1 = "1"

    OVERRIDE_TRACKING_CMD = "override_tracking"
    # Constant values for OVERRIDE_TRACKING_CMD
    OVERRIDE_TRACKING_0 = "0"
    OVERRIDE_TRACKING_1 = "1"

    PORT_HANDLE_CMD = "port_handle"

    REMOTE_ADDR_STEP_CMD = "remote_addr_step"

    REMOTE_AS_CMD = "remote_as"

    REMOTE_CONFEDERATION_MEMBER_CMD = "remote_confederation_member"

    REMOTE_IP_ADDR_CMD = "remote_ip_addr"

    REMOTE_IPV6_ADDR_CMD = "remote_ipv6_addr"

    REMOTE_LOOPBACK_IP_ADDR_CMD = "remote_loopback_ip_addr"

    REMOTE_LOOPBACK_IP_ADDR_STEP_CMD = "remote_loopback_ip_addr_step"

    REQUEST_VPN_LABEL_EXCHANGE_OVER_LSP_CMD = "request_vpn_label_exchange_over_lsp"
    # Constant values for REQUEST_VPN_LABEL_EXCHANGE_OVER_LSP_CMD
    REQUEST_VPN_LABEL_EXCHANGE_OVER_LSP_0 = "0"
    REQUEST_VPN_LABEL_EXCHANGE_OVER_LSP_1 = "1"

    RESET_CMD = "reset"

    RESTART_TIME_CMD = "restart_time"

    RETRIES_CMD = "retries"

    RETRY_TIME_CMD = "retry_time"

    ROUTE_REFRESH_CMD = "route_refresh"

    ROUTES_PER_MSG_CMD = "routes_per_msg"

    SEND_IXIA_SIGNATURE_WITH_ROUTES_CMD = "send_ixia_signature_with_routes"
    # Constant values for SEND_IXIA_SIGNATURE_WITH_ROUTES_CMD
    SEND_IXIA_SIGNATURE_WITH_ROUTES_0 = "0"
    SEND_IXIA_SIGNATURE_WITH_ROUTES_1 = "1"

    STAGGERED_START_ENABLE_CMD = "staggered_start_enable"

    STAGGERED_START_TIME_CMD = "staggered_start_time"

    STALE_TIME_CMD = "stale_time"

    START_RATE_CMD = "start_rate"

    START_RATE_ENABLE_CMD = "start_rate_enable"
    # Constant values for START_RATE_ENABLE_CMD
    START_RATE_ENABLE_0 = "0"
    START_RATE_ENABLE_1 = "1"

    START_RATE_INTERVAL_CMD = "start_rate_interval"

    START_RATE_SCALE_MODE_CMD = "start_rate_scale_mode"
    # Constant values for START_RATE_SCALE_MODE_CMD
    START_RATE_SCALE_MODE_DEVICEGROUP = "deviceGroup"
    START_RATE_SCALE_MODE_PORT = "port"

    STOP_RATE_CMD = "stop_rate"

    STOP_RATE_ENABLE_CMD = "stop_rate_enable"
    # Constant values for STOP_RATE_ENABLE_CMD
    STOP_RATE_ENABLE_0 = "0"
    STOP_RATE_ENABLE_1 = "1"

    STOP_RATE_INTERVAL_CMD = "stop_rate_interval"

    STOP_RATE_SCALE_MODE_CMD = "stop_rate_scale_mode"
    # Constant values for STOP_RATE_SCALE_MODE_CMD
    STOP_RATE_SCALE_MODE_DEVICEGROUP = "deviceGroup"
    STOP_RATE_SCALE_MODE_PORT = "port"

    SUPPRESS_NOTIFY_CMD = "suppress_notify"

    TCP_WINDOW_SIZE_CMD = "tcp_window_size"

    TIMEOUT_CMD = "timeout"

    TRIGGER_VPLS_PW_INITIATION_CMD = "trigger_vpls_pw_initiation"
    # Constant values for TRIGGER_VPLS_PW_INITIATION_CMD
    TRIGGER_VPLS_PW_INITIATION_0 = "0"
    TRIGGER_VPLS_PW_INITIATION_1 = "1"

    TTL_VALUE_CMD = "ttl_value"

    UPDATE_INTERVAL_CMD = "update_interval"

    UPDATE_MSG_SIZE_CMD = "update_msg_size"

    UPDATES_PER_ITERATION_CMD = "updates_per_iteration"

    VCI_CMD = "vci"

    VCI_STEP_CMD = "vci_step"

    VLAN_CMD = "vlan"
    # Constant values for VLAN_CMD
    VLAN_0 = "0"
    VLAN_1 = "1"

    VLAN_CFI_CMD = "vlan_cfi"

    VLAN_ID_CMD = "vlan_id"

    VLAN_ID_MODE_CMD = "vlan_id_mode"
    # Constant values for VLAN_ID_MODE_CMD
    VLAN_ID_MODE_FIXED = "fixed"
    VLAN_ID_MODE_INCREMENT = "increment"

    VLAN_ID_STEP_CMD = "vlan_id_step"

    VLAN_USER_PRIORITY_CMD = "vlan_user_priority"

    VPI_CMD = "vpi"

    VPI_STEP_CMD = "vpi_step"

    VPLS_CMD = "vpls"
    # Constant values for VPLS_CMD
    VPLS_0 = "0"
    VPLS_1 = "1"
    VPLS_DISABLED = "disabled"
    VPLS_VPN = "vpn"
    VPLS_NO_VPN = "no_vpn"

    VPLS_CAPABILITY_NLRI_CMD = "vpls_capability_nlri"

    VPLS_FILTER_NLRI_CMD = "vpls_filter_nlri"

    VPLS_NLRI_CMD = "vpls_nlri"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

# instantiate the class to access the constants
#   example EmulationBgpConfigConstants.ARGUMENTS
EmulationBgpConfigConstants = EmulationBgpConfigConstants()


"""
Implemented Commands (Alphabetical)
    -Arguments
    -act_as_restarted
    -active
    -active_connect_enable
    -advertise_end_of_rib
    -advertise_host_route
    -atm_encapsulation
    -bfd_registration
    -bfd_registration_mode
    -capability_route_constraint
    -capability_route_refresh
    -configure_keepalive_timer
    -count
    -disable_received_update_validation
    -discard_ixia_generated_routes
    -enable_4_byte_as
    -enable_ad_vpls_prefix_length
    -enable_flap
    -flap_down_time
    -flap_up_time
    -gateway_ip_addr
    -graceful_restart_enable
    -handle
    -hold_time
    -ibgp_tester_as_four_bytes
    -ibgp_tester_as_two_bytes
    -initiate_ebgp_active_connection
    -initiate_ibgp_active_connection
    -interface_handle
    -ip_version
    -ipv4_capability_mdt_nlri
    -ipv4_capability_mpls_nlri
    -ipv4_capability_mpls_vpn_nlri
    -ipv4_capability_multicast_nlri
    -ipv4_capability_multicast_vpn_nlri
    -ipv4_capability_unicast_nlri
    -ipv4_filter_mpls_nlri
    -ipv4_filter_mpls_vpn_nlri
    -ipv4_filter_multicast_nlri
    -ipv4_filter_multicast_vpn_nlri
    -ipv4_filter_unicast_nlri
    -ipv4_mdt_nlri
    -ipv4_mpls_nlri
    -ipv4_mpls_vpn_nlri
    -ipv4_multicast_nlri
    -ipv4_multicast_vpn_nlri
    -ipv4_unicast_nlri
    -ipv6_capability_mpls_nlri
    -ipv6_capability_mpls_vpn_nlri
    -ipv6_capability_multicast_nlri
    -ipv6_capability_multicast_vpn_nlri
    -ipv6_capability_unicast_nlri
    -ipv6_filter_mpls_nlri
    -ipv6_filter_mpls_vpn_nlri
    -ipv6_filter_multicast_nlri
    -ipv6_filter_multicast_vpn_nlri
    -ipv6_filter_unicast_nlri
    -ipv6_mpls_nlri
    -ipv6_mpls_vpn_nlri
    -ipv6_multicast_nlri
    -ipv6_multicast_vpn_nlri
    -ipv6_unicast_nlri
    -keepalive_timer
    -local_addr_step
    -local_as
    -local_as4
    -local_as_mode
    -local_as_step
    -local_ip_addr
    -local_ipv6_addr
    -local_loopback_ip_addr
    -local_loopback_ip_addr_step
    -local_loopback_ip_prefix_length
    -local_router_id
    -local_router_id_enable
    -local_router_id_step
    -local_router_id_type
    -mac_address_start
    -mac_address_step
    -md5_enable
    -md5_key
    -mldp_p2mp_fec_type
    -mode
    -modify_outgoing_as_path
    -neighbor_type
    -netmask
    -next_hop_enable
    -next_hop_ip
    -no_write
    -override_existence_check
    -override_tracking
    -port_handle
    -remote_addr_step
    -remote_as
    -remote_confederation_member
    -remote_ip_addr
    -remote_ipv6_addr
    -remote_loopback_ip_addr
    -remote_loopback_ip_addr_step
    -request_vpn_label_exchange_over_lsp
    -reset
    -restart_time
    -retries
    -retry_time
    -route_refresh
    -routes_per_msg
    -send_ixia_signature_with_routes
    -staggered_start_enable
    -staggered_start_time
    -stale_time
    -start_rate
    -start_rate_enable
    -start_rate_interval
    -start_rate_scale_mode
    -stop_rate
    -stop_rate_enable
    -stop_rate_interval
    -stop_rate_scale_mode
    -suppress_notify
    -tcp_window_size
    -timeout
    -trigger_vpls_pw_initiation
    -ttl_value
    -update_interval
    -update_msg_size
    -updates_per_iteration
    -vci
    -vci_step
    -vlan
    -vlan_cfi
    -vlan_id
    -vlan_id_mode
    -vlan_id_step
    -vlan_user_priority
    -vpi
    -vpi_step
    -vpls
    -vpls_capability_nlri
    -vpls_filter_nlri
    -vpls_nlri

Use this to regenerate this class in the devhelper

<?xml version="1.0" encoding="UTF-8"?>
<xml feature="emulation_bgp_config">
  <cmd name="Arguments">
    <description>Description</description>
    <param>Parameter</param>
    <constantlist>Constants</constantlist>
    <supported>Supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


This option defines the action to be taken on the BGP server.

Valid options are:

enable


enable and/or create the BGP4 configuration. If -handle is specified, then it will be enabled, otherwise created.

delete


delete the BGP4 configuration, requires the use of -handle.

disable


disable the BGP4 configuration, requires the use of -handle.

modify


modify the BGP4 configuration, requires the use of -handle.

reset


deletes all BGP4 configurations from the -port_handle and then creates the provided BGP4 configuration.

DEFAULT
 None

IxNetwork-NGPF [M]


DESCRIPTION


This option defines the action to be taken on the BGP server.

Valid options are:

delete


delete the BGP4 configuration, requires the use of -handle.

disable


disable the BGP4 configuration, requires the use of -handle.

enable


enable and/or create the BGP4 configuration. If -handle is specified, then it will be enabled, otherwise created.

create


create the BGP configuration

modify


modify the BGP4 configuration, requires the use of -handle.

reset


deletes all BGP4 configurations from the -port_handle and then creates the provided BGP4 configuration.

DEFAULT
 None</description>
    <param>opt</param>
    <constantlist>delete,disable,enable,create,modify,reset</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="active">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Activates the item

DEFAULT


1</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="md5_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If set to 1, enables MD5 authentication for emulated BGP node.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If set to 1, enables MD5 authentication for emulated BGP node.

Valid options are:

0


1


DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="md5_key">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The key used for md5 authentication.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The key used for md5 authentication.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'md5_enable' | value= '1' |</description>
    <param>String</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="port_handle">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The port on which the BGP neighbor is to be created.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The port on which the BGP neighbor is to be created.

DEFAULT
 None</description>
    <param>port</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="handle">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


BGP handle used for -mode modify/disable/delete.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


BGP handle used for -mode modify/disable/delete. When -handle is provided with the /globals value the arguments that configure global protocol setting accept both multivalue handles and simple values. When -handle is provided with a a protocol stack handle or a protocol session handle, the arguments that configure global settings will only accept simple values. In this situation, these arguments will configure only the settings of the parent device group or the ports associated with the parent topology.

DEFAULT
 None</description>
    <param>opt</param>
    <constantlist>delete,disable,enable,create,modify,reset</constantlist>
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


This option defines the IP version of the BGP4.

Valid options are:

4


IPv4

6


IPv6

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


This option defines the IP version of the BGP4 neighbor to be configured on the Ixia interface.

Valid options are:

4


IPv4

6


IPv6

DEFAULT


4</description>
    <param>opt</param>
    <constantlist>4,6</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="local_ip_addr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The IPv4 address of the Ixia simulated BGP node to be emulated.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The IPv4 address of the Ixia simulated BGP node to be emulated.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ip_version' | value= '4' |</description>
    <param>IPV4</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="gateway_ip_addr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The gateway IPV4 or IPV6 address of the BGP4 neighbor interface. If this parameter is not provided it will be initialized to the remote_ip_addr value.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The gateway IPV4 or IPV6 address of the BGP4 neighbor interface. If this parameter is not provided it will be initialized to the remote_ip_addr value.

DEFAULT
 None</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="remote_ip_addr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The IPv4 address of the DUTs interface connected to the emulated BGP port.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The IPv4 address of the DUTs interface connected to the emulated BGP port.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ip_version' | value= '4' |</description>
    <param>IPV4</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="local_ipv6_addr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The IPv6 address of the BGP node to be emulated by the test port.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The IPv6 address of the BGP node to be emulated by the test port.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ip_version' | value= '6' |</description>
    <param>IPV6</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="remote_ipv6_addr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The IPv6 address of the DUT interface connected to emulated BGP node.This parameter is mandatory when -mode is create, -ip_version is 6 and parameter -neighbor_type is external, or -neighbor_type is internal and ipv4_mpls_nlri, ipv6_mpls_nlri, ipv4_mpls_vpn_nlri, and ipv6_mpls_vpn_nlri are not enabled.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The IPv6 address of the DUT interface connected to emulated BGP node. This parameter is mandatory when -mode is create, -ip_version is 6 and parameter -neighbor_type is external, or -neighbor_type is internal and ipv4_mpls_nlri, ipv6_mpls_nlri, ipv4_mpls_vpn_nlri, and ipv6_mpls_vpn_nlri are not enabled.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ip_version' | value= '6' |</description>
    <param>IPV6</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="local_addr_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Defines the mask and increment step for the next -local_ip_addr or ""-local_ipv6_addr"".(DEFAULT = 0.1.0.0 | 0:0:0:0:1::0)

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Defines the mask and increment step for the next -local_ip_addr or ""-local_ipv6_addr"".

DEFAULT
 None</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="remote_addr_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Defines the mask and increment step for the next -remote_ip_addr or ""-remote_ipv6_addr"".(DEFAULT = 0.1.0.0 | 0:0:0:0:1::0)

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Defines the mask and increment step for the next -remote_ip_addr or ""-remote_ipv6_addr"".

DEFAULT
 None</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="next_hop_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


This option is used for IPv4 traffic, and enables the use of the BGP NEXT_HOP attributes. When enabled, the IP next hop must be configured (using the -next_hop_ip option).

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


This option is used for IPv4 traffic, and enables the use of the BGP NEXT_HOP attributes. When enabled, the IP next hop must be configured (using the -next_hop_ip option).

Valid options are:

0


1


DEFAULT


1</description>
    <param>opt</param>
    <constantlist>FLAG,0,1</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="next_hop_ip">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Defines the IP of the next hop. This option is used if the flag -next_hop_enable is set.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Defines the IP of the next hop. This option is used if the flag -next_hop_enable is set.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'next_hop_enable' | value= '1' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="enable_4_byte_as">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Allow 4 byte values for -local_as.

DEFAULT


0

IxNetwork-NGPF


DESCRIPTION


Allow 4 byte values for -local_as.

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="local_as">
    <description>Supported platforms  Details
RANGE 0 - 4294967295
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The AS number of the BGP node to be emulated by the test port.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The AS number of the BGP node to be emulated by the test port.

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="local_as4">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


The 4 bytes AS number of the BGP node to be emulated by the test port.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'enable_4_byte_as' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="local_as_mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


For External BGP type only. This option controls the AS number (local_as) assigned to additional routers.

Valid options are:

fixed


(default) the local_as remains fixed.

increment


increments the local_as.

DEFAULT


fixed

IxNetwork-NGPF


DESCRIPTION


For External BGP type only. This option controls the AS number (local_as) assigned to additional routers.

Valid options are:

fixed


(default) the local_as remains fixed

increment


increments the local_as

DEFAULT


fixed</description>
    <param>opt</param>
    <constantlist>fixed,increment</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="remote_as">
    <description>Supported platforms  Details
RANGE 0 - 4294967295

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The remote AS.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The remote AS. Not supported reason: not supported in NGPF, deprecated in legacy

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="local_as_step">
    <description>Supported platforms  Details
RANGE 0 - 4294967295
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If you configure more then 1 eBGP neighbor on the Ixia interface, and if you select the option local_as_mode to increment, the option local_as_step defines the step by which the AS number is incremented.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If you configure more then 1 eBGP neighbor on the Ixia interface, and if you select the option local_as_mode to increment, the option local_as_step defines the step by which the AS number is incremented.

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'local_as_mode' | value= 'increment' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="update_interval">
    <description>Supported platforms  Details
RANGE 0 - 65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The time intervals at which UPDATE messages are sent to the DUT, expressed in the number of milliseconds between UPDATE messages.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The time intervals at which UPDATE messages are sent to the DUT, expressed in the number of milliseconds between UPDATE messages.

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="count">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Number of BGP nodes to create.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Number of BGP nodes to create.

DEFAULT


1</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="local_router_id">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


BGP4 router ID of the emulated node, must be in IPv4 format.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


BGP4 router ID of the emulated node, must be in IPv4 format.

DEFAULT
 None</description>
    <param>IPV4</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="local_router_id_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


BGP4 router ID step of the emulated node, must be in IPv4 format.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


BGP4 router ID step of the emulated node, must be in IPv4 format.

DEFAULT


0.0.0.1</description>
    <param>IPV4</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="vlan">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


Enables vlan on the directly connected BGP router interface. Valid options are:

Valid options are:

0


disable

1


enable.This option is valid only when -mode is create or -mode is modify and -handle is a BGP router handle.This option is available only when IxNetwork tcl API is used.

DEFAULT


0

IxNetwork-NGPF


DESCRIPTION


Enables vlan on the directly connected BGP router interface. Valid options are: 0 - disable, 1 - enable. This option is valid only when -mode is create or -mode is modify and -handle is a BGP router handle. This option is available only when IxNetwork tcl API is used.

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'mode' | value= 'create' |
'mode' | value= 'modify' |</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="vlan_id">
    <description>Supported platforms  Details
RANGE 0 - 4095
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


VLAN ID for the emulated router node.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


VLAN ID for the emulated router node.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vlan' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="vlan_id_mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


For multiple neighbor configuration, configurest the VLAN ID mode. Valid options are:fixedincrement

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


For multiple neighbor configuration, configurest the VLAN ID mode.

Valid options are:

fixed


increment


DEFAULT


increment

DEPENDENCIES


Valid in combination with parameter(s)
'vlan' | value= '1' |</description>
    <param>opt</param>
    <constantlist>fixed,increment</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="vlan_id_step">
    <description>Supported platforms  Details
RANGE 0 - 4096
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Defines the step for every VLAN When -vlan_id_mode is set to increment.When vlan_id_step causes the vlan_id value to exceed it's maximum value the increment will be done modulo .Examples: vlan_id = 4094; vlan_id_step = 2 -&gt; new vlan_id value = 0vlan_id = 4095; vlan_id_step = 11 -&gt; new vlan_id value = 10

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Defines the step for every VLAN When -vlan_id_mode is set to increment. When vlan_id_step causes the vlan_id value to exceed it's maximum value the increment will be done modulo . Examples: vlan_id = 4094; vlan_id_step = 2 -&gt; new vlan_id value = 0 vlan_id = 4095; vlan_id_step = 11 -&gt; new vlan_id value = 10

DEFAULT


1

DEPENDENCIES


Valid in combination with parameter(s)
'vlan' | value= '1' |
'vlan_id_mode' | value= 'increment' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="vlan_user_priority">
    <description>Supported platforms  Details
RANGE 0 - 7
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The VLAN user priority assigned to emulated router node.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The VLAN user priority assigned to emulated router node.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'vlan' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="vpi">
    <description>Supported platforms  Details
RANGE 0 - 255
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


VPI for emulated router node. RANGE 0-255

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


VPI for emulated router node. RANGE 0-255

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="vci">
    <description>Supported platforms  Details
RANGE 0 - 65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


VCI for emulated router node. RANGE 0-65535

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


VCI for emulated router node. RANGE 0-65535

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="vpi_step">
    <description>Supported platforms  Details
RANGE 0 - 255
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The step value used for incrementing the -vpi option. RANGE 0-255When vpi_step causes the vpi value to exceed it's maximum value the increment will be done modulo .Examples: vpi = 254; vpi_step = 2 -&gt; new vpi value = 0vpi = 255; vpi_step = 11 -&gt; new vpi value = 10

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The step value used for incrementing the -vpi option. RANGE 0-255 When vpi_step causes the vpi value to exceed it's maximum value the increment will be done modulo . Examples: vpi = 254; vpi_step = 2 -&gt; new vpi value = 0 vpi = 255; vpi_step = 11 -&gt; new vpi value = 10

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="vci_step">
    <description>Supported platforms  Details
RANGE 0 - 65535
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The step value used for incrementing the -vci option. RANGE 0-65535 When vci_step causes the vci value to exceed it's maximum value the increment will be done modulo .Examples: vci = 65534; vci_step = 2 -&gt; new vci value = 0vci = 65535; vci_step = 11 -&gt; new vci value = 10

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The step value used for incrementing the -vci option. RANGE 0-65535 When vci_step causes the vci value to exceed it's maximum value the increment will be done modulo . Examples: vci = 65534; vci_step = 2 -&gt; new vci value = 0 vci = 65535; vci_step = 11 -&gt; new vci value = 10

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="atm_encapsulation">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The encapsulation of the ATM protocol interface associated with the emulated router.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The encapsulation of the ATM protocol interface associated with the emulated router.

Valid options are:

VccMuxIPV4Routed


VccMuxIPV6Routed


VccMuxBridgedEthernetFCS


VccMuxBridgedEthernetNoFCS


LLCRoutedCLIP


LLCBridgedEthernetFCS


LLCBridgedEthernetNoFCS


DEFAULT
 None</description>
    <param>opt</param>
    <constantlist>VccMuxIPV4Routed,VccMuxIPV6Routed,VccMuxBridgedEthernetFCS,VccMuxBridgedEthernetNoFCS,LLCRoutedCLIP,LLCBridgedEthernetFCS,LLCBridgedEthernetNoFCS</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="interface_handle">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


This parameter is valid only for IxTclNetwork API and represents a list of interfaces previously created using interface_config or another emulation__config command that returns the interfacehandles (for example: BFD).

Starting with IxNetwork 5.60 this parameter accepts handles returned by emulation_dhcp_group_config procedure in the following format: |,-, ... The DHCP ranges are separated from the Interface Index identifiers with the (|) character. The Interface Index identifiers are separated with comas (,). A range of Interface Index identifiers can be defined using the dash (-) character.

Ranges along with the Interface Index identifiers are grouped together in TCL Lists. The lists can contain mixed items, protocol interface handles returned by interface_config and handles returned by emulation_dhcp_group_config along with the interface index.

Example:count 10 (10 BGP neighbors). 3 DHCP range handles returned by ::::emulation_dhcp_group_config. Each DHCP range has 20 sessions (interfaces). If we pass -interface_handle in the following format: [list $dhcp_r1|1,5 $dhcp_r2|1-3 $dhcp_r3|1,3,5-9,13] The interfaces will be distributed to the routers in the following manner:

BGP Neighbor 1: $dhcp_r1 -&gt; interface 1
BGP Neighbor 2: $dhcp_r1 -&gt; interface 5
BGP Neighbor 3: $dhcp_r2 -&gt; interface 1
BGP Neighbor 4: $dhcp_r2 -&gt; interface 2
BGP Neighbor 5: $dhcp_r2 -&gt; interface 3
BGP Neighbor 6: $dhcp_r3 -&gt; interface 1
BGP Neighbor 7: $dhcp_r3 -&gt; interface 3
BGP Neighbor 8: $dhcp_r3 -&gt; interface 5
BGP Neighbor 9: $dhcp_r3 -&gt; interface 6
BGP Neighbor 10: $dhcp_r3 -&gt; interface 7
BGP Neighbor 11: $dhcp_r3 -&gt; interface 8
BGP Neighbor 12: $dhcp_r3 -&gt; interface 9
BGP Neighbor 13 $dhcp_r3 -&gt; interface 13

Starting with IxNetwork 6.30SP1 this parameter accepts handles returned by interface_config procedure with -l23_config_type static_type setting in the following format: |,-, ... The IP ranges are separated from the Interface Index identifiers with the (|) character. The Interface Index identifiers are separated with comas (,). A range of Interface Index identifiers can be defined using the dash (-) character.

Ranges along with the Interface Index identifiers are grouped together in TCL Lists. The lists can contain mixed items, protocol interface handles returned by interface_config with -l23_config_type protocol_interface and with -l23_config_type static_type.

Example:count 10 (10 BGP neighbors). 3 IP range handles returned by ::::interface_config. Each IP range has 20 sessions (interfaces). If we pass -interface_handle in the following format: [list $ip_r1|1,5 $ip_r2|1-3 $ip_r3|1,3,5-9,13] The interfaces will be distributed to the routers in the following manner:


BGP Neighbor 1: $ip_r1 -&gt; interface 1
BGP Neighbor 2: $ip_r1 -&gt; interface 5
BGP Neighbor 3: $ip_r2 -&gt; interface 1
BGP Neighbor 4: $ip_r2 -&gt; interface 2
BGP Neighbor 5: $ip_r2 -&gt; interface 3
BGP Neighbor 6: $ip_r3 -&gt; interface 1
BGP Neighbor 7: $ip_r3 -&gt; interface 3
BGP Neighbor 8: $ip_r3 -&gt; interface 5
BGP Neighbor 9: $ip_r3 -&gt; interface 6
BGP Neighbor 10: $ip_r3 -&gt; interface 7
BGP Neighbor 11: $ip_r3 -&gt; interface 8
BGP Neighbor 12: $ip_r3 -&gt; interface 9
BGP Neighbor 13 $ip_r3 -&gt; interface 13

Valid for mode create for IxTclNetwork only.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


This parameter is valid only for IxTclNetwork API and represents a list of interfaces previously created using interface_config or another emulation__config command that returns the interface handles (for example: BFD). Starting with IxNetwork 5.60 this parameter accepts handles returned by emulation_dhcp_group_config procedure in the following format: |,-, ... The DHCP ranges are separated from the Interface Index identifiers with the (|) character. The Interface Index identifiers are separated with comas (,). A range of Interface Index identifiers can be defined using the dash (-) character. Ranges along with the Interface Index identifiers are grouped together in TCL Lists. The lists can contain mixed items, protocol interface handles returned by interface_config and handles returned by emulation_dhcp_group_config along with the interface index. Example: count 10 (10 BGP neighbors). 3 DHCP range handles returned by ::::emulation_dhcp_group_config. Each DHCP range has 20 sessions (interfaces). If we pass a -interface_handle in the following format: [list $dhcp_r1|1,5 $dhcp_r2|1-3 $dhcp_r3|1,3,5-9,13] The interfaces will be distributed to the routers in the following manner: BGP Neighbor 1: $dhcp_r1 -&gt; interface 1 BGP Neighbor 2: $dhcp_r1 -&gt; interface 5 BGP Neighbor 3: $dhcp_r2 -&gt; interface 1 BGP Neighbor 4: $dhcp_r2 -&gt; interface 2 BGP Neighbor 5: $dhcp_r2 -&gt; interface 3 BGP Neighbor 6: $dhcp_r3 -&gt; interface 1 BGP Neighbor 7: $dhcp_r3 -&gt; interface 3 BGP Neighbor 8: $dhcp_r3 -&gt; interface 5 BGP Neighbor 9: $dhcp_r3 -&gt; interface 6 BGP Neighbor 10: $dhcp_r3 -&gt; interface 7 BGP Neighbor 11: $dhcp_r3 -&gt; interface 8 BGP Neighbor 12: $dhcp_r3 -&gt; interface 9 BGP Neighbor 13 $dhcp_r3 -&gt; interface 13 Starting with IxNetwork 6.30SP1 this parameter accepts handles returned by interface_config procedure with -l23_config_type static_type setting in the following format: |,-, ... The IP ranges are separated from the Interface Index identifiers with the (|) character. The Interface Index identifiers are separated with comas (,). A range of Interface Index identifiers can be defined using the dash (-) character. Ranges along with the Interface Index identifiers are grouped together in TCL Lists. The lists can contain mixed items, protocol interface handles returned by interface_config with -l23_config_type protocol_interface and with -l23_config_type static_type. Example: count 10 (10 BGP neighbors). 3 IP range handles returned by ::::interface_config. Each IP range has 20 sessions (interfaces). If we pass a -interface_handle in the following format: [list $ip_r1|1,5 $ip_r2|1-3 $ip_r3|1,3,5-9,13] The interfaces will be distributed to the routers in the following manner: BGP Neighbor 1: $ip_r1 -&gt; interface 1 BGP Neighbor 2: $ip_r1 -&gt; interface 5 BGP Neighbor 3: $ip_r2 -&gt; interface 1 BGP Neighbor 4: $ip_r2 -&gt; interface 2 BGP Neighbor 5: $ip_r2 -&gt; interface 3 BGP Neighbor 6: $ip_r3 -&gt; interface 1 BGP Neighbor 7: $ip_r3 -&gt; interface 3 BGP Neighbor 8: $ip_r3 -&gt; interface 5 BGP Neighbor 9: $ip_r3 -&gt; interface 6 BGP Neighbor 10: $ip_r3 -&gt; interface 7 BGP Neighbor 11: $ip_r3 -&gt; interface 8 BGP Neighbor 12: $ip_r3 -&gt; interface 9 BGP Neighbor 13 $ip_r3 -&gt; interface 13 Valid for mode create for IxTclNetwork only.

DEFAULT
 None</description>
    <param>string</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="retry_time">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


For External BGP neighbor. When retries are necessary, the delay in seconds between retries.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


For External BGP neighbor. When retries are necessary, the delay in seconds between retries. Not supported reason: not supported in NGPF

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="hold_time">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Configures the hold time for BGP sessions for this Neighbor. Keepalives are sent out every one-third of this interval. If the default value is 90, KeepAlive messages are sent every 30 seconds.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Configures the hold time for BGP sessions for this Neighbor. Keepalives are sent out every one-third of this interval. If the default value is 90, KeepAlive messages are sent every 30 seconds.

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="neighbor_type">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Sets the BGP neighbor type.

Valid options are:

internal


iBGP

external


eBGP

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Sets the BGP neighbor type.

Valid options are:

internal


iBGP

external


eBGP

DEFAULT
 None</description>
    <param>opt</param>
    <constantlist>internal,external</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="graceful_restart_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Will enable graceful restart (HA) on the BGP4 neighbor.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Will enable graceful restart (HA) on the BGP4 neighbor.

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="restart_time">
    <description>Supported platforms  Details
RANGE 0 - 10000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If -graceful_restart_enable is set, sets the amount of time following a restart operation allowed to re-establish a BGP session, in seconds.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If -graceful_restart_enable is set, sets the amount of time following a restart operation allowed to re-establish a BGP session, in seconds.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'graceful_restart_enable' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="stale_time">
    <description>Supported platforms  Details
RANGE 0 - 10000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If -graceful_restart_enable is set, sets the amount of time after which an End-Of-RIB marker is sent in an Update message to the peer to allow time for routing convergence via IGP and BGP selection, in seconds. Stale routing information for that address family is then deleted by the receiving peer.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If -graceful_restart_enable is set, sets the amount of time after which an End-Of-RIB marker is sent in an Update message to the peer to allow time for routing convergence via IGP and BGP selection, in seconds. Stale routing information for that address family is then deleted by the receiving peer.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'graceful_restart_enable' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="tcp_window_size">
    <description>Supported platforms  Details
RANGE 0 - 10000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


For External BGP neighbor only. The TCP window used for communications from the neighbor.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


For External BGP neighbor only. The TCP window used for communications from the neighbor.

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="retries">
    <description>Supported platforms  Details
RANGE 0 - 10000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


For External BGP neighbor. The number of times to attempt an OPEN connection with the DUT routers before giving up.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


For External BGP neighbor. The number of times to attempt an OPEN connection with the DUT routers before giving up. Not supported reason: not supported in NGPF

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="local_router_id_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Enables the BGP4 local router id option.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables the BGP4 local router id option.

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="netmask">
    <description>Supported platforms  Details
RANGE 1 - 128
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Mask of the IP address for the interface configuration.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Mask of the IP address for the interface configuration.

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="mac_address_start">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Initial MAC address of the interfaces created for the BGP4 neighbor.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Initial MAC address of the interfaces created for the BGP4 neighbor.

DEFAULT
 None</description>
    <param>MAC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="mac_address_step">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


The incrementing step for thr MAC address of the dirrectly connected interfaces created for the BGP4 neighbor.This option is valid only when IxTclNetwork API is used.

DEFAULT


0000.0000.0001

IxNetwork-NGPF


DESCRIPTION


The incrementing step for thr MAC address of the dirrectly connected interfaces created for the BGP4 neighbor. This option is valid only when IxTclNetwork API is used.

DEFAULT


0000.0000.0001</description>
    <param>MAC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ipv4_mdt_nlri">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If checked, this BGP/BGP+ router/peer supports IPv4 MDT address family messages.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If checked, this BGP/BGP+ router/peer supports IPv4 MDT address family messages.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ipv4_capability_mdt_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If checked, this BGP/BGP+ router/peer supports IPv4 MDT address family messages.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ipv4_unicast_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


If used, support for IPv4 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_capability_unicast_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_filter_unicast_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_multicast_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


If used, support for IPv4 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_capability_multicast_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_filter_multicast_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_mpls_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


If used, support for IPv4 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_capability_mpls_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_filter_mpls_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_mpls_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


If used, support for IPv4 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_capability_mpls_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv4_filter_mpls_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv4 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_unicast_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


If used, support for IPv6 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_capability_unicast_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_filter_unicast_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 Unicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_multicast_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


If used, support for IPv6 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_capability_multicast_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_filter_multicast_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 Multicast is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_mpls_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


If used, support for IPv6 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_capability_mpls_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_filter_mpls_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 MPLS is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_mpls_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork


DESCRIPTION


If used, support for IPv6 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_capability_mpls_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="ipv6_filter_mpls_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


If used, support for IPv6 MPLS VPN is advertised in the Capabilities Optional Parameter / Multiprotocol Extensions parameter in the OPEN message and in addition, for IxTclNetwork, also sets the filters for the respective learned routes.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="capability_route_refresh">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Route Refresh

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="capability_route_constraint">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Route Constraint

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="local_loopback_ip_addr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Required when the -ipv4_mpls_vpn_nlri option is used.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Required when the -ipv4_mpls_vpn_nlri option is used.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4_mpls_vpn_nlri' | value= '' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="local_loopback_ip_prefix_length">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Prefix length for local_loopback_ip_addr.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Prefix length for local_loopback_ip_addr.

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="local_loopback_ip_addr_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Required when the -ipv4_mpls_vpn_nlri option is used.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Required when the -ipv4_mpls_vpn_nlri option is used.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4_mpls_vpn_nlri' | value= '' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="remote_loopback_ip_addr">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Required when the -ipv4_mpls_vpn_nlri option is used.This parameter is mandatory when -mode is create, and parameter -neighbor_type is internal and and ipv4_mpls_nlri, ipv6_mpls_nlri, ipv4_mpls_vpn_nlri, and ipv6_mpls_vpn_nlri are enabled.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Required when the -ipv4_mpls_vpn_nlri option is used. This parameter is mandatory when -mode is create, and parameter -neighbor_type is internal and and ipv4_mpls_nlri, ipv6_mpls_nlri, ipv4_mpls_vpn_nlri, and ipv6_mpls_vpn_nlri are enabled.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4_mpls_vpn_nlri' | value= '' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="remote_loopback_ip_addr_step">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Required when the -ipv4_mpls_vpn_nlri option is used.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Required when the -ipv4_mpls_vpn_nlri option is used.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'ipv4_mpls_vpn_nlri' | value= '' |</description>
    <param>IP</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ttl_value">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


This attribute represents the limited number of iterations that a unit of data can experience before the data is discarded.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


This attribute represents the limited number of iterations that a unit of data can experience before the data is discarded.

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="updates_per_iteration">
    <description>Supported platforms  Details
RANGE 0 - 10000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


When the protocol server operates on older ports that do not possess a local processor, this tuning parameter controls how many UPDATE messages are sent at a time. When many routers are being simulated on such a port, changing this value may help to increase or decrease performance.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


When the protocol server operates on older ports that do not possess a local processor, this tuning parameter controls how many UPDATE messages are sent at a time. When many routers are being simulated on such a port, changing this value may help to increase or decrease performance.

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="bfd_registration">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Enable or disable BFD registration.

DEFAULT


0

IxNetwork-NGPF


DESCRIPTION


Enable or disable BFD registration.

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="bfd_registration_mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Set BFD registration mode to single hop or multi hop.

DEFAULT


multi_hop

IxNetwork-NGPF


DESCRIPTION


Set BFD registration mode to single hop or multi hop.

Valid options are:

single_hop


multi_hop


DEFAULT


multi_hop</description>
    <param>opt</param>
    <constantlist>single_hop,multi_hop</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="override_existence_check">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If this option is enabled, the interface existence check is skipped but the list of interfaces is still created and maintained in order to keep track of existing interfaces if required. Using this option will speed up the interfaces' creation.

DEFAULT


0

IxNetwork-NGPF


DESCRIPTION


If this option is enabled, the interface existence check is skipped but the list of interfaces is still created and maintained in order to keep track of existing interfaces if required. Using this option will speed up the interfaces' creation.

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="override_tracking">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If this option is enabled, the list of interfaces won't be created and maintained anymore, thus, speeding up the interfaces' creation even more. Also, it will enable -override_existence_check in case it wasn't already enabled because checking for interface existence becomes impossible if the the list of interfaces doesn't exist anymore.

DEFAULT


0

IxNetwork-NGPF


DESCRIPTION


If this option is enabled, the list of interfaces won?t be created and maintained anymore, thus, speeding up the interfaces' creation even more. Also, it will enable -override_existence_check in case it wasn?t already enabled because checking for interface existence becomes impossible if the the list of interfaces doesn?t exist anymore.

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="no_write">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If this option is present, the configuration is not written to the hardware. This option can be used to queue up multiple configurations before writing to the hardware.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


If this option is present, the configuration is not written to the hardware. This option can be used to queue up multiple configurations before writing to the hardware.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="vpls">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

Valid options are:

0


disabled

1


enabled

DEFAULT


0

IxNetwork-NGPF


DESCRIPTION


(deprecated) This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled. Valid choices are: 0 - disabled 1 - enabled

Valid options are:

0


1


disabled


vpn


no_vpn


DEFAULT


0</description>
    <param>opt</param>
    <constantlist>0,1,disabled,vpn,no_vpn</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="vpls_nlri">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="vpls_capability_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="vpls_filter_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


This BGP/BGP+ router/peer supports BGP/BGP+ VPLS per the Kompella draft. This will enable the L2 Sites. If present, means VPLS capabilities are enabled.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="advertise_host_route">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Not supported

DEFAULT
 Not supported

IxNetwork-NGPF


DESCRIPTION


Not supported

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="modify_outgoing_as_path">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Moved to emulation_bgp_route_config under AS Path configuration.

DEFAULT
 Not supported

IxNetwork-NGPF


DESCRIPTION


Moved to emulation_bgp_route_config under AS Path configuration.

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="remote_confederation_member">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Moved to emulation_bgp_route_config under AS Path configuration.

DEFAULT
 Not supported

IxNetwork-NGPF


DESCRIPTION


Moved to emulation_bgp_route_config under AS Path configuration.

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="reset">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Clears any BGP4 configuration on the targeted port before configuring further.

DEFAULT
 Not supported

IxNetwork-NGPF


DESCRIPTION


Clears any BGP4 configuration on the targeted port before configuring further.

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="route_refresh">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Details needed.

DEFAULT
 Not supported

IxNetwork-NGPF


DESCRIPTION


Details needed.

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="routes_per_msg">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Not supported

DEFAULT
 Not supported

IxNetwork-NGPF


DESCRIPTION


Not supported

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="suppress_notify">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


If set to 1, suppresses, the notification message sent to the peer. if set to 0, does not suppress the notification message sent to the peer.

DEFAULT
 Not supported

IxNetwork-NGPF


DESCRIPTION


If set to 1, suppresses, the notification message sent to the peer. if set to 0, does not suppress the notification message sent to the peer.

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="timeout">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Not supported

DEFAULT
 Not supported

IxNetwork-NGPF


DESCRIPTION


Not supported

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="update_msg_size">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Maximum size (bytes) of the UPDATE message transmitted by emulated router node.

DEFAULT
 Not supported

IxNetwork-NGPF


DESCRIPTION


Maximum size (bytes) of the UPDATE message transmitted by emulated router node.

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="vlan_cfi">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Canonical format indicator field in VLAN for emulated router node.

DEFAULT
 Not supported</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="act_as_restarted">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Act as restarted

DEFAULT


0

DEPENDENCIES


Valid in combination with parameter(s)
'graceful_restart_enable' | value= '1' |</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="discard_ixia_generated_routes">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Discard Ixia Generated Routes

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="flap_down_time">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Downtime in Seconds

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'enable_flap' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="local_router_id_type">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


BGP ID Same as Router ID

Valid options are:

same


new


DEFAULT


new</description>
    <param>opt</param>
    <constantlist>same,new</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="enable_flap">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Flap

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="send_ixia_signature_with_routes">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Send Ixia Signature With Routes

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="flap_up_time">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Uptime in Seconds

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'enable_flap' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ipv4_multicast_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


IPv4 Multicast VPN

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ipv4_capability_multicast_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


IPv4 Multicast VPN

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ipv4_filter_multicast_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


IPv4 Multicast VPN

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ipv6_multicast_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


IPv6 Multicast VPN

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ipv6_capability_multicast_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


IPv6 Multicast VPN

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ipv6_filter_multicast_vpn_nlri">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


IPv6 Multicast VPN

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="advertise_end_of_rib">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Advertise End-Of-RIB

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="configure_keepalive_timer">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Configure Keepalive Timer

DEFAULT


0</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="keepalive_timer">
    <description>Supported platforms  Details
RANGE 0 - 65535
IxNetwork-NGPF


DESCRIPTION


Keepalive Timer

DEFAULT


30</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="staggered_start_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


Enables staggered start of neighbors.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


Enables staggered start of neighbors.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="staggered_start_time">
    <description>Supported platforms  Details
RANGE 0 - 10000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


When the -staggered_start_enable flag is used, this is the duration of the start process in seconds.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


When the -staggered_start_enable flag is used, this is the duration of the start process in seconds.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'staggered_start_time' | value= '1' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="start_rate_enable">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Enable bgp globals start rate

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="start_rate_interval">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Time interval used to calculate the rate for triggering an action (rate = count/interval)

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="start_rate">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Number of times an action is triggered per time interval

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="start_rate_scale_mode">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Indicates whether the control is specified per port or per device group

Valid options are:

deviceGroup


The values regarding start rate are mapped per device group

port


The values regarding start rate are mapped per port

DEFAULT
 None</description>
    <param>port</param>
    <constantlist>deviceGroup,port</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="stop_rate_enable">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Enable bgp globals stop rate

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="stop_rate_interval">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Time interval used to calculate the rate for triggering an action (rate = count/interval)

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="stop_rate">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Number of times an action is triggered per time interval

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="stop_rate_scale_mode">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Indicates whether the control is specified per port or per device group

Valid options are:

deviceGroup


The values regarding stop rate are mapped per device group

port


The values regarding stop rate are mapped per port

DEFAULT
 None</description>
    <param>port</param>
    <constantlist>deviceGroup,port</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="active_connect_enable">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


For External BGP neighbor. If set, a HELLO message is actively sent when BGP testing starts. Otherwise, the port waits for the DUT to send its HELLO message.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


For External BGP neighbor. If set, a HELLO message is actively sent when BGP testing starts. Otherwise, the port waits for the DUT to send its HELLO message.

DEFAULT
 None</description>
    <param>FLAG</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="disable_received_update_validation">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Disable Received Update Validation (Enabled for High Performance)

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="enable_ad_vpls_prefix_length">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Enable AD VPLS Prefix Length in Bits

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ibgp_tester_as_four_bytes">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Tester 4 Byte AS# for iBGP

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="ibgp_tester_as_two_bytes">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Tester AS# for iBGP

DEFAULT
 None</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="initiate_ebgp_active_connection">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Initiate eBGP Active Connection

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="initiate_ibgp_active_connection">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Initiate iBGP Active Connection

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="mldp_p2mp_fec_type">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


MLDP P2MP FEC Type (Hex)

DEFAULT
 None</description>
    <param>HEX</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="request_vpn_label_exchange_over_lsp">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Request VPN Label Exchange over LSP

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="trigger_vpls_pw_initiation">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


Trigger VPLS PW Initiation

DEFAULT
 None</description>
    <param>bool</param>
    <constantlist>0,1</constantlist>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
</xml>

"""
