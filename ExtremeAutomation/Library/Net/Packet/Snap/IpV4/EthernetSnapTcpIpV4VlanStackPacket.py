from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapIpV4VlanStackPacket import \
    EthernetSnapIpV4VlanStackPacket


class EthernetSnapTcpIpV4VlanStackPacket(EthernetSnapIpV4VlanStackPacket, TcpPacketHeader):
    def __init__(self, num_tags):
        super(EthernetSnapTcpIpV4VlanStackPacket, self).__init__(num_tags)
        TcpPacketHeader.__init__(self)
        self.set_name("EthernetSnapTcpIpV4VlanStackPacket")

    def to_packet_string(self):
        return super(EthernetSnapTcpIpV4VlanStackPacket, self).to_packet_string() + \
            TcpPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapTcpIpV4VlanStackPacket, self).build()
        TcpPacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetSnapTcpIpV4VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_TCP  # + options

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapTcpIpV4VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(TcpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapTcpIpV4VlanStackPacket, self).set_payload(payload)
        TcpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapTcpIpV4VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + TcpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapTcpIpV4VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        TcpPacketHeader.config_thirdparty_traffic_generator_stream_tcp(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
