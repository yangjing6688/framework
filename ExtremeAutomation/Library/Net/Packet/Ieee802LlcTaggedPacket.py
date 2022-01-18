from ExtremeAutomation.Library.Net.Packet.EthernetTaggedPacket import EthernetTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Ieee802LlcPacketHeader import Ieee802LlcPacketHeader


class Ieee802LlcTaggedPacket(EthernetTaggedPacket, Ieee802LlcPacketHeader):
    def __init__(self):
        super(Ieee802LlcTaggedPacket, self).__init__()
        Ieee802LlcPacketHeader.__init__(self)
        self.set_name("LlcTaggedPacket")

    def build(self):
        super(Ieee802LlcTaggedPacket, self).build()
        Ieee802LlcPacketHeader.build(self)

    def get_header_length(self):
        return super(Ieee802LlcTaggedPacket, self).get_header_length() + self.HEADER_SIZE_LLC

    def to_packet_string(self):
        return super(Ieee802LlcTaggedPacket, self).to_packet_string() + Ieee802LlcPacketHeader.to_packet_string(self)

    def get_hltapi_commands(self):
        cmd_dict = super(Ieee802LlcTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(Ieee802LlcPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ieee802LlcTaggedPacket, self).set_payload(payload)
        Ieee802LlcPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ieee802LlcTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + Ieee802LlcPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ieee802LlcTaggedPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                       port_string, stream_id, **kwargs)
        Ieee802LlcPacketHeader.config_thirdparty_traffic_generator_stream_llc(self, tgen_type, generator_ref,
                                                                              port_string, stream_id, **kwargs)
