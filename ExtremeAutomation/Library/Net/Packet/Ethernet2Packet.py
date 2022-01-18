from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader


class Ethernet2Packet(EthernetPacket, Ethernet2PacketHeader):
    def __init__(self):
        super(Ethernet2Packet, self).__init__()
        Ethernet2PacketHeader.__init__(self)
        self.set_name("Ethernet2Packet")

    def build(self):
        super(Ethernet2Packet, self).build()
        Ethernet2PacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2Packet, self).get_header_length() + self.HEADER_SIZE_ETHERNET2

    def to_packet_string(self):
        return super(Ethernet2Packet, self).to_packet_string() + Ethernet2PacketHeader.to_packet_string(self)

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2Packet, self).get_hltapi_commands()
        cmd_dict.update(Ethernet2PacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2Packet, self).set_payload(payload)
        Ethernet2PacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + Ethernet2PacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2Packet, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref, port_string,
                                                                                stream_id, **kwargs)
        Ethernet2PacketHeader.config_thirdparty_traffic_generator_stream_enet2(self, tgen_type, generator_ref,
                                                                               port_string, stream_id, **kwargs)
