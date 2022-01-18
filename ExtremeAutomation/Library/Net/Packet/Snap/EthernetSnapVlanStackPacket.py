from ExtremeAutomation.Library.Net.Packet.Ieee802LlcVlanStackPacket import Ieee802LlcVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import SnapPacketHeader


class EthernetSnapVlanStackPacket(Ieee802LlcVlanStackPacket, SnapPacketHeader):
    def __init__(self, num_tags):
        super(EthernetSnapVlanStackPacket, self).__init__(num_tags)
        SnapPacketHeader.__init__(self)
        self.set_name("EthernetSnapVlanStackPacket")

    def to_packet_string(self):
        return super(EthernetSnapVlanStackPacket, self).to_packet_string() + \
            SnapPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapVlanStackPacket, self).build()
        SnapPacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetSnapVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_SNAP

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(SnapPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapVlanStackPacket, self).set_payload(payload)
        SnapPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + SnapPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapVlanStackPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                            port_string, stream_id,
                                                                                            **kwargs)
        SnapPacketHeader.config_thirdparty_traffic_generator_stream_snap(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
