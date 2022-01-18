from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 3 organization code
# 2 Ether Type

packetProtocol = "Snap"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "organization code", 24, PacketConstants.INTEGER, None, False, "", None],
    [2, "ether type", 16, PacketConstants.INTEGER, None, "", PacketConstants.INTEGER, None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ieee802Llc" + tag_type + "Packet", "EtherSnap", "Packet", packetProtocol, packetFields,
                              tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ieee802Llc" + tag_type + "Packet", "EtherSnap", tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ieee802Llc" + tag_type + "Packet", "EtherSnap", tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
