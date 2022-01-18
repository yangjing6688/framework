from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.mlt.base.MltBaseCustomShowTools import \
    MltBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return MltCustomShowTools(device)


class MltCustomShowTools(MltBaseCustomShowTools):
    def __init__(self, device):
        super(MltCustomShowTools, self).__init__(device)

    def check_mlt_exists(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "mlt-" + args["mlt_id"], 0)
        parse_result = parse_result.split()[0]

        result = True if parse_result == args["mlt_id"] else False
        return result, result

    def check_mlt_running_type_split(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "mlt-" + args["mlt_id"], 5)
        try:
            parse_result = parse_result.split()[0]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == "smlt" else False
        return result, {"ret_oper_type": parse_result}

    def check_mlt_running_type_normal(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "mlt-" + args["mlt_id"], 5)
        try:
            parse_result = parse_result.split()[0]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == "norm" else False
        return result, {"ret_oper_type": parse_result}

    def check_mlt_flex_uni_status(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["mlt_id"], 7)
        try:
            parse_result = parse_result.split()[-1]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == "enable" else False
        return result, {"ret_flex_uni_status": parse_result}

    def check_mlt_admin_type_split(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "mlt-" + args["mlt_id"], 4)
        try:
            parse_result = parse_result.split()[0]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == "smlt" else False
        return result, {"ret_admin_type": parse_result}

    def check_mlt_admin_type_normal(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "mlt-" + args["mlt_id"], 4)
        try:
            parse_result = parse_result.split()[0]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == "norm" else False
        return result, {"ret_admin_type": parse_result}

    def check_mlt_lacp_actor_admin_key(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["mlt_id"], 4)
        try:
            parse_result = parse_result.split()[2]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == args["actor_admin_key"] else False
        return result, {"ret_actor_admin_key": parse_result}

    def check_mlt_lacp_actor_oper_key(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["mlt_id"], 5)
        try:
            parse_result = parse_result.split()[-1]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == args["actor_oper_key"] else False
        return result, {"ret_actor_oper_key": parse_result}

    def check_mlt_lacp_actor_system_priority(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["mlt_id"], 2)
        try:
            parse_result = parse_result.split()[2]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == args["actor_system_priority"] else False
        return result, {"ret_actor_sys_priority": parse_result}

    def check_mlt_lacp_admin_status(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["mlt_id"], 3)
        try:
            parse_result = parse_result.split()[1]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == "enable" else False
        return result, {"ret_lacp_admin_status": parse_result}

    def check_mlt_lacp_oper_status(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["mlt_id"], 4)
        try:
            parse_result = parse_result.split()[1]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == "up" else False
        return result, {"ret_lacp_oper_status": parse_result}

    def check_mlt_port(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["mlt_id"], 6)
        try:
            parse_result = parse_result.split()[0]
        except IndexError:
            parse_result = "value not present"

        result = True if args["port"] in parse_result else False
        return result, {"ret_port": parse_result}

    def check_mlt_trunking(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output.lower(), args["mlt_id"], 2)
        try:
            parse_result = parse_result.split()[-1]
        except IndexError:
            parse_result = "value not present"

        result = True if parse_result == "enable" else False
        return result, {"ret_trunking": parse_result}
