from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# label = 20 bites
# exp   = 3 bits
# s-bit = 1 bit
# ttl   - 8 bits


packetProtocol = "Mpls"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "label", 20, PacketConstants.INTEGER, None, False, "", None],
    [1, "experimental bits", 3, PacketConstants.INTEGER, None, False, "", None],
    [1, "bottom of label stack", 1, PacketConstants.INTEGER, None, False, "", None],
    [1, "ttl", 8, PacketConstants.INTEGER, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2" + tag_type + "Packet", "Ethernet2", "Packet", packetProtocol, packetFields,
                              tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2" + tag_type + "Packet", "Ethernet2", tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2" + tag_type + "Packet", "Ethernet2", tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
