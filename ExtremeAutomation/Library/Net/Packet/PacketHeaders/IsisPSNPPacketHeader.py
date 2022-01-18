from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisPacketHeader import IsisTlvEntry
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb


class IsisPSNPPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    ISIS PSNP Packet Header
        # pdu_length = 16bits
        # source_id = 56bits
        # start_lsp_id = 64bits
        # end_lsp_id = 64bits
    """

    def __init__(self):
        self.add_snp_header()
        self.tlv_entries = []
        self.HEADER_SIZE_SNP = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start SNP pdu_length methods
    #  pdu_length is a 16 bit INTEGER example: 1
    def set_snp_pdu_length(self, pdu_length, ignore_check=False):
        pdu_length = self.normalize_value(pdu_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_SNP, SNPPacketConstants.SNP_PDU_LENGTH,
                                  pdu_length)

    def get_snp_pdu_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_SNP, SNPPacketConstants.SNP_PDU_LENGTH), PacketConstants.INTEGER)

    def get_snp_pdu_length_hltapi_cmd(self, dummy_dict):
        pdu_length = self.get_snp_pdu_length()
        if isinstance(pdu_length, int):
            pdu_length = str(pdu_length)
        if pdu_length and 'Not Set' not in pdu_length:
            dummy_dict[TrafficConfigConstants.TEMP_PDU_LENGTH_CMD] = pdu_length
    # end SNP pdu_length methods

    # start SNP source_id methods
    #  source_id is a 56 bit HEX_STRING example: FFFFFFFFFFFFFF
    def set_snp_source_id(self, source_id, ignore_check=False):
        source_id = self.normalize_value(source_id, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_SNP, SNPPacketConstants.SNP_SOURCE_ID,
                                  source_id)

    def get_snp_source_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_SNP, SNPPacketConstants.SNP_SOURCE_ID), PacketConstants.HEX_STRING)

    def get_snp_source_id_hltapi_cmd(self, dummy_dict):
        source_id = self.get_snp_source_id()
        if source_id and 'Not Set' not in source_id:
            dummy_dict[TrafficConfigConstants.TEMP_SOURCE_ID_CMD] = source_id
    # end SNP source_id methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("pdu_length", self.format_int(self.get_snp_pdu_length(), 4))
        table.add_row_value("source_id", self.get_snp_source_id())

        table_tlv = IsisTlvEntry.to_packet_string(self)

        return "\n\nSNP HEADER" + table.to_table_string() + "\n\nSNP TLV ENTRIES" + table_tlv.to_table_string()

    def add_snp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_SNP)

    def build(self):
        self.add_snp_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_snp_pdu_length_hltapi_cmd(dummy_dict)
        # self.get_snp_source_id_hltapi_cmd(dummy_dict)
        # self.get_snp_start_lsp_id_hltapi_cmd(dummy_dict)
        # self.get_snp_end_lsp_id_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_snp(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_snp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_snp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_snp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.ksnpFieldNumber
    # update this from the ostinato docs.
    #     snpField = p.Extensions[snp]
    #     if self.is_field_set(self.get_snp_pdu_length()):
    #         snpField.version = int(self.get_snp_pdu_length())
    #     if self.is_field_set(self.get_snp_source_id()):
    #         snpField.version = int(self.get_snp_source_id())

    def config_jets_stream_snp(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "SNP_HDR"
        pkt_bytes = "0x" + IsisPSNPPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_snp_pdu_length()):
            pkt_fields["pdu_length"] = int(self.get_snp_pdu_length())
        if self.is_field_set(self.get_snp_source_id()):
            pkt_fields["source_id"] = int(self.get_snp_source_id())

    def get_ixtclhal_snp_api_commands(self, port_string, streamid):
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
        self.set_snp_pdu_length("0x" + pdu_length)
        payload = self.remove_bits_from_string(16, payload)
        source_id = self.get_bits_from_string(56, payload)
        self.set_snp_source_id("0x" + source_id)
        payload = self.remove_bits_from_string(56, payload)
        # processTLVs
        self.payload = IsisTlvEntry.process_tlv(payload, self.tlv_entries, pdu_length, self)

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_snp_pdu_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_snp_source_id(),
                                              PacketConstants.HEX_STRING, 56).replace("0x", "")
        for entry in self.tlv_entries:
            ret_string += self.format_byte_string(entry.type, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.length, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.data, PacketConstants.HEX_STRING, entry.length * 8)
        return ret_string

    @staticmethod
    def compare_snp_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, IsisPSNPPacketHeader)
            assert isinstance(actual, IsisPSNPPacketHeader)
            if expected.is_field_set(expected.get_snp_pdu_length()) and \
                    SNPPacketConstants.SNP_PDU_LENGTH not in ignore_list:
                name = "SNP pdu_length : "
                if expected.get_snp_pdu_length() != actual.get_snp_pdu_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_snp_pdu_length()) + " != " +
                                                      str(actual.get_snp_pdu_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_snp_pdu_length()) + " == " +
                                                 str(actual.get_snp_pdu_length()) + " Pass")

            if expected.is_field_set(expected.get_snp_source_id()) and \
                    SNPPacketConstants.SNP_SOURCE_ID not in ignore_list:
                name = "SNP source_id : "
                if expected.get_snp_source_id() != actual.get_snp_source_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_snp_source_id()) + " != " +
                                                      str(actual.get_snp_source_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_snp_source_id()) + " == " +
                                                 str(actual.get_snp_source_id()) + " Pass")

            if expected.is_field_set(expected.get_snp_start_lsp_id()) and \
                    SNPPacketConstants.SNP_START_LSP_ID not in ignore_list:
                name = "SNP start_lsp_id : "
                if expected.get_snp_start_lsp_id() != actual.get_snp_start_lsp_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_snp_start_lsp_id()) + " != " +
                                                      str(actual.get_snp_start_lsp_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_snp_start_lsp_id()) + " == " +
                                                 str(actual.get_snp_start_lsp_id()) + " Pass")

            if expected.is_field_set(expected.get_snp_end_lsp_id()) and \
                    SNPPacketConstants.SNP_END_LSP_ID not in ignore_list:
                name = "SNP end_lsp_id : "
                if expected.get_snp_end_lsp_id() != actual.get_snp_end_lsp_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_snp_end_lsp_id()) + " != " +
                                                      str(actual.get_snp_end_lsp_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_snp_end_lsp_id()) + " == " +
                                                 str(actual.get_snp_end_lsp_id()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with SNPPacketHeader")
        return results


class SNPPacketConstants:
    def __init__(self):
        pass

    SNP_PDU_LENGTH = "SNP_PDU_LENGTH"
    SNP_SOURCE_ID = "SNP_SOURCE_ID"
    SNP_START_LSP_ID = "SNP_START_LSP_ID"
    SNP_END_LSP_ID = "SNP_END_LSP_ID"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
