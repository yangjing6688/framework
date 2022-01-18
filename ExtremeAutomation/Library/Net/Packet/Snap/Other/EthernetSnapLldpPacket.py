from ExtremeAutomation.Library.Net.Packet.Snap.EthernetSnapPacket import EthernetSnapPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LldpPacketHeader import LldpPacketHeader


class EthernetSnapLldpPacket(EthernetSnapPacket, LldpPacketHeader):
    def __init__(self):
        super(EthernetSnapLldpPacket, self).__init__()
        LldpPacketHeader.__init__(self)
        self.set_name("EthernetSnapLldpPacket")

    def to_packet_string(self):
        return super(EthernetSnapLldpPacket, self).to_packet_string() + \
            LldpPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapLldpPacket, self).build()
        LldpPacketHeader.build(self)

    def get_header_length(self):
        super(EthernetSnapLldpPacket, self).build()
        return super(EthernetSnapLldpPacket, self).get_header_length() + self.get_lldp_headers_length()

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapLldpPacket, self).get_hltapi_commands()
        cmd_dict.update(LldpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapLldpPacket, self).set_payload(payload)
        LldpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapLldpPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + LldpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapLldpPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                       port_string, stream_id, **kwargs)
        LldpPacketHeader.config_thirdparty_traffic_generator_stream_lldp(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
