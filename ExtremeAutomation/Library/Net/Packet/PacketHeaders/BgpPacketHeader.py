from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb


class BgpPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    BGP Packet Header
        # Marker = 128bits
        # Length = 16bits
        # Type = 8bits
    """

    def __init__(self):
        self.add_bgp_header()
        self.num_bgp_entries = 0
        self.bgp_entries = []
        self.set_bgp_entry_num(0, True)
        self.HEADER_SIZE_BGP = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################
    #
    # # start Bgp Marker methods
    # #  marker is a 128 bit INTEGER example: 1
    # def set_bgp_marker(self,marker, ignore_check=False):
    #     marker = self.normalize_value(marker, PacketConstants.INTEGER)
    #     self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BGP, BgpPacketConstants.BGP_MARKER, marker)
    #
    # def get_bgp_marker(self):
    #     return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L5_BGP,
    #                                                           BgpPacketConstants.BGP_MARKER), PacketConstants.INTEGER)
    #
    # def get_bgp_marker_hltapi_cmd(self, dummy_dict):
    #     marker = self.get_bgp_marker()
    #     if isinstance(marker, int):
    #         marker = str(marker)
    #     if marker and 'Not Set' not in marker:
    #         dummy_dict[TrafficConfigConstants.TEMP_MARKER_CMD] = marker
    # # end Bgp Marker methods
    #
    # # start Bgp Length methods
    # #  length is a 16 bit INTEGER example: 1
    # def set_bgp_length(self,length, ignore_check=False):
    #     length = self.normalize_value(length, PacketConstants.INTEGER)
    #     self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BGP, BgpPacketConstants.BGP_LENGTH, length)
    #
    # def get_bgp_length(self):
    #     return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L5_BGP,
    #                                                           BgpPacketConstants.BGP_LENGTH), PacketConstants.INTEGER)
    #
    # def get_bgp_length_hltapi_cmd(self, dummy_dict):
    #     length = self.get_bgp_length()
    #     if isinstance(length, int):
    #         length = str(length)
    #     if length and 'Not Set' not in length:
    #         dummy_dict[TrafficConfigConstants.TEMP_LENGTH_CMD] = length
    # # end Bgp Length methods
    #
    # # start Bgp Type methods
    # #  type is a 8 bit INTEGER example: 1
    # def set_bgp_type(self, pkt_type, ignore_check=False):
    #     type = self.normalize_value(type, PacketConstants.INTEGER)
    #     self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BGP, BgpPacketConstants.BGP_TYPE, type)
    #
    # def get_bgp_type(self):
    #     return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L5_BGP,
    #                                                           BgpPacketConstants.BGP_TYPE), PacketConstants.INTEGER)
    #
    # def get_bgp_type_hltapi_cmd(self, dummy_dict):
    #     pkt_type = self.get_bgp_type()
    #     if isinstance(type, int):
    #         pkt_type = str(pkt_type)
    #     if type and 'Not Set' not in type:
    #         dummy_dict[TrafficConfigConstants.TEMP_TYPE_CMD] = pkt_type
    # # end Bgp Type methods

    def get_bgp_entry_num(self):
        return self.num_bgp_entries

    def set_bgp_entry_num(self, num_bgp_entries, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BgpPacketConstants.BGP_ENTRY_NUM, ignore_check)
        self.num_bgp_entries = NumberUtils.to_integer_value(num_bgp_entries)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_BGP, BgpPacketConstants.BGP_ENTRY_NUM,
                                  num_bgp_entries)

    def add_bgp_entry(self, entry):
        self.set_bgp_entry_num(self.num_bgp_entries + 1)
        self.bgp_entries.append(entry)

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        rt_string = ""
        index = 0
        for entry in self.bgp_entries:
            index += 1
            assert isinstance(entry, BgpEntry)
            rt_string += "\n\n BGP Header #" + str(index) + "\n" + entry.to_packet_string()
        return rt_string

    def add_bgp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_BGP)

    def build(self):
        self.add_bgp_header()
        self.set_source_port(179, True)
        self.set_destination_port(179, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_bgp_marker_hltapi_cmd(dummy_dict)
        # self.get_bgp_length_hltapi_cmd(dummy_dict)
        # self.get_bgp_type_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_bgp(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_bgp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_bgp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_bgp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kbgpFieldNumber
    # update this from the ostinato docs.
    #     bgpField = p.Extensions[bgp]
        # if self.is_field_set(self.get_bgp_marker()):
        #     bgpField.version = int(self.get_bgp_marker())
        # if self.is_field_set(self.get_bgp_length()):
        #     bgpField.version = int(self.get_bgp_length())
        # if self.is_field_set(self.get_bgp_type()):
        #     bgpField.version = int(self.get_bgp_type())

    def config_jets_stream_bgp(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "BGP_HDR"
        pkt_bytes = "0x" + BgpPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_bgp_marker()):
        #     pkt_fields["marker"] = int(self.get_bgp_marker())
        # if self.is_field_set(self.get_bgp_length()):
        #     pkt_fields["length"] = int(self.get_bgp_length())
        # if self.is_field_set(self.get_bgp_type()):
        #     pkt_fields["type"] = int(self.get_bgp_type())

    def get_ixtclhal_bgp_api_commands(self, port_string, streamid):
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

        while len(payload) > 0:
            marker = self.get_bits_from_string(128, payload)
            # self.set_bgp_marker("0x" + marker)
            payload = self.remove_bits_from_string(128, payload)
            length = self.get_bits_from_string(16, payload)
            length = NumberUtils.to_integer_value("0x" + length)
            # self.set_bgp_length("0x" + length)
            payload = self.remove_bits_from_string(16, payload)
            tgen_type = self.get_bits_from_string(8, payload)
            tgen_type = NumberUtils.to_integer_value("0x" + tgen_type)
            # self.set_bgp_type("0x" + type)
            payload = self.remove_bits_from_string(8, payload)
            tgen_type = NumberUtils.to_integer_value(tgen_type)
            entry = None
            if tgen_type == 1:
                entry = BgpOpenMessageEntry(self, marker, tgen_type, length, payload)
            elif tgen_type == 2:
                entry = BgpUpdateMessageEntry(self, marker, tgen_type, length, payload)
            elif tgen_type == 3:
                entry = BgpNotificationMessageEntry(self, marker, tgen_type, length, payload)
            elif tgen_type == 4:
                entry = BgpKeepaliveMessageEntry(self, marker, tgen_type, length, payload)
            elif tgen_type == 5:
                entry = BgpRouteRefreshMessageEntry(self, marker, tgen_type, length, payload)
            if entry:
                self.add_bgp_entry(entry)
                payload = entry.payload

        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        index = 0
        for entry in self.bgp_entries:
            index += 1
            assert isinstance(entry, BgpEntry)
            ret_string += entry.get_header_bytes()
        return ret_string

    @staticmethod
    def compare_bgp_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, BgpPacketHeader)
            assert isinstance(actual, BgpPacketHeader)
            if expected.is_field_set(expected.get_bgp_marker()) and BgpPacketConstants.BGP_MARKER not in ignore_list:
                name = "BGP marker : "
                if expected.get_bgp_marker() != actual.get_bgp_marker():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bgp_marker()) + " != " +
                                                      str(actual.get_bgp_marker()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bgp_marker()) + " == " +
                                                 str(actual.get_bgp_marker()) + " Pass")

            if expected.is_field_set(expected.get_bgp_length()) and BgpPacketConstants.BGP_LENGTH not in ignore_list:
                name = "BGP length : "
                if expected.get_bgp_length() != actual.get_bgp_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bgp_length()) + " != " +
                                                      str(actual.get_bgp_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bgp_length()) + " == " +
                                                 str(actual.get_bgp_length()) + " Pass")

            if expected.is_field_set(expected.get_bgp_type()) and BgpPacketConstants.BGP_TYPE not in ignore_list:
                name = "BGP type : "
                if expected.get_bgp_type() != actual.get_bgp_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_bgp_type()) + " != " +
                                                      str(actual.get_bgp_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bgp_type()) + " == " +
                                                 str(actual.get_bgp_type()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with BgpPacketHeader")
        return results


class BgpEntry(object):
    def __init__(self, handler, marker, pkt_type, length):
        self.handler = handler
        # these have to be in decimal so convert them from hex first.
        self.marker = marker
        self.pkt_type = pkt_type
        self.length = length
        self.type_string = self.get_type_string(pkt_type)

    def get_type_string(self, pkt_type):
        if pkt_type == 0x01:
            return "OPEN Message"
        elif pkt_type == 0x02:
            return "UPDATE Message"
        elif pkt_type == 0x03:
            return "NOTIFICATION Message"
        elif pkt_type == 0x04:
            return "KEEPALIVE Message"
        elif pkt_type == 0x05:
            return "ROUTE-REFRESH Message"
        else:
            return "Unknown Type"

    def to_packet_string(self):
        table_tlv = TableFormatter()
        packet = self.handler
        table_tlv.add_row_value("Marker", self.marker)
        table_tlv.add_row_value("Length", packet.format_int(self.length, 2))
        table_tlv.add_row_value("Type", self.type_string + " " + packet.format_int(self.pkt_type, 1))
        return table_tlv.to_table_string()

    def get_header_bytes(self):
        ret_string = ""
        handler = self.handler
        ret_string += handler.format_byte_string(self.marker, PacketConstants.HEX_STRING, 16 * 8)
        ret_string += handler.format_byte_string(self.length, PacketConstants.INTEGER, 16)
        ret_string += handler.format_byte_string(self.pkt_type, PacketConstants.INTEGER, 8)
        return ret_string


class BgpOpenMessageEntry(BgpEntry):
    def __init__(self, handler, marker, pkt_type, length, payload):
        super(BgpOpenMessageEntry, self).__init__(handler, marker, pkt_type, length)
        self.version = None
        self.my_as = None
        self.hold_time = None
        self.bgp_id = None
        self.optional_paramenters_length = None
        self.optional_paramenters = None
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        size = 8
        self.version = handler.get_bits_from_string(size, payload)
        self.version = int(self.version, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 16
        self.my_as = handler.get_bits_from_string(size, payload)
        self.my_as = int(self.my_as, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 16
        self.hold_time = handler.get_bits_from_string(size, payload)
        self.hold_time = int(self.hold_time, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 32
        self.bgp_id = handler.get_bits_from_string(size, payload)
        self.bgp_id = int(self.bgp_id, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 8
        self.optional_paramenters_length = handler.get_bits_from_string(size, payload)
        self.optional_paramenters_length = int(self.optional_paramenters_length, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = self.optional_paramenters_length * 8 * 2
        self.optional_paramenters = handler.get_bits_from_string(size, payload)
        payload = handler.remove_bits_from_string(size, payload)

        self.payload = payload
        return payload

    def to_packet_string(self):
        rt_string = "OPEN Message\n"
        rt_string += super(BgpOpenMessageEntry, self).to_packet_string()
        table_tlv = TableFormatter()
        packet = self.handler
        table_tlv.add_row_value("Version", packet.format_int(self.version, 1))
        table_tlv.add_row_value("My AS", packet.format_int(self.my_as, 2))
        table_tlv.add_row_value("Hold Time", packet.format_int(self.hold_time, 2))
        table_tlv.add_row_value("BGP Identifier", Ipv4Address(self.bgp_id))
        table_tlv.add_row_value("Optional Paramenters Length", packet.format_int(self.optional_paramenters_length, 1))
        table_tlv.add_row_value("Optional Paramenters", self.optional_paramenters)
        rt_string += table_tlv.to_table_string()
        return rt_string

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(BgpOpenMessageEntry, self).get_header_bytes()
        ret_string += handler.format_byte_string(self.version, PacketConstants.INTEGER, 1 * 8)
        ret_string += handler.format_byte_string(self.my_as, PacketConstants.INTEGER, 2 * 8)
        ret_string += handler.format_byte_string(self.hold_time, PacketConstants.INTEGER, 2 * 8)
        ret_string += handler.format_byte_string(Ipv4Address.to_long(Ipv4Address(self.bgp_id)),
                                                 PacketConstants.INTEGER, 4 * 8)
        ret_string += handler.format_byte_string(self.optional_paramenters_length, PacketConstants.INTEGER, 1 * 8)
        length = NumberUtils.to_integer_value(self.optional_paramenters_length)
        ret_string += handler.format_byte_string(self.optional_paramenters, PacketConstants.HEX_STRING, length * 8)
        return ret_string


class BgpUpdateMessageEntry(BgpEntry):
    def __init__(self, handler, marker, pkt_type, length, payload):
        super(BgpUpdateMessageEntry, self).__init__(handler, marker, pkt_type, length)
        self.withdrawn_routes_length = None
        self.total_path_attribute_length = None
        self.path_attributes = None
        self.network_layer_reachability_information = None
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        size = 16
        self.withdrawn_routes_length = handler.get_bits_from_string(size, payload)
        self.withdrawn_routes_length = int(self.withdrawn_routes_length, 16)
        payload = handler.remove_bits_from_string(size, payload)

        size = 16
        self.total_path_attribute_length = handler.get_bits_from_string(size, payload)
        self.total_path_attribute_length = int(self.total_path_attribute_length, 16)
        payload = handler.remove_bits_from_string(size, payload)

        # look for the next marker or the end of the packet.
        if "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" in payload.upper():
            index = payload.upper().index("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
            temp = payload[:index]
            self.path_attributes = temp[:self.total_path_attribute_length * 2]
            self.network_layer_reachability_information = temp[self.total_path_attribute_length * 2:]
            payload = payload[index:]
        else:
            self.path_attributes = payload
            self.network_layer_reachability_information = ""
            payload = ""
        self.payload = payload
        return payload

    def to_packet_string(self):
        rt_string = "UPDATE Message\n"
        rt_string += super(BgpUpdateMessageEntry, self).to_packet_string()
        table_tlv = TableFormatter()
        packet = self.handler
        table_tlv.add_row_value("Withdrawn Routes Length", packet.format_int(self.withdrawn_routes_length, 2))
        table_tlv.add_row_value("Total Path Attribute Length", packet.format_int(self.total_path_attribute_length, 2))
        table_tlv.add_row_value("Path Attributes", self.path_attributes)
        table_tlv.add_row_value("Network Layer Reachability Information", self.network_layer_reachability_information)
        rt_string += table_tlv.to_table_string()
        return rt_string

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(BgpUpdateMessageEntry, self).get_header_bytes()
        ret_string += handler.format_byte_string(self.withdrawn_routes_length, PacketConstants.INTEGER, 2 * 8)
        ret_string += handler.format_byte_string(self.total_path_attribute_length, PacketConstants.INTEGER, 2 * 8)
        length = len(self.path_attributes)
        ret_string += handler.format_byte_string(self.path_attributes, PacketConstants.HEX_STRING, length)
        length = len(self.network_layer_reachability_information)
        ret_string += handler.format_byte_string(self.network_layer_reachability_information,
                                                 PacketConstants.HEX_STRING, length)
        return ret_string


class BgpRouteRefreshMessageEntry(BgpEntry):
    def __init__(self, handler, marker, pkt_type, length, payload):
        super(BgpRouteRefreshMessageEntry, self).__init__(handler, marker, pkt_type, length)
        self.address_family_id = None
        self.subtype = None
        self.subsequent_address_family_id = None
        self.orf_information = None
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        size = 16
        self.address_family_id = handler.get_bits_from_string(size, payload)
        self.address_family_id = int(self.address_family_id, 16)
        payload = handler.remove_bits_from_string(size, payload)
        size = 8
        self.subtype = handler.get_bits_from_string(size, payload)
        self.subtype = int(self.subtype, 16)
        payload = handler.remove_bits_from_string(size, payload)
        size = 8
        self.subsequent_address_family_id = handler.get_bits_from_string(size, payload)
        self.subsequent_address_family_id = int(self.subsequent_address_family_id, 16)
        payload = handler.remove_bits_from_string(size, payload)

        orf_length = self.length - 23
        self.orf_information = None
        if orf_length > 0:
            size = 8 * orf_length
            self.orf_information = handler.get_bits_from_string(size, payload)
            payload = handler.remove_bits_from_string(size, payload)

        self.payload = payload
        return payload

    def to_packet_string(self):
        rt_string = "ROUTE-REFRESH Message\n"
        rt_string += super(BgpRouteRefreshMessageEntry, self).to_packet_string()
        table_tlv = TableFormatter()
        packet = self.handler
        table_tlv.add_row_value("Address Family ID", packet.format_int(self.address_family_id, 2))
        table_tlv.add_row_value("Subtype", packet.format_int(self.subtype, 1))
        table_tlv.add_row_value("Subsequent Address Family ID", packet.format_int(self.subsequent_address_family_id, 1))
        if self.orf_information:
            table_tlv.add_row_value("ORF Information", self.orf_information)
        rt_string += table_tlv.to_table_string()
        return rt_string

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(BgpRouteRefreshMessageEntry, self).get_header_bytes()
        ret_string += handler.format_byte_string(self.address_family_id, PacketConstants.INTEGER, 2 * 8)
        ret_string += handler.format_byte_string(self.subtype, PacketConstants.INTEGER, 1 * 8)
        ret_string += handler.format_byte_string(self.subsequent_address_family_id, PacketConstants.INTEGER, 1 * 8)
        if self.orf_information:
            ret_string += handler.format_byte_string(self.orf_information, PacketConstants.HEX_STRING, 8)
        return ret_string


class BgpNotificationMessageEntry(BgpEntry):
    def __init__(self, handler, marker, pkt_type, length, payload):
        super(BgpNotificationMessageEntry, self).__init__(handler, marker, pkt_type, length)
        self.major_error_code = None
        self.minor_error_code = None
        self.data = None
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        size = 8
        self.major_error_code = handler.get_bits_from_string(size, payload)
        self.major_error_code = NumberUtils.to_integer_value("0x" + self.major_error_code)
        payload = handler.remove_bits_from_string(size, payload)
        size = 8
        self.minor_error_code = handler.get_bits_from_string(size, payload)
        self.minor_error_code = NumberUtils.to_integer_value("0x" + self.minor_error_code)
        payload = handler.remove_bits_from_string(size, payload)

        if "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" in payload.upper():
            index = payload.upper().index("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
            self.data = payload[:index]
            payload = payload[index:]
        else:
            self.data = payload
            payload = ""
        self.payload = payload
        return payload

    def to_packet_string(self):
        rt_string = "NOTIFICATION Message\n"
        rt_string += super(BgpNotificationMessageEntry, self).to_packet_string()
        table_tlv = TableFormatter()
        packet = self.handler
        table_tlv.add_row_value("Major Error Code", packet.format_int(self.major_error_code, 1))
        table_tlv.add_row_value("Minor Error Code", packet.format_int(self.minor_error_code, 1))
        table_tlv.add_row_value("Data", self.data)
        rt_string += table_tlv.to_table_string()
        return rt_string

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(BgpNotificationMessageEntry, self).get_header_bytes()
        ret_string += handler.format_byte_string(self.major_error_code, PacketConstants.INTEGER, 1 * 8)
        ret_string += handler.format_byte_string(self.minor_error_code, PacketConstants.INTEGER, 1 * 8)
        ret_string += handler.format_byte_string(self.data, PacketConstants.HEX_STRING, 0)
        return ret_string


class BgpKeepaliveMessageEntry(BgpEntry):
    def __init__(self, handler, marker, pkt_type, length, payload):
        super(BgpKeepaliveMessageEntry, self).__init__(handler, marker, pkt_type, length)
        self.parse_payload(payload)

    def parse_payload(self, payload):
        handler = self.handler
        self.payload = payload
        return payload

    def to_packet_string(self):
        rt_string = "KEEPALIVE Message\n"
        rt_string += super(BgpKeepaliveMessageEntry, self).to_packet_string()
        return rt_string

    def get_header_bytes(self):
        handler = self.handler
        ret_string = super(BgpKeepaliveMessageEntry, self).get_header_bytes()
        return ret_string


class BgpPacketConstants:
    def __init__(self):
        pass

    BGP_MARKER = "BGP_MARKER"

    BGP_LENGTH = "BGP_LENGTH"

    BGP_TYPE = "BGP_TYPE"
    BGP_TYPE_RESERVED = "0"
    BGP_TYPE_OPEN = "1"
    BGP_TYPE_UPDATE = "2"
    BGP_TYPE_NOTIFICATION = "3"
    BGP_TYPE_KEEPALIVE = "4"
    BGP_TYPE_ROUTE_REFRESH = "5"
    BGP_TYPES = {0: "Reserved",
                 1: "OPEN",
                 2: "UPDATE",
                 3: "NOTIFICATION",
                 4: "KEEPALIVE",
                 5: "ROUTE-REFRESH"}

    BGP_ENTRY_NUM = "BGP_ENTRY_NUM"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
