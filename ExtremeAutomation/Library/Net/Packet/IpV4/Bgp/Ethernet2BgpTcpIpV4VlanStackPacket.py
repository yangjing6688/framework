from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4VlanStackPacket import Ethernet2TcpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BgpPacketHeader import BgpPacketHeader


class Ethernet2BgpTcpIpV4VlanStackPacket(Ethernet2TcpIpV4VlanStackPacket, BgpPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2BgpTcpIpV4VlanStackPacket, self).__init__(num_tags)
        BgpPacketHeader.__init__(self)
        self.set_name("Ethernet2BgpTcpIpV4VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2BgpTcpIpV4VlanStackPacket, self).to_packet_string() + \
            BgpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2BgpTcpIpV4VlanStackPacket, self).build()
        BgpPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2BgpTcpIpV4VlanStackPacket, self).build()
        return super(Ethernet2BgpTcpIpV4VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_BGP

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2BgpTcpIpV4VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(BgpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2BgpTcpIpV4VlanStackPacket, self).set_payload(payload)
        BgpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2BgpTcpIpV4VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + BgpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2BgpTcpIpV4VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        BgpPacketHeader.config_thirdparty_traffic_generator_stream_bgp(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
