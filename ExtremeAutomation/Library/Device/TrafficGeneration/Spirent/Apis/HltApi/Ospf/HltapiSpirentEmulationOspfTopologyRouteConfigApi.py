from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfTopologyRouteConfigApi import EmulationOspfTopologyRouteConfigApi, EmulationOspfTopologyRouteConfigConstants

"""
    This is the API class for the command: emulation_ospf_topology_route_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentEmulationOspfTopologyRouteConfigApi(EmulationOspfTopologyRouteConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentEmulationOspfTopologyRouteConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_topology_route_config
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfTopologyRouteConfigConstants.EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG_API)
        assert isinstance(api, EmulationOspfTopologyRouteConfigApi)
        api.emulation_ospf_topology_route_config(dummyDict)
    """
    def emulation_ospf_topology_route_config(self, argdictionary):
        return super(SpirentEmulationOspfTopologyRouteConfigApi, self).emulation_ospf_topology_route_config(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_topology_route_config_area_id(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_bfd_registration(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_dead_interval(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_enable_advertise_loopback(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_entry_point_address(self, ip):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_entry_point_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_external_connect(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_external_prefix_forward_addr(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_connect_session(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_disconnect(self):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_start_gmpls_link_id(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_start_te_ip(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_grid_stub_per_router(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_hello_interval(self, range):
        return self.logger.log_unimplemented_method()

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

    def emulation_ospf_topology_route_config_link_te_admin_group(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_instance(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_link_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_local_ip_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_remote_ip_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_te_type(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_link_type(self, opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_neighbor_router_id(self, ipv4):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_neighbor_router_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_net_dr(self, any):
        return self.logger.log_unimplemented_method()

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

    def emulation_ospf_topology_route_config_router_connect(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_router_disconnect(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_summary_connect(self):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_topology_route_config_summary_route_type(self, opt):
        return self.logger.log_unimplemented_method()


    supportedSpirentHltapiCommands = {EmulationOspfTopologyRouteConfigConstants.COUNT_CMD, EmulationOspfTopologyRouteConfigConstants.ELEM_HANDLE_CMD, EmulationOspfTopologyRouteConfigConstants.ENABLE_ADVERTISE_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_ADDRESS_FAMILY_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_IP_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_NUMBER_OF_PREFIX_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_METRIC_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_START_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_STEP_CMD, EmulationOspfTopologyRouteConfigConstants.EXTERNAL_PREFIX_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_COL_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_CONNECT_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_LINK_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_START_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_PREFIX_STEP_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_ROUTER_ID_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_ROUTER_ID_STEP_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_ROW_CMD, EmulationOspfTopologyRouteConfigConstants.GRID_TE_CMD, EmulationOspfTopologyRouteConfigConstants.HANDLE_CMD, EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_ADDRESS_CMD, EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_MASK_CMD, EmulationOspfTopologyRouteConfigConstants.INTERFACE_IP_OPTIONS_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_MAX_BW_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_MAX_RESV_BW_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_METRIC_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY0_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY1_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY2_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY3_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY4_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY5_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY6_CMD, EmulationOspfTopologyRouteConfigConstants.LINK_TE_UNRESV_BW_PRIORITY7_CMD, EmulationOspfTopologyRouteConfigConstants.MODE_CMD, EmulationOspfTopologyRouteConfigConstants.NET_IP_CMD, EmulationOspfTopologyRouteConfigConstants.NET_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.NET_PREFIX_OPTIONS_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_ABR_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_ASBR_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_ID_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_TE_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_VIRTUAL_LINK_ENDPT_CMD, EmulationOspfTopologyRouteConfigConstants.ROUTER_WCR_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_ADDRESS_FAMILY_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_IP_TYPE_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_NUMBER_OF_PREFIX_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_LENGTH_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_METRIC_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_START_CMD, EmulationOspfTopologyRouteConfigConstants.SUMMARY_PREFIX_STEP_CMD, EmulationOspfTopologyRouteConfigConstants.TYPE_CMD}
