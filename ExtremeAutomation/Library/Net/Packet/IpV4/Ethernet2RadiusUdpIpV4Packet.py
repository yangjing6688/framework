from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4Packet import Ethernet2UdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RadiusPacketHeader import RadiusPacketHeader


class Ethernet2RadiusUdpIpV4Packet(Ethernet2UdpIpV4Packet, RadiusPacketHeader):
    def __init__(self):
        super(Ethernet2RadiusUdpIpV4Packet, self).__init__()
        RadiusPacketHeader.__init__(self)
        self.set_name("Ethernet2RadiusUdpIpV4Packet")

    def to_packet_string(self):
        return super(Ethernet2RadiusUdpIpV4Packet, self).to_packet_string() + \
            RadiusPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2RadiusUdpIpV4Packet, self).build()
        RadiusPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2RadiusUdpIpV4Packet, self).build()
        return super(Ethernet2RadiusUdpIpV4Packet, self).get_header_length() + self.get_radius_headers_length()

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2RadiusUdpIpV4Packet, self).get_hltapi_commands()
        cmd_dict.update(RadiusPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2RadiusUdpIpV4Packet, self).set_payload(payload)
        RadiusPacketHeader.parse_bytes(self)

    def configure_packet_length_fields(self, length=False):
        super(Ethernet2RadiusUdpIpV4Packet, self).configure_packet_length_fields(length)
        length = self.get_length_int()
        parent_header_legth = super(Ethernet2RadiusUdpIpV4Packet, self).get_header_length()
        length -= parent_header_legth
        length -= 4  # this is for the fsc
        self.configure_radius_length(length)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2RadiusUdpIpV4Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + RadiusPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2RadiusUdpIpV4Packet, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        RadiusPacketHeader.config_thirdparty_traffic_generator_stream_radius(self, tgen_type, generator_ref,
                                                                             port_string, stream_id, **kwargs)
