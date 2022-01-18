from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2UdpIpV6VlanStackPacket import Ethernet2UdpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DnsPacketHeader import DnsPacketHeader


class Ethernet2DnsUdpIpV6VlanStackPacket(Ethernet2UdpIpV6VlanStackPacket, DnsPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2DnsUdpIpV6VlanStackPacket, self).__init__(num_tags)
        DnsPacketHeader.__init__(self)
        self.set_name("Ethernet2DnsUdpIpV6VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2DnsUdpIpV6VlanStackPacket, self).to_packet_string() + \
            DnsPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2DnsUdpIpV6VlanStackPacket, self).build()
        DnsPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2DnsUdpIpV6VlanStackPacket, self).build()
        return super(Ethernet2DnsUdpIpV6VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_DNS

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2DnsUdpIpV6VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(DnsPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2DnsUdpIpV6VlanStackPacket, self).set_payload(payload)
        DnsPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2DnsUdpIpV6VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + DnsPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2DnsUdpIpV6VlanStackPacket, self).config_thirdparty_traffic_generator_stream(tgen_type,
                                                                                                   generator_ref,
                                                                                                   port_string,
                                                                                                   stream_id, **kwargs)
        DnsPacketHeader.config_thirdparty_traffic_generator_stream_dns(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
