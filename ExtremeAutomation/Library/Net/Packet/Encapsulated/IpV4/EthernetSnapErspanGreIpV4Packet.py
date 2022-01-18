from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapGreIpV4Packet import EthernetSnapGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ErspanPacketHeader import ErspanPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket


class EthernetSnapErspanGreIpV4Packet(EthernetSnapGreIpV4Packet, ErspanPacketHeader):
    def __init__(self, innerpacket=EthernetPacket()):
        super(EthernetSnapErspanGreIpV4Packet, self).__init__(innerpacket)
        ErspanPacketHeader.__init__(self)
        self.set_name("EthernetSnapErspanGreIpV4Packet")

    def to_packet_string(self):
        return super(EthernetSnapErspanGreIpV4Packet, self).to_packet_string() + \
            ErspanPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapErspanGreIpV4Packet, self).build()
        ErspanPacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetSnapErspanGreIpV4Packet, self).get_header_length() + self.HEADER_SIZE_ERSPAN

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapErspanGreIpV4Packet, self).get_hltapi_commands()
        cmd_dict.update(ErspanPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapErspanGreIpV4Packet, self).set_payload(payload)
        ErspanPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapErspanGreIpV4Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + ErspanPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapErspanGreIpV4Packet, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        ErspanPacketHeader.config_thirdparty_traffic_generator_stream_erspan(self, tgen_type, generator_ref,
                                                                             port_string, stream_id, **kwargs)
