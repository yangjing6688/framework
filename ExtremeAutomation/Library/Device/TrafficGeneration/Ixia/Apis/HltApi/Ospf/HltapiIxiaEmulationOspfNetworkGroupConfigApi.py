from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfNetworkGroupConfigApi import EmulationOspfNetworkGroupConfigApi, EmulationOspfNetworkGroupConfigConstants

"""
    This is the API class for the command: emulation_ospf_network_group_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaEmulationOspfNetworkGroupConfigApi(EmulationOspfNetworkGroupConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaEmulationOspfNetworkGroupConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_network_group_config
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfNetworkGroupConfigConstants.EMULATION_OSPF_NETWORK_GROUP_CONFIG_API)
        assert isinstance(api, EmulationOspfNetworkGroupConfigApi)
        api.emulation_ospf_network_group_config(dummyDict)
    """
    def emulation_ospf_network_group_config(self, argdictionary):
        return super(IxiaEmulationOspfNetworkGroupConfigApi, self).emulation_ospf_network_group_config(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_network_group_config_active_router_id(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option active_router_id
        Description:Not defined
            DEFAULT
                None
        Constants Available: ACTIVE_ROUTER_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ACTIVE_ROUTER_ID_CMD : bool_opt})

    def emulation_ospf_network_group_config_allow_propagate(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option allow_propagate
        Description:Allow Propagate
            DEFAULT
                None
        Constants Available: ALLOW_PROPAGATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ALLOW_PROPAGATE_CMD : bool_opt})

    def emulation_ospf_network_group_config_auto_select_forwarding_address(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option auto_select_forwarding_address
        Description:Auto Select Forwarding Address
            DEFAULT
                None
        Constants Available: AUTO_SELECT_FORWARDING_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.AUTO_SELECT_FORWARDING_ADDRESS_CMD : bool_opt})

    def emulation_ospf_network_group_config_connected_to_handle(self, any):
        """
        This is the method the command: emulation_ospf_network_group_config option connected_to_handle
        Description:Scenario element this connector is connecting to
            DEFAULT
                None
        Constants Available: CONNECTED_TO_HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.CONNECTED_TO_HANDLE_CMD : any})

    def emulation_ospf_network_group_config_custom_from_node_index(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option custom_from_node_index
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'custom' |
        Constants Available: CUSTOM_FROM_NODE_INDEX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.CUSTOM_FROM_NODE_INDEX_CMD : numeric})

    def emulation_ospf_network_group_config_custom_link_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option custom_link_multiplier
        Description:number of links between two nodes
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'custom' |
        Constants Available: CUSTOM_LINK_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.CUSTOM_LINK_MULTIPLIER_CMD : numeric})

    def emulation_ospf_network_group_config_custom_to_node_index(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option custom_to_node_index
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'custom' |
        Constants Available: CUSTOM_TO_NODE_INDEX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.CUSTOM_TO_NODE_INDEX_CMD : numeric})

    def emulation_ospf_network_group_config_enable_advertise_as_stub_network(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option enable_advertise_as_stub_network
        Description:Not defined
            DEFAULT
                None
        Constants Available: ENABLE_ADVERTISE_AS_STUB_NETWORK_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ENABLE_ADVERTISE_AS_STUB_NETWORK_CMD : bool_opt})

    def emulation_ospf_network_group_config_enable_device(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option enable_device
        Description:enables/disables device.
            DEFAULT
                None
        Constants Available: ENABLE_DEVICE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ENABLE_DEVICE_CMD : bool_opt})

    def emulation_ospf_network_group_config_enable_ip(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option enable_ip
        Description:Enable Simulated Interface IP
            DEFAULT
                None
        Constants Available: ENABLE_IP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ENABLE_IP_CMD : bool_opt})

    def emulation_ospf_network_group_config_external1_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external1_active
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL1_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_external1_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external1_metric
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL1_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_external1_network_address(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option external1_network_address
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL1_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_NETWORK_ADDRESS_CMD : ipv4})

    def emulation_ospf_network_group_config_external1_network_address_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option external1_network_address_step
        Description:Not defined
            DEFAULT

            0.0.0.1
        Constants Available: EXTERNAL1_NETWORK_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_NETWORK_ADDRESS_STEP_CMD : ipv4})

    def emulation_ospf_network_group_config_external1_number_of_routes(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external1_number_of_routes
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL1_NUMBER_OF_ROUTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_NUMBER_OF_ROUTES_CMD : numeric})

    def emulation_ospf_network_group_config_external1_prefix(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external1_prefix
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL1_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_PREFIX_CMD : numeric})

    def emulation_ospf_network_group_config_external2_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external2_active
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL2_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_external2_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external2_metric
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL2_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_external2_network_address(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option external2_network_address
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL2_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_NETWORK_ADDRESS_CMD : ipv4})

    def emulation_ospf_network_group_config_external2_network_address_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option external2_network_address_step
        Description:Not defined
            DEFAULT

            0.0.0.1
        Constants Available: EXTERNAL2_NETWORK_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_NETWORK_ADDRESS_STEP_CMD : ipv4})

    def emulation_ospf_network_group_config_external2_number_of_routes(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external2_number_of_routes
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL2_NUMBER_OF_ROUTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_NUMBER_OF_ROUTES_CMD : numeric})

    def emulation_ospf_network_group_config_external2_prefix(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external2_prefix
        Description:Not defined
            DEFAULT
                None
        Constants Available: EXTERNAL2_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_PREFIX_CMD : numeric})

    def emulation_ospf_network_group_config_external_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_active
        Description:Whether this is to be advertised or not
            DEFAULT
                None
        Constants Available: EXTERNAL_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_e_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_e_bit
        Description:External Metric Bit
            DEFAULT
                None
        Constants Available: EXTERNAL_E_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_E_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_external_route_tag(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option external_external_route_tag
        Description:External Route Tag
            DEFAULT
                None
        Constants Available: EXTERNAL_EXTERNAL_ROUTE_TAG_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_EXTERNAL_ROUTE_TAG_CMD : ipv4})

    def emulation_ospf_network_group_config_external_f_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_f_bit
        Description:Forwarding Address Bit
            DEFAULT
                None
        Constants Available: EXTERNAL_F_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_F_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_forwarding_address(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option external_forwarding_address
        Description:128 Bits IPv6 address.
            DEFAULT
                None
        Constants Available: EXTERNAL_FORWARDING_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_FORWARDING_ADDRESS_CMD : ipv6})

    def emulation_ospf_network_group_config_external_ipv6_network_address(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option external_ipv6_network_address
        Description:Network addresses of the simulated IPv6 network
            DEFAULT
                None
        Constants Available: EXTERNAL_IPV6_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_IPV6_NETWORK_ADDRESS_CMD : ipv6})

    def emulation_ospf_network_group_config_external_ipv6_network_address_step(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option external_ipv6_network_address_step
        Description:Not defined
            DEFAULT

            0:0:0:1:0:0:0:0
        Constants Available: EXTERNAL_IPV6_NETWORK_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_IPV6_NETWORK_ADDRESS_STEP_CMD : ipv6})

    def emulation_ospf_network_group_config_external_l_a_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_l_a_bit
        Description:Options-LA Bit(Local Address)
            DEFAULT
                None
        Constants Available: EXTERNAL_L_A_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_L_A_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_link_network_group_handle(self, any):
        """
        This is the method the command: emulation_ospf_network_group_config option external_link_network_group_handle
        Description:Network Topology this link is pointing to
            DEFAULT
                None
        Constants Available: EXTERNAL_LINK_NETWORK_GROUP_HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_NETWORK_GROUP_HANDLE_CMD : any})

    def emulation_ospf_network_group_config_external_link_router_destination(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external_link_router_destination
        Description:Index of the target node as defined in toNetworkTopology
            DEFAULT
                None
        Constants Available: EXTERNAL_LINK_ROUTER_DESTINATION_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_ROUTER_DESTINATION_CMD : numeric})

    def emulation_ospf_network_group_config_external_link_router_source(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external_link_router_source
        Description:Index of the originating node as defined in fromNetworkTopology
            DEFAULT
                None
        Constants Available: EXTERNAL_LINK_ROUTER_SOURCE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_ROUTER_SOURCE_CMD : numeric})

    def emulation_ospf_network_group_config_external_link_state_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option external_link_state_id
        Description:Link State Id of the simulated IPv6 network
            DEFAULT
                None
        Constants Available: EXTERNAL_LINK_STATE_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_STATE_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_external_link_state_id_prefix(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option external_link_state_id_prefix
        Description:Link State Id Prefix
            DEFAULT
                None
        Constants Available: EXTERNAL_LINK_STATE_ID_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_STATE_ID_PREFIX_CMD : ipv4})

    def emulation_ospf_network_group_config_external_m_c_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_m_c_bit
        Description:Options-MC Bit(Multicast)
            DEFAULT
                None
        Constants Available: EXTERNAL_M_C_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_M_C_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external_metric
        Description:Metric
            DEFAULT
                None
        Constants Available: EXTERNAL_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_external_n_u_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_n_u_bit
        Description:Options-NU Bit(No Unicast)
            DEFAULT
                None
        Constants Available: EXTERNAL_N_U_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_N_U_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_p_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_p_bit
        Description:Options-P Bit(Propagate)
            DEFAULT
                None
        Constants Available: EXTERNAL_P_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_P_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_prefix(self, any):
        """
        This is the method the command: emulation_ospf_network_group_config option external_prefix
        Description:Prefix Length
            DEFAULT
                None
        Constants Available: EXTERNAL_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_PREFIX_CMD : any})

    def emulation_ospf_network_group_config_external_prefix_count(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option external_prefix_count
        Description:Prefix Count
            DEFAULT
                None
        Constants Available: EXTERNAL_PREFIX_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_PREFIX_COUNT_CMD : numeric})

    def emulation_ospf_network_group_config_external_reference_ls_type(self, opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_reference_ls_type
        Description:Reference LS Type
            Valid options are:
            ignore

            router

            network

            DEFAULT
                None
        Constants Available: EXTERNAL_REFERENCE_LS_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_REFERENCE_LS_TYPE_CMD : opt})

    def emulation_ospf_network_group_config_external_referenced_link_state_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option external_referenced_link_state_id
        Description:Referenced Link State Id
            DEFAULT
                None
        Constants Available: EXTERNAL_REFERENCED_LINK_STATE_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_REFERENCED_LINK_STATE_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_external_t_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_t_bit
        Description:External Route Tag Bit
            DEFAULT
                None
        Constants Available: EXTERNAL_T_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_T_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_unused_bit4(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_unused_bit4
        Description:Options-(4)Unused
            DEFAULT
                None
        Constants Available: EXTERNAL_UNUSED_BIT4_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT4_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_unused_bit5(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_unused_bit5
        Description:Options-(5)Unused
            DEFAULT
                None
        Constants Available: EXTERNAL_UNUSED_BIT5_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT5_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_unused_bit6(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_unused_bit6
        Description:Options-(6)Unused
            DEFAULT
                None
        Constants Available: EXTERNAL_UNUSED_BIT6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT6_CMD : bool_opt})

    def emulation_ospf_network_group_config_external_unused_bit7(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option external_unused_bit7
        Description:Options-(7)Unused
            DEFAULT
                None
        Constants Available: EXTERNAL_UNUSED_BIT7_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT7_CMD : bool_opt})

    def emulation_ospf_network_group_config_fat_tree_level_count(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option fat_tree_level_count
        Description:Number of Levels
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'fat-tree' |
        Constants Available: FAT_TREE_LEVEL_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.FAT_TREE_LEVEL_COUNT_CMD : numeric})

    def emulation_ospf_network_group_config_fat_tree_link_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option fat_tree_link_multiplier
        Description:number of links between two nodes
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'fat-tree' |
        Constants Available: FAT_TREE_LINK_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.FAT_TREE_LINK_MULTIPLIER_CMD : numeric})

    def emulation_ospf_network_group_config_fat_tree_node_count(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option fat_tree_node_count
        Description:Number of Nodes Per Level
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'fat-tree' |
        Constants Available: FAT_TREE_NODE_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.FAT_TREE_NODE_COUNT_CMD : numeric})

    def emulation_ospf_network_group_config_forwarding_address(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option forwarding_address
        Description:Forwarding addresses of the Type-7 LSA
            DEFAULT
                None
        Constants Available: FORWARDING_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.FORWARDING_ADDRESS_CMD : ipv6})

    def emulation_ospf_network_group_config_forwarding_address_step(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option forwarding_address_step
        Description:Not defined
            DEFAULT
                None
        Constants Available: FORWARDING_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.FORWARDING_ADDRESS_STEP_CMD : ipv6})

    def emulation_ospf_network_group_config_from_ip(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option from_ip
        Description:Not defined
            DEFAULT
                None
        Constants Available: FROM_IP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.FROM_IP_CMD : ipv4})

    def emulation_ospf_network_group_config_from_ip_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option from_ip_step
        Description:Not defined
            DEFAULT
                None
        Constants Available: FROM_IP_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.FROM_IP_STEP_CMD : ipv4})

    def emulation_ospf_network_group_config_from_ipv6(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option from_ipv6
        Description:128 Bits IPv6 address.
            DEFAULT
                None
        Constants Available: FROM_IPV6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.FROM_IPV6_CMD : ipv6})

    def emulation_ospf_network_group_config_from_ipv6_step(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option from_ipv6_step
        Description:Not defined
            DEFAULT
                None
        Constants Available: FROM_IPV6_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.FROM_IPV6_STEP_CMD : ipv6})

    def emulation_ospf_network_group_config_grid_include_emulated_device(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option grid_include_emulated_device
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_INCLUDE_EMULATED_DEVICE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.GRID_INCLUDE_EMULATED_DEVICE_CMD : bool_opt})

    def emulation_ospf_network_group_config_grid_link_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option grid_link_multiplier
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_LINK_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.GRID_LINK_MULTIPLIER_CMD : numeric})

    def emulation_ospf_network_group_config_hub_spoke_enable_level_2(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option hub_spoke_enable_level_2
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'hub-and-spoke' |
        Constants Available: HUB_SPOKE_ENABLE_LEVEL_2_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_ENABLE_LEVEL_2_CMD : bool_opt})

    def emulation_ospf_network_group_config_hub_spoke_link_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option hub_spoke_link_multiplier
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'hub-and-spoke' |
        Constants Available: HUB_SPOKE_LINK_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_LINK_MULTIPLIER_CMD : numeric})

    def emulation_ospf_network_group_config_hub_spoke_number_of_first_level(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option hub_spoke_number_of_first_level
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'hub-and-spoke' |
        Constants Available: HUB_SPOKE_NUMBER_OF_FIRST_LEVEL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_NUMBER_OF_FIRST_LEVEL_CMD : numeric})

    def emulation_ospf_network_group_config_hub_spoke_number_of_second_level(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option hub_spoke_number_of_second_level
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'hub-and-spoke' |
        Constants Available: HUB_SPOKE_NUMBER_OF_SECOND_LEVEL_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_NUMBER_OF_SECOND_LEVEL_CMD : numeric})

    def emulation_ospf_network_group_config_inter_area_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_active
        Description:Whether this is to be advertised or not
            DEFAULT
                None
        Constants Available: INTER_AREA_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_d_c_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_d_c_bit
        Description:Demand Circuit bit
            DEFAULT
                None
        Constants Available: INTER_AREA_D_C_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_D_C_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_destination_router_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_destination_router_id
        Description:Destination Router Id
            DEFAULT
                None
        Constants Available: INTER_AREA_DESTINATION_ROUTER_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_DESTINATION_ROUTER_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_inter_area_destination_router_id_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_destination_router_id_step
        Description:Destination Router Id Prefix
            DEFAULT
                None
        Constants Available: INTER_AREA_DESTINATION_ROUTER_ID_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_DESTINATION_ROUTER_ID_STEP_CMD : ipv4})

    def emulation_ospf_network_group_config_inter_area_e_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_e_bit
        Description:bit describing how AS-external-LSAs are flooded
            DEFAULT
                None
        Constants Available: INTER_AREA_E_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_E_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_link_state_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_link_state_id
        Description:Link State Id of the simulated IPv6 network
            DEFAULT
                None
        Constants Available: INTER_AREA_LINK_STATE_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_LINK_STATE_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_inter_area_link_state_id_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_link_state_id_step
        Description:Link State Id Step for the LSAs to be generated for this set of IPv6
            Inter-Area networks.
            DEFAULT
                None
        Constants Available: INTER_AREA_LINK_STATE_ID_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_LINK_STATE_ID_STEP_CMD : ipv4})

    def emulation_ospf_network_group_config_inter_area_m_c_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_m_c_bit
        Description:bit for forwarding of IP multicast datagrams
            DEFAULT
                None
        Constants Available: INTER_AREA_M_C_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_M_C_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_metric
        Description:Metric
            DEFAULT
                None
        Constants Available: INTER_AREA_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_inter_area_n_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_n_bit
        Description:bit for handling Type 7 LSAs
            DEFAULT
                None
        Constants Available: INTER_AREA_N_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_N_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_prefix_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_active
        Description:Whether this is to be advertised or not
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_prefix_count(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_count
        Description:Count
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_COUNT_CMD : numeric})

    def emulation_ospf_network_group_config_inter_area_prefix_l_a_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_l_a_bit
        Description:Options-LA Bit(Local Address)
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_L_A_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_L_A_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_prefix_link_state_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_link_state_id
        Description:Link State Id of the simulated IPv6 network
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_LINK_STATE_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_LINK_STATE_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_inter_area_prefix_link_state_id_prefix(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_link_state_id_prefix
        Description:Link State Id Prefix
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_LINK_STATE_ID_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_LINK_STATE_ID_PREFIX_CMD : ipv4})

    def emulation_ospf_network_group_config_inter_area_prefix_m_c_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_m_c_bit
        Description:Options-MC Bit(Multicast)
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_M_C_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_M_C_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_prefix_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_metric
        Description:Metric
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_inter_area_prefix_n_u_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_n_u_bit
        Description:Options-NU Bit(No Unicast)
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_N_U_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_N_U_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_prefix_network_address(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_network_address
        Description:Prefixes of the simulated IPv6 network
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_NETWORK_ADDRESS_CMD : ipv6})

    def emulation_ospf_network_group_config_inter_area_prefix_p_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_p_bit
        Description:Options-P Bit(Propagate)
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_P_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_P_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_prefix_prefix(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_prefix
        Description:Prefix Length
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_PREFIX_CMD : numeric})

    def emulation_ospf_network_group_config_inter_area_prefix_prefix_count(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_prefix_count
        Description:Prefix Count
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_PREFIX_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_PREFIX_COUNT_CMD : numeric})

    def emulation_ospf_network_group_config_inter_area_prefix_unused_bit4(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_unused_bit4
        Description:Options-(4)Unused
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_UNUSED_BIT4_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT4_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_prefix_unused_bit5(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_unused_bit5
        Description:Options-(5)Unused
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_UNUSED_BIT5_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT5_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_prefix_unused_bit6(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_unused_bit6
        Description:Options-(6)Unused
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_UNUSED_BIT6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT6_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_prefix_unused_bit7(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_prefix_unused_bit7
        Description:Options-(7)Unused
            DEFAULT
                None
        Constants Available: INTER_AREA_PREFIX_UNUSED_BIT7_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT7_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_r_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_r_bit
        Description:Router bit
            DEFAULT
                None
        Constants Available: INTER_AREA_R_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_R_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_reserved_bit6(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_reserved_bit6
        Description:(6) Reserved Bit
            DEFAULT
                None
        Constants Available: INTER_AREA_RESERVED_BIT6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_RESERVED_BIT6_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_reserved_bit7(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_reserved_bit7
        Description:(7) Reserved Bit
            DEFAULT
                None
        Constants Available: INTER_AREA_RESERVED_BIT7_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_RESERVED_BIT7_CMD : bool_opt})

    def emulation_ospf_network_group_config_inter_area_v6_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option inter_area_v6_bit
        Description:bit for excluding the router/link from IPv6 routing calculations. If
            clear, router/link is excluded
            DEFAULT
                None
        Constants Available: INTER_AREA_V6_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTER_AREA_V6_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_intra_area_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_active
        Description:Whether this is to be advertised or not
            DEFAULT
                None
        Constants Available: INTRA_AREA_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_intra_area_l_a_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_l_a_bit
        Description:Options-LA Bit(Local Address)
            DEFAULT
                None
        Constants Available: INTRA_AREA_L_A_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_L_A_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_intra_area_link_state_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_link_state_id
        Description:Link State Id of the simulated IPv6 network
            DEFAULT
                None
        Constants Available: INTRA_AREA_LINK_STATE_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_LINK_STATE_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_intra_area_link_state_id_prefix(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_link_state_id_prefix
        Description:Link State Id Prefix
            DEFAULT
                None
        Constants Available: INTRA_AREA_LINK_STATE_ID_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_LINK_STATE_ID_PREFIX_CMD : ipv4})

    def emulation_ospf_network_group_config_intra_area_m_c_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_m_c_bit
        Description:Options-MC Bit(Multicast)
            DEFAULT
                None
        Constants Available: INTRA_AREA_M_C_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_M_C_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_intra_area_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_metric
        Description:Metric
            DEFAULT
                None
        Constants Available: INTRA_AREA_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_intra_area_n_u_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_n_u_bit
        Description:Options-NU Bit(No Unicast)
            DEFAULT
                None
        Constants Available: INTRA_AREA_N_U_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_N_U_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_intra_area_network_address(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_network_address
        Description:Prefixes of the simulated IPv6 network
            DEFAULT
                None
        Constants Available: INTRA_AREA_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_NETWORK_ADDRESS_CMD : ipv6})

    def emulation_ospf_network_group_config_intra_area_network_address_step(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_network_address_step
        Description:Not defined
            DEFAULT
                None
        Constants Available: INTRA_AREA_NETWORK_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_NETWORK_ADDRESS_STEP_CMD : ipv6})

    def emulation_ospf_network_group_config_intra_area_p_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_p_bit
        Description:Options-P Bit(Propagate)
            DEFAULT
                None
        Constants Available: INTRA_AREA_P_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_P_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_intra_area_prefix_count(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_prefix_count
        Description:Prefix Count
            DEFAULT
                None
        Constants Available: INTRA_AREA_PREFIX_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_PREFIX_COUNT_CMD : numeric})

    def emulation_ospf_network_group_config_intra_area_reference_ls_type(self, opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_reference_ls_type
        Description:Reference LS Type
            Valid options are:
            router

            network

            DEFAULT
                None
        Constants Available: INTRA_AREA_REFERENCE_LS_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCE_LS_TYPE_CMD : opt})

    def emulation_ospf_network_group_config_intra_area_referenced_link_state_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_referenced_link_state_id
        Description:Referenced Link State Id
            DEFAULT
                None
        Constants Available: INTRA_AREA_REFERENCED_LINK_STATE_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCED_LINK_STATE_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_intra_area_referenced_router_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_referenced_router_id
        Description:Referenced Advertising Router Id
            DEFAULT
                None
        Constants Available: INTRA_AREA_REFERENCED_ROUTER_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCED_ROUTER_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_intra_area_unused_bit4(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_unused_bit4
        Description:Options-(4)Unused
            DEFAULT
                None
        Constants Available: INTRA_AREA_UNUSED_BIT4_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT4_CMD : bool_opt})

    def emulation_ospf_network_group_config_intra_area_unused_bit5(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_unused_bit5
        Description:Options-(5)Unused
            DEFAULT
                None
        Constants Available: INTRA_AREA_UNUSED_BIT5_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT5_CMD : bool_opt})

    def emulation_ospf_network_group_config_intra_area_unused_bit6(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_unused_bit6
        Description:Options-(6)Unused
            DEFAULT
                None
        Constants Available: INTRA_AREA_UNUSED_BIT6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT6_CMD : bool_opt})

    def emulation_ospf_network_group_config_intra_area_unused_bit7(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option intra_area_unused_bit7
        Description:Options-(7)Unused
            DEFAULT
                None
        Constants Available: INTRA_AREA_UNUSED_BIT7_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT7_CMD : bool_opt})

    def emulation_ospf_network_group_config_ipv4_prefix_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv4_prefix_active
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv4-prefix' |
        Constants Available: IPV4_PREFIX_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_ipv4_prefix_allow_propagate(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv4_prefix_allow_propagate
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv4-prefix' |
        Constants Available: IPV4_PREFIX_ALLOW_PROPAGATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ALLOW_PROPAGATE_CMD : bool_opt})

    def emulation_ospf_network_group_config_ipv4_prefix_length(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv4_prefix_length
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv4-prefix' |
        Constants Available: IPV4_PREFIX_LENGTH_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_LENGTH_CMD : numeric})

    def emulation_ospf_network_group_config_ipv4_prefix_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv4_prefix_metric
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv4-prefix' |
        Constants Available: IPV4_PREFIX_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_ipv4_prefix_network_address(self, ip):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv4_prefix_network_address
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv4-prefix' |
        Constants Available: IPV4_PREFIX_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_NETWORK_ADDRESS_CMD : ip})

    def emulation_ospf_network_group_config_ipv4_prefix_network_address_step(self, ip):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv4_prefix_network_address_step
        Description:Not defined
            DEFAULT

            0.0.0.1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv4-prefix' |
        Constants Available: IPV4_PREFIX_NETWORK_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_NETWORK_ADDRESS_STEP_CMD : ip})

    def emulation_ospf_network_group_config_ipv4_prefix_number_of_addresses(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv4_prefix_number_of_addresses
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv4-prefix' |
        Constants Available: IPV4_PREFIX_NUMBER_OF_ADDRESSES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_NUMBER_OF_ADDRESSES_CMD : numeric})

    def emulation_ospf_network_group_config_ipv4_prefix_route_origin(self, opt):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv4_prefix_route_origin
        Description:Not defined
            Valid options are:
            another_area

            external_type_1

            external_type_2

            nssa

            same_area

            DEFAULT

            another_area
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv4-prefix' |
        Constants Available: IPV4_PREFIX_ROUTE_ORIGIN_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ROUTE_ORIGIN_CMD : opt})

    def emulation_ospf_network_group_config_ipv6_prefix_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv6_prefix_active
        Description:Flag.
            DEFAULT
                None
        Constants Available: IPV6_PREFIX_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_ipv6_prefix_length(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv6_prefix_length
        Description:Defines the length (in bits) of the mask to be used in conjunction with
            all the addresses created in the range.
            DEFAULT
                None
        Constants Available: IPV6_PREFIX_LENGTH_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_LENGTH_CMD : numeric})

    def emulation_ospf_network_group_config_ipv6_prefix_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv6_prefix_metric
        Description:Route Metric
            DEFAULT
                None
        Constants Available: IPV6_PREFIX_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_ipv6_prefix_network_address(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv6_prefix_network_address
        Description:Network addresses of the simulated IPv4 network
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv6-prefix' |
        Constants Available: IPV6_PREFIX_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_NETWORK_ADDRESS_CMD : ipv6})

    def emulation_ospf_network_group_config_ipv6_prefix_network_address_step(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv6_prefix_network_address_step
        Description:Network addresses step of the simulated IPv6 network
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv6-prefix' |
        Constants Available: IPV6_PREFIX_NETWORK_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_NETWORK_ADDRESS_STEP_CMD : ipv6})

    def emulation_ospf_network_group_config_ipv6_prefix_number_of_addresses(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv6_prefix_number_of_addresses
        Description:Number of Network Addresses
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ipv6-prefix' |
        Constants Available: IPV6_PREFIX_NUMBER_OF_ADDRESSES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_NUMBER_OF_ADDRESSES_CMD : numeric})

    def emulation_ospf_network_group_config_ipv6_prefix_route_origin(self, opt):
        """
        This is the method the command: emulation_ospf_network_group_config option ipv6_prefix_route_origin
        Description:Route Origin
            Valid options are:
            anotherarea

            externaltype1

            externaltype2

            samearea

            nssa

            DEFAULT
                None
        Constants Available: IPV6_PREFIX_ROUTE_ORIGIN_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_ROUTE_ORIGIN_CMD : opt})

    def emulation_ospf_network_group_config_linear_link_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option linear_link_multiplier
        Description:number of links between two nodes
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'linear' |
        Constants Available: LINEAR_LINK_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINEAR_LINK_MULTIPLIER_CMD : numeric})

    def emulation_ospf_network_group_config_linear_nodes(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option linear_nodes
        Description:number of nodes
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'linear' |
        Constants Available: LINEAR_NODES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINEAR_NODES_CMD : numeric})

    def emulation_ospf_network_group_config_link_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_metric
        Description:Not defined
            DEFAULT
                None
        Constants Available: LINK_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_link_te_administrator_group(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option link_te_administrator_group
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
            'type' | value= 'router' |
        Constants Available: LINK_TE_ADMINISTRATOR_GROUP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINK_TE_ADMINISTRATOR_GROUP_CMD : numeric})

    def emulation_ospf_network_group_config_linklsa_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_active
        Description:Whether this is to be advertised or not
            DEFAULT
                None
        Constants Available: LINKLSA_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_d_c_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_d_c_bit
        Description:Demand Circuit bit
            DEFAULT
                None
        Constants Available: LINKLSA_D_C_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_D_C_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_e_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_e_bit
        Description:bit describing how AS-external-LSAs are flooded
            DEFAULT
                None
        Constants Available: LINKLSA_E_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_E_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_l_a_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_l_a_bit
        Description:Options-LA Bit(Local Address)
            DEFAULT
                None
        Constants Available: LINKLSA_L_A_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_L_A_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_link_local_address(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_link_local_address
        Description:128 Bits IPv6 address.
            DEFAULT
                None
        Constants Available: LINKLSA_LINK_LOCAL_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_LINK_LOCAL_ADDRESS_CMD : ipv6})

    def emulation_ospf_network_group_config_linklsa_link_state_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_link_state_id
        Description:Link State Id of the simulated IPv6 network
            DEFAULT
                None
        Constants Available: LINKLSA_LINK_STATE_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_LINK_STATE_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_linklsa_link_state_id_prefix(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_link_state_id_prefix
        Description:Link State Id Prefix
            DEFAULT
                None
        Constants Available: LINKLSA_LINK_STATE_ID_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_LINK_STATE_ID_PREFIX_CMD : ipv4})

    def emulation_ospf_network_group_config_linklsa_m_c_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_m_c_bit
        Description:Options-MC Bit(Multicast)
            DEFAULT
                None
        Constants Available: LINKLSA_M_C_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_M_C_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_metric
        Description:Metric
            DEFAULT
                None
        Constants Available: LINKLSA_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_linklsa_n_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_n_bit
        Description:bit for handling Type 7 LSAs
            DEFAULT
                None
        Constants Available: LINKLSA_N_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_N_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_n_u_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_n_u_bit
        Description:Options-NU Bit(No Unicast)
            DEFAULT
                None
        Constants Available: LINKLSA_N_U_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_N_U_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_network_address(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_network_address
        Description:Network addresses of the simulated IPv6 network
            DEFAULT
                None
        Constants Available: LINKLSA_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_NETWORK_ADDRESS_CMD : ipv6})

    def emulation_ospf_network_group_config_linklsa_p_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_p_bit
        Description:Options-P Bit(Propagate)
            DEFAULT
                None
        Constants Available: LINKLSA_P_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_P_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_prefix(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_prefix
        Description:Prefix
            DEFAULT
                None
        Constants Available: LINKLSA_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_PREFIX_CMD : numeric})

    def emulation_ospf_network_group_config_linklsa_prefix_count(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_prefix_count
        Description:Range Size
            DEFAULT
                None
        Constants Available: LINKLSA_PREFIX_COUNT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_PREFIX_COUNT_CMD : numeric})

    def emulation_ospf_network_group_config_linklsa_r_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_r_bit
        Description:Router bit
            DEFAULT
                None
        Constants Available: LINKLSA_R_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_R_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_reserved_bit6(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_reserved_bit6
        Description:(6) Reserved Bit
            DEFAULT
                None
        Constants Available: LINKLSA_RESERVED_BIT6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_RESERVED_BIT6_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_reserved_bit7(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_reserved_bit7
        Description:(7) Reserved Bit
            DEFAULT
                None
        Constants Available: LINKLSA_RESERVED_BIT7_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_RESERVED_BIT7_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_router_priority(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_router_priority
        Description:Router Priority
            DEFAULT
                None
        Constants Available: LINKLSA_ROUTER_PRIORITY_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_ROUTER_PRIORITY_CMD : numeric})

    def emulation_ospf_network_group_config_linklsa_unused_bit4(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_unused_bit4
        Description:Options-(4)Unused
            DEFAULT
                None
        Constants Available: LINKLSA_UNUSED_BIT4_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT4_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_unused_bit5(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_unused_bit5
        Description:Options-(5)Unused
            DEFAULT
                None
        Constants Available: LINKLSA_UNUSED_BIT5_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT5_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_unused_bit6(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_unused_bit6
        Description:Options-(6)Unused
            DEFAULT
                None
        Constants Available: LINKLSA_UNUSED_BIT6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT6_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_unused_bit7(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_unused_bit7
        Description:Options-(7)Unused
            DEFAULT
                None
        Constants Available: LINKLSA_UNUSED_BIT7_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT7_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_v6_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_v6_bit
        Description:bit for excluding the router/link from IPv6 routing calculations. If
            clear, router/link is excluded
            DEFAULT
                None
        Constants Available: LINKLSA_V6_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_V6_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_linklsa_x_bit(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option linklsa_x_bit
        Description:bit for forwarding of IP multicast datagrams
            DEFAULT
                None
        Constants Available: LINKLSA_X_BIT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.LINKLSA_X_BIT_CMD : bool_opt})

    def emulation_ospf_network_group_config_mesh_include_emulated_device(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option mesh_include_emulated_device
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'mesh' |
        Constants Available: MESH_INCLUDE_EMULATED_DEVICE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.MESH_INCLUDE_EMULATED_DEVICE_CMD : bool_opt})

    def emulation_ospf_network_group_config_mesh_link_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option mesh_link_multiplier
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'mesh' |
        Constants Available: MESH_LINK_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.MESH_LINK_MULTIPLIER_CMD : numeric})

    def emulation_ospf_network_group_config_mesh_number_of_nodes(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option mesh_number_of_nodes
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'mesh' |
        Constants Available: MESH_NUMBER_OF_NODES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.MESH_NUMBER_OF_NODES_CMD : numeric})

    def emulation_ospf_network_group_config_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option multiplier
        Description:Not defined
            DEFAULT
                None
        Constants Available: MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.MULTIPLIER_CMD : numeric})

    def emulation_ospf_network_group_config_nssa_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_active
        Description:Not defined
            DEFAULT
                None
        Constants Available: NSSA_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_nssa_include_forwarding_address(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_include_forwarding_address
        Description:Include Forwarding Address
            DEFAULT
                None
        Constants Available: NSSA_INCLUDE_FORWARDING_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_INCLUDE_FORWARDING_ADDRESS_CMD : bool_opt})

    def emulation_ospf_network_group_config_nssa_link_state_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_link_state_id
        Description:Start Link State Id for the LSAs to be generated for this set of IPv6
            NSSA networks.
            DEFAULT
                None
        Constants Available: NSSA_LINK_STATE_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_LINK_STATE_ID_CMD : ipv4})

    def emulation_ospf_network_group_config_nssa_link_state_id_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_link_state_id_step
        Description:Link State Id Step for the LSAs to be generated for this set of IPv6
            NSSA networks.
            DEFAULT
                None
        Constants Available: NSSA_LINK_STATE_ID_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_LINK_STATE_ID_STEP_CMD : ipv4})

    def emulation_ospf_network_group_config_nssa_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_metric
        Description:Not defined
            DEFAULT
                None
        Constants Available: NSSA_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_nssa_network_address(self, ip):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_network_address
        Description:Not defined
            DEFAULT
                None
        Constants Available: NSSA_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_NETWORK_ADDRESS_CMD : ip})

    def emulation_ospf_network_group_config_nssa_network_address_step(self, ip):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_network_address_step
        Description:Not defined
            DEFAULT

            0.0.0.1
        Constants Available: NSSA_NETWORK_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_NETWORK_ADDRESS_STEP_CMD : ip})

    def emulation_ospf_network_group_config_nssa_number_of_routes(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_number_of_routes
        Description:Not defined
            DEFAULT
                None
        Constants Available: NSSA_NUMBER_OF_ROUTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_NUMBER_OF_ROUTES_CMD : numeric})

    def emulation_ospf_network_group_config_nssa_prefix(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_prefix
        Description:Not defined
            DEFAULT
                None
        Constants Available: NSSA_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_PREFIX_CMD : numeric})

    def emulation_ospf_network_group_config_nssa_propagate(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option nssa_propagate
        Description:Propagate
            DEFAULT
                None
        Constants Available: NSSA_PROPAGATE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.NSSA_PROPAGATE_CMD : bool_opt})

    def emulation_ospf_network_group_config_prefix(self, any):
        """
        This is the method the command: emulation_ospf_network_group_config option prefix
        Description:Prefix Length
            DEFAULT
                None
        Constants Available: PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.PREFIX_CMD : any})

    def emulation_ospf_network_group_config_protocol_name(self, alpha):
        """
        This is the method the command: emulation_ospf_network_group_config option protocol_name
        Description:Not defined
            DEFAULT
                None
        Constants Available: PROTOCOL_NAME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        alpha --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.PROTOCOL_NAME_CMD : alpha})

    def emulation_ospf_network_group_config_return_detailed_handles(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option return_detailed_handles
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
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.RETURN_DETAILED_HANDLES_CMD : bool_opt})

    def emulation_ospf_network_group_config_ring_include_emulated_device(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option ring_include_emulated_device
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ring' |
        Constants Available: RING_INCLUDE_EMULATED_DEVICE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.RING_INCLUDE_EMULATED_DEVICE_CMD : bool_opt})

    def emulation_ospf_network_group_config_ring_link_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option ring_link_multiplier
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ring' |
        Constants Available: RING_LINK_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.RING_LINK_MULTIPLIER_CMD : numeric})

    def emulation_ospf_network_group_config_ring_number_of_nodes(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option ring_number_of_nodes
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ring' |
        Constants Available: RING_NUMBER_OF_NODES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.RING_NUMBER_OF_NODES_CMD : numeric})

    def emulation_ospf_network_group_config_router_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option router_active
        Description:Flag.
            DEFAULT
                None
        Constants Available: ROUTER_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ROUTER_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_router_id(self, ip):
        """
        This is the method the command: emulation_ospf_network_group_config option router_id
        Description:The ID associated with the router.
            DEFAULT

            0.0.0.0
        Constants Available: ROUTER_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ROUTER_ID_CMD : ip})

    def emulation_ospf_network_group_config_router_system_id(self, hex8withspaces):
        """
        This is the method the command: emulation_ospf_network_group_config option router_system_id
        Description:6 Byte System Id in hex format.
            DEFAULT
                None
        Constants Available: ROUTER_SYSTEM_ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        hex8withspaces --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.ROUTER_SYSTEM_ID_CMD : hex8withspaces})

    def emulation_ospf_network_group_config_stub_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option stub_active
        Description:Not defined
            DEFAULT
                None
        Constants Available: STUB_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.STUB_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_stub_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option stub_metric
        Description:Not defined
            DEFAULT
                None
        Constants Available: STUB_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.STUB_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_stub_network_address(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option stub_network_address
        Description:Not defined
            DEFAULT
                None
        Constants Available: STUB_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.STUB_NETWORK_ADDRESS_CMD : ipv4})

    def emulation_ospf_network_group_config_stub_network_address_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option stub_network_address_step
        Description:Not defined
            DEFAULT

            0.0.0.1
        Constants Available: STUB_NETWORK_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.STUB_NETWORK_ADDRESS_STEP_CMD : ipv4})

    def emulation_ospf_network_group_config_stub_number_of_routes(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option stub_number_of_routes
        Description:Not defined
            DEFAULT
                None
        Constants Available: STUB_NUMBER_OF_ROUTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.STUB_NUMBER_OF_ROUTES_CMD : numeric})

    def emulation_ospf_network_group_config_stub_prefix(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option stub_prefix
        Description:Not defined
            DEFAULT
                None
        Constants Available: STUB_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.STUB_PREFIX_CMD : numeric})

    def emulation_ospf_network_group_config_subnet_prefix_length(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option subnet_prefix_length
        Description:Not defined
            DEFAULT
                None
        Constants Available: SUBNET_PREFIX_LENGTH_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.SUBNET_PREFIX_LENGTH_CMD : numeric})

    def emulation_ospf_network_group_config_summary_active(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option summary_active
        Description:Not defined
            DEFAULT
                None
        Constants Available: SUMMARY_ACTIVE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.SUMMARY_ACTIVE_CMD : bool_opt})

    def emulation_ospf_network_group_config_summary_metric(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option summary_metric
        Description:Not defined
            DEFAULT
                None
        Constants Available: SUMMARY_METRIC_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.SUMMARY_METRIC_CMD : numeric})

    def emulation_ospf_network_group_config_summary_network_address(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option summary_network_address
        Description:Not defined
            DEFAULT
                None
        Constants Available: SUMMARY_NETWORK_ADDRESS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.SUMMARY_NETWORK_ADDRESS_CMD : ipv4})

    def emulation_ospf_network_group_config_summary_network_address_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option summary_network_address_step
        Description:Not defined
            DEFAULT

            0.0.0.1
        Constants Available: SUMMARY_NETWORK_ADDRESS_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.SUMMARY_NETWORK_ADDRESS_STEP_CMD : ipv4})

    def emulation_ospf_network_group_config_summary_number_of_routes(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option summary_number_of_routes
        Description:Not defined
            DEFAULT
                None
        Constants Available: SUMMARY_NUMBER_OF_ROUTES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.SUMMARY_NUMBER_OF_ROUTES_CMD : numeric})

    def emulation_ospf_network_group_config_summary_prefix(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option summary_prefix
        Description:Not defined
            DEFAULT
                None
        Constants Available: SUMMARY_PREFIX_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.SUMMARY_PREFIX_CMD : numeric})

    def emulation_ospf_network_group_config_to_ip(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option to_ip
        Description:Not defined
            DEFAULT
                None
        Constants Available: TO_IP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TO_IP_CMD : ipv4})

    def emulation_ospf_network_group_config_to_ip_step(self, ipv4):
        """
        This is the method the command: emulation_ospf_network_group_config option to_ip_step
        Description:Not defined
            DEFAULT
                None
        Constants Available: TO_IP_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TO_IP_STEP_CMD : ipv4})

    def emulation_ospf_network_group_config_to_ipv6(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option to_ipv6
        Description:128 Bits IPv6 address.
            DEFAULT
                None
        Constants Available: TO_IPV6_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TO_IPV6_CMD : ipv6})

    def emulation_ospf_network_group_config_to_ipv6_step(self, ipv6):
        """
        This is the method the command: emulation_ospf_network_group_config option to_ipv6_step
        Description:Not defined
            DEFAULT
                None
        Constants Available: TO_IPV6_STEP_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        ipv6 --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TO_IPV6_STEP_CMD : ipv6})

    def emulation_ospf_network_group_config_tree_depth(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option tree_depth
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'tree' |
        Constants Available: TREE_DEPTH_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TREE_DEPTH_CMD : numeric})

    def emulation_ospf_network_group_config_tree_include_emulated_device(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option tree_include_emulated_device
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'tree' |
        Constants Available: TREE_INCLUDE_EMULATED_DEVICE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TREE_INCLUDE_EMULATED_DEVICE_CMD : bool_opt})

    def emulation_ospf_network_group_config_tree_link_multiplier(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option tree_link_multiplier
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'tree' |
        Constants Available: TREE_LINK_MULTIPLIER_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TREE_LINK_MULTIPLIER_CMD : numeric})

    def emulation_ospf_network_group_config_tree_max_children_per_node(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option tree_max_children_per_node
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'tree' |
        Constants Available: TREE_MAX_CHILDREN_PER_NODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TREE_MAX_CHILDREN_PER_NODE_CMD : numeric})

    def emulation_ospf_network_group_config_tree_number_of_nodes(self, numeric):
        """
        This is the method the command: emulation_ospf_network_group_config option tree_number_of_nodes
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'tree' |
        Constants Available: TREE_NUMBER_OF_NODES_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TREE_NUMBER_OF_NODES_CMD : numeric})

    def emulation_ospf_network_group_config_tree_use_tree_depth(self, bool_opt):
        """
        This is the method the command: emulation_ospf_network_group_config option tree_use_tree_depth
        Description:Not defined
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'tree' |
        Constants Available: TREE_USE_TREE_DEPTH_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_network_group_config({EmulationOspfNetworkGroupConfigConstants.TREE_USE_TREE_DEPTH_CMD : bool_opt})


    supportedIxiaHltapiCommands = {EmulationOspfNetworkGroupConfigConstants.ACTIVE_ROUTER_ID_CMD, EmulationOspfNetworkGroupConfigConstants.ALLOW_PROPAGATE_CMD, EmulationOspfNetworkGroupConfigConstants.AUTO_SELECT_FORWARDING_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.CONNECTED_TO_HANDLE_CMD, EmulationOspfNetworkGroupConfigConstants.CUSTOM_FROM_NODE_INDEX_CMD, EmulationOspfNetworkGroupConfigConstants.CUSTOM_LINK_MULTIPLIER_CMD, EmulationOspfNetworkGroupConfigConstants.CUSTOM_TO_NODE_INDEX_CMD, EmulationOspfNetworkGroupConfigConstants.ENABLE_ADVERTISE_AS_STUB_NETWORK_CMD, EmulationOspfNetworkGroupConfigConstants.ENABLE_DEVICE_CMD, EmulationOspfNetworkGroupConfigConstants.ENABLE_IP_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_NETWORK_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_NUMBER_OF_ROUTES_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL1_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_NETWORK_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_NUMBER_OF_ROUTES_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL2_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_E_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_EXTERNAL_ROUTE_TAG_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_F_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_FORWARDING_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_IPV6_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_IPV6_NETWORK_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_L_A_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_NETWORK_GROUP_HANDLE_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_ROUTER_DESTINATION_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_ROUTER_SOURCE_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_STATE_ID_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_LINK_STATE_ID_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_M_C_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_N_U_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_P_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_PREFIX_COUNT_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_REFERENCE_LS_TYPE_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_REFERENCED_LINK_STATE_ID_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_T_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT4_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT5_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT6_CMD, EmulationOspfNetworkGroupConfigConstants.EXTERNAL_UNUSED_BIT7_CMD, EmulationOspfNetworkGroupConfigConstants.FAT_TREE_LEVEL_COUNT_CMD, EmulationOspfNetworkGroupConfigConstants.FAT_TREE_LINK_MULTIPLIER_CMD, EmulationOspfNetworkGroupConfigConstants.FAT_TREE_NODE_COUNT_CMD, EmulationOspfNetworkGroupConfigConstants.FORWARDING_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.FORWARDING_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.FROM_IP_CMD, EmulationOspfNetworkGroupConfigConstants.FROM_IP_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.FROM_IPV6_CMD, EmulationOspfNetworkGroupConfigConstants.FROM_IPV6_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.GRID_COL_CMD, EmulationOspfNetworkGroupConfigConstants.GRID_INCLUDE_EMULATED_DEVICE_CMD, EmulationOspfNetworkGroupConfigConstants.GRID_LINK_MULTIPLIER_CMD, EmulationOspfNetworkGroupConfigConstants.GRID_ROW_CMD, EmulationOspfNetworkGroupConfigConstants.HANDLE_CMD, EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_ENABLE_LEVEL_2_CMD, EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_LINK_MULTIPLIER_CMD, EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_NUMBER_OF_FIRST_LEVEL_CMD, EmulationOspfNetworkGroupConfigConstants.HUB_SPOKE_NUMBER_OF_SECOND_LEVEL_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_D_C_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_DESTINATION_ROUTER_ID_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_DESTINATION_ROUTER_ID_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_E_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_LINK_STATE_ID_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_LINK_STATE_ID_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_M_C_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_N_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_COUNT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_L_A_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_LINK_STATE_ID_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_LINK_STATE_ID_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_M_C_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_N_U_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_P_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_PREFIX_COUNT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT4_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT5_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT6_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_PREFIX_UNUSED_BIT7_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_R_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_RESERVED_BIT6_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_RESERVED_BIT7_CMD, EmulationOspfNetworkGroupConfigConstants.INTER_AREA_V6_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_L_A_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_LINK_STATE_ID_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_LINK_STATE_ID_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_M_C_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_N_U_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_NETWORK_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_P_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_PREFIX_COUNT_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCE_LS_TYPE_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCED_LINK_STATE_ID_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_REFERENCED_ROUTER_ID_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT4_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT5_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT6_CMD, EmulationOspfNetworkGroupConfigConstants.INTRA_AREA_UNUSED_BIT7_CMD, EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ALLOW_PROPAGATE_CMD, EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_LENGTH_CMD, EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_NETWORK_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_NUMBER_OF_ADDRESSES_CMD, EmulationOspfNetworkGroupConfigConstants.IPV4_PREFIX_ROUTE_ORIGIN_CMD, EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_LENGTH_CMD, EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_NETWORK_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_NUMBER_OF_ADDRESSES_CMD, EmulationOspfNetworkGroupConfigConstants.IPV6_PREFIX_ROUTE_ORIGIN_CMD, EmulationOspfNetworkGroupConfigConstants.LINEAR_LINK_MULTIPLIER_CMD, EmulationOspfNetworkGroupConfigConstants.LINEAR_NODES_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_ADMINISTRATOR_GROUP_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_MAX_BW_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_MAX_RESV_BW_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY0_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY1_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY2_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY3_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY4_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY5_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY6_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY7_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_D_C_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_E_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_L_A_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_LINK_LOCAL_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_LINK_STATE_ID_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_LINK_STATE_ID_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_M_C_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_N_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_N_U_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_P_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_PREFIX_COUNT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_R_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_RESERVED_BIT6_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_RESERVED_BIT7_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_ROUTER_PRIORITY_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT4_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT5_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT6_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_UNUSED_BIT7_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_V6_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.LINKLSA_X_BIT_CMD, EmulationOspfNetworkGroupConfigConstants.MESH_INCLUDE_EMULATED_DEVICE_CMD, EmulationOspfNetworkGroupConfigConstants.MESH_LINK_MULTIPLIER_CMD, EmulationOspfNetworkGroupConfigConstants.MESH_NUMBER_OF_NODES_CMD, EmulationOspfNetworkGroupConfigConstants.MODE_CMD, EmulationOspfNetworkGroupConfigConstants.MULTIPLIER_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_INCLUDE_FORWARDING_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_LINK_STATE_ID_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_LINK_STATE_ID_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_NETWORK_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_NUMBER_OF_ROUTES_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.NSSA_PROPAGATE_CMD, EmulationOspfNetworkGroupConfigConstants.PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.PROTOCOL_NAME_CMD, EmulationOspfNetworkGroupConfigConstants.RETURN_DETAILED_HANDLES_CMD, EmulationOspfNetworkGroupConfigConstants.RING_INCLUDE_EMULATED_DEVICE_CMD, EmulationOspfNetworkGroupConfigConstants.RING_LINK_MULTIPLIER_CMD, EmulationOspfNetworkGroupConfigConstants.RING_NUMBER_OF_NODES_CMD, EmulationOspfNetworkGroupConfigConstants.ROUTER_ABR_CMD, EmulationOspfNetworkGroupConfigConstants.ROUTER_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.ROUTER_ASBR_CMD, EmulationOspfNetworkGroupConfigConstants.ROUTER_ID_CMD, EmulationOspfNetworkGroupConfigConstants.ROUTER_ID_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.ROUTER_SYSTEM_ID_CMD, EmulationOspfNetworkGroupConfigConstants.STUB_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.STUB_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.STUB_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.STUB_NETWORK_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.STUB_NUMBER_OF_ROUTES_CMD, EmulationOspfNetworkGroupConfigConstants.STUB_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.SUBNET_PREFIX_LENGTH_CMD, EmulationOspfNetworkGroupConfigConstants.SUMMARY_ACTIVE_CMD, EmulationOspfNetworkGroupConfigConstants.SUMMARY_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.SUMMARY_NETWORK_ADDRESS_CMD, EmulationOspfNetworkGroupConfigConstants.SUMMARY_NETWORK_ADDRESS_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.SUMMARY_NUMBER_OF_ROUTES_CMD, EmulationOspfNetworkGroupConfigConstants.SUMMARY_PREFIX_CMD, EmulationOspfNetworkGroupConfigConstants.TO_IP_CMD, EmulationOspfNetworkGroupConfigConstants.TO_IP_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.TO_IPV6_CMD, EmulationOspfNetworkGroupConfigConstants.TO_IPV6_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.TREE_DEPTH_CMD, EmulationOspfNetworkGroupConfigConstants.TREE_INCLUDE_EMULATED_DEVICE_CMD, EmulationOspfNetworkGroupConfigConstants.TREE_LINK_MULTIPLIER_CMD, EmulationOspfNetworkGroupConfigConstants.TREE_MAX_CHILDREN_PER_NODE_CMD, EmulationOspfNetworkGroupConfigConstants.TREE_NUMBER_OF_NODES_CMD, EmulationOspfNetworkGroupConfigConstants.TREE_USE_TREE_DEPTH_CMD, EmulationOspfNetworkGroupConfigConstants.TYPE_CMD}
