import re
import binascii
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject, PacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer7PacketHeader import Layer7PacketHeader
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class RadiusPacketHeader(Layer7PacketHeader):
    RADIUS_PACKET_HEADER_LENGTH = 20
    packet_name = None
    pkt_bytes = None
    """
    RADIUS Packet Header
        # code = 8bits
        # id = 8bits
        # length = 16bits
        # authenticator = 16 bytes
        # attribute value pair = 8bits
    """

    def __init__(self):
        super(RadiusPacketHeader, self).__init__()
        self.add_radius_header()
        self.HEADER_SIZE_RADIUS = 4  # BYTES
        self.set_radius_attribute_value_pairs_num(0)

    def set_radius_attribute_value_pairs_num(self, num):
        self.num_radius_attribute_value_pairs = NumberUtils.to_integer_value(num)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS,
                                  RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_NUM,
                                  num)

    def get_radius_attribute_value_pairs_num(self):
        return self.num_radius_attribute_value_pairs

    def add_radius_attribute_value_pair(self, pkt_type=None):
        self.set_radius_attribute_value_pairs_num(self.num_radius_attribute_value_pairs + 1)
        if pkt_type is not None:
            self.set_radius_attribute_value_pair_type(pkt_type, self.num_radius_attribute_value_pairs)
        return self.num_radius_attribute_value_pairs

    def add_radius_attribute_value_pair_with_ascii(self, pkt_type, ascii_value):
        self.set_radius_attribute_value_pairs_num(self.num_radius_attribute_value_pairs + 1)
        if pkt_type is not None:
            self.set_radius_attribute_value_pair_type(pkt_type, self.num_radius_attribute_value_pairs)
        return self.num_radius_attribute_value_pairs

    def get_radius_headers_length(self):
        extension_length = RadiusPacketHeader.RADIUS_PACKET_HEADER_LENGTH
        index = 1
        while index <= self.get_radius_attribute_value_pairs_num():
            extension_length += self.get_radius_attribute_value_pair_length(index)
            index += 1
        return extension_length

    def get_radius_attribute_value_pair_in_hex_string(self, index):
        pkt_type = hex((self.get_radius_attribute_value_pair_type(index)))[2:].zfill(2)
        length = None
        if self.is_field_set(self.get_radius_attribute_value_pair_length(index)):
            length = hex((self.get_radius_attribute_value_pair_length(index)))[2:].zfill(2)
        message = self.get_radius_attribute_value_pair_data_hex(index)
        if not length:
            length = hex(2 + len(message))[2:].zfill(2)
        # message = RadiusPacketConstants.convert_mesage_to_hex(self.get_radius_attribute_value_pair_type(index),
        #                                                       self.get_radius_attribute_value_pair_length(index),
        #                                                       message)
        return pkt_type + length + message

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Radius code methods
    #  code is a 8 bit INTEGER example: 1
    def set_radius_code(self, code, ignore_check=False):
        code = self.normalize_value(code, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS, RadiusPacketConstants.RADIUS_CODE, code)

    def get_radius_code(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_RADIUS, RadiusPacketConstants.RADIUS_CODE), PacketConstants.INTEGER)

    def get_radius_code_hltapi_cmd(self, dummy_dict):
        code = self.get_radius_code()
        if isinstance(code, int):
            code = str(code)
        if code and 'Not Set' not in code:
            dummy_dict[TrafficConfigConstants.TEMP_CODE_CMD] = code
    # end Radius code methods

    # start Radius id methods
    #  id is a 8 bit INTEGER example: 1
    def set_radius_id(self, pkt_id, ignore_check=False):
        pkt_id = self.normalize_value(pkt_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS, RadiusPacketConstants.RADIUS_ID, pkt_id)

    def get_radius_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_RADIUS, RadiusPacketConstants.RADIUS_ID), PacketConstants.INTEGER)

    def get_radius_id_hltapi_cmd(self, dummy_dict):
        pkt_id = self.get_radius_id()
        if isinstance(pkt_id, int):
            pkt_id = str(pkt_id)
        if pkt_id and 'Not Set' not in pkt_id:
            dummy_dict[TrafficConfigConstants.TEMP_ID_CMD] = pkt_id
    # end Radius id methods

    # start Radius length methods
    #  length is a 16 bit INTEGER example: 1
    def set_radius_length(self, length, ignore_check=False):
        length = self.normalize_value(length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS, RadiusPacketConstants.RADIUS_LENGTH, length)

    def get_radius_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_RADIUS, RadiusPacketConstants.RADIUS_LENGTH), PacketConstants.INTEGER)

    def get_radius_length_hltapi_cmd(self, dummy_dict):
        length = self.get_radius_length()
        if isinstance(length, int):
            length = str(length)
        if length and 'Not Set' not in length:
            dummy_dict[TrafficConfigConstants.TEMP_LENGTH_CMD] = length
    # end Radius length methods

    # start Radius authenticator methods
    #  authenticator is a 8 bit INTEGER example: 1
    def set_radius_authenticator(self, authenticator, ignore_check=False):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS,
                                  RadiusPacketConstants.RADIUS_AUTHENTICATOR, authenticator.strip())

    def get_radius_authenticator(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS,
                                         RadiusPacketConstants.RADIUS_AUTHENTICATOR)

    def get_radius_authenticator_hltapi_cmd(self, dummy_dict):
        authenticator = self.get_radius_authenticator()
        if isinstance(authenticator, int):
            authenticator = str(authenticator)
        if authenticator and 'Not Set' not in authenticator:
            dummy_dict[TrafficConfigConstants.TEMP_AUTHENTICATOR_CMD] = authenticator
    # end Radius authenticator methods

    # start Radius Attribute Value Pair Type  methods
    def set_radius_attribute_value_pair_type(self, version, avp_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_TYPE + " " +
                                                        str(avp_id), ignore_check)
        flag = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS,
                                  RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_TYPE + " " + str(avp_id),
                                  flag)

    def get_radius_attribute_value_pair_type(self, avp_id):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS,
                                                              RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_TYPE +
                                                              " " + str(avp_id)), PacketConstants.INTEGER)
    # end Radius Attribute Value Pair Type methods

    # start Radius Attribute Value Pair LENGTH  methods
    def set_radius_attribute_value_pair_length(self, version, avp_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_LENGTH + " " +
                                                        str(avp_id), ignore_check)
        flag = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS,
                                  RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_LENGTH + " " + str(avp_id), flag)

    def get_radius_attribute_value_pair_length(self, avp_id):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS,
                                                              RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_LENGTH +
                                                              " " + str(avp_id)), PacketConstants.INTEGER)
    # end Radius Attribute Value Pair LENGTH methods

    # start Lldp TLV Message  methods
    #  version is a 9 bit INTEGER example: 1
    def set_radius_attribute_value_pair_data(self, version, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_DATA + " " +
                                                        str(mstid_id), ignore_check)
        flag = version
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS,
                                  RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_DATA + " " + str(mstid_id),
                                  flag)

    def get_radius_attribute_value_pair_data(self, mstid_id):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_RADIUS,
                                         RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_DATA + " " + str(mstid_id))

    def get_radius_attribute_value_pair_data_hex(self, mstid_id):
        pkt_type = self.get_radius_attribute_value_pair_type(mstid_id)
        length = self.get_radius_attribute_value_pair_length(mstid_id)
        message = self.get_radius_attribute_value_pair_data(mstid_id)
        return RadiusPacketConstants.convert_mesage_to_hex(pkt_type, length, message)

    # ########### Acsii string types
    # example: packet.add_radius_attribute_value_pair_reply_message("Hell0, %u")
    def add_radius_attribute_value_pair_reply_message(self, reply_message):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_REPLY_MESSAGE)
        self.set_radius_attribute_value_pair_length(len(reply_message) + 2, index)
        self.set_radius_attribute_value_pair_data(reply_message, index)

    # example: packet.add_radius_attribute_value_pair_username("John.McGuirk")
    def add_radius_attribute_value_pair_username(self, username):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_USER_NAME)
        self.set_radius_attribute_value_pair_length(len(username) + 2, index)
        self.set_radius_attribute_value_pair_data(username, index)

    # example: packet.add_radius_attribute_value_pair_reply_message("00-19-06-EA-B8-8c")
    def add_radius_attribute_value_pair_called_station_id(self, station_id):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_CALLED_STATION_ID)
        self.set_radius_attribute_value_pair_length(len(station_id) + 2, index)
        self.set_radius_attribute_value_pair_data(station_id, index)

    # ########### hex string types
    # example: packet.add_radius_attribute_value_pair_framed_ip_address("FF FF FF FE")
    def add_radius_attribute_value_pair_framed_ip_address(self, ip):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_FRAMED_IP_ADDRESS)
        self.set_radius_attribute_value_pair_length(6, index)
        self.set_radius_attribute_value_pair_data(ip, index)

    # example: packet.add_radius_attribute_value_pair_eap_message("010100160410266b0e9a58322f4d01ab25b35f879464")
    def add_radius_attribute_value_pair_eap_message(self, reply_message):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_EAP_MESSAGE)
        self.set_radius_attribute_value_pair_length((len(reply_message.replace(" ", "")) / 2) + 2, index)
        self.set_radius_attribute_value_pair_data(reply_message, index)

    # example: packet.add_radius_attribute_value_pair_eap_message("11b5043c8a288758173133a5e07434cf")
    def add_radius_attribute_value_pair_message_authenticator(self, reply_message):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_MESSAGE_AUTHENTICATOR)
        self.set_radius_attribute_value_pair_length((len(reply_message.replace(" ", "")) / 2) + 2, index)
        self.set_radius_attribute_value_pair_data(reply_message, index)

    # example: packet.add_radius_attribute_value_pair_state("c6d195032fdc3024077313b231ef1d77")
    def add_radius_attribute_value_pair_state(self, reply_message):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_STATE)
        self.set_radius_attribute_value_pair_length((len(reply_message) / 2) + 2, index)
        self.set_radius_attribute_value_pair_data(reply_message, index)

    # ########### IP Address types
    # example: packet.add_radius_attribute_value_nas_ip_address("10.0.0.1")
    def add_radius_attribute_value_nas_ip_address(self, reply_message):
        ip = Ipv4Address(reply_message)
        reply_message = ip.to_formated_string(16, "")
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_NAS_IP_ADDRESS)
        self.set_radius_attribute_value_pair_length(6, index)
        self.set_radius_attribute_value_pair_data(reply_message, index)

    # ########### Integer types
    # example: packet.add_radius_attribute_value_pair_framed_mtu(576)
    def add_radius_attribute_value_pair_framed_mtu(self, mtu):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_FRAMED_MTU)
        self.set_radius_attribute_value_pair_length(6, index)
        self.set_radius_attribute_value_pair_data(hex(NumberUtils.to_integer_value(mtu)), index)

    # example: packet.add_radius_attribute_value_pair_service_type(2)
    def add_radius_attribute_value_pair_service_type(self, mtu):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_NAS_SERVICE_TYPE)
        self.set_radius_attribute_value_pair_length(6, index)
        self.set_radius_attribute_value_pair_data(hex(NumberUtils.to_integer_value(2)), index)

    # example: packet.add_radius_attribute_value_pair_nas_port(50012)
    def add_radius_attribute_value_pair_nas_port(self, mtu):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_NAS_PORT)
        self.set_radius_attribute_value_pair_length(6, index)
        self.set_radius_attribute_value_pair_data(hex(NumberUtils.to_integer_value(2)), index)

    # example: packet.add_radius_attribute_value_pair_nas_port_type(15)
    def add_radius_attribute_value_pair_nas_port_type(self, mtu):
        index = self.add_radius_attribute_value_pair(RadiusPacketConstants.AVP_NAS_PORT_TYPE)
        self.set_radius_attribute_value_pair_length(6, index)
        self.set_radius_attribute_value_pair_data(hex(NumberUtils.to_integer_value(2)), index)

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("code", RadiusPacketConstants.get_type_string(self.get_radius_code()) + " - " +
                            self.format_int(self.get_radius_code(), 2))
        table.add_row_value("id", self.format_int(self.get_radius_id(), 2))
        table.add_row_value("length", self.format_int(self.get_radius_length(), 4))
        table.add_row_value("authenticator", self.get_radius_authenticator())
        ret_string = "\n\nRADIUS HEADER" + table.to_table_string()
        ret_string2 = "\nAttribute Value Pairs" + self.to_packet_string_tags()
        return ret_string + ret_string2

    def to_packet_string_tags(self):
        table = TableFormatter()
        num_args = NumberUtils.to_integer_value(self.get_radius_attribute_value_pairs_num())
        index = 1
        while index <= num_args:
            table.add_row_value("Index", self.format_int(index, 1))
            table.add_row_value("Type", RadiusPacketConstants.get_type_string(
                                self.get_radius_attribute_value_pair_type(index)) + " - " +
                                self.format_int(self.get_radius_attribute_value_pair_type(index), 1))
            table.add_row_value("Length", self.format_int(self.get_radius_attribute_value_pair_length(index), 1))
            if self.is_field_set(self.get_radius_attribute_value_pair_data(index)):
                table.add_row_value("Data", self.get_radius_attribute_value_pair_data(index))
            else:
                table.add_row_value("Data", "n/a")
            index += 1
        return table.to_table_string()

    def add_radius_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_RADIUS)

    def build(self):
        self.add_radius_header()
        self.set_source_port(1812, True)
        self.set_destination_port(1813, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_radius_code_hltapi_cmd(dummy_dict)
        # self.get_radius_id_hltapi_cmd(dummy_dict)
        # self.get_radius_length_hltapi_cmd(dummy_dict)
        # self.get_radius_authenticator_hltapi_cmd(dummy_dict)
        # self.get_radius_attribute_value_pair_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_radius(self, tgen_type, generator_ref, port_string, stream_id,
                                                          **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_radius(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jet_stream_radius(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_radius(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = RadiusPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData

    def config_jets_stream_radius(self, jets_dev, port_string, stream_id, **kwargs):
        # this is not supported yet
        # do it with rawdata instead
        pkt_bytes = "0x" + RadiusPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_radius_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        # ### put some IxTclHal info here.
        payload = RadiusPacketHeader.get_header_bytes(self)
        payload = StringUtils.place_character_every_n_characters(payload.replace(" ", ""), " ", 2)
        dummy_dict.append("stream config -patternType                        nonRepeat")
        dummy_dict.append("stream config -dataPattern                        userpattern")
        dummy_dict.append("stream config -pattern                            \"" + payload + "\"")
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_radius_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def configure_radius_length(self, length):
        index = 1
        radius_length = RadiusPacketHeader.RADIUS_PACKET_HEADER_LENGTH
        while index <= self.get_radius_attribute_value_pairs_num():
            radius_length += self.get_radius_attribute_value_pair_length(index)
            index += 1

        self.set_radius_length(radius_length)

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        code = self.get_bits_from_string(8, payload)
        self.set_radius_code("0x" + code)
        payload = self.remove_bits_from_string(8, payload)
        pkt_id = self.get_bits_from_string(8, payload)
        self.set_radius_id("0x" + pkt_id)
        payload = self.remove_bits_from_string(8, payload)
        length = self.get_bits_from_string(16, payload)
        self.set_radius_length("0x" + length)
        payload = self.remove_bits_from_string(16, payload)
        authenticator = self.get_bits_from_string(128, payload)
        self.set_radius_authenticator("0x" + authenticator)
        payload = self.remove_bits_from_string(128, payload)
        avp_length = int(length, 16) - RadiusPacketHeader.RADIUS_PACKET_HEADER_LENGTH
        index = 0
        while avp_length > 0 and payload != "":
            index += 1
            inner_avp_type = self.get_bits_from_string(8, payload)
            self.set_radius_attribute_value_pair_type("0x" + inner_avp_type, index)
            payload = self.remove_bits_from_string(8, payload)
            inner_avp_length = self.get_bits_from_string(8, payload)
            self.set_radius_attribute_value_pair_length("0x" + inner_avp_length, index)
            payload = self.remove_bits_from_string(8, payload)
            inner_avp_length = int(inner_avp_length, 16)
            inner_avp_data = self.get_bits_from_string(8 * (inner_avp_length - 2), payload)
            self.set_radius_attribute_value_pair_data(inner_avp_data, index)
            payload = self.remove_bits_from_string(8 * (inner_avp_length - 2), payload)
            avp_length -= inner_avp_length
        self.set_radius_attribute_value_pairs_num(index)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_radius_code(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_radius_id(), PacketConstants.INTEGER, 8)
        # might have to check if the length is set first and then set it based on the AVP + 20
        ret_string += self.format_byte_string(self.get_radius_length(), PacketConstants.INTEGER, 16)
        ret_string += self.get_radius_authenticator().replace("0x", "")

        index = 1
        while index <= self.get_radius_attribute_value_pairs_num():
            message = self.get_radius_attribute_value_pair_in_hex_string(index)
            ret_string += message
            index += 1
        return ret_string

    @staticmethod
    def compare_radius_packet_header(expected, actual, ignore_list, include_list, dynamic_entries, print_results=True,
                                     print_failures=True):
        results = True
        try:
            assert isinstance(expected, RadiusPacketHeader)
            assert isinstance(actual, RadiusPacketHeader)
            if expected.is_field_set(expected.get_radius_code()) and \
                    RadiusPacketConstants.RADIUS_CODE not in ignore_list:
                name = "RADIUS code : "
                if expected.get_radius_code() != actual.get_radius_code():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_radius_code()) + " != " +
                                                      str(actual.get_radius_code()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_radius_code()) + " == " +
                                                 str(actual.get_radius_code()) + " Pass")

            if expected.is_field_set(expected.get_radius_id()) and \
                    RadiusPacketConstants.RADIUS_ID not in ignore_list:
                name = "RADIUS id : "
                if expected.get_radius_id() != actual.get_radius_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_radius_id()) + " != " +
                                                      str(actual.get_radius_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_radius_id()) + " == " +
                                                 str(actual.get_radius_id()) + " Pass")

            if expected.is_field_set(expected.get_radius_length()) and \
                    RadiusPacketConstants.RADIUS_LENGTH not in ignore_list:
                name = "RADIUS length : "
                if expected.get_radius_length() != actual.get_radius_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_radius_length()) + " != " +
                                                      str(actual.get_radius_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_radius_length()) + " == " +
                                                 str(actual.get_radius_length()) + " Pass")

            if expected.is_field_set(expected.get_radius_authenticator()) and \
                    RadiusPacketConstants.RADIUS_AUTHENTICATOR not in ignore_list:
                name = "RADIUS authenticator : "
                if "0x" + expected.get_radius_authenticator().upper() != actual.get_radius_authenticator():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_radius_authenticator()) + " != " +
                                                      str(actual.get_radius_authenticator()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_radius_authenticator()) + " == " +
                                                 str(actual.get_radius_authenticator()) + " Pass")

            if dynamic_entries:
                dynamic_results = dynamic_entries.compare_packet_fields(expected, actual)
                if not dynamic_results:
                    PacketObject.logger.log_error("Dynamic Ordering error ERROR")
                    PacketObject.logger.log_error(dynamic_entries)
                    PacketObject.logger.log_error("Expected:" + expected.to_packet_string_tags())
                    PacketObject.logger.log_error("Received:" + actual.to_packet_string_tags())
                else:
                    PacketObject.logger.log_info("Dynamic Ordering Pass")
                    PacketObject.logger.log_info(dynamic_entries)
                    PacketObject.logger.log_info("Expected:" + expected.to_packet_string_tags())
                    PacketObject.logger.log_info("Received:" + actual.to_packet_string_tags())
                results &= dynamic_results

            else:
                name = "RADIUS Attribute Pairs: "
                if expected.do_i_check_this_field(expected.get_radius_attribute_value_pairs_num(),
                                                  RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_NUM,
                                                  ignore_list, include_list):
                    if str(expected.get_radius_attribute_value_pairs_num()) != \
                            str(actual.get_radius_attribute_value_pairs_num()):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(name + str(expected.get_radius_attribute_value_pairs_num()) +
                                                          " != " + str(actual.get_radius_attribute_value_pairs_num()) +
                                                          " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_radius_attribute_value_pairs_num()) +
                                                     " == " + str(actual.get_radius_attribute_value_pairs_num()) +
                                                     " Pass")
                num_vlans = min(expected.get_radius_attribute_value_pairs_num(),
                                actual.get_radius_attribute_value_pairs_num())
                index = 0
                while index < num_vlans:
                    index += 1
                    results &= expected.compare_tags(expected, actual, index, index, ignore_list, include_list,
                                                     print_results, print_failures)

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with RadiusPacketHeader")
        return results

    @staticmethod
    def compare_tags(expected, actual, expected_index, actual_index, ignore_list=None, include_list=None,
                     print_results=True, print_failures=True):
        results = True
        wasSomethingChecked = False
        if expected.do_i_check_this_field(expected.get_radius_attribute_value_pair_type(expected_index),
                                          RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_TYPE + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "Radius Attribute Value Pair Type " + str(expected_index) + ": "
            if expected.get_radius_attribute_value_pair_type(expected_index) != \
                    actual.get_radius_attribute_value_pair_type(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name +
                                                  str(expected.get_radius_attribute_value_pair_type(expected_index)) +
                                                  " != " +
                                                  str(actual.get_radius_attribute_value_pair_type(actual_index)) +
                                                  " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_radius_attribute_value_pair_type(expected_index)) +
                                                 " == " +
                                                 str(actual.get_radius_attribute_value_pair_type(actual_index)) +
                                                 " Pass")

        if expected.do_i_check_this_field(expected.get_radius_attribute_value_pair_length(expected_index),
                                          RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_LENGTH + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "Radius Attribute Value Pair Length " + str(expected_index) + ": "
            if expected.get_radius_attribute_value_pair_length(expected_index) != \
                    actual.get_radius_attribute_value_pair_length(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name +
                                                  str(expected.get_radius_attribute_value_pair_length(expected_index)) +
                                                  " != " +
                                                  str(actual.get_radius_attribute_value_pair_length(actual_index)) +
                                                  " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_radius_attribute_value_pair_length(expected_index)) +
                                                 " == " +
                                                 str(actual.get_radius_attribute_value_pair_length(actual_index)) +
                                                 " Pass")

        if expected.do_i_check_this_field(expected.get_radius_attribute_value_pair_data_hex(expected_index),
                                          RadiusPacketConstants.RADIUS_ATTRIBUTE_VALUE_PAIR_DATA + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "Radius Attribute Value Pair Data " + str(expected_index) + ": "
            if expected.get_radius_attribute_value_pair_data_hex(expected_index).strip() != \
                    actual.get_radius_attribute_value_pair_data_hex(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(
                        name + str(expected.get_radius_attribute_value_pair_data_hex(expected_index)) + " != " +
                        str(actual.get_radius_attribute_value_pair_data_hex(actual_index)) + " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_radius_attribute_value_pair_data_hex(expected_index)) + " == " +
                        str(actual.get_radius_attribute_value_pair_data_hex(actual_index)) + " Pass")

        return results


class RadiusPacketConstants:
    def __init__(self):
        pass

    RADIUS_CODE = "RADIUS_CODE"
    RADIUS_ID = "RADIUS_ID"
    RADIUS_LENGTH = "RADIUS_LENGTH"
    RADIUS_AUTHENTICATOR = "RADIUS_AUTHENTICATOR"

    RADIUS_ATTRIBUTE_VALUE_PAIR = "RADIUS_ATTRIBUTE_VALUE_PAIR"
    RADIUS_ATTRIBUTE_VALUE_PAIR_NUM = "RADIUS_ATTRIBUTE_VALUE_PAIR_NUM"
    RADIUS_ATTRIBUTE_VALUE_PAIR_TYPE = "RADIUS_ATTRIBUTE_VALUE_PAIR_TYPE"
    RADIUS_ATTRIBUTE_VALUE_PAIR_LENGTH = "RADIUS_ATTRIBUTE_VALUE_PAIR_LENGTH"
    RADIUS_ATTRIBUTE_VALUE_PAIR_DATA = "RADIUS_ATTRIBUTE_VALUE_PAIR_DATA"

    RADIUS_STATE_ACCESS_REQUEST = 1
    RADIUS_STATE_ACCESS_REQUEST_DISPLAY = "Access Request"
    RADIUS_STATE_ACCESS_ACCEPT = 2
    RADIUS_STATE_ACCESS_ACCEPT_DISPLAY = "Access Accept"
    RADIUS_STATE_ACCESS_REJECT = 3
    RADIUS_STATE_ACCESS_REJECT_DISPLAY = "Access Reject"
    RADIUS_STATE_ACCOUNTING_REQUEST = 4
    RADIUS_STATE_ACCOUNTING_REQUEST_DISPLAY = "Accounting Request"
    RADIUS_STATE_ACCOUNTING_RESPONSE = 5
    RADIUS_STATE_ACCOUNTING_RESPONSE_DISPLAY = "Accounting Response"
    RADIUS_STATE_ACCESS_CHALLENGE = 11
    RADIUS_STATE_ACCESS_CHALLENGE_DISPLAY = "Access Challenge"
    RADIUS_STATE_STATUS_SERVER = 12
    RADIUS_STATE_STATUS_SERVER_DISPLAY = "Status Server"
    RADIUS_STATE_STATUS_CLIENT = 13
    RADIUS_STATE_STATUS_CLIENT_DISPLAY = "Statuc Client"
    RADIUS_STATE_RESERVED = 255
    RADIUS_STATE_RESERVED_DISPLAY = "Reserved"
    AVP_STATE_VALUES = [RADIUS_STATE_ACCESS_REQUEST, RADIUS_STATE_ACCESS_ACCEPT, RADIUS_STATE_ACCESS_REJECT,
                        RADIUS_STATE_ACCOUNTING_REQUEST, RADIUS_STATE_ACCOUNTING_RESPONSE,
                        RADIUS_STATE_ACCESS_CHALLENGE, RADIUS_STATE_STATUS_SERVER, RADIUS_STATE_STATUS_CLIENT,
                        RADIUS_STATE_RESERVED]
    AVP_STATE_DISPLAY_VALUES = [RADIUS_STATE_ACCESS_REQUEST_DISPLAY, RADIUS_STATE_ACCESS_ACCEPT_DISPLAY,
                                RADIUS_STATE_ACCESS_REJECT_DISPLAY, RADIUS_STATE_ACCOUNTING_REQUEST_DISPLAY,
                                RADIUS_STATE_ACCOUNTING_RESPONSE_DISPLAY, RADIUS_STATE_ACCESS_CHALLENGE_DISPLAY,
                                RADIUS_STATE_STATUS_SERVER_DISPLAY, RADIUS_STATE_STATUS_CLIENT_DISPLAY,
                                RADIUS_STATE_RESERVED_DISPLAY]

    AVP_USER_NAME = 1
    AVP_USER_NAME_DISPLAY = "User-Name"
    AVP_USER_PASSWORD = 2
    AVP_USER_PASSWORD_DISPLAY = "User-Password"
    AVP_CHAP_PASSWORD = 3
    AVP_CHAP_PASSWORD_DISPLAY = "CHAP-Password"
    AVP_NAS_IP_ADDRESS = 4
    AVP_NAS_IP_ADDRESS_DISPLAY = "NAS-IP-Address"
    AVP_NAS_PORT = 5
    AVP_NAS_PORT_DISPLAY = "NAS-Port"
    AVP_NAS_SERVICE_TYPE = 6
    AVP_NAS_SERVICE_TYPE_DISPLAY = "Service-Type"
    AVP_FRAMED_PROTOCOL = 7
    AVP_FRAMED_PROTOCOL_DISPLAY = "Framed-Protocol"
    AVP_FRAMED_IP_ADDRESS = 8
    AVP_FRAMED_IP_ADDRESS_DISPLAY = "Framed-IP-Address"
    AVP_FRAMED_IP_NETMASK = 9
    AVP_FRAMED_IP_NETMASK_DISPLAY = "Framed-IP-Netmask"
    AVP_FRAMED_ROUTING = 10
    AVP_FRAMED_ROUTING_DISPLAY = "Framed-Routing"
    AVP_FILTER_ID = 11
    AVP_FILTER_ID_DISPLAY = "Filter-Id"
    AVP_FRAMED_MTU = 12
    AVP_FRAMED_MTU_DISPLAY = "Framed-MTU"
    AVP_FRAMED_COMPRESSION = 13
    AVP_FRAMED_COMPRESSION_DISPLAY = "Framed-Compression"
    AVP_LOGIN_IP_HOST = 14
    AVP_LOGIN_IP_HOST_DISPLAY = "Login-IP-Host"
    AVP_LOGIN_IP_SERVICE = 15
    AVP_LOGIN_IP_SERVICE_DISPLAY = "Login-IP-Service"
    AVP_LOGIN_TCP_PORT = 16
    AVP_LOGIN_TCP_PORT_DISPLAY = "Login-TCP-Port"
    AVP_REPLY_MESSAGE = 18
    AVP_REPLY_MESSAGE_DISPLAY = "Reply-Message"
    AVP_CALLBACK_NUMBER = 19
    AVP_CALLBACK_NUMBER_DISPLAY = "Callback-Number"
    AVP_CALLBACK_ID = 20
    AVP_CALLBACK_ID_DISPLAY = "Callback-Id"
    AVP_FRAMED_ROUTE = 22
    AVP_FRAMED_ROUTE_DISPLAY = "Framed-Route"
    AVP_FRAMED_IPX_NETWORK = 23
    AVP_IPX_NETWORK_DISPLAY = "Framed-IPX-Network"
    AVP_STATE = 24
    AVP_STATE_DISPLAY = "State"
    AVP_CLASS = 25
    AVP_CLASS_DISPLAY = "Class"
    AVP_VENDOR_SPECIFIC = 26
    AVP_VENDOR_SPECIFIC_DISPLAY = "Vendor-Specific"
    AVP_SESSION_TIMEOUT = 27
    AVP_SESSION_TIMEOUT_DISPLAY = "Session-Timeout"
    AVP_IDLE_TIMEOUT = 28
    AVP_IDLE_TIMEOUT_DISPLAY = "Idle-Timeout"
    AVP_TERMINATION_ACTION = 29
    AVP_TERMINATION_ACTION_DISPLAY = "Termination-Action"
    AVP_CALLED_STATION_ID = 30
    AVP_CALLED_STATION_ID_DISPLAY = "Called-Station-Id"
    AVP_CALLING_STATION_ID = 31
    AVP_CALLING_STATION_ID_DISPLAY = "Calling-Station-Id"
    AVP_NAS_IDENTIFIER = 32
    AVP_NAS_IDENTIFIER_DISPLAY = "NAS-Identifier"
    AVP_PROXY_STATE = 33
    AVP_PROXY_STATE_DISPLAY = "Proxy-State"
    AVP_LOGIN_LAT_SERVICE = 34
    AVP_LOGIN_LAT_SERVICE_DISPLAY = "Login-LAT-Service"
    AVP_LOGIN_LAT_NODE = 35
    AVP_LOGIN_LAT_NODE_DISPLAY = "Login-LAT-Node"
    AVP_LOGIN_LAT_GROUP = 36
    AVP_LOGIN_LAT_GROUP_DISPLAY = "Login-LAT-Group"
    AVP_FRAMED_APPLETALK_LINK = 37
    AVP_FRAMED_APPLETALK_LINK_DISPLAY = "Framed-AppleTalk-Link"
    AVP_FRAMED_APPLETALK_NETWORK = 38
    AVP_FRAMED_APPLETALK_NETWORK_DISPLAY = "Framed-AppleTalk-Network"
    AVP_FRAMED_APPLETALK_ZONE = 39
    AVP_FRAMED_APPLETALK_ZONE_DISPLAY = "Framed-AppleTalk-Zone"
    AVP_ACCT_STATUS_TYPE = 40
    AVP_ACCT_STATUS_TYPE_DISPLAY = "Acct-Status-Type "
    AVP_ACCT_DELAY_TIME = 41
    AVP_ACCT_DELAY_TIME_DISPLAY = "Acct-Delay-Time"
    AVP_ACCT_INPUT_OCTETS = 42
    AVP_ACCT_INPUT_OCTETS_DISPLAY = "Acct-Input-Octets"
    AVP_ACCT_OUTPUT_OCTETS = 43
    AVP_ACCT_OUTPUT_OCTETS_DISPLAY = "Acct-Output-Octets"
    AVP_ACCT_SESSION_ID = 44
    AVP_ACCT_SESSION_ID_DISPLAY = "Acct-Session-Id"
    AVP_ACCT_AUTHENTIC = 45
    AVP_ACCT_AUTHENTIC_DISPLAY = "Acct-Authentic"
    AVP_ACCT_SESSION_TIME = 46
    AVP_ACCT_SESSION_TIME_DISPLAY = "Acct-Session-Time"
    AVP_ACCT_INPUT_PACKETS = 47
    AVP_ACCT_INPUT_PACKETS_DISPLAY = "Acct-Input-Packets"
    AVP_ACCT_OUTPUT_PACKETS = 48
    AVP_ACCT_OUTPUT_PACKETS_DISPLAY = "Acct-Output-Packets"
    AVP_ACCT_TERMINATE_CAUSE = 49
    AVP_ACCT_TERMINATE_CAUSE_DISPLAY = "Acct-Terminate-Cause"
    AVP_ACCT_MULTI_SESSION_ID = 50
    AVP_ACCT_MULTI_SESSION_ID_DISPLAY = "Acct-Multi-Session-Id"
    AVP_ACCT_LINK_COUNT = 51
    AVP_ACCT_LINK_COUNT_DISPLAY = "Acct-Link-Count"
    AVP_CHAP_CHALLENGE = 60
    AVP_CHAP_CHALLENGE_DISPLAY = "CHAP-Challenge"
    AVP_NAS_PORT_TYPE = 61
    AVP_NAS_PORT_TYPE_DISPLAY = "NAS-Port-Type"
    AVP_ARAP_SECURITY = 73
    AVP_ARAP_SECURITY_DISPLAY = "ARAP-Security"
    AVP_ARAP_SECURITY_DATA = 74
    AVP_ARAP_SECURITY_DATA_DISPLAY = "ARAP-Security-Data"
    AVP_PASSWORD_RETRY = 75
    AVP_PASSWORD_RETRY_DISPLAY = "Password-Retry"
    AVP_PROMPT = 76
    AVP_PROMPT_DISPLAY = "Prompt"
    AVP_CONNECT_INFO = 77
    AVP_CONNECT_INFO_DISPLAY = "Connect-Info"
    AVP_CONFIGURATION_TOKEN = 78
    AVP_CONFIGURATION_TOKEN_DISPLAY = "Configuration-Token"
    AVP_EAP_MESSAGE = 79
    AVP_EAP_MESSAGE_DISPLAY = "EAP-Message"
    AVP_MESSAGE_AUTHENTICATOR = 80
    AVP_MESSAGE_AUTHENTICATOR_DISPLAY = "Message-Authenticator"
    AVP_ARAP_CHALLENGE_RESPONSE = 84
    AVP_ARAP_CHALLENGE_RESPONSE_DISPLAY = "ARAP-Challenge-Response"
    AVP_ACCT_INTERIM_INTERVAL = 85
    AVP_ACCT_INTERIM_INTERVAL_DISPLAY = "Acct-Interim-Interval"
    AVP_NAS_PORT_ID = 87
    AVP_NAS_PORT_ID_DISPLAY = "NAS-Port-Id"
    AVP_FRAMED_POOL = 88
    AVP_FRAMED_POOL_DISPLAY = "Framed-Pool"
    AVP_UNUSED = 89
    AVP_UNUSED_DISPLAY = "Unused"
    AVP_NAS_IPV6_ADDRESS = 95
    AVP_NAS_IPV6_ADDRESS_DISPLAY = "NAS-IPv6-Address"

    AVP_VALUES = [AVP_USER_NAME, AVP_USER_PASSWORD, AVP_CHAP_PASSWORD, AVP_NAS_IP_ADDRESS, AVP_NAS_PORT,
                  AVP_NAS_SERVICE_TYPE, AVP_FRAMED_PROTOCOL, AVP_FRAMED_IP_ADDRESS, AVP_FRAMED_IP_NETMASK,
                  AVP_FRAMED_ROUTING, AVP_FILTER_ID, AVP_FRAMED_MTU, AVP_FRAMED_COMPRESSION, AVP_LOGIN_IP_HOST,
                  AVP_LOGIN_IP_SERVICE, AVP_LOGIN_TCP_PORT, AVP_REPLY_MESSAGE, AVP_CALLBACK_NUMBER, AVP_CALLBACK_ID,
                  AVP_FRAMED_ROUTE, AVP_FRAMED_IPX_NETWORK, AVP_STATE, AVP_CLASS, AVP_VENDOR_SPECIFIC,
                  AVP_SESSION_TIMEOUT, AVP_IDLE_TIMEOUT, AVP_TERMINATION_ACTION, AVP_CALLED_STATION_ID,
                  AVP_CALLING_STATION_ID, AVP_NAS_IDENTIFIER, AVP_PROXY_STATE, AVP_LOGIN_LAT_SERVICE,
                  AVP_LOGIN_LAT_NODE, AVP_LOGIN_LAT_GROUP, AVP_FRAMED_APPLETALK_LINK, AVP_FRAMED_APPLETALK_NETWORK,
                  AVP_FRAMED_APPLETALK_ZONE, AVP_ACCT_STATUS_TYPE, AVP_ACCT_DELAY_TIME, AVP_ACCT_INPUT_OCTETS,
                  AVP_ACCT_OUTPUT_OCTETS, AVP_ACCT_SESSION_ID, AVP_ACCT_AUTHENTIC, AVP_ACCT_SESSION_TIME,
                  AVP_ACCT_INPUT_PACKETS, AVP_ACCT_OUTPUT_PACKETS, AVP_ACCT_TERMINATE_CAUSE, AVP_ACCT_MULTI_SESSION_ID,
                  AVP_ACCT_LINK_COUNT, AVP_CHAP_CHALLENGE, AVP_NAS_PORT_TYPE, AVP_ARAP_SECURITY,
                  AVP_ARAP_SECURITY_DATA, AVP_PASSWORD_RETRY, AVP_PROMPT, AVP_CONNECT_INFO, AVP_CONFIGURATION_TOKEN,
                  AVP_EAP_MESSAGE, AVP_MESSAGE_AUTHENTICATOR, AVP_ARAP_CHALLENGE_RESPONSE, AVP_ACCT_INTERIM_INTERVAL,
                  AVP_NAS_PORT_ID, AVP_FRAMED_POOL, AVP_UNUSED, AVP_NAS_IPV6_ADDRESS]

    AVP_DISPLAY_VALUES = [AVP_USER_NAME_DISPLAY, AVP_USER_PASSWORD_DISPLAY, AVP_CHAP_PASSWORD_DISPLAY,
                          AVP_NAS_IP_ADDRESS_DISPLAY, AVP_NAS_PORT_DISPLAY, AVP_NAS_SERVICE_TYPE_DISPLAY,
                          AVP_FRAMED_PROTOCOL_DISPLAY, AVP_FRAMED_IP_ADDRESS_DISPLAY, AVP_FRAMED_IP_NETMASK_DISPLAY,
                          AVP_FRAMED_ROUTING_DISPLAY, AVP_FILTER_ID_DISPLAY, AVP_FRAMED_MTU_DISPLAY,
                          AVP_FRAMED_COMPRESSION_DISPLAY, AVP_LOGIN_IP_HOST_DISPLAY, AVP_LOGIN_IP_SERVICE_DISPLAY,
                          AVP_LOGIN_TCP_PORT_DISPLAY, AVP_REPLY_MESSAGE_DISPLAY, AVP_CALLBACK_NUMBER_DISPLAY,
                          AVP_CALLBACK_ID_DISPLAY, AVP_FRAMED_ROUTE_DISPLAY, AVP_IPX_NETWORK_DISPLAY, AVP_STATE_DISPLAY,
                          AVP_CLASS_DISPLAY, AVP_VENDOR_SPECIFIC_DISPLAY, AVP_SESSION_TIMEOUT_DISPLAY,
                          AVP_IDLE_TIMEOUT_DISPLAY, AVP_TERMINATION_ACTION_DISPLAY, AVP_CALLED_STATION_ID_DISPLAY,
                          AVP_CALLING_STATION_ID_DISPLAY, AVP_NAS_IDENTIFIER_DISPLAY, AVP_PROXY_STATE_DISPLAY,
                          AVP_LOGIN_LAT_SERVICE_DISPLAY, AVP_LOGIN_LAT_NODE_DISPLAY, AVP_LOGIN_LAT_GROUP_DISPLAY,
                          AVP_FRAMED_APPLETALK_LINK_DISPLAY, AVP_FRAMED_APPLETALK_NETWORK_DISPLAY,
                          AVP_FRAMED_APPLETALK_ZONE_DISPLAY, AVP_ACCT_STATUS_TYPE_DISPLAY, AVP_ACCT_DELAY_TIME_DISPLAY,
                          AVP_ACCT_INPUT_OCTETS_DISPLAY, AVP_ACCT_OUTPUT_OCTETS_DISPLAY, AVP_ACCT_SESSION_ID_DISPLAY,
                          AVP_ACCT_AUTHENTIC_DISPLAY, AVP_ACCT_SESSION_TIME_DISPLAY, AVP_ACCT_INPUT_PACKETS_DISPLAY,
                          AVP_ACCT_OUTPUT_PACKETS_DISPLAY, AVP_ACCT_TERMINATE_CAUSE_DISPLAY,
                          AVP_ACCT_MULTI_SESSION_ID_DISPLAY, AVP_ACCT_LINK_COUNT_DISPLAY, AVP_CHAP_CHALLENGE_DISPLAY,
                          AVP_NAS_PORT_TYPE_DISPLAY, AVP_ARAP_SECURITY_DISPLAY, AVP_ARAP_SECURITY_DATA_DISPLAY,
                          AVP_PASSWORD_RETRY_DISPLAY, AVP_PROMPT_DISPLAY, AVP_CONNECT_INFO_DISPLAY,
                          AVP_CONFIGURATION_TOKEN_DISPLAY, AVP_EAP_MESSAGE_DISPLAY, AVP_MESSAGE_AUTHENTICATOR_DISPLAY,
                          AVP_ARAP_CHALLENGE_RESPONSE_DISPLAY, AVP_ACCT_INTERIM_INTERVAL_DISPLAY,
                          AVP_NAS_PORT_ID_DISPLAY, AVP_FRAMED_POOL_DISPLAY, AVP_UNUSED_DISPLAY,
                          AVP_NAS_IPV6_ADDRESS_DISPLAY]

    @staticmethod
    def get_type_string(pkt_type):
        index = 0
        while index < len(RadiusPacketConstants.AVP_VALUES):
            if RadiusPacketConstants.AVP_VALUES[index] == pkt_type:
                return RadiusPacketConstants.AVP_DISPLAY_VALUES[index]
            index += 1
        return "unknown" + str(pkt_type)

    @staticmethod
    def get_code_string(code):
        index = 0
        while index < len(RadiusPacketConstants.AVP_STATE_VALUES):
            index += 1
            if RadiusPacketConstants.AVP_STATE_VALUES[index] == code:
                return RadiusPacketConstants.AVP_STATE_DISPLAY_VALUES[index]
        return "unknown" + code

    """
    1       User-Name
    2       User-Password
    3       CHAP-Password
    4       NAS-IP-Address
    5       NAS-Port
    6       Service-Type
    7       Framed-Protocol
    8       Framed-IP-Address
    9       Framed-IP-Netmask
    10      Framed-Routing
    11      Filter-Id
    12      Framed-MTU
    13      Framed-Compression
    14      Login-IP-Host
    15      Login-Service
    16      Login-TCP-Port
    17      (unassigned)
    18      Reply-Message
    19      Callback-Number
    20      Callback-Id
    21      (unassigned)
    22      Framed-Route
    23      Framed-IPX-Network
    24      State
    25      Class
    26      Vendor-Specific
    27      Session-Timeout
    28      Idle-Timeout
    29      Termination-Action
    30      Called-Station-Id
    31      Calling-Station-Id
    32      NAS-Identifier
    33      Proxy-State
    34      Login-LAT-Service
    35      Login-LAT-Node
    36      Login-LAT-Group
    37      Framed-AppleTalk-Link
    38      Framed-AppleTalk-Network
    39      Framed-AppleTalk-Zone
    40      Acct-Status-Type
    40-59   (reserved for accounting)
    60      CHAP-Challenge
    61      NAS-Port-Type
    62      Port-Limit
    63      Login-LAT-Port
    73      ARAP-Security
    74      ARAP-Security-Data
    75      Password-Retry
    76      Prompt
    77      Connect-Info
    78      Configuration-Token
    79      EAP-Message
    80      Message-Authenticator
    81-83   (refer to [6])
    84      ARAP-Challenge-Response
    85      Acct-Interim-Interval
    86      (refer to [7])
    87      NAS-Port-Id
    88      Framed-Pool
    89      Unused
    90-91   (refer to [6])
    92-191  Unused
    """

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

    @staticmethod
    def convert_mesage_to_hex(pkt_type, length, message):
        if isinstance(message, list):
            return ''.join(hex(i)[2:].zfill(2) for i in message)
        if message.startswith("0x") and len(message) > 2:
            message = message[2:]
        hexaPattern = re.compile(r'^([0-9a-fA-F]+)$')
        hexaPatternSpace = re.compile(r'^([0-9a-fA-F][0-9a-fA-F] )*([0-9a-fA-F][0-9a-fA-F])$')
        if re.search(hexaPattern, message):
            message = message.upper()
        elif re.search(hexaPatternSpace, message):
            message = message.replace(" ", "").upper()
        elif Ipv4Address.is_valid_ipv4(message):  # this is an ipaddress
            ip = Ipv4Address(message)
            message = ip.to_formated_string(16, "").encode('hex').upper()
            message = message.replace(" ", "")
        elif EnetAddress.is_valid_enet(message):  # this is an ipaddress
            ip = EnetAddress(message)
            message = ip.to_formated_string(16, "").encode('hex').upper()
            message = message.replace(" ", "")
        # elif type == LldpPacketConstants.LLDP_TLV_TYPE_PORT_DESCRIPTION or
        #     type == LldpPacketConstants.LLDP_TLV_TYPE_SYSTEM_DESCRIPTION or
        #     type == LldpPacketConstants.LLDP_TLV_TYPE_SYSTEM_NAME :
        #     message = " " + message.encode('hex')
        else:
            message = " " + message.encode('hex').upper()
        while (length - 2) > (len(message) / 2):
            message = "0" + message
        return message.upper()


class RadiusPacketHeaderDynamicFieldLogic(PacketHeaderDynamicFieldLogic):

    def compare_dynamic_fields(self, expected, actual, index, index_actual_vlans, print_results=False,
                               print_failures=False):
        assert isinstance(expected, RadiusPacketHeader)
        return expected.compare_tags(expected, actual, index, index_actual_vlans, None, None, print_results,
                                     print_failures)

    def get_compare_number(self, expected):
        assert isinstance(expected, RadiusPacketHeader)
        return expected.get_radius_attribute_value_pairs_num()
