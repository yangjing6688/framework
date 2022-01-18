from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 1 byte type
# 1 byte code
# 2 byte check sum
# 2 byte id
# 2 byte seq
# n byte data

packetProtocol = "Icmp"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "type", 8, PacketConstants.INTEGER, None, False, "", {0: "Echo Reply",
                                                              3: "Destination Unreachable",
                                                              4: "Source Quench",
                                                              5: "Redirect Message",
                                                              8: "Echo Request",
                                                              9: "Router Advertisement",
                                                              10: "Router  Solicitation",
                                                              11: "Time Exceeded",
                                                              12: "Parameter Problem Bad IP header",
                                                              13: "Timestamp",
                                                              14: "Timestamp Reply",
                                                              15: "Information Request",
                                                              16: "Information Reply",
                                                              17: "Address Mask Request",
                                                              18: "Address Mask Reply",
                                                              30: "Traceroute"}],
    [1, "code", 8, PacketConstants.INTEGER, None, False, "", {0: "Destination network unreachable",
                                                              1: "Destination host unreachable",
                                                              2: "Destination protocol unreachable",
                                                              3: "Destination port unreachable",
                                                              4: "Fragmentation required, and DF flag set",
                                                              5: "Source route failed",
                                                              6: "Destination network unknown",
                                                              7: "Destination host unknown",
                                                              8: "Source host isolated",
                                                              9: "Network administratively prohibited",
                                                              10: "Host administratively prohibited",
                                                              11: "Network unreachable for TOS",
                                                              12: "Host unreachable for TOS",
                                                              13: "Communication administratively prohibited",
                                                              14: "Host Precedence Violation",
                                                              15: "Precedence cutoff in effect"}],
    [1, "checksum", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "id", 16, PacketConstants.INTEGER, None, False, "", None],
    [1, "seq", 16, PacketConstants.INTEGER, None, False, "", None],
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
