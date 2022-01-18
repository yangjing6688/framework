import re
import os
import socket
from collections import OrderedDict

from ExtremeAutomation.Library.Device.Common.Agents.IxiaConnectionTelnetAgent import IxiaConnectionTelnetAgent
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingSpbmApi import \
    NetworkEmulatingSpbmConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingEndstationApi import \
    NetworkEmulatingEndstationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingBgpApi import NetworkEmulatingBgpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingLldpApi import \
    NetworkEmulatingLldpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingOspfApi import \
    NetworkEmulatingOspfConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingVrrpApi import \
    NetworkEmulatingVrrpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingTcpApi import NetworkEmulatingTcpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingRouteApi import \
    NetworkEmulatingRouteConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingDvrApi import NetworkEmulatingDvrConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceCaptureHelper import JetsDeviceCaptureHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceStatisticHelper import \
    JetsDeviceStatisticHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceTrafficHelper import \
    JetsDeviceTrafficHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsArpHelper import JetsArpHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.NetworkEmulatingDevice import NetworkEmulatingDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDevice import TrafficGeneratingDevice
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.Time import current_milli_time
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenConstants import TrafficGenConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsDvrApi import JetsDvrApi
from ExtremeAutomation.Library.Device.Common.Agents.SshAgent import SshAgent
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingDhcpApi import \
    NetworkEmulatingDhcpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingIgmpApi import \
    NetworkEmulatingIgmpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsSpbmApi import JetsSpbmApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsBgpApi import JetsBgpApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsLldpApi import JetsLldpApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsEndstationApi import JetsEndstationApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsRouteApi import JetsRouteApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsOspfApi import JetsOspfApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsTcpApi import JetsTcpApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsVrrpApi import JetsVrrpApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsTcpipStackHelper import JetsTcpipStackHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsDhcpApi import JetsDhcpApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.Apis.JetsIgmpApi import JetsIgmpApi
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult


