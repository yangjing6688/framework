from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   isis.lsp.pdu_length     		// 2*8 bits
#   isis.csnp.source_id     		// 7*8 bits
#   isis.csnp.start_lsp_id     		// 8*8 bits
#   isis.csnp.end_lsp_id     		// 8*8 bits

# dynamic LSPs after this

packetProtocol = "SNP"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "pdu_length", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "source_id", 7 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [1, "start_lsp_id", 8 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [1, "end_lsp_id", 8 * 8, PacketConstants.HEX_STRING, None, False, "", None],
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
