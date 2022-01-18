from ExtremeAutomation.Library.Net.Packet.Ethernet2VlanStackPacket import Ethernet2VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ProviderBackboneBridgePacketHeader import \
    ProviderBackboneBridgePacketHeader


class Ethernet2ProviderBackboneBridgeVlanStackPacket(Ethernet2VlanStackPacket, ProviderBackboneBridgePacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2ProviderBackboneBridgeVlanStackPacket, self).__init__(num_tags)
        ProviderBackboneBridgePacketHeader.__init__(self)
        self.set_name("Ethernet2ProviderBackboneBridgeVlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2ProviderBackboneBridgeVlanStackPacket, self).to_packet_string() + \
            ProviderBackboneBridgePacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2ProviderBackboneBridgeVlanStackPacket, self).build()
        ProviderBackboneBridgePacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2ProviderBackboneBridgeVlanStackPacket, self).build()
        return super(Ethernet2ProviderBackboneBridgeVlanStackPacket, self).get_header_length() + \
            self.HEADER_SIZE_PROVIDERBACKBONEBRIDGE

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2ProviderBackboneBridgeVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(ProviderBackboneBridgePacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2ProviderBackboneBridgeVlanStackPacket, self).set_payload(payload)
        ProviderBackboneBridgePacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2ProviderBackboneBridgeVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + ProviderBackboneBridgePacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2ProviderBackboneBridgeVlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        ProviderBackboneBridgePacketHeader.config_thirdparty_traffic_generator_stream_providerbackbonebridge(
            self, tgen_type, generator_ref, port_string, stream_id, **kwargs)
