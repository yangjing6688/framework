from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficStatsApi import TrafficStatsApi, TrafficStatsConstants

"""
    This is the API class for the command: traffic_stats

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentTrafficStatsApi(TrafficStatsApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentTrafficStatsApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_stats
    use this by passing in a dict() of all the commands

        api = device.getApi(TrafficStatsConstants.TRAFFIC_STATS_API)
        api.traffic_stats(dummyDict)
    """
    def traffic_stats(self, argdictionary):
        return super(SpirentTrafficStatsApi, self).traffic_stats(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_stats_atm_counter_vci_data_item_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vci_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vci_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vpi_data_item_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vpi_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_counter_vpi_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_reassembly_enable_ip_qos(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_reassembly_enable_iptcpudp_checksum(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_atm_reassembly_encapsulation(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_csv_path(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_flow(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_listening_port(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_port(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_traffic_item(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_drill_down_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_egress_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_egress_stats_list(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_ignore_rate(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_measure_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_packet_group_id(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_previous_data(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_qos_stats(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_return_method(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_traffic_generator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_action(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23ps_drilldown(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23ps_num_results(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23ps_sorting_statistic(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23ps_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_aggregated_across_ports(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_egress_latency_bin_display(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_enumeration_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_filter_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_tracking_operator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tf_tracking_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_dead_flows_treshold(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_flow_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_show_egress_flows(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_all_flows_num_results(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_all_flows_sort_by(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_all_flows_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_dead_flows_num_results(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_dead_flows_sort_by(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_dead_flows_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_live_flows_num_results(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_live_flows_sort_by(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_live_flows_sorting_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_operator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_statistic_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_tracking_operator(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_l23tfd_tracking_value(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_port_filter(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_port_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_protocol_stack_filter(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_protocol_stack_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_statistic_filter(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_statistic_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_tracking_filter(self, any):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_tracking_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_traffic_item_filter(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_traffic_item_filter_count(self, numeric):
        return self.logger.log_unimplemented_method()

    def traffic_stats_uds_type(self, opt):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vci(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vci_count(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vci_step(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vpi(self, range):
        return self.logger.log_unimplemented_method()

    def traffic_stats_vpi_step(self, range):
        return self.logger.log_unimplemented_method()


    supportedSpirentHltapiCommands = {TrafficStatsConstants.MODE_CMD, TrafficStatsConstants.PORT_HANDLE_CMD, TrafficStatsConstants.STREAM_CMD, TrafficStatsConstants.STREAMS_CMD}
