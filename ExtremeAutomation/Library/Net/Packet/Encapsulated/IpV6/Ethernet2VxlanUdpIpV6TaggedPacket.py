from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2UdpIpV6TaggedPacket import Ethernet2UdpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.VxlanPacketHeader import VxlanPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket


default_packet = EthernetPacket()


class Ethernet2VxlanUdpIpV6TaggedPacket(Ethernet2UdpIpV6TaggedPacket, VxlanPacketHeader):
    def __init__(self, innerpacket=default_packet):
        super(Ethernet2VxlanUdpIpV6TaggedPacket, self).__init__()
        VxlanPacketHeader.__init__(self)
        self.set_vxlan_inner_packet(innerpacket)
        self.set_name("Ethernet2VxlanUdpIpV6TaggedPacket")

    def to_packet_string(self):
        return super(Ethernet2VxlanUdpIpV6TaggedPacket, self).to_packet_string() + \
            VxlanPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2VxlanUdpIpV6TaggedPacket, self).build()
        VxlanPacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2VxlanUdpIpV6TaggedPacket, self).get_header_length() + self.HEADER_SIZE_VXLAN + \
            self.get_vxlan_inner_packet_length()

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2VxlanUdpIpV6TaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(VxlanPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2VxlanUdpIpV6TaggedPacket, self).set_payload(payload)
        VxlanPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2VxlanUdpIpV6TaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + VxlanPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2VxlanUdpIpV6TaggedPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        VxlanPacketHeader.config_thirdparty_traffic_generator_stream_vxlan(self, tgen_type, generator_ref, port_string,
                                                                           stream_id, **kwargs)
