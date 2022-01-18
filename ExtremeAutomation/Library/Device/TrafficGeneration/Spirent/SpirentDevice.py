import re
import socket
from ExtremeAutomation.Library.Utils.Time import current_milli_time
from ExtremeAutomation.Library.Net.Packet.SapPacketHeader import SapPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import SnapPacketHeader
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import IpxPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LldpPacketHeader import LldpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MstpPacketHeader import MstpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BpduPacketHeader import BpduPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IcmpPacketHeader import IcmpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RadiusPacketHeader import RadiusPacketHeader
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SpanningTreePacketHeader import SpanningTreePacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiConnectApi import ConnectApi
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import ArpPacketHeader
from ExtremeAutomation.Library.Device.Common.Agents.IxiaConnectionTelnetAgent import IxiaConnectionTelnetAgent
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiConnectApi import ConnectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import \
    InterfaceConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceStatsApi import \
    InterfaceStatsConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigBuffersApi import \
    PacketConfigBuffersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import \
    PacketConfigFilterConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketInfoApi import PacketInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentPacketInfoApi import \
    SpirentPacketInfoApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import \
    PacketConfigTriggersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketControlApi import \
    PacketControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketStatsApi import PacketStatsConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiResetPortApi import ResetPortConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiSessionInfoApi import SessionInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficControlApi import \
    TrafficControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficL47ConfigApi import \
    TrafficL47ConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficStatsApi import \
    TrafficStatsConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficTagConfigApi import \
    TrafficTagConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsConfigApi import UdsConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsFilterPalletteConfigApi import \
    UdsFilterPalletteConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfConfigApi import \
    EmulationOspfConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfControlApi import \
    EmulationOspfControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfInfoApi import \
    EmulationOspfInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfLsaConfigApi import \
    EmulationOspfLsaConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfNetworkGroupConfigApi \
    import EmulationOspfNetworkGroupConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfTopologyRouteConfigApi \
    import EmulationOspfTopologyRouteConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.HltapiTrafficGeneratingDevice import \
    HltapiTrafficGeneratingDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentConnectApi import \
    SpirentConnectApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentInterfaceConfigApi import \
    SpirentInterfaceConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentInterfaceStatsApi import \
    SpirentInterfaceStatsApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentPacketConfigBuffersApi import \
    SpirentPacketConfigBuffersApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentPacketConfigFilterApi import \
    SpirentPacketConfigFilterApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentPacketConfigTriggersApi \
    import SpirentPacketConfigTriggersApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentPacketControlApi import \
    SpirentPacketControlApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentPacketStatsApi import \
    SpirentPacketStatsApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentResetPortApi import \
    SpirentResetPortApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentSessionInfoApi import \
    SpirentSessionInfoApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentTrafficConfigApi import \
    SpirentTrafficConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentTrafficControlApi import \
    SpirentTrafficControlApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentTrafficL47ConfigApi import \
    SpirentTrafficL47ConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentTrafficStatsApi import \
    SpirentTrafficStatsApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentTrafficTagConfigApi import \
    SpirentTrafficTagConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentUdsConfigApi import \
    SpirentUdsConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentUdsFilterPalletteConfigApi \
    import SpirentUdsFilterPalletteConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.Ospf.HltapiSpirentEmulationOspfConfigApi \
    import SpirentEmulationOspfConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.Ospf.HltapiSpirentEmulationOspfControlApi \
    import SpirentEmulationOspfControlApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.Ospf.HltapiSpirentEmulationOspfInfoApi \
    import SpirentEmulationOspfInfoApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.Ospf.\
    HltapiSpirentEmulationOspfLsaConfigApi import SpirentEmulationOspfLsaConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.Ospf.\
    HltapiSpirentEmulationOspfNetworkGroupConfigApi import SpirentEmulationOspfNetworkGroupConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.Ospf.\
    HltapiSpirentEmulationOspfTopologyRouteConfigApi import SpirentEmulationOspfTopologyRouteConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.SpirentDeviceCaptureHelper import \
    SpirentDeviceCaptureHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.SpirentDeviceStatisticHelper import \
    SpirentDeviceStatisticHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.SpirentDeviceTrafficHelper import \
    SpirentDeviceTrafficHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.SpirentArpHelper import SpirentArpHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.SpirentStreamConfigTclApi import \
    SpirentStreamConfigTclApi


