from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfNetworkGroupConfigApi import EmulationOspfNetworkGroupConfigApi, EmulationOspfNetworkGroupConfigConstants

"""
    This is the API class for the command: emulation_ospf_network_group_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentEmulationOspfNetworkGroupConfigApi(EmulationOspfNetworkGroupConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentEmulationOspfNetworkGroupConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_network_group_config
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfNetworkGroupConfigConstants.EMULATION_OSPF_NETWORK_GROUP_CONFIG_API)
        assert isinstance(api, EmulationOspfNetworkGroupConfigApi)
        api.emulation_ospf_network_group_config(dummyDict)
    """
    def emulation_ospf_network_group_config(self, argdictionary):
        return super(SpirentEmulationOspfNetworkGroupConfigApi, self).emulation_ospf_network_group_config(argdictionary, self.supportedSpirentHltapiCommands)

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

    def emulation_ospf_network_group_config_grid_include_emulated_device(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_grid_link_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

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

    def emulation_ospf_network_group_config_link_te_administrator_group(self, numeric):
        return self.logger.log_unimplemented_method()

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

    def emulation_ospf_network_group_config_router_active(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_network_group_config_router_id(self, ip):
        return self.logger.log_unimplemented_method()

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


    supportedSpirentHltapiCommands = {EmulationOspfNetworkGroupConfigConstants.GRID_COL_CMD, EmulationOspfNetworkGroupConfigConstants.GRID_ROW_CMD, EmulationOspfNetworkGroupConfigConstants.HANDLE_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_MAX_BW_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_MAX_RESV_BW_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_METRIC_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY0_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY1_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY2_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY3_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY4_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY5_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY6_CMD, EmulationOspfNetworkGroupConfigConstants.LINK_TE_UNRESV_BW_PRIORITY7_CMD, EmulationOspfNetworkGroupConfigConstants.MODE_CMD, EmulationOspfNetworkGroupConfigConstants.ROUTER_ABR_CMD, EmulationOspfNetworkGroupConfigConstants.ROUTER_ASBR_CMD, EmulationOspfNetworkGroupConfigConstants.ROUTER_ID_STEP_CMD, EmulationOspfNetworkGroupConfigConstants.TYPE_CMD}
