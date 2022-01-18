from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.ntp.base.NtpBaseCustomShowTools import \
    NtpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return NtpCustomShowTools(device)


class NtpCustomShowTools(NtpBaseCustomShowTools):
    def __init__(self, device):
        super(NtpCustomShowTools, self).__init__(device)

    def check_ntp_enabled(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output, "Client Mode       :", 3)

        result = False if state.lower() == "disabled" else True

        return result, {"ret_state": state}

    def check_ntp_server_exists(self, output, args, **kwargs):
        exists = str(args["server"]) in output
        result = exists
        ret_dict = {"ret_oper_key": None,
                    "ret_oper_prec": None}

        if exists and args["key"] is not None:
            oper_key = self.pw.get_value_by_offset(output, str(args["server"]), 2)
            ret_dict["ret_oper_key"] = oper_key
            result = True if oper_key == str(args["key"]) else False
        if exists and args["precedence"] is not None:
            oper_prec = self.pw.get_value_by_offset(output, str(args["server"]), 1)
            ret_dict["ret_oper_prec"] = oper_prec
            result = True if oper_prec == str(args["precedence"]) else False

        return result, ret_dict
