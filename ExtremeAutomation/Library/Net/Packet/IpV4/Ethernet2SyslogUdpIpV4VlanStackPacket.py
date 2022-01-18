from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4VlanStackPacket import Ethernet2UdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SyslogPacketHeader import SyslogPacketHeader


class Ethernet2SyslogUdpIpV4VlanStackPacket(Ethernet2UdpIpV4VlanStackPacket, SyslogPacketHeader):
    def __init__(self, num_tags):
        super(Ethernet2SyslogUdpIpV4VlanStackPacket, self).__init__(num_tags)
        SyslogPacketHeader.__init__(self)
        self.set_name("Ethernet2SyslogUdpIpV4VlanStackPacket")

    def to_packet_string(self):
        return super(Ethernet2SyslogUdpIpV4VlanStackPacket, self).to_packet_string() + \
            SyslogPacketHeader.to_packet_string(self)

    def build(self):
        super(Ethernet2SyslogUdpIpV4VlanStackPacket, self).build()
        SyslogPacketHeader.build(self)

    def get_header_length(self):
        super(Ethernet2SyslogUdpIpV4VlanStackPacket, self).build()
        return super(Ethernet2SyslogUdpIpV4VlanStackPacket, self).get_header_length() + self.HEADER_SIZE_SYSLOG

    def get_hltapi_commands(self):
        cmd_dict = super(Ethernet2SyslogUdpIpV4VlanStackPacket, self).get_hltapi_commands()
        cmd_dict.update(SyslogPacketHeader.get_hltapi_commands(self))
        return cmd_dict

    def set_payload(self, payload):
        payload = payload.replace(" ", "")
        super(Ethernet2SyslogUdpIpV4VlanStackPacket, self).set_payload(payload)
        SyslogPacketHeader.parse_bytes(self)

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(Ethernet2SyslogUdpIpV4VlanStackPacket, self).get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "|"
        temp_bytes += " " + SyslogPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        super(Ethernet2SyslogUdpIpV4VlanStackPacket, self).config_thirdparty_traffic_generator_stream(tgen_type,
                                                                                                      generator_ref,
                                                                                                      port_string,
                                                                                                      stream_id,
                                                                                                      **kwargs)
        SyslogPacketHeader.config_thirdparty_traffic_generator_stream_syslog(self, tgen_type, generator_ref,
                                                                             port_string, stream_id, **kwargs)
