###########################################################################
# ###   start DnsPacketHeader
###########################################################################
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer5PacketHeader import Layer5PacketHeader
# from ExtremeAutomation.Library.Utils.NumberUtils import *
# import ostinato # pip install python-ostinato
# from ostinato.core import ost_pb, DroneProxy
# from ostinato.protocols.dns_pb2 import dns
# import binascii


# from ostinato.core import ost_pb
# from ostinato.protocols.hexdump_pb2 import hexDump


class DnsPacketHeader(Layer5PacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    init function
        # Length = 16bits
        # Transaction Id = 16bits
        # Flags = 16bits
        # Questions = 16bits
        # Answers = 16bits
        # Authority = 16bits
        # Additional = 16bits
        # Query Name = 64bits
        # Query Type = 16bits
        # Query Class = 16bits
        # Response Name = 64bits
        # Response Type = 16bits
        # Response Class = 16bits
        # Response Time To Live = 32bits
        # Response Data Length = 16bits
        # Response Resource Data = 64bits
    """

    def __init__(self):
        self.add_dns_header()
        self.HEADER_SIZE_DNS = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Dns Length methods
    #  length is a 16 bit INTEGER example: 1
    def set_dns_length(self, length, ignore_check=False):
        length = self.normalize_value(length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_LENGTH, length)

    def get_dns_length(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_LENGTH),
            PacketConstants.INTEGER)

    def get_dns_length_hltapi_cmd(self, dummy_dict):
        length = self.get_dns_length()
        if isinstance(length, int):
            length = str(length)
        if length and 'Not Set' not in length:
            dummy_dict[TrafficConfigConstants.TEMP_LENGTH_CMD] = length

    # end Dns Length methods

    # start Dns Transaction Id methods
    #  transaction_id is a 16 bit INTEGER example: 1
    def set_dns_transaction_id(self, transaction_id, ignore_check=False):
        transaction_id = self.normalize_value(transaction_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_TRANSACTION_ID,
                                  transaction_id)

    def get_dns_transaction_id(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_TRANSACTION_ID),
            PacketConstants.INTEGER)

    def get_dns_transaction_id_hltapi_cmd(self, dummy_dict):
        transaction_id = self.get_dns_transaction_id()
        if isinstance(transaction_id, int):
            transaction_id = str(transaction_id)
        if transaction_id and 'Not Set' not in transaction_id:
            dummy_dict[TrafficConfigConstants.TEMP_TRANSACTION_ID_CMD] = transaction_id

    # end Dns Transaction Id methods

    # start Dns Flags methods
    #  flags is a 16 bit INTEGER example: 1
    def set_dns_flags(self, flags, ignore_check=False):
        flags = self.normalize_value(flags, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_FLAGS, flags)

    def get_dns_flags(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_FLAGS),
            PacketConstants.INTEGER)

    def get_dns_flags_hltapi_cmd(self, dummy_dict):
        flags = self.get_dns_flags()
        if isinstance(flags, int):
            flags = str(flags)
        if flags and 'Not Set' not in flags:
            dummy_dict[TrafficConfigConstants.TEMP_FLAGS_CMD] = flags

    # end Dns Flags methods

    # start Dns Questions methods
    #  questions is a 16 bit INTEGER example: 1
    def set_dns_questions(self, questions, ignore_check=False):
        questions = self.normalize_value(questions, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_QUESTIONS, questions)

    def get_dns_questions(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_QUESTIONS),
            PacketConstants.INTEGER)

    def get_dns_questions_hltapi_cmd(self, dummy_dict):
        questions = self.get_dns_questions()
        if isinstance(questions, int):
            questions = str(questions)
        if questions and 'Not Set' not in questions:
            dummy_dict[TrafficConfigConstants.TEMP_QUESTIONS_CMD] = questions

    # end Dns Questions methods

    # start Dns Answers methods
    #  answers is a 16 bit INTEGER example: 1
    def set_dns_answers(self, answers, ignore_check=False):
        answers = self.normalize_value(answers, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_ANSWERS, answers)

    def get_dns_answers(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_ANSWERS),
            PacketConstants.INTEGER)

    def get_dns_answers_hltapi_cmd(self, dummy_dict):
        answers = self.get_dns_answers()
        if isinstance(answers, int):
            answers = str(answers)
        if answers and 'Not Set' not in answers:
            dummy_dict[TrafficConfigConstants.TEMP_ANSWERS_CMD] = answers

    # end Dns Answers methods

    # start Dns Authority methods
    #  authority is a 16 bit INTEGER example: 1
    def set_dns_authority(self, authority, ignore_check=False):
        authority = self.normalize_value(authority, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_AUTHORITY, authority)

    def get_dns_authority(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_AUTHORITY),
            PacketConstants.INTEGER)

    def get_dns_authority_hltapi_cmd(self, dummy_dict):
        authority = self.get_dns_authority()
        if isinstance(authority, int):
            authority = str(authority)
        if authority and 'Not Set' not in authority:
            dummy_dict[TrafficConfigConstants.TEMP_AUTHORITY_CMD] = authority

    # end Dns Authority methods

    # start Dns Additional methods
    #  additional is a 16 bit INTEGER example: 1
    def set_dns_additional(self, additional, ignore_check=False):
        additional = self.normalize_value(additional, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_ADDITIONAL, additional)

    def get_dns_additional(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_ADDITIONAL),
            PacketConstants.INTEGER)

    def get_dns_additional_hltapi_cmd(self, dummy_dict):
        additional = self.get_dns_additional()
        if isinstance(additional, int):
            additional = str(additional)
        if additional and 'Not Set' not in additional:
            dummy_dict[TrafficConfigConstants.TEMP_ADDITIONAL_CMD] = additional

    # end Dns Additional methods

    # start Dns Query Name methods
    #  query_name is a 64 bit HEX_STRING example: FFFFFFFFFFFFFFFF
    def set_dns_query_name(self, query_name, entry, ignore_check=False):
        query_name = self.normalize_value(query_name, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_QUERY_NAME + " " +
                                  str(entry), query_name)

    def get_dns_query_name(self, entry):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_QUERY_NAME + " " +
                                      str(entry)), PacketConstants.HEX_STRING)

    def get_dns_query_name_hltapi_cmd(self, entry, dummy_dict):
        query_name = self.get_dns_query_name(entry)
        if query_name and 'Not Set' not in query_name:
            dummy_dict[TrafficConfigConstants.TEMP_QUERY_NAME_CMD] = query_name

    # end Dns Query Name methods

    # start Dns Query Type methods
    #  query_type is a 16 bit INTEGER example: 1
    def set_dns_query_type(self, query_type, entry, ignore_check=False):
        query_type = self.normalize_value(query_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_QUERY_TYPE + " " +
                                  str(entry), query_type)

    def get_dns_query_type(self, entry):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_QUERY_TYPE + " " +
                                      str(entry)), PacketConstants.INTEGER)

    def get_dns_query_type_hltapi_cmd(self, entry, dummy_dict):
        query_type = self.get_dns_query_type(entry)
        if isinstance(query_type, int):
            query_type = str(query_type)
        if query_type and 'Not Set' not in query_type:
            dummy_dict[TrafficConfigConstants.TEMP_QUERY_TYPE_CMD] = query_type

    # end Dns Query Type methods

    # start Dns Query Class methods
    #  query_class is a 16 bit INTEGER example: 1
    def set_dns_query_class(self, query_class, entry, ignore_check=False):
        query_class = self.normalize_value(query_class, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_QUERY_CLASS + " " +
                                  str(entry), query_class)

    def get_dns_query_class(self, entry):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_QUERY_CLASS + " " +
                                      str(entry)), PacketConstants.INTEGER)

    def get_dns_query_class_hltapi_cmd(self, entry, dummy_dict):
        query_class = self.get_dns_query_class(entry)
        if isinstance(query_class, int):
            query_class = str(query_class)
        if query_class and 'Not Set' not in query_class:
            dummy_dict[TrafficConfigConstants.TEMP_QUERY_CLASS_CMD] = query_class

    # end Dns Query Class methods

    # start Dns Response Name methods
    #  response_name is a 64 bit HEX_STRING example: FFFFFFFFFFFFFFFF
    def set_dns_response_name(self, response_name, entry, ignore_check=False):
        response_name = self.normalize_value(response_name, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_RESPONSE_NAME + " " +
                                  str(entry), response_name)

    def get_dns_response_name(self, entry):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_RESPONSE_NAME + " " +
                                      str(entry)), PacketConstants.HEX_STRING)

    def get_dns_response_name_hltapi_cmd(self, entry, dummy_dict):
        response_name = self.get_dns_response_name(entry)
        if response_name and 'Not Set' not in response_name:
            dummy_dict[TrafficConfigConstants.TEMP_RESPONSE_NAME_CMD] = response_name

    # end Dns Response Name methods

    # start Dns Response Type methods
    #  response_type is a 16 bit INTEGER example: 1
    def set_dns_response_type(self, response_type, entry, ignore_check=False):
        response_type = self.normalize_value(response_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_RESPONSE_TYPE + " " +
                                  str(entry), response_type)

    def get_dns_response_type(self, entry):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_RESPONSE_TYPE + " " +
                                      str(entry)), PacketConstants.INTEGER)

    def get_dns_response_type_hltapi_cmd(self, entry, dummy_dict):
        response_type = self.get_dns_response_type(entry)
        if isinstance(response_type, int):
            response_type = str(response_type)
        if response_type and 'Not Set' not in response_type:
            dummy_dict[TrafficConfigConstants.TEMP_RESPONSE_TYPE_CMD] = response_type

    # end Dns Response Type methods

    # start Dns Response Class methods
    #  response_class is a 16 bit INTEGER example: 1
    def set_dns_response_class(self, response_class, entry, ignore_check=False):
        response_class = self.normalize_value(response_class, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS, DnsPacketConstants.DNS_RESPONSE_CLASS + " " +
                                  str(entry), response_class)

    def get_dns_response_class(self, entry):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS,
                                                              DnsPacketConstants.DNS_RESPONSE_CLASS + " " +
                                                              str(entry)), PacketConstants.INTEGER)

    def get_dns_response_class_hltapi_cmd(self, entry, dummy_dict):
        response_class = self.get_dns_response_class(entry)
        if isinstance(response_class, int):
            response_class = str(response_class)
        if response_class and 'Not Set' not in response_class:
            dummy_dict[TrafficConfigConstants.TEMP_RESPONSE_CLASS_CMD] = response_class

    # end Dns Response Class methods

    # start Dns Response Time To Live methods
    #  response_time_to_live is a 32 bit INTEGER example: 1
    def set_dns_response_time_to_live(self, response_time_to_live, entry, ignore_check=False):
        response_time_to_live = self.normalize_value(response_time_to_live, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS,
                                  DnsPacketConstants.DNS_RESPONSE_TIME_TO_LIVE + " " +
                                  str(entry), response_time_to_live)

    def get_dns_response_time_to_live(self, entry):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS,
                                                              DnsPacketConstants.DNS_RESPONSE_TIME_TO_LIVE + " " +
                                                              str(entry)), PacketConstants.INTEGER)

    def get_dns_response_time_to_live_hltapi_cmd(self, entry, dummy_dict):
        response_time_to_live = self.get_dns_response_time_to_live(entry)
        if isinstance(response_time_to_live, int):
            response_time_to_live = str(response_time_to_live)
        if response_time_to_live and 'Not Set' not in response_time_to_live:
            dummy_dict[TrafficConfigConstants.TEMP_RESPONSE_TIME_TO_LIVE_CMD] = response_time_to_live

    # end Dns Response Time To Live methods

    # start Dns Response Data Length methods
    #  response_data_length is a 16 bit INTEGER example: 1
    def set_dns_response_data_length(self, response_data_length, entry, ignore_check=False):
        response_data_length = self.normalize_value(response_data_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS,
                                  DnsPacketConstants.DNS_RESPONSE_DATA_LENGTH + " " +
                                  str(entry), response_data_length)

    def get_dns_response_data_length(self, entry):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS,
                                                              DnsPacketConstants.DNS_RESPONSE_DATA_LENGTH + " " +
                                                              str(entry)), PacketConstants.INTEGER)

    def get_dns_response_data_length_hltapi_cmd(self, entry, dummy_dict):
        response_data_length = self.get_dns_response_data_length(entry)
        if isinstance(response_data_length, int):
            response_data_length = str(response_data_length)
        if response_data_length and 'Not Set' not in response_data_length:
            dummy_dict[TrafficConfigConstants.TEMP_RESPONSE_DATA_LENGTH_CMD] = response_data_length

    # end Dns Response Data Length methods

    # start Dns Response Resource Data methods
    #  response_resource_data is a 64 bit HEX_STRING example: FFFFFFFFFFFFFFFF
    def set_dns_response_resource_data(self, response_resource_data, entry, ignore_check=False):
        response_resource_data = self.normalize_value(response_resource_data, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_DNS,
                                  DnsPacketConstants.DNS_RESPONSE_RESOURCE_DATA + " " +
                                  str(entry), response_resource_data)

    def get_dns_response_resource_data(self, entry):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L5_DNS,
                                                              DnsPacketConstants.DNS_RESPONSE_RESOURCE_DATA + " " +
                                                              str(entry)), PacketConstants.HEX_STRING)

    def get_dns_response_resource_data_hltapi_cmd(self, entry, dummy_dict):
        response_resource_data = self.get_dns_response_resource_data(entry)
        if response_resource_data and 'Not Set' not in response_resource_data:
            dummy_dict[TrafficConfigConstants.TEMP_RESPONSE_RESOURCE_DATA_CMD] = response_resource_data

    # end Dns Response Resource Data methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Length", self.format_int(self.get_dns_length(), 2))
        table.add_row_value("Transaction Id", self.format_int(self.get_dns_transaction_id(), 2))
        table.add_row_value("Flags", self.format_int(self.get_dns_flags(), 2))
        table.add_row_value("Questions", self.format_int(self.get_dns_questions(), 2))
        table.add_row_value("Answers", self.format_int(self.get_dns_answers(), 2))
        table.add_row_value("Authority", self.format_int(self.get_dns_authority(), 2))
        table.add_row_value("Additional", self.format_int(self.get_dns_additional(), 2))

        table.add_row_value("Query Name", self.get_dns_query_name())
        table.add_row_value("Query Type", self.format_int(self.get_dns_query_type(), 2))
        table.add_row_value("Query Class", self.format_int(self.get_dns_query_class(), 2))

        table.add_row_value("Response Name", self.get_dns_response_name())
        table.add_row_value("Response Type", self.format_int(self.get_dns_response_type(), 2))
        table.add_row_value("Response Class", self.format_int(self.get_dns_response_class(), 2))
        table.add_row_value("Response Time To Live", self.format_int(self.get_dns_response_time_to_live(), 4))
        table.add_row_value("Response Data Length", self.format_int(self.get_dns_response_data_length(), 2))
        table.add_row_value("Response Resource Data", self.get_dns_response_resource_data())
        return "\n\nDNS HEADER" + table.to_table_string()

    def add_dns_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_DNS)

    def build(self):
        self.add_dns_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_dns_length_hltapi_cmd(dummy_dict)
        # self.get_dns_transaction_id_hltapi_cmd(dummy_dict)
        # self.get_dns_flags_hltapi_cmd(dummy_dict)
        # self.get_dns_questions_hltapi_cmd(dummy_dict)
        # self.get_dns_answers_hltapi_cmd(dummy_dict)
        # self.get_dns_authority_hltapi_cmd(dummy_dict)
        # self.get_dns_additional_hltapi_cmd(dummy_dict)
        # self.get_dns_query_name_hltapi_cmd(dummy_dict)
        # self.get_dns_query_type_hltapi_cmd(dummy_dict)
        # self.get_dns_query_class_hltapi_cmd(dummy_dict)
        # self.get_dns_response_name_hltapi_cmd(dummy_dict)
        # self.get_dns_response_type_hltapi_cmd(dummy_dict)
        # self.get_dns_response_class_hltapi_cmd(dummy_dict)
        # self.get_dns_response_time_to_live_hltapi_cmd(dummy_dict)
        # self.get_dns_response_data_length_hltapi_cmd(dummy_dict)
        # self.get_dns_response_resource_data_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_dns(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_dns(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_dns(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_dns(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        # p.protocol_id.id = ost_pb.Protocol.kdnsFieldNumber
        # p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = DnsPacketHeader.get_header_bytes(self).replace(" ", "")
        # payloadData = binascii.a2b_hex(payloadData)
        # p.Extensions[hexDump].content = payloadData

    def config_jets_stream_dns(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "DNS_HDR"
        pkt_bytes = "0x" + DnsPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_dns_api_commands(self, port_string, streamid):
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
        length = self.get_bits_from_string(16, payload)
        self.set_dns_length("0x" + length)
        payload = self.remove_bits_from_string(16, payload)
        transaction_id = self.get_bits_from_string(16, payload)
        self.set_dns_transaction_id("0x" + transaction_id)
        payload = self.remove_bits_from_string(16, payload)
        flags = self.get_bits_from_string(16, payload)
        self.set_dns_flags("0x" + flags)
        payload = self.remove_bits_from_string(16, payload)
        questions = self.get_bits_from_string(16, payload)
        self.set_dns_questions("0x" + questions)
        payload = self.remove_bits_from_string(16, payload)
        answers = self.get_bits_from_string(16, payload)
        self.set_dns_answers("0x" + answers)
        payload = self.remove_bits_from_string(16, payload)
        authority = self.get_bits_from_string(16, payload)
        self.set_dns_authority("0x" + authority)
        payload = self.remove_bits_from_string(16, payload)
        additional = self.get_bits_from_string(16, payload)
        self.set_dns_additional("0x" + additional)
        payload = self.remove_bits_from_string(16, payload)

        query_name = self.get_bits_from_string(64, payload)
        self.set_dns_query_name("0x" + query_name)
        payload = self.remove_bits_from_string(64, payload)
        query_type = self.get_bits_from_string(16, payload)
        self.set_dns_query_type("0x" + query_type)
        payload = self.remove_bits_from_string(16, payload)
        query_class = self.get_bits_from_string(16, payload)
        self.set_dns_query_class("0x" + query_class)
        payload = self.remove_bits_from_string(16, payload)

        response_name = self.get_bits_from_string(64, payload)
        self.set_dns_response_name("0x" + response_name)
        payload = self.remove_bits_from_string(64, payload)
        response_type = self.get_bits_from_string(16, payload)
        self.set_dns_response_type("0x" + response_type)
        payload = self.remove_bits_from_string(16, payload)
        response_class = self.get_bits_from_string(16, payload)
        self.set_dns_response_class("0x" + response_class)
        payload = self.remove_bits_from_string(16, payload)
        response_time_to_live = self.get_bits_from_string(32, payload)
        self.set_dns_response_time_to_live("0x" + response_time_to_live)
        payload = self.remove_bits_from_string(32, payload)
        response_data_length = self.get_bits_from_string(16, payload)
        self.set_dns_response_data_length("0x" + response_data_length)
        payload = self.remove_bits_from_string(16, payload)
        response_resource_data = self.get_bits_from_string(64, payload)
        self.set_dns_response_resource_data("0x" + response_resource_data)
        payload = self.remove_bits_from_string(64, payload)

        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_dns_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_transaction_id(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_flags(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_questions(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_answers(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_authority(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_additional(), PacketConstants.INTEGER, 16)

        ret_string += self.format_byte_string(self.get_dns_query_name(), PacketConstants.HEX_STRING, 64)
        ret_string += self.format_byte_string(self.get_dns_query_type(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_query_class(), PacketConstants.INTEGER, 16)

        ret_string += self.format_byte_string(self.get_dns_response_name(), PacketConstants.HEX_STRING, 64)
        ret_string += self.format_byte_string(self.get_dns_response_type(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_response_class(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_response_time_to_live(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_dns_response_data_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dns_response_resource_data(), PacketConstants.HEX_STRING, 64)
        return ret_string

    @staticmethod
    def compare_dns_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, DnsPacketHeader)
            assert isinstance(actual, DnsPacketHeader)
            if expected.is_field_set(expected.get_dns_length()) and DnsPacketConstants.DNS_LENGTH not in ignore_list:
                name = "DNS length : "
                if expected.get_dns_length() != actual.get_dns_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dns_length()) + " != " + str(actual.get_dns_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dns_length()) + " == " + str(actual.get_dns_length()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_transaction_id()) and DnsPacketConstants.DNS_TRANSACTION_ID not in ignore_list:
                name = "DNS transaction id : "
                if expected.get_dns_transaction_id() != actual.get_dns_transaction_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dns_transaction_id()) + " != " + str(
                            actual.get_dns_transaction_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dns_transaction_id()) + " == " + str(
                        actual.get_dns_transaction_id()) + " Pass")

            if expected.is_field_set(expected.get_dns_flags()) and DnsPacketConstants.DNS_FLAGS not in ignore_list:
                name = "DNS flags : "
                if expected.get_dns_flags() != actual.get_dns_flags():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dns_flags()) + " != " + str(actual.get_dns_flags()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dns_flags()) + " == " + str(actual.get_dns_flags()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_questions()) and DnsPacketConstants.DNS_QUESTIONS not in ignore_list:
                name = "DNS questions : "
                if expected.get_dns_questions() != actual.get_dns_questions():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dns_questions()) + " != " + str(actual.get_dns_questions()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dns_questions()) + " == " + str(actual.get_dns_questions()) + " Pass")

            if expected.is_field_set(expected.get_dns_answers()) and DnsPacketConstants.DNS_ANSWERS not in ignore_list:
                name = "DNS answers : "
                if expected.get_dns_answers() != actual.get_dns_answers():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dns_answers()) + " != " + str(actual.get_dns_answers()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dns_answers()) + " == " + str(actual.get_dns_answers()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_authority()) and DnsPacketConstants.DNS_AUTHORITY not in ignore_list:
                name = "DNS authority : "
                if expected.get_dns_authority() != actual.get_dns_authority():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dns_authority()) + " != " + str(actual.get_dns_authority()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dns_authority()) + " == " + str(actual.get_dns_authority()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_additional()) and DnsPacketConstants.DNS_ADDITIONAL not in ignore_list:
                name = "DNS additional : "
                if expected.get_dns_additional() != actual.get_dns_additional():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dns_additional()) + " != " + str(actual.get_dns_additional()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dns_additional()) + " == " + str(actual.get_dns_additional()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_query_name()) and DnsPacketConstants.DNS_QUERY_NAME not in ignore_list:
                name = "DNS query name : "
                if expected.get_dns_query_name() != actual.get_dns_query_name():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dns_query_name()) + " != " + str(actual.get_dns_query_name()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dns_query_name()) + " == " + str(actual.get_dns_query_name()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_query_type()) and DnsPacketConstants.DNS_QUERY_TYPE not in ignore_list:
                name = "DNS query type : "
                if expected.get_dns_query_type() != actual.get_dns_query_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dns_query_type()) + " != " + str(actual.get_dns_query_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dns_query_type()) + " == " + str(actual.get_dns_query_type()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_query_class()) and DnsPacketConstants.DNS_QUERY_CLASS not in ignore_list:
                name = "DNS query class : "
                if expected.get_dns_query_class() != actual.get_dns_query_class():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dns_query_class()) + " != " + str(actual.get_dns_query_class()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dns_query_class()) + " == " + str(
                        actual.get_dns_query_class()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_response_name()) and DnsPacketConstants.DNS_RESPONSE_NAME not in ignore_list:
                name = "DNS response name : "
                if expected.get_dns_response_name() != actual.get_dns_response_name():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dns_response_name()) + " != " + str(
                            actual.get_dns_response_name()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dns_response_name()) + " == " + str(
                        actual.get_dns_response_name()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_response_type()) and DnsPacketConstants.DNS_RESPONSE_TYPE not in ignore_list:
                name = "DNS response type : "
                if expected.get_dns_response_type() != actual.get_dns_response_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dns_response_type()) + " != " + str(
                            actual.get_dns_response_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dns_response_type()) + " == " + str(
                        actual.get_dns_response_type()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_response_class()) and DnsPacketConstants.DNS_RESPONSE_CLASS not in ignore_list:
                name = "DNS response class : "
                if expected.get_dns_response_class() != actual.get_dns_response_class():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dns_response_class()) + " != " + str(
                            actual.get_dns_response_class()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dns_response_class()) + " == " + str(
                        actual.get_dns_response_class()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_response_time_to_live()) and \
                    DnsPacketConstants.DNS_RESPONSE_TIME_TO_LIVE not in ignore_list:
                name = "DNS response time to live : "
                if expected.get_dns_response_time_to_live() != actual.get_dns_response_time_to_live():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dns_response_time_to_live()) + " != " + str(
                            actual.get_dns_response_time_to_live()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dns_response_time_to_live()) + " == " + str(
                        actual.get_dns_response_time_to_live()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_response_data_length()) and \
                    DnsPacketConstants.DNS_RESPONSE_DATA_LENGTH not in ignore_list:
                name = "DNS response data length : "
                if expected.get_dns_response_data_length() != actual.get_dns_response_data_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dns_response_data_length()) + " != " + str(
                            actual.get_dns_response_data_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dns_response_data_length()) + " == " + str(
                        actual.get_dns_response_data_length()) + " Pass")

            if expected.is_field_set(
                    expected.get_dns_response_resource_data()) and \
                    DnsPacketConstants.DNS_RESPONSE_RESOURCE_DATA not in ignore_list:
                name = "DNS response resource data : "
                if expected.get_dns_response_resource_data() != actual.get_dns_response_resource_data():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dns_response_resource_data()) + " != " + str(
                            actual.get_dns_response_resource_data()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dns_response_resource_data()) + " == " + str(
                        actual.get_dns_response_resource_data()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_error("Error with DnsPacketHeader")
        return results


class DnsPacketConstants:
    """
    init function
    """

    def __init__(self):
        pass

    DNS_LENGTH = "DNS_LENGTH"

    DNS_TRANSACTION_ID = "DNS_TRANSACTION_ID"

    DNS_FLAGS = "DNS_FLAGS"

    DNS_QUESTIONS = "DNS_QUESTIONS"

    DNS_ANSWERS = "DNS_ANSWERS"

    DNS_AUTHORITY = "DNS_AUTHORITY"

    DNS_ADDITIONAL = "DNS_ADDITIONAL"

    DNS_QUERY_NAME = "DNS_QUERY_NAME"

    DNS_QUERY_TYPE = "DNS_QUERY_TYPE"

    DNS_QUERY_CLASS = "DNS_QUERY_CLASS"

    DNS_RESPONSE_NAME = "DNS_RESPONSE_NAME"

    DNS_RESPONSE_TYPE = "DNS_RESPONSE_TYPE"

    DNS_RESPONSE_CLASS = "DNS_RESPONSE_CLASS"

    DNS_RESPONSE_TIME_TO_LIVE = "DNS_RESPONSE_TIME_TO_LIVE"

    DNS_RESPONSE_DATA_LENGTH = "DNS_RESPONSE_DATA_LENGTH"

    DNS_RESPONSE_RESOURCE_DATA = "DNS_RESPONSE_RESOURCE_DATA"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
###########################################################################
# ###   end DnsPacketHeader
###########################################################################
