import abc
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpConfigApi import \
    EmulationBgpConfigApi, EmulationBgpConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpControlApi import \
    EmulationBgpControlApi, EmulationBgpControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpInfoApi import \
    EmulationBgpInfoApi, EmulationBgpInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpRouteConfigApi import \
    EmulationBgpRouteConfigApi, EmulationBgpRouteConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiConnectApi import ConnectApi, \
    ConnectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import \
    InterfaceConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import \
    InterfaceConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceStatsApi import \
    InterfaceStatsApi, InterfaceStatsConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigBuffersApi import \
    PacketConfigBuffersApi, PacketConfigBuffersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import \
    PacketConfigFilterConstants, PacketConfigFilterApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import \
    PacketConfigTriggersApi, PacketConfigTriggersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketControlApi import PacketControlApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketControlApi import \
    PacketControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketInfoApi import PacketInfoApi, \
    PacketInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketStatsApi import \
    PacketStatsConstants, PacketStatsApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiResetPortApi import ResetPortConstants, \
    ResetPortApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiSessionInfoApi import SessionInfoApi, \
    SessionInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigApi, \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficControlApi import TrafficControlApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficControlApi import \
    TrafficControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficL47ConfigApi import \
    TrafficL47ConfigApi, TrafficL47ConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficStatsApi import TrafficStatsApi, \
    TrafficStatsConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsConfigApi import UdsConfigApi, \
    UdsConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsFilterPalletteConfigApi import \
    UdsFilterPalletteConfigApi, UdsFilterPalletteConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfConfigApi import \
    EmulationOspfConfigApi, EmulationOspfConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfControlApi import \
    EmulationOspfControlApi, EmulationOspfControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfInfoApi import \
    EmulationOspfInfoApi, EmulationOspfInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfLsaConfigApi import \
    EmulationOspfLsaConfigApi, EmulationOspfLsaConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfNetworkGroupConfigApi \
    import EmulationOspfNetworkGroupConfigApi, EmulationOspfNetworkGroupConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfTopologyRouteConfigApi \
    import EmulationOspfTopologyRouteConfigApi, EmulationOspfTopologyRouteConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDevice import TrafficGeneratingDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.AbstractPacket import AbstractPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import ArpPacketHeader
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult


