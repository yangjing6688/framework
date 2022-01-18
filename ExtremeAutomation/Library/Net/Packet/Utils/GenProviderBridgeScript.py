from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
# http://www.tcpipguide.com/free/t_BGPConnectionEstablishmentOpenMessages-2.htm

#   flags    	        // 1*8 bits
#   isid    	        // 3*8 bits


packetProtocol = "ProviderBackboneBridge"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Flag Priority", 3, PacketConstants.INTEGER, None, False, "", None],
    [1, "Flag DROP", 1, PacketConstants.INTEGER, None, False, "", None],
    [1, "Flag NCA", 1, PacketConstants.INTEGER, None, False, "", None],
    [1, "Flag Res1", 1, PacketConstants.INTEGER, None, False, "", None],
    [1, "Flag Res2", 2, PacketConstants.INTEGER, None, False, "", None],
    [1, "iSID", 3 * 8, PacketConstants.INTEGER, None, False, "", None]
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2" + tag_type + "Packet", "Ethernet2", "" + tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2" + tag_type + "Packet", "Ethernet2", "" + tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2" + tag_type + "Packet", "Ethernet2", "" + tag_type + "Packet", packetProtocol,
                              packetFields, tag_type)

    GenScript.end_packet(packetProtocol, packetFields)
