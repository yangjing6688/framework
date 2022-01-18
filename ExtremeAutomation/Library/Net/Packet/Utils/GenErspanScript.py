from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 4 bits version
# 12 bits vlan
# 3 bits cos
# 2 bits en
# 1 bit T
# 10 bit session id
# 12 bit reserved
# 20 bit Index


#             ERSPAN Type II header (8 octets [42:49])
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |  Ver  |          VLAN         | COS | En|T|    Session ID     |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |      Reserved         |                  Index                |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# The above 8-octet header is immediately followed by the original
# mirrored frame and then by the standard 4-octet Ethernet CRC:
#
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                     Original Mirrored Frame                   |
#    |                              ...                              |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                              CRC                              |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#


packetProtocol = "Erspan"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "version", 4, PacketConstants.INTEGER, None, False, "", None],
    [2, "VLAN", 12, PacketConstants.INTEGER, None, False, "", None],
    [3, "COS", 3, PacketConstants.INTEGER, None, False, "", None],
    [4, "En", 2, PacketConstants.INTEGER, None, False, "", None],
    [5, "T", 1, PacketConstants.INTEGER, None, False, "", None],
    [6, "Session ID", 10, PacketConstants.INTEGER, None, False, "", None],
    [7, "Reserved", 12, PacketConstants.INTEGER, None, False, "", None],
    [8, "Index", 20, PacketConstants.INTEGER, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "GreIpV4Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "GreIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "GreIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("EthernetSnapIpV4" + tag_type + "Packet", "EthernetSnap", "GreIpV4Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("EthernetSnapIpV4" + tag_type + "Packet", "EthernetSnap", "GreIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("EthernetSnapIpV4" + tag_type + "Packet", "EthernetSnap", "GreIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "GreIpV6Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "GreIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "GreIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("EthernetSnapIpV6" + tag_type + "Packet", "EthernetSnap", "GreIpV6Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("EthernetSnapIpV6" + tag_type + "Packet", "EthernetSnap", "GreIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("EthernetSnapIpV6" + tag_type + "Packet", "EthernetSnap", "GreIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
