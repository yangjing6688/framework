from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4VlanStackPacket import Ethernet2IpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfPacketHeader import OspfPacketHeader


class Ethernet2OspfIpV4VlanStackPacket(Ethernet2IpV4VlanStackPacket, OspfPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2OspfIpV4VlanStackPacket, self).__init__(num_tags)
        OspfPacketHeader.__init__(self)
        self.set_name("Ethernet2OspfIpV4VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2OspfIpV4VlanStackPacket, self).to_packet_string() + \
            OspfPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2OspfIpV4VlanStackPacket, self).build()
        OspfPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2OspfIpV4VlanStackPacket, self).build()
        return super(Ethernet2OspfIpV4VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_OSPF

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2OspfIpV4VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(OspfPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2OspfIpV4VlanStackPacket, self).set_payload(payload)
        OspfPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2OspfIpV4VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + OspfPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2OspfIpV4VlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        OspfPacketHeader.config_thirdparty_traffic_generator_stream_ospf(self, tgen_type, generator_ref, port_string,
                                                                         stream_id, **kwargs)
