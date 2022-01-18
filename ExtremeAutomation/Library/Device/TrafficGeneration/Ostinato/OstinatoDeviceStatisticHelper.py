from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import DroneProxy
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceStatisticHelper import \
    TrafficGeneratingDeviceStatisticHelper


class OstinatoDeviceStatisticHelper(TrafficGeneratingDeviceStatisticHelper):

    def __init__(self, ixia_device):
        super(OstinatoDeviceStatisticHelper, self).__init__(ixia_device)

    # def get_port_rx_collisions_count(self, port_string):
    #     return self.logger.log_unimplemented_method()

    def get_port_tx_frame_count(self, port_string):
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_pkts

    def get_port_rx_frame_count(self, port_string):
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].rx_pkts

    def get_port_fcs_errors_count(self, port_string):
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].rx_frame_errors

    # def get_port_total_collisions_count(self, port_string):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_late_collisions_count(self, port_string):
    #    return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_uds2_count(self, port_handle, options=None):
    #   if options is None:
    #       options = {}
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos2_rate(self, port_handle, options=None):
    #   if options is None:
    #       options = {}
    #     return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_byte_count(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].rx_bytes

    # def get_port_statistic_rx_qos0_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_vlan_pkts_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_sequence_errors_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos4_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_crc_errors_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos7_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_statistic_rx_uds1_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_raw_pkt_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_data_int_errors_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_uds2_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos4_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_vlan_pkts_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_data_int_errors_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_raw_pkt_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_bit_count(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].rx_bytes

    # def get_port_statistic_rx_qos3_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos1_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_fragments_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_collisions_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos7_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_sequence_frames_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_sequence_errors_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_collisions_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_fragments_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_data_int_frames_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos6_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos2_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_pkt_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_uds1_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_dribble_errors_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos3_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos6_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_data_int_frames_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_dribble_errors_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos0_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_crc_errors_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_oversize_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_bit_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].rx_bps

    # def get_port_statistic_rx_sequence_frames_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].rx_pps

    # def get_port_statistic_rx_undersize_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos1_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_pkt_byte_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_protocol_pkt_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos5_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_undersize_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_oversize_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_qos5_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_rx_protocol_pkt_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()

    def get_port_statistic_capture_filter_count(self, port_string, options={}):
        return len(self.get_all_captured_frames(port_string))

    # def get_port_statistic_capture_trigger_count(self, port_string, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_capture_filter_rate(self, port_string, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    #
    # def get_port_statistic_capture_trigger_rate(self, port_string, options={}):
    #     return self.logger.log_unimplemented_method()

    def get_port_statistic_tx_raw_pkt_count(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection

        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        self.logger.log_debug(stats)
        return stats.port_stats._values[0].tx_pkts

    def get_port_statistic_rx_raw_pkt_count(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        self.logger.log_debug(stats)
        self.logger.log_debug("STATS")
        self.logger.log_debug(stats.port_stats._values[0].rx_pkts)
        return stats.port_stats._values[0].rx_pkts

    def get_port_statistic_tx_pkt_byte_count(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_bytes

    def get_port_statistic_tx_total_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_pps

    def get_port_statistic_tx_pkt_bit_count(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_bytes

    def get_port_statistic_tx_pkt_bit_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_bps

    def get_port_statistic_tx_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_pps

    def get_port_statistic_tx_pkt_count(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_pkts

    def get_port_statistic_tx_total_pkt_bytes(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_bps

    def get_port_statistic_tx_elapsed_time(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_statistic_tx_pkt_byte_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_bps

    # def get_port_statistic_tx_protocol_pkt_rate(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_statistic_tx_protocolServerTx(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()

    def get_port_statistic_tx_total_pkts(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_pkts

    def get_port_statistic_tx_raw_pkt_rate(self, port_handle, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_pkts

    # def get_port_statistic_tx_protocol_pkt_count(self, port_handle, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_rx_line_rate_percentage(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_rx_total_pkt_bit_rate(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_rx_total_pkt_bytes(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_rx_max_delay(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_rx_total_pkts(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_rx_total_pkts_bytes(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_rx_total_pkt_rate(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_rx_min_delay(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_rx_avg_delay(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_port_stream_statistic_tx_elapsed_time(self, port_handle, stream_id, options={}):
    #     return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_tx_total_pkts(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_pkts

    def get_port_stream_statistic_tx_total_pkt_rate(self, port_handle, stream_id, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        stats = drone.getStats(port_string)
        return stats.port_stats._values[0].tx_pps
