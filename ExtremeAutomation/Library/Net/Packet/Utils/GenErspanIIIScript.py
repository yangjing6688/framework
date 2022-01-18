from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 4 bits version
# 12 bits vlan
# 3 bits cos
# 2 bits bso
# 1 bit T
# 10 bit session id
# 32 bits timestamp
# 16 bits sgt
# 1 bit P
# 5 bits Frame Type
# 6 bits Hardware id
# 1 bit Direction
# 2 bits Gra Timestamp Granularity
# 1 bit Optional sub-header
# 6 bits Platf ID
# 58 bits platform specific info


#                  ERSPAN Type III header (12 octets)
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |  Ver  |          VLAN         | COS |BSO|T|     Session ID    |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                          Timestamp                            |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |             SGT               |P|    FT   |   Hw ID   |D|Gra|O|
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
#              Platform Specific SubHeader (8 octets, optional)
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |  Platf ID |               Platform Specific Info              |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                  Platform Specific Info                       |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# The above composite header is immediately followed by the original
# mirrored frame and then by the standard 4-octet Ethernet CRC.
#
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                     Original Mirrored Frame                   |
#    |                              ...                              |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                              CRC                              |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#


packetProtocol = "ErspanIII"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "version", 4, PacketConstants.INTEGER, None, False, "", None],
    [2, "VLAN", 12, PacketConstants.INTEGER, None, False, "", None],
    [3, "COS", 3, PacketConstants.INTEGER, None, False, "", None],
    [4, "BSO", 2, PacketConstants.INTEGER, None, False, "", None],
    [5, "T", 1, PacketConstants.INTEGER, None, False, "", None],
    [6, "Session ID", 10, PacketConstants.INTEGER, None, False, "", None],
    [7, "timestamp", 32, PacketConstants.INTEGER, None, False, "", None],
    [8, "Security Group Tag", 16, PacketConstants.INTEGER, None, False, "", None],
    [9, "P", 1, PacketConstants.INTEGER, None, False, "", None],
    [10, "Frame Type", 5, PacketConstants.INTEGER, None, False, "", None],
    [11, "Hardware ID", 6, PacketConstants.INTEGER, None, False, "", None],
    [12, "Direction", 1, PacketConstants.INTEGER, None, False, "", None],
    [13, "Gra Timestamp Granularity", 2, PacketConstants.INTEGER, None, False, "", None],
    [14, "Optional Subheader", 1, PacketConstants.INTEGER, None, False, "", None],
    [15, "platform specific ID", 6, PacketConstants.INTEGER, None, False, "", None],
    [16, "platform specific info 1", 10, PacketConstants.INTEGER, None, False, "", None],
    [17, "platform specific info 2", 16, PacketConstants.INTEGER, None, False, "", None],
    [18, "platform specific info 3", 32, PacketConstants.INTEGER, None, False, "", None],
]

# 0x1                       Corresponds to the following format:
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |    0x1    |          Reserved         |     VSM Domain ID     |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                        Port_ID/Index                          |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# 0x3                       Corresponds to the following format:
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |    0x3    |      Reserved         |       Port ID/Index       |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |       Timestamp (upper 4 octets of a UInteger64 value)        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# 0x4                       Corresponds to the following format:
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |    0x4    |      Reserved         |         Reserved          |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                        Reserved                               |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# 0x5-0x6                   Correspond to the following format:
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |0x5 or 0x6 |      Switch ID    |         Port ID/Index         |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                    Timestamp (seconds)                        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

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
