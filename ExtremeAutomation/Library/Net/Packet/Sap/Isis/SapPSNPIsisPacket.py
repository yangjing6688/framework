from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapIsisPacket import SapIsisPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisPSNPPacketHeader import IsisPSNPPacketHeader


class SapPSNPIsisPacket(SapIsisPacket, IsisPSNPPacketHeader):
    def __init__(self):
        super(SapPSNPIsisPacket, self).__init__()
        IsisPSNPPacketHeader.__init__(self)
        self.set_name("SapPSNPIsisPacket")

    def to_packet_string(self):
        return super(SapPSNPIsisPacket, self).to_packet_string() + \
            IsisPSNPPacketHeader.to_packet_string(self)

    def build(self):
        super(SapPSNPIsisPacket, self).build()
        IsisPSNPPacketHeader.build(self)

    def get_header_length(self):
        super(SapPSNPIsisPacket, self).build()
        return super(SapPSNPIsisPacket, self).get_header_length() + self.HEADER_SIZE_SNP

    def get_hltapi_commands(self):
        cmd_dict = super(SapPSNPIsisPacket, self).get_hltapi_commands()
        cmd_dict.update(IsisPSNPPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapPSNPIsisPacket, self).set_payload(payload)
        IsisPSNPPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapPSNPIsisPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IsisPSNPPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapPSNPIsisPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref, port_string,
                                                                                  stream_id, **kwargs)
        IsisPSNPPacketHeader.config_thirdparty_traffic_generator_stream_snp(self, tgen_type, generator_ref, port_string,
                                                                            stream_id, **kwargs)
