from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 2 byte hardware type
# 2 byte protocol type
# 1 byte header length
# 1 byte protocol length
# 2 byte operation
# 6 byte SHA
# 4 byte SIP
# 6 byte THA
# 4 byte TIP

packetProtocol = "Arp"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "hardware", 16, PacketConstants.INTEGER, None, False, "", {1: "Ethernet"}],
    [2, "proto", 16, PacketConstants.INTEGER, None, False, "", None],
    [3, "id", 8, PacketConstants.INTEGER, None, False, "", None],
    [4, "seq", 8, PacketConstants.INTEGER, None, False, "", None],
    [5, "operation", 16, PacketConstants.INTEGER, None, False, "", {0: "Reserved",
                                                                    1: "REQUEST",
                                                                    2: "REPLY",
                                                                    3: "request Reverse",
                                                                    4: "reply Reverse",
                                                                    5: "DRARP Request",
                                                                    6: "DRARP Reply",
                                                                    7: "DRARP Error",
                                                                    8: "InARP Request",
                                                                    9: "InARP Reply"}],
    [6, "sender hardware address", 48, PacketConstants.ENET_ADDRESS, None, False, "", None],
    [7, "source protocol address", 32, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [8, "target hardware address", 48, PacketConstants.ENET_ADDRESS, None, False, "", None],
    [9, "target protocol address", 32, PacketConstants.IPV4_ADDRESS, None, False, "", None],
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
