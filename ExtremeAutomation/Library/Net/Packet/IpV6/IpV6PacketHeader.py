from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.ip6_pb2 import ip6, Ip6
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import SnapPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer3PacketHeader import Layer3PacketHeader
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class IpV6PacketHeader(Layer3PacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    IPv6 Packet Header
        # version = 4bits
        # traffic class = 8bits
        # flow label = 20bits
        # payload length = 16bits
        # next header = 8bits
        # hop limit = 8bits
        # source address = 128bits
        # destination address = 128bits
    """

    def __init__(self):
        super(IpV6PacketHeader, self).__init__()
        self.add_ipv6_header()
        self.HEADER_SIZE_IPV6 = (4 + 8 + 20 + 16 + 8 + 8 + 128 + 128) // 8

    # start IpV6 version methods
    #  version is a 4 bit INTEGER example: 1
    def set_ipv6_version(self, version, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV6PacketConstants.IPV6_VERSION, ignore_check)
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_VERSION, version)

    def get_ipv6_version(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_VERSION),
            PacketConstants.INTEGER)

    def get_ipv6_version_hltapi_cmd(self, dummy_dict):
        version = self.get_ipv6_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end IpV6 version methods

    # start IpV6 traffic class methods
    #  traffic_class is a 8 bit INTEGER example: 1
    def set_ipv6_traffic_class(self, traffic_class, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV6PacketConstants.IPV6_TRAFFIC_CLASS, ignore_check)
        traffic_class = self.normalize_value(traffic_class, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_TRAFFIC_CLASS,
                                  traffic_class)

    def get_ipv6_traffic_class(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_TRAFFIC_CLASS),
            PacketConstants.INTEGER)

    def get_ipv6_traffic_class_hltapi_cmd(self, dummy_dict):
        traffic_class = self.get_ipv6_traffic_class()
        if isinstance(traffic_class, int):
            traffic_class = str(traffic_class)
        if traffic_class and 'Not Set' not in traffic_class:
            dummy_dict[TrafficConfigConstants.IPV6_TRAFFIC_CLASS_CMD] = traffic_class
    # end IpV6 traffic class methods

    # start IpV6 flow label methods
    #  flow_label is a 20 bit INTEGER example: 1
    def set_ipv6_flow_label(self, flow_label, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV6PacketConstants.IPV6_FLOW_LABEL, ignore_check)
        flow_label = self.normalize_value(flow_label, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_FLOW_LABEL,
                                  flow_label)

    def get_ipv6_flow_label(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_FLOW_LABEL),
            PacketConstants.INTEGER)

    def get_ipv6_flow_label_hltapi_cmd(self, dummy_dict):
        flow_label = self.get_ipv6_flow_label()
        if isinstance(flow_label, int):
            flow_label = str(flow_label)
        if flow_label and 'Not Set' not in flow_label:
            dummy_dict[TrafficConfigConstants.TEMP_FLOW_LABEL_CMD] = flow_label
    # end IpV6 flow label methods

    # start IpV6 payload length methods
    #  payload_length is a 16 bit INTEGER example: 1
    def set_ipv6_payload_length(self, payload_length, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV6PacketConstants.IPV6_PAYLOAD_LENGTH, ignore_check)
        payload_length = self.normalize_value(payload_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_PAYLOAD_LENGTH,
                                  payload_length)

    def get_ipv6_payload_length(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_PAYLOAD_LENGTH),
            PacketConstants.INTEGER)

    def get_ipv6_payload_length_hltapi_cmd(self, dummy_dict):
        payload_length = self.get_ipv6_payload_length()
        if isinstance(payload_length, int):
            payload_length = str(payload_length)
        if payload_length and 'Not Set' not in payload_length:
            dummy_dict[TrafficConfigConstants.TEMP_PAYLOAD_LENGTH_CMD] = payload_length
    # end IpV6 payload length methods

    # start IpV6 next header methods
    #  next_header is a 8 bit INTEGER example: 1
    def set_ipv6_next_header(self, next_header, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV6PacketConstants.IPV6_LAST_NEXT_HEADER, ignore_check)
        next_header = self.normalize_value(next_header, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_NEXT_HEADER,
                                  next_header)

    def get_ipv6_next_header(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_NEXT_HEADER), PacketConstants.INTEGER)

    def get_ipv6_next_header_hltapi_cmd(self, dummy_dict):
        next_header = self.get_ipv6_next_header()
        if isinstance(next_header, int):
            next_header = str(next_header)
            # if next_header and 'Not Set' not in next_header:
            #     dummy_dict[TrafficConfigConstants.IPV6_NEXT_HEADER_CMD] = next_header

    def set_ipv6_last_next_header(self, next_header):
        next_header = self.normalize_value(next_header, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_LAST_NEXT_HEADER,
                                  next_header)

    def get_ipv6_last_next_header(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_LAST_NEXT_HEADER),
            PacketConstants.INTEGER)
    # end IpV6 next header methods

    # start IpV6 hop limit methods
    #  hop_limit is a 8 bit INTEGER example: 1
    def set_ipv6_hop_limit(self, hop_limit, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV6PacketConstants.IPV6_HOP_LIMIT, ignore_check)
        hop_limit = self.normalize_value(hop_limit, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_HOP_LIMIT, hop_limit)

    def get_ipv6_hop_limit(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_HOP_LIMIT), PacketConstants.INTEGER)

    def get_ipv6_hop_limit_hltapi_cmd(self, dummy_dict):
        hop_limit = self.get_ipv6_hop_limit()
        if isinstance(hop_limit, int):
            hop_limit = str(hop_limit)
        if hop_limit and 'Not Set' not in hop_limit:
            dummy_dict[TrafficConfigConstants.IPV6_HOP_LIMIT_CMD] = hop_limit
    # end IpV6 hop limit methods

    # start IpV6 source address methods
    #  source_address is a 128 bit IPV6_ADDRESS example: FF01::0001
    def set_ipv6_source_address(self, source_address, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV6PacketConstants.IPV6_SOURCE_ADDRESS, ignore_check)
        source_address = self.normalize_value(source_address, PacketConstants.IPV6_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_SOURCE_ADDRESS,
                                  source_address)

    def get_ipv6_source_address(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_SOURCE_ADDRESS),
            PacketConstants.IPV6_ADDRESS)

    def get_ipv6_source_address_hltapi_cmd(self, dummy_dict):
        source_address = self.get_ipv6_source_address()
        if source_address and 'Not Set' not in source_address:
            dummy_dict[TrafficConfigConstants.IPV6_SRC_ADDR_CMD] = source_address

    def set_ipv6_source_address_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  IpV6PacketConstants.IPV6_SOURCE_ADDRESS_MODE, ip)

    def get_ipv6_source_address_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         IpV6PacketConstants.IPV6_SOURCE_ADDRESS_MODE)

    def set_ipv6_source_address_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  IpV6PacketConstants.IPV6_SOURCE_ADDRESS_COUNT, ip)

    def get_ipv6_source_address_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         IpV6PacketConstants.IPV6_SOURCE_ADDRESS_COUNT)

    def set_ipv6_source_address_mask(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  IpV6PacketConstants.IPV6_SOURCE_ADDRESS_MASK, ip)

    def get_ipv6_source_address_mask(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         IpV6PacketConstants.IPV6_SOURCE_ADDRESS_MASK)
    # end IpV6 source address methods

    # start IpV6 destination address methods
    #  destination_address is a 128 bit IPV6_ADDRESS example: FF01::0001
    def set_ipv6_destination_address(self, destination_address, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV6PacketConstants.IPV6_DESTINATION_ADDRESS, ignore_check)
        destination_address = self.normalize_value(destination_address, PacketConstants.IPV6_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_DESTINATION_ADDRESS,
                                  destination_address)

    def get_ipv6_destination_address(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                                              IpV6PacketConstants.IPV6_DESTINATION_ADDRESS),
                                    PacketConstants.IPV6_ADDRESS)

    def get_ipv6_destination_address_hltapi_cmd(self, dummy_dict):
        destination_address = self.get_ipv6_destination_address()
        if destination_address and 'Not Set' not in destination_address:
            dummy_dict[TrafficConfigConstants.IPV6_DST_ADDR_CMD] = destination_address

    def set_ipv6_destination_address_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  IpV6PacketConstants.IPV6_DESTINATION_ADDRESS_MODE, ip)

    def get_ipv6_destination_address_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         IpV6PacketConstants.IPV6_DESTINATION_ADDRESS_MODE)

    def set_ipv6_destination_address_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  IpV6PacketConstants.IPV6_DESTINATION_ADDRESS_COUNT, ip)

    def get_ipv6_destination_address_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         IpV6PacketConstants.IPV6_DESTINATION_ADDRESS_COUNT)

    def set_ipv6_destination_address_mask(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  IpV6PacketConstants.IPV6_DESTINATION_ADDRESS_MASK, ip)

    def get_ipv6_destination_address_mask(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         IpV6PacketConstants.IPV6_DESTINATION_ADDRESS_MASK)
        # end IpV6 destination address methods

    def set_ipv6_extension_headers(self, headers, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpV6PacketConstants.IPV6_EXTENSION_HEADERS, ignore_check)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6, IpV6PacketConstants.IPV6_EXTENSION_HEADERS,
                                  headers)

    def get_ipv6_extension_headers(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         IpV6PacketConstants.IPV6_EXTENSION_HEADERS)

    def get_ipv6_extension_headers_length(self):
        extension_length = 0
        if self.is_field_set(self.get_ipv6_extension_headers()):

            for row in self.get_ipv6_extension_headers():
                next_header = row.next_header
                if next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_AUTHENTICATION:
                    extension_length += 128 // 8
                else:
                    extension_length += 64 // 8
        return extension_length

    def check_ipv6_extension_headers(self):
        headers = self.get_ipv6_extension_headers()
        if not isinstance(headers, list):
            headers = []
            self.set_ipv6_extension_headers(headers)

    def add_ipv6_extension_headers_fragment(self):
        self.check_ipv6_extension_headers()
        headers = self.get_ipv6_extension_headers()
        header = Ipv6ExtentionHeaders()
        header.next_header = IpV6PacketConstants.IPV6_NEXT_HEADER_FRAGMENT
        if len(headers) == 0:
            nh = self.get_ipv6_next_header()
            header.next_next_header = nh
            self.set_ipv6_next_header(IpV6PacketConstants.IPV6_NEXT_HEADER_FRAGMENT)
        headers.append(header)

        #######################################
        # ### End of the Accessor Methods
        #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("version", self.format_int(self.get_ipv6_version(), 1))
        table.add_row_value("traffic class", self.format_int(self.get_ipv6_traffic_class(), 2))
        table.add_row_value("flow label", self.format_int(self.get_ipv6_flow_label(), 5))
        table.add_row_value("payload length", self.format_int(self.get_ipv6_payload_length(), 4))
        table.add_row_value("next header", self.format_int(self.get_ipv6_next_header(), 2))
        table.add_row_value("hop limit", self.format_int(self.get_ipv6_hop_limit(), 2))
        table.add_row_value("source address", self.get_ipv6_source_address())
        table.add_row_value("destination address", self.get_ipv6_destination_address())

        ext_hd = ""
        if self.get_ipv6_extension_headers() and isinstance(self.get_ipv6_extension_headers(), list):
            ext_hd = "\nIpV6 Extension Headers:"
            for row in self.get_ipv6_extension_headers():
                ext_hd += "\n\t" + str(row)
        return "\n\nIPV6 HEADER" + table.to_table_string() + ext_hd

    def get_ixtclhal_ipv6_api_commands(self, port_string, streamid):
        # if not self.get_ip_options():
        #     return
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = list()
        # index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        dummy_dict.append("ipV6 get " + port_string)
        # if self.is_field_set(self.get_ipv6_next_header()):
        #     dummy_dict.append("ipV6 config -nextHeader " + str(self.get_ipv6_next_header()))
        # dummy_dict.append("ipV6 set " + port_string)
        # dummy_dict.append("stream set " + port_string + " " + str(streamid))
        # dummy_dict.append("stream write " + port_string + " " + str(streamid))
        # dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        # dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")

        if self.get_ipv6_extension_headers() and isinstance(self.get_ipv6_extension_headers(), list):
            for row in self.get_ipv6_extension_headers():
                next_header = row.next_header
                dummy_dict.append("ipV6 clearAllExtensionHeaders")
                if next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_HOP_BY_HOP:
                    next_string = "HOP_BY_HOP"
                    dummy_dict.append("")
                    dummy_dict.append("ipV6HopByHop clearAllOptions")
                    dummy_dict.append("ipV6OptionPADN setDefault")
                    dummy_dict.append("ipV6OptionPADN config -length                             4")
                    dummy_dict.append("ipV6OptionPADN config -value                              \"00 00 00 00\"")
                    dummy_dict.append("ipV6HopByHop addOption ipV6OptionPADN")
                    dummy_dict.append("ipV6 addExtensionHeader ipV6HopByHopOptions")
                elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_DESTINATION:
                    next_string = "IPV6_NEXT_HEADER_DESTINATION"
                    dummy_dict.append("ipV6Destination clearAllOptions")
                    dummy_dict.append("ipV6OptionPADN setDefault")
                    dummy_dict.append("ipV6OptionPADN config -length                             4")
                    dummy_dict.append("ipV6OptionPADN config -value                              \"00 00 00 00\"")
                    dummy_dict.append("ipV6Destination addOption ipV6OptionPADN")
                    dummy_dict.append("ipV6 addExtensionHeader ipV6DestinationOptions")
                elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_ROUTING:
                    next_string = "ROUTING"
                    dummy_dict.append("ipV6Routing setDefault")
                    dummy_dict.append("ipV6Routing config -reserved                           \"00 00 00 00\"")
                    dummy_dict.append("ipV6Routing config -nodeList                           \"\"")

                    dummy_dict.append("ipV6 addExtensionHeader ipV6Routing")
                elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_FRAGMENT:
                    next_string = "FRAGMENT"
                    dummy_dict.append("ipV6Fragment setDefault")
                    dummy_dict.append("ipV6Fragment config -enableFlag                         true")
                    dummy_dict.append("ipV6Fragment config -fragmentOffset                     100")
                    dummy_dict.append("ipV6Fragment config -identification                     286335522")
                    dummy_dict.append("ipV6Fragment config -res                                3")
                    dummy_dict.append("ipV6Fragment config -reserved                           30")

                    dummy_dict.append("ipV6 addExtensionHeader ipV6Fragment")
                elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_AUTHENTICATION:
                    next_string = "AUTHENTICATION"
                    dummy_dict.append("ipV6Authentication setDefault")
                    dummy_dict.append("ipV6Authentication config -payloadLength                      2")
                    dummy_dict.append("ipV6Authentication config -securityParamIndex                 0")
                    dummy_dict.append("ipV6Authentication config -sequenceNumberField                0")
                    dummy_dict.append("ipV6Authentication config -authentication                     \"00 00 00 00\"")

                    dummy_dict.append("ipV6 addExtensionHeader ipV6Authentication")
                elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_ENCAPSULATION:
                    next_string = "ENCAPSULATION"
                    # idk yet
            if "Tcp" in self.get_name():  # can't include TcpPacketHeader
                dummy_dict.append("ipV6 addExtensionHeader ipV4ProtocolTcp")
            elif "Udp" in self.get_name():  # can't include UdpPacketHeader
                dummy_dict.append("ipV6 addExtensionHeader ipV4ProtocolUdp")

        if self.is_field_set(self.get_ipv6_next_header()):
            # dummy_dict.append("ipV6 config -nextHeader " + str(self.get_ipv6_next_header()))
            # dummy_dict.append("ipV6 set " + port_string)
            nh = self.get_ipv6_next_header()
            # https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
            if not self.does_next_header_and_class_match(nh) and \
                    nh not in [59, IpV6PacketConstants.IPV6_NEXT_HEADER_HOP_BY_HOP,
                               IpV6PacketConstants.IPV6_NEXT_HEADER_DESTINATION,
                               IpV6PacketConstants.IPV6_NEXT_HEADER_ROUTING,
                               IpV6PacketConstants.IPV6_NEXT_HEADER_FRAGMENT,
                               IpV6PacketConstants.IPV6_NEXT_HEADER_AUTHENTICATION,
                               IpV6PacketConstants.IPV6_NEXT_HEADER_ENCAPSULATION,
                               IpV6PacketConstants.IPV6_NEXT_HEADER_NO_NEXT_HEADER]:
                dummy_dict.append("udf setDefault")
                dummy_dict.append("udf config -enable                             true")
                dummy_dict.append("udf config -continuousCount                    false")
                offset = 20
                if "tagged" in self.get_name().lower():
                    offset = 24
                elif "vlanstack" in self.get_name().lower():
                    offset = 20 + 4 * self.get_vlan_num()
                else:
                    offset = 20
                dummy_dict.append("udf config -offset                             " + str(offset))
                dummy_dict.append("udf config -counterMode                        udfCounterMode")
                dummy_dict.append("udf config -chainFrom                          udfNone")
                dummy_dict.append("udf config -bitOffset                          0")
                dummy_dict.append("udf config -udfSize                            8")
                dummy_dict.append("udf config -updown                             uuuu")
                dummy_dict.append("udf config -initval                            " +
                                  NumberUtils.to_hex_value(str(self.get_ipv6_next_header()), True))
                dummy_dict.append("udf config -repeat                             1")
                dummy_dict.append("udf config -cascadeType                        udfCascadeNone")
                dummy_dict.append("udf config -enableCascade                      false")
                dummy_dict.append("udf config -step                               0")
                dummy_dict.append("udf set 1")
        dummy_dict.append("ipV6 set " + port_string)
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def does_next_header_and_class_match(self, nh):
        if "Tcp" in self.get_name():
            return nh == 0x06
        elif "Udp" in self.get_name():
            return nh == 0x11
        elif "Icmp" in self.get_name():
            return nh == 0x01 or nh == 58
        elif "Ospf" in self.get_name():
            return nh == 89
        else:
            return False
        # 0x11, 58, 0x06, 0x01,

    def get_spirent_ipv6_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def add_ipv6_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_IPV6)

    def build(self):
        self.add_ipv6_header()
        if isinstance(self, Ethernet2PacketHeader):
            self.set_ether_type("0x86DD", True)
        if isinstance(self, SnapPacketHeader):
            self.set_snap_ether_type("0x86DD", True)
        self.set_ipv6_version("6", True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_ipv6_version_hltapi_cmd(dummy_dict)
        self.get_ipv6_traffic_class_hltapi_cmd(dummy_dict)
        # self.get_ipv6_flow_label_hltapi_cmd(dummy_dict)
        # self.get_ipv6_payload_length_hltapi_cmd(dummy_dict)
        self.get_ipv6_next_header_hltapi_cmd(dummy_dict)
        self.get_ipv6_hop_limit_hltapi_cmd(dummy_dict)
        self.get_ipv6_source_address_hltapi_cmd(dummy_dict)
        self.get_ipv6_destination_address_hltapi_cmd(dummy_dict)
        dummy_dict[TrafficConfigConstants.L3_PROTOCOL_CMD] = TrafficConfigConstants.L3_PROTOCOL_IPV6  # constant value
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_ipv6(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_ipv6(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_ipv6(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_ipv6(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kIp6FieldNumber
        ipv6Field = p.Extensions[ip6]
        assert isinstance(ipv6Field, Ip6)
        # version = {int} 6
        if self.is_field_set(self.get_ipv6_version()) and self.get_ipv6_version() != 6:

            ipv6Field.version = int(self.get_ipv6_version())
            ipv6Field.is_override_version = True
        else:
            ipv6Field.is_override_version = False
        # traffic_class = {int} 0
        # is_override_version = {bool} False
        if self.is_field_set(self.get_ipv6_traffic_class()):
            ipv6Field.traffic_class = int(self.get_ipv6_traffic_class())
        # flow_label = {int} 0
        if self.is_field_set(self.get_ipv6_flow_label()):
            ipv6Field.flow_label = int(self.get_ipv6_flow_label())
        # hop_limit = {int} 127
        if self.is_field_set(self.get_ipv6_hop_limit()):
            ipv6Field.hop_limit = int(self.get_ipv6_hop_limit())
        # next_header = {int} 0
        # is_override_next_header = {bool} False
        if self.is_field_set(self.get_ipv6_next_header()):
            ipv6Field.next_header = int(self.get_ipv6_next_header())
            ipv6Field.is_override_next_header = True
        else:
            ipv6Field.is_override_next_header = False
        # payload_length = {int} 0
        # is_override_payload_length = {bool} False
        if self.is_field_set(self.get_ipv6_payload_length()):
            ipv6Field.payload_length = int(self.get_ipv6_payload_length())
            ipv6Field.is_override_payload_length = True
        else:
            ipv6Field.is_override_payload_length = False
        # src_addr_hi = {int} 0
        # src_addr_lo = {int} 0
        if self.is_field_set(self.get_ipv6_source_address()):
            addy = self.get_ipv6_source_address().replace(":", "")
            ipv6Field.src_addr_hi = int("0x" + addy[:16], 16)
            ipv6Field.src_addr_lo = int("0x" + addy[16:], 16)
        # dst_addr_hi = {int} 0
        # dst_addr_lo = {int} 0
        if self.is_field_set(self.get_ipv6_destination_address()):
            addy = self.get_ipv6_destination_address().replace(":", "")
            ipv6Field.dst_addr_hi = int("0x" + addy[:16], 16)
            ipv6Field.dst_addr_lo = int("0x" + addy[16:], 16)

    def config_jets_stream_ipv6(self, jets_dev, port_string, stream_id, **kwargs):
        """
        version     : 4   : default=6, legal_values=(RESERVED=0, UNASSIGNED=1-3, IPv4=4, STREAM_PROTOCOL_V2=5, IPv6=6,
                      TP_IX_NEXT_INTERNET=7, PIP=8, TUBA=9, UNASSIGNED=10-14, RESERVED=15 ),
                      display="IP Version %dec", index=1;
        priority    : 8   : default=6, legal_values=(UNCHARACTERIZED_0=0, FILLER_TRFC_1=1, UNATTENDED_BULK_2=2,
                      RESERVED_3=3, ATTENDED_BULK_4=4, RESERVED_5=5, INTERACTIVE_6=6, INTERNET_CONTROL_7=7,
                      AUDIO_VIDEO_8=8, AUDIO_VIDEO_9=9, AUDIO_VIDEO_10=10, AUDIO_VIDEO_11=11, AUDIO_VIDEO_12=12,
                      AUDIO_VIDEO_13=13, AUDIO_VIDEO_14=14, AUDIO_VIDEO_15=15 ),
                      display="Traffic Priority %dec", index=2;
        flow_label  : 20  : legal_values=(NO_FLOW=0),
                      display="Flow Label", index=3;

        payld_len   : 16  : legal_values=(JUMBO_PAYLOAD=0),
                      display="Payload Length %dec bytes",
                      send=length(node,pdu) - 40, index=4;
        next_header : 8   : legal_values=(IPv6_HOP=0, ICMP=1, IGMP=2, GGP=3, IP=4, ST=5, TCP=6, UCL=7, EGP=8, IGP=9,
                      BBN=10, NVP=11, PUP=12, ARGUS=13, EMCON=14, XNET=15, CHAOS=16, UDP=17, MUX=18, DCN=19, HMP=20,
                      PRM=21, XNS=22, TRUNK_1=23, TRUNK_2=24, LEAF_1=25, LEAF_2=26, RDP=27, IRTP=28, ISO_TP4=29,
                      NETBLT=30, MFE=31, MERIT=32, SEP=33, THREEPC=34, IDPR=35, XTP=36, DDP=37, IDPR=38, TPPLUSPLUS=39,
                      IL=40, IPv6=41, SDRP=42, IPv6_ROUTING=43, IPv6_FRAG=44, IDRP=45, RSVP=46, GRE=47, MHRP=48, BNA=49,
                      IPv6_ESP=50, IPv6_AH=51, I_NLSP=52, SWIPE=53, NHRP=54, ICMPv6=58, IPv6_NO_NEXT=59, IPv6_DEST=60,
                      CFTP=62, SAT_EXPAK=64, KRYPTOLAN=65, RVD=66, IPPC=67, SAT_MON=69, VISA=70, IPCV=71, CPNX=72,
                      CPHB=73, WSN=74, PVP=75, BR_SAT_MON=76, SUN_ND=77, WB_MON=78, WB_EXPAK=79, ISO_IP=80, VMTP=81,
                      SECURE_VMTP=82, VINES=83, TTP=84, NSFNET_IGP=85, DGP=86, TCF=87, IGRP=88, OSPF=89, SPRITE_RPC=90,
                      LARP=91, MTP=92, AX_25=93, IPIP=94, MICP=95, SCC_SP=96, ETHERIP=97, ENCAP=98, GMTP=100, VRRP=112,
                      RESERVED=255 ), default=0xff,
                      display="Next Header Proto: %dec", index=5;
        hop_limit   : 8   : legal_values=(INVALID=0),
                    default=30,
                    display="Hop Limit %dec hops", index=6;
        src_address : 128 : display="Source Address %ip6",
                    tags=("Source Address" ), index=7;
        dst_address : 128 : default=0x00000000000000000000000000000001,
                    display="Destination Address %ip6",
                    tags=("Destination Address" ), index=8;
        """
        pkt_fields = {}
        header_name = "IPv6_HDR"

        if self.is_field_set(self.get_ipv6_version()) and self.get_ipv6_version() != 6:
            pkt_fields["version"] = self.get_ipv6_version()
        if self.is_field_set(self.get_ipv6_traffic_class()):
            pkt_fields["priority"] = self.get_ipv6_traffic_class()
        if self.is_field_set(self.get_ipv6_flow_label()):
            pkt_fields["flow_label"] = self.get_ipv6_flow_label()
        if self.is_field_set(self.get_ipv6_hop_limit()):
            pkt_fields["hop_limit"] = self.get_ipv6_hop_limit()
        if self.is_field_set(self.get_ipv6_next_header()):
            pkt_fields["next_header"] = self.get_ipv6_next_header()
        if self.is_field_set(self.get_ipv6_payload_length()):
            pkt_fields["payld_len"] = self.get_ipv6_payload_length()
        if self.is_field_set(self.get_ipv6_source_address()):
            pkt_fields["src_address"] = self.get_ipv6_source_address()
        if self.is_field_set(self.get_ipv6_destination_address()):
            pkt_fields["dst_address"] = self.get_ipv6_destination_address()

        jets_dev.pdl_add_packet_header(header_name, pkt_fields)
        ext_hd = ""
        if self.get_ipv6_extension_headers() and isinstance(self.get_ipv6_extension_headers(), list):
            list_of_headers = self.get_ipv6_extension_headers()
            for row in list_of_headers:
                if str(row.get_bytes()) != "None":
                    ext_hd += row.get_bytes()  # set from byte array
                elif row.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_FRAGMENT:
                    # length 8
                    # bytes[0] = next header
                    # bytes[1] = 1E # res
                    # bytes[2-3] = 0x0327 off set + 3 bits flags?
                    # bytes[4-7] = 0x11112222 id
                    temp_bytes = []
                    temp_bytes.append(str(NumberUtils.to_hex_value(row.next_next_header, True)))
                    temp_bytes.append("1E")  # reserved
                    temp_bytes.append("0327")  # length + 3bit flags
                    temp_bytes.append("11112222")  # id
                    ext_hd += str("".join(temp_bytes))
                elif row.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_HOP_BY_HOP:
                    # length 4
                    # bytes[0] = next header                    #
                    temp_bytes = []
                    temp_bytes.append(str(NumberUtils.to_hex_value(row.next_next_header, True)))
                    temp_bytes.append("00010400000000")
                    ext_hd += str("".join(temp_bytes))
                elif row.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_DESTINATION:
                    # length 4
                    # bytes[0] = next header                    #
                    temp_bytes = []
                    temp_bytes.append(str(NumberUtils.to_hex_value(row.next_next_header, True)))
                    temp_bytes.append("00010400000000")
                    ext_hd += str("".join(temp_bytes))
                elif row.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_ROUTING:
                    # length 4
                    # bytes[0] = next header                    #
                    temp_bytes = []
                    temp_bytes.append(str(NumberUtils.to_hex_value(row.next_next_header, True)))
                    temp_bytes.append("00000000000000")
                    ext_hd += str("".join(temp_bytes))
                elif row.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_AUTHENTICATION:
                    # length 8
                    # bytes[0] = next header                    #
                    temp_bytes = []
                    temp_bytes.append(str(NumberUtils.to_hex_value(row.next_next_header, True)))
                    temp_bytes.append("020000000000000000000000000000")
                    ext_hd += str("".join(temp_bytes))
                else:
                    ext_hd += str(row.get_bytes())
            self.header_in_bytes_only = True
            jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": "0x" + ext_hd})

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        version = self.get_bits_from_string(4, payload)
        self.set_ipv6_version("0x" + version)
        payload = self.remove_bits_from_string(4, payload)
        traffic_class = self.get_bits_from_string(8, payload)
        self.set_ipv6_traffic_class("0x" + traffic_class)
        payload = self.remove_bits_from_string(8, payload)
        flow_label = self.get_bits_from_string(20, payload)
        self.set_ipv6_flow_label("0x" + flow_label)
        payload = self.remove_bits_from_string(20, payload)
        payload_length = self.get_bits_from_string(16, payload)
        self.set_ipv6_payload_length("0x" + payload_length)
        payload = self.remove_bits_from_string(16, payload)
        next_header = self.get_bits_from_string(8, payload)
        self.set_ipv6_next_header("0x" + next_header)
        payload = self.remove_bits_from_string(8, payload)
        hop_limit = self.get_bits_from_string(8, payload)
        self.set_ipv6_hop_limit("0x" + hop_limit)
        payload = self.remove_bits_from_string(8, payload)
        source_address = self.get_bits_from_string(128, payload)
        self.set_ipv6_source_address(source_address)
        payload = self.remove_bits_from_string(128, payload)
        destination_address = self.get_bits_from_string(128, payload)
        self.set_ipv6_destination_address(destination_address)
        payload = self.remove_bits_from_string(128, payload)

        next_header = self.get_ipv6_next_header()
        extension_headers = []
        header_types = [IpV6PacketConstants.IPV6_NEXT_HEADER_HOP_BY_HOP,
                        IpV6PacketConstants.IPV6_NEXT_HEADER_DESTINATION,
                        IpV6PacketConstants.IPV6_NEXT_HEADER_ROUTING,
                        IpV6PacketConstants.IPV6_NEXT_HEADER_FRAGMENT,
                        IpV6PacketConstants.IPV6_NEXT_HEADER_AUTHENTICATION,
                        IpV6PacketConstants.IPV6_NEXT_HEADER_ENCAPSULATION
                        # IpV6PacketConstants.IPV6_NEXT_HEADER_NO_NEXT_HEADER
                        ]
        while next_header in header_types and not self.check_payload(payload) and not payload == '':
            if IpV6PacketConstants.IPV6_NEXT_HEADER_HOP_BY_HOP in header_types:
                header_types.remove(IpV6PacketConstants.IPV6_NEXT_HEADER_HOP_BY_HOP)
            try:
                # if (next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_HOP_BY_HOP or
                #         next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_DESTINATION):
                #
                # elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_ROUTING:
                # elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_FRAGMENT:
                # elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_AUTHENTICATION:
                #     break
                # elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_ENCAPSULATION:
                #     break
                # elif next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_NO_NEXT_HEADER:
                # else:
                #     break
                if next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_AUTHENTICATION:
                    length = 128
                else:
                    length = 64
                upper_layer_header = self.get_bits_from_string(8, payload)
                self.set_ipv6_last_next_header("0x" + upper_layer_header)
                length_string = self.get_bits_from_string(16, payload)[2:]
                # hop by hop = Hdr Ext Len (8 bits) Length of this header in 8-octet units, not including the
                #   first 8 octets.
                # Routing Hdr Ext Len (8 bits) The length of this header, in multiples of 8 octets, not including
                #   the first 8 octets.
                # fragment = reserved
                # Payload Len (8 bits)
                # Authentication Header The length of this Authentication Header in 4-octet units, minus 2.
                byte_option = self.get_bits_from_string(length, payload)
                payload = self.remove_bits_from_string(length, payload)
                header = Ipv6ExtentionHeaders()
                header.next_header = next_header
                header.next_next_header = upper_layer_header
                header.next_length = length_string
                header.pkt_bytes = byte_option
                extension_headers.append(header)
                next_header = int(upper_layer_header, 16)
                self.set_ipv6_extension_headers(extension_headers)
            except Exception as e:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Possible malformed ipv6 extentions")

        self.payload = payload

    def check_payload(self, payload):
        return isinstance(payload, str) and payload[0:10] == "0001020304"

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string("6", PacketConstants.INTEGER, 4)
        ret_string += self.format_byte_string(self.get_ipv6_traffic_class(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_ipv6_flow_label(), PacketConstants.INTEGER, 20)
        ret_string += self.format_byte_string(self.get_ipv6_payload_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_ipv6_next_header(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_ipv6_hop_limit(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_ipv6_source_address(), PacketConstants.IPV6_ADDRESS, 128)
        ret_string += self.format_byte_string(self.get_ipv6_destination_address(), PacketConstants.IPV6_ADDRESS, 128)
        ext_hd = ""
        if self.get_ipv6_extension_headers() and isinstance(self.get_ipv6_extension_headers(), list):
            # remove the first one because the first one is the nextheader of the packet itself
            list_of_headers = self.get_ipv6_extension_headers()
            for row in list_of_headers:
                ext_hd += str(row.get_bytes())
        return ret_string + ext_hd

    @staticmethod
    def compare_ipv6_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                   print_failures=True):
        results = True
        try:
            assert isinstance(expected, IpV6PacketHeader)
            assert isinstance(actual, IpV6PacketHeader)
            if expected.do_i_check_this_field(expected.get_ipv6_version(), IpV6PacketConstants.IPV6_VERSION,
                                              ignore_list, include_list):
                name = "IPV6 version : "
                if expected.get_ipv6_version() != actual.get_ipv6_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipv6_version()) + " != " +
                                                      str(actual.get_ipv6_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipv6_version()) + " == " +
                                                 str(actual.get_ipv6_version()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipv6_traffic_class(), IpV6PacketConstants.IPV6_TRAFFIC_CLASS,
                                              ignore_list, include_list):
                name = "IPV6 traffic class : "
                if expected.get_ipv6_traffic_class() != actual.get_ipv6_traffic_class():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipv6_traffic_class()) + " != " +
                                                      str(actual.get_ipv6_traffic_class()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipv6_traffic_class()) + " == " +
                                                 str(actual.get_ipv6_traffic_class()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipv6_flow_label(), IpV6PacketConstants.IPV6_FLOW_LABEL,
                                              ignore_list, include_list):
                name = "IPV6 flow label : "
                if expected.get_ipv6_flow_label() != actual.get_ipv6_flow_label():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipv6_flow_label()) + " != " +
                                                      str(actual.get_ipv6_flow_label()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipv6_flow_label()) + " == " +
                                                 str(actual.get_ipv6_flow_label()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipv6_payload_length(),
                                              IpV6PacketConstants.IPV6_PAYLOAD_LENGTH, ignore_list, include_list):
                name = "IPV6 payload length : "
                if expected.get_ipv6_payload_length() != actual.get_ipv6_payload_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipv6_payload_length()) + " != " +
                                                      str(actual.get_ipv6_payload_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipv6_payload_length()) + " == " +
                                                 str(actual.get_ipv6_payload_length()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipv6_next_header(), IpV6PacketConstants.IPV6_NEXT_HEADER,
                                              ignore_list, include_list):
                name = "IPV6 next header : "
                if expected.get_ipv6_next_header() != actual.get_ipv6_next_header():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipv6_next_header()) + " != " +
                                                      str(actual.get_ipv6_next_header()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipv6_next_header()) + " == " +
                                                 str(actual.get_ipv6_next_header()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipv6_hop_limit(), IpV6PacketConstants.IPV6_HOP_LIMIT,
                                              ignore_list, include_list):
                name = "IPV6 hop limit : "
                if expected.get_ipv6_hop_limit() != actual.get_ipv6_hop_limit():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipv6_hop_limit()) + " != " +
                                                      str(actual.get_ipv6_hop_limit()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipv6_hop_limit()) + " == " +
                                                 str(actual.get_ipv6_hop_limit()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipv6_source_address(),
                                              IpV6PacketConstants.IPV6_SOURCE_ADDRESS, ignore_list, include_list):
                name = "IPV6 source address : "
                if expected.get_ipv6_source_address() != actual.get_ipv6_source_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipv6_source_address()) + " != " +
                                                      str(actual.get_ipv6_source_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipv6_source_address()) + " == " +
                                                 str(actual.get_ipv6_source_address()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipv6_destination_address(),
                                              IpV6PacketConstants.IPV6_DESTINATION_ADDRESS, ignore_list, include_list):
                name = "IPV6 destination address : "
                if expected.get_ipv6_destination_address() != actual.get_ipv6_destination_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipv6_destination_address()) + " != " +
                                                      str(actual.get_ipv6_destination_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipv6_destination_address()) + " == " +
                                                 str(actual.get_ipv6_destination_address()) + " Pass")
            if expected.do_i_check_this_field(expected.get_ipv6_extension_headers(),
                                              IpV6PacketConstants.IPV6_EXTENSION_HEADERS, ignore_list, include_list):
                name = "IPV6 Extension Headers : "
                ex_string = "".join([x.comp() for x in expected.get_ipv6_extension_headers()])
                act_string = "".join([x.comp() for x in actual.get_ipv6_extension_headers()])

                if ex_string != act_string:
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + ex_string + " != " + act_string + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + ex_string + " == " + act_string + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with IpV6PacketHeader")
        return results


class Ipv6ExtentionHeaders:
    def __init__(self):
        self.next_header = None
        self.next_next_header = None
        self.bytes = None
        self.pkt_bytes = None
        self.next_string = None
        self.next_length = None

    def set_next_header(self, next_header):
        self.next_header = next_header
        self.get_next_header_string(next_header)

    def set_bytes(self, pkt_bytes):
        self.pkt_bytes = pkt_bytes

    def get_next_header_string(self, next_header):
        self.next_string = "Unknown"
        if self.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_HOP_BY_HOP:
            self.next_string = "HOP_BY_HOP"
        elif self.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_DESTINATION:
            self.next_string = "IPV6_NEXT_HEADER_DESTINATION"
        elif self.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_ROUTING:
            self.next_string = "ROUTING"
        elif self.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_FRAGMENT:
            self.next_string = "FRAGMENT"
        elif self.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_AUTHENTICATION:
            self.next_string = "AUTHENTICATION"
        elif self.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_ENCAPSULATION:
            self.next_string = "ENCAPSULATION"
        elif self.next_header == IpV6PacketConstants.IPV6_NEXT_HEADER_NO_NEXT_HEADER:
            self.next_string = "NO_NEXT_HEADER"

    def get_bytes(self):
        # next_header to HEX, 00, 2C, etc..
        # next_length to HEX  08
        # bytes padded
        return self.pkt_bytes

    def __str__(self):
        self.get_next_header_string(self.next_header)
        return str(self.next_string) + "(" + str(self.next_header) + ") " + str(self.pkt_bytes)

    def comp(self):
        self.get_next_header_string(self.next_header)
        return str(self.next_string) + "(" + str(self.next_header) + ") "


class IpV6PacketConstants:
    def __init__(self):
        pass

    IPV6_VERSION = "IPV6_VERSION"

    IPV6_TRAFFIC_CLASS = "IPV6_TRAFFIC_CLASS"

    IPV6_FLOW_LABEL = "IPV6_FLOW_LABEL"

    IPV6_PAYLOAD_LENGTH = "IPV6_PAYLOAD_LENGTH"

    IPV6_NEXT_HEADER = "IPV6_NEXT_HEADER"
    IPV6_NEXT_HEADER_HOP_BY_HOP = 0
    IPV6_NEXT_HEADER_DESTINATION = 60
    IPV6_NEXT_HEADER_ROUTING = 43
    IPV6_NEXT_HEADER_FRAGMENT = 44
    IPV6_NEXT_HEADER_AUTHENTICATION = 51
    IPV6_NEXT_HEADER_ENCAPSULATION = 50
    IPV6_NEXT_HEADER_NO_NEXT_HEADER = 59

    IPV6_HOP_LIMIT = "IPV6_HOP_LIMIT"

    IPV6_SOURCE_ADDRESS = "IPV6_SOURCE_ADDRESS"
    IPV6_SOURCE_ADDRESS_MODE = "IPV6_SOURCE_ADDRESS_MODE"
    IPV6_SOURCE_ADDRESS_COUNT = "IPV6_SOURCE_ADDRESS_COUNT"
    IPV6_SOURCE_ADDRESS_MASK = "IPV6_SOURCE_ADDRESS_MASK"

    IPV6_DESTINATION_ADDRESS = "IPV6_DESTINATION_ADDRESS"
    IPV6_DESTINATION_ADDRESS_MODE = "IPV6_DESTINATION_ADDRESS_MODE"
    IPV6_DESTINATION_ADDRESS_COUNT = "IPV6_DESTINATION_ADDRESS_COUNT"
    IPV6_DESTINATION_ADDRESS_MASK = "IPV6_DESTINATION_ADDRESS_MASK"

    IPV6_EXTENSION_HEADERS = "IPV6_EXTENSION_HEADERS"

    IPV6_LAST_NEXT_HEADER = "IPV6_LAST_NEXT_HEADER"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
