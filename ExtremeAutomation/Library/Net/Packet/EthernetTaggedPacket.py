from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader


class EthernetTaggedPacket(EthernetPacket, TaggedPacketHeader):
    def __init__(self):
        super(EthernetTaggedPacket, self).__init__()
        TaggedPacketHeader.__init__(self)
        self.set_name("EthernetTaggedPacket")

    def to_packet_string(self):
        return super(EthernetTaggedPacket, self).to_packet_string() + TaggedPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetTaggedPacket, self).build()
        TaggedPacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetTaggedPacket, self).get_header_length() + self.HEADER_SIZE_TAGGED

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(TaggedPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetTaggedPacket, self).set_payload(payload)
        TaggedPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + TaggedPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetTaggedPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                     port_string, stream_id, **kwargs)
        TaggedPacketHeader.config_thirdparty_traffic_generator_stream_tagged(self, tgen_type, generator_ref,
                                                                             port_string, stream_id, **kwargs)