class SpirentDevice(HltapiTrafficGeneratingDevice, SpirentDeviceCaptureHelper, SpirentDeviceStatisticHelper,
                    SpirentDeviceTrafficHelper, SpirentArpHelper):
    def __init__(self):
        super(SpirentDevice, self).__init__()
        SpirentDeviceCaptureHelper.__init__(self, self)
        SpirentDeviceStatisticHelper.__init__(self, self)
        SpirentDeviceTrafficHelper.__init__(self, self)
        self._nameSpace = "sth"
        self.capture_buffer = SpirentCaptureBuffer(self)

    def connect(self, host, port=5679):
        if self.connection is None:
            self.connection = self.agents[TrafficGenerationConstants.TELNET]
        if self.connection.is_connected():
            return

        try:
            self.connection.connect()
            reply = self.connection.wait_until_quiet(1000)
            self.logger.log_debug(reply)
            self.init_connection()
        except socket.error:
            self.initialized = False

    def init_connection(self):
        if self.initialized:
            return
        ret_string = self.send_command("package require SpirentTestCenter")
        ret_string += self.send_command("package require SpirentHltApi")
        ret_string += self.send_command("::sth::test_config -logfile stats_hltLogfile \\\n" +
                                        "-log 1\\\n" +
                                        "-vendorlogfile stats_stcExport\\\n" +
                                        "-vendorlog 1\\\n" +
                                        "-hltlog 1\\\n" +
                                        "-hltlogfile stats_hltExport \\\n" +
                                        "-hlt2stcmappingfile  stats_hlt2StcMapping \\\n" +
                                        "-hlt2stcmapping 1 \\\n" +
                                        "-log_level 7")
        self.initialized = True
        self.logger.log_debug(ret_string)
        return ""

    def get_traffic_helper(self):
        return self

    def get_statistic_helper(self):
        return self

    def get_capture_helper(self):
        return self

    def send_command(self, cmd):
        if self.tgen_debug:
            self.logger.log_debug(cmd)
        cmd = cmd.encode('ascii', 'ignore')
        self.connection.write(cmd + "\n")
        reply = self.connection.wait_until_quiet(100)
        indexrt = 1
        while indexrt < 10 and not reply.strip().endswith("%"):
            reply += self.connection.wait_until_quiet(1000 * indexrt)
            indexrt += 1
        if self.tgen_debug:
            self.logger.log_debug(reply)
        return reply

    def convert_port_string_to_variable(self, port, stream=None):
        port_list = port.split("/")
        if len(port_list) > 2:
            port_list = port_list[-2:]
        port_name = self.convert_port_to_port_name(port)
        port = "/".join(port_list)
        port_name = port_name.replace("$", "")
        if stream:
            port_name += "_" + str(stream)
        return port_name

    def clear_stream(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        port_name_stream = "$" + self.convert_port_string_to_variable(port_string, stream_id)
        super(SpirentDevice, self).clear_stream(port_string, port_name_stream, options)
        self.send_command("puts [stc::delete " + port_name_stream + " ]")

    def clear_all_streams(self, port_string, options=None):
        if options is None:
            options = {}
        port_name_string = self.convert_port_to_port_name(port_string)
        port_string = self.convert_port_name_to_port_string(port_name_string)
        ret_string = self.send_command("" +
                                       "foreach sb [stc::get " + port_name_string + " -children-streamblock] {\n" +
                                       "set hltapitrafficconfigapi_traffic_config [sth::traffic_config \\\n " +
                                       "     -stream_id $sb \\\n " +
                                       "     -port_handle $port \\\n " +
                                       "     -mode remove \\\n " + "]\n" +
                                       "stc::delete $sb\n" + "}\n")

    def configure_stream_using_packet(self, port_string, stream_id, packet, clear_all_streams=False, options=None):
        if options is None:
            options = {}
        if isinstance(packet, SnapPacketHeader):
            options[TrafficConfigConstants.L2_ENCAP_CMD] = TrafficConfigConstants.L2_ENCAP_ETHERNET_8023_SNAP
        elif isinstance(packet, SapPacketHeader):
            options[TrafficConfigConstants.L2_ENCAP_CMD] = TrafficConfigConstants.L2_ENCAP_ETHERNET_8022_SAP
        super(SpirentDevice, self).configure_stream_using_packet(port_string, stream_id, packet, options=options)
        port_name_stream = self.convert_port_string_to_variable(port_string, stream_id)
        self.send_command("set " + str(port_name_stream) +
                          " [keylget hltapitrafficconfigapi_traffic_config stream_id ]")
        api = self.get_api(SpirentDeviceConstants.SPIRENT_STREAM_CONFIG_TCL_API)
        assert isinstance(api, SpirentStreamConfigTclApi)
        # self.logger.log_debug("VlanStackPacketHeader")

        api.configure_fixed_length(port_name_stream, packet)
        if isinstance(packet, Ethernet2PacketHeader):
            api.configure_ethernet2_traffic(port_name_stream, packet)
        if isinstance(packet, VlanStackPacketHeader):
            api.configure_vlan_stack_traffic(port_name_stream, packet)
        if isinstance(packet, TaggedPacketHeader):
            api.configure_tagged_traffic(port_name_stream, packet)
        if isinstance(packet, SapPacketHeader):
            api.configure_sap_traffic(port_name_stream, packet)
        if isinstance(packet, IpxPacketHeader):
            api.configure_ipx_traffic(port_name_stream, packet)
        if isinstance(packet, IpV4PacketHeader):
            api.configure_ipv4_traffic(port_name_stream, packet)
        if isinstance(packet, IpV6PacketHeader):
            api.configure_ipv6_traffic(port_name_stream, packet)
        if isinstance(packet, TcpPacketHeader):
            api.configure_tcp_traffic(port_name_stream, packet)
        if isinstance(packet, ArpPacketHeader):
            api.configure_arp_traffic(port_name_stream, packet)
        if isinstance(packet, IcmpPacketHeader):
            api.configure_icmp_traffic(port_name_stream, packet)

        # payload setters:
        if isinstance(packet, MstpPacketHeader):
            api.configure_mstp_traffic(port_name_stream, packet)
        elif isinstance(packet, SpanningTreePacketHeader):
            api.configure_spanningtree_traffic(port_name_stream, packet)
        elif isinstance(packet, BpduPacketHeader):
            api.configure_bpdu_traffic(port_name_stream, packet)
        elif isinstance(packet, LldpPacketHeader):
            api.configure_lldp_traffic(port_name_stream, packet)
        elif isinstance(packet, RadiusPacketHeader):
            api.configure_radius_traffic(port_name_stream, packet)

    # def clear_stream(self, port_string, stream_id, options=None):
    #     if options is None:
    #         options = {} # IxTclHal only
    #     return self.logger.log_unimplemented_method()

    def stream_exists(self, port_string, stream_id):
        port_name_stream = self.convert_port_string_to_variable(port_string, stream_id)
        ret_string = self.send_command("puts [stc::get $" + port_name_stream + " ]")
        return "no such variable" not in ret_string and "invalid handle" not in ret_string

    def get_stream(self, port_string, stream_id):
        port_name_stream = self.convert_port_string_to_variable(port_string, stream_id)
        #  this can get streams not saved....
        #         ret_string = self.send_command("set i 0\n"+
        #     "foreach port [stc::get project1 -children-port] {\n"+
        #     "        foreach sb [stc::get $port -children-streamblock] {\n"+
        #     "          incr i\n"+
        #     "          puts [stc::get $port -children-streamblock]\n"+
        #     "        }\n"+
        #     "        puts \"$port:[stc::get $port -location] stream_count:$i\"\nset i 0\n"+
        #            "}\n")
        #
        # self.send_command("[stc::get \"streamblock1\"]")
        if self.stream_exists(port_string, stream_id):
            ret_string = self.send_command("puts [stc::get $" + port_name_stream + " ]")
            ret_string += "port=" + str(port_string) + ";"
            ret_string += "ID=" + str(stream_id) + ";"
            ret_string += "name=" + self.trim_command(self.send_command("stc::get $" + port_name_stream +
                                                                        " -name")) + ";"
            ret_string += "DA=" + self.trim_command(self.send_command("stc::get $" + port_name_stream +
                                                                      " -ethernet:EthernetII.dstMac")) + ";"
            ret_string += "SA=" + self.trim_command(self.send_command("stc::get $" + port_name_stream +
                                                                      " -ethernet:EthernetII.srcMac")) + ";"
            ret_string += "name=" + self.trim_command(self.send_command("stc::get $" + port_name_stream +
                                                                        " -Active")) + ";"
            # ret_string += "is_enabled="+str(value).lower() + ";"
            # ret_string += self.is_stream_continuous(original_port, stream_id, True)
            return ret_string
        else:
            return None
    #
    # def get_all_stream(self, port_string):
    #     return self.logger.log_unimplemented_method()

    def get_stream_count(self, port_string):
        port_name_string = self.convert_port_to_port_name(port_string)
        port_string = self.convert_port_name_to_port_string(port_name_string)
        ret_string = self.send_command("set i 0\n" +
                                       "foreach port [stc::get project1 -children-port] {\n" +
                                       "        foreach sb [stc::get $port -children-streamblock] {\n" +
                                       "          incr i\n" +
                                       # "          puts [stc::get $port -children-streamblock]\n"+
                                       "        }\n" +
                                       "        puts \"$port:[stc::get $port -location] stream_count:$i\"\nset i 0\n" +
                                       "}\n")

        for line in ret_string.split("\n"):
            if "stream_count:" in line and "/" + port_string in line:
                return int(str(re.search(r'stream_count:(\d+)',
                                         ret_string).group()).replace("stream_count:", "").strip())
        return None

    def start_capture(self, port_string, options=None):
        self.capture_buffer.start_capture_buffer(port_string)
        super(SpirentDevice, self).start_capture(port_string, options)

    def stop_capture(self, port_string, options=None):
        if options is None:
            options = {}
        super(SpirentDevice, self).stop_capture(port_string, options)
        self.capture_buffer.stop_capture_buffer(port_string)

    def register_agents(self):
        super(SpirentDevice, self).register_agents()
        self.register_agent(TrafficGenerationConstants.TELNET, IxiaConnectionTelnetAgent(self))

    def take_port_ownership(self, host, user, port_string, reset=False, options=None):
        self.set_host_name(host)
        """
        set connect_info [sth::connect\
            -reset\
            -device 10.52.2.189\
            -port_list 1/1\
            -username ciscoUser
        ]
        """
        og_port_string = port_string
        port_string = self.convert_port_handle_to_port_string(port_string)
        capi = self.get_api(ConnectConstants.CONNECT_API)
        user = re.sub(r'[^A-Za-z0-9_]', '_', user)  # Valid values are: "An alphanumeric value (letters, numbers,
        #                                           # or underbars)"
        assert isinstance(capi, ConnectApi)
        options = {ConnectConstants.USERNAME_CMD: user}
        if reset:
            options[ConnectConstants.RESET_CMD] = ""
        temp = capi.connect_helper(host, port_string, options)

        if not isinstance(og_port_string, list):
            og_port_string = [og_port_string]
        for port in og_port_string:
            port_list = port.split("/")
            if len(port_list) > 2:
                port_list = port_list[-2:]
            port_name = self.convert_port_to_port_name(port)
            port = "/".join(port_list)
            port_name = port_name.replace("$", "")
            self.send_command("set " + port_name + " [keylget hltapiconnectapi_connect port_handle." + host + "." +
                              port + "]")

    def convert_port_to_port_handle(self, port_string):
        if isinstance(port_string, list):
            index = 0
            for port in port_string:
                port_string[index] = self.convert_port_to_port_handle(port)
                index += 1
        else:
            port_string = self.convert_port_to_port_name(port_string)
        if isinstance(port_string, list):
            return " ".join(port_string)
        else:
            return port_string

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
            port_string = self.convert_port_name_to_port_string(port_string)
        if isinstance(port_string, list):
            return " ".join(port_string)
        else:
            return port_string

    def get_name_space(self):
        if not hasattr(self, '_nameSpace') or self._nameSpace == "":
            self._nameSpace = "sth"
        return self._nameSpace

    def register_apis(self):
        super(SpirentDevice, self).register_apis()
        # print "registering Spirent Agents"
        self.logger.log_debug("registering Spirent Agents")
        self.register_api(SpirentDeviceConstants.SPIRENT_STREAM_CONFIG_TCL_API,
                          SpirentStreamConfigTclApi(self))

        self.register_api(TrafficTagConfigConstants.TRAFFIC_TAG_CONFIG_API, SpirentTrafficTagConfigApi(self))
        self.register_api(TrafficStatsConstants.TRAFFIC_STATS_API, SpirentTrafficStatsApi(self))
        self.register_api(TrafficControlConstants.TRAFFIC_CONTROL_API, SpirentTrafficControlApi(self))
        self.register_api(TrafficConfigConstants.TRAFFIC_CONFIG_API, SpirentTrafficConfigApi(self))
        self.register_api(SessionInfoConstants.SESSION_INFO_API, SpirentSessionInfoApi(self))
        self.register_api(ResetPortConstants.RESET_PORT_API, SpirentResetPortApi(self))
        self.register_api(PacketStatsConstants.PACKET_STATS_API, SpirentPacketStatsApi(self))
        self.register_api(PacketControlConstants.PACKET_CONTROL_API, SpirentPacketControlApi(self))
        self.register_api(PacketInfoConstants.PACKET_INFO_API, SpirentPacketInfoApi(self))
        self.register_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API,
                          SpirentPacketConfigTriggersApi(self))
        self.register_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API, SpirentPacketConfigFilterApi(self))
        self.register_api(PacketConfigBuffersConstants.PACKET_CONFIG_BUFFERS_API, SpirentPacketConfigBuffersApi(self))
        self.register_api(InterfaceStatsConstants.INTERFACE_STATS_API, SpirentInterfaceStatsApi(self))
        self.register_api(InterfaceConfigConstants.INTERFACE_CONFIG_API, SpirentInterfaceConfigApi(self))
        self.register_api(ConnectConstants.CONNECT_API, SpirentConnectApi(self))
        self.register_api(UdsFilterPalletteConfigConstants.UDS_FILTER_PALLETTE_CONFIG_API,
                          SpirentUdsFilterPalletteConfigApi(self))
        self.register_api(UdsConfigConstants.UDS_CONFIG_API, SpirentUdsConfigApi(self))
        self.register_api(TrafficL47ConfigConstants.TRAFFIC_L47_CONFIG_API, SpirentTrafficL47ConfigApi(self))

        # ospf
        self.register_api(EmulationOspfConfigConstants.EMULATION_OSPF_CONFIG_API, SpirentEmulationOspfConfigApi(self))
        self.register_api(EmulationOspfControlConstants.EMULATION_OSPF_CONTROL_API,
                          SpirentEmulationOspfControlApi(self))
        self.register_api(EmulationOspfInfoConstants.EMULATION_OSPF_INFO_API, SpirentEmulationOspfInfoApi(self))
        self.register_api(EmulationOspfLsaConfigConstants.EMULATION_OSPF_LSA_CONFIG_API,
                          SpirentEmulationOspfLsaConfigApi(self))
        self.register_api(EmulationOspfNetworkGroupConfigConstants.EMULATION_OSPF_NETWORK_GROUP_CONFIG_API,
                          SpirentEmulationOspfNetworkGroupConfigApi(self))
        self.register_api(EmulationOspfTopologyRouteConfigConstants.EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG_API,
                          SpirentEmulationOspfTopologyRouteConfigApi(self))


