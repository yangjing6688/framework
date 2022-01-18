import abc
import random
import re
import string
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import \
    PacketConfigFilterApi, PacketConfigFilterConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import \
    PacketConfigTriggersConstants, PacketConfigTriggersApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketStatsApi import PacketStatsConstants, \
    PacketStatsApi
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceCaptureHelper import \
    TrafficGeneratingDeviceCaptureHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier


class HltapiTrafficGeneratingDeviceCaptureHelper(TrafficGeneratingDeviceCaptureHelper, metaclass=abc.ABCMeta):
    def __init__(self, ixia_device):
        super(HltapiTrafficGeneratingDeviceCaptureHelper, self).__init__(ixia_device)

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
    #   {status cap10100DpmGoodPacket} {fir 11040700320} {latency 0} {length 64} {time_stamp 9209078740}
    #       {frame {00 00 00 00 00 11 00 00 00 00 00 33 08 00 45 00 00 2E 00 00 00 00 40 FF 71 CA 03 03 03 03 01 01
    #               01 01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 02 00 00 20 E7 62 C8 BA 9F 55 F9}}}}
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
        packet = self.get_captured_frame(port_string, frame_num, options)
        packet_string = packet.get_captured_bytes()
        if " " not in packet_string:
            packet_string = StringUtils.place_character_every_n_characters(packet_string, " ", 2)
        return packet_string

    def get_port_capture_frame_frame_data_in_bytes(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        packet = self.get_port_capture_frame_frame_data_string(port_string, frame_num, options)
        pkt_bytes = packet.strip().split(" ")
        index = 0
        for item in pkt_bytes:
            pkt_bytes[index] = int(pkt_bytes[index], 16)
            index += 1
        return pkt_bytes

    def get_captured_frame_count(self, port_string, options=None):
        if options is None:
            options = {}
        return len(self.get_all_captured_frames(port_string))

    def get_captured_frame(self, port_string, frame_num, options=None):
        if options is None:
            options = {}
        return self.get_all_captured_frames(port_string)[frame_num]

    def get_captured_frames(self, port_string, first_frame_num, last_frame_num, options=None):
        if options is None:
            options = {}
        return self.get_all_captured_frames(port_string, options)[first_frame_num:last_frame_num]

    def get_all_captured_frames(self, port_handle, options=None):
        if options is None:
            options = {}
        file_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".txt"

        port_string = self.convert_port_to_port_handle(port_handle)
        port_handle = self.convert_port_to_port_handle(port_string)
        api = self.dev.get_api(PacketStatsConstants.PACKET_STATS_API)
        # self.dev.send_command("set tmpdir [pwd]")
        # self.dev.send_command("if {[file exists \"/tmp\"]} {set tmpdir \"/tmp\"}")
        # self.dev.send_command("catch {set tmpdir $::env(TRASH_FOLDER)} ;")
        # self.dev.send_command("catch {set tmpdir $::env(TMP)}")
        # self.dev.send_command("catch {set tmpdir $::env(TEMP)}")
        # ret_string = self.dev.send_command("set filename [file join $tmpdir "+file_name+"]")
        # ret_string = ret_string.replace('%', '')
        # file_name = ret_string.strip()
        # file_name = file_name.replace("ADMINI~1", "Administrator")
        ret_list = list()

        file_name = "c:/Temp/" + file_name
        assert isinstance(api, PacketStatsApi)
        ret_string = api.packet_stats(TrafficGenerationUtils.merge_arrays(
            {PacketStatsConstants.PORT_HANDLE_CMD: port_string,
             PacketStatsConstants.FILENAME_CMD: "\"" + file_name + "\"",
             PacketStatsConstants.FORMAT_CMD: PacketStatsConstants.FORMAT_TXT}, options))
        if "Capture buffer is empty" in str(ret_string):
            return ret_list
        # process ret string into a dictionary
        port_string = TrafficGenerationUtils.convert_port_string_to_file_string(port_handle)
        file_name = file_name + port_string + ".txt"
        self.dev.send_command("set fp [open \"" + file_name + "\" r]")
        # temp_bool = self.dev.tgen_debug
        # self.dev.tgen_debug = False
        ret_string = self.dev.send_command("set file_data [read $fp]")
        self.dev.send_command("close $fp")
        # self.dev.send_command("set data [split $file_data \"\n\"]")
        # ret_string = self.dev.send_command("foreach line $data {\n\tputs ($line)\n}")
        # self.dev.tgen_debug = temp_bool
        self.dev.send_command("file delete \"" + file_name + "\"")
        ret_string = ret_string.replace('%', '')

        lines = ret_string.split("\n")
        for line in lines:
            if len(line) > 2 and line[0].isdigit():
                temp_list = re.split("\\t", line)
                # temp_list[0] = frame #
                # temp_list[1] = time
                # temp_list[2] = DA
                # temp_list[3] = SA
                # temp_list[4] = ETHERTYPE
                # temp_list[5] = payload
                # temp_list[6] = length
                # temp_list[7] = Status

                packet = PacketClassifier.classify_packet(temp_list[2], temp_list[3], temp_list[4], temp_list[5])
                # packet_bytes = temp_list[2] + temp_list[3] + temp_list[4] +temp_list[5]

                packet.set_timestamp(temp_list[1])
                # set payload parses off the layers.
                # packet.set_destination_mac(temp_list[2])
                # packet.set_source_mac(temp_list[3])
                # packet.set_ether_type(temp_list[4])
                # packet.set_payload(packet_bytes)
                packet.set_length(temp_list[6])
                packet.set_status(temp_list[7])
                ret_list.append(packet)
        return ret_list

    """ WARNING: this method is a single set. It will clear out all over capture filter data"""
    def set_capture_filter_da1(self, port_handle, da, da_mask, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        assert isinstance(api, PacketConfigFilterApi)
        api.packet_config_filter(TrafficGenerationUtils.merge_arrays(
            {PacketConfigFilterConstants.PORT_HANDLE_CMD: port_string,
             PacketConfigFilterConstants.DA1_CMD: da,
             PacketConfigFilterConstants.DA_MASK1_CMD: da_mask},
            options))

    """ WARNING: this method is a single set. It will clear out all over capture filter data"""
    def set_capture_filter_da2(self, port_handle, da, da_mask, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        assert isinstance(api, PacketConfigFilterApi)
        api.packet_config_filter(TrafficGenerationUtils.merge_arrays(
            {PacketConfigFilterConstants.PORT_HANDLE_CMD: port_string,
             PacketConfigFilterConstants.DA2_CMD: da,
             PacketConfigFilterConstants.DA_MASK2_CMD: da_mask},
            options))

    """ WARNING: this method is a single set. It will clear out all over capture filter data"""
    def set_capture_filter_sa1(self, port_handle, sa, sa_mask, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        assert isinstance(api, PacketConfigFilterApi)
        api.packet_config_filter(TrafficGenerationUtils.merge_arrays(
            {PacketConfigFilterConstants.PORT_HANDLE_CMD: port_string,
             PacketConfigFilterConstants.SA1_CMD: sa,
             PacketConfigFilterConstants.SA_MASK1_CMD: sa_mask},
            options))

    """ WARNING: this method is a single set. It will clear out all over capture filter data"""
    def set_capture_filter_sa2(self, port_handle, sa, sa_mask, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        assert isinstance(api, PacketConfigFilterApi)
        api.packet_config_filter(TrafficGenerationUtils.merge_arrays(
            {PacketConfigFilterConstants.PORT_HANDLE_CMD: port_string,
             PacketConfigFilterConstants.SA2_CMD: sa,
             PacketConfigFilterConstants.SA_MASK2_CMD: sa_mask},
            options))

    """ WARNING: this method is a single set. It will clear out all over capture filter data"""
    def set_capture_filter_pattern1(self, port_handle, pattern, pattern_mask, pattern_offset, pattern_offset_type,
                                    match_type, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        assert isinstance(api, PacketConfigFilterApi)
        api.packet_config_filter(TrafficGenerationUtils.merge_arrays(
            {PacketConfigFilterConstants.PORT_HANDLE_CMD: port_string,
             PacketConfigFilterConstants.PATTERN1_CMD: pattern,
             PacketConfigFilterConstants.PATTERN_MASK1_CMD: pattern_mask,
             PacketConfigFilterConstants.PATTERN_OFFSET1_CMD: pattern_offset,
             PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_CMD: pattern_offset_type,
             PacketConfigFilterConstants.MATCH_TYPE1_CMD: match_type},
            options))

    """ WARNING: this method is a single set. It will clear out all over capture filter data"""
    def set_capture_filter_pattern2(self, port_handle, pattern, pattern_mask, pattern_offset, pattern_offset_type,
                                    match_type, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        assert isinstance(api, PacketConfigFilterApi)
        api.packet_config_filter(TrafficGenerationUtils.merge_arrays(
            {PacketConfigFilterConstants.PORT_HANDLE_CMD: port_string,
             PacketConfigFilterConstants.PATTERN2_CMD: pattern,
             PacketConfigFilterConstants.PATTERN_MASK2_CMD: pattern_mask,
             PacketConfigFilterConstants.PATTERN_OFFSET2_CMD: pattern_offset,
             PacketConfigFilterConstants.PATTERN_OFFSET_TYPE2_CMD: pattern_offset_type,
             PacketConfigFilterConstants.MATCH_TYPE2_CMD: match_type},
            options))

    """ WARNING: this method is a single set. It will clear out all over capture filter data"""
    def set_capture_filter_pattern_atm(self, port_handle, pattern, pattern_mask, pattern_offset, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        assert isinstance(api, PacketConfigFilterApi)
        api.packet_config_filter(TrafficGenerationUtils.merge_arrays(
            {PacketConfigFilterConstants.PORT_HANDLE_CMD: port_string,
             PacketConfigFilterConstants.PATTERN_ATM_CMD: pattern,
             PacketConfigFilterConstants.PATTERN_MASK_ATM_CMD: pattern_mask,
             PacketConfigFilterConstants.PATTERN_OFFSET_ATM_CMD: pattern_offset},
            options))

    """ This will (eventually) get the settings on the port"""
    def get_capture_filter(self, port_string):
        self.temp_capture_filter_info = dict()
        return "Not Supported"

    """ Start off an empty capture filter block """
    def get_capture_filter_default(self):
        self.temp_capture_filter_info = dict()

    """ WARNING: don't forget to write this data with write_capture_filter """
    def add_capture_filter_da1(self, da, da_mask, options=None):
        if options is None:
            options = {}
        self.temp_capture_filter_info = TrafficGenerationUtils.merge_arrays(
            self.temp_capture_filter_info, TrafficGenerationUtils.merge_arrays(
                {PacketConfigFilterConstants.DA1_CMD: da, PacketConfigFilterConstants.DA_MASK1_CMD: da_mask}, options))

    """ WARNING: don't forget to write this data with write_capture_filter """
    def add_capture_filter_da2(self, da, da_mask, options=None):
        if options is None:
            options = {}
        self.temp_capture_filter_info = TrafficGenerationUtils.merge_arrays(
            self.temp_capture_filter_info, TrafficGenerationUtils.merge_arrays(
                {PacketConfigFilterConstants.DA2_CMD: da, PacketConfigFilterConstants.DA_MASK2_CMD: da_mask}, options))

    """ WARNING: don't forget to write this data with write_capture_filter """
    def add_capture_filter_sa1(self, sa, sa_mask, options=None):
        if options is None:
            options = {}
        self.temp_capture_filter_info = TrafficGenerationUtils.merge_arrays(
            self.temp_capture_filter_info, TrafficGenerationUtils.merge_arrays(
                {PacketConfigFilterConstants.SA1_CMD: sa, PacketConfigFilterConstants.SA_MASK1_CMD: sa_mask}, options))

    """ WARNING: don't forget to write this data with write_capture_filter """
    def add_capture_filter_sa2(self, sa, sa_mask, options=None):
        if options is None:
            options = {}
        self.temp_capture_filter_info = TrafficGenerationUtils.merge_arrays(
            self.temp_capture_filter_info, TrafficGenerationUtils.merge_arrays(
                {PacketConfigFilterConstants.SA2_CMD: sa, PacketConfigFilterConstants.SA_MASK2_CMD: sa_mask}, options))

    """ WARNING: don't forget to write this data with write_capture_filter """
    def add_capture_filter_pattern1(self, pattern, pattern_mask, pattern_offset, pattern_offset_type, match_type,
                                    options=None):
        if options is None:
            options = {}
        opt_dict = {}
        if pattern:
            opt_dict[PacketConfigFilterConstants.PATTERN1_CMD] = pattern
        if pattern_mask:
            opt_dict[PacketConfigFilterConstants.PATTERN_MASK1_CMD] = pattern_mask
        if pattern_offset:
            opt_dict[PacketConfigFilterConstants.PATTERN_OFFSET1_CMD] = pattern_offset
        if pattern_offset_type:
            opt_dict[PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_CMD] = pattern_offset_type
        if match_type:
            opt_dict[PacketConfigFilterConstants.MATCH_TYPE1_CMD] = match_type
        self.temp_capture_filter_info = TrafficGenerationUtils.merge_arrays(self.temp_capture_filter_info,
                                                                            TrafficGenerationUtils.merge_arrays(
                                                                                opt_dict, options))

    """ WARNING: don't forget to write this data with write_capture_filter """
    def add_capture_filter_pattern2(self, pattern, pattern_mask, pattern_offset, pattern_offset_type, match_type,
                                    options=None):
        if options is None:
            options = {}
        opt_dict = {}
        if pattern:
            opt_dict[PacketConfigFilterConstants.PATTERN2_CMD] = pattern
        if pattern_mask:
            opt_dict[PacketConfigFilterConstants.PATTERN_MASK2_CMD] = pattern_mask
        if pattern_offset:
            opt_dict[PacketConfigFilterConstants.PATTERN_OFFSET2_CMD] = pattern_offset
        if pattern_offset_type:
            opt_dict[PacketConfigFilterConstants.PATTERN_OFFSET_TYPE2_CMD] = pattern_offset_type
        if match_type:
            opt_dict[PacketConfigFilterConstants.MATCH_TYPE2_CMD] = match_type
        self.temp_capture_filter_info = TrafficGenerationUtils.merge_arrays(self.temp_capture_filter_info,
                                                                            TrafficGenerationUtils.merge_arrays(
                                                                                opt_dict, options))

    """ WARNING: don't forget to write this data with write_capture_filter """
    def add_capture_filter_pattern_atm(self, pattern, pattern_mask, pattern_offset, options=None):
        if options is None:
            options = {}
        self.temp_capture_filter_info = TrafficGenerationUtils.merge_arrays(
            self.temp_capture_filter_info,
            TrafficGenerationUtils.merge_arrays({PacketConfigFilterConstants.PATTERN_ATM_CMD: pattern,
                                                 PacketConfigFilterConstants.PATTERN_MASK_ATM_CMD: pattern_mask,
                                                 PacketConfigFilterConstants.PATTERN_OFFSET_ATM_CMD: pattern_offset},
                                                options))

    def write_capture_filter(self, port_handle, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        self.temp_capture_filter_info[PacketConfigFilterConstants.PORT_HANDLE_CMD] = port_string
        assert isinstance(api, PacketConfigFilterApi)
        api.packet_config_filter(TrafficGenerationUtils.merge_arrays(self.temp_capture_filter_info, options))

    """ WARNING: this method is a single set. It will clear out all over capture trigger data"""
    def set_capture_filter(self, port_handle, enable, da_logic, sa_logic, error_logic, frame_size_logic,
                           frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        opt_dict = dict()
        opt_dict[PacketConfigTriggersConstants.PORT_HANDLE_CMD] = port_string
        if enable:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_FILTER_CMD] = "1"
        else:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_FILTER_CMD] = "0"
        if da_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_FILTER_DA_CMD] = da_logic
        if sa_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_FILTER_SA_CMD] = sa_logic
        if error_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_FILTER_ERROR_CMD] = error_logic
        if frame_size_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_TO_CMD] = frame_end_size
        assert isinstance(api, PacketConfigTriggersApi)
        api.packet_config_triggers(TrafficGenerationUtils.merge_arrays(opt_dict, options))

    """ WARNING: this method is a single set. It will clear out all over capture trigger data"""
    def set_capture_trigger(self, port_handle, enable, da_logic, sa_logic, error_logic, frame_size_logic,
                            frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        opt_dict = dict()
        opt_dict[PacketConfigTriggersConstants.PORT_HANDLE_CMD] = port_string
        if enable:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_CMD] = "1"
        else:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_CMD] = "0"
        if da_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_DA_CMD] = da_logic
        if sa_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_SA_CMD] = sa_logic
        if error_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_ERROR_CMD] = error_logic
        if frame_size_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_TO_CMD] = frame_end_size
        assert isinstance(api, PacketConfigTriggersApi)
        api.packet_config_triggers(TrafficGenerationUtils.merge_arrays(opt_dict, options))

    """ WARNING: this method is a single set. It will clear out all over capture trigger data"""
    def set_capture_async_trigger1(self, port_handle, enable, da_logic, sa_logic, error_logic, frame_size_logic,
                                   frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        opt_dict = dict()
        opt_dict[PacketConfigTriggersConstants.PORT_HANDLE_CMD] = port_string
        if enable:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_CMD] = "1"
        else:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_CMD] = "0"
        if da_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_DA_CMD] = da_logic
        if sa_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_SA_CMD] = sa_logic
        if error_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_ERROR_CMD] = error_logic
        if frame_size_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_FRAMESIZE_TO_CMD] = frame_end_size
        assert isinstance(api, PacketConfigTriggersApi)
        api.packet_config_triggers(TrafficGenerationUtils.merge_arrays(opt_dict, options))

    """ WARNING: this method is a single set. It will clear out all over capture trigger data"""
    def set_capture_async_trigger2(self, port_handle, enable, da_logic, sa_logic, error_logic, frame_size_logic,
                                   frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        opt_dict = dict()
        opt_dict[PacketConfigTriggersConstants.PORT_HANDLE_CMD] = port_string
        if enable:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_CMD] = "1"
        else:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_CMD] = "0"
        if da_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_DA_CMD] = da_logic
        if sa_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_SA_CMD] = sa_logic
        if error_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_ERROR_CMD] = error_logic
        if frame_size_logic:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            opt_dict[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_FRAMESIZE_TO_CMD] = frame_end_size
        assert isinstance(api, PacketConfigTriggersApi)
        api.packet_config_triggers(TrafficGenerationUtils.merge_arrays(opt_dict, options))

    """ WARNING: this method is a single set. It will clear out all over capture trigger data"""
    def set_capture_user_defined_statistics1(self, port_handle, enable, da_logic, sa_logic, error_logic,
                                             frame_size_logic, frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        opt_dict = dict()
        opt_dict[PacketConfigTriggersConstants.PORT_HANDLE_CMD] = port_string
        if enable:
            opt_dict[PacketConfigTriggersConstants.UDS1_CMD] = "1"
        else:
            opt_dict[PacketConfigTriggersConstants.UDS1_CMD] = "0"
        if da_logic:
            opt_dict[PacketConfigTriggersConstants.UDS1_DA_CMD] = da_logic
        if sa_logic:
            opt_dict[PacketConfigTriggersConstants.UDS1_SA_CMD] = sa_logic
        if error_logic:
            opt_dict[PacketConfigTriggersConstants.UDS1_ERROR_CMD] = error_logic
        if frame_size_logic:
            opt_dict[PacketConfigTriggersConstants.UDS1_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            opt_dict[PacketConfigTriggersConstants.UDS1_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            opt_dict[PacketConfigTriggersConstants.UDS1_FRAMESIZE_TO_CMD] = frame_end_size
        assert isinstance(api, PacketConfigTriggersApi)
        api.packet_config_triggers(TrafficGenerationUtils.merge_arrays(opt_dict, options))

    """ WARNING: this method is a single set. It will clear out all over capture trigger data"""
    def set_capture_user_defined_statistics2(self, port_handle, enable, da_logic, sa_logic, error_logic,
                                             frame_size_logic, frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        opt_dict = dict()
        opt_dict[PacketConfigTriggersConstants.PORT_HANDLE_CMD] = port_string
        if enable:
            opt_dict[PacketConfigTriggersConstants.UDS2_CMD] = "1"
        else:
            opt_dict[PacketConfigTriggersConstants.UDS2_CMD] = "0"
        if da_logic:
            opt_dict[PacketConfigTriggersConstants.UDS2_DA_CMD] = da_logic
        if sa_logic:
            opt_dict[PacketConfigTriggersConstants.UDS2_SA_CMD] = sa_logic
        if error_logic:
            opt_dict[PacketConfigTriggersConstants.UDS2_ERROR_CMD] = error_logic
        if frame_size_logic:
            opt_dict[PacketConfigTriggersConstants.UDS2_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            opt_dict[PacketConfigTriggersConstants.UDS2_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            opt_dict[PacketConfigTriggersConstants.UDS2_FRAMESIZE_TO_CMD] = frame_end_size
        assert isinstance(api, PacketConfigTriggersApi)
        api.packet_config_triggers(TrafficGenerationUtils.merge_arrays(opt_dict, options))

    """ This will (eventually) get the settings on the port"""
    def get_capture_trigger(self, port_string):
        self.temp_capture_trigger_info = dict()
        return "Not Supported"

    """ Start off an empty capture filter block """
    def get_capture_trigger_default(self):
        self.temp_capture_trigger_info = dict()

    """ WARNING: don't forget to write this data with write_capture_trigger """

    def add_capture_trigger_capture_filter(self, enable, da_logic, sa_logic, pattern_logic, error_logic,
                                           frame_size_logic, frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        if enable:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_FILTER_CMD] = "1"
        else:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_FILTER_CMD] = "0"
        if da_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_FILTER_DA_CMD] = da_logic
        if sa_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_FILTER_SA_CMD] = sa_logic
        if pattern_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_CMD] = pattern_logic
        if error_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_FILTER_ERROR_CMD] = error_logic
        if frame_size_logic:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_TO_CMD] = frame_end_size

    """ WARNING: don't forget to write this data with write_capture_trigger """

    def add_capture_trigger_capture_trigger(self, enable, da_logic, sa_logic, pattern_logic, error_logic,
                                            frame_size_logic, frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        if enable:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_TRIGGER_CMD] = "1"
        else:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_TRIGGER_CMD] = "0"
        if da_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_TRIGGER_DA_CMD] = da_logic
        if sa_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_TRIGGER_SA_CMD] = sa_logic
        if pattern_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_TRIGGER_PATTERN_CMD] = pattern_logic
        if error_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_TRIGGER_ERROR_CMD] = error_logic
        if frame_size_logic:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_TO_CMD] = frame_end_size

    """ WARNING: don't forget to write this data with write_capture_trigger """

    def add_capture_trigger_capture_async_trigger1(self, enable, da_logic, sa_logic, pattern_logic, error_logic,
                                                   frame_size_logic, frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        if enable:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_CMD] = "1"
        else:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_CMD] = "0"
        if da_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_DA_CMD] = da_logic
        if sa_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_SA_CMD] = sa_logic
        if pattern_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_PATTERN_CMD] = pattern_logic
        if error_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_ERROR_CMD] = error_logic
        if frame_size_logic:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER1_FRAMESIZE_TO_CMD] = frame_end_size

    """ WARNING: don't forget to write this data with write_capture_trigger """

    def add_capture_trigger_capture_async_trigger2(self, enable, da_logic, sa_logic, pattern_logic, error_logic,
                                                   frame_size_logic, frame_start_size, frame_end_size, options=None):
        if options is None:
            options = {}
        if enable:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_CMD] = "1"
        else:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_CMD] = "0"
        if da_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_DA_CMD] = da_logic
        if sa_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_SA_CMD] = sa_logic
        if pattern_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_PATTERN_CMD] = pattern_logic
        if error_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_ERROR_CMD] = error_logic
        if frame_size_logic:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            self.temp_capture_trigger_info[
                PacketConfigTriggersConstants.CAPTURE_ASYNC_TRIGGER2_FRAMESIZE_TO_CMD] = frame_end_size

    """ WARNING: don't forget to write this data with write_capture_trigger """

    def add_capture_trigger_capture_user_defined_statistics1(self, enable, da_logic, sa_logic, pattern_logic,
                                                             error_logic, frame_size_logic, frame_start_size,
                                                             frame_end_size, options=None):
        if options is None:
            options = {}
        if enable:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS1_CMD] = "1"
        else:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS1_CMD] = "0"
        if da_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS1_DA_CMD] = da_logic
        if sa_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS1_SA_CMD] = sa_logic
        if pattern_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS1_PATTERN_CMD] = pattern_logic
        if error_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS1_ERROR_CMD] = error_logic
        if frame_size_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS1_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS1_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS1_FRAMESIZE_TO_CMD] = frame_end_size

    """ WARNING: don't forget to write this data with write_capture_trigger """

    def add_capture_trigger_capture_user_defined_statistics2(self, enable, da_logic, sa_logic, pattern_logic,
                                                             error_logic, frame_size_logic, frame_start_size,
                                                             frame_end_size, options=None):
        if options is None:
            options = {}
        if enable:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS2_CMD] = "1"
        else:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS2_CMD] = "0"
        if da_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS2_DA_CMD] = da_logic
        if sa_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS2_SA_CMD] = sa_logic
        if pattern_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS2_PATTERN_CMD] = pattern_logic
        if error_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS2_ERROR_CMD] = error_logic
        if frame_size_logic:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS2_FRAMESIZE_CMD] = frame_size_logic
        if frame_start_size:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS2_FRAMESIZE_FROM_CMD] = frame_start_size
        if frame_end_size:
            self.temp_capture_trigger_info[PacketConfigTriggersConstants.UDS2_FRAMESIZE_TO_CMD] = frame_end_size

    def write_capture_trigger(self, port_handle, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.dev.get_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        assert isinstance(api, PacketConfigTriggersApi)
        self.temp_capture_trigger_info[PacketConfigTriggersConstants.PORT_HANDLE_CMD] = port_string
        api.packet_config_triggers(TrafficGenerationUtils.merge_arrays(self.temp_capture_trigger_info, options))
        api.get_device().clear_output_buffer()
