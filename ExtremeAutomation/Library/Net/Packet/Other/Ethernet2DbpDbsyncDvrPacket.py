from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2DbsyncDvrPacket import Ethernet2DbsyncDvrPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DbsyncDvrDbpPacketHeader import DbsyncDvrDbpPacketHeader


class Ethernet2DbpDbsyncDvrPacket(Ethernet2DbsyncDvrPacket, DbsyncDvrDbpPacketHeader):
    def __init__(self):
        super(Ethernet2DbpDbsyncDvrPacket, self).__init__()
        DbsyncDvrDbpPacketHeader.__init__(self)
        self.set_name("Ethernet2DbpDbsyncDvrPacket")

    def to_packet_string(self):
        return super(Ethernet2DbpDbsyncDvrPacket, self).to_packet_string() + \
            DbsyncDvrDbpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2DbpDbsyncDvrPacket, self).build()
        DbsyncDvrDbpPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2DbpDbsyncDvrPacket, self).build()
        return super(Ethernet2DbpDbsyncDvrPacket, self).get_header_length() + self.HEADER_SIZE_DBSYNCDVR

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2DbpDbsyncDvrPacket, self).get_hltapi_commands()
        cmd_dict.update(DbsyncDvrDbpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2DbpDbsyncDvrPacket, self).set_payload(payload)
        DbsyncDvrDbpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2DbpDbsyncDvrPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + DbsyncDvrDbpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2DbpDbsyncDvrPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        DbsyncDvrDbpPacketHeader.config_thirdparty_traffic_generator_stream_dbpdbsyncdvr(
            self, tgen_type, generator_ref, port_string, stream_id, **kwargs)
