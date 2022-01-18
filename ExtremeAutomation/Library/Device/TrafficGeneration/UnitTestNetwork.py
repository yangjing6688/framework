import time
import unittest

from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import InterfaceConfigApi, InterfaceConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import \
    PacketConfigTriggersConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDevice import IxiaDevice
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
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxNetworkDevice import IxNetworkDevice
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpConfig import EmulationBgpConfigApi, EmulationBgpConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpRouteConfigApi import EmulationBgpRouteConfigApi, EmulationBgpRouteConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpControlApi import EmulationBgpControlApi, EmulationBgpControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpConfigApi import EmulationBgpConfigConstants, EmulationBgpConfigApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpInfoApi import EmulationBgpInfoApi, EmulationBgpInfoConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficGeneratorConnectionManager import TrafficGeneratorConnectionManager
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPortKeywords import TrafficPortKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketCreationKeywords import TrafficPacketCreationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.Constants.PacketTypeConstants import PacketTypeConstants
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStreamConfigurationKeywords import TrafficStreamConfigurationKeywords
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingDhcpApi import NetworkEmulatingDhcpApi, NetworkEmulatingDhcpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceUnitTestObject import IxiaDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.SpirentDeviceUnitTestObject import SpirentDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.OstinatoDeviceUnitTestObject import OstinatoDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceUnitTestObject import JetsDeviceUnitTestObject
from ExtremeAutomation.Library.Device.TrafficGeneration.NetworkEmulatingDevice import NetworkEmulatingDevice
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

from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


#device_object = IxiaDeviceUnitTestObject()
#device_object = SpirentDeviceUnitTestObject()
#device_object = OstinatoDeviceUnitTestObject()
device_object = JetsDeviceUnitTestObject()


