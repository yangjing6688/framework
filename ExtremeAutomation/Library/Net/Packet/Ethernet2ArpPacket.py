from ExtremeAutomation.Library.Net.Packet.Ethernet2Packet import Ethernet2Packet
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import ArpPacketHeader


class Ethernet2ArpPacket(Ethernet2Packet, ArpPacketHeader):
    def __init__(self):
        super(Ethernet2ArpPacket, self).__init__()
        ArpPacketHeader.__init__(self)
        self.set_name("Ethernet2ArpPacket")

    def to_packet_string(self):
        return super(Ethernet2ArpPacket, self).to_packet_string() + ArpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2ArpPacket, self).build()
        ArpPacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2ArpPacket, self).get_header_length() + self.HEADER_SIZE_ARP

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2ArpPacket, self).get_hltapi_commands()
        cmd_dict.update(ArpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2ArpPacket, self).set_payload(payload)
        ArpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2ArpPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + ArpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2ArpPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                   port_string, stream_id, **kwargs)
        ArpPacketHeader.config_thirdparty_traffic_generator_stream_arp(self, tgen_type, generator_ref, port_string,
                                                                       stream_id, **kwargs)
