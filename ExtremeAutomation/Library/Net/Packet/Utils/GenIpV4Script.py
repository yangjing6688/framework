from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants


# version = 4bits
# hdlen = 4bits
# TOS = 8 bits/1 byte
# Length = 16 bits
# ID = 16 bits
# flags + frag offset = 16 bits
# TTL = 8 bits
# Protocol = 8 bits
# checksum = 16 bits
# SIP = 32 bits
# DIP = 32 bits
# Options = Length - 20

packetProtocol = "IpV4"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "version", 4, PacketConstants.INTEGER, None, False, "", None],
    [2, "hdlen", 4, PacketConstants.INTEGER, None, False, "", None],
    [3, "tos", 8, PacketConstants.INTEGER, None, False, "", None],
    [4, "length", 16, PacketConstants.INTEGER, None, False, "", None],
    [5, "id", 16, PacketConstants.INTEGER, None, False, "", None],
    [5, "flags", 16, PacketConstants.INTEGER, None, False, "", None],
    [5, "ttl", 8, PacketConstants.INTEGER, None, False, "", None],
    [5, "protocol", 8, PacketConstants.INTEGER, None, False, "", None],
    [5, "checksum", 16, PacketConstants.INTEGER, None, False, "", None],
    [5, "source_ip", 32, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [5, "destination_ip", 32, PacketConstants.IPV4_ADDRESS, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2" + tag_type + "Packet", "Ethernet2", "Packet", packetProtocol, packetFields,
                              tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2" + tag_type + "Packet", "Ethernet2", tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2" + tag_type + "Packet", "Ethernet2", tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("EthernetSnap" + tag_type + "Packet", "EthernetSnap", "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("EthernetSnap" + tag_type + "Packet", "EthernetSnap", tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("EthernetSnap" + tag_type + "Packet", "EthernetSnap", tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
