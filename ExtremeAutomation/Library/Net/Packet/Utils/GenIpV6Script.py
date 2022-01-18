from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 4 bits version
# 8 bits traffic class
# 20 bits flow label
# 16 bits payload length
# 8 bits next header
# 8 bits hop limit
# 128 bits source address
# 128 bits destination address

packetProtocol = "IpV6"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "version", 4, PacketConstants.INTEGER, None, False, "", None],
    [2, "traffic class", 8, PacketConstants.INTEGER, None, False, "", None],
    [3, "flow label", 20, PacketConstants.INTEGER, None, False, "", None],
    [4, "payload length", 16, PacketConstants.INTEGER, None, False, "", None],
    [5, "next header", 8, PacketConstants.INTEGER, None, False, "", None],
    [6, "hop limit", 8, PacketConstants.INTEGER, None, False, "", None],
    [7, "source address", 128, PacketConstants.IPV6_ADDRESS, None, False, "", None],
    [8, "destination address", 128, PacketConstants.IPV6_ADDRESS, None, False, "", None],
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
