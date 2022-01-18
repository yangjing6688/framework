from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4VlanStackPacket import Ethernet2UdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.VxlanPacketHeader import VxlanPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket


class Ethernet2VxlanUdpIpV4VlanStackPacket(Ethernet2UdpIpV4VlanStackPacket, VxlanPacketHeader):
    def __init__(self, num_tags, innerpacket=EthernetPacket()):
        super(Ethernet2VxlanUdpIpV4VlanStackPacket, self).__init__(num_tags)
        VxlanPacketHeader.__init__(self)
        self.set_vxlan_inner_packet(innerpacket)
        self.set_name("Ethernet2VxlanUdpIpV4VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2VxlanUdpIpV4VlanStackPacket, self).to_packet_string() + \
            VxlanPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2VxlanUdpIpV4VlanStackPacket, self).build()
        VxlanPacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2VxlanUdpIpV4VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_VXLAN + \
            self.get_vxlan_inner_packet_length()

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2VxlanUdpIpV4VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(VxlanPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2VxlanUdpIpV4VlanStackPacket, self).set_payload(payload)
        VxlanPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2VxlanUdpIpV4VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + VxlanPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2VxlanUdpIpV4VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        VxlanPacketHeader.config_thirdparty_traffic_generator_stream_vxlan(self, tgen_type, generator_ref, port_string,
                                                                           stream_id, **kwargs)
