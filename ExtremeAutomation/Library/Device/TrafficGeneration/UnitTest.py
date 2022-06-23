import time
import unittest

from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import InterfaceConfigApi, InterfaceConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import \
    PacketConfigTriggersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import PacketConfigFilterConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDevice import IxiaDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxLoadDevice import IxLoadDevice
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4 import Ethernet2ErspanIIIGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Ethernet2Packet import Ethernet2Packet
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4Packet import Ethernet2IpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4TaggedPacket import Ethernet2IpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4Packet import Ethernet2TcpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import IpxPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier, PacketClassifierConstants
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IcmpPacketHeader import IcmpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.UdpPacketHeader import UdpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import ArpPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacketHeader import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketTagConstants, PacketConstants
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RadiusPacketHeader import RadiusPacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficGeneratorConnectionManager import TrafficGeneratorConnectionManager
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPortKeywords import TrafficPortKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketCreationKeywords import TrafficPacketCreationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.Constants.PacketTypeConstants import PacketTypeConstants
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStreamConfigurationKeywords import TrafficStreamConfigurationKeywords
from ExtremeAutomation.Library.Logger.Logger import Logger

from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceUnitTestObject import IxiaDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaLoadDeviceUnitTestObject import IxiaLoadDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaArpHelper import IxiaArpHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.SpirentDeviceUnitTestObject import SpirentDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDeviceUnitTestObject import OstinatoDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceUnitTestObject import JetsDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Scapy.ScapyDeviceUnitTestObject import ScapyDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.HltapiTrafficGeneratingDevice import HltapiTrafficGeneratingDevice

from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4Packet import Ethernet2IpV4Packet
from ExtremeAutomation.Library.Net.Packet.Ethernet2ArpPacket import Ethernet2ArpPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4Packet import Ethernet2UdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2TcpIpV6Packet import Ethernet2TcpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2GreIpV4Packet import Ethernet2GreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2ErspanGreIpV4Packet import Ethernet2ErspanGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2ErspanIIIGreIpV4Packet import Ethernet2ErspanIIIGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2VxlanUdpIpV4Packet import Ethernet2VxlanUdpIpV4Packet


from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2IpEncapsulatedIpV4Packet import Ethernet2IpEncapsulatedIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2IpEncapsulatedIpV6Packet import Ethernet2IpEncapsulatedIpV6Packet


from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingSpbmApi import NetworkEmulatingSpbmApi, NetworkEmulatingSpbmConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingBgpApi import NetworkEmulatingBgpApi, NetworkEmulatingBgpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingLldpApi import NetworkEmulatingLldpApi, NetworkEmulatingLldpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingEndstationApi import NetworkEmulatingEndstationApi, NetworkEmulatingEndstationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingOspfApi import NetworkEmulatingOspfApi, NetworkEmulatingOspfConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingVrrpApi import NetworkEmulatingVrrpApi, NetworkEmulatingVrrpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingRouteApi import NetworkEmulatingRouteApi, NetworkEmulatingRouteConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingDvrApi import NetworkEmulatingDvrApi, NetworkEmulatingDvrConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingTcpApi import NetworkEmulatingTcpApi, NetworkEmulatingTcpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingIgmpApi import NetworkEmulatingIgmpApi, NetworkEmulatingIgmpConstants

from netmiko import ConnectHandler  # pip install netmiko

from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import \
    NetworkElementConstants
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxLoadDevice import IxLoadDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxLoadDevice import IxLoadDevice


device_object = IxiaDeviceUnitTestObject()
# device_object = IxiaLoadDeviceUnitTestObject()
#device_object = SpirentDeviceUnitTestObject()
#device_object = OstinatoDeviceUnitTestObject()
# device_object = OstinatoDeviceUnitTestObject()
# device_object = OstinatoDeviceUnitTestObject(True)
# device_object = JetsDeviceUnitTestObject()


