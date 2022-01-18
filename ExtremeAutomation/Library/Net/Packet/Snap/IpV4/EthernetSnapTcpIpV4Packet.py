from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapIpV4Packet import EthernetSnapIpV4Packet


class EthernetSnapTcpIpV4Packet(EthernetSnapIpV4Packet, TcpPacketHeader):
    def __init__(self):
        super(EthernetSnapTcpIpV4Packet, self).__init__()
        TcpPacketHeader.__init__(self)
        self.set_name("EthernetSnapTcpIpV4Packet")

    def to_packet_string(self):
        return super(EthernetSnapTcpIpV4Packet, self).to_packet_string() + \
            TcpPacketHeader.to_packet_string(self)

    def get_header_length(self):
        return super(EthernetSnapTcpIpV4Packet, self).get_header_length() + self.HEADER_SIZE_TCP  # + options

    def build(self):
        super(EthernetSnapTcpIpV4Packet, self).build()
        TcpPacketHeader.build(self)

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapTcpIpV4Packet, self).get_hltapi_commands()
        cmd_dict.update(TcpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapTcpIpV4Packet, self).set_payload(payload)
        TcpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapTcpIpV4Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + TcpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapTcpIpV4Packet, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                          port_string, stream_id,
                                                                                          **kwargs)
        TcpPacketHeader.config_thirdparty_traffic_generator_stream_tcp(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
