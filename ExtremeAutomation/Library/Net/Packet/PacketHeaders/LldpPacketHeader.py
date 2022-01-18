import re
import binascii
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import SnapPacketHeader
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject, PacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class LldpPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    LLDP Packet Header
        # version = 4bits
        # traffic class = 8bits
    """

    def __init__(self):
        self.add_lldp_header()
        self.set_lldp_entries_num(0)

    def get_lldp_entries_num(self):
        return self.num_lldp_entries

    def set_lldp_entries_num(self, num_lldp):
        self.num_lldp_entries = NumberUtils.to_integer_value(num_lldp)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_LLDP,
                                  LldpPacketConstants.LLDP_TLV_ENTERY_NUM,
                                  num_lldp)

    def add_lldp_entry(self, tlv_type=None):
        self.set_lldp_entries_num(self.num_lldp_entries + 1)
        if tlv_type is not None:
            self.set_lldp_tlv_type(tlv_type, self.num_lldp_entries)

        return self.num_lldp_entries

    def get_lldp_headers_length(self):
        extension_length = 0
        index = 1
        while index <= self.get_lldp_entries_num():
            extension_length += 2 + self.get_lldp_tlv_length(index)
            index += 1
        return extension_length

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Lldp TLV TYPE methods
    #  version is a 3 bit INTEGER example: 1
    def set_lldp_tlv_type(self, version, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(LldpPacketConstants.LLDP_TLV_TYPE + " " + str(mstid_id),
                                                        ignore_check)
        flag = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_LLDP,
                                  LldpPacketConstants.LLDP_TLV_TYPE + " " + str(mstid_id),
                                  flag)

    def get_lldp_tlv_type(self, mstid_id):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_LLDP, LldpPacketConstants.LLDP_TLV_TYPE + " " + str(mstid_id)),
            PacketConstants.INTEGER)

    def get_lldp_tlv_type_hltapi_cmd(self, dummy_dict):
        version = self.get_lldp_tlv_type()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_TLV_TYPE_CMD] = version
    # end Lldp TLV TYPE methods

    # start Lldp TLV LENGTH  methods
    #  version is a 9 bit INTEGER example: 1
    def set_lldp_tlv_length(self, version, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(LldpPacketConstants.LLDP_TLV_LENGTH + " " + str(mstid_id),
                                                        ignore_check)
        flag = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_LLDP,
                                  LldpPacketConstants.LLDP_TLV_LENGTH + " " + str(mstid_id),
                                  flag)

    def get_lldp_tlv_length(self, mstid_id):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_LLDP, LldpPacketConstants.LLDP_TLV_LENGTH + " " + str(mstid_id)),
            PacketConstants.INTEGER)

    def get_lldp_tlv_length_hltapi_cmd(self, dummy_dict):
        version = self.get_lldp_tlv_length()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_TLV_LENGTH_CMD] = version
    # end Lldp TLV LENGTH methods

    # start Lldp TLV Message  methods
    #  version is a 9 bit INTEGER example: 1
    def set_lldp_tlv_message(self, version, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(LldpPacketConstants.LLDP_TLV_MESSAGE + " " + str(mstid_id),
                                                        ignore_check)
        flag = version
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_LLDP,
                                  LldpPacketConstants.LLDP_TLV_MESSAGE + " " + str(mstid_id),
                                  flag)

    def get_lldp_tlv_message(self, mstid_id):
        return self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_LLDP, LldpPacketConstants.LLDP_TLV_MESSAGE + " " + str(mstid_id))

    def get_lldp_tlv_message_hex(self, mstid_id):
        pkt_type = self.get_lldp_tlv_type(mstid_id)
        length = self.get_lldp_tlv_length(mstid_id)
        message = self.get_lldp_tlv_message(mstid_id)
        return LldpPacketHeader.convert_mesage_to_hex(pkt_type, length, message)

    def get_lldp_tlv_message_hltapi_cmd(self, dummy_dict):
        version = self.get_lldp_tlv_message()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_TLV_message_CMD] = version
    # end Lldp TLV LENGTH methods

    # example: packet.add_lldp_tlv_chassis_subtype("00:18:ba:98:68:Bf")
    def add_lldp_tlv_chassis_subtype(self, chassis_mac, pkt_type=0x01, length=None):
        index = self.add_lldp_entry(pkt_type)
        raw = "04," + str(EnetAddress(chassis_mac))
        length = length if (length is not None) else 1 + (len(chassis_mac.replace(":", "")) / 2)
        self.set_lldp_tlv_length(length, index)
        self.set_lldp_tlv_message("04," + str(EnetAddress(chassis_mac)), index)

    # example: packet.add_lldp_tlv_port_subtype("Fa0/13")
    def add_lldp_tlv_port_subtype(self, port, pkt_type=0x02, length=None):
        index = self.add_lldp_entry(pkt_type)
        length = length if (length is not None) else 1 + len(port)
        self.set_lldp_tlv_length(length, index)
        self.set_lldp_tlv_message("05," + port, index)

    # example: packet.add_lldp_tlv_time_to_live(120)
    def add_lldp_tlv_time_to_live(self, ttl, pkt_type=0x03, length=None):
        index = self.add_lldp_entry(pkt_type)
        self.set_lldp_tlv_length(length if (length is not None) else 0x02, index)
        if isinstance(ttl, int):
            ttl = hex(ttl)[2:]
        ttl = ttl.zfill(4)
        self.set_lldp_tlv_message(ttl, index)

    # example: packet.add_lldp_tlv_system_name("S1.cisco.com")
    def add_lldp_tlv_system_name(self, sys_name, pkt_type=0x05, length=None):
        index = self.add_lldp_entry(pkt_type)
        self.set_lldp_tlv_length(length if (length is not None) else len(sys_name), index)
        self.set_lldp_tlv_message(sys_name, index)

    # example: packet.add_lldp_tlv_system_description("436973636f20494f5320536f6674776172652c20433335363020536f667477617
    # 265202843333536302d414456495053455256494345534b392d4d292c2056657273696f6e2031322e322834342953452c2052454c454153452
    # 0534f4654574152452028666331290a436f707972696768742028632920313938362d3230303820627920436973636f2053797374656d732c2
    # 0496e632e0a436f6d70696c6564205361742030352d4a616e2d30382030303a3135206279207765696c6975".decode('hex'))

    # example: packet.add_lldp_tlv_system_description("blahblahblahblahblahblah something about the
    # system \nmore more more")
    def add_lldp_tlv_system_description(self, sys_desc, pkt_type=0x06, length=None):
        index = self.add_lldp_entry(pkt_type)
        self.set_lldp_tlv_length(length if (length is not None) else len(sys_desc), index)
        self.set_lldp_tlv_message(sys_desc, index)

    # example: packet.add_lldp_tlv_port_description("FastEthernet0/13")
    def add_lldp_tlv_port_description(self, port_desc, pkt_type=0x04, length=None):
        index = self.add_lldp_entry(pkt_type)
        self.set_lldp_tlv_length(length if (length is not None) else len(port_desc), index)
        self.set_lldp_tlv_message(port_desc, index)

    # example: packet.add_lldp_tlv_capabilities([0x00,0x14,0x00,0x04])
    def add_lldp_tlv_capabilities(self, caps, pkt_type=0x07, length=None):
        index = self.add_lldp_entry(pkt_type)
        temp = LldpPacketHeader.convert_mesage_to_hex(pkt_type, None, caps)
        self.set_lldp_tlv_length(length if (length is not None) else len(temp) / 2, index)
        self.set_lldp_tlv_message(caps, index)

    # example: packet.add_lldp_tlv_ieee_802_1_portvlan("0x0080c2010001")
    def add_lldp_tlv_ieee_802_1_portvlan(self, caps, pkt_type=127, length=None):
        index = self.add_lldp_entry(pkt_type)
        temp = LldpPacketHeader.convert_mesage_to_hex(pkt_type, None, caps)
        self.set_lldp_tlv_length(length if (length is not None) else len(temp) / 2, index)
        self.set_lldp_tlv_message(caps, index)

    # example: packet.add_lldp_tlv_ieee_802_3_mc_phy_config("00120f010300360010")
    def add_lldp_tlv_ieee_802_3_mc_phy_config(self, caps, pkt_type=127, length=None):
        index = self.add_lldp_entry(pkt_type)
        temp = LldpPacketHeader.convert_mesage_to_hex(pkt_type, None, caps)
        self.set_lldp_tlv_length(length if (length is not None) else len(temp) / 2, index)
        self.set_lldp_tlv_message(caps, index)

    # example: packet.add_lldp_tlv_end()
    def add_lldp_tlv_end(self, pkt_type=0x0, length=None):
        index = self.add_lldp_entry(pkt_type)
        self.set_lldp_tlv_length(length if (length is not None) else 0x00, index)
        self.set_lldp_tlv_message("", index)

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        return self.to_packet_string_tags()

    def to_packet_string_tags(self):
        table = TableFormatter()
        ret_string = "\n\nLLDP HEADER"
        for index in range(1, NumberUtils.to_integer_value(self.get_lldp_entries_num()) + 1):
            table.add_row_value("TLV Type", LldpPacketConstants.type_to_string(self.get_lldp_tlv_type(index)) +
                                " - " + self.format_int(self.get_lldp_tlv_type(index), 1))
            table.add_row_value("TLV Length", self.format_int(self.get_lldp_tlv_length(index), 1))
            if self.is_field_set(self.get_lldp_tlv_message(index)):
                table.add_row_value("TLV Message", self.get_lldp_tlv_message(index))
            else:
                table.add_row_value("TLV Message", "n/a")
            index += 1
        ret_string += table.to_table_string() + "\n"
        return ret_string

    def add_lldp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_LLDP)

    def build(self):
        self.add_lldp_header()
        if isinstance(self, SnapPacketHeader):
            self.set_snap_ether_type("0x88cc", True)
        else:
            try:
                self.set_ether_type("0x88cc", True)
            except Exception as e:
                PacketObject.logger.log_info("The following Exception was caught, Continuing on:\n" + repr(e))
                pass

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_lldp_version_hltapi_cmd(dummy_dict)
        # self.get_lldp_traffic_class_hltapi_cmd(dummy_dict)
        return dummy_dict

    def get_spirent_lldp_api_commands(self, port_name_stream):
        dummy_dict = []
        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_lldp(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_lldp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jet_stream_lldp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_lldp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = LldpPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData

    def config_jets_stream_lldp(self, jets_dev, port_string, stream_id, **kwargs):
        # this is not supported yet
        # do it with rawdata instead
        pkt_bytes = "0x" + LldpPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_lldp_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
    # ### put some IxTclHal info here.
        payload = LldpPacketHeader.get_header_bytes(self)
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
        index = 0
        last_type = 1
        while len(payload) > 0 and last_type > LldpPacketConstants.LLDP_TLV_TYPE_END:
            index += 1
            type_and_length = int(self.get_bits_from_string(16, payload), 16)
            pkt_type = (type_and_length & 0xFE00) >> 9
            last_type = pkt_type
            self.set_lldp_tlv_type(pkt_type, index)
            length = (type_and_length & 0x01FF)
            self.set_lldp_tlv_length(length, index)
            payload = self.remove_bits_from_string(16, payload)
            message = self.get_bits_from_string(length * 8, payload)
            self.set_lldp_tlv_message(message, index)
            payload = self.remove_bits_from_string(length * 8, payload)
            self.set_lldp_entries_num(index)

        self.payload = payload

    def get_lldp_tlv_in_hex_string(self, index):
        line = (hex((self.get_lldp_tlv_type(index) << 0x09) | self.get_lldp_tlv_length(index))[2:]).zfill(4)
        message = self.get_lldp_tlv_message(index)
        message = LldpPacketHeader.convert_mesage_to_hex(self.get_lldp_tlv_type(index), self.get_lldp_tlv_length(index),
                                                         message)
        return line + message

    def get_all_lldp_tlv_entries_in_hex_string(self):
        ret_string = []
        extension_length = 0
        index = 1
        while index <= self.get_lldp_entries_num():
            message = self.get_lldp_tlv_in_hex_string(index)
            ret_string.append(message)
            index += 1
        return ret_string

    def get_header_bytes(self):
        ret_string = ""
        extension_length = 0
        index = 1
        while index <= self.get_lldp_entries_num():
            message = self.get_lldp_tlv_in_hex_string(index)
            ret_string += message
            index += 1
        return ret_string

    @staticmethod
    def convert_mesage_to_hex(pkt_type, length, message):
        if isinstance(message, list):
            return ''.join(hex(i)[2:].zfill(2) for i in message)
        if message.startswith("0x") and len(message) > 2:
            message = message[2:]
        hexaPattern = re.compile(r'^([0-9a-fA-F]+)$')
        if re.search(hexaPattern, message):
            return message.upper()

        if "," in message and (pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_CHASSIS_SUBTYPE):
            if "," in message:
                parts = message.split(",", 1)
                message = parts[0] + " " + parts[1].replace(":", "")
            else:
                message = message.replace(",", "").replace(":", "")
            message = message.replace(" ", "")
        elif pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_PORT_SUBTYPE:
            if "," in message:
                parts = message.split(",", 1)
                message = parts[0] + " " + parts[1].encode('hex')
            else:
                message = message.replace(",", "").replace(":", "").encode('hex')
            message = message.replace(" ", "")
        elif pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_TIME_TO_LIVE:
            message = " " + message.replace(" ", "").replace(",", "").replace(":", "")
        # elif type == LldpPacketConstants.LLDP_TLV_TYPE_PORT_DESCRIPTION or
        #     type == LldpPacketConstants.LLDP_TLV_TYPE_SYSTEM_DESCRIPTION or
        #     type == LldpPacketConstants.LLDP_TLV_TYPE_SYSTEM_NAME :
        #     message = " " + message.encode('hex')
        else:
            if len(message) > 0:
                message = " " + message.encode('hex')
        return message.upper()

    @staticmethod
    def compare_lldp_packet_header(expected, actual, ignore_list=None, include_list=None, dynamic_entries=None,
                                   print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, LldpPacketHeader)
            assert isinstance(actual, LldpPacketHeader)
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
                name = "LLDP TLV Entries: "
                if expected.do_i_check_this_field(expected.get_lldp_entries_num(),
                                                  LldpPacketConstants.LLDP_TLV_ENTERY_NUM, ignore_list, include_list):
                    if str(expected.get_lldp_entries_num()) != str(actual.get_lldp_entries_num()):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(name + str(expected.get_lldp_entries_num()) + " != " +
                                                          str(actual.get_lldp_entries_num()) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_lldp_entries_num()) + " == " +
                                                     str(actual.get_lldp_entries_num()) + " Pass")
                num_vlans = min(expected.get_lldp_entries_num(), actual.get_lldp_entries_num())
                index = 0
                while index < num_vlans:
                    index += 1
                    results &= expected.compare_tags(expected, actual, index, index, ignore_list, include_list,
                                                     print_results, print_failures)

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with LldpPacketHeader")
        return results

    @staticmethod
    def compare_tags(expected, actual, expected_index, actual_index, ignore_list=None, include_list=None,
                     print_results=True, print_failures=True):
        results = True
        wasSomethingChecked = False
        if expected.do_i_check_this_field(expected.get_lldp_tlv_type(expected_index),
                                          LldpPacketConstants.LLDP_TLV_TYPE + " " + str(expected_index),
                                          ignore_list, include_list):
            name = "LLDP TLV Type " + str(expected_index) + ": "
            e_type = expected.get_lldp_tlv_type(expected_index)
            a_type = actual.get_lldp_tlv_type(actual_index)
            if e_type != actual.get_lldp_tlv_type(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name + str(e_type) + " != " + str(a_type) + " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_error(name + str(e_type) + " == " + str(a_type) + " Pass")

        if expected.do_i_check_this_field(expected.get_lldp_tlv_length(expected_index),
                                          LldpPacketConstants.LLDP_TLV_LENGTH + " " + str(expected_index),
                                          ignore_list, include_list):
            name = "LLDP TLV Length " + str(expected_index) + ": "
            e_length = expected.get_lldp_tlv_length(expected_index)
            a_length = actual.get_lldp_tlv_length(actual_index)
            if e_length != a_length:
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name + str(e_length) + " != " + str(a_length) + " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_error(name + str(e_length) + " == " + str(a_length) + " Pass")

        if expected.do_i_check_this_field(expected.get_lldp_tlv_message(expected_index),
                                          LldpPacketConstants.LLDP_TLV_MESSAGE + " " + str(expected_index),
                                          ignore_list, include_list):
            name = "LLDP TLV Message " + str(expected_index) + ": "
            e_message = expected.get_lldp_tlv_message(expected_index)
            if e_type:
                e_message = LldpPacketHeader.convert_mesage_to_hex(e_type, e_length, e_message).replace(" ", "")
            a_message = actual.get_lldp_tlv_message(actual_index)
            if a_type:
                a_message = LldpPacketHeader.convert_mesage_to_hex(a_type, e_length, a_message).replace(" ", "")
            if e_message != a_message:
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name + str(e_message) + " != " + str(a_message) + " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_error(name + str(e_message) + " == " + str(a_message) + " Pass")
        return results


class LldpPacketConstants:
    def __init__(self):
        pass

    LLDP_TLV_LENGTH = "LLDP_TLV_LENGTH"
    LLDP_TLV_TYPE = "LLDP_TLV_TYPE"
    LLDP_TLV_MESSAGE = "LLDP_TLV_MESSAGE"
    LLDP_TLV_ENTERY_NUM = "LLDP_TLV_ENTERY_NUM"

    LLDP_TLV_TYPE_CHASSIS_SUBTYPE = 0x01
    LLDP_TLV_TYPE_PORT_SUBTYPE = 0x02
    LLDP_TLV_TYPE_TIME_TO_LIVE = 0x03
    LLDP_TLV_TYPE_PORT_DESCRIPTION = 0x04
    LLDP_TLV_TYPE_SYSTEM_NAME = 0x05
    LLDP_TLV_TYPE_SYSTEM_DESCRIPTION = 0x06
    LLDP_TLV_TYPE_CAPABILITIES = 0x07
    LLDP_TLV_TYPE_MANAGEMENT_ADDRESS = 0x08
    LLDP_TLV_TYPE_IEEE_802_1 = 127
    LLDP_TLV_TYPE_IEEE_802_3 = 127
    LLDP_TLV_TYPE_END = 0x0

    @staticmethod
    def type_to_string(pkt_type):
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_CHASSIS_SUBTYPE:
            return "Chassis Subtype"
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_PORT_SUBTYPE:
            return "Port Subtype"
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_TIME_TO_LIVE:
            return "Time To Live"
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_PORT_DESCRIPTION:
            return "Port Description"
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_SYSTEM_NAME:
            return "System Name"
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_SYSTEM_DESCRIPTION:
            return "System Description"
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_CAPABILITIES:
            return "Capabilities"
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_MANAGEMENT_ADDRESS:
            return "Management Address"
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_IEEE_802_1:
            return "IEEE 802.1/3"
        if pkt_type == LldpPacketConstants.LLDP_TLV_TYPE_END:
            return "End Of LLDPU"
        return "Unknown"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


class LldpPacketHeaderDynamicFieldLogic(PacketHeaderDynamicFieldLogic):

    def compare_dynamic_fields(self, expected, actual, index, index_actual_vlans, print_results=False,
                               print_failures=False):
        return expected.compare_tags(expected, actual, index, index_actual_vlans, None, None, print_results,
                                     print_failures)

    def get_compare_number(self, expected):
        return expected.get_radius_attribute_value_pairs_num()
