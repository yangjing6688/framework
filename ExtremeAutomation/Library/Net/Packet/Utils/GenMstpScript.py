from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# public final static int VERSION_1_LENGTH = assignTag(); //8 bits
# public final static int VERSION_3_LENGTH = assignTag(); //16 bits
# public final static int VERSION_3_ID_FORMAT_SELECTOR = assignTag(); //8 bits
# public final static int VERSION_3_NAME = assignTag(); //256 bits
# public final static int VERSION_3_REVISION = assignTag(); //16 bits
# public final static int VERSION_3_DIGEST = assignTag(); //128 bits
# public final static int VERSION_3_CIST_INTERNAL_ROOT_PATH_COST = assignTag(); //32 bits
# public final static int VERSION_3_CIST_BRIDGE_INTERNAL_PRIORITY = assignTag(); //16 bits
# public final static int VERSION_3_CIST_BRIDGE_INTERNAL_SYSTEM_ID = assignTag(); //48 bits
# public final static int VERSION_3_CIST_REMAINING_HOPS = assignTag(); //8 bits


packetProtocol = "Mstp"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "version 1 length", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "version 3 length", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "version 3 id format", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "version 3 name", 256, PacketConstants.ASCII_STRING, None, False, "", None],
    [1, "version 3 revision", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "version 3 digest", 128, PacketConstants.HEX_STRING, None, False, "", None],
    [1, "version 3 cist internal root path cost", 32, PacketConstants.INTEGER, None, False, "", None],
    [1, "version 3 cist bridge internal priority", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "version 3 cist bridge internal system id", 48, PacketConstants.ENET_ADDRESS, None, False, "", None],
    [1, "version 3 cist remaining hops", 8, PacketConstants.INTEGER, None, False, "", None]
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    parentNameStart = "Sap"
    packetNameStartBeforeProtocol = "Sap"
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
