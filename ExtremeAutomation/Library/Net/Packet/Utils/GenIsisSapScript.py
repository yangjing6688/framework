from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   isis.irpd     			// 8 bits
#   isis.len     			// 8 bits
#   isis.version     		// 8 bits
#   isis.sysid_len     		// 8 bits
#   isis.type.reserved     	// 8 bits
#   isis.type     			// 8 bits
#   isis.version2     		// 8 bits
#   isis.reserved     		// 8 bits
#   isis.max_area_adr     	// 8 bits


packetProtocol = "Isis"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "intradomain routing protocol discriminator", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "length indicator", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "version protocol id extension", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "id length", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "reserved", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "pdu type", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "version", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "reserved 2", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "max area addresses", 8, PacketConstants.INTEGER, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Sap" + tag_type + "Packet", "Sap", "" + tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Sap" + tag_type + "Packet", "Sap", "" + tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Sap" + tag_type + "Packet", "Sap", "" + tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
