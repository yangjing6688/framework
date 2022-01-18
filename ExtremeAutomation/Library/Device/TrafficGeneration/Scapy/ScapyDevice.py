import re
from collections import OrderedDict
from ExtremeAutomation.Library.Device.Common.Agents.IxiaConnectionTelnetAgent import IxiaConnectionTelnetAgent
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Scapy.ScapyDeviceCaptureHelper import ScapyDeviceCaptureHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Scapy.ScapyDeviceStatisticHelper import \
    ScapyDeviceStatisticHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Scapy.ScapyDeviceTrafficHelper import \
    ScapyDeviceTrafficHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDevice import TrafficGeneratingDevice
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Utils.Time import current_milli_time
# from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
# from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
# from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants

# from scapy.all import *

r"""
Scapy install

apt-get install scapy
pip install scapy

# starting scapy
sudo scapy &

WINDOWS:
https://stackoverflow.com/questions/22996098/trouble-installing-pcapy-on-windows-7-cannot-open-include-file-pcap-h
download this: http://www.winpcap.org/devel.htm the devpack
set WPDPACK_BASE=C:\Software\WpdPack
set that to where you unzipped the devpack.
pip install pcapy << this should work.

scapy.runtime: WARNING: WinPcap is now deprecated (not maintened). Please use Npcap instead

"""


