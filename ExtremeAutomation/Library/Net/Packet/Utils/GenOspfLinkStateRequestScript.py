from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   ospf.lsa    	        // 4*8 bits
#   ospf.link_state_id           // 4*8 bits
#   ospf.advrouter    	                // 4*8 bits


packetProtocol = "LinkStateRequest"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "lsa", 4 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "link state id", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [1, "advertising router", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
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
