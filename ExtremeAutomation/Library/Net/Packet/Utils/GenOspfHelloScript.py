from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   ospf.hello.network_mask    	        // 4*8 bits
#   ospf.hello.hello_interval           // 2*8 bits
#   ospf.v2.options    	                // 8 bits
#   ospf.hello.router_priority    	    // 8 bits
#   ospf.hello.router_dead_interval    	// 4*8 bits
#   ospf.hello.designated_router    	// 4*8 bits
#   ospf.hello.backup_designated_router // 4*8 bits
#   ospf.hello.active_neighbor    	    // 4*8 bits


packetProtocol = "Hello"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "network mask", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [1, "hello interval", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "options", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "router priority", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "router_dead_interval", 4 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "designated_router", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [1, "backup_designated_router", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [1, "active_neighbor", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "OspfIpV4Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "OspfIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "OspfIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    # tag_type = ""
    # generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6Packet", packetProtocol, packetFields,
    #                 tag_type)
    # tag_type = "Tagged"
    # generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet", packetProtocol,
    #                 packetFields, tag_type)
    # tag_type = "VlanStack"
    # generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet", packetProtocol,
    #                 packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
