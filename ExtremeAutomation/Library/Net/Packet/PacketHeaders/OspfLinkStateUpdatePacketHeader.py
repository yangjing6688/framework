from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfPacketHeader import OspfPacketHeader
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address


class OspfLinkStateUpdatePacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    OSPF LS Update Packet Header
        # Number of LSAs = 16bits
    """

    def __init__(self):
        self.add_linkstateupdate_header()
        self.num_lsa = 0
        self.lsa_entries = []
        self.set_lsa_num(0, True)
        self.HEADER_SIZE_LINKSTATEUPDATE = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start LinkStateUpdate Number of LSAs methods
    #  number_of_lsas is a 16 bit INTEGER example: 1
    def set_linkstateupdate_number_of_lsas(self, number_of_lsas, ignore_check=False):
        number_of_lsas = self.normalize_value(number_of_lsas, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_LINKSTATEUPDATE,
                                  OspfLinkStateUpdatePacketConstants.LINKSTATEUPDATE_NUMBER_OF_LSAS, number_of_lsas)

    def get_linkstateupdate_number_of_lsas(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_LINKSTATEUPDATE,
            OspfLinkStateUpdatePacketConstants.LINKSTATEUPDATE_NUMBER_OF_LSAS), PacketConstants.INTEGER)

    def get_linkstateupdate_number_of_lsas_hltapi_cmd(self, dummy_dict):
        number_of_lsas = self.get_linkstateupdate_number_of_lsas()
        if isinstance(number_of_lsas, int):
            number_of_lsas = str(number_of_lsas)
        if number_of_lsas and 'Not Set' not in number_of_lsas:
            dummy_dict[TrafficConfigConstants.TEMP_NUMBER_OF_LSAS_CMD] = number_of_lsas
    # end LinkStateUpdate Number of LSAs methods

    def get_lsa_num(self):
        return self.num_lsa

    def set_lsa_num(self, num_lsas, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(OspfLinkStateUpdatePacketConstants.LINKSTATEUPDATE_LSA_NUM,
                                                        ignore_check)
        self.num_lsa = NumberUtils.to_integer_value(num_lsas)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  OspfLinkStateUpdatePacketConstants.LINKSTATEUPDATE_LSA_NUM, num_lsas)

    def add_lsa_entry(self, entry):
        self.set_lsa_num(self.num_lsa + 1)
        self.lsa_entries.append(entry)
    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        rt_string = ""
        table = TableFormatter()
        table.add_row_value("Number of LSAs", self.format_int(self.get_linkstateupdate_number_of_lsas(), 4))

        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            rt_string += "\n\nAuth Crypt Data:" + self.get_ospf_auth_crypt_data()

        rt_string += "\n\nLINKSTATEUPDATE HEADER" + table.to_table_string()
        index = 0
        for entry in self.lsa_entries:
            index += 1
            assert isinstance(entry, OspfLinkStateLSAEntry)
            rt_string += "\n\n Link State Advertisement header #" + str(index) + "" + entry.to_packet_string()
        return rt_string

    def add_linkstateupdate_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_OSPF_LINKSTATEUPDATE)

    def build(self):
        self.add_linkstateupdate_header()
        self.set_ospf_message_type(0x04, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_linkstateupdate_number_of_lsas_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_linkstateupdate(self, tgen_type, generator_ref, port_string,
                                                                   stream_id, **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_linkstateupdate(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_linkstateupdate(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_linkstateupdate(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.klinkstateupdateFieldNumber
        # update this from the ostinato docs.
        # linkstateupdateField = p.Extensions[linkstateupdate]
        # if self.is_field_set(self.get_linkstateupdate_number_of_lsas()):
        #     linkstateupdateField.version = int(self.get_linkstateupdate_number_of_lsas())

    def config_jets_stream_linkstateupdate(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "LINKSTATEUPDATE_HDR"
        pkt_bytes = "0x" + OspfLinkStateUpdatePacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_linkstateupdate_number_of_lsas()):
            pkt_fields["number_of_lsas"] = int(self.get_linkstateupdate_number_of_lsas())

    def get_ixtclhal_linkstateupdate_api_commands(self, port_string, streamid):
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
        number_of_lsas = self.get_bits_from_string(32, payload)
        self.set_linkstateupdate_number_of_lsas("0x" + number_of_lsas)
        payload = self.remove_bits_from_string(32, payload)
        self.payload = payload
        self.parse_bytes_lsa()

    def parse_bytes_lsa(self):
        payload = self.payload
        number_of_lsas = self.get_linkstateupdate_number_of_lsas()
        while number_of_lsas > 0:
            number_of_lsas -= 1
            link_state_age = int(self.get_bits_from_string(16, payload), 16)
            # self.set_link_state_update_link_state_age("0x" + link_state_age)
            payload = self.remove_bits_from_string(16, payload)
            link_state_options = int(self.get_bits_from_string(8, payload), 16)
            # self.set_link_state_update_link_state_options("0x" + link_state_options)
            payload = self.remove_bits_from_string(8, payload)
            link_state_type = int(self.get_bits_from_string(8, payload), 16)
            # self.set_link_state_update_link_state_type("0x" + link_state_type)
            payload = self.remove_bits_from_string(8, payload)
            link_state_id = int(self.get_bits_from_string(32, payload), 16)
            # self.set_link_state_update_link_state_id("0x" + link_state_id)
            payload = self.remove_bits_from_string(32, payload)
            advertising_router = int(self.get_bits_from_string(32, payload), 16)
            # self.set_link_state_update_advertising_router("0x" + advertising_router)
            payload = self.remove_bits_from_string(32, payload)
            sequence_number = int(self.get_bits_from_string(32, payload), 16)
            # self.set_link_state_update_sequence_number("0x" + sequence_number)
            payload = self.remove_bits_from_string(32, payload)
            checksum = int(self.get_bits_from_string(16, payload), 16)
            # self.set_link_state_update_checksum("0x" + checksum)
            payload = self.remove_bits_from_string(16, payload)
            length = int(self.get_bits_from_string(16, payload), 16)
            # self.set_link_state_update_length("0x" + length)
            payload = self.remove_bits_from_string(16, payload)
            entry = None
            if link_state_type == 1:
                entry = OspfLinkStateLSATypeOneEntry(self, link_state_age, link_state_options, link_state_type,
                                                     link_state_id, advertising_router, sequence_number, checksum,
                                                     length, payload)
            elif link_state_type == 2:
                entry = OspfLinkStateLSATypeTwoEntry(self, link_state_age, link_state_options, link_state_type,
                                                     link_state_id, advertising_router, sequence_number, checksum,
                                                     length, payload)
            elif link_state_type == 3:
                entry = OspfLinkStateLSATypeThreeEntry(self, link_state_age, link_state_options, link_state_type,
                                                       link_state_id, advertising_router, sequence_number, checksum,
                                                       length, payload)
            elif link_state_type == 4:
                entry = OspfLinkStateLSATypeFourEntry(self, link_state_age, link_state_options, link_state_type,
                                                      link_state_id, advertising_router, sequence_number, checksum,
                                                      length, payload)
            elif link_state_type == 5:
                entry = OspfLinkStateLSATypeFiveEntry(self, link_state_age, link_state_options, link_state_type,
                                                      link_state_id, advertising_router, sequence_number, checksum,
                                                      length, payload)
            if entry:
                self.add_lsa_entry(entry)
                payload = entry.payload

        payload = OspfPacketHeader.process_auth_entry(payload, self)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_linkstateupdate_number_of_lsas(), PacketConstants.INTEGER, 32)

        # loop through the entries
        for entry in self.lsa_entries:
            assert isinstance(entry, OspfLinkStateLSAEntry)
            ret_string += entry.get_header_bytes()

        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            ret_string += self.get_bytes_auth_entry(self).replace("0x", "")
        return ret_string

    @staticmethod
    def compare_linkstateupdate_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, OspfLinkStateUpdatePacketHeader)
            assert isinstance(actual, OspfLinkStateUpdatePacketHeader)
            if expected.is_field_set(expected.get_linkstateupdate_number_of_lsas()) and \
                    OspfLinkStateUpdatePacketConstants.LINKSTATEUPDATE_NUMBER_OF_LSAS not in ignore_list:
                name = "LINKSTATEUPDATE number of lsas : "
                if expected.get_linkstateupdate_number_of_lsas() != actual.get_linkstateupdate_number_of_lsas():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_linkstateupdate_number_of_lsas()) + " != " +
                                                      str(actual.get_linkstateupdate_number_of_lsas()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_linkstateupdate_number_of_lsas()) + " == " +
                                                 str(actual.get_linkstateupdate_number_of_lsas()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with LinkStateUpdatePacketHeader")
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


class OspfLinkStateLSATypeOneEntry(OspfLinkStateLSAEntry):
    """
    LSA type 1
    http://www.freesoft.org/CIE/RFC/1583/111.htm

            0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |    0    |V|E|B|        0      |            # links            |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                          Link ID                              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                         Link Data                             |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |     Type      |     # TOS     |        TOS 0 metric           |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                              ...                              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |      TOS      |        0      |            metric             |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                          Link ID                              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                         Link Data                             |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                              ...                              |
    """

    def __init__(self, handler, age, option, pkt_type, pkt_id, advertising_router, sequence_number, checksum, length,
                 payload):
        super(OspfLinkStateLSATypeOneEntry, self).__init__(handler, age, option, pkt_type, pkt_id, advertising_router,
                                                           sequence_number, checksum, length)
        self.links = []
        self.flags = None
        self.num_links = None
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        size = 16
        self.flags = handler.get_bits_from_string(size, payload)
        self.flags = int(self.flags, 16)
        payload = handler.remove_bits_from_string(size, payload)
        size = 16
        self.num_links = handler.get_bits_from_string(size, payload)
        self.num_links = int(self.num_links, 16)
        payload = handler.remove_bits_from_string(size, payload)
        index = 0

        # links after index 0 might look different.
        while index < self.num_links:
            index += 1
            size = 32
            link_id = handler.get_bits_from_string(size, payload)
            link_id = int(link_id, 16)
            payload = handler.remove_bits_from_string(size, payload)
            size = 32
            link_data = handler.get_bits_from_string(size, payload)
            link_data = int(link_data, 16)
            payload = handler.remove_bits_from_string(size, payload)
            size = 8
            link_type = handler.get_bits_from_string(size, payload)
            payload = handler.remove_bits_from_string(size, payload)
            size = 8
            tos = handler.get_bits_from_string(size, payload)
            tos = int(tos, 16)
            payload = handler.remove_bits_from_string(size, payload)
            size = 16
            metric = handler.get_bits_from_string(size, payload)
            metric = int(metric, 16)
            payload = handler.remove_bits_from_string(size, payload)
            entry = OspfLinkStateLSATypeOneEntryLink(link_id, link_data, link_type, tos, metric)
            self.links.append(entry)
        self.payload = payload
        return payload

    def to_packet_string(self):
        rt_string = "LSA Type 1 (Router LSA)\n"
        rt_string += super(OspfLinkStateLSATypeOneEntry, self).to_packet_string()
        table_tlv = TableFormatter()
        packet = self.handler
        table_tlv.add_row_value("Flags", packet.format_int(self.flags, 2))
        table_tlv.add_row_value("Num Links", packet.format_int(self.num_links, 2))
        rt_string += table_tlv.to_table_string()
        index = 0
        table_tlv = TableFormatter()
        # links after index 0 might look different.
        for entry in self.links:
            index += 1
            table_tlv.add_row_value("#", index)
            table_tlv.add_row_value("Link ID", Ipv4Address(entry.link_id))
            table_tlv.add_row_value("Link Data", Ipv4Address(entry.link_data))
            table_tlv.add_row_value("Link Type", self.get_link_type_string(entry.link_type) + " - 0x" +
                                    str(entry.link_type))
            table_tlv.add_row_value("TOS", packet.format_int(entry.tos, 2))
            table_tlv.add_row_value("Metric", packet.format_int(entry.metrics, 2))
        rt_string += "\n\nLinks" + table_tlv.to_table_string()
        return rt_string

    def get_link_type_string(self, pkt_type):
        if isinstance(pkt_type, str):
            pkt_type = int(pkt_type, 16)
        if pkt_type == 0x01:
            return "PTP"
        elif pkt_type == 0x02:
            return "Transit"
        elif pkt_type == 0x03:
            return "Stub"
        elif pkt_type == 0x04:
            return "Virtual"
        else:
            return "Unknown"

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(OspfLinkStateLSATypeOneEntry, self).get_header_bytes()
        ret_string += handler.format_byte_string(self.flags, PacketConstants.INTEGER, 16)
        ret_string += handler.format_byte_string(self.num_links, PacketConstants.INTEGER, 16)
        # links after index 0 might look different.
        for entry in self.links:
            assert isinstance(entry, OspfLinkStateLSATypeOneEntryLink)
            ret_string += handler.format_byte_string(entry.link_id, PacketConstants.IPV4_ADDRESS, 32)
            ret_string += handler.format_byte_string(entry.link_data, PacketConstants.IPV4_ADDRESS, 32)
            ret_string += handler.format_byte_string(entry.link_type, PacketConstants.INTEGER, 8)
            ret_string += handler.format_byte_string(entry.tos, PacketConstants.INTEGER, 8)
            ret_string += handler.format_byte_string(entry.metrics, PacketConstants.INTEGER, 16)
        return ret_string


class OspfLinkStateLSATypeOneEntryLink(object):
    """
    http://www.freesoft.org/CIE/RFC/1583/111.htm
    LSA type 1
            0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                          Link ID                              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                         Link Data                             |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |     Type      |     # TOS     |        TOS 0 metric           |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """

    def __init__(self, link_id, link_data, link_type, tos, metrics):
        self.link_id = link_id
        self.link_data = link_data
        self.link_type = link_type
        self.tos = tos
        self.metrics = metrics


