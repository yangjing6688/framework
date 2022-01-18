from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: emulation_ospf_topology_route_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class EmulationOspfTopologyRouteConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(EmulationOspfTopologyRouteConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_topology_route_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationOspfTopologyRouteConfigConstants.AREA_ID_CMD] = "dummyValue1" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.BFD_REGISTRATION_CMD] = "dummyValue2" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.COUNT_CMD] = "dummyValue3" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.DEAD_INTERVAL_CMD] = "dummyValue4" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ELEM_HANDLE_CMD] = "dummyValue5" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ENABLE_ADVERTISE_CMD] = "dummyValue6" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ENABLE_ADVERTISE_LOOPBACK_CMD] = "dummyValue7" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ENTRY_POINT_ADDRESS_CMD] = "dummyValue8" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ENTRY_POINT_PREFIX_LENGTH_CMD] = "dummyValue9" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_ADDRESS_FAMILY_CMD] = EmulationOspfTopologyRouteConfigConstants.EXTERNAL_ADDRESS_FAMILY_MULTICAST # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_CONNECT_CMD] = "dummyValue11" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_IP_TYPE_CMD] = EmulationOspfTopologyRouteConfigConstants.EXTERNAL_IP_TYPE_IPV4 # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_NUMBER_OF_PREFIX_CMD] = "dummyValue13" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_FORWARD_ADDR_CMD] = "dummyValue14" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_LENGTH_CMD] = "dummyValue15" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_METRIC_CMD] = "dummyValue16" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_START_CMD] = "dummyValue17" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_STEP_CMD] = "dummyValue18" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_TYPE_CMD] = EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_TYPE_1 # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_COL_CMD] = "dummyValue20" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_CONNECT_CMD] = "dummyValue21" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_CONNECT_SESSION_CMD] = "dummyValue22" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_DISCONNECT_CMD] = "dummyValue23" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_LINK_TYPE_CMD] = EmulationOspfTopologyRouteConfigConstants.GRID_LINK_TYPE_BROADCAST # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_LENGTH_CMD] = "dummyValue25" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_START_CMD] = "dummyValue26" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_STEP_CMD] = "dummyValue27" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_ROUTER_ID_CMD] = "dummyValue28" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_ROUTER_ID_STEP_CMD] = "dummyValue29" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_ROW_CMD] = "dummyValue30" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_START_GMPLS_LINK_ID_CMD] = "dummyValue31" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_START_TE_IP_CMD] = "dummyValue32" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_STUB_PER_ROUTER_CMD] = "dummyValue33" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.GRID_TE_CMD] = "dummyValue34" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.HANDLE_CMD] = "dummyValue35" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.HELLO_INTERVAL_CMD] = "dummyValue36" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_ADDRESS_CMD] = "dummyValue37" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_MASK_CMD] = "dummyValue38" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_OPTIONS_CMD] = "dummyValue39" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.INTERFACE_METRIC_CMD] = "dummyValue40" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.INTERFACE_MODE_CMD] = EmulationOspfTopologyRouteConfigConstants.INTERFACE_MODE_OSPF_AND_PROTOCOL_INTERFACE # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.INTERFACE_MODE2_CMD] = EmulationOspfTopologyRouteConfigConstants.INTERFACE_MODE2_OSPF_AND_PROTOCOL_INTERFACE # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_ENABLE_CMD] = "dummyValue43" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_INTF_ADDR_CMD] = "dummyValue44" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_METRIC_CMD] = "dummyValue45" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_CMD] = "dummyValue46" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_ADMIN_GROUP_CMD] = "dummyValue47" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_INSTANCE_CMD] = "dummyValue48" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_LINK_ID_CMD] = "dummyValue49" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_LOCAL_IP_ADDR_CMD] = "dummyValue50" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_MAX_BW_CMD] = "dummyValue51" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_MAX_RESV_BW_CMD] = "dummyValue52" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_METRIC_CMD] = "dummyValue53" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_REMOTE_IP_ADDR_CMD] = "dummyValue54" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_TYPE_CMD] = EmulationOspfTopologyRouteConfigConstants.LINK_TE_TYPE_MULTIACCESS # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY0_CMD] = "dummyValue56" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY1_CMD] = "dummyValue57" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY2_CMD] = "dummyValue58" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY3_CMD] = "dummyValue59" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY4_CMD] = "dummyValue60" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY5_CMD] = "dummyValue61" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY6_CMD] = "dummyValue62" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY7_CMD] = "dummyValue63" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.LINK_TYPE_CMD] = EmulationOspfTopologyRouteConfigConstants.LINK_TYPE_EXTERNALCAPABLE # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.MODE_CMD] = EmulationOspfTopologyRouteConfigConstants.MODE_CREATE # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NEIGHBOR_ROUTER_ID_CMD] = "dummyValue66" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NEIGHBOR_ROUTER_PREFIX_LENGTH_CMD] = "dummyValue67" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NET_DR_CMD] = "dummyValue68" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NET_IP_CMD] = "dummyValue69" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NET_PREFIX_LENGTH_CMD] = "dummyValue70" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NET_PREFIX_OPTIONS_CMD] = "dummyValue71" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NO_WRITE_CMD] = "dummyValue72" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NSSA_CONNECT_CMD] = "dummyValue73" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NSSA_NUMBER_OF_PREFIX_CMD] = "dummyValue74" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_FORWARD_ADD_CMD] = "dummyValue75" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_FORWARD_ADDR_CMD] = "dummyValue76" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_LENGTH_CMD] = "dummyValue77" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_METRIC_CMD] = "dummyValue78" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_START_CMD] = "dummyValue79" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_STEP_CMD] = "dummyValue80" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.NSSA_PREFIX_TYPE_CMD] = "dummyValue81" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ROUTER_ABR_CMD] = "dummyValue82" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ROUTER_ASBR_CMD] = "dummyValue83" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ROUTER_CONNECT_CMD] = "dummyValue84" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ROUTER_DISCONNECT_CMD] = "dummyValue85" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ROUTER_ID_CMD] = "dummyValue86" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ROUTER_TE_CMD] = "dummyValue87" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ROUTER_VIRTUAL_LINK_ENDPT_CMD] = "dummyValue88" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.ROUTER_WCR_CMD] = "dummyValue89" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.SUMMARY_ADDRESS_FAMILY_CMD] = EmulationOspfTopologyRouteConfigConstants.SUMMARY_ADDRESS_FAMILY_MULTICAST # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.SUMMARY_CONNECT_CMD] = "dummyValue91" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.SUMMARY_IP_TYPE_CMD] = EmulationOspfTopologyRouteConfigConstants.SUMMARY_IP_TYPE_IPV4 # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.SUMMARY_NUMBER_OF_PREFIX_CMD] = "dummyValue93" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_LENGTH_CMD] = "dummyValue94" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_METRIC_CMD] = "dummyValue95" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_START_CMD] = "dummyValue96" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_STEP_CMD] = "dummyValue97" # static value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.SUMMARY_ROUTE_TYPE_CMD] = EmulationOspfTopologyRouteConfigConstants.SUMMARY_ROUTE_TYPE_ANOTHER_AREA # constant value
        dummyDict[EmulationOspfTopologyRouteConfigConstants.TYPE_CMD] = EmulationOspfTopologyRouteConfigConstants.TYPE_EXT_ROUTES # constant value

        api = device.getApi(EmulationOspfTopologyRouteConfigConstants.EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG_API)
        assert isinstance(api, EmulationOspfTopologyRouteConfigApi)
        api.emulation_ospf_topology_route_config(dummyDict)
    """
    def emulation_ospf_topology_route_config(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::emulation_ospf_topology_route_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_topology_route_config_area_id(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_bfd_registration(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_count(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option count
        Description:Number of route ranges to be configured. This parameter is valid for
            -type summary, ext_routes. This option is available with IxTclNetwork.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Number of route ranges to be configured. This parameter is valid for
            -type summary, ext_routes. This option is available with IxTclNetwork.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'summary' |
            'type' | value= 'ext_routes' |
        Constants Available: COUNT_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.COUNT_CMD : any})

    def emulation_ospf_topology_route_config_dead_interval(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_elem_handle(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option elem_handle
        Description:This option specifies on which topology element to configure the route
            options. The user must pass in this option if the 'type' is modify or
            delete.This parameter is valid with IxTclProtocol and IxTclNetwork.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This option specifies on which topology element to configure the route
            options. The user must pass in this option if the 'type' is modify or
            delete. This parameter is valid with IxTclProtocol and IxTclNetwork.
            DEFAULT
                None
        Constants Available: ELEM_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ELEM_HANDLE_CMD : any})

    def emulation_ospf_topology_route_config_enable_advertise(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option enable_advertise
        Description:Enables the advertisement of a range of OSPF routers expressed as a
            matrix of n x m routers (grid). This parameter is valid for -type
            router, grid. This parameter is valid with IxTclProtocol and IxTclNetwork.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Enables the advertisement of a range of OSPF routers expressed as a
            matrix of n x m routers (grid). This parameter is valid for -type
            router, grid. This parameter is valid with IxTclProtocol and IxTclNetwork.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: ENABLE_ADVERTISE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ENABLE_ADVERTISE_CMD : bool_opt})

    def emulation_ospf_topology_route_config_enable_advertise_loopback(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_entry_point_address(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_entry_point_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_external_address_family(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_address_family
        Description:The external route's address family, choices are unicast or multicast
            DEFAULT

            unicast
        Constants Available: EXTERNAL_ADDRESS_FAMILY_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_ADDRESS_FAMILY_CMD : opt})

    def emulation_ospf_topology_route_config_external_connect(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_external_ip_type(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_ip_type
        Description:The external route's ip type choices are ipv4 or ipv6
            DEFAULT

            ipv6
        Constants Available: EXTERNAL_IP_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_IP_TYPE_CMD : opt})

    def emulation_ospf_topology_route_config_external_number_of_prefix(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_number_of_prefix
        Description:The number of prefixes to be advertised. This option is valid only when
            -type is ext_routes, otherwise it is ignored.This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The number of prefixes to be advertised. This option is valid only when
            -type is ext_routes, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            24
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ext_routes' |
        Constants Available: EXTERNAL_NUMBER_OF_PREFIX_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_NUMBER_OF_PREFIX_CMD : range})

    def emulation_ospf_topology_route_config_external_prefix_forward_addr(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_external_prefix_length(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_prefix_length
        Description:The number of bits in the prefixes to be advertised. For example, a
            value of 24 is equivalent to a network mask of 255.255.255.0.This option
            is valid only when -type is ext_routes, otherwise it is ignored.This
            option is available with IxTclNetwork and IxTclProtocol API.(DEFAULT =
            24 | 64)
            DEFAULT

            24 | 64
            IxNetwork-NGPF

            DESCRIPTION

            The number of bits in the prefixes to be advertised. For example, a
            value of 24 is equivalent to a network mask of 255.255.255.0. This
            option is valid only when -type is ext_routes, otherwise it is ignored.
            This option is available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            24
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ext_routes' |
        Constants Available: EXTERNAL_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_LENGTH_CMD : range})

    def emulation_ospf_topology_route_config_external_prefix_metric(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_prefix_metric
        Description:The cost metric associated with the route.This option is valid only when
            -type is ext_routes, otherwise it is ignored.This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The cost metric associated with the route. This option is valid only
            when -type is ext_routes, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ext_routes' |
        Constants Available: EXTERNAL_PREFIX_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_METRIC_CMD : range})

    def emulation_ospf_topology_route_config_external_prefix_start(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_prefix_start
        Description:The IP address of the routes to be advertised.This option is valid only
            when -type is ext_routes, otherwise it is ignored.This option is
            available with IxTclNetwork and IxTclProtocol API.(DEFAULT = 0.0.0.0 | 0::0)
            DEFAULT

            0.0.0.0 | 0::0
            IxNetwork-NGPF

            DESCRIPTION

            The IP address of the routes to be advertised. This option is valid only
            when -type is ext_routes, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0.0.0.0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ext_routes' |
        Constants Available: EXTERNAL_PREFIX_START_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_START_CMD : ip})

    def emulation_ospf_topology_route_config_external_prefix_step(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_prefix_step
        Description:The increment used between generated addresses for ext_routes prefixes.
            For usage with IxNetwork this is the step between route range objects.
            This option is valid only when -type is ext_routes, otherwise it is
            ignored.This option is available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            1 | IP
            IxNetwork-NGPF

            DESCRIPTION

            The increment used between generated addresses for ext_routes prefixes.
            For usage with IxNetwork this is the step between route range objects.
            This option is valid only when -type is ext_routes, otherwise it is
            ignored. This option is available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ext_routes' |
        Constants Available: EXTERNAL_PREFIX_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_STEP_CMD : range})

    def emulation_ospf_topology_route_config_external_prefix_type(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option external_prefix_type
        Description:This option is valid only when -type is ext_routes, otherwise it is
            ignored.This option is available with IxTclNetwork and IxTclProtocol
            API.1 - (default) Outside the area.2 - Outside the area, but with
            metrics which are larger than any internal metric.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This option is valid only when -type is ext_routes, otherwise it is
            ignored. This option is available with IxTclNetwork and IxTclProtocol
            API. Valid choices are: 1 - (default) Outside the area. 2 - Outside the
            area, but with metrics which are larger than any internal metric.
            Valid options are:
            1

            2

            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'ext_routes' |
        Constants Available: EXTERNAL_PREFIX_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_TYPE_CMD : opt})

    def emulation_ospf_topology_route_config_grid_col(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_col
        Description:Defines number of columns in a grid.This option is valid only when -type
            is grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Defines number of columns in a grid. This option is valid only when
            -type is grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT

            2
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_COL_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_COL_CMD : range})

    def emulation_ospf_topology_route_config_grid_connect(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_connect
        Description:Connects a router in the grid, as specified by the row and column, to
            the session router of specified OSPF session. The format for entering
            the row and column is 'grid_connect
            DEFAULT
                None
        Constants Available: GRID_CONNECT_CMD
        Supported:IxTclNetwork and IxTclProtocol API.(DEFAULT = 1 1)
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_CONNECT_CMD : numeric})

    def emulation_ospf_topology_route_config_grid_connect_session(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_disconnect(self):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_link_type(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_link_type
        Description:This is the Link Type advertised in the Router LSA interface list.
            Choose one of: broadcast ptop_numbered ptop_unnumberedThis option is
            valid only when -type is grid, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            ptop_numbered
            IxNetwork-NGPF

            DESCRIPTION

            This is the Link Type advertised in the Router LSA interface list.
            Choose one of: broadcast ptop_numbered ptop_unnumbered This option is
            valid only when -type is grid, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            Valid options are:
            broadcast

            Not supported in ixiangpf
            ptop_numbered

            Point to point grid
            ptop_unnumbered

            Not supported in ixiangpf
            DEFAULT

            ptop_numbered
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_LINK_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_LINK_TYPE_CMD : opt})

    def emulation_ospf_topology_route_config_grid_prefix_length(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_prefix_length
        Description:The length of the mask associated with the grid_prefix_start.This option
            is valid only when -type is grid, otherwise it is ignored. This option
            is available with IxTclNetwork and IxTclProtocol API.(DEFAULT = 24 | 64)
            DEFAULT

            64
            IxNetwork-NGPF

            DESCRIPTION

            The length of the mask associated with the grid_prefix_start. This
            option is valid only when -type is grid, otherwise it is ignored. This
            option is available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            24
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_LENGTH_CMD : range})

    def emulation_ospf_topology_route_config_grid_prefix_start(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_prefix_start
        Description:The IP subnet address associated with the first router.This option is
            valid only when -type is grid, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.(DEFAULT = 0.0.0.0 | 0::0)
            DEFAULT

            0.0.0.0 | 0::0
            IxNetwork-NGPF

            DESCRIPTION

            The IP subnet address associated with the first router. This option is
            valid only when -type is grid, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0.0.0.0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_PREFIX_START_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_START_CMD : ip})

    def emulation_ospf_topology_route_config_grid_prefix_step(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_prefix_step
        Description:This is the value used to increment the subnet address by between
            successively generated routers. This option is valid only when -type is
            grid, otherwise it is ignored.This option is available with IxTclNetwork
            and IxTclProtocol API.
            DEFAULT

            0.0.0.1 | 0::1
            IxNetwork-NGPF

            DESCRIPTION

            This is the value used to increment the subnet address by between
            successively generated routers. This option is valid only when -type is
            grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0.0.0.1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_PREFIX_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_STEP_CMD : ip})

    def emulation_ospf_topology_route_config_grid_router_id(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_router_id
        Description:The first router ID of the grid.This option is valid only when -type is
            grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The first router ID of the grid. This option is valid only when -type is
            grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0.0.0.0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_ROUTER_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_ROUTER_ID_CMD : ip})

    def emulation_ospf_topology_route_config_grid_router_id_step(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_router_id_step
        Description:The increment step for the router ID in a grid.This option is valid only
            when -type is grid, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The increment step for the router ID in a grid. This option is valid
            only when -type is grid, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0.0.0.0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_ROUTER_ID_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_ROUTER_ID_STEP_CMD : ip})

    def emulation_ospf_topology_route_config_grid_row(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_row
        Description:Defines number of rows in a grid.This option is valid only when -type is
            grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Defines number of rows in a grid. This option is valid only when -type
            is grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT

            2
        Constants Available: GRID_ROW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_ROW_CMD : range})

    def emulation_ospf_topology_route_config_grid_start_gmpls_link_id(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_start_te_ip(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_stub_per_router(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_te(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option grid_te
        Description:If true (1), enable traffic engineering on the router grid. OSPFv2 only.
            This can overwrite the settings on the session router.This option is
            valid only when -type is grid, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If true (1), enable traffic engineering on the router grid. OSPFv2 only.
            This can overwrite the settings on the session router. This option is
            valid only when -type is grid, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: GRID_TE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.GRID_TE_CMD : bool_opt})

    def emulation_ospf_topology_route_config_handle(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option handle
        Description:This option represents the handle the user *must* pass to the
            'emulation_ospf_topology_route_config' procedure. This option specifies
            on which OSPF router to configure the OSPF route range. The OSPF router
            handle(s) are returned by the procedure 'emulation_ospf_config' when
            configuring OSPF routers on the Ixia interface.
            DEFAULT
                None
            IxNetwork-NGPF[M]

            DESCRIPTION

            This option represents the handle the user *must* pass to the
            'emulation_ospf_topology_route_config' procedure. This option specifies
            on which OSPF router to configure the OSPF route range. The OSPF router
            handle(s) are returned by the procedure 'emulation_ospf_config' when
            configuring OSPF routers on the Ixia interface.
            DEFAULT
                None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork[M] , IxOS/IxNetwork-FT[M]
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.HANDLE_CMD : any})

    def emulation_ospf_topology_route_config_hello_interval(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_interface_ip_address(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option interface_ip_address
        Description:For OSPFv2 only. IP address of the unconnected interface between the
            router/grid to the session router. This option is valid only when -type
            is router or grid, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            For OSPFv2 only. IP address of the unconnected interface between the
            router/grid to the session router. This option is valid only when -type
            is router or grid, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0.0.0.0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: INTERFACE_IP_ADDRESS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_ADDRESS_CMD : ip})

    def emulation_ospf_topology_route_config_interface_ip_mask(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option interface_ip_mask
        Description:For OSPFv2 only. IP mask of the un-connected interface between the
            router/grid to the session router. This option is for router and grid
            route only. This option is available with IxTclNetwork and IxTclProtocol
            API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            For OSPFv2 only. IP mask of the un-connected interface between the
            router/grid to the session router. This option is for router and grid
            route only. This option is available with IxTclNetwork and IxTclProtocol
            API.
            DEFAULT
                None
        Constants Available: INTERFACE_IP_MASK_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_MASK_CMD : ip})

    def emulation_ospf_topology_route_config_interface_ip_options(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option interface_ip_options
        Description:For OSPFv2 only. Options related to the interface. Multiple options may
            be combined using a logical or. This option is for router and grid route
            only.
            Valid options are:
            ospfOptionBitTypeOfService

            0x01
            ospfOptionBitExternalRouting

            0x02
            ospfOptionBitMulticast

            0x04
            ospfOptionBitNSSACapability

            0x08
            ospfOptionBitExternalAttributes

            0x10
            ospfOptionBitDemandCircuit

            0x20
            ospfOptionBitLSANoForward

            0x40
            ospfOptionBitUnused

            0x80
            DEFAULT
                None
        Constants Available: INTERFACE_IP_OPTIONS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_OPTIONS_CMD : any})

    def emulation_ospf_topology_route_config_interface_metric(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_interface_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_interface_mode2(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_intf_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_metric(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te
        Description:This parameter enables Traffic Engineering on the link to the virtual
            ospf network Range topology.This field is applicable only when the -type
            is grid.This option is available with IxTclNetwork.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This parameter enables Traffic Engineering on the link to the virtual
            ospf network Range topology. This field is applicable only when the
            -type is grid. This option is available with IxTclNetwork.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'grid' |
        Constants Available: LINK_TE_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_CMD : bool_opt})

    def emulation_ospf_topology_route_config_link_te_admin_group(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_instance(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_link_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_local_ip_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_max_bw(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_max_bw
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_MAX_BW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_MAX_BW_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_max_resv_bw(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_max_resv_bw
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_MAX_RESV_BW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_MAX_RESV_BW_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_metric(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_metric
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            10
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            10
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_METRIC_CMD : range})

    def emulation_ospf_topology_route_config_link_te_remote_ip_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_type(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_unresv_bw_priority0(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_unresv_bw_priority0
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY0_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY0_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_unresv_bw_priority1(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_unresv_bw_priority1
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY1_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_unresv_bw_priority2(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_unresv_bw_priority2
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY2_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_unresv_bw_priority3(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_unresv_bw_priority3
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY3_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY3_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_unresv_bw_priority4(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_unresv_bw_priority4
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY4_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY4_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_unresv_bw_priority5(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_unresv_bw_priority5
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY5_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY5_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_unresv_bw_priority6(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_unresv_bw_priority6
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY6_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY6_CMD : numeric})

    def emulation_ospf_topology_route_config_link_te_unresv_bw_priority7(self, numeric):
        """
        This is the method the command: emulation_ospf_topology_route_config option link_te_unresv_bw_priority7
        Description:This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            IxNetwork-NGPF

            DESCRIPTION

            This parameter is valid for -type router, grid. This parameter is valid
            with IxTclProtocol and IxTclNetwork.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: LINK_TE_UNRESV_BW_PRIORITY7_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY7_CMD : numeric})

    def emulation_ospf_topology_route_config_link_type(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_mode(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option mode
        Description:Mode of the procedure call. Valid options
            are:createmodifydeleteenabledisable
            DEFAULT
                None
            IxNetwork-NGPF[M]

            DESCRIPTION

            Mode of the procedure call. Valid options are: create modify delete
            enable disable
            Valid options are:
            create

            modify

            delete

            enable

            disable

            DEFAULT
                None
        Constants Available: MODE_CMD
        Supported:IxNetwork[M] , IxOS/IxNetwork-FT[M]
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.MODE_CMD : opt})

    def emulation_ospf_topology_route_config_neighbor_router_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_neighbor_router_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_net_dr(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_net_ip(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option net_ip
        Description:IP address of the network (transit link) behind the session router.This
            option is valid only when -type is network, otherwise it is ignored.This
            option is available with IxTclNetwork and IxTclProtocol API.(DEFAULT =
            0.0.0.0 | 0::0)
            DEFAULT

            0.0.0.0 | 0::0
        Constants Available: NET_IP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NET_IP_CMD : ip})

    def emulation_ospf_topology_route_config_net_prefix_length(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option net_prefix_length
        Description:IP mask of the network (transit link).This option is valid only when
            -type is network, otherwise it is ignored.This option is available with
            IxTclNetwork and IxTclProtocol API.(DEFAULT = 24 | 64)
            DEFAULT

            24 | 64
        Constants Available: NET_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NET_PREFIX_LENGTH_CMD : range})

    def emulation_ospf_topology_route_config_net_prefix_options(self, any):
        """
        This is the method the command: emulation_ospf_topology_route_config option net_prefix_options
        Description:For OSPFv3 only. An 8-bit quantity with options related to the IP
            address of the network (transit link).Multiple bits may be combined
            using a logical 'or'. This option is valid only when -type is network,
            otherwise it is ignored.This option is available with IxTclNetwork and
            IxTclProtocol API.
            Valid options are:
            ospfV3PrefixOptionPBit

            0x08--The propagate bit, which is set on
            ospfV3PrefixOptionMCBit

            0x04--The multicast capability bit, which
            ospfV3PrefixOptionLABit

            0x02--The local address capability bit,
            ospfV3PrefixOptionNUBit

            0x01--The no unicast bit, which should be
            DEFAULT
                None
        Constants Available: NET_PREFIX_OPTIONS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.NET_PREFIX_OPTIONS_CMD : any})

    def emulation_ospf_topology_route_config_no_write(self, flag):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_nssa_connect(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_nssa_number_of_prefix(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_nssa_prefix_forward_add(self):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_nssa_prefix_forward_addr(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_nssa_prefix_length(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_nssa_prefix_metric(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_nssa_prefix_start(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_nssa_prefix_step(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_nssa_prefix_type(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_router_abr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option router_abr
        Description:If true (1), set router to be an area boundary router (ABR). Correspond
            to E (external) bit in router LSA.This option is valid only when -type
            is router or grid, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If true (1), set router to be an area boundary router (ABR). Correspond
            to E (external) bit in router LSA. This option is valid only when -type
            is router or grid, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: ROUTER_ABR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ROUTER_ABR_CMD : bool_opt})

    def emulation_ospf_topology_route_config_router_asbr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option router_asbr
        Description:If true (1), set router to be an AS boundary router (ASBR). Correspond
            to B (Border) bit in router LSA.This option is valid only when -type is
            router or grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If true (1), set router to be an AS boundary router (ASBR). Correspond
            to B (Border) bit in router LSA. This option is valid only when -type is
            router or grid, otherwise it is ignored. This option is available with
            IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: ROUTER_ASBR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ROUTER_ASBR_CMD : bool_opt})

    def emulation_ospf_topology_route_config_router_connect(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_router_disconnect(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_router_id(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option router_id
        Description:The ID associated with the router.This option is valid only when -type
            is router or grid, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0.0.0.0
            IxNetwork-NGPF

            DESCRIPTION

            The ID associated with the router. This option is valid only when -type
            is router or grid, otherwise it is ignored. This option is available
            with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0.0.0.0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'router' |
            'type' | value= 'grid' |
        Constants Available: ROUTER_ID_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ROUTER_ID_CMD : ip})

    def emulation_ospf_topology_route_config_router_te(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option router_te
        Description:If true (1), enable traffic engineering. OSPFv2 only.This option is
            valid only when -type is router or grid, otherwise it is ignored. This
            option is available with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
        Constants Available: ROUTER_TE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ROUTER_TE_CMD : bool_opt})

    def emulation_ospf_topology_route_config_router_virtual_link_endpt(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option router_virtual_link_endpt
        Description:This option is supported for OSPFV3 only. Indicates that the router is
            an endpoint of one or more fully adjacent virtual links. This option is
            valid only when -type is grid, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
        Constants Available: ROUTER_VIRTUAL_LINK_ENDPT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ROUTER_VIRTUAL_LINK_ENDPT_CMD : bool_opt})

    def emulation_ospf_topology_route_config_router_wcr(self, bool_opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option router_wcr
        Description:Indicates that the router is a wild-card multicast receiver and will
            receive multicast datagrams regardless of destination.
            DEFAULT
                None
        Constants Available: ROUTER_WCR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.ROUTER_WCR_CMD : bool_opt})

    def emulation_ospf_topology_route_config_summary_address_family(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option summary_address_family
        Description:The summary route's address family, choices are unicast or multicast
            DEFAULT

            unicast
        Constants Available: SUMMARY_ADDRESS_FAMILY_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.SUMMARY_ADDRESS_FAMILY_CMD : opt})

    def emulation_ospf_topology_route_config_summary_connect(self):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_summary_ip_type(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option summary_ip_type
        Description:The summary route's ip type choices are ipv4 or ipv6
            DEFAULT

            ipv6
        Constants Available: SUMMARY_IP_TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.SUMMARY_IP_TYPE_CMD : opt})

    def emulation_ospf_topology_route_config_summary_number_of_prefix(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option summary_number_of_prefix
        Description:The number of prefixes to be advertised. This option is valid only when
            -type is summary_routes, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The number of prefixes to be advertised. This option is valid only when
            -type is summary_routes, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            24
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'summary_routes' |
        Constants Available: SUMMARY_NUMBER_OF_PREFIX_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.SUMMARY_NUMBER_OF_PREFIX_CMD : range})

    def emulation_ospf_topology_route_config_summary_prefix_length(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option summary_prefix_length
        Description:The number of bits in the prefixes to be advertised. For example, a
            value of 24 is equivalent to a network mask of 255.255.255.0.This option
            is valid only when -type is summary_routes, otherwise it is ignored.
            This option is available with IxTclNetwork and IxTclProtocol
            API.(DEFAULT = 24 | 64)
            DEFAULT

            24 | 64
            IxNetwork-NGPF

            DESCRIPTION

            The number of bits in the prefixes to be advertised. For example, a
            value of 24 is equivalent to a network mask of 255.255.255.0. This
            option is valid only when -type is summary_routes, otherwise it is
            ignored. This option is available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            24
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'summary_routes' |
        Constants Available: SUMMARY_PREFIX_LENGTH_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_LENGTH_CMD : range})

    def emulation_ospf_topology_route_config_summary_prefix_metric(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option summary_prefix_metric
        Description:The cost metric associated with the route.This option is valid only when
            -type is summary_routes, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The cost metric associated with the route. This option is valid only
            when -type is summary_routes, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT
                None
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'summary_routes' |
        Constants Available: SUMMARY_PREFIX_METRIC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_METRIC_CMD : range})

    def emulation_ospf_topology_route_config_summary_prefix_start(self, ip):
        """
        This is the method the command: emulation_ospf_topology_route_config option summary_prefix_start
        Description:The IP address of the routes to be advertised.This option is valid only
            when -type is summary_routes, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.(DEFAULT = 0.0.0.0 | 0::0)
            DEFAULT

            0.0.0.0 | 0::0
            IxNetwork-NGPF

            DESCRIPTION

            The IP address of the routes to be advertised. This option is valid only
            when -type is summary_routes, otherwise it is ignored. This option is
            available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            0.0.0.0
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'summary_routes' |
        Constants Available: SUMMARY_PREFIX_START_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        ip --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_START_CMD : ip})

    def emulation_ospf_topology_route_config_summary_prefix_step(self, range):
        """
        This is the method the command: emulation_ospf_topology_route_config option summary_prefix_step
        Description:For usage with IxNetwork this is the step between route range
            objects.For usage with IxTclProtocol and IxTclNetwork this is the
            increment used to generate multiple summary addresses for OSPFv3 only.
            This option is valid only when -type is summary_routes, otherwise it is
            ignored. This option is available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            1 | IP
            IxNetwork-NGPF

            DESCRIPTION

            For usage with IxNetwork this is the step between route range objects.
            For usage with IxTclProtocol and IxTclNetwork this is the increment used
            to generate multiple summary addresses for OSPFv3 only. This option is
            valid only when -type is summary_routes, otherwise it is ignored. This
            option is available with IxTclNetwork and IxTclProtocol API.
            DEFAULT

            1
            DEPENDENCIES

            Valid in combination with parameter(s)
            'type' | value= 'summary_routes' |
        Constants Available: SUMMARY_PREFIX_STEP_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        range --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_STEP_CMD : range})

    def emulation_ospf_topology_route_config_summary_route_type(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_type(self, opt):
        """
        This is the method the command: emulation_ospf_topology_route_config option type
        Description:The type of topology route to create. router - Individual OSPF
            router.grid - A rectangular grid of routers.network - A subnet behind
            the selected session router.summary_routes - (default) A pool of summary
            route addresses.ext_routes - (default) A pool of external route addresses.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The type of topology route to create. This option is available with
            IxTclNetwork and IxTclProtocol API.
            Valid options are:
            router

            Individual OSPF router. This value is not supported in NGPF
            grid

            A rectangular grid of routers
            network

            A subnet behind the selected session router. This value is not supported
            in NGPF
            summary_routes

            A pool of summary route addresses
            ext_routes

            A pool of external route addresses
            DEFAULT
                None
        Constants Available: TYPE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_topology_route_config({EmulationOspfTopologyRouteConfigConstants.TYPE_CMD : opt})


