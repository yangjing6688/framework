from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.udp_pb2 import udp
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer4PacketHeader import Layer4PacketHeader
from ExtremeAutomation.Library.Net.Packet.Checksum import Checksum
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class UdpPacketHeader(Layer4PacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    UDP Packet Header
        # source port = 16bits
        # destination port = 16bits
        # sequence number = 32bits
        # acknowledgement number = 32bits
        # data offset = 4bits
        # reserved = 8bits
        # flags = 4bits
        # window = 16bits
        # checksum = 16bits
        # urgent porter = 16bits
        # options = nbits
    """
    def __init__(self):
        super(UdpPacketHeader, self).__init__()
        self.add_header()
        self.HEADER_SIZE_UDP = (16 + 16 + 16 + 16) // 8

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Udp source port methods
    #  source_port is a 16 bit INTEGER example: 1
    def set_source_port(self, source_port, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(UdpPacketConstants.UDP_SOURCE_PORT, ignore_check)
        source_port = self.normalize_value(source_port, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_UDP, UdpPacketConstants.UDP_SOURCE_PORT, source_port)

    def get_source_port(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_UDP, UdpPacketConstants.UDP_SOURCE_PORT),
            PacketConstants.INTEGER)

    def get_source_port_hltapi_cmd(self, dummy_dict):
        source_port = self.get_source_port()
        if isinstance(source_port, int):
            source_port = str(source_port)
        if source_port and 'Not Set' not in source_port:
            dummy_dict[TrafficConfigConstants.UDP_SRC_PORT_CMD] = source_port
    # end Udp source port methods

    # start Udp destination port methods
    #  destination_port is a 16 bit INTEGER example: 1
    def set_destination_port(self, destination_port, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(UdpPacketConstants.UDP_DESTINATION_PORT, ignore_check)
        destination_port = self.normalize_value(destination_port, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_UDP, UdpPacketConstants.UDP_DESTINATION_PORT,
                                  destination_port)

    def get_destination_port(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_UDP, UdpPacketConstants.UDP_DESTINATION_PORT),
            PacketConstants.INTEGER)

    def get_destination_port_hltapi_cmd(self, dummy_dict):
        destination_port = self.get_destination_port()
        if isinstance(destination_port, int):
            destination_port = str(destination_port)
        if destination_port and 'Not Set' not in destination_port:
            dummy_dict[TrafficConfigConstants.UDP_DST_PORT_CMD] = destination_port
    # end Udp destination port methods

    # start Udp length methods
    #  length is a 16 bit INTEGER example: 1
    def set_udp_length(self, length, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(UdpPacketConstants.UDP_LENGTH, ignore_check)
        length = self.normalize_value(length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_UDP, UdpPacketConstants.UDP_LENGTH, length)

    def get_udp_length(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_UDP, UdpPacketConstants.UDP_LENGTH),
            PacketConstants.INTEGER)

    def get_length_udp_hltapi_cmd(self, dummy_dict):
        length = self.get_length()
        if isinstance(length, int):
            length = str(length)
        if length and 'Not Set' not in length:
            dummy_dict[TrafficConfigConstants.TEMP_LENGTH_CMD] = length
    # end Udp length methods

    # start Udp checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_udp_checksum(self, checksum, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(UdpPacketConstants.UDP_CHECKSUM, ignore_check)
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_UDP, UdpPacketConstants.UDP_CHECKSUM, checksum)

    def get_udp_checksum(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_UDP, UdpPacketConstants.UDP_CHECKSUM),
            PacketConstants.INTEGER)

    def get_udp_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_udp_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end Udp checksum methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("source port", self.format_int(self.get_source_port(), 4))
        table.add_row_value("destination port", self.format_int(self.get_destination_port(), 4))
        table.add_row_value("length", self.format_int(self.get_udp_length(), 4))
        table.add_row_value("checksum", self.format_int(self.get_udp_checksum(), 4))
        return "\n\nUDP HEADER" + table.to_table_string()

    def add_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_UDP)

    def build(self):
        self.add_header()
        if isinstance(self, IpV4PacketHeader):  # you can either do this here OR in the build of each packet
            self.set_ip_protocol("0x11", True)
        elif isinstance(self, IpV6PacketHeader):
            self.set_ipv6_next_header("0x11", True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        self.get_source_port_hltapi_cmd(dummy_dict)
        self.get_destination_port_hltapi_cmd(dummy_dict)
        # self.get_length_hltapi_cmd(dummy_dict)
        # self.get_checksum_hltapi_cmd(dummy_dict)
        dummy_dict[TrafficConfigConstants.L4_PROTOCOL_CMD] = TrafficConfigConstants.L4_PROTOCOL_UDP  # constant value
        return dummy_dict

    def get_spirent_udp_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_udp(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_udp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_udp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_udp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kUdpFieldNumber
        udpField = p.Extensions[udp]
        # cksum = {int} 0
        # is_override_cksum = {bool} False
        if self.is_field_set(self.get_udp_checksum()):
            udpField.cksum = int(self.get_udp_checksum())
            udpField.is_override_cksum = True
        else:
            udpField.is_override_cksum = False
        # src_port = {int} 49152
        # is_override_src_port = {bool} False
        if self.is_field_set(self.get_source_port()):
            udpField.src_port = int(self.get_source_port())
            udpField.is_override_src_port = True
        else:
            udpField.is_override_src_port = False
        # dst_port = {int} 49153
        # is_override_dst_port = {bool} False
        if self.is_field_set(self.get_destination_port()):
            udpField.dst_port = int(self.get_destination_port())
            udpField.is_override_dst_port = True
        else:
            udpField.is_override_dst_port = False
        # totlen = {int} 0
        # is_override_totlen = {bool} False
        if self.is_field_set(self.get_udp_length()):
            udpField.totlen = int(self.get_udp_length())
            udpField.is_override_totlen = True
        else:
            udpField.is_override_totlen = False

    def config_jets_stream_udp(self, jets_dev, port_string, stream_id, **kwargs):
        """
        UDP_HDR {
          udp_src_port  : 16 : legal_values = (RESERVED=0, TCPMUX=1, ECHO=7, DISCARD=9, DAYTIME=13, CHARGEN=19, TIME=37,
                               NAME=42, DNS=53, BOOTP=67, BOOTP=68, TFTP=69, HTTP=80, SUNRPC=111, ERPC=121, NTP=123,
                               NETBIOS_NAME_SERVICE=137, NETBIOS_DGRAM_SERVICE=138, SNMP=161, SNMP_TRAP=162, XDM=177,
                               ALBD=371, EDDP=387, IKE=500, BIFF=512, WHO=513, SYSLOG=514, TALK=517, RIP=520, RIPNG=521,
                               NEW_RWHO=550, RMONITOR=560, MONITOR=561, LDP=646, SUNRPC=660, SECURID=755, PSADMIND=964,
                               SUNRPC=1021, SUNRPC=1022, AUTOMAT=1025, L2TP=1701, RADIUS_AUTH=1645, RADIUS_ACCT=1646,
                               RTP_HDR=2434, RTCP_HDR=2435, WSNOTIFY=2001, NETTIME=2002, CDXLOCK=2011, ZEPHYR_CTL=2103,
                               ZEPHYR_HM=2104, MGCP_HDR=2427, PUBLIC=700, BTS=50000 ), display="Source Port", index=1;
          udp_dest_port : 16 : legal_values = (RESERVED=0, TCPMUX=1, ECHO=7, DISCARD=9, DAYTIME=13, CHARGEN=19, TIME=37,
                               NAME=42, DNS=53, BOOTP=67, BOOTP=68, TFTP=69, HTTP=80, SUNRPC=111, ERPC=121, NTP=123,
                               NETBIOS_NAME_SERVICE=137, NETBIOS_DGRAM_SERVICE=138, SNMP=161, SNMP_TRAP=162, XDM=177,
                               ALBD=371, EDDP=387, IKE=500, BIFF=512, WHO=513, SYSLOG=514, TALK=517, RIP=520, RIPNG=521,
                               NEW_RWHO=550, RMONITOR=560, MONITOR=561, LDP=646, SUNRPC=660, SECURID=755, PSADMIND=964,
                               SUNRPC=1021, SUNRPC=1022, AUTOMAT=1025, L2TP=1701, RADIUS_AUTH=1645, RADIUS_ACCT=1646,
                               RTP_HDR=2434, RTCP_HDR=2435, WSNOTIFY=2001, NETTIME=2002, CDXLOCK=2011, ZEPHYR_CTL=2103,
                               ZEPHYR_HM=2104, MGCP_HDR=2427, PUBLIC=700, BTS=50000 ), display="Destination Port",
                               index=2;
          udp_length    : 16 : send = length(node, pdu), display = "Length %dec bytes", index=3;
          udp_xsum      : 16 : send = checksum(udp, ip_offset, ip_offset), display="Checksum", index=4;
        } display="UDP Header", index=5130;
        """
        if isinstance(self, IpV6PacketHeader):
            if not self.is_field_set(self.get_ipv6_next_header()):
                jets_dev.pdl_add_packet_header(JetsDeviceConstants.IPV6_HDR, {"next_header": 0x11})
                # if extention headers, find the last one and set that.
            if self.get_ipv6_extension_headers_length() > 1:
                self.get_ipv6_extension_headers()[-1].next_next_header = 0x11
        if self.header_in_bytes_only:
            pkt_bytes = "0x" + UdpPacketHeader.get_header_bytes(self)
            jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        else:
            pkt_fields = {}
            if self.is_field_set(self.get_source_port()):
                pkt_fields["udp_src_port"] = str(self.get_source_port())
            if self.is_field_set(self.get_destination_port()):
                pkt_fields["udp_dest_port"] = str(self.get_destination_port())
            if self.is_field_set(self.get_udp_length()):
                pkt_fields["udp_length"] = str(self.get_udp_length())
            if self.is_field_set(self.get_udp_checksum()):
                pkt_fields["udp_xsum"] = str(self.get_udp_checksum())

            jets_dev.pdl_add_packet_header("UDP_HDR", pkt_fields)

    def configure_udp_length(self, length):
        self.set_udp_length(length)

    def calculate_udp_checksum(self, header_offset):
        self.set_udp_checksum(0)
        header_sum = Checksum.calculate_udp_checksum(self, self.get_bytes(), header_offset)
        header_sum = Checksum.calculate_complement(header_sum)
        self.set_udp_checksum(header_sum)
        pass

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        if len(payload) >= 16:
            source_port = self.get_bits_from_string(16, payload)
            self.set_source_port("0x" + source_port)
            payload = self.remove_bits_from_string(16, payload)
            destination_port = self.get_bits_from_string(16, payload)
            self.set_destination_port("0x" + destination_port)
            payload = self.remove_bits_from_string(16, payload)
            length = self.get_bits_from_string(16, payload)
            self.set_udp_length("0x" + length)
            payload = self.remove_bits_from_string(16, payload)
            checksum = self.get_bits_from_string(16, payload)
            self.set_udp_checksum("0x" + checksum)
            payload = self.remove_bits_from_string(16, payload)
        else:
            PacketObject.logger.log_info("No UDP header in payload: " + str(payload))
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_source_port(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_destination_port(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_udp_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_udp_checksum(), PacketConstants.INTEGER, 16)
        return ret_string

    @staticmethod
    def compare_udp_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                  print_failures=True):
        results = True
        try:
            assert isinstance(expected, UdpPacketHeader)
            assert isinstance(actual, UdpPacketHeader)
            if expected.do_i_check_this_field(expected.get_source_port(), UdpPacketConstants.UDP_SOURCE_PORT,
                                              ignore_list, include_list):
                name = "UDP source port : "
                if expected.get_source_port() != actual.get_source_port():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_source_port()) + " != " +
                                                      str(actual.get_source_port()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_source_port()) + " == " +
                                                 str(actual.get_source_port()) + " Pass")

            if expected.do_i_check_this_field(expected.get_destination_port(), UdpPacketConstants.UDP_DESTINATION_PORT,
                                              ignore_list, include_list):
                name = "UDP destination port : "
                if expected.get_destination_port() != actual.get_destination_port():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_destination_port()) + " != " +
                                                      str(actual.get_destination_port()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_destination_port()) + " == " +
                                                 str(actual.get_destination_port()) + " Pass")

            if expected.do_i_check_this_field(expected.get_udp_length(), UdpPacketConstants.UDP_LENGTH,
                                              ignore_list, include_list):
                name = "UDP length : "
                if expected.get_udp_length() != actual.get_udp_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_udp_length()) + " != " +
                                                      str(actual.get_udp_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_udp_length()) + " == " +
                                                 str(actual.get_udp_length()) + " Pass")

            if expected.do_i_check_this_field(expected.get_udp_checksum(), UdpPacketConstants.UDP_CHECKSUM,
                                              ignore_list, include_list):
                name = "UDP checksum : "
                if expected.get_udp_checksum() != actual.get_udp_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_udp_checksum()) + " != " +
                                                      str(actual.get_udp_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_udp_checksum()) + " == " +
                                                 str(actual.get_udp_checksum()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with UdpPacketHeader")
        return results


class UdpPacketConstants:
    def __init__(self):
        pass

    UDP_SOURCE_PORT = "UDP_SOURCE_PORT"
    UDP_DESTINATION_PORT = "UDP_DESTINATION_PORT"
    UDP_LENGTH = "UDP_LENGTH"
    UDP_CHECKSUM = "UDP_CHECKSUM"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
