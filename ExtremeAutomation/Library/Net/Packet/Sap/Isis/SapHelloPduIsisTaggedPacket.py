from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapIsisTaggedPacket import SapIsisTaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisHelloPduPacketHeader import IsisHelloPduPacketHeader


class SapHelloPduIsisTaggedPacket(SapIsisTaggedPacket, IsisHelloPduPacketHeader):
    def __init__(self):
        super(SapHelloPduIsisTaggedPacket, self).__init__()
        IsisHelloPduPacketHeader.__init__(self)
        self.set_name("SapHelloPduTaggedIsisPacket")

    def to_packet_string(self):
        return super(SapHelloPduIsisTaggedPacket, self).to_packet_string() + \
            IsisHelloPduPacketHeader.to_packet_string(self)

    def build(self):
        super(SapHelloPduIsisTaggedPacket, self).build()
        IsisHelloPduPacketHeader.build(self)

    def get_header_length(self):
        super(SapHelloPduIsisTaggedPacket, self).build()
        return super(SapHelloPduIsisTaggedPacket, self).get_header_length() + self.HEADER_SIZE_HELLOPDU

    def get_hltapi_commands(self):
        cmd_dict = super(SapHelloPduIsisTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(IsisHelloPduPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapHelloPduIsisTaggedPacket, self).set_payload(payload)
        IsisHelloPduPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapHelloPduIsisTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IsisHelloPduPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapHelloPduIsisTaggedPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                            port_string, stream_id,
                                                                                            **kwargs)
        IsisHelloPduPacketHeader.config_thirdparty_traffic_generator_stream_hellopdu(self, tgen_type, generator_ref,
                                                                                     port_string, stream_id, **kwargs)
