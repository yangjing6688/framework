from ExtremeAutomation.Library.Net.Packet.SapVlanStackPacket import SapVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BpduPacketHeader import BpduPacketHeader


class SapBpduVlanStackPacket(SapVlanStackPacket, BpduPacketHeader):
    def __init__(self, num_tags):
        super(SapBpduVlanStackPacket, self).__init__(num_tags)
        BpduPacketHeader.__init__(self)
        self.set_name("SapBpduVlanStackPacket")

    def to_packet_string(self):
        return super(SapBpduVlanStackPacket, self).to_packet_string() + \
            BpduPacketHeader.to_packet_string(self)

    def build(self):
        super(SapBpduVlanStackPacket, self).build()
        BpduPacketHeader.build(self)

    def get_header_length(self):
        return super(SapBpduVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_BPDU

    def get_hltapi_commands(self):
        cmd_dict = super(SapBpduVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(BpduPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapBpduVlanStackPacket, self).set_payload(payload)
        BpduPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapBpduVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + BpduPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapBpduVlanStackPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                       port_string, stream_id, **kwargs)
        BpduPacketHeader.config_thirdparty_traffic_generator_stream_bpdu(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
