from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.radius.base.RadiusBaseCustomShowTools import \
    RadiusBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class RadiusCustomShowTools(RadiusBaseCustomShowTools):
    def __init__(self, device):
        super(RadiusCustomShowTools, self).__init__(device)

    def check_radius_state(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, " enable", 2)

        result = True if "true" == parse_result else False
        return result, {"ret_state": parse_result}

    def check_radius_accounting_state(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "acct-enable", 2)

        result = True if "true" == parse_result else False
        return result, {"ret_state": parse_result}

    def check_radius_max_servers(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "maxserver", 2)

        result = True if args["max_servers"] == parse_result else False
        return result, {"ret_max_servers": parse_result}

    def check_radius_access_priority(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "access-priority-attribute", 2)

        result = True if args["attr_value"] == parse_result else False
        return result, {"ret_access_priority": parse_result}

    def check_radius_acct_attr(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "acct-attribute-value", 2)

        result = True if args["attr_value"] == parse_result else False
        return result, {"ret_acct_attr": parse_result}

    def check_radius_include_cli_cmds(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "acct-include-cli-commands", 2)

        result = True if "true" == parse_result else False
        return result, {"ret_include_cli": parse_result}

    def check_radius_mcast_addr_attr(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "mcast-addr-attr-value", 2)

        result = True if args["attr_value"] == parse_result else False
        return result, {"ret_mcast_addr_attr": parse_result}

    def check_radius_auth_info_attr(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "auth-info-attr-value", 2)

        result = True if args["attr_value"] == parse_result else False
        return result, {"ret_auth_info_attr": parse_result}

    def check_radius_cmd_access_attr(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "command-access-attribute", 2)

        result = True if args["attr_value"] == parse_result else False
        return result, {"ret_cmd_access_attr": parse_result}

    def check_radius_cli_cmd_attr(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "cli-commands-attribute", 2)

        result = True if args["attr_value"] == parse_result else False
        return result, {"ret_cli_cmd_attr": parse_result}

    def check_radius_cli_profile(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "cli-profile-enable", 2)

        result = True if "true" == parse_result else False
        return result, {"ret_cli_profile": parse_result}

    def check_radius_src_ip_flag(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "sourceip-flag", 2)

        result = True if "true" == parse_result else False
        return result, {"ret_src_ip_flag": parse_result}

    def check_radius_cli_cmd_count(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "cli-cmd-count", 2)

        result = True if args["value"] == parse_result else False
        return result, {"ret_cli_cmd_count": parse_result}

    def check_radius_server_host_priority(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, args["addr"], 4)

        result = True if args["priority"] == parse_result else False
        return result, {"ret_priority": parse_result}

    def check_radius_server_host_timeout(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, args["addr"], 6)

        result = True if args["timeout"] == parse_result else False
        return result, {"ret_timeout": parse_result}

    def check_radius_server_host_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, args["addr"], 7)

        result = True if args["status"] == parse_result else False
        return result, {"ret_status": parse_result}

    def check_radius_server_host_max_retries(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, args["addr"], 5)

        result = True if args["max_retries"] == parse_result else False
        return result, {"ret_retries": parse_result}

    def check_radius_server_host_auth_port(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, args["addr"], 3)

        result = True if args["auth_port"] == parse_result else False
        return result, {"ret_auth_port": parse_result}

    def check_radius_server_host_acct_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, args["addr"], 9)

        result = True if args["status"] == parse_result else False
        return result, {"ret_accounting_state": parse_result}

    def check_radius_server_host_acct_port(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, args["addr"], 8)

        result = True if args["acct_port"] == parse_result else False
        return result, {"ret_acct_port": parse_result}

    def check_radius_server_host_source_ip(self, output, args, **kwargs):
        expected_ip = StringUtils.ipaddr_to_pure_hex(args["source_ip"])
        parse_result = self.pw.get_value_by_offset(output, args["addr"], 10)
        found_ip = StringUtils.ipaddr_to_pure_hex(parse_result)

        result = True if found_ip == expected_ip else False
        return result, {"ret_ip": found_ip}
