from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.fabricattach.base.\
    FabricattachBaseCustomShowTools import FabricattachBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class FabricattachCustomShowTools(FabricattachBaseCustomShowTools):
    def __init__(self, device):
        super(FabricattachCustomShowTools, self).__init__(device)

    def check_fa_service_state(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "service", 3)

        result = True if parse_result == "enabled" else False
        return result, {"ret_service_state": parse_result}

    def check_fa_element_type(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "type", 4)

        result = True if parse_result == "server" else False
        return result, {"ret_element_type": parse_result}

    def check_fa_provision_mode(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "provision", 4)

        result = True if parse_result == "spbm" else False
        return result, {"ret_provision_mode": parse_result}

    def check_fa_assignment_timeout(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "assignment", 4)

        result = True if parse_result == args["timeout"] else False
        return result, {"ret_assignment_timeout": parse_result}

    def check_fa_discovery_timeout(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "discovery", 4)

        result = True if parse_result == args["timeout"] else False
        return result, {"ret_discovery_timeout": parse_result}

    def check_fa_port_server_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 1)

        result = True if parse_result == "enabled" else False
        return result, {"ret_server_status": parse_result}

    def check_fa_port_authentication_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 4)

        result = True if parse_result == "enabled" else False
        return result, {"ret_port_auth_status": parse_result}

    def check_fa_port_exists(self, output, args, **kwargs):
        result = args["port"] in output
        return result, result

    def check_fa_mlt_exists(self, output, args, **kwargs):
        result = "mlt" + args["mlt_id"] in output
        return result, result

    def check_fa_mlt_authentication_status(self, output, args, **kwargs):
        item = "mlt" + args["mlt_id"]
        parse_result = self.pw.get_value_by_offset(output.lower(), item, 4)

        result = True if parse_result == "enabled" else False
        return result, {"ret_mlt_auth_status": parse_result}

    def check_fa_mlt_server_status(self, output, args, **kwargs):
        item = "mlt" + args["mlt_id"]
        parse_result = self.pw.get_value_by_offset(output.lower(), item, 1)

        result = True if parse_result == "enabled" else False
        return result, {"ret_mlt_server_status": parse_result}

    def check_fa_management_isid_on_port(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["port"], 2)

        result = True if parse_result == args["i_sid"] else False
        return result, {"ret_isid_on_port": parse_result}

    def check_fa_management_isid_on_mlt(self, output, args, **kwargs):
        item = "mlt" + args["mlt_id"]
        parse_result = self.pw.get_value_by_offset(output.lower(), item, 2)

        result = True if parse_result == args["i_sid"] else False
        return result, {"ret_isid_on_mlt": parse_result}

    def check_fa_management_isid_and_cvid_on_port(self, output, args, **kwargs):
        pr_svid = self.pw.get_value_by_offset(output.lower(), args["port"], 2)
        pr_cvid = self.pw.get_value_by_offset(output.lower(), args["port"], 3)

        result = True if pr_svid == args["i_sid"] and pr_cvid == args["c_vid"] else False
        return result, {"ret_port_isid": pr_svid,
                        "ret_port_cvid": pr_cvid}

    def check_fa_management_isid_and_cvid_on_mlt(self, output, args, **kwargs):
        item = "mlt" + args["mlt_id"]
        pr_svid = self.pw.get_value_by_offset(output.lower(), item, 2)
        pr_cvid = self.pw.get_value_by_offset(output.lower(), item, 3)

        result = True if pr_svid == args["i_sid"] and pr_cvid == args["c_vid"] else False
        return result, {"ret_mlt_isid": pr_svid,
                        "ret_mlt_cvid": pr_cvid}

    def check_fa_disc_element_type(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["port"], 1)
        parse_result = parse_result.split()[0]

        result = True if parse_result == args["element_type"].lower() else False
        return result, {"ret_disc_element_type": parse_result}

    def check_fa_disc_element_vlan(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["port"], 2)
        parse_result = parse_result.split()[0]

        result = True if parse_result == args["vlan"] else False
        return result, {"ret_disc_element_vlan": parse_result}

    def check_fa_disc_element_system_id(self, output, args, **kwargs):
        result = self.pw.is_exact_string_present_in_output(output, args["system_id"])
        return result, "Value not parsed."

    def check_fa_disc_element_state(self, output, args, **kwargs):

        parse_result = self.pw.get_value_from_string_to_eol(output.lower(), args["port"])
        pr = parse_result.split('\r\n')[0]
        g = pr.split()
        parse_result = ' '.join(g)

        result = True if self.pw.is_exact_string_present_in_output(parse_result, args["state"].lower()) else False
        return result, {"ret_disc_element_state": parse_result}

    def check_fa_disc_element_assign_auth(self, output, args, **kwargs):

        parse_result = self.pw.get_value_from_string_to_eol(output.lower(), args["port"])
        pr = parse_result.split('\r\n')[0]
        parse_result = pr.split()[-1]

        result = True if parse_result == args["element_assign_auth"].lower() else False
        return result, {"ret_disc_element_assign_auth": parse_result}

    def check_fa_disc_element_auth(self, output, args, **kwargs):

        parse_result = self.pw.get_value_from_string_to_eol(output.lower(), args["port"])
        pr = parse_result.split('\r\n')[0]
        try:
            parse_result = pr.split()[-2]
        except IndexError:
            parse_result = pr

        result = True if parse_result == args["element_auth"].lower() else False
        return result, {"ret_disc_element_auth": parse_result}

    def check_fa_disc_element_assigned_oper_auth(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["port"], 2)
        if len(parse_result.split()) > 1:
            parse_result = parse_result.split()[1]

        result = True if parse_result == args["element_assigned_oper_auth"].lower() else False
        return result, {"ret_disc_element_assign_oper_auth": parse_result}

    def check_fa_disc_element_oper_auth(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["port"], 1)
        try:
            parse_result = parse_result.split()[1]
        except IndexError:
            pass

        result = True if parse_result == args["element_oper_auth"].lower() else False
        return result, {"ret_disc_element_oper_euth": parse_result}

    def check_fa_assign_isid_to_vlan(self, output, args, **kwargs):
        ret_dict = {"ret_isid": None,
                    "ret_vlan": None}
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["port"]:
                    ret_dict["ret_isid"] = line.split()[1]
                    ret_dict["ret_vlan"] = line.split()[2]

                    if ret_dict["ret_isid"] == args["isid"] and ret_dict["ret_vlan"] == args["vlan"]:
                        return True, ret_dict
        return False, ret_dict

    def check_fa_assign_isid_to_vlan_state(self, output, args, **kwargs):
        ret_dict = {"ret_isid": None,
                    "ret_vlan": None,
                    "ret_state": None}
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["port"]:
                    ret_dict["ret_isid"] = line.split()[1]
                    ret_dict["ret_vlan"] = line.split()[2]
                    ret_dict["ret_state"] = line.split()[3]

                    if ret_dict["ret_isid"] == args["isid"] and \
                            ret_dict["ret_vlan"] == args["vlan"] and \
                            ret_dict["ret_state"] == args["state"]:
                        return True, ret_dict
        return False, ret_dict

    def check_fa_assign_isid_to_vlan_origin(self, output, args, **kwargs):
        ret_dict = {"ret_isid": None,
                    "ret_vlan": None,
                    "ret_origin": None}
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["port"]:
                    ret_dict["ret_isid"] = line.split()[1]
                    ret_dict["ret_vlan"] = line.split()[2]
                    ret_dict["ret_origin"] = line.split()[4]

                    if ret_dict["ret_isid"] == args["isid"] and \
                            ret_dict["ret_vlan"] == args["vlan"] and \
                            ret_dict["ret_origin"] == args["origin"]:
                        return True, ret_dict
        return False, ret_dict

    def check_fa_global_stats_disc_elem_received(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=0, name=None, row=10)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_element_received": parse_result}

    def check_fa_global_stats_asgn_received(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=0, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_received": parse_result}

    def check_fa_global_stats_asgn_accepted(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=1, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_accepted": parse_result}

    def check_fa_global_stats_asgn_rejected(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=2, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_rejected": parse_result}

    def check_fa_global_stats_asgn_expired(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=3, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_expired": parse_result}

    def check_fa_global_stats_disc_auth_failed(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=3, name=None, row=10)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_auth_failed": parse_result}

    def check_fa_global_stats_disc_elem_expired(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=1, name=None, row=10)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_element_expired": parse_result}

    def check_fa_global_stats_disc_elem_deleted(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=2, name=None, row=10)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_element_deleted": parse_result}

    def check_fa_global_stats_asgn_deleted(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=4, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_deleted": parse_result}

    def check_fa_global_stats_asgn_auth_failed(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=5, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_auth_failed": parse_result}

    def check_fa_port_stats_disc_elem_received(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=1, name=None, row=10)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_element_received": parse_result}

    def check_fa_port_stats_asgn_received(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=1, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_received": parse_result}

    def check_fa_port_stats_asgn_accepted(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=2, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_accepted": parse_result}

    def check_fa_port_stats_asgn_rejected(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=3, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_rejected": parse_result}

    def check_fa_port_stats_asgn_expired(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=4, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_expired": parse_result}

    def check_fa_port_stats_disc_auth_failed(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=4, name=None, row=10)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_auth_failed": parse_result}

    def check_fa_port_stats_disc_elem_expired(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=2, name=None, row=10)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_element_expired": parse_result}

    def check_fa_port_stats_disc_elem_deleted(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=3, name=None, row=10)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_element_expired": parse_result}

    def check_fa_port_stats_asgn_deleted(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=5, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_deleted": parse_result}

    def check_fa_port_stats_asgn_auth_failed(self, output, args, **kwargs):
        parse_result = self.pw.get_value_at_location(output, column=6, name=None, row=19)

        result = NumberUtils.verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_auth_failed": parse_result}

    def check_fa_zero_touch_client_auto_attach_isid(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["name"], 2)

        result = True if parse_result == args["i_sid"] else False
        return result, {"ret_auto_attach_isid": parse_result}

    def check_fa_zero_touch_client_auto_attach_vlan(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["name"], 3)

        result = True if parse_result == args["vlan_or_untagged"].lower() else False
        return result, {"ret_auth_attach_vlan": parse_result}

    def check_fa_zero_touch_client_auto_attach_name(self, output, args, **kwargs):
        result = self.pw.is_exact_string_present_in_output(output, args["name"])
        return result, "Value not parsed."

    def check_fa_isid_port_plat_vlan(self, output, args, **kwargs):
        port_parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 3)
        if len(port_parse_result.replace("c", "").split(":")) > 1:
            found_port = port_parse_result.replace("c", "").split(":")[1]
        else:
            found_port = port_parse_result
        parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 2)

        result = True if parse_result == args["vlan"] and found_port == args["port"] else False
        return result, {"ret_isid_port": found_port,
                        "ret_isid_vlan": parse_result}

    def check_fa_isid_port_cvid(self, output, args, **kwargs):
        port_parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 3)
        g = port_parse_result.replace("c", "")
        try:
            found_cvid = g.split(":")[0]
            found_port = g.split(":")[1]
        except IndexError:
            found_cvid = g
            found_port = g

        result = True if found_cvid == args["cvid"] and found_port == args["port"] else False
        return result, {"ret_isid_port": found_port,
                        "ret_isid_cvid": found_cvid}

    def check_fa_isid_port_isid_type(self, output, args, **kwargs):
        port_parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 3)
        if len(port_parse_result.replace("c", "").split(":")) > 1:
            found_port = port_parse_result.replace("c", "").split(":")[1]
        else:
            found_port = port_parse_result
        parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 1)

        result = True if parse_result == args["i_type"] and found_port == args["port"] else False
        return result, {"ret_isid_type": parse_result,
                        "ret_isid_port": found_port}

    def check_fa_isid_port_origin(self, output, args, **kwargs):
        found_port = self.pw.get_exact_value_by_offset(output, args["isid"], 3)
        parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 5)
        try:
            found_port = found_port.replace("c", "").split(":")[1]
        except IndexError:
            pass

        result = True if parse_result == args["i_origin"] and found_port == args["port"] else False
        return result, {"ret_isid_origin": parse_result,
                        "ret_isid_port": found_port}

    def check_fa_isid_mlt_plat_vlan(self, output, args, **kwargs):
        mlt_parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 4)
        if len(mlt_parse_result.replace("c", "").split(":")) > 1:
            found_mlt = mlt_parse_result.replace("c", "").split(":")[1]
        else:
            found_mlt = mlt_parse_result
        parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 2)

        result = True if parse_result == args["vlan"] and found_mlt == args["mlt_id"]else False
        return result, {"ret_isid_vlan": parse_result,
                        "ret_isid_mlt": found_mlt}

    def check_fa_isid_mlt_cvid(self, output, args, **kwargs):
        mlt_parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 4)
        g = mlt_parse_result.replace("c", "")
        try:
            found_cvid = g.split(":")[0]
            found_mlt = g.split(":")[1]
        except IndexError:
            found_cvid = g
            found_mlt = g

        result = True if found_cvid == args["cvid"] and found_mlt == args["mlt_id"]else False
        return result, {"ret_isid_cvid": found_cvid,
                        "ret_isid_mlt": found_mlt}

    def check_fa_isid_mlt_isid_type(self, output, args, **kwargs):
        mlt_parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 4)
        if len(mlt_parse_result.replace("c", "").split(":")) > 1:
            found_mlt = mlt_parse_result.replace("c", "").split(":")[1]
        else:
            found_mlt = mlt_parse_result
        parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 1)

        result = True if parse_result == args["i_type"] and found_mlt == args["mlt_id"]else False
        return result, {"ret_isid_type": parse_result,
                        "ret_isid_mlt": found_mlt}

    def check_fa_isid_mlt_origin(self, output, args, **kwargs):
        mlt_parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 4)
        try:
            found_mlt = mlt_parse_result.replace("c", "").split(":")[1]
        except IndexError:
            found_mlt = mlt_parse_result
        parse_result = self.pw.get_exact_value_by_offset(output, args["isid"], 5)

        result = True if parse_result == args["i_origin"] and found_mlt == args["mlt_id"] else False
        return result, {"ret_isid_origin": parse_result,
                        "ret_isid_mlt": found_mlt}

    def check_fa_agent_timeout(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "assignment", 4)

        result = True if parse_result == args["timeout"] else False
        return result, {"ret_agent_timeout": parse_result}
