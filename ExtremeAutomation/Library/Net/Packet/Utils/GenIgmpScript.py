from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 1 byte type
# 1 byte Max Resp Time
# 2 byte check sum
# 4 byte Group Address

packetProtocol = "Igmp"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]

# Indicates the message type as follows: Membership Query (0x11), Membership Report (IGMPv1: 0x12, IGMPv2: 0x16,
#                                                                                    IGMPv3: 0x22), Leave Group (0x17)
packetFields = [
    [1, "type", 8, PacketConstants.INTEGER, None, False, "", {0x11: "Membership Query ",
                                                              0x12: "Membership Report (IGMPv1)",
                                                              0x16: "Membership Report (IGMPv2)",
                                                              0x22: "Membership Report (IGMPv3)",
                                                              0x17: "Leave Group"}],
    [2, "maxresptime", 8, PacketConstants.INTEGER, None, False, "", None],
    [3, "checksum", 16, PacketConstants.INTEGER, None, False, "", None],
    [4, "groupaddress", 32, PacketConstants.IPV4_ADDRESS, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    GenScript.generate_packet("Ethernet2IpV4Packet", "Ethernet2", "IpV4Packet", packetProtocol, packetFields, "")
    GenScript.generate_packet("Ethernet2IpV4TaggedPacket", "Ethernet2", "IpV4TaggedPacket", packetProtocol,
                              packetFields, "Tagged")
    GenScript.generate_packet("Ethernet2IpV4VlanStackPacket", "Ethernet2", "IpV4VlanStackPacket", packetProtocol,
                              packetFields, "VlanStack")
    GenScript.end_packet(packetProtocol, packetFields)
