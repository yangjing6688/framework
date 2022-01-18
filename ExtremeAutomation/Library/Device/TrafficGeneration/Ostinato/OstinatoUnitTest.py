import time
import unittest
import logging
from ExtremeAutomation.Library.Logger.Logger import Logger

from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Net.Packet.AbstractPacket import AbstractPacket

import ostinato # pip install python-ostinato
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb, DroneProxy
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.mac_pb2 import mac
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.ip4_pb2 import ip4, Ip4
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.tcp_pb2 import tcp, Tcp

from ExtremeAutomation.Library.Device.Common.Agents.IxiaConnectionTelnetAgent import IxiaConnectionTelnetAgent
from ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent import TelnetAgentConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDevice import TrafficGeneratingDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficTagConfigApi import TrafficTagConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.HltApi.HltapiSpirentTrafficTagConfigApi import SpirentTrafficTagConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import IpxPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Utils.Time import current_milli_time

from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4Packet import Ethernet2TcpIpV4Packet

from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDeviceTrafficHelper import OstinatoDeviceTrafficHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDeviceStatisticHelper import OstinatoDeviceStatisticHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDeviceCaptureHelper import OstinatoDeviceCaptureHelper

from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants

from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import InterfaceConfigApi, InterfaceConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import \
    PacketConfigTriggersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDevice import IxiaDevice
from ExtremeAutomation.Library.Net.Packet.Ethernet2Packet import Ethernet2Packet
from ExtremeAutomation.Library.Net.Packet.EthernetPacketHeader import EthernetPacketHeader
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4Packet import Ethernet2IpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4TaggedPacket import Ethernet2IpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapRstpBpduPacket import SapRstpBpduPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import IpxPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import SnapPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IcmpPacketHeader import IcmpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import ArpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.UdpPacketHeader import UdpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketTagConstants
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader, VlanStackPacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Net.Packet.Ieee802LlcPacketHeader import Ieee802LlcPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MstpPacketHeader import MstpPacketHeader, MstpPacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LldpPacketHeader import LldpPacketHeader, LldpPacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import PacketConfigTriggersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import PacketConfigFilterConstants


from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDevice import OstinatoDevice


