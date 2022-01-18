from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfConfigApi import EmulationOspfConfigApi, EmulationOspfConfigConstants

"""
    This is the API class for the command: emulation_ospf_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentEmulationOspfConfigApi(EmulationOspfConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentEmulationOspfConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_config
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfConfigConstants.EMULATION_OSPF_CONFIG_API)
        assert isinstance(api, EmulationOspfConfigApi)
        api.emulation_ospf_config(dummyDict)
    """
    def emulation_ospf_config(self, argdictionary):
        return super(SpirentEmulationOspfConfigApi, self).emulation_ospf_config(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_config_area_id_as_number(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_area_id_as_number_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_area_id_type(self, opt):
        return self.logger.log_unimplemented_method()

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

    def emulation_ospf_config_bfd_registration(self, bool_opt):
        return self.logger.log_unimplemented_method()

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

    def emulation_ospf_config_external_attribute(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_external_capabilities(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_flood_lsupdates_per_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_hello_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_ignore_db_desc_mtu(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_inter_flood_lsupdate_burst_gap(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_interface_handle(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_intf_ipv6_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_intf_ipv6_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_intf_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_ipv6_gateway_ip(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_ipv6_gateway_ip_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_link_metric(self, range):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_lsa_refresh_time(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_lsa_retransmit_time(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_mac_address_init(self, mac):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_mac_address_step(self, mac):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_max_ls_updates_per_burst(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_max_mtu(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_multicast_capability(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_no_write(self, flag):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_nssa_capability(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_oob_resync_breakout(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_opaque_lsa_forwarded(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_ospfv3_lsa_flood_rate_control(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_override_existence_check(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_override_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_port_handle(self, any):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_protocol_name(self, alpha):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_rate_control_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_reset(self, any):
        return self.logger.log_unimplemented_method()

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

    def emulation_ospf_config_router_interface_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_type_of_service_routing(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_unused(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_v6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_validate_received_mtu(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_vlan(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_config_vlan_id_step(self, range):
        return self.logger.log_unimplemented_method()


    supportedSpirentHltapiCommands = {EmulationOspfConfigConstants.AREA_ID_CMD, EmulationOspfConfigConstants.AREA_ID_STEP_CMD, EmulationOspfConfigConstants.AREA_TYPE_CMD, EmulationOspfConfigConstants.AUTHENTICATION_MODE_CMD, EmulationOspfConfigConstants.COUNT_CMD, EmulationOspfConfigConstants.DEAD_INTERVAL_CMD, EmulationOspfConfigConstants.DEMAND_CIRCUIT_CMD, EmulationOspfConfigConstants.ENABLE_SUPPORT_RFC_5838_CMD, EmulationOspfConfigConstants.GET_NEXT_SESSION_MODE_CMD, EmulationOspfConfigConstants.GRACE_PERIOD_CMD, EmulationOspfConfigConstants.GRACEFUL_RESTART_ENABLE_CMD, EmulationOspfConfigConstants.GRACEFUL_RESTART_HELPER_MODE_ENABLE_CMD, EmulationOspfConfigConstants.GRACEFUL_RESTART_RESTARTING_MODE_ENABLE_CMD, EmulationOspfConfigConstants.GRE_CHECKSUM_CMD, EmulationOspfConfigConstants.GRE_LOCAL_IP_CMD, EmulationOspfConfigConstants.GRE_REMOTE_IP_CMD, EmulationOspfConfigConstants.GRE_TUNNEL_CMD, EmulationOspfConfigConstants.HANDLE_CMD, EmulationOspfConfigConstants.HELLO_INTERVAL_CMD, EmulationOspfConfigConstants.HOST_ROUTE_CMD, EmulationOspfConfigConstants.INSTANCE_ID_CMD, EmulationOspfConfigConstants.INSTANCE_ID_STEP_CMD, EmulationOspfConfigConstants.INT_MSG_EXCHANGE_CMD, EmulationOspfConfigConstants.INTERFACE_COST_CMD, EmulationOspfConfigConstants.INTF_IP_ADDR_CMD, EmulationOspfConfigConstants.INTF_IP_ADDR_STEP_CMD, EmulationOspfConfigConstants.INTF_IPV6_PREFIX_LENGTH_CMD, EmulationOspfConfigConstants.LOOPBACK_IP_ADDR_CMD, EmulationOspfConfigConstants.LOOPBACK_IP_ADDR_STEP_CMD, EmulationOspfConfigConstants.LSA_DISCARD_MODE_CMD, EmulationOspfConfigConstants.LSA_RETRANSMIT_DELAY_CMD, EmulationOspfConfigConstants.MAX_LSAS_PER_PKT_CMD, EmulationOspfConfigConstants.MD5_KEY_CMD, EmulationOspfConfigConstants.MD5_KEY_ID_CMD, EmulationOspfConfigConstants.MODE_CMD, EmulationOspfConfigConstants.MTU_CMD, EmulationOspfConfigConstants.NEIGHBOR_DR_ELIGIBILITY_CMD, EmulationOspfConfigConstants.NEIGHBOR_INTF_IP_ADDR_CMD, EmulationOspfConfigConstants.NEIGHBOR_INTF_IP_ADDR_STEP_CMD, EmulationOspfConfigConstants.NEIGHBOR_ROUTER_ID_CMD, EmulationOspfConfigConstants.NEIGHBOR_ROUTER_ID_STEP_CMD, EmulationOspfConfigConstants.NETWORK_TYPE_CMD, EmulationOspfConfigConstants.NUMBER_OF_RESTARTS_CMD, EmulationOspfConfigConstants.OPTION_BITS_CMD, EmulationOspfConfigConstants.PASSWORD_CMD, EmulationOspfConfigConstants.POLL_INTERVAL_CMD, EmulationOspfConfigConstants.RESTART_DOWN_TIME_CMD, EmulationOspfConfigConstants.RESTART_REASON_CMD, EmulationOspfConfigConstants.RESTART_START_TIME_CMD, EmulationOspfConfigConstants.RESTART_UP_TIME_CMD, EmulationOspfConfigConstants.ROUTER_ID_CMD, EmulationOspfConfigConstants.ROUTER_ID_STEP_CMD, EmulationOspfConfigConstants.ROUTER_PRIORITY_CMD, EmulationOspfConfigConstants.SESSION_TYPE_CMD, EmulationOspfConfigConstants.STRICT_LSA_CHECKING_CMD, EmulationOspfConfigConstants.SUPPORT_REASON_SW_RELOAD_OR_UPGRADE_CMD, EmulationOspfConfigConstants.SUPPORT_REASON_SW_RESTART_CMD, EmulationOspfConfigConstants.SUPPORT_REASON_SWITCH_TO_REDUNDANT_PROCESSOR_CONTROL_CMD, EmulationOspfConfigConstants.SUPPORT_REASON_UNKNOWN_CMD, EmulationOspfConfigConstants.TE_ADMIN_GROUP_CMD, EmulationOspfConfigConstants.TE_ENABLE_CMD, EmulationOspfConfigConstants.TE_MAX_BW_CMD, EmulationOspfConfigConstants.TE_MAX_RESV_BW_CMD, EmulationOspfConfigConstants.TE_METRIC_CMD, EmulationOspfConfigConstants.TE_ROUTER_ID_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY0_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY1_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY2_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY3_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY4_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY5_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY6_CMD, EmulationOspfConfigConstants.TE_UNRESV_BW_PRIORITY7_CMD, EmulationOspfConfigConstants.TRANSMIT_DELAY_CMD, EmulationOspfConfigConstants.VCI_CMD, EmulationOspfConfigConstants.VCI_STEP_CMD, EmulationOspfConfigConstants.VLAN_CFI_CMD, EmulationOspfConfigConstants.VLAN_ID_CMD, EmulationOspfConfigConstants.VLAN_ID_MODE_CMD, EmulationOspfConfigConstants.VLAN_USER_PRIORITY_CMD, EmulationOspfConfigConstants.VPI_CMD, EmulationOspfConfigConstants.VPI_STEP_CMD}
