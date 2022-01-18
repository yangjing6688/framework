from ExtremeAutomation.Library.Net.Packet.EthernetVlanStackPacket import EthernetVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.SapPacketHeader import SapPacketHeader


class SapVlanStackPacket(EthernetVlanStackPacket, SapPacketHeader):
    def __init__(self, num_tags):
        super(SapVlanStackPacket, self).__init__(num_tags)
        SapPacketHeader.__init__(self)
        self.set_name("SapVlanStackPacket")

    def build(self):
        super(SapVlanStackPacket, self).build()
        SapPacketHeader.build(self)

    def get_header_length(self):
        return super(SapVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_SAP

    def to_packet_string(self):
        return super(SapVlanStackPacket, self).to_packet_string() + SapPacketHeader.to_packet_string(self)

    def get_hltapi_commands(self):
        cmd_dict = super(SapVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(SapPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapVlanStackPacket, self).set_payload(payload)
        SapPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + SapPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(SapVlanStackPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                   port_string, stream_id, **kwargs)
        SapPacketHeader.config_thirdparty_traffic_generator_stream_llc(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
