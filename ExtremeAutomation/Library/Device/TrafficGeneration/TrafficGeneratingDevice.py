import time
import abc
from ExtremeAutomation.Library.Utils.Time import current_milli_time
from ExtremeAutomation.Library.Device.Common.ManagedDeviceObject import ManagedDeviceObject
from ExtremeAutomation.Library.Utils.CollectionUtils import CollectionUtils
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingCommandObject import \
    TrafficGeneratingCommandObject


class TrafficGeneratingDevice(ManagedDeviceObject, metaclass=abc.ABCMeta):
    def __init__(self):
        super(TrafficGeneratingDevice, self).__init__()
        self._nameSpace = ""
        self.connection = None
        self.initialized = None
        self.chassis_ip = ""
        self.vendor = ""
        self.register_agents()
        self.register_apis()
        self.tgen_debug = True

    def get_host_name(self):
        return self.hostname

    def set_host_name(self, hostname):
        self.hostname = hostname

    @staticmethod
    def trim_command(string):
        return str(string).replace("%", "").strip()

    def connect(self, arglist):
        self.logger.log_info(arglist)

    def disconnect(self):
        if self.connection is None:
            self.initialized = False
            return
        if self.connection.is_connected():
            self.connection.disconnect()
            self.connection = None
            self.initialized = False

    def is_connected(self):
        return self.connection is not None

    def is_initialized(self):
        return self.initialized

    def get_version(self, key=None):
        if key is None:
            return CollectionUtils.dict_to_string(self.version)
        return self.version[key]

    def send_command(self, cmd):
        if self.tgen_debug:
            self.logger.log_debug(cmd)
        cmd = cmd.encode('ascii', 'ignore')
        self.connection.write(cmd + "\n")
        reply = self.connection.wait_until_quiet(100)
        if not reply.strip().endswith("%"):
            reply += self.connection.read_until("%")
        if self.tgen_debug:
            self.logger.log_debug(reply)
        try:
            f = open("c:\\tmp\\ixia.sent.log", "a+")
            f.write(cmd + "\n")
            f.close()
        except:
            pass
        try:
            f = open("c:\\tmp\\ixia.rec.log", "a+")
            f.write(reply)
            f.close()
        except:
            pass
        return reply

    def send_command_return_obj(self, cmd):
        """sends the command to the Traffic Generator"""
        cmd_obj = TrafficGeneratingCommandObject()
        cmd_obj.command = cmd
        cmd_obj.start_time = current_milli_time()
        cmd_obj.return_text = self.send_command(cmd).strip()
        cmd_obj.end_time = current_milli_time()
        return cmd_obj

    @abc.abstractmethod
    def take_port_ownership(self, host, user, port_string, reset=False, options=None):
        return self.logger.log_unimplemented_method()

    def clear_port_ownership(self, host, port_string, reset=False, options=None):
        return self.logger.log_unimplemented_method()

    def set_port(self, port):
        self.port = port

    @abc.abstractmethod
    def get_traffic_helper(self):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_statistic_helper(self):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_capture_helper(self):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_port_duplex(self, port_string):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def set_port_duplex(self, port_string, duplex, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_port_speed(self, port_string):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def set_port_speed(self, port_string, speed, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def set_port_autonegotiation(self, port_string, set_bool, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def has_link(self, port_string):
        return self.logger.log_unimplemented_method()

    def wait_for_has_link(self, port_string, timeout_in_ms=10000, options=None):
        if options is None:
            options = {}
        if isinstance(timeout_in_ms, str):
            timeout_in_ms = int(timeout_in_ms)
        current_time = current_milli_time()
        if isinstance(port_string, list):
            for port in port_string:
                b_looking_for_link = self.has_link(port)
                while not b_looking_for_link and (current_milli_time() - current_time) < timeout_in_ms:
                    time.sleep(0.01)
                    b_looking_for_link = self.has_link(port)
        else:
            b_looking_for_link = self.has_link(port_string)
            while not b_looking_for_link and (current_milli_time() - current_time) < timeout_in_ms:
                time.sleep(0.01)
                b_looking_for_link = self.has_link(port_string)

    @abc.abstractmethod
    def reset_port(self, host, port_string):
        return self.logger.log_unimplemented_method()

    def start_traffic_and_wait(self, port_string, timeout_in_ms, options=None):
        if options is None:
            options = {}
        current_time = current_milli_time()
        self.start_traffic(port_string, options)

        if self.is_port_continuous(port_string):
            self.logger.log_error("Unable to wait on a port that is marked continuous")
        else:
            while self.is_port_transmitting(port_string) and (current_milli_time() - current_time) < timeout_in_ms:
                time.sleep(0.01)

        return current_milli_time() - current_time

    def wait_for_capture_count_on_port(self, port_string, expected_count, timeout_in_ms=60000, options=None):
        if options is None:
            options = {}
        current_time = current_milli_time()
        # self.start_traffic(port_string, options)

        while self.get_running_captured_frame_count(port_string) < expected_count \
                and (current_milli_time() - current_time) < timeout_in_ms:
            time.sleep(0.01)

        return current_milli_time() - current_time

    @abc.abstractmethod
    def is_port_transmitting(self, port_string):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def is_port_capturing(self, port_string):
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_traffic(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_traffic(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def start_capture(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def stop_capture(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def clear_capture_buffer(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def set_capture_mode(self, port_string, mode, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_port_capture(self, port_handle, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_port_capture_frame(self, port_handle, frame_num, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_port_statistic(self, port_handle, tx_or_rx, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def get_port_stream_statistic(self, port_handle, stream_id, tx_or_rx, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def clear_statistics_and_filters(self, port_string, options=None):
        if options is None:
            options = {}
        kw_results = []
        kw_results.append(self.clear_statistics(port_string, options))
        kw_results.append(self.clear_capture_filters_and_triggers(port_string))
        return kw_results

    @abc.abstractmethod
    def clear_statistics(self, port_string, options=None):
        if options is None:
            options = {}
        self.logger.log_unimplemented_method()

    def modify_stream_using_packet(self, port_string, stream_id, packet, options=None):
        if options is None:
            options = {}
        options[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY
        if TrafficConfigConstants.TRANSMIT_MODE_CMD not in options:
            options[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST
        self.configure_stream_using_packet(port_string, stream_id, packet, "Nothing", options)

    @abc.abstractmethod
    def configure_stream_using_packet(self, port_string, stream_id, packet, clear_all_streams=False, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_using_bytes(self, port_string, stream_id, packet_bytes, clear_all_streams=False, options=None):
        if options is None:
            options = {}
        return self.configure_stream_using_packet(port_string, stream_id,
                                                  PacketClassifier.classify_packet_bytes(packet_bytes),
                                                  clear_all_streams=False, options=None)

    def configure_streams_using_packets(self, port_string, packets, options=None):
        if options is None:
            options = {}
        self.clear_all_streams(port_string)
        index = 0
        while index < len(packets):
            packet = packets[index]
            index += 1
            if index == len(packets):
                options[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_RETURN_TO_ID
            else:
                options[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_NEXT
            self.configure_stream_using_packet(port_string, index, packet, "Nothing", options)

    @abc.abstractmethod
    def clear_stream(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def clear_all_streams(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def stream_exists(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_stream(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_all_stream(self, port_string):
        count = self.get_stream_count(port_string)
        index = 1
        streams = []
        while int(index) <= int(count):
            streams.append(self.get_stream(port_string, index))
            index += 1
        return streams

    def get_stream_count(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_stream_transmit_mode(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_stream_transmit_mode_string(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_port_transmit_mode(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_port_transmit_mode_string(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_stream_transmit_action(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_stream_transmit_action_string(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def is_stream_enabled(self, port_string, stream_id, stream=None):
        try:
            if not stream:
                stream = self.get_stream(port_string, stream_id)
            stream = str(stream)
            stream = stream.replace(":", "=")
            stream = stream.replace(" ", "")
            return "is_enabled=true" in stream
        except Exception as e:
            self.logger.log_debug(e)
            return False

    def set_stream_enabled(self, port_string, stream_id, enable):
        return self.logger.log_unimplemented_method()

    def is_stream_continuous(self, port_string, stream_id, extra_info=False):
        action = self.get_stream_transmit_action_string(port_string, stream_id)
        if "ixia" in str(self.__class__).lower():
            stream = action
        else:
            stream = self.get_stream_transmit_mode_string(port_string, stream_id)
        port = self.get_port_transmit_mode_string(port_string)
        if "Cont" in stream and 'Sequential' not in port:
            # ostinato should be port = 'Interleaved' and stream = 'Continuous'
            # ixia just needs stream = 'Continuous'
            continuous = True
        else:
            continuous = False
        ret_string = ""
        if extra_info:
            ret_string += "Stream Transmit Mode:" + stream + ";"
            ret_string += "Stream Transmit Action:" + action + ";"
            ret_string += "Port Transmit Mode:" + port + ";"
            ret_string += "isContinuous:" + str(continuous)
            return ret_string
        else:
            return continuous

    def is_port_continuous(self, port_string):
        stream_count = self.get_stream_count(port_string)
        if isinstance(stream_count, str):
            stream_count = int(stream_count)
        index = 0
        res = False
        while index < stream_count and not res:
            index += 1
            # streams have to be enabled to be considered.
            # stream = self.get_stream(port_string, index)
            # if self.is_stream_enabled(port_string, index, stream):
            if self.is_stream_enabled(port_string, index):
                # if it is continuous, then good... the port is continuous.
                res = res or self.is_stream_continuous(port_string, index)
                # if there are any ports that go back to the first stream, then it's continuous.
                res = res or (self.get_stream_transmit_action_string(port_string, index) == "Goto First")
                # also if port is sequential and a stream is stop, then it's not continuous.
                # res = res or (self.get_stream_transmit_action_string(port_string, index) == "Stop")
        return res

    def clear_capture_filters_and_triggers(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        helper = self.get_capture_helper()
        helper.get_capture_filter_default()
        helper.write_capture_filter(port_string)
        helper.get_capture_trigger_default()
        helper.write_capture_trigger(port_string)

    def clear_output_buffer(self):
        reply = self.connection.wait_until_quiet(100)
        # if reply and len(reply):
        #     self.logger.log_info("cleared from the buffer " + reply)

    def convert_port_to_port_handle(self, port_string):
        if isinstance(port_string, list):
            index = 0
            for port in port_string:
                port_string[index] = self.convert_port_to_port_handle(port)
                index += 1
        else:
            # change [0-9]+.[0-9]+.[0-9]+ to 1/1/1
            # change [0-9]+ [0-9]+ [0-9]+ to 1/1/1
            port_string = port_string.replace(".", "/")
            port_string = port_string.replace(" ", "/")
            if not len(port_string.split("/")) == 3:
                port_string = "1/" + port_string
        if isinstance(port_string, list):
            return " ".join(port_string)
        else:
            return port_string

    def convert_port_to_port_name(self, port):  # ex: port_10_69_11_55_2_1
        port_string = port.replace(".", " ").replace("/", " ").replace("_", " ")
        port_string_list = port_string.split(" ")
        if len(port_string_list) > 2:
            port_string_list = port_string_list[-2:]
        port_string = "_".join(port_string_list)
        return "$port_" + (str(self.get_host_name()) + "_" + str(port_string)).replace(".", "_").replace("/", "_")

    @staticmethod
    def convert_port_name_to_port_string(port):  # ex: port_10_69_11_55_2_1 to 2/1
        port_string = port.replace("$", " ").replace(".", " ").replace("/", " ").replace("_", " ")
        port_string_list = port_string.split(" ")
        if len(port_string_list) > 2:
            port_string_list = port_string_list[-2:]
        return "/".join(port_string_list)

    @staticmethod
    def convert_port_string_to_file_string(port_string):
        # change [0-9]+.[0-9]+.[0-9]+ to 1/1/1
        # change [0-9]+ [0-9]+ [0-9]+ to 1/1/1
        port_string = port_string.replace(" ", ".")
        port_string = port_string.replace("/", ".")
        if not len(port_string.split(".")) == 3:
            port_string = "1." + port_string
        port_string = port_string.replace(".", "")
        return "-1-" + port_string

    def convert_port_handle_to_port_string(self, port_string):
        # ixia can come in as 2/1, 2.1, 1.2.1, 1/2/1, or 1 2 1
        # smartbits can come in with 2/1, 2.1, 1.2.1, 1/2/1, or 1 2 1 or port_host_port (ex: port_10_69_11_55_2_1
        #              "port_" + (str(host)+"_"+str(port)).replace(".", "_").replace("/", "_")
        if isinstance(port_string, list):
            index = 0
            for port in port_string:
                port_string[index] = self.convert_port_handle_to_port_string(port)
                index += 1
        else:
            port_string = self.convert_port_to_port_handle(port_string)
            #  1/1/1 to 1/1
            spl = port_string.split("/")
            if not len(spl) == 2:
                port_string = spl[len(spl) - 2] + "/" + spl[len(spl) - 1]
        if isinstance(port_string, list):
            return " ".join(port_string)
        else:
            return port_string

    def set_port_phy_mode(self, port_string, mode):
        return self.logger.log_unimplemented_method()

    def register_apis(self):
        self.logger.log_debug("registering Traffic Generating Device Apis")

    def register_agents(self):
        self.logger.log_debug("registering Traffic Generating Device Apis")

    def register_api(self, name, api):
        self.apis[name] = api

    def register_agent(self, name, api):
        self.agents[name] = api

    def get_device(self):
        return
