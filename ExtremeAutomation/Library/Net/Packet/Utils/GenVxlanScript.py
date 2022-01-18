from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# flags 16 bits
# group policy id 16 bits
# vxlan network identifier 24 bits
# reserved 8 bits

packetProtocol = "Vxlan"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "flags", 16, PacketConstants.INTEGER, None, False, "", None],
    [2, "group policy id", 16, PacketConstants.INTEGER, None, False, "", None],
    [3, "vxlan network identifier", 24, PacketConstants.INTEGER, None, False, "", None],
    [4, "reserved", 8, PacketConstants.INTEGER, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2UdpIpV4" + tag_type + "Packet", "Ethernet2", "UdpIpV4Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2UdpIpV4" + tag_type + "Packet", "Ethernet2", "UdpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2UdpIpV4" + tag_type + "Packet", "Ethernet2", "UdpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
