from ExtremeAutomation.Library.Net.Packet.Utils import GenScript

#   public final static int PROTOCOL_ID = assignTag();            // 16 bits
#   public final static int VERSION = assignTag();                //  8 bits
#   public final static int MESSAGE_TYPE = assignTag();           //  8 bits
#   public final static int FLAGS = assignTag();                  //  8 bits
#   public final static int ROOT_PRIORITY = assignTag();          // 16 bits
#   public final static int ROOT_MAC = assignTag();               // 48 bits
#   public final static int COST = assignTag();                   // 32 bits
#   public final static int BRIDGE_PRIORITY = assignTag();        // 16 bits
#   public final static int BRIDGE_MAC = assignTag();             // 48 bits
#   public final static int PORT_ID = assignTag();                // 16 bits
#   public final static int AGE = assignTag();                    // 16 bits
#   public final static int MAX_AGE = assignTag();                // 16 bits
#   public final static int HELLO_TIMER = assignTag();            // 16 bits
#   public final static int FORWARD_DELAY = assignTag();          // 16 bits


packetProtocol = "SpanningTree"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    parentNameStart = "Ieee802LlcBpdu"
    packetNameStartBeforeProtocol = "Ieee802Llc"
    packetNameEndAfterProtocol = "Bpdu"
    GenScript.generate_packet(parentNameStart + tag_type + "Packet", packetNameStartBeforeProtocol,
                              packetNameEndAfterProtocol + tag_type + "Packet", packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet(parentNameStart + tag_type + "Packet", packetNameStartBeforeProtocol,
                              packetNameEndAfterProtocol + tag_type + "Packet", packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet(parentNameStart + tag_type + "Packet", packetNameStartBeforeProtocol,
                              packetNameEndAfterProtocol + tag_type + "Packet", packetProtocol, packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
