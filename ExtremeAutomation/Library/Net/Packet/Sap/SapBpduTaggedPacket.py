from ExtremeAutomation.Library.Net.Packet.SapTaggedPacket import SapTaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BpduPacketHeader import BpduPacketHeader


class SapBpduTaggedPacket(SapTaggedPacket, BpduPacketHeader):
    def __init__(self):
        super(SapBpduTaggedPacket, self).__init__()
        BpduPacketHeader.__init__(self)
        self.set_name("SapBpduTaggedPacket")

    def to_packet_string(self):
        return super(SapBpduTaggedPacket, self).to_packet_string() + \
            BpduPacketHeader.to_packet_string(self)

    def build(self):
        super(SapBpduTaggedPacket, self).build()
        BpduPacketHeader.build(self)

    def get_header_length(self):
        return super(SapBpduTaggedPacket, self).get_header_length() + self.HEADER_SIZE_BPDU

    def get_hltapi_commands(self):
        cmd_dict = super(SapBpduTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(BpduPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapBpduTaggedPacket, self).set_payload(payload)
        BpduPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapBpduTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + BpduPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapBpduTaggedPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                    port_string, stream_id, **kwargs)
        BpduPacketHeader.config_thirdparty_traffic_generator_stream_bpdu(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
