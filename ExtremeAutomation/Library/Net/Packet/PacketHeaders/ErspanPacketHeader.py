import binascii
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.GrePacketHeader import GrePacketConstants
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class ErspanPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    ERSPAN Packet Header
        # version = 4bits
        # VLAN = 12bits
        # COS = 3bits
        # En = 2bits
        # T = 1bits
        # Session ID = 10bits
        # Reserved = 12bits
        # Index = 20bits
    """

    def __init__(self):
        self.add_erspan_header()
        self.HEADER_SIZE_ERSPAN = 10  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Erspan version methods
    #  version is a 4 bit INTEGER example: 1
    def set_erspan_version(self, version, ignore_check=False):
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPAN,
                                  ErspanPacketConstants.ERSPAN_VERSION, version)

    def get_erspan_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_VERSION), PacketConstants.INTEGER)

    def get_erspan_version_hltapi_cmd(self, dummy_dict):
        version = self.get_erspan_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end Erspan version methods

    # start Erspan VLAN methods
    #  vlan is a 12 bit INTEGER example: 1
    def set_erspan_vlan(self, vlan, ignore_check=False):
        vlan = self.normalize_value(vlan, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_VLAN, vlan)

    def get_erspan_vlan(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_VLAN), PacketConstants.INTEGER)

    def get_erspan_vlan_hltapi_cmd(self, dummy_dict):
        vlan = self.get_erspan_vlan()
        if isinstance(vlan, int):
            vlan = str(vlan)
        if vlan and 'Not Set' not in vlan:
            dummy_dict[TrafficConfigConstants.TEMP_VLAN_CMD] = vlan
    # end Erspan VLAN methods

    # start Erspan COS methods
    #  cos is a 3 bit INTEGER example: 1
    def set_erspan_cos(self, cos, ignore_check=False):
        cos = self.normalize_value(cos, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_COS, cos)

    def get_erspan_cos(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_COS), PacketConstants.INTEGER)

    def get_erspan_cos_hltapi_cmd(self, dummy_dict):
        cos = self.get_erspan_cos()
        if isinstance(cos, int):
            cos = str(cos)
        if cos and 'Not Set' not in cos:
            dummy_dict[TrafficConfigConstants.TEMP_COS_CMD] = cos
    # end Erspan COS methods

    # start Erspan En methods
    #  en is a 2 bit INTEGER example: 1
    def set_erspan_en(self, en, ignore_check=False):
        en = self.normalize_value(en, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_EN, en)

    def get_erspan_en(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_EN), PacketConstants.INTEGER)

    def get_erspan_en_hltapi_cmd(self, dummy_dict):
        en = self.get_erspan_en()
        if isinstance(en, int):
            en = str(en)
        if en and 'Not Set' not in en:
            dummy_dict[TrafficConfigConstants.TEMP_EN_CMD] = en
    # end Erspan En methods

    # start Erspan T methods
    #  t is a 1 bit INTEGER example: 1
    def set_erspan_t(self, t, ignore_check=False):
        t = self.normalize_value(t, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_T, t)

    def get_erspan_t(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_T), PacketConstants.INTEGER)

    def get_erspan_t_hltapi_cmd(self, dummy_dict):
        t = self.get_erspan_t()
        if isinstance(t, int):
            t = str(t)
        if t and 'Not Set' not in t:
            dummy_dict[TrafficConfigConstants.TEMP_T_CMD] = t
    # end Erspan T methods

    # start Erspan Session ID methods
    #  session_id is a 10 bit INTEGER example: 1
    def set_erspan_session_id(self, session_id, ignore_check=False):
        session_id = self.normalize_value(session_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_SESSION_ID,
                                  session_id)

    def get_erspan_session_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_SESSION_ID), PacketConstants.INTEGER)

    def get_erspan_session_id_hltapi_cmd(self, dummy_dict):
        session_id = self.get_erspan_session_id()
        if isinstance(session_id, int):
            session_id = str(session_id)
        if session_id and 'Not Set' not in session_id:
            dummy_dict[TrafficConfigConstants.TEMP_SESSION_ID_CMD] = session_id
    # end Erspan Session ID methods

    # start Erspan Reserved methods
    #  reserved is a 12 bit INTEGER example: 1
    def set_erspan_reserved(self, reserved, ignore_check=False):
        reserved = self.normalize_value(reserved, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_RESERVED,
                                  reserved)

    def get_erspan_reserved(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_RESERVED), PacketConstants.INTEGER)

    def get_erspan_reserved_hltapi_cmd(self, dummy_dict):
        reserved = self.get_erspan_reserved()
        if isinstance(reserved, int):
            reserved = str(reserved)
        if reserved and 'Not Set' not in reserved:
            dummy_dict[TrafficConfigConstants.TEMP_RESERVED_CMD] = reserved
    # end Erspan Reserved methods

    # start Erspan Index methods
    #  index is a 20 bit INTEGER example: 1
    def set_erspan_index(self, index, ignore_check=False):
        index = self.normalize_value(index, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_INDEX, index)

    def get_erspan_index(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPAN, ErspanPacketConstants.ERSPAN_INDEX), PacketConstants.INTEGER)

    def get_erspan_index_hltapi_cmd(self, dummy_dict):
        index = self.get_erspan_index()
        if isinstance(index, int):
            index = str(index)
        if index and 'Not Set' not in index:
            dummy_dict[TrafficConfigConstants.TEMP_INDEX_CMD] = index
    # end Erspan Index methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("version", self.format_int(self.get_erspan_version(), 1))
        table.add_row_value("VLAN", self.format_int(self.get_erspan_vlan(), 3))
        table.add_row_value("COS", self.format_int(self.get_erspan_cos(), 0))
        table.add_row_value("En", self.format_int(self.get_erspan_en(), 0))
        table.add_row_value("T", self.format_int(self.get_erspan_t(), 0))
        table.add_row_value("Session ID", self.format_int(self.get_erspan_session_id(), 2))
        table.add_row_value("Reserved", self.format_int(self.get_erspan_reserved(), 3))
        table.add_row_value("Index", self.format_int(self.get_erspan_index(), 5))
        ret_string = "\n\nERSPAN HEADER" + table.to_table_string()
        ret_string += "\n\nInner Packet\n" + self.get_gre_inner_packet().to_packet_string()
        return ret_string

    def add_erspan_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_ERSPAN)

    def build(self):
        self.add_erspan_header()
        self.set_gre_protocol_type(GrePacketConstants.GRE_PROTOCOL_ESPAN_II, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_erspan_version_hltapi_cmd(dummy_dict)
        # self.get_erspan_vlan_hltapi_cmd(dummy_dict)
        # self.get_erspan_cos_hltapi_cmd(dummy_dict)
        # self.get_erspan_en_hltapi_cmd(dummy_dict)
        # self.get_erspan_t_hltapi_cmd(dummy_dict)
        # self.get_erspan_session_id_hltapi_cmd(dummy_dict)
        # self.get_erspan_reserved_hltapi_cmd(dummy_dict)
        # self.get_erspan_index_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_erspan(self, tgen_type, generator_ref, port_string, stream_id,
                                                          **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_erspan(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jet_stream_erspan(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_erspan(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
    # update this from the ostinato docs.
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = ErspanPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData
        p.Extensions[hexDump].pad_until_end = False

    def config_jet_stream_erspan(self, jets_dev, port_string, stream_id, **kwargs):
        # this is not supported yet
        # do it with rawdata instead
        pkt_bytes = "0x" + ErspanPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_erspan_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
    # ### put some IxTclHal info here.
        payload = ErspanPacketHeader.get_header_bytes(self)
        payload = StringUtils.place_character_every_n_characters(payload.replace(" ", ""), " ", 2)
        dummy_dict.append("stream config -patternType                        nonRepeat")
        dummy_dict.append("stream config -dataPattern                        userpattern")
        dummy_dict.append("stream config -pattern                            \"" + payload + "\"")
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        version = self.get_bits_from_string(4, payload)
        self.set_erspan_version("0x" + version)
        payload = self.remove_bits_from_string(4, payload)
        vlan = self.get_bits_from_string(12, payload)
        self.set_erspan_vlan("0x" + vlan)
        payload = self.remove_bits_from_string(12, payload)

        # start read 16 bits and parse out the values.
        val = self.get_bits_from_string(16, payload)
        payload = self.remove_bits_from_string(16, payload)

        cos = self.get_bits_from_string_with_positions(val, 15, 3)
        self.set_erspan_cos(cos)
        en = self.get_bits_from_string_with_positions(val, 12, 2)
        self.set_erspan_en(en)
        t = self.get_bits_from_string_with_positions(val, 11, 1)
        self.set_erspan_t(t)
        session_id = self.get_bits_from_string_with_positions(val, 10, 10)
        self.set_erspan_en(session_id)
        # end read 16 bits and parse out the values.

        reserved = self.get_bits_from_string(12, payload)
        self.set_erspan_reserved("0x" + reserved)
        payload = self.remove_bits_from_string(12, payload)
        index = self.get_bits_from_string(20, payload)
        self.set_erspan_index("0x" + index)
        payload = self.remove_bits_from_string(20, payload)
        packet = EthernetPacket()
        packet.set_payload(payload)
        self.set_gre_inner_packet(packet)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_erspan_version(), PacketConstants.INTEGER, 4)
        ret_string += self.format_byte_string(self.get_erspan_vlan(), PacketConstants.INTEGER, 12)

        # start read 16 bits and parse out the values.
        val = 0
        val = self.shift_bits_from_string_with_positions(val, 15, 3, self.get_erspan_cos())
        val = self.shift_bits_from_string_with_positions(val, 12, 2, self.get_erspan_en())
        val = self.shift_bits_from_string_with_positions(val, 11, 1, self.get_erspan_t())
        val = self.shift_bits_from_string_with_positions(val, 10, 10, self.get_erspan_session_id())
        ret_string += self.format_byte_string(val, PacketConstants.INTEGER, 16)
        # end read 16 bits and parse out the values.

        ret_string += self.format_byte_string(self.get_erspan_reserved(), PacketConstants.INTEGER, 12)
        ret_string += self.format_byte_string(self.get_erspan_index(), PacketConstants.INTEGER, 20)
        ret_string += self.get_gre_inner_packet().get_bytes()
        return ret_string

    @staticmethod
    def compare_erspan_packet_header(expected, actual, ignore_list=None, include_list=None, dynamic_entries=None,
                                     print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, ErspanPacketHeader)
            assert isinstance(actual, ErspanPacketHeader)
            if expected.do_i_check_this_field(expected.get_erspan_version(), ignore_list, include_list):
                name = "ERSPAN version : "
                if expected.get_erspan_version() != actual.get_erspan_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspan_version()) + " != " +
                                                      str(actual.get_erspan_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspan_version()) + " == " +
                                                 str(actual.get_erspan_version()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspan_vlan(), ignore_list, include_list):
                name = "ERSPAN vlan : "
                if expected.get_erspan_vlan() != actual.get_erspan_vlan():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspan_vlan()) + " != " +
                                                      str(actual.get_erspan_vlan()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspan_vlan()) + " == " +
                                                 str(actual.get_erspan_vlan()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspan_cos(), ignore_list, include_list):
                name = "ERSPAN cos : "
                if expected.get_erspan_cos() != actual.get_erspan_cos():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspan_cos()) + " != " +
                                                      str(actual.get_erspan_cos()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspan_cos()) + " == " +
                                                 str(actual.get_erspan_cos()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspan_en(), ignore_list, include_list):
                name = "ERSPAN en : "
                if expected.get_erspan_en() != actual.get_erspan_en():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspan_en()) + " != " +
                                                      str(actual.get_erspan_en()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspan_en()) + " == " +
                                                 str(actual.get_erspan_en()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspan_t(), ignore_list, include_list):
                name = "ERSPAN t : "
                if expected.get_erspan_t() != actual.get_erspan_t():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspan_t()) + " != " +
                                                      str(actual.get_erspan_t()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspan_t()) + " == " +
                                                 str(actual.get_erspan_t()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspan_session_id(), ignore_list, include_list):
                name = "ERSPAN session id : "
                if expected.get_erspan_session_id() != actual.get_erspan_session_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspan_session_id()) + " != " +
                                                      str(actual.get_erspan_session_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspan_session_id()) + " == " +
                                                 str(actual.get_erspan_session_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspan_reserved(), ignore_list, include_list):
                name = "ERSPAN reserved : "
                if expected.get_erspan_reserved() != actual.get_erspan_reserved():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspan_reserved()) + " != " +
                                                      str(actual.get_erspan_reserved()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspan_reserved()) + " == " +
                                                 str(actual.get_erspan_reserved()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspan_index(), ignore_list, include_list):
                name = "ERSPAN index : "
                if expected.get_erspan_index() != actual.get_erspan_index():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspan_index()) + " != " +
                                                      str(actual.get_erspan_index()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspan_index()) + " == " +
                                                 str(actual.get_erspan_index()) + " Pass")
            if expected.do_i_check_this_field(expected.get_gre_inner_packet(),
                                              ErspanPacketConstants.GRE_INNER_PACKET, ignore_list, include_list):
                name = "GRE Inner packet : "
                expected_inner = expected.get_inner_packet()
                actual_inner = actual.get_inner_packet()
                results_print = PacketConstants.PRINT_FLAG_NONE
                if print_results:
                    results_print = PacketConstants.PRINT_FLAG_EVERYTHING
                elif print_failures:
                    results_print = PacketConstants.PRINT_FLAG_ERRORS
                if not expected_inner.compare_packet_fields(actual_inner, False, ignore_list, include_list,
                                                            dynamic_entries, results_print):
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error("Inner Packet ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + "Inner Packet Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with ErspanPacketHeader")
        return results


class ErspanPacketConstants:
    def __init__(self):
        pass

    ERSPAN_VERSION = "ERSPAN_VERSION"
    ERSPAN_VLAN = "ERSPAN_VLAN"
    ERSPAN_COS = "ERSPAN_COS"
    ERSPAN_EN = "ERSPAN_EN"
    ERSPAN_T = "ERSPAN_T"
    ERSPAN_SESSION_ID = "ERSPAN_SESSION_ID"
    ERSPAN_RESERVED = "ERSPAN_RESERVED"
    ERSPAN_INDEX = "ERSPAN_INDEX"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
