from ExtremeAutomation.Library.Net.Packet.Utils import GenScript
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants

# 2	Checksum (always 0xFFFF - no checksum)
# 2	Packet Length (including the IPX header)
# 1	Transport Control (hop count)
# 1	Packet Type
# 12	Destination address
# Octets	Field
# 4	Network number
# 6	Node number
# 2	Socket number
# 12	Source address
# Octets	Field
# 4	Network number
# 6	Node number
# 2	Socket number
packetProtocol = "Ipx"
# [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
packetFields = [
    [1, "checksum", 16, PacketConstants.INTEGER, None, False, "", None],
    [2, "packet length", 16, PacketConstants.INTEGER, None, "ipx config -lengthOverride true\nipx config -length",
     PacketConstants.INTEGER, None],
    [3, "transport control", 8, PacketConstants.INTEGER, None, "ipx config -transportControl", PacketConstants.INTEGER,
     None],
    [4, "packet type", 8, PacketConstants.INTEGER, None, "ipx config -packetType", PacketConstants.INTEGER,
     {0: "Unknown", "1": "RIP", "2": "Echo Packet", "3": "Error Packet", "4": "PEP", "5": "SPX", "17": "NCP"}],
    [5, "destination network", 32, PacketConstants.HEX_STRING, None, "ipx config -destNetwork",
     PacketConstants.HEX_STRING, None],
    [6, "destination node", 48, PacketConstants.HEX_STRING, None, "ipx config -destNode", PacketConstants.HEX_STRING,
     None],
    [7, "destination socket", 16, PacketConstants.INTEGER, None, "ipx config -destSocket", PacketConstants.INTEGER,
     None],
    [8, "source network", 32, PacketConstants.HEX_STRING, None, "ipx config -sourceNetwork", PacketConstants.HEX_STRING,
     None],
    [9, "source node", 48, PacketConstants.HEX_STRING, None, "ipx config -sourceNode", PacketConstants.HEX_STRING,
     None],
    [10, "source socket", 16, PacketConstants.INTEGER, None, "ipx config -sourceSocket", PacketConstants.INTEGER, None]
]
if __name__ == "__main__":
    GenScript.generate_packet_header(packetProtocol, packetFields)
    # generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    GenScript.generate_packet("LlcPacket", "Ieee802_2", "Packet", packetProtocol, packetFields, "")
    GenScript.generate_packet("LlcTaggedPacket", "Ieee802_2", "Packet", packetProtocol, packetFields, "Tagged")
    GenScript.generate_packet("LlcVlanStackPacket", "Ieee802_2", "Packet", packetProtocol, packetFields, "VlanStack")
    GenScript.end_packet(packetProtocol, packetFields)
