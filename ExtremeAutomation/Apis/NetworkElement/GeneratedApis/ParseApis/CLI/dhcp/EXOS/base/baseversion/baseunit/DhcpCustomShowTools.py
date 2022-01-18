from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.dhcp.base.DhcpBaseCustomShowTools import \
    DhcpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return DhcpCustomShowTools(device)


class DhcpCustomShowTools(DhcpBaseCustomShowTools):
    def __init__(self, device):
        super(DhcpCustomShowTools, self).__init__(device)

    def check_dhcp_vlan_address_range(self, output, args, **kwargs):
        output = output.replace("->", " ")

        result = False
        start_addr = self.pw.get_value_by_offset(output, 'DHCP Address Range', 4)
        end_addr = self.pw.get_value_by_offset(output, 'DHCP Address Range', 5)
        if start_addr == args["start_addr"] and end_addr == args["end_addr"]:
            result = True

        return result, {"ret_start_address": start_addr,
                        "ret_end_address": end_addr}

    def check_dhcp_vlan_netlogin_lease_timer(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, 'Netlogin Lease Timer', 4)

        result = True if res == args["seconds"] else False
        return result, {"ret_lease_timer": res}

    def check_dhcp_vlan_netlogin_lease_timer_default(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, 'Netlogin Lease Timer', 4)

        result = True if res == 'Not' else False
        return result, {"ret_lease_timer": res}

    def check_dhcp_vlan_lease_timer(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, 'DHCP Lease Timer', 4)

        result = True if res == args["seconds"] else False
        return result, {"ret_lease_timer": res}

    def check_dhcp_vlan_enabled_ports(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, 'Ports DHCP Enabled', 4)

        result = True if res == args["port"] else False
        return result, {"ret_enabled_ports": res}

    def check_dhcp_vlan_default_gateway(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, 'Default Gateway', 3)

        result = True if res == args["gateway_ip"] else False
        return result, {"ret_gateway": res}

    def check_dhcp_vlan_primary_dns(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, 'Primary DNS Server', 4)

        result = True if res == args["dns1_ip"] else False
        return result, {"ret_primary_dns": res}

    def check_dhcp_vlan_secondary_dns(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, 'Primary DNS Server', 4)

        result = True if res == args["dns2_ip"] else False
        return result, {"ret_secondary_dns": res}

    def check_dhcp_vlan_assigned_ip_address_allocation(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, args["ip_address"], 2)

        result = True if res == "Assigned" else False
        return result, {"ret_ip_allocation": res}

    def check_dhcp_vlan_assigned_mac_address_allocation(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, args["mac"], 2)

        result = True if res == "Assigned" else False
        return result, {"ret_mac_allocation": res}

    def check_bootprelay_servers(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output, " " + args["ip"] + " ", 0)

        result = True if res == "BOOTP" else False
        return result, {"ret_relay_servers": res}

    def check_bootprelay_interface_enabled(self, output, args, **kwargs):
        res = str.splitlines(output, False)
        final_line = ""
        list_num = 0
        for line in res:
            if args["vlan"] in line:
                final_line = res[list_num + 1]
            list_num += 1

        result = True if "Enabled" in final_line else False
        return result, {"ret_interface_enabled": final_line}

    def check_bootprelay_interface_disabled(self, output, args, **kwargs):
        res = str.splitlines(output, False)
        if len(res) == 4:
            return True
        final_line = ""
        list_num = 0
        for line in res:
            if args["vlan"] in line:
                final_line = res[list_num + 1]
            list_num += 1

        result = True if "Disabled" in final_line else False
        return result, {"ret_interface_disabled": final_line}