class HltapiTrafficGeneratingDevice(TrafficGeneratingDevice, metaclass=abc.ABCMeta):
    def get_host_name(self):
        return self.hostname

    def set_host_name(self, hostname):
        self.hostname = hostname

    def connect(self, arglist):
        self.logger.log_debug(arglist)

    def disconnect(self):
        if self.connection is None:
            self.initialized = False
            return
        if self.connection.is_connected():
            self.connection.disconnect()
            self.connection = None
            self.initialized = False

    def send_command(self, cmd):
        if self.tgen_debug:
            self.logger.log_debug(cmd)
        self.connection.write(cmd + "\n")
        reply = self.connection.wait_until_quiet(300)
        if not reply.strip().endswith("%"):
            reply += self.connection.read_until("%")
        if self.tgen_debug:
            self.logger.log_trace(reply)
        # try:
        #     f = open("c:\\tmp\\ixia.sent.log", "a+")
        #     f.write(cmd + "\n")
        #     f.close()
        # except:
        #     pass
        # try:
        #     f = open("c:\\tmp\\ixia.rec.log", "a+")
        #     f.write(reply)
        #     f.close()
        # except:
        #     pass
        return reply

    def send_command_no_wait(self, cmd):
        if self.tgen_debug:
            self.logger.log_debug(cmd)
        cmd = cmd.encode('ascii', 'ignore')
        self.connection.write(cmd + "\n")
        reply = self.connection.wait_until_quiet(100)
        if self.tgen_debug:
            self.logger.log_trace(reply)
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

    def read_console_no_wait(self):
        reply = self.connection.wait_until_quiet(100)
        if self.tgen_debug:
            if reply != '':
                self.logger.log_trace(reply)
        return reply

    def take_port_ownership(self, host, user, port_string, reset=False, options=None):
        """
        set connect_info [ixia::connect\
            -reset\
            -device 10.52.2.189\
            -port_list 1/1\
            -username ciscoUser
        ]
        """
        if not options:
            options = {}
        og_options = options.copy()
        og_port_string = port_string
        kw_results = []

        port_string = self.convert_port_handle_to_port_string(port_string)
        capi = self.get_api(ConnectConstants.CONNECT_API)
        assert isinstance(capi, ConnectApi)
        if user:
            options = {ConnectConstants.USERNAME_CMD: user}
        if reset:
            options[ConnectConstants.RESET_CMD] = ""
        cmd_obj = capi.connect_helper(host, port_string, options)
        kw_results.extend(self._determine_error(self.take_port_ownership.__name__, cmd_obj, port_string))
        if reset:
            if InterfaceConfigConstants.AUTONEGOTIATION_CMD not in og_options:
                og_options[InterfaceConfigConstants.AUTONEGOTIATION_CMD] = 1
            if InterfaceConfigConstants.SPEED_CMD not in og_options:
                og_options[InterfaceConfigConstants.SPEED_CMD] = InterfaceConfigConstants.SPEED_AUTO
            if InterfaceConfigConstants.DUPLEX_CMD not in og_options:
                og_options[InterfaceConfigConstants.DUPLEX_CMD] = InterfaceConfigConstants.DUPLEX_AUTO
            if isinstance(og_port_string, list):
                for ps in og_port_string:
                    port_string = self.convert_port_handle_to_port_string(ps)
                    kw_results.extend(
                        self.set_capture_mode(port_string, "{" + InterfaceConfigConstants.PORT_RX_MODE_CAPTURE + " " +
                                              InterfaceConfigConstants.PORT_RX_MODE_WIDE_PACKET_GROUP + "}",
                                              og_options))
            else:
                kw_results.extend(
                    self.set_capture_mode(og_port_string, "{" + InterfaceConfigConstants.PORT_RX_MODE_CAPTURE + " " +
                                          InterfaceConfigConstants.PORT_RX_MODE_WIDE_PACKET_GROUP + "}", og_options))
        return kw_results

    def clear_port_ownership(self, host, port_string, reset=False, options=None):
        return self.take_port_ownership(host, None, port_string, reset, options)

    def set_port(self, port):
        self.port = port

    def get_traffic_helper(self):
        return self

    def get_statistic_helper(self):
        return self

    def get_capture_helper(self):
        return self

    def set_arp_transmit(self, port_string, enabled=True, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        # assert isinstance(api, InterfaceConfigApi)
        if enabled:
            enabled = 1
        else:
            enabled = 0
        if InterfaceConfigConstants.MODE_CMD not in options:
            options[InterfaceConfigConstants.MODE_CMD] = InterfaceConfigConstants.MODE_CONFIG
        cmd_obj = api.interface_config(TrafficGenerationUtils.merge_arrays(
            {InterfaceConfigConstants.ARP_SEND_REQ_CMD: enabled,
             InterfaceConfigConstants.PORT_HANDLE_CMD: port_string},
            options))

    def get_port_duplex(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'duplex')

    def set_port_duplex(self, port_string, duplex, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        # assert isinstance(api, InterfaceConfigApi)
        if disable_autonegotiation:
            disable_autonegotiation = 0
        else:
            disable_autonegotiation = 1
        if InterfaceConfigConstants.MODE_CMD not in options:
            options[InterfaceConfigConstants.MODE_CMD] = InterfaceConfigConstants.MODE_CONFIG
        cmd_obj = api.interface_config(TrafficGenerationUtils.merge_arrays(
            {InterfaceConfigConstants.DUPLEX_CMD: duplex,
             InterfaceConfigConstants.AUTONEGOTIATION_CMD: disable_autonegotiation,
             InterfaceConfigConstants.PORT_HANDLE_CMD: port_string},
            options))

    def get_port_mtu(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'mtu')

    def set_port_mtu(self, port_string, mtu, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        if InterfaceConfigConstants.MODE_CMD not in options:
            options[InterfaceConfigConstants.MODE_CMD] = InterfaceConfigConstants.MODE_CONFIG
        cmd_obj = api.interface_config(TrafficGenerationUtils.merge_arrays(
            {InterfaceConfigConstants.MTU_CMD: mtu,
             InterfaceConfigConstants.PORT_HANDLE_CMD: port_string},
            options))

    # set hltapiinterfacestatsapi_interface_stats [ixia::interface_stats \
    # -port_handle 1/1/1 \
    # ]
    #  {1/1/1 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}} {port_name {10/100/1000 Base T}}
    #  {tx_frames 0} {rx_frames 0} {elapsed_time 0.00} {rx_collisions 0} {total_collisions 0} {duplex full}
    #  {intf_speed 1000} {fcs_errors 0} {late_collisions 0} {link 1} {portCpuMemory 256}}} {status 1}
    # %
    def get_port_speed(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                     'intf_speed')

    def set_port_speed(self, port_string, speed, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        # assert isinstance(api, InterfaceConfigApi)
        if str(disable_autonegotiation) == 'True' or str(disable_autonegotiation) == '1':
            disable_autonegotiation = 0
        else:
            disable_autonegotiation = 1

        speed = str(speed)
        speed_parts = speed.split(" ")
        speed_settings = []
        for sp in speed_parts:
            if sp == "10":
                sp = InterfaceConfigConstants.SPEED_ETHER10
            elif sp == "100":
                sp = InterfaceConfigConstants.SPEED_ETHER100
            elif sp == "1000":
                sp = InterfaceConfigConstants.SPEED_ETHER1000
            speed_settings.append(sp)
        options[InterfaceConfigConstants.SPEED_CMD] = " ".join(speed_settings)

        if InterfaceConfigConstants.MODE_CMD not in options:
            options[InterfaceConfigConstants.MODE_CMD] = InterfaceConfigConstants.MODE_CONFIG
        cmd_obj = api.interface_config(TrafficGenerationUtils.merge_arrays(
            {InterfaceConfigConstants.AUTONEGOTIATION_CMD: disable_autonegotiation,
             InterfaceConfigConstants.PORT_HANDLE_CMD: port_string},
            options))

    def set_port_autonegotiation(self, port_string, set_bool, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        # assert isinstance(api, InterfaceConfigApi)
        if str(set_bool) == 'True' or str(set_bool) == '1':
            set_bool = 1
        else:
            set_bool = 0
        if InterfaceConfigConstants.MODE_CMD not in options:
            options[InterfaceConfigConstants.MODE_CMD] = InterfaceConfigConstants.MODE_CONFIG
        cmd_obj = api.interface_config(TrafficGenerationUtils.merge_arrays(
            {InterfaceConfigConstants.AUTONEGOTIATION_CMD: set_bool,
             InterfaceConfigConstants.PORT_HANDLE_CMD: port_string},
            options))

    # reply {1/1/1 {{intf_type ethernet} {framing {}} {card_name {10/100/1000 LSM XMVR16}}
    # {port_name {10/100/1000 Base T}} {tx_frames 0} {rx_frames 0} {elapsed_time 0.00} {rx_collisions 0}
    # {total_collisions 0} {duplex full} {intf_speed 10} {fcs_errors 0} {late_collisions 0} {link 1}
    # {portCpuMemory 256}}} {status 1}

    def has_link(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        capi = self.get_api(InterfaceStatsConstants.INTERFACE_STATS_API)
        return (InterfaceStatsApi.get_flattened_value(capi.interface_stats_port_handle(port_string), port_string,
                                                      'link') == "1")

    def reset_port(self, host, port_string):
        port_string = self.convert_port_handle_to_port_string(port_string)
        capi = self.get_api(ConnectConstants.CONNECT_API)
        cmd_obj = capi.connect_helper(host, port_string, {"reset": ""})
        self.set_capture_mode(port_string, InterfaceConfigConstants.PORT_RX_MODE_CAPTURE,
                              {InterfaceConfigConstants.SEQUENCE_CHECKING_CMD: 1})

    # set hltapitrafficcontrolapi_traffic_control [ixia::traffic_control \
    # -action poll \
    # -port_handle 1/1/1 \
    # ]
    #  {clicks 2038344610} {seconds 1549308411} {status 1} {stopped 1}

    def is_port_transmitting(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(TrafficControlConstants.TRAFFIC_CONTROL_API)
        cmd_obi = api.traffic_control({TrafficControlConstants.ACTION_CMD: TrafficControlConstants.ACTION_POLL,
                                       TrafficControlConstants.PORT_HANDLE_CMD: port_string})
        return str(InterfaceStatsApi.get_flattened_value(cmd_obi.return_text, "", 'stopped')) == "0"

    def is_port_capturing(self, port_string):
        port_name_string = self.convert_port_to_port_name(port_string)
        api = self.get_api(PacketInfoConstants.PACKET_INFO_API)
        cmd_obi = api.packet_info({PacketInfoConstants.ACTION_CMD: PacketInfoConstants.ACTION_STATUS,
                                   PacketInfoConstants.PORT_HANDLE_CMD: port_name_string})

        # ret_string = self.send_command("set control_sta [sth::packet_info \\\n "+
        # "-port_handle                                      "+port_name_string+" \\\n"+
        # "-action                                           status]\n")
        return str(InterfaceStatsApi.get_flattened_value(cmd_obi.return_text, "", 'stopped')) == "0"

    def start_traffic(self, port_string, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(TrafficControlConstants.TRAFFIC_CONTROL_API)
        # assert isinstance(api, TrafficControlApi)
        cmd_obj = api.traffic_control(TrafficGenerationUtils.merge_arrays(
            {TrafficControlConstants.ACTION_CMD: TrafficControlConstants.ACTION_RUN,
             TrafficControlConstants.PORT_HANDLE_CMD: port_string},
            options))

    def stop_traffic(self, port_string, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(TrafficControlConstants.TRAFFIC_CONTROL_API)
        # assert isinstance(api, TrafficControlApi)
        cmd_obj = api.traffic_control(TrafficGenerationUtils.merge_arrays(
            {TrafficControlConstants.ACTION_CMD: TrafficControlConstants.ACTION_STOP,
             TrafficControlConstants.PORT_HANDLE_CMD: port_string},
            options))

    def start_capture(self, port_string, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(PacketControlConstants.PACKET_CONTROL_API)
        # assert isinstance(api, PacketControlApi)
        cmd_obj = api.packet_control(TrafficGenerationUtils.merge_arrays(
            {PacketControlConstants.ACTION_CMD: PacketControlConstants.ACTION_START,
             PacketControlConstants.PORT_HANDLE_CMD: port_string},
            options))

    def stop_capture(self, port_string, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(PacketControlConstants.PACKET_CONTROL_API)
        # assert isinstance(api, PacketControlApi)
        cmd_obj = api.packet_control(TrafficGenerationUtils.merge_arrays(
            {PacketControlConstants.ACTION_CMD: PacketControlConstants.ACTION_STOP,
             PacketControlConstants.PORT_HANDLE_CMD: port_string},
            options))

    # set hltapipacketcontrolapi_packet_control [ixia::packet_control \
    # -action reset \
    # -port_handle 1/1/1 \
    # ]
    # DEBUG - 2019-02-04 14:27:51,226 -  Checking link states on ports ...
    # Links on all ports are up.
    # %
    def clear_capture_buffer(self, port_string, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(PacketControlConstants.PACKET_CONTROL_API)
        # assert isinstance(api, PacketControlApi)
        cmd_obj = api.packet_control(TrafficGenerationUtils.merge_arrays(
            {PacketControlConstants.ACTION_CMD: PacketControlConstants.ACTION_RESET,
             PacketControlConstants.PORT_HANDLE_CMD: port_string},
            options))
        if "Ixia" not in self.__class__.__name__:
            self.capture_buffer.clear_capture_buffer(port_string)

    def set_capture_mode(self, port_string, mode, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        # assert isinstance(api, InterfaceConfigApi)
        cmd_obj = api.interface_config(TrafficGenerationUtils.merge_arrays(
            {InterfaceConfigConstants.PORT_RX_MODE_CMD: mode,
             InterfaceConfigConstants.PORT_HANDLE_CMD: port_string},
            options))
        # assert isinstance(cmd_obj, TrafficGeneratingCommandObject)
        return self._determine_error(self.set_capture_mode.__name__, cmd_obj, port_string)

    def _determine_error(self, method_name, cmd_obj, port_string=None):
        kw_results = []
        ret_string = str(cmd_obj.return_text)
        if method_name == self.set_capture_mode.__name__:
            if "ERROR " in ret_string:
                if "transmitMode" in ret_string:
                    self.logger.log_info("Port " + str(port_string) + " did not set the port capture mode correctly.")
                    self.logger.log_error("Port " + str(port_string) + " did not set the port capture mode correctly.")
                    self.logger.log_debug(ret_string)
                    kw_results.append(KeywordResult(self.name, False,
                                                    "Port " + str(port_string) +
                                                    " did not set the port capture mode correctly.",
                                                    "",
                                                    cmd_obj))
                elif "Cannot retrieve configured settings for port" in ret_string:  # this might be more global
                    self.logger.log_info("Port " + str(port_string) + " did not set the port capture mode correctly.")
                    self.logger.log_error("Port " + str(port_string) + " did not set the port capture mode correctly.")
                    self.logger.log_debug(ret_string)
                    kw_results.append(KeywordResult(self.name, False,
                                                    "Port " + str(port_string) +
                                                    " did not set the port capture mode correctly.",
                                                    "",
                                                    cmd_obj))
            else:
                kw_results.append(KeywordResult(self.name, True,
                                                "Port " + str(port_string) + " set the port capture mode correctly.",
                                                "",
                                                cmd_obj))
        elif method_name == self.take_port_ownership.__name__:
            if "Error" in ret_string:
                mess = "Port " + str(port_string) + " failed to take ownership."
                self.logger.log_info(mess)
                self.logger.log_error(mess)
                self.logger.log_debug(ret_string)
                kw_results.append(KeywordResult(self.name, False, mess, "", cmd_obj))
            else:
                kw_results.append(KeywordResult(self.name, True, "Port " + str(port_string) +
                                                " set the port capture mode correctly.", "", cmd_obj))

        return kw_results

    # {status 1} {1/1/2 {{aggregate {{uds1_frame_count 0} {uds2_frame_count 0} {average_deviation N/A}
    # {average_latency N/A} {num_frames N/A} {max_latency N/A} {min_latency N/A} {standard_deviation N/A}
    # {average_deviation_per_chunk N/A} {standard_deviation_per_chunk N/A}}}}}
    # set temp_stats [keylget hltapipacketstatsapi_packet_stats 1/1/2.aggregate.num_frames]
    # N/A
    def get_port_capture(self, port_handle, key, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.get_api(PacketStatsConstants.PACKET_STATS_API)
        assert isinstance(api, PacketStatsApi)
        ret_string = api.packet_stats(TrafficGenerationUtils.merge_arrays(
            {PacketStatsConstants.PORT_HANDLE_CMD: port_string,
             PacketStatsConstants.ACTION_CMD: PacketStatsConstants.ACTION_FILTERED,
             PacketStatsConstants.FORMAT_CMD: PacketStatsConstants.FORMAT_VAR}, options))
        ret_string = self.send_command("set temp_stats [keylget hltapipacketstatsapi_packet_stats " + port_string +
                                       ".aggregate." + key + "]")
        # process ret string into a dictionary
        ret_string = ret_string.replace('%', '')
        return ret_string.strip()

    def get_port_capture_frame(self, port_handle, frame_num, key, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.get_api(PacketStatsConstants.PACKET_STATS_API)
        assert isinstance(api, PacketStatsApi)
        ret_string = api.packet_stats(TrafficGenerationUtils.merge_arrays(
            {PacketStatsConstants.PORT_HANDLE_CMD: port_string,
             PacketStatsConstants.FORMAT_CMD: PacketStatsConstants.FORMAT_VAR}, options))
        ret_string = self.send_command("set temp_stats [keylget hltapipacketstatsapi_packet_stats " + port_string +
                                       ".frame." + str(frame_num) + "." + key + "]")
        # process ret string into a dictionary
        ret_string = ret_string.replace('%', '')
        return ret_string.strip()

    # set hltapitrafficstatsapi_traffic_stats [ixia::traffic_stats \
    # -mode all \
    # -port_handle 1/1/1 \
    # ]
    # DEBUG - 2019-02-06 11:25:00,517 - {1/1/1 {{aggregate {{rx {{uds2_count {Stat userDefinedStat2 not supported}}
    # {qos2_rate 0} {pkt_byte_count {Stat bytesReceived not supported}} {qos0_count 0} {vlan_pkts_rate
    # {Stat vlanTaggedFramesRx not supported}} {sequence_errors_count {Stat sequenceErrors not supported}}
    # {qos4_count 0} {crc_errors_count 0} {qos7_rate 0} {uds1_count {Stat userDefinedStat1 not supported}}
    # {raw_pkt_count 0} {data_int_errors_count {Stat dataIntegrityErrors not supported}} {uds2_rate
    # {Stat userDefinedStat2 not supported}} {qos4_rate 0} {vlan_pkts_count {Stat vlanTaggedFramesRx not supported}}
    # {data_int_errors_rate {Stat dataIntegrityErrors not supported}} {raw_pkt_rate 0}
    # {pkt_bit_count {Stat bitsReceived not supported}} {qos3_count 0} {qos1_rate 0} {fragments_count 0}
    # {collisions_count 0} {qos7_count 0} {sequence_frames_count {Stat sequenceFrames not supported}}
    # {sequence_errors_rate {Stat sequenceErrors not supported}} {collisions_rate 0} {fragments_rate 0}
    # {data_int_frames_rate {Stat dataIntegrityFrames not supported}} {qos6_rate 0} {qos2_count 0} {pkt_count 0}
    # {dribble_errors_count 0} {uds1_rate {Stat userDefinedStat1 not supported}} {qos3_rate 0} {qos6_count 0}
    # {data_int_frames_count {Stat dataIntegrityFrames not supported}} {dribble_errors_rate 0} {qos0_rate 0}
    # {crc_errors_rate 0} {oversize_count 0} {pkt_bit_rate {Stat bitsReceived not supported}}
    # {sequence_frames_rate {Stat sequenceFrames not supported}} {pkt_rate 0} {undersize_rate 0} {qos1_count 0}
    # {pkt_byte_rate {Stat bytesReceived not supported}} {protocol_pkt_count 0} {qos5_count 0} {undersize_count 0}
    # {oversize_rate 0} {qos5_rate 0} {protocol_pkt_rate {Stat protocolServerRx not supported}}}} {tx {{raw_pkt_count 0}
    # {pkt_byte_count 0} {total_pkt_rate 0} {pkt_bit_count 0} {pkt_bit_rate 0} {pkt_rate 0} {pkt_count 0}
    # {total_pkt_bytes 0} {total_pkts_bytes 0} {elapsed_time 0.00} {pkt_byte_rate 0} {protocol_pkt_rate
    # {Stat protocolServerTx not supported}} {total_pkts 0} {raw_pkt_rate 0} {protocol_pkt_count 0}}}}}
    # {elapsed_time {Stat transmitDuration not supported}}}} {seconds 1549470299} {clicks 718319134} {status 1}
    # %

    def get_port_statistic(self, port_handle, tx_or_rx, key, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.get_api(TrafficStatsConstants.TRAFFIC_STATS_API)
        assert isinstance(api, TrafficStatsApi)
        ret_string = api.traffic_stats(TrafficGenerationUtils.merge_arrays(
            {TrafficStatsConstants.MODE_CMD: TrafficStatsConstants.MODE_ALL,
             TrafficStatsConstants.PORT_HANDLE_CMD: port_string},
            options))
        ret_string = self.send_command("set temp_stats [keylget hltapitrafficstatsapi_traffic_stats " + port_string +
                                       ".aggregate." + tx_or_rx + "." + key + "]")
        # process ret string into a dictionary
        ret_string = ret_string.replace('%', '')
        return ret_string.strip()

    def get_port_stream_statistic(self, port_handle, stream_id, tx_or_rx, key, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_handle)
        api = self.get_api(TrafficStatsConstants.TRAFFIC_STATS_API)
        assert isinstance(api, TrafficStatsApi)
        ret_string = api.traffic_stats(TrafficGenerationUtils.merge_arrays(
            {TrafficStatsConstants.MODE_CMD: TrafficStatsConstants.MODE_ALL,
             TrafficStatsConstants.PORT_HANDLE_CMD: port_string},
            options))
        ret_string = self.send_command("set temp_stats [keylget hltapitrafficstatsapi_traffic_stats " + port_string +
                                       ".stream." + str(stream_id) + "." + tx_or_rx + "." + key + "]")
        # process ret string into a dictionary
        ret_string = ret_string.replace('%', '')
        return ret_string.strip()

    def clear_statistics(self, port_string, options=None):
        if options is None:
            options = {}
        r"""
        set stats_info [ixia::traffic_control \
            -port_handle $tx_handle \
            -action clear_stats]
        """
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(TrafficControlConstants.TRAFFIC_CONTROL_API)
        # assert isinstance(api, TrafficControlApi)
        cmd_obj = api.traffic_control(TrafficGenerationUtils.merge_arrays(
            {TrafficControlConstants.ACTION_CMD: TrafficControlConstants.ACTION_CLEAR_STATS,
             TrafficControlConstants.PORT_HANDLE_CMD: port_string},
            options))

    def set_stream_transmit_mode(self, port_string, stream_id, mode):
        return self.logger.log_unimplemented_method()

    def configure_stream_using_packet(self, port_string, stream_id, packet, clear_all_streams=False, options=None):
        r"""
        set stream_info [ixia::traffic_config\
            -mode create\
            -streamid 1\
            -port_handle 1/1/1\
            -l3_protocol ipv4\
            -ip_src_addr "1.1.1.1"\
            -ip_dst_addr "2.2.2.2"\
            -transmit_mode continuous\
            -mac_src "00:22:33:44:55:65"\
            -mac_dst "00:22:33:44:55:66"\
            -rate_pps $rate_pps]
        """
        if options is None:
            options = {}

        port_string = self.convert_port_to_port_handle(port_string)
        if clear_all_streams:
            if clear_all_streams != "Nothing":
                self.clear_all_streams(port_string)
        else:
            self.clear_stream(port_string, stream_id)  # atg0007417
        if isinstance(packet, AbstractPacket):
            assert isinstance(packet, AbstractPacket)
            packet_dict = {}
            packet_dict.update(options)
            packet_dict.update(packet.get_all_hltapi_commands(self, stream_id))

            packet_dict[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
            packet_dict[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
            # packet_dict[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_MODIFY # atg0007417
            if TrafficConfigConstants.MODE_CMD not in packet_dict:
                packet_dict[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            packet_dict[TrafficConfigConstants.ENABLE_PGID_CMD] = 0
            packet_length = packet.get_length()
            if packet_length and str(packet_length) != "False":
                packet_dict[TrafficConfigConstants.FRAME_SIZE_CMD] = packet.get_length()
            api = self.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
            assert isinstance(api, TrafficConfigApi)
            ret_string = api.traffic_config(TrafficGenerationUtils.merge_arrays(packet_dict, options))
            # if 'no such element' in str(ret_string) or 'ERROR' in str(ret_string): # atg0007417
            #     packet_dict[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_CREATE
            #     ret_string = api.traffic_config(TrafficGenerationUtils.merge_arrays(packet_dict, options))
            output = ""
            if "ERROR" in str(ret_string.return_text):
                for item in ret_string.return_text:
                    new_output = "".join(item)
                    output += new_output + "\n"
                self.logger.log_error(output)
                self.logger.log_error("Packet config was rejected!!!")

            if packet.is_field_set(packet.get_source_mac_mode()):
                self.configure_stream_mac_src_options(port_string, stream_id,
                                                      packet.get_source_mac(),
                                                      packet.get_source_mac_mode(),
                                                      packet.get_source_mac_count(),
                                                      packet.get_source_mac_mask(),
                                                      packet.get_source_mac_seed())

            if packet.is_field_set(packet.get_destination_mac_mode()):
                self.configure_stream_mac_dst_options(port_string, stream_id,
                                                      packet.get_destination_mac(),
                                                      packet.get_destination_mac_mode(),
                                                      packet.get_destination_mac_count(),
                                                      packet.get_destination_mac_mask(),
                                                      packet.get_destination_mac_seed())
            if isinstance(packet, IpV4PacketHeader):
                if packet.is_field_set(packet.get_source_ip_mode()):
                    self.configure_stream_ip_src_options(port_string, stream_id,
                                                         packet.get_source_ip(),
                                                         packet.get_source_ip_mode(),
                                                         packet.get_source_ip_count(),
                                                         packet.get_source_ip_mask())
                if packet.is_field_set(packet.get_destination_ip_mode()):
                    self.configure_stream_ip_dst_options(port_string, stream_id,
                                                         packet.get_destination_ip(),
                                                         packet.get_destination_ip_mode(),
                                                         packet.get_destination_ip_count(),
                                                         packet.get_destination_ip_mask())

            if isinstance(packet, IpV6PacketHeader):
                if packet.is_field_set(packet.get_ipv6_source_address_mode()):
                    self.get_traffic_helper().configure_stream_ipv6_src_options(port_string, stream_id,
                                                                                packet.get_ipv6_source_address(),
                                                                                packet.get_ipv6_source_address_mode(),
                                                                                packet.get_ipv6_source_address_count(),
                                                                                packet.get_ipv6_source_address_mask())
                if packet.is_field_set(packet.get_ipv6_destination_address_mode()):
                    self.configure_stream_ipv6_dst_options(port_string, stream_id,
                                                           packet.get_ipv6_destination_address(),
                                                           packet.get_ipv6_destination_address_mode(),
                                                           packet.get_ipv6_destination_address_count(),
                                                           packet.get_ipv6_destination_address_mask())

            if isinstance(packet, ArpPacketHeader):
                assert isinstance(packet, ArpPacketHeader)
                if packet.is_field_set(packet.get_arp_sender_hardware_address_mode()):
                    self.get_traffic_helper().\
                        configure_stream_arp_sender_hardware_options(port_string, stream_id,
                                                                     packet.get_arp_sender_hardware_address(),
                                                                     packet.get_arp_sender_hardware_address_mode(),
                                                                     packet.get_arp_sender_hardware_address_count()
                                                                     # packet.get_arp_sender_hardware_address_step()
                                                                     )

                if packet.is_field_set(packet.get_arp_source_protocol_address_mode()):
                    self.get_traffic_helper().\
                        configure_stream_arp_source_protocol_options(port_string, stream_id,
                                                                     packet.get_arp_sender_protocol_address(),
                                                                     packet.get_arp_source_protocol_address_mode(),
                                                                     packet.get_arp_source_protocol_address_count()
                                                                     # packet.get_arp_sender_protocol_address_step()
                                                                     )

                if packet.is_field_set(packet.get_arp_target_hardware_address_mode()):
                    self.get_traffic_helper().\
                        configure_stream_arp_target_hardware_options(port_string, stream_id,
                                                                     packet.get_arp_target_hardware_address(),
                                                                     packet.get_arp_target_hardware_address_mode(),
                                                                     packet.get_arp_target_hardware_address_count()
                                                                     # packet.get_arp_target_hardware_address_step()
                                                                     )

                if packet.is_field_set(packet.get_arp_target_protocol_address_mode()):
                    self.get_traffic_helper().\
                        configure_stream_arp_target_protocol_options(port_string, stream_id,
                                                                     packet.get_arp_target_protocol_address(),
                                                                     packet.get_arp_target_protocol_address_mode(),
                                                                     packet.get_arp_target_protocol_address_count()
                                                                     # packet.get_arp_target_protocol_address_step()
                                                                     )

    def clear_stream(self, port_string, stream_id, options=None):
        r"""
        remove Remove/disable an existing stream/traffic item.
        Dependencies: traffic_generator must be ixos/ixnetwork/ixnetwork_540 and stream_id must be provided.
        When traffic_generator is ixos, it disables the stream, when traffic_generator is ixnetwork it removes the
        traffic item.
        When traffic_generator is ixnetwork_540: if stream_id is a traffic_item it removes it;
        if stream_id is a high level stream it suspends it;
        if stream_id is a header handle it removes it.
        set stream_info [ixia::traffic_config\
            -mode remove\
            -streamid 1\
            -port_handle 1/1/1\
            ]
        """
        if options is None:
            options = {}

        port_string = self.convert_port_to_port_handle(port_string)
        packet_dict = dict()
        packet_dict[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        packet_dict[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        packet_dict[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_REMOVE
        api = self.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        cmd_obj = api.traffic_config(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    # set hltapitrafficconfigapi_traffic_config [ixia::traffic_config \
    # -port_handle 1/1/1 \
    # -mode reset \
    # ]
    # DEBUG - 2019-02-04 14:27:48,522 - {status 1}
    # %
    def clear_all_streams(self, port_string, options=None):
        if options is None:
            options = {}
        """
        remove Remove/disable an existing stream/traffic item.
        Dependencies: traffic_generator must be ixos/ixnetwork/ixnetwork_540 and stream_id must be provided.
        When traffic_generator is ixos, it disables the stream, when traffic_generator is ixnetwork it removes the
        traffic item.
        When traffic_generator is ixnetwork_540: if stream_id is a traffic_item it removes it;
        if stream_id is a high level stream it suspends it;
        if stream_id is a header handle it removes it.
        set stream_info [ixia::traffic_config\
            -mode remove\
            -streamid 1\
            -port_handle 1/1/1\
            ]
        """

        port_string = self.convert_port_to_port_handle(port_string)
        packet_dict = dict()
        packet_dict[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        packet_dict[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_RESET
        api = self.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        cmd_obj = api.traffic_config(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    def set_port_phy_mode(self, port_string, mode):
        return self.logger.log_unimplemented_method()

    def register_apis(self):
        super(HltapiTrafficGeneratingDevice, self).register_apis()
        self.logger.log_debug("registering HltapiTrafficGeneratingDevice Apis")
        # self.logger.log_info("registering HltapiTrafficGeneratingDevice Apis")
        self.register_api(ConnectConstants.CONNECT_API, ConnectApi(self))
        self.register_api(SessionInfoConstants.SESSION_INFO_API, SessionInfoApi(self))
        self.register_api(InterfaceConfigConstants.INTERFACE_CONFIG_API, InterfaceConfigApi(self))
        self.register_api(TrafficConfigConstants.TRAFFIC_CONFIG_API, TrafficConfigApi(self))
        self.register_api(TrafficControlConstants.TRAFFIC_CONTROL_API, TrafficControlApi(self))
        self.register_api(PacketConfigBuffersConstants.PACKET_CONFIG_BUFFERS_API, PacketConfigBuffersApi(self))
        self.register_api(PacketControlConstants.PACKET_CONTROL_API, PacketControlApi(self))
        self.register_api(PacketInfoConstants.PACKET_INFO_API, PacketInfoApi(self))
        self.register_api(TrafficStatsConstants.TRAFFIC_STATS_API, TrafficStatsApi(self))
        self.register_api(PacketStatsConstants.PACKET_STATS_API, PacketStatsApi(self))
        self.register_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API, PacketConfigFilterApi(self))
        self.register_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API, PacketConfigTriggersApi(self))
        self.register_api(InterfaceStatsConstants.INTERFACE_STATS_API, InterfaceStatsApi(self))
        self.register_api(ResetPortConstants.RESET_PORT_API, ResetPortApi(self))

        # bgp
        self.register_api(EmulationBgpConfigConstants.EMULATION_BGP_CONFIG_API, EmulationBgpConfigApi(self))
        self.register_api(EmulationBgpControlConstants.EMULATION_BGP_CONTROL_API, EmulationBgpControlApi(self))
        self.register_api(EmulationBgpInfoConstants.EMULATION_BGP_INFO_API, EmulationBgpInfoApi(self))
        self.register_api(EmulationBgpRouteConfigConstants.EMULATION_BGP_ROUTE_CONFIG_API,
                          EmulationBgpRouteConfigApi(self))

        self.register_api(UdsFilterPalletteConfigConstants.UDS_FILTER_PALLETTE_CONFIG_API,
                          UdsFilterPalletteConfigApi(self))
        self.register_api(UdsConfigConstants.UDS_CONFIG_API, UdsConfigApi(self))
        self.register_api(TrafficL47ConfigConstants.TRAFFIC_L47_CONFIG_API, TrafficL47ConfigApi(self))

        # ospf
        self.register_api(EmulationOspfConfigConstants.EMULATION_OSPF_CONFIG_API, EmulationOspfConfigApi(self))
        self.register_api(EmulationOspfControlConstants.EMULATION_OSPF_CONTROL_API, EmulationOspfControlApi(self))
        self.register_api(EmulationOspfInfoConstants.EMULATION_OSPF_INFO_API, EmulationOspfInfoApi(self))
        self.register_api(EmulationOspfTopologyRouteConfigConstants.EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG_API,
                          EmulationOspfTopologyRouteConfigApi(self))
        self.register_api(EmulationOspfNetworkGroupConfigConstants.EMULATION_OSPF_NETWORK_GROUP_CONFIG_API,
                          EmulationOspfNetworkGroupConfigApi(self))
        self.register_api(EmulationOspfLsaConfigConstants.EMULATION_OSPF_LSA_CONFIG_API,
                          EmulationOspfLsaConfigApi(self))
