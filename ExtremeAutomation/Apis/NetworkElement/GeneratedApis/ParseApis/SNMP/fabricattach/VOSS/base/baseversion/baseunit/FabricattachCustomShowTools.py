from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.fabricattach.base.\
    FabricattachBaseCustomShowTools import FabricattachBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils import NetworkElementSnmpUtils


class FabricattachCustomShowTools(FabricattachBaseCustomShowTools):
    def __init__(self, device):
        super(FabricattachCustomShowTools, self).__init__(device)

    def check_fa_service_state(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def check_fa_element_type(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "2" else False
        return result, {"ret_type": parse_result}

    def check_fa_provision_mode(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "2" else False
        return result, {"ret_mode": parse_result}

    def check_fa_assignment_timeout(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.22." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["timeout"] else False
        return result, {"ret_timeout": parse_result}

    def check_fa_discovery_timeout(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.26." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["timeout"] else False
        return result, {"ret_timeout": parse_result}

    def check_fa_port_server_status(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_status": parse_result}

    def check_fa_port_authentication_status(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_auth_status": parse_result}

    def check_fa_port_exists(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_port_exists": parse_result}

    def check_fa_mlt_exists(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_mlt_exists": parse_result}

    def check_fa_mlt_authentication_status(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_auth_status": parse_result}

    def check_fa_mlt_server_status(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_status": parse_result}

    def check_fa_management_isid_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["i_sid"] else False
        return result, {"ret_isid": parse_result}

    def check_fa_management_isid_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["i_sid"] else False
        return result, {"ret_isid": parse_result}

    def check_fa_management_isid_and_cvid_on_port(self, output, args, **kwargs):
        item1 = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.6." + args["oid_index"]
        item2 = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.7." + args["oid_index"]
        pw_svid = self.pw.get_value_by_offset(output, item1, 2)
        pw_cvid = self.pw.get_value_by_offset(output, item2, 2)

        result = True if pw_svid == args["i_sid"] and pw_cvid == args["c_vid"]else False
        return result, {"ret_isid": pw_svid,
                        "ret_cvid": pw_cvid}

    def check_fa_management_isid_and_cvid_on_mlt(self, output, args, **kwargs):
        item1 = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.6." + args["oid_index"]
        item2 = "SNMPv2-SMI::enterprises.45.5.46.1.6.1.7." + args["oid_index"]
        pw_svid = self.pw.get_value_by_offset(output, item1, 2)
        pw_cvid = self.pw.get_value_by_offset(output, item2, 2)

        result = True if pw_svid == args["i_sid"] and pw_cvid == args["c_vid"]else False
        return result, {"ret_isid": pw_svid,
                        "ret_cvid": pw_cvid}

    def check_fa_disc_element_type(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.11.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_element_type"] else False
        return result, {"ret_type": parse_result}

    def check_fa_disc_element_vlan(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.11.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["vlan"] else False
        return result, {"ret_vlan": parse_result}

    def check_fa_disc_element_system_id(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.11.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        sysid_arg = StringUtils().normalize_hex_string_to_0x_hex_expression(args["system_id"])

        result = True if parse_result == sysid_arg else False
        return result, {"ret_system_id": parse_result}

    def check_fa_disc_element_state(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.11.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        compare_result = StringUtils().hex_string_to_bit_string(parse_result)
        state_bit = NetworkElementSnmpUtils().fa_element_state(args["state"])

        result = True if compare_result[int(state_bit)] == "1" else False
        return result, {"ret_state": parse_result}

    def check_fa_disc_element_assign_auth(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.11.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_element_assign_auth"] else False
        return result, {"ret_assign_auth": parse_result}

    def check_fa_disc_element_auth(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.11.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_element_auth"] else False
        return result, {"ret_auth": parse_result}

    def check_fa_disc_element_assigned_oper_auth(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.11.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_element_assigned_oper_auth"] else False
        return result, {"ret_assign_oper_auth": parse_result}

    def check_fa_disc_element_oper_auth(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.11.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["enum_element_oper_auth"] else False
        return result, {"ret_oper_auth": parse_result}

    def check_fa_assign_isid_to_vlan(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.5.1.4." + args["oid_index"] + "." + args["isid"] + "." + args["vlan"]

        result = self.pw.is_exact_string_present_in_output(output, item)
        return result, result

    def check_fa_assign_isid_to_vlan_state(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.5.1.4." + args["oid_index"] + "." + args["isid"] + "." + args["vlan"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == NetworkElementSnmpUtils().fa_assign_state(args["state"]) else False
        return result, {"ret_state": parse_result}

    def check_fa_assign_isid_to_vlan_origin(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.5.1.6." + args["oid_index"] + "." + args["isid"] + "." + args["vlan"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == NetworkElementSnmpUtils().fa_assign_origin(args["origin"]) else False
        return result, {"ret_origin": parse_result}

    def check_fa_global_stats_disc_elem_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.1." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_elem_rx": parse_result}

    def check_fa_global_stats_asgn_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_rx": parse_result}

    def check_fa_global_stats_asgn_accepted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_accepted": parse_result}

    def check_fa_global_stats_asgn_rejected(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_rejected": parse_result}

    def check_fa_global_stats_asgn_expired(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_expired": parse_result}

    def check_fa_global_stats_disc_auth_failed(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_auth_failed": parse_result}

    def check_fa_global_stats_disc_elem_expired(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_elem_expired": parse_result}

    def check_fa_global_stats_disc_elem_deleted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_elem_deleted": parse_result}

    def check_fa_global_stats_asgn_deleted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_deleted": parse_result}

    def check_fa_global_stats_asgn_auth_failed(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.24.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_auth_failed": parse_result}

    def check_fa_port_stats_disc_elem_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_elem_rx": parse_result}

    def check_fa_port_stats_asgn_received(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_rx": parse_result}

    def check_fa_port_stats_asgn_accepted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_accepted": parse_result}

    def check_fa_port_stats_asgn_rejected(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_rejected": parse_result}

    def check_fa_port_stats_asgn_expired(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_expired": parse_result}

    def check_fa_port_stats_disc_auth_failed(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_auth_failed": parse_result}

    def check_fa_port_stats_disc_elem_expired(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_elem_expired": parse_result}

    def check_fa_port_stats_disc_elem_deleted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_disc_elem_deleted": parse_result}

    def check_fa_port_stats_asgn_deleted(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_deleted": parse_result}

    def check_fa_port_stats_asgn_auth_failed(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.23.1.11." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = NumberUtils().verify_expected_count(parse_result, args["count_operator"], args["count"])
        return result, {"ret_assign_auth_failed": parse_result}

    def check_fa_zero_touch_client_auto_attach_isid(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.29.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        return True if parse_result == args["i_sid"] else False

    def check_fa_zero_touch_client_auto_attach_vlan(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.29.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if parse_result == "4096":
            parse_result = "untagged"

        result = True if parse_result == args["vlan_or_untagged"] else False
        return result, {"ret_zero_touch_vlan": parse_result}

    def check_fa_zero_touch_client_auto_attach_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.45.5.46.1.29.1.5." + args["oid_index"]

        result = self.pw.is_exact_string_present_in_output(output, item)
        return result, result

    def check_fa_isid_port_plat_vlan(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.87.5.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["vlan"] else False
        return result, {"ret_vlan": parse_result}

    def check_fa_isid_port_cvid(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.87.5.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["cvid"] else False
        return result, {"ret_cvid": parse_result}

    def check_fa_isid_port_isid_type(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.87.5.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == NetworkElementSnmpUtils().isid_type(args["i_type"]) else False
        return result, {"ret_isid_type": parse_result}

    def check_fa_isid_port_origin(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.87.5.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == NetworkElementSnmpUtils().isid_origin(args["i_origin"]) else False
        return result, {"ret_origin": parse_result}

    def check_fa_isid_mlt_plat_vlan(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.87.5.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if parse_result == "4096":
            parse_result = "u"

        result = True if parse_result == args["vlan"] else False
        return result, {"ret_vlan": parse_result}

    def check_fa_isid_mlt_cvid(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.87.5.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["vlan"] else False
        return result, {"ret_cvid": parse_result}

    def check_fa_isid_mlt_isid_type(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.87.5.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == NetworkElementSnmpUtils().isid_type(args["i_type"]) else False
        return result, {"ret_isid_type": parse_result}

    def check_fa_isid_mlt_origin(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.87.5.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == NetworkElementSnmpUtils().isid_origin(args["i_origin"]) else False
        return result, {"ret_origin": parse_result}
