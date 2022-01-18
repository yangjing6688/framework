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
        state = self.pw.get_value_by_offset(output, "enable", 2)

        result = True if state.lower() == "true" else False

        return result, {"ret_state": state}

    def check_ntp_server_exists(self, output, args, **kwargs):
        server_ip = self.pw.get_value_by_offset(output, str(args["server"]), 0)
        ret_dict = {"ret_oper_key": server_ip,
                    "ret_oper_prec": None}
        result = True if server_ip == str(args["server"]) else False

        return result, ret_dict

    def check_ntp_interval(self, output, args, ** kwargs):
        interval = self.pw.get_value_by_offset(output, "interval", 2)

        result = True if interval == str(args["interval"]) else False

        return result, {"ret_interval": interval}

    def check_ntp_server_enabled(self, output, args, ** kwargs):
        status = self.pw.get_value_by_offset(output, str(args["server"]), 1)

        result = True if status.lower() == "true" else False

        return result, {"ret_status": status}

    def check_ntp_server_authentication_enabled(self, output, args, ** kwargs):
        status = self.pw.get_value_by_offset(output, str(args["server"]), 2)

        result = True if status.lower() == "true" else False

        return result, {"ret_status": status}

    def check_ntp_server_key_index(self, output, args, ** kwargs):
        key_id = self.pw.get_value_by_offset(output, str(args["server"]), 3)

        result = True if key_id == str(args["key_index"]) else False

        return result, {"ret_key_id": key_id}

    def check_ntp_server_source_ip(self, output, args, **kwargs):
        sip = self.pw.get_value_by_offset(output, str(args["server"]), 4)

        result = True if sip == str(args["source_ip"]) else False

        return result, {"ret_sip": sip}

    def check_ntp_server_key_type(self, output, args, **kwargs):
        k_type = self.pw.get_value_by_offset(output, str(args["server"]), 5)

        result = True if k_type.lower() == str(args["key_type"]).lower() else False

        return result, {"ret_k_type": k_type}

    def check_ntp_key_exists(self, output, args, **kwargs):
        output = output.splitlines()
        output = "\r\n".join(["pubkey_" + i for i in output])
        item = "pubkey_" + args["key_id"]
        k_id = self.pw.get_value_by_offset(output, item, 0)

        result = True if k_id == item else False

        return result, {"ret_k_id": k_id}

    def check_ntp_key_type(self, output, args, **kwargs):
        output = output.splitlines()
        output = "\r\n".join(["pubkey_" + i for i in output])
        item = "pubkey_" + args["key_id"]
        k_type = self.pw.get_value_by_offset(output, item, 2)

        result = True if k_type.lower() == str(args["key_type"]).lower() else False

        return result, {"ret_k_type": k_type}

    def check_ntp_key_secret(self, output, args, **kwargs):
        output = output.splitlines()
        output = "\r\n".join(["pubkey_" + i for i in output])
        item = "pubkey_" + args["key_id"]
        k_secret = self.pw.get_value_by_offset(output, item, 1)

        result = True if k_secret == str(args["key_secret"]) else False

        return result, {"ret_k_secret": k_secret}

    def check_ntp_server_access_attempts(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ntp_server_access_success(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ntp_server_access_failure(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ntp_server_stratum(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ntp_server_version(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ntp_server_root_delay(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ntp_server_precision(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ntp_server_reachable(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ntp_server_synchronized(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
