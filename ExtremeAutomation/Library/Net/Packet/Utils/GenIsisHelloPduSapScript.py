from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   isis.hello.circuit_type     		// 8 bits
#   isis.hello.source_id    			// 6x8 bits
#   isis.hello.holding_timer     		// 2x8 bits
#   isis.hello.pdu_length    		    // 2x8 bits
#   isis.hello.priority    	            // 8 bits
#   isis.hello.lan_id     			    // 7x8 bits
# dynamic TLVs after this

packetProtocol = "HelloPdu"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "circuit_type", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "source_id", 6 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [1, "holding_timer", 2 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [1, "pdu_length", 2 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [1, "priority", 8, PacketConstants.HEX_STRING, None, False, "", None],
    [1, "lan_id", 7 * 8, PacketConstants.HEX_STRING, None, False, "", None],
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
