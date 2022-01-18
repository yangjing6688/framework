from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2OspfIpV4Packet import Ethernet2OspfIpV4Packet
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfDBDescriptionPacketHeader import \
    OspfDBDescriptionPacketHeader


class Ethernet2DBDescriptionOspfIpV4Packet(Ethernet2OspfIpV4Packet, OspfDBDescriptionPacketHeader):
    def __init__(self):
        super(Ethernet2DBDescriptionOspfIpV4Packet, self).__init__()
        OspfDBDescriptionPacketHeader.__init__(self)
        self.set_name("Ethernet2DBDescriptionOspfIpV4Packet")

    def to_packet_string(self):
        return super(Ethernet2DBDescriptionOspfIpV4Packet, self).to_packet_string() + \
            OspfDBDescriptionPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2DBDescriptionOspfIpV4Packet, self).build()
        OspfDBDescriptionPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2DBDescriptionOspfIpV4Packet, self).build()
        return super(Ethernet2DBDescriptionOspfIpV4Packet, self).get_header_length() + self.HEADER_SIZE_DBDESCRIPTION

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2DBDescriptionOspfIpV4Packet, self).get_hltapi_commands()
        cmd_dict.update(OspfDBDescriptionPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2DBDescriptionOspfIpV4Packet, self).set_payload(payload)
        OspfDBDescriptionPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2DBDescriptionOspfIpV4Packet, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + OspfDBDescriptionPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2DBDescriptionOspfIpV4Packet, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        OspfDBDescriptionPacketHeader.config_thirdparty_traffic_generator_stream_dbdescription(
            self, tgen_type, generator_ref, port_string, stream_id, **kwargs)
