from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfConfigApi import EmulationOspfConfigApi, EmulationOspfConfigConstants

"""
    This is the API class for the command: emulation_ospf_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaEmulationOspfConfigApi(EmulationOspfConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaEmulationOspfConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_config
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfConfigConstants.EMULATION_OSPF_CONFIG_API)
        assert isinstance(api, EmulationOspfConfigApi)
        api.emulation_ospf_config(dummyDict)
    """
    def emulation_ospf_config(self, argdictionary):
        return super(IxiaEmulationOspfConfigApi, self).emulation_ospf_config(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_config_area_id_as_number(self, numeric):
        """
        This is the method the command: emulation_ospf_config option area_id_as_number
        Description:OSPF Area ID for a non-connected interface, displayed in Integer format
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'area_id_type' | value= 'number' |
        Constants Available: AREA_ID_AS_NUMBER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.AREA_ID_AS_NUMBER_CMD : numeric})

    def emulation_ospf_config_area_id_as_number_step(self, numeric):
        """
        This is the method the command: emulation_ospf_config option area_id_as_number_step
        Description:OSPF Area ID step for a non-connected interface, displayed in Integer format
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'area_id_type' | value= 'number' |
        Constants Available: AREA_ID_AS_NUMBER_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.AREA_ID_AS_NUMBER_STEP_CMD : numeric})

    def emulation_ospf_config_area_id_type(self, opt):
        """
        This is the method the command: emulation_ospf_config option area_id_type
        Description:Area ID Type
            Valid options are:
            number

            ip

            area_id_as_number

            area_id_as_ip

            DEFAULT

            ip
        Constants Available: AREA_ID_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.AREA_ID_TYPE_CMD : opt})

    def emulation_ospf_config_atm_encapsulation(self, opt):
        """
        This is the method the command: emulation_ospf_config option atm_encapsulation
        Description:This parameter is not valid on mode modify when IxTclProtocol is used.
            The encapsulation of the ATM protocol interface associated with the
            emulated router.
            DEFAULT
                None
        Constants Available: ATM_ENCAPSULATION_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ATM_ENCAPSULATION_CMD : opt})

    def emulation_ospf_config_attempt_enabled(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option attempt_enabled
        Description:Not defined
            DEFAULT
                None
        Constants Available: ATTEMPT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ATTEMPT_ENABLED_CMD : bool_opt})

    def emulation_ospf_config_attempt_interval(self, numeric):
        """
        This is the method the command: emulation_ospf_config option attempt_interval
        Description:Time interval used to calculate the rate for triggering an action(rate =
            count/interval).
            DEFAULT
                None
        Constants Available: ATTEMPT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ATTEMPT_INTERVAL_CMD : numeric})

    def emulation_ospf_config_attempt_rate(self, range):
        """
        This is the method the command: emulation_ospf_config option attempt_rate
        Description:Number of times an action is triggered per second.
            DEFAULT
                None
        Constants Available: ATTEMPT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ATTEMPT_RATE_CMD : range})

    def emulation_ospf_config_attempt_scale_mode(self, opt):
        """
        This is the method the command: emulation_ospf_config option attempt_scale_mode
        Description:Indicates whether the control is specified per port or per device group.
            This setting is global for all the ospf protocols configured in the
            ixncfg and can be configured just when handle is /globals (when the user
            wants to configure just the global settings)
            Valid options are:
            port

            device_group

            DEFAULT

            port
        Constants Available: ATTEMPT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ATTEMPT_SCALE_MODE_CMD : opt})

    def emulation_ospf_config_bfd_registration(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option bfd_registration
        Description:Enable or disable BFD registration.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            Enable or disable BFD registration.
            DEFAULT

            0
        Constants Available: BFD_REGISTRATION_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.BFD_REGISTRATION_CMD : bool_opt})

    def emulation_ospf_config_disable_auto_generate_link_lsa(self, any):
        """
        This is the method the command: emulation_ospf_config option disable_auto_generate_link_lsa
        Description:Support graceful restart helper mode when restart reason is unknown and
            unplanned.
            DEFAULT
                None
        Constants Available: DISABLE_AUTO_GENERATE_LINK_LSA_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.DISABLE_AUTO_GENERATE_LINK_LSA_CMD : any})

    def emulation_ospf_config_disconnect_enabled(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option disconnect_enabled
        Description:Not defined
            DEFAULT
                None
        Constants Available: DISCONNECT_ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.DISCONNECT_ENABLED_CMD : bool_opt})

    def emulation_ospf_config_disconnect_interval(self, numeric):
        """
        This is the method the command: emulation_ospf_config option disconnect_interval
        Description:Time interval used to calculate the rate for triggering an action(rate =
            count/interval).
            DEFAULT
                None
        Constants Available: DISCONNECT_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.DISCONNECT_INTERVAL_CMD : numeric})

    def emulation_ospf_config_disconnect_rate(self, range):
        """
        This is the method the command: emulation_ospf_config option disconnect_rate
        Description:Number of times an action is triggered per second.
            DEFAULT
                None
        Constants Available: DISCONNECT_RATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.DISCONNECT_RATE_CMD : range})

    def emulation_ospf_config_disconnect_scale_mode(self, opt):
        """
        This is the method the command: emulation_ospf_config option disconnect_scale_mode
        Description:Indicates whether the control is specified per port or per device group.
            This setting is global for all the ospf protocols configured in the
            ixncfg and can be configured just when handle is /globals (when the user
            wants to configure just the global settings)
            Valid options are:
            port

            device_group

            DEFAULT

            port
        Constants Available: DISCONNECT_SCALE_MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.DISCONNECT_SCALE_MODE_CMD : opt})

    def emulation_ospf_config_do_not_generate_router_lsa(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option do_not_generate_router_lsa
        Description:Generate/not generate router lsa
            DEFAULT
                None
        Constants Available: DO_NOT_GENERATE_ROUTER_LSA_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.DO_NOT_GENERATE_ROUTER_LSA_CMD : bool_opt})

    def emulation_ospf_config_enable_dr_bdr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option enable_dr_bdr
        Description:If 1, enables the OSPF Designated Router/Backup Designated Router
            DR/BDR) feature for all router interfaces on this port.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            If 1, enables the OSPF Designated Router/Backup Designated Router
            DR/BDR) feature for all router interfaces on this port.
            DEFAULT

            0
        Constants Available: ENABLE_DR_BDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ENABLE_DR_BDR_CMD : bool_opt})

    def emulation_ospf_config_enable_fast_hello(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option enable_fast_hello
        Description:Enable/disable fast hello
            DEFAULT
                None
        Constants Available: ENABLE_FAST_HELLO_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ENABLE_FAST_HELLO_CMD : bool_opt})

    def emulation_ospf_config_enable_ignore_db_desc_mtu(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option enable_ignore_db_desc_mtu
        Description:Ignore DB-Desc MTU
            DEFAULT

            0
        Constants Available: ENABLE_IGNORE_DB_DESC_MTU_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ENABLE_IGNORE_DB_DESC_MTU_CMD : bool_opt})

    def emulation_ospf_config_external_attribute(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option external_attribute
        Description:Option bit 4
            DEFAULT
                None
        Constants Available: EXTERNAL_ATTRIBUTE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.EXTERNAL_ATTRIBUTE_CMD : bool_opt})

    def emulation_ospf_config_external_capabilities(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option external_capabilities
        Description:Option bit 1
            DEFAULT
                None
        Constants Available: EXTERNAL_CAPABILITIES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.EXTERNAL_CAPABILITIES_CMD : bool_opt})

    def emulation_ospf_config_flood_lsupdates_per_interval(self, numeric):
        """
        This is the method the command: emulation_ospf_config option flood_lsupdates_per_interval
        Description:Flood link state updates per interval.
            DEFAULT
                None
        Constants Available: FLOOD_LSUPDATES_PER_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.FLOOD_LSUPDATES_PER_INTERVAL_CMD : numeric})

    def emulation_ospf_config_hello_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_config option hello_multiplier
        Description:Hello multiplier value
            DEFAULT
                None
        Constants Available: HELLO_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.HELLO_MULTIPLIER_CMD : numeric})

    def emulation_ospf_config_ignore_db_desc_mtu(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option ignore_db_desc_mtu
        Description:This option is only available for OSPFv3 interfaces that are directly
            connected to the DUT. If the parameter ignore_db_desc_mtu is 0 the MTU
            will be verified during the exchange. If the parameter value is 1, the
            Valid options are:
            0

            (default) verify MTU during the exchange.
            1

            ignore MTU size during exchange.
            DEFAULT

            0
        Constants Available: IGNORE_DB_DESC_MTU_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.IGNORE_DB_DESC_MTU_CMD : bool_opt})

    def emulation_ospf_config_inter_flood_lsupdate_burst_gap(self, numeric):
        """
        This is the method the command: emulation_ospf_config option inter_flood_lsupdate_burst_gap
        Description:Inter flood LSUpdate burst gap (ms)
            DEFAULT
                None
        Constants Available: INTER_FLOOD_LSUPDATE_BURST_GAP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INTER_FLOOD_LSUPDATE_BURST_GAP_CMD : numeric})

    def emulation_ospf_config_interface_handle(self, any):
        """
        This is the method the command: emulation_ospf_config option interface_handle
        Description:A handle or list of the handles that are returned from the
            interface_config call. These provide a direct link to an already
            existing interface and supercede the use of the intf_ip_addr
            value.Starting with IxNetwork 5.60 this parameter accepts handles
            returned by emulation_dhcp_group_config procedure in the following
            format: |,-, ... The DHCP ranges are separated from the Interface Index
            identifiers with the (|) character. The Interface Index identifiers are
            separated with comas (,). A range of Interface Index identifiers can be
            defined using the dash (-) character.Ranges along with the Interface
            Index identifiers are grouped together in TCL Lists. The lists can
            contain mixed items, protocol interface handles returned by
            interface_config and handles returned by emulation_dhcp_group_config
            along with the interface index. Example:count 10 (10 OSPF routers). 3
            DHCP range handles returned by ::::emulation_dhcp_group_config. Each
            DHCP range has 20 sessions (interfaces). If we pass -interface_handle in
            the following format: [list $dhcp_r1|1,5 $dhcp_r2|1-3
            $dhcp_r3|1,3,5-9,13] The interfaces will be distributed to the routers
            in the following manner:OSPF Router 1: $dhcp_r1 -> interface 1OSPF
            Router 2: $dhcp_r1 -> interface 5OSPF Router 3: $dhcp_r2 -> interface
            1OSPF Router 4: $dhcp_r2 -> interface 2OSPF Router 5: $dhcp_r2 ->
            interface 3OSPF Router 6: $dhcp_r3 -> interface 1OSPF Router 7: $dhcp_r3
            -> interface 3OSPF Router 8: $dhcp_r3 -> interface 5OSPF Router 9:
            $dhcp_r3 -> interface 6OSPF Router 10: $dhcp_r3 -> interface 7OSPF
            Router 11: $dhcp_r3 -> interface 8OSPF Router 12: $dhcp_r3 -> interface
            9OSPF Router 13 $dhcp_r3 -> interface 13Valid for mode create for
            IxTclNetwork only.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            A handle or list of the handles that are returned from the
            interface_config call. These provide a direct link to an already
            existing interface and supercede the use of the intf_ip_addr value.
            Starting with IxNetwork 5.60 this parameter accepts handles returned by
            emulation_dhcp_group_config procedure and pppox_config procedure in the
            following format: |,-, ... The DHCP ranges are separated from the
            Interface Index identifiers with the (|) character. The Interface Index
            identifiers are separated with comas (,). A range of Interface Index
            identifiers can be defined using the dash (-) character. Ranges along
            with the Interface Index identifiers are grouped together in TCL Lists.
            The lists can contain mixed items, protocol interface handles returned
            by interface_config and handles returned by emulation_dhcp_group_config
            along with the interface index. Example: count 10 (10 OSPF routers). 3
            DHCP range handles returned by ::ixia::emulation_dhcp_group_config. Each
            DHCP range has 20 sessions (interfaces). If we pass 'interface_handle in
            the following format: [list $dhcp_r1|1,5 $dhcp_r2|1-3
            $dhcp_r3|1,3,5-9,13] The interfaces will be distributed to the routers
            in the following manner: OSPF Router 1: $dhcp_r1 -> interface 1 OSPF
            Router 2: $dhcp_r1 -> interface 5 OSPF Router 3: $dhcp_r2 -> interface 1
            OSPF Router 4: $dhcp_r2 -> interface 2 OSPF Router 5: $dhcp_r2 ->
            interface 3 OSPF Router 6: $dhcp_r3 -> interface 1 OSPF Router 7:
            $dhcp_r3 -> interface 3 OSPF Router 8: $dhcp_r3 -> interface 5 OSPF
            Router 9: $dhcp_r3 -> interface 6 OSPF Router 10: $dhcp_r3 -> interface
            7 OSPF Router 11: $dhcp_r3 -> interface 8 OSPF Router 12: $dhcp_r3 ->
            interface 9 OSPF Router 13 $dhcp_r3 -> interface 13 Valid for mode
            create for IxTclNetwork only.
            DEFAULT
                None
        Constants Available: INTERFACE_HANDLE_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INTERFACE_HANDLE_CMD : any})

    def emulation_ospf_config_intf_ipv6_addr(self, ipv6):
        """
        This is the method the command: emulation_ospf_config option intf_ipv6_addr
        Description:IPv6 addresses of the layer
            DEFAULT
                None
        Constants Available: INTF_IPV6_ADDR_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INTF_IPV6_ADDR_CMD : ipv6})

    def emulation_ospf_config_intf_ipv6_addr_step(self, ipv6):
        """
        This is the method the command: emulation_ospf_config option intf_ipv6_addr_step
        Description:Not defined
            DEFAULT
                None
        Constants Available: INTF_IPV6_ADDR_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INTF_IPV6_ADDR_STEP_CMD : ipv6})

    def emulation_ospf_config_intf_prefix_length(self, range):
        """
        This is the method the command: emulation_ospf_config option intf_prefix_length
        Description:Defines the mask of the IP address used for the Ixia (-intf_ip_addr) and
            the DUT interface. This parameter is not valid on mode modify when
            IxTclProtocol is used. RANGE 1-128(DEFAULT = 24 | 64)
            DEFAULT

            24 | 64
            IxNetwork-NGPF

            DESCRIPTION

            Defines the mask of the IP address used for the Ixia (-intf_ip_addr) and
            the DUT interface. This parameter is not valid on mode modify when
            IxTclProtocol is used. RANGE 1-128
            DEFAULT

            24
        Constants Available: INTF_PREFIX_LENGTH_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.INTF_PREFIX_LENGTH_CMD : range})

    def emulation_ospf_config_ipv6_gateway_ip(self, ipv6):
        """
        This is the method the command: emulation_ospf_config option ipv6_gateway_ip
        Description:gateways of the layer
            DEFAULT
                None
        Constants Available: IPV6_GATEWAY_IP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.IPV6_GATEWAY_IP_CMD : ipv6})

    def emulation_ospf_config_ipv6_gateway_ip_step(self, ipv6):
        """
        This is the method the command: emulation_ospf_config option ipv6_gateway_ip_step
        Description:Not defined
            DEFAULT
                None
        Constants Available: IPV6_GATEWAY_IP_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.IPV6_GATEWAY_IP_STEP_CMD : ipv6})

    def emulation_ospf_config_link_metric(self, range):
        """
        This is the method the command: emulation_ospf_config option link_metric
        Description:Link Metric
            DEFAULT

            0
        Constants Available: LINK_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.LINK_METRIC_CMD : range})

    def emulation_ospf_config_lsa_refresh_time(self, numeric):
        """
        This is the method the command: emulation_ospf_config option lsa_refresh_time
        Description:LSA refresh time (s)
            DEFAULT
                None
        Constants Available: LSA_REFRESH_TIME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.LSA_REFRESH_TIME_CMD : numeric})

    def emulation_ospf_config_lsa_retransmit_time(self, numeric):
        """
        This is the method the command: emulation_ospf_config option lsa_retransmit_time
        Description:LSA retransmit time (s)
            DEFAULT
                None
        Constants Available: LSA_RETRANSMIT_TIME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.LSA_RETRANSMIT_TIME_CMD : numeric})

    def emulation_ospf_config_mac_address_init(self, mac):
        """
        This is the method the command: emulation_ospf_config option mac_address_init
        Description:This option defines the MAC address that will be configured on the Ixia
            interface. This parameter is not valid on mode modify when IxTclProtocol
            is used.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This option defines the MAC address that will be configured on the Ixia
            interface. This parameter is not valid on mode modify when IxTclProtocol
            is used.
            DEFAULT
                None
        Constants Available: MAC_ADDRESS_INIT_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MAC_ADDRESS_INIT_CMD : mac})

    def emulation_ospf_config_mac_address_step(self, mac):
        """
        This is the method the command: emulation_ospf_config option mac_address_step
        Description:This option defines the incrementing step for the MAC address that will
            be configured on the Ixia interface. This option is valid only when
            IxTclNetwork API is used.
            DEFAULT

            0000.0000.0001
            IxNetwork-NGPF

            DESCRIPTION

            This option defines the incrementing step for the MAC address that will
            be configured on the Ixia interface. This option is valid only when
            IxTclNetwork API is used.
            DEFAULT

            0000.0000.0001
        Constants Available: MAC_ADDRESS_STEP_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MAC_ADDRESS_STEP_CMD : mac})

    def emulation_ospf_config_max_ls_updates_per_burst(self, numeric):
        """
        This is the method the command: emulation_ospf_config option max_ls_updates_per_burst
        Description:Max flood LSUpdates per burst
            DEFAULT
                None
        Constants Available: MAX_LS_UPDATES_PER_BURST_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MAX_LS_UPDATES_PER_BURST_CMD : numeric})

    def emulation_ospf_config_max_mtu(self, numeric):
        """
        This is the method the command: emulation_ospf_config option max_mtu
        Description:Max mtu value
            DEFAULT
                None
        Constants Available: MAX_MTU_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MAX_MTU_CMD : numeric})

    def emulation_ospf_config_multicast_capability(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option multicast_capability
        Description:Option bit 2
            DEFAULT
                None
        Constants Available: MULTICAST_CAPABILITY_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.MULTICAST_CAPABILITY_CMD : bool_opt})

    def emulation_ospf_config_no_write(self, flag):
        """
        This is the method the command: emulation_ospf_config option no_write
        Description:If this option is present, the protocol configuration will not be
            written to the server.
            DEFAULT
                None
        Constants Available: NO_WRITE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        flag --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.NO_WRITE_CMD : flag})

    def emulation_ospf_config_nssa_capability(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option nssa_capability
        Description:Option bit 3
            DEFAULT
                None
        Constants Available: NSSA_CAPABILITY_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.NSSA_CAPABILITY_CMD : bool_opt})

    def emulation_ospf_config_oob_resync_breakout(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option oob_resync_breakout
        Description:Enable out-of-band resynchronization breakout
            DEFAULT
                None
        Constants Available: OOB_RESYNC_BREAKOUT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.OOB_RESYNC_BREAKOUT_CMD : bool_opt})

    def emulation_ospf_config_opaque_lsa_forwarded(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option opaque_lsa_forwarded
        Description:Option bit 6
            DEFAULT
                None
        Constants Available: OPAQUE_LSA_FORWARDED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.OPAQUE_LSA_FORWARDED_CMD : bool_opt})

    def emulation_ospf_config_ospfv3_lsa_flood_rate_control(self, any):
        """
        This is the method the command: emulation_ospf_config option ospfv3_lsa_flood_rate_control
        Description:Inter Flood LSUpdate burst gap (ms)
            DEFAULT

            1
        Constants Available: OSPFV3_LSA_FLOOD_RATE_CONTROL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.OSPFV3_LSA_FLOOD_RATE_CONTROL_CMD : any})

    def emulation_ospf_config_override_existence_check(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option override_existence_check
        Description:If this option is enabled, the interface existence check is skipped but
            the list of interfaces is still created and maintained in order to keep
            track of existing interfaces if required. Using this option will speed
            up the interfaces' creation.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            If this option is enabled, the interface existence check is skipped but
            the list of interfaces is still created and maintained in order to keep
            track of existing interfaces if required. Using this option will speed
            up the interfaces' creation.
            DEFAULT

            0
        Constants Available: OVERRIDE_EXISTENCE_CHECK_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.OVERRIDE_EXISTENCE_CHECK_CMD : bool_opt})

    def emulation_ospf_config_override_tracking(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option override_tracking
        Description:If this option is enabled, the list of interfaces won't be created and
            maintained anymore, thus, speeding up the interfaces' creation even
            more. Also, it will enable -override_existence_check in case it wasn't
            already enabled because checking for interface existence becomes
            impossible if the the list of interfaces doesn't exist anymore.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            If this option is enabled, the list of interfaces won't be created and
            maintained anymore, thus, speeding up the interfaces' creation even
            more. Also, it will enable -override_existence_check in case it wasn't
            already enabled because checking for interface existence becomes
            impossible if the the list of interfaces doesn't exist anymore.
            DEFAULT

            0
        Constants Available: OVERRIDE_TRACKING_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.OVERRIDE_TRACKING_CMD : bool_opt})

    def emulation_ospf_config_port_handle(self, any):
        """
        This is the method the command: emulation_ospf_config option port_handle
        Description:Ixia interface upon which to act.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Ixia interface upon which to act.
            DEFAULT
                None
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork[M] , IxOS/IxNetwork-FT[M]
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.PORT_HANDLE_CMD : any})

    def emulation_ospf_config_protocol_name(self, alpha):
        """
        This is the method the command: emulation_ospf_config option protocol_name
        Description:Name of the ospf protocol as it should appear in the IxNetwork GUI
            DEFAULT
                None
        Constants Available: PROTOCOL_NAME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        alpha --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.PROTOCOL_NAME_CMD : alpha})

    def emulation_ospf_config_rate_control_interval(self, numeric):
        """
        This is the method the command: emulation_ospf_config option rate_control_interval
        Description:Flood link state updates per interval.
            DEFAULT
                None
        Constants Available: RATE_CONTROL_INTERVAL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.RATE_CONTROL_INTERVAL_CMD : numeric})

    def emulation_ospf_config_reset(self, any):
        """
        This is the method the command: emulation_ospf_config option reset
        Description:If this option is selected, this will clear any OSPF router on the
            targeted interface.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If this option is selected, this will clear any OSPF router on the
            targeted interface.
            DEFAULT
                None
        Constants Available: RESET_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.RESET_CMD : any})

    def emulation_ospf_config_return_detailed_handles(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option return_detailed_handles
        Description:This argument determines if individual interface, session or router
            handles are returned by the current command. This applies only to the
            command on which it is specified. Setting this to 0 means that only
            NGPF-specific protocol stack handles will be returned. This will
            significantly decrease the size of command results and speed up script
            execution. The default is 0, meaning only protocol stack handles will be
            returned.
            DEFAULT

            0
        Constants Available: RETURN_DETAILED_HANDLES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.RETURN_DETAILED_HANDLES_CMD : bool_opt})

    def emulation_ospf_config_router_abr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option router_abr
        Description:If true (1), set router to be an area boundary router (ABR). Correspond
            to E (external) bit in router LSA. This option is valid only when -type
            is router or grid, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0
        Constants Available: ROUTER_ABR_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ROUTER_ABR_CMD : bool_opt})

    def emulation_ospf_config_router_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option router_active
        Description:Enable/disable the ospf router
            DEFAULT
                None
        Constants Available: ROUTER_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ROUTER_ACTIVE_CMD : bool_opt})

    def emulation_ospf_config_router_asbr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option router_asbr
        Description:If true (1), set router to be an AS boundary router (ASBR). Correspond
            to B (Border) bit in router LSA. This option is valid only when -type is
            router or grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0
        Constants Available: ROUTER_ASBR_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ROUTER_ASBR_CMD : bool_opt})

    def emulation_ospf_config_router_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option router_bit
        Description:Option bit 4
            DEFAULT

            0
        Constants Available: ROUTER_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ROUTER_BIT_CMD : bool_opt})

    def emulation_ospf_config_router_interface_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option router_interface_active
        Description:Enable/disable router interface
            DEFAULT
                None
        Constants Available: ROUTER_INTERFACE_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.ROUTER_INTERFACE_ACTIVE_CMD : bool_opt})

    def emulation_ospf_config_type_of_service_routing(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option type_of_service_routing
        Description:Option bit 0
            DEFAULT
                None
        Constants Available: TYPE_OF_SERVICE_ROUTING_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.TYPE_OF_SERVICE_ROUTING_CMD : bool_opt})

    def emulation_ospf_config_unused(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option unused
        Description:Option bit 7
            DEFAULT
                None
        Constants Available: UNUSED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.UNUSED_CMD : bool_opt})

    def emulation_ospf_config_v6(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option v6
        Description:Option bit 0
            DEFAULT

            0
        Constants Available: V6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.V6_CMD : bool_opt})

    def emulation_ospf_config_validate_received_mtu(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option validate_received_mtu
        Description:Enabling this option means that the MTU will be verified during the DB
            exchange. This is only available for OSPFv2 interfaces that are directly
            connected to the DUT.
            DEFAULT

            1
            IxNetwork-NGPF

            DESCRIPTION

            Enabling this option means that the MTU will be verified during the DB
            exchange. This is only available for OSPFv2 interfaces that are directly
            connected to the DUT.
            DEFAULT

            1
        Constants Available: VALIDATE_RECEIVED_MTU_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VALIDATE_RECEIVED_MTU_CMD : bool_opt})

    def emulation_ospf_config_vlan(self, bool_opt):
        """
        This is the method the command: emulation_ospf_config option vlan
        Description:Enables vlan on the directly connected OSPF router interface. Valid
            options are: 0 - disable, 1 - enable.This option is valid only when
            -mode is create or -mode is modify and -handle is a OSPF router
            handle.This option is available only when IxNetwork tcl API is used.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Enables vlan on the directly connected OSPF router interface. Valid
            options are: 0 - disable, 1 - enable. This option is valid only when
            -mode is create or -mode is modify and -handle is a OSPF router handle.
            This option is available only when IxNetwork tcl API is used.
            DEFAULT
                None
        Constants Available: VLAN_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VLAN_CMD : bool_opt})

    def emulation_ospf_config_vlan_id_step(self, range):
        """
        This is the method the command: emulation_ospf_config option vlan_id_step
        Description:This parameter is not valid on mode modify when IxTclProtocol is used.
            If the -vlan_id_mode is increment, this will be the step value by which
            the VLAN tags are incremented. RANGE 0-4095When vlan_id_step causes the
            vlan_id value to exceed it's maximum value the increment will be done
            modulo .Examples: vlan_id = 4094; vlan_id_step = 2 -> new vlan_id value
            = 0vlan_id = 4095; vlan_id_step = 11 -> new vlan_id value = 10
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is not valid on mode modify when IxTclProtocol is used.
            If the -vlan_id_mode is increment, this will be the step value by which
            the VLAN tags are incremented. RANGE 0-4095 When vlan_id_step causes the
            vlan_id value to exceed it's maximum value the increment will be done
            modulo . Examples: vlan_id = 4094; vlan_id_step = 2 -> new vlan_id value
            = 0 vlan_id = 4095; vlan_id_step = 11 -> new vlan_id value = 10
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'vlan_id_mode' | value= 'increment' |
        Constants Available: VLAN_ID_STEP_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_config({EmulationOspfConfigConstants.VLAN_ID_STEP_CMD : range})


    supportedIxiaHltapiCommands = {EmulationOspfConfigConstants.AREA_ID_CMD, EmulationOspfConfigConstants.AREA_ID_AS_NUMBER_CMD, EmulationOspfConfigConstants.AREA_ID_AS_NUMBER_STEP_CMD, EmulationOspfConfigConstants.AREA_ID_STEP_CMD, EmulationOspfConfigConstants.AREA_ID_TYPE_CMD, EmulationOspfConfigConstants.AREA_TYPE_CMD, EmulationOspfConfigConstants.ATM_ENCAPSULATION_CMD, EmulationOspfConfigConstants.ATTEMPT_ENABLED_CMD, EmulationOspfConfigConstants.ATTEMPT_INTERVAL_CMD, EmulationOspfConfigConstants.ATTEMPT_RATE_CMD, EmulationOspfConfigConstants.ATTEMPT_SCALE_MODE_CMD, EmulationOspfConfigConstants.AUTHENTICATION_MODE_CMD, EmulationOspfConfigConstants.BFD_REGISTRATION_CMD, EmulationOspfConfigConstants.COUNT_CMD, EmulationOspfConfigConstants.DEAD_INTERVAL_CMD, EmulationOspfConfigConstants.DEMAND_CIRCUIT_CMD, EmulationOspfConfigConstants.DISABLE_AUTO_GENERATE_LINK_LSA_CMD, EmulationOspfConfigConstants.DISCONNECT_ENABLED_CMD, EmulationOspfConfigConstants.DISCONNECT_INTERVAL_CMD, EmulationOspfConfigConstants.DISCONNECT_RATE_CMD, EmulationOspfConfigConstants.DISCONNECT_SCALE_MODE_CMD, EmulationOspfConfigConstants.DO_NOT_GENERATE_ROUTER_LSA_CMD, EmulationOspfConfigConstants.ENABLE_DR_BDR_CMD, EmulationOspfConfigConstants.ENABLE_FAST_HELLO_CMD, EmulationOspfConfigConstants.ENABLE_IGNORE_DB_DESC_MTU_CMD, EmulationOspfConfigConstants.ENABLE_SUPPORT_RFC_5838_CMD, EmulationOspfConfigConstants.EXTERNAL_ATTRIBUTE_CMD, EmulationOspfConfigConstants.EXTERNAL_CAPABILITIES_CMD, EmulationOspfConfigConstants.FLOOD_LSUPDATES_PER_INTERVAL_CMD, EmulationOspfConfigConstants.GET_NEXT_SESSION_MODE_CMD, EmulationOspfConfigConstants.GRACE_PERIOD_CMD, EmulationOspfConfigConstants.GRACEFUL_RESTART_ENABLE_CMD, EmulationOspfConfigConstants.GRACEFUL_RESTART_HELPER_MODE_ENABLE_CMD, EmulationOspfConfigConstants.GRACEFUL_RESTART_RESTARTING_MODE_ENABLE_CMD, EmulationOspfConfigConstants.GRE_CHECKSUM_CMD, EmulationOspfConfigConstants.GRE_LOCAL_IP_CMD, EmulationOspfConfigConstants.GRE_REMOTE_IP_CMD, EmulationOspfConfigConstants.GRE_TUNNEL_CMD, EmulationOspfConfigConstants.HANDLE_CMD, EmulationOspfConfigConstants.HELLO_INTERVAL_CMD, EmulationOspfConfigConstants.HELLO_MULTIPLIER_CMD, EmulationOspfConfigConstants.HOST_ROUTE_CMD, EmulationOspfConfigConstants.IGNORE_DB_DESC_MTU_CMD, EmulationOspfConfigConstants.INSTANCE_ID_CMD, EmulationOspfConfigConstants.INSTANCE_ID_STEP_CMD, EmulationOspfConfigConstants.INT_MSG_EXCHANGE_CMD, EmulationOspfConfigConstants.INTER_FLOOD_LSUPDATE_BURST_GAP_CMD, EmulationOspfConfigConstants.INTERFACE_COST_CMD, EmulationOspfConfigConstants.INTERFACE_HANDLE_CMD, EmulationOspfConfigConstants.INTF_IP_ADDR_CMD, EmulationOspfConfigConstants.INTF_IP_ADDR_STEP_CMD, EmulationOspfConfigConstants.INTF_IPV6_ADDR_CMD, EmulationOspfConfigConstants.INTF_IPV6_ADDR_STEP_CMD, EmulationOspfConfigConstants.INTF_IPV6_PREFIX_LENGTH_CMD, EmulationOspfConfigConstants.INTF_PREFIX_LENGTH_CMD, EmulationOspfConfigConstants.IPV6_GATEWAY_IP_CMD, EmulationOspfConfigConstants.IPV6_GATEWAY_IP_STEP_CMD, EmulationOspfConfigConstants.LINK_METRIC_CMD, EmulationOspfConfigConstants.LOOPBACK_IP_ADDR_CMD, EmulationOspfConfigConstants.LOOPBACK_IP_ADDR_STEP_CMD, EmulationOspfConfigConstants.LSA_DISCARD_MODE_CMD, EmulationOspfConfigConstants.LSA_REFRESH_TIME_CMD, EmulationOspfConfigConstants.LSA_RETRANSMIT_DELAY_CMD, EmulationOspfConfigConstants.LSA_RETRANSMIT_TIME_CMD, EmulationOspfConfigConstants.MAC_ADDRESS_INIT_CMD, EmulationOspfConfigConstants.MAC_ADDRESS_STEP_CMD, EmulationOspfConfigConstants.MAX_LS_UPDATES_PER_BURST_CMD, EmulationOspfConfigConstants.MAX_LSAS_PER_PKT_CMD, EmulationOspfConfigConstants.MAX_MTU_CMD, EmulationOspfConfigConstants.MD5_KEY_CMD, EmulationOspfConfigConstants.MD5_KEY_ID_CMD, EmulationOspfConfigConstants.MODE_CMD, EmulationOspfConfigConstants.MTU_CMD, EmulationOspfConfigConstants.MULTICAST_CAPABILITY_CMD, EmulationOspfConfigConstants.NEIGHBOR_DR_ELIGIBILITY_CMD, EmulationOspfConfigConstants.NEIGHBOR_INTF_IP_ADDR_CMD, EmulationOspfConfigConstants.NEIGHBOR_INTF_IP_ADDR_STEP_CMD, EmulationOspfConfigConstants.NEIGHBOR_ROUTER_ID_CMD, EmulationOspfConfigConstants.NEIGHBOR_ROUTER_ID_STEP_CMD, EmulationOspfConfigConstants.NETWORK_TYPE_CMD, EmulationOspfConfigConstants.NO_WRITE_CMD, EmulationOspfConfigConstants.NSSA_CAPABILITY_CMD, EmulationOspfConfigConstants.NUMBER_OF_RESTARTS_CMD, EmulationOspfConfigConstants.OOB_RESYNC_BREAKOUT_CMD, EmulationOspfConfigConstants.OPAQUE_LSA_FORWARDED_CMD, EmulationOspfConfigConstants.OPTION_BITS_CMD, EmulationOspfConfigConstants.OSPFV3_LSA_FLOOD_RATE_CONTROL_CMD, EmulationOspfConfigConstants.OVERRIDE_EXISTENCE_CHECK_CMD, EmulationOspfConfigConstants.OVERRIDE_TRACKING_CMD, EmulationOspfConfigConstants.PASSWORD_CMD, EmulationOspfConfigConstants.POLL_INTERVAL_CMD, EmulationOspfConfigConstants.PORT_HANDLE_CMD, EmulationOspfConfigConstants.PROTOCOL_NAME_CMD, EmulationOspfConfigConstants.RATE_CONTROL_INTERVAL_CMD, EmulationOspfConfigConstants.RESET_CMD, EmulationOspfConfigConstants.RESTART_DOWN_TIME_CMD, EmulationOspfConfigConstants.RESTART_REASON_CMD, EmulationOspfConfigConstants.RESTART_START_TIME_CMD, EmulationOspfConfigConstants.RESTART_UP_TIME_CMD, EmulationOspfConfigConstants.RETURN_DETAILED_HANDLES_CMD, EmulationOspfConfigConstants.ROUTER_ABR_CMD, EmulationOspfConfigConstants.ROUTER_ACTIVE_CMD, EmulationOspfConfigConstants.ROUTER_ASBR_CMD, EmulationOspfConfigConstants.ROUTER_BIT_CMD, EmulationOspfConfigConstants.ROUTER_ID_CMD, EmulationOspfConfigConstants.ROUTER_ID_STEP_CMD, EmulationOspfConfigConstants.ROUTER_INTERFACE_ACTIVE_CMD, EmulationOspfConfigConstants.ROUTER_PRIORITY_CMD, EmulationOspfConfigConstants.SESSION_TYPE_CMD, EmulationOspfConfigConstants.STRICT_LSA_CHECKING_CMD, EmulationOspfConfigConstants.SUPPORT_REASON_SW_RELOAD_OR_UPGRADE_CMD, EmulationOspfConfigConstants.SUPPORT_REASON_SW_RESTART_CMD, EmulationOspfConfigConstants.SUPPORT_REASON_SWITCH_TO_REDUNDANT_PROCESSOR_CONTROL_CMD, EmulationOspfConfigConstants.SUPPORT_REASON_UNKNOWN_CMD, EmulationOspfConfigConstants.TE_ADMIN_GROUP_CMD, EmulationOspfConfigConstants.TE_ENABLE_CMD, EmulationOspfConfigConstants.TE_MAX_BW_CMD, EmulationOspfConfigConstants.TE_MAX_RESV_BW_CMD, EmulationOspfConfigConstants.TE_METRIC_CMD, EmulationOspfConfigConstants.TE_ROUTER_ID_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY0_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY1_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY2_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY3_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY4_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY5_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY6_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY7_CMD, EmulationOspfConfigConstants.TRANSMIT_DELAY_CMD, EmulationOspfConfigConstants.TYPE_OF_SERVICE_ROUTING_CMD, EmulationOspfConfigConstants.UNUSED_CMD, EmulationOspfConfigConstants.V6_CMD, EmulationOspfConfigConstants.VALIDATE_RECEIVED_MTU_CMD, EmulationOspfConfigConstants.VCI_CMD, EmulationOspfConfigConstants.VCI_STEP_CMD, EmulationOspfConfigConstants.VLAN_CMD, EmulationOspfConfigConstants.VLAN_CFI_CMD, EmulationOspfConfigConstants.VLAN_ID_CMD, EmulationOspfConfigConstants.VLAN_ID_MODE_CMD, EmulationOspfConfigConstants.VLAN_ID_STEP_CMD, EmulationOspfConfigConstants.VLAN_USER_PRIORITY_CMD, EmulationOspfConfigConstants.VPI_CMD, EmulationOspfConfigConstants.VPI_STEP_CMD}
