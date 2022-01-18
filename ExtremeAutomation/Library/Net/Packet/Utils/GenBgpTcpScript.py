from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
# http://www.tcpipguide.com/free/t_BGPConnectionEstablishmentOpenMessages-2.htm

#   bgp.marker    	        // 16*8 bits
#   bgp.length    	        // 2*8 bits
#   bgp.type    	        // 1*8 bits


packetProtocol = "Bgp"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Marker", 16 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Length", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Type", 1 * 8, PacketConstants.INTEGER, None, False, "", {0: "Reserved",
                                                                  1: "OPEN",
                                                                  2: "UPDATE",
                                                                  3: "NOTIFICATION",
                                                                  4: "KEEPALIVE",
                                                                  5: "ROUTE-REFRESH"}], ]
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

    GenScript.end_packet(packetProtocol, packetFields)
