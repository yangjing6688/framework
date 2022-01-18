from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: emulation_ospf_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class EmulationOspfConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(EmulationOspfConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationOspfConfigConstants.AREA_ID_CMD] = "dummyValue1" # static value
        dummyDict[EmulationOspfConfigConstants.AREA_ID_AS_NUMBER_CMD] = "dummyValue2" # static value
        dummyDict[EmulationOspfConfigConstants.AREA_ID_AS_NUMBER_STEP_CMD] = "dummyValue3" # static value
        dummyDict[EmulationOspfConfigConstants.AREA_ID_STEP_CMD] = "dummyValue4" # static value
        dummyDict[EmulationOspfConfigConstants.AREA_ID_TYPE_CMD] = EmulationOspfConfigConstants.AREA_ID_TYPE_AREA_ID_AS_IP # constant value
        dummyDict[EmulationOspfConfigConstants.AREA_TYPE_CMD] = EmulationOspfConfigConstants.AREA_TYPE_EXTERNALCAPABLE # constant value
        dummyDict[EmulationOspfConfigConstants.ATM_ENCAPSULATION_CMD] = EmulationOspfConfigConstants.ATM_ENCAPSULATION_LLCBRIDGEDETHERNETFCS # constant value
        dummyDict[EmulationOspfConfigConstants.ATTEMPT_ENABLED_CMD] = "dummyValue8" # static value
        dummyDict[EmulationOspfConfigConstants.ATTEMPT_INTERVAL_CMD] = "dummyValue9" # static value
        dummyDict[EmulationOspfConfigConstants.ATTEMPT_RATE_CMD] = "dummyValue10" # static value
        dummyDict[EmulationOspfConfigConstants.ATTEMPT_SCALE_MODE_CMD] = EmulationOspfConfigConstants.ATTEMPT_SCALE_MODE_DEVICE_GROUP # constant value
        dummyDict[EmulationOspfConfigConstants.AUTHENTICATION_MODE_CMD] = EmulationOspfConfigConstants.AUTHENTICATION_MODE_MD5 # constant value
        dummyDict[EmulationOspfConfigConstants.BFD_REGISTRATION_CMD] = "dummyValue13" # static value
        dummyDict[EmulationOspfConfigConstants.COUNT_CMD] = "dummyValue14" # static value
        dummyDict[EmulationOspfConfigConstants.DEAD_INTERVAL_CMD] = "dummyValue15" # static value
        dummyDict[EmulationOspfConfigConstants.DEMAND_CIRCUIT_CMD] = "dummyValue16" # static value
        dummyDict[EmulationOspfConfigConstants.DISABLE_AUTO_GENERATE_LINK_LSA_CMD] = "dummyValue17" # static value
        dummyDict[EmulationOspfConfigConstants.DISCONNECT_ENABLED_CMD] = "dummyValue18" # static value
        dummyDict[EmulationOspfConfigConstants.DISCONNECT_INTERVAL_CMD] = "dummyValue19" # static value
        dummyDict[EmulationOspfConfigConstants.DISCONNECT_RATE_CMD] = "dummyValue20" # static value
        dummyDict[EmulationOspfConfigConstants.DISCONNECT_SCALE_MODE_CMD] = EmulationOspfConfigConstants.DISCONNECT_SCALE_MODE_DEVICE_GROUP # constant value
        dummyDict[EmulationOspfConfigConstants.DO_NOT_GENERATE_ROUTER_LSA_CMD] = "dummyValue22" # static value
        dummyDict[EmulationOspfConfigConstants.ENABLE_DR_BDR_CMD] = "dummyValue23" # static value
        dummyDict[EmulationOspfConfigConstants.ENABLE_FAST_HELLO_CMD] = "dummyValue24" # static value
        dummyDict[EmulationOspfConfigConstants.ENABLE_IGNORE_DB_DESC_MTU_CMD] = "dummyValue25" # static value
        dummyDict[EmulationOspfConfigConstants.ENABLE_SUPPORT_RFC_5838_CMD] = "dummyValue26" # static value
        dummyDict[EmulationOspfConfigConstants.EXTERNAL_ATTRIBUTE_CMD] = "dummyValue27" # static value
        dummyDict[EmulationOspfConfigConstants.EXTERNAL_CAPABILITIES_CMD] = "dummyValue28" # static value
        dummyDict[EmulationOspfConfigConstants.FLOOD_LSUPDATES_PER_INTERVAL_CMD] = "dummyValue29" # static value
        dummyDict[EmulationOspfConfigConstants.GET_NEXT_SESSION_MODE_CMD] = "dummyValue30" # static value
        dummyDict[EmulationOspfConfigConstants.GRACE_PERIOD_CMD] = "dummyValue31" # static value
        dummyDict[EmulationOspfConfigConstants.GRACEFUL_RESTART_ENABLE_CMD] = "dummyValue32" # static value
        dummyDict[EmulationOspfConfigConstants.GRACEFUL_RESTART_HELPER_MODE_ENABLE_CMD] = "dummyValue33" # static value
        dummyDict[EmulationOspfConfigConstants.GRACEFUL_RESTART_RESTARTING_MODE_ENABLE_CMD] = "dummyValue34" # static value
        dummyDict[EmulationOspfConfigConstants.GRE_CHECKSUM_CMD] = "dummyValue35" # static value
        dummyDict[EmulationOspfConfigConstants.GRE_LOCAL_IP_CMD] = "dummyValue36" # static value
        dummyDict[EmulationOspfConfigConstants.GRE_REMOTE_IP_CMD] = "dummyValue37" # static value
        dummyDict[EmulationOspfConfigConstants.GRE_TUNNEL_CMD] = "dummyValue38" # static value
        dummyDict[EmulationOspfConfigConstants.HANDLE_CMD] = "dummyValue39" # static value
        dummyDict[EmulationOspfConfigConstants.HELLO_INTERVAL_CMD] = "dummyValue40" # static value
        dummyDict[EmulationOspfConfigConstants.HELLO_MULTIPLIER_CMD] = "dummyValue41" # static value
        dummyDict[EmulationOspfConfigConstants.HOST_ROUTE_CMD] = "dummyValue42" # static value
        dummyDict[EmulationOspfConfigConstants.IGNORE_DB_DESC_MTU_CMD] = "dummyValue43" # static value
        dummyDict[EmulationOspfConfigConstants.INSTANCE_ID_CMD] = "dummyValue44" # static value
        dummyDict[EmulationOspfConfigConstants.INSTANCE_ID_STEP_CMD] = "dummyValue45" # static value
        dummyDict[EmulationOspfConfigConstants.INT_MSG_EXCHANGE_CMD] = "dummyValue46" # static value
        dummyDict[EmulationOspfConfigConstants.INTER_FLOOD_LSUPDATE_BURST_GAP_CMD] = "dummyValue47" # static value
        dummyDict[EmulationOspfConfigConstants.INTERFACE_COST_CMD] = "dummyValue48" # static value
        dummyDict[EmulationOspfConfigConstants.INTERFACE_HANDLE_CMD] = "dummyValue49" # static value
        dummyDict[EmulationOspfConfigConstants.INTF_IP_ADDR_CMD] = "dummyValue50" # static value
        dummyDict[EmulationOspfConfigConstants.INTF_IP_ADDR_STEP_CMD] = "dummyValue51" # static value
        dummyDict[EmulationOspfConfigConstants.INTF_IPV6_ADDR_CMD] = "dummyValue52" # static value
        dummyDict[EmulationOspfConfigConstants.INTF_IPV6_ADDR_STEP_CMD] = "dummyValue53" # static value
        dummyDict[EmulationOspfConfigConstants.INTF_IPV6_PREFIX_LENGTH_CMD] = "dummyValue54" # static value
        dummyDict[EmulationOspfConfigConstants.INTF_PREFIX_LENGTH_CMD] = "dummyValue55" # static value
        dummyDict[EmulationOspfConfigConstants.IPV6_GATEWAY_IP_CMD] = "dummyValue56" # static value
        dummyDict[EmulationOspfConfigConstants.IPV6_GATEWAY_IP_STEP_CMD] = "dummyValue57" # static value
        dummyDict[EmulationOspfConfigConstants.LINK_METRIC_CMD] = "dummyValue58" # static value
        dummyDict[EmulationOspfConfigConstants.LOOPBACK_IP_ADDR_CMD] = "dummyValue59" # static value
        dummyDict[EmulationOspfConfigConstants.LOOPBACK_IP_ADDR_STEP_CMD] = "dummyValue60" # static value
        dummyDict[EmulationOspfConfigConstants.LSA_DISCARD_MODE_CMD] = "dummyValue61" # static value
        dummyDict[EmulationOspfConfigConstants.LSA_REFRESH_TIME_CMD] = "dummyValue62" # static value
        dummyDict[EmulationOspfConfigConstants.LSA_RETRANSMIT_DELAY_CMD] = "dummyValue63" # static value
        dummyDict[EmulationOspfConfigConstants.LSA_RETRANSMIT_TIME_CMD] = "dummyValue64" # static value
        dummyDict[EmulationOspfConfigConstants.MAC_ADDRESS_INIT_CMD] = "dummyValue65" # static value
        dummyDict[EmulationOspfConfigConstants.MAC_ADDRESS_STEP_CMD] = "dummyValue66" # static value
        dummyDict[EmulationOspfConfigConstants.MAX_LS_UPDATES_PER_BURST_CMD] = "dummyValue67" # static value
        dummyDict[EmulationOspfConfigConstants.MAX_LSAS_PER_PKT_CMD] = "dummyValue68" # static value
        dummyDict[EmulationOspfConfigConstants.MAX_MTU_CMD] = "dummyValue69" # static value
        dummyDict[EmulationOspfConfigConstants.MD5_KEY_CMD] = "dummyValue70" # static value
        dummyDict[EmulationOspfConfigConstants.MD5_KEY_ID_CMD] = "dummyValue71" # static value
        dummyDict[EmulationOspfConfigConstants.MODE_CMD] = EmulationOspfConfigConstants.MODE_CREATE # constant value
        dummyDict[EmulationOspfConfigConstants.MTU_CMD] = "dummyValue73" # static value
        dummyDict[EmulationOspfConfigConstants.MULTICAST_CAPABILITY_CMD] = "dummyValue74" # static value
        dummyDict[EmulationOspfConfigConstants.NEIGHBOR_DR_ELIGIBILITY_CMD] = "dummyValue75" # static value
        dummyDict[EmulationOspfConfigConstants.NEIGHBOR_INTF_IP_ADDR_CMD] = "dummyValue76" # static value
        dummyDict[EmulationOspfConfigConstants.NEIGHBOR_INTF_IP_ADDR_STEP_CMD] = "dummyValue77" # static value
        dummyDict[EmulationOspfConfigConstants.NEIGHBOR_ROUTER_ID_CMD] = "dummyValue78" # static value
        dummyDict[EmulationOspfConfigConstants.NEIGHBOR_ROUTER_ID_STEP_CMD] = "dummyValue79" # static value
        dummyDict[EmulationOspfConfigConstants.NETWORK_TYPE_CMD] = EmulationOspfConfigConstants.NETWORK_TYPE_BROADCAST # constant value
        dummyDict[EmulationOspfConfigConstants.NO_WRITE_CMD] = "dummyValue81" # static value
        dummyDict[EmulationOspfConfigConstants.NSSA_CAPABILITY_CMD] = "dummyValue82" # static value
        dummyDict[EmulationOspfConfigConstants.NUMBER_OF_RESTARTS_CMD] = "dummyValue83" # static value
        dummyDict[EmulationOspfConfigConstants.OOB_RESYNC_BREAKOUT_CMD] = "dummyValue84" # static value
        dummyDict[EmulationOspfConfigConstants.OPAQUE_LSA_FORWARDED_CMD] = "dummyValue85" # static value
        dummyDict[EmulationOspfConfigConstants.OPTION_BITS_CMD] = "dummyValue86" # static value
        dummyDict[EmulationOspfConfigConstants.OSPFV3_LSA_FLOOD_RATE_CONTROL_CMD] = "dummyValue87" # static value
        dummyDict[EmulationOspfConfigConstants.OVERRIDE_EXISTENCE_CHECK_CMD] = "dummyValue88" # static value
        dummyDict[EmulationOspfConfigConstants.OVERRIDE_TRACKING_CMD] = "dummyValue89" # static value
        dummyDict[EmulationOspfConfigConstants.PASSWORD_CMD] = "dummyValue90" # static value
        dummyDict[EmulationOspfConfigConstants.POLL_INTERVAL_CMD] = "dummyValue91" # static value
        dummyDict[EmulationOspfConfigConstants.PORT_HANDLE_CMD] = "dummyValue92" # static value
        dummyDict[EmulationOspfConfigConstants.PROTOCOL_NAME_CMD] = "dummyValue93" # static value
        dummyDict[EmulationOspfConfigConstants.RATE_CONTROL_INTERVAL_CMD] = "dummyValue94" # static value
        dummyDict[EmulationOspfConfigConstants.RESET_CMD] = "dummyValue95" # static value
        dummyDict[EmulationOspfConfigConstants.RESTART_DOWN_TIME_CMD] = "dummyValue96" # static value
        dummyDict[EmulationOspfConfigConstants.RESTART_REASON_CMD] = "dummyValue97" # static value
        dummyDict[EmulationOspfConfigConstants.RESTART_START_TIME_CMD] = "dummyValue98" # static value
        dummyDict[EmulationOspfConfigConstants.RESTART_UP_TIME_CMD] = "dummyValue99" # static value
        dummyDict[EmulationOspfConfigConstants.RETURN_DETAILED_HANDLES_CMD] = "dummyValue100" # static value
        dummyDict[EmulationOspfConfigConstants.ROUTER_ABR_CMD] = "dummyValue101" # static value
        dummyDict[EmulationOspfConfigConstants.ROUTER_ACTIVE_CMD] = "dummyValue102" # static value
        dummyDict[EmulationOspfConfigConstants.ROUTER_ASBR_CMD] = "dummyValue103" # static value
        dummyDict[EmulationOspfConfigConstants.ROUTER_BIT_CMD] = "dummyValue104" # static value
        dummyDict[EmulationOspfConfigConstants.ROUTER_ID_CMD] = "dummyValue105" # static value
        dummyDict[EmulationOspfConfigConstants.ROUTER_ID_STEP_CMD] = "dummyValue106" # static value
        dummyDict[EmulationOspfConfigConstants.ROUTER_INTERFACE_ACTIVE_CMD] = "dummyValue107" # static value
        dummyDict[EmulationOspfConfigConstants.ROUTER_PRIORITY_CMD] = "dummyValue108" # static value
        dummyDict[EmulationOspfConfigConstants.SESSION_TYPE_CMD] = EmulationOspfConfigConstants.SESSION_TYPE_OSPFV2 # constant value
        dummyDict[EmulationOspfConfigConstants.STRICT_LSA_CHECKING_CMD] = "dummyValue110" # static value
        dummyDict[EmulationOspfConfigConstants.SUPPORT_REASON_SW_RELOAD_OR_UPGRADE_CMD] = "dummyValue111" # static value
        dummyDict[EmulationOspfConfigConstants.SUPPORT_REASON_SW_RESTART_CMD] = "dummyValue112" # static value
        dummyDict[EmulationOspfConfigConstants.SUPPORT_REASON_SWITCH_TO_REDUNDANT_PROCESSOR_CONTROL_CMD] = "dummyValue113" # static value
        dummyDict[EmulationOspfConfigConstants.SUPPORT_REASON_UNKNOWN_CMD] = "dummyValue114" # static value
        dummyDict[EmulationOspfConfigConstants.TE_ADMIN_GROUP_CMD] = "dummyValue115" # static value
        dummyDict[EmulationOspfConfigConstants.TE_ENABLE_CMD] = "dummyValue116" # static value
        dummyDict[EmulationOspfConfigConstants.TE_MAX_BW_CMD] = "dummyValue117" # static value
        dummyDict[EmulationOspfConfigConstants.TE_MAX_RESV_BW_CMD] = "dummyValue118" # static value
        dummyDict[EmulationOspfConfigConstants.TE_METRIC_CMD] = "dummyValue119" # static value
        dummyDict[EmulationOspfConfigConstants.TE_ROUTER_ID_CMD] = "dummyValue120" # static value
        dummyDict[EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY0_CMD] = "dummyValue121" # static value
        dummyDict[EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY1_CMD] = "dummyValue122" # static value
        dummyDict[EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY2_CMD] = "dummyValue123" # static value
        dummyDict[EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY3_CMD] = "dummyValue124" # static value
        dummyDict[EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY4_CMD] = "dummyValue125" # static value
        dummyDict[EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY5_CMD] = "dummyValue126" # static value
        dummyDict[EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY6_CMD] = "dummyValue127" # static value
        dummyDict[EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY7_CMD] = "dummyValue128" # static value
        dummyDict[EmulationOspfConfigConstants.TRANSMIT_DELAY_CMD] = "dummyValue129" # static value
        dummyDict[EmulationOspfConfigConstants.TYPE_OF_SERVICE_ROUTING_CMD] = "dummyValue130" # static value
        dummyDict[EmulationOspfConfigConstants.UNUSED_CMD] = "dummyValue131" # static value
        dummyDict[EmulationOspfConfigConstants.V6_CMD] = "dummyValue132" # static value
        dummyDict[EmulationOspfConfigConstants.VALIDATE_RECEIVED_MTU_CMD] = "dummyValue133" # static value
        dummyDict[EmulationOspfConfigConstants.VCI_CMD] = "dummyValue134" # static value
        dummyDict[EmulationOspfConfigConstants.VCI_STEP_CMD] = "dummyValue135" # static value
        dummyDict[EmulationOspfConfigConstants.VLAN_CMD] = "dummyValue136" # static value
        dummyDict[EmulationOspfConfigConstants.VLAN_CFI_CMD] = "dummyValue137" # static value
        dummyDict[EmulationOspfConfigConstants.VLAN_ID_CMD] = "dummyValue138" # static value
        dummyDict[EmulationOspfConfigConstants.VLAN_ID_MODE_CMD] = EmulationOspfConfigConstants.VLAN_ID_MODE_ # constant value
        dummyDict[EmulationOspfConfigConstants.VLAN_ID_STEP_CMD] = "dummyValue140" # static value
        dummyDict[EmulationOspfConfigConstants.VLAN_USER_PRIORITY_CMD] = "dummyValue141" # static value
        dummyDict[EmulationOspfConfigConstants.VPI_CMD] = "dummyValue142" # static value
        dummyDict[EmulationOspfConfigConstants.VPI_STEP_CMD] = "dummyValue143" # static value

        api = device.getApi(EmulationOspfConfigConstants.EMULATION_OSPF_CONFIG_API)
        assert isinstance(api, EmulationOspfConfigApi)
        api.emulation_ospf_config(dummyDict)
    """
    def emulation_ospf_config(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::emulation_ospf_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_config_area_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_config option area_id
        Description:The OSPF area ID associated with the interface.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The OSPF area ID associated with the interface.
            DEFAULT

            0.0.0.0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'area_id_type' | value= 'ip' |
        Constants Available: AREA_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.AREA_ID_CMD : ipv4})

    def emulation_ospf_config_area_id_as_number(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_area_id_as_number_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_area_id_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_config option area_id_step
        Description:The OSPF area ID step associated with the -area_id option on the ISPF
            interface.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The OSPF area ID step associated with the -area_id option on the ISPF
            interface.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'area_id_type' | value= 'ip' |
        Constants Available: AREA_ID_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.AREA_ID_STEP_CMD : ipv4})

    def emulation_ospf_config_area_id_type(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_area_type(self, opt):
        """
        This is the method the command: emulation_ospf_config option area_type
        Description:The 'area_type' advertised in the Router LSA interface list.
            Valid options are:
            external-capable

            (default) A transit network.
            ppp

            A point-to-point network.
            stub

            A stub network.
            DEFAULT
                None
        Constants Available: AREA_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.AREA_TYPE_CMD : opt})

    def emulation_ospf_config_atm_encapsulation(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_attempt_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_attempt_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_attempt_rate(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_attempt_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_authentication_mode(self, opt):
        """
        This is the method the command: emulation_ospf_config option authentication_mode
        Description:This option defines the authentification mode used for OSPF.
            Valid options are:
            null

            (default) No authentication
            simple

            Clear text authentication (see also -password)
            md5

            MD5 based authentication (see also -md5_key and -md5_key_id)
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This option defines the authentification mode used for OSPF.
            Valid options are:
            null

            (default) No authentication
            simple

            Clear text authentication (see also -password)
            md5

            MD5 based authentication (see also -md5_key and -md5_key_id)
            DEFAULT
                None
        Constants Available: AUTHENTICATION_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.AUTHENTICATION_MODE_CMD : opt})

    def emulation_ospf_config_bfd_registration(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_count(self, range):
        """
        This is the method the command: emulation_ospf_config option count
        Description:Defines the number of OSPF routers to configure on the -port_handle.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Defines the number of OSPF routers to configure on the -port_handle.
            DEFAULT

            1
        Constants Available: COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.COUNT_CMD : range})

    def emulation_ospf_config_dead_interval(self, range):
        """
        This is the method the command: emulation_ospf_config option dead_interval
        Description:The time after which the DUT router is considered dead if it does not
            send HELLO messages.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The time after which the DUT router is considered dead if it does not
            send HELLO messages.
            DEFAULT
                None
        Constants Available: DEAD_INTERVAL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.DEAD_INTERVAL_CMD : range})

    def emulation_ospf_config_demand_circuit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option demand_circuit
        Description:Enables the Demand Circuit bit. Pertains to handling of demand circuits
            (DCs) by the router. CHOICES 0 1
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Enables the Demand Circuit bit. Pertains to handling of demand circuits
            (DCs) by the router. CHOICES 0 1
            DEFAULT

            0
        Constants Available: DEMAND_CIRCUIT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.DEMAND_CIRCUIT_CMD : bool_opt})

    def emulation_ospf_config_disable_auto_generate_link_lsa(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_disconnect_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_disconnect_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_disconnect_rate(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_disconnect_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_do_not_generate_router_lsa(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_enable_dr_bdr(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_enable_fast_hello(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_enable_ignore_db_desc_mtu(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_enable_support_rfc_5838(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option enable_support_rfc_5838
        Description:Enables the support for rfc 5838 in OSPFv3 router. This enables OSPFv3
            router to advertise ipv4 and ipv6 unicast an multicast routes CHOICES 0 1
            DEFAULT
                None
        Constants Available: ENABLE_SUPPORT_RFC_5838_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ENABLE_SUPPORT_RFC_5838_CMD : bool_opt})

    def emulation_ospf_config_external_attribute(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_external_capabilities(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_flood_lsupdates_per_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_get_next_session_mode(self):
        """
        This is the method the command: emulation_ospf_config option get_next_session_mode
        Constants Available: GET_NEXT_SESSION_MODE_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.GET_NEXT_SESSION_MODE_CMD : ""})

    def emulation_ospf_config_grace_period(self):
        """
        This is the method the command: emulation_ospf_config option grace_period
        Constants Available: GRACE_PERIOD_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.GRACE_PERIOD_CMD : ""})

    def emulation_ospf_config_graceful_restart_enable(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option graceful_restart_enable
        Description:Will enable graceful restart (HA) on the OSPF neighbor.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Will enable graceful restart (HA) on the OSPF neighbor.
            DEFAULT
                None
        Constants Available: GRACEFUL_RESTART_ENABLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.GRACEFUL_RESTART_ENABLE_CMD : bool_opt})

    def emulation_ospf_config_graceful_restart_helper_mode_enable(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option graceful_restart_helper_mode_enable
        Description:This parameter -graceful_restart_helper_mode_enable will allow Ixia
            toact as a helping neighbor to a restarting router.If the attribute is
            set to 1, the router will act as restarting router's neighbors, which
            must cooperate in order for the restart to be graceful.This
            attribute/argument is valid when session_type is ospfV3.0 - disable
            (default)1 - enable
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter -graceful_restart_helper_mode_enable will allow Ixia to
            act as a helping neighbor to a restarting router.If the attribute is set
            to 1, the router will act as restarting router's neighbors, which must
            cooperate in order for the restart to be graceful.This
            attribute/argument is valid when session_type is ospfV3. Valid choices
            are: 0 - disable (default) 1 - enable
            DEFAULT

            0
        Constants Available: GRACEFUL_RESTART_HELPER_MODE_ENABLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.GRACEFUL_RESTART_HELPER_MODE_ENABLE_CMD : bool_opt})

    def emulation_ospf_config_graceful_restart_restarting_mode_enable(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option graceful_restart_restarting_mode_enable
        Description:The new attribute -graceful_restart_restarting_mode_enable will allow 0
            - disable (default)1 - enable-grace_periodThis parameter denotes the
            time period (represent in seconds), between the restart/reload and the
            reestablishment of adjacencies, specified by the restarting router. Its
            value is specified in seconds and ranges from 1 to 1800.This attribute
            is valid/relevant when the router is in restarting mode, meaning
            graceful_restart_enable is set to 1.This attribute/argument is valid
            when session_type is ospfV3.-restart_reasonThis paramter allows user to
            select the reason for the router restart as one of the following
            options.This attribute is valid/relevant when the router is in
            restarting mode, i.e. graceful_restart_enable is set to 1.This
            attribute/argument is valid when session_type is ospfV3.unknown - The
            restart resaon is unknownsoftware_restart - (default) The restart resaon
            is software restartsoftware_reload_upgrade - The restart resaon is
            software reload or software
            upgrade.switch_to_redundant_control_processor - The restart resaon is
            swithing to redundant control processor.-number_of_restartsThe number of
            times the Ixia emulated OSPF router will move to Restarting and Up
            states before stopping the cycle. It ranges from 0 to the max value of a
            short type integer.This attribute is valid/relevant when the router is
            in restarting mode, i.e. graceful_restart_enable is set to 1. This
            attribute/argument is valid when session_type is
            ospfV3.-restart_start_timeThe router (Ixia) restarts after this timer
            gets fired, from the time the router reaches the full state.Its value is
            specified in seconds and ranges from 1 to the max value of a short type
            integer.This attribute is valid/relevant when the router is in
            restarting mode, i.e. graceful_restart_enable is set to 1.This
            attribute/argument is valid when session_type is ospfV3 and Valid if
            'number_of_restarts' value is greater than 0.-restart_down_timeThe time
            period the router will be down (to upgrade/reload software etc.) before
            sending any Hello packet or trying to re-establish the adjacencies. Its
            value is specified in seconds and ranges from 1 sec to the max value of
            a short type integer.It is user's responsibility to set the value less
            than the value of 'grace_period' for a successful graceful restart. This
            attribute is valid/relevant when the router is in restarting mode, i.e.
            graceful_restart_enable is set to 1.This attribute/argument is valid
            when session_type is ospfV3.-restart_up_timeAfter the session becomes
            full (gracefully or ungracefully), Ixia will wait for this configured
            interval before trying to repeat the Restart cycle. Its value is
            specified in seconds and ranges from 1 sec to the max value of a short
            type integer.This attribute is valid/relevant when the router is in
            restarting mode, i.e. graceful_restart_enable is set to 1. This
            attribute/argument is valid when session_type is ospfV3 and valid if
            'number_of_restarts' value is greater than 1.
            DEFAULT

            0
        Constants Available: GRACEFUL_RESTART_RESTARTING_MODE_ENABLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.GRACEFUL_RESTART_RESTARTING_MODE_ENABLE_CMD : bool_opt})

    def emulation_ospf_config_gre_checksum(self, any):
        """
        This is the method the command: emulation_ospf_config option gre_checksum
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: GRE_CHECKSUM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.GRE_CHECKSUM_CMD : any})

    def emulation_ospf_config_gre_local_ip(self, any):
        """
        This is the method the command: emulation_ospf_config option gre_local_ip
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: GRE_LOCAL_IP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.GRE_LOCAL_IP_CMD : any})

    def emulation_ospf_config_gre_remote_ip(self, any):
        """
        This is the method the command: emulation_ospf_config option gre_remote_ip
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: GRE_REMOTE_IP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.GRE_REMOTE_IP_CMD : any})

    def emulation_ospf_config_gre_tunnel(self, any):
        """
        This is the method the command: emulation_ospf_config option gre_tunnel
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: GRE_TUNNEL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.GRE_TUNNEL_CMD : any})

    def emulation_ospf_config_handle(self, any):
        """
        This is the method the command: emulation_ospf_config option handle
        Description:OSPF session handle for using the modes delete, modify, enable, and disable.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            OSPF session handle for using the modes delete, modify, enable, and
            disable. When -handle is provided with the /globals value the arguments
            that configure global protocol setting accept both multivalue handles
            and simple values. When -handle is provided with a a protocol stack
            handle or a protocol session handle, the arguments that configure global
            settings will only accept simple values. In this situation, these
            arguments will configure only the settings of the parent device group or
            the ports associated with the parent topology.
            DEFAULT
                None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.HANDLE_CMD : any})

    def emulation_ospf_config_hello_interval(self, range):
        """
        This is the method the command: emulation_ospf_config option hello_interval
        Description:The time between HELLO messages sent over the interface. RANGE 1-65535
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The time between HELLO messages sent over the interface. RANGE 1-65535
            DEFAULT
                None
        Constants Available: HELLO_INTERVAL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.HELLO_INTERVAL_CMD : range})

    def emulation_ospf_config_hello_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_host_route(self, any):
        """
        This is the method the command: emulation_ospf_config option host_route
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: HOST_ROUTE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.HOST_ROUTE_CMD : any})

    def emulation_ospf_config_ignore_db_desc_mtu(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_instance_id(self, range):
        """
        This is the method the command: emulation_ospf_config option instance_id
        Description:Defines the instance ID of the OSPFv3 process. It allows multiple
            instances of the OSPFv3 protocol to be run simultaneously over the same
            link. RANGE 0-255
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Defines the instance ID of the OSPFv3 process. It allows multiple
            instances of the OSPFv3 protocol to be run simultaneously over the same
            link. RANGE 0-255
            DEFAULT

            0
        Constants Available: INSTANCE_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INSTANCE_ID_CMD : range})

    def emulation_ospf_config_instance_id_step(self, range):
        """
        This is the method the command: emulation_ospf_config option instance_id_step
        Description:Step at which the -instance_id will be incremented. RANGE 0-255
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            Step at which the -instance_id will be incremented. RANGE 0-255
            DEFAULT

            0
        Constants Available: INSTANCE_ID_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INSTANCE_ID_STEP_CMD : range})

    def emulation_ospf_config_int_msg_exchange(self, any):
        """
        This is the method the command: emulation_ospf_config option int_msg_exchange
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: INT_MSG_EXCHANGE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INT_MSG_EXCHANGE_CMD : any})

    def emulation_ospf_config_inter_flood_lsupdate_burst_gap(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_interface_cost(self, range):
        """
        This is the method the command: emulation_ospf_config option interface_cost
        Description:The metric associated with the OSPF interface. RANGE 1-65535
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The metric associated with the OSPF interface. RANGE 1-65535
            DEFAULT
                None
        Constants Available: INTERFACE_COST_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INTERFACE_COST_CMD : range})

    def emulation_ospf_config_interface_handle(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_intf_ip_addr(self, ip):
        """
        This is the method the command: emulation_ospf_config option intf_ip_addr
        Description:The IP address of the Ixia Simulated OSPF router. This parameter is not
            valid on mode modify when IxTclProtocol is used. IP
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The IP address of the Ixia Simulated OSPF router. This parameter is not
            valid on mode modify when IxTclProtocol is used. IP
            DEFAULT
                None
        Constants Available: INTF_IP_ADDR_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INTF_IP_ADDR_CMD : ip})

    def emulation_ospf_config_intf_ip_addr_step(self, ip):
        """
        This is the method the command: emulation_ospf_config option intf_ip_addr_step
        Description:What step will be use for incrementing the -intf_ip_addr option.This
            parameter is not valid on mode modify when IxTclProtocol is used.
            (DEFAULT = 0.0.1.0 | 0:0:0:1::0)
            DEFAULT

            0.0.1.0 | 0:0:0:1::0
            IxNetwork-NGPF

            DESCRIPTION

            What step will be use for incrementing the -intf_ip_addr option. This
            parameter is not valid on mode modify when IxTclProtocol is used.
            DEFAULT

            0.0.1.0
        Constants Available: INTF_IP_ADDR_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INTF_IP_ADDR_STEP_CMD : ip})

    def emulation_ospf_config_intf_ipv6_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_intf_ipv6_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_intf_ipv6_prefix_length(self, range):
        """
        This is the method the command: emulation_ospf_config option intf_ipv6_prefix_length
        Description:Defines the mask of the IP address used for the Ixia (-intf_ipv6_addr)
            and the DUT interface. This parameter is not valid on mode modify when
            IxTclProtocol is used. RANGE 1-128
            DEFAULT

            64
        Constants Available: INTF_IPV6_PREFIX_LENGTH_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INTF_IPV6_PREFIX_LENGTH_CMD : range})

    def emulation_ospf_config_intf_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_ipv6_gateway_ip(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_ipv6_gateway_ip_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_link_metric(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_loopback_ip_addr(self, ip):
        """
        This is the method the command: emulation_ospf_config option loopback_ip_addr
        Description:Defines the IP address of the loopback interface for MPLS VPN
            testing.This parameter is not valid on mode modify when IxTclProtocol is
            used.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Defines the IP address of the loopback interface for MPLS VPN testing.
            This parameter is not valid on mode modify when IxTclProtocol is used.
            DEFAULT

            0.0.0.0
        Constants Available: LOOPBACK_IP_ADDR_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.LOOPBACK_IP_ADDR_CMD : ip})

    def emulation_ospf_config_loopback_ip_addr_step(self, ip):
        """
        This is the method the command: emulation_ospf_config option loopback_ip_addr_step
        Description:Defines the IP address step of the loopback interface for MPLS VPN.This
            parameter is not valid on mode modify when IxTclProtocol is used.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Defines the IP address step of the loopback interface for MPLS VPN. This
            parameter is not valid on mode modify when IxTclProtocol is used.
            DEFAULT

            0.0.0.0
        Constants Available: LOOPBACK_IP_ADDR_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.LOOPBACK_IP_ADDR_STEP_CMD : ip})

    def emulation_ospf_config_lsa_discard_mode(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option lsa_discard_mode
        Description:Enables/Disables the LSA discard mode on the OSPF router. CHOICES 0 1
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Enables/Disables the LSA discard mode on the OSPF router. CHOICES 0 1
            DEFAULT
                None
        Constants Available: LSA_DISCARD_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.LSA_DISCARD_MODE_CMD : bool_opt})

    def emulation_ospf_config_lsa_refresh_time(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_lsa_retransmit_delay(self, any):
        """
        This is the method the command: emulation_ospf_config option lsa_retransmit_delay
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LSA_RETRANSMIT_DELAY_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.LSA_RETRANSMIT_DELAY_CMD : any})

    def emulation_ospf_config_lsa_retransmit_time(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_mac_address_init(self, mac):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_mac_address_step(self, mac):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_max_ls_updates_per_burst(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_max_lsas_per_pkt(self, any):
        """
        This is the method the command: emulation_ospf_config option max_lsas_per_pkt
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: MAX_LSAS_PER_PKT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MAX_LSAS_PER_PKT_CMD : any})

    def emulation_ospf_config_max_mtu(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_md5_key(self, any):
        """
        This is the method the command: emulation_ospf_config option md5_key
        Description:Active only when 'MD5' is selected in the Authentication field. Enter a
            character string (maximum 16 characters) to be used as a 'secret' MD5 Key.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Active only when 'MD5' is selected in the Authentication field. Enter a
            character string (maximum 16 characters) to be used as a 'secret' MD5 Key.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'authentication_mode' | value= 'md5' |
        Constants Available: MD5_KEY_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MD5_KEY_CMD : any})

    def emulation_ospf_config_md5_key_id(self, range):
        """
        This is the method the command: emulation_ospf_config option md5_key_id
        Description:Active only when 'MD5' is selected in the Authentication field. Enter a
            value to be used as a Key ID. This identifier is associated with the MD5
            Key entered previously.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Active only when 'MD5' is selected in the Authentication field. Enter a
            value to be used as a Key ID. This identifier is associated with the MD5
            Key entered previously.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'authentication_mode' | value= 'md5' |
        Constants Available: MD5_KEY_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MD5_KEY_ID_CMD : range})

    def emulation_ospf_config_mode(self, opt):
        """
        This is the method the command: emulation_ospf_config option mode
        Description:enable - Enables the OSPF router on the Ixia interface.disable -
            Disables the OSPF router.delete - Deletes the OSPF router on the Ixia
            interface.create - Creates the OSPF router on the Ixia interface.modify
            - Modifies the OSPF router on the Ixia interface.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Not defined
            Valid options are:
            create

            Creates the OSPF router on the Ixia interface.
            delete

            Deletes the OSPF router on the Ixia interface.
            modify

            Modifies the OSPF router on the Ixia interface.
            enable

            Enables the OSPF router on the Ixia interface.
            disable

            Disables the OSPF router.
            DEFAULT

            create
        Constants Available: MODE_CMD
        Supported:IxNetwork[M] , IxOS/IxNetwork-FT[M]
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MODE_CMD : opt})

    def emulation_ospf_config_mtu(self, range):
        """
        This is the method the command: emulation_ospf_config option mtu
        Description:The advertised MTU value in database entries sent to other routers
            create on the Ixia interface. RANGE 68-9216.OSPFv2 Only. For OSPFv3 this
            option is ignored.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The advertised MTU value in database entries sent to other routers
            create on the Ixia interface. RANGE 68-9216. OSPFv2 Only. For OSPFv3
            this option is ignored.
            DEFAULT
                None
        Constants Available: MTU_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MTU_CMD : range})

    def emulation_ospf_config_multicast_capability(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_neighbor_dr_eligibility(self, any):
        """
        This is the method the command: emulation_ospf_config option neighbor_dr_eligibility
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NEIGHBOR_DR_ELIGIBILITY_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.NEIGHBOR_DR_ELIGIBILITY_CMD : any})

    def emulation_ospf_config_neighbor_intf_ip_addr(self, ip):
        """
        This is the method the command: emulation_ospf_config option neighbor_intf_ip_addr
        Description:The IP address of the DUT OSPF Interface. This parameter is not valid on
            mode modify when IxTclProtocol is used. (DEFAULT = 0.0.0.0 | 0:0:0:0::0)
            DEFAULT

            0.0.0.0 | 0:0:0:0::0
            IxNetwork-NGPF

            DESCRIPTION

            The IP address of the DUT OSPF Interface. This parameter is not valid on
            mode modify when IxTclProtocol is used.
            DEFAULT

            0.0.0.0
        Constants Available: NEIGHBOR_INTF_IP_ADDR_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.NEIGHBOR_INTF_IP_ADDR_CMD : ip})

    def emulation_ospf_config_neighbor_intf_ip_addr_step(self, ip):
        """
        This is the method the command: emulation_ospf_config option neighbor_intf_ip_addr_step
        Description:This parameter is not valid on mode modify when IxTclProtocol is used.
            What step will be use for incrementing the -neighbor_intf_ip_addr
            option.(DEFAULT = 0.0.0.0 | 0:0:0:0::0)
            DEFAULT

            0.0.0.0 | 0:0:0:0::0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is not valid on mode modify when IxTclProtocol is used.
            What step will be use for incrementing the -neighbor_intf_ip_addr option.
            DEFAULT

            0.0.0.0
        Constants Available: NEIGHBOR_INTF_IP_ADDR_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.NEIGHBOR_INTF_IP_ADDR_STEP_CMD : ip})

    def emulation_ospf_config_neighbor_router_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_config option neighbor_router_id
        Description:Available only for use when the Point-Multipoint network type is
            selected. The DUT IP Interface address can be provided.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Available only for use when the Point-Multipoint network type is
            selected. The DUT IP Interface address can be provided.
            DEFAULT
                None
        Constants Available: NEIGHBOR_ROUTER_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.NEIGHBOR_ROUTER_ID_CMD : ipv4})

    def emulation_ospf_config_neighbor_router_id_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_config option neighbor_router_id_step
        Description:Available only for use when the Point-Multipoint network type is
            selected. The DUT IP Interface address step can be provided.
            DEFAULT

            0.0.1.0
            IxNetwork-NGPF

            DESCRIPTION

            Available only for use when the Point-Multipoint network type is
            selected. The DUT IP Interface address step can be provided.
            DEFAULT

            0.0.1.0
        Constants Available: NEIGHBOR_ROUTER_ID_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.NEIGHBOR_ROUTER_ID_STEP_CMD : ipv4})

    def emulation_ospf_config_network_type(self, opt):
        """
        This is the method the command: emulation_ospf_config option network_type
        Description:broadcast - (default) Indicates that the network is a broadcast network,
            as in an Ethernet connection.ptop - Indicates that the network is point
            to point.ptomp - Indicates that the network is point to multi-point
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Indicates the type of network for the interface.
            Valid options are:
            broadcast

            (default) Indicates that the network is a broadcast network, as in an
            Ethernet connection.
            ptomp

            Indicates that the network is point to multi-point
            ptop

            Indicates that the network is point to point.
            DEFAULT
                None
        Constants Available: NETWORK_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.NETWORK_TYPE_CMD : opt})

    def emulation_ospf_config_no_write(self, flag):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_nssa_capability(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_number_of_restarts(self):
        """
        This is the method the command: emulation_ospf_config option number_of_restarts
        Constants Available: NUMBER_OF_RESTARTS_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.NUMBER_OF_RESTARTS_CMD : ""})

    def emulation_ospf_config_oob_resync_breakout(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_opaque_lsa_forwarded(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_option_bits(self, any):
        """
        This is the method the command: emulation_ospf_config option option_bits
        Description:The bit sum of the different OSPF option bits. This switch is for users
            to customize options since area_type will determine a default value for
            those bits. The Demand circuit option can be modified with the
            -demand_circuit option. In HEX.If (option_bits & 0x8) then area_id must
            not be 0. (option_bits & 0x2) is not allowed - can't have external
            routing and NSSA capability at the same time.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The bit sum of the different OSPF option bits. This switch is for users
            to customize options since area_type will determine a default value for
            those bits. The Demand circuit option can be modified with the
            -demand_circuit option. In HEX. If (option_bits & 0x8) then area_id must
            not be 0. (option_bits & 0x2) is not allowed - can't have external
            routing and NSSA capability at the same time.
            DEFAULT
                None
        Constants Available: OPTION_BITS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.OPTION_BITS_CMD : any})

    def emulation_ospf_config_ospfv3_lsa_flood_rate_control(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_override_existence_check(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_override_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_password(self, any):
        """
        This is the method the command: emulation_ospf_config option password
        Description:Password to be used in the OSPF authentication mode is enabled and set
            to 'simple'.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Password to be used in the OSPF authentication mode is enabled and set
            to 'simple'.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'authentication_mode' | value= 'simple' |
        Constants Available: PASSWORD_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.PASSWORD_CMD : any})

    def emulation_ospf_config_poll_interval(self, any):
        """
        This is the method the command: emulation_ospf_config option poll_interval
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: POLL_INTERVAL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.POLL_INTERVAL_CMD : any})

    def emulation_ospf_config_port_handle(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_protocol_name(self, alpha):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_rate_control_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_reset(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_restart_down_time(self):
        """
        This is the method the command: emulation_ospf_config option restart_down_time
        Constants Available: RESTART_DOWN_TIME_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.RESTART_DOWN_TIME_CMD : ""})

    def emulation_ospf_config_restart_reason(self):
        """
        This is the method the command: emulation_ospf_config option restart_reason
        Constants Available: RESTART_REASON_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.RESTART_REASON_CMD : ""})

    def emulation_ospf_config_restart_start_time(self):
        """
        This is the method the command: emulation_ospf_config option restart_start_time
        Constants Available: RESTART_START_TIME_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.RESTART_START_TIME_CMD : ""})

    def emulation_ospf_config_restart_up_time(self):
        """
        This is the method the command: emulation_ospf_config option restart_up_time
        Constants Available: RESTART_UP_TIME_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.RESTART_UP_TIME_CMD : ""})

    def emulation_ospf_config_return_detailed_handles(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_router_abr(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_router_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_router_asbr(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_router_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_router_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_config option router_id
        Description:The Router ID for this emulated OSPF Router, in IPv4 format. IP
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The Router ID for this emulated OSPF Router, in IPv4 format. IP
            DEFAULT
                None
        Constants Available: ROUTER_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ROUTER_ID_CMD : ipv4})

    def emulation_ospf_config_router_id_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_config option router_id_step
        Description:The Router ID step for this emulated OSPF Router, in IPv4 format. IP
            DEFAULT

            0.0.1.0
            IxNetwork-NGPF

            DESCRIPTION

            The Router ID step for this emulated OSPF Router, in IPv4 format. IP
            DEFAULT

            0.0.1.0
        Constants Available: ROUTER_ID_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ROUTER_ID_STEP_CMD : ipv4})

    def emulation_ospf_config_router_interface_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_router_priority(self, range):
        """
        This is the method the command: emulation_ospf_config option router_priority
        Description:The priority of the interface, for use in election of the designated or
            backup master. RANGE 0-255
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The priority of the interface, for use in election of the designated or
            backup master. RANGE 0-255
            DEFAULT
                None
        Constants Available: ROUTER_PRIORITY_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ROUTER_PRIORITY_CMD : range})

    def emulation_ospf_config_session_type(self, opt):
        """
        This is the method the command: emulation_ospf_config option session_type
        Description:The OSPF version to be emulated. CHOICES: ospfv2 ospfv3.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The OSPF version to be emulated. CHOICES: ospfv2 ospfv3.
            Valid options are:
            ospfv2

            ospfv3

            DEFAULT

            ospfv2
        Constants Available: SESSION_TYPE_CMD
        Supported:IxNetwork[M] , IxOS/IxNetwork-FT[M]
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.SESSION_TYPE_CMD : opt})

    def emulation_ospf_config_strict_lsa_checking(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option strict_lsa_checking
        Description:If enabled, the helping router continues to help the restarting router
            even if there is a topology change detected. Relevant with
            'graceful_restart_helper_mode_enable'. This attribute is associated with
            the four Graceful Restart reasons. This attribute/argument is valid when
            session_type is ospfV3.
            DEFAULT

            1
            IxNetwork-NGPF

            DESCRIPTION

            If enabled, the helping router continues to help the restarting router
            even if there is a topology change detected. Relevant with
            'graceful_restart_helper_mode_enable'. This attribute is associated with
            the four Graceful Restart reasons. This attribute/argument is valid when
            session_type is ospfV3.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'graceful_restart_helper_mode_enable' | value= '1' |
        Constants Available: STRICT_LSA_CHECKING_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.STRICT_LSA_CHECKING_CMD : bool_opt})

    def emulation_ospf_config_support_reason_sw_reload_or_upgrade(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option support_reason_sw_reload_or_upgrade
        Description:This is one of the reasons supported by this helping router when the
            neighboring router gracefully restarts.Helping router will support only
            those restart reasons which are enabled by the user. User can select
            more than one reason at a time. Relevant with
            'graceful_restart_helper_mode_enable'.This attribute/argument is valid
            when session_type is ospfV3.
            DEFAULT

            1
            IxNetwork-NGPF

            DESCRIPTION

            This is one of the reasons supported by this helping router when the
            neighboring router gracefully restarts. Helping router will support only
            those restart reasons which are enabled by the user. User can select
            more than one reason at a time. Relevant with
            'graceful_restart_helper_mode_enable'. This attribute/argument is valid
            when session_type is ospfV3.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'graceful_restart_helper_mode_enable' | value= '1' |
        Constants Available: SUPPORT_REASON_SW_RELOAD_OR_UPGRADE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.SUPPORT_REASON_SW_RELOAD_OR_UPGRADE_CMD : bool_opt})

    def emulation_ospf_config_support_reason_sw_restart(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option support_reason_sw_restart
        Description:This is one of the reasons supported by this helping router when the
            neighboring router gracefully restarts. Helping router will support only
            those restart reasons which are enabled by the user. User can select
            more than one reason at a time. Relevant with
            'graceful_restart_helper_mode_enable'.This attribute/argument is valid
            when session_type is ospfV3.
            DEFAULT

            1
            IxNetwork-NGPF

            DESCRIPTION

            This is one of the reasons supported by this helping router when the
            neighboring router gracefully restarts. Helping router will support only
            those restart reasons which are enabled by the user. User can select
            more than one reason at a time. Relevant with
            'graceful_restart_helper_mode_enable'.This attribute/argument is valid
            when session_type is ospfV3.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'graceful_restart_helper_mode_enable' | value= '1' |
        Constants Available: SUPPORT_REASON_SW_RESTART_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.SUPPORT_REASON_SW_RESTART_CMD : bool_opt})

    def emulation_ospf_config_support_reason_switch_to_redundant_processor_control(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option support_reason_switch_to_redundant_processor_control
        Description:This is one of the reasons supported by this helping router when the
            neighboring router gracefully restarts.Helping router will support only
            those restart reasons which are enabled by the user. User can select
            more than one reason at a time. Relevant with
            'graceful_restart_helper_mode_enable'.This attribute/argument is valid
            when session_type is ospfV3.
            DEFAULT

            1
            IxNetwork-NGPF

            DESCRIPTION

            This is one of the reasons supported by this helping router when the
            neighboring router gracefully restarts. Helping router will support only
            those restart reasons which are enabled by the user. User can select
            more than one reason at a time. Relevant with
            'graceful_restart_helper_mode_enable'. This attribute/argument is valid
            when session_type is ospfV3.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'graceful_restart_helper_mode_enable' | value= '1' |
        Constants Available: SUPPORT_REASON_SWITCH_TO_REDUNDANT_PROCESSOR_CONTROL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.SUPPORT_REASON_SWITCH_TO_REDUNDANT_PROCESSOR_CONTROL_CMD : bool_opt})

    def emulation_ospf_config_support_reason_unknown(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option support_reason_unknown
        Description:This is one of the reasons supported by this helping router when the
            neighboring router gracefully restarts.Helping router will support only
            those restart reasons which are enabled by the user. User can select
            more than one reason at a time. Relevant with
            'graceful_restart_helper_mode_enable'.This attribute/argument is valid
            when session_type is ospfV3.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This is one of the reasons supported by this helping router when the
            neighboring router gracefully restarts. Helping router will support only
            those restart reasons which are enabled by the user. User can select
            more than one reason at a time. Relevant with
            'graceful_restart_helper_mode_enable'. This attribute/argument is valid
            when session_type is ospfV3.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'graceful_restart_helper_mode_enable' | value= '1' |
        Constants Available: SUPPORT_REASON_UNKNOWN_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.SUPPORT_REASON_UNKNOWN_CMD : bool_opt})

    def emulation_ospf_config_te_admin_group(self, any):
        """
        This is the method the command: emulation_ospf_config option te_admin_group
        Description:Assignment of traffic engineering administrative group numbers to the
            interface.Valid only with IxTclNetwork API.
            DEFAULT

            00.00.00.00
            IxNetwork-NGPF

            DESCRIPTION

            Assignment of traffic engineering administrative group numbers to the
            interface. Valid only with IxTclNetwork API.
            DEFAULT
                None
        Constants Available: TE_ADMIN_GROUP_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_ADMIN_GROUP_CMD : any})

    def emulation_ospf_config_te_enable(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option te_enable
        Description:If set to 1, this will enable Traffic Engineering on the OSPF router.
            The user can then configure the TE parameters by using '-te_metric',
            '-te_max_bw', '-te_max_resv_bw', '-te_unresv_bw_priority0-7'.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If set to 1, this will enable Traffic Engineering on the OSPF router.
            The user can then configure the TE parameters by using '-te_metric',
            '-te_max_bw', '-te_max_resv_bw', '-te_unresv_bw_priority0-7'.
            DEFAULT
                None
        Constants Available: TE_ENABLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_ENABLE_CMD : bool_opt})

    def emulation_ospf_config_te_max_bw(self, any):
        """
        This is the method the command: emulation_ospf_config option te_max_bw
        Description:If 'te_enable' is 1, then this indicates the maximum bandwidth that can
            be used on the link between this interface and its neighbors in the
            outbound direction.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this indicates the maximum bandwidth that can
            be used on the link between this interface and its neighbors in the
            outbound direction.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_MAX_BW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_MAX_BW_CMD : any})

    def emulation_ospf_config_te_max_resv_bw(self, any):
        """
        This is the method the command: emulation_ospf_config option te_max_resv_bw
        Description:If 'te_enable' is 1, then this indicates the maximum bandwidth, in bytes
            per second, that can be reserved on the link between this interface and
            its neighbors in the outbound direction.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this indicates the maximum bandwidth, in
            bytes per second, that can be reserved on the link between this
            interface and its neighbors in the outbound direction.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_MAX_RESV_BW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_MAX_RESV_BW_CMD : any})

    def emulation_ospf_config_te_metric(self, range):
        """
        This is the method the command: emulation_ospf_config option te_metric
        Description:If set to 1, then this indicates the traffic engineering metric
            associated with the interface. RANGE 1-2147483647
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If set to 1, then this indicates the traffic engineering metric
            associated with the interface. RANGE 1-2147483647
            DEFAULT
                None
        Constants Available: TE_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_METRIC_CMD : range})

    def emulation_ospf_config_te_router_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_config option te_router_id
        Description:This parameter is ignored.
            DEFAULT
                None
        Constants Available: TE_ROUTER_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_ROUTER_ID_CMD : ipv4})

    def emulation_ospf_config_te_unresv_bw_priority0(self, any):
        """
        This is the method the command: emulation_ospf_config option te_unresv_bw_priority0
        Description:If 'te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 0 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 0. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 0 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 0. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_UNRESV_BW_PRIORITY0_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY0_CMD : any})

    def emulation_ospf_config_te_unresv_bw_priority1(self, any):
        """
        This is the method the command: emulation_ospf_config option te_unresv_bw_priority1
        Description:If 'te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 1 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 1. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 1 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 1. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_UNRESV_BW_PRIORITY1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY1_CMD : any})

    def emulation_ospf_config_te_unresv_bw_priority2(self, any):
        """
        This is the method the command: emulation_ospf_config option te_unresv_bw_priority2
        Description:If 'te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 2 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 2. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 2 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 2. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_UNRESV_BW_PRIORITY2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY2_CMD : any})

    def emulation_ospf_config_te_unresv_bw_priority3(self, any):
        """
        This is the method the command: emulation_ospf_config option te_unresv_bw_priority3
        Description:If 'te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 3 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 3. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 3 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 3. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_UNRESV_BW_PRIORITY3_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY3_CMD : any})

    def emulation_ospf_config_te_unresv_bw_priority4(self, any):
        """
        This is the method the command: emulation_ospf_config option te_unresv_bw_priority4
        Description:If 'te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 4 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 4. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 4 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 4. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_UNRESV_BW_PRIORITY4_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY4_CMD : any})

    def emulation_ospf_config_te_unresv_bw_priority5(self, any):
        """
        This is the method the command: emulation_ospf_config option te_unresv_bw_priority5
        Description:If 'te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 5 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 5. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 5 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 5. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_UNRESV_BW_PRIORITY5_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY5_CMD : any})

    def emulation_ospf_config_te_unresv_bw_priority6(self, any):
        """
        This is the method the command: emulation_ospf_config option te_unresv_bw_priority6
        Description:If 'te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 6 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 6. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 6 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 6. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_UNRESV_BW_PRIORITY6_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY6_CMD : any})

    def emulation_ospf_config_te_unresv_bw_priority7(self, any):
        """
        This is the method the command: emulation_ospf_config option te_unresv_bw_priority7
        Description:If 'te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 7 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 7. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If '-te_enable' is 1, then this value indicates the amount of bandwidth,
            in bytes per second, not yet reserved at the 7 priority level. This
            value corresponds to the bandwidth that can be reserved with a setup
            priority of 7. The value must be less than the maxReservableBandwidth
            option.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'te_enable' | value= '1' |
        Constants Available: TE_UNRESV_BW_PRIORITY7_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY7_CMD : any})

    def emulation_ospf_config_transmit_delay(self, any):
        """
        This is the method the command: emulation_ospf_config option transmit_delay
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: TRANSMIT_DELAY_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TRANSMIT_DELAY_CMD : any})

    def emulation_ospf_config_type_of_service_routing(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_unused(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_v6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_validate_received_mtu(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_vci(self, range):
        """
        This is the method the command: emulation_ospf_config option vci
        Description:This parameter is not valid on mode modify when IxTclProtocol is used.
            VCI for emulated router node. RANGE 0-65535
            DEFAULT
                None
        Constants Available: VCI_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VCI_CMD : range})

    def emulation_ospf_config_vci_step(self, any):
        """
        This is the method the command: emulation_ospf_config option vci_step
        Description:This parameter is not valid on mode modify when IxTclProtocol is used.
            The step value used for incrementing the -vci option.When vci_step
            causes the vci value to exceed it's maximum value the increment will be
            done modulo .Examples: vci = 65534; vci_step = 2 -> new vci value = 0vci
            = 65535; vci_step = 11 -> new vci value = 10
            DEFAULT
                None
        Constants Available: VCI_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VCI_STEP_CMD : any})

    def emulation_ospf_config_vlan(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_vlan_cfi(self):
        """
        This is the method the command: emulation_ospf_config option vlan_cfi
        Constants Available: VLAN_CFI_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VLAN_CFI_CMD : ""})

    def emulation_ospf_config_vlan_id(self, range):
        """
        This is the method the command: emulation_ospf_config option vlan_id
        Description:If VLAN is enable on the Ixia interface, this option will configure the
            VLAN number. This parameter is not valid on mode modify when
            IxTclProtocol is used. RANGE 0-4095
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If VLAN is enable on the Ixia interface, this option will configure the
            VLAN number. This parameter is not valid on mode modify when
            IxTclProtocol is used. RANGE 0-4095
            DEFAULT
                None
        Constants Available: VLAN_ID_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VLAN_ID_CMD : range})

    def emulation_ospf_config_vlan_id_mode(self, opt):
        """
        This is the method the command: emulation_ospf_config option vlan_id_mode
        Description:If the user configures more than one interface on the Ixia with VLAN, he
            can choose to automatically increment the VLAN tag or leave it idle for
            each interface. CHOICES fixed increment. This parameter is not valid on
            mode modify when IxTclProtocol is used.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If the user configures more than one interface on the Ixia with VLAN, he
            can choose to automatically increment the VLAN tag or leave it idle for
            each interface. CHOICES fixed increment. This parameter is not valid on
            mode modify when IxTclProtocol is used.
            Valid options are:
            fixed

            increment

            DEFAULT

            increment
        Constants Available: VLAN_ID_MODE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VLAN_ID_MODE_CMD : opt})

    def emulation_ospf_config_vlan_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_vlan_user_priority(self, range):
        """
        This is the method the command: emulation_ospf_config option vlan_user_priority
        Description:This parameter is not valid on mode modify when IxTclProtocol is used.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is not valid on mode modify when IxTclProtocol is used.
            DEFAULT

            0
        Constants Available: VLAN_USER_PRIORITY_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VLAN_USER_PRIORITY_CMD : range})

    def emulation_ospf_config_vpi(self, range):
        """
        This is the method the command: emulation_ospf_config option vpi
        Description:This parameter is not valid on mode modify when IxTclProtocol is used.
            VPI for emulated router node. RANGE 0-255
            DEFAULT
                None
        Constants Available: VPI_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VPI_CMD : range})

    def emulation_ospf_config_vpi_step(self, any):
        """
        This is the method the command: emulation_ospf_config option vpi_step
        Description:This parameter is not valid on mode modify when IxTclProtocol is used.
            The step value used for incrementing the -vpi option.When vpi_step
            causes the vpi value to exceed it's maximum value the increment will be
            done modulo .Examples: vpi = 254; vpi_step = 2 -> new vpi value = 0vpi =
            255; vpi_step = 11 -> new vpi value = 10
            DEFAULT
                None
        Constants Available: VPI_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VPI_STEP_CMD : any})


