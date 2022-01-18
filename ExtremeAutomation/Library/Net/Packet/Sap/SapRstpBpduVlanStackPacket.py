from ExtremeAutomation.Library.Net.Packet.Sap.SapBpduVlanStackPacket import SapBpduVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RstpPacketHeader import RstpPacketHeader


class SapRstpBpduVlanStackPacket(SapBpduVlanStackPacket, RstpPacketHeader):
    def __init__(self, num_tags):
        super(SapRstpBpduVlanStackPacket, self).__init__(num_tags)
        RstpPacketHeader.__init__(self)
        self.set_name("SapRstpBpduVlanStackPacket")

    def to_packet_string(self):
        return super(SapRstpBpduVlanStackPacket, self).to_packet_string() + \
            RstpPacketHeader.to_packet_string(self)

    def build(self):
        super(SapRstpBpduVlanStackPacket, self).build()
        RstpPacketHeader.build(self)

    def get_hltapi_commands(self):
        cmd_dict = super(SapRstpBpduVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(RstpPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(SapRstpBpduVlanStackPacket, self).set_payload(payload)
        RstpPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(SapRstpBpduVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + RstpPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")
