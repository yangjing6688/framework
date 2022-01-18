from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.radius.base.RadiusBaseCustomShowTools import \
    RadiusBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return RadiusCustomShowTools(device)


class RadiusCustomShowTools(RadiusBaseCustomShowTools):
    def __init__(self, device):
        super(RadiusCustomShowTools, self).__init__(device)

    def check_radius_state(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.1." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def check_radius_accounting_state(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def check_radius_max_servers(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == str(args["max_servers"]) else False
        return result, {"ret_max_servers": parse_result}

    def check_radius_access_priority(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == str(args["attr_value"]) else False
        return result, {"ret_access_priority": parse_result}

    def check_radius_acct_attr(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == str(args["attr_value"]) else False
        return result, {"ret_acct_attr": parse_result}

    def check_radius_include_cli_cmds(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_include_cli_cmds": parse_result}

    def check_radius_mcast_addr_attr(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == str(args["attr_value"]) else False
        return result, {"ret_mcast_addr_attr": parse_result}

    def check_radius_auth_info_attr(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == str(args["attr_value"]) else False
        return result, {"ret_auth_info_attr": parse_result}

    def check_radius_cmd_access_attr(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.11." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == str(args["attr_value"]) else False
        return result, {"ret_cmd_access_attr": parse_result}

    def check_radius_cli_cmd_attr(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.12." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == str(args["attr_value"]) else False
        return result, {"ret_cmd_attr": parse_result}

    def check_radius_cli_profile(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.14." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_profile": parse_result}

    def check_radius_src_ip_flag(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.16." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_flag": parse_result}

    def check_radius_cli_cmd_count(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.1.18." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == str(args["value"]) else False
        return result, {"ret_cmd_count": parse_result}

    def check_radius_server_host_priority(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.5.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if args["priority"] == parse_result else False
        return result, {"ret_priority": parse_result}

    def check_radius_server_host_timeout(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.5.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if args["timeout"] == parse_result else False
        return result, {"ret_timeout": parse_result}

    def check_radius_server_host_status(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.5.1.6." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if args["status_snmp"] == parse_result else False
        return result, {"ret_status": parse_result}

    def check_radius_server_host_max_retries(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.5.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if args["max_retries"] == parse_result else False
        return result, {"ret_retries": parse_result}

    def check_radius_server_host_auth_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.5.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if args["auth_port"] == parse_result else False
        return result, {"ret_auth_port": parse_result}

    def check_radius_server_host_acct_status(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.5.1.17." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if args["status_snmp"] == parse_result else False
        return result, {"ret_acct_status": parse_result}

    def check_radius_server_host_acct_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.5.1.18." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if args["acct_port"] == parse_result else False
        return result, {"ret_acct_port": parse_result}

    def check_radius_server_host_source_ip(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.29.5.1.30." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        expected_ip = StringUtils.ipaddr_to_pure_hex(args["source_ip"])
        found_ip = parse_result

        result = True if found_ip == expected_ip else False
        return result, {"ret_ip": parse_result}
