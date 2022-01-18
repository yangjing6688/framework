from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4MplsVlanStackPacket import Ethernet2IpV4MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.UdpPacketHeader import UdpPacketHeader


class Ethernet2UdpIpV4MplsVlanStackPacket(Ethernet2IpV4MplsVlanStackPacket, UdpPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2UdpIpV4MplsVlanStackPacket, self).__init__(num_tags)
        UdpPacketHeader.__init__(self)
        self.set_name("Ethernet2UdpIpV4MplsVlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2UdpIpV4MplsVlanStackPacket, self).to_packet_string() + \
            UdpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2UdpIpV4MplsVlanStackPacket, self).build()
        UdpPacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2UdpIpV4MplsVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_UDP

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2UdpIpV4MplsVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(UdpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2UdpIpV4MplsVlanStackPacket, self).set_payload(payload)
        UdpPacketHeader.parse_bytes(self)

    def configure_packet_length_fields(self, length=False):
        super(Ethernet2UdpIpV4MplsVlanStackPacket, self).configure_packet_length_fields(length)
        length = self.get_length_int()
        parent_header_legth = super(Ethernet2UdpIpV4MplsVlanStackPacket, self).get_header_length()
        length -= parent_header_legth
        length -= 4  # this is for the fsc
        self.configure_udp_length(length)

    def configure_packet_checksum_fields(self):
        parent_header_legth = super(Ethernet2UdpIpV4MplsVlanStackPacket, self).get_header_length()
        self.calculate_udp_checksum(parent_header_legth)
        super(Ethernet2UdpIpV4MplsVlanStackPacket, self).configure_packet_checksum_fields()

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2UdpIpV4MplsVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + UdpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2UdpIpV4MplsVlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        UdpPacketHeader.config_thirdparty_traffic_generator_stream_udp(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
