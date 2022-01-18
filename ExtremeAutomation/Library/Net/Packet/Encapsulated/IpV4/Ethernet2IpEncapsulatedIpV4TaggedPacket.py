from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4TaggedPacket import Ethernet2IpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IpEncapsulatedPacketHeader import IpEncapsulatedPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket


class Ethernet2IpEncapsulatedIpV4TaggedPacket(Ethernet2IpV4TaggedPacket, IpEncapsulatedPacketHeader):
    def __init__(self, innerpacket=EthernetPacket()):
        super(Ethernet2IpEncapsulatedIpV4TaggedPacket, self).__init__()
        IpEncapsulatedPacketHeader.__init__(self)
        self.set_inner_packet(innerpacket)
        self.set_name("Ethernet2EncapsulatedIpV4TaggedPacket")

    def to_packet_string(self):
        return super(Ethernet2IpEncapsulatedIpV4TaggedPacket, self).to_packet_string() + \
            IpEncapsulatedPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2IpEncapsulatedIpV4TaggedPacket, self).build()
        IpEncapsulatedPacketHeader.build(self)

    def get_header_length(self):
        return super(Ethernet2IpEncapsulatedIpV4TaggedPacket, self).get_header_length() + \
            self.HEADER_SIZE_ENCAPSULATED + self.get_inner_packet_length()

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2IpEncapsulatedIpV4TaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(IpEncapsulatedPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2IpEncapsulatedIpV4TaggedPacket, self).set_payload(payload)
        IpEncapsulatedPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2IpEncapsulatedIpV4TaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IpEncapsulatedPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2IpEncapsulatedIpV4TaggedPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        IpEncapsulatedPacketHeader.config_thirdparty_traffic_generator_stream_encapsulated(
            self, tgen_type, generator_ref, port_string, stream_id, **kwargs)
