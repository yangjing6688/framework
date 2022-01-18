from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.isis.base.IsisBaseCustomShowTools import \
    IsisBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class IsisCustomShowTools(IsisBaseCustomShowTools):
    def __init__(self, device):
        super(IsisCustomShowTools, self).__init__(device)

    def verify_isis_globally_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.1.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def verify_isis_globally_disabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.1.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_state": parse_result}

    def verify_isis_manual_area(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.1.2.1.2." + \
               StringUtils().hex_str_to_dotted_decimal_with_len(args["manual_area"])
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_manual_area": parse_result}

    def verify_isis_sys_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["name"] else False
        return result, {"ret_name": parse_result}

    def verify_isis_ip_source_address(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_inband_mgmt_ip(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_metric_narrow(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_metric_wide(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_overload(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_redistribute_bgp(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_redistribute_direct(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.100.22.1.15." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        return True if parse_result == "1" else False

    def verify_isis_redistribute_ospf(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_redistribute_rip(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_redistribute_static(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_spf_delay(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_sys_id(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.1.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        sysid_arg = StringUtils().normalize_hex_string_to_0x_hex_expression(args["sys_id"])

        result = True if parse_result == sysid_arg else False
        return result, {"ret_sys_id": parse_result}

    def check_isis_circuit_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.3.2.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["port_if_index"] else False
        return result, {"ret_port": parse_result}

    def check_enable_isis_circuit_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.3.2.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def check_isis_circuit_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.3.2.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["mlt_if_index"] else False
        return result, {"ret_mlt": parse_result}

    def check_enable_isis_circuit_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.3.2.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def check_isis_circuit_auth_type_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_auth_type"] else False
        return result, {"ret_auth_type": parse_result}

    def check_isis_circuit_auth_type_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_auth_type"] else False
        return result, {"ret_auth_type": parse_result}

    def check_isis_circuit_auth_key_id_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["key_id"] else False
        return result, {"ret_key_id": parse_result}

    def check_isis_circuit_auth_key_id_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["key_id"] else False
        return result, {"ret_key_id": parse_result}

    def check_isis_adjacency_level_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["level"] else False
        return result, {"ret_level": parse_result}

    def check_isis_adjacency_level_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["level"] else False
        return result, {"ret_level": parse_result}

    def check_isis_adjacency_state_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_state"] else False
        return result, {"ret_adj_state": parse_result}

    def check_isis_adjacency_state_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_state"] else False
        return result, {"ret_adj_state": parse_result}

    def check_isis_adjacency_status_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.10.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_adj_status": parse_result}

    def check_isis_adjacency_status_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.10.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_adj_status": parse_result}

    def check_isis_adjacency_uptime_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.11." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            num_of_seconds = StringUtils().convert_elapsed_time_to_seconds(args["time"])

            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], num_of_seconds)
            return result, {"ret_uptime": parse_result}

    def check_isis_adjacency_uptime_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.11." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            num_of_seconds = StringUtils().convert_elapsed_time_to_seconds(args["time"])

            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], num_of_seconds)
            return result, {"ret_uptime": parse_result}

    def check_isis_adjacency_priority_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["priority"] else False
        return result, {"ret_adj_priority": parse_result}

    def check_isis_adjacency_priority_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["priority"] else False
        return result, {"ret_adj_priority": parse_result}

    def check_isis_adjacency_holdtime_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["holdtime"])
            return result, {"ret_holdtime": parse_result}

    def check_isis_adjacency_holdtime_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["holdtime"])
            return result, {"ret_holdtime": parse_result}

    def check_isis_adjacency_sysid_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        sysid_arg = StringUtils().normalize_hex_string_to_0x_hex_expression(args["sys_id"])

        result = True if parse_result == sysid_arg else False
        return result, {"ret_sys_id": parse_result}

    def check_isis_adjacency_sysid_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        sysid_arg = StringUtils().normalize_hex_string_to_0x_hex_expression(args["sys_id"])

        result = True if parse_result == sysid_arg else False
        return result, {"ret_sys_id": parse_result}

    def check_isis_adjacency_hostname_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.10.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["hostname"] else False
        return result, {"ret_hostname": parse_result}

    def check_isis_adjacency_hostname_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.10.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["hostname"] else False
        return result, {"ret_hostname": parse_result}

    def check_isis_l1_hello_interval_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.4.1.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = True if parse_result == StringUtils.convert_seconds_to_milliseconds(args["interval"]) else False
            return result, {"ret_hello_interval": parse_result}

    def check_isis_l1_hello_interval_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.4.1.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = True if parse_result == StringUtils.convert_seconds_to_milliseconds(args["interval"]) else False
            return result, {"ret_hello_interval": parse_result}

    def check_isis_l1_hello_multiplier_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.4.1.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["multiplier"] else False
        return result, {"ret_hello_multiplier": parse_result}

    def check_isis_l1_hello_multiplier_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.4.1.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["multiplier"] else False
        return result, {"ret_hello_multiplier": parse_result}

    def check_isis_l1_dr_hello_interval_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.4.1.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = True if parse_result == StringUtils.convert_seconds_to_milliseconds(args["interval"]) else False
            return result, {"ret_dr_hello": parse_result}

    def check_isis_l1_dr_hello_interval_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.4.1.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = True if parse_result == StringUtils.convert_seconds_to_milliseconds(args["interval"]) else False
            return result, {"ret_dr_hello": parse_result}

    def check_isis_corrupted_lsps(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.1.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_corrupted_lsps": parse_result}

    def check_isis_authentication_key_fails(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.1.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_auth_key_fails": parse_result}

    def check_isis_manual_addresses_dropped_from_area(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.1.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_addrs_dropped": parse_result}

    def check_isis_maximum_sequence_number_exceeded_attempts(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.1.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_max_seq_exceeded": parse_result}

    def check_isis_sequence_number_skips(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.1.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_seq_num_skips": parse_result}

    def check_isis_own_lsp_purges(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.1.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_own_lsp_purges": parse_result}

    def check_isis_id_length_mismatches(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.1.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_id_len_mismatches": parse_result}

    def check_isis_partition_changes(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.1.1.11." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_partition_changes": parse_result}

    def check_isis_lsp_database_overloads(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.1.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_db_overloads": parse_result}

    def check_isis_port_authentication_fails(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_auth_fails": parse_result}

    def check_isis_port_adjacency_changes(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_adj_changes": parse_result}

    def check_isis_port_initialization_fails(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_init_fails": parse_result}

    def check_isis_port_rejected_adjancencies(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_rejected_adj": parse_result}

    def check_isis_port_id_field_length_mismatches(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_id_len_mismatches": parse_result}

    def check_isis_port_max_area_address_mismatches(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_max_addr_mismatches": parse_result}

    def check_isis_port_designated_is_changes(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_is_changes": parse_result}

    def check_isis_l1_port_is_is_hellos_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hello_tx": parse_result}

    def check_isis_l1_port_is_is_hellos_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hello_rx": parse_result}

    def check_isis_l1_port_is_is_lsps_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_tx": parse_result}

    def check_isis_l1_port_is_is_lsps_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_rx": parse_result}

    def check_isis_l1_port_is_is_csnps_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_tx": parse_result}

    def check_isis_l1_port_is_is_csnps_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_rx": parse_result}

    def check_isis_l1_port_is_is_psnps_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_tx": parse_result}

    def check_isis_l1_port_is_is_psnps_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_rx": parse_result}

    def verify_isis_logical_interface_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.26.1.8." + args["oid_index"]
        name_found = self.pw.get_value_by_offset(output, item, 2)

        result = True if name_found == args["name"] else False
        return result, {"ret_name": name_found}

    def verify_isis_logical_interface_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.26.1.5." + args["oid_index"]
        port_found = self.pw.get_value_by_offset(output, item, 2)

        result = True if port_found == args["port_if_index"] else False
        return result, {"ret_port": port_found}

    def verify_isis_logical_interface_port_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.26.1.8." + args["oid_index"]
        name_found = self.pw.get_value_by_offset(output, item, 2)

        result = True if name_found == args["name"] else False
        return result, {"ret_name": name_found}

    def verify_isis_logical_interface_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.26.1.5." + args["oid_index"]
        port_found = self.pw.get_value_by_offset(output, item, 2)

        result = True if port_found == args["mlt_if_index"] else False
        return result, {"ret_mlt": port_found}

    def verify_isis_logical_interface_mlt_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.26.1.8." + args["oid_index"]
        name_found = self.pw.get_value_by_offset(output, item, 2)

        result = True if name_found == args["name"] else False
        return result, {"ret_name": name_found}

    def check_isis_circuit_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.3.2.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["isis_logical_interface_index"] else False
        return result, {"ret_logical_interface": parse_result}

    def check_enable_isis_circuit_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.3.2.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def check_isis_circuit_auth_type_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_auth_type"] else False
        return result, {"ret_auth_type": parse_result}

    def check_isis_circuit_auth_key_id_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["key_id"] else False
        return result, {"ret_key_id": parse_result}

    def check_isis_adjacency_level_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["level"] else False
        return result, {"ret_level": parse_result}

    def check_isis_adjacency_state_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_state"] else False
        return result, {"ret_adj_state": parse_result}

    def check_isis_adjacency_status_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.10.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_adj_status": parse_result}

    def check_isis_adjacency_uptime_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.11." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            num_of_seconds = StringUtils().convert_elapsed_time_to_seconds(args["time"])
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], num_of_seconds)
            return result, {"ret_uptime": parse_result}

    def check_isis_adjacency_priority_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["priority"] else False
        return result, {"ret_adj_priority": parse_result}

    def check_isis_adjacency_holdtime_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["holdtime"])
            return result, {"ret_holdtime": parse_result}

    def check_isis_adjacency_sysid_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.6.1.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        sysid_arg = StringUtils().normalize_hex_string_to_0x_hex_expression(args["sys_id"])

        result = True if parse_result == sysid_arg else False
        return result, {"ret_sys_id": parse_result}

    def check_isis_adjacency_hostname_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.10.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["hostname"] else False
        return result, {"ret_hostname": parse_result}

    def check_isis_l1_hello_interval_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.4.1.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = True if parse_result == StringUtils.convert_seconds_to_milliseconds(args["interval"]) else False
            return result, {"ret_hello_interval": parse_result}

    def check_isis_l1_hello_multiplier_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.4.1.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["multiplier"] else False
        return result, {"ret_hello_multiplier": parse_result}

    def check_isis_l1_dr_hello_interval_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.4.1.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = True if parse_result == StringUtils.convert_seconds_to_milliseconds(args["interval"]) else False
            return result, {"ret_dr_hello": parse_result}

    def check_isis_lsdb_ip_and_hostname(self, output, args, **kwargs):
        return self.constants.METHOD_NOT_SUPPORTED

    def check_isis_mlt_authentication_fails(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_auth_fails": parse_result}

    def check_isis_mlt_adjacency_changes(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_adj_changes": parse_result}

    def check_isis_mlt_initialization_fails(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_init_fails": parse_result}

    def check_isis_mlt_rejected_adjancencies(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_rejected_adj": parse_result}

    def check_isis_mlt_id_field_length_mismatches(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_id_len_mismatches": parse_result}

    def check_isis_mlt_max_area_address_mismatches(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_max_addr_mismatches": parse_result}

    def check_isis_mlt_designated_is_changes(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_is_changes": parse_result}

    def check_isis_l1_mlt_is_is_hellos_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hello_tx": parse_result}

    def check_isis_l1_mlt_is_is_hellos_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hello_rx": parse_result}

    def check_isis_l1_mlt_is_is_lsps_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_tx": parse_result}

    def check_isis_l1_mlt_is_is_lsps_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_rx": parse_result}

    def check_isis_l1_mlt_is_is_csnps_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_tx": parse_result}

    def check_isis_l1_mlt_is_is_csnps_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_rx": parse_result}

    def check_isis_l1_mlt_is_is_psnps_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_tx": parse_result}

    def check_isis_l1_mlt_is_is_psnps_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_rx": parse_result}

    def check_isis_logical_interface_authentication_fails(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_auth_fails": parse_result}

    def check_isis_logical_interface_adjacency_changes(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_adj_changes": parse_result}

    def check_isis_logical_interface_initialization_fails(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_init_fails": parse_result}

    def check_isis_logical_interface_rejected_adjancencies(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_rejected_adj": parse_result}

    def check_isis_logical_interface_id_field_length_mismatches(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_id_len_mismatches": parse_result}

    def check_isis_logical_interface_max_area_address_mismatches(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_max_addr_mismatches": parse_result}

    def check_isis_logical_interface_designated_is_changes(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.2.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_is_changes": parse_result}

    def check_isis_l1_logical_interface_is_is_hellos_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hello_tx": parse_result}

    def check_isis_l1_logical_interface_is_is_hellos_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hello_rx": parse_result}

    def check_isis_l1_logical_interface_is_is_lsps_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_tx": parse_result}

    def check_isis_l1_logical_interface_is_is_lsps_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_rx": parse_result}

    def check_isis_l1_logical_interface_is_is_csnps_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_tx": parse_result}

    def check_isis_l1_logical_interface_is_is_csnps_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_rx": parse_result}

    def check_isis_l1_logical_interface_is_is_psnps_transmitted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_tx": parse_result}

    def check_isis_l1_logical_interface_is_is_psnps_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::experimental.37.1.5.3.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_rx": parse_result}

    def verify_isis_logical_interface_ipv4(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.26.1.4." + args["oid_index"]
        ip_found = self.pw.get_value_by_offset(output, item, 2)

        result = True if ip_found == args["ip"] else False
        return result, {"ret_ip": ip_found}

    def check_isis_ipv4_source_address(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.1.13." + args["oid_index"]
        ip_found = StringUtils().hex_str_to_dotted_decimal(self.pw.get_value_by_offset(output, item, 2))

        result = True if ip_found == args["ip"] else False
        return result, {"ret_ip": ip_found}

    def check_isis_ipv4_tunnel_source_address(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.1.17." + args["oid_index"]
        ip_found = self.pw.get_value_by_offset(output, item, 2)

        result = True if ip_found == args["ip"] else False
        return result, {"ret_ip": ip_found}

    def verify_isis_redistribute_direct_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.100.22.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def verify_isis_redistribute_direct_disabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.100.22.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_state": parse_result}

    def check_isis_ipv6_source_address(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.1.15." + args["oid_index"]
        ip_found = self.pw.get_value_by_offset(output, item, 2)

        result = True if ip_found == StringUtils().ipaddr_to_pure_hex(args["ipv6_addr"]) else False
        return result, {"ret_ip": ip_found}

    def verify_isis_redistribute_direct_route_map_policy(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.100.22.1.11." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["policy_name"] else False
        return result, {"ret_rmap": parse_result}

    def verify_isis_redistribute_direct_route_map_policy_clear(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.100.22.1.11." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = False if parse_result == args["policy_name"] else True
        return result, {"ret_rmap": parse_result}