"""
    This is the Constants class for the command: emulation_ospf_topology_route_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationOspfTopologyRouteConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG_API = "EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG_API"

    AREA_ID_CMD = "area_id"

    BFD_REGISTRATION_CMD = "bfd_registration"

    COUNT_CMD = "count"

    DEAD_INTERVAL_CMD = "dead_interval"

    ELEM_HANDLE_CMD = "elem_handle"

    ENABLE_ADVERTISE_CMD = "enable_advertise"

    ENABLE_ADVERTISE_LOOPBACK_CMD = "enable_advertise_loopback"

    ENTRY_POINT_ADDRESS_CMD = "entry_point_address"

    ENTRY_POINT_PREFIX_LENGTH_CMD = "entry_point_prefix_length"

    EXTERNAL_ADDRESS_FAMILY_CMD = "external_address_family"
    # Constant values for EXTERNAL_ADDRESS_FAMILY_CMD
    EXTERNAL_ADDRESS_FAMILY_MULTICAST = "multicast"
    EXTERNAL_ADDRESS_FAMILY_UNICAST = "unicast"

    EXTERNAL_CONNECT_CMD = "external_connect"

    EXTERNAL_IP_TYPE_CMD = "external_ip_type"
    # Constant values for EXTERNAL_IP_TYPE_CMD
    EXTERNAL_IP_TYPE_IPV4 = "ipv4"
    EXTERNAL_IP_TYPE_IPV6 = "ipv6"

    EXTERNAL_NUMBER_OF_PREFIX_CMD = "external_number_of_prefix"

    EXTERNAL_PREFIX_FORWARD_ADDR_CMD = "external_prefix_forward_addr"

    EXTERNAL_PREFIX_LENGTH_CMD = "external_prefix_length"

    EXTERNAL_PREFIX_METRIC_CMD = "external_prefix_metric"

    EXTERNAL_PREFIX_START_CMD = "external_prefix_start"

    EXTERNAL_PREFIX_STEP_CMD = "external_prefix_step"

    EXTERNAL_PREFIX_TYPE_CMD = "external_prefix_type"
    # Constant values for EXTERNAL_PREFIX_TYPE_CMD
    EXTERNAL_PREFIX_TYPE_1 = "1"
    EXTERNAL_PREFIX_TYPE_2 = "2"

    GRID_COL_CMD = "grid_col"

    GRID_CONNECT_CMD = "grid_connect"

    GRID_CONNECT_SESSION_CMD = "grid_connect_session"

    GRID_DISCONNECT_CMD = "grid_disconnect"

    GRID_LINK_TYPE_CMD = "grid_link_type"
    # Constant values for GRID_LINK_TYPE_CMD
    GRID_LINK_TYPE_BROADCAST = "broadcast"
    GRID_LINK_TYPE_PTOP_NUMBERED = "ptop_numbered"
    GRID_LINK_TYPE_PTOP_UNNUMBERED = "ptop_unnumbered"

    GRID_PREFIX_LENGTH_CMD = "grid_prefix_length"

    GRID_PREFIX_START_CMD = "grid_prefix_start"

    GRID_PREFIX_STEP_CMD = "grid_prefix_step"

    GRID_ROUTER_ID_CMD = "grid_router_id"

    GRID_ROUTER_ID_STEP_CMD = "grid_router_id_step"

    GRID_ROW_CMD = "grid_row"

    GRID_START_GMPLS_LINK_ID_CMD = "grid_start_gmpls_link_id"

    GRID_START_TE_IP_CMD = "grid_start_te_ip"

    GRID_STUB_PER_ROUTER_CMD = "grid_stub_per_router"

    GRID_TE_CMD = "grid_te"

    HANDLE_CMD = "handle"

    HELLO_INTERVAL_CMD = "hello_interval"

    INTERFACE_IP_ADDRESS_CMD = "interface_ip_address"

    INTERFACE_IP_MASK_CMD = "interface_ip_mask"

    INTERFACE_IP_OPTIONS_CMD = "interface_ip_options"

    INTERFACE_METRIC_CMD = "interface_metric"

    INTERFACE_MODE_CMD = "interface_mode"
    # Constant values for INTERFACE_MODE_CMD
    INTERFACE_MODE_OSPF_AND_PROTOCOL_INTERFACE = "ospf_and_protocol_interface"
    INTERFACE_MODE_OSPF_INTERFACE = "ospf_interface"

    INTERFACE_MODE2_CMD = "interface_mode2"
    # Constant values for INTERFACE_MODE2_CMD
    INTERFACE_MODE2_OSPF_AND_PROTOCOL_INTERFACE = "ospf_and_protocol_interface"
    INTERFACE_MODE2_OSPF_INTERFACE = "ospf_interface"

    LINK_ENABLE_CMD = "link_enable"

    LINK_INTF_ADDR_CMD = "link_intf_addr"

    LINK_METRIC_CMD = "link_metric"

    LINK_TE_CMD = "link_te"

    LINK_TE_ADMIN_GROUP_CMD = "link_te_admin_group"

    LINK_TE_INSTANCE_CMD = "link_te_instance"

    LINK_TE_LINK_ID_CMD = "link_te_link_id"

    LINK_TE_LOCAL_IP_ADDR_CMD = "link_te_local_ip_addr"

    LINK_TE_MAX_BW_CMD = "link_te_max_bw"

    LINK_TE_MAX_RESV_BW_CMD = "link_te_max_resv_bw"

    LINK_TE_METRIC_CMD = "link_te_metric"

    LINK_TE_REMOTE_IP_ADDR_CMD = "link_te_remote_ip_addr"

    LINK_TE_TYPE_CMD = "link_te_type"
    # Constant values for LINK_TE_TYPE_CMD
    LINK_TE_TYPE_MULTIACCESS = "multiaccess"
    LINK_TE_TYPE_PTOP = "ptop"

    LINK_TE_UNRESV_BW_PRIORITY0_CMD = "link_te_unresv_bw_priority0"

    LINK_TE_UNRESV_BW_PRIORITY1_CMD = "link_te_unresv_bw_priority1"

    LINK_TE_UNRESV_BW_PRIORITY2_CMD = "link_te_unresv_bw_priority2"

    LINK_TE_UNRESV_BW_PRIORITY3_CMD = "link_te_unresv_bw_priority3"

    LINK_TE_UNRESV_BW_PRIORITY4_CMD = "link_te_unresv_bw_priority4"

    LINK_TE_UNRESV_BW_PRIORITY5_CMD = "link_te_unresv_bw_priority5"

    LINK_TE_UNRESV_BW_PRIORITY6_CMD = "link_te_unresv_bw_priority6"

    LINK_TE_UNRESV_BW_PRIORITY7_CMD = "link_te_unresv_bw_priority7"

    LINK_TYPE_CMD = "link_type"
    # Constant values for LINK_TYPE_CMD
    LINK_TYPE_EXTERNALCAPABLE = "externalcapable"
    LINK_TYPE_PPP = "ppp"
    LINK_TYPE_STUB = "stub"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CREATE = "create"
    MODE_DELETE = "delete"
    MODE_DISABLE = "disable"
    MODE_ENABLE = "enable"
    MODE_MODIFY = "modify"

    NEIGHBOR_ROUTER_ID_CMD = "neighbor_router_id"

    NEIGHBOR_ROUTER_PREFIX_LENGTH_CMD = "neighbor_router_prefix_length"

    NET_DR_CMD = "net_dr"

    NET_IP_CMD = "net_ip"

    NET_PREFIX_LENGTH_CMD = "net_prefix_length"

    NET_PREFIX_OPTIONS_CMD = "net_prefix_options"

    NO_WRITE_CMD = "no_write"

    NSSA_CONNECT_CMD = "nssa_connect"

    NSSA_NUMBER_OF_PREFIX_CMD = "nssa_number_of_prefix"

    NSSA_PREFIX_FORWARD_ADD_CMD = "nssa_prefix_forward_add"

    NSSA_PREFIX_FORWARD_ADDR_CMD = "nssa_prefix_forward_addr"

    NSSA_PREFIX_LENGTH_CMD = "nssa_prefix_length"

    NSSA_PREFIX_METRIC_CMD = "nssa_prefix_metric"

    NSSA_PREFIX_START_CMD = "nssa_prefix_start"

    NSSA_PREFIX_STEP_CMD = "nssa_prefix_step"

    NSSA_PREFIX_TYPE_CMD = "nssa_prefix_type"

    ROUTER_ABR_CMD = "router_abr"

    ROUTER_ASBR_CMD = "router_asbr"

    ROUTER_CONNECT_CMD = "router_connect"

    ROUTER_DISCONNECT_CMD = "router_disconnect"

    ROUTER_ID_CMD = "router_id"

    ROUTER_TE_CMD = "router_te"

    ROUTER_VIRTUAL_LINK_ENDPT_CMD = "router_virtual_link_endpt"

    ROUTER_WCR_CMD = "router_wcr"

    SUMMARY_ADDRESS_FAMILY_CMD = "summary_address_family"
    # Constant values for SUMMARY_ADDRESS_FAMILY_CMD
    SUMMARY_ADDRESS_FAMILY_MULTICAST = "multicast"
    SUMMARY_ADDRESS_FAMILY_UNICAST = "unicast"

    SUMMARY_CONNECT_CMD = "summary_connect"

    SUMMARY_IP_TYPE_CMD = "summary_ip_type"
    # Constant values for SUMMARY_IP_TYPE_CMD
    SUMMARY_IP_TYPE_IPV4 = "ipv4"
    SUMMARY_IP_TYPE_IPV6 = "ipv6"

    SUMMARY_NUMBER_OF_PREFIX_CMD = "summary_number_of_prefix"

    SUMMARY_PREFIX_LENGTH_CMD = "summary_prefix_length"

    SUMMARY_PREFIX_METRIC_CMD = "summary_prefix_metric"

    SUMMARY_PREFIX_START_CMD = "summary_prefix_start"

    SUMMARY_PREFIX_STEP_CMD = "summary_prefix_step"

    SUMMARY_ROUTE_TYPE_CMD = "summary_route_type"
    # Constant values for SUMMARY_ROUTE_TYPE_CMD
    SUMMARY_ROUTE_TYPE_ANOTHER_AREA = "another_area"
    SUMMARY_ROUTE_TYPE_SAME_AREA = "same_area"

    TYPE_CMD = "type"
    # Constant values for TYPE_CMD
    TYPE_EXT_ROUTES = "ext_routes"
    TYPE_GRID = "grid"
    TYPE_NETWORK = "network"
    TYPE_ROUTER = "router"
    TYPE_SUMMARY_ROUTES = "summary_routes"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -area_id
    -bfd_registration
    -count
    -dead_interval
    -elem_handle
    -enable_advertise
    -enable_advertise_loopback
    -entry_point_address
    -entry_point_prefix_length
    -external_address_family
    -external_connect
    -external_ip_type
    -external_number_of_prefix
    -external_prefix_forward_addr
    -external_prefix_length
    -external_prefix_metric
    -external_prefix_start
    -external_prefix_step
    -external_prefix_type
    -grid_col
    -grid_connect
    -grid_connect_session
    -grid_disconnect
    -grid_link_type
    -grid_prefix_length
    -grid_prefix_start
    -grid_prefix_step
    -grid_router_id
    -grid_router_id_step
    -grid_row
    -grid_start_gmpls_link_id
    -grid_start_te_ip
    -grid_stub_per_router
    -grid_te
    -handle
    -hello_interval
    -interface_ip_address
    -interface_ip_mask
    -interface_ip_options
    -interface_metric
    -interface_mode
    -interface_mode2
    -link_enable
    -link_intf_addr
    -link_metric
    -link_te
    -link_te_admin_group
    -link_te_instance
    -link_te_link_id
    -link_te_local_ip_addr
    -link_te_max_bw
    -link_te_max_resv_bw
    -link_te_metric
    -link_te_remote_ip_addr
    -link_te_type
    -link_te_unresv_bw_priority0
    -link_te_unresv_bw_priority1
    -link_te_unresv_bw_priority2
    -link_te_unresv_bw_priority3
    -link_te_unresv_bw_priority4
    -link_te_unresv_bw_priority5
    -link_te_unresv_bw_priority6
    -link_te_unresv_bw_priority7
    -link_type
    -mode
    -neighbor_router_id
    -neighbor_router_prefix_length
    -net_dr
    -net_ip
    -net_prefix_length
    -net_prefix_options
    -no_write
    -nssa_connect
    -nssa_number_of_prefix
    -nssa_prefix_forward_add
    -nssa_prefix_forward_addr
    -nssa_prefix_length
    -nssa_prefix_metric
    -nssa_prefix_start
    -nssa_prefix_step
    -nssa_prefix_type
    -router_abr
    -router_asbr
    -router_connect
    -router_disconnect
    -router_id
    -router_te
    -router_virtual_link_endpt
    -router_wcr
    -summary_address_family
    -summary_connect
    -summary_ip_type
    -summary_number_of_prefix
    -summary_prefix_length
    -summary_prefix_metric
    -summary_prefix_start
    -summary_prefix_step
    -summary_route_type
    -type
If you want to update this file, look in the CSV
"""
