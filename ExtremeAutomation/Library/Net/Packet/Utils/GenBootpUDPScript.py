from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# flags 16 bits
# group policy id 16 bits
# vxlan network identifier 24 bits
# reserved 8 bits

packetProtocol = "Bootp"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Op Code", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [2, "Hardware Type", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [3, "Hardward Address", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [4, "Hops", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [5, "Transaction ID", 4 * 8, PacketConstants.INTEGER, None, False, "", None],
    [6, "Seconds", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [7, "Flags", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [8, "Client IP Address", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [9, "Your Client IP Address", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [10, "Next Server IP Address", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [11, "Relay Agent IP Address", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [12, "Client MAC Address", 16 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [14, "Server Host Name", 8 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [15, "Boot File Name", 128 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [16, "Magic Cookie", 4 * 8, PacketConstants.HEX_STRING, None, False, "", None],
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
