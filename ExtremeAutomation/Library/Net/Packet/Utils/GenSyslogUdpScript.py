from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
# http://www.tcpipguide.com/free/t_BGPConnectionEstablishmentOpenMessages-2.htm

#   syslog.facility    	        // 5 bits
#   syslog.level    	        // 3 bits
#   syslog.message    	        // (rest of packet


packetProtocol = "Syslog"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Facility", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [2, "Level", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [3, "Message", 1 * 8, PacketConstants.ASCII_STRING, None, False, "", None], ]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
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
