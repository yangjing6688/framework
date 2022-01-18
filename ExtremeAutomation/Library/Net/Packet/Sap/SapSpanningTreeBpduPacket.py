from ExtremeAutomation.Library.Net.Packet.Sap.SapBpduPacket import SapBpduPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SpanningTreePacketHeader import SpanningTreePacketHeader


class SapSpanningTreeBpduPacket(SapBpduPacket, SpanningTreePacketHeader):
    def __init__(self):
        super(SapSpanningTreeBpduPacket, self).__init__()
        SpanningTreePacketHeader.__init__(self)
        self.set_name("SapSpanningTreeBpduPacket")

    def to_packet_string(self):
        return super(SapSpanningTreeBpduPacket, self).to_packet_string() + \
            SpanningTreePacketHeader.to_packet_string(self)

    def build(self):
        super(SapSpanningTreeBpduPacket, self).build()
        SpanningTreePacketHeader.build(self)

    def get_hltapi_commands(self):
        cmd_dict = super(SapSpanningTreeBpduPacket, self).get_hltapi_commands()
        cmd_dict.update(SpanningTreePacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapSpanningTreeBpduPacket, self).set_payload(payload)
        SpanningTreePacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapSpanningTreeBpduPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + SpanningTreePacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")
