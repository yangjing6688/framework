from ExtremeAutomation.Library.Net.Packet.Sap.SapBpduTaggedPacket import SapBpduTaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SpanningTreePacketHeader import SpanningTreePacketHeader


class SapSpanningTreeBpduTaggedPacket(SapBpduTaggedPacket, SpanningTreePacketHeader):
    def __init__(self):
        super(SapSpanningTreeBpduTaggedPacket, self).__init__()
        SpanningTreePacketHeader.__init__(self)
        self.set_name("SapSpanningTreeBpduTaggedPacket")

    def to_packet_string(self):
        return super(SapSpanningTreeBpduTaggedPacket, self).to_packet_string() + \
            SpanningTreePacketHeader.to_packet_string(self)

    def build(self):
        super(SapSpanningTreeBpduTaggedPacket, self).build()
        SpanningTreePacketHeader.build(self)

    def get_hltapi_commands(self):
        cmd_dict = super(SapSpanningTreeBpduTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(SpanningTreePacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapSpanningTreeBpduTaggedPacket, self).set_payload(payload)
        SpanningTreePacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapSpanningTreeBpduTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + SpanningTreePacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")
