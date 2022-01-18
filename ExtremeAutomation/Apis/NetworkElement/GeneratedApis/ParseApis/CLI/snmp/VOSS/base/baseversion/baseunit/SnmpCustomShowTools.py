from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.snmp.base.SnmpBaseCustomShowTools import \
    SnmpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return SnmpCustomShowTools(device)


class SnmpCustomShowTools(SnmpBaseCustomShowTools):
    def __init__(self, device):
        super(SnmpCustomShowTools, self).__init__(device)

    def check_snmp_enable_authentication_trap(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "authenticationtrap", 2)

        result = True if "true" == parse_result else False

        return result, {"ret_auth_trap": parse_result}

    def check_snmp_enable_same_snmp_and_ip_sender_flag(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "force-iphdr-sender", 2)

        result = True if "true" == parse_result else False

        return result, {"ret_ip_sender": parse_result}

    def check_snmp_enable_same_snmp_trap_sender_ip(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "force-trap-sender", 2)

        result = True if "true" == parse_result else False

        return result, {"ret_trap_sender": parse_result}

    def check_snmp_v1_trap_server(self, output, args, **kwargs):
        addr_and_port = args["ip_addr"] + ":" + args["port"]
        target_name = self.pw.get_value_by_offset(output.lower(), addr_and_port, 0)
        ret_dict = {"ret_target_name": target_name,
                    "ret_trap_tag": None,
                    "ret_security": None}
        if target_name == "valueNotPresent":
            return False, ret_dict
        else:
            expected_version = target_name + " snmpv1"
            parse_result1 = self.pw.get_value_by_offset(output.lower(), target_name + " " + "1500", 3)
            parse_result2 = self.pw.get_value_by_offset(output, expected_version, 2)
            ret_dict["ret_trap_tag"] = parse_result1
            ret_dict["ret_security"] = parse_result2
            result = True if (self.pw.is_exact_string_present_in_output(output.lower(), expected_version) and
                              parse_result1 == "traptag" and parse_result2 == args["security_name"]) else False
            return result, ret_dict

    def check_snmp_v2c_trap_server(self, output, args, **kwargs):
        addr_and_port = args["ip_addr"] + ":" + args["port"]
        target_name = self.pw.get_value_by_offset(output.lower(), addr_and_port, 0)
        ret_dict = {"ret_target_name": target_name,
                    "ret_trap_tag": None,
                    "ret_security": None}
        if target_name == "valueNotPresent":
            return False, ret_dict
        else:
            expected_version = target_name + " snmpv2c"
            parse_result1 = self.pw.get_value_by_offset(output.lower(), target_name + " " + "1500", 3)
            parse_result2 = self.pw.get_value_by_offset(output, expected_version, 2)
            ret_dict["ret_trap_tag"] = parse_result1
            ret_dict["ret_security"] = parse_result2
            result = True if (self.pw.is_exact_string_present_in_output(output.lower(), expected_version) and
                              parse_result1 == "traptag" and parse_result2 == args["security_name"]) else False
            return result, ret_dict

    def check_snmp_v2c_inform_server(self, output, args, **kwargs):
        addr_and_port = args["ip_addr"] + ":" + args["port"]
        target_name = self.pw.get_value_by_offset(output.lower(), addr_and_port, 0)
        ret_dict = {"ret_target_name": target_name,
                    "ret_trap_tag": None,
                    "ret_security": None}
        if target_name == "valueNotPresent":
            return False, ret_dict
        else:
            expected_version = target_name + " snmpv2c"
            parse_result1 = self.pw.get_value_by_offset(output.lower(), target_name + " " + args["timeout"], 3)
            parse_result2 = self.pw.get_value_by_offset(output, expected_version, 2)
            ret_dict["ret_trap_tag"] = parse_result1
            ret_dict["ret_security"] = parse_result2
            result = True if (self.pw.is_exact_string_present_in_output(output.lower(), expected_version) and
                              parse_result1 == "informtag" and parse_result2 == args["security_name"]) else False

            return result, ret_dict

    def check_snmp_v3_trap_server(self, output, args, **kwargs):
        addr_and_port = args["ip_addr"] + ":" + args["port"]
        target_name = self.pw.get_value_by_offset(output.lower(), addr_and_port, 0)
        ret_dict = {"ret_target_name": target_name,
                    "ret_trap_tag": None,
                    "ret_security": None,
                    "ret_security_lvl": None}
        if target_name == "valueNotPresent":
            return False, ret_dict
        else:
            expected_version = target_name + " usm"
            parse_result1 = self.pw.get_value_by_offset(output.lower(), target_name + " " + "1500", 3)
            parse_result2 = self.pw.get_value_by_offset(output, expected_version, 2)
            parse_result3 = self.pw.get_value_by_offset(output.lower(), expected_version, 3)
            ret_dict["ret_trap_tag"] = parse_result1
            ret_dict["ret_security"] = parse_result2
            ret_dict["ret_security_lvl"] = parse_result3
            result = True if (self.pw.is_exact_string_present_in_output(output.lower(), expected_version) and
                              parse_result1 == "traptag" and parse_result2 == args["security_name"] and
                              parse_result3 == args["security_level"].lower()) else False

            return result, ret_dict

    def check_snmp_v3_inform_server(self, output, args, **kwargs):
        addr_and_port = args["ip_addr"] + ":" + args["port"]
        target_name = self.pw.get_value_by_offset(output.lower(), addr_and_port, 0)
        ret_dict = {"ret_target_name": target_name,
                    "ret_trap_tag": None,
                    "ret_security": None,
                    "ret_security_lvl": None}
        if target_name == "valueNotPresent":
            return False, ret_dict
        else:
            expected_version = target_name + " usm"
            parse_result1 = self.pw.get_value_by_offset(output.lower(), target_name + " " + args["timeout"], 3)
            parse_result2 = self.pw.get_value_by_offset(output, expected_version, 2)
            parse_result3 = self.pw.get_value_by_offset(output.lower(), expected_version, 3)
            ret_dict["ret_trap_tag"] = parse_result1
            ret_dict["ret_security"] = parse_result2
            ret_dict["ret_security_lvl"] = parse_result3
            result = True if (self.pw.is_exact_string_present_in_output(output.lower(), expected_version) and
                              parse_result1 == "informtag" and parse_result2 == args["security_name"] and
                              parse_result3 == args["security_level"].lower()) else False

            return result, ret_dict

    def check_snmp_community(self, output, args, **kwargs):
        result = True if self.pw.is_exact_string_present_in_output(output, args["community_index"]) else False

        return result, result

    def check_snmp_user(self, output, args, **kwargs):
        result = True if self.pw.is_exact_string_present_in_output(output, args["user_name"]) else False
        return result, result

    def check_snmp_user_engine_id(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_snmp_group(self, output, args, **kwargs):
        result = True if self.pw.is_exact_string_present_in_output(output, args["group"]) else False

        return result, result

    def check_snmp_view(self, output, args, **kwargs):
        output = output.replace(" ", "")
        item = args["view_name"] + args["oid_tree"]

        result = True if self.pw.is_exact_string_present_in_output(output, item) else False

        return result, result

    def check_snmp_notify_filter(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["profile_name"].lower(), 1)

        result = True if parse_result == args["oid_tree"] else False

        return result, {"ret_profile": parse_result}

    def check_snmp_access(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, args["group"], 2)
        parse_result = parse_result.lower()
        group_result = parse_result
        if "noauthnopriv" in parse_result:
            # Then there should be an entry for each of the 3 security models.
            parse_result = parse_result.split()
            if parse_result[0] == args["security_level"].lower():
                if parse_result[1] == args["security_level"].lower():
                    result = True if parse_result[2] == args["security_level"].lower() else False
                    return result, {"ret_group": group_result}
            return False, {"ret_group": group_result}
        else:
            result = True if parse_result == args["security_level"].lower() else False
            return result, {"ret_group": group_result}
