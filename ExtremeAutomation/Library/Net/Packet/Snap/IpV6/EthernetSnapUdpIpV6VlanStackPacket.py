from ExtremeAutomation.Library.Net.Packet.PacketHeaders.UdpPacketHeader import UdpPacketHeader
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapIpV6VlanStackPacket import \
    EthernetSnapIpV6VlanStackPacket


class EthernetSnapUdpIpV6VlanStackPacket(EthernetSnapIpV6VlanStackPacket, UdpPacketHeader):
    def __init__(self, num_tags):
        super(EthernetSnapUdpIpV6VlanStackPacket, self).__init__(num_tags)
        UdpPacketHeader.__init__(self)
        self.set_name("EthernetSnapUdpIpV6VlanStackPacket")

    def to_packet_string(self):
        return super(EthernetSnapUdpIpV6VlanStackPacket, self).to_packet_string() + \
            UdpPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapUdpIpV6VlanStackPacket, self).build()
        UdpPacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetSnapUdpIpV6VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_UDP

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapUdpIpV6VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(UdpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapUdpIpV6VlanStackPacket, self).set_payload(payload)
        UdpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapUdpIpV6VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + UdpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapUdpIpV6VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        UdpPacketHeader.config_thirdparty_traffic_generator_stream_udp(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
