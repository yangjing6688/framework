from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4MplsPacket import Ethernet2IpV4MplsPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IcmpPacketHeader import IcmpPacketHeader


class Ethernet2IcmpIpV4MplsPacket(Ethernet2IpV4MplsPacket, IcmpPacketHeader):
    def __init__(self):
        super(Ethernet2IcmpIpV4MplsPacket, self).__init__()
        IcmpPacketHeader.__init__(self)
        self.set_name("Ethernet2IcmpIpV4MplsPacket")

    def to_packet_string(self):
        return super(Ethernet2IcmpIpV4MplsPacket, self).to_packet_string() + \
            IcmpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2IcmpIpV4MplsPacket, self).build()
        IcmpPacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2IcmpIpV4MplsPacket, self).get_header_length() + self.HEADER_SIZE_ICMP

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2IcmpIpV4MplsPacket, self).get_hltapi_commands()
        cmd_dict.update(IcmpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2IcmpIpV4MplsPacket, self).set_payload(payload)
        IcmpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2IcmpIpV4MplsPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IcmpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2IcmpIpV4MplsPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        IcmpPacketHeader.config_thirdparty_traffic_generator_stream_icmp(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)

    def configure_packet_checksum_fields(self):
        parent_header_legth = super(Ethernet2IcmpIpV4MplsPacket, self).get_header_length()
        self.calculate_icmp_checksum(parent_header_legth)
        super(Ethernet2IcmpIpV4MplsPacket, self).configure_packet_checksum_fields()
