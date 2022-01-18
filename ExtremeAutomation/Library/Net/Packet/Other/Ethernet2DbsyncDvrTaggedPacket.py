from ExtremeAutomation.Library.Net.Packet.Ethernet2TaggedPacket import Ethernet2TaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DbsyncDvrPacketHeader import DbsyncDvrPacketHeader


class Ethernet2DbsyncDvrTaggedPacket(Ethernet2TaggedPacket, DbsyncDvrPacketHeader):
    def __init__(self):
        super(Ethernet2DbsyncDvrTaggedPacket, self).__init__()
        DbsyncDvrPacketHeader.__init__(self)
        self.set_name("Ethernet2DbsyncDvrTaggedPacket")

    def to_packet_string(self):
        return super(Ethernet2DbsyncDvrTaggedPacket, self).to_packet_string() + \
            DbsyncDvrPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2DbsyncDvrTaggedPacket, self).build()
        DbsyncDvrPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2DbsyncDvrTaggedPacket, self).build()
        return super(Ethernet2DbsyncDvrTaggedPacket, self).get_header_length() + self.HEADER_SIZE_DBSYNCDVR

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2DbsyncDvrTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(DbsyncDvrPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2DbsyncDvrTaggedPacket, self).set_payload(payload)
        DbsyncDvrPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2DbsyncDvrTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + DbsyncDvrPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2DbsyncDvrTaggedPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        DbsyncDvrPacketHeader.config_thirdparty_traffic_generator_stream_dbsyncdvr(self, tgen_type, generator_ref,
                                                                                   port_string, stream_id, **kwargs)
