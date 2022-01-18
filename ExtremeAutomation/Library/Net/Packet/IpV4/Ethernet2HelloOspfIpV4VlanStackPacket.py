from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2OspfIpV4VlanStackPacket import Ethernet2OspfIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfHelloPacketHeader import OspfHelloPacketHeader


class Ethernet2HelloOspfIpV4VlanStackPacket(Ethernet2OspfIpV4VlanStackPacket, OspfHelloPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2HelloOspfIpV4VlanStackPacket, self).__init__(num_tags)
        OspfHelloPacketHeader.__init__(self)
        self.set_name("Ethernet2HelloOspfIpV4VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2HelloOspfIpV4VlanStackPacket, self).to_packet_string() + \
            OspfHelloPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2HelloOspfIpV4VlanStackPacket, self).build()
        OspfHelloPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2HelloOspfIpV4VlanStackPacket, self).build()
        return super(Ethernet2HelloOspfIpV4VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_HELLO

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2HelloOspfIpV4VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(OspfHelloPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2HelloOspfIpV4VlanStackPacket, self).set_payload(payload)
        OspfHelloPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2HelloOspfIpV4VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + OspfHelloPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2HelloOspfIpV4VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        OspfHelloPacketHeader.config_thirdparty_traffic_generator_stream_hello(self, tgen_type, generator_ref,
                                                                               port_string, stream_id, **kwargs)
