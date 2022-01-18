from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb


class RipPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    RIP Packet Header
        # Command = 8bits
        # Version = 8bits
        # zeros = 16bits

        #each routing metric:
            # Address Family = 16bits
            # Route Tag = 16bits
            # Ip Address = 32bits
            # Netmask = 32bits
            # Next Hop = 32bits
            # Metric = 32bits
    """

    def __init__(self):
        self.add_rip_header()
        self.num_metrics = 0
        self.HEADER_SIZE_RIP = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    def add_rip_metric(self):
        self.num_metrics += 1
        return self.num_metrics

    def get_metric_num(self):
        return self.num_metrics

    def set_metric_num(self, num_metrics):
        self.num_metrics = NumberUtils.to_integer_value(num_metrics)

    # start Rip Command methods
    #  command is a 8 bit INTEGER example: 1
    def set_rip_command(self, command, ignore_check=False):
        command = self.normalize_value(command, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_COMMAND, command)

    def get_rip_command(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_COMMAND), PacketConstants.INTEGER)

    def get_rip_command_string(self):
        cmd = self.get_rip_command()
        if cmd == 2:
            return "Response"
        elif cmd == 1:
            return "Request"
        else:
            return "Unknown"

    def get_rip_command_hltapi_cmd(self, dummy_dict):
        command = self.get_rip_command()
        if isinstance(command, int):
            command = str(command)
        if command and 'Not Set' not in command:
            dummy_dict[TrafficConfigConstants.TEMP_COMMAND_CMD] = command
    # end Rip Command methods

    # start Rip Version methods
    #  version is a 8 bit INTEGER example: 1
    def set_rip_version(self, version, ignore_check=False):
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_VERSION, version)

    def get_rip_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_VERSION), PacketConstants.INTEGER)

    def get_rip_version_string(self):
        cmd = self.get_rip_version()
        if cmd == 1:
            return "RIPv1"
        elif cmd == 2:
            return "RIPv2"
        else:
            return "Unknown"

    def get_rip_version_hltapi_cmd(self, dummy_dict):
        version = self.get_rip_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end Rip Version methods

    # start Rip Zeros methods
    #  zeros is a 16 bit INTEGER example: 1
    def set_rip_zeros(self, zeros, ignore_check=False):
        zeros = self.normalize_value(zeros, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_ZEROS, zeros)

    def get_rip_zeros(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_ZEROS), PacketConstants.INTEGER)

    def get_rip_zeros_hltapi_cmd(self, dummy_dict):
        zeros = self.get_rip_zeros()
        if isinstance(zeros, int):
            zeros = str(zeros)
        if zeros and 'Not Set' not in zeros:
            dummy_dict[TrafficConfigConstants.TEMP_ZEROS_CMD] = zeros
    # end Rip Zeros methods

    # start Rip Address Family methods
    #  address_family is a 16 bit INTEGER example: 1
    def set_rip_address_family(self, address_family, index, ignore_check=False):
        address_family = self.normalize_value(address_family, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_ADDRESS_FAMILY + " " +
                                  str(index), address_family)

    def get_rip_address_family(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_ADDRESS_FAMILY + " " + str(index)),
            PacketConstants.INTEGER)

    def get_rip_address_family_string(self, index):
        cmd = self.get_rip_version(index)
        if cmd == 2:
            return "IP"
        else:
            return "Unknown"

    def get_rip_address_family_hltapi_cmd(self, index, dummy_dict):
        address_family = self.get_rip_address_family(index)
        if isinstance(address_family, int):
            address_family = str(address_family)
        if address_family and 'Not Set' not in address_family:
            dummy_dict[TrafficConfigConstants.TEMP_ADDRESS_FAMILY_CMD] = address_family
    # end Rip Address Family methods

    # start Rip Route Tag methods
    #  route_tag is a 16 bit INTEGER example: 1
    def set_rip_route_tag(self, route_tag, index, ignore_check=False):
        route_tag = self.normalize_value(route_tag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIP,
                                  RipPacketConstants.RIP_ROUTE_TAG + " " + str(index), route_tag)

    def get_rip_route_tag(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_ROUTE_TAG + " " + str(index)),
            PacketConstants.INTEGER)

    def get_rip_route_tag_hltapi_cmd(self, index, dummy_dict):
        route_tag = self.get_rip_route_tag(index)
        if isinstance(route_tag, int):
            route_tag = str(route_tag)
        if route_tag and 'Not Set' not in route_tag:
            dummy_dict[TrafficConfigConstants.TEMP_ROUTE_TAG_CMD] = route_tag
    # end Rip Route Tag methods

    # start Rip Ip Address methods
    #  ip_address is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_rip_ip_address(self, ip_address, index, ignore_check=False):
        ip_address = self.normalize_value(ip_address, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIP,
                                  RipPacketConstants.RIP_IP_ADDRESS + " " + str(index), ip_address)

    def get_rip_ip_address(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_IP_ADDRESS + " " + str(index)),
            PacketConstants.IPV4_ADDRESS)

    def get_rip_ip_address_hltapi_cmd(self, index, dummy_dict):
        ip_address = self.get_rip_ip_address(index)
        if ip_address and 'Not Set' not in ip_address:
            dummy_dict[TrafficConfigConstants.TEMP_IP_ADDRESS_CMD] = ip_address
    # end Rip Ip Address methods

    # start Rip Netmask methods
    #  netmask is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_rip_netmask(self, netmask, index, ignore_check=False):
        netmask = self.normalize_value(netmask, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIP,
                                  RipPacketConstants.RIP_NETMASK + " " + str(index), netmask)

    def get_rip_netmask(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_NETMASK + " " + str(index)),
            PacketConstants.IPV4_ADDRESS)

    def get_rip_netmask_hltapi_cmd(self, index, dummy_dict):
        netmask = self.get_rip_netmask(index)
        if netmask and 'Not Set' not in netmask:
            dummy_dict[TrafficConfigConstants.TEMP_NETMASK_CMD] = netmask
    # end Rip Netmask methods

    # start Rip Next Hop methods
    #  next_hop is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_rip_next_hop(self, next_hop, index, ignore_check=False):
        next_hop = self.normalize_value(next_hop, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIP,
                                  RipPacketConstants.RIP_NEXT_HOP + " " + str(index), next_hop)

    def get_rip_next_hop(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_NEXT_HOP + " " + str(index)),
            PacketConstants.IPV4_ADDRESS)

    def get_rip_next_hop_hltapi_cmd(self, index, dummy_dict):
        next_hop = self.get_rip_next_hop(index)
        if next_hop and 'Not Set' not in next_hop:
            dummy_dict[TrafficConfigConstants.TEMP_NEXT_HOP_CMD] = next_hop
    # end Rip Next Hop methods

    # start Rip Metric methods
    #  metric is a 32 bit INTEGER example: 1
    def set_rip_metric(self, metric, index, ignore_check=False):
        metric = self.normalize_value(metric, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_RIP,
                                  RipPacketConstants.RIP_METRIC + " " + str(index), metric)

    def get_rip_metric(self, index):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_RIP, RipPacketConstants.RIP_METRIC + " " + str(index)),
            PacketConstants.INTEGER)

    def get_rip_metric_hltapi_cmd(self, index, dummy_dict):
        metric = self.get_rip_metric(index)
        if isinstance(metric, int):
            metric = str(metric)
        if metric and 'Not Set' not in metric:
            dummy_dict[TrafficConfigConstants.TEMP_METRIC_CMD] = metric
    # end Rip Metric methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Command", self.get_rip_command_string() + " - " +
                            self.format_int(self.get_rip_command(), 1))
        table.add_row_value("Version", self.get_rip_version_string() + " - " +
                            self.format_int(self.get_rip_version(), 1))
        table.add_row_value("zeros", self.format_int(self.get_rip_zeros(), 2))

        ret_string = table.to_table_string()
        version = self.get_rip_version()

        ret_string += "\nRIP Metric number : " + str(self.get_metric_num())
        table = TableFormatter()
        for index in range(1, NumberUtils.to_integer_value(self.get_metric_num()) + 1):
            table.add_row_value("#", index)
            table.add_row_value("Address Family", self.format_int(self.get_rip_address_family(index), 2))
            table.add_row_value("Route Tag", self.format_int(self.get_rip_route_tag(index), 2))
            table.add_row_value("Ip Address", self.get_rip_ip_address(index))
            table.add_row_value("Netmask", self.get_rip_netmask(index))
            table.add_row_value("Next Hop", self.get_rip_next_hop(index))
            table.add_row_value("Metric", self.format_int(self.get_rip_metric(index), 4))
            index += 1
        return "\n\nRIP HEADER" + ret_string + table.to_table_string()

    def add_rip_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_RIP)

    def build(self):
        self.add_rip_header()
        self.set_source_port(520, True)
        self.set_destination_port(520, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_rip_command_hltapi_cmd(dummy_dict)
        # self.get_rip_length_hltapi_cmd(dummy_dict)
        # self.get_rip_zeros_hltapi_cmd(dummy_dict)
        # self.get_rip_metric_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_rip(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_rip(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_rip(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_rip(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kripFieldNumber
        # update this from the ostinato docs.
        #     ripField = p.Extensions[rip]
        #     if self.is_field_set(self.get_rip_command()):
        #         ripField.version = int(self.get_rip_command())
        #     if self.is_field_set(self.get_rip_length()):
        #         ripField.version = int(self.get_rip_length())
        #     if self.is_field_set(self.get_rip_zeros()):
        #         ripField.version = int(self.get_rip_zeros())
        #     if self.is_field_set(self.get_rip_metric()):
        #         ripField.version = int(self.get_rip_metric())

    def config_jets_stream_rip(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "RIP_HDR"
        pkt_bytes = "0x" + RipPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_rip_command()):
        #     pkt_fields["command"] = int(self.get_rip_command())
        # if self.is_field_set(self.get_rip_length()):
        #     pkt_fields["length"] = int(self.get_rip_length())
        # if self.is_field_set(self.get_rip_zeros()):
        #     pkt_fields["zeros"] = int(self.get_rip_zeros())
        # if self.is_field_set(self.get_rip_metric()):
        #     pkt_fields["metric"] = int(self.get_rip_metric())

    def get_ixtclhal_rip_api_commands(self, port_string, streamid):
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
        self.set_rip_command("0x" + command)
        payload = self.remove_bits_from_string(8, payload)
        version = self.get_bits_from_string(8, payload)
        self.set_rip_version("0x" + version)
        payload = self.remove_bits_from_string(8, payload)
        zeros = self.get_bits_from_string(16, payload)
        self.set_rip_zeros("0x" + zeros)
        payload = self.remove_bits_from_string(16, payload)

        self.set_metric_num(0)
        index = 0
        while len(payload) > 0:
            index += 1
            self.add_rip_metric()
            address_family = self.get_bits_from_string(16, payload)
            self.set_rip_address_family(address_family, index)
            payload = self.remove_bits_from_string(16, payload)
            route_tag = self.get_bits_from_string(16, payload)
            self.set_rip_route_tag(route_tag, index)
            payload = self.remove_bits_from_string(16, payload)
            ip_address = self.get_bits_from_string(32, payload)
            self.set_rip_ip_address(ip_address, index)
            payload = self.remove_bits_from_string(32, payload)
            netmask = self.get_bits_from_string(32, payload)
            self.set_rip_netmask(netmask, index)
            payload = self.remove_bits_from_string(32, payload)
            next_hop = self.get_bits_from_string(32, payload)
            self.set_rip_next_hop(next_hop, index)
            payload = self.remove_bits_from_string(32, payload)
            metric = self.get_bits_from_string(32, payload)
            self.set_rip_metric("0x" + metric, index)
            payload = self.remove_bits_from_string(32, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_rip_command(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_rip_version(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_rip_zeros(), PacketConstants.INTEGER, 16)

        for index in range(1, NumberUtils.to_integer_value(self.get_metric_num()) + 1):
            ret_string += self.format_byte_string(self.get_rip_address_family(index), PacketConstants.INTEGER, 16)
            ret_string += self.format_byte_string(self.get_rip_route_tag(index), PacketConstants.INTEGER, 16)
            ret_string += self.format_byte_string(self.get_rip_ip_address(index), PacketConstants.IPV4_ADDRESS, 32)
            ret_string += self.format_byte_string(self.get_rip_netmask(index), PacketConstants.IPV4_ADDRESS, 32)
            ret_string += self.format_byte_string(self.get_rip_next_hop(index), PacketConstants.IPV4_ADDRESS, 32)
            ret_string += self.format_byte_string(self.get_rip_metric(index), PacketConstants.INTEGER, 32)
        return ret_string

    @staticmethod
    def compare_rip_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, RipPacketHeader)
            assert isinstance(actual, RipPacketHeader)
            if expected.is_field_set(expected.get_rip_command()) and \
                    RipPacketConstants.RIP_COMMAND not in ignore_list:
                name = "RIP command : "
                if expected.get_rip_command() != actual.get_rip_command():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_rip_command()) + " != " +
                                                      str(actual.get_rip_command()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_rip_command()) + " == " +
                                                 str(actual.get_rip_command()) + " Pass")

            if expected.is_field_set(expected.get_rip_version()) and \
                    RipPacketConstants.RIP_VERSION not in ignore_list:
                name = "RIP version : "
                if expected.get_rip_version() != actual.get_rip_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_rip_version()) + " != " +
                                                      str(actual.get_rip_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_rip_version()) + " == " +
                                                 str(actual.get_rip_version()) + " Pass")

            if expected.is_field_set(expected.get_rip_zeros()) and \
                    RipPacketConstants.RIP_ZEROS not in ignore_list:
                name = "RIP zeros : "
                if expected.get_rip_zeros() != actual.get_rip_zeros():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_rip_zeros()) + " != " +
                                                      str(actual.get_rip_zeros()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_rip_zeros()) + " == " +
                                                 str(actual.get_rip_zeros()) + " Pass")

            index = 1
            for index in range(1, NumberUtils.to_integer_value(expected.get_metric_num(index)) + 1):
                if expected.is_field_set(expected.get_rip_address_family(index)) and \
                        RipPacketConstants.RIP_ADDRESS_FAMILY not in ignore_list:
                    name = "RIP address_family : "
                    if expected.get_rip_address_family(index) != actual.get_rip_address_family(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_rip_address_family(index)) + " != " +
                                                          str(actual.get_rip_address_family(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_rip_address_family(index)) + " == " +
                                                     str(actual.get_rip_address_family(index)) + " Pass")

                if expected.is_field_set(expected.get_rip_route_tag(index)) and \
                        RipPacketConstants.RIP_ROUTE_TAG not in ignore_list:
                    name = "RIP route_tag : "
                    if expected.get_rip_route_tag(index) != actual.get_rip_route_tag(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_rip_route_tag(index)) + " != " +
                                                          str(actual.get_rip_route_tag(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_rip_route_tag(index)) + " == " +
                                                     str(actual.get_rip_route_tag(index)) + " Pass")

                if expected.is_field_set(expected.get_rip_ip_address(index)) and \
                        RipPacketConstants.RIP_IP_ADDRESS not in ignore_list:
                    name = "RIP ip_address : "
                    if expected.get_rip_ip_address(index) != actual.get_rip_ip_address(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_rip_ip_address(index)) + " != " +
                                                          str(actual.get_rip_ip_address(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_rip_ip_address(index)) + " == " +
                                                     str(actual.get_rip_ip_address(index)) + " Pass")

                if expected.is_field_set(expected.get_rip_netmask(index)) and \
                        RipPacketConstants.RIP_NETMASK not in ignore_list:
                    name = "RIP netmask : "
                    if expected.get_rip_netmask(index) != actual.get_rip_netmask(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_rip_netmask(index)) + " != " +
                                                          str(actual.get_rip_netmask(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_rip_netmask(index)) + " == " +
                                                     str(actual.get_rip_netmask(index)) + " Pass")

                if expected.is_field_set(expected.get_rip_next_hop(index)) and \
                        RipPacketConstants.RIP_NEXT_HOP not in ignore_list:
                    name = "RIP next_hop : "
                    if expected.get_rip_next_hop(index) != actual.get_rip_next_hop(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_rip_next_hop(index)) + " != " +
                                                          str(actual.get_rip_next_hop(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_rip_next_hop(index)) + " == " +
                                                     str(actual.get_rip_next_hop(index)) + " Pass")

                if expected.is_field_set(expected.get_rip_metric(index)) and \
                        RipPacketConstants.RIP_METRIC not in ignore_list:
                    name = "RIP metric : "
                    if expected.get_rip_metric(index) != actual.get_rip_metric(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_rip_metric(index)) + " != " +
                                                          str(actual.get_rip_metric(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_rip_metric(index)) + " == " +
                                                     str(actual.get_rip_metric(index)) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with RipPacketHeader")
        return results


class RipPacketConstants:
    def __init__(self):
        pass

    RIP_COMMAND = "RIP_COMMAND"
    RIP_VERSION = "RIP_VERSION"
    RIP_ZEROS = "RIP_ZEROS"
    RIP_ADDRESS_FAMILY = "RIP_ADDRESS_FAMILY"

    RIP_ROUTE_TAG = "RIP_ROUTE_TAG"
    RIP_IP_ADDRESS = "RIP_IP_ADDRESS"
    RIP_NETMASK = "RIP_NETMASK"
    RIP_NEXT_HOP = "RIP_NEXT_HOP"
    RIP_METRIC = "RIP_METRIC"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
