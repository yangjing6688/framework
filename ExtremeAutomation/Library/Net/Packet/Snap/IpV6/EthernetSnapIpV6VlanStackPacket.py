from ExtremeAutomation.Library.Net.Packet.Snap.EthernetSnapVlanStackPacket import EthernetSnapVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader


class EthernetSnapIpV6VlanStackPacket(EthernetSnapVlanStackPacket, IpV6PacketHeader):
    def __init__(self, num_tags):
        super(EthernetSnapIpV6VlanStackPacket, self).__init__(num_tags)
        IpV6PacketHeader.__init__(self)
        self.set_name("EthernetSnapIpV6VlanStackPacket")

    def to_packet_string(self):
        return super(EthernetSnapIpV6VlanStackPacket, self).to_packet_string() + \
            IpV6PacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapIpV6VlanStackPacket, self).build()
        IpV6PacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetSnapIpV6VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_IPV6 + \
            self.get_ipv6_extension_headers_length()

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapIpV6VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(IpV6PacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapIpV6VlanStackPacket, self).set_payload(payload)
        IpV6PacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapIpV6VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IpV6PacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapIpV6VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        IpV6PacketHeader.config_thirdparty_traffic_generator_stream_ipv6(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
