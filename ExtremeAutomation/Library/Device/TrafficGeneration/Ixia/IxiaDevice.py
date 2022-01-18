import socket
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxRouteIxTclHalApi import \
    IxRouteIxTclHalApi, IxRouteIxTclHalConstants
from ExtremeAutomation.Library.Device.Common.Agents.IxiaConnectionTelnetAgent import IxiaConnectionTelnetAgent
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaTrafficTagConfigApi import \
    IxiaTrafficTagConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaCaptureIxTclHalApi import \
    IxiaCaptureIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaStatisticsIxTclHal import \
    IxiaStatisticsIxTclHal
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaPortConfigIxTclHalApi import \
    IxiaPortConfigIxTclHalConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaStreamConfigIxTclHalApi import \
    IxiaStreamConfigIxTclHalApi, IxiaStreamConfigIxTclHalConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceCaptureHelper import IxiaDeviceCaptureHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceStatisticHelper import \
    IxiaDeviceStatisticHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceTrafficHelper import IxiaDeviceTrafficHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingTcpApi import NetworkEmulatingTcpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.HltapiTrafficGeneratingDevice import \
    HltapiTrafficGeneratingDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceConstants import IxiaDeviceConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficTagConfigApi import \
    TrafficTagConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.SapPacketHeader import SapPacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import IpxPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LldpPacketHeader import LldpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MstpPacketHeader import MstpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BpduPacketHeader import BpduPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IcmpPacketHeader import IcmpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RadiusPacketHeader import RadiusPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import ArpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.GrePacketHeader import GrePacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.VxlanPacketHeader import VxlanPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IpEncapsulatedPacketHeader import IpEncapsulatedPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SpanningTreePacketHeader import SpanningTreePacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficStatsApi import TrafficStatsConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaTrafficStatsApi import \
    IxiaTrafficStatsApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficControlApi import \
    TrafficControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaTrafficControlApi import \
    IxiaTrafficControlApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaTrafficConfigApi import \
    IxiaTrafficConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiSessionInfoApi import SessionInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaSessionInfoApi import \
    IxiaSessionInfoApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiResetPortApi import ResetPortConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaResetPortApi import IxiaResetPortApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketStatsApi import PacketStatsConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaPacketStatsApi import \
    IxiaPacketStatsApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketControlApi import PacketControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaPacketControlApi import \
    IxiaPacketControlApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketInfoApi import PacketInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaPacketInfoApi import \
    IxiaPacketInfoApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import \
    PacketConfigTriggersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaPacketConfigTriggersApi import \
    IxiaPacketConfigTriggersApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import \
    PacketConfigFilterConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaPacketConfigFilterApi import \
    IxiaPacketConfigFilterApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigBuffersApi import \
    PacketConfigBuffersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaPacketConfigBuffersApi import \
    IxiaPacketConfigBuffersApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceStatsApi import \
    InterfaceStatsConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaInterfaceStatsApi import \
    IxiaInterfaceStatsApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import \
    InterfaceConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaInterfaceConfigApi import \
    IxiaInterfaceConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiConnectApi import ConnectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaConnectApi import IxiaConnectApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsFilterPalletteConfigApi import \
    UdsFilterPalletteConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaUdsFilterPalletteConfigApi import \
    IxiaUdsFilterPalletteConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsConfigApi import UdsConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaUdsConfigApi import IxiaUdsConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficL47ConfigApi import \
    TrafficL47ConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.HltapiIxiaTrafficL47ConfigApi import \
    IxiaTrafficL47ConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxNetworkDevice import IxNetworkDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaArpHelper import IxiaArpHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfConfigApi import \
    EmulationOspfConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.Ospf.HltapiIxiaEmulationOspfConfigApi import \
    IxiaEmulationOspfConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfTopologyRouteConfigApi \
    import EmulationOspfTopologyRouteConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.Ospf.\
    HltapiIxiaEmulationOspfTopologyRouteConfigApi import IxiaEmulationOspfTopologyRouteConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfNetworkGroupConfigApi \
    import EmulationOspfNetworkGroupConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.Ospf.\
    HltapiIxiaEmulationOspfNetworkGroupConfigApi import IxiaEmulationOspfNetworkGroupConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfLsaConfigApi import \
    EmulationOspfLsaConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.Ospf.HltapiIxiaEmulationOspfLsaConfigApi \
    import IxiaEmulationOspfLsaConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfInfoApi import \
    EmulationOspfInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.Ospf.HltapiIxiaEmulationOspfInfoApi import \
    IxiaEmulationOspfInfoApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfControlApi import \
    EmulationOspfControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.HltApi.Ospf.HltapiIxiaEmulationOspfControlApi import \
    IxiaEmulationOspfControlApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaFilterPalletteIxTclHalApi import \
    IxiaFilterPalletteIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaFilterIxTclHalApi import IxiaFilterIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaPortConfigIxTclHalApi import \
    IxiaPortConfigIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaTcpApi import IxiaTcpApi
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult


