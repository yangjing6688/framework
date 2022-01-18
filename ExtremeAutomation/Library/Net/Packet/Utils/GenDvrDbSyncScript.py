from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# dbsync.version 8 bits
# dbsync.appid 4*8 bits
# dbsync.pkttype 8 bits
# dbsync.pktlen 2*8 bits
# dbsync.srcid 6*8 bits

# dbp.reserved1   8 bits
# dbp.hdrlen  8 bits
# dbp.reserved2 8 bits
# dbp.idlen  8 bits
# dbp.pdutype 8 bits
# dbp.reserved3 8 bits
# dbp.reserved4 8 bits
# dbp.reserved5 8 bits
# dbp.pdulen 2*8 bits
# dbp.remlifetime 2*8 bits

# dbp.idsource 6*8 bits
# dbp.idpnode 8 bits
# dbp.num 4*8 bits

# dbp.seqnum 4*8 bits
# dbp.checksum 2*8 bits
# dbp.reserved6 8 bits

packetProtocol = "DbsyncDvr"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Version", 8, PacketConstants.INTEGER, None, False, "", {1: "Ethernet"}],
    [2, "App Id", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [3, "Packet Type", 8, PacketConstants.INTEGER, None, False, "", None],
    [4, "Packet Length", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [5, "Source ID", 4 * 8, PacketConstants.HEX_STRING, None, False, "", None],

    [6, "DBP Reserved 1", 8, PacketConstants.INTEGER, None, False, "", None],
    [7, "DBP Header Length", 8, PacketConstants.INTEGER, None, False, "", None],
    [8, "DBP Reserved 2", 8, PacketConstants.INTEGER, None, False, "", None],
    [9, "DBP ID Length", 8, PacketConstants.INTEGER, None, False, "", None],
    [10, "DBP PDU Type", 8, PacketConstants.INTEGER, None, False, "", None],
    [11, "DBP Reserved 3", 8, PacketConstants.INTEGER, None, False, "", None],
    [12, "DBP Reserved 4", 8, PacketConstants.INTEGER, None, False, "", None],
    [13, "DBP Reserved 5", 8, PacketConstants.INTEGER, None, False, "", None],
    [14, "DBP PDU Length", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [15, "DBP Remaining Lifetime", 2 * 8, PacketConstants.INTEGER, None, False, "", None],

    [16, "DBP ID Source", 6 * 8, PacketConstants.HEX_STRING, None, False, "", None],
    [17, "DBP ID Node", 8, PacketConstants.INTEGER, None, False, "", None],
    [18, "DBP ID Number", 4 * 8, PacketConstants.INTEGER, None, False, "", None],

    [19, "DBP Sequence Number", 4 * 8, PacketConstants.INTEGER, None, False, "", None],
    [20, "DBP Checksum", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [21, "DBP Reserved 6", 8, PacketConstants.INTEGER, None, False, "", None],
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
