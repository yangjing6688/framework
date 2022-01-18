from collections import OrderedDict
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class PacketInspectionUtils(TrafficKeywordBaseClass):
    def __init__(self):
        super(PacketInspectionUtils, self).__init__()

        self.capture_length = None

    def _capture_inspection(self, port, expected_packet_name, packet_check_list, check_all_fields,
                            ignore_list, include_list):
        if self.debug_packet:
            self.logger.log_info(self.traffic_gen.get_filtered_captured_frames_report(port))

        inspection_result = True

        self.get_capture_length(port)

        if self.capture_length == 0:
            return False

        if self.pkt_dict.get_packet(expected_packet_name):
            expected_packet = self.pkt_dict.get_packet(expected_packet_name)
        else:
            expected_packet = expected_packet_name

        packets_to_check = self._get_packets(packet_check_list, port)

        for packet_index in packets_to_check:
            if self.debug_packet:
                self.logger.log_info(self.traffic_gen.get_captured_frame(port, packet_index))
            self.logger.log_info("\nPacket " + str(packet_index) + " of " + str(self.capture_length))

            if not expected_packet.compare_packet_fields(packets_to_check[packet_index], check_all_fields,
                                                         ignore_list, include_list):
                inspection_result = False

        self.debug_packet = False

        return inspection_result

    def get_capture_length(self, port):
        """
        Updates the capture length if it is currently set to None, otherwise return the current
        capture length.
        """
        if self.capture_length is None:
            self.capture_length = int(self.capture_helper.get_captured_frame_count(port))
        return self.capture_length

    def _get_packets(self, packet_list, port):
        packets = OrderedDict()

        for i in packet_list:
            packets[i] = self.capture_helper.get_captured_frame(port, i)
        return packets
