from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2DbsyncDvrVlanStackPacket import \
    Ethernet2DbsyncDvrVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DbsyncDvrDbpPacketHeader import DbsyncDvrDbpPacketHeader


class Ethernet2DbpDbsyncDvrVlanStackPacket(Ethernet2DbsyncDvrVlanStackPacket, DbsyncDvrDbpPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2DbpDbsyncDvrVlanStackPacket, self).__init__(num_tags)
        DbsyncDvrDbpPacketHeader.__init__(self)
        self.set_name("Ethernet2DbpDbsyncDvrVlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2DbpDbsyncDvrVlanStackPacket, self).to_packet_string() + \
            DbsyncDvrDbpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2DbpDbsyncDvrVlanStackPacket, self).build()
        DbsyncDvrDbpPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2DbpDbsyncDvrVlanStackPacket, self).build()
        return super(Ethernet2DbpDbsyncDvrVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_DBSYNCDVR

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2DbpDbsyncDvrVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(DbsyncDvrDbpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2DbpDbsyncDvrVlanStackPacket, self).set_payload(payload)
        DbsyncDvrDbpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2DbpDbsyncDvrVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + DbsyncDvrDbpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2DbpDbsyncDvrVlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        DbsyncDvrDbpPacketHeader.config_thirdparty_traffic_generator_stream_dbpdbsyncdvr(
            self, tgen_type, generator_ref, port_string, stream_id, **kwargs)
