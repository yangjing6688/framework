from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
# http://www.tcpipguide.com/free/t_BGPConnectionEstablishmentOpenMessages-2.htm

#   bgp.marker    	        // 16*8 bits
#   bgp.length    	        // 2*8 bits
#   bgp.type    	        // 1*8 bits


packetProtocol = "Dns"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Length", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [2, "Transaction Id", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [3, "Flags", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [4, "Questions", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [5, "Answers", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [6, "Authority", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [7, "Additional", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [8, "Query Name", 8*8, PacketConstants.HEX_STRING, None, False, "", None],
    [9, "Query Type", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [10, "Query Class", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [11, "Response Name", 8*8, PacketConstants.HEX_STRING, None, False, "", None],
    [12, "Response Type", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [13, "Response Class", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [14, "Response Time To Live", 4*8, PacketConstants.INTEGER, None, False, "", None],
    [15, "Response Data Length", 2*8, PacketConstants.INTEGER, None, False, "", None],
    [16, "Response Resource Data", 8*8, PacketConstants.HEX_STRING, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2TcpIpV4" + tag_type + "Packet", "Ethernet2", "TcpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2TcpIpV4" + tag_type + "Packet", "Ethernet2", "TcpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2TcpIpV4" + tag_type + "Packet", "Ethernet2", "TcpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("Ethernet2TcpIpV6" + tag_type + "Packet", "Ethernet2", "TcpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2TcpIpV6" + tag_type + "Packet", "Ethernet2", "TcpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2TcpIpV6" + tag_type + "Packet", "Ethernet2", "TcpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("Ethernet2UdpIpV4" + tag_type + "Packet", "Ethernet2", "UdpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2UdpIpV4" + tag_type + "Packet", "Ethernet2", "UdpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2UdpIpV4" + tag_type + "Packet", "Ethernet2", "UdpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)

    GenScript.end_packet(packetProtocol, packetFields)