class ScapyDevice(TrafficGeneratingDevice, ScapyDeviceCaptureHelper, ScapyDeviceStatisticHelper,
                  ScapyDeviceTrafficHelper):
    tgen_debug = True

    def __init__(self):
        super(ScapyDevice, self).__init__()
        ScapyDeviceCaptureHelper.__init__(self, self)
        ScapyDeviceStatisticHelper.__init__(self, self)
        ScapyDeviceTrafficHelper.__init__(self, self)
        self.drone = None
        # self.capture_buffer = ScapyCaptureBuffer(self)
        self.capture_buffer = ScapyCaptureBuffer(self)
        self.os = NetworkElementConstants.OS_JETS
        self.dev.os = NetworkElementConstants.OS_JETS
        self.prompt_regex = '[%\\$]$'
        self._ports_group = {}
        self._ports_group_index = []
        self._streams = {}
        self._stream_objects = {}
        self.pdl_stream_headers_and_values = OrderedDict()  # this gets cleared out after a stream is configured.
        self.pdl_level = 0
        self.initialized_network_device = False
        self._nameSpace = "jets"
        self.oper_sys = NetworkElementConstants.OS_JETS
        self.port = 22
        self.main_prompt = "#"
        self.initialized = True

    def connect(self, host, port=-1):
        pass

    def is_connected(self):
        return True

    def init_connection(self):
        if self.initialized:
            return
        self.initialized = True

    def disconnect(self):
        pass

    def take_port_ownership(self, host, user, port_string, reset=False, options=None):
        pass

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

    def get_traffic_helper(self):
        return self

    def get_statistic_helper(self):
        return self

    def get_capture_helper(self):
        return self

    def get_port_duplex(self, port_string):
        return self.logger.log_unimplemented_method()

    def set_port_duplex(self, port_string, duplex, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def get_port_speed(self, port_string):
        return self.logger.log_unimplemented_method()

    def set_port_speed(self, port_string, speed, disable_autonegotiation=False, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def set_port_autonegotiation(self, port_string, _bool, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def has_link(self, port_string):
        return self.logger.log_unimplemented_method()

    def reset_port(self, host, port_string):
        return self.logger.log_unimplemented_method()

# port_stats {
#   port_id {
#     id: 1
#   }
#   state {
#     link_state: LinkStateUp
#     is_transmit_on: false
#     is_capture_on: true
#   }
#   rx_pkts: 241
#   rx_bytes: 31571
#   rx_pps: 0
#   rx_bps: 0
#   tx_pkts: 0
#   tx_bytes: 0
#   tx_pps: 0
#   tx_bps: 0
#   rx_drops: 0
#   rx_errors: 0
#   rx_fifo_errors: 0
#   rx_frame_errors: 0
# }

    def is_port_transmitting(self, port_string):
        return self.logger.log_unimplemented_method()

    def is_port_capturing(self, port_string):
        return self.logger.log_unimplemented_method()

    def start_traffic(self, port_string, options=None):
        self.logger.log_debug("start_traffic(" + port_string + ")")
        if options is None:
            options = {}
        streams = self._streams[port_string]
        for stream_id, stream in streams.items():
            so = self._stream_objects[stream]
            if so.enabled:
                self.send_command(stream + " run")
                self._stream_objects[stream].state = "Run"

    def stop_traffic(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def start_capture(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def stop_capture(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def clear_capture_buffer(self, port_string, options=None):
        self.cached_capture_buffer = None
        self.cached_capture_buffer_time_stampe = None
        return self.logger.log_unimplemented_method()

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
        return self.logger.log_unimplemented_method()

    def configure_stream_using_packet(self, port_string, stream_id, packet, clear_all_streams=False, options=None):
        if options is None:
            options = {}

        opt_dict = options
        self.clear_stream(port_string, stream_id)
        stream_name = self.add_jets_stream(port_string, stream_id)
        self.pdl_clear_packet_header_cashe()
        packet.config_thirdparty_traffic_generator_stream(EthernetPacketConstants.TRAFFIC_GENERATION_SCAPY, self,
                                                          port_string, stream_name, options)
        pkt_string = self.pdl_build_packet_string_and_clear()
        if packet.is_field_set(packet.get_payload()):
            self.pdl_add_packet_header(ScapyDeviceConstants.RAW_DATA, {"data": packet.get_payload().replace(" ", "")})
        length = packet.get_length()
        if TrafficConfigConstants.FRAME_SIZE_CMD in opt_dict:
            length = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.FRAME_SIZE_CMD])
            self.logger.log_debug("setting " + TrafficConfigConstants.FRAME_SIZE_CMD + " to " + str(
                opt_dict[TrafficConfigConstants.FRAME_SIZE_CMD]))
        if length < 64:
            length = 64
            self.logger.log_debug(
                "updating " + TrafficConfigConstants.FRAME_SIZE_CMD + " to " + str(length) + " min packet size")
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
                self.logger.log_debug(
                    "setting number of packets to " + str(opt_dict[TrafficConfigConstants.RATE_PPS_CMD]))
        elif TrafficConfigConstants.PKTS_PER_BURST_CMD in opt_dict:
            rate_burst = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.RATE_PPS_CMD])
            self.logger.log_debug("setting " + TrafficConfigConstants.PKTS_PER_BURST_CMD + " to " + str(
                opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))
            num_packets = NumberUtils.to_integer_value(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD])
            self.logger.log_debug(
                "setting number of packets to " + str(opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD]))

        self._stream_objects[stream_name] = ScapyStreamObject(stream_name, port_string, stream_id, length,
                                                              packet_mode, num_packets, rate_pps, rate_burst)
        self._stream_objects[stream_name].generate_pdl(pkt_string)
        # self.send_command(self._stream_objects[stream_name].str)

    def add_jets_stream(self, port_string, stream_id):
        port_string = str(port_string)
        stream_id = str(stream_id)
        if port_string not in self._streams:
            self._streams[port_string] = {}
        port_streams = self._streams[port_string]
        port_streams[stream_id] = self.generate_stream_name(port_string, stream_id)
        return port_streams[stream_id]

    def generate_stream_name(self, port_string, stream_id):
        port_string = str(port_string)
        stream_id = str(stream_id)
        return "stream_" + port_string + "_" + stream_id

    def pdl_add_packet_header(self, header, pkt_string):
        if self.pdl_level > 0:
            header += "_ecap" + str(self.pdl_level)
        if header not in self.pdl_stream_headers_and_values:
            self.pdl_stream_headers_and_values[header] = {}
        elif header == "rawdata":
            self.pdl_stream_headers_and_values["rawdata"]["data"] = \
                self.pdl_stream_headers_and_values["rawdata"]["data"] + " " + pkt_string["data"]
        self.pdl_stream_headers_and_values[header].update(pkt_string)

    def pdl_build_packet_string(self, cache_ordered_dict):
        tmp = []
        # if not self.pdl_contains_header("rawdata"):
        #     self.pdl_add_packet_header("rawdata", {"data" : "0x00"})
        # if self.pdl_contains_header("rawdata"):
        #     raw_data = self.pdl_stream_headers_and_values["rawdata"]["data"].replace(" ", "")
        #     while len(raw_data) < 20:
        #         raw_data = raw_data + "00"
        #     self.pdl_stream_headers_and_values["rawdata"]["data"] = raw_data
        for key, value in cache_ordered_dict.items():
            string = key + "(" + ','.join('{}="{}"'.format(k, v) for k, v in value.items()) + ")"
            string = re.sub('"0x([A-F0-9a-f]+)"', '0x\\1', string)
            tmp.append(string)
        return '/'.join(tmp)

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
        if port_string in self._streams:
            self._streams[port_string] = []

    def clear_all_streams(self, port_string, options=None):
        self._streams = {}

    def stream_exists(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_stream(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def get_all_stream(self, port_string):
        return self.logger.log_unimplemented_method()

    def get_stream_count(self, port_string, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def clear_statistics_and_filters(self, port_string, options=None):
        if options is None:
            options = {}
        self.clear_statistics(port_string, options)
        self.capture_buffer.clear_capture_buffer(port_string)
        # Scapy doesn't have filters or triggers
        # self.clear_capture_filters_and_triggers(port_string)

    def clear_capture_filters_and_triggers(self, port_string):
        self.cached_capture_buffer = None
        self.cached_capture_buffer_time_stampe = None
        return self.logger.log_unimplemented_method()
        # return self.logger.log_unimplemented_method()

    def register_agents(self):
        super(ScapyDevice, self).register_agents()
        self.register_agent(TrafficGenerationConstants.TELNET, IxiaConnectionTelnetAgent(self))

    def register_apis(self):
        super(ScapyDevice, self).register_apis()
        # print "registering Scapy Agents"
        self.logger.log_debug("registering Scapy Agents")
        # self.register_api(TrafficTagConfigConstants.TRAFFIC_TAG_CONFIG_API, SpirentTrafficTagConfigApi(self))


class ScapyDeviceConstants(object, metaclass=Singleton):
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

    ENET_HDR = "ENET_HDR"
    LLC_HDR = "LLC"
    IEEE_8021Q_HDR = "IEEE_8021Q_HDR"
    QNQ_HDR = "QNQ_HDR"
    VXLAN_HDR = "VXLAN_HDR"
    SNAP_HDR = "SNAP_HDR"
    ARP_HDR = "ARP_HDR"
    IP_HDR = "IP_HDR"
    IPX_HDR = "IPX_HDR"
    IPv6_HDR = "IPv6_HDR"

    ICMP_HDR = "ICMP_HDR"
    UDP_HDR = "UDP_HDR"
    TCP_HDR = "TCP_HDR"
    IGMP_HDR = "IGMP_HDR"
    IGMP_V1V2_HDR = "IGMP_V1V2_HDR"
    IGMP_GROUP_ONLY = "IGMP_GROUP_ONLY"
    MEMBERSHIP_QUERY_MSG = "MEMBERSHIP_QUERY_MSG"

    RAW_DATA = "rawdata"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


class ScapyStreamObject(object):
    def __init__(self, stream_name, port_string, stream_id, length, packet_mode, num_packets, rate_pps, rate_burst):
        self.enabled = True
        self.port = port_string
        self.stream_id = stream_id
        self.name = stream_name
        self.length = length
        self.packet_mode = packet_mode
        self.num_packets = num_packets
        self.rate_pps = rate_pps
        self.rate_burst = rate_burst
        self.state = None
        self.str = None

    def generate_pdl(self, pkt_string):
        # get_windows_if_list()
        # ifaces.load_from_powershell()
        # ifaces.dev_from_name('Intel(R) Ethernet Connection I217-LM')
        self.str = eval("send(" + pkt_string + ", iface=\"" + self.port + "\", count=1000)")


class ScapyCaptureBuffer(object):
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
