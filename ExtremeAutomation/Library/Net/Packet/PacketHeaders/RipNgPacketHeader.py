from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb


class RipNgPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    RIPng Packet Header
        # Command = 8bits
        # Version = 8bits
        # Zeros = 16bits
        # IPv6 Prefix = 128bits
        # Route Tag = 16bits
        # Prefix Length = 8bits
        # Metric = 8bits
    """

    def __init__(self):
        self.add_ripng_header()
        self.route_entry_num = 0
        self.HEADER_SIZE_RIPNG = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    def add_route_entry_num(self):
        self.route_entry_num += 1
        return self.route_entry_num

    def get_route_entry_num(self):
        return self.route_entry_num

    def set_route_entry_num(self, route_entry):
        self.route_entry_num = NumberUtils.to_integer_value(route_entry)

    # start RipNg Command methods
    #  command is a 8 bit INTEGER example: 1
    def set_ripng_command(self, command, ignore_check=False):
        command = self.normalize_value(command, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_COMMAND, command)

    def get_ripng_command(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_COMMAND), PacketConstants.INTEGER)

    def get_ripng_command_hltapi_cmd(self, dummy_dict):
        command = self.get_ripng_command()
        if isinstance(command, int):
            command = str(command)
        if command and 'Not Set' not in command:
            dummy_dict[TrafficConfigConstants.TEMP_COMMAND_CMD] = command
    # end RipNg Command methods

    # start RipNg Version methods
    #  version is a 8 bit INTEGER example: 1
    def set_ripng_version(self, version, ignore_check=False):
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_VERSION, version)

    def get_ripng_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_VERSION), PacketConstants.INTEGER)

    def get_ripng_version_hltapi_cmd(self, dummy_dict):
        version = self.get_ripng_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end RipNg Version methods

    # start RipNg Zeros methods
    #  zeros is a 16 bit INTEGER example: 1
    def set_ripng_zeros(self, zeros, ignore_check=False):
        zeros = self.normalize_value(zeros, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_ZEROS, zeros)

    def get_ripng_zeros(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_ZEROS), PacketConstants.INTEGER)

    def get_ripng_zeros_hltapi_cmd(self, dummy_dict):
        zeros = self.get_ripng_zeros()
        if isinstance(zeros, int):
            zeros = str(zeros)
        if zeros and 'Not Set' not in zeros:
            dummy_dict[TrafficConfigConstants.TEMP_ZEROS_CMD] = zeros
    # end RipNg Zeros methods

    # start RipNg IPv6 Prefix methods
    #  ipv6_prefix is a 128 bit IPV6_ADDRESS example: FF01::0001
    def set_ripng_ipv6_prefix(self, ipv6_prefix, index, ignore_check=False):
        ipv6_prefix = self.normalize_value(ipv6_prefix, PacketConstants.IPV6_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIPNG,
                                  RipNgPacketConstants.RIPNG_IPV6_PREFIX + " " + str(index), ipv6_prefix)

    def get_ripng_ipv6_prefix(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_IPV6_PREFIX + " " + str(index)),
            PacketConstants.IPV6_ADDRESS)

    def get_ripng_ipv6_prefix_hltapi_cmd(self, index, dummy_dict):
        ipv6_prefix = self.get_ripng_ipv6_prefix(index)
        if ipv6_prefix and 'Not Set' not in ipv6_prefix:
            dummy_dict[TrafficConfigConstants.TEMP_IPV6_PREFIX_CMD] = ipv6_prefix
    # end RipNg IPv6 Prefix methods

    # start RipNg Route Tag methods
    #  route_tag is a 16 bit INTEGER example: 1
    def set_ripng_route_tag(self, route_tag, index, ignore_check=False):
        route_tag = self.normalize_value(route_tag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIPNG,
                                  RipNgPacketConstants.RIPNG_ROUTE_TAG + " " + str(index), route_tag)

    def get_ripng_route_tag(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_ROUTE_TAG + " " + str(index)),
            PacketConstants.INTEGER)

    def get_ripng_route_tag_hltapi_cmd(self, index, dummy_dict):
        route_tag = self.get_ripng_route_tag(index)
        if isinstance(route_tag, int):
            route_tag = str(route_tag)
        if route_tag and 'Not Set' not in route_tag:
            dummy_dict[TrafficConfigConstants.TEMP_ROUTE_TAG_CMD] = route_tag
    # end RipNg Route Tag methods

    # start RipNg Prefix Length methods
    #  prefix_length is a 8 bit INTEGER example: 1
    def set_ripng_prefix_length(self, prefix_length, index, ignore_check=False):
        prefix_length = self.normalize_value(prefix_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIPNG,
                                  RipNgPacketConstants.RIPNG_PREFIX_LENGTH + " " + str(index), prefix_length)

    def get_ripng_prefix_length(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_PREFIX_LENGTH + " " + str(index)),
            PacketConstants.INTEGER)

    def get_ripng_prefix_length_hltapi_cmd(self, index, dummy_dict):
        prefix_length = self.get_ripng_prefix_length(index)
        if isinstance(prefix_length, int):
            prefix_length = str(prefix_length)
        if prefix_length and 'Not Set' not in prefix_length:
            dummy_dict[TrafficConfigConstants.TEMP_PREFIX_LENGTH_CMD] = prefix_length
    # end RipNg Prefix Length methods

    # start RipNg Metric methods
    #  metric is a 8 bit INTEGER example: 1
    def set_ripng_metric(self, metric, index, ignore_check=False):
        metric = self.normalize_value(metric, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIPNG,
                                  RipNgPacketConstants.RIPNG_METRIC + " " + str(index), metric)

    def get_ripng_metric(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIPNG, RipNgPacketConstants.RIPNG_METRIC + " " + str(index)),
            PacketConstants.INTEGER)

    def get_ripng_metric_hltapi_cmd(self, index, dummy_dict):
        metric = self.get_ripng_metric(index)
        if isinstance(metric, int):
            metric = str(metric)
        if metric and 'Not Set' not in metric:
            dummy_dict[TrafficConfigConstants.TEMP_METRIC_CMD] = metric
    # end RipNg Metric methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Command", self.format_int(self.get_ripng_command(), 1))
        table.add_row_value("Version", self.format_int(self.get_ripng_version(), 1))
        table.add_row_value("Zeros", self.format_int(self.get_ripng_zeros(), 2))
        ret_string = table.to_table_string()
        ret_string += "\nRIP Router Entry number : " + str(self.get_route_entry_num())
        table = TableFormatter()
        for index in range(1, NumberUtils.to_integer_value(self.get_route_entry_num()) + 1):
            table.add_row_value("#", index)
            table.add_row_value("IPv6 Prefix", self.get_ripng_ipv6_prefix(index))
            table.add_row_value("Route Tag", self.format_int(self.get_ripng_route_tag(index), 2))
            table.add_row_value("Prefix Length", self.format_int(self.get_ripng_prefix_length(index), 1))
            table.add_row_value("Metric", self.format_int(self.get_ripng_metric(index), 1))
        return "\n\nRIPNG HEADER" + ret_string + table.to_table_string()

    def add_ripng_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_RIPNG)

    def build(self):
        self.add_ripng_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_ripng_command_hltapi_cmd(dummy_dict)
        # self.get_ripng_version_hltapi_cmd(dummy_dict)
        # self.get_ripng_zeros_hltapi_cmd(dummy_dict)
        # self.get_ripng_ipv6_prefix_hltapi_cmd(dummy_dict)
        # self.get_ripng_route_tag_hltapi_cmd(dummy_dict)
        # self.get_ripng_prefix_length_hltapi_cmd(dummy_dict)
        # self.get_ripng_metric_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_ripng(self, tgen_type, generator_ref, port_string, stream_id,
                                                         **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_ripng(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_ripng(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_ripng(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kripngFieldNumber
        # update this from the ostinato docs.
        # ripngField = p.Extensions[ripng]
        # if self.is_field_set(self.get_ripng_command()):
        #     ripngField.version = int(self.get_ripng_command())
        # if self.is_field_set(self.get_ripng_version()):
        #     ripngField.version = int(self.get_ripng_version())
        # if self.is_field_set(self.get_ripng_zeros()):
        #     ripngField.version = int(self.get_ripng_zeros())
        # if self.is_field_set(self.get_ripng_ipv6_prefix()):
        #     ripngField.version = int(self.get_ripng_ipv6_prefix())
        # if self.is_field_set(self.get_ripng_route_tag()):
        #     ripngField.version = int(self.get_ripng_route_tag())
        # if self.is_field_set(self.get_ripng_prefix_length()):
        #     ripngField.version = int(self.get_ripng_prefix_length())
        # if self.is_field_set(self.get_ripng_metric()):
        #     ripngField.version = int(self.get_ripng_metric())

    def config_jets_stream_ripng(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "RIPNG_HDR"
        pkt_bytes = "0x" + RipNgPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_ripng_command()):
            pkt_fields["command"] = int(self.get_ripng_command())
        if self.is_field_set(self.get_ripng_version()):
            pkt_fields["version"] = int(self.get_ripng_version())
        if self.is_field_set(self.get_ripng_zeros()):
            pkt_fields["zeros"] = int(self.get_ripng_zeros())
        if self.is_field_set(self.get_ripng_ipv6_prefix()):
            pkt_fields["ipv6_prefix"] = int(self.get_ripng_ipv6_prefix())
        if self.is_field_set(self.get_ripng_route_tag()):
            pkt_fields["route_tag"] = int(self.get_ripng_route_tag())
        if self.is_field_set(self.get_ripng_prefix_length()):
            pkt_fields["prefix_length"] = int(self.get_ripng_prefix_length())
        if self.is_field_set(self.get_ripng_metric()):
            pkt_fields["metric"] = int(self.get_ripng_metric())

    def get_ixtclhal_ripng_api_commands(self, port_string, streamid):
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
        command = self.get_bits_from_string(8, payload)
        self.set_ripng_command("0x" + command)
        payload = self.remove_bits_from_string(8, payload)
        version = self.get_bits_from_string(8, payload)
        self.set_ripng_version("0x" + version)
        payload = self.remove_bits_from_string(8, payload)
        zeros = self.get_bits_from_string(16, payload)
        self.set_ripng_zeros("0x" + zeros)
        payload = self.remove_bits_from_string(16, payload)

        self.set_route_entry_num(0)
        index = 0
        while len(payload) > 0:
            self.add_route_entry_num()
            index += 1
            ipv6_prefix = self.get_bits_from_string(128, payload)
            self.set_ripng_ipv6_prefix(ipv6_prefix, index, ignore_check=False)
            payload = self.remove_bits_from_string(128, payload)
            route_tag = self.get_bits_from_string(16, payload)
            self.set_ripng_route_tag("0x" + route_tag, index, ignore_check=False)
            payload = self.remove_bits_from_string(16, payload)
            prefix_length = self.get_bits_from_string(8, payload)
            self.set_ripng_prefix_length("0x" + prefix_length, index, ignore_check=False)
            payload = self.remove_bits_from_string(8, payload)
            metric = self.get_bits_from_string(8, payload)
            self.set_ripng_metric("0x" + metric, index, ignore_check=False)
            payload = self.remove_bits_from_string(8, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_ripng_command(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_ripng_version(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_ripng_zeros(), PacketConstants.INTEGER, 16)
        for index in range(1, NumberUtils.to_integer_value(self.get_route_entry_num()) + 1):
            ret_string += self.format_byte_string(self.get_ripng_ipv6_prefix(index), PacketConstants.IPV6_ADDRESS, 128)
            ret_string += self.format_byte_string(self.get_ripng_route_tag(index), PacketConstants.INTEGER, 16)
            ret_string += self.format_byte_string(self.get_ripng_prefix_length(index), PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(self.get_ripng_metric(index), PacketConstants.INTEGER, 8)
        return ret_string

    @staticmethod
    def compare_ripng_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, RipNgPacketHeader)
            assert isinstance(actual, RipNgPacketHeader)
            if expected.is_field_set(expected.get_ripng_command()) and \
                    RipNgPacketConstants.RIPNG_COMMAND not in ignore_list:
                name = "RIPNG command : "
                if expected.get_ripng_command() != actual.get_ripng_command():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ripng_command()) + " != " +
                                                      str(actual.get_ripng_command()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ripng_command()) + " == " +
                                                 str(actual.get_ripng_command()) + " Pass")

            if expected.is_field_set(expected.get_ripng_version()) and \
                    RipNgPacketConstants.RIPNG_VERSION not in ignore_list:
                name = "RIPNG version : "
                if expected.get_ripng_version() != actual.get_ripng_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ripng_version()) + " != " +
                                                      str(actual.get_ripng_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ripng_version()) + " == " +
                                                 str(actual.get_ripng_version()) + " Pass")

            if expected.is_field_set(expected.get_ripng_zeros()) and \
                    RipNgPacketConstants.RIPNG_ZEROS not in ignore_list:
                name = "RIPNG zeros : "
                if expected.get_ripng_zeros() != actual.get_ripng_zeros():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_ripng_zeros()) + " != " +
                                                      str(actual.get_ripng_zeros()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ripng_zeros()) + " == " +
                                                 str(actual.get_ripng_zeros()) + " Pass")

            index = 1
            for index in range(1, NumberUtils.to_integer_value(expected.set_route_entry_num(index)) + 1):
                if expected.is_field_set(expected.get_ripng_ipv6_prefix(index)) and \
                        RipNgPacketConstants.RIPNG_IPV6_PREFIX not in ignore_list:
                    name = "RIPNG ipv6_prefix : "
                    if expected.get_ripng_ipv6_prefix(index) != actual.get_ripng_ipv6_prefix(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_ripng_ipv6_prefix(index)) + " != " +
                                                          str(actual.get_ripng_ipv6_prefix(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_ripng_ipv6_prefix(index)) + " == " +
                                                     str(actual.get_ripng_ipv6_prefix(index)) + " Pass")

                if expected.is_field_set(expected.get_ripng_route_tag(index)) and \
                        RipNgPacketConstants.RIPNG_ROUTE_TAG not in ignore_list:
                    name = "RIPNG route_tag : "
                    if expected.get_ripng_route_tag(index) != actual.get_ripng_route_tag(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_ripng_route_tag(index)) + " != " +
                                                          str(actual.get_ripng_route_tag(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_ripng_route_tag(index)) + " == " +
                                                     str(actual.get_ripng_route_tag(index)) + " Pass")

                if expected.is_field_set(expected.get_ripng_prefix_length(index)) and \
                        RipNgPacketConstants.RIPNG_PREFIX_LENGTH not in ignore_list:
                    name = "RIPNG prefix_length : "
                    if expected.get_ripng_prefix_length(index) != actual.get_ripng_prefix_length(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_ripng_prefix_length(index)) + " != " +
                                                          str(actual.get_ripng_prefix_length(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_ripng_prefix_length(index)) + " == " +
                                                     str(actual.get_ripng_prefix_length(index)) + " Pass")

                if expected.is_field_set(expected.get_ripng_metric(index)) and \
                        RipNgPacketConstants.RIPNG_METRIC not in ignore_list:
                    name = "RIPNG metric : "
                    if expected.get_ripng_metric(index) != actual.get_ripng_metric(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_ripng_metric(index)) + " != " +
                                                          str(actual.get_ripng_metric(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_ripng_metric(index)) + " == " +
                                                     str(actual.get_ripng_metric(index)) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with RipNgPacketHeader")
        return results


class RipNgPacketConstants:
    def __init__(self):
        pass

    RIPNG_COMMAND = "RIPNG_COMMAND"
    RIPNG_VERSION = "RIPNG_VERSION"
    RIPNG_ZEROS = "RIPNG_ZEROS"

    RIPNG_IPV6_PREFIX = "RIPNG_IPV6_PREFIX"
    RIPNG_ROUTE_TAG = "RIPNG_ROUTE_TAG"
    RIPNG_PREFIX_LENGTH = "RIPNG_PREFIX_LENGTH"
    RIPNG_METRIC = "RIPNG_METRIC"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
