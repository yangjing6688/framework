from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfPacketHeader import OspfPacketHeader
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address


class OspfLinkStateAcknowledgePacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    OSPF LS Ack Packet Header
        # Number of LSAs = 16bits
    """

    def __init__(self):
        self.add_linkstateacknowledge_header()
        self.num_lsa = 0
        self.lsa_entries = []
        self.set_lsa_num(0, True)
        self.HEADER_SIZE_LINKSTATEACKNOWLEDGE = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################
    def get_lsa_num(self):
        return self.num_lsa

    def set_lsa_num(self, num_lsas, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(
            OspfLinkStateAcknowledgePacketConstants.LINKSTATEACKNOWLEDGE_LSA_NUM, ignore_check)
        self.num_lsa = NumberUtils.to_integer_value(num_lsas)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  OspfLinkStateAcknowledgePacketConstants.LINKSTATEACKNOWLEDGE_LSA_NUM, num_lsas)

    def add_lsa_entry(self, entry):
        self.set_lsa_num(self.num_lsa + 1)
        self.lsa_entries.append(entry)
    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        rt_string = ""
        table = TableFormatter()

        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            rt_string += "\n\nAuth Crypt Data:" + self.get_ospf_auth_crypt_data()

        rt_string += "\n\nLINKSTATEACKNOWLEDGE HEADER" + table.to_table_string()
        index = 0
        for entry in self.lsa_entries:
            index += 1
            assert isinstance(entry, OspfLinkStateLSAEntry)
            rt_string += "\n\n Link State Advertisement header #" + str(index) + "" + entry.to_packet_string()
        return rt_string

    def add_linkstateacknowledge_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_OSPF_LINKSTATEACKNOWLEDGE)

    def build(self):
        self.add_linkstateacknowledge_header()
        self.set_ospf_message_type(0x04, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_linkstateacknowledge_number_of_lsas_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_linkstateacknowledge(self, tgen_type, generator_ref, port_string,
                                                                        stream_id, **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_linkstateacknowledge(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_linkstateacknowledge(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_linkstateacknowledge(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.klinkstateacknowledgeFieldNumber
        # acknowledge this from the ostinato docs.

    def config_jets_stream_linkstateacknowledge(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "LINKSTATEACKNOWLEDGE_HDR"
        pkt_bytes = "0x" + OspfLinkStateAcknowledgePacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_linkstateacknowledge_api_commands(self, port_string, streamid):
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
        self.parse_bytes_lsa()

    def parse_bytes_lsa(self):
        payload = self.payload
        number_of_lsas = ((self.get_ospf_packet_length() - 24) / 20)
        while number_of_lsas > 0:
            number_of_lsas -= 1
            link_state_age = int(self.get_bits_from_string(16, payload), 16)
            # self.set_link_state_acknowledge_link_state_age("0x" + link_state_age)
            payload = self.remove_bits_from_string(16, payload)
            link_state_options = int(self.get_bits_from_string(8, payload), 16)
            # self.set_link_state_acknowledge_link_state_options("0x" + link_state_options)
            payload = self.remove_bits_from_string(8, payload)
            link_state_type = int(self.get_bits_from_string(8, payload), 16)
            # self.set_link_state_acknowledge_link_state_type("0x" + link_state_type)
            payload = self.remove_bits_from_string(8, payload)
            link_state_id = int(self.get_bits_from_string(32, payload), 16)
            # self.set_link_state_acknowledge_link_state_id("0x" + link_state_id)
            payload = self.remove_bits_from_string(32, payload)
            advertising_router = int(self.get_bits_from_string(32, payload), 16)
            # self.set_link_state_acknowledge_advertising_router("0x" + advertising_router)
            payload = self.remove_bits_from_string(32, payload)
            sequence_number = int(self.get_bits_from_string(32, payload), 16)
            # self.set_link_state_acknowledge_sequence_number("0x" + sequence_number)
            payload = self.remove_bits_from_string(32, payload)
            checksum = int(self.get_bits_from_string(16, payload), 16)
            # self.set_link_state_acknowledge_checksum("0x" + checksum)
            payload = self.remove_bits_from_string(16, payload)
            length = int(self.get_bits_from_string(16, payload), 16)
            # self.set_link_state_acknowledge_length("0x" + length)
            payload = self.remove_bits_from_string(16, payload)
            entry = OspfLinkStateLSAEntry(self, link_state_age, link_state_options, link_state_type, link_state_id,
                                          advertising_router, sequence_number, checksum, length)
            self.add_lsa_entry(entry)

        payload = OspfPacketHeader.process_auth_entry(payload, self)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""

        # loop through the entries
        for entry in self.lsa_entries:
            assert isinstance(entry, OspfLinkStateLSAEntry)
            ret_string += entry.get_header_bytes()

        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            ret_string += self.get_bytes_auth_entry(self).replace("0x", "")
        return ret_string

    @staticmethod
    def compare_linkstateacknowledge_packet_header(expected, actual, ignore_list, print_results=True,
                                                   print_failures=True):
        results = True
        try:
            assert isinstance(expected, OspfLinkStateAcknowledgePacketHeader)
            assert isinstance(actual, OspfLinkStateAcknowledgePacketHeader)
            if expected.is_field_set(expected.get_linkstateacknowledge_number_of_lsas()) and \
                    OspfLinkStateAcknowledgePacketConstants.LINKSTATEACKNOWLEDGE_NUMBER_OF_LSAS not in ignore_list:
                name = "LINKSTATEACKNOWLEDGE number of lsas : "
                if expected.get_linkstateacknowledge_number_of_lsas() != \
                        actual.get_linkstateacknowledge_number_of_lsas():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_linkstateacknowledge_number_of_lsas()) +
                                                      " != " + str(actual.get_linkstateacknowledge_number_of_lsas()) +
                                                      " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_linkstateacknowledge_number_of_lsas()) +
                                                 " == " + str(actual.get_linkstateacknowledge_number_of_lsas()) +
                                                 " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with LinkStateAcknowledgePacketHeader")
        return results


class OspfLinkStateLSAEntry(object):
    """
     LSA header (they all have this):
       0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |            LS age             |     Options   |       1       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                        Link State ID                          |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                     Advertising Router                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                     LS sequence number                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |         LS checksum           |             length            |
    """

    def __init__(self, handler, age, option, pkt_type, pkt_id, advertising_router, sequence_number, checksum, length):
        self.handler = handler
        # these have to be in decimal so convert them from hex first.
        self.age = age
        self.option = option
        self.pkt_type = pkt_type
        self.pkt_id = pkt_id
        self.advertising_router = advertising_router
        self.sequence_number = sequence_number
        self.checksum = checksum
        self.length = length
        self.type_string = self.get_type_string(pkt_type)

    def get_type_string(self, lsa_type):
        if lsa_type == 0x01:
            return "LSA Type 1 (Router-LSA)"
        elif lsa_type == 0x02:
            return "LSA Type 2 (Network-LSA)"
        elif lsa_type == 0x03:
            return "LSA Type 3 (Summary-LSA IP Network)"
        elif lsa_type == 0x04:
            return "LSA Type 4 (Summary-LSA ASBR)"
        elif lsa_type == 0x05:
            return "LSA Type 5 (AS-External-LSA)"
        elif lsa_type == 0x07:
            return "LSA Type 7 (NSSA AS-External-LSA)"
        elif 0x05 < lsa_type <= 0x0A:
            return "Future Expansion"
        else:
            return "Unknown Type"

    def to_packet_string(self):
        table_tlv = TableFormatter()
        packet = self.handler
        table_tlv.add_row_value("Age", packet.format_int(self.age, 2))
        table_tlv.add_row_value("Options", packet.format_int(self.option, 2))
        table_tlv.add_row_value("Type", self.type_string + " " + packet.format_int(self.pkt_type, 2))
        table_tlv.add_row_value("ID", Ipv4Address(self.pkt_id))
        table_tlv.add_row_value("Advertising Router", Ipv4Address(self.advertising_router))
        table_tlv.add_row_value("Sequence Number", packet.format_int(self.sequence_number, 2))
        table_tlv.add_row_value("Checksum", packet.format_int(self.checksum, 2))
        table_tlv.add_row_value("Length", packet.format_int(self.length, 2))
        return table_tlv.to_table_string()

    def get_header_bytes(self):
        ret_string = ""
        handler = self.handler
        ret_string += handler.format_byte_string(self.age, PacketConstants.INTEGER, 16)
        ret_string += handler.format_byte_string(self.option, PacketConstants.INTEGER, 8)
        ret_string += handler.format_byte_string(self.pkt_type, PacketConstants.INTEGER, 8)
        ret_string += handler.format_byte_string(self.pkt_id, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.advertising_router, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.sequence_number, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.checksum, PacketConstants.INTEGER, 16)
        ret_string += handler.format_byte_string(self.length, PacketConstants.INTEGER, 16)
        return ret_string


class OspfLinkStateAcknowledgePacketConstants:
    def __init__(self):
        pass

    LINKSTATEACKNOWLEDGE_NUMBER_OF_LSAS = "LINKSTATEACKNOWLEDGE_NUMBER_OF_LSAS"
    LINKSTATEACKNOWLEDGE_LSA_NUM = "LINKSTATEACKNOWLEDGE_LSA_NUM"

    LINKSTATEACKNOWLEDGE_LINK_STATE_AGE = "LINKSTATEACKNOWLEDGE_LINK_STATE_AGE"
    LINKSTATEACKNOWLEDGE_LINK_STATE_OPTIONS = "LINKSTATEACKNOWLEDGE_LINK_STATE_OPTIONS"
    LINKSTATEACKNOWLEDGE_LINK_STATE_TYPE = "LINKSTATEACKNOWLEDGE_LINK_STATE_TYPE"
    LINKSTATEACKNOWLEDGE_LINK_STATE_TYPE_ROUTER_LINKS = "1"
    LINKSTATEACKNOWLEDGE_LINK_STATE_TYPE_NETWORK_LINKS = "2"
    LINKSTATEACKNOWLEDGE_LINK_STATE_TYPE_SUMMARY_LINK_IP_NETWORK = "3"
    LINKSTATEACKNOWLEDGE_LINK_STATE_TYPE_SUMMARY_LINK_ASBR = "4"
    LINKSTATEACKNOWLEDGE_LINK_STATE_TYPE_AS_EXTERNAL_LINK = "5"
    LINKSTATEACKNOWLEDGE_LINK_STATE_TYPES = {1: "Router links",
                                             2: "Network links",
                                             3: "Summary link(IP network)",
                                             4: "Summary link(ASBR)",
                                             5: "AS external link"}

    LINKSTATEACKNOWLEDGE_LINK_STATE_ID = "LINKSTATEACKNOWLEDGE_LINK_STATE_ID"
    LINKSTATEACKNOWLEDGE_ADVERTISING_ROUTER = "LINKSTATEACKNOWLEDGE_ADVERTISING_ROUTER"
    LINKSTATEACKNOWLEDGE_SEQUENCE_NUMBER = "LINKSTATEACKNOWLEDGE_SEQUENCE_NUMBER"
    LINKSTATEACKNOWLEDGE_CHECKSUM = "LINKSTATEACKNOWLEDGE_CHECKSUM"
    LINKSTATEACKNOWLEDGE_LENGTH = "LINKSTATEACKNOWLEDGE_LENGTH"

    # don't allow values to be acknowledged
    def __setattr__(self, *_):
        pass