class JetsDevice(TrafficGeneratingDevice, NetworkEmulatingDevice, JetsDeviceCaptureHelper, JetsDeviceStatisticHelper,
                 JetsDeviceTrafficHelper, JetsArpHelper, JetsTcpipStackHelper):
    def __init__(self):
        super(JetsDevice, self).__init__()
        JetsArpHelper.__init__(self, self)
        JetsDeviceCaptureHelper.__init__(self, self)
        JetsDeviceStatisticHelper.__init__(self, self)
        JetsDeviceTrafficHelper.__init__(self, self)
        JetsTcpipStackHelper.__init__(self, self)
        self.capture_buffer = JetsCaptureBuffer(self)
        self.os = TrafficGenConstants.JETS_CHASSIS
        self.dev.os = TrafficGenConstants.JETS_CHASSIS
        self.prompt_regex = '[%\\$]$'
        self._ports_group = {}
        self._ports_group_index = []
        self._streams = {}
        self._stream_objects = {}
        self.pdl_stream_headers_and_values = OrderedDict()  # this gets cleared out after a stream is configured.
        self.pdl_level = 0
        self.initialized_network_device = False
        self._nameSpace = "jets"
        self.oper_sys = TrafficGenConstants.JETS_CHASSIS
        self.port = 22
        self.main_prompt = "#"
        self.jets_dir = None
        self.view_tag = None
        self.cached_capture_buffer = None
        self.cached_capture_buffer_time_stampe = None
        self.capturing_ports = []
        self.jets_log_directory = '/tmp/jets'
        os.makedirs(os.path.dirname(self.jets_log_directory), exist_ok=True)
       

    def connect(self, host, port=22):
        if self.connection is not None and self.is_connected():
            self.init_connection()
            return
        if self.connection is None:
            self.set_host_name(host)
            host_name = host  # self.get_host_name() # '10.52.153.101'
            self.connection = SshAgent(self.dev)

        try:
            self.connection.connect()
            self.connection.login()
            self.init_connection()
        except socket.error:
            self.initialized = False

    def connect_network_generator(self, host, ixnetwork_ip, port=22):
        """
            Jets connection is the same as the network emulation
        :param host:
        :param ixnetwork_ip:
        :param port:
        :return:
        """
        self.connect(host, port)

    def init_connection(self):
        if self.initialized:
            return
        if self.view_tag:
            reply = self.send_command_no_wait("sct setview " + str(self.view_tag))
            reply += self.send_command_no_wait("y")
        if self.jets_dir:
            reply = self.send_command_no_wait("cd " + str(self.jets_dir))
        self.send_command("./setupEnvPerl")
        self.send_command("lappend auto_path .")
        self.send_command("package req jetsAdtech")
        self.send_command("source test.tcl")
        self.send_command("set debug 0")
        self.initialized = True

    def init_network_generator_device(self):
        """
            Jets init_network_generator_device is the same as the network emulation
        :return:
        """
        self.init_connection()

    def disconnect(self):
        if self.connection is None:
            self.initialized = False
            return
        else:
            try:
                self.connection.disconnect()
            except:
                pass
            self.connection = None
            self.initialized = False

    def send_command(self, command):
        assert isinstance(self.connection, SshAgent)
        self.connection.write_encode_ln(command)
        output = self.connection.wait_for_regex_prompt_or_quiet(self.prompt_regex, 100000)
        # two \r will not
        self.logger.log_debug(output.replace('\r\r', '\r'))
        if self.jets_log_directory:
            log_path = os.path.join(self.jets_log_directory, self.hostname)
            if not os.path.exists(log_path):
                os.makedirs(log_path)
            try:
                f = open(os.path.join(log_path, "sent.log"), "a+")
                f.write(command + "\n")
                f.close()
            except:
                pass
            try:
                f = open(os.path.join(log_path, "rec.log"), "a+")
                f.write(output)
                f.close()
            except:
                pass
        if "wrong # args" in output:
            self.logger.log_error("Command missing from test.tcl:" + command)
        elif "can't read" in output:
            if "deviceMapping" in output:
                self.logger.log_error(
                    "Either using a port name (string) when you need and device index (int) of vice versa" + command)
        return output

    def send_command_no_wait(self, command):
        assert isinstance(self.connection, SshAgent)
        self.connection.write_encode_ln(command)
        output = self.connection.wait_until_quiet(100)
        if self.tgen_debug:
            self.logger.log_debug(output)
        try:
            f = open("c:\\tmp\\jets.sent.log", "a+")
            f.write(command + "\n")
            f.close()
        except:
            pass
        try:
            f = open("c:\\tmp\\jets.rec.log", "a+")
            f.write(output)
            f.close()
        except:
            pass
        if "wrong # args" in output:
            self.logger.log_error("Command missing from test.tcl:" + command)
        elif "can't read" in output:
            if "deviceMapping" in output:
                self.logger.log_error(
                    "Either using a port name (string) when you need and device index (int) of vice versa" + command)
        return output

    def get_name_space(self):
        if not hasattr(self, '_nameSpace') or self._nameSpace == "":
            self._nameSpace = "jets"
        return self._nameSpace

    def take_port_ownership(self, host, user, port_string, reset=False, options=None):
        kw_results = []
        if not isinstance(port_string, list):
            port_string = [port_string]
        for port in port_string:
            if self.is_port_registered(port):
                self.logger.log_info("Port " + port + "already taken")
                continue
            prt_id = str(self.__get_port_group_count() + 1)
            reply = self.send_command("global deviceIdMapping")
            reply += self.send_command("set deviceIdMapping(" + prt_id + ") " + port)
            reply += self.send_command("interface create i" + prt_id + " " + prt_id +
                                       " -ifmode IPoETHER -mode NORMAL_MODE")
            cmd_obj = self.send_command_return_obj("i" + prt_id + " run")
            if "cannot open the Dlpi interface" in cmd_obj.return_text:
                kw_results.append(KeywordResult(self.name, False,
                                                "Port " + str(port_string) +
                                                " did not take port ownership correctly.",
                                                "",
                                                cmd_obj))

            self.__add_port_from_group(port, "i" + prt_id)
        return kw_results

    def take_network_generator_port_ownership(self, host, user, port_string, reset=False, options=None):
        """
            Jets take_network_generator_port_ownership is the same as the network emulation
        :param host:
        :param user:
        :param port_string:
        :param reset:
        :return:
        """
        self.take_port_ownership(host, user, port_string, reset, options)

    def set_host_name(self, hostname):
        self.hostname = hostname

    def set_port(self, port):
        self.port = port

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_os(self, dev_os):
        self.os = dev_os

    def get_os(self):
        return self.os

    def set_jets_directory(self, _dir):
        self.jets_dir = _dir

    def get_jets_directory(self):
        return self.jets_dir

    def set_view_tag(self, tag):
        self.view_tag = tag

    def get_view_tag(self):
        return self.view_tag

    def get_traffic_helper(self):
        return self

    def get_statistic_helper(self):
        return self

    def get_capture_helper(self):
        return self

    def get_port_duplex(self, port_string):
        reply = self.send_command("exec ethtool " + port_string + " | grep \"Duplex:\"")
        parts = reply.split("Duplex:")
        return parts[1].strip()

    def set_port_duplex(self, port_string, duplex, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        # ethtool -s eth0 speed 10 duplex half autoneg off << not reliable
        return self.logger.log_unimplemented_method()

    def get_port_mtu(self, port_string):
        prt_id = self.get_port_index_from_group_string(port_string)
        reply = self.send_command("i" + prt_id + " getMtu")
        return reply.split("\n")[1].strip()

    def set_port_mtu(self, port_string, mtu, options=None):
        if options is None:
            options = {}
        prt_id = self.get_port_index_from_group_string(port_string)
        reply = self.send_command("i" + prt_id + " setMtu -mtu " + str(mtu))

    def get_port_speed(self, port_string):
        reply = self.send_command("exec ethtool " + port_string + " | grep \"Speed:\"")
        parts = reply.split("Speed:")
        return parts[1].strip()

    def set_port_speed(self, port_string, speed, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        # ethtool -s eth0 speed 10 duplex half autoneg off << not reliable
        return self.logger.log_unimplemented_method()

    def get_port_autonegotiation(self, port_string):
        reply = self.send_command("exec ethtool " + port_string + " | grep \"Auto-negotiation:\"")
        parts = reply.split("Speed:")
        return parts[1].strip()

    def set_port_autonegotiation(self, port_string, set_bool, options=None):
        if options is None:
            options = {}
        # ethtool -s eth0 speed 10 duplex half autoneg off << not reliable
        return self.logger.log_unimplemented_method()

    def has_link(self, port_string):
        """
        LinkStateUnknown = 0;
        LinkStateDown = 1;
        LinkStateUp = 2;
        """
        # reply = self.send_command("ifconfig " + port_string).upper()
        # reply = re.sub(r"[^\w\s]", '', reply)
        # reply = re.sub(r"\s+", '', reply)
        # if "LINKUP" in reply:
        #     return True
        # else:
        #     return False
        reply = self.send_command("exec ethtool " + port_string + " | grep \"Link\"")
        return "yes" in reply

    def reset_port(self, host, port_string):
        # self.clear_jets_capture_filter(port_string)
        # self.clear_all_streams(port_string)
        reply = self.send_command("exec ifdown " + port_string)
        reply = self.send_command("exec ifup " + port_string)

    def __get_port_from_group(self, name):
        return self._ports_group[name]

    def get_circuit_name_from_interface_name(self, name):
        return self._ports_group[name]

    def get_port_index_from_group(self, name):
        return self._ports_group_index.index(name) + 1

    def get_port_index_from_group_string(self, name):
        if name.isdigit():
            return name
        return str(self.get_port_index_from_group(name))

    def get_interface_base_address(self, name, num=0):
        prt_id = self.get_port_index_from_group_string(name)
        if name.isdigit():
            return name
        return str(prt_id) + "." + str(prt_id) + "." + str(prt_id) + "." + str(int(prt_id) + int(num))

    def __add_port_from_group(self, name, value):
        self._ports_group[name] = value
        self._ports_group_index.append(name)
        return self.get_port_index_from_group(name)

    def __get_port_group_count(self):
        return len(self._ports_group)

    def __remove_port_from_group(self, name):
        self._ports_group_index.remove(name)
        self._ports_group.remove(name)

    def get_all_jets_ports(self):
        return self._ports_group.keys()

    def is_port_registered(self, port_string):
        return port_string in self._ports_group.keys()

    def add_jets_stream(self, port_string, stream_id):
        port_string = str(port_string)
        stream_id = str(stream_id)
        if port_string not in self._streams:
            self._streams[port_string] = {}
        port_streams = self._streams[port_string]
        port_streams[stream_id] = self.generate_jets_stream_name(port_string, stream_id)
        return port_streams[stream_id]

    @staticmethod
    def generate_jets_stream_name(port_string, stream_id):
        port_string = str(port_string)
        stream_id = str(stream_id)
        return "stream_" + port_string + "_" + stream_id

    def is_port_transmitting(self, port_string):
        self.logger.log_debug("is_port_transmitting(" + port_string + ")")
        if port_string not in self._streams:
            return False
        streams = self._streams[port_string]
        for stream_id, stream in streams.items():
            so = self._stream_objects[stream]
            if so.enabled:
                reply = self.send_command(stream + " stats")

                if "sendingPkts" in reply:
                    if "sendingPkts true" in reply:
                        return True
                else:
                    self.logger.log_error("Update your JETS server to support is_port_transmitting")
        return False

    def is_port_capturing(self, port_string):
        prt_id = self.get_port_index_from_group_string(port_string)
        return prt_id in self.capturing_ports

    def start_traffic(self, port_string, options=None):
        self.logger.log_debug("start_traffic(" + port_string + ")")
        if options is None:
            options = {}
        if port_string in self._streams:
            streams = self._streams[port_string]
            for stream_id, stream in streams.items():
                so = self._stream_objects[stream]
                if so.enabled:
                    if stream in self._stream_objects:
                        if self._stream_objects[stream].state == "Run":
                            self.send_command(stream + " stop")
                        self.send_command(stream + " reset")
                    self.send_command(stream + " run")
                    self._stream_objects[stream].state = "Run"
        else:
            self.logger.log_error("No streams on port " + str(port_string))

    def stop_traffic(self, port_string, options=None):
        self.logger.log_debug("stop_traffic(" + port_string + ")")
        if options is None:
            options = {}
        if port_string in self._streams:
            streams = self._streams[port_string]
            for stream in streams:
                self.send_command(streams[stream] + " stop")
                self.send_command(streams[stream] + " stats")
                self._stream_objects[streams[stream]].state = "Stop"
        else:
            self.logger.log_error("No streams on port " + str(port_string))

    def start_capture(self, port_string, options=None):
        self.logger.log_debug("start_capture(" + port_string + ")")
        if self.is_port_capturing(port_string):
            self.logger.log_debug("port (" + port_string + ") is already capturing")
            return
        self.capture_buffer.start_capture_buffer(port_string)
        if options is None:
            options = {}
        prt_id = self.get_port_index_from_group_string(port_string)
        self.send_command("analyzer create an" + prt_id + " " + prt_id)
        self.send_command("an" + prt_id + " clearlist")
        self.send_command("an" + prt_id + " subfilter set -filtA {pdlStr -pdlStr \"" +
                          self.get_jets_capture_filter(port_string) + "\"}")
        self.send_command("an" + prt_id + " run")
        self.capturing_ports.append(prt_id)

    def stop_capture(self, port_string, options=None):
        self.logger.log_debug("stop_capture(" + port_string + ")")
        if not self.is_port_capturing(port_string):
            self.logger.log_debug("port (" + port_string + ") not capturing")
            return
        if options is None:
            options = {}
        prt_id = self.get_port_index_from_group_string(port_string)
        self.send_command("an" + prt_id + " stop")
        self.send_command("an" + prt_id + " stats")
        try:
            self.capture_buffer.stop_capture_buffer(port_string)
        except:
            self.logger.log_trace("problem in stop_capture with stop_capture_buffer")
        try:
            self.capturing_ports.remove(prt_id)
        except:
            self.logger.log_trace("problem in stop_capture with removing port from capture list")

    def clear_capture_buffer(self, port_string, options=None):
        self.cached_capture_buffer = None
        self.cached_capture_buffer_time_stampe = None
        if options is None:
            options = {}
        self.clear_statistics(port_string)
        self.capture_buffer.clear_capture_buffer(port_string)

    def set_capture_mode(self, port_string, mode, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture(self, port_handle, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_capture_frame(self, port_handle, frame_num, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_statistic(self, port_handle, tx_or_rx, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_stream_statistic(self, port_handle, stream_id, tx_or_rx, key, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def clear_statistics(self, port_string, options=None):
        self.logger.log_debug("clear_statistics(" + port_string + ")")
        self._clear_jets_tx_statistics(port_string)
        self._clear_jets_rx_statistics(port_string)
        name = self.get_circuit_name_from_interface_name(port_string)
        self.send_command(name + " clear")

    def _clear_jets_tx_statistics(self, port_string):
        try:
            if port_string in self._streams:
                streams = self._streams[port_string]
                for stream in streams:
                    self.send_command(streams[stream] + " clearStats")
        except:
            pass

    def _clear_jets_rx_statistics(self, port_string):
        try:
            if self.is_port_capturing(port_string):
                prt_id = self.get_port_index_from_group_string(port_string)
                self.send_command("an" + prt_id + " clearlist")
        except:
            pass

    def set_stream_transmit_mode(self, port_string, stream_id, mode):
        return self.logger.log_unimplemented_method()

    def get_stream_transmit_action(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_stream_transmit_action_string(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_stream_transmit_mode(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_stream_transmit_mode_string(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def configure_stream_using_packet(self, port_string, stream_id, packet, clear_all_streams=False, options=None):
        if options is None:
            options = {}
        prt_id = self.get_port_index_from_group_string(port_string)
        stream_num = stream_id
        opt_dict = options
        self.clear_stream(port_string, stream_id)
        stream_name = self.add_jets_stream(port_string, stream_id)
        self.pdl_clear_packet_header_cashe()
        packet.config_thirdparty_traffic_generator_stream(EthernetPacketConstants.TRAFFIC_GENERATION_JETS, self,
                                                          port_string, stream_name, options=opt_dict)
        pkt_string = self.pdl_build_packet_string_and_clear()
        if packet.is_field_set(packet.get_payload()):
            self.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": packet.get_payload().replace(" ", "")})
        length = packet.get_length()
        if TrafficConfigConstants.FRAME_SIZE_CMD in opt_dict:
            length = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.FRAME_SIZE_CMD])
            self.logger.log_debug("setting " + TrafficConfigConstants.FRAME_SIZE_CMD + " to " +
                                  str(opt_dict[TrafficConfigConstants.FRAME_SIZE_CMD]))
        if length < 64:
            length = 64
            self.logger.log_debug("updating " + TrafficConfigConstants.FRAME_SIZE_CMD + " to " + str(length) +
                                  " min packet size")
        packet_mode = "ManualBurst "
        if TrafficConfigConstants.TRANSMIT_MODE_CMD in opt_dict:
            mode = options[TrafficConfigConstants.TRANSMIT_MODE_CMD]
            if mode == TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST:
                packet_mode = "Periodic "
            elif mode == TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS:
                packet_mode = "Periodic "
            elif mode == TrafficConfigConstants.TRANSMIT_MODE_SINGLE_PKT:
                packet_mode = "ManualBurst "
            elif mode == TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST:
                packet_mode = "ManualBurst "
            else:
                packet_mode = "ManualBurst "
                self.logger.log_error("JETS not supported: " + TrafficConfigConstants.TRANSMIT_MODE_CMD + "  " + str(
                    opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD]))
        num_packets = 1
        if TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD in opt_dict:
            self.logger.log_debug("setting " + TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD + " to " + str(
                opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD]))
            num_packets = NumberUtils.to_integer_value(opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD])
        if TrafficConfigConstants.NUMBER_OF_PACKETS_TX_CMD in opt_dict:
            num_packets = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.NUMBER_OF_PACKETS_TX_CMD])
            self.logger.log_debug("setting " + TrafficGenerationConstants.NUMBER_OF_PACKETS_TX_CMD + " to " + str(
                opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_TX_CMD]))

        rate_pps = 1
        rate_burst = 1
        if TrafficConfigConstants.RATE_PPS_CMD in opt_dict:
            rate_pps = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.RATE_PPS_CMD])
            self.logger.log_debug("setting rate pps to " + str(opt_dict[TrafficConfigConstants.RATE_PPS_CMD]))
            if TrafficConfigConstants.PKTS_PER_BURST_CMD in opt_dict:
                rate_burst = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD])
                self.logger.log_debug(
                    "setting number of packets to " + str(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))
            else:
                rate_burst = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.RATE_PPS_CMD])
                self.logger.log_debug("setting number of packets to " +
                                      str(opt_dict[TrafficConfigConstants.RATE_PPS_CMD]))
        elif TrafficConfigConstants.PKTS_PER_BURST_CMD in opt_dict:
            rate_burst = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.RATE_PPS_CMD])
            self.logger.log_debug("setting " + TrafficConfigConstants.PKTS_PER_BURST_CMD + " to " + str(
                opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))
            num_packets = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD])
            self.logger.log_debug("setting number of packets to " +
                                  str(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))

        self._stream_objects[stream_name] = JetsStreamObject(stream_name, port_string, prt_id, stream_id, length,
                                                             packet_mode, num_packets, rate_pps, rate_burst)
        self._stream_objects[stream_name].generate_pdl(pkt_string)
        self.send_command(self._stream_objects[stream_name].cmd_str)

    def pdl_add_packet_header(self, header, pkt_string):
        if self.pdl_level > 0:
            header += "_ecap" + str(self.pdl_level)
        if header not in self.pdl_stream_headers_and_values:
            self.pdl_stream_headers_and_values[header] = {}
        elif header == "rawdata":
            pkt_string = self.pdl_stream_headers_and_values["rawdata"]["data"] + " " + pkt_string["data"]
            pkt_string = {"data": "0x" + pkt_string.replace("0x", "")}
        self.pdl_stream_headers_and_values[header].update(pkt_string)

    def pdl_get_last_header(self):
        # get the last header key
        last_key = next(reversed(self.pdl_stream_headers_and_values))
        return last_key

    def pdl_update_packet_header_value(self, header_name, field_name, value):
        if header_name not in self.pdl_stream_headers_and_values:
            self.pdl_stream_headers_and_values[header_name] = {}
        self.pdl_stream_headers_and_values[header_name][field_name] = value

    def pdl_build_packet_string(self, cache_ordered_dict):
        tmp = []
        if not self.pdl_contains_header("rawdata"):
            self.pdl_add_packet_header("rawdata", {"data": "0x00"})
        if self.pdl_contains_header("rawdata"):
            raw_data = self.pdl_stream_headers_and_values["rawdata"]["data"].replace(" ", "")
            while len(raw_data) < 20:
                raw_data = raw_data + "00"
            self.pdl_stream_headers_and_values["rawdata"]["data"] = raw_data
        for key, value in cache_ordered_dict.items():
            tmp.append(re.sub("_ecap[0-9]", "", re.sub("_[0-9]$", "", key)) + " " +
                       ' '.join('{}={}'.format(k, v) for k, v in value.items()))
        return ','.join(tmp)

    def pdl_contains_header(self, header):
        return header in self.pdl_stream_headers_and_values

    def pdl_build_packet_string_and_clear(self):
        pdl_string = self.pdl_build_packet_string(self.pdl_stream_headers_and_values)
        self.pdl_clear_packet_header_cashe()
        return pdl_string

    def pdl_clear_packet_header_cashe(self):
        self.pdl_stream_headers_and_values = OrderedDict()

    def pdl_up_encap_level(self):
        self.pdl_level -= 1

    def pdl_down_encap_level(self):
        self.pdl_level += 1

    def clear_stream(self, port_string, stream_id, options=None):
        self.logger.log_debug("stop_traffic(" + port_string + ")")
        if options is None:
            options = {}
        if port_string in self._streams:
            streams = self._streams[port_string]
            stream_id = str(stream_id)
            if stream_id in streams:
                stream_name = streams[stream_id]
                self.send_command(streams[stream_id] + " destroy")
                if stream_id in self._streams[port_string]:
                    del self._streams[port_string][stream_id]
                if stream_name in self._stream_objects:
                    del self._stream_objects[stream_name]

    def clear_all_streams(self, port_string, options=None):
        self.logger.log_debug("clear_all_streams(" + port_string + ")")
        if options is None:
            options = {}
        # generator destroyAllGenerators -device 1
        if port_string in self._streams:
            streams = self._streams[port_string]
            for stream in streams:
                self.send_command(streams[stream] + " destroy")
                if streams[stream] in self._stream_objects:
                    del self._stream_objects[streams[stream]]
            if port_string in self._streams:
                del self._streams[port_string]
            pass

    def stream_exists(self, port_string, stream_id):
        stream_name = self.generate_jets_stream_name(port_string, stream_id)
        return stream_name in self._stream_objects

    def get_stream(self, port_string, stream_num):
        return self.get_stream_from_stream_id(port_string, stream_num)

    def set_stream_enabled(self, port_string, stream_id, enable):
        stream_name = self.generate_jets_stream_name(port_string, stream_id)
        so = self._stream_objects[stream_name]
        so.enabled = enable

    def get_stream_from_stream_id(self, port_string, stream_id):
        stream_name = self.generate_jets_stream_name(port_string, stream_id)
        so = None
        if stream_name in self._stream_objects:
            so = self._stream_objects[stream_name]
        return so

    def get_port_transmit_mode(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_port_transmit_mode_string(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_all_stream(self, port_string):
        count = self.get_stream_count(port_string)
        prt_id = self.get_port_index_from_group_string(port_string)
        # generator getAllGenerators -device prt_id
        index = 1
        streams = []
        while int(index) <= int(count):
            streams.append(self.get_stream(port_string, index))
            index += 1
        return streams

    def get_stream_count(self, port_string, options=None):
        num = 0
        if port_string in self._streams:
            num = len(self._streams[port_string])
        return num

    def clear_statistics_and_filters(self, port_string, options=None):
        if options is None:
            options = {}
        self.clear_statistics(port_string, options)
        self.capture_buffer.clear_capture_buffer(port_string)

    def list_port_list(self):
        return self.send_command("netstat -i")

    def clear_capture_filters_and_triggers(self, port_string):
        self.cached_capture_buffer = None
        self.cached_capture_buffer_time_stampe = None
        self.clear_jets_capture_filter(port_string)

    #########################################################################################
    ##############
    # ####               INTERNAL JETS ONLY METHODS AFTER THIS POINT
    ##############
    #########################################################################################

    def send_pdl_pkt(self, port_string, pdl_string, count, gap_in_msecs, mode, total_len, pad_pattern):
        # <port> sendPdlPkt -pdlStr <pdlStr> -count <nPkts> -gapInMsecs <ipg> -mode <streamMode> -totalLen <lenOfPkt>
        # -padPattern <paddingStr>
        #     <port> - Name of port - mandatory
        #     <pdlStr> - The PDL based string for the packet to send - mandatory
        #     <nPkts> - number of packets to send - default is 1.
        #     <ipg> - Inter-pkt gap in msecs.
        #     <mode> - Mode of sending, one of continuous or continuous_burst - optional - if not one of continuous or
        #              continuous_burst, then don't send it.
        #     <lenOfPkt> - Total length of packet - optional - if not specified, then don't send it.
        #     <paddingStr> - String to use for padding the pkt to totalLen - default is 01. This should be sent only if
        #                    totalLen is specified.
        #
        # If mode is not specified, then we are doing a blocking call to send <nPkts>.
        # In this case, the timeout for the command to come back is (<ipg> * <nPkts> / 1000) + 60
        cmd = str(port_string) + " sendPdlPkt "
        cmd += "-pdlStr " + str(pdl_string)
        cmd += " -count " + str(count)
        cmd += " -gapInMsecs " + str(gap_in_msecs)
        cmd += " -mode " + str(mode)
        cmd += " -totalLen " + str(total_len)
        cmd += " -padPattern " + str(pad_pattern)
        return self.send_command(cmd)

    def stop_pdl_pkt(self, port_string):
        # <port> stopPdlPkts
        #     <port> - Name of port - mandatory

        cmd = str(port_string) + " stopPdlPkts"
        return self.send_command(cmd)

    def analyzer_create(self, name, port_string, or_filters=False, action="LOG"):
        # analyzer create <anaName> <logPort> -orFilters <true|false> -action  <analyzerAction>
        #       anaName - unique name for the analyzer
        #       logPort - logical port name of the port on which to start the analyzer
        #       orFilters - true or false - defaults to false
        #       action - action to perform - one of LOG, DROP, FWD - default is LOG
        cmd = "analyzer create " + str(name) + " " + str(port_string) + \
              " -orFilters " + str(or_filters) + \
              " -action " + str(action)
        return self.send_command(cmd)

    def analyzer_subfilter(self, name, filter_a_pdl_string, filter_b_pdl_string=None, filter_c_pdl_string=None):
        # <anaName> subfilter set -filtA <filtAStr> -filtB <filtBStr> -filtC <filtCStr>
        #        anaName - unique name of the analyzer
        #        filtAStr, filtBStr, filtCStr - "{pdlStr -pdlStr \"<pdlStr>\"} - where pdlStr is a string. filtA is
        #        mandatory, but filtB and filtC are optional
        # example: ana1 subfilter set -filtA {pdlStr -pdlStr "pdlStrA"}
        cmd = str(name) + " subfilter set -filtA \"{pdlStr -pdlStr \\\"" + str(filter_a_pdl_string) + "\\\"}\""
        if filter_b_pdl_string:
            cmd += " -filtB \"{pdlStr -pdlStr \\\"" + str(filter_b_pdl_string) + "\\\"}\""
        if filter_c_pdl_string:
            cmd += " -filtC \"{pdlStr -pdlStr \\\"" + str(filter_c_pdl_string) + "\\\"}\""
        return self.send_command(cmd)

    def analyzer_run(self, name):
        # <anaName> run
        #       anaName - unique name for the analyzer
        cmd = str(name) + " run"
        return self.send_command(cmd)

    def analyzer_stats(self, name):
        # <anaName> stats
        #       anaName - unique name for the analyzer
        cmd = str(name) + " stats"
        return self.send_command(cmd)

    def analyzer_stop(self, name):
        # <anaName> stop
        #       anaName - unique name for the analyzer
        cmd = str(name) + " stop"
        return self.send_command(cmd)

    def analyzer_reset(self, name):
        # <anaName> reset
        #       anaName - unique name for the analyzer
        cmd = str(name) + " reset"
        return self.send_command(cmd)

    def analyzer_clearlist(self, name):
        # <anaName> reset
        #       anaName - unique name for the analyzer
        cmd = str(name) + " clearlist"
        return self.send_command(cmd)

    def analyzer_destroy(self, name):
        # <anaName> destroy
        #       anaName - unique name for the analyzer
        cmd = str(name) + " destroy"
        return self.send_command(cmd)

    def analyzer_destroy_all(self):
        # analyzer destroyAll
        cmd = "analyzer destroyAll"
        return self.send_command(cmd)

    #########################################################################################
    ##############
    # ####               APIS
    ##############
    #########################################################################################

    def register_agents(self):
        super(JetsDevice, self).register_agents()
        self.register_agent(TrafficGenerationConstants.TELNET, IxiaConnectionTelnetAgent(self))

    def register_apis(self):
        super(JetsDevice, self).register_apis()
        self.logger.log_debug("registering Jets Agents")
        self.register_api(NetworkEmulatingSpbmConstants.SBP_API, JetsSpbmApi(self))
        self.register_api(NetworkEmulatingEndstationConstants.END_STATION_API, JetsEndstationApi(self))
        self.register_api(NetworkEmulatingBgpConstants.BGP_API, JetsBgpApi(self))
        self.register_api(NetworkEmulatingDhcpConstants.DHCP_API, JetsDhcpApi(self))
        self.register_api(NetworkEmulatingIgmpConstants.IGMP_API, JetsIgmpApi(self))
        self.register_api(NetworkEmulatingLldpConstants.LLDP_API, JetsLldpApi(self))
        self.register_api(NetworkEmulatingOspfConstants.OSPF_API, JetsOspfApi(self))
        self.register_api(NetworkEmulatingTcpConstants.TCP_API, JetsTcpApi(self))
        self.register_api(NetworkEmulatingVrrpConstants.VRRP_API, JetsVrrpApi(self))
        self.register_api(NetworkEmulatingRouteConstants.ROUTE_API, JetsRouteApi(self))
        self.register_api(NetworkEmulatingDvrConstants.DVR_API, JetsDvrApi(self))


class JetsStreamObject(object):
    def __init__(self, stream_name, port_string, port_id, stream_id, length, packet_mode, num_packets, rate_pps,
                 rate_burst):
        self.enabled = True
        self.port = port_string
        self.port_id = port_id
        self.stream_id = stream_id
        self.name = stream_name
        self.length = length
        self.packet_mode = packet_mode
        self.num_packets = num_packets
        self.rate_pps = rate_pps
        self.rate_burst = rate_burst
        self.state = None
        self.cmd_str = None

    def generate_pdl(self, pkt_string):
        self.cmd_str = "generator addPdlStream " + self.name + " " + str(self.port_id) + " -pdlStr \"" + pkt_string + \
                       "\"  " + "-totalLen " + str(self.length) + "  -mode " + self.packet_mode + " -rate " + \
                       str(max(self.rate_pps, self.num_packets)) + " -burstSize " + str(self.rate_burst)


class JetsCaptureBuffer(object):
    def __init__(self, dev):
        self.dev = dev
        self.buffer = {}
        self.bufferStartStamp = {}
        self.bufferStopStamp = {}

    def start_capture_buffer(self, port_string):
        self.clear_capture_buffer(port_string)
        self.bufferStartStamp[port_string] = current_milli_time()

    def stop_capture_buffer(self, port_string):
        self.bufferStopStamp[port_string] = current_milli_time()
        self.buffer[port_string] = self.dev.get_all_captured_frames(port_string)

    def get_stored_capture_buffer(self, port_string):
        return self.buffer[port_string]

    def clear_capture_buffer(self, port_string):
        self.buffer[port_string] = None
        self.bufferStartStamp[port_string] = -1
        self.bufferStopStamp[port_string] = -1

    def clear_all_capture_buffer(self, port_string):
        self.buffer = {}
        self.bufferStartStamp = {}
        self.bufferStopStamp = {}

    def is_capture_buffer_filled(self, port_string):
        return port_string in self.buffer and self.buffer[port_string] is not None

# protocol fields
# kArpFieldNumber = {int} 300
# kDot2LlcFieldNumber = {int} 206
# kDot2SnapFieldNumber = {int} 207
# kDot3FieldNumber = {int} 201
# kEth2FieldNumber = {int} 200
# kHexDumpFieldNumber = {int} 104
# kIcmpFieldNumber = {int} 402
# kIgmpFieldNumber = {int} 403
# kIp4FieldNumber = {int} 301
# kIp4over4FieldNumber = {int} 305
# kIp4over6FieldNumber = {int} 304
# kIp6FieldNumber = {int} 302
# kIp6over4FieldNumber = {int} 303
# kIp6over6FieldNumber = {int} 306
# kLlcFieldNumber = {int} 202
# kMacFieldNumber = {int} 100
# kMldFieldNumber = {int} 404
# kPayloadFieldNumber = {int} 101
# kSampleFieldNumber = {int} 102
# kSnapFieldNumber = {int} 203
# kSvlanFieldNumber = {int} 204
# kTcpFieldNumber = {int} 400
# kTextProtocolFieldNumber = {int} 500
# kUdpFieldNumber = {int} 401
# kUserScriptFieldNumber = {int} 103
# kVlanFieldNumber = {int} 205
# kVlanStackFieldNumber = {int} 208