class OspfLinkStateLSATypeTwoEntry(OspfLinkStateLSAEntry):
    """
    http://www.freesoft.org/CIE/RFC/1583/112.htm
    LSA Type 2
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                         Network Mask                          |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                        Attached Router                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                              ...                              |
    """

    def __init__(self, handler, age, option, pkt_type, pkt_id, advertising_router, sequence_number, checksum, length,
                 payload):
        super(OspfLinkStateLSATypeTwoEntry, self).__init__(handler, age, option, pkt_type, pkt_id, advertising_router,
                                                           sequence_number, checksum, length)

        self.network_mask = None
        self.attached_routers = []
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        length = self.length - 24
        size = 32
        self.network_mask = handler.get_bits_from_string(size, payload)
        self.network_mask = int(self.network_mask, 16)
        payload = handler.remove_bits_from_string(size, payload)
        while length > 0:
            length -= 4
            size = 32
            attached_router = handler.get_bits_from_string(size, payload)
            attached_router = int(attached_router, 16)
            payload = handler.remove_bits_from_string(size, payload)
            self.attached_routers.append(attached_router)
        self.payload = payload
        return payload

    def to_packet_string(self):
        rt_string = "\nLSA Type 2 (Network LSA)\n"
        rt_string += super(OspfLinkStateLSATypeTwoEntry, self).to_packet_string()
        rt_string += "\nNetwork Mask: " + str(Ipv4Address(self.network_mask))
        index = 0
        for entry in self.attached_routers:
            index += 1
            rt_string += "\nAttached Router " + str(index) + ": " + str(Ipv4Address(entry))
        return rt_string

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(OspfLinkStateLSATypeTwoEntry, self).get_header_bytes()
        ret_string += handler.format_byte_string(self.network_mask, PacketConstants.INTEGER, 32)
        index = 0
        for entry in self.attached_routers:
            index += 1
            ret_string += handler.format_byte_string(entry, PacketConstants.INTEGER, 32)
        return ret_string


