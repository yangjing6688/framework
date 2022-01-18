from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb


# https://sites.google.com/site/amitsciscozone/home/is-is/is-is-packets
class IsisPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    ISIS Packet Header
        # intradomain routing protocol discriminator = 8bits
        # length indicator = 8bits
        # version protocol id extension = 8bits
        # id length = 8bits
        # reserved = 8bits
        # pdu type = 8bits
        # version = 8bits
        # reserved 2 = 8bits
        # max area addresses = 8bits
    """

    def __init__(self):
        self.add_isis_header()
        self.HEADER_SIZE_ISIS = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Isis intradomain routing protocol discriminator methods
    #  intradomain_routing_protocol_discriminator is a 8 bit INTEGER example: 1
    def set_isis_intradomain_routing_protocol_discriminator(self, intradomain_routing_protocol_discriminator,
                                                            ignore_check=False):
        intradomain_routing_protocol_discriminator = self.normalize_value(
            intradomain_routing_protocol_discriminator, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ISIS,
                                  IsisPacketConstants.ISIS_INTRADOMAIN_ROUTING_PROTOCOL_DISCRIMINATOR,
                                  intradomain_routing_protocol_discriminator)

    def get_isis_intradomain_routing_protocol_discriminator(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_INTRADOMAIN_ROUTING_PROTOCOL_DISCRIMINATOR),
            PacketConstants.INTEGER)

    def get_isis_intradomain_routing_protocol_discriminator_hltapi_cmd(self, dummy_dict):
        intradomain_routing_protocol_discriminator = self.get_isis_intradomain_routing_protocol_discriminator()
        if isinstance(intradomain_routing_protocol_discriminator, int):
            intradomain_routing_protocol_discriminator = str(intradomain_routing_protocol_discriminator)
        if intradomain_routing_protocol_discriminator and 'Not Set' not in intradomain_routing_protocol_discriminator:
            dummy_dict[TrafficConfigConstants.TEMP_INTRADOMAIN_ROUTING_PROTOCOL_DISCRIMINATOR_CMD] = \
                intradomain_routing_protocol_discriminator
    # end Isis intradomain routing protocol discriminator methods

    # start Isis length indicator methods
    #  length_indicator is a 8 bit INTEGER example: 1
    def set_isis_length_indicator(self, length_indicator, ignore_check=False):
        length_indicator = self.normalize_value(length_indicator, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ISIS,
                                  IsisPacketConstants.ISIS_LENGTH_INDICATOR, length_indicator)

    def get_isis_length_indicator(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_LENGTH_INDICATOR), PacketConstants.INTEGER)

    def get_isis_length_indicator_hltapi_cmd(self, dummy_dict):
        length_indicator = self.get_isis_length_indicator()
        if isinstance(length_indicator, int):
            length_indicator = str(length_indicator)
        if length_indicator and 'Not Set' not in length_indicator:
            dummy_dict[TrafficConfigConstants.TEMP_LENGTH_INDICATOR_CMD] = length_indicator
    # end Isis length indicator methods

    # start Isis version protocol id extension methods
    #  version_protocol_id_extension is a 8 bit INTEGER example: 1
    def set_isis_version_protocol_id_extension(self, version_protocol_id_extension, ignore_check=False):
        version_protocol_id_extension = self.normalize_value(version_protocol_id_extension, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ISIS,
                                  IsisPacketConstants.ISIS_VERSION_PROTOCOL_ID_EXTENSION, version_protocol_id_extension)

    def get_isis_version_protocol_id_extension(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_VERSION_PROTOCOL_ID_EXTENSION),
            PacketConstants.INTEGER)

    def get_isis_version_protocol_id_extension_hltapi_cmd(self, dummy_dict):
        version_protocol_id_extension = self.get_isis_version_protocol_id_extension()
        if isinstance(version_protocol_id_extension, int):
            version_protocol_id_extension = str(version_protocol_id_extension)
        if version_protocol_id_extension and 'Not Set' not in version_protocol_id_extension:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_PROTOCOL_ID_EXTENSION_CMD] = version_protocol_id_extension
    # end Isis version protocol id extension methods

    # start Isis id length methods
    #  id_length is a 8 bit INTEGER example: 1
    def set_isis_id_length(self, id_length, ignore_check=False):
        id_length = self.normalize_value(id_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_ID_LENGTH, id_length)

    def get_isis_id_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_ID_LENGTH), PacketConstants.INTEGER)

    def get_isis_id_length_hltapi_cmd(self, dummy_dict):
        id_length = self.get_isis_id_length()
        if isinstance(id_length, int):
            id_length = str(id_length)
        if id_length and 'Not Set' not in id_length:
            dummy_dict[TrafficConfigConstants.TEMP_ID_LENGTH_CMD] = id_length
    # end Isis id length methods

    # start Isis reserved methods
    #  reserved is a 8 bit INTEGER example: 1
    def set_isis_reserved(self, reserved, ignore_check=False):
        reserved = self.normalize_value(reserved, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_RESERVED, reserved)

    def get_isis_reserved(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_RESERVED), PacketConstants.INTEGER)

    def get_isis_reserved_hltapi_cmd(self, dummy_dict):
        reserved = self.get_isis_reserved()
        if isinstance(reserved, int):
            reserved = str(reserved)
        if reserved and 'Not Set' not in reserved:
            dummy_dict[TrafficConfigConstants.TEMP_RESERVED_CMD] = reserved
    # end Isis reserved methods

    # start Isis pdu type methods
    #  pdu_type is a 8 bit INTEGER example: 1
    def set_isis_pdu_type(self, pdu_type, ignore_check=False):
        pdu_type = self.normalize_value(pdu_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_PDU_TYPE, pdu_type)

    def get_isis_pdu_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_PDU_TYPE), PacketConstants.INTEGER)

    def get_isis_pdu_type_hltapi_cmd(self, dummy_dict):
        pdu_type = self.get_isis_pdu_type()
        if isinstance(pdu_type, int):
            pdu_type = str(pdu_type)
        if pdu_type and 'Not Set' not in pdu_type:
            dummy_dict[TrafficConfigConstants.TEMP_PDU_TYPE_CMD] = pdu_type
    # end Isis pdu type methods

    # start Isis version methods
    #  version is a 8 bit INTEGER example: 1
    def set_isis_version(self, version, ignore_check=False):
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_VERSION, version)

    def get_isis_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_VERSION), PacketConstants.INTEGER)

    def get_isis_version_hltapi_cmd(self, dummy_dict):
        version = self.get_isis_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end Isis version methods

    # start Isis reserved 2 methods
    #  reserved_2 is a 8 bit INTEGER example: 1
    def set_isis_reserved_2(self, reserved_2, ignore_check=False):
        reserved_2 = self.normalize_value(reserved_2, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ISIS,
                                  IsisPacketConstants.ISIS_RESERVED_2, reserved_2)

    def get_isis_reserved_2(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_RESERVED_2), PacketConstants.INTEGER)

    def get_isis_reserved_2_hltapi_cmd(self, dummy_dict):
        reserved_2 = self.get_isis_reserved_2()
        if isinstance(reserved_2, int):
            reserved_2 = str(reserved_2)
        if reserved_2 and 'Not Set' not in reserved_2:
            dummy_dict[TrafficConfigConstants.TEMP_RESERVED_2_CMD] = reserved_2
    # end Isis reserved 2 methods

    # start Isis max area addresses methods
    #  max_area_addresses is a 8 bit INTEGER example: 1
    def set_isis_max_area_addresses(self, max_area_addresses, ignore_check=False):
        max_area_addresses = self.normalize_value(max_area_addresses, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ISIS,
                                  IsisPacketConstants.ISIS_MAX_AREA_ADDRESSES, max_area_addresses)

    def get_isis_max_area_addresses(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ISIS, IsisPacketConstants.ISIS_MAX_AREA_ADDRESSES),
            PacketConstants.INTEGER)

    def get_isis_max_area_addresses_hltapi_cmd(self, dummy_dict):
        max_area_addresses = self.get_isis_max_area_addresses()
        if isinstance(max_area_addresses, int):
            max_area_addresses = str(max_area_addresses)
        if max_area_addresses and 'Not Set' not in max_area_addresses:
            dummy_dict[TrafficConfigConstants.TEMP_MAX_AREA_ADDRESSES_CMD] = max_area_addresses
    # end Isis max area addresses methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("intradomain routing protocol discriminator",
                            self.format_int(self.get_isis_intradomain_routing_protocol_discriminator(), 2))
        table.add_row_value("length indicator", self.format_int(self.get_isis_length_indicator(), 2))
        table.add_row_value("version protocol id extension",
                            self.format_int(self.get_isis_version_protocol_id_extension(), 2))
        table.add_row_value("id length", self.format_int(self.get_isis_id_length(), 2))
        table.add_row_value("reserved", self.format_int(self.get_isis_reserved(), 2))
        table.add_row_value("pdu type", self.format_int(self.get_isis_pdu_type(), 2))
        table.add_row_value("version", self.format_int(self.get_isis_version(), 2))
        table.add_row_value("reserved 2", self.format_int(self.get_isis_reserved_2(), 2))
        table.add_row_value("max area addresses", self.format_int(self.get_isis_max_area_addresses(), 2))
        return "\n\nISIS HEADER" + table.to_table_string()

    def add_isis_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_ISIS)

    def build(self):
        self.add_isis_header()
        self.set_llc_dsap(0xFE)
        self.set_llc_ssap(0xFE)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_isis_intradomain_routing_protocol_discriminator_hltapi_cmd(dummy_dict)
        # self.get_isis_length_indicator_hltapi_cmd(dummy_dict)
        # self.get_isis_version_protocol_id_extension_hltapi_cmd(dummy_dict)
        # self.get_isis_id_length_hltapi_cmd(dummy_dict)
        # self.get_isis_reserved_hltapi_cmd(dummy_dict)
        # self.get_isis_pdu_type_hltapi_cmd(dummy_dict)
        # self.get_isis_version_hltapi_cmd(dummy_dict)
        # self.get_isis_reserved_2_hltapi_cmd(dummy_dict)
        # self.get_isis_max_area_addresses_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_isis(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_isis(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_isis(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_isis(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kisisFieldNumber
    # update this from the ostinato docs.
    #     isisField = p.Extensions[isis]
    #     if self.is_field_set(self.get_isis_intradomain_routing_protocol_discriminator()):
    #         isisField.version = int(self.get_isis_intradomain_routing_protocol_discriminator())
    #     if self.is_field_set(self.get_isis_length_indicator()):
    #         isisField.version = int(self.get_isis_length_indicator())
    #     if self.is_field_set(self.get_isis_version_protocol_id_extension()):
    #         isisField.version = int(self.get_isis_version_protocol_id_extension())
    #     if self.is_field_set(self.get_isis_id_length()):
    #         isisField.version = int(self.get_isis_id_length())
    #     if self.is_field_set(self.get_isis_reserved()):
    #         isisField.version = int(self.get_isis_reserved())
    #     if self.is_field_set(self.get_isis_pdu_type()):
    #         isisField.version = int(self.get_isis_pdu_type())
    #     if self.is_field_set(self.get_isis_version()):
    #         isisField.version = int(self.get_isis_version())
    #     if self.is_field_set(self.get_isis_reserved_2()):
    #         isisField.version = int(self.get_isis_reserved_2())
    #     if self.is_field_set(self.get_isis_max_area_addresses()):
    #         isisField.version = int(self.get_isis_max_area_addresses())

    def config_jets_stream_isis(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "ISIS_HDR"
        pkt_bytes = "0x" + IsisPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_isis_intradomain_routing_protocol_discriminator()) :
        #    pkt_fields["intradomain_routing_protocol_discriminator"] = \
        #        int(self.get_isis_intradomain_routing_protocol_discriminator())
        # if self.is_field_set(self.get_isis_length_indicator()) :
        # 	pkt_fields["length_indicator"] = int(self.get_isis_length_indicator())
        # if self.is_field_set(self.get_isis_version_protocol_id_extension()) :
        # 	pkt_fields["version_protocol_id_extension"] = int(self.get_isis_version_protocol_id_extension())
        # if self.is_field_set(self.get_isis_id_length()) :
        # 	pkt_fields["id_length"] = int(self.get_isis_id_length())
        # if self.is_field_set(self.get_isis_reserved()) :
        # 	pkt_fields["reserved"] = int(self.get_isis_reserved())
        # if self.is_field_set(self.get_isis_pdu_type()) :
        # 	pkt_fields["pdu_type"] = int(self.get_isis_pdu_type())
        # if self.is_field_set(self.get_isis_version()) :
        # 	pkt_fields["version"] = int(self.get_isis_version())
        # if self.is_field_set(self.get_isis_reserved_2()) :
        # 	pkt_fields["reserved_2"] = int(self.get_isis_reserved_2())
        # if self.is_field_set(self.get_isis_max_area_addresses()) :
        # 	pkt_fields["max_area_addresses"] = int(self.get_isis_max_area_addresses())

    def get_ixtclhal_isis_api_commands(self, port_string, streamid):
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
        intradomain_routing_protocol_discriminator = self.get_bits_from_string(8, payload)
        self.set_isis_intradomain_routing_protocol_discriminator("0x" + intradomain_routing_protocol_discriminator)
        payload = self.remove_bits_from_string(8, payload)
        length_indicator = self.get_bits_from_string(8, payload)
        self.set_isis_length_indicator("0x" + length_indicator)
        payload = self.remove_bits_from_string(8, payload)
        version_protocol_id_extension = self.get_bits_from_string(8, payload)
        self.set_isis_version_protocol_id_extension("0x" + version_protocol_id_extension)
        payload = self.remove_bits_from_string(8, payload)
        id_length = self.get_bits_from_string(8, payload)
        self.set_isis_id_length("0x" + id_length)
        payload = self.remove_bits_from_string(8, payload)

        # this is only 3 bits, but is a reserved field so ignore it
        # reserved = self.get_bits_from_string(8, payload)
        # self.set_isis_reserved("0x" + reserved)
        # payload = self.remove_bits_from_string(8, payload)

        # this is only 5 bits, but is a reserved field or it with 0x01F if there is a problem.
        pdu_type = self.get_bits_from_string(8, payload)
        self.set_isis_pdu_type("0x" + pdu_type)
        payload = self.remove_bits_from_string(8, payload)
        version = self.get_bits_from_string(8, payload)
        self.set_isis_version("0x" + version)
        payload = self.remove_bits_from_string(8, payload)
        reserved_2 = self.get_bits_from_string(8, payload)
        self.set_isis_reserved_2("0x" + reserved_2)
        payload = self.remove_bits_from_string(8, payload)
        max_area_addresses = self.get_bits_from_string(8, payload)
        self.set_isis_max_area_addresses("0x" + max_area_addresses)
        payload = self.remove_bits_from_string(8, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_isis_intradomain_routing_protocol_discriminator(),
                                              PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_isis_length_indicator(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_isis_version_protocol_id_extension(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_isis_id_length(), PacketConstants.INTEGER, 8)
        # this is only 3 bits, but is a reserved field so ignore it
        # ret_string += self.format_byte_string(self.get_isis_reserved(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_isis_pdu_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_isis_version(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_isis_reserved_2(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_isis_max_area_addresses(), PacketConstants.INTEGER, 8)
        return ret_string.replace("0x", "")

    @staticmethod
    def compare_isis_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, IsisPacketHeader)
            assert isinstance(actual, IsisPacketHeader)
            if expected.is_field_set(expected.get_isis_intradomain_routing_protocol_discriminator()) and \
                    IsisPacketConstants.ISIS_INTRADOMAIN_ROUTING_PROTOCOL_DISCRIMINATOR not in ignore_list:
                name = "ISIS intradomain routing protocol discriminator : "
                if expected.get_isis_intradomain_routing_protocol_discriminator() != \
                        actual.get_isis_intradomain_routing_protocol_discriminator():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_isis_intradomain_routing_protocol_discriminator()) + " != " +
                            str(actual.get_isis_intradomain_routing_protocol_discriminator()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_isis_intradomain_routing_protocol_discriminator()) + " == " +
                        str(actual.get_isis_intradomain_routing_protocol_discriminator()) + " Pass")

            if expected.is_field_set(expected.get_isis_length_indicator()) and \
                    IsisPacketConstants.ISIS_LENGTH_INDICATOR not in ignore_list:
                name = "ISIS length indicator : "
                if expected.get_isis_length_indicator() != actual.get_isis_length_indicator():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_isis_length_indicator()) + " != " +
                                                      str(actual.get_isis_length_indicator()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_isis_length_indicator()) + " == " +
                                                 str(actual.get_isis_length_indicator()) + " Pass")

            if expected.is_field_set(expected.get_isis_version_protocol_id_extension()) and \
                    IsisPacketConstants.ISIS_VERSION_PROTOCOL_ID_EXTENSION not in ignore_list:
                name = "ISIS version protocol id extension : "
                if expected.get_isis_version_protocol_id_extension() != actual.get_isis_version_protocol_id_extension():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_isis_version_protocol_id_extension()) + " != " +
                                                      str(actual.get_isis_version_protocol_id_extension()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_isis_version_protocol_id_extension()) +
                                                 " == " + str(actual.get_isis_version_protocol_id_extension()) +
                                                 " Pass")

            if expected.is_field_set(expected.get_isis_id_length()) and \
                    IsisPacketConstants.ISIS_ID_LENGTH not in ignore_list:
                name = "ISIS id length : "
                if expected.get_isis_id_length() != actual.get_isis_id_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_isis_id_length()) + " != " +
                                                      str(actual.get_isis_id_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_isis_id_length()) + " == " +
                                                 str(actual.get_isis_id_length()) + " Pass")

            if expected.is_field_set(expected.get_isis_reserved()) and \
                    IsisPacketConstants.ISIS_RESERVED not in ignore_list:
                name = "ISIS reserved : "
                if expected.get_isis_reserved() != actual.get_isis_reserved():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_isis_reserved()) + " != " +
                                                      str(actual.get_isis_reserved()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_isis_reserved()) + " == " +
                                                 str(actual.get_isis_reserved()) + " Pass")

            if expected.is_field_set(expected.get_isis_pdu_type()) and \
                    IsisPacketConstants.ISIS_PDU_TYPE not in ignore_list:
                name = "ISIS pdu type : "
                if expected.get_isis_pdu_type() != actual.get_isis_pdu_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_isis_pdu_type()) + " != " +
                                                      str(actual.get_isis_pdu_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_isis_pdu_type()) + " == " +
                                                 str(actual.get_isis_pdu_type()) + " Pass")

            if expected.is_field_set(expected.get_isis_version()) and \
                    IsisPacketConstants.ISIS_VERSION not in ignore_list:
                name = "ISIS version : "
                if expected.get_isis_version() != actual.get_isis_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_isis_version()) + " != " +
                                                      str(actual.get_isis_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_isis_version()) + " == " +
                                                 str(actual.get_isis_version()) + " Pass")

            if expected.is_field_set(expected.get_isis_reserved_2()) and \
                    IsisPacketConstants.ISIS_RESERVED_2 not in ignore_list:
                name = "ISIS reserved 2 : "
                if expected.get_isis_reserved_2() != actual.get_isis_reserved_2():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_isis_reserved_2()) + " != " +
                                                      str(actual.get_isis_reserved_2()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_isis_reserved_2()) + " == " +
                                                 str(actual.get_isis_reserved_2()) + " Pass")

            if expected.is_field_set(expected.get_isis_max_area_addresses()) and \
                    IsisPacketConstants.ISIS_MAX_AREA_ADDRESSES not in ignore_list:
                name = "ISIS max area addresses : "
                if expected.get_isis_max_area_addresses() != actual.get_isis_max_area_addresses():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_isis_max_area_addresses()) + " != " +
                                                      str(actual.get_isis_max_area_addresses()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_isis_max_area_addresses()) + " == " +
                                                 str(actual.get_isis_max_area_addresses()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_error("Error with IsisPacketHeader")
        return results


# https://www.cisco.com/c/en/us/support/docs/ip/integrated-intermediate-system-to-intermediate-system-is-is/5739-tlvs-5739.html#topic1
class IsisTlvEntry(object):
    def __init__(self, pkt_type, length, data):
        self.pkt_type = pkt_type
        self.type_string = self.get_type_string(pkt_type)
        self.length = length
        self.data = data

    def get_type_string(self, pkt_type):
        if pkt_type == 0x01:
            return "Area Address(es)"
        elif pkt_type == 2:
            return "IIS Neighbors"
        elif pkt_type == 3:
            return "ES Neighbors"
        elif pkt_type == 4:
            return "Part. DIS"
        elif pkt_type == 5:
            return "Prefix Neighbors"
        elif pkt_type == 6:
            return "IIS Neighbors"
        elif pkt_type == 8:
            return "Padding"
        elif pkt_type == 9:
            return "LSP Entries"
        elif pkt_type == 10:
            return "Authentication"
        elif pkt_type == 12:
            return "Opt. Checksum"
        elif pkt_type == 14:
            return "LSPBufferSize"
        elif pkt_type == 22:
            return "TE IIS Neighbors"
        elif pkt_type == 54:
            return "HMAC-MD5 Authentic"
        elif pkt_type == 128:
            return "IP Int. Reach"
        elif pkt_type == 129:
            return "Prot. Supported"
        elif pkt_type == 130:
            return "IP Ext. Address"
        elif pkt_type == 131:
            return "IDRPI"
        elif pkt_type == 132:
            return "IP Intf. Address"
        elif pkt_type == 133:
            return "Authentication"
        elif pkt_type == 134:
            return "TE-Router ID"
        elif pkt_type == 135:
            return "TE IP. Reach"
        elif pkt_type == 137:
            return "Dynamic Name"
        elif pkt_type == 138:
            return "Shared Risk Link Group"
        elif pkt_type == 222:
            return "MT-ISN"
        elif pkt_type == 229:
            return "M-Topologies"
        elif pkt_type == 232:
            return "IPv6 Intf. Addr."
        elif pkt_type == 235:
            return "MT IP. Reach"
        elif pkt_type == 211:
            return "Restart TLV"
        elif pkt_type == 236:
            return "IPv6 Reachability"
        elif pkt_type == 237:
            return "MT IPv6 IP Reach"
        elif pkt_type == 240:
            return "p2p 3-way Adj. or 3-Way hellos"
        else:
            return "Unknown Type"
    # https://www.iana.org/assignments/isis-tlv-codepoints/isis-tlv-codepoints.xhtml#tlv-codepoints
    # http://m1k3.s3cur1ty.de/isis/doku.php/link-state_pakete

    @staticmethod
    def process_tlv(payload, tlv_entries, pdu_length, hanlder):
        pdu_length = int(pdu_length, 16)
        try:
            while pdu_length > 0 and payload.replace("0", "").strip() != "":
                tlv_type = hanlder.get_bits_from_string(8, payload)
                tlv_type = int(tlv_type, 16)
                payload = hanlder.remove_bits_from_string(8, payload)
                pdu_length -= 1
                tlv_length = hanlder.get_bits_from_string(8, payload)
                tlv_length = int(tlv_length, 16)
                payload = hanlder.remove_bits_from_string(8, payload)
                pdu_length -= 1
                tlv_data = hanlder.get_bits_from_string(tlv_length * 8, payload)
                payload = hanlder.remove_bits_from_string(tlv_length * 8, payload)
                pdu_length -= tlv_length
                tlv_entries.append(IsisTlvEntry(tlv_type, tlv_length, tlv_data))
        except Exception as e:
            PacketObject.logger.log_info(e)
        return payload

    @staticmethod
    def to_packet_string(packet):
        table_tlv = TableFormatter()
        for entry in packet.tlv_entries:
            table_tlv.add_row_value("type", entry.type_string + " " + packet.format_int(entry.type, 1))
            table_tlv.add_row_value("length", packet.format_int(entry.length, 1))
            table_tlv.add_row_value("data", entry.data)
        return table_tlv


class IsisPacketConstants:
    def __init__(self):
        pass

    ISIS_INTRADOMAIN_ROUTING_PROTOCOL_DISCRIMINATOR = "ISIS_INTRADOMAIN_ROUTING_PROTOCOL_DISCRIMINATOR"
    ISIS_LENGTH_INDICATOR = "ISIS_LENGTH_INDICATOR"
    ISIS_VERSION_PROTOCOL_ID_EXTENSION = "ISIS_VERSION_PROTOCOL_ID_EXTENSION"
    ISIS_ID_LENGTH = "ISIS_ID_LENGTH"
    ISIS_RESERVED = "ISIS_RESERVED"
    ISIS_PDU_TYPE = "ISIS_PDU_TYPE"
    ISIS_VERSION = "ISIS_VERSION"
    ISIS_RESERVED_2 = "ISIS_RESERVED_2"
    ISIS_MAX_AREA_ADDRESSES = "ISIS_MAX_AREA_ADDRESSES"

    ISIS_PDU_TYPE_L1_HELLO = 0x0F
    ISIS_PDU_TYPE_L2_HELLO = 0x10
    ISIS_PDU_TYPE_P2P_HELLO = 0x11
    # LSP
    ISIS_PDU_TYPE_L1_ISP = 0x12
    ISIS_PDU_TYPE_L2_ISP = 0x14
    # SNP
    ISIS_PDU_TYPE_L1_CSNP = 0x18
    ISIS_PDU_TYPE_L2_CSNP = 0x19
    ISIS_PDU_TYPE_L1_PSNP = 0x1A
    ISIS_PDU_TYPE_L2_PSNP = 0x1B

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
