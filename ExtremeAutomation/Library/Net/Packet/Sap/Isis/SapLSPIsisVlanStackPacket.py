from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapIsisVlanStackPacket import SapIsisVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisLSPPacketHeader import IsisLSPPacketHeader


class SapLSPIsisVlanStackPacket(SapIsisVlanStackPacket, IsisLSPPacketHeader):
    def __init__(self, num_tags):
        super(SapLSPIsisVlanStackPacket, self).__init__(num_tags)
        IsisLSPPacketHeader.__init__(self)
        self.set_name("SapLSPVlanStackIsisPacket")

    def to_packet_string(self):
        return super(SapLSPIsisVlanStackPacket, self).to_packet_string() + \
            IsisLSPPacketHeader.to_packet_string(self)

    def build(self):
        super(SapLSPIsisVlanStackPacket, self).build()
        IsisLSPPacketHeader.build(self)

    def get_header_length(self):
        super(SapLSPIsisVlanStackPacket, self).build()
        return super(SapLSPIsisVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_LSP

    def get_hltapi_commands(self):
        cmd_dict = super(SapLSPIsisVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(IsisLSPPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapLSPIsisVlanStackPacket, self).set_payload(payload)
        IsisLSPPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapLSPIsisVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IsisLSPPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapLSPIsisVlanStackPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                          port_string, stream_id,
                                                                                          **kwargs)
        IsisLSPPacketHeader.config_thirdparty_traffic_generator_stream_lsp(self, tgen_type, generator_ref, port_string,
                                                                           stream_id, **kwargs)
