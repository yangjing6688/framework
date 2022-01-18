from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapIsisTaggedPacket import SapIsisTaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisLSPPacketHeader import IsisLSPPacketHeader


class SapLSPIsisTaggedPacket(SapIsisTaggedPacket, IsisLSPPacketHeader):
    def __init__(self):
        super(SapLSPIsisTaggedPacket, self).__init__()
        IsisLSPPacketHeader.__init__(self)
        self.set_name("SapLSPTaggedIsisPacket")

    def to_packet_string(self):
        return super(SapLSPIsisTaggedPacket, self).to_packet_string() + \
            IsisLSPPacketHeader.to_packet_string(self)

    def build(self):
        super(SapLSPIsisTaggedPacket, self).build()
        IsisLSPPacketHeader.build(self)

    def get_header_length(self):
        super(SapLSPIsisTaggedPacket, self).build()
        return super(SapLSPIsisTaggedPacket, self).get_header_length() + self.HEADER_SIZE_LSP

    def get_hltapi_commands(self):
        cmd_dict = super(SapLSPIsisTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(IsisLSPPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapLSPIsisTaggedPacket, self).set_payload(payload)
        IsisLSPPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapLSPIsisTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IsisLSPPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapLSPIsisTaggedPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                       port_string, stream_id, **kwargs)
        IsisLSPPacketHeader.config_thirdparty_traffic_generator_stream_lsp(self, tgen_type, generator_ref, port_string,
                                                                           stream_id, **kwargs)
