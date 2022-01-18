from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4Packet import Ethernet2UdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RipPacketHeader import RipPacketHeader


class Ethernet2RipUdpIpV4Packet(Ethernet2UdpIpV4Packet, RipPacketHeader):
    def __init__(self):
        super(Ethernet2RipUdpIpV4Packet, self).__init__()
        RipPacketHeader.__init__(self)
        self.set_name("Ethernet2RipUdpIpV4Packet")

    def to_packet_string(self):
        return super(Ethernet2RipUdpIpV4Packet, self).to_packet_string() + \
            RipPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2RipUdpIpV4Packet, self).build()
        RipPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2RipUdpIpV4Packet, self).build()
        return super(Ethernet2RipUdpIpV4Packet, self).get_header_length() + self.HEADER_SIZE_RIP

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2RipUdpIpV4Packet, self).get_hltapi_commands()
        cmd_dict.update(RipPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2RipUdpIpV4Packet, self).set_payload(payload)
        RipPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2RipUdpIpV4Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + RipPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2RipUdpIpV4Packet, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        RipPacketHeader.config_thirdparty_traffic_generator_stream_rip(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
