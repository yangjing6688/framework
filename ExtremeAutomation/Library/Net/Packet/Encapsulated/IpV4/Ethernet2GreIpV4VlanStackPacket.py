from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4VlanStackPacket import Ethernet2IpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.GrePacketHeader import GrePacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket


class Ethernet2GreIpV4VlanStackPacket(Ethernet2IpV4VlanStackPacket, GrePacketHeader):
    def __init__(self, num_tags, innerpacket=EthernetPacket()):
        super(Ethernet2GreIpV4VlanStackPacket, self).__init__(num_tags)
        GrePacketHeader.__init__(self)
        self.set_gre_inner_packet(innerpacket)
        self.set_name("Ethernet2GreIpV4VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2GreIpV4VlanStackPacket, self).to_packet_string() + \
            GrePacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2GreIpV4VlanStackPacket, self).build()
        GrePacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2GreIpV4VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_GRE + \
            self.get_gre_inner_packet_length()

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2GreIpV4VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(GrePacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2GreIpV4VlanStackPacket, self).set_payload(payload)
        GrePacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2GreIpV4VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + GrePacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2GreIpV4VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        GrePacketHeader.config_thirdparty_traffic_generator_stream_gre(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
