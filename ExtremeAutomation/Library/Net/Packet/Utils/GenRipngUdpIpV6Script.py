from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
# http://www.tcpipguide.com/free/t_BGPConnectionEstablishmentOpenMessages-2.htm

#   Command    	        // 1*8 bits
#   version    	        // 1*8 bits
#   zeros    	        // 20*8 bits

packetProtocol = "RipNg"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Command", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Version", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Zeros", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "IPv6 Prefix", 128, PacketConstants.IPV6_ADDRESS, None, False, "", None, True],
    [1, "Route Tag", 2 * 8, PacketConstants.INTEGER, None, False, "", None, True],
    [1, "Prefix Length", 1 * 8, PacketConstants.INTEGER, None, False, "", None, True],
    [1, "Metric", 1 * 8, PacketConstants.INTEGER, None, False, "", None, True]
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("Ethernet2UdpIpV6Mpls" + tag_type + "Packet", "Ethernet2", "UdpIpV6Mpls" + tag_type +
                              "Packet", packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2UdpIpV6Mpls" + tag_type + "Packet", "Ethernet2", "UdpIpV6Mpls" + tag_type +
                              "Packet", packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2UdpIpVMpls" + tag_type + "Packet", "Ethernet2", "UdpIpV6Mpls" + tag_type +
                              "Packet", packetProtocol, packetFields, tag_type)

    GenScript.end_packet(packetProtocol, packetFields)
