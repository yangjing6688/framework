from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# csnp.reserved1   8 bits
# csnp.hdrlen  8 bits
# csnp.reserved2 8 bits
# csnp.idlen  8 bits
# csnp.pdutype 8 bits
# csnp.reserved3 8 bits
# csnp.reserved4 8 bits
# csnp.reserved5 8 bits
# csnp.pdulen 2*8 bits
# dbp.idsource 6*8 bits
# csnp.reserved6 8 bits

# csnp.idsource 6*8 bits
# csnp.idpnode 8 bits
# csnp.num 4*8 bits

# csnp.seqnum 4*8 bits
# csnp.checksum 2*8 bits

packetProtocol = "DbsyncDvrCsnp"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [

    [6, "CSNP Reserved 1", 8, PacketConstants.INTEGER, None, False, "", None],
    [7, "CSNP Header Length", 8, PacketConstants.INTEGER, None, False, "", None],
    [8, "CSNP Reserved 2", 8, PacketConstants.INTEGER, None, False, "", None],
    [9, "CSNP ID Length", 8, PacketConstants.INTEGER, None, False, "", None],
    [10, "CSNP PDU Type", 8, PacketConstants.INTEGER, None, False, "", None],
    [11, "CSNP Reserved 3", 8, PacketConstants.INTEGER, None, False, "", None],
    [12, "CSNP Reserved 4", 8, PacketConstants.INTEGER, None, False, "", None],
    [13, "CSNP Reserved 5", 8, PacketConstants.INTEGER, None, False, "", None],
    [14, "CSNP PDU Length", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [15, "CSNP DBP Source", 6 * 8, PacketConstants.INTEGER, None, False, "", None],
    [21, "CSNP Reserved 6", 8, PacketConstants.INTEGER, None, False, "", None],

    [16, "CSNP Start ID Source", 6 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [17, "CSNP Start ID Node", 8, PacketConstants.INTEGER, None, False, "", None],
    [18, "CSNP Start ID Number", 4 * 8, PacketConstants.INTEGER, None, False, "", None],

    [16, "CSNP End ID Source", 6 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [17, "CSNP End ID Node", 8, PacketConstants.INTEGER, None, False, "", None],
    [18, "CSNP End ID Number", 4 * 8, PacketConstants.INTEGER, None, False, "", None],

]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    GenScript.generate_packet("Ethernet2Packet", "Ethernet2", "Packet", packetProtocol, packetFields, "")
    GenScript.generate_packet("Ethernet2TaggedPacket", "Ethernet2", "TaggedPacket", packetProtocol, packetFields,
                              "Tagged")
    GenScript.generate_packet("Ethernet2VlanStackPacket", "Ethernet2", "VlanStackPacket", packetProtocol, packetFields,
                              "VlanStack")
    GenScript.end_packet(packetProtocol, packetFields)