"""
    This is the Constants class for the command: emulation_ospf_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationOspfConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    EMULATION_OSPF_CONFIG_API = "EMULATION_OSPF_CONFIG_API"

    AREA_ID_CMD = "area_id"

    AREA_ID_AS_NUMBER_CMD = "area_id_as_number"

    AREA_ID_AS_NUMBER_STEP_CMD = "area_id_as_number_step"

    AREA_ID_STEP_CMD = "area_id_step"

    AREA_ID_TYPE_CMD = "area_id_type"
    # Constant values for AREA_ID_TYPE_CMD
    AREA_ID_TYPE_AREA_ID_AS_IP = "area_id_as_ip"
    AREA_ID_TYPE_AREA_ID_AS_NUMBER = "area_id_as_number"
    AREA_ID_TYPE_IP = "ip"
    AREA_ID_TYPE_NUMBER = "number"

    AREA_TYPE_CMD = "area_type"
    # Constant values for AREA_TYPE_CMD
    AREA_TYPE_EXTERNALCAPABLE = "externalcapable"
    AREA_TYPE_PPP = "ppp"
    AREA_TYPE_STUB = "stub"

    ATM_ENCAPSULATION_CMD = "atm_encapsulation"
    # Constant values for ATM_ENCAPSULATION_CMD
    ATM_ENCAPSULATION_LLCBRIDGEDETHERNETFCS = "LLCBridgedEthernetFCS"
    ATM_ENCAPSULATION_LLCBRIDGEDETHERNETNOFCS = "LLCBridgedEthernetNoFCS"
    ATM_ENCAPSULATION_LLCROUTEDCLIP = "LLCRoutedCLIP"
    ATM_ENCAPSULATION_VCCMUXBRIDGEDETHERNETFCS = "VccMuxBridgedEthernetFCS"
    ATM_ENCAPSULATION_VCCMUXBRIDGEDETHERNETNOFCS = "VccMuxBridgedEthernetNoFCS"
    ATM_ENCAPSULATION_VCCMUXIPV4ROUTED = "VccMuxIPV4Routed"
    ATM_ENCAPSULATION_VCCMUXIPV6ROUTED = "VccMuxIPV6Routed"

    ATTEMPT_ENABLED_CMD = "attempt_enabled"

    ATTEMPT_INTERVAL_CMD = "attempt_interval"

    ATTEMPT_RATE_CMD = "attempt_rate"

    ATTEMPT_SCALE_MODE_CMD = "attempt_scale_mode"
    # Constant values for ATTEMPT_SCALE_MODE_CMD
    ATTEMPT_SCALE_MODE_DEVICE_GROUP = "device_group"
    ATTEMPT_SCALE_MODE_PORT = "port"

    AUTHENTICATION_MODE_CMD = "authentication_mode"
    # Constant values for AUTHENTICATION_MODE_CMD
    AUTHENTICATION_MODE_MD5 = "md5"
    AUTHENTICATION_MODE_NULL = "null"
    AUTHENTICATION_MODE_SIMPLE = "simple"

    BFD_REGISTRATION_CMD = "bfd_registration"

    COUNT_CMD = "count"

    DEAD_INTERVAL_CMD = "dead_interval"

    DEMAND_CIRCUIT_CMD = "demand_circuit"

    DISABLE_AUTO_GENERATE_LINK_LSA_CMD = "disable_auto_generate_link_lsa"

    DISCONNECT_ENABLED_CMD = "disconnect_enabled"

    DISCONNECT_INTERVAL_CMD = "disconnect_interval"

    DISCONNECT_RATE_CMD = "disconnect_rate"

    DISCONNECT_SCALE_MODE_CMD = "disconnect_scale_mode"
    # Constant values for DISCONNECT_SCALE_MODE_CMD
    DISCONNECT_SCALE_MODE_DEVICE_GROUP = "device_group"
    DISCONNECT_SCALE_MODE_PORT = "port"

    DO_NOT_GENERATE_ROUTER_LSA_CMD = "do_not_generate_router_lsa"

    ENABLE_DR_BDR_CMD = "enable_dr_bdr"

    ENABLE_FAST_HELLO_CMD = "enable_fast_hello"

    ENABLE_IGNORE_DB_DESC_MTU_CMD = "enable_ignore_db_desc_mtu"

    ENABLE_SUPPORT_RFC_5838_CMD = "enable_support_rfc_5838"

    EXTERNAL_ATTRIBUTE_CMD = "external_attribute"

    EXTERNAL_CAPABILITIES_CMD = "external_capabilities"

    FLOOD_LSUPDATES_PER_INTERVAL_CMD = "flood_lsupdates_per_interval"

    GET_NEXT_SESSION_MODE_CMD = "get_next_session_mode"

    GRACE_PERIOD_CMD = "grace_period"

    GRACEFUL_RESTART_ENABLE_CMD = "graceful_restart_enable"

    GRACEFUL_RESTART_HELPER_MODE_ENABLE_CMD = "graceful_restart_helper_mode_enable"

    GRACEFUL_RESTART_RESTARTING_MODE_ENABLE_CMD = "graceful_restart_restarting_mode_enable"

    GRE_CHECKSUM_CMD = "gre_checksum"

    GRE_LOCAL_IP_CMD = "gre_local_ip"

    GRE_REMOTE_IP_CMD = "gre_remote_ip"

    GRE_TUNNEL_CMD = "gre_tunnel"

    HANDLE_CMD = "handle"

    HELLO_INTERVAL_CMD = "hello_interval"

    HELLO_MULTIPLIER_CMD = "hello_multiplier"

    HOST_ROUTE_CMD = "host_route"

    IGNORE_DB_DESC_MTU_CMD = "ignore_db_desc_mtu"

    INSTANCE_ID_CMD = "instance_id"

    INSTANCE_ID_STEP_CMD = "instance_id_step"

    INT_MSG_EXCHANGE_CMD = "int_msg_exchange"

    INTER_FLOOD_LSUPDATE_BURST_GAP_CMD = "inter_flood_lsupdate_burst_gap"

    INTERFACE_COST_CMD = "interface_cost"

    INTERFACE_HANDLE_CMD = "interface_handle"

    INTF_IP_ADDR_CMD = "intf_ip_addr"

    INTF_IP_ADDR_STEP_CMD = "intf_ip_addr_step"

    INTF_IPV6_ADDR_CMD = "intf_ipv6_addr"

    INTF_IPV6_ADDR_STEP_CMD = "intf_ipv6_addr_step"

    INTF_IPV6_PREFIX_LENGTH_CMD = "intf_ipv6_prefix_length"

    INTF_PREFIX_LENGTH_CMD = "intf_prefix_length"

    IPV6_GATEWAY_IP_CMD = "ipv6_gateway_ip"

    IPV6_GATEWAY_IP_STEP_CMD = "ipv6_gateway_ip_step"

    LINK_METRIC_CMD = "link_metric"

    LOOPBACK_IP_ADDR_CMD = "loopback_ip_addr"

    LOOPBACK_IP_ADDR_STEP_CMD = "loopback_ip_addr_step"

    LSA_DISCARD_MODE_CMD = "lsa_discard_mode"

    LSA_REFRESH_TIME_CMD = "lsa_refresh_time"

    LSA_RETRANSMIT_DELAY_CMD = "lsa_retransmit_delay"

    LSA_RETRANSMIT_TIME_CMD = "lsa_retransmit_time"

    MAC_ADDRESS_INIT_CMD = "mac_address_init"

    MAC_ADDRESS_STEP_CMD = "mac_address_step"

    MAX_LS_UPDATES_PER_BURST_CMD = "max_ls_updates_per_burst"

    MAX_LSAS_PER_PKT_CMD = "max_lsas_per_pkt"

    MAX_MTU_CMD = "max_mtu"

    MD5_KEY_CMD = "md5_key"

    MD5_KEY_ID_CMD = "md5_key_id"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CREATE = "create"
    MODE_DELETE = "delete"
    MODE_DISABLE = "disable"
    MODE_ENABLE = "enable"
    MODE_MODIFY = "modify"

    MTU_CMD = "mtu"

    MULTICAST_CAPABILITY_CMD = "multicast_capability"

    NEIGHBOR_DR_ELIGIBILITY_CMD = "neighbor_dr_eligibility"

    NEIGHBOR_INTF_IP_ADDR_CMD = "neighbor_intf_ip_addr"

    NEIGHBOR_INTF_IP_ADDR_STEP_CMD = "neighbor_intf_ip_addr_step"

    NEIGHBOR_ROUTER_ID_CMD = "neighbor_router_id"

    NEIGHBOR_ROUTER_ID_STEP_CMD = "neighbor_router_id_step"

    NETWORK_TYPE_CMD = "network_type"
    # Constant values for NETWORK_TYPE_CMD
    NETWORK_TYPE_BROADCAST = "broadcast"
    NETWORK_TYPE_PTOMP = "ptomp"
    NETWORK_TYPE_PTOP = "ptop"

    NO_WRITE_CMD = "no_write"

    NSSA_CAPABILITY_CMD = "nssa_capability"

    NUMBER_OF_RESTARTS_CMD = "number_of_restarts"

    OOB_RESYNC_BREAKOUT_CMD = "oob_resync_breakout"

    OPAQUE_LSA_FORWARDED_CMD = "opaque_lsa_forwarded"

    OPTION_BITS_CMD = "option_bits"

    OSPFV3_LSA_FLOOD_RATE_CONTROL_CMD = "ospfv3_lsa_flood_rate_control"

    OVERRIDE_EXISTENCE_CHECK_CMD = "override_existence_check"

    OVERRIDE_TRACKING_CMD = "override_tracking"

    PASSWORD_CMD = "password"

    POLL_INTERVAL_CMD = "poll_interval"

    PORT_HANDLE_CMD = "port_handle"

    PROTOCOL_NAME_CMD = "protocol_name"

    RATE_CONTROL_INTERVAL_CMD = "rate_control_interval"

    RESET_CMD = "reset"

    RESTART_DOWN_TIME_CMD = "restart_down_time"

    RESTART_REASON_CMD = "restart_reason"

    RESTART_START_TIME_CMD = "restart_start_time"

    RESTART_UP_TIME_CMD = "restart_up_time"

    RETURN_DETAILED_HANDLES_CMD = "return_detailed_handles"

    ROUTER_ABR_CMD = "router_abr"

    ROUTER_ACTIVE_CMD = "router_active"

    ROUTER_ASBR_CMD = "router_asbr"

    ROUTER_BIT_CMD = "router_bit"

    ROUTER_ID_CMD = "router_id"

    ROUTER_ID_STEP_CMD = "router_id_step"

    ROUTER_INTERFACE_ACTIVE_CMD = "router_interface_active"

    ROUTER_PRIORITY_CMD = "router_priority"

    SESSION_TYPE_CMD = "session_type"
    # Constant values for SESSION_TYPE_CMD
    SESSION_TYPE_OSPFV2 = "ospfv2"
    SESSION_TYPE_OSPFV3 = "ospfv3"

    STRICT_LSA_CHECKING_CMD = "strict_lsa_checking"

    SUPPORT_REASON_SW_RELOAD_OR_UPGRADE_CMD = "support_reason_sw_reload_or_upgrade"

    SUPPORT_REASON_SW_RESTART_CMD = "support_reason_sw_restart"

    SUPPORT_REASON_SWITCH_TO_REDUNDANT_PROCESSOR_CONTROL_CMD = "support_reason_switch_to_redundant_processor_control"

    SUPPORT_REASON_UNKNOWN_CMD = "support_reason_unknown"

    TE_ADMIN_GROUP_CMD = "te_admin_group"

    TE_ENABLE_CMD = "te_enable"

    TE_MAX_BW_CMD = "te_max_bw"

    TE_MAX_RESV_BW_CMD = "te_max_resv_bw"

    TE_METRIC_CMD = "te_metric"

    TE_ROUTER_ID_CMD = "te_router_id"

    TE_UNRESV_BW_PRIORITY0_CMD = "te_unresv_bw_priority0"

    TE_UNRESV_BW_PRIORITY1_CMD = "te_unresv_bw_priority1"

    TE_UNRESV_BW_PRIORITY2_CMD = "te_unresv_bw_priority2"

    TE_UNRESV_BW_PRIORITY3_CMD = "te_unresv_bw_priority3"

    TE_UNRESV_BW_PRIORITY4_CMD = "te_unresv_bw_priority4"

    TE_UNRESV_BW_PRIORITY5_CMD = "te_unresv_bw_priority5"

    TE_UNRESV_BW_PRIORITY6_CMD = "te_unresv_bw_priority6"

    TE_UNRESV_BW_PRIORITY7_CMD = "te_unresv_bw_priority7"

    TRANSMIT_DELAY_CMD = "transmit_delay"

    TYPE_OF_SERVICE_ROUTING_CMD = "type_of_service_routing"

    UNUSED_CMD = "unused"

    V6_CMD = "v6"

    VALIDATE_RECEIVED_MTU_CMD = "validate_received_mtu"

    VCI_CMD = "vci"

    VCI_STEP_CMD = "vci_step"

    VLAN_CMD = "vlan"

    VLAN_CFI_CMD = "vlan_cfi"

    VLAN_ID_CMD = "vlan_id"

    VLAN_ID_MODE_CMD = "vlan_id_mode"
    # Constant values for VLAN_ID_MODE_CMD
    VLAN_ID_MODE_ = ""
    VLAN_ID_MODE_FIXED = "fixed"
    VLAN_ID_MODE_INCREMENT = "increment"

    VLAN_ID_STEP_CMD = "vlan_id_step"

    VLAN_USER_PRIORITY_CMD = "vlan_user_priority"

    VPI_CMD = "vpi"

    VPI_STEP_CMD = "vpi_step"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -area_id
    -area_id_as_number
    -area_id_as_number_step
    -area_id_step
    -area_id_type
    -area_type
    -atm_encapsulation
    -attempt_enabled
    -attempt_interval
    -attempt_rate
    -attempt_scale_mode
    -authentication_mode
    -bfd_registration
    -count
    -dead_interval
    -demand_circuit
    -disable_auto_generate_link_lsa
    -disconnect_enabled
    -disconnect_interval
    -disconnect_rate
    -disconnect_scale_mode
    -do_not_generate_router_lsa
    -enable_dr_bdr
    -enable_fast_hello
    -enable_ignore_db_desc_mtu
    -enable_support_rfc_5838
    -external_attribute
    -external_capabilities
    -flood_lsupdates_per_interval
    -get_next_session_mode
    -grace_period
    -graceful_restart_enable
    -graceful_restart_helper_mode_enable
    -graceful_restart_restarting_mode_enable
    -gre_checksum
    -gre_local_ip
    -gre_remote_ip
    -gre_tunnel
    -handle
    -hello_interval
    -hello_multiplier
    -host_route
    -ignore_db_desc_mtu
    -instance_id
    -instance_id_step
    -int_msg_exchange
    -inter_flood_lsupdate_burst_gap
    -interface_cost
    -interface_handle
    -intf_ip_addr
    -intf_ip_addr_step
    -intf_ipv6_addr
    -intf_ipv6_addr_step
    -intf_ipv6_prefix_length
    -intf_prefix_length
    -ipv6_gateway_ip
    -ipv6_gateway_ip_step
    -link_metric
    -loopback_ip_addr
    -loopback_ip_addr_step
    -lsa_discard_mode
    -lsa_refresh_time
    -lsa_retransmit_delay
    -lsa_retransmit_time
    -mac_address_init
    -mac_address_step
    -max_ls_updates_per_burst
    -max_lsas_per_pkt
    -max_mtu
    -md5_key
    -md5_key_id
    -mode
    -mtu
    -multicast_capability
    -neighbor_dr_eligibility
    -neighbor_intf_ip_addr
    -neighbor_intf_ip_addr_step
    -neighbor_router_id
    -neighbor_router_id_step
    -network_type
    -no_write
    -nssa_capability
    -number_of_restarts
    -oob_resync_breakout
    -opaque_lsa_forwarded
    -option_bits
    -ospfv3_lsa_flood_rate_control
    -override_existence_check
    -override_tracking
    -password
    -poll_interval
    -port_handle
    -protocol_name
    -rate_control_interval
    -reset
    -restart_down_time
    -restart_reason
    -restart_start_time
    -restart_up_time
    -return_detailed_handles
    -router_abr
    -router_active
    -router_asbr
    -router_bit
    -router_id
    -router_id_step
    -router_interface_active
    -router_priority
    -session_type
    -strict_lsa_checking
    -support_reason_sw_reload_or_upgrade
    -support_reason_sw_restart
    -support_reason_switch_to_redundant_processor_control
    -support_reason_unknown
    -te_admin_group
    -te_enable
    -te_max_bw
    -te_max_resv_bw
    -te_metric
    -te_router_id
    -te_unresv_bw_priority0
    -te_unresv_bw_priority1
    -te_unresv_bw_priority2
    -te_unresv_bw_priority3
    -te_unresv_bw_priority4
    -te_unresv_bw_priority5
    -te_unresv_bw_priority6
    -te_unresv_bw_priority7
    -transmit_delay
    -type_of_service_routing
    -unused
    -v6
    -validate_received_mtu
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
If you want to update this file, look in the CSV
"""