class TestStringMethods(unittest.TestCase):

    def test_uds_EUAS_348_for_jeffb(self):
        trafficDevice = device_object.connect_and_take_ports()
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        trafficDevice.clear_port_ownership("10.52.2.189", tx_port)
        trafficDevice.clear_port_ownership("10.52.2.189",rx_port)
        trafficDevice.send_command("set hltapiconnectapi_connect [ixia::connect -device 10.52.2.189 -port_list 1/1 1/2  -reset  ]")
        trafficDevice.send_command("")
        trafficDevice.send_command("")
        trafficDevice.send_command("")
        trafficDevice.send_command("")
        trafficDevice.send_command("")
        trafficDevice.send_command("")
        trafficDevice.send_command("")
        trafficDevice.send_command("")

    def test_uds_era38_for_jeffb(self):
        trafficDevice = device_object.connect_and_take_ports()
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packet = PacketClassifier.get_one_of_every_packet("ETHERNET2IPV4PACKET")[0]

        trafficDevice.clear_all_streams(tx_port)
        PacketClassifier.set_default_test_packet_values(packet)
        packet.set_ip_flags(0x07)
        print("=======" * 20)
        print("SENDING PACKET")
        print(str(packet))
        print("-*-" * 20)
        print("JETS output:")
        trafficDevice.clear_statistics(tx_port)
        trafficDevice.clear_statistics(rx_port)
        trafficDevice.start_capture(rx_port)
        opt_dict = {}
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 1
        opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST

        trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)

        print("Set up filter/triggers")
        trafficDevice.get_capture_filter_default()
        trafficDevice.add_capture_filter_da1(packet.get_destination_mac(), "00:00:00:00:00:00")
        trafficDevice.write_capture_filter(rx_port)
        trafficDevice.get_capture_trigger_default()
        trafficDevice.add_capture_trigger_capture_user_defined_statistics1(True,
                                                PacketConfigTriggersConstants.UDS1_DA_NOTDA1,
                                                  PacketConfigTriggersConstants.UDS1_SA_ANY,
                                                  None, None, None, None, None)
        trafficDevice.write_capture_trigger(rx_port)

        packet.set_destination_mac("00:44:55:33:22:11")
        trafficDevice.configure_stream_using_packet(tx_port, 2, packet, options=opt_dict)

        trafficDevice.start_traffic(tx_port)
        trafficDevice.wait_for_capture_count_on_port(rx_port, 10)
        trafficDevice.get_port_tx_frame_count(tx_port)
        trafficDevice.get_port_statistic_capture_filter_count(tx_port)
        trafficDevice.get_port_statistic_capture_filter_count(rx_port)
        trafficDevice.stop_traffic(tx_port)
        trafficDevice.stop_capture(rx_port)
        frames = trafficDevice.get_all_captured_frames(rx_port)
        print("Number of packets received: " + str(len(frames)))
        found = 0
        print(trafficDevice.get_filtered_captured_frames_report(rx_port))
        for frame in frames:
            print(str(frame))
        stat = trafficDevice.get_port_statistic_rx_uds1_count(tx_port)
        print("The UDS1 value for port " + str(tx_port) + " is " + str(stat))
        stat = trafficDevice.get_port_statistic_rx_uds1_count(rx_port)
        print("The UDS1 value for port " + str(rx_port) + " is " + str(stat))
        stat = trafficDevice.get_port_statistic_rx_uds2_count(tx_port)
        print("The UDS2 value for port " + str(tx_port) + " is " + str(stat))
        stat = trafficDevice.get_port_statistic_rx_uds2_count(rx_port)
        print("The UDS2 value for port " + str(rx_port) + " is " + str(stat))

    def test_new_features_for_sandeep(self):
        trafficDevice = device_object.connect_and_take_ports()
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packet = PacketClassifier.get_one_of_every_packet("ETHERNET2IPV4PACKET")[0]

        trafficDevice.clear_all_streams(tx_port)
        PacketClassifier.set_default_test_packet_values(packet)
        packet.set_ip_flags(0x07)
        print("=======" * 20)
        print("SENDING PACKET")
        print(str(packet))
        print("-*-" * 20)
        print("JETS output:")
        trafficDevice.clear_statistics(tx_port)
        trafficDevice.clear_statistics(rx_port)
        # trafficDevice.get_jets_stats(tx_port)
        # trafficDevice.get_jets_stats_array(tx_port)
        trafficDevice.start_capture(rx_port)
        trafficDevice.start_capture(rx_port)
        opt_dict = {}
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 1
        opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST

        trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)

        print("Set up filter/triggers")
        trafficDevice.get_capture_filter_default()
        trafficDevice.add_capture_filter_da1(packet.get_destination_mac(), "00:00:00:00:00:00")
        trafficDevice.write_capture_filter(rx_port)
        trafficDevice.get_capture_trigger_default()
        trafficDevice.add_capture_trigger_capture_filter(True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_ANY,
                                                  None, None, None, None, None)
        trafficDevice.add_capture_trigger_capture_trigger(True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                                   PacketConfigTriggersConstants.CAPTURE_FILTER_SA_ANY,
                                                   None, None, None, None, None)
        trafficDevice.write_capture_trigger(rx_port)

        packet.set_destination_mac("00:44:55:33:22:11")
        trafficDevice.configure_stream_using_packet(tx_port, 2, packet, options=opt_dict)

        trafficDevice.start_traffic(tx_port)
        trafficDevice.wait_for_capture_count_on_port(rx_port, 10)
        trafficDevice.get_port_tx_frame_count(tx_port)
        trafficDevice.get_port_statistic_capture_filter_count(tx_port)
        trafficDevice.get_port_statistic_capture_filter_count(rx_port)
        trafficDevice.stop_traffic(tx_port)
        trafficDevice.stop_capture(rx_port)
        frames = trafficDevice.get_all_captured_frames(rx_port)
        print("Number of packets received: " + str(len(frames)))
        found = 0
        print(trafficDevice.get_filtered_captured_frames_report(rx_port))
        for frame in frames:
            print(str(frame))

    def test_captured_filtered_by_packet(self):
        trafficDevice = device_object.connect_and_take_ports()
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packet = PacketClassifier.get_one_of_every_packet("ETHERNET2ICMPV6IPV6TAGGEDPACKET")[0]
        PacketClassifier.set_default_test_packet_values(packet)

        trafficDevice.clear_all_streams(tx_port)
        packet.set_destination_mac("00:44:55:66:77:88")
        packet.set_source_mac("00:33:55:66:77:88")
        # packet.set_destination_ip("1.2.3.1")
        # packet.set_source_ip("1.2.3.4")
        trafficDevice.clear_statistics(tx_port)
        trafficDevice.clear_statistics(rx_port)
        # trafficDevice.get_jets_stats(tx_port)
        # trafficDevice.get_jets_stats_array(tx_port)
        trafficDevice.start_capture(rx_port)
        trafficDevice.start_capture(rx_port)
        opt_dict = {}
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 1
        opt_dict[TrafficConfigConstants.PKTS_PER_BURST_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST

        trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
        packet.set_destination_mac("00:44:55:66:77:88")
        packet.set_source_mac("00:33:55:66:77:99")
        packet.set_destination_ip("1.2.3.1")
        packet.set_source_ip("1.2.3.5")
        packet.set_source_port(75)
        trafficDevice.configure_stream_using_packet(tx_port, 2, packet, options=opt_dict)
        packet.set_destination_mac("00:44:55:66:77:88")
        packet.set_source_mac("00:33:55:66:77:AA")
        packet.set_destination_ip("1.2.3.1")
        packet.set_source_ip("1.2.3.6")
        packet.set_source_port(74)
        trafficDevice.configure_stream_using_packet(tx_port, 3, packet, options=opt_dict)
        packet = PacketClassifier.get_one_of_every_packet("ETHERNET2TCPIPV6PACKET")[0]
        PacketClassifier.set_default_test_packet_values(packet)
        packet.set_destination_mac("00:44:55:66:77:88")
        packet.set_source_mac("00:33:55:66:77:88")
        packet.set_ipv6_destination_address("FFFF::0001")
        packet.set_ipv6_source_address("2800::0001")
        packet.set_source_port(75)
        trafficDevice.configure_stream_using_packet(tx_port, 4, packet, options=opt_dict)
        packet = PacketClassifier.get_one_of_every_packet("ETHERNETSNAPIPV4PACKET")[0]
        PacketClassifier.set_default_test_packet_values(packet)
        packet.set_destination_mac("00:44:55:66:77:88")
        packet.set_source_mac("00:33:55:66:77:88")
        packet.set_destination_ip("1.2.3.1")
        packet.set_source_ip("1.2.3.6")
        trafficDevice.configure_stream_using_packet(tx_port, 5, packet, options=opt_dict)
        packet = PacketClassifier.get_one_of_every_packet("ETHERNET2TCPIPV6TAGGEDPACKET")[0]
        PacketClassifier.set_default_test_packet_values(packet)
        packet.set_destination_mac("00:44:55:66:77:88")
        packet.set_source_mac("00:33:55:66:77:88")
        packet.set_ipv6_destination_address("FFFF::0001")
        packet.set_ipv6_source_address("2800::0001")
        packet.set_source_port(75)
        trafficDevice.configure_stream_using_packet(tx_port, 6, packet, options=opt_dict)

        trafficDevice.start_traffic(tx_port)
        time.sleep(10)
        trafficDevice.get_port_tx_frame_count(tx_port)
        trafficDevice.get_port_statistic_capture_filter_count(tx_port)
        trafficDevice.get_port_statistic_capture_filter_count(rx_port)
        trafficDevice.stop_traffic(tx_port)
        trafficDevice.stop_capture(rx_port)

        packet = PacketClassifier.get_one_of_every_packet("ETHERNET2TCPIPV4PACKET")[0]
        # packet.set_source_ip("1.2.3.5")
        packet.set_source_port(75)
        frames = trafficDevice.get_all_captured_frames_filtered_by_packet(rx_port, packet)
        for frame in frames:
            print(str(frame))
        packet = PacketClassifier.get_one_of_every_packet("ETHERNET2IPV4PACKET")[0]
        packet.set_destination_ip("1.2.3.1")
        frames = trafficDevice.get_all_captured_frames_filtered_by_packet(rx_port, packet)
        for frame in frames:
            print(str(frame))

    def test_bytes_packet_send(self):
        trafficDevice = device_object.connect_and_take_ports()
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packet_byte = "0044444444440011111111118100A47F86DD6000000000102C0A21510000000000000000000000000001215100000000000000000000000000333A1E0327111122220100BBE70000000023EFD481"
        packet = PacketClassifier.classify_packet_bytes(packet_byte)

        packet_byte = "00444444444400aabbccddff8100000a86dd6000000005a22cff2151000000000000000000000000000121510000000000000000000000000044061e032711112222003700420000000000000000000000000000000001010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101"
        packet = PacketClassifier.classify_packet_bytes(packet_byte)

        packet_byte = "00444444444400aabbccddff8100000a86dd6000000005a22cff2151000000000000000000000000000121510000000000000000000000000044111e032711112222003700420000000001010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101"
        packet = PacketClassifier.classify_packet_bytes(packet_byte)

        trafficDevice.clear_all_streams(tx_port)
        print("=======" * 20)
        print("SENDING PACKET")
        print(str(packet))
        print("-*-" * 20)
        print("JETS output:")
        opt_dict = dict()
        trafficDevice.clear_statistics(tx_port)
        trafficDevice.clear_statistics(rx_port)
        trafficDevice.start_capture(rx_port)
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST
        trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
        time.sleep(3)
        packet.configure_packet()
        trafficDevice.stop_traffic(tx_port)
        trafficDevice.stop_capture(rx_port)
        frames = trafficDevice.get_all_captured_frames(rx_port)
        print("Number of packets received: " + str(len(frames)))
        print(trafficDevice.get_filtered_captured_frames_report(rx_port))
        for frame in frames:
            print("RECEIVED PACKET:")
            print(str(frame))

    def test_jets_ping(self):
        trafficDevice = device_object.connect_and_take_ports()
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port


        tcp_api = trafficDevice.get_api(NetworkEmulatingTcpConstants.TCP_API)
        assert isinstance(tcp_api, NetworkEmulatingTcpApi)

        print("Create 1 TCP Stacks on each port:")
        trafficDevice.start_capture(rx_port)

        # trafficDevice.send_command("protocolServer setDefault")
        # trafficDevice.send_command("protocolServer config -enableArpResponse true")
        # trafficDevice.send_command("protocolServer set 1 1 1")
        # trafficDevice.send_command("protocolServer set 1 1 2")

        # trafficDevice.wait_for_ping(tx_port, "10.120.10.11", "10.120.10.10")

        trafficDevice.ping(rx_port, "10.120.10.10", "10.120.10.11", timeout_secs=60)
        trafficDevice.ping(tx_port, "10.120.10.11", "10.120.10.10", timeout_secs=60)
        trafficDevice.stop_capture(rx_port)
        frames = trafficDevice.get_all_captured_frames(rx_port)
        print("Number of packets received: " + str(len(frames)))
        found = 0
        print(trafficDevice.get_filtered_captured_frames_report(rx_port))

    def test_python_traffic_keywords(self):  # test out the packet capture filters, triggers, etc... Get/Add/Write
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port


    def test_xrf_play(self):
        guid = "90ce9c21-229c-4f30-b211-4b08a8be3acb"
        # try:
        #     trafficDevice = device_object.connect_and_take_ports()
        #     trafficDevice.set_guid(guid)
        # except:
        #     print("Could not connect")
        # try:
        #     trafficDevice.run_config_file("c:/Temp/WH-Emp-Wireless-Throughput.rxf")
        # except:
        #     pass
        # try:
        #     trafficDevice.copy_results_file("c:/temp/output.html")
        # except:
        #     pass
        # trafficDevice.clean_up()
        trafficDevice = IxLoadDevice()
        trafficDevice.set_guid(guid)
        trafficDevice.set_results_file_name("c:/temp/output.html")
        trafficDevice.check_all_parsed_results_column_containing_value_greater_than("failed", 0)

    def test_tcl_play(self):
        trafficDevice = device_object.connect_and_take_ports()
        trafficDevice.play_tcl_file("testscript.tcl")

    def test_cap(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        trafficDevice.start_capture(rx_port)
        time.sleep(3)
        trafficDevice.stop_capture(rx_port)

    def test_jets(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        print("get MTU " + str(trafficDevice.get_port_mtu(tx_port)))
        trafficDevice.set_port_mtu(tx_port, 9000)
        print("get MTU " + str(trafficDevice.get_port_mtu(tx_port)))
        packets = PacketClassifier.get_one_of_every_packet()
        mac1 = "00:44:33:22:35:66"
        mac2 = "00:44:33:22:45:77"
        mac3 = "00:44:33:22:45:88"
        opt_dict = dict()
        for packet in packets:
            if "SNAP" not in packet.get_name().upper() or "TAG" not in packet.get_name().upper() or "GRE" in packet.get_name().upper() or "ENCAP" in packet.get_name().upper():
                continue
            trafficDevice.clear_all_streams(tx_port)
            PacketClassifier.set_default_test_packet_values(packet)
            print("=======" * 20)
            print("SENDING PACKET")
            print(str(packet))
            print("-*-" * 20)
            print("JETS output:")
            trafficDevice.clear_statistics(tx_port)
            trafficDevice.clear_statistics(rx_port)
            # trafficDevice.get_jets_stats(tx_port)
            # trafficDevice.get_jets_stats_array(tx_port)
            trafficDevice.start_capture(rx_port)
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST
            packet.set_destination_mac(mac1)
            trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST
            packet.set_destination_mac(mac2)
            trafficDevice.configure_stream_using_packet(tx_port, 2, packet, options=opt_dict)
            trafficDevice.get_port_statistic_rx_raw_pkt_count(tx_port)
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 20
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST
            trafficDevice.set_stream_enabled(tx_port, 2, False)
            packet.set_destination_mac(mac3)
            trafficDevice.configure_stream_using_packet(tx_port, 3, packet, options=opt_dict)
            trafficDevice.configure_stream_using_packet(tx_port, 3, packet, options=opt_dict)
            trafficDevice.configure_stream_using_packet(tx_port, 3, packet, options=opt_dict)
            trafficDevice.clear_statistics(rx_port)
            trafficDevice.start_traffic(tx_port)
            trafficDevice.get_port_tx_frame_count(tx_port)
            trafficDevice.start_traffic(tx_port)
            trafficDevice.get_port_tx_frame_count(tx_port)
            trafficDevice.start_traffic(tx_port)
            trafficDevice.get_port_tx_frame_count(tx_port)
            time.sleep(3)
            trafficDevice.get_port_tx_frame_count(tx_port)
            trafficDevice.get_port_statistic_capture_filter_count(tx_port)
            trafficDevice.get_port_statistic_capture_filter_count(rx_port)
            trafficDevice.stop_traffic(tx_port)
            trafficDevice.stop_capture(rx_port)
            print(str(rx_port) + " RX Frame Count = " + str(trafficDevice.get_port_rx_frame_count(rx_port)))
            print(str(tx_port) + " TX Frame Count = " + str(trafficDevice.get_port_tx_frame_count(tx_port)))
            print(str(tx_port) + " RX Frame Count = " + str(trafficDevice.get_port_rx_frame_count(tx_port)))
            print(str(rx_port) + " TX Frame Count = " + str(trafficDevice.get_port_tx_frame_count(rx_port)))
            try:
                trafficDevice.clear_stream(tx_port, 3)
            except:
                pass
            frames = trafficDevice.get_all_captured_frames(rx_port)
            print("Number of packets received: " + str(len(frames)))
            found = 0
            print(trafficDevice.get_filtered_captured_frames_report(rx_port))
            print("there should be 10  stream 1")
            print("there should be  0  stream 2")
            print("there should be 60+ stream 3")
            printed = []
            for frame in frames:
                if frame.get_destination_mac() == mac1 \
                        or frame.get_destination_mac() == mac2 \
                        or frame.get_destination_mac() == mac3:
                    if frame.get_destination_mac() not in printed:
                        printed.append(frame.get_destination_mac())
                        print("RECEIVED PACKET:")
                        print(str(frame))
                        print("-*-" * 20)
                    found += 1

            trafficDevice.clear_statistics(tx_port)
            trafficDevice.clear_statistics(rx_port)
            print(str(rx_port) + " RX Frame Count = " + str(trafficDevice.get_port_rx_frame_count(rx_port)))
            print(str(tx_port) + " TX Frame Count = " + str(trafficDevice.get_port_tx_frame_count(tx_port)))
            print(str(tx_port) + " RX Frame Count = " + str(trafficDevice.get_port_rx_frame_count(tx_port)))
            print(str(rx_port) + " TX Frame Count = " + str(trafficDevice.get_port_tx_frame_count(rx_port)))
            # if found != 2:
            #     print("error " + found)


        # trafficDevice.send_command("i1 sendPdlPkt -pdlStr \"ENET_HDR src=00:01:02:03:04:05 dst=ff:ff:ff:ff:ff:ff, IP_HDR ip_src_address=1.1.1.1 ip_dest_address=255.255.255.255, UDP_HDR udp_src_port=2000 udp_dest_port=2000\" -totalLen 100 -count 10")
        # trafficDevice.send_command("generator addPdlStream gen1 1 -pdlStr \"ENET_HDR src=00:00:00:0a:02:02 dst=01:00:5e:01:01:05,  IP_HDR ip_src_address=1.1.1.21 ip_dest_address=224.1.1.5, UDP_HDR udp_src_port=2010 udp_dest_port=2000\" -totalLen 100 -mode ManualBurst -rate 1 -burstSize 1 -numOfBursts 1 -ibgInMsecs 0")
        # trafficDevice.send_command("generator addPdlStream gen2 1 -pdlStr \"ENET_HDR src=00:00:00:0a:02:01 dst=01:00:5e:01:01:05,  IP_HDR ip_src_address=1.1.1.20 ip_dest_address=224.1.1.5, UDP_HDR udp_src_port=2010 udp_dest_port=2000\" -totalLen 100 -mode ManualBurst -rate 1 -burstSize 1 -numOfBursts 1 -ibgInMsecs 0")
        #
        # # tcpip addUdpDataConn -device 2 -port 2000 -remotePort 2010 -remoteIp 1.1.1.20 -localIp 224.1.1.5 -group test -trackSeqNum true
        # # tcpip clearUdpDataPktCount -device 2 -group test
        # #
        # # gen1 dist 1 ManualBurst -rate 4 -burstSize 4 -numOfBurst 1 -envRate 0
        # trafficDevice.send_command("gen1 run")
        # trafficDevice.send_command("gen2 run")
        # trafficDevice.send_command("gen1 stop")
        # trafficDevice.send_command("gen2 stop")
        # trafficDevice.stop_capture(rx_port)
        # frames = trafficDevice.get_all_captured_frames(rx_port)
        # for frame in frames:
        #     print(str(frame))

        # trafficDevice.clear_all_streams(tx_port)
        # trafficDevice.clear_all_streams(rx_port)
        # packets = PacketClassifier.get_one_of_every_packet("ICMP")
        # PacketClassifier.save_to_pcap_file_contents(packets, "c:\\TRM_DATA\\file.pcap")
        # for packet in packets:
        #     trafficDevice.clear_all_streams(tx_port)

        trafficDevice.disconnect()
        print("done")

    def test_spirent_support(self):
        # this contains all the things needed to test whether or not a new TGD is supported ot not.
        trafficDevice = device_object.connect_and_take_ports()
        # trafficDevice.tgen_debug = True
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        trafficDevice.get_port_statistic_rx_raw_pkt_count(rx_port)
        trafficDevice.get_port_capture_num_frames(rx_port)

        print("TESTING check is methods")
        print("trafficDevice.is_connected() = " + str(trafficDevice.is_connected()))
        print("trafficDevice.is_initialized() = " + str(trafficDevice.is_initialized()))
        print("is_port_capturing " + tx_port + " = " + str(trafficDevice.is_port_capturing(tx_port)))
        print("is_port_transmitting " + tx_port + " = " + str(trafficDevice.is_port_transmitting(tx_port)))
        print("is_port_continuous " + tx_port + " = " + str(trafficDevice.is_port_continuous(tx_port)))
        print("is_stream_enabled " + tx_port + " = " + str(trafficDevice.is_stream_enabled(tx_port, 1)))
        #print("is_stream_continuous " + tx_port + " = " + str(trafficDevice.is_stream_continuous(tx_port, 1)))


        print("TESTING: traffic generation method")
        print("TESTING PORT DUPLEX")
        print("duplex " + tx_port + " = " + str(trafficDevice.get_port_duplex(tx_port)))
        trafficDevice.set_port_duplex(tx_port, "half")
        time.sleep(5)
        print("duplex " + tx_port + " = " + str(trafficDevice.get_port_duplex(tx_port)))
        trafficDevice.set_port_duplex(tx_port, "full")
        time.sleep(5)
        print("duplex " + tx_port + " = " + str(trafficDevice.get_port_duplex(tx_port)))

        print("TESTING PORT SPEED")
        print("speed " + tx_port + " = " + str(trafficDevice.get_port_speed(tx_port)))
        print("setting port speed on " +tx_port +" to 10")
        trafficDevice.set_port_speed(tx_port, InterfaceConfigConstants.SPEED_ETHER10, True)
        print("speed " + tx_port + " = " + str(trafficDevice.get_port_speed(tx_port)))
        print("setting port speed on " +tx_port +" to 1000")
        trafficDevice.set_port_speed(tx_port, InterfaceConfigConstants.SPEED_ETHER1000, True)
        print("speed " + tx_port + " = " + str(trafficDevice.get_port_speed(tx_port)))

        print("TESTING PORT AUTONEGOTIATION")
        # print("autonegotiation " + tx_port + " = " + trafficDevice.get_port_autonagotiation(tx_port))
        trafficDevice.set_port_autonegotiation(tx_port, False)
        #print("autonegotiation " + tx_port + " = " + trafficDevice.get_port_autonagotiation(tx_port))
        trafficDevice.set_port_autonegotiation(tx_port, True)
        #print("autonegotiation " + tx_port + " = " + trafficDevice.get_port_autonagotiation(tx_port))

        print("port link check " + str(trafficDevice.has_link(tx_port)))
        print("link " + tx_port + " = " + str(trafficDevice.has_link(tx_port)))

        trafficDevice.get_port_statistic(tx_port, 'rx', "qos0_count")


        print("TESTING: traffic generation method (Statistics Helper)")
        helper = trafficDevice.get_statistic_helper()
        print("rx frame count " + tx_port + " = "+ str(helper.get_port_rx_frame_count(tx_port)))
        print("tx frame count " + tx_port + " = "+ str(helper.get_port_tx_frame_count(tx_port)))
        print("rx collisions count " + tx_port + " = "+ str(helper.get_port_rx_collisions_count(tx_port)))
        print("late collisions count " + tx_port + " = "+ str(helper.get_port_late_collisions_count(tx_port)))
        print("total collision count " + tx_port + " = "+ str(helper.get_port_total_collisions_count(tx_port)))
        print("fcs error count " + tx_port + " = "+ str(helper.get_port_fcs_errors_count(tx_port)))

        print("capture filter count " + rx_port +" = " + str(helper.get_port_statistic_capture_filter_count(rx_port)))
        print("capture filter rate " + rx_port +" = " + str(helper.get_port_statistic_capture_filter_rate(rx_port)))
        print("capture trigger count" + rx_port +" = " + str(helper.get_port_statistic_capture_trigger_count(rx_port)))
        print("capture trigger rate " + rx_port +" = " + str(helper.get_port_statistic_capture_trigger_rate(rx_port)))

        print("clear_all_streams " + str(tx_port))
        trafficDevice.clear_all_streams(tx_port)
        print("clear_capture_buffer " + str(tx_port))
        trafficDevice.clear_capture_buffer(tx_port)
        print("clear_capture_filters_and_triggers " + str(tx_port))
        trafficDevice.clear_capture_filters_and_triggers(tx_port)
        print("clear_statistics " + str(tx_port))
        trafficDevice.clear_statistics(tx_port)
        print("clear_statistics_and_filters " + str(tx_port))
        trafficDevice.clear_statistics_and_filters(tx_port)
        print("clear_stream " + str(tx_port))
        trafficDevice.clear_stream(tx_port, 1)

        if isinstance(trafficDevice, HltapiTrafficGeneratingDevice):
            print("set port ARP SEND off")
            trafficDevice.set_arp_transmit(tx_port, False)
            trafficDevice.set_arp_transmit(rx_port, False)

        packets = PacketClassifier.get_one_of_every_packet("ipv4")
        one_of_each = []

        packet = packets[0]
        print("TESTING: traffic generation method packets and streams")
        PacketClassifier.set_default_test_packet_values(packet)
        print("set ip stream id 1 on port " +device_object.tx_port + "\n")
        packet.set_length(124)
        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
        opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
        opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
        print("CONFIGURING PACKET\n" + str(packet))
        trafficDevice.configure_stream_using_packet(device_object.tx_port, 1, packet, options=opt_dict)
        trafficDevice.configure_stream_using_packet(device_object.tx_port, 2, packet, options=opt_dict)
        trafficDevice.configure_stream_using_packet(device_object.tx_port, 3, packet, options=opt_dict)
        print("Stream count on " + device_object.tx_port +  " = " + str(trafficDevice.get_stream_count(device_object.tx_port)))
        trafficDevice.get_all_stream(device_object.tx_port)
        print("Remove streams 2 and 3")
        trafficDevice.clear_stream(device_object.tx_port, 3)
        trafficDevice.clear_stream(device_object.tx_port, 2)

        print("Does stream 2 exist? " + str(trafficDevice.stream_exists(device_object.tx_port, 2)))
        print("Does stream 3 exist? " + str(trafficDevice.stream_exists(device_object.tx_port, 3)))

        print("Stream count on " + device_object.tx_port +  " = " + str(trafficDevice.get_stream_count(device_object.tx_port)))
        trafficDevice.clear_all_streams(tx_port)
        trafficDevice.configure_stream_using_packet(device_object.tx_port, 2, packet, options=opt_dict)
        print("Stream count on " + device_object.tx_port +  " = " + str(trafficDevice.get_stream_count(device_object.tx_port)))

        # trafficDevice.reset_port()

        print("is " + device_object.rx_port + " capturing? " + str(trafficDevice.is_port_capturing(device_object.rx_port)))
        print("start capture on port " +device_object.rx_port + "\n")
        trafficDevice.start_capture(rx_port)
        print("is " + device_object.rx_port + " capturing? " + str(trafficDevice.is_port_capturing(device_object.rx_port)))
        print("is " + device_object.tx_port + " transmitting? " + str(trafficDevice.is_port_transmitting(device_object.tx_port)))
        print("start traffic on port " +device_object.tx_port + "\n")
        trafficDevice.start_traffic_and_wait(tx_port, 2000)
        print("is " + device_object.rx_port + " transmitting? " + str(trafficDevice.is_port_transmitting(device_object.tx_port)))
        print("stop capture on port " +device_object.rx_port + "\n")
        trafficDevice.stop_capture(rx_port)
        print("stop traffic on port " +device_object.tx_port + "\n")
        trafficDevice.stop_traffic(tx_port)
        print("is " + device_object.rx_port + " transmitting? " + str(trafficDevice.is_port_transmitting(device_object.tx_port)))

        print("get all captured packets on port " +device_object.rx_port + "\n")
        packets = trafficDevice.get_all_captured_frames(rx_port)
        for packet in packets:
            print(str(packet))
        packet = trafficDevice.get_captured_frame(rx_port, 5)
        count = trafficDevice.get_captured_frame_count(rx_port)
        packet = trafficDevice.get_port_capture_frame_frame_data_in_bytes(rx_port,5)
        packet = trafficDevice.get_port_capture_frame_frame_data_string(rx_port,5)

        trafficDevice.disconnect()
        print("done")

    def test_main_capture_filter_get_add_write(self):  # test out the packet capture filters, triggers, etc... Get/Add/Write
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        rx_port = device_object.rx_port

        helper = trafficDevice.get_capture_helper()
        helper.clear_capture_filters_and_triggers(rx_port)
        trafficDevice.wait_for_has_link(rx_port)

        print("port " + str(rx_port) + " link? " + str(trafficDevice.has_link(rx_port)))
        print("port " +str(rx_port)+ "3" +" link? " + str(trafficDevice.has_link(str(rx_port) + "3")))
        helper.get_capture_filter_default()
        helper.add_capture_filter_da1("00:ee:00:ff:00:00", "00:00:00:00:00:00")
        helper.add_capture_filter_da2("00:ee:00:ff:aa:00", "00:00:00:00:00:ff")
        helper.add_capture_filter_sa1("00:dd:00:ff:00:00", "00:00:00:00:00:00")
        helper.add_capture_filter_sa2("00:dd:00:ff:aa:00", "00:00:00:00:00:ff")
        helper.write_capture_filter(rx_port)

        helper.get_capture_trigger_default()
        helper.add_capture_trigger_capture_filter(True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                                  None, None, None, None, None)
        helper.add_capture_trigger_capture_trigger(True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                                   PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                                   None, None, None, None, None)
        helper.add_capture_trigger_capture_user_defined_statistics1(True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                                                    PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                                                    None, None, None, None, None)
        helper.write_capture_trigger(rx_port)
        print(trafficDevice.get_capture_filter_and_trigger_settings(rx_port))

    def test_main_capture_trigger_atg8971(self):  # test out the packet capture filters, triggers, etc... Get/Add/Write
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        helper = trafficDevice.get_capture_helper()
        helper.clear_capture_filters_and_triggers(rx_port)
        trafficDevice.wait_for_has_link(rx_port)

        packets = PacketClassifier.get_one_of_every_packet("arp")
        one_of_each = []

        packet = packets[0]
        print("TESTING: traffic generation method packets and streams")
        PacketClassifier.set_default_test_packet_values(packet)
        packet.set_destination_mac("AA:AA:AA:AA:AA:AA")
        packet.set_source_mac("02:04:96:98:71:D8")
        assert isinstance(packet, Ethernet2ArpPacket)
        packet.set_arp_operation(0x02)
        packet.set_arp_sender_hardware_address("02:04:96:98:71:D8")
        packet.set_arp_source_protocol_address("10.10.10.66")
        packet.set_arp_target_protocol_address("10.10.10.111")
        packet.set_arp_target_hardware_address("AA:AA:AA:AA:AA:AA")
        packet.set_arp_proto(2048)
        packet.set_arp_seq(4)
        packet.set_arp_hardware(0x01)

        helper.get_capture_filter_default()
        helper.get_capture_trigger_default()
        trafficDevice.add_capture_filter_pattern1("2", None, "21", None,PacketConfigFilterConstants.MATCH_TYPE1_USER)
        trafficDevice.add_capture_trigger_capture_filter(True, PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_ANY,
                                                            PacketConfigTriggersConstants.CAPTURE_FILTER_SA_ANY,
                                                            PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_PATTERN1, None, None, None, None)
        helper.write_capture_filter(rx_port)
        helper.write_capture_trigger(rx_port)
        print(str(packet))
        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST # constant value
        # packet = PacketClassifier.classify_packet_bytes("00005e00011054ee758acc0c0800450002913c60000080110000868d5a55868d16380d3dfc8e027d80369617c40d00c8000c000100c0c540604bc540591a7259e2f6f1e0cccd9615e85d913a1d838014881e1b4f9d5e4ceb5013d5f9d8731a137f2f6cf6e5e966fd9a113cb42fa97c24f70e4eebd45073a750531a95add9d12ecacb0fa0c7119a231bdb163277cae13dd5d8d2a6acf1b6358b73b75d04e14bec9e407f442c2f2e9535e59b745b138c72a9f52397ac43f1cedd261ddc0a61910f0505c6649b1afe89c78a593c0c8efb40397d2b0ad713606ba97dd5878302de68d81e7c1f803f090c86f73bb354ef0fcf2435dc4eef4916fbab349a5213b8e90da4275552dc7be486424f7e224b9f8c8a6dcb37e095c1d3eb760493ba2b4dd49a17ae707500686a5c40825818e64bbc0b6da6ffb0f6c760e2c6b159e0ee058e882a3b44e83c6779333276cf87b824fe073b01aacf99e572ce0a01a0ad4c106cfe5ef5d58a590d1a5848dfb64b1f132dafefc18e77456d849a7f5596519b5b43489a7a1b6c60c5e6ae9edc2b1ecb94627d9604afa2a47f80f885738026754692b7169dc86862082a2be46eb6fa4814fa468eabd9216f0120486a27df1421ba466f73962d67718d23eb60a13d35bfe38b01981aab2ce743b72ccb0a8d2f885266e52244614efb2a52ba70bc21854dfe71ce664f83a4c4c43b74fc4616a72393c35723d455a46b01f9c107533f24b28d7eb7ecfb35425afe424b6e643a5d3d52be27da58740ad80256239cf0e1e0167a7680ba9128c642ec222fa9da7dc969bd713590298ac6d1a54154919a1080bd1f67e84dc273b7ca2b32b4fb1da7cab11400b66b398950aad4fd3b492ff6b7b4853cc55ab07ca030867b98551f1a306b9a29512266a71c2425f3e4d20337df1b33262add77cadd889b6137932dff4dbef292")

        trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
        print("start capture on port " +device_object.rx_port + "\n")
        trafficDevice.start_capture(rx_port)
        trafficDevice.start_traffic(tx_port)
        time.sleep(5)
        trafficDevice.stop_capture(rx_port)
        trafficDevice.stop_traffic(tx_port)

        frames = trafficDevice.get_all_captured_frames(rx_port)
        print("Number of packets received: " + str(len(frames)))
        found = 0
        print(trafficDevice.get_filtered_captured_frames_report(rx_port))

        trafficDevice.get_port_statistic_rx_raw_pkt_count(rx_port)
        list_index = [1,4,7,8]
        for packet_index in list_index:
            try:
                helper = trafficDevice.get_capture_helper()
                print("get capture count " + str(helper.get_captured_frame_count(rx_port)))
                # frames = trafficDevice.get_all_captured_frames(rx_port)
                frame = trafficDevice.get_captured_frame(rx_port, packet_index)
            except:
                pass

    def test_configuring_arp_tgd_with_ping(self):  # test out the packet capture filters, triggers, etc... SINGLE CALLS
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        helper = trafficDevice
        ip1 = "151.1.1.1"
        ip2 = "151.1.1.20"
        ip12 = "151.1.1.1"
        ip22 = "151.1.1.21"
        ip11 = "151.1.2.1"
        ip21 = "151.1.2.20"
        ip121 = "151.1.2.1"
        ip221 = "151.1.2.21"
        print("configuring port " + str(tx_port))
        trafficDevice.configure_arp(tx_port, ip1, "00:33:44:55:66:77", 5)
        trafficDevice.configure_arp(tx_port, ip11, "00:33:44:55:66:71", 5)
        print("configuring port " + str(rx_port))
        trafficDevice.configure_arp(rx_port, ip2, "00:22:44:55:66:77", 5)
        trafficDevice.configure_arp(rx_port, ip21, "00:22:44:55:66:71", 5)
        trafficDevice.start_capture(rx_port)
        print("now ping " +ip2 +" from " +ip1)
        trafficDevice.ping(tx_port, ip1, ip2)
        trafficDevice.ping(tx_port, ip11, ip21)
        trafficDevice.get_arp_table(tx_port)
        trafficDevice.get_arp_table(rx_port)
        trafficDevice.verify_arp_entry(tx_port, "151.1.1.20", "0.22.44.55.66.77")
        trafficDevice.verify_arp_entry(tx_port, "151.1.1.1", "0.33.44.55.66.77")
        trafficDevice.verify_arp_entry(rx_port, "151.1.1.20", "0.22.44.55.66.77")
        trafficDevice.verify_arp_entry(rx_port, "151.1.1.1", "0.33.44.55.66.77")
        print("now ping " +ip2 +" from " +ip1)
        trafficDevice.ping(tx_port, ip12, ip22)
        trafficDevice.stop_capture(rx_port)

        frames = trafficDevice.get_all_captured_frames(rx_port)

    def test_configuring_arp(self):  # test out the packet capture filters, triggers, etc... SINGLE CALLS
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        helper = trafficDevice
        print("configuring port " + str(tx_port))
        trafficDevice.configure_arp(tx_port, "151.1.1.1", "00:33:44:55:66:77", 5, "0.0.0.0")
        print("configuring port " + str(rx_port))
        trafficDevice.configure_arp(rx_port, "152.1.1.1", "00:22:44:55:66:77", 5, "0.0.0.0", vlan_enable=True, vlan_id=152)

        print("now configure the device")

        #ip_address = "10.52.16.34"
        ip_address = "10.69.11.30"
        print(("====" *20))
        print("Testing Telnet")
        # create a device
        dev = NetworkElement(NetworkElementConstants.OS_EXOS, NetworkElementConstants.PLATFORM_EXOS_BASE,
                             NetworkElementConstants.UNIT_BASE, NetworkElementConstants.VERSION_BASE)
        dev.hostname = ip_address  # this is the host that the current agent will use.
        dev.port = AgentConstants.TELNET_PORT  # this is the port that the current agent will use. no need to
        # set for telnet. defaults to 23.

        # initialize the values of the current agent which the dut will use. True in the beginning means "initialize
        # and login"
        # dev.init_current_agent(True, AgentConstants.TYPE_TELNET,"admin","enterasysTPB","login:","password:","#")
        dev.init_current_agent(True, AgentConstants.TYPE_TELNET, "admin", "", "login:", "password:", "#")
        print(dev.send_command(u'dir'))
        # tx_port_dut = "1:21"
        tx_port_dut = "2:21"
        tx_port_dut = "1"
        print(dev.send_command(u'enable ports ' +tx_port_dut))
        print("From the EXOS cli: Create a VLAN, set it to tagged or untagged egress on the ixia port (based on whether you want to test with tagged ARPs or not)")
        print(dev.send_command(u'create vlan 151'))
        print(dev.send_command(u'configure vlan 151 add port ' +tx_port_dut +u' untagged'))
        print(dev.send_command(u'configure vlan 151 ipadd 151.1.1.100'))

        print("Then ping:(have to specify the VR)")
        print(dev.send_command(u'ping vr VR-Default 151.1.1.1'))
        time.sleep(3)
        print(dev.send_command(u'show iparp'))


        # tx_port_dut = "1:2"
        tx_port_dut = "2:21"
        tx_port_dut = "2"
        print(dev.send_command(u'enable ports ' +tx_port_dut))
        print("From the EXOS cli: Create a VLAN, set it to tagged or untagged egress on the ixia port (based on whether you want to test with tagged ARPs or not)")
        print(dev.send_command(u'create vlan 152'))
        print(dev.send_command(u'configure vlan 152 add port ' +tx_port_dut +u' tagged'))
        print(dev.send_command(u'configure vlan 152 ipadd 152.1.1.100'))

        print("Then ping:(have to specify the VR)")
        print(dev.send_command(u'ping vr VR-Default 152.1.1.1'))
        time.sleep(3)
        print(dev.send_command(u'show iparp'))

        print("something")

    def test_main_capture_filter_single(self):  # test out the packet capture filters, triggers, etc... SINGLE CALLS
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        helper = trafficDevice.get_capture_helper()
        helper.set_capture_filter_da1(device_object.rx_port, "00:ee:00:ff:00:00","00:00:00:00:00:00")
        helper.set_capture_filter_da2(device_object.rx_port, "00:ee:00:ff:aa:00","00:00:00:00:00:ff")
        helper.set_capture_filter_sa1(device_object.rx_port, "00:dd:00:ff:00:00","00:00:00:00:00:00")
        helper.set_capture_filter_sa2(device_object.rx_port, "00:dd:00:ff:aa:00","00:00:00:00:00:ff")
        #set_capture_filter(self, port_handle, daLogic, saLogic, errorLogic, frameSizeLogic, frameStartSize, frameEndSize, options={}):
        helper.set_capture_filter(device_object.rx_port, True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)
        helper.set_capture_trigger(device_object.rx_port, True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)
        helper.set_capture_user_defined_statistics1(device_object.rx_port, True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)
        helper.set_capture_user_defined_statistics2(device_object.rx_port, True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)
        helper.set_capture_user_defined_statistics2(device_object.rx_port, False, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)

    def test_main_capture_filter_set_send_capture(self):  # test out the packet capture filters, triggers, etc... SINGLE CALLS
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        helper = trafficDevice.get_capture_helper()
        helper.set_capture_filter_da1(device_object.rx_port, "00:ee:00:ff:00:00","00:00:00:00:00:00")
        helper.set_capture_filter_da2(device_object.rx_port, "00:ee:00:ff:aa:00","00:00:00:00:00:ff")
        helper.set_capture_filter_sa1(device_object.rx_port, "00:dd:00:ff:00:00","00:00:00:00:00:00")
        helper.set_capture_filter_sa2(device_object.rx_port, "00:dd:00:ff:aa:00","00:00:00:00:00:ff")
        #set_capture_filter(self, port_handle, daLogic, saLogic, errorLogic, frameSizeLogic, frameStartSize, frameEndSize, options={}):
        helper.set_capture_filter(device_object.rx_port, True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)
        helper.set_capture_trigger(device_object.rx_port, True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)
        helper.set_capture_user_defined_statistics1(device_object.rx_port, True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)
        helper.set_capture_user_defined_statistics2(device_object.rx_port, True, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)
        helper.set_capture_user_defined_statistics2(device_object.rx_port, False, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_NOTDA1,
                                  PacketConfigTriggersConstants.CAPTURE_FILTER_SA_SA1,
                                  None, None, None, None)
        trafficDevice.clear_all_streams(rx_port)
        # packets = PacketClassifier.get_one_of_every_untagged()
        packets = PacketClassifier.get_one_of_every_packet()
        # packets = PacketClassifier.get_one_of_every_snap()
        # packets = PacketClassifier.get_one_of_every_sap()
        for packet in packets:
            trafficDevice.clear_all_streams(tx_port)
            # trafficDevice.clear_capture_buffer(rx_port)
            if isinstance(packet, VlanStackPacketHeader):
                packet.set_vlan_num(2)
            PacketClassifier.set_default_test_packet_values(packet)
            # packet.set_length(500)
            print("set ip stream id 1 on port " +device_object.tx_port + "\n")
            print(str(packet))
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            # packet = PacketClassifier.classify_packet_bytes("00005e00011054ee758acc0c0800450002913c60000080110000868d5a55868d16380d3dfc8e027d80369617c40d00c8000c000100c0c540604bc540591a7259e2f6f1e0cccd9615e85d913a1d838014881e1b4f9d5e4ceb5013d5f9d8731a137f2f6cf6e5e966fd9a113cb42fa97c24f70e4eebd45073a750531a95add9d12ecacb0fa0c7119a231bdb163277cae13dd5d8d2a6acf1b6358b73b75d04e14bec9e407f442c2f2e9535e59b745b138c72a9f52397ac43f1cedd261ddc0a61910f0505c6649b1afe89c78a593c0c8efb40397d2b0ad713606ba97dd5878302de68d81e7c1f803f090c86f73bb354ef0fcf2435dc4eef4916fbab349a5213b8e90da4275552dc7be486424f7e224b9f8c8a6dcb37e095c1d3eb760493ba2b4dd49a17ae707500686a5c40825818e64bbc0b6da6ffb0f6c760e2c6b159e0ee058e882a3b44e83c6779333276cf87b824fe073b01aacf99e572ce0a01a0ad4c106cfe5ef5d58a590d1a5848dfb64b1f132dafefc18e77456d849a7f5596519b5b43489a7a1b6c60c5e6ae9edc2b1ecb94627d9604afa2a47f80f885738026754692b7169dc86862082a2be46eb6fa4814fa468eabd9216f0120486a27df1421ba466f73962d67718d23eb60a13d35bfe38b01981aab2ce743b72ccb0a8d2f885266e52244614efb2a52ba70bc21854dfe71ce664f83a4c4c43b74fc4616a72393c35723d455a46b01f9c107533f24b28d7eb7ecfb35425afe424b6e643a5d3d52be27da58740ad80256239cf0e1e0167a7680ba9128c642ec222fa9da7dc969bd713590298ac6d1a54154919a1080bd1f67e84dc273b7ca2b32b4fb1da7cab11400b66b398950aad4fd3b492ff6b7b4853cc55ab07ca030867b98551f1a306b9a29512266a71c2425f3e4d20337df1b33262add77cadd889b6137932dff4dbef292")

            trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
            print("start capture on port " +device_object.rx_port + "\n")
            trafficDevice.start_capture(rx_port)
            trafficDevice.start_traffic(tx_port)
            time.sleep(5)
            trafficDevice.stop_capture(rx_port)
            trafficDevice.stop_traffic(tx_port)
            trafficDevice.get_port_statistic_rx_raw_pkt_count(rx_port)
            list_index = [1,4,7,8]
            for packet_index in list_index:
                try:
                    helper = trafficDevice.get_capture_helper()
                    print("get capture count " + str(helper.get_captured_frame_count(rx_port)))
                    # frames = trafficDevice.get_all_captured_frames(rx_port)
                    frame = trafficDevice.get_captured_frame(rx_port, packet_index)

                    # if len(frames) > 0:
                    trafficDevice.get_all_captured_frames(rx_port)
                    print("sent")
                    print(str(packet))
                    print("received")
                    print(str(frame))
                    if isinstance(packet, TaggedPacketHeader) and not isinstance(frame, TaggedPacketHeader):
                        print("Error! Tag not parsed")
                    elif not isinstance(packet, TaggedPacketHeader) and isinstance(frame, TaggedPacketHeader):
                        print("Error! Tag added")
                    elif isinstance(packet, VlanStackPacketHeader) and not isinstance(frame, VlanStackPacketHeader):
                        print("Error! Tag not parsed")
                    elif not isinstance(packet, VlanStackPacketHeader) and isinstance(frame, VlanStackPacketHeader):
                        print("Error! Tag added")
                    # else:
                    #     print("Empty")
                except:
                    print("Error with the frames")

    def test_duplex_speed(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        print("Port Speed" + tx_port + " = " + str(trafficDevice.get_port_speed(tx_port)))
        print("Port Speed" + rx_port + " = " + str(trafficDevice.get_port_speed(rx_port)))
        print("setting port speed on tx to 10")
        trafficDevice.set_port_speed(tx_port, InterfaceConfigConstants.SPEED_ETHER10, True)
        time.sleep(5)
        print("port link check " + str(trafficDevice.has_link(tx_port)))

        print("Port Speed" + tx_port + " = " + str(trafficDevice.get_port_speed(tx_port)))
        print("Port Speed" + rx_port + " = " + str(trafficDevice.get_port_speed(rx_port)))

        print("setting port speed on tx to 10")
        trafficDevice.set_port_speed(rx_port, InterfaceConfigConstants.SPEED_ETHER10, True)
        time.sleep(5)
        print("port link check " + str(trafficDevice.has_link(tx_port)))
        print("Port Speed" + tx_port + " = " + str(trafficDevice.get_port_speed(tx_port)))
        print("Port Speed" + rx_port + " = " + str(trafficDevice.get_port_speed(rx_port)))

    def test_port_lists(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        print("Port Speed" + str(tx_port) + " = " + str(trafficDevice.get_port_speed(tx_port)))
        print("Port Speed" + str(rx_port) + " = " + str(trafficDevice.get_port_speed(rx_port)))
        print("setting port speed on tx to 10")
        trafficDevice.set_port_speed(tx_port, InterfaceConfigConstants.SPEED_ETHER10, True)
        time.sleep(5)
        trafficDevice.tgen_debug = True
        trafficDevice.set_capture_mode([tx_port, rx_port], "{" + InterfaceConfigConstants.PORT_RX_MODE_CAPTURE + " " +
                                                    InterfaceConfigConstants.PORT_RX_MODE_WIDE_PACKET_GROUP + "}")
        # print("port link check " + str(trafficDevice.has_link([tx_port, rx_port])))

        print("Port Speed" + str(tx_port) + " = " + str(trafficDevice.get_port_speed(tx_port)))
        print("Port Speed" + str(rx_port) + " = " + str(trafficDevice.get_port_speed(rx_port)))

        print("setting port speed on tx to 10")
        trafficDevice.set_port_speed(rx_port, InterfaceConfigConstants.SPEED_ETHER10, True)
        time.sleep(5)
        print("port link check " + str(trafficDevice.has_link(tx_port)))
        print("Port Speed" + str(tx_port) + " = " + str(trafficDevice.get_port_speed(tx_port)))
        print("Port Speed" + str(rx_port) + " = " + str(trafficDevice.get_port_speed(rx_port)))
        trafficDevice.wait_for_has_link([tx_port, rx_port])

    def test_frame_sequence_checking(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        trafficDevice.tgen_debug = True

        packets = PacketClassifier.get_one_of_every_packet()
        packet = packets[0]
        packet.set_destination_mac("00:33:22:33:44:55")
        packet.set_source_mac("00:33:22:33:44:66")
        opt_dict = {}
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value

        index = 0
        for index in range(0, 6):
            index += 1
            trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
            if index == 1:
                trafficDevice.configure_stream_fcs_bad_packet(tx_port, 1)
            elif index == 2:
                trafficDevice.configure_stream_fcs_alignment(tx_port, 1)
            elif index == 3:
                trafficDevice.configure_stream_fcs_dribble(tx_port, 1)
            elif index == 4:
                trafficDevice.configure_stream_fcs_good_packet(tx_port, 1)
            elif index == 5:
                trafficDevice.configure_stream_fcs_jabber(tx_port, 1)
            elif index == 6:
                trafficDevice.configure_stream_fcs_none(tx_port, 1)
            print("start capture on port " +rx_port +"\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +tx_port +"\n")
            trafficDevice.start_traffic(tx_port)
            print("sleep for 5 seconds\n")
            time.sleep(5)
            print("stop traffic on port " +tx_port +"\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +rx_port +"\n")
            trafficDevice.stop_capture(rx_port)
            helper = trafficDevice.get_capture_helper()
            frames = helper.get_all_captured_frames(rx_port)
            print(rx_port +" had " + str(len(frames)) + " packets captured")
            print("here is packet #2")
            if len(frames) >= 1:
                print(frames[1].to_packet_string())
                print("FCS: " + str(frames[1].status))
                print("get_captured_frame_status: " + hex(int(trafficDevice.get_captured_frame_status(rx_port, 1))))

    def test_pcap_out(self):  # test out the packet capture with all packets.

        packets = PacketClassifier.get_one_of_every_packet()
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            packet.auto_set_minimum_length()

        PacketClassifier.save_to_pcap_file_contents(packets, "c:\\TRM_DATA\\file.pcap")

        print("dasdasd")

    def test_one_of_every_packet_capture(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        trafficDevice.clear_all_streams(tx_port)
        trafficDevice.clear_all_streams(rx_port)
        # packets = PacketClassifier.get_one_of_every_untagged()
        packets = PacketClassifier.get_one_of_every_packet("ICMP")
        # packets = PacketClassifier.get_one_of_every_snap()
        # packets = PacketClassifier.get_one_of_every_sap()
        PacketClassifier.save_to_pcap_file_contents(packets, "c:\\TRM_DATA\\file.pcap")
        for packet in packets:
            trafficDevice.clear_all_streams(tx_port)
            # trafficDevice.clear_capture_buffer(rx_port)
            if isinstance(packet, VlanStackPacketHeader):
                packet.set_vlan_num(2)
            PacketClassifier.set_default_test_packet_values(packet)
            # packet.set_length(500)
            print("set ip stream id 1 on port " +device_object.tx_port + "\n")
            print(str(packet))
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            # packet = PacketClassifier.classify_packet_bytes("00005e00011054ee758acc0c0800450002913c60000080110000868d5a55868d16380d3dfc8e027d80369617c40d00c8000c000100c0c540604bc540591a7259e2f6f1e0cccd9615e85d913a1d838014881e1b4f9d5e4ceb5013d5f9d8731a137f2f6cf6e5e966fd9a113cb42fa97c24f70e4eebd45073a750531a95add9d12ecacb0fa0c7119a231bdb163277cae13dd5d8d2a6acf1b6358b73b75d04e14bec9e407f442c2f2e9535e59b745b138c72a9f52397ac43f1cedd261ddc0a61910f0505c6649b1afe89c78a593c0c8efb40397d2b0ad713606ba97dd5878302de68d81e7c1f803f090c86f73bb354ef0fcf2435dc4eef4916fbab349a5213b8e90da4275552dc7be486424f7e224b9f8c8a6dcb37e095c1d3eb760493ba2b4dd49a17ae707500686a5c40825818e64bbc0b6da6ffb0f6c760e2c6b159e0ee058e882a3b44e83c6779333276cf87b824fe073b01aacf99e572ce0a01a0ad4c106cfe5ef5d58a590d1a5848dfb64b1f132dafefc18e77456d849a7f5596519b5b43489a7a1b6c60c5e6ae9edc2b1ecb94627d9604afa2a47f80f885738026754692b7169dc86862082a2be46eb6fa4814fa468eabd9216f0120486a27df1421ba466f73962d67718d23eb60a13d35bfe38b01981aab2ce743b72ccb0a8d2f885266e52244614efb2a52ba70bc21854dfe71ce664f83a4c4c43b74fc4616a72393c35723d455a46b01f9c107533f24b28d7eb7ecfb35425afe424b6e643a5d3d52be27da58740ad80256239cf0e1e0167a7680ba9128c642ec222fa9da7dc969bd713590298ac6d1a54154919a1080bd1f67e84dc273b7ca2b32b4fb1da7cab11400b66b398950aad4fd3b492ff6b7b4853cc55ab07ca030867b98551f1a306b9a29512266a71c2425f3e4d20337df1b33262add77cadd889b6137932dff4dbef292")

            trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
            print("start capture on port " +device_object.rx_port + "\n")
            trafficDevice.start_capture(rx_port)
            trafficDevice.start_traffic(tx_port)
            time.sleep(5)
            trafficDevice.stop_capture(rx_port)
            trafficDevice.stop_traffic(tx_port)
            trafficDevice.get_port_statistic_rx_raw_pkt_count(rx_port)
            list_index = [1,4,7,8]
            for packet_index in list_index:
                try:
                    helper = trafficDevice.get_capture_helper()
                    print("get capture count " + str(helper.get_captured_frame_count(rx_port)))
                    # frames = trafficDevice.get_all_captured_frames(rx_port)
                    frame = trafficDevice.get_captured_frame(rx_port, packet_index)
                    helper.save_all_captured_frames_to_pcap(rx_port,"c:\\TRM_DATA\\file.pcap")
                    # if len(frames) > 0:
                    trafficDevice.get_all_captured_frames(rx_port)
                    print("sent")
                    print(str(packet))
                    print("received")
                    print(str(frame))
                    if isinstance(packet, TaggedPacketHeader) and not isinstance(frame, TaggedPacketHeader):
                        print("Error! Tag not parsed")
                    elif not isinstance(packet, TaggedPacketHeader) and isinstance(frame, TaggedPacketHeader):
                        print("Error! Tag added")
                    elif isinstance(packet, VlanStackPacketHeader) and not isinstance(frame, VlanStackPacketHeader):
                        print("Error! Tag not parsed")
                    elif not isinstance(packet, VlanStackPacketHeader) and isinstance(frame, VlanStackPacketHeader):
                        print("Error! Tag added")
                    # else:
                    #     print("Empty")
                except:
                    print("Error with the frames")

    def test_main_capture(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_untagged()
        packets = PacketClassifier.get_one_of_every_packet()
        #packets = PacketClassifier.get_all_packets_from_tags(["icmp"])

        one_of_each = []
        for packet in packets:
            # if not isinstance(packet, IpV4PacketHeader):
            #     continue
            # if not isinstance(packet, RadiusPacketHeader):
            #     continue
            # if not isinstance(packet, TcpPacketHeader):
            #     continue
            PacketClassifier.set_default_test_packet_values(packet)
            # packet.set_ipv6_next_header(0x55)
            new_packet = PacketClassifier.translate_packet(packet, PacketClassifierConstants.ETHERNETSNAPUDPIPV6VLANSTACKPACKET)
            print(str(new_packet))
            print("set ip stream id 1 on port " +device_object.tx_port + "\n")
            print(str(packet))
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
            trafficDevice.get_traffic_helper().configure_stream_mac_dst_options(tx_port, 1, None,
                                                                                TrafficConfigConstants.MAC_DST_MODE_INCREMENT,
                                                                                11, 10, None)
            trafficDevice.get_traffic_helper().configure_stream_mac_src_options(tx_port, 1, None,
                                                                                TrafficConfigConstants.MAC_SRC_MODE_DECREMENT,
                                                                                4, 44, None)
            if isinstance(packet, IpV4PacketHeader):
                trafficDevice.get_traffic_helper().configure_stream_ip_dst_options(tx_port, 1, "3.3.3.3",
                                                                                   TrafficConfigConstants.IP_DST_MODE_INCREMENT,
                                                                                   4, "1.1.1.1")
                trafficDevice.get_traffic_helper().configure_stream_ip_src_options(tx_port, 1, "2.2.2.2",
                                                                                   TrafficConfigConstants.IP_SRC_MODE_DECREMENT,
                                                                                   4, "1.1.1.1")
            if isinstance(packet, IpV6PacketHeader):
                trafficDevice.get_traffic_helper().configure_stream_ipv6_dst_options(tx_port, 1, "FFFF::0001",
                                                                                     TrafficConfigConstants.IPV6_DST_MODE_INCREMENT,
                                                                                     4, "0001::0001")
                trafficDevice.get_traffic_helper().configure_stream_ipv6_src_options(tx_port, 1, "FFFE::0001",
                                                                                     TrafficConfigConstants.IPV6_SRC_MODE_DECREMENT,
                                                                                     4, "0002::0001")

            if isinstance(packet, IpV6PacketHeader):
                trafficDevice.get_traffic_helper().configure_stream_ipv6_dst_options(tx_port, 1, "FFFF::0001",
                                                                                     TrafficConfigConstants.IPV6_DST_MODE_INCREMENT,
                                                                                     4, "0001::0001")
                trafficDevice.get_traffic_helper().configure_stream_ipv6_src_options(tx_port, 1, "FFFE::0001",
                                                                                TrafficConfigConstants.IPV6_SRC_MODE_DECREMENT,
                                                                                                 4, "0002::0001")
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

    def configure_stream_arp_sender_hardware_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_untagged()
        packets = PacketClassifier.get_one_of_every_packet()
        packets = PacketClassifier.get_all_packets_from_tags("Arp")
        one_of_each = []
        for packet in packets:
            print("start capture on port " +device_object.rx_port + "\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +device_object.tx_port + "\n")
            trafficDevice.start_traffic(tx_port)
            print("sleep for 5 seconds\n")
            time.sleep(15)
            print("stop traffic on port " +device_object.tx_port + "\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +device_object.rx_port + "\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +device_object.tx_port + " and " +device_object.rx_port + "")
            helper = trafficDevice.get_capture_helper()
            frames = helper.get_all_captured_frames(rx_port)
            print("" +device_object.rx_port + " had " + str(len(frames)) + " packets captured")
            print("here is packet #2")
            if len(frames) >= 2:
                one_of_each.append(frames[2])
                print(packet.compare_packet_fields(frames[2]))
                print(frames[2].to_packet_string())
                if isinstance(packet, IpV4PacketHeader):
                    ipChecksum1 = frames[2].get_ip_checksum()
                if isinstance(packet, UdpPacketHeader):
                    udpChecksum1 = frames[2].get_udp_checksum()
                if isinstance(packet, TcpPacketHeader):
                    tcpChecksum1 = frames[2].get_tcp_checksum()

                if isinstance(frames[2], IpV4PacketHeader):
                    frames[2].configure_packet(frames[2].get_length())
                    print(frames[2].to_packet_string())

                if isinstance(frames[2], IpV4PacketHeader):
                    ipChecksum2 = frames[2].get_ip_checksum()
                    print("IPv4 check sums before " + (packet.format_int(ipChecksum1, 2)) + " and after " + (packet.format_int(ipChecksum2, 2)) + " match = " + str(ipChecksum1 == ipChecksum2))
                    if ipChecksum1 != ipChecksum2:
                        print("failed")
                if isinstance(frames[2], TcpPacketHeader):
                    tcpChecksum2 = frames[2].get_tcp_checksum()
                    print("TCP check sums before " + (packet.format_int(tcpChecksum1, 2)) + " and after " + (packet.format_int(tcpChecksum2, 2)) + " match = " + str(tcpChecksum1 == tcpChecksum2))
                    if tcpChecksum1 != tcpChecksum2:
                        print("failed")
                if isinstance(frames[2], UdpPacketHeader):
                    udpChecksum2 = frames[2].get_udp_checksum()
                    print("UDP check sums before " + (packet.format_int(udpChecksum1, 2)) + " and after " + (packet.format_int(udpChecksum2, 2)) + " match = " + str(udpChecksum1 == udpChecksum2))
                    if udpChecksum1 != udpChecksum2:
                        print("failed")
            print("" +device_object.rx_port + " clear buffers")
            trafficDevice.clear_capture_buffer(device_object.rx_port)
            frames = helper.get_all_captured_frames(rx_port)
            print("" +device_object.rx_port + " had " + str(len(frames)) + " packets captured")

            print("" +device_object.rx_port + " clear statistics and filters and buffers")
            trafficDevice.clear_statistics_and_filters(rx_port)
            frames = helper.get_all_captured_frames(rx_port)
            print("" +device_object.tx_port + " had " + str(len(frames)) + " packets captured")
        for packet in one_of_each:
            print("===" * 20)
            print(packet.to_packet_string())
        print("0000" * 20)

    def test_encapsulated_traffic(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        inner_packet = Ethernet2UdpIpV4Packet()
        inner_packet_v6 = Ethernet2TcpIpV6Packet()
        PacketClassifier.set_default_test_packet_values(inner_packet)
        inner_packet.configure_packet()
        inner_packet_v6.configure_packet()
        gre_packet = Ethernet2GreIpV4Packet(inner_packet)
        print(gre_packet.to_packet_string())
        gre_packet.set_gre_flag_checksum_present(True)

        vxlan_packet = Ethernet2VxlanUdpIpV4Packet(inner_packet)
        inner_packet = Ethernet2UdpIpV4Packet()
        PacketClassifier.set_default_test_packet_values(inner_packet)
        inner_packet.configure_packet()
        gre1_packet = Ethernet2IpEncapsulatedIpV6Packet(inner_packet)

        inner_packet = Ethernet2UdpIpV4Packet()
        PacketClassifier.set_default_test_packet_values(inner_packet)
        inner_packet.configure_packet()
        gre2_packet = Ethernet2IpEncapsulatedIpV4Packet(inner_packet)

        inner_packet_v6 = Ethernet2TcpIpV6Packet()
        PacketClassifier.set_default_test_packet_values(inner_packet_v6)
        inner_packet_v6.configure_packet()
        gre3_packet = Ethernet2IpEncapsulatedIpV6Packet(inner_packet_v6)

        inner_packet_v6 = Ethernet2TcpIpV6Packet()
        PacketClassifier.set_default_test_packet_values(inner_packet_v6)
        inner_packet_v6.configure_packet()
        gre4_packet = Ethernet2IpEncapsulatedIpV4Packet(inner_packet_v6)

        inner_packet = Ethernet2UdpIpV4Packet()
        PacketClassifier.set_default_test_packet_values(inner_packet)
        inner_packet.configure_packet()
        gre_erpsan = Ethernet2ErspanGreIpV4Packet(inner_packet)

        inner_packet = Ethernet2UdpIpV4Packet()
        PacketClassifier.set_default_test_packet_values(inner_packet)
        inner_packet.configure_packet()
        gre_erpsan_iii = Ethernet2ErspanIIIGreIpV4Packet(inner_packet)

        packets = [gre_packet, gre_erpsan, gre_erpsan_iii, vxlan_packet,gre1_packet,gre2_packet,gre3_packet,gre4_packet]
        one_of_each = []
        stream_id = 0
        for packet in packets:
            trafficDevice.clear_all_streams(tx_port)
            print(packet)
            stream_id += 0
            PacketClassifier.set_default_test_packet_values(packet)
            print("set ip stream id " + str(stream_id) + " on port " +device_object.tx_port + "\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 1000
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_NEXT # constant value

            trafficDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)

            print("start capture on port " +rx_port +"\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +tx_port +"\n")
            trafficDevice.start_traffic_and_wait(tx_port, 60000)
            print("stop traffic on port " +tx_port +"\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +rx_port +"\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +tx_port +" and " +rx_port)
            helper = trafficDevice.get_capture_helper()
            frames = helper.get_all_captured_frames(rx_port)
            # filtered_frames = helper.get_filtered_captured_frames(rx_port, IpV4PacketHeader)
            # print("filtered frame count for ipv4=" + str(len(filtered_frames)))
            # filtered_frames = helper.get_filtered_captured_frames(rx_port, [IpV4PacketHeader, TcpPacketHeader])
            # print("filtered frame count for ipv4 + tcp=" + str(len(filtered_frames)))
            print("" +rx_port +" had " + str(len(frames)) + " packets captured")
            print(packet.get_bytes())
            print("here is packet #2")
            if len(frames) > 0:
                print(frames[0].to_packet_string())
                print(frames[-1].to_packet_string())
                one_of_each.append(frames[-1])
                packet.compare_packet_fields(
                    frames[-1]
                )
                print(frames[-1].get_bytes())
            print("" +rx_port +" clear buffers")
            trafficDevice.clear_capture_buffer(device_object.rx_port)
            frames = helper.get_all_captured_frames(rx_port)
            print("" +rx_port +" had " + str(len(frames)) + " packets captured")

            print("" +rx_port +" clear statistics and filters and buffers")
            trafficDevice.clear_statistics_and_filters(rx_port)
            frames = helper.get_all_captured_frames(rx_port)
            print("" +tx_port +" had " + str(len(frames)) + " packets captured")
        for packet in one_of_each:
            print("===" * 20)
            print(packet.to_packet_string())
        print("0000" * 20)

    def test_igmp_stream_capture(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_packet("IGMP")
        one_of_each = []
        stream_id = 0
        packet = packets[stream_id]
        igmp_types = [0x10, 0x11, 0x12, 0x16, 0x17, 0x1e, 0x1f]
        PacketClassifier.set_default_test_packet_values(packet)
        while stream_id < len(igmp_types):
            trafficDevice.clear_all_streams(rx_port)
            igmp_type = igmp_types[stream_id]
            stream_id += 1
            packet.set_igmp_type(igmp_type)
            print("set ip stream id " + str(stream_id) + " on port " +device_object.tx_port + "\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 1000
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_NEXT # constant value
            # trafficDevice.clear_stream(tx_port, 1)
            trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)

            print("start capture on port " +rx_port +"\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +tx_port +"\n")
            trafficDevice.start_traffic_and_wait(tx_port, 60000)
            print("stop traffic on port " +tx_port +"\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +rx_port +"\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +tx_port +" and " +rx_port)
            helper = trafficDevice.get_capture_helper()
            frames = helper.get_all_captured_frames(rx_port)
            filtered_frames = helper.get_all_captured_frames_filtered_by_tags(rx_port, IpV4PacketHeader)
            print("filtered frame count for ipv4=" + str(len(filtered_frames)))
            filtered_frames = helper.get_all_captured_frames_filtered_by_tags(rx_port, [IpV4PacketHeader, TcpPacketHeader])
            print("filtered frame count for ipv4 + tcp=" + str(len(filtered_frames)))
            print("" +rx_port +" had " + str(len(frames)) + " packets captured")
            print("here is packet #2")
            if len(frames) >= 2:
                print(packet.to_packet_string())
                print(frames[2].to_packet_string())
        print("0000" * 20)

    def test_multiple_streams_capture(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_packet()
        one_of_each = []
        stream_id = 0
        trafficDevice.clear_all_streams(rx_port)
        while stream_id < len(packets):
            packet = packets[stream_id]
            stream_id += 1
            PacketClassifier.set_default_test_packet_values(packet)
            print("set ip stream id " + str(stream_id) + " on port " +device_object.tx_port + "\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 1000
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_NEXT # constant value

            trafficDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)

            print("start capture on port " +rx_port +"\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +tx_port +"\n")
            trafficDevice.start_traffic_and_wait(tx_port, 60000)
            print("stop traffic on port " +tx_port +"\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +rx_port +"\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +tx_port +" and " +rx_port)
            helper = trafficDevice.get_capture_helper()
            frames = helper.get_all_captured_frames(rx_port)
            filtered_frames = helper.get_all_captured_frames_filtered_by_tags(rx_port, IpV4PacketHeader)
            print("filtered frame count for ipv4=" + str(len(filtered_frames)))
            filtered_frames = helper.get_all_captured_frames_filtered_by_tags(rx_port, [IpV4PacketHeader, TcpPacketHeader])
            print("filtered frame count for ipv4 + tcp=" + str(len(filtered_frames)))
            print("" +rx_port +" had " + str(len(frames)) + " packets captured")
            print("here is packet #2")
            if len(frames) >= 2:
                print(frames[2].to_packet_string())
                one_of_each.append(frames[2])
            print("" +rx_port +" clear buffers")
            trafficDevice.clear_capture_buffer(device_object.rx_port)
            frames = helper.get_all_captured_frames(rx_port)
            print("" +rx_port +" had " + str(len(frames)) + " packets captured")

            print("" +rx_port +" clear statistics and filters and buffers")
            trafficDevice.clear_statistics_and_filters(rx_port)
            frames = helper.get_all_captured_frames(rx_port)
            print("" +tx_port +" had " + str(len(frames)) + " packets captured")
        for packet in one_of_each:
            print("===" * 20)
            print(packet.to_packet_string())
        print("0000" * 20)

    def test_multiple_streams_array_capture(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_ethernet2()
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        trafficDevice.configure_streams_using_packets(tx_port, packets)
        print("start capture on port " +rx_port +"\n")
        trafficDevice.start_capture(rx_port)
        print("start traffic on port " +tx_port +"\n")
        trafficDevice.start_traffic(tx_port)
        print("sleep for 5 seconds\n")
        time.sleep(15)
        print("stop traffic on port " +tx_port +"\n")
        trafficDevice.stop_traffic(tx_port)
        print("stop capture on port " +rx_port +"\n")
        trafficDevice.stop_capture(rx_port)
        print("get some port capture stats " +tx_port +" and " +rx_port)
        helper = trafficDevice.get_capture_helper()
        frames = helper.get_all_captured_frames(rx_port)
        print("" +rx_port +" had " + str(len(frames)) + " packets captured")
        print("" +rx_port +" clear buffers")
        trafficDevice.clear_capture_buffer(device_object.rx_port)
        frames = helper.get_all_captured_frames(rx_port)
        print("" +rx_port +" had " + str(len(frames)) + " packets captured")

        print("" +rx_port +" clear statistics and filters and buffers")
        trafficDevice.clear_statistics_and_filters(rx_port)
        frames = helper.get_all_captured_frames(rx_port)
        print("" +tx_port +" had " + str(len(frames)) + " packets captured")

    def test_multiple_streams_and_modify_capture(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_ethernet2()
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)

        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        trafficDevice.configure_streams_using_packets(tx_port, packets)

        print("Copy packet 5's setting to stream 3")
        trafficDevice.modify_stream_using_packet(tx_port, 3, packets[5])
        print("start capture on port " +rx_port +"\n")
        trafficDevice.start_capture(rx_port)
        print("start traffic on port " +tx_port +"\n")
        trafficDevice.start_traffic(tx_port)
        print("sleep for 5 seconds\n")
        time.sleep(15)
        print("stop traffic on port " +tx_port +"\n")
        trafficDevice.stop_traffic(tx_port)
        print("stop capture on port " +rx_port +"\n")
        trafficDevice.stop_capture(rx_port)
        print("get some port capture stats " +tx_port +" and " +rx_port)
        helper = trafficDevice.get_capture_helper()
        frames = helper.get_all_captured_frames(rx_port)
        print("" +rx_port +" had " + str(len(frames)) + " packets captured")
        print("" +rx_port +" clear buffers")
        trafficDevice.clear_capture_buffer(device_object.rx_port)
        frames = helper.get_all_captured_frames(rx_port)
        print("" +rx_port +" had " + str(len(frames)) + " packets captured")

        print("" +rx_port +" clear statistics and filters and buffers")
        trafficDevice.clear_statistics_and_filters(rx_port)
        frames = helper.get_all_captured_frames(rx_port)
        print("" +tx_port +" had " + str(len(frames)) + " packets captured")

    def test_stream_increamenting_payload_packetsetting(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

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
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_SINGLE_BURST # constant value
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
            elif isinstance(packet, IpV4PacketHeader):
                assert isinstance(packet, IpV4PacketHeader)
                packet.set_destination_ip_mode(TrafficConfigConstants.IP_DST_MODE_INCREMENT)
                packet.set_destination_ip_count(10)
                packet.set_destination_ip_mask("255.255.255.0")
                packet.set_source_ip_mode(TrafficConfigConstants.IP_SRC_MODE_DECREMENT)
                packet.set_source_ip_count(4)
                packet.set_source_ip_mask("10")

            trafficDevice.configure_stream_using_packet(tx_port, stream_id, packet, options=opt_dict)
            trafficDevice.configure_stream_using_packet(tx_port, stream_id +1, packet, options=opt_dict)
            trafficDevice.configure_stream_using_packet(tx_port, stream_id +2, packet, options=opt_dict)
            trafficDevice.configure_stream_using_packet(tx_port, stream_id +3, packet, options=opt_dict)
            # opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            trafficDevice.configure_stream_using_packet(tx_port, stream_id +4, packet, options=opt_dict)

            print("stream count = " + str(trafficDevice.get_stream_count(tx_port)))
            print("get all streams:")
            streams = trafficDevice.get_all_stream(tx_port)
            print("Is Port Continuously transmitting?" + str(trafficDevice.is_port_continuous(tx_port)))

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
            print(trafficDevice.get_filtered_captured_frames_report(rx_port))
            if frame:
                print("compare = " + str(packet.compare_packet_fields(frame)))
            print("Printing out all the streams:")
            streams = trafficDevice.get_all_stream(tx_port)
            for stream in streams:
                print(stream)
            if len(streams) != 1:
                print("Error")

    def test_only_set_packet_fields(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        trafficDevice.tgen_debug = True

        packets = PacketClassifier.get_one_of_every_packet()
        one_of_each = []
        for packet in packets:
            packet.set_destination_mac("00:33:22:33:44:55")
            packet.set_source_mac("00:33:22:33:44:66")
            tags = packet.get_packet_tags()
            if not isinstance(packet, VlanStackPacketHeader) or not isinstance(packet, IpV4PacketHeader):
                continue
            if PacketTagConstants.TAG_QTAGGED in tags or isinstance(packet, TaggedPacketHeader):
                packet.set_vlan_id(44)
                packet.set_vlan_tci(3)
            if PacketTagConstants.TAG_ENET2 in tags or isinstance(packet, Ethernet2PacketHeader):
                pass
            if PacketTagConstants.TAG_IPV4 in tags or isinstance(packet, IpV4PacketHeader):
                packet.set_destination_ip("1.1.1.1")
                packet.set_source_ip("2.2.2.2")
                packet.set_ip_tos(255)
                packet.set_ip_ttl(250)
                packet.set_ip_fragment_offset("2")
                packet.set_ip_flags_dont_frag()
                packet.set_ip_flags_more_frag()
            if PacketTagConstants.TAG_IPV6 in tags or isinstance(packet, IpV6PacketHeader):
                packet.set_ipv6_destination_address("FF00::dddd")
                packet.set_ipv6_source_address("FF00::dddd")
            if PacketTagConstants.TAG_TCP in tags or isinstance(packet, TcpPacketHeader):
                packet.set_destination_port("44")
                packet.set_source_port("33")
            if PacketTagConstants.TAG_UDP in tags or isinstance(packet, UdpPacketHeader):
                packet.set_destination_port("0x66")
                packet.set_source_port("55")
            if PacketTagConstants.TAG_IPX in tags or isinstance(packet, IpxPacketHeader):
                print("Ipx")
            if isinstance(packet, VlanStackPacketHeader):
                num = packet.get_vlan_num()
                index = 1
                for index in range(1, num + 1):
                    packet.set_vlan_protocol_id(index, "0x9100")
                    packet.set_vlan_id(index, 10 + index)
                    packet.set_vlan_tci(index, index)
                    index += 1
            if isinstance(packet, Ethernet2Packet):
                packet.set_ether_type("0x0800")
            print("set ip stream id 1 on port " +device_object.tx_port + "\n")

            if (PacketTagConstants.TAG_IPV6 in tags or isinstance(packet, IpV6PacketHeader))  and (isinstance(packet, TcpPacketHeader) or isinstance(packet, UdpPacketHeader)):
                print("blah")
            packet.set_length(124)
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            trafficDevice.configure_stream_using_packet(tx_port, 1, packet, options=opt_dict)
            trafficDevice.get_traffic_helper().configure_stream_mac_dst_options(tx_port, 1, None,
                                                                                TrafficConfigConstants.MAC_DST_MODE_INCREMENT,
                                                                                11, 10, None)
            trafficDevice.get_traffic_helper().configure_stream_mac_src_options(tx_port, 1, None,
                                                                                TrafficConfigConstants.MAC_SRC_MODE_DECREMENT,
                                                                                4, 44, None)
            if isinstance(packet, IpV4PacketHeader):
                trafficDevice.get_traffic_helper().configure_stream_ip_dst_options(tx_port, 1, "3.3.3.3",
                                                                                   TrafficConfigConstants.IP_DST_MODE_INCREMENT,
                                                                                   4, "1.1.1.1")
                trafficDevice.get_traffic_helper().configure_stream_ip_src_options(tx_port, 1, "2.2.2.2",
                                                                                   TrafficConfigConstants.IP_SRC_MODE_DECREMENT,
                                                                                   4, "1.1.1.1")
            if isinstance(packet, IpV6PacketHeader):
                trafficDevice.get_traffic_helper().configure_stream_ipv6_dst_options(tx_port, 1, "FFFF::0001",
                                                                                     TrafficConfigConstants.IPV6_DST_MODE_INCREMENT,
                                                                                     4, "0001::0001")
                trafficDevice.get_traffic_helper().configure_stream_ipv6_src_options(tx_port, 1, "FFFE::0001",
                                                                                     TrafficConfigConstants.IPV6_SRC_MODE_DECREMENT,
                                                                                     4, "0002::0001")
            print("start capture on port " +device_object.rx_port + "\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +device_object.tx_port + "\n")
            trafficDevice.start_traffic(tx_port)
            print("sleep for 5 seconds\n")
            time.sleep(15)
            print("stop traffic on port " +device_object.tx_port + "\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +device_object.rx_port + "\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +device_object.tx_port + " and " +device_object.rx_port + "")
            helper = trafficDevice.get_capture_helper()
            frames = helper.get_all_captured_frames(rx_port)
            print("" +device_object.rx_port + " had " + str(len(frames)) + " packets captured")
            print("Original Packet: ")
            print(packet.to_packet_string())
            print("here is packet #2")
            if len(frames) >= 2:
                print(frames[2].to_packet_string())
                res = packet.compare_packet_fields(frames[2], [EthernetPacketConstants.ETHER_DESTINATION_ADDRESS], PacketConstants.PRINT_FLAG_EVERYTHING)
                print("The compare came back with " + str(res))
                res = packet.compare_packet_fields(frames[2], [EthernetPacketConstants.ETHER_DESTINATION_ADDRESS], PacketConstants.PRINT_FLAG_ERRORS)
                print("The compare came back with " + str(res))
                res = packet.compare_packet_fields(frames[2], [EthernetPacketConstants.ETHER_DESTINATION_ADDRESS])
                print("The compare came back with " + str(res))
                res = packet.compare_packet_fields(frames[2], [EthernetPacketConstants.ETHER_DESTINATION_ADDRESS, EthernetPacketConstants.ETHER_SOURCE_ADDRESS])
                print("The compare came back with " + str(res))
                one_of_each.append(frames[2])
            print("" +device_object.rx_port + " clear buffers")
            trafficDevice.clear_capture_buffer(device_object.rx_port)
            frames = helper.get_all_captured_frames(rx_port)
            print("" +device_object.rx_port + " had " + str(len(frames)) + " packets captured")

            print("" +device_object.rx_port + " clear statistics and filters and buffers")
            trafficDevice.clear_statistics_and_filters(rx_port)
            frames = helper.get_all_captured_frames(rx_port)
            print("" +device_object.tx_port + " had " + str(len(frames)) + " packets captured")
        for packet in one_of_each:
            print("===" * 20)
            print(packet.to_packet_string())
        print("0000" * 20)

    def test_main_capture_transmit_wait(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_packet("ICMP")
        one_of_each = []
        trafficDevice.tgen_debug = True
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            packet.set_ip_protocol(0xFF)
            print("set ip stream id 1 on port " +device_object.tx_port + "\n")
            packet.set_length(124)
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
            opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
            print("CONFIGURING PACKET\n" + str(packet))
            trafficDevice.configure_stream_using_packet(device_object.tx_port, 1, packet, options=opt_dict)
            print("start capture on port " +device_object.rx_port + "\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +device_object.tx_port + "\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("duplex " + tx_port + " = " + str(trafficDevice.get_port_duplex(tx_port)))
            print("speed " + tx_port + " = " + str(trafficDevice.get_port_speed(tx_port)))
            print("link " + tx_port + " = " + str(trafficDevice.has_link(tx_port)))


            print("sleep for 5 seconds\n")
            time.sleep(2)
            helper = trafficDevice.get_statistic_helper()
            print("rx frame count " + tx_port + " = " + str(helper.get_port_rx_frame_count(tx_port)))
            print("tx frame count " + tx_port + " = " + str(helper.get_port_tx_frame_count(tx_port)))
            print("rx collisions count " + tx_port + " = " + str(helper.get_port_rx_collisions_count(tx_port)))
            print("late collisions count " + tx_port + " = " + str(helper.get_port_late_collisions_count(tx_port)))
            print("total collision count " + tx_port + " = " + str(helper.get_port_total_collisions_count(tx_port)))
            print("fcs error count " + tx_port + " = " + str(helper.get_port_fcs_errors_count(tx_port)))

            helper.get_port_statistic_capture_filter_count(rx_port)
            helper.get_port_statistic_capture_filter_rate(rx_port)
            helper.get_port_statistic_capture_trigger_count(rx_port)
            helper.get_port_statistic_capture_trigger_rate(rx_port)

            print("stop traffic on port " +device_object.tx_port + "\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +device_object.rx_port + "\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +device_object.tx_port + " and " +device_object.rx_port + "")
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + helper.get_captured_frame_count(device_object.rx_port))

            frames = helper.get_all_captured_frames(device_object.rx_port)
            print("" +device_object.rx_port + " had " + str(len(frames)) + " packets captured")
            print("here is packet #2")
            if len (frames) >= 2:
                print(frames[2].to_packet_string())

                one_of_each.append(frames[2])
            print("getting a single frame")
            print(helper.get_captured_frame(device_object.rx_port, 2))
            print("getting a 5 frames")
            frames = helper.get_captured_frames(device_object.rx_port, 2, 7)
            if len (frames) >= 2:
                print(frames[2].to_packet_string())
                frames[2].get_length()
                one_of_each.append(frames[2])
            print("" +device_object.rx_port + " clear buffers")
            trafficDevice.clear_capture_buffer(device_object.rx_port)
            frames = helper.get_all_captured_frames(device_object.rx_port)
            print("" +device_object.rx_port + " had " + str(len(frames)) + " packets captured")

            print("" +device_object.rx_port + " clear statistics and filters and buffers")
            trafficDevice.clear_statistics_and_filters(device_object.rx_port)
            frames = helper.get_all_captured_frames(device_object.rx_port)
            print(device_object.tx_port + " had " + str(len(frames)) + " packets captured")
            trafficDevice.clear_all_streams(tx_port)
        for packet in one_of_each:
            print("===" * 20)
            print(packet.to_packet_string())
        print("0000" * 20)

    def test_stream_gets(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_packet()
        one_of_each = []
        trafficDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            length = packet.get_header_length()
            packet.set_length(max(length +4, 64))
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
            stream_id += 1

    def test_clear_all_streams(self):
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        port_send = device_object.tx_port
        port_rec  = device_object.rx_port

        trafficDevice.clear_all_streams(port_send)
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
                trafficDevice.configure_stream_using_packet(port_send, index, packet, options=opt_dict)
                index += 1
        except:
            print("Error on packet" + str(packet))
        created_streams_count = trafficDevice.get_stream_count(port_send)
        if created_streams_count == len(packets):
            print("PASSED: Stream count = " + str(created_streams_count))
        else:
            print("Failed expected " + str(created_streams_count) + " received " + str(len(packets)))
        streams = trafficDevice.get_all_stream(port_send)
        print(str(streams))
        print(str(streams[0]))
        print("is stream enabled" + str(trafficDevice.is_stream_enabled(port_send, 1)))
        trafficDevice.set_stream_enabled(port_send, 1, False)
        print("is stream enabled" + str(trafficDevice.is_stream_enabled(port_send, 1)))
        trafficDevice.set_stream_enabled(port_send, 1, True)
        print("is stream enabled" + str(trafficDevice.is_stream_enabled(port_send, 1)))
        print("Stream count " + str(created_streams_count))
        print("clear_statistics_and_filters(" + port_send +")")
        trafficDevice.clear_statistics_and_filters(port_send)
        print("Capture Buffer Count " + str(trafficDevice.get_port_tx_frame_count(port_send)))
        print("Starting off tx count: " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        trafficDevice.start_traffic(port_send)
        trafficDevice.start_capture(port_rec)
        time.sleep(1)
        trafficDevice.stop_traffic(port_send)
        trafficDevice.stop_capture(port_rec)
        print("Capture Buffer Count " + str(trafficDevice.get_port_tx_frame_count(port_send))+ " after")
        print("Number of captured packets in the buffer is: " + str(trafficDevice.get_port_capture_num_frames(port_rec)))
        trafficDevice.clear_all_streams(port_send)
        if (opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD] * len(packets)) == trafficDevice.get_port_tx_frame_count(port_rec):
            print("PASSED: stream test streams tx count = " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        else:
            print("FAILED: stream test streams tx count = " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        if trafficDevice.get_port_tx_frame_count(port_rec) > 0:
            packets = trafficDevice.get_all_captured_frames(port_rec)
            p = None
            for p in packets:
                print(str(p))
        print("clear_statistics_and_filters(" + port_send +")")
        trafficDevice.clear_statistics_and_filters(port_send)
        print("Capture Buffer Count " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        print("Stream count " + str(trafficDevice.get_stream_count(port_send)))
        if 0 == trafficDevice.get_port_tx_frame_count(port_rec):
            print("PASSED: stream test streams tx count = 0")
        else:
            print("FAILED: stream test streams tx count = " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        print("************\nNo streams, no packets")
        print("Starting off tx count: " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        trafficDevice.start_traffic(port_send)
        trafficDevice.start_capture(port_rec)
        time.sleep(1)
        trafficDevice.stop_traffic(port_send)
        trafficDevice.stop_capture(port_rec)
        created_streams_count = trafficDevice.get_stream_count(port_send)
        if created_streams_count == 0:
            print("PASSED: Stream count = 0")
        else:
            print("FAILED: expected " + created_streams_count + " received " + len(packets))
        print("Stream count " + str(created_streams_count))
        print("After clearing streams: " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        if trafficDevice.get_port_tx_frame_count(port_rec) > 0:
            packets = trafficDevice.get_all_captured_frames(port_rec)
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
        trafficDevice.configure_stream_using_packet(port_send, 1, packet, options=opt_dict)
        print("Stream count " + str(trafficDevice.get_stream_count(port_send)))
        print("clear_statistics_and_filters(" + port_send +")")
        trafficDevice.clear_statistics_and_filters(port_send)
        print("Capture Buffer Count " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        print("Starting off tx count: " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        trafficDevice.start_traffic(port_send)
        trafficDevice.start_capture(port_rec)
        time.sleep(1)
        trafficDevice.stop_traffic(port_send)
        trafficDevice.stop_capture(port_rec)
        trafficDevice.clear_all_streams(port_send)
        if opt_dict[TrafficGenerationConstants.NUMBER_OF_PACKETS_CMD] == trafficDevice.get_port_tx_frame_count(port_rec):
            print("PASSED: stream test streams tx count = " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        else:
            print("FAILED: stream test streams tx count = " + str(trafficDevice.get_port_tx_frame_count(port_rec)))
        if trafficDevice.get_port_tx_frame_count(port_rec) > 0:
            packets = trafficDevice.get_all_captured_frames(port_rec)
            p = None
            for p in packets:
                str(p)
        trafficDevice.disconnect()
        print("End Test Case")
        print("++++++++++++++++++++++++++++++")

    def test_stream_length_check(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_packet()
        one_of_each = []
        trafficDevice.tgen_debug = True
        stream_id = 1
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            length = packet.get_header_length()
            packet.auto_set_minimum_length()
            print("packet length is auto set to " + packet.get_length())
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
            print("start capture on port " +device_object.rx_port + "\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +device_object.tx_port + "\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("sleep for 5 seconds\n")
            time.sleep(2)
            print("stop traffic on port " +device_object.tx_port + "\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +device_object.rx_port + "\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +device_object.tx_port + " and " +device_object.rx_port + "")
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + helper.get_captured_frame_count(device_object.rx_port))
            frames = helper.get_all_captured_frames(device_object.rx_port)
            for frame in frames:
                print(str(frame))
            if frame:
                packet.set_destination_mac("FF:FF:FF:FF:FF:FF", True)
                print(packet.compare_packet_fields(frame))
                print("Don't check only Ether destination address ")
                print(packet.compare_packet_fields(frame, [EthernetPacketConstants.ETHER_DESTINATION_ADDRESS]))
                print("Check only Ether destination address ")
                print(packet.compare_packet_fields(frame, None, [EthernetPacketConstants.ETHER_DESTINATION_ADDRESS]))
                packet.set_destination_mac("FF:FF:FF:FF:FF:FF")
                print(packet.compare_packet_fields(frame))
                print("Don't check only Ether destination address ")
                print(packet.compare_packet_fields(frame, [EthernetPacketConstants.ETHER_DESTINATION_ADDRESS]))
                print("Check only Ether destination address ")
                print(packet.compare_packet_fields(frame, None, [EthernetPacketConstants.ETHER_DESTINATION_ADDRESS]))

    def test_stream_stp_payload(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        trafficDevice.clear_all_streams(tx_port)

        packets = PacketClassifier.get_one_of_every_llc_stp()
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
            print("start capture on port " +device_object.rx_port + "\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +device_object.tx_port + "\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("sleep for 5 seconds\n")
            time.sleep(2)
            print("stop traffic on port " +device_object.tx_port + "\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +device_object.rx_port + "\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +device_object.tx_port + " and " +device_object.rx_port + "")
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + helper.get_captured_frame_count(device_object.rx_port))
            frames = helper.get_all_captured_frames(device_object.rx_port)
            for frame in frames:
                print(str(frame))
            if frame:
                print(packet.compare_packet_fields(frame))

    def test_stream_lldp_payload(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

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
            print("start capture on port " +device_object.rx_port + "\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +device_object.tx_port + "\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("sleep for 5 seconds\n")
            time.sleep(2)
            print("stop traffic on port " +device_object.tx_port + "\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +device_object.rx_port + "\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +device_object.tx_port + " and " +device_object.rx_port + "")
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + helper.get_captured_frame_count(device_object.rx_port))
            frames = helper.get_all_captured_frames(device_object.rx_port)
            for frame in frames:
                print(str(frame))
            if frame:
                print("compare = " + str(packet.compare_packet_fields(frame)))

    def test_qos_mode(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        trafficDevice.set_qos_mode(tx_port)
        trafficDevice.enable_qos_stats(tx_port, False)
        trafficDevice.disconnect()

        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

    def test_empty_template_step(self):  # test out the packet capture with all packets.
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        packets = PacketClassifier.get_one_of_every_packet("ARP")
        one_of_each = []
        trafficDevice.tgen_debug = True
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            print(str(packet))
            print("set ip stream id 1 on port " +device_object.tx_port + "\n")
            opt_dict = dict()
            opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
            opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS_BURST # constant value
            opt_dict[TrafficConfigConstants.MAC_DST_COUNT_CMD] = 10
            opt_dict[TrafficConfigConstants.MAC_DST_STEP_CMD] = 1
            print("CONFIGURING PACKET\n" + str(packet))
            trafficDevice.configure_stream_using_packet(device_object.tx_port, 1, packet, options=opt_dict)
            print("start capture on port " +device_object.rx_port + "\n")
            trafficDevice.start_capture(rx_port)
            print("start traffic on port " +device_object.tx_port + "\n")
            trafficDevice.start_traffic_and_wait(tx_port, 2000)
            print("sleep for 5 seconds\n")
            time.sleep(2)
            print("stop traffic on port " +device_object.tx_port + "\n")
            trafficDevice.stop_traffic(tx_port)
            print("stop capture on port " +device_object.rx_port + "\n")
            trafficDevice.stop_capture(rx_port)
            print("get some port capture stats " +device_object.tx_port + " and " +device_object.rx_port + "")
            helper = trafficDevice.get_capture_helper()
            print("get capture count " + helper.get_captured_frame_count(device_object.rx_port))
            frames = helper.get_all_captured_frames(device_object.rx_port)
            for frame in frames:
                print(str(frame))

    def test_main(self):
        trafficDevice = device_object.connect_and_take_ports()
        if not trafficDevice:
            print("ERROR!!!! Device not connected!!!!")
            return
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port

        print("set ip stream id 1 on port " +device_object.tx_port + "\n")
        packet = Ethernet2TcpIpV4Packet()
        packet.set_destination_mac("00:00:00:00:00:11")
        packet.set_source_mac("00:00:00:00:00:22")
        packet.set_destination_ip("1.1.1.1")
        packet.set_source_ip("3.3.3.3")
        opt_dict = dict()
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 10
        opt_dict[TrafficConfigConstants.TRANSMIT_MODE_CMD] = TrafficConfigConstants.TRANSMIT_MODE_CONTINUOUS # constant value
        trafficDevice.configure_stream_using_packet(device_object.tx_port, 1, packet, options=opt_dict)
        trafficDevice.configure_stream_using_packet(device_object.tx_port, 1, packet, options=opt_dict)
        packet = Ethernet2IpV4Packet()
        packet.set_destination_mac("00:00:00:00:00:11")
        packet.set_source_mac("00:00:00:00:00:33")
        packet.set_source_ip("3.3.3.3")
        print("set ip stream id 2 on port " +device_object.tx_port + "\n")
        trafficDevice.configure_stream_using_packet(device_object.tx_port, 2, packet, options=opt_dict)
        trafficDevice.get_statistic_helper().get_port_statistic_rx_raw_pkt_count(rx_port)

        print("set ip stream id 1 on port " +device_object.rx_port + "\n")
        packet = Ethernet2IpV4TaggedPacket()
        packet.set_destination_mac("00:00:00:00:00:22")
        packet.set_source_mac("00:00:00:00:00:11")
        packet.set_destination_ip("2.2.2.2")
        packet.set_source_ip("1.1.1.1")
        packet.set_vlan_id(555)
        packet.set_vlan_tci(3)
        opt_dict[TrafficConfigConstants.RATE_PPS_CMD] = 5
        trafficDevice.configure_stream_using_packet(device_object.rx_port, 1, packet, options=opt_dict)

        for item in [1, 2, 3, 4]:
            trafficDevice.tgen_debug = False
            print("clear the statics of ports " +device_object.tx_port + " and " +device_object.rx_port + "\n")
            trafficDevice.clear_statistics_and_filters(tx_port)
            trafficDevice.clear_statistics_and_filters(rx_port)
            helper = trafficDevice.get_statistic_helper()
            if isinstance(device_object, IxiaDeviceUnitTestObject):
                print("tx_port raw tx pkt count: " +  helper.get_port_statistic_tx_raw_pkt_count(tx_port))
                print("tx_port raw rx pkt count: " +  helper.get_port_statistic_rx_raw_pkt_count(tx_port))
                print("rx_port raw tx pkt count: " +  helper.get_port_statistic_tx_raw_pkt_count(rx_port))
                print("rx_port raw tx pkt count: " +  helper.get_port_statistic_rx_raw_pkt_count(rx_port))
            else:
                print("Unsupported on this device raw tx")
            print("start capture on port " +device_object.rx_port + "")
            # Put in to your unit test
            trafficDevice.start_capture(rx_port)
            print("sleep for 5 seconds\n")
            time.sleep(5)

            print("start traffic on port " +device_object.tx_port + "\n")
            trafficDevice.start_traffic(tx_port)

            print("start traffic on port " +device_object.rx_port + "\n")
            trafficDevice.start_traffic(rx_port)

            print("sleep for " +str(5 * item) +" seconds\n")
            time.sleep(5 * item)

            print("stop capture on port " +device_object.tx_port + " and " +device_object.rx_port + "")
            # Put in to your unit test
            trafficDevice.stop_capture(device_object.tx_port)
            trafficDevice.stop_capture(device_object.rx_port)

            print("sleep for 5 seconds\n")
            time.sleep(5)

            print("stop traffic on port " +device_object.tx_port + "\n")
            trafficDevice.stop_traffic(device_object.tx_port)

            print("stop traffic on port " +device_object.rx_port + "\n")
            trafficDevice.stop_traffic(device_object.rx_port)

            print("get some port stats " +device_object.tx_port + " and " +device_object.rx_port + "")
            helper = trafficDevice.get_statistic_helper()
            if isinstance(device_object, IxiaDeviceUnitTestObject):
                print("tx_port raw tx pkt count: " +  helper.get_port_statistic_tx_raw_pkt_count(tx_port))
                print("tx_port raw rx pkt count: " +  helper.get_port_statistic_rx_raw_pkt_count(tx_port))
                print("rx_port raw tx pkt count: " +  helper.get_port_statistic_tx_raw_pkt_count(rx_port))
                print("rx_port raw tx pkt count: " +  helper.get_port_statistic_rx_raw_pkt_count(rx_port))
            else:
                print("Unsupported on this device raw tx")

        print("get some port capture stats " +device_object.tx_port + " and " +device_object.rx_port + "")
        helper = trafficDevice.get_capture_helper()
        frames = helper.get_all_captured_frames(device_object.tx_port)
        print("" +device_object.tx_port + " had " + str(len(frames)) + " packets captured")
        print("here is packet #2")
        if len (frames) >= 2:
            print(frames[2].to_packet_string())
        print("" +device_object.tx_port + " clear buffers")
        trafficDevice.clear_capture_buffer(device_object.tx_port)
        print("" +device_object.tx_port + " had " + str(len(frames)) + " packets captured")
        frames = helper.get_all_captured_frames(device_object.tx_port)
        print("" +device_object.tx_port + " clear statistics and filters and buffers")
        trafficDevice.clear_statistics_and_filters(device_object.tx_port)
        print("" +device_object.tx_port + " had " + str(len(frames)) + " packets captured")
        print("here is packet #2")
        if len (frames) >= 2:
            print(frames[2].to_packet_string())
        frames = helper.get_all_captured_frames(device_object.rx_port)
        print("" +device_object.rx_port + " had " + str(len(frames)) + " packets captured")
        print("here is packet #2")
        if len (frames) >= 2:
            print(frames[2].to_packet_string())

        num_frames = helper.get_port_capture_num_frames(device_object.tx_port)
        print("" +device_object.tx_port + " total captured frames: " + str(num_frames))

        print("" +device_object.rx_port + " total captured frame 1 " + str(helper.get_port_capture_frame_frame_data_string(device_object.rx_port, 1)))

        print("test creating an interface\n")
        if isinstance(device_object, IxiaDeviceUnitTestObject):
            api = trafficDevice.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
            assert isinstance(api, InterfaceConfigApi)

            opt_dict = dict()
            opt_dict[InterfaceConfigConstants.AUTONEGOTIATION_CMD] = 0 # static value
            opt_dict[InterfaceConfigConstants.INTF_IP_ADDR_CMD] = "1.1.1.1" # static value
            opt_dict[InterfaceConfigConstants.NETMASK_CMD] = "0.0.0.0" # static value
            opt_dict[InterfaceConfigConstants.MODE_CMD] = InterfaceConfigConstants.MODE_CONFIG # constant value
            opt_dict[InterfaceConfigConstants.PORT_HANDLE_CMD] = device_object.tx_port # static value
            api.interface_config(opt_dict)
        else:
            print("Unsupported on this device")

    def testing_jakes_thing(self):
        logger = Logger()
        logger.console_level = Logger.ALL

        tgen_con = TrafficGeneratorConnectionManager()
        tgen_port = TrafficPortKeywords()
        traffic_create = TrafficPacketCreationKeywords()
        traffic_stream = TrafficStreamConfigurationKeywords()

        port_1 = ["ixia", device_object.tx_port]
        port_2 = ["ixia", device_object.rx_port]

        port_list = [port_1, port_2]

        tgen_con.connect_to_traffic_generator("ixia", "ixia", "10.52.2.189", "10.52.2.60", "jhall-robot", "5678")

        tgen_port.reset_port_to_factory_defaults(port_list)
        traffic_stream.remove_all_streams_from_port(port_list)

        traffic_create.create_packet("packet", PacketTypeConstants.ETH2_IPV4_PACKET)
        traffic_create.set_ethernet2("packet", "00:ab:ad:ca:fe:11", "00:ab:ad:ca:fe:22", "0xFFFF")
        traffic_create.set_ipv4("packet", "22.22.22.1", "11.11.11.1")

        traffic_stream.configure_stream_packet(port_1, "1", "packet")
        traffic_stream.configure_stream_count(port_1, "1", "1000")
        traffic_stream.configure_stream_mode_single_burst(port_1, "1")
        traffic_stream.configure_stream_rate(port_1, "1", "10")
        traffic_stream.configure_stream_unit(port_1, "1", "%")
        traffic_stream.configure_stream_ip_dst_mode_increment(port_1, "1", "10")#, "255.255.255.0")
        traffic_stream.configure_stream_ip_src_mode_increment(port_1, "1", "10")#, "255.255.255.0")
        traffic_stream.add_stream_to_port(port_1, "1")


if __name__ == '__main__':
    unittest.main()
