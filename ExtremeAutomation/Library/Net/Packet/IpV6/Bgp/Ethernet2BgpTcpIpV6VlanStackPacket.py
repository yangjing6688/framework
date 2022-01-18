from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2TcpIpV6VlanStackPacket import Ethernet2TcpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BgpPacketHeader import BgpPacketHeader


class Ethernet2BgpTcpIpV6VlanStackPacket(Ethernet2TcpIpV6VlanStackPacket, BgpPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2BgpTcpIpV6VlanStackPacket, self).__init__(num_tags)
        BgpPacketHeader.__init__(self)
        self.set_name("Ethernet2BgpTcpIpV6VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2BgpTcpIpV6VlanStackPacket, self).to_packet_string() + \
            BgpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2BgpTcpIpV6VlanStackPacket, self).build()
        BgpPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2BgpTcpIpV6VlanStackPacket, self).build()
        return super(Ethernet2BgpTcpIpV6VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_BGP

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2BgpTcpIpV6VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(BgpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2BgpTcpIpV6VlanStackPacket, self).set_payload(payload)
        BgpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2BgpTcpIpV6VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + BgpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2BgpTcpIpV6VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        BgpPacketHeader.config_thirdparty_traffic_generator_stream_bgp(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
