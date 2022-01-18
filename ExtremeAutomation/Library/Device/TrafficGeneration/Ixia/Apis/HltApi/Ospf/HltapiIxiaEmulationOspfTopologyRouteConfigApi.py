from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfTopologyRouteConfigApi import EmulationOspfTopologyRouteConfigApi, EmulationOspfTopologyRouteConfigConstants

"""
    This is the API class for the command: emulation_ospf_topology_route_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaEmulationOspfTopologyRouteConfigApi(EmulationOspfTopologyRouteConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaEmulationOspfTopologyRouteConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_topology_route_config
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfTopologyRouteConfigConstants.EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG_API)
        assert isinstance(api, EmulationOspfTopologyRouteConfigApi)
        api.emulation_ospf_topology_route_config(dummyDict)
    """
    def emulation_ospf_topology_route_config(self, argdictionary):
        return super(IxiaEmulationOspfTopologyRouteConfigApi, self).emulation_ospf_topology_route_config(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_topology_route_config_area_id(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option area_id
        Description:The OSPF area ID associated with the interface. This parameter is valid
            for -type router, grid, network. This parameter is valid with
            IxTclProtocol and IxTclNetwork.
            DEFAULT

            0.0.0.0
        Constants Available: AREA_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.AREA_ID_CMD : ip})

    def emulation_ospf_topology_route_config_bfd_registration(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option bfd_registration
        Description:Enable or disable BFD registration.
            DEFAULT

            0
        Constants Available: BFD_REGISTRATION_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.BFD_REGISTRATION_CMD : bool_opt})

    def emulation_ospf_topology_route_config_dead_interval(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option dead_interval
        Description:The number of seconds before declaring a silent router down. This
            parameter is valid for -type router, grid, network. This parameter is
            valid with IxTclProtocol and IxTclNetwork.
            DEFAULT

            40
        Constants Available: DEAD_INTERVAL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.DEAD_INTERVAL_CMD : range})

    def emulation_ospf_topology_route_config_enable_advertise_loopback(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option enable_advertise_loopback
        Description:Used for Traffic Engineering. If checked, a stub interface will be added
            to each router with IP = Router ID with a 32-bit mask. (x.x.x.x/32).
            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            Used for Traffic Engineering. If checked, a stub interface will be added
            to each router with IP = Router ID with a 32-bit mask. (x.x.x.x/32).
            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: ENABLE_ADVERTISE_LOOPBACK_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ENABLE_ADVERTISE_LOOPBACK_CMD : bool_opt})

    def emulation_ospf_topology_route_config_entry_point_address(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option entry_point_address
        Description:The entry point address of the OSPFv3 network range grid.This parameter
            is valid for -type grid. This parameter is valid with IxTclNetwork.
            DEFAULT
                None
        Constants Available: ENTRY_POINT_ADDRESS_CMD
        Supported:IxNetwork
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ENTRY_POINT_ADDRESS_CMD : ip})

    def emulation_ospf_topology_route_config_entry_point_prefix_length(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option entry_point_prefix_length
        Description:The prefix length of the entry point address of the OSPFv3 network range
            grid.This parameter is valid for -type grid. This parameter is valid
            with IxTclNetwork.
            DEFAULT
                None
        Constants Available: ENTRY_POINT_PREFIX_LENGTH_CMD
        Supported:IxNetwork
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ENTRY_POINT_PREFIX_LENGTH_CMD : range})

    def emulation_ospf_topology_route_config_external_connect(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_connect
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: EXTERNAL_CONNECT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_CONNECT_CMD : any})

    def emulation_ospf_topology_route_config_external_prefix_forward_addr(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_prefix_forward_addr
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: EXTERNAL_PREFIX_FORWARD_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_FORWARD_ADDR_CMD : any})

    def emulation_ospf_topology_route_config_grid_connect_session(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_connect_session
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: GRID_CONNECT_SESSION_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_CONNECT_SESSION_CMD : any})

    def emulation_ospf_topology_route_config_grid_disconnect(self):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_disconnect
        Constants Available: GRID_DISCONNECT_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_DISCONNECT_CMD : ""})

    def emulation_ospf_topology_route_config_grid_start_gmpls_link_id(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_start_gmpls_link_id
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: GRID_START_GMPLS_LINK_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_START_GMPLS_LINK_ID_CMD : any})

    def emulation_ospf_topology_route_config_grid_start_te_ip(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_start_te_ip
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: GRID_START_TE_IP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_START_TE_IP_CMD : any})

    def emulation_ospf_topology_route_config_grid_stub_per_router(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_stub_per_router
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: GRID_STUB_PER_ROUTER_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_STUB_PER_ROUTER_CMD : any})

    def emulation_ospf_topology_route_config_hello_interval(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option hello_interval
        Description:The number of seconds between Hello packets sent from an Ixia router.
            The Ixia state machine sends Hello packets at this interval for all of
            the defined interfaces. This parameter is valid for -type router, grid,
            network. This parameter is valid with IxTclProtocol and IxTclNetwork.
            DEFAULT

            10
        Constants Available: HELLO_INTERVAL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.HELLO_INTERVAL_CMD : range})

    def emulation_ospf_topology_route_config_interface_metric(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option interface_metric
        Description:This parameter is valid for OSPFv2 -type router, grid, network and
            OSPFv3 -type grid. This parameter is valid with IxTclProtocol and
            IxTclNetwork.
            DEFAULT

            10
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for OSPFv2 -type router, grid, network and
            OSPFv3 -type grid. This parameter is valid with IxTclProtocol and
            IxTclNetwork.
            DEFAULT

            10
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
            'type' | value= 'network' |
        Constants Available: INTERFACE_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.INTERFACE_METRIC_CMD : range})

    def emulation_ospf_topology_route_config_interface_mode(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option interface_mode
        Description:Available only for use when the Point-Point link type is selected
            (-link_type ppp). When this option is provided as
            ospf_and_protocol_interface (default), an unconnected protocol interface
            will be created, having the IP address provided by -neighbor_router_id
            option and the gateway will be the OSPF router's connected interface.
            This parameter is valid for OSPFv2. This parameter is valid for -type
            router, grid; -enable_advertise 0; -link_type ppp. This parameter is
            valid with IxTclProtocol and IxTclNetwork.
            DEFAULT

            ospf_and_protocol_interface
        Constants Available: INTERFACE_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.INTERFACE_MODE_CMD : opt})

    def emulation_ospf_topology_route_config_interface_mode2(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option interface_mode2
        Description:When this option is provided as ospf_and_protocol_interface (default),
            an unconnected protocol interface will be created, having the IP address
            provided by the -interface_ip_address option andthe gateway will be the
            ospf router's connected interface.This parameter is valid only for
            IxTclNetwork.
            DEFAULT

            ospf_and_protocol_interface
        Constants Available: INTERFACE_MODE2_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.INTERFACE_MODE2_CMD : opt})

    def emulation_ospf_topology_route_config_link_enable(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_enable
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LINK_ENABLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_ENABLE_CMD : bool_opt})

    def emulation_ospf_topology_route_config_link_intf_addr(self, ipv4):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_intf_addr
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LINK_INTF_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_INTF_ADDR_CMD : ipv4})

    def emulation_ospf_topology_route_config_link_metric(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_metric
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LINK_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_METRIC_CMD : range})

    def emulation_ospf_topology_route_config_link_te_admin_group(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_admin_group
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LINK_TE_ADMIN_GROUP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_ADMIN_GROUP_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_instance(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_instance
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LINK_TE_INSTANCE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_INSTANCE_CMD : range})

    def emulation_ospf_topology_route_config_link_te_link_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_link_id
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LINK_TE_LINK_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_LINK_ID_CMD : ipv4})

    def emulation_ospf_topology_route_config_link_te_local_ip_addr(self, ipv4):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_local_ip_addr
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LINK_TE_LOCAL_IP_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_LOCAL_IP_ADDR_CMD : ipv4})

    def emulation_ospf_topology_route_config_link_te_remote_ip_addr(self, ipv4):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_remote_ip_addr
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LINK_TE_REMOTE_IP_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_REMOTE_IP_ADDR_CMD : ipv4})

    def emulation_ospf_topology_route_config_link_te_type(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_type
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: LINK_TE_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_TYPE_CMD : opt})

    def emulation_ospf_topology_route_config_link_type(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_type
        Description:The link type advertised in the Router LSA interface list. This option
            is for router and grid route only.
            Valid options are:
            external-capable

            (default) A transit network.
            ppp

            A point-to-point network.
            stub

            A stub network.
            DEFAULT
                None
        Constants Available: LINK_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TYPE_CMD : opt})

    def emulation_ospf_topology_route_config_neighbor_router_id(self, ipv4):
        """
        This is the method the command: emulation_ospf_topology_route_config option neighbor_router_id
        Description:Available only for use when the Point-Point link type is selected. The
            DUT IP Interface address can be provided. This parameter is valid for
            OSPFv2. This parameter is valid for -type router, grid;
            -enable_advertise 0; -link_type ppp. This parameter is valid with
            IxTclProtocol and IxTclNetwork.
            DEFAULT
                None
        Constants Available: NEIGHBOR_ROUTER_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ipv4 --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NEIGHBOR_ROUTER_ID_CMD : ipv4})

    def emulation_ospf_topology_route_config_neighbor_router_prefix_length(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option neighbor_router_prefix_length
        Description:Available only for use when the Point-Point link type is selected. The
            prefix length of the DUT IP Interface address can be provided. This
            parameter is valid for OSPFv2. This parameter is valid for -type router,
            grid; -enable_advertise 0; -link_type ppp. This parameter is valid with
            IxTclProtocol and IxTclNetwork.
            DEFAULT

            32
        Constants Available: NEIGHBOR_ROUTER_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NEIGHBOR_ROUTER_PREFIX_LENGTH_CMD : range})

    def emulation_ospf_topology_route_config_net_dr(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option net_dr
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NET_DR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NET_DR_CMD : any})

    def emulation_ospf_topology_route_config_no_write(self, flag):
        """
        This is the method the command: emulation_ospf_topology_route_config option no_write
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
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NO_WRITE_CMD : flag})

    def emulation_ospf_topology_route_config_nssa_connect(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option nssa_connect
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_CONNECT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NSSA_CONNECT_CMD : any})

    def emulation_ospf_topology_route_config_nssa_number_of_prefix(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option nssa_number_of_prefix
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_NUMBER_OF_PREFIX_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NSSA_NUMBER_OF_PREFIX_CMD : any})

    def emulation_ospf_topology_route_config_nssa_prefix_forward_add(self):
        """
        This is the method the command: emulation_ospf_topology_route_config option nssa_prefix_forward_add
        Constants Available: NSSA_PREFIX_FORWARD_ADD_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_FORWARD_ADD_CMD : ""})

    def emulation_ospf_topology_route_config_nssa_prefix_forward_addr(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option nssa_prefix_forward_addr
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_FORWARD_ADDR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_FORWARD_ADDR_CMD : any})

    def emulation_ospf_topology_route_config_nssa_prefix_length(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option nssa_prefix_length
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_LENGTH_CMD : any})

    def emulation_ospf_topology_route_config_nssa_prefix_metric(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option nssa_prefix_metric
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_METRIC_CMD : any})

    def emulation_ospf_topology_route_config_nssa_prefix_start(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option nssa_prefix_start
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_START_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_START_CMD : any})

    def emulation_ospf_topology_route_config_nssa_prefix_step(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option nssa_prefix_step
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_STEP_CMD : any})

    def emulation_ospf_topology_route_config_nssa_prefix_type(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option nssa_prefix_type
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NSSA_PREFIX_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_TYPE_CMD : any})

    def emulation_ospf_topology_route_config_router_connect(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option router_connect
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: ROUTER_CONNECT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ROUTER_CONNECT_CMD : any})

    def emulation_ospf_topology_route_config_router_disconnect(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option router_disconnect
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: ROUTER_DISCONNECT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ROUTER_DISCONNECT_CMD : any})

    def emulation_ospf_topology_route_config_summary_connect(self):
        """
        This is the method the command: emulation_ospf_topology_route_config option summary_connect
        Constants Available: SUMMARY_CONNECT_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.SUMMARY_CONNECT_CMD : ""})

    def emulation_ospf_topology_route_config_summary_route_type(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option summary_route_type
        Description:The type of summary route to be created.This option is valid only when
            -type is summary_routes, otherwise it is ignored. This option is
            available with IxTclNetwork.
            DEFAULT

            another_area
            IxNetwork-NGPF

            DESCRIPTION

            The type of summary route to be created. This option is valid only when
            -type is summary_routes, otherwise it is ignored. This option is
            available with IxTclNetwork.
            Valid options are:
            another_area

            same_area

            DEFAULT

            another_area
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'summary_routes' |
        Constants Available: SUMMARY_ROUTE_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.SUMMARY_ROUTE_TYPE_CMD : opt})


    supportedIxiaHltapiCommands = {EmulationOspfTopologyRouteConfigConstants.AREA_ID_CMD, EmulationOspfTopologyRouteConfigConstants.BFD_REGISTRATION_CMD, EmulationOspfTopologyRouteConfigConstants.COUNT_CMD, EmulationOspfTopologyRouteConfigConstants.DEAD_INTERVAL_CMD, EmulationOspfTopologyRouteConfigConstants.ELEM_HANDLE_CMD, EmulationOspfTopologyRouteConfigConstants.ENABLE_ADVERTISE_CMD, EmulationOspfTopologyRouteConfigConstants.ENABLE_ADVERTISE_LOOPBACK_CMD, EmulationOspfTopologyRouteConfigConstants.ENTRY_POINT_ADDRESS_CMD, EmulationOspfTopologyRouteConfigConstants.ENTRY_POINT_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_ADDRESS_FAMILY_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_CONNECT_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_IP_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_NUMBER_OF_PREFIX_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_FORWARD_ADDR_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_METRIC_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_START_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_STEP_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_COL_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_CONNECT_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_CONNECT_SESSION_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_DISCONNECT_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_LINK_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_START_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_STEP_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_ROUTER_ID_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_ROUTER_ID_STEP_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_ROW_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_START_GMPLS_LINK_ID_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_START_TE_IP_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_STUB_PER_ROUTER_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_TE_CMD, EmulationOspfTopologyRouteConfigConstants.HANDLE_CMD, EmulationOspfTopologyRouteConfigConstants.HELLO_INTERVAL_CMD, EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_ADDRESS_CMD, EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_MASK_CMD, EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_OPTIONS_CMD, EmulationOspfTopologyRouteConfigConstants.INTERFACE_METRIC_CMD, EmulationOspfTopologyRouteConfigConstants.INTERFACE_MODE_CMD, EmulationOspfTopologyRouteConfigConstants.INTERFACE_MODE2_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_ENABLE_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_INTF_ADDR_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_METRIC_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_ADMIN_GROUP_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_INSTANCE_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_LINK_ID_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_LOCAL_IP_ADDR_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_MAX_BW_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_MAX_RESV_BW_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_METRIC_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_REMOTE_IP_ADDR_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY0_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY1_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY2_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY3_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY4_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY5_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY6_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY7_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.MODE_CMD, EmulationOspfTopologyRouteConfigConstants.NEIGHBOR_ROUTER_ID_CMD, EmulationOspfTopologyRouteConfigConstants.NEIGHBOR_ROUTER_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.NET_DR_CMD, EmulationOspfTopologyRouteConfigConstants.NET_IP_CMD, EmulationOspfTopologyRouteConfigConstants.NET_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.NET_PREFIX_OPTIONS_CMD, EmulationOspfTopologyRouteConfigConstants.NO_WRITE_CMD, EmulationOspfTopologyRouteConfigConstants.NSSA_CONNECT_CMD, EmulationOspfTopologyRouteConfigConstants.NSSA_NUMBER_OF_PREFIX_CMD, EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_FORWARD_ADD_CMD, EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_FORWARD_ADDR_CMD, EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_METRIC_CMD, EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_START_CMD, EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_STEP_CMD, EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_ABR_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_ASBR_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_CONNECT_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_DISCONNECT_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_ID_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_TE_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_VIRTUAL_LINK_ENDPT_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_WCR_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_ADDRESS_FAMILY_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_CONNECT_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_IP_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_NUMBER_OF_PREFIX_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_METRIC_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_START_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_STEP_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_ROUTE_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.TYPE_CMD}
