# from ostinato.core import DroneProxy
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceStatisticHelper import \
    TrafficGeneratingDeviceStatisticHelper


class JetsDeviceStatisticHelper(TrafficGeneratingDeviceStatisticHelper):
    def __init__(self, ixia_device):
        super(JetsDeviceStatisticHelper, self).__init__(ixia_device)

    def get_jets_analyer_rx_stats(self, port_string):
        prt_id = self.get_port_index_from_group_string(port_string)
        return self.send_command("an" + prt_id + " stats")

    def get_jets_analyer_rx_stats_array(self, port_string):
        stats_string = self.get_jets_analyer_rx_stats(port_string)
        # split Key|Value
        if "invalid" in stats_string:
            return {}
        try:
            stats_string = stats_string.split("\n")[1].strip()
            # stats_string = eval("{" + re.sub('-([A-Za-z]+) ([0-9E\.]+)', r'"\1":"\2",', stats_string.strip()) + "}")
            span = 2
            words = stats_string.split(" ")
            array = [":".join(words[i:i + span]) for i in range(0, len(words), span)]
            ret_arr = {}
            for a in array:
                spl = a.split(":")
                ret_arr[spl[0][1:]] = spl[1]
            return ret_arr
        except:
            return {}

    def get_jets_stats(self, port_string):
        prt_id = self.get_circuit_name_from_interface_name(port_string)
        return self.send_command(prt_id + " stats")

    def get_jets_stats_array(self, port_string):
        stats_string = self.get_jets_stats(port_string)
        # split Key|Value
        if "invalid" in stats_string:
            return {}
        try:
            stats_string = stats_string.split("\n")[1].strip()
            # stats_string += "txPkts: 0, rxPkts: 1\n%"
            stats_string = stats_string.replace(":", "")
            stats_string = stats_string.replace(",", "")
            stats_string = stats_string.replace("%", "")
            stats_string = stats_string.strip()
            # stats_string = eval("{" + re.sub('-([A-Za-z]+) ([0-9E\.]+)', r'"\1":"\2",', stats_string.strip()) + "}")
            span = 2
            words = stats_string.split(" ")
            array = [":".join(words[i:i + span]) for i in range(0, len(words), span)]
            ret_arr = {}
            for a in array:
                spl = a.split(":")
                ret_arr[spl[0]] = spl[1]
            return ret_arr
        except:
            return {}

    def get_jets_analyer_tx_stats(self, port_string):
        if port_string not in self._streams:
            return False
        streams = self._streams[port_string]
        stats_array = []
        for key, stream in streams.items():
            stats_array.append(self.send_command(stream + " stats").split("\n")[1])
        return stats_array

    def get_jets_analyer_tx_stats_array(self, port_string):
        stats_array = self.get_jets_analyer_tx_stats(port_string)
        ret_array = []
        if not stats_array:
            return None
        for stats_string in stats_array:
            ret_arr = {}
            # split Key|Value
            if "invalid" in stats_string:
                ret_array.append(ret_arr)
                continue
            try:
                if "\n" in stats_string:
                    stats_string = stats_string.split("\n")[1].strip()
                # stats_string = eval("{" + re.sub('-([A-Za-z]+) ([0-9E\.]+)', r'"\1":"\2",', stats_string.strip()) +
                #                     "}")
                span = 2
                words = stats_string.split(" ")
                array = [":".join(words[i:i + span]) for i in range(0, len(words), span)]
                for a in array:
                    spl = a.split(":")
                    ret_arr[spl[0][1:]] = spl[1]
                ret_array.append(ret_arr)
            except:
                ret_array.append(ret_arr)
                continue
        return ret_array

    def get_jets_analyer_tx_stats_combined_array(self, port_string):
        stats_array = self.get_jets_analyer_tx_stats_array(port_string)
        ret_array = False
        if not stats_array or 'xception' in str(stats_array):
            return None
        for arr in stats_array:
            for key, val in arr.items():
                try:
                    if isinstance(val, str):
                        val = val.strip()
                    if "." in val:
                        arr[key] = float(val)
                    elif "false" in val.lower():
                        arr[key] = False
                    elif "true" in val.lower():
                        arr[key] = True
                    else:
                        arr[key] = int(val)
                except:
                    self.logger.log_debug("error: get_jets_analyer_tx_stats_combined_array")
            if ret_array:
                # combine ret_array with arr
                for key, val in arr.items():
                    ret_array[key] += val
            else:
                ret_array = arr
        return ret_array

    def _get_stats_value(self, stats, _type, default_value=0):
        try:
            if _type in stats:
                return stats[_type]
        except:
            pass
        return default_value

    def get_port_rx_collisions_count(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_port_tx_frame_count(self, port_string):
        stats = self.get_jets_analyer_tx_stats_combined_array(port_string)
        return self._get_stats_value(stats, "pktCount")

    def get_port_rx_frame_count(self, port_string):
        stats = self.get_jets_analyer_rx_stats_array(port_string)
        return self._get_stats_value(stats, "totalPackets")

    def get_port_fcs_errors_count(self, port_string):
        stats = self.get_jets_analyer_rx_stats_array(port_string)
        return self._get_stats_value(stats, "totalPackets") - self._get_stats_value(stats, "goodPackets")

    def get_port_total_collisions_count(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_port_late_collisions_count(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_uds2_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos2_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_byte_count(self, port_handle, options=None):
        stats = self.get_jets_analyer_rx_stats_array(port_handle)
        return self._get_stats_value(stats, "totalPacketBytes")

    def get_port_statistic_rx_qos0_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_vlan_pkts_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_sequence_errors_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos4_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_crc_errors_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos7_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_uds1_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_raw_pkt_count(self, port_handle, options=None):
        return self.get_jets_stats_array(port_handle)["rxPkts"]

    def get_port_statistic_rx_data_int_errors_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_uds2_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos4_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_vlan_pkts_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_data_int_errors_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_raw_pkt_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_bit_count(self, port_handle, options=None):
        stats = self.get_jets_analyer_rx_stats_array(port_handle)
        return self._get_stats_value(stats, "totalPacketBytes") * 8

    def get_port_statistic_rx_qos3_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos1_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_fragments_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_collisions_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos7_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_sequence_frames_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_sequence_errors_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_collisions_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_fragments_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_data_int_frames_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos6_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos2_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_uds1_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_dribble_errors_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos3_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos6_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_data_int_frames_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_dribble_errors_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos0_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_crc_errors_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_oversize_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_bit_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].rx_bps

    def get_port_statistic_rx_sequence_frames_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_rate(self, port_handle, options=None):
        stats = self.get_jets_analyer_rx_stats_array(port_handle)
        return self._get_stats_value(stats, "totalPacketRate")

    def get_port_statistic_rx_undersize_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos1_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_pkt_byte_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_protocol_pkt_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos5_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_undersize_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_oversize_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_qos5_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_rx_protocol_pkt_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_capture_filter_count(self, port_string, options=None):
        return self.get_captured_frame_count(port_string)
        # stats = self.get_jets_analyer_stats_array(port_string)
        # return len(self.get_all_captured_frames(port_string))

    def get_port_statistic_capture_trigger_count(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_capture_filter_rate(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_capture_trigger_rate(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_tx_raw_pkt_count(self, port_handle, options=None):
        return self.get_port_tx_frame_count(port_handle)
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_pkts

    def get_port_statistic_tx_pkt_byte_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_bytes

    def get_port_statistic_tx_total_pkt_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_pps

    def get_port_statistic_tx_pkt_bit_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_bytes

    def get_port_statistic_tx_pkt_bit_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_bps

    def get_port_statistic_tx_pkt_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_pps

    def get_port_statistic_tx_pkt_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_pkts

    def get_port_statistic_tx_total_pkt_bytes(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_bps

    def get_port_statistic_tx_elapsed_time(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return self.logger.log_unimplemented_method()

    def get_port_statistic_tx_pkt_byte_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_bps

    def get_port_statistic_tx_protocol_pkt_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_tx_protocol_server_tx(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_statistic_tx_total_pkts(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_pkts

    def get_port_statistic_tx_raw_pkt_rate(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_pkts

    def get_port_statistic_tx_protocol_pkt_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_rx_line_rate_percentage(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_rx_total_pkt_bit_rate(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_rx_total_pkt_bytes(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_rx_max_delay(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_rx_total_pkts(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_rx_total_pkts_bytes(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_rx_total_pkt_rate(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_rx_min_delay(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_rx_avg_delay(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_tx_elapsed_time(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic_tx_total_pkts(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_pkts

    def get_port_stream_statistic_tx_total_pkt_rate(self, port_handle, stream_id, options=None):
        return self.logger.log_unimplemented_method()
        # stats = self.get_jets_analyer_stats_array(port_handle)
        # return stats.port_stats._values[0].tx_pps
