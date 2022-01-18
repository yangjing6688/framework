from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   ospf.version    	// 8 bits
#   ospf.msg    	// 8 bits
#   ospf.packet_length    	// 2*8 bits
#   ospf.srcrouter    	// 4*8 bits
#   ospf.area_id    	// 4*8 bits
#   ospf.checksum    	// 2*8 bits
#   ospf.auth.type    	// 2*8 bits
#   ospf.auth.none    	// 8*8 bits

packetProtocol = "Ospf"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "version", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "message type", 8, PacketConstants.INTEGER, None, False, "", {1: "Hello",
                                                                      2: "Database Description",
                                                                      3: "Link State Request",
                                                                      4: "Link State Update",
                                                                      5: "Link State Acknowledgment"}],
    [1, "packet length", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "source OSPF route", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [1, "Area Id", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [1, "checksum", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "auth type", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "auth data", 8 * 8, PacketConstants.HEX_STRING, None, False, "", None],
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
