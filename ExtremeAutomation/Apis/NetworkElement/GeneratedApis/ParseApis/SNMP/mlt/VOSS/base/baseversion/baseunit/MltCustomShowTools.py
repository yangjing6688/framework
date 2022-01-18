from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.mlt.base.MltBaseCustomShowTools import \
    MltBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return MltCustomShowTools(device)


class MltCustomShowTools(MltBaseCustomShowTools):
    def __init__(self, device):
        super(MltCustomShowTools, self).__init__(device)

    def check_mlt_exists(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == args["mlt_id"] else False
        return result, {"ret_mlt_id": parse_result}

    def check_mlt_running_type_split(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "3" else False
        return result, {"ret_oper_type": parse_result}

    def check_mlt_running_type_normal(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "1" else False
        return result, {"ret_oper_type": parse_result}

    def check_mlt_flex_uni_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "1" else False
        return result, {"ret_status": parse_result}

    def check_mlt_admin_type_split(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "3" else False
        return result, {"ret_admin_type": parse_result}

    def check_mlt_admin_type_normal(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "1" else False
        return result, {"ret_admin_type": parse_result}

    def check_mlt_lacp_actor_admin_key(self, output, args, **kwargs):
        item = "SNMPv2-SMI::iso.2.840.10006.300.43.1.1.1.1.6." + args["oid_index"]
        result_name = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_name == args["actor_admin_key"] else False
        return result, {"ret_actor_admin_key": result_name}

    def check_mlt_lacp_actor_oper_key(self, output, args, **kwargs):
        item = "SNMPv2-SMI::iso.2.840.10006.300.43.1.1.1.1.7." + args["oid_index"]
        result_name = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_name == args["actor_oper_key"] else False
        return result, {"ret_actor_oper_key": result_name}

    def check_mlt_lacp_actor_system_priority(self, output, args, **kwargs):
        item = "SNMPv2-SMI::iso.2.840.10006.300.43.1.1.1.1.9." + args["oid_index"]
        result_name = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_name == args["actor_system_priority"] else False
        return result, {"ret_actor_system_priority": result_name}

    def check_mlt_lacp_admin_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "1" else False
        return result, {"ret_admin_status": parse_result}

    def check_mlt_lacp_oper_status(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "1" else False
        return result, {"ret_oper_status": parse_result}

    def check_mlt_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.17.10.1.3." + args["mlt_id"]
        final_hex = self.pw.get_value_by_offset(output, item, 2)
        if final_hex.startswith("0x"):
            final_hex = final_hex[2:]
            final_hex = list(final_hex)
            final_hex[0] = '8'
            final_hex = "".join(final_hex)
            d_bin = bin(int(final_hex, 16))[2:]
            ports = [i for i in range(len(d_bin)) if d_bin.startswith('1', i)]
            ports.pop(0)
            ports = map(str, ports)
            found_ports = "\r\n".join(ports)

            result = True if args["port_index"] in found_ports else False
            return result, {"ret_ports": str(found_ports)}
        else:
            return False, None

    def check_mlt_trunking(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == "2" else False
        return result, {"ret_trunking": parse_result}
