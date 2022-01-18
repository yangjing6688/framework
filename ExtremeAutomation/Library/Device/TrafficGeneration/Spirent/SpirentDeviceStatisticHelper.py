from ExtremeAutomation.Library.Device.TrafficGeneration.HltapiTrafficGeneratingDeviceStatisticHelper import \
    HltapiTrafficGeneratingDeviceStatisticHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceStatsApi import \
    InterfaceStatsApi, InterfaceStatsConstants


class SpirentDeviceStatisticHelper(HltapiTrafficGeneratingDeviceStatisticHelper):
    def __init__(self, smartbits_device):
        super(SpirentDeviceStatisticHelper, self).__init__(smartbits_device)

    def get_port_statistic_capture_filter_count(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_statistic_capture_trigger_count(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_statistic_capture_filter_rate(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_statistic_capture_trigger_rate(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_rx_collisions_count(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_port_total_collisions_count(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_port_late_collisions_count(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_port_fcs_errors_count(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.dev.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'rx_fcs_error')


#     {intf_speed 1000}
# {port_name port1}
# {mac_address _none_}
# {duplex full}
# {link 1}
# {card_name CM-1G-D12}
# {intf_type ethernet}
# {rx_ipv6_over_ipv4_frame_rate 0}
# {rx_byte_rate 0}\n{rx_prbs_fill_byte_count 0}
# {rx_max_frame_length 0}
# {rx_tcp_CheckSum_error_count 0}
# {rx_sig_count 0}
# {rx_ipv6_over_ipv4_frame_count 0}
# {rx_trigger1_count 0}
# {rx_sig_rate 0}
# {rx_trigger2_count 0}
# {rx_frames 0}
# {rx_ipv4_CheckSum_error_count 0}
# {rx_prbsbit_error_count 0}
# {rx_bytes 0}
# {rx_jumbo_frame_count 0}
# {rx_ipv4_frame_rate 0}
# {rx_trigger4_count 0}
# {rx_hw_frame_count 0}
# {rx_trigger5_count 0}
# {rx_oversize_frame_count 0}
# {rx_ipv6_frame_rate 0}
# {rx_jumbo_frame_rate 0}
# {rx_trigger6_count 0}
# {rx_pause_frame_rate 0}
# {rx_combo_trigger_count 0}
# {rx_fcs_error 0}
# {rx_frame_rate 0}
# {rx_runt_frames 0}
# {rx_mpls_frame_count 0}
# {tx_total_octet_rate 0}
# {tx_generator_sig_frame_rate 0}
# {tx_total_frame_rate 0}
# {tx_generator_l4_checksum_error_count 0}
# {tx_total_mpls_frame_count 0}
# {tx_generator_vlan_frame_count 0}
# {tx_generator_crc_error_frame_count 0}
# {tx_generator_abort_frame_rate 0}
# {tx_generator_l3_checksum_error_rate 0}
# {tx_generator_ipv4_frame_count 0}
# {tx_generator_l4_checksum_error_rate 0}
# {tx_generator_crc_error_frame_rate 0}
# {tx_generator_vlan_frame_rate 0}
# {tx_total_mpls_frame_rate 0}
# {tx_generator_jumbo_frame_count 0}
# {tx_generator_octet_count 0}
# {tx_generator_ipv6_frame_count 0}
# {tx_generator_ipv4_frame_rate 0}
# {tx_frames 0}
# {tx_generator_mpls_frame_rate 0}
# {tx_generator_oversize_frame_count 0}
# {tx_bytes 0}
# {tx_generator_jumbo_frame_rate 0}
# {tx_generator_ipv6_frame_rate 0}
# {tx_generator_octet_rate 0}
# {tx_generator_abort_frame_count 0}
# {tx_generator_l3_checksum_error_count 0}
# {tx_hw_frame_count 0}
# {tx_generator_undersize_frame_count 0}
# {tx_generator_frame_count 0}
# {tx_generator_oversize_frame_rate 0}
# {tx_generator_sig_frame_count 0}
# {tx_generator_undersize_frame_rate 0}
# {tx_generator_frame_rate 0}
# {tx_generator_mpls_frame_count 0}
# {status 1}
# %
