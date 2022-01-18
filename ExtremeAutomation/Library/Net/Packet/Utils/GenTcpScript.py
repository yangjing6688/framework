from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 16 bits source port
# 16 bits destination port
# 32 bits sequence number
# 32 bits acknowledgement number
# 4 bits data offset
# 8 bits reserved
# 4 bits flags
# 16 bits window
# 16 bits checksum
# 16 bits urgent porter
# n bits options


packetProtocol = "Tcp"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "source port", 16, PacketConstants.INTEGER, None, False, "", None],
    [2, "destination port", 16, PacketConstants.INTEGER, None, False, "", None],
    [3, "sequence number", 32, PacketConstants.INTEGER, None, False, "", None],
    [4, "acknowledgement number", 32, PacketConstants.INTEGER, None, False, "", None],
    [5, "data offset", 4, PacketConstants.INTEGER, None, False, "", None],
    [6, "reserved", 8, PacketConstants.INTEGER, None, False, "", None],
    [7, "flags", 4, PacketConstants.INTEGER, None, False, "", None],
    [8, "window", 16, PacketConstants.INTEGER, None, False, "", None],
    [9, "checksum", 16, PacketConstants.INTEGER, None, False, "", None],
    [10, "urgent porter", 16, PacketConstants.INTEGER, None, False, "", None],
    [11, "options", 0, PacketConstants.HEX_STRING, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "IpV4Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "IpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "IpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("EthernetSnapIpV4" + tag_type + "Packet", "EthernetSnap", "IpV4Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("EthernetSnapIpV4" + tag_type + "Packet", "EthernetSnap", "IpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("EthernetSnapIpV4" + tag_type + "Packet", "EthernetSnap", "IpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("EthernetSnapIpV6" + tag_type + "Packet", "EthernetSnap", "IpV6Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("EthernetSnapIpV6" + tag_type + "Packet", "EthernetSnap", "IpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("EthernetSnapIpV6" + tag_type + "Packet", "EthernetSnap", "IpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
