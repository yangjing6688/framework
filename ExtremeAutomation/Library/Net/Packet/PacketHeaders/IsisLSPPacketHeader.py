from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisPacketHeader import IsisTlvEntry
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb


class IsisLSPPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    ISIS LS Packet Header
        # pdu_length = 16bits
        # remaining_life = 16bits
        # lsp_id = 64bits
        # sequence_number = 32bits
        # checksum = 16bits
    """

    def __init__(self):
        self.add_lsp_header()
        self.tlv_entries = []
        self.HEADER_SIZE_LSP = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start LSP pdu_length methods
    #  pdu_length is a 16 bit INTEGER example: 1
    def set_lsp_pdu_length(self, pdu_length, ignore_check=False):
        pdu_length = self.normalize_value(pdu_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_LSP,
                                  LSPPacketConstants.LSP_PDU_LENGTH, pdu_length)

    def get_lsp_pdu_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_LSP, LSPPacketConstants.LSP_PDU_LENGTH), PacketConstants.INTEGER)

    def get_lsp_pdu_length_hltapi_cmd(self, dummy_dict):
        pdu_length = self.get_lsp_pdu_length()
        if isinstance(pdu_length, int):
            pdu_length = str(pdu_length)
        if pdu_length and 'Not Set' not in pdu_length:
            dummy_dict[TrafficConfigConstants.TEMP_PDU_LENGTH_CMD] = pdu_length
    # end LSP pdu_length methods

    # start LSP remaining_life methods
    #  remaining_life is a 16 bit INTEGER example: 1
    def set_lsp_remaining_life(self, remaining_life, ignore_check=False):
        remaining_life = self.normalize_value(remaining_life, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_LSP,
                                  LSPPacketConstants.LSP_REMAINING_LIFE, remaining_life)

    def get_lsp_remaining_life(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_LSP, LSPPacketConstants.LSP_REMAINING_LIFE), PacketConstants.INTEGER)

    def get_lsp_remaining_life_hltapi_cmd(self, dummy_dict):
        remaining_life = self.get_lsp_remaining_life()
        if isinstance(remaining_life, int):
            remaining_life = str(remaining_life)
        if remaining_life and 'Not Set' not in remaining_life:
            dummy_dict[TrafficConfigConstants.TEMP_REMAINING_LIFE_CMD] = remaining_life
    # end LSP remaining_life methods

    # start LSP lsp_id methods
    #  lsp_id is a 64 bit INTEGER example: 1
    def set_lsp_lsp_id(self, lsp_id, ignore_check=False):
        lsp_id = self.normalize_value(lsp_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_LSP, LSPPacketConstants.LSP_LSP_ID, lsp_id)

    def get_lsp_lsp_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_LSP, LSPPacketConstants.LSP_LSP_ID), PacketConstants.INTEGER)

    def get_lsp_lsp_id_hltapi_cmd(self, dummy_dict):
        lsp_id = self.get_lsp_lsp_id()
        if isinstance(lsp_id, int):
            lsp_id = str(lsp_id)
        if lsp_id and 'Not Set' not in lsp_id:
            dummy_dict[TrafficConfigConstants.TEMP_LSP_ID_CMD] = lsp_id
    # end LSP lsp_id methods

    # start LSP sequence_number methods
    #  sequence_number is a 32 bit INTEGER example: 1
    def set_lsp_sequence_number(self, sequence_number, ignore_check=False):
        sequence_number = self.normalize_value(sequence_number, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_LSP,
                                  LSPPacketConstants.LSP_SEQUENCE_NUMBER, sequence_number)

    def get_lsp_sequence_number(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_LSP, LSPPacketConstants.LSP_SEQUENCE_NUMBER), PacketConstants.INTEGER)

    def get_lsp_sequence_number_hltapi_cmd(self, dummy_dict):
        sequence_number = self.get_lsp_sequence_number()
        if isinstance(sequence_number, int):
            sequence_number = str(sequence_number)
        if sequence_number and 'Not Set' not in sequence_number:
            dummy_dict[TrafficConfigConstants.TEMP_SEQUENCE_NUMBER_CMD] = sequence_number
    # end LSP sequence_number methods

    # start LSP checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_lsp_checksum(self, checksum, ignore_check=False):
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_LSP, LSPPacketConstants.LSP_CHECKSUM, checksum)

    def get_lsp_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_LSP, LSPPacketConstants.LSP_CHECKSUM), PacketConstants.INTEGER)

    def get_lsp_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_lsp_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end LSP checksum methods

    # start LSP flags methods
    #  flags is a 8 bit INTEGER example: 1
    def set_lsp_flags(self, flags, ignore_check=False):
        flags = self.normalize_value(flags, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_LSP, LSPPacketConstants.LSP_FLAGS, flags)

    def get_lsp_flags(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_LSP, LSPPacketConstants.LSP_FLAGS), PacketConstants.INTEGER)

    def get_lsp_flags_hltapi_cmd(self, dummy_dict):
        flags = self.get_lsp_flags()
        if isinstance(flags, int):
            flags = str(flags)
        if flags and 'Not Set' not in flags:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = flags
    # end LSP flags methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("pdu_length", self.format_int(self.get_lsp_pdu_length(), 4))
        table.add_row_value("remaining_life", self.format_int(self.get_lsp_remaining_life(), 4))
        table.add_row_value("lsp_id", self.format_int(self.get_lsp_lsp_id(), 16))
        table.add_row_value("sequence_number", self.format_int(self.get_lsp_sequence_number(), 8))
        table.add_row_value("checksum", self.format_int(self.get_lsp_checksum(), 4))
        table.add_row_value("flags", self.format_int(self.get_lsp_flags(), 2))

        table_tlv = IsisTlvEntry.to_packet_string(self)

        return "\n\nLSP HEADER" + table.to_table_string() + "\n\nLSP TLV ENTRIES" + table_tlv.to_table_string()

    def add_lsp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_LSP)

    def build(self):
        self.add_lsp_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_lsp_pdu_length_hltapi_cmd(dummy_dict)
        # self.get_lsp_remaining_life_hltapi_cmd(dummy_dict)
        # self.get_lsp_lsp_id_hltapi_cmd(dummy_dict)
        # self.get_lsp_sequence_number_hltapi_cmd(dummy_dict)
        # self.get_lsp_checksum_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_lsp(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_lsp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_lsp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_lsp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.klspFieldNumber
    # update this from the ostinato docs.
    #     lspField = p.Extensions[lsp]
    #     if self.is_field_set(self.get_lsp_pdu_length()):
    #         lspField.version = int(self.get_lsp_pdu_length())
    #     if self.is_field_set(self.get_lsp_remaining_life()):
    #         lspField.version = int(self.get_lsp_remaining_life())
    #     if self.is_field_set(self.get_lsp_lsp_id()):
    #         lspField.version = int(self.get_lsp_lsp_id())
    #     if self.is_field_set(self.get_lsp_sequence_number()):
    #         lspField.version = int(self.get_lsp_sequence_number())
    #     if self.is_field_set(self.get_lsp_checksum()):
    #         lspField.version = int(self.get_lsp_checksum())

    def config_jets_stream_lsp(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "LSP_HDR"
        pkt_bytes = "0x" + IsisLSPPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_lsp_pdu_length()):
            pkt_fields["pdu_length"] = int(self.get_lsp_pdu_length())
        if self.is_field_set(self.get_lsp_remaining_life()):
            pkt_fields["remaining_life"] = int(self.get_lsp_remaining_life())
        if self.is_field_set(self.get_lsp_lsp_id()):
            pkt_fields["lsp_id"] = int(self.get_lsp_lsp_id())
        if self.is_field_set(self.get_lsp_sequence_number()):
            pkt_fields["sequence_number"] = int(self.get_lsp_sequence_number())
        if self.is_field_set(self.get_lsp_checksum()):
            pkt_fields["checksum"] = int(self.get_lsp_checksum())

    def get_ixtclhal_lsp_api_commands(self, port_string, streamid):
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
        self.tlv_entries = []
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        pdu_length = self.get_bits_from_string(16, payload)
        self.set_lsp_pdu_length("0x" + pdu_length)
        payload = self.remove_bits_from_string(16, payload)
        remaining_life = self.get_bits_from_string(16, payload)
        self.set_lsp_remaining_life("0x" + remaining_life)
        payload = self.remove_bits_from_string(16, payload)
        lsp_id = self.get_bits_from_string(64, payload)
        self.set_lsp_lsp_id("0x" + lsp_id)
        payload = self.remove_bits_from_string(64, payload)
        sequence_number = self.get_bits_from_string(32, payload)
        self.set_lsp_sequence_number("0x" + sequence_number)
        payload = self.remove_bits_from_string(32, payload)
        checksum = self.get_bits_from_string(16, payload)
        self.set_lsp_checksum("0x" + checksum)
        payload = self.remove_bits_from_string(16, payload)

        flags = self.get_bits_from_string(8, payload)
        self.set_lsp_flags("0x" + flags)
        payload = self.remove_bits_from_string(8, payload)

        # processTLVs
        self.payload = IsisTlvEntry.process_tlv(payload, self.tlv_entries, pdu_length, self)

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_lsp_pdu_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_lsp_remaining_life(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_lsp_lsp_id(), PacketConstants.INTEGER, 64)
        ret_string += self.format_byte_string(self.get_lsp_sequence_number(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_lsp_checksum(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_lsp_flags(), PacketConstants.INTEGER, 8)
        for entry in self.tlv_entries:
            ret_string += self.format_byte_string(entry.type, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.length, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.data, PacketConstants.HEX_STRING, entry.length * 8)
        return ret_string

    @staticmethod
    def compare_lsp_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, IsisLSPPacketHeader)
            assert isinstance(actual, IsisLSPPacketHeader)
            if expected.is_field_set(expected.get_lsp_pdu_length()) and \
                    LSPPacketConstants.LSP_PDU_LENGTH not in ignore_list:
                name = "LSP pdu_length : "
                if expected.get_lsp_pdu_length() != actual.get_lsp_pdu_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_lsp_pdu_length()) + " != " +
                                                      str(actual.get_lsp_pdu_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_lsp_pdu_length()) + " == " +
                                                 str(actual.get_lsp_pdu_length()) + " Pass")

            if expected.is_field_set(expected.get_lsp_remaining_life()) and \
                    LSPPacketConstants.LSP_REMAINING_LIFE not in ignore_list:
                name = "LSP remaining_life : "
                if expected.get_lsp_remaining_life() != actual.get_lsp_remaining_life():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_lsp_remaining_life()) + " != " +
                                                      str(actual.get_lsp_remaining_life()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_lsp_remaining_life()) + " == " +
                                                 str(actual.get_lsp_remaining_life()) + " Pass")

            if expected.is_field_set(expected.get_lsp_lsp_id()) and \
                    LSPPacketConstants.LSP_LSP_ID not in ignore_list:
                name = "LSP lsp_id : "
                if expected.get_lsp_lsp_id() != actual.get_lsp_lsp_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_lsp_lsp_id()) + " != " +
                                                      str(actual.get_lsp_lsp_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_lsp_lsp_id()) + " == " +
                                                 str(actual.get_lsp_lsp_id()) + " Pass")

            if expected.is_field_set(expected.get_lsp_sequence_number()) and \
                    LSPPacketConstants.LSP_SEQUENCE_NUMBER not in ignore_list:
                name = "LSP sequence_number : "
                if expected.get_lsp_sequence_number() != actual.get_lsp_sequence_number():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_lsp_sequence_number()) + " != " +
                                                      str(actual.get_lsp_sequence_number()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_lsp_sequence_number()) + " == " +
                                                 str(actual.get_lsp_sequence_number()) + " Pass")

            if expected.is_field_set(expected.get_lsp_checksum()) and \
                    LSPPacketConstants.LSP_CHECKSUM not in ignore_list:
                name = "LSP checksum : "
                if expected.get_lsp_checksum() != actual.get_lsp_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_lsp_checksum()) + " != " +
                                                      str(actual.get_lsp_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_lsp_checksum()) + " == " +
                                                 str(actual.get_lsp_checksum()) + " Pass")

            if expected.is_field_set(expected.get_lsp_checksum()) and \
                    LSPPacketConstants.LSP_FLAGS not in ignore_list:
                name = "LSP flags : "
                if expected.get_lsp_flags() != actual.get_lsp_flags():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_lsp_flags()) + " != " +
                                                      str(actual.get_lsp_flags()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_lsp_flags()) + " == " +
                                                 str(actual.get_lsp_flags()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with LSPPacketHeader")
        return results


class LSPPacketConstants:
    def __init__(self):
        pass

    LSP_PDU_LENGTH = "LSP_PDU_LENGTH"
    LSP_REMAINING_LIFE = "LSP_REMAINING_LIFE"
    LSP_LSP_ID = "LSP_LSP_ID"
    LSP_SEQUENCE_NUMBER = "LSP_SEQUENCE_NUMBER"
    LSP_CHECKSUM = "LSP_CHECKSUM"
    LSP_FLAGS = "LSP_FLAGS"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
