from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4TaggedPacket import Ethernet2UdpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DnsPacketHeader import DnsPacketHeader


class Ethernet2DnsUdpIpV4TaggedPacket(Ethernet2UdpIpV4TaggedPacket, DnsPacketHeader):
    def __init__(self):
        super(Ethernet2DnsUdpIpV4TaggedPacket, self).__init__()
        DnsPacketHeader.__init__(self)
        self.set_name("Ethernet2DnsUdpIpV4TaggedPacket")

    def to_packet_string(self):
        return super(Ethernet2DnsUdpIpV4TaggedPacket, self).to_packet_string() + \
            DnsPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2DnsUdpIpV4TaggedPacket, self).build()
        DnsPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2DnsUdpIpV4TaggedPacket, self).build()
        return super(Ethernet2DnsUdpIpV4TaggedPacket, self).get_header_length() + self.HEADER_SIZE_DNS

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2DnsUdpIpV4TaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(DnsPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2DnsUdpIpV4TaggedPacket, self).set_payload(payload)
        DnsPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2DnsUdpIpV4TaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + DnsPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2DnsUdpIpV4TaggedPacket, self).config_thirdparty_traffic_generator_stream(tgen_type,
                                                                                                generator_ref,
                                                                                                port_string, stream_id,
                                                                                                **kwargs)
        DnsPacketHeader.config_thirdparty_traffic_generator_stream_dns(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
