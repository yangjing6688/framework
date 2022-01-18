from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IpV6MplsPacket import Ethernet2IpV6MplsPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.VrrpPacketHeader import VrrpPacketHeader


class Ethernet2VrrpIpV6MplsPacket(Ethernet2IpV6MplsPacket, VrrpPacketHeader):
    def __init__(self):
        super(Ethernet2VrrpIpV6MplsPacket, self).__init__()
        VrrpPacketHeader.__init__(self)
        self.set_name("Ethernet2VrrpIpV6MplsPacket")

    def to_packet_string(self):
        return super(Ethernet2VrrpIpV6MplsPacket, self).to_packet_string() + \
            VrrpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2VrrpIpV6MplsPacket, self).build()
        VrrpPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2VrrpIpV6MplsPacket, self).build()
        return super(Ethernet2VrrpIpV6MplsPacket, self).get_header_length() + self.HEADER_SIZE_VRRP

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2VrrpIpV6MplsPacket, self).get_hltapi_commands()
        cmd_dict.update(VrrpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2VrrpIpV6MplsPacket, self).set_payload(payload)
        VrrpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2VrrpIpV6MplsPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + VrrpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2VrrpIpV6MplsPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        VrrpPacketHeader.config_thirdparty_traffic_generator_stream_vrrp(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
