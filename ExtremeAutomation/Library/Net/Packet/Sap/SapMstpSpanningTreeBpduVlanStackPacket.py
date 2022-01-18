from ExtremeAutomation.Library.Net.Packet.Sap.SapSpanningTreeBpduVlanStackPacket import \
    SapSpanningTreeBpduVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MstpPacketHeader import MstpPacketHeader


class SapMstpSpanningTreeBpduVlanStackPacket(SapSpanningTreeBpduVlanStackPacket, MstpPacketHeader):
    def __init__(self, num_tags):
        super(SapMstpSpanningTreeBpduVlanStackPacket, self).__init__(num_tags)
        MstpPacketHeader.__init__(self)
        self.set_name("SapMstpSpanningTreeBpduVlanStackPacket")

    def to_packet_string(self):
        return super(SapMstpSpanningTreeBpduVlanStackPacket, self).to_packet_string() + \
            MstpPacketHeader.to_packet_string(self)

    def get_header_length(self):
        return super(SapMstpSpanningTreeBpduVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_MSTP + \
            (self.get_mstid_num() * 16)

    def build(self):
        super(SapMstpSpanningTreeBpduVlanStackPacket, self).build()
        MstpPacketHeader.build(self)

    def get_hltapi_commands(self):
        cmd_dict = super(SapMstpSpanningTreeBpduVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(MstpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapMstpSpanningTreeBpduVlanStackPacket, self).set_payload(payload)
        MstpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapMstpSpanningTreeBpduVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + MstpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapMstpSpanningTreeBpduVlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        MstpPacketHeader.config_thirdparty_traffic_generator_stream_mstp(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
