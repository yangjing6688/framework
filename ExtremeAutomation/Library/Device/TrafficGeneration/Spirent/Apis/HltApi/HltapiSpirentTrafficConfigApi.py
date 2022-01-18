from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigApi, TrafficConfigConstants

"""
    This is the API class for the command: traffic_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentTrafficConfigApi(TrafficConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentTrafficConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_config
    use this by passing in a dict() of all the commands

        api = device.getApi(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        api.traffic_config(dummyDict)
    """
    def traffic_config(self, argdictionary):
        return super(SpirentTrafficConfigApi, self).traffic_config(argdictionary, self.supportedSpirentHltapiCommands, self.addedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_config_adjust_rate(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_allow_self_destined(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_dst_hw_step(self, mac):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_dst_hw_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_address_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_hw_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_operation_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_operation_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_addr_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_protocol_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_src_hw_step(self, mac):
        return self.logger.log_unimplemented_method()

    def traffic_config_arp_src_hw_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_data_item_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_mask_select(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_mask_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vci_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_data_item_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_mask_select(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_mask_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_counter_vpi_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_aal5error(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_cell_loss_priority(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_cpcs_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_enable_auto_vpi_vci(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_enable_cl(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_enable_cpcs_length(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_encapsulation(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_generic_flow_ctrl(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_header_hec_errors(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_atm_range_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_becn(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_circuit_endpoint_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_circuit_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_convert_to_raw(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_custom_offset(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_custom_values(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_pattern(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_pattern_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_tos(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_tos_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_tos_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_data_tos_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_destination_filter(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_boot_filename(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_boot_filename_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_hw_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_client_ip_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_flags(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_flags_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_flags_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hops_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_len_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_hw_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_magic_cookie_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_operation_code(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_operation_code_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_operation_code_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_option(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_option_data(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_relay_agent_ip_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_seconds_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_host_name(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_host_name_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_server_ip_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_transaction_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_dhcp_your_ip_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_discard_eligible(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_core_enable(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_core_value(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_count_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_extended_address0(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_extended_address1(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_extended_address2(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_extended_address3(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_mask_select(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_mask_value(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_repeat_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_size(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_dlci_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_duration(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_dynamic_update_fields(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_custom_field_offset(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_custom_offset(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_custom_width(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_tracking(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_egress_tracking_encap(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_dst_vlan_protocol_tag_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_dst_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_dst_handle_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_rcvr_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_rcvr_host_index(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_rcvr_mcast_index(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_multicast_rcvr_port_index(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_override_ppp_ip_addr(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_intf_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_intf_start(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_port_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_dst_port_start(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_handle(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_intf_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_intf_start(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_port_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_scalable_src_port_start(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_emulation_src_vlan_protocol_tag_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_auto_detect_instrumentation(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_ce_to_pe_traffic(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_data_integrity(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_dynamic_mpls_labels(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_override_value(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_pgid(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_test_objective(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_time_stamp(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf1(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf2(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf3(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf4(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_enable_udf5(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_endpointset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_enforce_min_gap(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value(self, value):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value_step(self, hexdefault0x01):
        return self.logger.log_unimplemented_method()

    def traffic_config_ethernet_value_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_fcs_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_fecn(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_activeFieldChoice(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_auto(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_countValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_fieldValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_fullMesh(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_linked(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_linked_to(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_optionalEnabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_singleValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_startValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_stepValue(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_trackingEnabled(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_valueList(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_field_valueType(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_rate_distribution_port(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_rate_distribution_stream(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_sequencing(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_sequencing_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_sequencing_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size(self, size):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_distribution(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_gauss(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_imix(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_max(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_min(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_frame_size_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_dest_mac_retry_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_dest_mac_retry_delay(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_display_mpls_current_label_value(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_dest_mac_retry(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_mac_change_on_fly(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_min_frame_size(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_staggered_transmit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_enable_stream_ordering(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_frame_ordering(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_large_error_threshhold(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_max_traffic_generation_queries(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_mpls_label_learning_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_peak_loading_replication_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_refresh_learned_info_before_apply(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_stream_control(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_stream_control_iterations(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_use_tx_rx_sync(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_global_wait_time(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_enable_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_enable_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_enable_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_enable_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_key_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved0_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_reserved1_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_enable_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_enable_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_seq_number_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_valid_checksum_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_gre_version_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_header_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_hosts_per_net(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_checksum_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_code_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_code_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_code_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_code_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_max_response_delay_ms_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_interval_code_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_robustness_var_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_s_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_s_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mc_query_v2_s_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_m_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_m_bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_m_bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_o_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_o_bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_mobile_pam_o_bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_multicast_address_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_o_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_o_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_o_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_r_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_r_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_r_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_s_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_s_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_nam_s_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_h_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_h_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_h_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_hop_limit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_m_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_m_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_m_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_o_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_o_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_o_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_reachable_time_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_retransmit_timer_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_ram_router_lifetime_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_ndp_rm_dest_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_param_problem_message_pointer_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_pkt_too_big_mtu_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_seq_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_seq_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_seq_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_seq_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_target_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_type_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_icmp_unused_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_aux_data_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_data_v3r_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_group_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_length_v3r_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_max_response_time_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_max_response_time_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_max_response_time_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_max_response_time_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_msg_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_multicast_src_count(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_multicast_src_mode(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_multicast_src_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_multicast_src_tracking(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qqic_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qqic_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qqic_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qqic_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qrv_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qrv_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qrv_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_qrv_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_record_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_record_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3q_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r1_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_reserved_v3r2_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_s_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_s_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_unused(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_unused_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_unused_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_unused_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_igmp_unused_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_indirect(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_addr(self, ipv4):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_step(self, ipv4):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ip_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_mask(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_flow_label_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_more_flag(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_more_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_more_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_frag_offset_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_hop_limit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_mask(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_ipv6_traffic_class_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_inner_protocol_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_integrity_signature(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_integrity_signature_offset(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_inter_frame_gap(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_inter_frame_gap_unit(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_intf_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_bit_flags(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_checksum_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cost(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cost_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cost_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cu_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cu_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cu_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_cu_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_delay(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_delay_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_delay_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_dscp_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_dscp_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_dst_prefix_len(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_last_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_last_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_offset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_offset_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_offset_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_offset_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_fragment_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_hdr_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_hdr_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_hdr_length_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_hdr_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_length_override(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_length_override_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_length_override_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_opt_loose_routing(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_opt_security(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_opt_strict_routing(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_opt_timestamp(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_precedence_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_precedence_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_precedence_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_precedence_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_protocol_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_protocol_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_protocol_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_protocol_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reliability(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reliability_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reliability_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reserved(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reserved_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_reserved_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_throughput(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_throughput_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_throughput_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_total_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_total_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_total_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_total_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_total_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_ttl_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_ttl_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_ttl_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ip_ttl_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_md5sha1_string_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_next_header_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_padding_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_payload_len_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_reserved_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_seq_num_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_spi_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_string_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_auth_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_dst_mask(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_seq_number_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_encap_spi_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_extension_header(self, header):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_label_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_label_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_label_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_label_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_flow_version_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_id_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_more_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_more_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_offset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_offset_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_offset_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_offset_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_2bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_frag_res_8bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_by_hop_options(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_limit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_limit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_limit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_hop_limit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_next_header_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_next_header_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_next_header_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_next_header_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_dst_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr_step(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_src_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_uppper_layer_pkt_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_pseudo_zero_number_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_node_list(self, ipv6):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_res_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_routing_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_src_mask(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_traffic_class_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_traffic_class_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_traffic_class_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_ipv6_traffic_class_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu_step(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_bpdu_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_frame_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_frame_type_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_frame_type_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_index_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_high_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low_step(self, hex):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_mac_src_low_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_user_priority_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_isl_vlan_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_l3_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_lan_range_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_latency_bins(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_latency_bins_enable(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_latency_values(self, decimal):
        return self.logger.log_unimplemented_method()

    def traffic_config_loop_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_mac_dst_count_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_mac_dst_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mac_src_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_merge_destinations(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_min_gap_bytes(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_bottom_stack_bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_exp_bit_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_labels_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_labels_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_labels_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_labels_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_ttl_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_mpls_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_multiple_queues(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_name(self, name_string):
        return self.logger.log_unimplemented_method()

    def traffic_config_no_write(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_num_dst_ports(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_number_of_packets_per_stream(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_number_of_packets_tx(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_override_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_pause_control_time(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_pending_operations_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_pgid_offset(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_pgid_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_preamble_custom_size(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_preamble_size_mode(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_pt_handle(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_public_port_ip(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_pvc_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_pvc_count_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_byte_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_ipv6_flow_label(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_ipv6_traffic_class(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_type_ixn(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_qos_value_ixn_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_queue_id(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_ramp_up_percentage(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_range_per_spoke(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_byteps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_kbps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_kbyteps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_mbps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_mbyteps(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rate_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_return_to_id(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_command(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_command_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_command_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_addr_family_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_ipv4_addr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_metric_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused2_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused3_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v1_unused4_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_next_hop_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_route_tag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask_step(self, ip):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_rte_v2_subnet_mask_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_unused_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_rip_version(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_route_mesh(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_session_aware_traffic(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_signature(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_signature_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_site_id(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_site_id_enable(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_site_id_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_skip_frame_size_validation(self, flag):
        return self.logger.log_unimplemented_method()

    def traffic_config_source_filter(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_src_dest_mesh(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_stream_packing(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_column_name(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_column_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_column_size(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_column_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_table_udf_rows(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_tag_filter(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_num_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_num_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_num_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ack_num_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum_step(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_checksum_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_cwr_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_cwr_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_cwr_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_data_offset_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_dst_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_dst_port_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_dst_port_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_dst_port_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ecn_echo_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ecn_echo_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ecn_echo_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_fin_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_fin_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ns_flag(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ns_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_ns_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_psh_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_psh_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_reserved_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_reserved_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_reserved_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_reserved_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_rst_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_rst_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_seq_num_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_seq_num_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_seq_num_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_seq_num_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_src_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_src_port_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_src_port_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_src_port_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_syn_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_syn_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urg_flag_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urg_flag_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urgent_ptr_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urgent_ptr_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urgent_ptr_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_urgent_ptr_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_window_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_window_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_window_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_tcp_window_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_test_objective_value(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_track_by(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_traffic_generate(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_traffic_generator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_transmit_distribution(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tx_delay(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_tx_delay_unit(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_tx_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf1_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf2_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf3_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf4_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_cascade_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_chain_from(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_init_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_type(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_counter_up_down(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_enable_cascade(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_inner_repeat_count(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_inner_repeat_value(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_inner_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_mask_select(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_mask_val(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_mode(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_offset(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_skip_mask_bits(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_skip_zeros_and_ones(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udf5_value_list(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_checksum_value(self, hexhex):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_checksum_value_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_dst_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_dst_port_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_dst_port_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_dst_port_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_length_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_src_port_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_src_port_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_src_port_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_udp_src_port_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_use_all_ip_subnets(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_use_cp_rate(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_use_cp_size(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vci_increment(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_vci_increment_step(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_cfi_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_cfi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_cfi_step(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_cfi_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_enable(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_id_step(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id_step(self, hexdefault0x01):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_protocol_tag_id_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_user_priority_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_user_priority_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_user_priority_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_config_vlan_user_priority_tracking(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_config_vpi_increment(self):
        return self.logger.log_unimplemented_method()

    def traffic_config_vpi_increment_step(self):
        return self.logger.log_unimplemented_method()

    supportedSpirentHltapiCommands = {TrafficConfigConstants.APP_PROFILE_TYPE_CMD,
                                      TrafficConfigConstants.ARP_DST_HW_ADDR_CMD,
                                      TrafficConfigConstants.ARP_DST_HW_COUNT_CMD,
                                      TrafficConfigConstants.ARP_DST_HW_MODE_CMD,
                                      TrafficConfigConstants.ARP_OPERATION_CMD,
                                      TrafficConfigConstants.ARP_SRC_HW_ADDR_CMD,
                                      TrafficConfigConstants.ARP_SRC_HW_COUNT_CMD,
                                      TrafficConfigConstants.ARP_SRC_HW_MODE_CMD,
                                      TrafficConfigConstants.BIDIRECTIONAL_CMD,
                                      TrafficConfigConstants.BURST_LOOP_COUNT_CMD,
                                      TrafficConfigConstants.COMMAND_RESPONSE_CMD, TrafficConfigConstants.CSRC_LIST_CMD,
                                      TrafficConfigConstants.DATA_TOS_COUNT_CMD,
                                      TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_COUNT_CMD,
                                      TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_MODE_CMD,
                                      TrafficConfigConstants.DHCP_CLIENT_IP_ADDR_STEP_CMD,
                                      TrafficConfigConstants.DLCI_REPEAT_COUNT_STEP_CMD,
                                      TrafficConfigConstants.DLCI_VALUE_STEP_CMD,
                                      TrafficConfigConstants.EMULATION_DST_HANDLE_CMD,
                                      TrafficConfigConstants.EMULATION_SRC_HANDLE_CMD, TrafficConfigConstants.FCS_CMD,
                                      TrafficConfigConstants.FR_RANGE_COUNT_CMD,
                                      TrafficConfigConstants.ICMP_CHECKSUM_CMD, TrafficConfigConstants.ICMP_CODE_CMD,
                                      TrafficConfigConstants.ICMP_ID_CMD, TrafficConfigConstants.ICMP_SEQ_CMD,
                                      TrafficConfigConstants.ICMP_TYPE_CMD, TrafficConfigConstants.IGMP_GROUP_ADDR_CMD,
                                      TrafficConfigConstants.IGMP_GROUP_COUNT_CMD,
                                      TrafficConfigConstants.IGMP_GROUP_MODE_CMD,
                                      TrafficConfigConstants.IGMP_GROUP_STEP_CMD,
                                      TrafficConfigConstants.IGMP_MAX_RESPONSE_TIME_CMD,
                                      TrafficConfigConstants.IGMP_MSG_TYPE_CMD,
                                      TrafficConfigConstants.IGMP_MULTICAST_SRC_CMD,
                                      TrafficConfigConstants.IGMP_QQIC_CMD, TrafficConfigConstants.IGMP_QRV_CMD,
                                      TrafficConfigConstants.IGMP_RECORD_TYPE_CMD,
                                      TrafficConfigConstants.IGMP_S_FLAG_CMD, TrafficConfigConstants.IGMP_TYPE_CMD,
                                      TrafficConfigConstants.IGMP_VALID_CHECKSUM_CMD,
                                      TrafficConfigConstants.IGMP_VERSION_CMD,
                                      TrafficConfigConstants.INTER_BURST_GAP_CMD,
                                      TrafficConfigConstants.INTER_STREAM_GAP_CMD,
                                      TrafficConfigConstants.IP_CHECKSUM_CMD, TrafficConfigConstants.IP_CU_CMD,
                                      TrafficConfigConstants.IP_DSCP_CMD, TrafficConfigConstants.IP_DSCP_COUNT_CMD,
                                      TrafficConfigConstants.IP_DSCP_STEP_CMD, TrafficConfigConstants.IP_DST_ADDR_CMD,
                                      TrafficConfigConstants.IP_DST_COUNT_CMD,
                                      TrafficConfigConstants.IP_DST_COUNT_STEP_CMD,
                                      TrafficConfigConstants.IP_DST_INCREMENT_CMD,
                                      TrafficConfigConstants.IP_DST_INCREMENT_STEP_CMD,
                                      TrafficConfigConstants.IP_DST_MODE_CMD,
                                      TrafficConfigConstants.IP_DST_PREFIX_LEN_STEP_CMD,
                                      TrafficConfigConstants.IP_DST_RANGE_STEP_CMD,
                                      TrafficConfigConstants.IP_DST_SKIP_BROADCAST_CMD,
                                      TrafficConfigConstants.IP_DST_SKIP_MULTICAST_CMD,
                                      TrafficConfigConstants.IP_DST_STEP_CMD, TrafficConfigConstants.IP_FRAGMENT_CMD,
                                    #  TrafficConfigConstants.IP_FRAGMENT_LAST_CMD,
                                      TrafficConfigConstants.IP_FRAGMENT_OFFSET_CMD,
                                      TrafficConfigConstants.IP_HDR_LENGTH_CMD, TrafficConfigConstants.IP_ID_CMD,
                                      TrafficConfigConstants.IP_MBZ_CMD, TrafficConfigConstants.IP_PRECEDENCE_CMD,
                                      TrafficConfigConstants.IP_PROTOCOL_CMD, TrafficConfigConstants.IP_RANGE_COUNT_CMD,
                                      TrafficConfigConstants.IP_SRC_ADDR_CMD, TrafficConfigConstants.IP_SRC_COUNT_CMD,
                                      TrafficConfigConstants.IP_SRC_MODE_CMD,
                                      TrafficConfigConstants.IP_SRC_SKIP_BROADCAST_CMD,
                                      TrafficConfigConstants.IP_SRC_SKIP_MULTICAST_CMD,
                                      TrafficConfigConstants.IP_SRC_STEP_CMD, TrafficConfigConstants.IP_TOS_COUNT_CMD,
                                      TrafficConfigConstants.IP_TOS_FIELD_CMD, TrafficConfigConstants.IP_TOS_STEP_CMD,
                                      TrafficConfigConstants.IP_TTL_CMD, TrafficConfigConstants.IPV6_CHECKSUM_CMD,
                                      TrafficConfigConstants.IPV6_DST_ADDR_CMD,
                                      TrafficConfigConstants.IPV6_DST_COUNT_CMD,
                                      TrafficConfigConstants.IPV6_DST_MODE_CMD,
                                      TrafficConfigConstants.IPV6_DST_STEP_CMD,
                                      TrafficConfigConstants.IPV6_FLOW_LABEL_CMD,
                                      TrafficConfigConstants.IPV6_FRAG_ID_CMD,
                                      TrafficConfigConstants.IPV6_FRAG_MORE_FLAG_CMD,
                                      TrafficConfigConstants.IPV6_FRAG_NEXT_HEADER_CMD,
                                      TrafficConfigConstants.IPV6_FRAG_OFFSET_CMD,
                                      TrafficConfigConstants.IPV6_HOP_LIMIT_CMD, TrafficConfigConstants.IPV6_LENGTH_CMD,
                                      TrafficConfigConstants.IPV6_NEXT_HEADER_CMD,
                                      TrafficConfigConstants.IPV6_SRC_ADDR_CMD,
                                      TrafficConfigConstants.IPV6_SRC_COUNT_CMD,
                                      TrafficConfigConstants.IPV6_SRC_MODE_CMD,
                                      TrafficConfigConstants.IPV6_SRC_STEP_CMD,
                                      TrafficConfigConstants.IPV6_TRAFFIC_CLASS_CMD,
                                      TrafficConfigConstants.L2_ENCAP_CMD,
                                      TrafficConfigConstants.L3_GAUS1_AVG_CMD,
                                      TrafficConfigConstants.L3_GAUS1_HALFBW_CMD,
                                      TrafficConfigConstants.L3_GAUS1_WEIGHT_CMD,
                                      TrafficConfigConstants.L3_GAUS2_AVG_CMD,
                                      TrafficConfigConstants.L3_GAUS2_HALFBW_CMD,
                                      TrafficConfigConstants.L3_GAUS2_WEIGHT_CMD,
                                      TrafficConfigConstants.L3_GAUS3_AVG_CMD,
                                      TrafficConfigConstants.L3_GAUS3_HALFBW_CMD,
                                      TrafficConfigConstants.L3_GAUS3_WEIGHT_CMD,
                                      TrafficConfigConstants.L3_GAUS4_AVG_CMD,
                                      TrafficConfigConstants.L3_GAUS4_HALFBW_CMD,
                                      TrafficConfigConstants.L3_GAUS4_WEIGHT_CMD,
                                      TrafficConfigConstants.L3_IMIX1_RATIO_CMD,
                                      TrafficConfigConstants.L3_IMIX1_SIZE_CMD,
                                      TrafficConfigConstants.L3_IMIX2_RATIO_CMD,
                                      TrafficConfigConstants.L3_IMIX2_SIZE_CMD,
                                      TrafficConfigConstants.L3_IMIX3_RATIO_CMD,
                                      TrafficConfigConstants.L3_IMIX3_SIZE_CMD,
                                      TrafficConfigConstants.L3_IMIX4_RATIO_CMD,
                                      TrafficConfigConstants.L3_IMIX4_SIZE_CMD, TrafficConfigConstants.L3_LENGTH_CMD,
                                      TrafficConfigConstants.L3_LENGTH_MAX_CMD,
                                      TrafficConfigConstants.L3_LENGTH_MIN_CMD, TrafficConfigConstants.L3_PROTOCOL_CMD,
                                      TrafficConfigConstants.L4_PROTOCOL_CMD, TrafficConfigConstants.LENGTH_MODE_CMD,
                                      TrafficConfigConstants.MAC_DISCOVERY_GW_CMD, TrafficConfigConstants.MAC_DST_CMD,
                                      TrafficConfigConstants.MAC_DST2_CMD, TrafficConfigConstants.MAC_DST2_COUNT_CMD,
                                      TrafficConfigConstants.MAC_DST2_MODE_CMD,
                                      TrafficConfigConstants.MAC_DST2_STEP_CMD,
                                      TrafficConfigConstants.MAC_DST_COUNT_CMD, TrafficConfigConstants.MAC_DST_MASK_CMD,
                                      TrafficConfigConstants.MAC_DST_MODE_CMD, TrafficConfigConstants.MAC_DST_SEED_CMD,
                                      TrafficConfigConstants.MAC_DST_STEP_CMD, TrafficConfigConstants.MAC_SRC_CMD,
                                      TrafficConfigConstants.MAC_SRC2_CMD, TrafficConfigConstants.MAC_SRC2_COUNT_CMD,
                                      TrafficConfigConstants.MAC_SRC2_MODE_CMD,
                                      TrafficConfigConstants.MAC_SRC2_STEP_CMD,
                                      TrafficConfigConstants.MAC_SRC_COUNT_CMD, TrafficConfigConstants.MAC_SRC_MASK_CMD,
                                      TrafficConfigConstants.MAC_SRC_MODE_CMD, TrafficConfigConstants.MAC_SRC_SEED_CMD,
                                      TrafficConfigConstants.MAC_SRC_STEP_CMD, TrafficConfigConstants.MODE_CMD,
                                      TrafficConfigConstants.MPLS_LABELS_CMD, TrafficConfigConstants.PKTS_PER_BURST_CMD,
                                      TrafficConfigConstants.PORT_HANDLE_CMD, TrafficConfigConstants.PORT_HANDLE2_CMD,
                                      TrafficConfigConstants.PPP_SESSION_ID_CMD, TrafficConfigConstants.RATE_BPS_CMD,
                                      TrafficConfigConstants.RATE_FRAME_GAP_CMD,
                                      TrafficConfigConstants.RATE_PERCENT_CMD, TrafficConfigConstants.RATE_PPS_CMD,
                                      TrafficConfigConstants.RTP_CSRC_COUNT_CMD,
                                      TrafficConfigConstants.RTP_PAYLOAD_TYPE_CMD, TrafficConfigConstants.SSRC_CMD,
                                      TrafficConfigConstants.STACK_INDEX_CMD, TrafficConfigConstants.STREAM_ID_CMD,
                                      TrafficConfigConstants.TCP_ACK_FLAG_CMD, TrafficConfigConstants.TCP_ACK_NUM_CMD,
                                      TrafficConfigConstants.TCP_DST_PORT_CMD, TrafficConfigConstants.TCP_FIN_FLAG_CMD,
                                      TrafficConfigConstants.TCP_PSH_FLAG_CMD, TrafficConfigConstants.TCP_RESERVED_CMD,
                                      TrafficConfigConstants.TCP_RST_FLAG_CMD, TrafficConfigConstants.TCP_SEQ_NUM_CMD,
                                      TrafficConfigConstants.TCP_SRC_PORT_CMD, TrafficConfigConstants.TCP_SYN_FLAG_CMD,
                                      TrafficConfigConstants.TCP_URG_FLAG_CMD,
                                      TrafficConfigConstants.TCP_URGENT_PTR_CMD, TrafficConfigConstants.TCP_WINDOW_CMD,
                                      TrafficConfigConstants.TIMESTAMP_INITIAL_VALUE_CMD,
                                      TrafficConfigConstants.TRANSMIT_MODE_CMD, TrafficConfigConstants.UDP_CHECKSUM_CMD,
                                      TrafficConfigConstants.UDP_DST_PORT_CMD, TrafficConfigConstants.UDP_SRC_PORT_CMD,
                                      }
    # these are the commands that have been added in other methods.
    # it suppresses the command output.
    addedSpirentHltapiCommands = [TrafficConfigConstants.ENABLE_PGID_CMD, # << this is ignored.
                                  TrafficConfigConstants.ETHERNET_VALUE_CMD,
                                  TrafficConfigConstants.ETHERNET_TYPE_CMD, # << I don't think this has any alternative
                                  TrafficConfigConstants.FRAME_SIZE_CMD,

                                  TrafficConfigConstants.VCI_CMD, TrafficConfigConstants.VCI_COUNT_CMD,
                                  TrafficConfigConstants.VCI_STEP_CMD, TrafficConfigConstants.VLAN_CFI_CMD,
                                  TrafficConfigConstants.VLAN_ID_CMD, TrafficConfigConstants.VLAN_ID_COUNT_CMD,
                                  TrafficConfigConstants.VLAN_ID_MODE_CMD,
                                  TrafficConfigConstants.VLAN_USER_PRIORITY_CMD,
                                  TrafficConfigConstants.VPI_CMD,
                                  TrafficConfigConstants.VPI_COUNT_CMD,
                                  TrafficConfigConstants.VPI_STEP_CMD
                                  ]
