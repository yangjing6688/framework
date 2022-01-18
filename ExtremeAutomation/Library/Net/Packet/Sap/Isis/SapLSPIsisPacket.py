from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapIsisPacket import SapIsisPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisLSPPacketHeader import IsisLSPPacketHeader


class SapLSPIsisPacket(SapIsisPacket, IsisLSPPacketHeader):
    def __init__(self):
        super(SapLSPIsisPacket, self).__init__()
        IsisLSPPacketHeader.__init__(self)
        self.set_name("SapLSPIsisPacket")

    def to_packet_string(self):
        return super(SapLSPIsisPacket, self).to_packet_string() + \
            IsisLSPPacketHeader.to_packet_string(self)

    def build(self):
        super(SapLSPIsisPacket, self).build()
        IsisLSPPacketHeader.build(self)

    def get_header_length(self):
        super(SapLSPIsisPacket, self).build()
        return super(SapLSPIsisPacket, self).get_header_length() + self.HEADER_SIZE_LSP

    def get_hltapi_commands(self):
        cmd_dict = super(SapLSPIsisPacket, self).get_hltapi_commands()
        cmd_dict.update(IsisLSPPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapLSPIsisPacket, self).set_payload(payload)
        IsisLSPPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapLSPIsisPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IsisLSPPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapLSPIsisPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref, port_string,
                                                                                 stream_id, **kwargs)
        IsisLSPPacketHeader.config_thirdparty_traffic_generator_stream_lsp(self, tgen_type, generator_ref, port_string,
                                                                           stream_id, **kwargs)
