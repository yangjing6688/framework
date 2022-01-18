from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IpV6MplsTaggedPacket import Ethernet2IpV6MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader


class Ethernet2TcpIpV6MplsTaggedPacket(Ethernet2IpV6MplsTaggedPacket, TcpPacketHeader):
    def __init__(self):
        super(Ethernet2TcpIpV6MplsTaggedPacket, self).__init__()
        TcpPacketHeader.__init__(self)
        self.set_name("Ethernet2TcpIpV6MplsTaggedPacket")

    def to_packet_string(self):
        return super(Ethernet2TcpIpV6MplsTaggedPacket, self).to_packet_string() + \
            TcpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2TcpIpV6MplsTaggedPacket, self).build()
        TcpPacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2TcpIpV6MplsTaggedPacket, self).get_header_length() + self.HEADER_SIZE_TCP

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2TcpIpV6MplsTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(TcpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2TcpIpV6MplsTaggedPacket, self).set_payload(payload)
        TcpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2TcpIpV6MplsTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + TcpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2TcpIpV6MplsTaggedPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        TcpPacketHeader.config_thirdparty_traffic_generator_stream_tcp(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
