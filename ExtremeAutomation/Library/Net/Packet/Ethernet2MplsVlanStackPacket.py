from ExtremeAutomation.Library.Net.Packet.Ethernet2VlanStackPacket import Ethernet2VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MplsPacketHeader import MplsPacketHeader


class Ethernet2MplsVlanStackPacket(Ethernet2VlanStackPacket, MplsPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2MplsVlanStackPacket, self).__init__(num_tags)
        MplsPacketHeader.__init__(self)
        self.set_name("Ethernet2MplsVlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2MplsVlanStackPacket, self).to_packet_string() + \
            MplsPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2MplsVlanStackPacket, self).build()
        MplsPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2MplsVlanStackPacket, self).build()
        return super(Ethernet2MplsVlanStackPacket, self).get_header_length() + (
            self.HEADER_SIZE_MPLS * self.get_label_num())

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2MplsVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(MplsPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2MplsVlanStackPacket, self).set_payload(payload)
        MplsPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2MplsVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + MplsPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2MplsVlanStackPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                             port_string, stream_id,
                                                                                             **kwargs)
        MplsPacketHeader.config_thirdparty_traffic_generator_stream_mpls(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
