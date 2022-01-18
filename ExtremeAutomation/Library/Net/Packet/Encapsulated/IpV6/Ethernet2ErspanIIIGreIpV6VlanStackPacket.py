from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2GreIpV6VlanStackPacket import \
    Ethernet2GreIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ErspanIIIPacketHeader import ErspanIIIPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket


class Ethernet2ErspanIIIGreIpV6VlanStackPacket(Ethernet2GreIpV6VlanStackPacket, ErspanIIIPacketHeader):
    def __init__(self, num_tags, innerpacket=EthernetPacket()):
        super(Ethernet2ErspanIIIGreIpV6VlanStackPacket, self).__init__(num_tags, innerpacket)
        ErspanIIIPacketHeader.__init__(self)
        self.set_name("Ethernet2ErspanIIIGreIpV6VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2ErspanIIIGreIpV6VlanStackPacket, self).to_packet_string() + \
            ErspanIIIPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2ErspanIIIGreIpV6VlanStackPacket, self).build()
        ErspanIIIPacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2ErspanIIIGreIpV6VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_ERSPANIII

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2ErspanIIIGreIpV6VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(ErspanIIIPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2ErspanIIIGreIpV6VlanStackPacket, self).set_payload(payload)
        ErspanIIIPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2ErspanIIIGreIpV6VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + ErspanIIIPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2ErspanIIIGreIpV6VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        ErspanIIIPacketHeader.config_thirdparty_traffic_generator_stream_erspaniii(self, tgen_type, generator_ref,
                                                                                   port_string, stream_id, **kwargs)
