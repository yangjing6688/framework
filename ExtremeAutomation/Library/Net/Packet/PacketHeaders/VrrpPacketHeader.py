from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader


class VrrpPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    VRRP Packet Header
        # Version = 4bits
        # Type = 4bits
        # Virtual Router ID = 8bits
        # Priority = 8bits
        # IP Address Count = 8bits
        # Authentication Type = 8bits
        # Advertisement Interval = 8bits
        # Checksum = 16bits
        # IP Addresses = 32bits
        # Authentication Data = 32bits
    """

    def __init__(self):
        self.add_vrrp_header()
        self.HEADER_SIZE_VRRP = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Vrrp Version methods
    #  version is a 4 bit INTEGER example: 1
    def set_vrrp_version(self, version, ignore_check=False):
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_VERSION, version)

    def get_vrrp_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_VERSION), PacketConstants.INTEGER)

    def get_vrrp_version_hltapi_cmd(self, dummy_dict):
        version = self.get_vrrp_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end Vrrp Version methods

    # start Vrrp Type methods
    #  type is a 4 bit INTEGER example: 1
    def set_vrrp_type(self, pkt_type, ignore_check=False):
        pkt_type = self.normalize_value(pkt_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_TYPE, pkt_type)

    def get_vrrp_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_TYPE), PacketConstants.INTEGER)

    def get_vrrp_type_hltapi_cmd(self, dummy_dict):
        pkt_type = self.get_vrrp_type()
        if isinstance(pkt_type, int):
            pkt_type = str(pkt_type)
        if pkt_type and 'Not Set' not in pkt_type:
            dummy_dict[TrafficConfigConstants.TEMP_TYPE_CMD] = pkt_type
    # end Vrrp Type methods

    # start Vrrp Virtual Router ID methods
    #  virtual_router_id is a 8 bit INTEGER example: 1
    def set_vrrp_virtual_router_id(self, virtual_router_id, ignore_check=False):
        virtual_router_id = self.normalize_value(virtual_router_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP,
                                  VrrpPacketConstants.VRRP_VIRTUAL_ROUTER_ID, virtual_router_id)

    def get_vrrp_virtual_router_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_VIRTUAL_ROUTER_ID), PacketConstants.INTEGER)

    def get_vrrp_virtual_router_id_hltapi_cmd(self, dummy_dict):
        virtual_router_id = self.get_vrrp_virtual_router_id()
        if isinstance(virtual_router_id, int):
            virtual_router_id = str(virtual_router_id)
        if virtual_router_id and 'Not Set' not in virtual_router_id:
            dummy_dict[TrafficConfigConstants.TEMP_VIRTUAL_ROUTER_ID_CMD] = virtual_router_id
    # end Vrrp Virtual Router ID methods

    # start Vrrp Priority methods
    #  priority is a 8 bit INTEGER example: 1
    def set_vrrp_priority(self, priority, ignore_check=False):
        priority = self.normalize_value(priority, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_PRIORITY, priority)

    def get_vrrp_priority(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_PRIORITY), PacketConstants.INTEGER)

    def get_vrrp_priority_hltapi_cmd(self, dummy_dict):
        priority = self.get_vrrp_priority()
        if isinstance(priority, int):
            priority = str(priority)
        if priority and 'Not Set' not in priority:
            dummy_dict[TrafficConfigConstants.TEMP_PRIORITY_CMD] = priority
    # end Vrrp Priority methods

    # start Vrrp IP Address Count methods
    #  ip_address_count is a 8 bit INTEGER example: 1
    def set_vrrp_ip_address_count(self, ip_address_count, ignore_check=False):
        ip_address_count = self.normalize_value(ip_address_count, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP,
                                  VrrpPacketConstants.VRRP_IP_ADDRESS_COUNT, ip_address_count)

    def get_vrrp_ip_address_count(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_IP_ADDRESS_COUNT), PacketConstants.INTEGER)

    def get_vrrp_ip_address_count_hltapi_cmd(self, dummy_dict):
        ip_address_count = self.get_vrrp_ip_address_count()
        if isinstance(ip_address_count, int):
            ip_address_count = str(ip_address_count)
        if ip_address_count and 'Not Set' not in ip_address_count:
            dummy_dict[TrafficConfigConstants.TEMP_IP_ADDRESS_COUNT_CMD] = ip_address_count
    # end Vrrp IP Address Count methods

    # start Vrrp Authentication Type methods
    #  authentication_type is a 8 bit INTEGER example: 1
    def set_vrrp_authentication_type(self, authentication_type, ignore_check=False):
        authentication_type = self.normalize_value(authentication_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP,
                                  VrrpPacketConstants.VRRP_AUTHENTICATION_TYPE, authentication_type)

    def get_vrrp_authentication_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_AUTHENTICATION_TYPE),
            PacketConstants.INTEGER)

    def get_vrrp_authentication_type_hltapi_cmd(self, dummy_dict):
        authentication_type = self.get_vrrp_authentication_type()
        if isinstance(authentication_type, int):
            authentication_type = str(authentication_type)
        if authentication_type and 'Not Set' not in authentication_type:
            dummy_dict[TrafficConfigConstants.TEMP_AUTHENTICATION_TYPE_CMD] = authentication_type
    # end Vrrp Authentication Type methods

    # start Vrrp Advertisement Interval methods
    #  advertisement_interval is a 8 bit INTEGER example: 1
    def set_vrrp_advertisement_interval(self, advertisement_interval, ignore_check=False):
        advertisement_interval = self.normalize_value(advertisement_interval, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP,
                                  VrrpPacketConstants.VRRP_ADVERTISEMENT_INTERVAL, advertisement_interval)

    def get_vrrp_advertisement_interval(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_ADVERTISEMENT_INTERVAL),
            PacketConstants.INTEGER)

    def get_vrrp_advertisement_interval_hltapi_cmd(self, dummy_dict):
        advertisement_interval = self.get_vrrp_advertisement_interval()
        if isinstance(advertisement_interval, int):
            advertisement_interval = str(advertisement_interval)
        if advertisement_interval and 'Not Set' not in advertisement_interval:
            dummy_dict[TrafficConfigConstants.TEMP_ADVERTISEMENT_INTERVAL_CMD] = advertisement_interval
    # end Vrrp Advertisement Interval methods

    # start Vrrp Checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_vrrp_checksum(self, checksum, ignore_check=False):
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_CHECKSUM, checksum)

    def get_vrrp_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_CHECKSUM),
            PacketConstants.INTEGER)

    def get_vrrp_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_vrrp_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end Vrrp Checksum methods

    # start Vrrp IP Addresses methods
    #  ip_addresses is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_vrrp_ip_addresses(self, ip_addresses, ignore_check=False):
        ip_addresses = self.normalize_value(ip_addresses, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP,
                                  VrrpPacketConstants.VRRP_IP_ADDRESSES, ip_addresses)

    def get_vrrp_ip_addresses(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_IP_ADDRESSES), PacketConstants.HEX_STRING)

    def get_vrrp_ip_addresses_hltapi_cmd(self, dummy_dict):
        ip_addresses = self.get_vrrp_ip_addresses()
        if ip_addresses and 'Not Set' not in ip_addresses:
            dummy_dict[TrafficConfigConstants.TEMP_IP_ADDRESSES_CMD] = ip_addresses
    # end Vrrp IP Addresses methods

    # start Vrrp Authentication Data methods
    #  authentication_data is a 32 bit HEX_STRING example: FFFFFFFF
    def set_vrrp_authentication_data(self, authentication_data, ignore_check=False):
        authentication_data = self.normalize_value(authentication_data, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_VRRP,
                                  VrrpPacketConstants.VRRP_AUTHENTICATION_DATA, authentication_data)

    def get_vrrp_authentication_data(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_VRRP, VrrpPacketConstants.VRRP_AUTHENTICATION_DATA),
            PacketConstants.HEX_STRING)

    def get_vrrp_authentication_data_hltapi_cmd(self, dummy_dict):
        authentication_data = self.get_vrrp_authentication_data()
        if authentication_data and 'Not Set' not in authentication_data:
            dummy_dict[TrafficConfigConstants.TEMP_AUTHENTICATION_DATA_CMD] = authentication_data
    # end Vrrp Authentication Data methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Version", self.format_int(self.get_vrrp_version(), 0))
        table.add_row_value("Type", self.format_int(self.get_vrrp_type(), 0))
        table.add_row_value("Virtual Router ID", self.format_int(self.get_vrrp_virtual_router_id(), 1))
        table.add_row_value("Priority", self.format_int(self.get_vrrp_priority(), 1))
        table.add_row_value("IP Address Count", self.format_int(self.get_vrrp_ip_address_count(), 1))
        table.add_row_value("Authentication Type", self.format_int(self.get_vrrp_authentication_type(), 1))
        table.add_row_value("Advertisement Interval", self.format_int(self.get_vrrp_advertisement_interval(), 1))
        table.add_row_value("Checksum", self.format_int(self.get_vrrp_checksum(), 2))
        if isinstance(self, IpV4PacketHeader):
            ips = self.get_vrrp_ip_addresses().replace(" ", "")
            ips = "/".join(StringUtils.hex_str_to_ipv4_list(ips))
            table.add_row_value("IPv6 Addresses", ips)
        elif isinstance(self, IpV6PacketHeader):
            ips = self.get_vrrp_ip_addresses().replace(" ", "")
            ips = "/".join(StringUtils.hex_str_to_ipv6_list(ips))
            table.add_row_value("IPv6 Addresses", ips)
        authentication_type = self.get_vrrp_authentication_type()
        if authentication_type > 0:
            table.add_row_value("Authentication Data", self.get_vrrp_authentication_data())
        else:
            table.add_row_value("Authentication Data", "none")
        return "\n\nVRRP HEADER" + table.to_table_string()

    def add_vrrp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_VRRP)

    def build(self):
        self.add_vrrp_header()
        if isinstance(self, IpV4PacketHeader):  # you can either do this here OR in the build of each packet
            self.set_ip_protocol(112, True)
        elif isinstance(self, IpV6PacketHeader):
            self.set_ipv6_next_header(112, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_vrrp_version_hltapi_cmd(dummy_dict)
        # self.get_vrrp_type_hltapi_cmd(dummy_dict)
        # self.get_vrrp_virtual_router_id_hltapi_cmd(dummy_dict)
        # self.get_vrrp_priority_hltapi_cmd(dummy_dict)
        # self.get_vrrp_ip_address_count_hltapi_cmd(dummy_dict)
        # self.get_vrrp_authentication_type_hltapi_cmd(dummy_dict)
        # self.get_vrrp_advertisement_interval_hltapi_cmd(dummy_dict)
        # self.get_vrrp_checksum_hltapi_cmd(dummy_dict)
        # self.get_vrrp_ip_addresses_hltapi_cmd(dummy_dict)
        # self.get_vrrp_authentication_data_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_vrrp(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_vrrp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_vrrp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_vrrp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
    #     p.protocol_id.id = ost_pb.Protocol.kvrrpFieldNumber
    # # update this from the ostinato docs.
    #     vrrpField = p.Extensions[vrrp]
    #     if self.is_field_set(self.get_vrrp_version()) :
    #         vrrpField.version = int(self.get_vrrp_version())
    #     if self.is_field_set(self.get_vrrp_type()) :
    #         vrrpField.version = int(self.get_vrrp_type())
    #     if self.is_field_set(self.get_vrrp_virtual_router_id()) :
    #         vrrpField.version = int(self.get_vrrp_virtual_router_id())
    #     if self.is_field_set(self.get_vrrp_priority()) :
    #         vrrpField.version = int(self.get_vrrp_priority())
    #     if self.is_field_set(self.get_vrrp_ip_address_count()) :
    #         vrrpField.version = int(self.get_vrrp_ip_address_count())
    #     if self.is_field_set(self.get_vrrp_authentication_type()) :
    #         vrrpField.version = int(self.get_vrrp_authentication_type())
    #     if self.is_field_set(self.get_vrrp_advertisement_interval()) :
    #         vrrpField.version = int(self.get_vrrp_advertisement_interval())
    #     if self.is_field_set(self.get_vrrp_checksum()) :
    #         vrrpField.version = int(self.get_vrrp_checksum())
    #     if self.is_field_set(self.get_vrrp_ip_addresses()) :
    #         vrrpField.version = int(self.get_vrrp_ip_addresses())
    #     if self.is_field_set(self.get_vrrp_authentication_data()) :
    #         vrrpField.version = int(self.get_vrrp_authentication_data())

    def config_jets_stream_vrrp(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "VRRP_HDR"
        pkt_bytes = "0x" + VrrpPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_vrrp_version()) :
        #     pkt_fields["version"] = int(self.get_vrrp_version())
        # if self.is_field_set(self.get_vrrp_type()) :
        #     pkt_fields["type"] = int(self.get_vrrp_type())
        # if self.is_field_set(self.get_vrrp_virtual_router_id()) :
        #     pkt_fields["virtual_router_id"] = int(self.get_vrrp_virtual_router_id())
        # if self.is_field_set(self.get_vrrp_priority()) :
        #     pkt_fields["priority"] = int(self.get_vrrp_priority())
        # if self.is_field_set(self.get_vrrp_ip_address_count()) :
        #     pkt_fields["ip_address_count"] = int(self.get_vrrp_ip_address_count())
        # if self.is_field_set(self.get_vrrp_authentication_type()) :
        #     pkt_fields["authentication_type"] = int(self.get_vrrp_authentication_type())
        # if self.is_field_set(self.get_vrrp_advertisement_interval()) :
        #     pkt_fields["advertisement_interval"] = int(self.get_vrrp_advertisement_interval())
        # if self.is_field_set(self.get_vrrp_checksum()) :
        #     pkt_fields["checksum"] = int(self.get_vrrp_checksum())
        # if self.is_field_set(self.get_vrrp_ip_addresses()) :
        #     pkt_fields["ip_addresses"] = int(self.get_vrrp_ip_addresses())
        # if self.is_field_set(self.get_vrrp_authentication_data()) :
        #     pkt_fields["authentication_data"] = int(self.get_vrrp_authentication_data())

    def get_ixtclhal_vrrp_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        # ### put some IxTclHal info here.
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        version = self.get_bits_from_string(4, payload)
        self.set_vrrp_version("0x" + version)
        payload = self.remove_bits_from_string(4, payload)
        pkt_type = self.get_bits_from_string(4, payload)
        self.set_vrrp_type("0x" + pkt_type)
        payload = self.remove_bits_from_string(4, payload)
        virtual_router_id = self.get_bits_from_string(8, payload)
        self.set_vrrp_virtual_router_id("0x" + virtual_router_id)
        payload = self.remove_bits_from_string(8, payload)
        priority = self.get_bits_from_string(8, payload)
        self.set_vrrp_priority("0x" + priority)
        payload = self.remove_bits_from_string(8, payload)
        ip_address_count = self.get_bits_from_string(8, payload)
        self.set_vrrp_ip_address_count("0x" + ip_address_count)
        ip_address_count = NumberUtils.to_integer_value("0x" + ip_address_count)
        payload = self.remove_bits_from_string(8, payload)
        authentication_type = self.get_bits_from_string(8, payload)
        self.set_vrrp_authentication_type("0x" + authentication_type)
        payload = self.remove_bits_from_string(8, payload)
        authentication_type = NumberUtils.to_integer_value("0x" + authentication_type)
        advertisement_interval = self.get_bits_from_string(8, payload)
        self.set_vrrp_advertisement_interval("0x" + advertisement_interval)
        payload = self.remove_bits_from_string(8, payload)
        checksum = self.get_bits_from_string(16, payload)
        self.set_vrrp_checksum("0x" + checksum)
        payload = self.remove_bits_from_string(16, payload)
        if isinstance(self, IpV4PacketHeader):
            size = ip_address_count * 32
        elif isinstance(self, IpV6PacketHeader):
            size = ip_address_count * 128
        ip_addresses = self.get_bits_from_string(size, payload)
        self.set_vrrp_ip_addresses(ip_addresses)
        payload = self.remove_bits_from_string(size, payload)
        # if the auth type doesn't = 0
        if authentication_type > 0:
            authentication_data = self.get_bits_from_string(32, payload)
            self.set_vrrp_authentication_data("0x" + authentication_data)
            payload = self.remove_bits_from_string(32, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_vrrp_version(), PacketConstants.INTEGER, 4)
        ret_string += self.format_byte_string(self.get_vrrp_type(), PacketConstants.INTEGER, 4)
        ret_string += self.format_byte_string(self.get_vrrp_virtual_router_id(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_vrrp_priority(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_vrrp_ip_address_count(), PacketConstants.INTEGER, 8)
        ip_count = self.get_vrrp_ip_address_count()
        ret_string += self.format_byte_string(self.get_vrrp_authentication_type(), PacketConstants.INTEGER, 8)
        authentication_type = self.get_vrrp_authentication_type()
        ret_string += self.format_byte_string(self.get_vrrp_advertisement_interval(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_vrrp_checksum(), PacketConstants.INTEGER, 16)
        # mights have to convert and expand here depending on the type (ipv4 or ipv6).
        # need an example of more than one address and ipv6
        ret_string += self.format_byte_string(self.get_vrrp_ip_addresses(), PacketConstants.HEX_STRING, 32)
        if authentication_type > 0:
            ret_string += self.format_byte_string(self.get_vrrp_authentication_data(), PacketConstants.HEX_STRING, 32)
        return ret_string

    @staticmethod
    def compare_vrrp_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, VrrpPacketHeader)
            assert isinstance(actual, VrrpPacketHeader)
            if expected.is_field_set(expected.get_vrrp_version()) and \
                    VrrpPacketConstants.VRRP_VERSION not in ignore_list:
                name = "VRRP version : "
                if expected.get_vrrp_version() != actual.get_vrrp_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_version()) + " != " +
                                                      str(actual.get_vrrp_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_version()) + " == " +
                                                 str(actual.get_vrrp_version()) + " Pass")

            if expected.is_field_set(expected.get_vrrp_type()) and \
                    VrrpPacketConstants.VRRP_TYPE not in ignore_list:
                name = "VRRP type : "
                if expected.get_vrrp_type() != actual.get_vrrp_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_type()) + " != " +
                                                      str(actual.get_vrrp_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_type()) + " == " +
                                                 str(actual.get_vrrp_type()) + " Pass")

            if expected.is_field_set(expected.get_vrrp_virtual_router_id()) and \
                    VrrpPacketConstants.VRRP_VIRTUAL_ROUTER_ID not in ignore_list:
                name = "VRRP virtual router id : "
                if expected.get_vrrp_virtual_router_id() != actual.get_vrrp_virtual_router_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_virtual_router_id()) + " != " +
                                                      str(actual.get_vrrp_virtual_router_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_virtual_router_id()) + " == " +
                                                 str(actual.get_vrrp_virtual_router_id()) + " Pass")

            if expected.is_field_set(expected.get_vrrp_priority()) and \
                    VrrpPacketConstants.VRRP_PRIORITY not in ignore_list:
                name = "VRRP priority : "
                if expected.get_vrrp_priority() != actual.get_vrrp_priority():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_priority()) + " != " +
                                                      str(actual.get_vrrp_priority()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_priority()) + " == " +
                                                 str(actual.get_vrrp_priority()) + " Pass")

            if expected.is_field_set(expected.get_vrrp_ip_address_count()) and \
                    VrrpPacketConstants.VRRP_IP_ADDRESS_COUNT not in ignore_list:
                name = "VRRP ip address count : "
                if expected.get_vrrp_ip_address_count() != actual.get_vrrp_ip_address_count():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_ip_address_count()) + " != " +
                                                      str(actual.get_vrrp_ip_address_count()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_ip_address_count()) + " == " +
                                                 str(actual.get_vrrp_ip_address_count()) + " Pass")

            if expected.is_field_set(expected.get_vrrp_authentication_type()) and \
                    VrrpPacketConstants.VRRP_AUTHENTICATION_TYPE not in ignore_list:
                name = "VRRP authentication type : "
                if expected.get_vrrp_authentication_type() != actual.get_vrrp_authentication_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_authentication_type()) + " != " +
                                                      str(actual.get_vrrp_authentication_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_authentication_type()) + " == " +
                                                 str(actual.get_vrrp_authentication_type()) + " Pass")

            if expected.is_field_set(expected.get_vrrp_advertisement_interval()) and \
                    VrrpPacketConstants.VRRP_ADVERTISEMENT_INTERVAL not in ignore_list:
                name = "VRRP advertisement interval : "
                if expected.get_vrrp_advertisement_interval() != actual.get_vrrp_advertisement_interval():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_advertisement_interval()) + " != " +
                                                      str(actual.get_vrrp_advertisement_interval()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_advertisement_interval()) + " == " +
                                                 str(actual.get_vrrp_advertisement_interval()) + " Pass")

            if expected.is_field_set(expected.get_vrrp_checksum()) and \
                    VrrpPacketConstants.VRRP_CHECKSUM not in ignore_list:
                name = "VRRP checksum : "
                if expected.get_vrrp_checksum() != actual.get_vrrp_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_checksum()) + " != " +
                                                      str(actual.get_vrrp_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_checksum()) + " == " +
                                                 str(actual.get_vrrp_checksum()) + " Pass")

            if expected.is_field_set(expected.get_vrrp_ip_addresses()) and \
                    VrrpPacketConstants.VRRP_IP_ADDRESSES not in ignore_list:
                name = "VRRP ip addresses : "
                if expected.get_vrrp_ip_addresses() != actual.get_vrrp_ip_addresses():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_ip_addresses()) + " != " +
                                                      str(actual.get_vrrp_ip_addresses()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_ip_addresses()) + " == " +
                                                 str(actual.get_vrrp_ip_addresses()) + " Pass")

            if expected.is_field_set(expected.get_vrrp_authentication_data()) and \
                    VrrpPacketConstants.VRRP_AUTHENTICATION_DATA not in ignore_list:
                name = "VRRP authentication data : "
                if expected.get_vrrp_authentication_data() != actual.get_vrrp_authentication_data():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vrrp_authentication_data()) + " != " +
                                                      str(actual.get_vrrp_authentication_data()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vrrp_authentication_data()) + " == " +
                                                 str(actual.get_vrrp_authentication_data()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with VrrpPacketHeader")
        return results


class VrrpPacketConstants:
    def __init__(self):
        pass

    VRRP_VERSION = "VRRP_VERSION"
    VRRP_TYPE = "VRRP_TYPE"
    VRRP_VIRTUAL_ROUTER_ID = "VRRP_VIRTUAL_ROUTER_ID"
    VRRP_PRIORITY = "VRRP_PRIORITY"
    VRRP_IP_ADDRESS_COUNT = "VRRP_IP_ADDRESS_COUNT"
    VRRP_AUTHENTICATION_TYPE = "VRRP_AUTHENTICATION_TYPE"
    VRRP_ADVERTISEMENT_INTERVAL = "VRRP_ADVERTISEMENT_INTERVAL"
    VRRP_CHECKSUM = "VRRP_CHECKSUM"
    VRRP_IP_ADDRESSES = "VRRP_IP_ADDRESSES"
    VRRP_AUTHENTICATION_DATA = "VRRP_AUTHENTICATION_DATA"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