class SpirentCaptureBuffer(object):
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

    def set_capture_buffer(self, port_string, buff):
        self.bufferStopStamp[port_string] = current_milli_time()
        self.buffer[port_string] = buff

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


class SpirentDeviceConstants(object, metaclass=Singleton):
    """
    This is the Constants class for the command: traffic_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
    """

    # api reference constant for this api to get it from the device

    ARP_DST_HW_ADDR_CMD = "arp_dst_hw_addr"

    IPV6_DST_MODE_CMD = "ipv6_dst_mode"
    # Constant values for IPV6_DST_MODE_CMD
    IPV6_DST_MODE_FIXED_INCREMENT = "fixed increment"
    IPV6_DST_MODE_DECREMENT_LIST_RANDOM = "decrement list random"
    IPV6_DST_MODE_INCR_HOST_DECR_HOST = "incr_host decr_host"
    IPV6_DST_MODE_INCR_NETWORK = "incr_network"
    IPV6_DST_MODE_DECR_NETWORK = "decr_network"
    IPV6_DST_MODE_INCR_INTF_ID = "incr_intf_id"
    IPV6_DST_MODE_DECR_INTF_ID = "decr_intf_id"
    IPV6_DST_MODE_INCR_GLOBAL_TOP_LEVEL = "incr_global_top_level"
    IPV6_DST_MODE_DECR_GLOBAL_TOP_LEVEL = "decr_global_top_level"
    IPV6_DST_MODE_INCR_GLOBAL_NEXT_LEVEL = "incr_global_next_level"
    IPV6_DST_MODE_DECR_GLOBAL_NEXT_LEVEL = "decr_global_next_level"
    IPV6_DST_MODE_INCR_GLOBAL_SITE_LEVEL = "incr_global_site_level"
    IPV6_DST_MODE_DECR_GLOBAL_SITE_LEVEL = "decr_global_site_level"
    IPV6_DST_MODE_INCR_LOCAL_SITE_SUBNET = "incr_local_site_subnet"
    IPV6_DST_MODE_DECR_LOCAL_SITE_SUBNET = "decr_local_site_subnet"
    IPV6_DST_MODE_INCR_MCAST_GROUP = "incr_mcast_group"
    IPV6_DST_MODE_DECR_MCAST_GROUP = "decr_mcast_group"

    SPIRENT_STREAM_CONFIG_TCL_API = "SPIRENT_STREAM_CONFIG_TCL_API"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


# instantiate the class to access the constants
#   example TrafficConfigConstants.ARP_DST_HW_ADDR
