from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MstpPacketHeader import MstpPacketHeader
from ExtremeAutomation.Library.Net.Packet.Sap.SapSpanningTreeBpduPacket import SapSpanningTreeBpduPacket


class SapMstpSpanningTreeBpduPacket(SapSpanningTreeBpduPacket, MstpPacketHeader):
    def __init__(self):
        super(SapMstpSpanningTreeBpduPacket, self).__init__()
        MstpPacketHeader.__init__(self)
        self.set_name("SapMstpSpanningTreeBpduPacket")

    def to_packet_string(self):
        return super(SapMstpSpanningTreeBpduPacket, self).to_packet_string() + \
            MstpPacketHeader.to_packet_string(self)

    def build(self):
        super(SapMstpSpanningTreeBpduPacket, self).build()
        MstpPacketHeader.build(self)

    def get_header_length(self):
        return super(SapMstpSpanningTreeBpduPacket, self).get_header_length() + \
            self.HEADER_SIZE_MSTP + (self.get_mstid_num() * 16)

    def get_hltapi_commands(self):
        cmd_dict = super(SapMstpSpanningTreeBpduPacket, self).get_hltapi_commands()
        cmd_dict.update(MstpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapMstpSpanningTreeBpduPacket, self).set_payload(payload)
        MstpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapMstpSpanningTreeBpduPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + MstpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapMstpSpanningTreeBpduPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                              port_string, stream_id,
                                                                                              **kwargs)
        MstpPacketHeader.config_thirdparty_traffic_generator_stream_mstp(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
