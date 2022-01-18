from ExtremeAutomation.Library.Net.Packet.Snap.EthernetSnapVlanStackPacket import EthernetSnapVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader


class EthernetSnapIpV4VlanStackPacket(EthernetSnapVlanStackPacket, IpV4PacketHeader):
    def __init__(self, num_tags):
        super(EthernetSnapIpV4VlanStackPacket, self).__init__(num_tags)
        IpV4PacketHeader.__init__(self)
        self.set_name("EthernetSnapIpV4VlanStackPacket")

    def to_packet_string(self):
        return super(EthernetSnapIpV4VlanStackPacket, self).to_packet_string() + \
            IpV4PacketHeader.to_packet_string(self)

    def get_header_length(self):
        return super(EthernetSnapIpV4VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_IPV4  # + options

    def build(self):
        super(EthernetSnapIpV4VlanStackPacket, self).build()
        IpV4PacketHeader.build(self)

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapIpV4VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(IpV4PacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapIpV4VlanStackPacket, self).set_payload(payload)
        IpV4PacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapIpV4VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IpV4PacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapIpV4VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        IpV4PacketHeader.config_thirdparty_traffic_generator_stream_ipv4(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
