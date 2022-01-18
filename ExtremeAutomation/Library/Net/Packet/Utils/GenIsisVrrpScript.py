from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

#   vrrp.ver     		// 4 bits
#   vrrp.type     		// 4 bits
#   vrrp.virt_rtr_id     	// 1*8 bits
#   vrrp.prio     		    // 1*8 bits
#   vrrp.addr_count     	// 1*8 bits
#   vrrp.auth_type     		// 1*8 bits
#   vrrp.adver_int     		// 1*8 bits
#   vrrp.checksum     		// 2*8 bits
#   vrrp.ip_addres    		// 4*8 bits
#        		// 1*8 bits

# dynamic TLVs after this

packetProtocol = "Vrrp"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "Version", 4, PacketConstants.INTEGER, None, False, "", None],
    [1, "Type", 4, PacketConstants.INTEGER, None, False, "", None],
    [1, "Virtual Router ID", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Priority", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "IP Address Count", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Authentication Type", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Advertisement Interval", 1 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "Checksum", 2 * 8, PacketConstants.INTEGER, None, False, "", None],
    [1, "IP Addresses", 4 * 8, PacketConstants.IPV4_ADDRESS, None, False, "", None],
    [1, "Authentication Data", 4 * 8, PacketConstants.HEX_STRING, None, False, "", None],
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    tag_type = ""
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "IpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "IpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2IpV4" + tag_type + "Packet", "Ethernet2", "IpV4" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = ""
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "Tagged"
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    tag_type = "VlanStack"
    GenScript.generate_packet("Ethernet2IpV6" + tag_type + "Packet", "Ethernet2", "IpV6" + tag_type + "Packet",
                              packetProtocol, packetFields, tag_type)
    GenScript.end_packet(packetProtocol, packetFields)
