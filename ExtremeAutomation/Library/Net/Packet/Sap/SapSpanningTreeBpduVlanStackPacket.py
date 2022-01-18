from ExtremeAutomation.Library.Net.Packet.Sap.SapBpduVlanStackPacket import SapBpduVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SpanningTreePacketHeader import SpanningTreePacketHeader


class SapSpanningTreeBpduVlanStackPacket(SapBpduVlanStackPacket, SpanningTreePacketHeader):
    def __init__(self, num_tags):
        super(SapSpanningTreeBpduVlanStackPacket, self).__init__(num_tags)
        SpanningTreePacketHeader.__init__(self)
        self.set_name("SapSpanningTreeBpduVlanStackPacket")

    def to_packet_string(self):
        return super(SapSpanningTreeBpduVlanStackPacket, self).to_packet_string() + \
            SpanningTreePacketHeader.to_packet_string(self)

    def build(self):
        super(SapSpanningTreeBpduVlanStackPacket, self).build()
        SpanningTreePacketHeader.build(self)

    def get_hltapi_commands(self):
        cmd_dict = super(SapSpanningTreeBpduVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(SpanningTreePacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapSpanningTreeBpduVlanStackPacket, self).set_payload(payload)
        SpanningTreePacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapSpanningTreeBpduVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + SpanningTreePacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")
