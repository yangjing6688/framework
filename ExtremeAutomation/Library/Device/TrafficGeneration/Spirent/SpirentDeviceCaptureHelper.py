from ExtremeAutomation.Library.Device.TrafficGeneration.HltapiTrafficGeneratingDeviceCaptureHelper import \
    HltapiTrafficGeneratingDeviceCaptureHelper
import random
import string
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketStatsApi import \
    PacketStatsConstants, PacketStatsApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier


class SpirentDeviceCaptureHelper(HltapiTrafficGeneratingDeviceCaptureHelper):
    def __init__(self, ixia_device):
        super(SpirentDeviceCaptureHelper, self).__init__(ixia_device)

    # def get_captured_frame_count(self, port_string):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_captured_frame(self, port_string, frame_num):
    #     return self.logger.log_unimplemented_method()
    #
    # def get_captured_frames(self, port_string, first_frame_num, last_frame_num):
    #     return self.logger.log_unimplemented_method()

    def get_all_captured_frames(self, port_handle, options=None):
        if self.capture_buffer.is_capture_buffer_filled(port_handle):
            return self.capture_buffer.get_stored_capture_buffer(port_handle)
        if options is None:
            options = {}
        file_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

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
             PacketStatsConstants.ACTION_CMD: PacketStatsConstants.ACTION_FILTERED,
             PacketStatsConstants.STOP_CMD: "1",
             PacketStatsConstants.FILENAME_CMD: "\"" + file_name + "\"",
             PacketStatsConstants.FORMAT_CMD: PacketStatsConstants.FORMAT_PCAP}, options))
        if "Capture buffer is empty" in str(ret_string):
            return ret_list
        # process ret string into a dictionary
        # port_string = TrafficGenerationUtils.convert_port_string_to_file_string(port_handle)
        file_name = file_name + ".pcap"
        intries = 0
        reply = "invalid command name"
        while intries < 3 and "invalid command name" in reply:
            self.dev.send_command("set fp [open \"" + file_name + "\" r]")
            self.dev.send_command("fconfigure $fp -translation binary")
            # temp_bool = self.dev.tgen_debug
            # self.dev.tgen_debug = False
            ret_string = self.dev.send_command("set file_data [read $fp]")
            reply = self.dev.send_command("close $fp")
            intries += 1
            if "invalid command name" in reply:
                self.dev.send_command("close $fp")
                self.dev.send_command("\r\n")
                self.dev.send_command("\r\n")
        ret_string = self.dev.send_command("set chars [split $file_data {}]\n" +
                                           "set vals []\n" +
                                           "foreach c $chars {\n" +
                                           "scan $c \"%c\" i\n" +
                                           "" +
                                           "lappend vals [format %x $i]\n}\n")
        ret_string = self.dev.send_command("puts $vals")
        # self.dev.send_command("file delete \"" + file_name+"\"")
        ret_string = self.dev.trim_command(ret_string)
        chars = ret_string.split(" ")
        new_str = ""
        for c in chars:
            new_str += chr(int(c, 16))
        buff = PacketClassifier.process_pcap_file_contents(new_str)
        self.capture_buffer.set_capture_buffer(port_handle, buff)
        return buff

    def get_captured_frame_count(self, port_string, options=None):
        port_handle = self.convert_port_to_port_handle(port_string)
        if options is None:
            options = {}
        # self.dev.send_command("set results [stc::get [stc::get [stc::get " + port_handle +
        #                       " -children-Analyzer] -children-AnalyzerPortResults] -totalFrameCount]")
        self.dev.send_command("set hCapture [stc::get " + port_handle + " -children-capture]")
        # self.dev.send_command("puts $hCapture")
        self.dev.send_command("stc::perform CaptureStop -captureProxyId $hCapture")
        return self.dev.trim_command(self.dev.send_command("puts [stc::get $hCapture -PktCount]").strip())
        # self.dev.send_command("puts \"Saved Captured frames:\t[stc::get $hCapture -PktSavedCount]\"")

        # return self.dev.send_command("puts $results")
