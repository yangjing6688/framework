from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   ospf.db.interface_mtu   	        // 2*8 bits
#   ospf.v2.options         	        // 1*8 bits
#   ospf.dbd   	                        // 1*8 bits
#   ospf.db.dd_sequence      	        // 4*8 bits
#   ospf.lsa.age      	        // 2*8 bits
#   ospf.v2.options      	        // 1*8 bits
#   ospf.lsa      	        // 1*8 bits
#   ospf.lsa.id      	        // 4*8 bits
#   ospf.advrouter      	        // 4*8 bits
#   ospf.lsa.seqnum      	        // 4*8 bits
#   ospf.lsa.chksum      	        // 2*8 bits
#   ospf.lsa.length      	        // 2*8 bits


packetProtocol = "DBDescription"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Interface MTU", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Options", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "DB Descript", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "DD Sequence", 4 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "link state age", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "link state options", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "link state type", 1 * 8, PacketConstants.INTEGER, None, False, "", {1: "Router links",
                                                                             2: "Network links",
                                                                             3: "Summary link(IP network)",
                                                                             4: "Summary link(ASBR)",
                                                                             5: "AS external link}"}],
    [1, "link state id", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [1, "advertising router", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [1, "sequence number", 4 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "checksum", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "length", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
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
