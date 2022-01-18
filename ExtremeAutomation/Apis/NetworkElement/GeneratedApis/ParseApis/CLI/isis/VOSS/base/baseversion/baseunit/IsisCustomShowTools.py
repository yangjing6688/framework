from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.isis.base.IsisBaseCustomShowTools import \
    IsisBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


def create_instance(device):
    return IsisCustomShowTools(device)


class IsisCustomShowTools(IsisBaseCustomShowTools):
    def __init__(self, device):
        super(IsisCustomShowTools, self).__init__(device)

    def verify_isis_globally_enabled(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        isis_state = self.pw.get_value_by_offset(output.lower(), "adminstate", 2)

        result = True if isis_state == "enabled" else False
        return result, {"ret_global_state": isis_state}

    def verify_isis_globally_disabled(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        isis_state = self.pw.get_value_by_offset(output.lower(), "adminstate", 2)

        result = True if isis_state == "disabled" else False
        return result, {"ret_global_state": isis_state}

    def verify_isis_sys_id(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        system_id = self.pw.get_value_by_offset(output.lower(), "system", 3)

        result = True if system_id == args["sys_id"] else False
        return result, {"ret_sys_id": system_id}

    def verify_isis_manual_area(self, output, args, **kwargs):
        area = []
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["manual_area"]:
                    area = line.split()[0]
                    break
        result = True if area == args["manual_area"] else False
        return result, {"ret_manual_area": area}

    def verify_isis_sys_name(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        sys_name = self.pw.get_value_by_offset(output, "Name", 3)

        result = True if sys_name == args["name"] else False
        return result, {"ret_sys_name": sys_name}

    def verify_isis_ip_source_address(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_inband_mgmt_ip(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_metric_narrow(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_metric_wide(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_overload(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_redistribute_bgp(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_redistribute_ospf(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_redistribute_rip(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_redistribute_static(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_spf_delay(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_isis_circuit_on_port(self, output, args, **kwargs):
        found_port = self.pw.get_value_by_offset(output, args["port"], 0)

        result = True if found_port == "Port" + args["port"] else False
        return result, {"ret_circuit_port": found_port}

    def check_enable_isis_circuit_on_port(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output, args["port"], 5)

        result = True if found_status == "UP" else False
        return result, {"ret_circuit_status": found_status}

    def check_isis_circuit_on_mlt(self, output, args, **kwargs):
        found_mlt = self.pw.get_exact_value_by_offset(output, "Mlt" + args["mlt_id"], 0)

        result = True if found_mlt == "Mlt" + args["mlt_id"] else False
        return result, {"ret_circuit_mlt": found_mlt}

    def check_enable_isis_circuit_on_mlt(self, output, args, **kwargs):
        found_status = self.pw.get_exact_value_by_offset(output, "Mlt" + args["mlt_id"], 5)

        result = True if found_status == "UP" else False
        return result, {"ret_circuit_status": found_status}

    def check_isis_circuit_auth_type_on_port(self, output, args, **kwargs):
        output = output.lower()
        auth_type = self.pw.get_exact_value_by_offset(output, "port" + args["port"], 1)

        result = True if auth_type == args["auth_type"] else False
        return result, {"ret_auth_type": auth_type}

    def check_isis_circuit_auth_type_on_mlt(self, output, args, **kwargs):
        output = output.lower()
        auth_type = self.pw.get_exact_value_by_offset(output, "mlt" + args["mlt_id"], 1)

        result = True if auth_type == args["auth_type"] else False
        return result, {"ret_auth_type": auth_type}

    def check_isis_circuit_auth_key_id_on_port(self, output, args, **kwargs):
        output = output.lower()
        key_id = self.pw.get_exact_value_by_offset(output, "port" + args["port"], 2)

        result = True if key_id == args["key_id"] else False
        return result, {"ret_auth_key_id": key_id}

    def check_isis_circuit_auth_key_id_on_mlt(self, output, args, **kwargs):
        output = output.lower()
        key_id = self.pw.get_exact_value_by_offset(output, "mlt" + args["mlt_id"], 2)

        result = True if key_id == args["key_id"] else False
        return result, {"ret_auth_key_id": key_id}

    def check_isis_adjacency_level_on_port(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "port" + args["port"], 1)
        if args["adj_index"].isdigit():
            if len(parse_result.split()) >= int(args["adj_index"]):
                parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == args["level"] else False
        return result, {"ret_adj_level": parse_result}

    def check_isis_adjacency_level_on_mlt(self, output, args, **kwargs):
        output = output.lower()
        adj_level = self.pw.get_exact_value_by_offset(output, "mlt" + args["mlt_id"], 1)
        if args["adj_index"].isdigit():
            adj_level = adj_level.split()[int(args["adj_index"]) - 1]

        result = True if adj_level == args["level"] else False
        return result, {"ret_adj_level": adj_level}

    def check_isis_adjacency_state_on_port(self, output, args, **kwargs):
        output = output.lower()
        adj_state = self.pw.get_exact_value_by_offset(output, "port" + args["port"], 2)
        if args["adj_index"].isdigit():
            adj_state = adj_state.split()[int(args["adj_index"]) - 1]

        result = True if adj_state == args["state"] else False
        return result, {"ret_adj_state": adj_state}

    def check_isis_adjacency_state_on_mlt(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "mlt" + args["mlt_id"], 2)
        if args["adj_index"].isdigit():
            if len(parse_result.split()) >= int(args["adj_index"]):
                parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == args["state"] else False
        return result, {"ret_adj_state": parse_result}

    def check_isis_adjacency_status_on_port(self, output, args, **kwargs):
        output = output.lower().replace("d ", ":")
        adj_status = self.pw.get_exact_value_by_offset(output, "port" + args["port"], 8)
        if args["adj_index"].isdigit():
            adj_status = adj_status.split()[int(args["adj_index"]) - 1]

        result = True if adj_status == "active" else False
        return result, {"ret_adj_status": adj_status}

    def check_isis_adjacency_status_on_mlt(self, output, args, **kwargs):
        output = output.lower().replace("d ", ":")
        adj_status = self.pw.get_exact_value_by_offset(output, "mlt" + args["mlt_id"], 8)
        if args["adj_index"].isdigit():
            adj_status = adj_status.split()[int(args["adj_index"]) - 1]

        result = True if adj_status == "active" else False
        return result, {"ret_adj_status": adj_status}

    def check_isis_adjacency_uptime_on_port(self, output, args, **kwargs):
        output = output.lower().replace("d ", "d:")
        parse_result = self.pw.get_exact_value_by_offset(output, "port" + args["port"], 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            adj_uptime = parse_result.split()
            num_of_seconds = StringUtils().convert_elapsed_time_to_seconds(args["time"])
            adj_uptime = adj_uptime[int(args["adj_index"]) - 1]
            adj_uptime = StringUtils().convert_elapsed_time_to_seconds(adj_uptime)

            result = NumberUtils.verify_expected_count(adj_uptime, args["count_operator"], num_of_seconds)
            return result, {"ret_adj_uptime": adj_uptime}

    def check_isis_adjacency_uptime_on_mlt(self, output, args, **kwargs):
        output = output.lower().replace("d ", "d:")
        parse_result = self.pw.get_exact_value_by_offset(output, "mlt" + args["mlt_id"], 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            adj_uptime = parse_result.split()
            num_of_seconds = StringUtils().convert_elapsed_time_to_seconds(args["time"])
            adj_uptime = StringUtils().convert_elapsed_time_to_seconds(adj_uptime[int(args["adj_index"]) - 1])

            result = NumberUtils.verify_expected_count(adj_uptime, args["count_operator"], num_of_seconds)
            return result, {"ret_adj_uptime": adj_uptime}

    def check_isis_adjacency_priority_on_port(self, output, args, **kwargs):
        output = output.lower().replace("d ", ":")
        parse_result = self.pw.get_exact_value_by_offset(output, "port" + args["port"], 4)
        if args["adj_index"].isdigit():
            parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == args["priority"] else False
        return result, {"ret_adj_priority": parse_result}

    def check_isis_adjacency_priority_on_mlt(self, output, args, **kwargs):
        output = output.lower().replace("d ", ":")
        parse_result = self.pw.get_exact_value_by_offset(output, "mlt" + args["mlt_id"], 4)
        if args["adj_index"].isdigit():
            if len(parse_result.split()) >= int(args["adj_index"]):
                parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == args["priority"] else False
        return result, {"ret_adj_priority": parse_result}

    def check_isis_adjacency_holdtime_on_port(self, output, args, **kwargs):
        output = output.lower().replace("d ", ":")
        parse_result = self.pw.get_exact_value_by_offset(output, "port" + args["port"], 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            hold_time = parse_result.split()[int(args["adj_index"]) - 1]
            result = NumberUtils.verify_expected_count(hold_time, args["count_operator"],
                                                       args["holdtime"])
            return result, {"ret_adj_hold_time": hold_time}

    def check_isis_adjacency_holdtime_on_mlt(self, output, args, **kwargs):
        output = output.lower().replace("d ", ":")
        parse_result = self.pw.get_exact_value_by_offset(output, "mlt" + args["mlt_id"], 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            hold_time = parse_result.split()[int(args["adj_index"]) - 1]
            result = NumberUtils.verify_expected_count(hold_time, args["count_operator"],
                                                       args["holdtime"])
            return result, {"ret_adj_hold_time": hold_time}

    def check_isis_adjacency_sysid_on_port(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, args["sys_id"].lower(), 0)
        if args["adj_index"].isdigit():
            parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == "port" + args["port"] else False
        return result, {"ret_adj_sysid": parse_result}

    def check_isis_adjacency_sysid_on_mlt(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, args["sys_id"].lower(), 0)
        if args["adj_index"].isdigit():
            if len(parse_result.split()) >= int(args["adj_index"]):
                parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == "mlt" + args["mlt_id"] else False
        return result, {"ret_adj_sysid": parse_result}

    def check_isis_adjacency_hostname_on_port(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output, args["hostname"], 0)
        if args["adj_index"].isdigit():
            if len(parse_result.split()) >= int(args["adj_index"]):
                parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == "Port" + args["port"] else False
        return result, {"ret_adj_hostname": parse_result}

    def check_isis_adjacency_hostname_on_mlt(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output, args["hostname"], 0)

        hostname = "valueNotPresent"
        if args["adj_index"].isdigit():
            try:
                hostname = parse_result.split()[int(args["adj_index"]) - 1]
            except IndexError:
                pass

        result = True if hostname == "Mlt" + args["mlt_id"] else False
        return result, {"ret_adj_hostname": hostname}

    def check_isis_l1_hello_interval_on_port(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + "1"
        l1_hello = self.pw.get_exact_value_by_offset(output, item, 3)

        result = True if l1_hello == args["interval"] else False
        return result, {"ret_l1_hello": l1_hello}

    def check_isis_l1_hello_interval_on_mlt(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + "1"
        l1_hello = self.pw.get_exact_value_by_offset(output, item, 3)

        result = True if l1_hello == args["interval"] else False
        return result, {"ret_l1_hello": l1_hello}

    def check_isis_l1_hello_multiplier_on_port(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + "1"
        hello_mult = self.pw.get_exact_value_by_offset(output, item, 4)

        result = True if hello_mult == args["multiplier"] else False
        return result, {"ret_hello_multiplier": hello_mult}

    def check_isis_l1_hello_multiplier_on_mlt(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + "1"
        hello_mult = self.pw.get_exact_value_by_offset(output, item, 4)

        result = True if hello_mult == args["multiplier"] else False
        return result, {"ret_hello_multiplier": hello_mult}

    def check_isis_l1_dr_hello_interval_on_port(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + "1"
        hello_int = self.pw.get_exact_value_by_offset(output, item, 5)

        result = True if hello_int == args["interval"] else False
        return result, {"ret_dr_hello": hello_int}

    def check_isis_l1_dr_hello_interval_on_mlt(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + "1"
        hello_int = self.pw.get_exact_value_by_offset(output, item, 5)

        result = True if hello_int == args["interval"] else False
        return result, {"ret_dr_hello": hello_int}

    def check_isis_lsdb_ip_and_hostname(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output, args["address"], 7)

        result = True if parse_result == args["host_name"] else False
        return result, {"ret_hostname": parse_result}

    def check_isis_corrupted_lsps(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "level-" + args["level"], 1)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_currupted_lsps": parse_result}

    def check_isis_authentication_key_fails(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "level-" + args["level"], 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_auth_key_fails": parse_result}

    def check_isis_manual_addresses_dropped_from_area(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "level-" + args["level"], 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_addr_dropped": parse_result}

    def check_isis_maximum_sequence_number_exceeded_attempts(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "level-" + args["level"], 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_seq_num_exceeded": parse_result}

    def check_isis_sequence_number_skips(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "level-" + args["level"], 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_seq_num_skips": parse_result}

    def check_isis_own_lsp_purges(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "level-" + args["level"], 6)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_own_lsp_purges": parse_result}

    def check_isis_id_length_mismatches(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "level-" + args["level"], 7)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_id_len_mismatches": parse_result}

    def check_isis_partition_changes(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "level-" + args["level"], 8)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_partition_changes": parse_result}

    def check_isis_lsp_database_overloads(self, output, args, **kwargs):
        output = output.lower()
        parse_result = self.pw.get_exact_value_by_offset(output, "level-" + args["level"], 9)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsp_db_overloads": parse_result}

    def verify_isis_logical_interface_name(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        name_found = self.pw.get_exact_value_by_offset(output, args["index"], 1)

        result = True if name_found == args["name"].lower() else False
        return result, {"ret_logical_int_name": name_found}

    def verify_isis_logical_interface_port(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        port_found = self.pw.get_exact_value_by_offset(output, args["index"], 3)
        port_found = port_found.replace("port", "")

        result = True if port_found == args["port"] else False
        return result, {"ret_logical_int_port": port_found}

    def verify_isis_logical_interface_port_name(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        name_found = self.pw.get_exact_value_by_offset(output, args["index"], 1)

        result = True if name_found == args["name"].lower() else False
        return result, {"ret_logical_int_port_name": name_found}

    def verify_isis_logical_interface_mlt(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        mlt_found = self.pw.get_exact_value_by_offset(output, args["index"], 3)
        mlt_found = mlt_found.replace("mlt", "")

        result = True if mlt_found == args["mlt_index"] else False
        return result, {"ret_logical_int_mlt": mlt_found}

    def verify_isis_logical_interface_mlt_name(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        name_found = self.pw.get_exact_value_by_offset(output, args["index"], 1)

        result = True if name_found == args["name"].lower() else False
        return result, {"ret_logical_int_mlt_name": name_found}

    def check_isis_port_authentication_fails(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_auth_fails": parse_result}

    def check_isis_port_adjacency_changes(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_adj_changes": result}

    def check_isis_port_initialization_fails(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_init_fails": parse_result}

    def check_isis_port_rejected_adjancencies(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 6)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_rejected_adj": parse_result}

    def check_isis_port_id_field_length_mismatches(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 7)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_id_len_mismatches": parse_result}

    def check_isis_port_max_area_address_mismatches(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 8)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_max_addr_mismatches": parse_result}

    def check_isis_port_designated_is_changes(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 9)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_is_changes": parse_result}

    def check_isis_l1_port_is_is_hellos_transmitted(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hellos_tx": parse_result}

    def check_isis_l1_port_is_is_hellos_received(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hellos_rx": parse_result}

    def check_isis_l1_port_is_is_lsps_transmitted(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_tx": parse_result}

    def check_isis_l1_port_is_is_lsps_received(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_rx": parse_result}

    def check_isis_l1_port_is_is_csnps_transmitted(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_tx": parse_result}

    def check_isis_l1_port_is_is_csnps_received(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_rx": parse_result}

    def check_isis_l1_port_is_is_psnps_transmitted(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_tx": parse_result}

    def check_isis_l1_port_is_is_psnps_received(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "port" + args["port"] + " " + "received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_rx": parse_result}

    def check_isis_mlt_authentication_fails(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_auth_fails": parse_result}

    def check_isis_mlt_adjacency_changes(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_adj_changes": parse_result}

    def check_isis_mlt_initialization_fails(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_init_fails": parse_result}

    def check_isis_mlt_rejected_adjancencies(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 6)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_rejected_adj": parse_result}

    def check_isis_mlt_id_field_length_mismatches(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 7)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_id_len_mismatches": parse_result}

    def check_isis_mlt_max_area_address_mismatches(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 8)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_max_addr_mismatches": parse_result}

    def check_isis_mlt_designated_is_changes(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 9)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_is_changes": parse_result}

    def check_isis_l1_mlt_is_is_hellos_transmitted(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hellos_tx": parse_result}

    def check_isis_l1_mlt_is_is_hellos_received(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hellos_rx": parse_result}

    def check_isis_l1_mlt_is_is_lsps_transmitted(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_tx": parse_result}

    def check_isis_l1_mlt_is_is_lsps_received(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_rx": parse_result}

    def check_isis_l1_mlt_is_is_csnps_transmitted(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_tx": parse_result}

    def check_isis_l1_mlt_is_is_csnps_received(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_rx": parse_result}

    def check_isis_l1_mlt_is_is_psnps_transmitted(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_tx": parse_result}

    def check_isis_l1_mlt_is_is_psnps_received(self, output, args, **kwargs):
        output = output.lower()
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = "mlt" + args["mlt_id"] + " " + "received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_rx": parse_result}

    def check_isis_logical_interface_authentication_fails(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_auth_fails": parse_result}

    def check_isis_logical_interface_adjacency_changes(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_adj_changes": parse_result}

    def check_isis_logical_interface_initialization_fails(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_init_fails": parse_result}

    def check_isis_logical_interface_rejected_adjancencies(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 6)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_rejected_adj": parse_result}

    def check_isis_logical_interface_id_field_length_mismatches(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 7)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_id_len_mismatches": parse_result}

    def check_isis_logical_interface_max_area_address_mismatches(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 8)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_max_addr_mismatches": parse_result}

    def check_isis_logical_interface_designated_is_changes(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + args["level"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 9)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_is_changes": parse_result}

    def check_isis_l1_logical_interface_is_is_hellos_transmitted(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0).split()[0]
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hellos_tx": parse_result}

    def check_isis_l1_logical_interface_is_is_hellos_received(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0).split()[0]
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_hellos_rx": parse_result}

    def check_isis_l1_logical_interface_is_is_lsps_transmitted(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0).split()[0]
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_tx": parse_result}

    def check_isis_l1_logical_interface_is_is_lsps_received(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0).split()[0]
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_lsps_rx": parse_result}

    def check_isis_l1_logical_interface_is_is_csnps_transmitted(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0).split()[0]
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_tx": parse_result}

    def check_isis_l1_logical_interface_is_is_csnps_received(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0).split()[0]
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_csnps_rx": parse_result}

    def check_isis_l1_logical_interface_is_is_psnps_transmitted(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0).split()[0]
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Transmitted"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_tx": parse_result}

    def check_isis_l1_logical_interface_is_is_psnps_received(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0).split()[0]
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Received"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
            return result, {"ret_psnps_rx": parse_result}

    def check_isis_circuit_on_logical_interface(self, output, args, **kwargs):
        found_interface = self.pw.get_value_by_offset(output, args["isis_id"], 0)

        result = True if found_interface != "valueNotPresent" else False
        return result, {"ret_circuit_logical_int": found_interface}

    def check_enable_isis_circuit_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        found_status = self.pw.get_value_by_offset(output, cli_ifidx, 5)

        result = True if found_status == "UP" else False
        return result, {"ret_circuit_status": found_status}

    def check_isis_circuit_auth_type_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        found_type = self.pw.get_exact_value_by_offset(output, cli_ifidx, 1)

        result = True if found_type == args["auth_type"] else False
        return result, {"ret_auth_type": found_type}

    def check_isis_circuit_auth_key_id_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        parse_result = self.pw.get_exact_value_by_offset(output, cli_ifidx, 2)

        result = True if parse_result == args["key_id"] else False
        return result, {"ret_auth_key_id": parse_result}

    def check_isis_adjacency_level_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        parse_result = self.pw.get_exact_value_by_offset(output, cli_ifidx, 1)
        if args["adj_index"].isdigit():
            if len(parse_result.split()) >= int(args["adj_index"]):
                parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == args["level"] else False
        return result, {"ret_adj_level": parse_result}

    def check_isis_adjacency_state_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        parse_result = self.pw.get_exact_value_by_offset(output, cli_ifidx, 2)
        if args["adj_index"].isdigit():
            parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == args["state"] else False
        return result, {"ret_adj_state": parse_result}

    def check_isis_adjacency_status_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        output = output.replace("d ", ":")
        parse_result = self.pw.get_exact_value_by_offset(output, cli_ifidx, 8)
        if args["adj_index"].isdigit():
            parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == "active" else False
        return result, {"ret_adj_status": parse_result}

    def check_isis_adjacency_uptime_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        output = output.replace("d ", "d:")
        parse_result = self.pw.get_exact_value_by_offset(output, cli_ifidx, 3)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            result = parse_result.split()
            num_of_seconds = StringUtils().convert_elapsed_time_to_seconds(args["time"])
            res = result[int(args["adj_index"]) - 1]
            res = StringUtils().convert_elapsed_time_to_seconds(res)

            result = NumberUtils.verify_expected_count(res, args["count_operator"], num_of_seconds)
            return result, {"ret_adj_uptime": res}

    def check_isis_adjacency_priority_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        output = output.replace("d ", ":")
        parse_result = self.pw.get_exact_value_by_offset(output, cli_ifidx, 4)
        if args["adj_index"].isdigit():
            parse_result = parse_result.split()[int(args["adj_index"]) - 1]

        result = True if parse_result == args["priority"] else False
        return result, {"ret_adj_priority": parse_result}

    def check_isis_adjacency_holdtime_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        output = output.replace("d ", ":")
        parse_result = self.pw.get_exact_value_by_offset(output, cli_ifidx, 5)
        if "valueNotPresent" in parse_result:
            return False, None
        else:
            parse_result = parse_result.split()[int(args["adj_index"]) - 1]
            result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["holdtime"])
            return result, {"ret_adj_hold_time": parse_result}

    def check_isis_adjacency_sysid_on_logical_interface(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output, args["sys_id"].lower(), 0)
        if args["adj_index"].isdigit():
            parse_result = parse_result.split()[int(args["adj_index"]) - 1]
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)

        result = True if parse_result == cli_ifidx else False
        return result, {"ret_adj_sysid": parse_result}

    def check_isis_adjacency_hostname_on_logical_interface(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output, args["hostname"], 0)
        if args["adj_index"].isdigit():
            if len(parse_result.split()) >= int(args["adj_index"]):
                parse_result = parse_result.split()[int(args["adj_index"]) - 1]
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)

        result = True if parse_result == cli_ifidx else False
        return result, {"ret_adj_hostname": parse_result}

    def check_isis_l1_hello_interval_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + "1"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 3)

        result = True if parse_result == args["interval"] else False
        return result, {"ret_l1_hello": parse_result}

    def check_isis_l1_hello_multiplier_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + "1"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 4)

        result = True if parse_result == args["multiplier"] else False
        return result, {"ret_hello_multiplier": parse_result}

    def check_isis_l1_dr_hello_interval_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = cli_ifidx + " " + "Level" + " " + "1"
        parse_result = self.pw.get_exact_value_by_offset(output, item, 5)

        result = True if parse_result == args["interval"] else False
        return result, {"ret_dr_hello": parse_result}

    def verify_isis_logical_interface_ipv4(self, output, args, **kwargs):
        ip_found = self.pw.get_exact_value_by_offset(output, args["index"], 5)

        result = True if ip_found == args["ip"] else False
        return result, {"ret_logical_int_ipv4": ip_found}

    def check_isis_ipv4_source_address(self, output, args, **kwargs):
        ip_found = self.pw.get_exact_value_by_offset(output, "ip source-address", 3)

        result = True if ip_found == args["ip"] else False
        return result, {"ret_ipv4_src": ip_found}

    def check_isis_ipv4_tunnel_source_address(self, output, args, **kwargs):
        ip_found = self.pw.get_exact_value_by_offset(output, "tunnel source-address", 4)

        result = True if ip_found == args["ip"] else False
        return result, {"ret_ipv4_tun_src": ip_found}

    def verify_isis_redistribute_direct(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "LOC":
                    return True, True

        return False, None

    def verify_isis_redistribute_direct_enabled(self, output, args, **kwargs):
        red_dir = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "LOC":
                    red_dir = line.split()[4]
                    break

        result = True if red_dir == "TRUE" else False
        return result, {"ret_redist_direct": red_dir}

    def verify_isis_redistribute_direct_disabled(self, output, args, **kwargs):
        red_dir = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "LOC":
                    red_dir = line.split()[4]
                    break

        result = True if red_dir == "FALSE" else False
        return result, {"ret_redist_direct": red_dir}

    def verify_isis_redistribute_direct_ipv6_enabled(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        red_dir = self.pw.get_value_by_offset(output, "direct", 2)

        result = True if red_dir == "enabled" else False
        return result, {"ret_redist_ipv6_direct": red_dir}

    def verify_isis_redistribute_direct_ipv6_disabled(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        red_dir = self.pw.get_value_by_offset(output, "direct", 2)

        result = True if red_dir == "disabled" else False
        return result, {"ret_redist_ipv6_direct": red_dir}

    def check_isis_ipv6_source_address(self, output, args, **kwargs):
        ipv6_addr_found = self.pw.get_exact_value_by_offset(output, "ipv6 source-address", 3)

        result = True if ipv6_addr_found == args["ipv6_addr"] else False
        return result, {"ret_ipv6_src": ipv6_addr_found}

    def verify_isis_redistribute_direct_route_map_policy(self, output, args, **kwargs):
        rmap_pol = self.pw.get_exact_value_by_offset(output, "LOC", 6)

        result = True if rmap_pol == args["policy_name"] else False
        return result, {"ret_redist_direct_rmap": rmap_pol}

    def verify_isis_redistribute_direct_route_map_policy_clear(self, output, args, **kwargs):
        rmap_pol = self.pw.get_exact_value_by_offset(output, "LOC", 0)

        result = False if rmap_pol == args["policy_name"] else True
        return result, {"ret_redist_direct_rmap": rmap_pol}
