from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapIpV6Packet import EthernetSnapIpV6Packet
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IpEncapsulatedPacketHeader import IpEncapsulatedPacketHeader
from ExtremeAutomation.Library.Net.Packet.Snap.EthernetSnapPacket import EthernetSnapPacket


default_packet = EthernetSnapPacket()


class EthernetSnapIpEncapsulatedIpV6Packet(EthernetSnapIpV6Packet, IpEncapsulatedPacketHeader):
    def __init__(self, innerpacket=default_packet):
        super(EthernetSnapIpEncapsulatedIpV6Packet, self).__init__()
        IpEncapsulatedPacketHeader.__init__(self)
        self.set_inner_packet(innerpacket)
        self.set_name("EthernetSnapEncapsulatedIpV6Packet")

    def to_packet_string(self):
        return super(EthernetSnapIpEncapsulatedIpV6Packet, self).to_packet_string() + \
            IpEncapsulatedPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetSnapIpEncapsulatedIpV6Packet, self).build()
        IpEncapsulatedPacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetSnapIpEncapsulatedIpV6Packet, self).get_header_length() + self.HEADER_SIZE_ENCAPSULATED + \
            self.get_inner_packet_length()

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetSnapIpEncapsulatedIpV6Packet, self).get_hltapi_commands()
        cmd_dict.update(IpEncapsulatedPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetSnapIpEncapsulatedIpV6Packet, self).set_payload(payload)
        IpEncapsulatedPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetSnapIpEncapsulatedIpV6Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + IpEncapsulatedPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetSnapIpEncapsulatedIpV6Packet, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        IpEncapsulatedPacketHeader.config_thirdparty_traffic_generator_stream_encapsulated(
            self, tgen_type, generator_ref, port_string, stream_id, **kwargs)
