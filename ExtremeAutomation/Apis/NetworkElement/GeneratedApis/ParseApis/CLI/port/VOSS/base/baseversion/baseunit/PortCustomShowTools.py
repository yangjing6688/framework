from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.port.base.PortBaseCustomShowTools import \
    PortBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


def create_instance(device):
    return PortCustomShowTools(device)


class PortCustomShowTools(PortBaseCustomShowTools):
    def __init__(self, device):
        super(PortCustomShowTools, self).__init__(device)

    def verify_port_enabled(self, output, args, **kwargs):
        port_obj = self.it.get_port_parser_obj(args["port"])
        for port in port_obj.port_list:
            oper_state = self.pw.get_value_by_offset(output, port + "  ", 1)
            if " " in oper_state:
                oper_state = oper_state.split(" ")[0]
            if oper_state.lower() != "up":
                return False, False
        return True, True

    def verify_port_operational(self, output, args, **kwargs):
        port_num = args["port"] + " "
        oper_state = self.pw.get_value_by_offset(output, port_num, 2)

        result = True if oper_state.lower() == "up" else False
        return result, {"ret_oper_state": oper_state}

    def verify_port_mtu(self, output, args, **kwargs):
        port_num = args["port"] + " "
        mtu = self.pw.get_value_by_offset(output, port_num, 5)

        result = True if mtu == args["mtu"] else False
        return result, {"ret_mtu": mtu}

    def verify_port_mac_address(self, output, args, **kwargs):
        mac = StringUtils.normalize_mac(args["mac"])
        port_num = args["port"] + " "
        mac_result = self.pw.get_value_by_offset(output, port_num, 6)
        mac_result = StringUtils.normalize_mac(mac_result)

        result = True if mac_result == mac else False
        return result, {"ret_mac_result": mac_result}

    def verify_port_high_speed(self, output, args, **kwargs):
        port_num = args["port"] + " "
        h_speed = self.pw.get_value_by_offset(output, port_num, 6)

        result = True if h_speed == args["speed"] else False
        return result, {"ret_h_speed": h_speed}

    def verify_port_alias(self, output, args, **kwargs):
        port_num = args["port"] + " "
        name = self.pw.get_value_by_offset(output, port_num, 1)

        result = True if name == args["alias"] else False
        return result, {"ret_name": name}

    def check_port_in_octets(self, output, args, **kwargs):
        port_count = self.pw.get_value_at_location(output, 1, None, 13)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_in_octets": count}

    def check_port_in_unicast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 1)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_in_unicast": count}

    def check_port_in_discard_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_error_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_unknown_protocol_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_out_octets(self, output, args, **kwargs):
        port_count = self.pw.get_value_at_location(output, 2, None, 13)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_out_octets": count}

    def check_port_out_unicast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 2)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_out_unicast": count}

    def check_port_out_discard_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_at_location(output, 5, None, 19)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_out_discard": count}

    def check_port_out_error_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_in_multicast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 3)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_in_mcast": count}

    def check_port_in_broadcast_packets(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_out_multicast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 4)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_out_mcast": count}

    def check_port_out_broadcast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 6)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_out_bcast": count}

    def check_port_64_bit_in_octets(self, output, args, **kwargs):
        port_count = self.pw.get_value_at_location(output, 1, None, 13)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_in_octets": count}

    def check_port_64_bit_out_octets(self, output, args, **kwargs):
        port_count = self.pw.get_value_at_location(output, 2, None, 13)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_out_octets": count}

    def check_port_64_bit_in_unicast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 1)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_in_unicast": count}

    def check_port_64_bit_in_multicast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 3)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_in_mcast": count}

    def check_port_64_bit_in_broadcast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 5)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_in_bcast": count}

    def check_port_64_bit_out_unicast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 2)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_out_unicast": count}

    def check_port_64_bit_out_multicast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 4)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_out_mcast": count}

    def check_port_64_bit_out_broadcast_packets(self, output, args, **kwargs):
        port_num = args["port"] + " "
        port_count = self.pw.get_value_by_offset(output, port_num, 6)
        parse_result = port_count
        self.logger.log_debug(parse_result)
        count_operator = args["count_operator"]
        count = args["count"]

        result = NumberUtils().verify_expected_count(parse_result, count_operator, count)
        return result, {"ret_out_bcast": count}

    def check_port_flex_uni_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 6)
        parse_result = parse_result.split()
        if len(parse_result) == 1:
            result = True if parse_result[0] == "enable" else False
            return result, {"ret_parse_result": parse_result}
        else:
            result = True if parse_result[1] == "enable" else False
            return result, {"ret_parse_result": parse_result}
