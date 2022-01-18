from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 16 bits flags_and_version
# 16 bits dprotocol_type
# 16 bits checksum #optional
# 16 bits offset #optional
# 32 bits key #optional
# 32 bits sequence #optional
# n bits routing #optional


packetProtocol = "Gre"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "flags_and_version", 16, PacketConstants.INTEGER, None, False, "", None],
    [2, "protocol_type", 16, PacketConstants.INTEGER, None, False, "", None],
    [2, "checksum", 16, PacketConstants.INTEGER, None, False, "", None],  # optional
    [2, "offset", 16, PacketConstants.INTEGER, None, False, "", None],  # optional
    [2, "key", 32, PacketConstants.INTEGER, None, False, "", None],  # optional
    [2, "sequence", 32, PacketConstants.INTEGER, None, False, "", None],  # optional
    [2, "routing", 32, PacketConstants.INTEGER, None, False, "", None],  # (variable/optional)
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
