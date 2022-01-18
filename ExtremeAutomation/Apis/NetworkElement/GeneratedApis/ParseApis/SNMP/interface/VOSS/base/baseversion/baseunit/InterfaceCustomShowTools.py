from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.interface.base.InterfaceBaseCustomShowTools \
    import InterfaceBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return InterfaceCustomShowTools(device)


class InterfaceCustomShowTools(InterfaceBaseCustomShowTools):
    def __init__(self, device):
        super(InterfaceCustomShowTools, self).__init__(device)

    def check_loopback_ipv4_address(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.2.1.2." + args["voss_oid_index"]
        ip_found = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if ip_found == args["ip"] else False
        return result, {"ret_ip": ip_found}

    def check_brouter_port_vlan(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.2.1.7." + args["oid_index"]
        vlan_found = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if vlan_found == args["vlan"] else False
        return result, {"ret_vlan": vlan_found}

    def check_brouter_port_ipv4(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.2.1.2." + args["oid_index"]
        ip_found = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if ip_found == args["ip"] else False
        return result, {"ret_ip": ip_found}

    def check_chassis_force_topology_ip_flag(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.4.53." + args["oid_index"]
        flag_found = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if flag_found == "1" else False
        return result, {"ret_flag": flag_found}

    def check_port_interface_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::mib-2.31.1.1.1.18." + args["oid_index"]
        name_found = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if name_found == args["name"] else False
        return result, {"ret_name": name_found}

    def check_loopback_ipv6_address(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.62.1.1.3.1.10." + args["voss_oid_index"]
        ip_found = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if ip_found == "1" else False
        return result, {"ret_ipv6": ip_found}

    def check_loopback_ipv6_address_exists(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.62.1.1.3.1.10." + args["voss_oid_index"]
        ip_found = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if ip_found == "1" else False
        return result, {"ret_ipv6": ip_found}
