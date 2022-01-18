from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2OspfIpV4TaggedPacket import Ethernet2OspfIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfLinkStateRequestPacketHeader import \
    OspfLinkStateRequestPacketHeader


class Ethernet2LinkStateRequestOspfIpV4TaggedPacket(Ethernet2OspfIpV4TaggedPacket, OspfLinkStateRequestPacketHeader):
    def __init__(self):
        super(Ethernet2LinkStateRequestOspfIpV4TaggedPacket, self).__init__()
        OspfLinkStateRequestPacketHeader.__init__(self)
        self.set_name("Ethernet2LinkStateRequestOspfIpV4TaggedPacket")

    def to_packet_string(self):
        return super(Ethernet2LinkStateRequestOspfIpV4TaggedPacket, self).to_packet_string() + \
            OspfLinkStateRequestPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2LinkStateRequestOspfIpV4TaggedPacket, self).build()
        OspfLinkStateRequestPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2LinkStateRequestOspfIpV4TaggedPacket, self).build()
        return super(Ethernet2LinkStateRequestOspfIpV4TaggedPacket, self).get_header_length() + \
            self.HEADER_SIZE_LINKSTATEREQUEST

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2LinkStateRequestOspfIpV4TaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(OspfLinkStateRequestPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2LinkStateRequestOspfIpV4TaggedPacket, self).set_payload(payload)
        OspfLinkStateRequestPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2LinkStateRequestOspfIpV4TaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + OspfLinkStateRequestPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2LinkStateRequestOspfIpV4TaggedPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        OspfLinkStateRequestPacketHeader.config_thirdparty_traffic_generator_stream_linkstaterequest(
            self, tgen_type, generator_ref, port_string, stream_id, **kwargs)
