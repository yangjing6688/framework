from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2OspfIpV4Packet import Ethernet2OspfIpV4Packet
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfLinkStateAcknowledgePacketHeader import \
    OspfLinkStateAcknowledgePacketHeader


class Ethernet2LinkStateAcknowledgeOspfIpV4Packet(Ethernet2OspfIpV4Packet, OspfLinkStateAcknowledgePacketHeader):
    def __init__(self):
        super(Ethernet2LinkStateAcknowledgeOspfIpV4Packet, self).__init__()
        OspfLinkStateAcknowledgePacketHeader.__init__(self)
        self.set_name("Ethernet2LinkStateAcknowledgeOspfIpV4Packet")

    def to_packet_string(self):
        return super(Ethernet2LinkStateAcknowledgeOspfIpV4Packet, self).to_packet_string() + \
            OspfLinkStateAcknowledgePacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2LinkStateAcknowledgeOspfIpV4Packet, self).build()
        OspfLinkStateAcknowledgePacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2LinkStateAcknowledgeOspfIpV4Packet, self).build()
        return super(Ethernet2LinkStateAcknowledgeOspfIpV4Packet, self).get_header_length() + \
            self.HEADER_SIZE_LINKSTATEACKNOWLEDGE

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2LinkStateAcknowledgeOspfIpV4Packet, self).get_hltapi_commands()
        cmd_dict.update(OspfLinkStateAcknowledgePacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2LinkStateAcknowledgeOspfIpV4Packet, self).set_payload(payload)
        OspfLinkStateAcknowledgePacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2LinkStateAcknowledgeOspfIpV4Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + OspfLinkStateAcknowledgePacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2LinkStateAcknowledgeOspfIpV4Packet, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        OspfLinkStateAcknowledgePacketHeader.config_thirdparty_traffic_generator_stream_linkstateacknowledge(
            self, tgen_type, generator_ref, port_string, stream_id, **kwargs)
