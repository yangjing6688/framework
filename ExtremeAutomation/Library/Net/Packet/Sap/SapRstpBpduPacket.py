from ExtremeAutomation.Library.Net.Packet.Sap.SapBpduPacket import SapBpduPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RstpPacketHeader import RstpPacketHeader


class SapRstpBpduPacket(SapBpduPacket, RstpPacketHeader):
    def __init__(self):
        super(SapRstpBpduPacket, self).__init__()
        RstpPacketHeader.__init__(self)
        self.set_name("SapRstpBpduPacket")

    def to_packet_string(self):
        return super(SapRstpBpduPacket, self).to_packet_string() + \
            RstpPacketHeader.to_packet_string(self)

    def build(self):
        super(SapRstpBpduPacket, self).build()
        RstpPacketHeader.build(self)

    def get_hltapi_commands(self):
        cmd_dict = super(SapRstpBpduPacket, self).get_hltapi_commands()
        cmd_dict.update(RstpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapRstpBpduPacket, self).set_payload(payload)
        RstpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapRstpBpduPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + RstpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")
