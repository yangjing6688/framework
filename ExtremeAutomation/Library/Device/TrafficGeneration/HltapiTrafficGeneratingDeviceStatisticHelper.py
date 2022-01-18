import abc
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceStatsApi import \
    InterfaceStatsApi, InterfaceStatsConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceStatisticHelper import \
    TrafficGeneratingDeviceStatisticHelper


class HltapiTrafficGeneratingDeviceStatisticHelper(TrafficGeneratingDeviceStatisticHelper, metaclass=abc.ABCMeta):
    def __init__(self, ixia_device):
        super(HltapiTrafficGeneratingDeviceStatisticHelper, self).__init__(ixia_device)

    def get_port_rx_collisions_count(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.dev.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'rx_collisions')

    def get_port_tx_frame_count(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.dev.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'tx_frames')

    def get_port_rx_frame_count(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.dev.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'rx_frames')

    def get_port_fcs_errors_count(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.dev.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'fcs_errors')

    def get_port_total_collisions_count(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.dev.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'total_collisions')

    def get_port_late_collisions_count(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.dev.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'late_collisions')

    # {rx {{uds2_count 0} {qos2_rate {Stat qualityOfService2 not supported}} {pkt_byte_count 0}
    # {qos0_count {Stat qualityOfService0 not supported}} {vlan_pkts_rate {Stat vlanTaggedFramesRx not supported}}
    # {sequence_errors_count 0} {qos4_count {Stat qualityOfService4 not supported}} {crc_errors_count 0}
    # {qos7_rate {Stat qualityOfService7 not supported}} {uds1_count 0} {raw_pkt_count 0}
    # {data_int_errors_count {Stat dataIntegrityErrors not supported}} {uds2_rate 0}
    # {qos4_rate {Stat qualityOfService4 not supported}} {vlan_pkts_count {Stat vlanTaggedFramesRx not supported}}
    # {data_int_errors_rate {Stat dataIntegrityErrors not supported}} {raw_pkt_rate 0} {pkt_bit_count 0}
    # {qos3_count {Stat qualityOfService3 not supported}} {qos1_rate {Stat qualityOfService1 not supported}}
    # {fragments_count 0} {collisions_count 0} {qos7_count {Stat qualityOfService7 not supported}}
    # {sequence_frames_count 0} {sequence_errors_rate 0} {collisions_rate 0} {fragments_rate 0}
    # {data_int_frames_rate {Stat dataIntegrityFrames not supported}}
    # {qos6_rate {Stat qualityOfService6 not supported}} {qos2_count {Stat qualityOfService2 not supported}}
    # {pkt_count 0} {uds1_rate 0} {dribble_errors_count 0} {qos3_rate {Stat qualityOfService3 not supported}}
    # {qos6_count {Stat qualityOfService6 not supported}}
    # {data_int_frames_count {Stat dataIntegrityFrames not supported}} {dribble_errors_rate 0}
    # {qos0_rate {Stat qualityOfService0 not supported}} {crc_errors_rate 0} {oversize_count 0} {pkt_bit_rate 0}
    # {sequence_frames_rate 0} {pkt_rate 0} {undersize_rate 0} {qos1_count {Stat qualityOfService1 not supported}}
    # {pkt_byte_rate 0} {protocol_pkt_count 0} {qos5_count {Stat qualityOfService5 not supported}} {undersize_count 0}
    # {oversize_rate 0} {qos5_rate {Stat qualityOfService5 not supported}}
    # {protocol_pkt_rate {Stat protocolServerRx not supported}}}}

    def get_port_statistic_rx_uds2_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "uds2_count", options)

    def get_port_statistic_rx_qos2_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos2_rate", options)

    def get_port_statistic_rx_pkt_byte_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "pkt_byte_count", options)

    def get_port_statistic_rx_qos0_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos0_count", options)

    def get_port_statistic_rx_vlan_pkts_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "vlan_pkts_rate", options)

    def get_port_statistic_rx_sequence_errors_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "sequence_errors_count", options)

    def get_port_statistic_rx_qos4_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos4_count", options)

    def get_port_statistic_rx_crc_errors_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "crc_errors_count", options)

    def get_port_statistic_rx_qos7_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos7_rate", options)

    def get_port_statistic_rx_uds1_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "uds1_count", options)

    def get_port_statistic_rx_raw_pkt_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "raw_pkt_count", options)

    def get_port_statistic_rx_data_int_errors_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "data_int_errors_count", options)

    def get_port_statistic_rx_uds2_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "uds2_rate", options)

    def get_port_statistic_rx_qos4_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos4_rate", options)

    def get_port_statistic_rx_vlan_pkts_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "vlan_pkts_count", options)

    def get_port_statistic_rx_data_int_errors_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "data_int_errors_rate", options)

    def get_port_statistic_rx_raw_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "raw_pkt_rate", options)

    def get_port_statistic_rx_pkt_bit_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "pkt_bit_count", options)

    def get_port_statistic_rx_qos3_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos3_count", options)

    def get_port_statistic_rx_qos1_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos1_rate", options)

    def get_port_statistic_rx_fragments_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "fragments_count", options)

    def get_port_statistic_rx_collisions_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "collisions_count", options)

    def get_port_statistic_rx_qos7_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos7_count", options)

    def get_port_statistic_rx_sequence_frames_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "sequence_frames_count", options)

    def get_port_statistic_rx_sequence_errors_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "sequence_errors_rate", options)

    def get_port_statistic_rx_collisions_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "collisions_rate", options)

    def get_port_statistic_rx_fragments_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "fragments_rate", options)

    def get_port_statistic_rx_data_int_frames_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "data_int_frames_rate", options)

    def get_port_statistic_rx_qos6_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos6_rate", options)

    def get_port_statistic_rx_qos2_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos2_count", options)

    def get_port_statistic_rx_pkt_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "pkt_count", options)

    def get_port_statistic_rx_uds1_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "uds1_rate", options)

    def get_port_statistic_rx_dribble_errors_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "dribble_errors_count", options)

    def get_port_statistic_rx_qos3_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos3_rate", options)

    def get_port_statistic_rx_qos6_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos6_count", options)

    def get_port_statistic_rx_data_int_frames_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "data_int_frames_count", options)

    def get_port_statistic_rx_dribble_errors_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "dribble_errors_rate", options)

    def get_port_statistic_rx_qos0_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos0_rate", options)

    def get_port_statistic_rx_crc_errors_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "crc_errors_rate", options)

    def get_port_statistic_rx_oversize_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "oversize_count", options)

    def get_port_statistic_rx_pkt_bit_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "pkt_bit_rate", options)

    def get_port_statistic_rx_sequence_frames_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "sequence_frames_rate", options)

    def get_port_statistic_rx_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "pkt_rate", options)

    def get_port_statistic_rx_undersize_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "undersize_rate", options)

    def get_port_statistic_rx_qos1_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos1_count", options)

    def get_port_statistic_rx_pkt_byte_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "pkt_byte_rate", options)

    def get_port_statistic_rx_protocol_pkt_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "protocol_pkt_count", options)

    def get_port_statistic_rx_qos5_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos5_count", options)

    def get_port_statistic_rx_undersize_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "undersize_count", options)

    def get_port_statistic_rx_oversize_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "oversize_rate", options)

    def get_port_statistic_rx_qos5_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "qos5_rate", options)

    def get_port_statistic_rx_protocol_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "rx", "protocol_pkt_rate", options)

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

    # {tx {{raw_pkt_count 106} {pkt_byte_count 6784} {total_pkt_rate 9}
    # {pkt_bit_count 54272} {pkt_bit_rate 5121} {pkt_rate 10} {pkt_count 106}
    # {total_pkt_bytes 0} {total_pkts_bytes 0} {elapsed_time 10.50}
    # {pkt_byte_rate 640} {protocol_pkt_rate {Stat protocolServerTx not supported}}
    # {total_pkts 119} {raw_pkt_rate 10} {protocol_pkt_count 0}}}
    def get_port_statistic_tx_raw_pkt_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "raw_pkt_count", options)

    def get_port_statistic_tx_pkt_byte_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "pkt_byte_count", options)

    def get_port_statistic_tx_total_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "total_pkt_rate", options)

    def get_port_statistic_tx_pkt_bit_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "pkt_bit_count", options)

    def get_port_statistic_tx_pkt_bit_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "pkt_bit_rate", options)

    def get_port_statistic_tx_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "pkt_rate", options)

    def get_port_statistic_tx_pkt_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "pkt_count", options)

    def get_port_statistic_tx_total_pkt_bytes(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "total_pkt_bytes", options)

    def get_port_statistic_tx_elapsed_time(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "elapsed_time", options)

    def get_port_statistic_tx_pkt_byte_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "pkt_byte_rate", options)

    def get_port_statistic_tx_protocol_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "protocol_pkt_rate", options)

    def get_port_statistic_tx_protocol_server_tx(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "protocolServerTx", options)

    def get_port_statistic_tx_total_pkts(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "total_pkts", options)

    def get_port_statistic_tx_raw_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "raw_pkt_rate", options)

    def get_port_statistic_tx_protocol_pkt_count(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_statistic(port_handle, "tx", "protocol_pkt_count", options)

    #   {{stream
    # {{1 {{rx {{line_rate_percentage 0} {total_pkt_bit_rate 0} {total_pkt_bytes 0} {max_delay 0} {total_pkts 0}
    # {total_pkts_bytes 0} {total_pkt_rate 0} {min_delay 0} {avg_delay 0}}}
    # {tx {{elapsed_time 10.50} {total_pkts 118} {total_pkt_rate 9}}}}}}}
    def get_port_stream_statistic_rx_line_rate_percentage(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "rx", "line_rate_percentage", options)

    def get_port_stream_statistic_rx_total_pkt_bit_rate(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "rx", "total_pkt_bit_rate", options)

    def get_port_stream_statistic_rx_total_pkt_bytes(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "rx", "total_pkt_bytes", options)

    def get_port_stream_statistic_rx_max_delay(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "rx", "max_delay", options)

    def get_port_stream_statistic_rx_total_pkts(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "rx", "total_pkts", options)

    def get_port_stream_statistic_rx_total_pkts_bytes(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "rx", "total_pkts_bytes", options)

    def get_port_stream_statistic_rx_total_pkt_rate(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "rx", "total_pkt_rate", options)

    def get_port_stream_statistic_rx_min_delay(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "rx", "min_delay", options)

    def get_port_stream_statistic_rx_avg_delay(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "rx", "avg_delay", options)

    def get_port_stream_statistic_tx_elapsed_time(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "tx", "elapsed_time", options)

    def get_port_stream_statistic_tx_total_pkts(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "tx", "total_pkts", options)

    def get_port_stream_statistic_tx_total_pkt_rate(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_stream_statistic(port_handle, stream_id, "tx", "total_pkt_rate", options)
