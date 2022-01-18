from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapGreIpV4VlanStackPacket import \
    EthernetSnapGreIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ErspanPacketHeader import ErspanPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket


class EthernetSnapErspanGreIpV4VlanStackPacket(EthernetSnapGreIpV4VlanStackPacket, ErspanPacketHeader):
    def __init__(self, num_tags, innerpacket=EthernetPacket()):
        super(EthernetSnapErspanGreIpV4VlanStackPacket, self).__init__(num_tags, innerpacket)
        ErspanPacketHeader.__init__(self)
        self.set_name("EthernetSnapErspanGreIpV4VlanStackPacket")

    def to_packet_string(self):
        return super(EthernetSnapErspanGreIpV4VlanStackPacket, self).to_packet_string() + \
            ErspanPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapErspanGreIpV4VlanStackPacket, self).build()
        ErspanPacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetSnapErspanGreIpV4VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_ERSPAN

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapErspanGreIpV4VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(ErspanPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapErspanGreIpV4VlanStackPacket, self).set_payload(payload)
        ErspanPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapErspanGreIpV4VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + ErspanPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapErspanGreIpV4VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        ErspanPacketHeader.config_thirdparty_traffic_generator_stream_erspan(self, tgen_type, generator_ref,
                                                                             port_string, stream_id, **kwargs)
