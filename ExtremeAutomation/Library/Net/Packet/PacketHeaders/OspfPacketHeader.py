from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb


class OspfPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    OSPF Packet Header
        # version = 8bits
        # message type = 8bits
        # packet length = 16bits
        # source OSPF route = 32bits
        # Area Id = 32bits
        # checksum = 16bits
        # auth type = 16bits
        # auth data = 64bits

        http://www.freesoft.org/CIE/RFC/1583/103.htm
        0                   1                   2                   3
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |   Version #   |       1       |         Packet length         |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                          Router ID                            |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                           Area ID                             |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |           Checksum            |             AuType            |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                       Authentication                          |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                       Authentication                          |
    """

    def __init__(self):
        self.add_ospf_header()
        self.HEADER_SIZE_OSPF = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Ospf version methods
    #  version is a 8 bit INTEGER example: 1
    def set_ospf_version(self, version, ignore_check=False):
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_VERSION, version)

    def get_ospf_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_VERSION), PacketConstants.INTEGER)

    def get_ospf_version_hltapi_cmd(self, dummy_dict):
        version = self.get_ospf_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end Ospf version methods

    # start Ospf message type methods
    #  message_type is a 8 bit INTEGER example: 1
    def set_ospf_message_type(self, message_type, ignore_check=False):
        message_type = self.normalize_value(message_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF,
                                  OspfPacketConstants.OSPF_MESSAGE_TYPE, message_type)

    def get_ospf_message_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_MESSAGE_TYPE), PacketConstants.INTEGER)

    def get_ospf_message_type_string(self):
        try:
            return OspfPacketConstants.OSPF_MESSAGE_TYPES[self.get_ospf_message_type()]
        except Exception as e:
            PacketObject.logger.log_info(repr(e))
            return "Unknown"

    def get_ospf_message_type_hltapi_cmd(self, dummy_dict):
        message_type = self.get_ospf_message_type()
        if isinstance(message_type, int):
            message_type = str(message_type)
        if message_type and 'Not Set' not in message_type:
            dummy_dict[TrafficConfigConstants.TEMP_MESSAGE_TYPE_CMD] = message_type
    # end Ospf message type methods

    # start Ospf packet length methods
    #  packet_length is a 16 bit INTEGER example: 1
    def set_ospf_packet_length(self, packet_length, ignore_check=False):
        packet_length = self.normalize_value(packet_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF,
                                  OspfPacketConstants.OSPF_PACKET_LENGTH, packet_length)

    def get_ospf_packet_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_PACKET_LENGTH), PacketConstants.INTEGER)

    def get_ospf_packet_length_hltapi_cmd(self, dummy_dict):
        packet_length = self.get_ospf_packet_length()
        if isinstance(packet_length, int):
            packet_length = str(packet_length)
        if packet_length and 'Not Set' not in packet_length:
            dummy_dict[TrafficConfigConstants.TEMP_PACKET_LENGTH_CMD] = packet_length
    # end Ospf packet length methods

    # start Ospf source OSPF route methods
    #  source_ospf_route is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_ospf_source_ospf_route(self, source_ospf_route, ignore_check=False):
        source_ospf_route = self.normalize_value(source_ospf_route, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF,
                                  OspfPacketConstants.OSPF_SOURCE_OSPF_ROUTE, source_ospf_route)

    def get_ospf_source_ospf_route(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_SOURCE_OSPF_ROUTE),
            PacketConstants.IPV4_ADDRESS)

    def get_ospf_source_ospf_route_hltapi_cmd(self, dummy_dict):
        source_ospf_route = self.get_ospf_source_ospf_route()
        if source_ospf_route and 'Not Set' not in source_ospf_route:
            dummy_dict[TrafficConfigConstants.TEMP_SOURCE_OSPF_ROUTE_CMD] = source_ospf_route
    # end Ospf source OSPF route methods

    # start Ospf Area Id methods
    #  area_id is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_ospf_area_id(self, area_id, ignore_check=False):
        area_id = self.normalize_value(area_id, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_AREA_ID, area_id)

    def get_ospf_area_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_AREA_ID), PacketConstants.IPV4_ADDRESS)

    def get_ospf_area_id_hltapi_cmd(self, dummy_dict):
        area_id = self.get_ospf_area_id()
        if area_id and 'Not Set' not in area_id:
            dummy_dict[TrafficConfigConstants.TEMP_AREA_ID_CMD] = area_id
    # end Ospf Area Id methods

    # start Ospf checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_ospf_checksum(self, checksum, ignore_check=False):
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_CHECKSUM, checksum)

    def get_ospf_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_CHECKSUM), PacketConstants.INTEGER)

    def get_ospf_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_ospf_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end Ospf checksum methods

    # start Ospf auth type methods
    #  auth_type is a 16 bit INTEGER example: 1
    def set_ospf_auth_type(self, auth_type, ignore_check=False):
        auth_type = self.normalize_value(auth_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_AUTH_TYPE, auth_type)

    def get_ospf_auth_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_AUTH_TYPE), PacketConstants.INTEGER)

    def get_ospf_auth_type_hltapi_cmd(self, dummy_dict):
        auth_type = self.get_ospf_auth_type()
        if isinstance(auth_type, int):
            auth_type = str(auth_type)
        if auth_type and 'Not Set' not in auth_type:
            dummy_dict[TrafficConfigConstants.TEMP_AUTH_TYPE_CMD] = auth_type
    # end Ospf auth type methods

    # start Ospf auth data methods
    #  auth_data is a 64 bit HEX_STRING example: FFFFFFFFFFFFFFFF
    def set_ospf_auth_data(self, auth_data, ignore_check=False):
        auth_data = self.normalize_value(auth_data, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_AUTH_DATA, auth_data)

    def get_ospf_auth_data(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_AUTH_DATA), PacketConstants.HEX_STRING)

    def get_ospf_auth_data_hltapi_cmd(self, dummy_dict):
        auth_data = self.get_ospf_auth_data()
        if auth_data and 'Not Set' not in auth_data:
            dummy_dict[TrafficConfigConstants.TEMP_AUTH_DATA_CMD] = auth_data
    # end Ospf auth data methods

    # start Ospf auth crypt data methods
    #  auth_data is a 64 bit HEX_STRING example: FFFFFFFFFFFFFFFF
    def set_ospf_auth_crypt_data(self, auth_data, ignore_check=False):
        auth_data = self.normalize_value(auth_data, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF,
                                  OspfPacketConstants.OSPF_AUTH_CRYPT_DATA, auth_data)

    def get_ospf_auth_crypt_data(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF, OspfPacketConstants.OSPF_AUTH_CRYPT_DATA),
            PacketConstants.HEX_STRING)

    def get_ospf_auth_crypt_data_hltapi_cmd(self, dummy_dict):
        auth_data = self.get_ospf_auth_data()
        if auth_data and 'Not Set' not in auth_data:
            dummy_dict[TrafficConfigConstants.TEMP_AUTH_DATA_CMD] = auth_data
    # end Ospf auth data methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("version", self.format_int(self.get_ospf_version(), 2))
        table.add_row_value("message type", self.get_ospf_message_type_string() + " " +
                            str(self.format_int(self.get_ospf_message_type(), 2)))
        table.add_row_value("packet length", self.format_int(self.get_ospf_packet_length(), 4))
        table.add_row_value("source OSPF route", self.get_ospf_source_ospf_route())
        table.add_row_value("Area Id", self.get_ospf_area_id())
        table.add_row_value("checksum", self.format_int(self.get_ospf_checksum(), 4))
        table.add_row_value("auth type", self.format_int(self.get_ospf_auth_type(), 4))
        table.add_row_value("auth data", self.get_ospf_auth_data())
        return "\n\nOSPF HEADER" + table.to_table_string()

    def add_ospf_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_OSPF)

    def build(self):
        self.add_ospf_header()
        self.set_ip_protocol(0x89, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_ospf_version_hltapi_cmd(dummy_dict)
        # self.get_ospf_message_type_hltapi_cmd(dummy_dict)
        # self.get_ospf_packet_length_hltapi_cmd(dummy_dict)
        # self.get_ospf_source_ospf_route_hltapi_cmd(dummy_dict)
        # self.get_ospf_area_id_hltapi_cmd(dummy_dict)
        # self.get_ospf_checksum_hltapi_cmd(dummy_dict)
        # self.get_ospf_auth_type_hltapi_cmd(dummy_dict)
        # self.get_ospf_auth_data_hltapi_cmd(dummy_dict)
        dummy_dict[TrafficConfigConstants.L4_PROTOCOL_CMD] = TrafficConfigConstants.L4_PROTOCOL_OSPF  # constant value
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_ospf(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_ospf(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_ospf(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_ospf(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kospfFieldNumber
        # update this from the ostinato docs.
        # ospfField = p.Extensions[ospf]
        # if self.is_field_set(self.get_ospf_version()):
        #     ospfField.version = int(self.get_ospf_version())
        # if self.is_field_set(self.get_ospf_message_type()):
        #     ospfField.version = int(self.get_ospf_message_type())
        # if self.is_field_set(self.get_ospf_packet_length()):
        #     ospfField.version = int(self.get_ospf_packet_length())
        # if self.is_field_set(self.get_ospf_source_ospf_route()):
        #     ospfField.version = int(self.get_ospf_source_ospf_route())
        # if self.is_field_set(self.get_ospf_area_id()):
        #     ospfField.version = int(self.get_ospf_area_id())
        # if self.is_field_set(self.get_ospf_checksum()):
        #     ospfField.version = int(self.get_ospf_checksum())
        # if self.is_field_set(self.get_ospf_auth_type()):
        #     ospfField.version = int(self.get_ospf_auth_type())
        # if self.is_field_set(self.get_ospf_auth_data()):
        #     ospfField.version = int(self.get_ospf_auth_data())

    def config_jets_stream_ospf(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "OSPF_HDR"
        pkt_bytes = "0x" + OspfPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_ospf_version()) :
        #     pkt_fields["version"] = int(self.get_ospf_version())
        # if self.is_field_set(self.get_ospf_message_type()) :
        #     pkt_fields["message_type"] = int(self.get_ospf_message_type())
        # if self.is_field_set(self.get_ospf_packet_length()) :
        #     pkt_fields["packet_length"] = int(self.get_ospf_packet_length())
        # if self.is_field_set(self.get_ospf_source_ospf_route()) :
        #     pkt_fields["source_ospf_route"] = int(self.get_ospf_source_ospf_route())
        # if self.is_field_set(self.get_ospf_area_id()) :
        #     pkt_fields["area_id"] = int(self.get_ospf_area_id())
        # if self.is_field_set(self.get_ospf_checksum()) :
        #     pkt_fields["checksum"] = int(self.get_ospf_checksum())
        # if self.is_field_set(self.get_ospf_auth_type()) :
        #     pkt_fields["auth_type"] = int(self.get_ospf_auth_type())
        # if self.is_field_set(self.get_ospf_auth_data()) :
        #     pkt_fields["auth_data"] = int(self.get_ospf_auth_data())

    def get_ixtclhal_ospf_api_commands(self, port_string, streamid):
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
        version = self.get_bits_from_string(8, payload)
        self.set_ospf_version("0x" + version)
        payload = self.remove_bits_from_string(8, payload)
        message_type = self.get_bits_from_string(8, payload)
        self.set_ospf_message_type("0x" + message_type)
        payload = self.remove_bits_from_string(8, payload)
        packet_length = self.get_bits_from_string(16, payload)
        self.set_ospf_packet_length("0x" + packet_length)
        payload = self.remove_bits_from_string(16, payload)
        source_ospf_route = self.get_bits_from_string(32, payload)
        self.set_ospf_source_ospf_route("0x" + source_ospf_route)
        payload = self.remove_bits_from_string(32, payload)
        area_id = self.get_bits_from_string(32, payload)
        self.set_ospf_area_id("0x" + area_id)
        payload = self.remove_bits_from_string(32, payload)
        checksum = self.get_bits_from_string(16, payload)
        self.set_ospf_checksum("0x" + checksum)
        payload = self.remove_bits_from_string(16, payload)
        auth_type = self.get_bits_from_string(16, payload)
        self.set_ospf_auth_type("0x" + auth_type)
        payload = self.remove_bits_from_string(16, payload)
        auth_type = int(auth_type, 16)
        # if auth_type == 2: # pull off the length field.
        #     auth_crypt_data_length = int(self.get_bits_from_string(16, payload), 16) | 0x0FF
        #     auth_length = auth_crypt_data_length*8
        # else:
        auth_length = 64

        auth_data = self.get_bits_from_string(auth_length, payload)
        self.set_ospf_auth_data("0x" + auth_data)
        payload = self.remove_bits_from_string(auth_length, payload)
        self.payload = payload

    @staticmethod
    def process_auth_entry(payload, packet):
        auth_type = packet.get_ospf_auth_type()
        auth_data = packet.get_ospf_auth_data()
        if auth_type == 2:
            auth_length = auth_data.replace("0x", "").replace(" ", "")
            auth_length = int(auth_length[0:8], 16)
            auth_crypt_data = packet.get_bits_from_string(auth_length * 8, payload)
            packet.set_ospf_auth_crypt_data("0x" + auth_crypt_data)
            payload = packet.remove_bits_from_string(auth_length * 8, payload)
        return payload

    @staticmethod
    def get_bytes_auth_entry(packet):
        auth_type = packet.get_ospf_auth_type()
        auth_data = packet.get_ospf_auth_data()
        ret_string = ""
        if auth_type == 2:
            auth_length = auth_data.replace("0x", "").replace(" ", "")
            auth_length = int(auth_length[0:8], 16)
            ret_string = packet.format_byte_string(packet.get_ospf_auth_crypt_data(), PacketConstants.HEX_STRING,
                                                   auth_length * 8)
        return ret_string

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_ospf_version(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_ospf_message_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_ospf_packet_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_ospf_source_ospf_route(), PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_ospf_area_id(), PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_ospf_checksum(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_ospf_auth_type(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_ospf_auth_data(),
                                              PacketConstants.HEX_STRING, 64).replace("0x", "")
        return ret_string

    @staticmethod
    def compare_ospf_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, OspfPacketHeader)
            assert isinstance(actual, OspfPacketHeader)
            if expected.is_field_set(expected.get_ospf_version()) and \
                    OspfPacketConstants.OSPF_VERSION not in ignore_list:
                name = "OSPF version : "
                if expected.get_ospf_version() != actual.get_ospf_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ospf_version()) + " != " +
                                                      str(actual.get_ospf_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ospf_version()) + " == " +
                                                 str(actual.get_ospf_version()) + " Pass")

            if expected.is_field_set(expected.get_ospf_message_type()) and \
                    OspfPacketConstants.OSPF_MESSAGE_TYPE not in ignore_list:
                name = "OSPF message type : "
                if expected.get_ospf_message_type() != actual.get_ospf_message_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ospf_message_type()) + " != " +
                                                      str(actual.get_ospf_message_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ospf_message_type()) + " == " +
                                                 str(actual.get_ospf_message_type()) + " Pass")

            if expected.is_field_set(expected.get_ospf_packet_length()) and \
                    OspfPacketConstants.OSPF_PACKET_LENGTH not in ignore_list:
                name = "OSPF packet length : "
                if expected.get_ospf_packet_length() != actual.get_ospf_packet_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ospf_packet_length()) + " != " +
                                                      str(actual.get_ospf_packet_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ospf_packet_length()) + " == " +
                                                 str(actual.get_ospf_packet_length()) + " Pass")

            if expected.is_field_set(expected.get_ospf_source_ospf_route()) and \
                    OspfPacketConstants.OSPF_SOURCE_OSPF_ROUTE not in ignore_list:
                name = "OSPF source ospf route : "
                if expected.get_ospf_source_ospf_route() != actual.get_ospf_source_ospf_route():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ospf_source_ospf_route()) + " != " +
                                                      str(actual.get_ospf_source_ospf_route()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ospf_source_ospf_route()) + " == " +
                                                 str(actual.get_ospf_source_ospf_route()) + " Pass")

            if expected.is_field_set(expected.get_ospf_area_id()) and \
                    OspfPacketConstants.OSPF_AREA_ID not in ignore_list:
                name = "OSPF area id : "
                if expected.get_ospf_area_id() != actual.get_ospf_area_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ospf_area_id()) + " != " +
                                                      str(actual.get_ospf_area_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ospf_area_id()) + " == " +
                                                 str(actual.get_ospf_area_id()) + " Pass")

            if expected.is_field_set(expected.get_ospf_checksum()) and \
                    OspfPacketConstants.OSPF_CHECKSUM not in ignore_list:
                name = "OSPF checksum : "
                if expected.get_ospf_checksum() != actual.get_ospf_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ospf_checksum()) + " != " +
                                                      str(actual.get_ospf_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ospf_checksum()) + " == " +
                                                 str(actual.get_ospf_checksum()) + " Pass")

            if expected.is_field_set(expected.get_ospf_auth_type()) and \
                    OspfPacketConstants.OSPF_AUTH_TYPE not in ignore_list:
                name = "OSPF auth type : "
                if expected.get_ospf_auth_type() != actual.get_ospf_auth_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ospf_auth_type()) + " != " +
                                                      str(actual.get_ospf_auth_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ospf_auth_type()) + " == " +
                                                 str(actual.get_ospf_auth_type()) + " Pass")

            if expected.is_field_set(expected.get_ospf_auth_data()) and \
                    OspfPacketConstants.OSPF_AUTH_DATA not in ignore_list:
                name = "OSPF auth data : "
                if expected.get_ospf_auth_data() != actual.get_ospf_auth_data():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ospf_auth_data()) + " != " +
                                                      str(actual.get_ospf_auth_data()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ospf_auth_data()) + " == " +
                                                 str(actual.get_ospf_auth_data()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with OspfPacketHeader")
        return results


class OspfTlvEntry(object):
    def __init__(self, pkt_type, length, data):
        self.pkt_type = pkt_type
        self.type_string = self.get_type_string(pkt_type)
        self.length = length
        self.data = data

    def get_type_string(self, pkt_type):
        if pkt_type == 0x01:
            return "Extended options TLV"
        elif pkt_type == 2:
            return "Crypto Authentication TLV"
        else:
            return "Unknown Type"

    @staticmethod
    def process_tlv(payload, tlv_entries, pdu_length, handler):
        pdu_length = int(pdu_length, 16)
        while pdu_length > 0 and payload != "":
            tlv_type = handler.get_bits_from_string(16, payload)
            tlv_type = int(tlv_type, 16)
            payload = handler.remove_bits_from_string(16, payload)
            pdu_length -= 1
            tlv_length = handler.get_bits_from_string(16, payload)
            tlv_length = int(tlv_length, 16)
            payload = handler.remove_bits_from_string(16, payload)
            pdu_length -= 1
            tlv_data = handler.get_bits_from_string(tlv_length * 8, payload)
            payload = handler.remove_bits_from_string(tlv_length * 8, payload)
            pdu_length -= tlv_length
            tlv_entries.append(OspfTlvEntry(tlv_type, tlv_length, tlv_data))
        return payload

    @staticmethod
    def to_packet_string(packet):
        table_tlv = TableFormatter()
        for entry in packet.tlv_entries:
            table_tlv.add_row_value("type", entry.type_string + " " + packet.format_int(entry.type, 2))
            table_tlv.add_row_value("length", packet.format_int(entry.length, 2))
            table_tlv.add_row_value("data", entry.data)
        return table_tlv


class OspfPacketConstants:
    def __init__(self):
        pass

    OSPF_VERSION = "OSPF_VERSION"

    OSPF_MESSAGE_TYPE = "OSPF_MESSAGE_TYPE"
    OSPF_MESSAGE_TYPE_HELLO = "1"
    OSPF_MESSAGE_TYPE_DATABASE_DESCRIPTION = "2"
    OSPF_MESSAGE_TYPE_LINK_STATE_REQUEST = "3"
    OSPF_MESSAGE_TYPE_LINK_STATE_UPDATE = "4"
    OSPF_MESSAGE_TYPE_LINK_STATE_ACKNOWLEDGMENT = "5"
    OSPF_MESSAGE_TYPES = {1: "Hello",
                          2: "Database Description",
                          3: "Link State Request",
                          4: "Link State Update",
                          5: "Link State Acknowledgment"}

    OSPF_PACKET_LENGTH = "OSPF_PACKET_LENGTH"
    OSPF_SOURCE_OSPF_ROUTE = "OSPF_SOURCE_OSPF_ROUTE"
    OSPF_AREA_ID = "OSPF_AREA_ID"
    OSPF_CHECKSUM = "OSPF_CHECKSUM"

    OSPF_AUTH_TYPE = "OSPF_AUTH_TYPE"
    OSPF_AUTH_DATA = "OSPF_AUTH_DATA"
    OSPF_AUTH_CRYPT_DATA = "OSPF_AUTH_CRYPT_DATA"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