class TestStringMethods(unittest.TestCase):
    username = "aaron"
    dev = "10.52.153.101"
    # dev = "10.52.10.62"
    tx_port = "lo"
    rx_port = "lo"

    def test_unsupported_methods(self):
        ostinatoDevice = self.connect_and_take_ports()
        port_send = self.tx_port
        port_receive  = self.rx_port
        print("++++++++++++++++++")
        print("start")
        ostinatoDevice.get_port_stream_statistic(port_send, 3, "tx", "blah")
        ostinatoDevice.get_port_capture_uds2_frame_count(port_send)
        print("end")
        print("++++++++++++++++++")

    def test_stream_gets2(self):  # test out the packet capture with all packets.
        ostinatoDevice = self.connect_and_take_ports()
        port_send = self.tx_port
        port_receive  = self.rx_port
        tx_port = self.tx_port
        rx_port = self.rx_port

        packets = PacketClassifier.get_one_of_every_packet("igmp")
        one_of_each = []
        ostinatoDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            ostinatoDevice.clear_all_streams(tx_port)
            PacketClassifier.set_default_test_packet_values(packet)
            print("set ip stream id 1 on port " +tx_port +"\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            # opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST # constant value
            opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
            opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
            opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()
            print("CONFIGURING PACKET\n" + str(packet))
            ostinatoDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)
            ostinatoDevice.configure_stream_using_packet(tx_port, stream_id +1, packet, options=opt_dict)
            ostinatoDevice.configure_stream_using_packet(tx_port, stream_id +2, packet, options=opt_dict)
            ostinatoDevice.configure_stream_using_packet(tx_port, stream_id +3, packet, options=opt_dict)
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST
            ostinatoDevice.configure_stream_using_packet(tx_port, stream_id +4, packet, options=opt_dict)
            print("stream count = " + str(ostinatoDevice.get_stream_count(tx_port)))
            print("get all streams:")
            streams = ostinatoDevice.get_all_stream(tx_port)
            for stream in streams:
                print(stream)
            stream_id += 1
            ostinatoDevice.start_traffic_and_wait(tx_port, 3000)
            print("Is Port Continuously transmitting?" + str(ostinatoDevice.is_port_continuous(tx_port)))
            print("done loop")


    def test_empty_template_step(self):  # test out the packet capture with all packets.
        trafficDevice = self.connect_and_take_ports()
        tx_port = self.tx_port
        rx_port = self.rx_port

        packets = PacketClassifier.get_one_of_every_packet("ARP")
        one_of_each = []
        trafficDevice.tgen_debug = True
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            print(str(packet))
            print("set ip stream id 1 on port 1/1\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
            opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
            print("CONFIGURING PACKET\n" + str(packet))
            trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
            print("start capture on port 1/1/2\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port 1/1/1\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("sleep for 5 seconds\n")
            time.sleep(2)
            print("stop traffic on port 1/1/1\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port 1/1/2\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats 1/1/1 and 1/1/2")
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + str( helper.get_captured_frame_count(rx_port)))
            frames = helper.get_all_captured_frames(rx_port)
            for frame in frames:
                print(str(frame))

    def test_stream_gets(self):  # test out the packet capture with all packets.
        ostinatoDevice = self.connect_and_take_ports()
        port_send = self.tx_port
        port_receive  = self.rx_port
        tx_port = self.tx_port
        rx_port = self.rx_port

        packets = PacketClassifier.get_one_of_every_packet()
        one_of_each = []
        ostinatoDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            ostinatoDevice.clear_all_streams(tx_port)
            PacketClassifier.set_default_test_packet_values(packet)
            print("set ip stream id 1 on port " +tx_port +"\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
            opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
            opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()
            print("CONFIGURING PACKET\n" + str(packet))
            ostinatoDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)

            ostinatoDevice.get_capture_filter_default()
            ostinatoDevice.add_capture_filter_da1("00:33:22:33:44:55", "00:00:00:00:00:00")
            ostinatoDevice.add_capture_filter_sa1("00:33:22:33:44:66", "00:FF:00:00:00:FF")
            ostinatoDevice.add_capture_filter_da2("FF:FF:FF:FF:FF:FF", "00:00:00:00:00:FF")
            ostinatoDevice.add_capture_filter_sa2("00:33:22:33:44:66", "00:00:00:00:00:FF")
            ostinatoDevice.add_capture_filter_pattern1("08 00", "00 00", 12, PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_STARTOFFRAME, PacketConfigFilterConstants.MATCH_TYPE1_USER)

            ostinatoDevice.write_capture_filter(rx_port)

            ostinatoDevice.get_capture_trigger_default()
            ostinatoDevice.add_capture_trigger_capture_trigger(True, PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_ANY,
                                                            PacketConfigTriggersConstants.CAPTURE_FILTER_SA_ANY,
                                                            PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_PATTERN1, None, None, None, None)

            ostinatoDevice.add_capture_trigger_capture_filter(True, PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_ANY,
                                                            PacketConfigTriggersConstants.CAPTURE_FILTER_SA_ANY,
                                                            PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_PATTERN1, None, None, None, None)
            ostinatoDevice.write_capture_trigger(rx_port)

            print(ostinatoDevice.get_capture_filter_and_trigger_settings(rx_port))
            print(ostinatoDevice.get_capture_filter_and_trigger_settings(tx_port))

            ostinatoDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)
            ostinatoDevice.start_capture(rx_port)
            ostinatoDevice.start_traffic(tx_port)
            time.sleep(5)
            print("is transmitting" + str(ostinatoDevice.is_port_transmitting(tx_port)))
            ostinatoDevice.start_traffic(tx_port)
            time.sleep(5)
            print("is transmitting" + str(ostinatoDevice.is_port_transmitting(tx_port)))
            ostinatoDevice.stop_traffic(tx_port)
            print("is transmitting" + str(ostinatoDevice.is_port_transmitting(tx_port)))
            ostinatoDevice.stop_capture(rx_port)
            buffer = ostinatoDevice.get_all_captured_frames(rx_port)
            print("received :")
            if len (buffer) > 0:
                print(buffer[0])
            else:
                print("empty")
            print(ostinatoDevice.get_filtered_captured_frames_report(rx_port))

    def test_multiple_streams_array_capture(self):  # test out the packet capture with all packets.
        ostinatoDevice = self.connect_and_take_ports()
        tx_port = self.tx_port
        rx_port = self.rx_port

        packets = PacketClassifier.get_one_of_every_ethernet2()
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)

        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        ostinatoDevice.configure_streams_using_packets(tx_port, packets)
        print("start capture on port " +rx_port +"\n")
        ostinatoDevice.start_capture(rx_port)
        print("start traffic on port " +tx_port +"\n")
        ostinatoDevice.start_traffic(tx_port)
        print("sleep for 5 seconds\n")
        time.sleep(15)
        print("stop traffic on port " +tx_port +"\n")
        ostinatoDevice.stop_traffic(tx_port)
        print("stop capture on port " +rx_port +"\n")
        ostinatoDevice.stop_capture(rx_port)
        print("get some port capture stats " +tx_port +" and " +rx_port)
        helper = ostinatoDevice.get_capture_helper()
        frames = helper.get_all_captured_frames(rx_port)
        print("" +rx_port +" had " + str(len(frames)) + " packets captured")
        print("" +rx_port +" clear buffers")
        ostinatoDevice.clear_capture_buffer("1/1/2")
        frames = helper.get_all_captured_frames(rx_port)
        print("" +rx_port +" had " + str(len(frames)) + " packets captured")

        print("" +rx_port +" clear statistics and filters and buffers")
        ostinatoDevice.clear_statistics_and_filters(rx_port)
        frames = helper.get_all_captured_frames(rx_port)
        print("" +tx_port +" had " + str(len(frames)) + " packets captured")

    def test_multiple_streams_and_modify_capture(self):  # test out the packet capture with all packets.
        ostinatoDevice = self.connect_and_take_ports()
        tx_port = self.tx_port
        rx_port = self.rx_port

        packets = PacketClassifier.get_one_of_every_ethernet2()
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)

        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        ostinatoDevice.configure_streams_using_packets(tx_port, packets)

        print("Copy packet 5's setting to stream 3")
        ostinatoDevice.modify_stream_using_packet(tx_port, 3, packets[5])
        print("start capture on port " +rx_port +"\n")
        ostinatoDevice.start_capture(rx_port)
        print("start traffic on port " +tx_port +"\n")
        ostinatoDevice.start_traffic(tx_port)
        print("sleep for 5 seconds\n")
        time.sleep(15)
        print("stop traffic on port " +tx_port +"\n")
        ostinatoDevice.stop_traffic(tx_port)
        print("stop capture on port " +rx_port +"\n")
        ostinatoDevice.stop_capture(rx_port)
        print("get some port capture stats " +tx_port +" and " +rx_port)
        helper = ostinatoDevice.get_capture_helper()
        frames = helper.get_all_captured_frames(rx_port)
        print("" +rx_port +" had " + str(len(frames)) + " packets captured")
        print("" +rx_port +" clear buffers")
        ostinatoDevice.clear_capture_buffer("1/1/2")
        frames = helper.get_all_captured_frames(rx_port)
        print("" +rx_port +" had " + str(len(frames)) + " packets captured")

        print("" +rx_port +" clear statistics and filters and buffers")
        ostinatoDevice.clear_statistics_and_filters(rx_port)
        frames = helper.get_all_captured_frames(rx_port)
        print("" +tx_port +" had " + str(len(frames)) + " packets captured")

    def test_stream_continuous(self):  # test out the packet capture with all packets.
        ostinatoDevice = self.connect_and_take_ports()
        port_send = self.tx_port
        port_receive  = self.rx_port
        tx_port = self.tx_port
        rx_port = self.rx_port

        packets = PacketClassifier.get_one_of_every_packet()
        one_of_each = []
        ostinatoDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            ostinatoDevice.clear_all_streams(tx_port)
            PacketClassifier.set_default_test_packet_values(packet)
            print("set ip stream id 1 on port " +tx_port +"\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 100# constant value
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            print("CONFIGURING PACKET\n" + str(packet))
            ostinatoDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)
            ostinatoDevice.start_traffic(tx_port)
            time.sleep(5)
            print("is transmitting" + str(ostinatoDevice.is_port_transmitting(tx_port)))
            ostinatoDevice.start_traffic(tx_port)
            time.sleep(5)
            print("is transmitting" + str(ostinatoDevice.is_port_transmitting(tx_port)))
            ostinatoDevice.stop_traffic(tx_port)
            print("is transmitting" + str(ostinatoDevice.is_port_transmitting(tx_port)))


    def test_stream_testing(self):  # test out the packet capture with all packets.
        ostinatoDevice = self.connect_and_take_ports()
        port_send = self.tx_port
        port_receive  = self.rx_port
        tx_port = self.tx_port
        rx_port = self.rx_port

        packets = PacketClassifier.get_one_of_every_vlan_stacked_packet()
        one_of_each = []
        ostinatoDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            ostinatoDevice.clear_all_streams(tx_port)
            PacketClassifier.set_default_test_packet_values(packet)
            print("set ip stream id 1 on port " +tx_port +"\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 100# constant value
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST # constant value
            print("CONFIGURING PACKET\n" + str(packet))
            ostinatoDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)
            ostinatoDevice.start_capture(rx_port)
            ostinatoDevice.start_traffic(tx_port)
            time.sleep(5)
            print("is transmitting" + str(ostinatoDevice.is_port_transmitting(tx_port)))
            ostinatoDevice.start_traffic(tx_port)
            time.sleep(5)
            print("is transmitting" + str(ostinatoDevice.is_port_transmitting(tx_port)))
            ostinatoDevice.stop_traffic(tx_port)
            print("is transmitting" + str(ostinatoDevice.is_port_transmitting(tx_port)))
            ostinatoDevice.stop_capture(rx_port)
            buffer = ostinatoDevice.get_all_captured_frames(rx_port)
            print("received :")
            if len (buffer) > 0:
                print(buffer[0])
            else:
                print("empty")
            print(ostinatoDevice.get_filtered_captured_frames_report(rx_port))


    def test_stream_lldp_payload(self):  # test out the packet capture with all packets.
        trafficDevice = self.connect_and_take_ports()
        tx_port = self.tx_port
        rx_port = self.rx_port

        trafficDevice.clear_all_streams(tx_port)

        packets = PacketClassifier.get_one_of_every_lldp_packet()
        one_of_each = []
        trafficDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            trafficDevice.clear_all_streams(tx_port)
            print("set ip stream id 1 on port " +tx_port +"\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
            opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
            opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()
            print("CONFIGURING PACKET\n" + str(packet))
            trafficDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)
            print("stream count = " + str(trafficDevice.get_stream_count(tx_port)))
            print("get all streams:")
            streams = trafficDevice.get_all_stream(tx_port)
            for stream in streams:
                print(stream)
            print("start capture on port " +rx_port +"\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +tx_port +"\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("sleep for 5 seconds\n")
            time.sleep(2)
            print("stop traffic on port " +tx_port +"\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +rx_port +"\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +tx_port +" and "+ rx_port)
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + str(helper.get_captured_frame_count(rx_port)))
            frames = helper.get_all_captured_frames(rx_port)
            for frame in frames:
                print(str(frame))
            if frame:
                print("compare = " + str(packet.compare_packet_fields(frame)))


    def test_stream_increamenting_payload(self):  # test out the packet capture with all packets.
        trafficDevice = self.connect_and_take_ports()
        tx_port = self.tx_port
        rx_port = self.rx_port

        trafficDevice.clear_all_streams(tx_port)

        packets = PacketClassifier.get_one_of_every_packet("arp")
        one_of_each = []
        trafficDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            trafficDevice.clear_all_streams(tx_port)
            print("set ip stream id 1 on port " +tx_port +"\n")
            # opt_dict = dict()
            # opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            # opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_PKT # constant value
            # opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 10
            # opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
            # opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
            # opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 1000
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_PKT # constant value
            opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 100
            opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()
            print("CONFIGURING PACKET\n" + str(packet))
            trafficDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)
            trafficDevice.get_traffic_helper().configure_stream_mac_dst_options(tx_port, 1, packet.get_destination_mac(), TrafficConfigConstants.MAC_SRC_MODE_DECREMENT,4, "00:00:00:00:00:FF")
            trafficDevice.get_traffic_helper().configure_stream_mac_src_options(tx_port, 1, packet.get_source_mac(), TrafficConfigConstants.MAC_SRC_MODE_INCREMENT,10, "00:00:00:00:00:FF")

            if isinstance(packet, IpV6PacketHeader):
                assert isinstance(packet, IpV6PacketHeader)
                trafficDevice.get_traffic_helper().configure_stream_ipv6_dst_options(tx_port, 1, packet.get_ipv6_destination_address(), TrafficConfigConstants.IPV6_DST_MODE_INCREMENT,4, "ff00::1")
                trafficDevice.get_traffic_helper().configure_stream_ipv6_src_options(tx_port, 1, packet.get_ipv6_source_address(), TrafficConfigConstants.IPV6_SRC_MODE_INCREMENT,7, "ffE0::1")
            if isinstance(packet, IpV4PacketHeader):
                trafficDevice.get_traffic_helper().configure_stream_ip_dst_options(tx_port, 1, packet.get_destination_ip(), TrafficConfigConstants.IP_DST_MODE_INCREMENT,4, "1.1.1.1")
                trafficDevice.get_traffic_helper().configure_stream_ip_src_options(tx_port, 1, packet.get_source_ip(), TrafficConfigConstants.IP_SRC_MODE_DECREMENT,10, "2.2.2.2")

            if isinstance(packet, ArpPacketHeader):
                trafficDevice.get_traffic_helper().configure_stream_arp_sender_hardware_options(tx_port, 1, packet.get_arp_sender_hardware_address(),
                                                                                     TrafficConfigConstants.ARP_SRC_HW_MODE_DECREMENT,
                                                                                     4)
                trafficDevice.get_traffic_helper().configure_stream_arp_source_protocol_options(tx_port, 1, packet.get_arp_source_protocol_address(),
                                                                                     TrafficConfigConstants.ARP_SRC_HW_MODE_DECREMENT,
                                                                                     6)
                trafficDevice.get_traffic_helper().configure_stream_arp_target_hardware_options(tx_port, 1, packet.get_arp_target_hardware_address(),
                                                                                     TrafficConfigConstants.ARP_DST_HW_MODE_INCREMENT,
                                                                                     14)
                trafficDevice.get_traffic_helper().configure_stream_arp_target_protocol_options(tx_port, 1, packet.get_arp_target_protocol_address(),
                                                                                     TrafficConfigConstants.ARP_DST_HW_MODE_INCREMENT,
                                                                                     18)
            print("stream count = " + str(trafficDevice.get_stream_count(tx_port)))
            print("get all streams:")
            streams = trafficDevice.get_all_stream(tx_port)
            for stream in streams:
                print(stream)
            print("start capture on port " +rx_port +"\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +tx_port +"\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("sleep for 5 seconds\n")
            time.sleep(2)
            print("stop traffic on port " +tx_port +"\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +rx_port +"\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +tx_port +" and "+ rx_port)
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + str(helper.get_captured_frame_count(rx_port)))
            frames = helper.get_all_captured_frames(rx_port)
            for frame in frames:
                print(str(frame))
            if frame:
                print("compare = " + str(packet.compare_packet_fields(frame)))
                if isinstance(frame, VlanStackPacketHeader):
                    vs = VlanStackPacketHeaderDynamicFieldLogic()
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
            print("Printing out all the streams:")
            streams = trafficDevice.get_all_stream(tx_port)
            for stream in streams:
                print(stream)
            if len(streams) != 1:
                print("Error")


    def test_stream_dynamic_fields(self):  # test out the packet capture with all packets.
        trafficDevice = self.connect_and_take_ports()
        tx_port = self.tx_port
        rx_port = self.rx_port

        trafficDevice.clear_all_streams(tx_port)

        packets = PacketClassifier.get_one_of_every_packet()
        one_of_each = []
        trafficDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            trafficDevice.clear_all_streams(tx_port)
            print("set ip stream id 1 on port " +tx_port +"\n")
            # opt_dict = dict()
            # opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            # opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_PKT # constant value
            # opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 10
            # opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
            # opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
            # opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 1000
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_PKT # constant value
            opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 100
            opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()
            print("CONFIGURING PACKET\n" + str(packet))
            trafficDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)
            print("stream count = " + str(trafficDevice.get_stream_count(tx_port)))
            print("get all streams:")
            streams = trafficDevice.get_all_stream(tx_port)
            for stream in streams:
                print(stream)
            print("start capture on port " +rx_port +"\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +tx_port +"\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("sleep for 5 seconds\n")
            time.sleep(2)
            print("stop traffic on port " +tx_port +"\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +rx_port +"\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +tx_port +" and "+ rx_port)
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + str(helper.get_captured_frame_count(rx_port)))
            frames = helper.get_all_captured_frames(rx_port)
            for frame in frames:
                print(str(frame))
            if frame:
                print("compare = " + str(packet.compare_packet_fields(frame)))
                if isinstance(frame, VlanStackPacketHeader):
                    vs = VlanStackPacketHeaderDynamicFieldLogic()
                    print("this should pass.")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    # changes packets vlan info
                    packet.swap_tags(2, 1)
                    vs.set_match_type(vs.MATCH_ALL)
                    print("this should fail cause the order is different")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    vs.set_order_matters(False)
                    vs.set_match_type(vs.MATCH_ALL)
                    print("this should pass cause all match and the order is different, but that is ok.")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    vs.set_order_matters(False)
                    vs.set_match_type(vs.MATCH_ONE)
                    print("this should pass cause at least one matches and the order is different, but that is ok.")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    vs.set_order_matters(False)
                    vs.set_match_type(vs.MATCH_ONLY)
                    print("this should pass cause at only matches and the order is different, but that is ok.")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    vs.set_match_type(vs.MATCH_NONE)
                    print("this should fail cause they match")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                if isinstance(frame, MstpPacketHeader):
                    vs = MstpPacketHeaderDynamicFieldLogic()
                    print("this should pass.")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    # changes packets vlan info
                    vs.set_match_type(vs.MATCH_ALL)
                    print("this should fail cause the order is different")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    vs.set_match_type(vs.MATCH_ONE)
                    vs.set_order_matters(False)
                    print("this should fail cause the order is different")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    vs.set_match_type(vs.MATCH_NONE)
                    vs.set_order_matters(False)
                    print("this should fail")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                if isinstance(frame, LldpPacketHeader):
                    vs = LldpPacketHeaderDynamicFieldLogic()
                    print("this should pass.")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    # changes packets vlan info
                    vs.set_match_type(vs.MATCH_ALL)
                    print("this should fail cause the order is different")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    vs.set_match_type(vs.MATCH_ONE)
                    vs.set_order_matters(False)
                    print("this should fail cause the order is different")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
                    vs.set_match_type(vs.MATCH_NONE)
                    vs.set_order_matters(False)
                    print("this should fail")
                    print("compare = " + str(packet.compare_packet_fields(frame,False, None, None, vs)))
            print("Printing out all the streams:")
            streams = trafficDevice.get_all_stream(tx_port)
            for stream in streams:
                print(stream)
            if len(streams) != 1:
                print("Error")

    def test_stream_increamenting_payload_packetsetting(self):  # test out the packet capture with all packets.
        trafficDevice = self.connect_and_take_ports()
        tx_port = self.tx_port
        rx_port = self.rx_port

        trafficDevice.clear_all_streams(tx_port)

        packets = PacketClassifier.get_one_of_every_packet("ip")
        one_of_each = []
        trafficDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            trafficDevice.clear_all_streams(tx_port)
            print("set ip stream id 1 on port " +tx_port +"\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
            opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
            opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()
            print("CONFIGURING PACKET\n" + str(packet))
            packet.set_destination_mac_mode(TrafficConfigConstants.MAC_DST_MODE_INCREMENT)
            packet.set_destination_mac_count(4)
            packet.set_destination_mac_mask("00:00:00:00:00:FF")
            packet.set_source_mac_mode(TrafficConfigConstants.MAC_SRC_MODE_DECREMENT)
            packet.set_source_mac_count(40)
            packet.set_source_mac_mask("00:00:00:00:00:FF")

            if isinstance(packet, IpV6PacketHeader):
                assert isinstance(packet, IpV6PacketHeader)
                packet.set_ipv6_destination_address_mode(TrafficConfigConstants.IPV6_DST_MODE_INCR_HOST)
                packet.set_ipv6_destination_address_count(10)
                packet.set_ipv6_source_address_mode(TrafficConfigConstants.IPV6_DST_MODE_DECR_HOST)
                packet.set_ipv6_source_address_count(4)
            else:
                assert isinstance(packet, IpV4PacketHeader)
                packet.set_destination_ip_mode(TrafficConfigConstants.IP_DST_MODE_INCREMENT)
                packet.set_destination_ip_count(10)
                packet.set_destination_ip_mask("255.255.0.0")
                packet.set_source_ip_mode(TrafficConfigConstants.IP_SRC_MODE_DECREMENT)
                packet.set_source_ip_count(4)
                packet.set_source_ip_mask("255.255.255.0")

            trafficDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)

            print("stream count = " + str(trafficDevice.get_stream_count(tx_port)))
            print("get all streams:")
            streams = trafficDevice.get_all_stream(tx_port)
            for stream in streams:
                print(stream)
            print("start capture on port " +rx_port +"\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +tx_port +"\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("sleep for 5 seconds\n")
            time.sleep(2)
            print("stop traffic on port " +tx_port +"\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +rx_port +"\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +tx_port +" and "+ rx_port)
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + str(helper.get_captured_frame_count(rx_port)))
            frames = helper.get_all_captured_frames(rx_port)
            for frame in frames:
                print(str(frame))
            if frame:
                print("compare = " + str(packet.compare_packet_fields(frame)))
            print("Printing out all the streams:")
            streams = trafficDevice.get_all_stream(tx_port)
            for stream in streams:
                print(stream)
            if len(streams) != 1:
                print("Error")

    def test_clear_all_streams(self):
        ostinatoDevice = self.connect_and_take_ports()
        port_send = self.tx_port
        port_rec  = self.rx_port

        ostinatoDevice.clear_all_streams(port_send)
        packets = PacketClassifier.get_one_of_every_packet()
        one_of_each = []
        index = 1
        print("This Unit test case will:")
        print("Create " + str(len(packets)) + " streams, transmit, check counts, remove, try transmit, check counts,")
        print("\tattempt with one packet")
        print("++++++++++++++++++++++++++++++")

        print("Create " + str(len(packets)) + " streams on port " + port_send)
        try:
            for packet in packets:
                packet.set_destination_mac("00:33:22:33:44:" +str(index +10))
                packet.set_source_mac("00:33:22:33:44:" +str(index +20))
                packet.auto_set_minimum_length()
                opt_dict = dict()
                opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST
                opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 1000
                opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 1000
                opt_dict[TrafficConfigConstants.FRAME_SIZE_CMD] = 250
                opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD] = 100
                ostinatoDevice.configure_stream_using_packet(port_send, index, packet, options=opt_dict)
                index += 1
        except:
            print("Error on packet" + str(packet))
        created_streams_count = ostinatoDevice.get_stream_count(port_send)
        if created_streams_count == len(packets):
            print("PASSED: Stream count = " + str(created_streams_count))
        else:
            print("Failed expected " + str(created_streams_count) + " received " + str(len(packets)))
        streams = ostinatoDevice.get_all_stream(port_send)
        print(str(streams))
        print(str(streams[0]))
        print("is stream enabled" + str(ostinatoDevice.is_stream_enabled(port_send, 1)))
        ostinatoDevice.set_stream_enabled(port_send, 1, False)
        print("is stream enabled" + str(ostinatoDevice.is_stream_enabled(port_send, 1)))
        ostinatoDevice.set_stream_enabled(port_send, 1, True)
        print("is stream enabled" + str(ostinatoDevice.is_stream_enabled(port_send, 1)))
        print("Stream count " + str(created_streams_count))
        print("clear_statistics_and_filters(" + port_send +")")
        ostinatoDevice.clear_statistics_and_filters(port_send)
        print("Capture Buffer Count " + str(ostinatoDevice.get_port_tx_frame_count(port_send)))
        print("Starting off tx count: " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        ostinatoDevice.start_traffic(port_send)
        ostinatoDevice.start_capture(port_rec)
        time.sleep(1)
        ostinatoDevice.stop_traffic(port_send)
        ostinatoDevice.stop_capture(port_rec)
        print("Capture Buffer Count " + str(ostinatoDevice.get_port_tx_frame_count(port_send))+ " after")
        print("Number of captured packets in the buffer is: " + str(ostinatoDevice.get_port_capture_num_frames(port_rec)))
        ostinatoDevice.clear_all_streams(port_send)
        if (opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD] * len(packets)) == ostinatoDevice.get_port_tx_frame_count(port_rec):
            print("PASSED: stream test streams tx count = " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        else:
            print("FAILED: stream test streams tx count = " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        if ostinatoDevice.get_port_tx_frame_count(port_rec) > 0:
            packets = ostinatoDevice.get_all_captured_frames(port_rec)
            p = None
            for p in packets:
                print(str(p))
        print("clear_statistics_and_filters(" + port_send +")")
        ostinatoDevice.clear_statistics_and_filters(port_send)
        print("Capture Buffer Count " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        print("Stream count " + str(ostinatoDevice.get_stream_count(port_send)))
        if 0 == ostinatoDevice.get_port_tx_frame_count(port_rec):
            print("PASSED: stream test streams tx count = 0")
        else:
            print("FAILED: stream test streams tx count = " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        print("************\nNo streams, no packets")
        print("Starting off tx count: " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        ostinatoDevice.start_traffic(port_send)
        ostinatoDevice.start_capture(port_rec)
        time.sleep(1)
        ostinatoDevice.stop_traffic(port_send)
        ostinatoDevice.stop_capture(port_rec)
        created_streams_count = ostinatoDevice.get_stream_count(port_send)
        if created_streams_count == 0:
            print("PASSED: Stream count = 0")
        else:
            print("FAILED: expected " + created_streams_count + " received " + len(packets))
        print("Stream count " + str(created_streams_count))
        print("After clearing streams: " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        if ostinatoDevice.get_port_tx_frame_count(port_rec) > 0:
            packets = ostinatoDevice.get_all_captured_frames(port_rec)
            p = None
            for p in packets:
                str(p)
        print("***************Now try 1 new packet")
        packet.set_destination_mac("00:33:22:33:44:AA")
        packet.set_source_mac("00:33:22:33:44:AA")
        opt_dict = dict()
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 10
        opt_dict[TrafficConfigConstants.FRAME_SIZE_CMD] = 250
        opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD] = 50
        ostinatoDevice.configure_stream_using_packet(port_send, 1, packet, options=opt_dict)
        print("Stream count " + str(ostinatoDevice.get_stream_count(port_send)))
        print("clear_statistics_and_filters(" + port_send +")")
        ostinatoDevice.clear_statistics_and_filters(port_send)
        print("Capture Buffer Count " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        print("Starting off tx count: " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        ostinatoDevice.start_traffic(port_send)
        ostinatoDevice.start_capture(port_rec)
        time.sleep(1)
        ostinatoDevice.stop_traffic(port_send)
        ostinatoDevice.stop_capture(port_rec)
        ostinatoDevice.clear_all_streams(port_send)
        if opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD] == ostinatoDevice.get_port_tx_frame_count(port_rec):
            print("PASSED: stream test streams tx count = " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        else:
            print("FAILED: stream test streams tx count = " + str(ostinatoDevice.get_port_tx_frame_count(port_rec)))
        if ostinatoDevice.get_port_tx_frame_count(port_rec) > 0:
            packets = ostinatoDevice.get_all_captured_frames(port_rec)
            p = None
            for p in packets:
                str(p)
        ostinatoDevice.disconnect()
        print("End Test Case")
        print("++++++++++++++++++++++++++++++")

    def test_all_packets_set_up_streams(self):
        ostinatoDevice = self.connect_and_take_ports()
        port_send = self.tx_port
        port_rec  = self.rx_port

        ostinatoDevice.clear_statistics_and_filters(port_send)
        ostinatoDevice.clear_statistics_and_filters(port_rec)
        ostinatoDevice.clear_all_streams(port_send)
        ostinatoDevice.clear_all_streams(port_rec)
        print("This Test Case will")
        print("Create send and receive packets of all supported types")
        print("++++++++++++++++++++++++++++++")
        self.check_packets(ostinatoDevice, port_send, port_rec)
        ostinatoDevice.disconnect()

        print("End Test Case")
        print("++++++++++++++++++++++++++++++")
        # buff = drone.getCaptureBuffer(rx_port.port_id[0])
        # packetsCaptured = PacketClassifier.process_pcap_file_contents(buff)
        # print(str(packetsCaptured))

    def check_packets(self, ostinatoDevice, port_send, port_rec):
        packets = PacketClassifier.get_one_of_every_packet()
        # packets = PacketClassifier.get_one_of_every_llc_stp()
        one_of_each = []
        for packet in packets:
            print("\nStart testing packet type " + packet.get_name())
            print("----------------------------")
            PacketClassifier.set_default_test_packet_values(packet)
            # if not isinstance(packet, ArpPacketHeader):
            #     continue
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 100
            opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 100
            opt_dict[TrafficConfigConstants.FRAME_SIZE_CMD] = 250
            opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD] = 500000
            ostinatoDevice.configure_stream_using_packet(port_send, 1, packet, options=opt_dict)
            packet.set_destination_mac("00:ff:ee:dd:44:55")
            packet.set_source_mac("00:ff:ee:dd:44:66")
            print("Stream count " + str(ostinatoDevice.get_stream_count(port_send)))

            ostinatoDevice.clear_statistics_and_filters(port_send)
            ostinatoDevice.clear_statistics_and_filters(port_rec)
            ostinatoDevice.start_traffic(port_send)
            ostinatoDevice.start_capture(port_rec)
            self.check_transmit(ostinatoDevice, 'lo')
            self.check_capture(ostinatoDevice, 'lo')

            # wait for transmit to finish
            time.sleep(5)
            #ostinatoDevice.start_traffic_and_wait('lo',10000)

            ostinatoDevice.stop_traffic(port_send)
            ostinatoDevice.stop_capture(port_rec)

            self.check_transmit(ostinatoDevice, 'lo')
            self.check_capture(ostinatoDevice, 'lo')


            tx_port = ost_pb.PortIdList()
            tx_port.port_id.add().id = 4
            rx_port = ost_pb.PortIdList()
            rx_port.port_id.add().id = 4

            drone = ostinatoDevice.connection
            tx_stats = drone.getStats(tx_port)
            rx_stats = drone.getStats(rx_port)

            print(str(tx_port) + "  " + str(tx_stats))
            print(str(rx_port) + "  " + str(rx_stats))

            print(ostinatoDevice.get_filtered_captured_frames_report(port_rec))

            packets = ostinatoDevice.get_all_captured_frames(port_rec)
            p = None
            for p in packets:
              str(p)
            print("EXPECTED PACKET:\n" +str(packet))
            print("Total Captured count = " + str(ostinatoDevice.get_port_capture_num_frames(port_rec)))
            print("ACTUAL   PACKET:\n" +str(p))
            packet.compare_packet_fields(p)

            print("rx_pkt_bit_count lo " + str( ostinatoDevice.get_port_statistic_rx_pkt_bit_count("lo")))
            print("rx_pkt_bit_rate lo " + str( ostinatoDevice.get_port_statistic_rx_pkt_bit_rate("lo")))
            ostinatoDevice.clear_all_streams(port_send)
            ostinatoDevice.clear_all_streams(port_rec)
            print("End Testing packet type " + packet.get_name())
            print("----------------------------")

    def check_transmit(self, ostinatoDevice, port):
        print(port + " transmitting = " + str(ostinatoDevice.is_port_transmitting(port)))

    def check_capture(self, ostinatoDevice, port):
        print(port + " capturing = " + str(ostinatoDevice.is_port_capturing(port)))

    def connect_and_take_ports(self):
        ostinatoDevice = OstinatoDevice()
        ostinatoDevice.logger.log_level = Logger.DEBUG
        ostinatoDevice.logger.console_level = Logger.ALL
        ostinatoDevice.connect('10.52.153.101')
        port_send = "lo"
        port_rec = "lo"
        drone = ostinatoDevice.connection
        assert isinstance(drone, DroneProxy)

        port_send = self.tx_port
        port_rec  = self.rx_port
        ostinatoDevice.clear_capture_filters_and_triggers(port_send)
        ostinatoDevice.clear_capture_filters_and_triggers(port_rec)
        ostinatoDevice.clear_all_streams(port_send)
        ostinatoDevice.clear_all_streams(port_rec)
        return ostinatoDevice

   # rpc getPortIdList(Void) returns (PortIdList); << check
   #  rpc getPortConfig(PortIdList) returns (PortConfigList); << check
   #  rpc modifyPort(PortConfigList) returns (Ack);
   #
   #  rpc getStreamIdList(PortId) returns (StreamIdList);
   #  rpc getStreamConfig(StreamIdList) returns (StreamConfigList);
   #  rpc addStream(StreamIdList) returns (Ack);
   #  rpc deleteStream(StreamIdList) returns (Ack);
   #  rpc modifyStream(StreamConfigList) returns (Ack);
   #
   #  rpc startTransmit(PortIdList) returns (Ack);
   #  rpc stopTransmit(PortIdList) returns (Ack);
   #
   #  rpc startCapture(PortIdList) returns (Ack);
   #  rpc stopCapture(PortIdList) returns (Ack);
   #  rpc getCaptureBuffer(PortId) returns (CaptureBuffer);
   #
   #  rpc getStats(PortIdList) returns (PortStatsList);
   #  rpc clearStats(PortIdList) returns (Ack);
   #
   #  rpc checkVersion(VersionInfo) returns (VersionCompatibility);





if __name__ == '__main__':
    unittest.main()
