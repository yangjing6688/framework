from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.ntp.base.NtpBaseCustomShowTools import \
    NtpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return NtpCustomShowTools(device)


class NtpCustomShowTools(NtpBaseCustomShowTools):
    def __init__(self, device):
        super(NtpCustomShowTools, self).__init__(device)

    def check_ntp_enabled(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output, "SNMPv2-SMI::enterprises.2272.1.33.1.1.0", 2)

        result = True if str(state) == "1" else False
        return result, {"ret_state": state}

    def check_ntp_server_exists(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.1." + args["server"]
        server_ip = self.pw.get_value_by_offset(output, item, 2)

        result = True if server_ip == str(args["server"]) else False
        return result, {"ret_server": server_ip}

    def check_ntp_interval(self, output, args, **kwargs):
        interval = self.pw.get_value_by_offset(output, "SNMPv2-SMI::enterprises.2272.1.33.1.2.0", 2)

        result = True if str(interval) == str(args["interval"]) else False
        return result, {"ret_interval": interval}

    def check_ntp_server_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.2." + args["server"]
        status = self.pw.get_value_by_offset(output, item, 2)

        result = True if status == "1" else False
        return result, {"ret_status": status}

    def check_ntp_server_authentication_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.3." + args["server"]
        status = self.pw.get_value_by_offset(output, item, 2)

        result = True if status == "1" else False
        return result, {"ret_auth_status": status}

    def check_ntp_server_key_index(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.4." + args["server"]
        key_id = self.pw.get_value_by_offset(output, item, 2)

        result = True if key_id == str(args["key_index"]) else False
        return result, {"ret_key_id": key_id}

    def check_ntp_server_source_ip(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.3." + args["server"]
        status = self.pw.get_value_by_offset(output, item, 2)

        result = True if status == "1" else False
        return result, {"ret_ip": status}

    def check_ntp_key_exists(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.3.1.1." + args["key_id"]
        k_id = self.pw.get_value_by_offset(output, item, 2)

        result = True if k_id == args["key_id"] else False
        return result, {"ret_key_id": k_id}

    def check_ntp_key_type(self, output, args, **kwargs):
        kt = "0"
        if args["key_type"].lower() == "md5":
            kt = "1"
        elif args["key_type"].lower() == "sha1":
            kt = "2"

        item = "SNMPv2-SMI::enterprises.2272.1.33.3.1.4." + args["key_id"]
        k_type = self.pw.get_value_by_offset(output, item, 2)

        result = True if k_type == kt else False
        return result, {"ret_key_type": k_type}

    def check_ntp_key_secret(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.3.1.2." + args["key_id"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["key_secret"] else False
        return result, {"ret_key_secret": parse_result}

    def check_ntp_server_access_attempts(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.5." + args["server"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["access_attempts"] else False
        return result, {"ret_access_attempts": parse_result}

    def check_ntp_server_access_success(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.6." + args["server"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["access_success"] else False
        return result, {"ret_access_success": parse_result}

    def check_ntp_server_access_failure(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.7." + args["server"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["access_failure"] else False
        return result, {"ret_access_failures": parse_result}

    def check_ntp_server_stratum(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.9." + args["server"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["server_stratum"] else False
        return result, {"ret_server_stratum": parse_result}

    def check_ntp_server_version(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.10." + args["server"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["server_version"] else False
        return result, {"ret_version": parse_result}

    def check_ntp_server_root_delay(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.11." + args["server"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["root_delay"] else False
        return result, {"ret_root_delay": parse_result}

    def check_ntp_server_precision(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.12." + args["server"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["server_precision"] else False
        return result, {"ret_precision": parse_result}

    def check_ntp_server_reachable(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.13." + args["server"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "reachable" else False
        return result, {"ret_reachable": parse_result}

    def check_ntp_server_synchronized(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.33.2.1.14." + args["server"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "synchronized" else False
        return result, {"ret_synchronized": parse_result}
