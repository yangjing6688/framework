from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import SnapPacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.ip4_pb2 import ip4
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.Checksum import Checksum
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer3PacketHeader import Layer3PacketHeader
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class IpV4PacketHeader(Layer3PacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    IPv4 Packet Header
        # version = 4bits
        # hdlen = 4bits
        # TOS = 8 bits/1 byte
        # Length = 16 bits
        # ID = 16 bits
        # flags + frag offset = 16 bits
        # TTL = 8 bits
        # Protocol = 8 bits
        # checksum = 16 bits
        # SIP = 32 bits
        # DIP = 32 bits
        # Options = Length - 20
    """
    def __init__(self):
        super(IpV4PacketHeader, self).__init__()
        self.add_ipv4_header()
        self.HEADER_SIZE_IPV4 = (4 + 4 + 8 + 16 + 16 + 16 + 8 + 8 + 16 + 32 + 32) // 8  # + optinos

    # start destination ip methods
    def set_destination_ip(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_DIP, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_DIP, ip)

    def get_destination_ip(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_DIP), PacketConstants.IPV4_ADDRESS)

    def get_destination_ip_hex_string(self):
        ip = self.get_destination_ip()
        if Ipv4Address.is_valid_ipv4(ip):
            ip = Ipv4Address(ip)
            return ip.to_formated_string(16, "")
        else:
            return None

    def get_destination_ip_hltapi_cmd(self, dummy_dict):
        if self.get_destination_ip() and 'Not Set' not in self.get_destination_ip():
            dummy_dict[TrafficConfigConstants.IP_DST_ADDR_CMD] = self.get_destination_ip()

    def set_destination_ip_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_DIP_MODE, ip)

    def get_destination_ip_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_DIP_MODE)

    def set_destination_ip_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_DIP_COUNT, ip)

    def get_destination_ip_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_DIP_COUNT)

    def set_destination_ip_mask(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_DIP_MASK, ip)

    def get_destination_ip_mask(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_DIP_MASK)
    # end destination ip method

    # start source ip methods
    def set_source_ip(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_SIP, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_SIP, ip)

    def get_source_ip(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_SIP), PacketConstants.IPV4_ADDRESS)

    def get_source_ip_hex_string(self):
        ip = self.get_source_ip()
        if Ipv4Address.is_valid_ipv4(ip):
            ip = Ipv4Address(ip)
            return ip.to_formated_string(16, "")
        else:
            return None

    def get_source_ip_hltapi_cmd(self, dummy_dict):
        if self.get_source_ip() and 'Not Set' not in self.get_source_ip():
            dummy_dict[TrafficConfigConstants.IP_SRC_ADDR_CMD] = self.get_source_ip()

    def set_source_ip_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_SIP_MODE, ip)

    def get_source_ip_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_SIP_MODE)

    def set_source_ip_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_SIP_COUNT, ip)

    def get_source_ip_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_SIP_COUNT)

    def set_source_ip_mask(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_SIP_MASK, ip)

    def get_source_ip_mask(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_SIP_MASK)
    # end source ip methods

    # start protocol ip methods
    def set_ip_protocol(self, protocol, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_PROTOCOL, ignore_check)
        protocol = self.normalize_value(protocol, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_PROTOCOL, protocol)

    def get_ip_protocol(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_PROTOCOL), PacketConstants.INTEGER)

    def get_ip_protocol_hltapi_cmd(self, dummy_dict):
        protocol = self.get_ip_protocol()
        if isinstance(protocol, int):
            protocol = str(protocol)
        if protocol and 'Not Set' not in protocol:
            dummy_dict[TrafficConfigConstants.IP_PROTOCOL_CMD] = protocol
    # end protocol ip methods

    # start ip tos methods
    def set_ip_tos(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_IP_TOS, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_IP_TOS, ip)

    def get_ip_tos(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_IP_TOS), PacketConstants.INTEGER)

    def get_ip_tos_hltapi_cmd(self, dummy_dict):
        tos = self.get_ip_tos()
        if isinstance(tos, int):
            tos = str(tos)
        if tos and 'Not Set' not in tos:
            dummy_dict[TrafficConfigConstants.IP_PRECEDENCE_CMD] = str((int(tos) & 0x0E0) >> 5)
            dummy_dict[TrafficConfigConstants.IP_DELAY_CMD] = str((int(tos) & 0x010) >> 4)
            dummy_dict[TrafficConfigConstants.IP_THROUGHPUT_CMD] = str((int(tos) & 0x08) >> 3)
            dummy_dict[TrafficConfigConstants.IP_RELIABILITY_CMD] = str((int(tos) & 0x04) >> 2)
            dummy_dict[TrafficConfigConstants.IP_COST_CMD] = str((int(tos) & 0x02) >> 1)
            dummy_dict[TrafficConfigConstants.IP_RESERVED_CMD] = str((int(tos) & 0x01) >> 0)
    # end ip tos methods

    # start ip hdr length methods
    def set_ip_length(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_IP_LENGTH, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_IP_LENGTH, ip)

    def get_ip_length(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_IP_LENGTH),
            PacketConstants.INTEGER)

    def get_ip_length_hltapi_cmd(self, dummy_dict):
        tos = self.get_ip_length()
        if isinstance(tos, int):
            tos = str(tos)
        if tos and 'Not Set' not in tos:
            dummy_dict[TrafficConfigConstants.IP_LENGTH_CMD] = tos
    # end ip hdr length methods

    # start ip hdr length methods
    def set_ip_hdr_length(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_IP_HDR_LENGTH, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_IP_HDR_LENGTH, ip)

    def get_ip_hdr_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_IP_HDR_LENGTH), PacketConstants.INTEGER)

    def get_ip_hdr_length_hltapi_cmd(self, dummy_dict):
        tos = self.get_ip_hdr_length()
        if isinstance(tos, int):
            tos = str(tos)
        if tos and 'Not Set' not in tos:
            dummy_dict[TrafficConfigConstants.IP_HDR_LENGTH_CMD] = tos
    # end ip hdr length methods

    # start ip chrecksum methods
    def set_ip_checksum(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_CHECKSUM, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_CHECKSUM, ip)

    def get_ip_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_CHECKSUM), PacketConstants.INTEGER)

    def get_ip_checksum_hltapi_cmd(self, dummy_dict):
        tos = self.get_ip_checksum()
        if isinstance(tos, int):
            tos = str(tos)
        if tos and 'Not Set' not in tos:
            dummy_dict[TrafficConfigConstants.IP_CHECKSUM_CMD] = tos
    # end ip checksum methods

    # start ip id methods
    def set_ip_id(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_ID, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_ID, ip)

    def get_ip_id(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_ID),
            PacketConstants.INTEGER)

    def get_ip_id_hltapi_cmd(self, dummy_dict):
        tos = self.get_ip_id()
        if isinstance(tos, int):
            tos = str(tos)
        if tos and 'Not Set' not in tos:
            dummy_dict[TrafficConfigConstants.IP_ID_CMD] = tos
    # end ip id methods

    # start ip flags methods
    def set_ip_flags(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_FLAGS, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_FLAGS, ip)

    def set_ip_flags_dont_frag(self):
        tos = self.get_ip_flags()
        if isinstance(tos, str):
            if 'Not Set' in tos:
                tos = 0
            else:
                tos = int(tos)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_FLAGS, tos | 0x02)

    def set_ip_flags_may_frag(self):
        tos = self.get_ip_flags()
        if isinstance(tos, str):
            if 'Not Set' in tos:
                tos = 0
            else:
                tos = int(tos)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_FLAGS, tos & 0x0D)

    def set_ip_flags_more_frag(self):
        tos = self.get_ip_flags()
        if isinstance(tos, str):
            if 'Not Set' in tos:
                tos = 0
            else:
                tos = int(tos)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_FLAGS, tos | 0x01)

    def set_ip_flags_last_frag(self):
        tos = self.get_ip_flags()
        if isinstance(tos, str):
            if 'Not Set' in tos:
                tos = 0
            else:
                tos = int(tos)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_FLAGS, tos & 0x0E)

    def get_ip_flags(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_FLAGS),
            PacketConstants.INTEGER)

    def get_ip_flags_hltapi_cmd(self, dummy_dict):
        tos = self.get_ip_flags()
        if isinstance(tos, int):
            tos = str(tos)
        if tos and 'Not Set' not in tos:
            # dummy_dict[TrafficConfigConstants.IP_FRAGMENT_CMD] = (int(tos) & 0x02) >> 1
            # dummy_dict[TrafficConfigConstants.IP_FRAGMENT_LAST_CMD] = (int(tos) & 0x01)
            if (int(tos) & 0x02) > 0:
                dummy_dict[TrafficConfigConstants.IP_FRAGMENT_CMD] = 0
            else:
                dummy_dict[TrafficConfigConstants.IP_FRAGMENT_CMD] = 1
            if (int(tos) & 0x01) > 0:
                dummy_dict[TrafficConfigConstants.IP_FRAGMENT_LAST_CMD] = 0
            else:
                dummy_dict[TrafficConfigConstants.IP_FRAGMENT_LAST_CMD] = 1
    # end ip flags methods

    # start ip fragment offset methods
    def set_ip_fragment_offset(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_FRAGMENT_OFFSET, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_FRAGMENT_OFFSET, ip)

    def get_ip_fragment_offset(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_FRAGMENT_OFFSET),
            PacketConstants.INTEGER)

    def get_ip_fragment_offset_hltapi_cmd(self, dummy_dict):
        tos = self.get_ip_fragment_offset()
        if isinstance(tos, int):
            tos = str(tos)
        if tos and 'Not Set' not in tos:
            dummy_dict[TrafficConfigConstants.IP_FRAGMENT_OFFSET_CMD] = tos
    # end ip flags methods

    # start source ttl methods
    def set_ip_ttl(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_TTL, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_TTL, ip)

    def get_ip_ttl(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_TTL), PacketConstants.INTEGER)

    def get_ip_ttl_hltapi_cmd(self, dummy_dict):
        ttl = self.get_ip_ttl()
        if isinstance(ttl, int):
            ttl = str(ttl)
        if ttl and 'Not Set' not in ttl:
            dummy_dict[TrafficConfigConstants.IP_TTL_CMD] = ttl
    # end source ttl methods

    # start source ip options methods
    def set_ip_options(self, ip, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV4PacketConstants.IPV4_OPTIONS, ignore_check)
        ip = self.normalize_value(ip, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_OPTIONS, ip)

    def set_ip_options_and_auto_pad(self, ip):
        ip = self.normalize_value(ip, PacketConstants.HEX_STRING)
        if len(ip.replace(" ", "")) % 8 != 0:
            ip += "0" * (8 - len(ip.replace(" ", "")) % 8)
            ip = self.normalize_value(ip, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_OPTIONS, ip)

    def get_ip_options(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV4, IpV4PacketConstants.IPV4_OPTIONS),
            PacketConstants.HEX_STRING)

    def get_ip_options_hltapi_cmd(self, dummy_dict):
        ttl = self.get_ip_options()
        if isinstance(ttl, int):
            ttl = str(ttl)
            # if ttl and 'Not Set' not in ttl:
            #     dummy_dict[TrafficConfigConstants.IP_TTL_CMD] = ttl
    # end source ip options methods

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Hdr Length", self.format_int(self.get_ip_hdr_length(), 2))
        table.add_row_value("TOS", self.format_int(self.get_ip_tos(), 1))
        table.add_row_value("Length", self.format_int(self.get_ip_length(), 2))
        table.add_row_value("ID", self.format_int(self.get_ip_id(), 2))
        table.add_row_value("Flags", self.format_int(self.get_ip_flags(), 1))
        table.add_row_value("Fragment Offset", self.format_int(self.get_ip_fragment_offset(), 2))
        table.add_row_value("TTL", self.format_int(self.get_ip_ttl(), 1))
        table.add_row_value("Protocol", self.format_int(self.get_ip_protocol(), 1))
        table.add_row_value("Checksum", self.format_int(self.get_ip_checksum(), 2))
        table.add_row_value("Destination IP", self.get_destination_ip())
        table.add_row_value("Source IP", self.get_source_ip())
        table.add_row_value("Options", self.get_ip_options())
        return "\n\nIPV4 HEADER" + table.to_table_string()

    def get_ixtclhal_ipv4_api_commands(self, port_string, streamid):
        if not self.get_ip_options() or 'Not' in self.get_ip_options():
            return []
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        dummy_dict.append("ip configure -options \"" + self.get_ip_options() + "\"")
        # ### put some IxTclHal info here.
        dummy_dict.append("ip set " + port_string)
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_ipv4_api_commands(self, port_name_stream):
        dummy_dict = []
        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def add_ipv4_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_IPV4)

    def build(self):
        self.add_ipv4_header()
        # if isinstance(self, Ethernet2PacketHeader):
        #     self.set_ether_type("0x800")
        if isinstance(self, SnapPacketHeader):
            self.set_snap_ether_type("0x800", True)
        else:
            try:
                self.set_ether_type("0x800", True)
            except Exception as e:
                PacketObject.logger.log_info("The following Exception was caught, Continuing on:\n" + repr(e))
        # self.set_destination_ip("0.0.0.0")
        # self.set_source_ip("0.0.0.0")

    def config_thirdparty_traffic_generator_stream_ipv4(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_ipv4(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_ipv4(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_ipv4(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kIp4FieldNumber
        # reduce typing by creating a shorter reference to p.Extensions[ip4]
        # src_ip = {int} 0
        ip = p.Extensions[ip4]
        if self.is_field_set(self.get_source_ip()):
            ip.src_ip = int("0x" + self.get_source_ip_hex_string(), 16)
        if self.is_field_set(self.get_destination_ip()):
            ip.dst_ip = int("0x" + self.get_destination_ip_hex_string(), 16)
        if self.is_field_set(self.get_ip_ttl()):
            ip.ttl = int(self.get_ip_ttl())
        # cksum = {int} 0
        # is_override_cksum = {bool} False
        if self.is_field_set(self.get_ip_checksum()):
            ip.cksum = int(self.get_ip_checksum())
            ip.is_override_cksum = True
        else:
            ip.is_override_cksum = False

        # ver_hdrlen = {int} 69
        # is_override_ver = {bool} False
        # is_override_hdrlen = {bool} False
        #
        # tos = {int} 0
        if self.is_field_set(self.get_ip_tos()):
            ip.tos = int(self.get_ip_tos())
        # totlen = {int} 0
        # is_override_totlen = {bool} False
        if self.is_field_set(self.get_ip_length()):
            ip.totlen = int(self.get_ip_length())
            ip.is_override_totlen = True
        else:
            ip.is_override_totlen = False
        # self.get_ip_length_hltapi_cmd(dummy_dict)
        # id = {int} 1234
        if self.is_field_set(self.get_ip_id()):
            ip.id = int(self.get_ip_id())
        # flags = {int} 0
        if self.is_field_set(self.get_ip_flags()):
            ip.flags = int(self.get_ip_flags())
        # frag_ofs = {int} 0
        if self.is_field_set(self.get_ip_fragment_offset()):
            ip.frag_ofs = int(self.get_ip_fragment_offset())
        # ttl = {int} 127
        if self.is_field_set(self.get_ip_ttl()):
            ip.ttl = int(self.get_ip_ttl())
        # self.get_ip_options_hltapi_cmd(dummy_dict)
        # proto = {int} 0
        # is_override_proto = {bool} False
        if self.is_field_set(self.get_ip_protocol()):
            ip.proto = int(self.get_ip_protocol())
            ip.is_override_proto = True
        else:
            ip.is_override_proto = False

        # ip.dst_ip_mode = Ip4.e_im_inc_host

    def config_jets_stream_ipv4(self, jets_dev, port_string, stream_id, **kwargs):
        """
        ip_ver      : 4  : legal_values=(RESERVED=0, UNASSIGNED=1-3, IP=4, STREAM_PROTOCOL_V2_=5, IPv6=6,
                      TP_IX_NEXT_INTERNET=7, PIP=8, TUBA=9, UNASSIGNED=10-14, RESERVED=15 ), default=4,
                      display="Version %dec", index=1;
        ip_ihl      : 4  : send = length(node, node) // 4,
                      display="Header Length %dec 32-bit words",
                      index=2;
        ip_prec	  : 3  : legal_values=(ROUTINE=0, PRIORITY=1, IMMEDIATE=2, FLASH=3, FLASH_OVERRIDE=4, CRITIC_ECP=5,
                      INTERNET_CONTROL=6, NETWORK_CONTROL=7 ),
                      display="Precedence", index=3;
        ip_tos	  : 4  : legal_values=(NORMAL_SERVICE=0, MIN_MONETARY_COST=1, MAX_RELIABILITY=2, MAX_THROUGHPUT=4,
                      MIN_DELAY=8, MAX_SECURITY=15 ),
                      display="Type of Service", index=4;
        ip_tos_mbz    : 1  : display="Unused", index=5;
        ip_total_length : 16 : send = length(node, pdu),
                        display = "Total Length %dec bytes",
                        index=6;
        ip_id         : 16 : default = 0x508, display="Identification %dec",
                      index=7;
        flgs = ip_flags << 2 | ip_df_bit << 1 | ip_mf_bit;
        ip_flags      : 1  : display="Flags, Unused", index=8;
        ip_df_bit	    : 1  : legal_values=(MAY_FRAGMENT=0, DONT_FRAGMENT=1),
                      display="Flags, DF bit", index=9;
        ip_mf_bit	    : 1  : legal_values=(LAST_FRAGMENT=0, MORE_FRAGMENTS=1),
                      display="Flags, MF bit", index=10;
        ip_frag_offset  : 13 : display="Fragment Offset %dec * 8 octets",
                        index=11;
        ip_ttl        : 8  : default = 0x1e,
                      display="Time To Live %dec seconds/hops",
                      index=12;
        ip_protocol   : 8  : default=0xff, legal_values = (IPv6_HOP_BY_HOP=0, ICMP=1, IGMP=2, GGP=3, IP=4, ST=5,
                      TCP=6, UCL=7, EGP=8, IGP=9, BBN=10, NVP=11, PUP=12, ARGUS=13, EMCON=14, XNET=15, CHAOS=16,
                      UDP=17, MUX=18, DCN=19, HMP=20, PRM=21, XNS=22, TRUNK_1=23, TRUNK_2=24, LEAF_1=25, LEAF_2=26,
                      RDP=27, IRTP=28, ISO_TP4=29, NETBLT=30, MFE=31, MERIT=32, SEP=33, THREEPC=34, IDPR=35, XTP=36,
                      DDP=37, IDPR=38, TPPLUSPLUS=39, IL=40, IPv6=41, SDRP=42, IPv6_SR=43, IPv6_FRAG=44, IDRP=45,
                      RSVP=46, GRE=47, MHRP=48, BNA=49, IPSEC_ESP=50, IPSEC_AH=51, I_NLSP=52, SWIPE=53, NHRP=54,
                      ICMPv6=58, IPv6_DEST=60, CFTP=62, SAT_EXPAK=64, KRYPTOLAN=65, RVD=66, IPPC=67, SAT_MON=69,
                      VISA=70, IPCV=71, CPNX=72, CPHB=73, WSN=74, PVP=75, BR_SAT_MON=76, SUN_ND=77, WB_MON=78,
                      WB_EXPAK=79, ISO_IP=80, VMTP=81, SECURE_VMTP=82, VINES=83, TTP=84, NSFNET_IGP=85, DGP=86,
                      TCF=87, IGRP=88, OSPF=89, SPRITE_RPC=90, LARP=91, MTP=92, AX_25=93, IPIP=94, MICP=95,
                      SCC_SP=96, ETHERIP=97, ENCAP=98, GMTP=100, PIM=103, PGM=113, ISIS=124, RESERVED=255 ),
                      display="Protocol", index=13;
        ip_xsum         : 16 : send = checksum(dod, node, node), display="Checksum",
                      index=14;
        ip_src_address  : 32 : legal_values = (1-0xffffffff),
                      display="Source Address %ipa",
                      tags=("Source Address" ), index=15;
        ip_dest_address : 32 : legal_values = (0-0xffffffff), default=0xFFFFFFFF,
                      display="Destination Address %ipa",
                      tags=("Destination Address" ), index=16;
        IP_OPTION_TUPLE[]   : (ip_ihl - 5) * 32;
        """
        pkt_fields = {}
        header_name = "IP_HDR"

        if self.is_field_set(self.get_source_ip()):
            pkt_fields["ip_src_address"] = self.get_source_ip()
        if self.is_field_set(self.get_destination_ip()):
            pkt_fields["ip_dest_address"] = self.get_destination_ip()
        if self.is_field_set(self.get_ip_ttl()):
            pkt_fields["ip_ttl"] = self.get_ip_ttl()
        if self.is_field_set(self.get_ip_checksum()):
            pkt_fields["xsum"] = self.get_ip_checksum()
        if self.is_field_set(self.get_ip_hdr_length()):
            pkt_fields["ip_ihl"] = self.get_ip_hdr_length()
        if self.is_field_set(self.get_ip_tos()):
            tos = self.get_ip_tos()
            ip_prec = (0xE0 & tos) >> 5
            ip_tos = (0x1E & tos) >> 1
            ip_tos_mbz = (0x01 & tos)
            pkt_fields["ip_prec"] = ip_prec
            pkt_fields["ip_tos"] = ip_tos
            pkt_fields["ip_tos_mbz"] = ip_tos_mbz
        if self.is_field_set(self.get_ip_length()):
            pkt_fields["ip_total_length"] = self.get_ip_length()
        if self.is_field_set(self.get_ip_id()):
            pkt_fields["ip_id"] = self.get_ip_id()
        if self.is_field_set(self.get_ip_flags()):
            flags = NumberUtils.to_integer_value(self.get_ip_flags())
            if (flags & 0x04) > 0:
                pkt_fields["ip_flags"] = 1
            if (flags & 0x02) > 0:
                pkt_fields["ip_df_bit"] = 1
            if (flags & 0x01) > 0:
                pkt_fields["ip_mf_bit"] = 1
        if self.is_field_set(self.get_ip_fragment_offset()):
            pkt_fields["ip_frag_offset"] = self.get_ip_fragment_offset()
        if self.is_field_set(self.get_ip_protocol()):
            pkt_fields["ip_protocol"] = self.get_ip_protocol()

        # ip.dst_ip_mode = Ip4.e_im_inc_host
        jets_dev.pdl_add_packet_header(header_name, pkt_fields)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        self.get_ip_hdr_length_hltapi_cmd(dummy_dict)
        self.get_ip_tos_hltapi_cmd(dummy_dict)
        # self.get_ip_length_hltapi_cmd(dummy_dict)
        self.get_ip_id_hltapi_cmd(dummy_dict)
        self.get_ip_flags_hltapi_cmd(dummy_dict)
        self.get_ip_fragment_offset_hltapi_cmd(dummy_dict)
        self.get_ip_ttl_hltapi_cmd(dummy_dict)
        self.get_ip_options_hltapi_cmd(dummy_dict)
        self.get_ip_protocol_hltapi_cmd(dummy_dict)
        self.get_ip_checksum_hltapi_cmd(dummy_dict)
        self.get_destination_ip_hltapi_cmd(dummy_dict)
        self.get_source_ip_hltapi_cmd(dummy_dict)
        dummy_dict[TrafficConfigConstants.L3_PROTOCOL_CMD] = TrafficConfigConstants.L3_PROTOCOL_IPV4
        return dummy_dict

    def calculate_ip_checksum(self, header_offset):
        self.set_ip_checksum(0)
        header_sum = Checksum.calculate_ip_checksum(self.get_bytes(), header_offset, self.HEADER_SIZE_IPV4)
        header_sum = Checksum.calculate_complement(header_sum)
        self.set_ip_checksum(header_sum)
        pass

    def configure_ip_length(self, length):
        hdr_length = 20
        if self.is_field_set(self.get_ip_options()):
            hdr_length += len(self.get_ip_options())
        self.set_ip_hdr_length(hdr_length // 4)
        length = NumberUtils.to_integer_value(length)
        self.set_ip_length(length - 18)

    # def get_pseudo_ip_header(self, header_offset):
    #     sip = self.format_byte_string(self.get_source_ip(), PacketConstants.IPV4_ADDRESS, 32)
    #     dip = self.format_byte_string(self.get_destination_ip(), PacketConstants.IPV4_ADDRESS, 32)
    #     protocol = self.format_byte_string(self.get_ip_protocol(), PacketConstants.INTEGER, 8)
    #     length = (len(self.get_bytes())/2 - header_offset)
    #     length = self.format_byte_string(length, PacketConstants.INTEGER, 16)
    #     return sip + dip + "00" + protocol + length

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        # set the values in ipv4, remove them from the payload and set the payload back
        # 45 00 00 2E 00 00 00 00 40 FF 71 CA 03 03 03 03 01 01 01 01 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D DE AD
        # BE EF 00 02 00 00 85 5F BB A4 00 8A 53 5C
        # version = 4bits
        self.ipv4_version = self.get_bits_from_string(4, payload)
        payload = self.remove_bits_from_string(4, payload)
        # hdlen = 4bits
        ipv4_hdlen = self.get_bits_from_string(4, payload)
        self.set_ip_hdr_length("0x" + ipv4_hdlen)
        payload = self.remove_bits_from_string(4, payload)
        # TOS = 8 bits
        ipv4_tos = self.get_bits_from_string(8, payload)
        self.set_ip_tos("0x" + ipv4_tos)
        payload = self.remove_bits_from_string(8, payload)
        # Length = 16 bits
        ipv4_length = self.get_bits_from_string(16, payload)
        self.set_ip_length("0x" + ipv4_length)
        payload = self.remove_bits_from_string(16, payload)
        # ID = 16 bits
        ipv4_id = self.get_bits_from_string(16, payload)
        self.set_ip_id("0x" + ipv4_id)
        payload = self.remove_bits_from_string(16, payload)
        # flags + frag offset = 16 bits
        ipv4_flags = int(self.get_bits_from_string(16, payload), 16)
        self.set_ip_flags((ipv4_flags & 0x0FE00) >> 13)
        self.set_ip_fragment_offset((ipv4_flags & 0x01FF))
        payload = self.remove_bits_from_string(16, payload)
        # TTL = 8 bits
        ipv4_ttl = self.get_bits_from_string(8, payload)
        self.set_ip_ttl("0x" + ipv4_ttl)
        payload = self.remove_bits_from_string(8, payload)
        # Protocol = 8 bits
        protocol = self.get_bits_from_string(8, payload)
        self.set_ip_protocol("0x" + protocol)
        payload = self.remove_bits_from_string(8, payload)
        # checksum = 16 bits
        ipv4_checksum = self.get_bits_from_string(16, payload)
        self.set_ip_checksum("0x" + ipv4_checksum)
        payload = self.remove_bits_from_string(16, payload)
        # SIP = 32 bits
        sip = self.get_bits_from_string(32, payload)
        self.set_source_ip("0x" + sip)
        payload = self.remove_bits_from_string(32, payload)
        # DIP = 32 bits
        dip = self.get_bits_from_string(32, payload)
        self.set_destination_ip("0x" + dip)
        payload = self.remove_bits_from_string(32, payload)
        # Options = Length - 20
        header_length = int(ipv4_hdlen) * 4
        if header_length > 20:
            ipv4_option = self.get_bits_from_string((header_length - 20) * 8, payload)
            payload = self.remove_bits_from_string((header_length - 20) * 8, payload)
            self.set_ip_options(ipv4_option)
        self.payload = payload

    def get_header_bytes(self):
        # version = 4bits
        # hdlen = 4bits
        # TOS = 8 bits/1 byte
        # Length = 16 bits
        # ID = 16 bits
        # flags + frag offset = 16 bits
        # TTL = 8 bits
        # Protocol = 8 bits
        # checksum = 16 bits
        # SIP = 32 bits
        # DIP = 32 bits
        # Options = Length - 20
        version = self.format_byte_string("4", PacketConstants.INTEGER, 4)
        hdlen = self.format_byte_string(self.get_ip_hdr_length(), PacketConstants.INTEGER, 4)
        tos = self.format_byte_string(self.get_ip_tos(), PacketConstants.INTEGER, 8)
        length = self.format_byte_string(self.get_ip_length(), PacketConstants.INTEGER, 16)
        pkt_id = self.format_byte_string(self.get_ip_id(), PacketConstants.INTEGER, 16)

        flags = self.format_byte_string(self.get_ip_flags(), PacketConstants.INTEGER, 16)
        fragments = self.format_byte_string(self.get_ip_fragment_offset(), PacketConstants.INTEGER, 16)
        all_flags = int(flags, 16) << 13 | int(fragments, 16)
        all_flags = self.format_byte_string(all_flags, PacketConstants.INTEGER, 16)

        ttl = self.format_byte_string(self.get_ip_ttl(), PacketConstants.INTEGER, 8)
        protocol = self.format_byte_string(self.get_ip_protocol(), PacketConstants.INTEGER, 8)
        checksum = self.format_byte_string(self.get_ip_checksum(), PacketConstants.INTEGER, 16)
        sip = self.format_byte_string(self.get_source_ip(), PacketConstants.IPV4_ADDRESS, 32)
        dip = self.format_byte_string(self.get_destination_ip(), PacketConstants.IPV4_ADDRESS, 32)
        # options = self.format_byte_string (self.get_destination_ip(), PacketConstants.IPV4_ADDRESS, 8)
        # Options = Length - 20
        return version + " " + hdlen + " " + tos + " " + length + " " + pkt_id + " " + \
            all_flags + " " + ttl + " " + protocol + " " + checksum + " " + sip + " " + dip

    @staticmethod
    def compare_ipv4_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                   print_failures=True):
        results = True
        try:
            assert isinstance(expected, IpV4PacketHeader)
            assert isinstance(actual, IpV4PacketHeader)
            # if (expected.is_field_set(expected.get_ip_version()) and
            #         IpV4PacketConstants.IPV4_VERSION not in ignore_list):
            #     name = "IPV4 version : "
            #     if expected.get_ip_version() != actual.get_ip_version():
            #         results = False
            #         if print_results or print_failures:
            #             print name + str(expected.get_ip_version()) + " != " + str(actual.get_ip_version()) + " ERROR"
            #     elif print_results:
            #         print name + str(expected.get_ip_version()) + " == " + str(actual.get_ip_version()) + " Pass"

            if expected.do_i_check_this_field(expected.get_ip_hdr_length(), IpV4PacketConstants.IPV4_IP_HDR_LENGTH,
                                              ignore_list, include_list):
                name = "IPV4 hdlen : "
                if expected.get_ip_hdr_length() != actual.get_ip_hdr_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ip_hdr_length()) + " != " +
                                                      str(actual.get_ip_hdr_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ip_hdr_length()) + " == " +
                                                 str(actual.get_ip_hdr_length()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ip_tos(), IpV4PacketConstants.IPV4_IP_TOS,
                                              ignore_list, include_list):
                name = "IPV4 tos : "
                if expected.get_ip_tos() != actual.get_ip_tos():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ip_tos()) + " != " +
                                                      str(actual.get_ip_tos()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ip_tos()) + " == " +
                                                 str(actual.get_ip_tos()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ip_length(), IpV4PacketConstants.IPV4_IP_LENGTH,
                                              ignore_list, include_list):
                name = "IPV4 length : "
                if expected.get_ip_length() != actual.get_ip_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ip_length()) + " != " +
                                                      str(actual.get_ip_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ip_length()) + " == " +
                                                 str(actual.get_ip_length()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ip_id(), IpV4PacketConstants.IPV4_ID,
                                              ignore_list, include_list):
                name = "IPV4 id : "
                if expected.get_ip_id() != actual.get_ip_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ip_id()) + " != " +
                                                      str(actual.get_ip_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ip_id()) + " == " +
                                                 str(actual.get_ip_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ip_flags(), IpV4PacketConstants.IPV4_FLAGS,
                                              ignore_list, include_list):
                name = "IPV4 flags : "
                if expected.get_ip_flags() != actual.get_ip_flags():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ip_flags()) + " != " +
                                                      str(actual.get_ip_flags()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ip_flags()) + " == " +
                                                 str(actual.get_ip_flags()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ip_ttl(), IpV4PacketConstants.IPV4_TTL,
                                              ignore_list, include_list):
                name = "IPV4 ttl : "
                if expected.get_ip_ttl() != actual.get_ip_ttl():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ip_ttl()) + " != " +
                                                      str(actual.get_ip_ttl()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ip_ttl()) + " == " +
                                                 str(actual.get_ip_ttl()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ip_protocol(), IpV4PacketConstants.IPV4_PROTOCOL,
                                              ignore_list, include_list):
                name = "IPV4 protocol : "
                if expected.get_ip_protocol() != actual.get_ip_protocol():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ip_protocol()) + " != " +
                                                      str(actual.get_ip_protocol()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ip_protocol()) + " == " +
                                                 str(actual.get_ip_protocol()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ip_checksum(), IpV4PacketConstants.IPV4_CHECKSUM,
                                              ignore_list, include_list):
                name = "IPV4 checksum : "
                if expected.get_ip_checksum() != actual.get_ip_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ip_checksum()) + " != " +
                                                      str(actual.get_ip_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ip_checksum()) + " == " +
                                                 str(actual.get_ip_checksum()) + " Pass")

            if expected.do_i_check_this_field(expected.get_source_ip(), IpV4PacketConstants.IPV4_SIP,
                                              ignore_list, include_list):
                name = "IPV4 source_ip : "
                if expected.get_source_ip() != actual.get_source_ip():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_source_ip()) + " != " +
                                                      str(actual.get_source_ip()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_source_ip()) + " == " +
                                                 str(actual.get_source_ip()) + " Pass")

            if expected.do_i_check_this_field(expected.get_destination_ip(), IpV4PacketConstants.IPV4_DIP,
                                              ignore_list, include_list):
                name = "IPV4 destination_ip : "
                if expected.get_destination_ip() != actual.get_destination_ip():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_destination_ip()) + " != " +
                                                      str(actual.get_destination_ip()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_destination_ip()) + " == " +
                                                 str(actual.get_destination_ip()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(repr(e))
                PacketObject.logger.log_error("Error with IpV4PacketHeader")
        return results


class IpV4PacketConstants:
    def __init__(self):
        pass

    IPV4_VERSION = "IPV4_VERSION"
    IPV4_IP_HDR_LENGTH = "IPV4_IP_HDR_LENGTH"
    IPV4_IP_TOS = "IPV4_IP_TOS"
    IPV4_IP_CU = "IPV4_IP_CU"
    IPV4_IP_DSCP = "IPV4_IP_DSCP"
    IPV4_IP_LENGTH = "IPV4_IP_LENGTH"
    IPV4_ID = "IPV4_ID"
    IPV4_FLAGS = "IPV4_FLAGS"
    IPV4_FRAGMENT_OFFSET = "IPV4_FRAGMENT_OFFSET"
    IPV4_TTL = "IPV4_TTL"
    IPV4_PROTOCOL = "IPV4_PROTOCOL"
    IPV4_CHECKSUM = "IPV4_CHECKSUM"
    IPV4_DIP = "IPV4_DIP"
    IPV4_DIP_MODE = "IPV4_DIP_MODE"
    IPV4_DIP_COUNT = "IPV4_DIP_COUNT"
    IPV4_DIP_MASK = "IPV4_DIP_MASK"
    IPV4_SIP = "IPV4_SIP"
    IPV4_SIP_MODE = "IPV4_SIP_MODE"
    IPV4_SIP_COUNT = "IPV4_SIP_COUNT"
    IPV4_SIP_MASK = "IPV4_SIP_MASK"
    IPV4_OPTIONS = "IPV4_OPTIONS"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
