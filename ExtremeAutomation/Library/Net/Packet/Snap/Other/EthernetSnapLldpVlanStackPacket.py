from ExtremeAutomation.Library.Net.Packet.Snap.EthernetSnapVlanStackPacket import EthernetSnapVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LldpPacketHeader import LldpPacketHeader


class EthernetSnapLldpVlanStackPacket(EthernetSnapVlanStackPacket, LldpPacketHeader):
    def __init__(self, num_tags):
        super(EthernetSnapLldpVlanStackPacket, self).__init__(num_tags)
        LldpPacketHeader.__init__(self)
        self.set_name("EthernetSnapLldpVlanStackPacket")

    def to_packet_string(self):
        return super(EthernetSnapLldpVlanStackPacket, self).to_packet_string() + \
            LldpPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapLldpVlanStackPacket, self).build()
        LldpPacketHeader.build(self)

    def get_header_length(self):
        super(EthernetSnapLldpVlanStackPacket, self).build()
        return super(EthernetSnapLldpVlanStackPacket, self).get_header_length() + self.get_lldp_headers_length()

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapLldpVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(LldpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapLldpVlanStackPacket, self).set_payload(payload)
        LldpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapLldpVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + LldpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapLldpVlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        LldpPacketHeader.config_thirdparty_traffic_generator_stream_lldp(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