class OspfLinkStateLSATypeThreeEntry(OspfLinkStateLSAEntry):
    """
    http://www.freesoft.org/CIE/RFC/1583/113.htm
    LSA Type 3
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                         Network Mask                          |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |     TOS       |                  metric                       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    """

    def __init__(self, handler, age, option, pkt_type, pkt_id, advertising_router, sequence_number, checksum, length,
                 payload):
        super(OspfLinkStateLSATypeThreeEntry, self).__init__(handler, age, option, pkt_type, pkt_id, advertising_router,
                                                             sequence_number, checksum, length)

        self.network_mask = None
        self.tos = None
        self.metric = None
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        length = self.length - 24
        size = 32
        self.network_mask = handler.get_bits_from_string(size, payload)
        self.network_mask = int(self.network_mask, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 8
        self.tos = handler.get_bits_from_string(size, payload)
        self.tos = int(self.tos, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 24
        self.metric = handler.get_bits_from_string(size, payload)
        self.metric = int(self.metric, 16)
        payload = handler.remove_bits_from_string(size, payload)

        self.payload = payload
        return payload

    def to_packet_string(self):
        packet = self.handler
        rt_string = "\nLSA Type 3 (Summary-LSA (IP Network))\n"
        rt_string += super(OspfLinkStateLSATypeThreeEntry, self).to_packet_string()
        rt_string += "\nNetwork Mask: " + str(Ipv4Address(self.network_mask))
        rt_string += "\nTOS: " + packet.format_int(self.tos, 1)
        rt_string += "\nMetric: " + packet.format_int(self.metric, 3)
        return rt_string

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(OspfLinkStateLSATypeThreeEntry, self).get_header_bytes()
        ret_string += handler.format_byte_string(self.network_mask, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.tos, PacketConstants.INTEGER, 8)
        ret_string += handler.format_byte_string(self.metric, PacketConstants.INTEGER, 24)
        return ret_string


class OspfLinkStateLSATypeFourEntry(OspfLinkStateLSAEntry):
    """
    http://www.freesoft.org/CIE/RFC/1583/113.htm
    LSA Type 4
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                         Network Mask                          |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |     TOS       |                  metric                       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    """

    def __init__(self, handler, age, option, pkt_type, pkt_id, advertising_router, sequence_number, checksum, length,
                 payload):
        super(OspfLinkStateLSATypeFourEntry, self).__init__(handler, age, option, pkt_type, pkt_id, advertising_router,
                                                            sequence_number, checksum, length)

        self.network_mask = None
        self.tos = None
        self.metric = None
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        length = self.length - 24
        size = 32
        self.network_mask = handler.get_bits_from_string(size, payload)
        self.network_mask = int(self.network_mask, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 8
        self.tos = handler.get_bits_from_string(size, payload)
        self.tos = int(self.tos, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 24
        self.metric = handler.get_bits_from_string(size, payload)
        self.metric = int(self.metric, 16)
        payload = handler.remove_bits_from_string(size, payload)

        self.payload = payload
        return payload

    def to_packet_string(self):
        packet = self.handler
        rt_string = "\nLSA Type 4 (Summary-LSA (ASBR))\n"
        rt_string += super(OspfLinkStateLSATypeFourEntry, self).to_packet_string()
        rt_string += "\nNetwork Mask: " + str(Ipv4Address(self.network_mask))
        rt_string += "\nTOS: " + packet.format_int(self.tos, 1)
        rt_string += "\nMetric: " + packet.format_int(self.metric, 3)
        return rt_string

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(OspfLinkStateLSATypeFourEntry, self).get_header_bytes()
        ret_string += handler.format_byte_string(self.network_mask, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.tos, PacketConstants.INTEGER, 8)
        ret_string += handler.format_byte_string(self.metric, PacketConstants.INTEGER, 24)
        return ret_string


class OspfLinkStateLSATypeFiveEntry(OspfLinkStateLSAEntry):
    """
    http://www.freesoft.org/CIE/RFC/1583/114.htm
    LSA Type 5
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                         Network Mask                          |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |E|    TOS      |                  metric                       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                      Forwarding address                       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                      External Route Tag                       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                              ...                              |
    """

    def __init__(self, handler, age, option, pkt_type, pkt_id, advertising_router, sequence_number, checksum, length,
                 payload):
        super(OspfLinkStateLSATypeFiveEntry, self).__init__(handler, age, option, pkt_type, pkt_id, advertising_router,
                                                            sequence_number, checksum, length)

        self.network_mask = None
        self.tos = None
        self.metric = None
        self.forwarding_address = None
        self.external_route_tag = None
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        length = self.length - 24
        size = 32
        self.network_mask = handler.get_bits_from_string(size, payload)
        self.network_mask = int(self.network_mask, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 8
        self.tos = handler.get_bits_from_string(size, payload)
        self.tos = int(self.tos, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 24
        self.metric = handler.get_bits_from_string(size, payload)
        self.metric = int(self.metric, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 32
        self.forwarding_address = handler.get_bits_from_string(size, payload)
        self.forwarding_address = int(self.forwarding_address, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 32
        self.external_route_tag = handler.get_bits_from_string(size, payload)
        self.external_route_tag = int(self.external_route_tag, 16)
        payload = handler.remove_bits_from_string(size, payload)

        self.payload = payload
        return payload

    def to_packet_string(self):
        packet = self.handler
        rt_string = "\nLSA Type 5 (AS-External-LSA (ASBR))\n"
        rt_string += super(OspfLinkStateLSATypeFiveEntry, self).to_packet_string()
        rt_string += "\nNetwork Mask: " + str(Ipv4Address(self.network_mask))
        rt_string += "\nTOS: " + packet.format_int(self.tos, 1)
        rt_string += "\nMetric: " + packet.format_int(self.metric, 3)
        rt_string += "\nForwarding Address: " + str(Ipv4Address(self.forwarding_address))
        rt_string += "\nExternal Route Tag: " + str(self.external_route_tag)
        return rt_string

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(OspfLinkStateLSATypeFiveEntry, self).get_header_bytes()
        ret_string += handler.format_byte_string(self.network_mask, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.tos, PacketConstants.INTEGER, 8)
        ret_string += handler.format_byte_string(self.metric, PacketConstants.INTEGER, 24)
        ret_string += handler.format_byte_string(self.forwarding_address, PacketConstants.INTEGER, 32)
        ret_string += handler.format_byte_string(self.external_route_tag, PacketConstants.INTEGER, 32)
        return ret_string


class OspfLinkStateUpdatePacketConstants:
    def __init__(self):
        pass

    LINKSTATEUPDATE_NUMBER_OF_LSAS = "LINKSTATEUPDATE_NUMBER_OF_LSAS"
    LINKSTATEUPDATE_LSA_NUM = "LINKSTATEUPDATE_LSA_NUM"

    LINKSTATEUPDATE_LINK_STATE_AGE = "LINKSTATEUPDATE_LINK_STATE_AGE"

    LINKSTATEUPDATE_LINK_STATE_OPTIONS = "LINKSTATEUPDATE_LINK_STATE_OPTIONS"

    LINKSTATEUPDATE_LINK_STATE_TYPE = "LINKSTATEUPDATE_LINK_STATE_TYPE"
    LINKSTATEUPDATE_LINK_STATE_TYPE_ROUTER_LINKS = "1"
    LINKSTATEUPDATE_LINK_STATE_TYPE_NETWORK_LINKS = "2"
    LINKSTATEUPDATE_LINK_STATE_TYPE_SUMMARY_LINK_IP_NETWORK = "3"
    LINKSTATEUPDATE_LINK_STATE_TYPE_SUMMARY_LINK_ASBR = "4"
    LINKSTATEUPDATE_LINK_STATE_TYPE_AS_EXTERNAL_LINK = "5"
    LINKSTATEUPDATE_LINK_STATE_TYPES = {1: "Router links",
                                        2: "Network links",
                                        3: "Summary link(IP network)",
                                        4: "Summary link(ASBR)",
                                        5: "AS external link"}

    LINKSTATEUPDATE_LINK_STATE_ID = "LINKSTATEUPDATE_LINK_STATE_ID"
    LINKSTATEUPDATE_ADVERTISING_ROUTER = "LINKSTATEUPDATE_ADVERTISING_ROUTER"
    LINKSTATEUPDATE_SEQUENCE_NUMBER = "LINKSTATEUPDATE_SEQUENCE_NUMBER"
    LINKSTATEUPDATE_CHECKSUM = "LINKSTATEUPDATE_CHECKSUM"
    LINKSTATEUPDATE_LENGTH = "LINKSTATEUPDATE_LENGTH"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