class TestStringMethods(unittest.TestCase):

    def test_tcp_ping(self):
        trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
        assert isinstance(trafficDevice,NetworkEmulatingDevice)
        tx_port = device_object.tx_port
        rx_port = device_object.rx_port
        print("Start port capturing")
        trafficDevice.start_capture(rx_port)

        tcp_api = trafficDevice.get_api(NetworkEmulatingTcpConstants.TCP_API)
        assert isinstance(tcp_api, NetworkEmulatingTcpApi)

        print("Create 1 TCP Stacks on each port:")
        tcp_api.create_tcp_stack(tx_port, "10.10.10.10", "255.255.255.0", "10.10.10.1", "00:33:22:33:44:55")
        tcp_api.create_tcp_stack(rx_port, "10.10.10.11", "255.255.255.0", "10.10.10.1", "00:33:22:33:44:56")

        print("Test ping:")
        trafficDevice.ping(tx_port, "10.10.10.10", "10.10.10.11")
        trafficDevice.ping(rx_port, "10.10.10.11", "10.10.10.10")

        print("Stop port capturing and print received packets:")
        trafficDevice.stop_capture(rx_port)
        frames = trafficDevice.get_all_captured_frames(rx_port)
        for frame in frames:
            print("RECEIVED PACKET:")
            print(str(frame))
            print("-*-" * 20)
        pass

    def test_jets_igmp_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True
            bridge_a_port = device_object.tx_port
            bridge_b_port = device_object.rx_port

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)

            api = trafficDevice.get_api(NetworkEmulatingIgmpConstants.IGMP_API)
            assert isinstance(api,NetworkEmulatingIgmpApi)
            trafficDevice.start_capture(bridge_b_port)

            print("Creating igmp host on port " + str(bridge_a_port))
            api.create_igmp_host(bridge_a_port, "16.1.1.1", "255.255.255.0", "16.1.1.6", "0.0.11.11.16.01")
            print("Creating igmp host on port " + str(bridge_b_port))
            api.create_igmp_host(bridge_b_port, "16.1.1.2", "255.255.255.0", "16.1.1.6", "0.0.11.11.16.02")
            time.sleep(5)

            print("Generate igmp joins on port " + str(bridge_a_port))
            api.generate_igmp_join(bridge_a_port, "16.1.1.1", "225.1.1.1")
            api.generate_igmp_join(bridge_a_port, "16.1.1.1", "226.1.1.1")
            time.sleep(5)

            print("Generate igmp leaves on port " + str(bridge_a_port))
            api.generate_igmp_leave(bridge_a_port, "16.1.1.1", "225.1.1.1")
            api.generate_igmp_leave(bridge_a_port, "16.1.1.1", "226.1.1.1")
            time.sleep(5)

            trafficDevice.stop_capture(bridge_b_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_b_port))
            trafficDevice.disconnect()
        except Exception as e:
            print(StringUtils.exception_to_string(e))


    def test_jets_dhcp_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True
            bridge_a_port = device_object.tx_port

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            api = trafficDevice.get_api(NetworkEmulatingDhcpConstants.DHCP_API)
            assert isinstance(api,NetworkEmulatingDhcpApi)
            trafficDevice.start_capture(bridge_a_port)

            api.create_dhcp_client(bridge_a_port, "00:44:55:66:77:88", "255.255.0.0", count=4, step=5)
            api.start_dhcp_client(bridge_a_port, "00:44:55:66:77:88", "255.255.0.0", count=4, step=5)

            api.wait_for_dhcp_client_address(bridge_a_port, "00:44:55:66:77:88")

            api.get_dhcp_client_address(bridge_a_port, "00:44:55:66:77:88")
            api.get_dhcp_client_address(bridge_a_port, "00:44:55:66:77:92")
            api.create_dhcp_client(bridge_a_port, "00:44:55:66:77:88", "255.255.0.0", count=4, step=5)
            api.remove_dhcp_client(bridge_a_port, "00:44:55:66:77:88", "255.255.0.0", count=4, step=5)
            api.create_dhcp_client(bridge_a_port, "00:44:55:66:77:88", "255.255.0.0", count=4, step=5)



            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))
            trafficDevice.disconnect()
        except Exception as e:
            print(StringUtils.exception_to_string(e))

    def test_dvr_isis_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            spbm_api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            route_api = trafficDevice.get_api(NetworkEmulatingRouteConstants.ROUTE_API)
            end_station_api = trafficDevice.get_api(NetworkEmulatingEndstationConstants.END_STATION_API)
            lldp_api = trafficDevice.get_api(NetworkEmulatingLldpConstants.LLDP_API)
            dvr_api = trafficDevice.get_api(NetworkEmulatingDvrConstants.DVR_API)
            assert isinstance(spbm_api,NetworkEmulatingSpbmApi)
            assert isinstance(route_api,NetworkEmulatingRouteApi)
            assert isinstance(end_station_api,NetworkEmulatingEndstationApi)
            assert isinstance(lldp_api, NetworkEmulatingLldpApi)
            assert isinstance(dvr_api, NetworkEmulatingDvrApi)

            bridge_a_port = device_object.tx_port
            trafficDevice.start_capture(bridge_a_port)
            bridge_name_a = "EzEdgeA"
            api.create_and_go_isis_interface_dvr_controller(bridge_a_port, bridge_name_a, "00:00:00:0c:0a:01", 4051, 4052, "490000", "00:bb:30:00:00:00", 10, 3, 10, 25)
            # api.create_and_go_isis_interface(device_object.rx_port, bridge_name_b, "00:00:00:0c:0a:02", 4051, 4052, "490000", "00:00:00:0e:0a:06", 10, 3, 10)
            api.set_multicast_enabled()

            router_handle = "3.3.3.3"
            interface_address = trafficDevice.get_interface_base_address(bridge_a_port)
            lldp_api.create_and_go_lldp_interface(bridge_a_port, router_handle, "00:00:fa:fa:16:01","00:fa:fa:16:01:00", 120)


            route_api.advetise_ipv4_routes(bridge_a_port, bridge_name_a, interface_address, '255.255.255.255')
            spbm_api.create_isis_ipv4_route_stack(bridge_a_port, bridge_name_a, True,  '10.0.0.230', '255.255.255.255', interface_address,1, 1, 1)

            time.sleep(1)
            end_station_api.create_isis_endpoint(bridge_name_a, "B_host", 2002000, '00:00:00:0e:0a:0f', 2000, 0, '00:00:00:0c:0a:01', '200.200.200.1', '255.255.255.0', 1, 4051, 1, 0)

            # JETS_SIM>bridge addDvrGw -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24 -gateway 10.10.10.1 -vrfId 0 -vlan_ip_interface 10.10.10.2
            dvr_api.add_dvr_gateway(bridge_name_a, 0, 2002000, "0:0:0:0:0:0", 24, "200.200.200.200","200.200.200.202")


            # JETS_SIM>bridge addDvrRoute -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24 -network 10.10.10.0 -nexthop 10.10.10.1 -vrfId 0 -domainId 3
            # def add_dvr_route(bridge_a_port, router_handle, 0, 200200, cmac, mask_length, network_address, next_hop, domain_id)
            #dvr_api.add_dvr_route(bridge_name_a, 0, 200200, "0:0:0:0:0:0", 24, "66.66.66.0", "66.66.66.1", 25)
            dvr_api.add_dvr_route(bridge_name_a, 0, 2002000, "0:0:0:0:0:0", 24, "200.200.200.0", "200.200.200.200", 25)

            # JETS_SIM>bridge addDvrMcast -bridgeName edgeA -l3isid 0 -l2isid 999 -mcastCfg 1 -igmpVersion 2
            # def add_dvr_multicast(bridge_name_a, 0, 2002000, multicast_config, igmp_version)
            dvr_api.add_dvr_multicast(bridge_name_a, 0, 2002000, 1, 2)

            # JETS_SIM>bridge addHostBehindDvrGw -bridgeName edgeA -l3isid 0 -ipAddr 10.10.10.53 -macAddr 00:00:00:aa:aa:01 -gwAddr 10.10.10.1
            # Created DvrEp:10.10.10.53:Behind:10.10.10.1
            # def create_dvr_gw_endpoint(router_handle, 0, starting_ip, mac_address, gateway)
            dvr_api.create_dvr_gw_endpoint(bridge_name_a, 0, "200.200.200.100", "00:00:00:aa:aa:01", "200.200.200.200")

            # on the switch:
            # 200.200.200.100  00:00:00:aa:aa:01   0          2002000    0          2/15                 25         DYNAMIC    EzEdgeA
            # 200.200.200.202  00:bb:30:00:00:53   0          2002000    0          2/15                 25         DYNAMIC    EzEdgeA

            time.sleep(1)
            trafficDevice.ping(bridge_a_port, '200.200.200.1', '200.200.200.2')
            trafficDevice.ping(bridge_a_port, '200.200.200.100', '200.200.200.1')
            route_api.get_routes(bridge_a_port, "200.200.200.1")
            route_api.get_all_routes_from_interface(bridge_a_port)

            dvr_api.verify_dvr_gateway( bridge_name_a, 0, 100999,  "64:6a:52:a3:25:1", "0:bb:0:0:20:0", 24, "172.9.99.99")

            dvrlist = dvr_api.get_all_dvr_enties(bridge_name_a)

            for l in dvrlist:
                print(str(l))

            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))
            trafficDevice.disconnect()
        except Exception as e:
            print(StringUtils.exception_to_string(e))

    def test_dvr_leaf_isis_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            spbm_api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            route_api = trafficDevice.get_api(NetworkEmulatingRouteConstants.ROUTE_API)
            end_station_api = trafficDevice.get_api(NetworkEmulatingEndstationConstants.END_STATION_API)
            lldp_api = trafficDevice.get_api(NetworkEmulatingLldpConstants.LLDP_API)
            dvr_api = trafficDevice.get_api(NetworkEmulatingDvrConstants.DVR_API)
            assert isinstance(spbm_api,NetworkEmulatingSpbmApi)
            assert isinstance(route_api,NetworkEmulatingRouteApi)
            assert isinstance(end_station_api,NetworkEmulatingEndstationApi)
            assert isinstance(lldp_api, NetworkEmulatingLldpApi)
            assert isinstance(dvr_api, NetworkEmulatingDvrApi)

            bridge_a_port = device_object.tx_port
            trafficDevice.start_capture(bridge_a_port)
            bridge_name_a = "EzEdgeA"
            api.create_and_go_isis_interface_dvr_leaf(bridge_a_port, bridge_name_a, "00:00:00:0c:0a:01", 4051, 4052, "490000", "00:bb:30:00:00:00", 10, 3, 10)
            # api.create_and_go_isis_interface(device_object.rx_port, bridge_name_b, "00:00:00:0c:0a:02", 4051, 4052, "490000", "00:00:00:0e:0a:06", 10, 3, 10)

            router_handle = "3.3.3.3"
            interface_address = trafficDevice.get_interface_base_address(bridge_a_port)
            lldp_api.create_and_go_lldp_interface(bridge_a_port, router_handle, "00:00:fa:fa:16:01","00:fa:fa:16:01:00", 120)

            route_api.advetise_ipv4_routes(bridge_a_port, bridge_name_a, interface_address, '255.255.255.255')
            spbm_api.create_isis_ipv4_route_stack(bridge_a_port, bridge_name_a, True,  '10.0.0.230', '255.255.255.255', interface_address,1, 1, 1)

            time.sleep(1)
            end_station_api.create_isis_endpoint(bridge_name_a, "B_host", 2002000, '00:00:00:0e:0a:0f', 2000, 0, '00:00:00:0c:0a:01', '200.200.200.1', '255.255.255.0', 1, 4051, 1, 0)

            time.sleep(1)
            trafficDevice.ping(bridge_a_port, '200.200.200.1', '200.200.200.2')

            route_api.get_routes(bridge_a_port, "200.200.200.1")
            route_api.get_all_routes_from_interface(bridge_a_port)
            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))
            trafficDevice.disconnect()
        except Exception as e:
            print(StringUtils.exception_to_string(e))

    def test_lldp_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            lldp_api = trafficDevice.get_api(NetworkEmulatingLldpConstants.LLDP_API)
            assert isinstance(lldp_api, NetworkEmulatingLldpApi)

            bridge_a_port = device_object.tx_port
            router_handle = "3.3.3.3"
            trafficDevice.start_capture(bridge_a_port)
            # def create_vrrp_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address, vlan_id=None, advertise_interval_msecs=1000, version=2):
            lldp_api.create_and_go_lldp_interface(bridge_a_port, router_handle, "00:00:fa:fa:16:01","00:fa:fa:16:01:00", 120)
            time.sleep(10)
            lldp_api.add_lldp_tlv_dot1_vlan_name(bridge_a_port, router_handle, 666, "Dogs")
            lldp_api.send_lldp_tlv_dot1_vlan_name(bridge_a_port, router_handle)
            lldp_api.add_lldp_tlv_local_mgmt_addr(bridge_a_port, router_handle, "192.168.1.1","1/1","1.3.1.4.1.2272.1.8.2.1.2.64")
            lldp_api.send_lldp_tlv_local_mgmt_addr(bridge_a_port, router_handle)
            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))

            frames = trafficDevice.get_all_captured_frames(bridge_a_port)
            trafficDevice.save_all_captured_frames_to_pcap(bridge_a_port, "C:\\tmp\\bgp.pcap")
            for frame in frames:
                if "lldp" in frame.get_name().lower():
                    print(str(frame))
            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_vrrp_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            vrrp_api = trafficDevice.get_api(NetworkEmulatingVrrpConstants.VRRP_API)
            assert isinstance(vrrp_api, NetworkEmulatingVrrpApi)

            bridge_a_port = device_object.tx_port
            trafficDevice.start_capture(bridge_a_port)
            # def create_vrrp_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address, vlan_id=None, advertise_interval_msecs=1000, version=2):
            vrrp_api.create_and_go_vrrp_interface(bridge_a_port, "3.3.3.3", "151.1.1.3", "255.255.255.0", "151.1.1.1", "00:00:00:0e:0a:0f", "151.1.1.2", priority=50)
            time.sleep(10)
            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))

            frames = trafficDevice.get_all_captured_frames(bridge_a_port)
            trafficDevice.save_all_captured_frames_to_pcap(bridge_a_port, "C:\\tmp\\bgp.pcap")
            for frame in frames:
                if "vrrp" in frame.get_name().lower():
                    print(str(frame))
            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_bgp_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            spbm_api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            route_api = trafficDevice.get_api(NetworkEmulatingRouteConstants.ROUTE_API)
            bgp_api = trafficDevice.get_api(NetworkEmulatingBgpConstants.BGP_API)
            end_station_api =  trafficDevice.get_api(NetworkEmulatingEndstationConstants.END_STATION_API)
            assert isinstance(spbm_api, NetworkEmulatingSpbmApi)
            assert isinstance(route_api, NetworkEmulatingRouteApi)
            assert isinstance(end_station_api, NetworkEmulatingEndstationApi)
            assert isinstance(bgp_api, NetworkEmulatingBgpApi)

            bridge_a_port = device_object.tx_port
            trafficDevice.start_capture(bridge_a_port)
            # def create_bgp_interface(self, port_string, router_id, local_as, source_ip, netmask, gateway_address, mac_address, vlan_id=None, neighbor_type=None,  ip_version="IPv4", options=None):
            bgp_api.create_bgp_interface(bridge_a_port, "3.3.3.3", 6661, "151.1.1.2", "255.255.255.0",
                                           "151.1.1.1", "00:00:00:0e:0a:0f")

            # add_bgp_neighbor(self, port_string, router_id,  ip_address, netmask, local_as):
            bgp_api.add_bgp_neighbor(bridge_a_port, "3.3.3.3", "151.1.1.1", "255.255.255.0", 6660)
            time.sleep(1)
            bgp_api.get_bgp_state(bridge_a_port, "3.3.3.3")
            bgp_api.get_bgp_stats(bridge_a_port, "3.3.3.3")
            # ospf_api.delete_ospf_route(bridge_a_port, "3.3.3.3", "179.0.10.0", "255.255.255.0", 5, 1)

            # port_string, router_id, area_id, source_ip, netmask, gateway_address, mac_address, vlan_id,
            # tcpip config -device 1 -ipAddr 16.1.1.1 -netmask 255.255.255.0 -gateway 16.1.1.6 -macAddress 0.0.11.11.16.01 -state enable
            # router create simOspfRtr ospf -device 1 -routerID 3.3.3.3 -areaID 0.0.0.0 -helloInterval 10 -deadInterval 40 -retransmittal 47 -cost 1 -priority 1 -intftype standard -learn true -areatype extcapable

            index = 0
            while index < 10:
                time.sleep(1)
                bgp_api.get_bgp_state(bridge_a_port, "3.3.3.3")
                bgp_api.get_bgp_stats(bridge_a_port, "3.3.3.3")
                route_api.get_routes(bridge_a_port, "151.1.1.2")
                time.sleep(1 +index)
                index += 1

            trafficDevice.ping(bridge_a_port, '151.1.1.2', '151.1.1.1')
            # trafficDevice.ping(bridge_a_port, '16.1.1.1', '16.1.1.6')

            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))
            bgp_api.remove_bgp_router(bridge_a_port, "3.3.3.3")
            bgp_api.get_bgp_state(bridge_a_port, "3.3.3.3")

            frames = trafficDevice.get_all_captured_frames(bridge_a_port)
            trafficDevice.save_all_captured_frames_to_pcap(bridge_a_port, "C:\\tmp\\bgp.pcap")
            for frame in frames:
                if "bgp" in frame.get_name().lower():
                    print(str(frame))
            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_ospf_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            spbm_api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            route_api = trafficDevice.get_api(NetworkEmulatingRouteConstants.ROUTE_API)
            ospf_api = trafficDevice.get_api(NetworkEmulatingOspfConstants.OSPF_API)
            end_station_api=  trafficDevice.get_api(NetworkEmulatingEndstationConstants.END_STATION_API)
            assert isinstance(spbm_api,NetworkEmulatingSpbmApi)
            assert isinstance(route_api,NetworkEmulatingRouteApi)
            assert isinstance(end_station_api,NetworkEmulatingEndstationApi)
            assert isinstance(ospf_api,NetworkEmulatingOspfApi)

            bridge_a_port = device_object.tx_port
            trafficDevice.start_capture(bridge_a_port)
            # ospf_api.create_ospf_interface(bridge_a_port, "3.3.3.3", "0.0.0.0", "151.1.1.1", "255.255.255.0", "151.1.1.2", "00:00:00:0e:0a:0f")
            # ospf_api.add_ospf_route(bridge_a_port, "3.3.3.3", "177.0.10.0", "255.255.255.0", 5, 1, 100)
            # ospf_api.add_ospf_route(bridge_a_port, "3.3.3.3", "179.0.10.0", "255.255.255.0", 5, 1, 100)
            ospf_api.create_ospf_interface(bridge_a_port, "3.3.3.3", "0.0.0.0", "151.1.1.2", "255.255.255.0",
                                           "151.1.1.1", "00:00:00:0e:0a:0f")
            ospf_api.add_ospf_route(bridge_a_port, "3.3.3.3", "177.0.10.0", "255.255.255.0", 5, 1, 100,
                                    adv_rtr="3.3.3.3", forward_address="151.1.1.2")

            time.sleep(1)
            ospf_api.get_ospf_state(bridge_a_port, "3.3.3.3")
            ospf_api.get_ospf_stats(bridge_a_port, "3.3.3.3")
            # ospf_api.delete_ospf_route(bridge_a_port, "3.3.3.3", "179.0.10.0", "255.255.255.0", 5, 1)


            # port_string, router_id, area_id, source_ip, netmask, gateway_address, mac_address, vlan_id,
            # tcpip config -device 1 -ipAddr 16.1.1.1 -netmask 255.255.255.0 -gateway 16.1.1.6 -macAddress 0.0.11.11.16.01 -state enable
            # router create simOspfRtr ospf -device 1 -routerID 3.3.3.3 -areaID 0.0.0.0 -helloInterval 10 -deadInterval 40 -retransmittal 47 -cost 1 -priority 1 -intftype standard -learn true -areatype extcapable

            index = 0
            while index < 10:
                time.sleep(1)
                ospf_api.get_ospf_state(bridge_a_port, "3.3.3.3")
                ospf_api.get_ospf_stats(bridge_a_port, "3.3.3.3")
                route_api.get_routes(bridge_a_port, "151.1.1.2")
                time.sleep(1 +index)
                index += 1

            trafficDevice.ping(bridge_a_port, '151.1.1.1', '151.1.1.2')
            # trafficDevice.ping(bridge_a_port, '16.1.1.1', '16.1.1.6')

            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))
            ospf_api.remove_ospf_router(bridge_a_port, "3.3.3.3")
            ospf_api.get_ospf_state(bridge_a_port, "3.3.3.3")

            frames = trafficDevice.get_all_captured_frames(bridge_a_port)
            for frame in frames:
                print(str(frame))
            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_isis_l3vsn_uni_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            spbm_api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            route_api = trafficDevice.get_api(NetworkEmulatingRouteConstants.ROUTE_API)
            end_station_api = trafficDevice.get_api(NetworkEmulatingEndstationConstants.END_STATION_API)
            assert isinstance(spbm_api,NetworkEmulatingSpbmApi)
            assert isinstance(route_api,NetworkEmulatingRouteApi)
            assert isinstance(end_station_api,NetworkEmulatingEndstationApi)
            bridge_a_name = "EzEdgeA"
            bridge_a_port = device_object.tx_port
            bridge_b_name = "EzEdgeB"
            bridge_b_port = device_object.rx_port

            trafficDevice.start_capture(bridge_b_port)
            trafficDevice.start_capture(bridge_a_port)
            # spbm_api.create_and_go_isis_interface(bridge_a_port, bridge_a_name, "00:00:00:0c:0a:01", 4051, 4052, "490000", "00:00:00:0e:0a:0f", 10, 3, 10)
            # spbm_api.create_and_go_isis_interface(bridge_b_port, bridge_b_name, "00:00:00:0c:0a:02", 4051, 4052, "490000", "00:00:00:0e:0a:06", 10, 3, 10)

            #for some reason I has to do this separately.
            spbm_api.create_isis_interface(bridge_a_port, bridge_a_name, "00:00:00:0c:0a:01", 4051, 4052, "490000", "00:00:00:0e:0a:0f", 10, 3, 10)
            spbm_api.create_isis_interface(bridge_b_port, bridge_b_name, "00:00:00:0c:0a:02", 4051, 4052, "490000", "00:00:00:0e:0a:06", 10, 3, 10)
            spbm_api.set_isis_globals()
            spbm_api.set_bridge_enabled()

            route_api.advetise_ipv4_routes(bridge_a_port, bridge_a_name, '1.1.1.13', '255.255.255.255')
            end_station_api.create_l3vsn_ipv4_endpoint(bridge_a_name, "A_host", 999, '10.10.10.0','10.10.10.55', '255.255.255.0')
            route_api.advetise_ipv4_routes(bridge_b_port, bridge_b_name, '1.1.1.14', '255.255.255.255')
            end_station_api.create_l3vsn_ipv4_endpoint(bridge_b_name, "B_host", 999, '11.10.10.0','11.10.10.55', '255.255.255.0')

            time.sleep(5)
            trafficDevice.ping(bridge_b_port, '11.10.10.55', '10.10.10.55')

            trafficDevice.stop_capture(bridge_b_port)
            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_b_port))
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))

            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_isis_ipshort_uni_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            spbm_api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            route_api = trafficDevice.get_api(NetworkEmulatingRouteConstants.ROUTE_API)
            end_station_api = trafficDevice.get_api(NetworkEmulatingEndstationConstants.END_STATION_API)
            assert isinstance(spbm_api,NetworkEmulatingSpbmApi)
            assert isinstance(route_api,NetworkEmulatingRouteApi)
            assert isinstance(end_station_api,NetworkEmulatingEndstationApi)
            bridge_a_name = "EzEdgeA"
            bridge_a_port = device_object.tx_port
            bridge_b_name = "EzEdgeB"
            bridge_b_port = device_object.rx_port

            trafficDevice.start_capture(bridge_b_port)
            trafficDevice.start_capture(bridge_a_port)
            spbm_api.create_and_go_isis_interface(bridge_a_port, bridge_a_name, "00:00:00:0c:0a:01", 4051, 4052, "490000", "00:00:00:0e:0a:0f", 10, 3, 10)
            spbm_api.create_and_go_isis_interface(bridge_b_port, bridge_b_name, "00:00:00:0c:0a:02", 4051, 4052, "490000", "00:00:00:0e:0a:06", 10, 3, 10)

            route_api.advetise_ipv4_routes(bridge_a_port, bridge_a_name, '1.1.1.13', '255.255.255.255')
            spbm_api.create_isis_ipv4_route_stack(bridge_a_port, bridge_a_name, True,  '10.10.10.1', '255.255.255.0', '1.1.1.13',1, 1, 1)

            route_api.advetise_ipv4_routes(bridge_b_port, bridge_b_name, '1.1.1.14', '255.255.255.255')
            spbm_api.create_isis_ipv4_route_stack(bridge_b_port, bridge_b_name, True, '11.10.10.1', '255.255.255.0', '1.1.1.14',1, 1, 1)
            time.sleep(5)
            trafficDevice.ping(bridge_b_port, '11.10.10.1', '10.10.10.1')
            trafficDevice.ping(bridge_a_port, '10.10.10.1', '11.10.10.1')
            trafficDevice.ping(bridge_a_port, '10.10.10.1', '1.1.1.14')
            trafficDevice.ping(bridge_b_port, '11.10.10.1', '1.1.1.13')

            trafficDevice.stop_capture(bridge_b_port)
            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_b_port))
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))

            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_isis_ipshort_and_routedL2vasn_uni_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            spbm_api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            route_api = trafficDevice.get_api(NetworkEmulatingRouteConstants.ROUTE_API)
            end_station_api = trafficDevice.get_api(NetworkEmulatingEndstationConstants.END_STATION_API)
            assert isinstance(spbm_api,NetworkEmulatingSpbmApi)
            assert isinstance(route_api,NetworkEmulatingRouteApi)
            assert isinstance(end_station_api,NetworkEmulatingEndstationApi)
            bridge_a_name = "EzEdgeA"
            bridge_a_port = device_object.tx_port
            bridge_b_name = "EzEdgeB"
            bridge_b_port = device_object.rx_port

            trafficDevice.start_capture(bridge_b_port)
            trafficDevice.start_capture(bridge_a_port)
            spbm_api.create_and_go_isis_interface(bridge_a_port, bridge_a_name, "00:00:00:0c:0a:01", 4051, 4052, "490000", "00:00:00:0e:0a:0f", 10, 3, 10)
            spbm_api.create_and_go_isis_interface(bridge_b_port, bridge_b_name, "00:00:00:0c:0a:02", 4051, 4052, "490000", "00:00:00:0e:0a:06", 10, 3, 10)

            end_station_api.create_l2vsn_ipv4_endpoint(bridge_a_name, "A_host", 999, '10.10.10.55', '255.255.255.0','00:00:00:0c:0a:01')
            end_station_api.create_l2vsn_ipv4_endpoint(bridge_b_name, "B_host", 999, '10.10.10.100', '255.255.255.0','00:00:00:0c:0a:02')

            route_api.advetise_ipv4_routes(bridge_a_port, bridge_a_name, '1.1.1.13', '255.255.255.255')
            end_station_api.create_routed_l2vsn_ipv4_endpoint(bridge_a_name, "Ar_host", 999, '10.10.10.56', '255.255.255.0', '1.1.1.13', '00:00:00:0c:0a:03')

            spbm_api.create_isis_ipv4_route_stack(bridge_a_port, bridge_a_name, True,  '10.10.10.1', '255.255.255.0', '1.1.1.13',1, 1, 1)

            route_api.advetise_ipv4_routes(bridge_b_port, bridge_b_name, '1.1.1.14', '255.255.255.255')
            spbm_api.create_isis_ipv4_route_stack(bridge_b_port, bridge_b_name, True, '11.10.10.1', '255.255.255.0', '1.1.1.14',1, 1, 1)
            spbm_api.create_isis_ipv4_route_stack(bridge_b_port, bridge_b_name, True, '11.10.10.10', '255.255.255.0', '1.1.1.14',1, 1, 1)
            spbm_api.create_isis_ipv4_route_stack(bridge_b_port, bridge_b_name, True, '11.10.10.100', '255.255.255.0', '1.1.1.14',1, 1, 1)
            time.sleep(5)
            trafficDevice.ping(bridge_b_port, '11.10.10.1', '10.10.10.1')
            trafficDevice.ping(bridge_b_port, '11.10.10.10', '10.10.10.1')
            trafficDevice.ping(bridge_b_port, '11.10.10.100', '10.10.10.1')
            trafficDevice.ping(bridge_a_port, '10.10.10.56', '10.10.10.100')
            trafficDevice.ping(bridge_a_port, '10.10.10.56', '11.10.10.1')
            trafficDevice.ping(bridge_a_port, '10.10.10.1', '11.10.10.1')
            trafficDevice.ping(bridge_a_port, '10.10.10.1', '1.1.1.14')
            trafficDevice.ping(bridge_b_port, '11.10.10.1', '1.1.1.13')
            trafficDevice.ping(bridge_b_port, '11.10.10.1', '1.1.1.13')

            trafficDevice.stop_capture(bridge_b_port)
            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_b_port))
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))

            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_isis_l2vsn_uni_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            spbm_api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            end_station_api = trafficDevice.get_api(NetworkEmulatingEndstationConstants.END_STATION_API)
            assert isinstance(spbm_api,NetworkEmulatingSpbmApi)
            bridge_a_name = "EzEdgeA"
            bridge_a_port = device_object.tx_port
            bridge_b_name = "EzEdgeB"
            bridge_b_port = device_object.rx_port

            trafficDevice.start_capture(bridge_b_port)
            trafficDevice.start_capture(bridge_a_port)
            spbm_api.create_and_go_isis_interface(bridge_a_port, bridge_a_name, "00:00:00:0c:0a:01", 4051, 4052, "490000", "00:00:00:0e:0a:0f", 10, 3, 10)
            spbm_api.create_and_go_isis_interface(bridge_b_port, bridge_b_name, "00:00:00:0c:0a:02", 4051, 4052, "490000", "00:00:00:0e:0a:06", 10, 3, 10)
            time.sleep(2)
            #net_api.create_isis_endpoint(bridge_name_a, "A_host", 999, '00:00:00:0e:0a:0f', 100, 0, '00:00:00:0c:0a:01', '10.10.10.55', '255.255.255.0', 1, 4051, 1, 0)
            end_station_api.create_l2vsn_ipv4_endpoint(bridge_a_name, "A_host", 999, '10.10.10.55', '255.255.255.0','00:00:00:0c:0a:01')
            # net_api.create_isis_endpoint(bridge_name_b, "B_host", 999, '00:00:00:0e:0a:06', 100, 0, '00:00:00:0c:0a:02', '10.10.10.100', '255.255.255.0', 1, 4051, 1, 0)
            end_station_api.create_l2vsn_ipv4_endpoint(bridge_b_name, "B_host", 999, '10.10.10.100', '255.255.255.0','00:00:00:0c:0a:02')
            time.sleep(5)
            trafficDevice.ping(bridge_a_port, '10.10.10.55', '10.10.10.100')
            trafficDevice.ping(bridge_b_port, '10.10.10.100', '10.10.10.55')
            time.sleep(2)
            trafficDevice.stop_capture(bridge_b_port)
            trafficDevice.stop_capture(bridge_a_port)
            print(trafficDevice.get_filtered_captured_frames_report(bridge_b_port))
            print(trafficDevice.get_filtered_captured_frames_report(bridge_a_port))

            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_isis_uni_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            net_api = trafficDevice.get_api(NetworkEmulatingEndstationConstants.END_STATION_API)
            assert isinstance(api,NetworkEmulatingSpbmApi)
            bridge_name_a = "EzEdgeA"
            bridge_name_b = "EzEdgeB"
            api.create_and_go_isis_interface(device_object.tx_port, bridge_name_a, "00:00:00:0c:0a:01", 4051, 4052, "490000", "00:00:00:0e:0a:0f", 10, 3, 10)
            api.create_and_go_isis_interface(device_object.rx_port, bridge_name_b, "00:00:00:0c:0a:02", 4051, 4052, "490000", "00:00:00:0e:0a:06", 10, 3, 10)

            time.sleep(1)
            trafficDevice.start_capture(device_object.rx_port)
            trafficDevice.start_capture(device_object.tx_port)
            time.sleep(5)
            trafficDevice.stop_capture(device_object.rx_port)
            trafficDevice.stop_capture(device_object.tx_port)
            print(trafficDevice.get_filtered_captured_frames_report(device_object.rx_port))
            print(trafficDevice.get_filtered_captured_frames_report(device_object.tx_port))
            trafficDevice.start_capture(device_object.rx_port)
            trafficDevice.start_capture(device_object.tx_port)

            net_api.create_isis_endpoint(bridge_name_a, "A_host", 999, '00:00:00:0e:0a:0f', 100, 0, '00:00:00:0c:0a:01', '10.10.10.55', '255.255.255.0', 1, 4051, 1, 0)
            net_api.create_isis_endpoint(bridge_name_b, "B_host", 999, '00:00:00:0e:0a:06', 100, 0, '00:00:00:0c:0a:02', '10.10.10.100', '255.255.255.0', 1, 4051, 1, 0)

            api.advetise_isis_ipv4_routes(device_object.rx_port, bridge_name_a, True, '1.1.1.13', '255.255.255.255', '10.10.10.1', '255.255.255.0', 1, 1, 1)
            api.advetise_isis_ipv4_routes(device_object.tx_port, bridge_name_b, True, '1.1.1.14', '255.255.255.255', '11.10.10.1', '255.255.255.0', 1, 1, 1)
            api.advetise_isis_ipv6_routes(device_object.rx_port, bridge_name_a, True, '::867:5309:867:5309', '1000:5309::', 64, 2, 1, 1, 0)
            api.advetise_isis_ipv6_routes(device_object.tx_port, bridge_name_b, True, '::feed:deaf:beef', '1000:feed::', 64, 2, 1, 1, 0)

            net_api.create_routed_l2vsn_ipv4_endpoint(bridge_name_a, 'edgeA_vlan200ipv4host', 200, '200.1.1.200',  '255.255.255.0', '200.1.1.1','00:aa:c8:aa:c8:aa', 1)
            net_api.create_l2vsn_ipv4_endpoint(bridge_name_b, 'edgeB_vlan200ipv4host', 200, '200.1.1.201', '255.255.255.0', '00:bb:c8:bb:c8:bb', 1)

            net_api.create_routed_l2vsn_ipv6_endpoint(bridge_name_a,'edgeB_vlan201ipv6host', 201, '1017::201', 64, '00:bb:c9:00:c8:bb', 1)
            net_api.create_l2vsn_ipv6_endpoint(bridge_name_b, 'edgeA_vlan201ipv6host', 201, '1017::200', 64, '00:aa:c9:00:c8:aa', 1)

            net_api.create_l3vsn_ipv4_endpoint(bridge_name_a, 'edgeA_blue', 682007, '19.74.6.0', '19.74.6.5', '255.255.255.0', 1, 1, 1, 1)
            net_api.create_l3vsn_ipv6_endpoint(bridge_name_b, 'edgeB_blue', 682007, '6:8:2007::', '6:8:2007::10', 64, 1, 1, 1, 1)

            trafficDevice.send_command("axping config -device 1")
            trafficDevice.send_command("axping clear -device 1 ")
            trafficDevice.send_command("axping 1.1.1.14 -device 1 -t 60 -d 0 -n 1 -l 4 -srcAddress 201.1.1.200 -timeout 10")

            time.sleep(30)
            trafficDevice.stop_capture(device_object.rx_port)
            trafficDevice.stop_capture(device_object.tx_port)
            print(trafficDevice.get_filtered_captured_frames_report(device_object.rx_port))
            print(trafficDevice.get_filtered_captured_frames_report(device_object.tx_port))
            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_isis_emulation(self):
        try:
            trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
            assert isinstance(trafficDevice,NetworkEmulatingDevice)

            #connect to the Ixia_Device
            trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
            #alternatively inline version
            trafficDevice.tgen_debug = True

            trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
            api = trafficDevice.get_api(NetworkEmulatingSpbmConstants.SBP_API)
            assert isinstance(api,NetworkEmulatingSpbmApi)
            api.create_and_go_isis_interface(device_object.tx_port, 'EzEdgeA', "00:00:00:0c:0a:01", 4051, 4052, "490000", "00:00:00:0e:0a:0f", 10, 3, 10)
            api.create_and_go_isis_interface(device_object.rx_port, 'EzEdgeB', "00:00:00:0c:0a:02", 4051, 4052, "490000", "00:00:00:0e:0a:06", 10, 3, 10)

            time.sleep(1)
            trafficDevice.start_capture(device_object.rx_port)
            trafficDevice.start_capture(device_object.tx_port)
            time.sleep(30)
            trafficDevice.stop_capture(device_object.rx_port)
            trafficDevice.stop_capture(device_object.tx_port)
            print(trafficDevice.get_filtered_captured_frames_report(device_object.rx_port))
            print(trafficDevice.get_filtered_captured_frames_report(device_object.tx_port))
            trafficDevice.disconnect()
        except Exception:
            print(StringUtils.exception_to_string())

    def test_ixnetwork_traffic(self):
        trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
        assert isinstance(trafficDevice,NetworkEmulatingDevice)

        #connect to the Ixia_Device
        trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
        #alternatively inline version
        trafficDevice.tgen_debug = True

        trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)
        ip_handle1 = trafficDevice.add_network_generator_interface(device_object.tx_port, "interface1", "192.168.1.2", "192.168.1.1", "255.255.255.0", "00:00:88:77:55:44")
        ip_handle2 = trafficDevice.add_network_generator_interface(device_object.rx_port, "interface2", "192.168.1.1", "192.168.1.2", "255.255.255.0", "00:00:88:77:55:55")
        trafficDevice.clear_network_generator_all_streams()
        trafficDevice.configure_network_generator_one_to_one_traffic(ip_handle1, ip_handle2, "IPv4_Traffic", TrafficConfigConstants.CIRCUIT_ENDPOINT_TYPE_IPV4)
        trafficDevice.start_network_generator_traffic()
        time.sleep(10000)
        trafficDevice.disconnect()

    def test_ixnetwork_bgp_traffic_chill_test(self):
        trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
        assert isinstance(trafficDevice,NetworkEmulatingDevice)

        #connect to the Ixia_Device
        trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
        #alternatively inline version
        trafficDevice.tgen_debug = True

        c_port = "4/16"

        trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, c_port , True)

        # print("set up the interfaces on port " + c_port)
        # ip_handle1 = trafficDevice.add_network_generator_interface(c_port, "interface1", "192.168.1.2", "192.168.1.1", "255.255.255.0", "00:00:88:77:55:44")

        print("set up BGP routes 1 and the peers #1 on port " + c_port)
        route_handle = trafficDevice.configure_network_generator_bgp_peer(c_port, "bgp_peer1","192.168.1.2", "192.168.1.1", None, "00:00:88:77:55:44",
                                                EmulationBgpConfigConstants.NEIGHBOR_TYPE_EXTERNAL, 200,
                                             EmulationBgpConfigConstants.IP_VERSION_4)
        trafficDevice.configure_network_generator_bgp_routes_on_bgp_peer(route_handle, "55.0.0.1", "255.255.255.0", 10, True, EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)

        print("Start BGP eemulation on port " + c_port)
        trafficDevice.start_network_generator_bgp_emulation(c_port)
        time.sleep(10)
        trafficDevice.start_network_generator_traffic()
        time.sleep(10)
        trafficDevice.disconnect()

    def test_ixnetwork_bgp_traffic(self):
        trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
        assert isinstance(trafficDevice,NetworkEmulatingDevice)

        #connect to the Ixia_Device
        trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
        #alternatively inline version
        trafficDevice.tgen_debug = True

        trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)

        # print("set up the interfaces on ports " + device_object.tx_port + " and " + device_object.rx_port)
        # ip_handle1 = trafficDevice.add_network_generator_interface(device_object.tx_port, "interface1", "192.168.1.2", "192.168.1.1", "255.255.255.0", "00:00:88:77:55:44")
        # ip_handle2 = trafficDevice.add_network_generator_interface(device_object.rx_port, "interface2", "192.168.1.1", "192.168.1.2", "255.255.255.0", "00:00:88:77:55:55")

        print("set up BGP routes 1 and the peers #1 on port " + device_object.tx_port)
        route_handle = trafficDevice.configure_network_generator_bgp_peer(device_object.tx_port, "bgp_peer1","192.1.1.2", "192.1.1.1", None, "00:00:88:77:55:44",
                                                EmulationBgpConfigConstants.NEIGHBOR_TYPE_INTERNAL, 200,
                                             EmulationBgpConfigConstants.IP_VERSION_4)
        trafficDevice.configure_network_generator_bgp_routes_on_bgp_peer(route_handle, "55.0.0.1", "255.255.255.0", 1, True, EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)

        print("set up BGP routes 2 and the peers #2 on port " + device_object.rx_port)
        route_handle2 = trafficDevice.configure_network_generator_bgp_peer(device_object.rx_port, "bgp_peer2","192.1.1.1", "192.1.1.2", None,"00:00:88:77:55:55",
                                                EmulationBgpConfigConstants.NEIGHBOR_TYPE_INTERNAL, 100,
                                             EmulationBgpConfigConstants.IP_VERSION_4)
        trafficDevice.configure_network_generator_bgp_routes_on_bgp_peer(route_handle2, "77.0.0.1", "255.255.255.0", 1, True, EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)

        print("Start BGP eemulation on port " + device_object.tx_port + " and " + device_object.rx_port)
        trafficDevice.start_network_generator_bgp_emulation(device_object.tx_port)
        trafficDevice.start_network_generator_bgp_emulation(device_object.rx_port)
        time.sleep(10)
        trafficDevice.start_network_generator_traffic()
        time.sleep(10)
        trafficDevice.disconnect()

    def test_ixnetwork_multiple_bgp_peers_traffic(self):
        trafficDevice = device_object.connect_and_take_ports() #instantiate an Ixia Device
        assert isinstance(trafficDevice,NetworkEmulatingDevice)

        #connect to the Ixia_Device
        trafficDevice.connect_network_generator(device_object.vm, device_object.ixNetworkIp, device_object.vm_port)
        #alternatively inline version
        trafficDevice.tgen_debug = True

        trafficDevice.take_network_generator_port_ownership(device_object.dev, device_object.username, [device_object.tx_port, device_object.rx_port], True)

        # print("set up the interfaces on ports " + device_object.tx_port + " and " + device_object.rx_port)
        # ip_handle1 = trafficDevice.add_network_generator_interface(device_object.tx_port, "interface1", "192.168.1.2", "192.168.1.1", "255.255.255.0", "00:00:88:77:55:44")
        # ip_handle2 = trafficDevice.add_network_generator_interface(device_object.rx_port, "interface2", "192.168.1.1", "192.168.1.2", "255.255.255.0", "00:00:88:77:55:55")

        print("set up BGP routes 1 and the peers #1 on port " + device_object.tx_port)
        route_handle = trafficDevice.configure_network_generator_bgp_peer(device_object.tx_port, "bgp_peer1","192.1.1.2", "192.1.1.1", None, "00:00:88:77:55:44",
                                                EmulationBgpConfigConstants.NEIGHBOR_TYPE_INTERNAL, 200,
                                             EmulationBgpConfigConstants.IP_VERSION_4)
        trafficDevice.configure_network_generator_bgp_routes_on_bgp_peer(route_handle, "55.0.0.1", "255.255.255.0", 4, True, EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)
        # trafficDevice.configure_network_generator_bgp_routes_on_bgp_peer(route_handle, "56.0.0.1", "255.255.255.0", 1, True, EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)

        print("set up BGP routes 2 and the peers #2 on port " + device_object.rx_port)
        route_handle2 = trafficDevice.configure_network_generator_bgp_peer(device_object.rx_port, "bgp_peer2","192.1.1.1", "192.1.1.2", None,"00:00:88:77:55:55",
                                                EmulationBgpConfigConstants.NEIGHBOR_TYPE_INTERNAL, 100,
                                             EmulationBgpConfigConstants.IP_VERSION_4)
        trafficDevice.configure_network_generator_bgp_routes_on_bgp_peer(route_handle2, "77.0.0.1", "255.255.255.0", 4, True, EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)
        # trafficDevice.configure_network_generator_bgp_routes_on_bgp_peer(route_handle2, "78.0.0.1", "255.255.255.0", 1, True, EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)
        # trafficDevice.configure_network_generator_bgp_routes_on_bgp_peer(route_handle2, "79.0.0.1", "255.255.255.0", 1, True, EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)
        #

        print("Start BGP eemulation on port " + device_object.tx_port + " and " + device_object.rx_port)
        trafficDevice.start_network_generator_bgp_emulation(device_object.tx_port)
        trafficDevice.start_network_generator_bgp_emulation(device_object.rx_port)
        time.sleep(10)
        trafficDevice.start_network_generator_traffic()
        time.sleep(10)
        trafficDevice.disconnect()


if __name__ == '__main__':
    unittest.main()
