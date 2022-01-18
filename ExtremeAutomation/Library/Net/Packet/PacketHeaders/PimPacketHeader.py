from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader


class PimPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    PIM Packet Header
        # Version = 4bits
        # Length = 4bits
        # Reserve = 8bits
        # Checksum = 16bits
        # Options = 32bits
    """

    def __init__(self):
        self.add_pim_header()
        self.HEADER_SIZE_PIM = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Pim Version methods
    #  version is a 4 bit INTEGER example: 1
    def set_pim_version(self, version, ignore_check=False):
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_VERSION, version)

    def get_pim_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_VERSION), PacketConstants.INTEGER)

    def get_pim_version_hltapi_cmd(self, dummy_dict):
        version = self.get_pim_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version

    def get_pim_type(self):
        return (self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_VERSION),
            PacketConstants.INTEGER) | 0x0ff)
    # end Pim Version methods

    # start Pim Length methods
    #  length is a 4 bit INTEGER example: 1
    def set_pim_length(self, length, ignore_check=False):
        length = self.normalize_value(length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_LENGTH, length)

    def get_pim_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_LENGTH), PacketConstants.INTEGER)

    def get_pim_length_hltapi_cmd(self, dummy_dict):
        length = self.get_pim_length()
        if isinstance(length, int):
            length = str(length)
        if length and 'Not Set' not in length:
            dummy_dict[TrafficConfigConstants.TEMP_LENGTH_CMD] = length
    # end Pim Length methods

    # start Pim Reserve methods
    #  reserve is a 8 bit INTEGER example: 1
    def set_pim_reserve(self, reserve, ignore_check=False):
        reserve = self.normalize_value(reserve, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_RESERVE, reserve)

    def get_pim_reserve(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_RESERVE), PacketConstants.INTEGER)

    def get_pim_reserve_hltapi_cmd(self, dummy_dict):
        reserve = self.get_pim_reserve()
        if isinstance(reserve, int):
            reserve = str(reserve)
        if reserve and 'Not Set' not in reserve:
            dummy_dict[TrafficConfigConstants.TEMP_RESERVE_CMD] = reserve
    # end Pim Reserve methods

    # start Pim Checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_pim_checksum(self, checksum, ignore_check=False):
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_CHECKSUM, checksum)

    def get_pim_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_CHECKSUM), PacketConstants.INTEGER)

    def get_pim_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_pim_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end Pim Checksum methods

    # start Pim Options methods
    #  options is a 32 bit INTEGER example: 1
    def set_pim_options(self, options, ignore_check=False):
        options = self.normalize_value(options, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_OPTIONS, options)

    def get_pim_options(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_PIM, PimPacketConstants.PIM_OPTIONS), PacketConstants.INTEGER)

    def get_pim_options_hltapi_cmd(self, dummy_dict):
        options = self.get_pim_options()
        if isinstance(options, int):
            options = str(options)
        if options and 'Not Set' not in options:
            dummy_dict[TrafficConfigConstants.TEMP_OPTIONS_CMD] = options
    # end Pim Options methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Version", self.format_int(self.get_pim_version(), 1))
        table.add_row_value("Length", self.format_int(self.get_pim_length(), 1))
        table.add_row_value("Reserve", self.format_int(self.get_pim_reserve(), 2))
        table.add_row_value("Checksum", self.format_int(self.get_pim_checksum(), 4))
        table.add_row_value("Options", self.format_int(self.get_pim_options(), 8))
        return "\n\nPIM HEADER" + table.to_table_string()

    def add_pim_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_PIM)

    def build(self):
        self.add_pim_header()
        if isinstance(self, IpV4PacketHeader):  # you can either do this here OR in the build of each packet
            self.set_ip_protocol("0x67", True)
        elif isinstance(self, IpV6PacketHeader):
            self.set_ipv6_next_header("0x67", True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_pim_version_hltapi_cmd(dummy_dict)
        # self.get_pim_length_hltapi_cmd(dummy_dict)
        # self.get_pim_reserve_hltapi_cmd(dummy_dict)
        # self.get_pim_checksum_hltapi_cmd(dummy_dict)
        # self.get_pim_options_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_pim(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_pim(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_pim(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_pim(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kpimFieldNumber
        # update this from the ostinato docs.
        # if self.is_field_set(self.get_pim_version()):
        #     pimField.version = int(self.get_pim_version())
        # if self.is_field_set(self.get_pim_length()):
        #     pimField.version = int(self.get_pim_length())
        # if self.is_field_set(self.get_pim_reserve()):
        #     pimField.version = int(self.get_pim_reserve())
        # if self.is_field_set(self.get_pim_checksum()):
        #     pimField.version = int(self.get_pim_checksum())
        # if self.is_field_set(self.get_pim_options()):
        #     pimField.version = int(self.get_pim_options())

    def config_jets_stream_pim(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "PIM_HDR"
        pkt_bytes = "0x" + PimPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_pim_version()):
            pkt_fields["version"] = int(self.get_pim_version())
        if self.is_field_set(self.get_pim_length()):
            pkt_fields["length"] = int(self.get_pim_length())
        if self.is_field_set(self.get_pim_reserve()):
            pkt_fields["reserve"] = int(self.get_pim_reserve())
        if self.is_field_set(self.get_pim_checksum()):
            pkt_fields["checksum"] = int(self.get_pim_checksum())
        if self.is_field_set(self.get_pim_options()):
            pkt_fields["options"] = int(self.get_pim_options())

    def get_ixtclhal_pim_api_commands(self, port_string, streamid):
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
        version = self.get_bits_from_string(4, payload)
        self.set_pim_version("0x" + version)
        payload = self.remove_bits_from_string(4, payload)
        length = self.get_bits_from_string(4, payload)
        self.set_pim_length("0x" + length)
        payload = self.remove_bits_from_string(4, payload)
        reserve = self.get_bits_from_string(8, payload)
        self.set_pim_reserve("0x" + reserve)
        payload = self.remove_bits_from_string(8, payload)
        checksum = self.get_bits_from_string(16, payload)
        self.set_pim_checksum("0x" + checksum)
        payload = self.remove_bits_from_string(16, payload)

        # https://github.com/wireshark/wireshark/blob/fe219637a6748130266a0b0278166046e60a2d68/epan/dissectors/packet-pim.c
        pim_type = self.get_pim_type()
        if pim_type == 1:
            pim_length = 8
            options = self.get_bits_from_string(32, payload)
            self.set_pim_options("0x" + options)
            payload = self.remove_bits_from_string(32, payload)
        else:
            pass
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_pim_version(), PacketConstants.INTEGER, 4)
        ret_string += self.format_byte_string(self.get_pim_length(), PacketConstants.INTEGER, 4)
        ret_string += self.format_byte_string(self.get_pim_reserve(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_pim_checksum(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_pim_options(), PacketConstants.INTEGER, 32)
        return ret_string

    @staticmethod
    def compare_pim_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, PimPacketHeader)
            assert isinstance(actual, PimPacketHeader)
            if expected.is_field_set(expected.get_pim_version()) and \
                    PimPacketConstants.PIM_VERSION not in ignore_list:
                name = "PIM version : "
                if expected.get_pim_version() != actual.get_pim_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_pim_version()) + " != " +
                                                      str(actual.get_pim_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_pim_version()) + " == " +
                                                 str(actual.get_pim_version()) + " Pass")

            if expected.is_field_set(expected.get_pim_length()) and \
                    PimPacketConstants.PIM_LENGTH not in ignore_list:
                name = "PIM length : "
                if expected.get_pim_length() != actual.get_pim_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_pim_length()) + " != " +
                                                      str(actual.get_pim_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_pim_length()) + " == " +
                                                 str(actual.get_pim_length()) + " Pass")

            if expected.is_field_set(expected.get_pim_reserve()) and \
                    PimPacketConstants.PIM_RESERVE not in ignore_list:
                name = "PIM reserve : "
                if expected.get_pim_reserve() != actual.get_pim_reserve():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_pim_reserve()) + " != " +
                                                      str(actual.get_pim_reserve()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_pim_reserve()) + " == " +
                                                 str(actual.get_pim_reserve()) + " Pass")

            if expected.is_field_set(expected.get_pim_checksum()) and \
                    PimPacketConstants.PIM_CHECKSUM not in ignore_list:
                name = "PIM checksum : "
                if expected.get_pim_checksum() != actual.get_pim_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_pim_checksum()) + " != " +
                                                      str(actual.get_pim_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_pim_checksum()) + " == " +
                                                 str(actual.get_pim_checksum()) + " Pass")

            if expected.is_field_set(expected.get_pim_options()) and \
                    PimPacketConstants.PIM_OPTIONS not in ignore_list:
                name = "PIM options : "
                if expected.get_pim_options() != actual.get_pim_options():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_pim_options()) + " != " +
                                                      str(actual.get_pim_options()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_pim_options()) + " == " +
                                                 str(actual.get_pim_options()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with PimPacketHeader")
        return results


class PimPacketConstants:
    def __init__(self):
        pass

    PIM_VERSION = "PIM_VERSION"
    PIM_LENGTH = "PIM_LENGTH"
    PIM_RESERVE = "PIM_RESERVE"
    PIM_CHECKSUM = "PIM_CHECKSUM"
    PIM_OPTIONS = "PIM_OPTIONS"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
