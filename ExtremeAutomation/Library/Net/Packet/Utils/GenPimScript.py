from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   pim.version  	        // 4 bits
#   pim.hdr_len  	        // 4 bits
#   pim.res_bytes           // 8 bits
#   pim.cksum               // 16 bits
#   pim.options               // 32 bits?

"""
    PacketField pf[] = packet.getPacketField();
    int value = getBufferOffset() - PIM_HEADER_LENGTH + 4;
    int number = b.length - value;
    if(number > PIM_HEADER_LENGTH)
        number = PIM_HEADER_LENGTH;
    byte[] pimbytes = new byte[number];
    System.arraycopy(b, value, pimbytes, 0, number);
    setPimParamaters(pimbytes);
"""


packetProtocol = "Pim"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Version", 4, PacketConstants.INTEGER, None, False, "", None],
    [1, "Length", 4, PacketConstants.INTEGER, None, False, "", None],
    [1, "Reserve", 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Checksum", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "Options", 32, PacketConstants.INTEGER, None, False, "", None],
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
    tag_type = ""
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
