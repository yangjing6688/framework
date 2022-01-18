from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4Packet import Ethernet2IpV4Packet
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.PimPacketHeader import PimPacketHeader


class Ethernet2PimIpV4Packet(Ethernet2IpV4Packet, PimPacketHeader):
    def __init__(self):
        super(Ethernet2PimIpV4Packet, self).__init__()
        PimPacketHeader.__init__(self)
        self.set_name("Ethernet2PimIpV4Packet")

    def to_packet_string(self):
        return super(Ethernet2PimIpV4Packet, self).to_packet_string() + \
            PimPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2PimIpV4Packet, self).build()
        PimPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2PimIpV4Packet, self).build()
        return super(Ethernet2PimIpV4Packet, self).get_header_length() + self.HEADER_SIZE_PIM

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2PimIpV4Packet, self).get_hltapi_commands()
        cmd_dict.update(PimPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2PimIpV4Packet, self).set_payload(payload)
        PimPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2PimIpV4Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + PimPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2PimIpV4Packet, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                       port_string, stream_id, **kwargs)
        PimPacketHeader.config_thirdparty_traffic_generator_stream_pim(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
