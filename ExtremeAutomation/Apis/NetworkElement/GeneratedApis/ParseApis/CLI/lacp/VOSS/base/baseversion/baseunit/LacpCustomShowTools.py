from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.lacp.base.LacpBaseCustomShowTools import \
    LacpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return LacpCustomShowTools(device)


class LacpCustomShowTools(LacpBaseCustomShowTools):
    def __init__(self, device):
        super(LacpCustomShowTools, self).__init__(device)

    def verify_lacp_enabled(self, output, args, **kwargs):
        lacp_output = self.pw.get_value_by_offset(output, "Lacp:", 1)

        result = True if lacp_output.lower() == "enable" else False
        return result, {"ret_lacp_enabled": lacp_output}

    def check_port_is_in_lag(self, output, args, **kwargs):
        port_num = args["lag_port"]

        found_port = self.pw.get_value_at_location(output, column=0, name=None, row=8)
        active = self.pw.get_value_at_location(output, column=6, name=None, row=8)

        result = True if found_port == port_num and active == "act" else False
        return result, {"ret_ports": found_port}

    def check_mlt_lacp_actor_admin_key(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["mlt_id"], 4)
        parse_result = parse_result.split()[2]

        result = True if parse_result == args["actor_admin_key"] else False
        return result, {"ret_actor_admin_key": parse_result}

    def check_mlt_lacp_actor_oper_key(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["mlt_id"], 5)
        parse_result = parse_result.split()[-1]

        result = True if parse_result == args["actor_oper_key"] else False
        return result, {"ret_actor_oper_key": parse_result}

    def check_mlt_lacp_actor_system_priority(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["mlt_id"], 2)
        parse_result = parse_result.split()[2]

        result = True if parse_result == args["actor_system_priority"] else False
        return result, {"ret_actor_sys_priority": parse_result}
