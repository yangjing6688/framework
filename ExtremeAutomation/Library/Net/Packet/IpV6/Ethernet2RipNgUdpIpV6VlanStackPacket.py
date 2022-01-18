from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2UdpIpV6VlanStackPacket import Ethernet2UdpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RipNgPacketHeader import RipNgPacketHeader


class Ethernet2RipNgUdpIpV6VlanStackPacket(Ethernet2UdpIpV6VlanStackPacket, RipNgPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2RipNgUdpIpV6VlanStackPacket, self).__init__(num_tags)
        RipNgPacketHeader.__init__(self)
        self.set_name("Ethernet2RipNgUdpIpV6VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2RipNgUdpIpV6VlanStackPacket, self).to_packet_string() + \
            RipNgPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2RipNgUdpIpV6VlanStackPacket, self).build()
        RipNgPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2RipNgUdpIpV6VlanStackPacket, self).build()
        return super(Ethernet2RipNgUdpIpV6VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_RIPNG

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2RipNgUdpIpV6VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(RipNgPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2RipNgUdpIpV6VlanStackPacket, self).set_payload(payload)
        RipNgPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2RipNgUdpIpV6VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + RipNgPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2RipNgUdpIpV6VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        RipNgPacketHeader.config_thirdparty_traffic_generator_stream_ripng(self, tgen_type, generator_ref, port_string,
                                                                           stream_id, **kwargs)
