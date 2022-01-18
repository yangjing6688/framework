from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.spbm.base.SpbmBaseCustomShowTools import \
    SpbmBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return SpbmCustomShowTools(device)


class SpbmCustomShowTools(SpbmBaseCustomShowTools):
    def __init__(self, device):
        super(SpbmCustomShowTools, self).__init__(device)

    def check_spbm_ethertype(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "ethertype", 2)

        result = True if parse_result == args["ethertype"] else False
        return result, {"ret_parse_result": parse_result}

    def verify_spbm_enabled(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "spbm", 2)

        result = True if parse_result == "enable" else False
        return result, {"ret_parse_result": parse_result}

    def verify_spbm_ip_enabled(self, output, args, **kwargs):
        ip_found = self.pw.get_value_at_location(output, column=5, name=None, row=10)

        result = True if ip_found == "enable" else False
        return result, {"ret_ip_found": ip_found}

    def verify_spbm_ipv6_enabled(self, output, args, **kwargs):
        ipv6_found = self.pw.get_value_at_location(output, column=6, name=None, row=10)

        result = True if ipv6_found == "enable" else False
        return result, {"ret_ipv6_found": ipv6_found}

    def verify_spbm_lsdb_trap_enabled(self, output, args, **kwargs):
        lsdb_trap_found = self.pw.get_value_at_location(output, column=4, name=None, row=10)

        result = True if lsdb_trap_found == "enable" else False
        return result, {"ret_lsdb_trap_found": lsdb_trap_found}

    def verify_isis_spbm_instance_id(self, output, args, **kwargs):
        instance_found = self.pw.get_value_at_location(output, column=0, name=None, row=10)

        result = True if instance_found == args["spbm_id"] else False
        return result, {"ret_instance_found": instance_found}

    def verify_isis_spbm_nick_name(self, output, args, **kwargs):
        nickname_found = self.pw.is_exact_string_present_in_output(output, args["nickname"])

        result = True if nickname_found == args["nickname"] else False
        return result, {"ret_nickname_found": nickname_found}

    def verify_isis_spbm_bvid(self, output, args, **kwargs):
        bvid_found = self.pw.get_value_at_location(output, column=1, name=None, row=10)

        result = True if args["bvid"] in bvid_found else False
        return result, {"ret_bvid_found": bvid_found}

    def verify_isis_spbm_multicast_enabled(self, output, args, **kwargs):
        multicast = self.pw.get_value_at_location(output, column=7, name=None, row=10)

        result = True if multicast == "enable" else False
        return result, {"ret_multicast_state": multicast}

    def verify_isis_spbm_smlt_virtual_bmac(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output, args["spbm_id"], 2)
        try:
            parse_result = parse_result.split()[1]
        except IndexError:
            pass

        result = True if parse_result == args["bmac"] else False
        return result, {"ret_parse_result": parse_result}

    def verify_isis_spbm_smlt_peer_system_id(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output, args["spbm_id"], 3)
        if len(parse_result.split()) > 1:
            parse_result = parse_result.split()[1]

        result = True if parse_result == args["peer_sys_id"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_instance_on_port(self, output, args, **kwargs):
        # Note:  Proper CLI Show command is not available. Use SNMP method to verify.
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_isis_spbm_admin_status_on_port(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "port" + args["port"], 5)

        result = True if found_status == "up" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_oper_status_on_port(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "port" + args["port"], 4)

        result = True if found_status == "up" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_adjacencies_on_port(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "port" + args["port"], 6)

        result = True if found_status == args["total_adj"] else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_up_adjacencies_on_port(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "port" + args["port"], 7)

        result = True if found_status == args["up_adj"] else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_l1_metric_on_port(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "port" + args["port"], 8)

        result = True if found_status == args["l1_metric"] else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_type_broadcast_on_port(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "port" + args["port"], 1)

        result = True if found_status == "broadcast" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_type_point_to_point_on_port(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "port" + args["port"], 1)

        result = True if found_status == "pt-pt" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_instance_on_mlt(self, output, args, **kwargs):
        # Note:  Proper CLI Show command is not available. Use SNMP method to verify.
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_isis_spbm_admin_status_on_mlt(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "mlt" + args["mlt_id"], 5)

        result = True if found_status == "up" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_oper_status_on_mlt(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "mlt" + args["mlt_id"], 4)

        result = True if found_status == "up" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_adjacencies_on_mlt(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "mlt" + args["mlt_id"], 6)

        result = True if found_status == args["total_adj"] else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_up_adjacencies_on_mlt(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "mlt" + args["mlt_id"], 7)

        result = True if found_status == args["up_adj"] else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_l1_metric_on_mlt(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "mlt" + args["mlt_id"], 8)

        result = True if found_status == args["l1_metric"] else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_type_broadcast_on_mlt(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "mlt" + args["mlt_id"], 1)

        result = True if found_status == "broadcast" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_type_point_to_point_on_mlt(self, output, args, **kwargs):
        found_status = self.pw.get_value_by_offset(output.lower(), "mlt" + args["mlt_id"], 1)

        result = True if found_status == "pt-pt" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_smlt_split_beb_primary(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["spbm_id"], 1)
        try:
            parse_result = parse_result.split()[1]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == "primary" else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_smlt_split_beb_secondary(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["spbm_id"], 1)
        if len(parse_result.split()) > 1:
            parse_result = parse_result.split()[1]

        result = True if parse_result == "secondary" else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_unicast_fib_host_name(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 3)

        result = True if parse_result == args["hostname"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_unicast_fib_cost(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 5)

        result = True if parse_result == args["cost"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_unicast_fib_outgoing_interface(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 4)

        result = True if parse_result == args["port"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_multicast_fwd_cache_timeout(self, output, args, **kwargs):
        item = "fwd-cache-timeout(seconds)"
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["timeout"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_multicast_fib_isid(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["isid"] + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 1)

        result = True if parse_result == args["isid"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_multicast_fib_type(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_isis_spbm_multicast_fib_host_name(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["isid"] + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 4)

        result = True if parse_result == args["hostname"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_multicast_fib_out_ports(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["isid"] + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 5)

        result = True if parse_result == args["port"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_multicast_fib_out_mlts(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["isid"] + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 5)

        result = True if parse_result == "MLT" + "-" + args["mlt_id"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_multicast_fib_in_ports(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["isid"] + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 6)

        result = True if parse_result == args["port"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_multicast_fib_in_mlts(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["isid"] + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 6)

        result = True if parse_result == "MLT" + "-" + args["mlt_id"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_multicast_fib_cvlan(self, output, args, **kwargs):
        out1 = StringUtils().replace_multiple_spaces_in_string(output.replace("\r\n", "&"))
        output = out1.replace("&", "\r\n")
        item = args["da"].lower() + " " + args["isid"] + " " + args["bvlan"] + " " + args["sysid"].lower()
        parse_result = self.pw.get_value_by_offset(output, item, 7)

        result = True if parse_result == args["cvlan"] else False
        return result, {"ret_parse_result": parse_result}

    def check_isis_spbm_instance_on_logical_interface(self, output, args, **kwargs):
        # Note:  Proper CLI Show command is not available. Use SNMP method to verify.
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_isis_spbm_admin_status_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        found_status = self.pw.get_exact_value_by_offset(output, cli_ifidx, 5)

        result = True if found_status == "UP" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_oper_status_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        found_status = self.pw.get_exact_value_by_offset(output, cli_ifidx, 4)

        result = True if found_status == "UP" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_adjacencies_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        found_status = self.pw.get_exact_value_by_offset(output, cli_ifidx, 6)

        result = True if found_status == args["total_adj"] else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_up_adjacencies_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        found_status = self.pw.get_exact_value_by_offset(output, cli_ifidx, 7)

        result = True if found_status == args["up_adj"] else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_l1_metric_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        found_status = self.pw.get_exact_value_by_offset(output, cli_ifidx, 8)

        result = True if found_status == args["l1_metric"] else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_type_broadcast_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["isis_id"], 0)
        found_status = self.pw.get_exact_value_by_offset(output, cli_ifidx, 1)

        result = True if found_status == "broadcast" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_type_point_to_point_on_logical_interface(self, output, args, **kwargs):
        cli_ifidx = self.pw.get_value_by_offset(output, args["spbm_id"], 0)
        found_status = self.pw.get_exact_value_by_offset(output, cli_ifidx, 1)

        result = True if found_status == "pt-pt" else False
        return result, {"ret_found_status": found_status}

    def check_isis_spbm_ip_unicast_fib_entry_exists(self, output, args, **kwargs):
        ret_ip_unicast_fib_entry = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    dest = line.split()[3]
                    nh_beb = line.split()[4]
                    bvlan = line.split()[5]
                    ret_ip_unicast_fib_entry = {"ret_dest": dest,
                                                "ret_nh_beb": nh_beb,
                                                "ret_bvlan": bvlan}

                    # THE IF statement that contains the arguments that will be used to establish a match
                    if dest == args["dest"] and nh_beb == args["nh_beb"] and bvlan == args["bvlan"]:
                        return True, ret_ip_unicast_fib_entry

        return False, ret_ip_unicast_fib_entry

    def check_isis_spbm_ip_unicast_fib_spbm_cost(self, output, args, **kwargs):
        ret_ip_unicast_fib_cost = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_spbm_cost = line.split()[7]
                    ret_ip_unicast_fib_cost = {"ret_found_dest": found_dest,
                                               "ret_found_nh_beb": found_nh_beb,
                                               "ret_found_bvlan": found_bvlan,
                                               "ret_found_spbm_cost": found_spbm_cost}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_spbm_cost == args["spbm_cost"]:
                        return True, ret_ip_unicast_fib_cost
        return False, ret_ip_unicast_fib_cost

    def check_isis_spbm_ip_unicast_fib_prefix_cost(self, output, args, **kwargs):
        ret_ip_unicast_fib_prefix_cost = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_prefix_cost = line.split()[8]
                    ret_ip_unicast_fib_prefix_cost = {"ret_found_dest": found_dest,
                                                      "ret_found_nh_beb": found_nh_beb,
                                                      "ret_found_bvlan": found_bvlan,
                                                      "ret_found_prefix_cost": found_prefix_cost}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_prefix_cost == args["prefix_cost"]:
                        return True, ret_ip_unicast_fib_prefix_cost
        return False, ret_ip_unicast_fib_prefix_cost

    def check_isis_spbm_ip_unicast_fib_prefix_type(self, output, args, **kwargs):
        ret_ip_unicast_fib_prefix_type = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_prefix_type = line.split()[9]
                    ret_ip_unicast_fib_prefix_type = {"ret_found_dest": found_dest,
                                                      "ret_found_nh_beb": found_nh_beb,
                                                      "ret_found_bvlan": found_bvlan,
                                                      "ret_found_prefix_type": found_prefix_type}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_prefix_type == args["prefix_type"]:
                        return True, ret_ip_unicast_fib_prefix_type
        return False, ret_ip_unicast_fib_prefix_type

    def check_isis_spbm_ip_unicast_fib_ip_route_preference(self, output, args, **kwargs):
        ret_ip_unicast_fib_ip_route_pref = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_ip_route_pref = line.split()[10]
                    ret_ip_unicast_fib_ip_route_pref = {"ret_found_dest": found_dest,
                                                        "ret_found_nh_beb": found_nh_beb,
                                                        "ret_found_bvlan": found_bvlan,
                                                        "ret_found_ip_route_pref": found_ip_route_pref}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_ip_route_pref == args["ip_route_pref"]:
                        return True, ret_ip_unicast_fib_ip_route_pref
        return False, ret_ip_unicast_fib_ip_route_pref

    def check_isis_spbm_ip_unicast_fib_destination_isid(self, output, args, **kwargs):
        ret_ip_unicast_fib_dest_isid = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_dest_isid = line.split()[2]
                    if found_dest_isid == "-":
                        found_dest_isid = "0"
                    ret_ip_unicast_fib_dest_isid = {"ret_found_dest": found_dest,
                                                    "ret_found_nh_beb": found_nh_beb,
                                                    "ret_found_bvlan": found_bvlan,
                                                    "ret_found_dest_isid": found_dest_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_dest_isid == args["dest_isid"]:
                        return True, ret_ip_unicast_fib_dest_isid
        return False, ret_ip_unicast_fib_dest_isid

    def check_isis_spbm_ip_unicast_fib_nh_mac(self, output, args, **kwargs):
        ret_ip_unicast_fib_nh_mac = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_bmac = line.split()[4]
                    found_bvlan = line.split()[5]
                    ret_ip_unicast_fib_nh_mac = {"ret_found_dest": found_dest,
                                                 "ret_found_nh_bmac": found_nh_bmac,
                                                 "ret_found_bvlan": found_bvlan}

                    if found_dest == args["dest"] and found_bvlan == \
                            args["bvlan"] and found_nh_bmac == args["nh_bmac"]:
                        return True, ret_ip_unicast_fib_nh_mac
        return False, ret_ip_unicast_fib_nh_mac

    def check_isis_spbm_ip_unicast_fib_out_port(self, output, args, **kwargs):
        ret_ip_unicast_fib_out_port = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_out_int = line.split()[6]
                    ret_ip_unicast_fib_out_port = {"ret_found_dest": found_dest,
                                                   "ret_found_nh_beb": found_nh_beb,
                                                   "ret_found_bvlan": found_bvlan,
                                                   "ret_found_out_int": found_out_int}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_out_int == args["port"]:
                        return True, ret_ip_unicast_fib_out_port
        return False, ret_ip_unicast_fib_out_port

    def check_isis_spbm_ip_unicast_fib_out_logical_interface(self, output, args, **kwargs):
        ret_ip_unicast_fib_out_logical_int = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_out_int = line.split()[6]
                    ret_ip_unicast_fib_out_logical_int = {"ret_found_dest": found_dest,
                                                          "ret_found_nh_beb": found_nh_beb,
                                                          "ret_found_bvlan": found_bvlan,
                                                          "ret_found_out_int": found_out_int}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_out_int == args["out_int"]:
                        return True, ret_ip_unicast_fib_out_logical_int
        return False, ret_ip_unicast_fib_out_logical_int

    def check_isis_spbm_ip_unicast_fib_vrf_isid(self, output, args, **kwargs):
        ret_ip_unicast_fib_vrf_isid = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_vrf_isid = {"ret_found_dest": found_dest,
                                                   "ret_found_nh_beb": found_nh_beb,
                                                   "ret_found_bvlan": found_bvlan,
                                                   "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_vrf_isid
        return False, ret_ip_unicast_fib_vrf_isid

    def check_isis_spbm_ip_unicast_fib_prefix_type_internal(self, output, args, **kwargs):
        ret_ip_unicast_fib_prefix_type_internal = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_prefix_type = line.split()[9]
                    ret_ip_unicast_fib_prefix_type_internal = {"ret_found_dest": found_dest,
                                                               "ret_found_nh_beb": found_nh_beb,
                                                               "ret_found_bvlan": found_bvlan,
                                                               "ret_found_prfix_type": found_prefix_type}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_prefix_type == "Internal":
                        return True, ret_ip_unicast_fib_prefix_type_internal
        return False, ret_ip_unicast_fib_prefix_type_internal

    def check_isis_spbm_ip_unicast_fib_prefix_type_external(self, output, args, **kwargs):
        ret_ip_unicast_fib_prefix_type_external = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_prefix_type = line.split()[9]
                    ret_ip_unicast_fib_prefix_type_external = {"ret_found_dest": found_dest,
                                                               "ret_found_nh_beb": found_nh_beb,
                                                               "ret_found_bvlan": found_bvlan,
                                                               "ret_found_prfix_type": found_prefix_type}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_prefix_type == "External":
                        return True, ret_ip_unicast_fib_prefix_type_external
        return False, ret_ip_unicast_fib_prefix_type_external

    def check_isis_spbm_ip_unicast_fib_dest_network(self, output, args, **kwargs):
        ret_ip_unicast_fib_dest_network = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    ret_ip_unicast_fib_dest_network = {"ret_found_dest": found_dest,
                                                       "ret_found_nh_beb": found_nh_beb,
                                                       "ret_found_bvlan": found_bvlan}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                        return True, ret_ip_unicast_fib_dest_network
        return False, ret_ip_unicast_fib_dest_network

    def check_isis_spbm_ip_unicast_fib_bvlan(self, output, args, **kwargs):
        ret_ip_unicast_fib_bvlan = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    ret_ip_unicast_fib_bvlan = {"ret_found_dest": found_dest,
                                                "ret_found_nh_beb": found_nh_beb,
                                                "ret_found_bvlan": found_bvlan}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                        return True, ret_ip_unicast_fib_bvlan
        return False, ret_ip_unicast_fib_bvlan

    def check_isis_spbm_ipv6_unicast_fib_dest_network(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_dest_network = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    ret_ipv6_unicast_fib_dest_network = {"ret_found_dest": found_dest,
                                                         "ret_found_nh_beb": found_nh_beb,
                                                         "ret_found_bvlan": found_bvlan}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                        return True, ret_ipv6_unicast_fib_dest_network
        return False, ret_ipv6_unicast_fib_dest_network

    def check_isis_spbm_ipv6_unicast_fib_out_port(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_out_port = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_out_int = line.split()[5]
                    ret_ipv6_unicast_fib_out_port = {"ret_found_dest": found_dest,
                                                     "ret_found_nh_beb": found_nh_beb,
                                                     "ret_found_bvlan": found_bvlan,
                                                     "ret_found_out_int": found_out_int}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_out_int == args["port"]:
                        return True, ret_ipv6_unicast_fib_out_port
        return False, ret_ipv6_unicast_fib_out_port

    def check_isis_spbm_ipv6_unicast_fib_spbm_cost(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_spbm_cost = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_spbm_cost = line.split()[6]
                    ret_ipv6_unicast_fib_spbm_cost = {"ret_found_dest": found_dest,
                                                      "ret_found_nh_beb": found_nh_beb,
                                                      "ret_found_bvlan": found_bvlan,
                                                      "ret_found_spbm_cost": found_spbm_cost}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_spbm_cost == args["spbm_cost"]:
                        return True, ret_ipv6_unicast_fib_spbm_cost
        return False, ret_ipv6_unicast_fib_spbm_cost

    def check_isis_spbm_ipv6_unicast_fib_prefix_cost(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_prefix_cost = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "GRT":
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_prefix_cost = line.split()[7]
                    ret_ipv6_unicast_fib_prefix_cost = {"ret_found_dest": found_dest,
                                                        "ret_found_nh_beb": found_nh_beb,
                                                        "ret_found_bvlan": found_bvlan,
                                                        "ret_found_prefix_cost": found_prefix_cost}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_prefix_cost == args["prefix_cost"]:
                        return True, ret_ipv6_unicast_fib_prefix_cost
        return False, ret_ipv6_unicast_fib_prefix_cost

    def check_isis_spbm_ip_unicast_fib_vrf_name(self, output, args, **kwargs):
        ret_ip_unicast_fib_vrf_name = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_vrf_name = line.split()[0]
                    ret_ip_unicast_fib_vrf_name = {"ret_found_dest": found_dest,
                                                   "ret_found_nh_beb": found_nh_beb,
                                                   "ret_found_bvlan": found_bvlan,
                                                   "ret_found_vrf_name": found_vrf_name}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == \
                            args["bvlan"] and found_vrf_name == args["vrf_name"]:
                        return True, ret_ip_unicast_fib_vrf_name
        return False, ret_ip_unicast_fib_vrf_name

    def check_isis_spbm_ip_unicast_fib_isid_dest_network(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_dest_network = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_dest_network = {"ret_found_dest": found_dest,
                                                            "ret_found_nh_beb": found_nh_beb,
                                                            "ret_found_bvlan": found_bvlan,
                                                            "ret_found_vrf_name": found_vrf_name,
                                                            "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_dest_network
        return False, ret_ip_unicast_fib_isid_dest_network

    def check_isis_spbm_ip_unicast_fib_isid_nh_beb(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_nh_beb = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_nh_beb = {"ret_found_dest": found_dest,
                                                      "ret_found_nh_beb": found_nh_beb,
                                                      "ret_found_bvlan": found_bvlan,
                                                      "ret_found_vrf_name": found_vrf_name,
                                                      "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_nh_beb
        return False, ret_ip_unicast_fib_isid_nh_beb

    def check_isis_spbm_ip_unicast_fib_isid_bvlan(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_bvlan = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_bvlan = {"ret_found_dest": found_dest,
                                                     "ret_found_nh_beb": found_nh_beb,
                                                     "ret_found_bvlan": found_bvlan,
                                                     "ret_found_vrf_name": found_vrf_name,
                                                     "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_bvlan
        return False, ret_ip_unicast_fib_isid_bvlan

    def check_isis_spbm_ip_unicast_fib_isid_out_int_port(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_out_int_port = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_out_int = line.split()[6]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_out_int_port = {"ret_found_dest": found_dest,
                                                            "ret_found_nh_beb": found_nh_beb,
                                                            "ret_found_bvlan": found_bvlan,
                                                            "ret_found_out_int": found_out_int,
                                                            "ret_found_vrf_name": found_vrf_name,
                                                            "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_out_int == args["out_int"] and found_vrf_name == args["vrf_name"] \
                            and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_out_int_port
        return False, ret_ip_unicast_fib_isid_out_int_port

    def check_isis_spbm_ip_unicast_fib_isid_spbm_cost(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_spbm_cost = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_spbm_cost = line.split()[7]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_spbm_cost = {"ret_found_dest": found_dest,
                                                         "ret_found_nh_beb": found_nh_beb,
                                                         "ret_found_bvlan": found_bvlan,
                                                         "ret_found_spbm_cost": found_spbm_cost,
                                                         "ret_found_vrf_name": found_vrf_name,
                                                         "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_spbm_cost == args["spbm_cost"] and found_vrf_name == args["vrf_name"] \
                            and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_spbm_cost
        return False, ret_ip_unicast_fib_isid_spbm_cost

    def check_isis_spbm_ip_unicast_fib_isid_prefix_cost(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_prefix_cost = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_prefix_cost = line.split()[8]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_prefix_cost = {"ret_found_dest": found_dest,
                                                           "ret_found_nh_beb": found_nh_beb,
                                                           "ret_found_bvlan": found_bvlan,
                                                           "ret_found_prefix_cost": found_prefix_cost,
                                                           "ret_found_vrf_name": found_vrf_name,
                                                           "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_prefix_cost == args["prefix_cost"] and found_vrf_name == args["vrf_name"] \
                            and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_prefix_cost
        return False, ret_ip_unicast_fib_isid_prefix_cost

    def check_isis_spbm_ip_unicast_fib_isid_prefix_type(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_prefix_type = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_prefix_type = line.split()[9]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_prefix_type = {"ret_found_dest": found_dest,
                                                           "ret_found_nh_beb": found_nh_beb,
                                                           "ret_found_bvlan": found_bvlan,
                                                           "ret_found_prefix_type": found_prefix_type,
                                                           "ret_found_vrf_name": found_vrf_name,
                                                           "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_prefix_type == args["prefix_type"] and found_vrf_name == args["vrf_name"] \
                            and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_prefix_type
        return False, ret_ip_unicast_fib_isid_prefix_type

    def check_isis_spbm_ip_unicast_fib_isid_ip_route_pref(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_ip_route_pref = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_ip_route_pref = line.split()[10]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_ip_route_pref = {"ret_found_dest": found_dest,
                                                             "ret_found_nh_beb": found_nh_beb,
                                                             "ret_found_bvlan": found_bvlan,
                                                             "ret_found_ip_route_pref": found_ip_route_pref,
                                                             "ret_found_vrf_name": found_vrf_name,
                                                             "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_ip_route_pref == args["ip_route_pref"] and found_vrf_name == args["vrf_name"] \
                            and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_ip_route_pref
        return False, ret_ip_unicast_fib_isid_ip_route_pref

    def check_isis_spbm_ip_unicast_fib_isid_vrf_name(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_vrf_name = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_vrf_name = {"ret_found_dest": found_dest,
                                                        "ret_found_nh_beb": found_nh_beb,
                                                        "ret_found_bvlan": found_bvlan,
                                                        "ret_found_vrf_name": found_vrf_name,
                                                        "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_vrf_name
        return False, ret_ip_unicast_fib_isid_vrf_name

    def check_isis_spbm_ip_unicast_fib_isid_vrf_isid(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_vrf_isid = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_vrf_isid = {"ret_found_dest": found_dest,
                                                        "ret_found_nh_beb": found_nh_beb,
                                                        "ret_found_bvlan": found_bvlan,
                                                        "ret_found_vrf_name": found_vrf_name,
                                                        "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_vrf_isid == args["vrf_isid"]:
                        return True, ret_ip_unicast_fib_isid_vrf_isid
        return False, ret_ip_unicast_fib_isid_vrf_isid

    def check_isis_spbm_ip_unicast_fib_isid_dest_network_isid(self, output, args, **kwargs):
        ret_ip_unicast_fib_isid_dest_network_isid = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[3]
                    found_nh_beb = line.split()[4]
                    found_bvlan = line.split()[5]
                    found_dest_isid = line.split()[2]
                    if found_dest_isid == "-":
                        found_dest_isid = "0"
                    found_vrf_name = line.split()[0]
                    found_vrf_isid = line.split()[1]
                    if found_vrf_isid == "-":
                        found_vrf_isid = "0"
                    ret_ip_unicast_fib_isid_dest_network_isid = {"ret_found_dest": found_dest,
                                                                 "ret_found_nh_beb": found_nh_beb,
                                                                 "ret_found_bvlan": found_bvlan,
                                                                 "ret_found_dest_isid": found_dest_isid,
                                                                 "ret_found_vrf_name": found_vrf_name,
                                                                 "ret_found_vrf_isid": found_vrf_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                        and found_dest_isid == args["dest_isid"] \
                            and found_vrf_name == args["vrf_name"] and found_vrf_isid == args["isid"]:
                        return True, ret_ip_unicast_fib_isid_dest_network_isid
        return False, ret_ip_unicast_fib_isid_dest_network_isid

    def check_isis_spbm_ipv6_unicast_fib_isid_dest_network(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_isid_dest_network = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_vrf_name = line.split()[0]
                    found_isid = line.split()[1]
                    if found_isid == "-":
                        found_isid = "0"
                    ret_ipv6_unicast_fib_isid_dest_network = {"ret_found_dest": found_dest,
                                                              "ret_found_nh_beb": found_nh_beb,
                                                              "ret_found_bvlan": found_bvlan,
                                                              "ret_found_vrf_name": found_vrf_name,
                                                              "ret_found_isid": found_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_isid == args["isid"]:
                        return True, ret_ipv6_unicast_fib_isid_dest_network
        return False, ret_ipv6_unicast_fib_isid_dest_network

    def check_isis_spbm_ipv6_unicast_fib_isid_nh_beb(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_isid_nh_beb = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_vrf_name = line.split()[0]
                    found_isid = line.split()[1]
                    if found_isid == "-":
                        found_isid = "0"
                    ret_ipv6_unicast_fib_isid_nh_beb = {"ret_found_dest": found_dest,
                                                        "ret_found_nh_beb": found_nh_beb,
                                                        "ret_found_bvlan": found_bvlan,
                                                        "ret_found_vrf_name": found_vrf_name,
                                                        "ret_found_isid": found_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_isid == args["isid"]:
                        return True, ret_ipv6_unicast_fib_isid_nh_beb
        return False, ret_ipv6_unicast_fib_isid_nh_beb

    def check_isis_spbm_ipv6_unicast_fib_isid_bvlan(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_isid_bvlan = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_vrf_name = line.split()[0]
                    found_isid = line.split()[1]
                    if found_isid == "-":
                        found_isid = "0"
                    ret_ipv6_unicast_fib_isid_bvlan = {"ret_found_dest": found_dest,
                                                       "ret_found_nh_beb": found_nh_beb,
                                                       "ret_found_bvlan": found_bvlan,
                                                       "ret_found_vrf_name": found_vrf_name,
                                                       "ret_found_isid": found_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_isid == args["isid"]:
                        return True, ret_ipv6_unicast_fib_isid_bvlan
        return False, ret_ipv6_unicast_fib_isid_bvlan

    def check_isis_spbm_ipv6_unicast_fib_isid_out_int_port(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_isid_out_int_port = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_out_int = line.split()[5]
                    found_vrf_name = line.split()[0]
                    found_isid = line.split()[1]
                    if found_isid == "-":
                        found_isid = "0"
                    ret_ipv6_unicast_fib_isid_out_int_port = {"ret_found_dest": found_dest,
                                                              "ret_found_nh_beb": found_nh_beb,
                                                              "ret_found_bvlan": found_bvlan,
                                                              "ret_found_out_int": found_out_int,
                                                              "ret_found_vrf_name": found_vrf_name,
                                                              "ret_found_isid": found_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_out_int == args["out_int"] and found_vrf_name == args["vrf_name"] \
                            and found_isid == args["isid"]:
                        return True, ret_ipv6_unicast_fib_isid_out_int_port
        return False, ret_ipv6_unicast_fib_isid_out_int_port

    def check_isis_spbm_ipv6_unicast_fib_isid_spbm_cost(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_isid_spbm_cost = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_spbm_cost = line.split()[6]
                    found_vrf_name = line.split()[0]
                    found_isid = line.split()[1]
                    if found_isid == "-":
                        found_isid = "0"
                    ret_ipv6_unicast_fib_isid_spbm_cost = {"ret_found_dest": found_dest,
                                                           "ret_found_nh_beb": found_nh_beb,
                                                           "ret_found_bvlan": found_bvlan,
                                                           "ret_found_spbm_cost": found_spbm_cost,
                                                           "ret_found_vrf_name": found_vrf_name,
                                                           "ret_found_isid": found_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_spbm_cost == args["spbm_cost"] and found_vrf_name == args["vrf_name"] \
                            and found_isid == args["isid"]:
                        return True, ret_ipv6_unicast_fib_isid_spbm_cost
        return False, ret_ipv6_unicast_fib_isid_spbm_cost

    def check_isis_spbm_ipv6_unicast_fib_isid_prefix_cost(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_isid_prefix_cost = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_prefix_cost = line.split()[7]
                    found_vrf_name = line.split()[0]
                    found_isid = line.split()[1]
                    if found_isid == "-":
                        found_isid = "0"
                    ret_ipv6_unicast_fib_isid_prefix_cost = {"ret_found_dest": found_dest,
                                                             "ret_found_nh_beb": found_nh_beb,
                                                             "ret_found_bvlan": found_bvlan,
                                                             "ret_found_prefix_cost": found_prefix_cost,
                                                             "ret_found_vrf_name": found_vrf_name,
                                                             "ret_found_isid": found_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_prefix_cost == args["prefix_cost"] and found_vrf_name == args["vrf_name"] \
                            and found_isid == args["isid"]:
                        return True, ret_ipv6_unicast_fib_isid_prefix_cost
        return False, ret_ipv6_unicast_fib_isid_prefix_cost

    def check_isis_spbm_ipv6_unicast_fib_isid_vrf_name(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_isid_vrf_name = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_vrf_name = line.split()[0]
                    found_isid = line.split()[1]
                    if found_isid == "-":
                        found_isid = "0"
                    ret_ipv6_unicast_fib_isid_vrf_name = {"ret_found_dest": found_dest,
                                                          "ret_found_nh_beb": found_nh_beb,
                                                          "ret_found_bvlan": found_bvlan,
                                                          "ret_found_vrf_name": found_vrf_name,
                                                          "ret_found_isid": found_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_isid == args["isid"]:
                        return True, ret_ipv6_unicast_fib_isid_vrf_name
        return False, ret_ipv6_unicast_fib_isid_vrf_name

    def check_isis_spbm_ipv6_unicast_fib_isid(self, output, args, **kwargs):
        ret_ipv6_unicast_fib_isid = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["vrf_name"]:
                    found_dest = line.split()[2]
                    found_nh_beb = line.split()[3]
                    found_bvlan = line.split()[4]
                    found_vrf_name = line.split()[0]
                    found_isid = line.split()[1]
                    if found_isid == "-":
                        found_isid = "0"
                    ret_ipv6_unicast_fib_isid = {"ret_found_dest": found_dest,
                                                 "ret_found_nh_beb": found_nh_beb,
                                                 "ret_found_bvlan": found_bvlan,
                                                 "ret_found_vrf_name": found_vrf_name,
                                                 "ret_found_isid": found_isid}

                    if found_dest == args["dest"] and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                            and found_vrf_name == args["vrf_name"] and found_isid == args["isid"]:
                        return True, ret_ipv6_unicast_fib_isid
        return False, ret_ipv6_unicast_fib_isid

    def verify_virtual_ist_peer_ip(self, output, args, **kwargs):
        ret_virtual_ist_peer_ip = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["ip"]:
                    found_ip = line.split()[0]
                    found_vlan = line.split()[1]
                    ret_virtual_ist_peer_ip = {"ret_found_ip": found_ip,
                                               "ret_found_vlan": found_vlan}

                    if found_ip == args["ip"] and found_vlan == args["vlan"]:
                        return True, ret_virtual_ist_peer_ip

        return False, ret_virtual_ist_peer_ip
