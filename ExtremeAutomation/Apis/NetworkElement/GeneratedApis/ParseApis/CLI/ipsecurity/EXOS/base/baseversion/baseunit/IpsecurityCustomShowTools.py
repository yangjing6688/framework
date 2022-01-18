from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.ipsecurity.base.IpsecurityBaseCustomShowTools \
    import IpsecurityBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
import ipaddress


class IpsecurityCustomShowTools(IpsecurityBaseCustomShowTools):
    def __init__(self, device):
        super(IpsecurityCustomShowTools, self).__init__(device)

    def check_trusted_port_global(self, output, args, **kwargs):
        ports_list = self.pw.get_value_by_offset(output, "trusted-ports", 2)
        port_obj = self.it.get_port_parser_obj(ports_list)
        ret_dict = {"ret_trusted_ports": ports_list}
        for port in port_obj.port_list:
            if port == args["port"]:
                return True, ret_dict
        return False, ret_dict

    def check_dhcp_snooping_vlan(self, output, args, **kwargs):
        useful_output = str.splitlines(output, False)
        final_output = ""
        iter1 = 0
        for line in useful_output:
            if iter1 > 7:
                final_output += line + "\n"
            iter1 += 1
        res = self.pw.get_value_by_offset(final_output, args["port"], 0)

        result = True if res == args["port"] else False
        return result, {"ret_dhcp_snooping_vlan": res}

    def check_dhcp_snooping_vlan_entries(self, output, args, **kwargs):
        ip = self.pw.get_value_by_offset(output, args["mac"], 0)

        result = False
        if ip != self.constants.VALUE_NOT_PRESENT:
            result = True if ipaddress.ip_address(ip) in ipaddress.ip_network(args["subnet"]) else False
        return result, result

    def check_dhcp_snooping_vlan_violations(self, output, args, **kwargs):
        result = True if args["port"] + " " in output else False
        return result, result
