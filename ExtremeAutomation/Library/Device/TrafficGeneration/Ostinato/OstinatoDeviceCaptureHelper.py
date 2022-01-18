from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import \
    PacketConfigFilterConstants
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceCaptureHelper import \
    TrafficGeneratingDeviceCaptureHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import DroneProxy
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class OstinatoDeviceCaptureHelper(TrafficGeneratingDeviceCaptureHelper):
    def __init__(self, ixia_device):
        super(OstinatoDeviceCaptureHelper, self).__init__(ixia_device)
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
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_uds2_frame_count(self, port_string, options=None):
        if options is None:
            options = {}
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
    #     {frame {00 00 00 00 00 11 00 00 00 00 00 22 08 00 45 00 00 2E 00 00 00 00 40 FF 73 CC 02 02 02 02 01 01 01
    #             01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 01 00 00 1E 85 08 A7 D7 E0 E8 16}}
    # {status cap10100DpmGoodPacket} {fir 11040700320} {latency 0} {length 64} {time_stamp 9209078740}
    #     {frame {00 00 00 00 00 11 00 00 00 00 00 33 08 00 45 00 00 2E 00 00 00 00 40 FF 71 CA 03 03 03 03 01 01 01
    #             01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 02 00 00 20 E7 62 C8 BA 9F 55 F9}}}}
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
        assert isinstance(self.connection, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        buff = self.dev.connection.getCaptureBuffer(port_string.port_id[0])
        if buff:
            packetsCaptured = PacketClassifier.process_pcap_file_contents(buff)
            return packetsCaptured[frame_num - 1].get_bytes()
        else:
            return None

    def get_unfiltered_captured_frame_count(self, port_handle, options=None):
        return len(self.get_all_unfiltered_captured_frames(port_handle))

    def get_all_unfiltered_captured_frames(self, port_handle, options=None):
        if self.capture_buffer.is_capture_buffer_filled(port_handle):
            return self.capture_buffer.get_stored_capture_buffer(port_handle)
        if options is None:
            options = {}
        packetsCaptured = []
        assert isinstance(self.connection, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        buff = self.dev.connection.getCaptureBuffer(port_string.port_id[0])
        if buff:
            packetsCaptured = PacketClassifier.process_pcap_file_contents(buff)
        return str(packetsCaptured)

    def get_captured_frame_count(self, port_handle,options=None):
        return len(self.get_all_captured_frames(port_handle))

    def get_captured_frame(self, port_string, frame_num):
        return self.get_all_captured_frames(port_string)[frame_num - 1]

    def get_captured_frames(self, port_string, first_frame_num, last_frame_num):
        return self.get_all_captured_frames(port_string)[first_frame_num -1:last_frame_num - 1]

    def get_all_captured_frames(self, port_handle, options=None):
        Logger().log_debug("get_all_captured_frames")
        if self.capture_buffer.is_capture_buffer_filled(port_handle):
            return self.capture_buffer.get_stored_capture_buffer(port_handle)
        if options is None:
            options = {}
        assert isinstance(self.connection, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_handle)
        buff = self.dev.connection.getCaptureBuffer(port_string.port_id[0])
        if buff:
            Logger().log_debug("\tprocessing capture")
            packetsCaptured = PacketClassifier.process_pcap_file_contents(buff)
            Logger().log_debug("\ttotal captured " + str(len(packetsCaptured)))
            is_trigger_set = port_handle in self.capture_trigger_info
            is_capture_set = port_handle in  self.capture_filter_info
            # if trigger is set or capture is set to something that isn't ANY,
            # We have to do work
            if is_trigger_set or is_capture_set:
                temp_cap = []
                trigger_found = True
                if is_trigger_set:
                    trigger_found = False
                packet_index = 0
                for packet in packetsCaptured:
                    Logger().log_debug("Port " + str(port_handle) + " Packet " + str(packet_index) + ") " +
                                       packet.get_name() + " DA=" + str(packet.get_destination_mac()) + " SA=" +
                                       str(packet.get_source_mac() ))
                    packet_index += 1
                    # if is_trigger_set, loop until trigger is found
                    if is_trigger_set and not trigger_found:
                        # trigger_found = check triggers
                        # otherwise,
                        # check for all Any if all Any, it matches
                        trigger_found = self.capture_trigger_info[port_handle].matches(
                            packet, self.capture_filter_info[port_handle])
                        Logger().log_debug("Port " + str(port_handle) + " Packet " + str(packet_index) +
                                           ") Trigger hit=" + str(trigger_found))
                        if not trigger_found:
                            continue
                        trigger_found = packet_index
                        # print "triggered at packet #"+str(packet_index)
                    # once trigger_found you get here
                    # capture_match = check captures
                    if port_handle in self.capture_trigger_info:
                        capture_match = self.capture_filter_info[port_handle].matches(
                            packet,self.capture_trigger_info[port_handle])
                    else:
                        capture_match = True
                    Logger().log_debug("Port " + str(port_handle) + " Packet " + str(packet_index) +
                                       ") capture matched = " + str(capture_match))
                    if not is_capture_set or capture_match:
                        temp_cap.append(packet)
                    # else:
                    #     print "packet #"+str(packet_index) + " didn't matched " + packet.get_destination_mac() +
                    #           "/" + packet.get_source_mac()
                Logger().log_debug("\ttotal return filtered packets " + str(len(temp_cap)))
                return temp_cap
            Logger().log_debug("\ttotal return packets " + str(len(packetsCaptured)))
            return packetsCaptured
        else:
            Logger().log_debug("\tcapture buffer is empty")
            return []

    def clear_capture_filters_and_triggers(self, port_string):
        self.dev.clear_capture_filters_and_triggers(port_string)
        if port_string in self.capture_filter_info:
            self.capture_filter_info[port_string] = OstinatoDeviceCaptureFilterHelperInfo()
        if port_string in self.capture_trigger_info:
            self.capture_trigger_info[port_string] = OstinatoDeviceCaptureFilterHelperInfo()

    def set_capture_filter_da1(self, port_handle, da, daMask, options=None):
        if port_handle not in self.capture_filter_info:
            self.capture_filter_info[port_handle] = OstinatoDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_da1_da = da
        self.capture_filter_info[port_handle].capture_filter_da1_daMask = daMask

    def set_capture_filter_da2(self, port_handle, da, daMask, options=None):
        if port_handle not in self.capture_filter_info:
            self.capture_filter_info[port_handle] = OstinatoDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_da2_da = da
        self.capture_filter_info[port_handle].capture_filter_da2_daMask = daMask

    def set_capture_filter_sa1(self, port_handle, sa, saMask, options=None):
        if not port_handle in self.capture_filter_info:
            self.capture_filter_info[port_handle] = OstinatoDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_sa1_sa = sa
        self.capture_filter_info[port_handle].capture_filter_sa1_saMask = saMask

    def set_capture_filter_sa2(self, port_handle, sa, saMask, options=None):
        if not port_handle in self.capture_filter_info:
            self.capture_filter_info[port_handle] = OstinatoDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_sa2_sa = sa
        self.capture_filter_info[port_handle].capture_filter_sa2_saMask = saMask

    def set_capture_filter_pattern1(self, port_handle, pattern, patternMask, patternOffest, pattern_offset_type,
                                    match_type, options=None):
        if not port_handle in self.capture_filter_info:
            self.capture_filter_info[port_handle] = OstinatoDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_pattern1_pattern = pattern
        self.capture_filter_info[port_handle].capture_filter_pattern1_patternMask = patternMask
        self.capture_filter_info[port_handle].capture_filter_pattern1_patternOffest = patternOffest
        self.capture_filter_info[port_handle].capture_filter_pattern1_pattern_offset_type = pattern_offset_type
        self.capture_filter_info[port_handle].capture_filter_pattern1_match_type = match_type

    def set_capture_filter_pattern2(self, port_handle, pattern, patternMask, patternOffest, pattern_offset_type,
                                    match_type, options=None):
        if not port_handle in self.capture_filter_info:
            self.capture_filter_info[port_handle] = OstinatoDeviceCaptureFilterHelperInfo()
        self.capture_filter_info[port_handle].capture_filter_pattern2_pattern = pattern
        self.capture_filter_info[port_handle].capture_filter_pattern2_patternMask = patternMask
        self.capture_filter_info[port_handle].capture_filter_pattern2_patternOffest = patternOffest
        self.capture_filter_info[port_handle].capture_filter_pattern2_pattern_offset_type = pattern_offset_type
        self.capture_filter_info[port_handle].capture_filter_pattern2_match_type = match_type

    def set_capture_filter_pattern_atm(self, port_handle, pattern, patternMask, patternOffest, options=None):
        return self.logger.log_unimplemented_method()

    def get_capture_filter(self, port_string):
        if port_string not in self.capture_filter_info:
            self.capture_filter_info[port_string] = OstinatoDeviceCaptureFilterHelperInfo()
        self.current_filter = self.capture_filter_info[port_string]

    def get_capture_filter_default(self):
        self.current_filter = OstinatoDeviceCaptureFilterHelperInfo()

    def add_capture_filter_da1(self, da, daMask, options=None):
        self.current_filter.capture_filter_da1_da = da
        self.current_filter.capture_filter_da1_daMask = daMask

    def add_capture_filter_da2(self, da, daMask, options=None):
        self.current_filter.capture_filter_da2_da = da
        self.current_filter.capture_filter_da2_daMask = daMask

    def add_capture_filter_sa1(self, sa, saMask, options=None):
        self.current_filter.capture_filter_sa1_sa = sa
        self.current_filter.capture_filter_sa1_saMask = saMask

    def add_capture_filter_sa2(self, sa, saMask, options=None):
        self.current_filter.capture_filter_sa2_sa = sa
        self.current_filter.capture_filter_sa2_saMask = saMask

    def add_capture_filter_pattern1(self, pattern, patternMask, patternOffest, pattern_offset_type, match_type,
                                    options=None):
        self.current_filter.capture_filter_pattern1_pattern = pattern
        self.current_filter.capture_filter_pattern1_patternMask = patternMask
        self.current_filter.capture_filter_pattern1_patternOffest = patternOffest
        self.current_filter.capture_filter_pattern1_pattern_offset_type = pattern_offset_type
        self.current_filter.capture_filter_pattern1_match_type = match_type

    def add_capture_filter_pattern2(self, pattern, patternMask, patternOffest, pattern_offset_type, match_type,
                                    options=None):
        self.current_filter.capture_filter_pattern2_pattern = pattern
        self.current_filter.capture_filter_pattern2_patternMask = patternMask
        self.current_filter.capture_filter_pattern2_patternOffest = patternOffest
        self.current_filter.capture_filter_pattern2_pattern_offset_type = pattern_offset_type
        self.current_filter.capture_filter_pattern2_match_type = match_type

    def add_capture_filter_pattern_atm(self, pattern, patternMask, patternOffest, options=None):
        return self.logger.log_unimplemented_method()

    def write_capture_filter(self, port_handle, options=None):
        self.capture_filter_info[port_handle] = self.current_filter

    def set_capture_filter(self, port_handle,enable, daLogic, saLogic, errorLogic, frameSizeLogic, frameStartSize,
                           frameEndSize, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_trigger(self, port_handle, enable, daLogic, saLogic, errorLogic, frameSizeLogic, frameStartSize,
                            frameEndSize, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_async_trigger1(self, port_handle, enable, daLogic, saLogic, errorLogic, frameSizeLogic,
                                   frameStartSize, frameEndSize, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_async_trigger2(self, port_handle, enable, daLogic, saLogic, errorLogic, frameSizeLogic,
                                   frameStartSize, frameEndSize, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_user_defined_statistics1(self, port_handle, enable, daLogic, saLogic, errorLogic, frameSizeLogic,
                                             frameStartSize, frameEndSize, options=None):
        return self.logger.log_unimplemented_method()

    def set_capture_user_defined_statistics2(self, port_handle, enable, daLogic, saLogic, errorLogic, frameSizeLogic,
                                             frameStartSize, frameEndSize, options=None):
        return self.logger.log_unimplemented_method()

    def get_capture_trigger(self, port_string):
        if port_string not in self.capture_trigger_info:
            self.capture_trigger_info[port_string] = OstinatoDeviceCaptureTriggerHelperInfo()
        self.current_trigger = self.capture_trigger_info[port_string]

    def get_capture_trigger_default(self):
        self.current_trigger = OstinatoDeviceCaptureTriggerHelperInfo()

    def add_capture_trigger_capture_filter(self, enable, daLogic, saLogic, patternLogic, errorLogic, frameSizeLogic,
                                           frameStartSize, frameEndSize, options=None):
        if self.current_trigger is None:
            self.current_trigger = OstinatoDeviceCaptureTriggerHelperInfo()
        self.current_trigger.capture_filter_enable = enable
        self.current_trigger.capture_filter_daLogic = daLogic
        self.current_trigger.capture_filter_saLogic = saLogic
        self.current_trigger.capture_filter_patternLogic = patternLogic
        self.current_trigger.capture_filter_errorLogic = errorLogic
        self.current_trigger.capture_filter_frameSizeLogic = frameSizeLogic
        self.current_trigger.capture_filter_frameStartSize = frameStartSize
        self.current_trigger.capture_filter_frameEndSize = frameEndSize

    def add_capture_trigger_capture_trigger(self, enable, daLogic, saLogic, patternLogic, errorLogic, frameSizeLogic,
                                            frameStartSize, frameEndSize, options=None):
        if self.current_trigger is None:
            self.current_trigger = OstinatoDeviceCaptureTriggerHelperInfo()
        self.current_trigger.capture_trigger_enable = enable
        self.current_trigger.capture_trigger_daLogic = daLogic
        self.current_trigger.capture_trigger_saLogic = saLogic
        self.current_trigger.capture_trigger_patternLogic = patternLogic
        self.current_trigger.capture_trigger_errorLogic = errorLogic
        self.current_trigger.capture_trigger_frameSizeLogic = frameSizeLogic
        self.current_trigger.capture_trigger_frameStartSize = frameStartSize
        self.current_trigger.capture_trigger_frameEndSize = frameEndSize

    def add_capture_trigger_capture_async_trigger1(self, enable, daLogic, saLogic, patternLogic, errorLogic,
                                                   frameSizeLogic, frameStartSize, frameEndSize, options=None):
        return self.logger.log_unimplemented_method()

    def add_capture_trigger_capture_async_trigger2(self, enable, daLogic, saLogic, patternLogic, errorLogic,
                                                   frameSizeLogic, frameStartSize, frameEndSize, options=None):
        return self.logger.log_unimplemented_method()

    def add_capture_trigger_capture_user_defined_statistics1(self, enable, daLogic, saLogic, patternLogic, errorLogic,
                                                             frameSizeLogic, frameStartSize, frameEndSize,
                                                             options=None):
        return self.logger.log_unimplemented_method()

    def add_capture_trigger_capture_user_defined_statistics2(self, enable, daLogic, saLogic, patternLogic, errorLogic,
                                                             frameSizeLogic, frameStartSize, frameEndSize,
                                                             options=None):
        return self.logger.log_unimplemented_method()

    def write_capture_trigger(self, port_handle, options=None):
        Logger().log_debug("TRIGGER")
        Logger().log_debug(str(self.current_filter))
        Logger().log_debug(str(self.current_trigger))
        self.capture_trigger_info[port_handle] = self.current_trigger

    def get_capture_filter_and_trigger_settings(self, port_string):
        capture_filter = self.capture_filter_info[port_string]
        capture_trigger = self.capture_trigger_info[port_string]
        return "Port " + str(port_string) + "\nCapture Filters:" + str(capture_filter) + "\nCapture Trigger" + \
               str(capture_trigger)

        # for key, value in reportCount.items():
        #         frame = reportPacket[key]
        #         table.add_row_value("Packet Type", frame.get_name())
        #         table.add_row_value("DA", frame.get_destination_mac())
        #         table.add_row_value("SA", frame.get_source_mac())
        #         table.add_row_value("Count", reportCount[key])
        # return table.to_table_string()


class OstinatoDeviceCaptureFilterHelperInfo(object):
    def __init__(self):
        self.capture_filter_da1_da = None
        self.capture_filter_da1_daMask = None
        self.capture_filter_da2_da = None
        self.capture_filter_da2_daMask = None
        self.capture_filter_sa1_sa = None
        self.capture_filter_sa1_saMask = None
        self.capture_filter_sa2_sa = None
        self.capture_filter_sa2_saMask = None
        self.capture_filter_pattern1_pattern = None
        self.capture_filter_pattern1_patternMask = None
        self.capture_filter_pattern1_patternOffest = None
        self.capture_filter_pattern1_pattern_offset_type = None
        self.capture_filter_pattern1_match_type = None
        self.capture_filter_pattern2_pattern = None
        self.capture_filter_pattern2_patternMask = None
        self.capture_filter_pattern2_patternOffest = None
        self.capture_filter_pattern2_pattern_offset_type = None
        self.capture_filter_pattern2_match_type = None

    def matches(self, packet, logic_values):
        da = packet.get_destination_mac()
        sa = packet.get_source_mac()

        # daMatch = None
        # daMatch = None
        # if self.capture_filter_da1_da:
        #     self.check_value(da, 'mac', self.capture_filter_da1_da, self.capture_filter_da1_daMask)
        # if self.capture_filter_da2_da:
        #     self.check_value(da, 'mac', self.capture_filter_da2_da, self.capture_filter_da2_daMask)
        # if self.capture_filter_sa1_sa:
        #     self.check_value(sa, 'mac', self.capture_filter_sa1_sa, self.capture_filter_sa1_saMask)
        # if self.capture_filter_sa2_sa:
        #     self.check_value(sa, 'mac', self.capture_filter_sa2_sa, self.capture_filter_sa2_saMask)
        daLogic = True
        saLogic = True
        patterLogic = True
        errorLogic = True
        sizeLogic = True
        if logic_values.capture_filter_daLogic:
            daLogic = self.packet_mac_field_with_logic(da, logic_values.capture_filter_daLogic,
                                                       self.capture_filter_da1_da, self.capture_filter_da1_daMask,
                                                       self.capture_filter_da2_da, self.capture_filter_da2_daMask)
            Logger().log_debug("Filter daLogic: result " + str(daLogic) + ":" + str(da) + ", " +
                               str(logic_values.capture_filter_daLogic) + ", " +str(self.capture_filter_da1_da) + ", " +
                               str(self.capture_filter_da1_daMask) + ", " + str(self.capture_filter_da2_da) + ", " +
                               str(self.capture_filter_da2_daMask))
        if logic_values.capture_filter_saLogic:
            saLogic = self.packet_mac_field_with_logic(sa, logic_values.capture_filter_saLogic,
                                                       self.capture_filter_sa1_sa, self.capture_filter_sa1_saMask,
                                                       self.capture_filter_sa2_sa, self.capture_filter_sa2_saMask)
            Logger().log_debug("Filter saLogic: result " + str(saLogic) + ":" + str(sa) + ", " +
                               str(logic_values.capture_filter_saLogic) + ", " +str(self.capture_filter_sa1_sa) + ", " +
                               str(self.capture_filter_sa1_saMask) + ", " +str(self.capture_filter_sa2_sa) + ", " +
                               str(self.capture_filter_sa2_saMask))
        if logic_values.capture_filter_patternLogic:
            patterLogic = self.packet_byte_field_with_logic(packet, logic_values.capture_filter_patternLogic,
                                                            # Pattern 1
                                                            self.capture_filter_pattern1_pattern,
                                                            self.capture_filter_pattern1_patternMask,
                                                            self.capture_filter_pattern1_patternOffest,
                                                            self.capture_filter_pattern1_pattern_offset_type,
                                                            self.capture_filter_pattern1_match_type,
                                                            # Pattern 2
                                                            self.capture_filter_pattern2_pattern,
                                                            self.capture_filter_pattern2_patternMask,
                                                            self.capture_filter_pattern2_patternOffest,
                                                            self.capture_filter_pattern2_pattern_offset_type,
                                                            self.capture_filter_pattern2_match_type)

            Logger().log_debug("Filter patterLogic: result " + str(patterLogic) + ":" +
                               str(logic_values.capture_filter_patternLogic) + ", " +
                               str(self.capture_filter_pattern1_pattern) + ", " +
                               str(self.capture_filter_pattern1_patternMask) + ", " +
                               str(self.capture_filter_pattern1_patternOffest) + ", " +
                               str(self.capture_filter_pattern1_pattern_offset_type) + ", " +
                               str(self.capture_filter_pattern1_match_type) + ", " +
                               str(self.capture_filter_pattern2_pattern) + ", " +
                               str(self.capture_filter_pattern2_patternMask) + ", " +
                               str(self.capture_filter_pattern2_patternOffest) + ", " +
                               str(self.capture_filter_pattern2_pattern_offset_type) + ", " +
                               str(self.capture_filter_pattern2_match_type))
            Logger().log_debug("Payload:" + str(packet.get_bytes()))
        return daLogic and saLogic and patterLogic and errorLogic and sizeLogic

    def packet_mac_field_with_logic(self, value, logic, check1, check1_mask, check2, check2_mask):
        match_val = False
        logic = logic.lower()
        if logic == 'any':
            return True
        if '1' in logic:
            match_val1 = OstinatoDeviceCaptureFilterHelperInfo.check_mac_value(value, check1, check1_mask)
            match_val = match_val1
        if '2' in logic:
            match_val2 = OstinatoDeviceCaptureFilterHelperInfo.check_mac_value(value, check2, check2_mask)
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

    def packet_byte_field_with_logic(self, value, logic,
                                     pattern1_pattern,
                                     pattern1_patternMask,
                                     pattern1_patternOffest,
                                     pattern1_pattern_offset_type,
                                     pattern1_match_type,
                                     pattern2_pattern,
                                     pattern2_patternMask,
                                     pattern2_patternOffest,
                                     pattern2_pattern_offset_type,
                                     pattern2_match_type):
        match_val = False
        logic = logic.lower()
        if logic == 'any':
            return True
        if '1' in logic:
            match_val1 = OstinatoDeviceCaptureFilterHelperInfo.check_byte_value(value, pattern1_pattern,
                                                                                pattern1_patternMask,
                                                                                pattern1_patternOffest,
                                                                                pattern1_pattern_offset_type,
                                                                                pattern1_match_type)
            match_val = match_val1
        if '2' in logic:
            match_val2 = OstinatoDeviceCaptureFilterHelperInfo.check_byte_value(value, pattern2_pattern,
                                                                                pattern2_patternMask,
                                                                                pattern2_patternOffest,
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
    def check_byte_value(value, pattern, patternMask, patternOffest,
                         pattern_offset_type=PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_STARTOFFRAME,
                         match_type=PacketConfigFilterConstants.MATCH_TYPE1_USER):
        if match_type is None or match_type == PacketConfigFilterConstants.MATCH_TYPE1_USER:
            # PATTERN_OFFSET_TYPE1_CMD = "pattern_offset_type1"
            # # Constant values for PATTERN_OFFSET_TYPE1_CMD
            # PATTERN_OFFSET_TYPE1_STARTOFFRAME = "startOfFrame"
            # PATTERN_OFFSET_TYPE1_STARTOFIP = "startOfIp"
            # PATTERN_OFFSET_TYPE1_STARTOFPROTOCOL = "startOfProtocol"
            # PATTERN_OFFSET_TYPE1_STARTOFSONET = "startOfSonet"
            if pattern_offset_type is None or \
                    pattern_offset_type == PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_STARTOFFRAME:
                byte_offset = int(patternOffest) * 2
                bytes = value.get_captured_bytes()
                pattern = pattern.replace(":", "")
                val1 = pattern.replace(" ", "")
                while len(pattern) % 2 > 0:
                    pattern = "0" + pattern
                val2 = bytes[byte_offset:byte_offset + len(pattern)]
                if not patternMask:
                    patternMask = "0"
                patternMask = patternMask.replace(":", "")
                patternMask = patternMask.replace(" ", "")
                patternMask = StringUtils.rzfill(patternMask, len(val1))
                matches = True
                while matches and len(val1) > 0:
                    o1 = int(val1[0:2], 16)
                    val1 = val1[2::]
                    o2 = int(val2[0:2], 16)
                    val2 = val2[2::]
                    oMask = ~int(patternMask[::2], 16)
                    patternMask = patternMask[2::]
                    matches = matches and ((o1 & oMask) == (o2 & oMask))
                return matches

    def __str__(self):
        return "\tDA1 da:" + str(self.capture_filter_da1_da) + "\n" + \
            "\tDA1 daMask:" + str(self.capture_filter_da1_daMask) + "\n" + \
            "\tDA2 da:" + str(self.capture_filter_da2_da) + "\n" + \
            "\tDA2 daMask:" + str(self.capture_filter_da2_daMask) + "\n" + \
            "\tSA1 sa:" + str(self.capture_filter_sa1_sa) + "\n" + \
            "\tSA1 saMask:" + str(self.capture_filter_sa1_saMask) + "\n" + \
            "\tSA2 sa:" + str(self.capture_filter_sa2_sa) + "\n" + \
            "\tSA2 saMask" + str(self.capture_filter_sa2_saMask) + "\n" + \
            "\tpattern 1 pattern:" + str(self.capture_filter_pattern1_pattern) + "\n" + \
            "\tpattern 1 patternMask:" + str(self.capture_filter_pattern1_patternMask) + "\n" + \
            "\tpattern 1 pattern Offset:" + str(self.capture_filter_pattern1_patternOffest) + "\n" + \
            "\tpattern 1 pattern Offset Type:" + str(self.capture_filter_pattern1_pattern_offset_type) + "\n" + \
            "\tpattern 1 match type:" + str(self.capture_filter_pattern1_match_type) + "\n" + \
            "\tpattern 2 pattern:" + str(self.capture_filter_pattern2_pattern) + "\n" + \
            "\tpattern 2 patternMask:" + str(self.capture_filter_pattern2_patternMask) + "\n" + \
            "\tpattern 2 pattern Offset:" + str(self.capture_filter_pattern2_patternOffest) + "\n" + \
            "\tpattern 2 offset type:" + str(self.capture_filter_pattern2_pattern_offset_type) + "\n" + \
            "\tPattern 2 match type:" + str(self.capture_filter_pattern2_match_type)


class OstinatoDeviceCaptureTriggerHelperInfo(object):
    def __init__(self):
        self.capture_filter_enable = None
        self.capture_filter_daLogic = None
        self.capture_filter_saLogic = None
        self.capture_filter_patternLogic = None
        self.capture_filter_errorLogic = None
        self.capture_filter_frameSizeLogic = None
        self.capture_filter_frameStartSize = None
        self.capture_filter_frameEndSize = None
        self.capture_trigger_enable = None
        self.capture_trigger_daLogic = None
        self.capture_trigger_saLogic = None
        self.capture_trigger_patternLogic = None
        self.capture_trigger_errorLogic = None
        self.capture_trigger_frameSizeLogic = None
        self.capture_trigger_frameStartSize = None
        self.capture_trigger_frameEndSize = None

    def matches(self, packet, filter_values):
        if self.capture_filter_enable:
            if self.capture_filter_daLogic.lower() == 'any' and \
                    self.capture_filter_daLogic.capture_filter_saLogic.lower() == 'any' and \
                    self.capture_filter_daLogic.capture_filter_patternLogic.lower() == 'any' and \
                    self.capture_filter_daLogic.capture_filter_errorLogic.lower() == 'any':
                return True
            assert isinstance(filter_values, OstinatoDeviceCaptureFilterHelperInfo)

            da = packet.get_destination_mac()
            sa = packet.get_source_mac()

            daLogic = True
            saLogic = True
            patterLogic = True
            errorLogic = True
            sizeLogic = True
            if self.capture_trigger_daLogic:
                daLogic = filter_values.packet_mac_field_with_logic(da, self.capture_trigger_daLogic,
                                                                    filter_values.capture_filter_da1_da,
                                                                    filter_values.capture_filter_da1_daMask,
                                                                    filter_values.capture_filter_da2_da,
                                                                    filter_values.capture_filter_da2_daMask)
                Logger().log_debug("Trigger daLogic: result " + str(daLogic) + ":" + str(da) + ", " +
                                   str(self.capture_trigger_daLogic) + ", " +
                                   str(filter_values.capture_filter_da1_da) + ", " +
                                   str(filter_values.capture_filter_da1_daMask) + ", " +
                                   str(filter_values.capture_filter_da2_da) + ", " +
                                   str(filter_values.capture_filter_da2_daMask))

            if self.capture_trigger_saLogic:
                saLogic = filter_values.packet_mac_field_with_logic(sa, self.capture_trigger_saLogic,
                                                                    filter_values.capture_filter_sa1_sa,
                                                                    filter_values.capture_filter_sa1_saMask,
                                                                    filter_values.capture_filter_sa2_sa,
                                                                    filter_values.capture_filter_sa2_saMask)
                Logger().log_debug("Trigger saLogic: result " + str(saLogic) + ":" + str(sa) + ", " +
                                   str(self.capture_trigger_saLogic) + ", " +
                                   str(filter_values.capture_filter_sa1_sa) + ", " +
                                   str(filter_values.capture_filter_sa1_saMask) + ", " +
                                   str(filter_values.capture_filter_sa2_sa) + ", " +
                                   str(filter_values.capture_filter_sa2_saMask))

            if self.capture_trigger_patternLogic:
                patterLogic = filter_values.packet_byte_field_with_logic(
                    packet, self.capture_trigger_patternLogic,
                    # Pattern 1
                    filter_values.capture_filter_pattern1_pattern,
                    filter_values.capture_filter_pattern1_patternMask,
                    filter_values.capture_filter_pattern1_patternOffest,
                    filter_values.capture_filter_pattern1_pattern_offset_type,
                    filter_values.capture_filter_pattern1_match_type,
                    # Pattern 2
                    filter_values.capture_filter_pattern2_pattern,
                    filter_values.capture_filter_pattern2_patternMask,
                    filter_values.capture_filter_pattern2_patternOffest,
                    filter_values.capture_filter_pattern2_pattern_offset_type,
                    filter_values.capture_filter_pattern2_match_type)
                Logger().log_debug("Trigger patterLogic: result " + str(patterLogic) + ":" +
                                   str(self.capture_filter_patternLogic) + ", " +
                                   str(filter_values.capture_filter_pattern1_pattern) + ", " +
                                   str(filter_values.capture_filter_pattern1_patternMask) + ", " +
                                   str(filter_values.capture_filter_pattern1_patternOffest) + ", " +
                                   str(filter_values.capture_filter_pattern1_pattern_offset_type) + ", " +
                                   str(filter_values.capture_filter_pattern1_match_type) + ", " +
                                   str(filter_values.capture_filter_pattern2_pattern) + ", " +
                                   str(filter_values.capture_filter_pattern2_patternMask) + ", " +
                                   str(filter_values.capture_filter_pattern2_patternOffest) + ", " +
                                   str(filter_values.capture_filter_pattern2_pattern_offset_type) + ", " +
                                   str(filter_values.capture_filter_pattern2_match_type))
                Logger().log_debug("Payload:" +str(packet.get_bytes()))
            return daLogic and saLogic and patterLogic and errorLogic and sizeLogic

    def __str__(self):
        return "\tcapture_filter_enable:" + str(self.capture_filter_enable) + "\n" + \
            "\tcapture_filter_daLogic:" + str(self.capture_filter_daLogic) + "\n" + \
            "\tcapture_filter_saLogic:" + str(self.capture_filter_saLogic) + "\n" + \
            "\tcapture_filter_patternLogic:" + str(self.capture_filter_patternLogic) + "\n" + \
            "\tcapture_filter_errorLogic:" + str(self.capture_filter_errorLogic) + "\n" + \
            "\tcapture_filter_frameSizeLogic:" + str(self.capture_filter_frameSizeLogic) + "\n" + \
            "\tcapture_filter_frameStartSize:" + str(self.capture_filter_frameStartSize) + "\n" + \
            "\tcapture_filter_frameEndSize:" + str(self.capture_filter_frameEndSize) + "\n" + \
            "\tcapture_trigger_enable):" + str(self.capture_trigger_enable) + "\n" + \
            "\tcapture_trigger_daLogic:" + str(self.capture_trigger_daLogic) + "\n" + \
            "\tcapture_trigger_saLogic:" + str(self.capture_trigger_saLogic) + "\n" + \
            "\tcapture_trigger_patternLogic:" + str(self.capture_trigger_patternLogic) + "\n" + \
            "\tcapture_trigger_errorLogic:" + str(self.capture_trigger_errorLogic) + "\n" + \
            "\tcapture_trigger_frameSizeLogic:" + str(self.capture_trigger_frameSizeLogic) + "\n" + \
            "\tcapture_trigger_frameStartSize:" + str(self.capture_trigger_frameStartSize) + "\n" + \
            "\tcapture_trigger_frameEndSize:" + str(self.capture_trigger_frameEndSize)

