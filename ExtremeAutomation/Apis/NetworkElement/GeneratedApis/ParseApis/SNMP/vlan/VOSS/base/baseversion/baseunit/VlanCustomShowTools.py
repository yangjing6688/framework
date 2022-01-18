from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return VlanCustomShowTools(device)


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_exists(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.3.2.1.1." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["vlan"] else False
        return result, {"ret_vlan": parse_result}

    def check_vlan_isid(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "=", 2)

        result = True if parse_result == args["i_sid"] else False
        return result, {"ret_isid": parse_result}

    def verify_port_encapsulation_dot1q_is_set(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.3.3.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_encapsulation": parse_result}

    def check_port_is_member_of_default_vlan(self, output, args, **kwargs):
        vlan_id = "1"
        item = "SNMPv2-SMI::enterprises.2272.1.3.2.1.11." + vlan_id
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
        return result, {"ret_ports": str(found_ports)}

    def check_vlan_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.3.2.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["name"] else False
        return result, {"ret_name": parse_result}

    def check_port_is_member_of_vlan(self, output, args, **kwargs):
        vlan_id = args["vlan"]
        item = "SNMPv2-SMI::enterprises.2272.1.3.2.1.11." + vlan_id
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
        return result, {"ret_ports": found_ports}
