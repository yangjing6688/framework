from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   ospf.db.interface_mtu   	        // 2*8 bits

"""
https://github.com/wireshark/wireshark/blob/fe219637a6748130266a0b0278166046e60a2d68/epan/dissectors/packet-ospf.c
static void
dissect_ospf_ls_ack(tvbuff_t *tvb, packet_info *pinfo, int offset, proto_tree *tree, guint8 version,
                    guint16 length, guint8 address_family)
{
    int orig_offset = offset;
    DISSECTOR_ASSERT((version == OSPF_VERSION_2) || (version == OSPF_VERSION_3));
    /* the body of a LS Ack packet simply contains zero or more LSA Headers */
    while (orig_offset + length > offset) {
        if (version == OSPF_VERSION_2)
            offset = dissect_ospf_v2_lsa(tvb, pinfo, offset, tree, FALSE);
        else
            offset = dissect_ospf_v3_lsa(tvb, pinfo, offset, tree, FALSE, address_family);
    }
}
http://www.freesoft.org/CIE/RFC/1583/108.htm
        0                   1                   2                   3
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |   Version #   |       5       |         Packet length         |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                          Router ID                            |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                           Area ID                             |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |           Checksum            |             AuType            |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                       Authentication                          |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                       Authentication                          |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                                                               |
       +-                                                             -+
       |                             A                                 |
       +-                 Link State Advertisement                    -+
       |                           Header                              |
       +-                                                             -+
       |                                                               |
       +-                                                             -+
       |                                                               |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                              ...                              |
"""


packetProtocol = "LinkStateAcknowledge"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Number of LSAs", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2OspfIpV4" + tag_type + "Packet", "Ethernet2", "OspfIpV4Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2OspfIpV4" + tag_type + "Packet", "Ethernet2", "OspfIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2OspfIpV4" + tag_type + "Packet", "Ethernet2", "OspfIpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    # tag_type = ""
    # generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6Packet", packetProtocol, packetFields,
    #                 tag_type)
    # tag_type = "Tagged"
    # generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet", packetProtocol,
    #                 packetFields, tag_type)
    # tag_type = "VlanStack"
    # generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet", packetProtocol,
    #                 packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
