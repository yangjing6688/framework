from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4Packet import Ethernet2TcpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DnsPacketHeader import DnsPacketHeader


class Ethernet2DnsTcpIpV4Packet(Ethernet2TcpIpV4Packet, DnsPacketHeader):
    def __init__(self):
        super(Ethernet2DnsTcpIpV4Packet, self).__init__()
        DnsPacketHeader.__init__(self)
        self.set_name("Ethernet2DnsTcpIpV4Packet")

    def to_packet_string(self):
        return super(Ethernet2DnsTcpIpV4Packet, self).to_packet_string() + \
            DnsPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2DnsTcpIpV4Packet, self).build()
        DnsPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2DnsTcpIpV4Packet, self).build()
        return super(Ethernet2DnsTcpIpV4Packet, self).get_header_length() + self.HEADER_SIZE_DNS

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2DnsTcpIpV4Packet, self).get_hltapi_commands()
        cmd_dict.update(DnsPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2DnsTcpIpV4Packet, self).set_payload(payload)
        DnsPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2DnsTcpIpV4Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + DnsPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2DnsTcpIpV4Packet, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                          port_string, stream_id,
                                                                                          **kwargs)
        DnsPacketHeader.config_thirdparty_traffic_generator_stream_dns(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
