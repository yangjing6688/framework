from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisPacketHeader import IsisTlvEntry
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb


class IsisHelloPduPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    ISIS Hello PDU Packet Header
        # circuit_type = 8bits
        # source_id = 48bits
        # holding_timer = 16bits
        # pdu_length = 16bits
        # priority = 8bits
        # lan_id = 56bits
    """

    def __init__(self):
        self.add_hellopdu_header()
        self.tlv_entries = []
        self.HEADER_SIZE_HELLOPDU = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start HelloPdu circuit_type methods
    #  circuit_type is a 8 bit INTEGER example: 1
    def set_hellopdu_circuit_type(self, circuit_type, ignore_check=False):
        circuit_type = self.normalize_value(circuit_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU,
                                  HelloPduPacketConstants.HELLOPDU_CIRCUIT_TYPE, circuit_type)

    def get_hellopdu_circuit_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU, HelloPduPacketConstants.HELLOPDU_CIRCUIT_TYPE),
            PacketConstants.INTEGER)

    def get_hellopdu_circuit_type_hltapi_cmd(self, dummy_dict):
        circuit_type = self.get_hellopdu_circuit_type()
        if isinstance(circuit_type, int):
            circuit_type = str(circuit_type)
        if circuit_type and 'Not Set' not in circuit_type:
            dummy_dict[TrafficConfigConstants.TEMP_CIRCUIT_TYPE_CMD] = circuit_type
    # end HelloPdu circuit_type methods

    # start HelloPdu source_id methods
    #  source_id is a 48 bit HEX_STRING example: FFFFFFFFFFFF
    def set_hellopdu_source_id(self, source_id, ignore_check=False):
        source_id = self.normalize_value(source_id, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU,
                                  HelloPduPacketConstants.HELLOPDU_SOURCE_ID, source_id)

    def get_hellopdu_source_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU, HelloPduPacketConstants.HELLOPDU_SOURCE_ID),
            PacketConstants.HEX_STRING)

    def get_hellopdu_source_id_hltapi_cmd(self, dummy_dict):
        source_id = self.get_hellopdu_source_id()
        if source_id and 'Not Set' not in source_id:
            dummy_dict[TrafficConfigConstants.TEMP_SOURCE_ID_CMD] = source_id
    # end HelloPdu source_id methods

    # start HelloPdu holding_timer methods
    #  holding_timer is a 16 bit HEX_STRING example: FFFF
    def set_hellopdu_holding_timer(self, holding_timer, ignore_check=False):
        holding_timer = self.normalize_value(holding_timer, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU,
                                  HelloPduPacketConstants.HELLOPDU_HOLDING_TIMER, holding_timer)

    def get_hellopdu_holding_timer(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU, HelloPduPacketConstants.HELLOPDU_HOLDING_TIMER),
            PacketConstants.HEX_STRING)

    def get_hellopdu_holding_timer_hltapi_cmd(self, dummy_dict):
        holding_timer = self.get_hellopdu_holding_timer()
        if holding_timer and 'Not Set' not in holding_timer:
            dummy_dict[TrafficConfigConstants.TEMP_HOLDING_TIMER_CMD] = holding_timer
    # end HelloPdu holding_timer methods

    # start HelloPdu pdu_length methods
    #  pdu_length is a 16 bit HEX_STRING example: FFFF
    def set_hellopdu_pdu_length(self, pdu_length, ignore_check=False):
        pdu_length = self.normalize_value(pdu_length, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU,
                                  HelloPduPacketConstants.HELLOPDU_PDU_LENGTH, pdu_length)

    def get_hellopdu_pdu_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU, HelloPduPacketConstants.HELLOPDU_PDU_LENGTH),
            PacketConstants.HEX_STRING)

    def get_hellopdu_pdu_length_hltapi_cmd(self, dummy_dict):
        pdu_length = self.get_hellopdu_pdu_length()
        if pdu_length and 'Not Set' not in pdu_length:
            dummy_dict[TrafficConfigConstants.TEMP_PDU_LENGTH_CMD] = pdu_length
    # end HelloPdu pdu_length methods

    # start HelloPdu priority methods
    #  priority is a 8 bit HEX_STRING example: FF
    def set_hellopdu_priority(self, priority, ignore_check=False):
        priority = self.normalize_value(priority, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU,
                                  HelloPduPacketConstants.HELLOPDU_PRIORITY, priority)

    def get_hellopdu_priority(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU, HelloPduPacketConstants.HELLOPDU_PRIORITY),
            PacketConstants.HEX_STRING)

    def get_hellopdu_priority_hltapi_cmd(self, dummy_dict):
        priority = self.get_hellopdu_priority()
        if priority and 'Not Set' not in priority:
            dummy_dict[TrafficConfigConstants.TEMP_PRIORITY_CMD] = priority
    # end HelloPdu priority methods

    # start HelloPdu lan_id methods
    #  lan_id is a 56 bit HEX_STRING example: FFFFFFFFFFFFFF
    def set_hellopdu_lan_id(self, lan_id, ignore_check=False):
        lan_id = self.normalize_value(lan_id, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU,
                                  HelloPduPacketConstants.HELLOPDU_LAN_ID, lan_id)

    def get_hellopdu_lan_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_ISIS_HELLOPDU, HelloPduPacketConstants.HELLOPDU_LAN_ID),
            PacketConstants.HEX_STRING)

    def get_hellopdu_lan_id_hltapi_cmd(self, dummy_dict):
        lan_id = self.get_hellopdu_lan_id()
        if lan_id and 'Not Set' not in lan_id:
            dummy_dict[TrafficConfigConstants.TEMP_LAN_ID_CMD] = lan_id
    # end HelloPdu lan_id methods

    def add_hellopdu_tlv(self, tlv_type, tlv_length, tlv_data):
        self.tlv_entries.append(IsisTlvEntry(tlv_type, tlv_length, tlv_data))

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("circuit_type", self.format_int(self.get_hellopdu_circuit_type(), 2))
        table.add_row_value("source_id", self.get_hellopdu_source_id())
        table.add_row_value("holding_timer", self.get_hellopdu_holding_timer())
        table.add_row_value("pdu_length", self.get_hellopdu_pdu_length())
        table.add_row_value("priority", self.get_hellopdu_priority())
        table.add_row_value("lan_id", self.get_hellopdu_lan_id())

        table_tlv = IsisTlvEntry.to_packet_string(self)

        return "\n\nHELLOPDU HEADER" + table.to_table_string() + \
               "\n\nHELLOPDU TLV ENTRIES" + table_tlv.to_table_string()

    def add_hellopdu_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_HELLOPDU)

    def build(self):
        self.add_hellopdu_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_hellopdu_circuit_type_hltapi_cmd(dummy_dict)
        # self.get_hellopdu_source_id_hltapi_cmd(dummy_dict)
        # self.get_hellopdu_holding_timer_hltapi_cmd(dummy_dict)
        # self.get_hellopdu_pdu_length_hltapi_cmd(dummy_dict)
        # self.get_hellopdu_priority_hltapi_cmd(dummy_dict)
        # self.get_hellopdu_lan_id_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_hellopdu(self, tgen_type, generator_ref, port_string, stream_id,
                                                            **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_hellopdu(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_hellopdu(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_hellopdu(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.khellopduFieldNumber
    # update this from the ostinato docs.
    #     hellopduField = p.Extensions[hellopdu]
    #     if self.is_field_set(self.get_hellopdu_circuit_type()):
    #         hellopduField.version = int(self.get_hellopdu_circuit_type())
    #     if self.is_field_set(self.get_hellopdu_source_id()):
    #         hellopduField.version = int(self.get_hellopdu_source_id())
    #     if self.is_field_set(self.get_hellopdu_holding_timer()):
    #         hellopduField.version = int(self.get_hellopdu_holding_timer())
    #     if self.is_field_set(self.get_hellopdu_pdu_length()):
    #         hellopduField.version = int(self.get_hellopdu_pdu_length())
    #     if self.is_field_set(self.get_hellopdu_priority()):
    #         hellopduField.version = int(self.get_hellopdu_priority())
    #     if self.is_field_set(self.get_hellopdu_lan_id()):
    #         hellopduField.version = int(self.get_hellopdu_lan_id())

    def config_jets_stream_hellopdu(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "HELLOPDU_HDR"
        pkt_bytes = "0x" + IsisHelloPduPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_hellopdu_circuit_type()):
            pkt_fields["circuit_type"] = int(self.get_hellopdu_circuit_type())
        if self.is_field_set(self.get_hellopdu_source_id()):
            pkt_fields["source_id"] = int(self.get_hellopdu_source_id())
        if self.is_field_set(self.get_hellopdu_holding_timer()):
            pkt_fields["holding_timer"] = int(self.get_hellopdu_holding_timer())
        if self.is_field_set(self.get_hellopdu_pdu_length()):
            pkt_fields["pdu_length"] = int(self.get_hellopdu_pdu_length())
        if self.is_field_set(self.get_hellopdu_priority()):
            pkt_fields["priority"] = int(self.get_hellopdu_priority())
        if self.is_field_set(self.get_hellopdu_lan_id()):
            pkt_fields["lan_id"] = int(self.get_hellopdu_lan_id())

    def get_ixtclhal_hellopdu_api_commands(self, port_string, streamid):
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
        circuit_type = self.get_bits_from_string(8, payload)
        self.set_hellopdu_circuit_type("0x" + circuit_type)
        payload = self.remove_bits_from_string(8, payload)
        source_id = self.get_bits_from_string(48, payload)
        self.set_hellopdu_source_id("0x" + source_id)
        payload = self.remove_bits_from_string(48, payload)
        holding_timer = self.get_bits_from_string(16, payload)
        self.set_hellopdu_holding_timer("0x" + holding_timer)
        payload = self.remove_bits_from_string(16, payload)
        pdu_length = self.get_bits_from_string(16, payload)
        self.set_hellopdu_pdu_length("0x" + pdu_length)
        payload = self.remove_bits_from_string(16, payload)
        priority = self.get_bits_from_string(8, payload)
        self.set_hellopdu_priority("0x" + priority)
        payload = self.remove_bits_from_string(8, payload)
        lan_id = self.get_bits_from_string(56, payload)
        self.set_hellopdu_lan_id("0x" + lan_id)
        payload = self.remove_bits_from_string(56, payload)
        # processTLVs
        self.payload = IsisTlvEntry.process_tlv(payload, self.tlv_entries, pdu_length, self)

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_hellopdu_circuit_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_hellopdu_source_id(), PacketConstants.HEX_STRING, 48)
        ret_string += self.format_byte_string(self.get_hellopdu_holding_timer(), PacketConstants.HEX_STRING, 16)
        ret_string += self.format_byte_string(self.get_hellopdu_pdu_length(), PacketConstants.HEX_STRING, 16)
        ret_string += self.format_byte_string(self.get_hellopdu_priority(), PacketConstants.HEX_STRING, 8)
        ret_string += self.format_byte_string(self.get_hellopdu_lan_id(), PacketConstants.HEX_STRING, 56)
        for entry in self.tlv_entries:
            ret_string += self.format_byte_string(entry.type, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.length, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.data, PacketConstants.HEX_STRING, entry.length * 8)

        return ret_string.replace("0x", "")

    @staticmethod
    def compare_hellopdu_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, IsisHelloPduPacketHeader)
            assert isinstance(actual, IsisHelloPduPacketHeader)
            if expected.is_field_set(expected.get_hellopdu_circuit_type()) and \
                    HelloPduPacketConstants.HELLOPDU_CIRCUIT_TYPE not in ignore_list:
                name = "HELLOPDU circuit_type : "
                if expected.get_hellopdu_circuit_type() != actual.get_hellopdu_circuit_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hellopdu_circuit_type()) + " != " +
                                                      str(actual.get_hellopdu_circuit_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hellopdu_circuit_type()) + " == " +
                                                 str(actual.get_hellopdu_circuit_type()) + " Pass")

            if expected.is_field_set(expected.get_hellopdu_source_id()) and \
                    HelloPduPacketConstants.HELLOPDU_SOURCE_ID not in ignore_list:
                name = "HELLOPDU source_id : "
                if expected.get_hellopdu_source_id() != actual.get_hellopdu_source_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hellopdu_source_id()) + " != " +
                                                      str(actual.get_hellopdu_source_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hellopdu_source_id()) + " == " +
                                                 str(actual.get_hellopdu_source_id()) + " Pass")

            if expected.is_field_set(expected.get_hellopdu_holding_timer()) and \
                    HelloPduPacketConstants.HELLOPDU_HOLDING_TIMER not in ignore_list:
                name = "HELLOPDU holding_timer : "
                if expected.get_hellopdu_holding_timer() != actual.get_hellopdu_holding_timer():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hellopdu_holding_timer()) + " != " +
                                                      str(actual.get_hellopdu_holding_timer()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hellopdu_holding_timer()) + " == " +
                                                 str(actual.get_hellopdu_holding_timer()) + " Pass")

            if expected.is_field_set(expected.get_hellopdu_pdu_length()) and \
                    HelloPduPacketConstants.HELLOPDU_PDU_LENGTH not in ignore_list:
                name = "HELLOPDU pdu_length : "
                if expected.get_hellopdu_pdu_length() != actual.get_hellopdu_pdu_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hellopdu_pdu_length()) + " != " +
                                                      str(actual.get_hellopdu_pdu_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hellopdu_pdu_length()) + " == " +
                                                 str(actual.get_hellopdu_pdu_length()) + " Pass")

            if expected.is_field_set(expected.get_hellopdu_priority()) and \
                    HelloPduPacketConstants.HELLOPDU_PRIORITY not in ignore_list:
                name = "HELLOPDU priority : "
                if expected.get_hellopdu_priority() != actual.get_hellopdu_priority():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hellopdu_priority()) + " != " +
                                                      str(actual.get_hellopdu_priority()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hellopdu_priority()) + " == " +
                                                 str(actual.get_hellopdu_priority()) + " Pass")

            if expected.is_field_set(expected.get_hellopdu_lan_id()) and \
                    HelloPduPacketConstants.HELLOPDU_LAN_ID not in ignore_list:
                name = "HELLOPDU lan_id : "
                if expected.get_hellopdu_lan_id() != actual.get_hellopdu_lan_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hellopdu_lan_id()) + " != " +
                                                      str(actual.get_hellopdu_lan_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hellopdu_lan_id()) + " == " +
                                                 str(actual.get_hellopdu_lan_id()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with HelloPduPacketHeader")
        return results


class HelloPduPacketConstants:
    def __init__(self):
        pass

    HELLOPDU_CIRCUIT_TYPE = "HELLOPDU_CIRCUIT_TYPE"
    HELLOPDU_SOURCE_ID = "HELLOPDU_SOURCE_ID"
    HELLOPDU_HOLDING_TIMER = "HELLOPDU_HOLDING_TIMER"
    HELLOPDU_PDU_LENGTH = "HELLOPDU_PDU_LENGTH"
    HELLOPDU_PRIORITY = "HELLOPDU_PRIORITY"
    HELLOPDU_LAN_ID = "HELLOPDU_LAN_ID"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
