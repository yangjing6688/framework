import time
import unittest

from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Net.Packet.AbstractPacket import AbstractPacket

import ostinato # pip install python-ostinato
from ostinato.core import ost_pb, DroneProxy
from ostinato.protocols.mac_pb2 import mac
from ostinato.protocols.ip4_pb2 import ip4, Ip4
from ostinato.protocols.tcp_pb2 import tcp, Tcp

from ExtremeAutomation.Library.Device.NetworkElement.Constants.DutConstants import DutConstants
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
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
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
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Net.Packet.Ieee802LlcPacketHeader import Ieee802LlcPacketHeader


from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDevice import OstinatoDevice

from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import \
    PacketConfigFilterApi, PacketConfigFilterConstants


class TestStringMethods(unittest.TestCase):
    username = "aaron"
    dev1 = "10.52.10.70"
    dev2 = "10.52.10.71"
    tx_port = "eth1"
    rx_port = "eth1"

    def test_two_ostinato_with_filter_out_stp(self):
        tx_port = self.tx_port
        ostinatoDeviceTx = self.connect_and_take_ports(self.dev1, tx_port)

        rx_port = self.rx_port
        ostinatoDeviceRx = self.connect_and_take_ports(self.dev2, rx_port)

        print("This Test Case will")
        print("send 18 packets from 2 streams should filter out all STP and get 9 packets.")
        print("++++++++++++++++++++++++++++++")
        packet = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet)
        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
        opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
        opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
        opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()

        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)

        packet2 = SapRstpBpduPacket()
        PacketClassifier.set_default_test_packet_values(packet2)
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 2, packet2, options=opt_dict)

        ostinatoDeviceRx.get_capture_filter_default()
        ostinatoDeviceRx.add_capture_filter_da1("00:33:22:33:44:55", "00:00:00:00:00:00")
        ostinatoDeviceRx.add_capture_filter_sa1("00:33:22:33:44:66", "00:00:00:00:00:FF")
        ostinatoDeviceRx.write_capture_filter(rx_port)

        ostinatoDeviceRx.get_capture_trigger_default()
        ostinatoDeviceRx.add_capture_trigger_capture_trigger(True,PacketConfigTriggersConstants.CAPTURE_FILTER_DA_DA1,
                                                             PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                                             None, None, None, None, None)

        ostinatoDeviceRx.add_capture_trigger_capture_filter(True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_DA1,
                                                        PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                                        None, None, None, None, None)
        ostinatoDeviceRx.write_capture_trigger(rx_port)

        ostinatoDeviceRx.start_capture(rx_port)
        inex = 1
        for inex in range(1, 10):
            ostinatoDeviceTx.start_traffic(tx_port)
            time.sleep(1)
        time.sleep(5)
        ostinatoDeviceTx.stop_traffic(tx_port)
        ostinatoDeviceRx.stop_capture(rx_port)

        frames = ostinatoDeviceRx.get_all_captured_frames(rx_port)
        for frame in frames:
            str(frame)
        ostinatoDeviceTx.get_port_tx_frame_count(tx_port)
        if ostinatoDeviceRx.get_captured_frame_count(rx_port) == 9:
            print("PASSED: sent " +str(ostinatoDeviceTx.get_port_tx_frame_count(tx_port)) +" filtered " +str(ostinatoDeviceRx.get_captured_frame_count(tx_port)) +" packets. STP all filtered out.")
        else:
            print("FAILED: received " +str(ostinatoDeviceRx.get_captured_frame_count(tx_port)) +" packets. STP not all filtered out.")
        ostinatoDeviceTx.disconnect()
        ostinatoDeviceRx.disconnect()
        print("End Test Case")
        print("++++++++++++++++++++++++++++++")

    def test_two_ostinato_with_filter_out_stp_3_streams(self):
        tx_port = self.tx_port
        ostinatoDeviceTx = self.connect_and_take_ports(self.dev1, tx_port)

        rx_port = self.rx_port
        ostinatoDeviceRx = self.connect_and_take_ports(self.dev2, rx_port)

        print("This Test Case will")
        print("send 18 packets from 2 streams should filter out all STP and get 9 packets.")
        print("++++++++++++++++++++++++++++++")
        packet = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet)
        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
        opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
        opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
        opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()

        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)

        packet2 = SapRstpBpduPacket()
        PacketClassifier.set_default_test_packet_values(packet2)
        packet2.set_source_mac("00:00:CA:FE:FE:ED")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 2, packet2, options=opt_dict)

        packet3 = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet3)
        packet3.set_destination_mac("FF:FF:FF:FF:FF:FF")
        packet3.set_source_mac("00:33:22:33:44:66")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 3, packet3, options=opt_dict)

        ostinatoDeviceRx.get_capture_filter_default()
        ostinatoDeviceRx.add_capture_filter_da1("00:33:22:33:44:55", "00:00:00:00:00:00")
        ostinatoDeviceRx.add_capture_filter_sa1("00:33:22:33:44:66", "00:00:00:00:00:FF")
        ostinatoDeviceRx.add_capture_filter_da2("FF:FF:FF:FF:FF:FF", "00:00:00:00:00:FF")
        ostinatoDeviceRx.add_capture_filter_sa2("00:33:22:33:44:66", "00:00:00:00:00:FF")

        ostinatoDeviceRx.write_capture_filter(rx_port)

        ostinatoDeviceRx.get_capture_trigger_default()
        ostinatoDeviceRx.add_capture_trigger_capture_trigger(True,PacketConfigTriggersConstants.CAPTURE_FILTER_DA_DA2,
                                                             PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA2,
                                                             None, None, None, None, None)

        ostinatoDeviceRx.add_capture_trigger_capture_filter(True, PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_ANY,
                                                        PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                                        None, None, None, None, None)
        ostinatoDeviceRx.write_capture_trigger(rx_port)

        ostinatoDeviceRx.start_capture(rx_port)
        inex = 1
        for inex in range(1, 10):
            ostinatoDeviceTx.start_traffic(tx_port)
            time.sleep(1)
        time.sleep(5)
        ostinatoDeviceTx.stop_traffic(tx_port)
        ostinatoDeviceRx.stop_capture(rx_port)

        frames = ostinatoDeviceRx.get_all_captured_frames(rx_port)
        for frame in frames:
            str(frame)
        ostinatoDeviceTx.get_port_tx_frame_count(tx_port)
        print("This should miss the first packet 1, start capturing at packet 3 and filter all packet 2 out.")
        if ostinatoDeviceRx.get_captured_frame_count(rx_port) == (9 +8):
            print("PASSED: sent " +str(ostinatoDeviceTx.get_port_tx_frame_count(tx_port)) +" filtered " +str(ostinatoDeviceRx.get_captured_frame_count(tx_port)) +" packets. STP all filtered out.")
        else:
            print("FAILED: received " +str(ostinatoDeviceRx.get_captured_frame_count(tx_port)) +" packets. STP not all filtered out.")
        ostinatoDeviceTx.disconnect()
        ostinatoDeviceRx.disconnect()
        print("End Test Case")
        print("++++++++++++++++++++++++++++++")


    def test_two_ostinato_with_filter_out_stp_4_streams(self):
        tx_port = self.tx_port
        ostinatoDeviceTx = self.connect_and_take_ports(self.dev1, tx_port)

        rx_port = self.rx_port
        ostinatoDeviceRx = self.connect_and_take_ports(self.dev2, rx_port)

        print("This Test Case will")
        print("send 5*9 packets from 2 streams should filter out all STP and get 9 packets.")
        print("The the 4th should be filtered out, but the second should not cause of the mask")
        print("++++++++++++++++++++++++++++++")
        packet = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet)
        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
        opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
        opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
        opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()

        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)

        packet2 = SapRstpBpduPacket()
        PacketClassifier.set_default_test_packet_values(packet2)
        packet2.set_source_mac("00:00:CA:FE:FE:ED")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 2, packet2, options=opt_dict)

        packet3 = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet3)
        packet3.set_destination_mac("FF:FF:FF:FF:FF:FF")
        packet3.set_source_mac("00:44:22:33:44:66")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 3, packet3, options=opt_dict)

        packet4 = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet4)
        packet4.set_destination_mac("FF:FF:FF:FF:FF:FF")
        packet4.set_source_mac("00:33:22:33:55:66")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 4, packet4, options=opt_dict)

        packet4 = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet4)
        packet4.set_destination_mac("FF:FF:FF:FF:FF:FF")
        packet4.set_source_mac("00:33:22:33:44:66")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 5, packet4, options=opt_dict)

        ostinatoDeviceRx.get_capture_filter_default()
        ostinatoDeviceRx.add_capture_filter_da1("00:33:22:33:44:55", "00:00:00:00:00:00")
        ostinatoDeviceRx.add_capture_filter_sa1("00:33:22:33:44:66", "00:FF:00:00:00:FF")
        ostinatoDeviceRx.add_capture_filter_da2("FF:FF:FF:FF:FF:FF", "00:00:00:00:00:FF")
        ostinatoDeviceRx.add_capture_filter_sa2("00:33:22:33:44:66", "00:00:00:00:00:FF")

        ostinatoDeviceRx.write_capture_filter(rx_port)

        ostinatoDeviceRx.get_capture_trigger_default()
        ostinatoDeviceRx.add_capture_trigger_capture_trigger(True,PacketConfigTriggersConstants.CAPTURE_FILTER_DA_DA2,
                                                             PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA2,
                                                             None, None, None, None, None)

        ostinatoDeviceRx.add_capture_trigger_capture_filter(True, PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_ANY,
                                                        PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                                        None, None, None, None, None)
        ostinatoDeviceRx.write_capture_trigger(rx_port)

        ostinatoDeviceRx.start_capture(rx_port)
        inex = 1
        for inex in range(1, 10):
            ostinatoDeviceTx.start_traffic(tx_port)
            time.sleep(1)
        time.sleep(5)
        ostinatoDeviceTx.stop_traffic(tx_port)
        ostinatoDeviceRx.stop_capture(rx_port)

        frames = ostinatoDeviceRx.get_all_captured_frames(rx_port)
        for frame in frames:
            str(frame)
        ostinatoDeviceTx.get_port_tx_frame_count(tx_port)
        print("This should miss the first packet 1, start capturing at packet 3 and filter all packet 2 out.")
        if ostinatoDeviceRx.get_captured_frame_count(rx_port) == (9 +9 +9):
            print("PASSED: sent " +str(ostinatoDeviceTx.get_port_tx_frame_count(tx_port)) +" filtered " +str(ostinatoDeviceRx.get_captured_frame_count(tx_port)) +" packets. STP all filtered out.")
        else:
            print("FAILED: received " +str(ostinatoDeviceRx.get_captured_frame_count(tx_port)) +" packets. STP not all filtered out.")
        ostinatoDeviceTx.disconnect()
        ostinatoDeviceRx.disconnect()
        print("End Test Case")
        print("++++++++++++++++++++++++++++++")


    def test_two_ostinato_with_filter_out_stp_4_with_pattern_streams(self):
        tx_port = self.tx_port
        ostinatoDeviceTx = self.connect_and_take_ports(self.dev1, tx_port)

        rx_port = self.rx_port
        ostinatoDeviceRx = self.connect_and_take_ports(self.dev2, rx_port)

        print("This Test Case will")
        print("send 5*9 packets from 2 streams should filter out all STP and get 9 packets.")
        print("The the 4th should be filtered out, but the second should not cause of the mask")
        print("++++++++++++++++++++++++++++++")
        packet = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet)
        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
        opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
        opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
        opt_dict[TrafficConfigConstants.NAME_CMD] = packet.get_name()

        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)

        packet2 = SapRstpBpduPacket()
        PacketClassifier.set_default_test_packet_values(packet2)
        packet2.set_source_mac("00:00:CA:FE:FE:ED")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 2, packet2, options=opt_dict)

        packet3 = Ethernet2Packet()
        PacketClassifier.set_default_test_packet_values(packet3)
        packet3.set_destination_mac("FF:FF:FF:FF:FF:FF")
        packet3.set_source_mac("00:44:22:33:44:66")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 3, packet3, options=opt_dict)

        packet4 = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet4)
        packet4.set_destination_mac("FF:FF:FF:FF:FF:FF")
        packet4.set_source_mac("00:33:22:33:55:66")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 4, packet4, options=opt_dict)

        packet5 = Ethernet2Packet()
        PacketClassifier.set_default_test_packet_values(packet5)
        packet5.set_destination_mac("FF:FF:FF:FF:FF:FF")
        packet5.set_source_mac("00:33:22:33:44:66")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 5, packet5, options=opt_dict)

        packet6 = Ethernet2IpV4Packet()
        PacketClassifier.set_default_test_packet_values(packet6)
        packet6.set_destination_mac("FF:FF:FF:FF:FF:FF")
        packet6.set_source_mac("00:33:22:33:44:66")
        ostinatoDeviceTx.configure_stream_using_packet(tx_port, 6, packet6, options=opt_dict)

        ostinatoDeviceRx.get_capture_filter_default()
        ostinatoDeviceRx.add_capture_filter_da1("00:33:22:33:44:55", "00:00:00:00:00:00")
        ostinatoDeviceRx.add_capture_filter_sa1("00:33:22:33:44:66", "00:FF:00:00:00:FF")
        ostinatoDeviceRx.add_capture_filter_da2("FF:FF:FF:FF:FF:FF", "00:00:00:00:00:FF")
        ostinatoDeviceRx.add_capture_filter_sa2("00:33:22:33:44:66", "00:00:00:00:00:FF")
        ostinatoDeviceRx.add_capture_filter_pattern1("08 00", "00 00", 12, PacketConfigFilterConstants.PATTERN_OFFSET_TYPE1_STARTOFFRAME, PacketConfigFilterConstants.MATCH_TYPE1_USER)

        ostinatoDeviceRx.write_capture_filter(rx_port)

        ostinatoDeviceRx.get_capture_trigger_default()
        ostinatoDeviceRx.add_capture_trigger_capture_trigger(True,PacketConfigTriggersConstants.CAPTURE_FILTER_DA_DA2,
                                                             PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA2,
                                                             PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_ANY, None, None, None, None)

        ostinatoDeviceRx.add_capture_trigger_capture_filter(True, PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_ANY,
                                                        PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                                        PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_PATTERN1, None, None, None, None)
        ostinatoDeviceRx.write_capture_trigger(rx_port)

        ostinatoDeviceRx.start_capture(rx_port)
        inex = 1
        for inex in range(1, 10):
            ostinatoDeviceTx.start_traffic(tx_port)
            time.sleep(1)
        time.sleep(5)
        ostinatoDeviceTx.stop_traffic(tx_port)
        ostinatoDeviceRx.stop_capture(rx_port)

        frames = ostinatoDeviceRx.get_all_captured_frames(rx_port)
        for frame in frames:
            str(frame)
        ostinatoDeviceTx.get_port_tx_frame_count(tx_port)
        print("This should miss the first packet 1, start capturing at packet 3 and filter all packet 2 out.")
        if ostinatoDeviceRx.get_captured_frame_count(rx_port) == (9 +9 +9 +8):
            print("PASSED: sent " +str(ostinatoDeviceTx.get_port_tx_frame_count(tx_port)) +" filtered " +str(ostinatoDeviceRx.get_captured_frame_count(tx_port)) +" packets. STP all filtered out.")
        else:
            print("FAILED: received " +str(ostinatoDeviceRx.get_captured_frame_count(tx_port)) +" packets. STP not all filtered out.")
        ostinatoDeviceTx.disconnect()
        ostinatoDeviceRx.disconnect()
        print("End Test Case")
        print("++++++++++++++++++++++++++++++")

    def connect_and_take_ports(self, ip, port):
        ostinatoDevice = OstinatoDevice()
        ostinatoDevice.connect(ip)
        port_send = port
        drone = ostinatoDevice.connection
        ostinatoDevice.clear_capture_filters_and_triggers(port_send)
        ostinatoDevice.clear_all_streams(port_send)
        ostinatoDevice.clear_statistics(port_send)
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
