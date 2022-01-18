from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2DbsyncDvrVlanStackPacket import \
    Ethernet2DbsyncDvrVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DbsyncDvrCsnpPacketHeader import DbsyncDvrCsnpPacketHeader


class Ethernet2CsnpDbsyncDvrVlanStackPacket(Ethernet2DbsyncDvrVlanStackPacket, DbsyncDvrCsnpPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2CsnpDbsyncDvrVlanStackPacket, self).__init__(num_tags)
        DbsyncDvrCsnpPacketHeader.__init__(self)
        self.set_name("Ethernet2CsnpDbsyncDvrVlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2CsnpDbsyncDvrVlanStackPacket, self).to_packet_string() + \
            DbsyncDvrCsnpPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2CsnpDbsyncDvrVlanStackPacket, self).build()
        DbsyncDvrCsnpPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2CsnpDbsyncDvrVlanStackPacket, self).build()
        return super(Ethernet2CsnpDbsyncDvrVlanStackPacket, self).get_header_length() + self.HEADER_SIZE_DBSYNCDVR

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2CsnpDbsyncDvrVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(DbsyncDvrCsnpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2CsnpDbsyncDvrVlanStackPacket, self).set_payload(payload)
        DbsyncDvrCsnpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2CsnpDbsyncDvrVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + DbsyncDvrCsnpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2CsnpDbsyncDvrVlanStackPacket, self).config_thirdparty_traffic_generator_stream(
            tgen_type, generator_ref, port_string, stream_id, **kwargs)
        DbsyncDvrCsnpPacketHeader.config_thirdparty_traffic_generator_stream_dbsyncdvrcsnp(
            self, tgen_type, generator_ref, port_string, stream_id, **kwargs)
