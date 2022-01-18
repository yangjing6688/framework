from ExtremeAutomation.Library.Net.Packet.Ethernet2MplsVlanStackPacket import Ethernet2MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader


class Ethernet2IpV4MplsVlanStackPacket(Ethernet2MplsVlanStackPacket, IpV4PacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2IpV4MplsVlanStackPacket, self).__init__(num_tags)
        IpV4PacketHeader.__init__(self)
        self.set_name("Ethernet2IpV4MplsVlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2IpV4MplsVlanStackPacket, self).to_packet_string() + \
            IpV4PacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2IpV4MplsVlanStackPacket, self).build()
        IpV4PacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2IpV4MplsVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_IPV4  # + options

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2IpV4MplsVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(IpV4PacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        super(Ethernet2IpV4MplsVlanStackPacket, self).set_payload(payload)
        IpV4PacketHeader.parse_bytes(self)

    def configure_packet_checksum_fields(self):
        parent_header_legth = super(Ethernet2IpV4MplsVlanStackPacket, self).get_header_length()
        self.calculate_ip_checksum(parent_header_legth)
        super(Ethernet2IpV4MplsVlanStackPacket, self).configure_packet_checksum_fields()

    def configure_packet_length_fields(self, length=False):
        super(Ethernet2IpV4MplsVlanStackPacket, self).configure_packet_length_fields(length)
        self.configure_ip_length(length)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2IpV4MplsVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IpV4PacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2IpV4MplsVlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        IpV4PacketHeader.config_thirdparty_traffic_generator_stream_ipv4(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
