from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import InterfaceConfigApi, InterfaceConfigConstants

"""
    This is the API class for the command: interface_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentInterfaceConfigApi(InterfaceConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentInterfaceConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: interface_config
    use this by passing in a dict() of all the commands

        api = device.getApi(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        api.interface_config(dummyDict)
    """
    def interface_config(self, argdictionary):
        return super(SpirentInterfaceConfigApi, self).interface_config(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def interface_config_additional_fcoe_stat_1(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_additional_fcoe_stat_2(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_addresses_per_svlan(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_addresses_per_vci(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_addresses_per_vlan(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_addresses_per_vpi(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_arp(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_arp_on_linkup(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_arp_refresh_interval(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_arp_req_retries(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_arp_req_timer(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_enable_coset(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_enable_pattern_matching(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_encapsulation(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_filler_cell(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_interface_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_packet_decode_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_atm_reassembly_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_auto_detect_instrumentation_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_bad_blocks_number(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_bert_configuration(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_bert_error_insertion(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_check_gateway_exists(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_connected_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_connected_to_handle(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_data_integrity(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_data_center_shared_stats(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_flow_control(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_loopback(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_ndp(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_rs_fec(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_enable_rs_fec_statistics(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_attempt_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_attempt_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_attempt_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_attempt_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_diconnect_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_disconnect_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_disconnect_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ethernet_disconnect_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_credit_starvation_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_fixed_delay_value(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_force_errors(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_max_delay_for_random_value(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_min_delay_for_random_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_no_rrdy_after(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_rrdy_response_delays(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_tx_ignore_available_credits(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fc_tx_ignore_rx_link_faults(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fcoe_flow_control_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fcoe_priority_group_size(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_fcoe_priority_groups(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_flow_control_directed_addr(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_gateway_incr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_gateway_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def interface_config_good_blocks_number(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_checksum_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_dst_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_dst_ip_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ip_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ip_addr_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ip_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ipv6_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ipv6_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_ipv6_prefix_length(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_key_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_key_in(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_key_out(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_gre_seq_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ieee_media_defaults(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_integrity_signature(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_integrity_signature_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_intf_ip_addr_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_attempt_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_attempt_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_attempt_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_attempt_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_diconnect_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_disconnect_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_disconnect_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_disconnect_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_manual_gateway_mac(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_manual_gateway_mac_step(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_re_send_arp_on_link_up(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_resolve_gateway(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_send_arp_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_send_arp_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_send_arp_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv4_send_arp_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_attempt_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_attempt_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_attempt_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_attempt_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_attempt_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_disconnect_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_ns_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_ns_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_ns_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_ns_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_autoconfiguration_send_rs_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_diconnect_enabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_disconnect_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_disconnect_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_disconnect_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_gateway_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_intf_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_loopback_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_manual_gateway_mac(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_manual_gateway_mac_step(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_multiplier(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_re_send_ns_on_link_up(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_resolve_gateway(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_send_ns_interval(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_send_ns_max_outstanding(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_send_ns_rate(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ipv6_send_ns_scale_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_l23_config_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_laser_on(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_link_training(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_loop_continuously(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_loop_count_number(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_master_slave_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_mss(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_mtu(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ndp_send_req(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_no_write(self, flag):
        return self.logger.log_unimplemented_method()

    def interface_config_notify_mac_move(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ns_on_linkup(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_override_existence_check(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_override_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_enabled_continuous(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_lane(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_marker_fields(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_period(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_period_type(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_repeat(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pcs_sync_bits(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_128k_bin_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_encap(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split1_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split1_offset(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split1_offset_from(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split1_width(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split2_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split2_offset(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split2_offset_from(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split2_width(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split3_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split3_offset(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split3_offset_from(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_pgid_split3_width(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_ping_dst(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_port_rx_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_ipv4_address(self, ip):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_ipv4_negotiation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_ipv6_negotiation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_mpls_negotiation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_ppp_osi_negotiation(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_protocol_handle(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_protocol_name(self, name):
        return self.logger.log_unimplemented_method()

    def interface_config_pvc_incr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qinq_incr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_byte_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_packet_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_pattern_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_pattern_match(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_pattern_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_qos_stats(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_router_solicitation_retries(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_rpr_hec_seed(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_send_ping(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_send_router_solicitation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_send_sets_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_sequence_checking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_sequence_num_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_signature(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_signature_mask(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_signature_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_signature_start_offset(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_single_arp_per_gateway(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_single_ns_per_gateway(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_site_id(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_src_mac_addr_step(self, mac):
        return self.logger.log_unimplemented_method()

    def interface_config_start_error_insertion(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_atm_encap(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_interface_enable_list(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_interface_handle_list(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_ip_type(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_range_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_static_ig_vlan_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_count_per_vc(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_incr_per_vc_vlan_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_intermediate_objref(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_mac_range_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_number_of_vcs(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_skip_vlan_id_zero(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_tpid(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_vlan_priority(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_static_lan_vlan_stack_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def interface_config_target_link_layer_address(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_transmit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_tx_gap_control_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_tx_ignore_rx_link_faults(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_tx_lanes(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_type_a_ordered_sets(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_type_b_ordered_sets(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_use_vpn_parameters(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vci(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vci_count(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vci_step(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_count(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_inner(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_inner_count(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_inner_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_inner_step(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_list(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_protocol_id(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_tpid(self, opt):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_user_priority(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vlan_user_priority_step(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vpi(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vpi_count(self, range):
        return self.logger.log_unimplemented_method()

    def interface_config_vpi_step(self, range):
        return self.logger.log_unimplemented_method()


    supportedSpirentHltapiCommands = {InterfaceConfigConstants.ARP_SEND_REQ_CMD, InterfaceConfigConstants.AUTONEGOTIATION_CMD, InterfaceConfigConstants.CHECK_OPPOSITE_IP_VERSION_CMD, InterfaceConfigConstants.CLOCKSOURCE_CMD, InterfaceConfigConstants.DUPLEX_CMD, InterfaceConfigConstants.FCOE_SUPPORT_DATA_CENTER_MODE_CMD, InterfaceConfigConstants.FRAMING_CMD, InterfaceConfigConstants.GATEWAY_CMD, InterfaceConfigConstants.IGNORE_LINK_CMD, InterfaceConfigConstants.INTERFACE_HANDLE_CMD, InterfaceConfigConstants.INTERNAL_PPM_ADJUST_CMD, InterfaceConfigConstants.INTF_IP_ADDR_CMD, InterfaceConfigConstants.INTF_MODE_CMD, InterfaceConfigConstants.INTRINSIC_LATENCY_ADJUSTMENT_CMD, InterfaceConfigConstants.IPV6_GATEWAY_CMD, InterfaceConfigConstants.IPV6_INTF_ADDR_CMD, InterfaceConfigConstants.IPV6_PREFIX_LENGTH_CMD, InterfaceConfigConstants.MODE_CMD, InterfaceConfigConstants.NETMASK_CMD, InterfaceConfigConstants.OP_MODE_CMD, InterfaceConfigConstants.PHY_MODE_CMD, InterfaceConfigConstants.PORT_HANDLE_CMD, InterfaceConfigConstants.RX_C2_CMD, InterfaceConfigConstants.RX_FCS_CMD, InterfaceConfigConstants.RX_SCRAMBLING_CMD, InterfaceConfigConstants.SPEED_CMD, InterfaceConfigConstants.SRC_MAC_ADDR_CMD, InterfaceConfigConstants.STATIC_ATM_HEADER_ENCAPSULATION_CMD, InterfaceConfigConstants.STATIC_ATM_RANGE_COUNT_CMD, InterfaceConfigConstants.STATIC_DLCI_COUNT_MODE_CMD, InterfaceConfigConstants.STATIC_DLCI_REPEAT_COUNT_CMD, InterfaceConfigConstants.STATIC_DLCI_VALUE_CMD, InterfaceConfigConstants.STATIC_DLCI_VALUE_STEP_CMD, InterfaceConfigConstants.STATIC_ENABLE_CMD, InterfaceConfigConstants.STATIC_FR_RANGE_COUNT_CMD, InterfaceConfigConstants.STATIC_INDIRECT_CMD, InterfaceConfigConstants.STATIC_INTF_HANDLE_CMD, InterfaceConfigConstants.STATIC_IP_DST_ADDR_CMD, InterfaceConfigConstants.STATIC_IP_DST_COUNT_CMD, InterfaceConfigConstants.STATIC_IP_DST_COUNT_STEP_CMD, InterfaceConfigConstants.STATIC_IP_DST_INCREMENT_CMD, InterfaceConfigConstants.STATIC_IP_DST_INCREMENT_STEP_CMD, InterfaceConfigConstants.STATIC_IP_DST_PREFIX_LEN_CMD, InterfaceConfigConstants.STATIC_IP_DST_PREFIX_LEN_STEP_CMD, InterfaceConfigConstants.STATIC_IP_DST_RANGE_STEP_CMD, InterfaceConfigConstants.STATIC_IP_RANGE_COUNT_CMD, InterfaceConfigConstants.STATIC_L3_PROTOCOL_CMD, InterfaceConfigConstants.STATIC_LAN_RANGE_COUNT_CMD, InterfaceConfigConstants.STATIC_MAC_DST_CMD, InterfaceConfigConstants.STATIC_MAC_DST_COUNT_CMD, InterfaceConfigConstants.STATIC_MAC_DST_COUNT_STEP_CMD, InterfaceConfigConstants.STATIC_MAC_DST_MODE_CMD, InterfaceConfigConstants.STATIC_MAC_DST_STEP_CMD, InterfaceConfigConstants.STATIC_PVC_COUNT_CMD, InterfaceConfigConstants.STATIC_PVC_COUNT_STEP_CMD, InterfaceConfigConstants.STATIC_RANGE_PER_SPOKE_CMD, InterfaceConfigConstants.STATIC_SITE_ID_CMD, InterfaceConfigConstants.STATIC_SITE_ID_ENABLE_CMD, InterfaceConfigConstants.STATIC_SITE_ID_STEP_CMD, InterfaceConfigConstants.STATIC_VCI_CMD, InterfaceConfigConstants.STATIC_VCI_INCREMENT_CMD, InterfaceConfigConstants.STATIC_VCI_INCREMENT_STEP_CMD, InterfaceConfigConstants.STATIC_VCI_STEP_CMD, InterfaceConfigConstants.STATIC_VLAN_ENABLE_CMD, InterfaceConfigConstants.STATIC_VLAN_ID_CMD, InterfaceConfigConstants.STATIC_VLAN_ID_MODE_CMD, InterfaceConfigConstants.STATIC_VLAN_ID_STEP_CMD, InterfaceConfigConstants.STATIC_VPI_CMD, InterfaceConfigConstants.STATIC_VPI_INCREMENT_CMD, InterfaceConfigConstants.STATIC_VPI_INCREMENT_STEP_CMD, InterfaceConfigConstants.STATIC_VPI_STEP_CMD, InterfaceConfigConstants.TRANSMIT_CLOCK_SOURCE_CMD, InterfaceConfigConstants.TX_C2_CMD, InterfaceConfigConstants.TX_FCS_CMD, InterfaceConfigConstants.TX_RX_SYNC_STATS_ENABLE_CMD, InterfaceConfigConstants.TX_RX_SYNC_STATS_INTERVAL_CMD, InterfaceConfigConstants.TX_SCRAMBLING_CMD, InterfaceConfigConstants.VLAN_CMD}
