from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import \
    PacketConfigFilterConstants
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceCaptureHelper import \
    TrafficGeneratingDeviceCaptureHelper
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class ScapyDeviceCaptureHelper(TrafficGeneratingDeviceCaptureHelper):
    def __init__(self, ixia_device):
        super(ScapyDeviceCaptureHelper, self).__init__(ixia_device)
        self.dev = ixia_device
        self.current_filter = None
        self.current_trigger = None
        self.capture_filter_info = {}
        self.capture_trigger_info = {}
        pass

    # {status 1} {1/1/2 {{aggregate {{uds1_frame_count 0} {uds2_frame_count 0} {average_deviation 0}
    # {average_latency 0} {num_frames 192} {max_latency 0} {min_latency 0} {standard_deviation 0}
    # {average_deviation_per_chunk 0} {standard_deviation_per_chunk 0}}}}}

    def get_port_capture_uds1_frame_count(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_capture_uds2_frame_count(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def get_port_capture_average_deviation(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_average_latency(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_num_frames(self, port_string, options=None):
        if options is None:
            options = {}
        return len(self.get_all_captured_frames(port_string, options))

    def get_port_capture_max_latency(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_min_latency(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_standard_deviation(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_average_deviation_per_chunk(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_standard_deviation_per_chunk(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    #     % set temp_stats [keylget stats_status 1/1/2.frame.1]
    # {status cap10100DpmGoodPacket} {fir 10240699660} {latency 0} {length 64} {time_stamp 8409078100}
    # {frame {00 00 00 00 00 11 00 00 00 00 00 22 08 00 45 00 00 2E 00 00 00 00 40 FF 73 CC 02 02 02 02 01 01 01 01 00
    # 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 01 00 00 1E 85 08 A7 D7 E0 E8 16}}
    # {status cap10100DpmGoodPacket} {fir 11040700320} {latency 0} {length 64} {time_stamp 9209078740}
    # {frame {00 00 00 00 00 11 00 00 00 00 00 33 08 00 45 00 00 2E 00 00 00 00 40 FF 71 CA 03 03 03 03 01 01 01 01 00
    # 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 02 00 00 20 E7 62 C8 BA 9F 55 F9}}}}
    def get_port_capture_frame_status(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_frame_fir(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_frame_latency(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_frame_length(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_frame_time_stamp(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_frame_frame_data_string(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_frame_frame_data_in_bytes(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        # assert isinstance(self.connection, DroneProxy)
        port_string = self.Scapy_port_number_to_port(port_string)
        buff = self.dev.connection.getCaptureBuffer(port_string.port_id[0])
        if buff:
            packets_captured = PacketClassifier.process_pcap_file_contents(buff)
            return packets_captured[frame_num].get_bytes()
        else:
            return None

    def get_unfiltered_captured_frame_count(self, port_handle, options=None):
        return len(self.get_all_unfiltered_captured_frames(port_handle))

    def get_all_unfiltered_captured_frames(self, port_handle, options=None):
        if self.capture_buffer.is_capture_buffer_filled(port_handle):
            return self.capture_buffer.get_stored_capture_buffer(port_handle)
        if options is None:
            options = {}
        packets_captured = []
        # assert isinstance(self.connection, DroneProxy)
        port_string = self.Scapy_port_number_to_port(port_handle)
        buff = self.dev.connection.getCaptureBuffer(port_string.port_id[0])
        if buff:
            packets_captured = PacketClassifier.process_pcap_file_contents(buff)
        return str(packets_captured)

    def get_captured_frame_count(self, port_handle, options=None):
        return len(self.get_all_captured_frames(port_handle))

    def get_captured_frame(self, port_string, frame_num):
        return self.get_all_captured_frames(port_string)[frame_num]

    def get_captured_frames(self, port_string, first_frame_num, last_frame_num):
        return self.get_all_captured_frames(port_string)[first_frame_num:last_frame_num]

    def get_all_captured_frames(self, port_handle, options=None):
        if self.capture_buffer.is_capture_buffer_filled(port_handle):
            return self.capture_buffer.get_stored_capture_buffer(port_handle)
        if options is None:
            options = {}
        # assert isinstance(self.connection, DroneProxy)
        port_string = self.Scapy_port_number_to_port(port_handle)
        buff = self.dev.connection.getCaptureBuffer(port_string.port_id[0])
        if buff:
            packets_captured = PacketClassifier.process_pcap_file_contents(buff)

            is_trigger_set = port_handle in self.capture_trigger_info
            is_capture_set = port_handle in self.capture_filter_info
            # if trigger is set or capture is set to something that isn't ANY,
            # We have to do work
            if is_trigger_set or is_capture_set:
                temp_cap = []
                trigger_found = True
                if is_trigger_set:
                    trigger_found = False
                packet_index = 0
                for packet in packets_captured:
                    packet_index += 1
                    # if is_trigger_set, loop until trigger is found
                    if is_trigger_set and not trigger_found:
                        # trigger_found = check triggers
                        # otherwise,
                        # check for all Any if all Any, it matches
                        trigger_found = self.capture_trigger_info[port_handle].matches(
                            packet, self.capture_filter_info[port_handle])
                        if not trigger_found:
                            continue
                        trigger_found = packet_index
                        # print("triggered at packet #"+str(packet_index))
                    # once trigger_found you get here
                    # capture_match = check captures
                    capture_match = self.capture_filter_info[port_handle].matches(
                        packet, self.capture_trigger_info[port_handle])
                    if not is_capture_set or capture_match:
                        # print("packet #"+str(packet_index) + " matched " + packet.get_destination_mac() + "/" +
                        #       packet.get_source_mac())
                        temp_cap.append(packet)
                    # else:
                    #     print("packet #"+str(packet_index) + " didn't matched " + packet.get_destination_mac() +
                    #           "/" + packet.get_source_mac())
                return temp_cap
            return packets_captured
        else:
            return []

    def clear_capture_filters_and_triggers(self, port_string):
        self.dev.clear_capture_filters_and_triggers(port_string)
        if port_string in self.capture_filter_info:
            self.capture_filter_info[port_string] = ScapyDeviceCaptureFilterHelperInfo()
        if port_string in self.capture_trigger_info:
            self.capture_trigger_info[port_string] = ScapyDeviceCaptureFilterHelperInfo()

    def set_capture_filter_da1(self, port_handle, da, da_mask, options=None):
        if port_handle not in self.capture_filter_info:
            self.capture_filter_info[port_handle] = ScapyDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_da1_da = da
        self.capture_filter_info[port_handle].capture_filter_da1_da_mask = da_mask

    def set_capture_filter_da2(self, port_handle, da, da_mask, options=None):
        if port_handle not in self.capture_filter_info:
            self.capture_filter_info[port_handle] = ScapyDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_da2_da = da
        self.capture_filter_info[port_handle].capture_filter_da2_da_mask = da_mask

    def set_capture_filter_sa1(self, port_handle, sa, sa_mask, options=None):
        if port_handle not in self.capture_filter_info:
            self.capture_filter_info[port_handle] = ScapyDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_sa1_sa = sa
        self.capture_filter_info[port_handle].capture_filter_sa1_sa_mask = sa_mask

    def set_capture_filter_sa2(self, port_handle, sa, sa_mask, options=None):
        if port_handle not in self.capture_filter_info:
            self.capture_filter_info[port_handle] = ScapyDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_sa2_sa = sa
        self.capture_filter_info[port_handle].capture_filter_sa2_sa_mask = sa_mask

    def set_capture_filter_pattern1(self, port_handle, pattern, pattern_mask, pattern_offset, pattern_offset_type,
                                    match_type, options=None):
        if port_handle not in self.capture_filter_info:
            self.capture_filter_info[port_handle] = ScapyDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_pattern1_pattern = pattern
        self.capture_filter_info[port_handle].capture_filter_pattern1_pattern_mask = pattern_mask
        self.capture_filter_info[port_handle].capture_filter_pattern1_pattern_offset = pattern_offset
        self.capture_filter_info[port_handle].capture_filter_pattern1_pattern_offset_type = pattern_offset_type
        self.capture_filter_info[port_handle].capture_filter_pattern1_match_type = match_type

    def set_capture_filter_pattern2(self, port_handle, pattern, pattern_mask, pattern_offset, pattern_offset_type,
                                    match_type, options=None):
        if port_handle not in self.capture_filter_info:
            self.capture_filter_info[port_handle] = ScapyDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_pattern2_pattern = pattern
        self.capture_filter_info[port_handle].capture_filter_pattern2_pattern_mask = pattern_mask
        self.capture_filter_info[port_handle].capture_filter_pattern2_pattern_offset = pattern_offset
        self.capture_filter_info[port_handle].capture_filter_pattern2_pattern_offset_type = pattern_offset_type
        self.capture_filter_info[port_handle].capture_filter_pattern2_match_type = match_type

    def set_capture_filter_pattern_atm(self, port_handle, pattern, pattern_mask, pattern_offset, options=None):
        return self.logger.log_unimplemented_method()

    def get_capture_filter(self, port_string):
        if port_string not in self.capture_filter_info:
            self.capture_filter_info[port_string] = ScapyDeviceCaptureFilterHelperInfo()
        self.current_filter = self.capture_filter_info[port_string]

    def get_capture_filter_default(self):
        self.current_filter = ScapyDeviceCaptureFilterHelperInfo()

    def add_capture_filter_da1(self, da, da_mask, options=None):
        self.current_filter.capture_filter_da1_da = da
        self.current_filter.capture_filter_da1_da_mask = da_mask

    def add_capture_filter_da2(self, da, da_mask, options=None):
        self.current_filter.capture_filter_da2_da = da
        self.current_filter.capture_filter_da2_da_mask = da_mask

    def add_capture_filter_sa1(self, sa, sa_mask, options=None):
        self.current_filter.capture_filter_sa1_sa = sa
        self.current_filter.capture_filter_sa1_sa_mask = sa_mask

    def add_capture_filter_sa2(self, sa, sa_mask, options=None):
        self.current_filter.capture_filter_sa2_sa = sa
        self.current_filter.capture_filter_sa2_sa_mask = sa_mask

    def add_capture_filter_pattern1(self, pattern, pattern_mask, pattern_offset, pattern_offset_type, match_type,
                                    options=None):
        self.current_filter.capture_filter_pattern1_pattern = pattern
        self.current_filter.capture_filter_pattern1_pattern_mask = pattern_mask
        self.current_filter.capture_filter_pattern1_pattern_offset = pattern_offset
        self.current_filter.capture_filter_pattern1_pattern_offset_type = pattern_offset_type
        self.current_filter.capture_filter_pattern1_match_type = match_type

    def add_capture_filter_pattern2(self, pattern, pattern_mask, pattern_offset, pattern_offset_type, match_type,
                                    options=None):
        self.current_filter.capture_filter_pattern2_pattern = pattern
        self.current_filter.capture_filter_pattern2_pattern_mask = pattern_mask
        self.current_filter.capture_filter_pattern2_pattern_offset = pattern_offset
        self.current_filter.capture_filter_pattern2_pattern_offset_type = pattern_offset_type
        self.current_filter.capture_filter_pattern2_match_type = match_type

    def add_capture_filter_pattern_atm(self, pattern, pattern_mask, pattern_offset, options=None):
        return self.logger.log_unimplemented_method()

    def write_capture_filter(self, port_handle, options=None):
        self.capture_filter_info[port_handle] = self.current_filter

    def set_capture_filter(self, port_handle, enable, da_logic, sa_logic, error_logic, frame_size_logic,
                           frame_start_size, frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_trigger(self, port_handle, enable, da_logic, sa_logic, error_logic, frame_size_logic,
                            frame_start_size, frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_async_trigger1(self, port_handle, enable, da_logic, sa_logic, error_logic, frame_size_logic,
                                   frame_start_size, frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_async_trigger2(self, port_handle, enable, da_logic, sa_logic, error_logic, frame_size_logic,
                                   frame_start_size, frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_user_defined_statistics1(self, port_handle, enable, da_logic, sa_logic, error_logic,
                                             frame_size_logic, frame_start_size, frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_user_defined_statistics2(self, port_handle, enable, da_logic, sa_logic, error_logic,
                                             frame_size_logic, frame_start_size, frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def get_capture_trigger(self, port_string):
        if port_string not in self.capture_trigger_info:
            self.capture_trigger_info[port_string] = ScapyDeviceCaptureTriggerHelperInfo()
        self.current_trigger = self.capture_trigger_info[port_string]

    def get_capture_trigger_default(self):
        self.current_trigger = ScapyDeviceCaptureTriggerHelperInfo()

    def add_capture_trigger_capture_filter(self, enable, da_logic, sa_logic, pattern_logic, error_logic,
                                           frame_size_logic, frame_start_size, frame_end_size, options=None):
        if self.current_trigger is None:
            self.current_trigger = ScapyDeviceCaptureTriggerHelperInfo()
        self.current_trigger.capture_filter_enable = enable
        self.current_trigger.capture_filter_da_logic = da_logic
        self.current_trigger.capture_filter_sa_logic = sa_logic
        self.current_trigger.capture_filter_pattern_logic = pattern_logic
        self.current_trigger.capture_filter_error_logic = error_logic
        self.current_trigger.capture_filter_frame_size_logic = frame_size_logic
        self.current_trigger.capture_filter_frame_start_size = frame_start_size
        self.current_trigger.capture_filter_frame_end_size = frame_end_size

    def add_capture_trigger_capture_trigger(self, enable, da_logic, sa_logic, pattern_logic, error_logic,
                                            frame_size_logic, frame_start_size, frame_end_size, options=None):
        if self.current_trigger is None:
            self.current_trigger = ScapyDeviceCaptureTriggerHelperInfo()
        self.current_trigger.capture_trigger_enable = enable
        self.current_trigger.capture_trigger_da_logic = da_logic
        self.current_trigger.capture_trigger_sa_logic = sa_logic
        self.current_trigger.capture_trigger_pattern_logic = pattern_logic
        self.current_trigger.capture_trigger_error_logic = error_logic
        self.current_trigger.capture_trigger_frame_size_logic = frame_size_logic
        self.current_trigger.capture_trigger_frame_start_size = frame_start_size
        self.current_trigger.capture_trigger_frame_end_size = frame_end_size

    def add_capture_trigger_capture_async_trigger1(self, enable, da_logic, sa_logic, pattern_logic, error_logic,
                                                   frame_size_logic, frame_start_size, frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def add_capture_trigger_capture_async_trigger2(self, enable, da_logic, sa_logic, pattern_logic, error_logic,
                                                   frame_size_logic, frame_start_size, frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def add_capture_trigger_capture_user_defined_statistics1(self, enable, da_logic, sa_logic, pattern_logic,
                                                             error_logic, frame_size_logic, frame_start_size,
                                                             frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def add_capture_trigger_capture_user_defined_statistics2(self, enable, da_logic, sa_logic, pattern_logic,
                                                             error_logic, frame_size_logic, frame_start_size,
                                                             frame_end_size, options=None):
        return self.logger.log_unimplemented_method()

    def write_capture_trigger(self, port_handle, options=None):
        self.logger.log_info("TRIGGER")
        self.logger.log_info(self.current_filter)
        self.logger.log_info(self.current_trigger)
        self.capture_trigger_info[port_handle] = self.current_trigger


class ScapyDeviceCaptureFilterHelperInfo(object):
    def __init__(self):
        self.capture_filter_da1_da = None
        self.capture_filter_da1_da_mask = None
        self.capture_filter_da2_da = None
        self.capture_filter_da2_da_mask = None
        self.capture_filter_sa1_sa = None
        self.capture_filter_sa1_sa_mask = None
        self.capture_filter_sa2_sa = None
        self.capture_filter_sa2_sa_mask = None
        self.capture_filter_pattern1_pattern = None
        self.capture_filter_pattern1_pattern_mask = None
        self.capture_filter_pattern1_pattern_offset = None
        self.capture_filter_pattern1_pattern_offset_type = None
        self.capture_filter_pattern1_match_type = None
        self.capture_filter_pattern2_pattern = None
        self.capture_filter_pattern2_pattern_mask = None
        self.capture_filter_pattern2_pattern_offset = None
        self.capture_filter_pattern2_pattern_offset_type = None
        self.capture_filter_pattern2_match_type = None

    def matches(self, packet, logic_values):
        da = packet.get_destination_mac()
        sa = packet.get_source_mac()

        # daMatch = None
        # daMatch = None
        # if self.capture_filter_da1_da:
        #     self.check_value(da, 'mac', self.capture_filter_da1_da, self.capture_filter_da1_da_mask)
        # if self.capture_filter_da2_da:
        #     self.check_value(da, 'mac', self.capture_filter_da2_da, self.capture_filter_da2_da_mask)
        # if self.capture_filter_sa1_sa:
        #     self.check_value(sa, 'mac', self.capture_filter_sa1_sa, self.capture_filter_sa1_sa_mask)
        # if self.capture_filter_sa2_sa:
        #     self.check_value(sa, 'mac', self.capture_filter_sa2_sa, self.capture_filter_sa2_sa_mask)
        da_logic = True
        sa_logic = True
        pattern_logic = True
        error_logic = True
        size_logic = True
        if logic_values.capture_filter_da_logic:
            da_logic = self.packet_mac_field_with_logic(da, logic_values.capture_filter_da_logic,
                                                        self.capture_filter_da1_da, self.capture_filter_da1_da_mask,
                                                        self.capture_filter_da2_da, self.capture_filter_da2_da_mask)
        if logic_values.capture_filter_sa_logic:
            sa_logic = self.packet_mac_field_with_logic(sa, logic_values.capture_filter_sa_logic,
                                                        self.capture_filter_sa1_sa, self.capture_filter_sa1_sa_mask,
                                                        self.capture_filter_sa2_sa, self.capture_filter_sa2_sa_mask)
        if logic_values.capture_filter_pattern_logic:
            pattern_logic = self.packet_byte_field_with_logic(packet, logic_values.capture_filter_pattern_logic,
                                                              self.capture_filter_pattern1_pattern,
                                                              self.capture_filter_pattern1_pattern_mask,
                                                              self.capture_filter_pattern1_pattern_offset,
                                                              self.capture_filter_pattern1_pattern_offset_type,
                                                              self.capture_filter_pattern1_match_type,

                                                              self.capture_filter_pattern2_pattern,
                                                              self.capture_filter_pattern2_pattern_mask,
                                                              self.capture_filter_pattern2_pattern_offset,
                                                              self.capture_filter_pattern2_pattern_offset_type,
                                                              self.capture_filter_pattern2_match_type)
        return da_logic and sa_logic and pattern_logic and error_logic and size_logic

    @staticmethod
    def packet_mac_field_with_logic(value, logic, check1, check1_mask, check2, check2_mask):
        match_val = False
        logic = logic.lower()
        if logic == 'any':
            return True
        if '1' in logic:
            match_val1 = ScapyDeviceCaptureFilterHelperInfo.check_mac_value(value, check1, check1_mask)
            match_val = match_val1
        if '2' in logic:
            match_val2 = ScapyDeviceCaptureFilterHelperInfo.check_mac_value(value, check2, check2_mask)
            match_val = match_val2

        if 'or' in logic:
            match_val = match_val1 or match_val2
        elif '&' in logic:
            match_val = match_val1 and match_val2

        if 'not' in logic:
            return not match_val
        else:
            return match_val

    @staticmethod
    def check_mac_value(value, check1, check1_mask):
        mac1 = EnetAddress(value)
        mac2 = EnetAddress(check1)
        return mac1.equals(EnetAddress(check1), check1_mask)

    @staticmethod
    def packet_byte_field_with_logic(value, logic,
                                     pattern1_pattern,
                                     pattern1_pattern_mask,
                                     pattern1_pattern_offset,
                                     pattern1_pattern_offset_type,
                                     pattern1_match_type,

                                     pattern2_pattern,
                                     pattern2_pattern_mask,
                                     pattern2_pattern_offset,
                                     pattern2_pattern_offset_type,
                                     pattern2_match_type):
        match_val = False
        logic = logic.lower()
        if logic == 'any':
            return True
        if '1' in logic:
            match_val1 = ScapyDeviceCaptureFilterHelperInfo.check_byte_value(value, pattern1_pattern,
                                                                             pattern1_pattern_mask,
                                                                             pattern1_pattern_offset,
                                                                             pattern1_pattern_offset_type,
                                                                             pattern1_match_type)
            match_val = match_val1
        if '2' in logic:
            match_val2 = ScapyDeviceCaptureFilterHelperInfo.check_byte_value(value, pattern2_pattern,
                                                                             pattern2_pattern_mask,
                                                                             pattern2_pattern_offset,
                                                                             pattern2_pattern_offset_type,
                                                                             pattern2_match_type)
            match_val = match_val2

        if 'or' in logic:
            match_val = match_val1 or match_val2
        elif '&' in logic:
            match_val = match_val1 and match_val2

        if 'not' in logic:
            return not match_val
        else:
            return match_val

    @staticmethod
    def check_byte_value(value, pattern, pattern_mask, pattern_offset,
                         pattern_offset_type=PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_STARTOFFRAME,
                         match_type=PacketConfigFilterConstants.MATCH_TYPE1_USER):
        if match_type == PacketConfigFilterConstants.MATCH_TYPE1_USER:
            # PATTERN_OFFSET_TYPE1_CMD = "pattern_offset_type1"
            # # Constant values for PATTERN_OFFSET_TYPE1_CMD
            # PATTERN_OFFSET_TYPE1_STARTOFFRAME = "startOfFrame"
            # PATTERN_OFFSET_TYPE1_STARTOFIP = "startOfIp"
            # PATTERN_OFFSET_TYPE1_STARTOFPROTOCOL = "startOfProtocol"
            # PATTERN_OFFSET_TYPE1_STARTOFSONET = "startOfSonet"
            if pattern_offset_type is None or pattern_offset_type == \
                    PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_STARTOFFRAME:
                byte_offset = pattern_offset * 2
                pkt_bytes = value.get_captured_bytes()
                pattern = pattern.replace(":", "")
                val1 = pattern.replace(" ", "")
                val2 = pkt_bytes[byte_offset:byte_offset + len(pattern) - 1]
                pattern_mask = pattern_mask.replace(":", "")
                pattern_mask = pattern_mask.replace(" ", "")
                pattern_mask = StringUtils.rzfill(pattern_mask, len(val1))
                matches = True
                while matches and len(val1) > 0:
                    o1 = int(val1[::2], 16)
                    val1 = val1[2::]
                    o2 = int(val2[::2], 16)
                    val2 = val2[2::]
                    o_mask = ~int(pattern_mask[::2], 16)
                    pattern_mask = pattern_mask[2::]
                    matches = matches and ((o1 & o_mask) == (o2 & o_mask))
                return matches


class ScapyDeviceCaptureTriggerHelperInfo(object):
    def __init__(self):
        self.capture_filter_enable = None
        self.capture_filter_da_logic = None
        self.capture_filter_sa_logic = None
        self.capture_filter_pattern_logic = None
        self.capture_filter_error_logic = None
        self.capture_filter_frame_size_logic = None
        self.capture_filter_frame_start_size = None
        self.capture_filter_frame_end_size = None
        self.capture_trigger_enable = None
        self.capture_trigger_da_logic = None
        self.capture_trigger_sa_logic = None
        self.capture_trigger_pattern_logic = None
        self.capture_trigger_error_logic = None
        self.capture_trigger_frame_size_logic = None
        self.capture_trigger_frame_start_size = None
        self.capture_trigger_frame_end_size = None

    def matches(self, packet, filter_values):
        if self.capture_filter_enable:
            if self.capture_filter_da_logic.lower() == 'any' and \
                    self.capture_filter_da_logic.capture_filter_sa_logic.lower() == 'any' and \
                    self.capture_filter_da_logic.capture_filter_pattern_logic.lower() == 'any' and \
                    self.capture_filter_da_logic.capture_filter_error_logic.lower() == 'any':
                return True
            assert isinstance(filter_values, ScapyDeviceCaptureFilterHelperInfo)

            da = packet.get_destination_mac()
            sa = packet.get_source_mac()

            da_logic = True
            sa_logic = True
            pattern_logic = True
            error_logic = True
            size_logic = True
            if self.capture_trigger_da_logic:
                da_logic = filter_values.packet_mac_field_with_logic(da, self.capture_trigger_da_logic,
                                                                     filter_values.capture_filter_da1_da,
                                                                     filter_values.capture_filter_da1_da_mask,
                                                                     filter_values.capture_filter_da2_da,
                                                                     filter_values.capture_filter_da2_da_mask)
            if self.capture_trigger_sa_logic:
                sa_logic = filter_values.packet_mac_field_with_logic(sa, self.capture_trigger_sa_logic,
                                                                     filter_values.capture_filter_sa1_sa,
                                                                     filter_values.capture_filter_sa1_sa_mask,
                                                                     filter_values.capture_filter_sa2_sa,
                                                                     filter_values.capture_filter_sa2_sa_mask)
            if self.capture_trigger_pattern_logic:
                pattern_logic = filter_values.packet_byte_field_with_logic(
                    sa, self.capture_trigger_pattern_logic,
                    filter_values.capture_filter_pattern1_pattern,
                    filter_values.capture_filter_pattern1_pattern_mask,
                    filter_values.capture_filter_pattern1_pattern_offset,
                    filter_values.capture_filter_pattern1_pattern_offset_type,
                    filter_values.capture_filter_pattern1_match_type,

                    filter_values.capture_filter_pattern2_pattern,
                    filter_values.capture_filter_pattern2_pattern_mask,
                    filter_values.capture_filter_pattern2_pattern_offset,
                    filter_values.capture_filter_pattern2_pattern_offset_type,
                    filter_values.capture_filter_pattern2_match_type)
            return da_logic and sa_logic and pattern_logic and error_logic and size_logic
