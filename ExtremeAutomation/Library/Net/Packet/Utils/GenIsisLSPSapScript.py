from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   isis.lsp.pdu_length     		// 2*8 bits
#   isis.lsp.remaining_life     		// 2*8 bits
#   isis.lsp.lsp_id     		// 8*8 bits
#   isis.lsp.sequence_number     		// 4*8 bits
#   isis.lsp.checksum     		// 2*8 bits

# dynamic TLVs after this

packetProtocol = "LSP"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "pdu_length", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "remaining_life", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "lsp_id", 8 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "sequence_number", 4 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "checksum", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Sap" + tag_type + "Packet", "Sap", "" + tag_type + "IsisPacket", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Sap" + tag_type + "Packet", "Sap", "" + tag_type + "IsisPacket", packetProtocol,
                              packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Sap" + tag_type + "Packet", "Sap", "" + tag_type + "IsisPacket", packetProtocol,
                              packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
