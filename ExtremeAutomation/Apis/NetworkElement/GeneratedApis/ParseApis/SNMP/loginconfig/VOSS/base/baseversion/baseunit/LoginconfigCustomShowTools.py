from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.loginconfig.base.\
    LoginconfigBaseCustomShowTools import LoginconfigBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return LoginconfigCustomShowTools(device)


class LoginconfigCustomShowTools(LoginconfigBaseCustomShowTools):
    def __init__(self, device):
        super(LoginconfigCustomShowTools, self).__init__(device)

    def check_cli_timeout(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.19.13." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == str(args["timeout"]) else False
        return result, {"ret_timeout": result_item}

    def check_max_telnet_sessions(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.19.11." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == str(args["max_sessions"]) else False
        return result, {"ret_max_sessions": result_item}

    def check_max_rlogin_sessions(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.19.12." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == str(args["max_sessions"]) else False
        return result, {"ret_max_sessions": result_item}

    def check_read_only_account(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.19.23." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == "1" else False
        return result, {"ret_account_type": result_item}

    def check_read_write_account(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.19.19." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == "1" else False
        return result, {"ret_account_type": result_item}

    def check_l1_read_write_account(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.19.20." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == "1" else False
        return result, {"ret_account_type": result_item}

    def check_l2_read_write_account(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.19.21." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == "1" else False
        return result, {"ret_account_type": result_item}

    def check_l3_read_write_account(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.19.22." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == "1" else False
        return result, {"ret_account_type": result_item}
