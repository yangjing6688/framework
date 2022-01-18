import unittest
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Net.Address.Ipv6Address import Ipv6Address
from ExtremeAutomation.Library.Net.Packet.AbstractPacket import AbstractPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4TaggedPacket import Ethernet2IpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4Packet import Ethernet2UdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketClassifier import PacketClassifier
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.UdpPacketHeader import UdpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketTagConstants
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapTcpIpV4VlanStackPacket import EthernetSnapTcpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2TcpIpV6Packet import Ethernet2TcpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2GreIpV4Packet import Ethernet2GreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2ErspanGreIpV4Packet import Ethernet2ErspanGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2VxlanUdpIpV4Packet import Ethernet2VxlanUdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2IpEncapsulatedIpV6Packet import Ethernet2IpEncapsulatedIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2IpEncapsulatedIpV4Packet import Ethernet2IpEncapsulatedIpV4Packet


class TestStringMethods(unittest.TestCase):

    def test_main(self):
        packet = Ethernet2IpV4TaggedPacket()
        print(packet.get_header_bytes())
        packet.set_source_mac("AA:BB:CC:DD:EE:FF")
        packet.set_vlan_tci(6)
        packet.set_vlan_id(66)
        print(packet.get_header_bytes())
        packet = PacketClassifier.classify_packet("00 11 22 33 44 55", "AA BB CC DD EE FF", " 81 00", "01 BC 08 00 45 00 00 2E 00 00 00 00 40 FF 73 CC 02 02 02 02 01 01 01 01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD BE EF 00 01 00 00 1E F2 F3 D6 D6 91 5C A7")
        packet = PacketClassifier.classify_packet("00 22 33 44 55 66", "00 22 33 44 55 67", "81 00", "01 BC 08 00 45 00 00 2E 00 00 00 00 40 FF 73 CC 02 02 02 02 01 01 01 01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD")
        print(str(packet))
        packet = Ethernet2UdpIpV4Packet()
        packet.set_ip_options_and_auto_pad("23 42 34")
        packet.set_destination_mac("00:33:22:33:44:55")
        packet.set_source_mac("00:33:22:33:44:66")
        packet.set_destination_ip("1.1.1.1")
        packet.set_source_ip("2.2.2.2")
        packet2 = PacketClassifier.copy_to_vlanstack_packet(packet)
        print(str(packet2))
        packet2 = PacketClassifier.copy_to_untag_packet(packet)
        print(str(packet2))
        packet2 = PacketClassifier.copy_to_tag_packet(packet)
        print(str(packet2))
        packet2.set_vlan_id("10")
        packet2.set_destination_ip("2.3.4.5")
        packet2.set_ip_tos(45)
        packet3 = PacketClassifier.clone_packet(packet)
        packet3.set_destination_ip("1.2.2.1")
        print(str(packet))
        print(str(packet3))
        print(str(packet2))
        print(packet2.get_header_bytes())
        packet2 = PacketClassifier.copy_to_untag_packet(packet2)
        print(str(packet2))
        print(packet2.get_hltapi_commands())
        packet2.set_ether_type("0xffff")
        print(packet2.get_hltapi_commands())
        print(str(packet2))

        print(packet2.get_header_bytes())

        print("\n\n")
        packets = PacketClassifier.get_one_of_every_packet()

        # packets = [Ethernet2TcpIpV4TaggedPacket()]

        for packet in packets:
            print("===" * 20)
            packet.set_destination_mac("00:33:22:33:44:55")
            packet.set_source_mac("00:33:22:33:44:66")
            tags = packet.get_packet_tags()
            if PacketTagConstants.TAG_QTAGGED in tags or isinstance(packet, TaggedPacketHeader):
                packet.set_vlan_id(44)
                packet.set_vlan_tci(3)
            if PacketTagConstants.TAG_VLAN_STACK in tags or isinstance(packet, VlanStackPacketHeader):
                num = packet.get_vlan_num()
                index = 1
                for index in range(1, num + 1):
                    packet.set_vlan_id(index, 44)
                    packet.set_vlan_tci(index, 3)
                    index += 1
            if PacketTagConstants.TAG_ENET2 in tags or isinstance(packet, Ethernet2PacketHeader):
                pass
            if PacketTagConstants.TAG_IPV4 in tags or isinstance(packet, IpV4PacketHeader):
                packet.set_destination_ip("1.1.1.1")
                packet.set_source_ip("2.2.2.2")
                packet.set_ip_ttl(250)
                packet.set_ip_tos(255)
                packet.set_ip_fragment_offset("2")
                packet.set_ip_flags("3")
            if PacketTagConstants.TAG_IPV6 in tags or isinstance(packet, IpV6PacketHeader):
                packet.set_ipv6_destination_address("FF00::dddd")
                packet.set_ipv6_source_address("FF00::dddd")
                packet.set_ipv6_hop_limit(255)
                packet.set_ipv6_traffic_class(5)
            if PacketTagConstants.TAG_TCP in tags or isinstance(packet, TcpPacketHeader):
                packet.set_destination_port("44")
                packet.set_source_port("33")
            if PacketTagConstants.TAG_UDP in tags or isinstance(packet, UdpPacketHeader):
                packet.set_destination_port("0x66")
                packet.set_source_port("55")
                packet.set_source_port("65000")
            if PacketTagConstants.TAG_IPX in tags:
                pass
            print("Packet tags: " + " ".join(tags))
            print(packet.to_packet_string())
            print(packet.get_bytes(True))

            print("HLTAPI cmds:")
            hltapi_dict = packet.get_hltapi_commands()
            for key in hltapi_dict:
                print("\t\t" + str(key) + " " + str(hltapi_dict[key]))
            print("\nNOW SET PAYLOAD")
            if isinstance(packet, TaggedPacketHeader):
                packet.set_payload("000000000001" + "000033221122" + "8100" + "2ECC" + "0800" + "450002400846000080060000868d5a4e4134d945c5dc01bb894c57cdebd9865850100101051d000053118749795449983d126560cddd50b4ac64af9f987c7227a168ea6b462f884a2d89241f968b74710f85a1f557c3efb05f37f93ae632e717fbf6b8dba0d77ae86e9452704fe260a0d0e22f319bf339ca57ec44acf88535319c51fb407589ebc03decb9be416181560805526b99c743835c365f1448e6ba675d9137217ec614073bbf64d23f5e2268a8ba4b05e6a809e3fa07260419cd00a771640000773841569cd108ad32e90dd21cc15b839969ffef7393966b8151008a8edc719030c461064b7f2ae98d38713d25bc3438ca041a71e0c3eabe956c54a6245e15a1d4f2a4304ffab875b8674d18f40dd66fffb604b77a9717b3f3d3081f85f830892991be592ac323b96404cf6f018836a199c470c3ae3976b66e43a32411e91fd25cac40396eef7946c8da54cf5d5b342630c8b7bb09e411406ca6bc84f268d1c97f0d1bc24a4669964fa8f1db53bb7bb98f0cf3e079327337e0c1c3e6da08679d62f1c06ab2e6a5d42a0be6daa6b7d986808b73169a99adf19b18a8f1addc4fd36f953da72f66e11e22f7a1ff452743c76a68346b18f7b00ce471da9d4ecd85acdc941d4b5798d31e99c6b5da4d3086947832d62698c947bb7a51a6d0fc5ae414597d2a5213007476c6f8d97b0a9834d8663d8943e183fe3d66cbc88a0aa708d41556f3e88da5de4a49710c4bb3d76805971b5aa798c4fcee968b8c793e5aba5c07715202a5ce9dbd964c203ff9a0880d98f59db6cdda4541c076445e")
            elif isinstance(packet, VlanStackPacketHeader):
                packet.set_payload(
                    "000000000001" + "000033221122" + "8100" + "2ECD" + "88A8" + "2ECD" + "8100" + "2ECC" + "0800" + "450002400846000080060000868d5a4e4134d945c5dc01bb894c57cdebd9865850100101051d000053118749795449983d126560cddd50b4ac64af9f987c7227a168ea6b462f884a2d89241f968b74710f85a1f557c3efb05f37f93ae632e717fbf6b8dba0d77ae86e9452704fe260a0d0e22f319bf339ca57ec44acf88535319c51fb407589ebc03decb9be416181560805526b99c743835c365f1448e6ba675d9137217ec614073bbf64d23f5e2268a8ba4b05e6a809e3fa07260419cd00a771640000773841569cd108ad32e90dd21cc15b839969ffef7393966b8151008a8edc719030c461064b7f2ae98d38713d25bc3438ca041a71e0c3eabe956c54a6245e15a1d4f2a4304ffab875b8674d18f40dd66fffb604b77a9717b3f3d3081f85f830892991be592ac323b96404cf6f018836a199c470c3ae3976b66e43a32411e91fd25cac40396eef7946c8da54cf5d5b342630c8b7bb09e411406ca6bc84f268d1c97f0d1bc24a4669964fa8f1db53bb7bb98f0cf3e079327337e0c1c3e6da08679d62f1c06ab2e6a5d42a0be6daa6b7d986808b73169a99adf19b18a8f1addc4fd36f953da72f66e11e22f7a1ff452743c76a68346b18f7b00ce471da9d4ecd85acdc941d4b5798d31e99c6b5da4d3086947832d62698c947bb7a51a6d0fc5ae414597d2a5213007476c6f8d97b0a9834d8663d8943e183fe3d66cbc88a0aa708d41556f3e88da5de4a49710c4bb3d76805971b5aa798c4fcee968b8c793e5aba5c07715202a5ce9dbd964c203ff9a0880d98f59db6cdda4541c076445e")
            else:
                packet.set_payload("000000000001" + "000033221122" + "0800" + "450002400846000080060000868d5a4e4134d945c5dc01bb894c57cdebd9865850100101051d000053118749795449983d126560cddd50b4ac64af9f987c7227a168ea6b462f884a2d89241f968b74710f85a1f557c3efb05f37f93ae632e717fbf6b8dba0d77ae86e9452704fe260a0d0e22f319bf339ca57ec44acf88535319c51fb407589ebc03decb9be416181560805526b99c743835c365f1448e6ba675d9137217ec614073bbf64d23f5e2268a8ba4b05e6a809e3fa07260419cd00a771640000773841569cd108ad32e90dd21cc15b839969ffef7393966b8151008a8edc719030c461064b7f2ae98d38713d25bc3438ca041a71e0c3eabe956c54a6245e15a1d4f2a4304ffab875b8674d18f40dd66fffb604b77a9717b3f3d3081f85f830892991be592ac323b96404cf6f018836a199c470c3ae3976b66e43a32411e91fd25cac40396eef7946c8da54cf5d5b342630c8b7bb09e411406ca6bc84f268d1c97f0d1bc24a4669964fa8f1db53bb7bb98f0cf3e079327337e0c1c3e6da08679d62f1c06ab2e6a5d42a0be6daa6b7d986808b73169a99adf19b18a8f1addc4fd36f953da72f66e11e22f7a1ff452743c76a68346b18f7b00ce471da9d4ecd85acdc941d4b5798d31e99c6b5da4d3086947832d62698c947bb7a51a6d0fc5ae414597d2a5213007476c6f8d97b0a9834d8663d8943e183fe3d66cbc88a0aa708d41556f3e88da5de4a49710c4bb3d76805971b5aa798c4fcee968b8c793e5aba5c07715202a5ce9dbd964c203ff9a0880d98f59db6cdda4541c076445e")
            print(".." * 20)
            print("Packet tags: " + " ".join(tags))
            print(packet.to_packet_string())
            print(packet.get_bytes())
            print("HLTAPI cmds:")
            hltapi_dict = packet.get_hltapi_commands()
            for key in hltapi_dict:
                print("\t\t" + str(key) + " " + str(hltapi_dict[key]))
            print("+++" * 20)

    def test_gre(self):
        innerp_packet = Ethernet2UdpIpV4Packet()
        packet = Ethernet2GreIpV4Packet(innerp_packet)
        print(packet.to_packet_string())

        print(innerp_packet.to_packet_string())

    def test_erspan(self):
        innerp_packet = Ethernet2UdpIpV4Packet()
        packet = Ethernet2ErspanGreIpV4Packet(innerp_packet)
        print(packet.to_packet_string())

        print(innerp_packet.to_packet_string())

    def test_ip_ip(self):
        innerp_packet = Ethernet2UdpIpV4Packet()
        packet = Ethernet2IpEncapsulatedIpV4Packet(innerp_packet)
        print(packet.to_packet_string())

        print(innerp_packet.to_packet_string())

    def test(self):
        packet = PacketClassifier.get_packet("ETHERNET2TAGGEDPACKET")
        print(str(packet))
        packet = PacketClassifier.get_packet("Ethernet2Ipv4Packet")
        print(str(packet))
        packet = PacketClassifier.get_packet("Ethernet2VlanStackPacket")
        packet.set_vlan_num(4)
        print(str(packet))
        packet = PacketClassifier.get_packet(EthernetSnapTcpIpV4VlanStackPacket(0).get_name())
        packet.set_vlan_num(4)
        print(str(packet))

    def test_lldp(self):
        packets = PacketClassifier.get_one_of_every_lldp_packet()
        for packet in packets:
            PacketClassifier.set_default_test_packet_values(packet)
            print(str(packet))

    def test_encap_length(self):
        inner_packet = Ethernet2UdpIpV4Packet()
        inner_packet_v6 = Ethernet2TcpIpV6Packet()
        PacketClassifier.set_default_test_packet_values(inner_packet)
        inner_packet.configure_packet()
        inner_packet_v6.configure_packet()
        gre_packet = Ethernet2GreIpV4Packet(inner_packet)
        print(gre_packet.to_packet_string())
        gre_packet.set_gre_flag_checksun_present(True)
        gre_packet.set_gre_flag_strict_source_route(True)
        print(gre_packet.to_packet_string())
        gre_packet.set_gre_flag_version_number(0x02)
        print(gre_packet.to_packet_string())
        gre_packet = Ethernet2VxlanUdpIpV4Packet(inner_packet)
        gre1_packet = Ethernet2IpEncapsulatedIpV6Packet(inner_packet)
        gre2_packet = Ethernet2IpEncapsulatedIpV4Packet(inner_packet)
        gre3_packet = Ethernet2IpEncapsulatedIpV6Packet(inner_packet_v6)
        gre4_packet = Ethernet2IpEncapsulatedIpV4Packet(inner_packet_v6)
        packets = [gre1_packet, gre2_packet, gre3_packet, gre4_packet]
        AbstractPacket.compare_packet_fields(gre1_packet, gre1_packet)

    def test_min_length(self):
        packet = PacketClassifier.get_packet("ETHERNETPACKET")
        print(packet.get_name() + " min size " + str(packet.get_header_length()))
        PacketClassifier.set_default_test_packet_values(packet)
        print("set defaults")
        print(packet.get_name() + " min size " + str(packet.get_header_length()))
        packet = PacketClassifier.get_packet("ETHERNET2PACKET")
        print(packet.get_name() + " min size " + str(packet.get_header_length()))
        PacketClassifier.set_default_test_packet_values(packet)
        print("set defaults")
        print(packet.get_name() + " min size " + str(packet.get_header_length()))

        packet = PacketClassifier.get_packet("SAPMSTPSPANNINGTREEBPDUPACKET")
        print(packet.get_name() + " min size " + str(packet.get_header_length()))
        PacketClassifier.set_default_test_packet_values(packet)
        print("set defaults")
        print(packet.get_name() + " min size " + str(packet.get_header_length()))

        packet = PacketClassifier.get_packet("SAPMSTPSPANNINGTREEBPDUTAGGEDPACKET")
        print(packet.get_name() + " min size " + str(packet.get_header_length()))
        PacketClassifier.set_default_test_packet_values(packet)
        print("set defaults")
        print(packet.get_name() + " min size " + str(packet.get_header_length()))

    def test_ipv4_address(self):
        print(Ipv4Address(16985093).to_string())
        print(Ipv4Address("1.3.44.5").to_string())
        print(Ipv4Address("01032C05").to_string())

    def test_ipv6_address(self):
        print("expanded")
        print(Ipv6Address("FF01:1234:1234:1234::1").to_string())
        print(Ipv6Address("FF01:1234:1234:1234::").to_string())
        print(Ipv6Address("::1").to_string())
        print(Ipv6Address("FF01:1234:1234:1234:1234:1234:1234:1").to_string())
        print("collapsed")
        print(Ipv6Address("FF01:1234:1234:1234::1").to_string(True))
        print(Ipv6Address("FF01:1234:1234:1234::").to_string(True))
        print(Ipv6Address("::1").to_string(True))
        print(Ipv6Address("FF01:1234:1234:1234:1234:1234:1234:1").to_string(True))


if __name__ == '__main__':
    unittest.main()
