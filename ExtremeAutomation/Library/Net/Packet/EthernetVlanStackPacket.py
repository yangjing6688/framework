from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader


class EthernetVlanStackPacket(EthernetPacket, VlanStackPacketHeader):
    def __init__(self, num_tags):
        super(EthernetVlanStackPacket, self).__init__()
        VlanStackPacketHeader.__init__(self)
        self.set_name("EthernetVlanStackPacket")
        self.num_tags = num_tags

    def to_packet_string(self):
        return super(EthernetVlanStackPacket, self).to_packet_string() + VlanStackPacketHeader.to_packet_string(self)

    def build(self):
        super(EthernetVlanStackPacket, self).build()
        VlanStackPacketHeader.build(self)

    def get_header_length(self):
        return super(EthernetVlanStackPacket, self).get_header_length() + (self.get_vlan_num() *
                                                                           self.HEADER_SIZE_VLAN_STACK)

    def get_hltapi_commands(self):
        cmd_dict = super(EthernetVlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(VlanStackPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(EthernetVlanStackPacket, self).set_payload(payload)
        VlanStackPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetVlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + VlanStackPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(EthernetVlanStackPacket, self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref,
                                                                                        port_string, stream_id,
                                                                                        **kwargs)
        VlanStackPacketHeader.config_thirdparty_traffic_generator_stream_vlan_stack(self, tgen_type, generator_ref,
                                                                                    port_string, stream_id, **kwargs)
