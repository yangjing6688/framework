from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapIsisTaggedPacket import SapIsisTaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisCSNPPacketHeader import IsisCSNPPacketHeader


class SapCSNPIsisTaggedPacket(SapIsisTaggedPacket, IsisCSNPPacketHeader):
    def __init__(self):
        super(SapCSNPIsisTaggedPacket, self).__init__()
        IsisCSNPPacketHeader.__init__(self)
        self.set_name("SapCSNPTaggedIsisPacket")

    def to_packet_string(self):
        return super(SapCSNPIsisTaggedPacket, self).to_packet_string() + \
            IsisCSNPPacketHeader.to_packet_string(self)

    def build(self):
        super(SapCSNPIsisTaggedPacket, self).build()
        IsisCSNPPacketHeader.build(self)

    def get_header_length(self):
        super(SapCSNPIsisTaggedPacket, self).build()
        return super(SapCSNPIsisTaggedPacket, self).get_header_length() + self.HEADER_SIZE_SNP

    def get_hltapi_commands(self):
        cmd_dict = super(SapCSNPIsisTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(IsisCSNPPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapCSNPIsisTaggedPacket, self).set_payload(payload)
        IsisCSNPPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapCSNPIsisTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IsisCSNPPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapCSNPIsisTaggedPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                        port_string, stream_id,
                                                                                        **kwargs)
        IsisCSNPPacketHeader.config_thirdparty_traffic_generator_stream_snp(self, tgen_type, generator_ref, port_string,
                                                                            stream_id, **kwargs)
