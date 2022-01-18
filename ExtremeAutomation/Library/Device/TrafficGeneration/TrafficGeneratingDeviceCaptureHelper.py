import abc
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier


class TrafficGeneratingDeviceCaptureHelper(object, metaclass=abc.ABCMeta):
    def __init__(self, ixia_device):
        self.dev = ixia_device
        self.logger = Logger()
        self.temp_capture_filter_info = dict()
        self.temp_capture_trigger_info = dict()

    # {status 1} {1/1/2 {{aggregate {{uds1_frame_count 0} {uds2_frame_count 0} {average_deviation 0}
    # {average_latency 0} {num_frames 192} {max_latency 0} {min_latency 0} {standard_deviation 0}
    # {average_deviation_per_chunk 0} {standard_deviation_per_chunk 0}}}}}

    def get_port_capture_uds1_frame_count(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "uds1_frame_count", options)

    def get_port_capture_uds2_frame_count(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "uds2_frame_count", options)

    def get_port_capture_average_deviation(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "average_deviation", options)

    def get_port_capture_average_latency(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "average_latency", options)

    def get_port_capture_num_frames(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "num_frames", options)

    def get_port_capture_max_latency(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "max_latency", options)

    def get_port_capture_min_latency(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "min_latency", options)

    def get_port_capture_standard_deviation(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "standard_deviation", options)

    def get_port_capture_average_deviation_per_chunk(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "average_deviation_per_chunk", options)

    def get_port_capture_standard_deviation_per_chunk(self, port_string, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture(port_string, "standard_deviation_per_chunk", options)

    #     % set temp_stats [keylget stats_status 1/1/2.frame.1]
    # {status cap10100DpmGoodPacket} {fir 10240699660} {latency 0} {length 64} {time_stamp 8409078100}
    #     {frame {00 00 00 00 00 11 00 00 00 00 00 22 08 00 45 00 00 2E 00 00 00 00 40 FF 73 CC 02 02 02 02 01 01 01
    #             01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 01 00 00 1E 85 08 A7 D7 E0 E8 16}}
    # {status cap10100DpmGoodPacket} {fir 11040700320} {latency 0} {length 64} {time_stamp 9209078740}
    #     {frame {00 00 00 00 00 11 00 00 00 00 00 33 08 00 45 00 00 2E 00 00 00 00 40 FF 71 CA 03 03 03 03 01 01 01
    #             01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 02 00 00 20 E7 62 C8 BA 9F 55 F9}}}}
    def get_port_capture_frame_status(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture_frame(port_string, frame_num, "status", options)

    def get_port_capture_frame_fir(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture_frame(port_string, frame_num, "fir", options)

    def get_port_capture_frame_latency(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture_frame(port_string, frame_num, "latency", options)

    def get_port_capture_frame_length(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture_frame(port_string, frame_num, "length", options)

    def get_port_capture_frame_time_stamp(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture_frame(port_string, frame_num, "time_stamp", options)

    def get_port_capture_frame_frame_data_string(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.dev.get_port_capture_frame(port_string, frame_num, "frame", options)

    def get_port_capture_frame_frame_data_in_bytes(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        packet = self.dev.get_port_capture_frame(port_string, frame_num, "frame", options)
        pkt_bytes = packet.strip().split(" ")
        index = 0
        for item in pkt_bytes:
            pkt_bytes[index] = int(pkt_bytes[index], 16)
            index += 1
        return pkt_bytes

    def get_captured_frame_count(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_running_captured_frame_count(self, port_handle, options=None):
        return self.logger.log_unimplemented_method()

    def get_captured_frame(self, port_string, frame_num):
        return self.logger.log_unimplemented_method()

    def get_captured_frame_status(self, port_string, frame_num):
        return self.logger.log_unimplemented_method()

    def get_captured_frames(self, port_string, first_frame_num, last_frame_num):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_all_captured_frames(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_all_captured_frames_filtered_by_packet(self, port_string, expected_packet):
        captured_frames = self.get_all_captured_frames(port_string)
        filtered_frames = []
        packet_index = 1
        for frame in captured_frames:
            self.logger.log_debug("Packet " + str(packet_index) + " filtered")
            if expected_packet.match_packet_fields(frame):
                filtered_frames.append(frame)
                self.logger.log_debug("MATCH")
            else:
                self.logger.log_debug("NO MATCH")
            packet_index += 1
        return filtered_frames

    def save_all_captured_frames_to_pcap(self, port_handle, output_file, options=None):
        packets = self.get_all_captured_frames(port_handle, options)
        PacketClassifier.save_to_pcap_file_contents(packets, output_file)

    def clear_capture_filters_and_triggers(self, port_string):
        self.dev.clear_capture_filters_and_triggers(port_string)

    @abc.abstractmethod
    def write_capture_trigger(self, port_handle, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_all_captured_frames_filtered_by_tags(self, port_handle, class_filters):
        frames = self.get_all_captured_frames(port_handle)
        if not isinstance(class_filters, list):
            class_filters = [class_filters]
        ret_frames = []
        for frame in frames:
            match = True
            for class_filter in class_filters:
                if not isinstance(frame, class_filter):
                    match = False
                    break
            if match:
                ret_frames.append(frame)
        return ret_frames

    def get_filtered_captured_frames_report(self, port_handle):
        frames = self.get_all_captured_frames(port_handle)
        report_count = {}
        report_packet = {}
        for frame in frames:
            key = frame.get_name() + " " + frame.get_destination_mac() + " " + frame.get_source_mac()
            if key not in report_count:
                report_count[key] = 0
                report_packet[key] = frame
            report_count[key] += 1

        table = TableFormatter()
        for key, value in report_count.items():
            frame = report_packet[key]
            table.add_row_value("Packet Type", frame.get_name())
            table.add_row_value("DA", frame.get_destination_mac())
            table.add_row_value("SA", frame.get_source_mac())
            table.add_row_value("Count", report_count[key])
        return table.to_table_string()
