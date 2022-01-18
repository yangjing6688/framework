from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapIpV6TaggedPacket import EthernetSnapIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.GrePacketHeader import GrePacketHeader
from ExtremeAutomation.Library.Net.Packet.Snap.EthernetSnapPacket import EthernetSnapPacket


default_packet = EthernetSnapPacket()


class EthernetSnapGreIpV6TaggedPacket(EthernetSnapIpV6TaggedPacket, GrePacketHeader):
    def __init__(self, innerpacket=default_packet):
        super(EthernetSnapGreIpV6TaggedPacket, self).__init__()
        GrePacketHeader.__init__(self)
        self.set_gre_inner_packet(innerpacket)
        self.set_name("EthernetSnapGreIpV6TaggedPacket")

    def to_packet_string(self):
        return super(EthernetSnapGreIpV6TaggedPacket, self).to_packet_string() + \
            GrePacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapGreIpV6TaggedPacket, self).build()
        GrePacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetSnapGreIpV6TaggedPacket, self).get_header_length() + self.HEADER_SIZE_GRE + \
            self.get_gre_inner_packet_length()

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapGreIpV6TaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(GrePacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapGreIpV6TaggedPacket, self).set_payload(payload)
        GrePacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapGreIpV6TaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + GrePacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapGreIpV6TaggedPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        GrePacketHeader.config_thirdparty_traffic_generator_stream_gre(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
