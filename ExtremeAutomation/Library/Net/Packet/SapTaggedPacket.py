from ExtremeAutomation.Library.Net.Packet.EthernetTaggedPacket import EthernetTaggedPacket
from ExtremeAutomation.Library.Net.Packet.SapPacketHeader import SapPacketHeader


class SapTaggedPacket(EthernetTaggedPacket, SapPacketHeader):
    def __init__(self):
        super(SapTaggedPacket, self).__init__()
        SapPacketHeader.__init__(self)
        self.set_name("SapTaggedPacket")

    def build(self):
        super(SapTaggedPacket, self).build()
        SapPacketHeader.build(self)

    def get_header_length(self):
        return super(SapTaggedPacket, self).get_header_length() + self.HEADER_SIZE_SAP

    def to_packet_string(self):
        return super(SapTaggedPacket, self).to_packet_string() + SapPacketHeader.to_packet_string(self)

    def get_hltapi_commands(self):
        cmd_dict = super(SapTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(SapPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapTaggedPacket, self).set_payload(payload)
        SapPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + SapPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapTaggedPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref, port_string,
                                                                                stream_id, **kwargs)
        SapPacketHeader.config_thirdparty_traffic_generator_stream_llc(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
