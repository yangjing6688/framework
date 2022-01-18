from ExtremeAutomation.Library.Net.Packet.Sap.SapBpduTaggedPacket import SapBpduTaggedPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RstpPacketHeader import RstpPacketHeader


class SapRstpBpduTaggedPacket(SapBpduTaggedPacket, RstpPacketHeader):
    def __init__(self):
        super(SapRstpBpduTaggedPacket, self).__init__()
        RstpPacketHeader.__init__(self)
        self.set_name("SapRstpBpduTaggedPacket")

    def to_packet_string(self):
        return super(SapRstpBpduTaggedPacket, self).to_packet_string() + \
            RstpPacketHeader.to_packet_string(self)

    def build(self):
        super(SapRstpBpduTaggedPacket, self).build()
        RstpPacketHeader.build(self)

    def get_hltapi_commands(self):
        cmd_dict = super(SapRstpBpduTaggedPacket, self).get_hltapi_commands()
        cmd_dict.update(RstpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapRstpBpduTaggedPacket, self).set_payload(payload)
        RstpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapRstpBpduTaggedPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + RstpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")
