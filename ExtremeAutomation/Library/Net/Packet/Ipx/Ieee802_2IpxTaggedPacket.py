from ExtremeAutomation.Library.Net.Packet.Ieee802LlcTaggedPacket import Ieee802LlcTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import IpxPacketHeader


class Ieee802_2IpxTaggedPacket(Ieee802LlcTaggedPacket, IpxPacketHeader):
    def __init__(self):
        super(Ieee802_2IpxTaggedPacket, self).__init__()
        IpxPacketHeader.__init__(self)
        self.set_name("Ieee802_2IpxTaggedPacket")

    def to_packet_string(self):
        return super(Ieee802_2IpxTaggedPacket, self).to_packet_string() + \
            IpxPacketHeader.to_packet_string(self)

    def build(self):
        super(Ieee802_2IpxTaggedPacket, self).build()
        IpxPacketHeader.build(self)

    def get_header_length(self):
        return super(Ieee802_2IpxTaggedPacket, self).get_header_length() + self.HEADER_SIZE_IPX

    def get_hltapi_commands(self):
        cmd_dict = super(Ieee802_2IpxTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(IpxPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ieee802_2IpxTaggedPacket, self).set_payload(payload)
        IpxPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ieee802_2IpxTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IpxPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ieee802_2IpxTaggedPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        IpxPacketHeader.config_thirdparty_traffic_generator_stream_ipx(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
