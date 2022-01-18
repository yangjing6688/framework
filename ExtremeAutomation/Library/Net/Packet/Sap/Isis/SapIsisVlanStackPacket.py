from ExtremeAutomation.Library.Net.Packet.SapVlanStackPacket import SapVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisPacketHeader import IsisPacketHeader


class SapIsisVlanStackPacket(SapVlanStackPacket, IsisPacketHeader):
    def __init__(self, num_tags):
        super(SapIsisVlanStackPacket, self).__init__(num_tags)
        IsisPacketHeader.__init__(self)
        self.set_name("SapIsisVlanStackPacket")

    def to_packet_string(self):
        return super(SapIsisVlanStackPacket, self).to_packet_string() + \
            IsisPacketHeader.to_packet_string(self)

    def build(self):
        super(SapIsisVlanStackPacket, self).build()
        IsisPacketHeader.build(self)

    def get_header_length(self):
        super(SapIsisVlanStackPacket, self).build()
        return super(SapIsisVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_ISIS

    def get_hltapi_commands(self):
        cmd_dict = super(SapIsisVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(IsisPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapIsisVlanStackPacket, self).set_payload(payload)
        IsisPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapIsisVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IsisPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapIsisVlanStackPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                       port_string, stream_id, **kwargs)
        IsisPacketHeader.config_thirdparty_traffic_generator_stream_isis(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
