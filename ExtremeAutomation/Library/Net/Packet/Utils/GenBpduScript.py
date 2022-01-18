from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

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


packetProtocol = "Bpdu"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "protocol id", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "version", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "message type", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "flags", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "root priority", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "root mac", 48, PacketConstants.ENET_ADDRESS, None, False, "", None],
    [1, "cost", 32, PacketConstants.INTEGER, None, False, "", None],
    [1, "bridge priority", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "bridge mac", 48, PacketConstants.ENET_ADDRESS, None, False, "", None],
    [1, "port id", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "age", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "max age", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "hello timer", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "forward delay", 16, PacketConstants.INTEGER, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ieee802Llc" + tag_type + "Packet", "Ieee802Llc", "" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ieee802Llc" + tag_type + "Packet", "Ieee802Llc", "" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ieee802Llc" + tag_type + "Packet", "Ieee802Llc", "" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