class IxiaDevice(HltapiTrafficGeneratingDevice, IxiaDeviceCaptureHelper, IxiaDeviceStatisticHelper,
                 IxiaDeviceTrafficHelper, IxNetworkDevice, IxiaArpHelper):
    def __init__(self):
        super(IxiaDevice, self).__init__()
        IxNetworkDevice.__init__(self)
        IxiaDeviceCaptureHelper.__init__(self, self)
        IxiaDeviceStatisticHelper.__init__(self, self)
        IxiaDeviceTrafficHelper.__init__(self, self)
        self._nameSpace = "ixia"

    def connect(self, host, port=5678):
        self.set_host_name(host)
        self.set_port(port)
        if self.connection is None:
            self.connection = self.agents[TrafficGenerationConstants.TELNET]
        if self.connection.is_connected():
            return

        try:
            self.connection.connect()
            reply = self.connection.wait_until_quiet(2000)
            self.logger.log_debug(reply)
            if "8.50" in reply:
                self.send_command("set env(IXIA_VERSION) HLTSET224")
            elif "8.10" in reply:
                self.send_command("set env(IXIA_VERSION) HLTSET197")

            self.init_connection()
        except socket.error as e:
            self.initialized = False

    def init_connection(self):
        if self.initialized:
            return
        ret_string = self.send_command("package require Ixia")
        self.initialized = True
        retries = 3
        index = 0
        while "Loaded" not in ret_string and index < retries:
            ret_string += self.connection.wait_until_quiet(180)
            index += 1
        lines = ret_string.split("\n")
        for line in lines:
            if "Loaded" in line:
                try:
                    cols = line.split(" ")
                    key = cols[1]
                    val = cols[2].strip()
                    self.version[key] = val
                except Exception as e:
                    self.logger.log_debug(e)
        ret_string += self.send_command("package require IxTclHal")
        # self.logger.log_debug(ret_string)
        return ret_string

    def get_traffic_helper(self):
        return self

    def get_statistic_helper(self):
        return self

    def get_capture_helper(self):
        return self

    def set_stream_transmit_mode(self, port_string, stream_id, mode):
        api = self.get_api(IxiaDeviceConstants.IXIA_PORT_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaPortConfigIxTclHalApi)
        cmd_obj = api.set_transmit_mode(port_string, IxiaPortConfigIxTclHalConstants.TRANSMIT_MODE_PORTTXPACKETSTREAMS)

        api = self.get_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaStreamConfigIxTclHalApi)
        cmd_obj = api.set_dma_mode(port_string, stream_id, mode)

    def get_stream_transmit_action(self, port_string, stream_id):
        api = self.get_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaStreamConfigIxTclHalApi)
        return api.get_dma_mode(port_string, stream_id)

    def get_stream_transmit_action_string(self, port_string, stream_id):
        val = self.get_stream_transmit_action(port_string, stream_id)
        if val == "3":
            return "Next/Advance"
        elif val == "2":
            return "Stop Stream"
        elif val == "4":
            return "Goto First"
        elif val == "5":
            return "Goto First Loop Count"
        elif val == "1":
            return "Continuous Burst"
        elif val == "0":
            return "Continuous Packet"
        else:
            return "Unknown (" + str(val) + ")"

    def get_stream_transmit_mode(self, port_string, stream_id):
        api = self.get_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaStreamConfigIxTclHalApi)
        return api.get_dma_mode(port_string, stream_id)

    def get_stream_transmit_mode_string(self, port_string, stream_id):
        val = self.get_stream_transmit_mode(port_string, stream_id)
        if val == "3":
            return "Next/Advance"
        elif val == "2":
            return "Stop Stream"
        elif val == "4":
            return "Goto First"
        elif val == "5":
            return "Goto First Loop Count"
        elif val == "1":
            return "Continuous Burst"
        elif val == "0":
            return "Continuous Packet"
        else:
            return "Unknown (" + str(val) + ")"

    def get_port_transmit_mode(self, port_string):
        api = self.get_api(IxiaDeviceConstants.IXIA_PORT_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaPortConfigIxTclHalApi)
        return api.get_transmit_mode(port_string)

    def get_port_transmit_mode_string(self, port_string):
        val = self.get_port_transmit_mode(port_string)
        if val == "0":
            return "Packet Streams"
        elif val == "4":
            return "Advanced Stream Scheduler"
        else:
            return "Unknown (" + str(val) + ")"

    def configure_stream_using_packet(self, port_string, stream_id, packet, clear_all_streams=False, options=None):
        if options is None:
            options = {}
        new_mode = None
        if TrafficConfigConstants.TRANSMIT_MODE_CMD in options:
            mode = options[TrafficConfigConstants.TRANSMIT_MODE_CMD]
            if mode == TrafficConfigConstants.TRANSMIT_MODE_NEXT \
                    or mode == TrafficConfigConstants.TRANSMIT_MODE_END \
                    or mode == TrafficConfigConstants.TRANSMIT_MODE_RETURN_TO_ID:
                new_mode = mode
                options[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST
        port_string = self.convert_port_to_port_handle(port_string)
        super(IxiaDevice, self).configure_stream_using_packet(port_string, stream_id, packet, clear_all_streams,
                                                              options)
        if new_mode:
            if new_mode == TrafficConfigConstants.TRANSMIT_MODE_NEXT:
                self.set_stream_transmit_mode(port_string, stream_id,
                                              IxiaStreamConfigIxTclHalConstants.DMA_MODE_ADVANCE)
            elif new_mode == TrafficConfigConstants.TRANSMIT_MODE_END:
                self.set_stream_transmit_mode(port_string, stream_id,
                                              IxiaStreamConfigIxTclHalConstants.DMA_MODE_STOPSTREAM)
            elif new_mode == TrafficConfigConstants.TRANSMIT_MODE_RETURN_TO_ID:
                self.set_stream_transmit_mode(port_string, stream_id,
                                              IxiaStreamConfigIxTclHalConstants.DMA_MODE_GOTOFIRST)
        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaStreamConfigIxTclHalApi)
        cmd_obj = api.disable_time_stamp(port_string, stream_id)
        # self.logger.log_debug("VlanStackPacketHeader")
        if isinstance(packet, VlanStackPacketHeader):
            cmd_obj = api.configure_vlan_stack_traffic(port_string, stream_id, packet)
        if isinstance(packet, SapPacketHeader):
            cmd_obj = api.configure_sap_traffic(port_string, stream_id, packet)
        if isinstance(packet, IpxPacketHeader):
            cmd_obj = api.configure_ipx_traffic(port_string, stream_id, packet)
        if isinstance(packet, IpV4PacketHeader):
            cmd_obj = api.configure_ipv4_traffic(port_string, stream_id, packet)
        if isinstance(packet, IpV6PacketHeader):
            cmd_obj = api.configure_ipv6_traffic(port_string, stream_id, packet)
        if isinstance(packet, TcpPacketHeader):
            cmd_obj = api.configure_tcp_traffic(port_string, stream_id, packet)
        if isinstance(packet, ArpPacketHeader):
            cmd_obj = api.configure_arp_traffic(port_string, stream_id, packet)
        if isinstance(packet, IcmpPacketHeader):
            cmd_obj = api.configure_icmp_traffic(port_string, stream_id, packet)

        # payload setters:
        if isinstance(packet, MstpPacketHeader):
            cmd_obj = api.configure_mstp_traffic(port_string, stream_id, packet)
        elif isinstance(packet, SpanningTreePacketHeader):
            cmd_obj = api.configure_spanningtree_traffic(port_string, stream_id, packet)
        elif isinstance(packet, BpduPacketHeader):
            cmd_obj = api.configure_bpdu_traffic(port_string, stream_id, packet)
        elif isinstance(packet, LldpPacketHeader):
            cmd_obj = api.configure_lldp_traffic(port_string, stream_id, packet)
        elif isinstance(packet, RadiusPacketHeader):
            cmd_obj = api.configure_radius_traffic(port_string, stream_id, packet)
        elif isinstance(packet, GrePacketHeader):
            cmd_obj = api.configure_gre_traffic(port_string, stream_id, packet)
        elif isinstance(packet, VxlanPacketHeader):
            cmd_obj = api.configure_vxlan_traffic(port_string, stream_id, packet)
        elif isinstance(packet, IpEncapsulatedPacketHeader):
            cmd_obj = api.configure_ipencap_traffic(port_string, stream_id, packet)
        else:
            cmd_obj = api.configure_payload(port_string, stream_id, packet)

    def set_qos_mode(self, port_string, mode=InterfaceConfigConstants.QOS_PACKET_TYPE_VLAN, qos_byte_offset=None,
                     pattern_offset=None, pattern_match=None, pattern_mask=None, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        self.enable_qos_stats(port_string, True)
        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        options[InterfaceConfigConstants.QOS_PACKET_TYPE_CMD] = mode

        if qos_byte_offset:
            options[InterfaceConfigConstants.QOS_BYTE_OFFSET_CMD] = qos_byte_offset
        if pattern_mask:
            options[InterfaceConfigConstants.QOS_PATTERN_MASK_CMD] = pattern_mask
        if pattern_offset:
            options[InterfaceConfigConstants.QOS_PATTERN_MATCH_CMD] = pattern_match
        if pattern_offset:
            options[InterfaceConfigConstants.QOS_PATTERN_OFFSET_CMD] = pattern_offset
        options[InterfaceConfigConstants.PORT_RX_MODE_CMD] = (InterfaceConfigConstants.PORT_RX_MODE_CAPTURE + " " +
                                                              InterfaceConfigConstants.PORT_RX_MODE_WIDE_PACKET_GROUP)
        cmd_obj = api.interface_config(TrafficGenerationUtils.merge_arrays(
            {InterfaceConfigConstants.PORT_HANDLE_CMD: port_string}, options))
        return self._determine_error(self.set_qos_mode.__name__, cmd_obj, port_string)

    def enable_qos_stats(self, port_string, enable=True, options=None):
        if options is None:
            options = {}

        options[InterfaceConfigConstants.PORT_RX_MODE_CMD] = (InterfaceConfigConstants.PORT_RX_MODE_CAPTURE + " " +
                                                              InterfaceConfigConstants.PORT_RX_MODE_WIDE_PACKET_GROUP)

        port_string = self.convert_port_to_port_handle(port_string)
        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        # assert isinstance(api, InterfaceConfigApi)
        if enable:
            enable = 1
        else:
            enable = 0
        cmd_obj = api.interface_config(TrafficGenerationUtils.merge_arrays({
            InterfaceConfigConstants.QOS_STATS_CMD: enable,
            InterfaceConfigConstants.PORT_HANDLE_CMD: port_string}, options))
        return self._determine_error(self.enable_qos_stats.__name__, cmd_obj, port_string)

    def is_port_capturing(self, port_string):
        return self.logger.log_unimplemented_method()

    def take_port_ownership(self, host, user, port_string, reset=False, options=None):
        self.set_host_name(host)
        kw_results = []
        og_port_string = port_string
        # if reset:
        #     # set all the autonegotiation fields
        #     # ixia::interface_config -autonegotiation 1 -port_handle $port_handle -speed auto -duplex auto
        #     self.send_command("port setFactoryDefaults " + port_string)
        #     self.send_command("port set " + port_string)
        #     self.send_command("port write " + port_string)
        kw_results.extend(super(IxiaDevice, self).take_port_ownership(host, user, port_string, reset, options))
        if reset:
            # set all the autonegotiation fields
            # ixia::interface_config -autonegotiation 1 -port_handle $port_handle -speed auto -duplex auto
            pass
        return kw_results

    def clear_port_ownership(self, host, port_string, reset=False, options=None):
        kw = super(IxiaDevice, self).clear_port_ownership(host, port_string, reset, options)
        port_string = self.convert_port_to_port_handle(port_string)
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        self.send_command("ixPortClearOwnership " + str(port_string) + " force")
        return kw

    def clear_stream(self, port_string, stream_id, options=None):  # IxTclHal only
        if options is None:
            options = {}
        port_string = self.convert_port_to_port_handle(port_string)
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        self.send_command("stream remove " + str(port_string) + " " + str(stream_id))

    def stream_exists(self, port_string, stream_id):
        count = self.get_stream_count(port_string)
        return stream_id <= int(count)

    def get_stream(self, port_string, stream_id):
        original_port = port_string
        port_string = self.convert_port_to_port_handle(port_string)
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        if self.stream_exists(port_string, stream_id):
            self.send_command("stream get " + str(port_string) + " " + str(stream_id))
            ret_string = ""
            ret_string += "port=" + str(port_string) + ";"
            ret_string += "ID=" + str(stream_id) + ";"
            ret_string += "name=" + self.trim_command(self.send_command("stream cget -name")) + ";"
            ret_string += "DA=" + self.trim_command(self.send_command("stream cget -da")) + ";"
            ret_string += "SA=" + self.trim_command(self.send_command("stream cget -sa")) + ";"
            value = self.trim_command(self.send_command("stream cget -enable")) == "1"
            ret_string += "is_enabled=" + str(value).lower() + ";"
            ret_string += self.is_stream_continuous(original_port, stream_id, True)
            return ret_string
        else:
            return None

    def set_stream_enabled(self, port_string, stream_id, enable):
        original_port = port_string
        port_string = self.convert_port_to_port_handle(port_string)
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        if self.stream_exists(port_string, stream_id):
            self.send_command("stream get " + str(port_string) + " " + str(stream_id))
            if not enable or str(enable) == "False":
                self.send_command("stream config -enable 0")
            else:
                self.send_command("stream config -enable 1")
            self.send_command("port set " + str(port_string))
            self.send_command("port write " + str(port_string))
            self.send_command("set portList [ list [ list " + port_string + "]]")
            self.send_command("ixWriteConfigToHardware portList -noProtocolServer")

    def get_stream_count(self, port_string):
        port_string = self.convert_port_to_port_handle(port_string)
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)

        return self.trim_command(self.send_command("port getStreamCount " + str(port_string)))

    def set_port_phy_mode(self, port_string, mode):
        # if phy_mode is None, the port speed/duplex advertisement is gone besides gig
        port_string = self.convert_port_to_port_handle(port_string)

        options = dict()
        if mode is not None:
            if mode.lower() == "fiber":
                options[InterfaceConfigConstants.PHY_MODE_CMD] = InterfaceConfigConstants.PHY_MODE_FIBER
            elif mode.lower() == "copper":
                options[InterfaceConfigConstants.PHY_MODE_CMD] = InterfaceConfigConstants.PHY_MODE_COPPER
            elif mode.lower() == "sgmii":
                options[InterfaceConfigConstants.PHY_MODE_CMD] = InterfaceConfigConstants.PHY_MODE_SGMII
        options[InterfaceConfigConstants.PORT_HANDLE_CMD] = port_string

        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        cmd_obj = api.interface_config_phy_mode(options)

    def register_agents(self):
        super(IxiaDevice, self).register_agents()
        self.register_agent(TrafficGenerationConstants.TELNET, IxiaConnectionTelnetAgent(self))

    def get_name_space(self):
        if not hasattr(self, '_nameSpace') or self._nameSpace == "":
            self._nameSpace = "ixia"
        return self._nameSpace

    def _determine_error(self, method_name, cmd_obj, port_string=None):
        kw_results = super(IxiaDevice, self)._determine_error(method_name, cmd_obj, port_string)
        ret_string = str(cmd_obj.return_text)
        if method_name == self.enable_qos_stats.__name__ or method_name == self.set_qos_mode.__name__:
            if "ERROR " in ret_string:
                if "transmitMode" in ret_string:
                    self.logger.log_error("Port " + str(port_string) + " did not set the port capture mode correctly.")
                    kw_results.append(KeywordResult(self.name, False,
                                                    "Port " + str(port_string) +
                                                    " did not set the port capture mode correctly.",
                                                    "", cmd_obj))
            else:
                kw_results.append(KeywordResult(self.name, True,
                                                "Port " + str(port_string) +
                                                " set the port capture mode correctly.",
                                                "", cmd_obj))
        return kw_results

    def register_apis(self):
        super(IxiaDevice, self).register_apis()
        self.logger.log_debug("registering Ixia Agents")
        self.register_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API,
                          IxiaStreamConfigIxTclHalApi(self))
        self.register_api(IxiaDeviceConstants.IXIA_CAPTURE_IX_TCL_HAL_API,
                          IxiaCaptureIxTclHalApi(self))
        self.register_api(IxiaDeviceConstants.IXIA_STATISTIC_IX_TCL_HAL_API,
                          IxiaStatisticsIxTclHal(self))

        self.register_api(IxiaDeviceConstants.IXIA_FILER_PALLETTE_IX_TCL_HAL_API,
                          IxiaFilterPalletteIxTclHalApi(self))
        self.register_api(IxiaDeviceConstants.IXIA_FILER_IX_TCL_HAL_API,
                          IxiaFilterIxTclHalApi(self))
        self.register_api(IxiaDeviceConstants.IXIA_PORT_CONFIG_IX_TCL_HAL_API,
                          IxiaPortConfigIxTclHalApi(self))

        self.register_api(TrafficTagConfigConstants.TRAFFIC_TAG_CONFIG_API, IxiaTrafficTagConfigApi(self))
        self.register_api(TrafficStatsConstants.TRAFFIC_STATS_API, IxiaTrafficStatsApi(self))
        self.register_api(TrafficControlConstants.TRAFFIC_CONTROL_API, IxiaTrafficControlApi(self))
        self.register_api(TrafficConfigConstants.TRAFFIC_CONFIG_API, IxiaTrafficConfigApi(self))
        self.register_api(SessionInfoConstants.SESSION_INFO_API, IxiaSessionInfoApi(self))
        self.register_api(ResetPortConstants.RESET_PORT_API, IxiaResetPortApi(self))
        self.register_api(PacketStatsConstants.PACKET_STATS_API, IxiaPacketStatsApi(self))
        self.register_api(PacketControlConstants.PACKET_CONTROL_API, IxiaPacketControlApi(self))
        self.register_api(PacketInfoConstants.PACKET_INFO_API, IxiaPacketInfoApi(self))
        self.register_api(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API, IxiaPacketConfigTriggersApi(self))
        self.register_api(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API, IxiaPacketConfigFilterApi(self))
        self.register_api(PacketConfigBuffersConstants.PACKET_CONFIG_BUFFERS_API, IxiaPacketConfigBuffersApi(self))
        self.register_api(InterfaceStatsConstants.INTERFACE_STATS_API, IxiaInterfaceStatsApi(self))
        self.register_api(InterfaceConfigConstants.INTERFACE_CONFIG_API, IxiaInterfaceConfigApi(self))
        self.register_api(ConnectConstants.CONNECT_API, IxiaConnectApi(self))
        self.register_api(UdsFilterPalletteConfigConstants.UDS_FILTER_PALLETTE_CONFIG_API,
                          IxiaUdsFilterPalletteConfigApi(self))
        self.register_api(UdsConfigConstants.UDS_CONFIG_API, IxiaUdsConfigApi(self))
        self.register_api(TrafficL47ConfigConstants.TRAFFIC_L47_CONFIG_API, IxiaTrafficL47ConfigApi(self))

        # OSPF
        self.register_api(EmulationOspfTopologyRouteConfigConstants.EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG_API,
                          IxiaEmulationOspfTopologyRouteConfigApi(self))
        self.register_api(EmulationOspfConfigConstants.EMULATION_OSPF_CONFIG_API, IxiaEmulationOspfConfigApi(self))
        self.register_api(EmulationOspfNetworkGroupConfigConstants.EMULATION_OSPF_NETWORK_GROUP_CONFIG_API,
                          IxiaEmulationOspfNetworkGroupConfigApi(self))
        self.register_api(EmulationOspfLsaConfigConstants.EMULATION_OSPF_LSA_CONFIG_API,
                          IxiaEmulationOspfLsaConfigApi(self))
        self.register_api(EmulationOspfInfoConstants.EMULATION_OSPF_INFO_API, IxiaEmulationOspfInfoApi(self))
        self.register_api(EmulationOspfControlConstants.EMULATION_OSPF_CONTROL_API, IxiaEmulationOspfControlApi(self))

        self.register_api(IxRouteIxTclHalConstants.IXROUTE_TCL_HAL_API, IxRouteIxTclHalApi(self))
        self.register_api(NetworkEmulatingTcpConstants.TCP_API, IxiaTcpApi(self))
