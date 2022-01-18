from ExtremeAutomation.Library.Net.Packet.Ethernet2MplsTaggedPacket import Ethernet2MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MplsEncapsulatedPacketHeader import MplsEncapsulatedPacketHeader


class Ethernet2MplsEncapsulatedTaggedPacket(Ethernet2MplsTaggedPacket, MplsEncapsulatedPacketHeader):
    def __init__(self):
        super(Ethernet2MplsEncapsulatedTaggedPacket, self).__init__()
        MplsEncapsulatedPacketHeader.__init__(self)
        self.set_name("Ethernet2MplsEncapsulatedTaggedPacket")

    def to_packet_string(self):
        return super(Ethernet2MplsEncapsulatedTaggedPacket, self).to_packet_string() + \
            MplsEncapsulatedPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2MplsEncapsulatedTaggedPacket, self).build()
        MplsEncapsulatedPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2MplsEncapsulatedTaggedPacket, self).build()
        return super(Ethernet2MplsEncapsulatedTaggedPacket, self).get_header_length() + \
            self.HEADER_SIZE_MPLSENCAPSULATED

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2MplsEncapsulatedTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(MplsEncapsulatedPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2MplsEncapsulatedTaggedPacket, self).set_payload(payload)
        MplsEncapsulatedPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2MplsEncapsulatedTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + MplsEncapsulatedPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2MplsEncapsulatedTaggedPacket, self).config_thirdparty_traffic_generator_stream(tgen_type,
                                                                                                      generator_ref,
                                                                                                      port_string,
                                                                                                      stream_id,
                                                                                                      **kwargs)
        MplsEncapsulatedPacketHeader.config_thirdparty_traffic_generator_stream_mplsencapsulated(self, tgen_type,
                                                                                                 generator_ref,
                                                                                                 port_string, stream_id,
                                                                                                 **kwargs)
