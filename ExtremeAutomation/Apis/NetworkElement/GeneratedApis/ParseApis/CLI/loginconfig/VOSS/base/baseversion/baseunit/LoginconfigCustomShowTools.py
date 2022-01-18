from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.loginconfig.base.LoginconfigBaseCustomShowTools \
    import LoginconfigBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return LoginconfigCustomShowTools(device)


class LoginconfigCustomShowTools(LoginconfigBaseCustomShowTools):
    def __init__(self, device):
        super(LoginconfigCustomShowTools, self).__init__(device)

    def check_cli_timeout(self, output, args, **kwargs):
        found_item = self.pw.get_value_by_offset(output, "timeout", 2)

        result = True if found_item == args["timeout"] else False

        return result, {"ret_timeout": found_item}

    def check_max_telnet_sessions(self, output, args, **kwargs):
        found_item = self.pw.get_value_by_offset(output, "telnet-sessions", 2)

        result = True if found_item == args["max_sessions"] else False

        return result, {"ret_telent": found_item}

    def check_max_rlogin_sessions(self, output, args, **kwargs):
        found_item = self.pw.get_value_by_offset(output, "rlogin-sessions", 2)

        result = True if found_item == args["max_sessions"] else False

        return result, {"ret_rlogin": found_item}

    def check_read_only_account(self, output, args, **kwargs):
        output = output.splitlines()
        output = [i.lstrip(" ") for i in output]
        output = [i.replace("\t", "") for i in output]

        output = "\r\n".join(["access_" + i for i in output])
        item = "access_" + "ro"
        found_state = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if found_state == "ena" else False

        return result, {"ret_state": found_state}

    def check_read_write_account(self, output, args, **kwargs):
        output = output.splitlines()
        output = [i.lstrip(" ") for i in output]
        output = [i.replace("\t", "") for i in output]

        output = "\r\n".join(["access_" + i for i in output])
        item = "access_" + "rw"
        found_state = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if found_state == "ena" else False

        return result, {"ret_state": found_state}

    def check_l1_read_write_account(self, output, args, **kwargs):
        output = output.splitlines()
        output = [i.lstrip(" ") for i in output]
        output = [i.replace("\t", "") for i in output]

        output = "\r\n".join(["access_" + i for i in output])
        item = "access_" + "l1"
        found_state = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if found_state == "ena" else False

        return result, {"ret_state": found_state}

    def check_l2_read_write_account(self, output, args, **kwargs):
        output = output.splitlines()
        output = [i.lstrip(" ") for i in output]
        output = [i.replace("\t", "") for i in output]

        output = "\r\n".join(["access_" + i for i in output])
        item = "access_" + "l2"
        found_state = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if found_state == "ena" else False

        return result, {"ret_state": found_state}

    def check_l3_read_write_account(self, output, args, **kwargs):
        output = output.splitlines()
        output = [i.lstrip(" ") for i in output]
        output = [i.replace("\t", "") for i in output]

        output = "\r\n".join(["access_" + i for i in output])
        item = "access_" + "l3"
        found_state = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if found_state == "ena" else False

        return result, {"ret_state": found_state}
