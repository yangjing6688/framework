from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   // public final static Integer PROTOCOL_ID = new Integer(0x0888E);
#   public final static int RADIUS_CODE = assignTag();                  // 1 byte
#   public final static int RADIUS_ID = assignTag();                  // 1 byte
# public final static int RADIUS_LENGTH = assignTag();                   // 2 byte2
# public final static int RADIUS_AUTHENTICATOR = assignTag();                  // 1 byte
# public final static int RADIUS_ATTRIBUTE_VALUE_PAIRS = assignTag();                   // 1 byte


packetProtocol = "Radius"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "code", 8, PacketConstants.INTEGER, None, False, "", None],
    [2, "id", 8, PacketConstants.INTEGER, None, False, "", None],
    [3, "length", 16, PacketConstants.INTEGER, None, False, "", None],
    [4, "authenticator", 8, PacketConstants.INTEGER, None, False, "", None],
    [4, "attribute value pair", 8, PacketConstants.INTEGER, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2UdpIpV4" + tag_type + "Packet", "Ethernet2", "UdpIpV4Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2UdpIpV4" + tag_type + "Packet", "Ethernet2", "UdpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2UdpIpV4" + tag_type + "Packet", "Ethernet2", "UdpIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2UdpIpV6" + tag_type + "Packet", "Ethernet2", "UdpIpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
