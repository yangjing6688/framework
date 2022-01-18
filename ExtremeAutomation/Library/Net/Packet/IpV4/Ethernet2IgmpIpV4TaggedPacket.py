from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4TaggedPacket import Ethernet2IpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IgmpPacketHeader import IgmpPacketHeader


class Ethernet2IgmpIpV4TaggedPacket(Ethernet2IpV4TaggedPacket, IgmpPacketHeader):
    def __init__(self):
        super(Ethernet2IgmpIpV4TaggedPacket, self).__init__()
        IgmpPacketHeader.__init__(self)
        self.set_name("Ethernet2IgmpIpV4TaggedPacket")

    def to_packet_string(self):
        return super(Ethernet2IgmpIpV4TaggedPacket, self).to_packet_string() + \
            IgmpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2IgmpIpV4TaggedPacket, self).build()
        IgmpPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2IgmpIpV4TaggedPacket, self).build()
        return super(Ethernet2IgmpIpV4TaggedPacket, self).get_header_length() + self.HEADER_SIZE_IGMP

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2IgmpIpV4TaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(IgmpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2IgmpIpV4TaggedPacket, self).set_payload(payload)
        IgmpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2IgmpIpV4TaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IgmpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2IgmpIpV4TaggedPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        IgmpPacketHeader.config_thirdparty_traffic_generator_stream_igmp(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)

    def configure_packet_checksum_fields(self):
        parent_header_legth = super(Ethernet2IgmpIpV4TaggedPacket, self).get_header_length()
        self.calculate_igmp_checksum(parent_header_legth)
        super(Ethernet2IgmpIpV4TaggedPacket, self).configure_packet_checksum_fields()
