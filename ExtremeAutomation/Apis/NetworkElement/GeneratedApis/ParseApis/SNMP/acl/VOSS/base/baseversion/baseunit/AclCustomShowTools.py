from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.acl.base.AclBaseCustomShowTools import \
    AclBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return AclCustomShowTools(device)


class AclCustomShowTools(AclBaseCustomShowTools):
    def __init__(self, device):
        super(AclCustomShowTools, self).__init__(device)

    def check_acl_exists(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.202.1.1.2.3.1.1.3." + args["acl_id"]
        result_name = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_name == str(args["acl_name"]) else False
        return result, {"ret_name": result_name}

    def check_ace_exists(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.202.1.1.2.4.1.1.3." + args["acl_id"] + "." + args["ace_index"]
        result_name = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_name == str(args["ace_name"]) else False
        return result, {"ret_name": result_name}

    def check_acl_enable(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.202.1.1.2.3.1.1.8." + args["acl_id"]
        result_state = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_state == "1" else False
        return result, {"ret_state": result_state}

    def check_acl_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.202.1.1.2.3.1.1.3." + args["acl_id"]
        result_name = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_name == str(args["acl_name"]) else False
        return result, {"ret_name": result_name}

    def check_acl_action(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.202.1.1.2.3.1.1.6." + args["acl_id"]
        result_acl_action = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_acl_action == args["action_snmp"] else False
        return result, {"ret_action": result_acl_action}

    def check_acl_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.202.1.1.2.3.1.1.10." + args["acl_id"]
        final_hex = self.pw.get_value_by_offset(output, item, 2)
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
        return result, {"ret_ports": " ".join(ports)}

    def check_acl_vlan(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.202.1.1.2.3.1.1.9." + args["acl_id"]
        get_val = self.pw.get_value_by_offset(output, item, 2)
        get_val = get_val[2:]
        hex_values = StringUtils.split_every_n(4, get_val)
        final_value = [StringUtils.hex_str_to_int(x) for x in hex_values]

        result = True if args["vlan"] in final_value else False
        return result, {"ret_vlans": str(final_value)}

    def check_ace_index_oper_state(self, output, args, **kwargs):
        result_ace_action = self.pw.get_value_by_offset(output, "=", 2)

        result = True if result_ace_action == "1" else False
        return result, {"ret_action": result_ace_action}

    def check_ace_index_name(self, output, args, **kwargs):
        result_ace_name = self.pw.get_value_by_offset(output, "=", 2)

        result = True if result_ace_name == args["ace_name"] else False
        return result, {"ret_name": result_ace_name}

    def check_ace_index_action(self, output, args, **kwargs):
        result_ace_action = self.pw.get_value_by_offset(output, "=", 2)

        result = True if result_ace_action == args["ace_action_snmp"] else False
        return result, {"ret_action": result_ace_action}

    def check_ace_index_ethernet_ethertype(self, output, args, **kwargs):
        result_ace_ethertype = self.pw.get_value_by_offset(output, "=", 2)

        result = True if result_ace_ethertype == args["ace_ethertype"] else False
        return result, {"ret_ethertype": result_ace_ethertype}
