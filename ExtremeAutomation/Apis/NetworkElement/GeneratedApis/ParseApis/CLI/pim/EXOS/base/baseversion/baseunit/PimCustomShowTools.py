from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.pim.base.PimBaseCustomShowTools import \
    PimBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return PimCustomShowTools(device)


class PimCustomShowTools(PimBaseCustomShowTools):
    def __init__(self, device):
        super(PimCustomShowTools, self).__init__(device)

    def check_pim_state(self, output, args, **kwargs):
        pim_enabled = self.pw.get_value_by_offset(output, "PIM Enabled", 1)

        result = True if pim_enabled == "Enabled" else False
        return result, {"ret_state": pim_enabled}

    def check_pim_interface_state(self, output, args, **kwargs):
        interface = args["interface"]
        if interface.isdigit():
            interface = StringUtils.exos_vlan_string(interface)

        pim_enabled_ifaces = self.pw.get_value_by_offset(output, interface, 0).split()

        result = True if interface in pim_enabled_ifaces else False
        return result, {"ret_enabled_interfaces": pim_enabled_ifaces}

    def check_pim_bsr(self, output, args, **kwargs):
        bsr_interface_ip = self.pw.get_value_by_offset(output, "Configured BSR Info", 0)

        result = True if bsr_interface_ip == args["ip_address"] else False
        return result, {"ret_bsr_ip": bsr_interface_ip}

    def check_pim_rp(self, output, args, **kwargs):
        interface = args["interface"]
        if interface.isdigit():
            interface = StringUtils.exos_vlan_string(interface)

        rp_interface = self.pw.get_value_by_offset(output, "configure pim crp", 4).replace('"', "")
        rp_acl = self.pw.get_value_by_offset(output, "configure pim crp", 5).replace('"', "")

        result = True if interface == rp_interface and args["acl"] == rp_acl else False
        return result, {"ret_acl": rp_acl,
                        "ret_interface": rp_interface}

    def check_pim_type_sparse(self, *args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_pim_vlan_state(self, *args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_pim_expected_bsr(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        bsr_ip_found = self.pw.get_value_by_offset(output, "Current BSR Info", 4)

        result = False
        if bsr_ip_found == args["expected_bsr_ip"]:
            result = True
        return result, {"ret_bsr_ip": bsr_ip_found}

    def verify_pim_rp_set(self, output, args, **kwargs):
        result = False
        mcast_group_address_found = None
        rp_ip_found = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["mcast_group_address"]:
                    mcast_group_address_found = line.split()[0]
                    rp_ip_found = line.split()[2]
                    if mcast_group_address_found == args["mcast_group_address"] and rp_ip_found == args["ip"]:
                        result = True
                        break

        return result, {"ret_mcast_group": mcast_group_address_found,
                        "ret_rp_ip": rp_ip_found}

    def verify_pim_rp_set_group(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_pim_source_group(self, output, args, **kwargs):
        result = False
        flag_found = None
        dest_group_found = None
        source_ip = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[1] == args["dest_group"]:
                    dest_group_found = line.split()[1]
                    source_ip_found = line.split()[2]
                    flag_found = line.split()[3]
                    if flag_found == "(S)":
                        if dest_group_found == args["dest_group"] and source_ip_found == args["source_ip"]:
                            result = True
                            break

        return result, {"ret_flag": flag_found,
                        "ret_dest_group": dest_group_found,
                        "ret_source_ip": source_ip}

    def verify_pim_any_source_group(self, output, args, **kwargs):
        result = False
        flag_found = None
        dest_group_found = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[1] == args["dest_group"]:
                    dest_group_found = line.split()[1]
                    flag_found = line.split()[3]
                    if flag_found == "(WR)":
                        if dest_group_found == args["dest_group"]:
                            result = True
                            break

        return result, {"ret_flag": flag_found,
                        "ret_dest_group": dest_group_found}

    def check_pim_cache(self, output, args, **kwargs):
        result = False
        mcast_group_address_found = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[1] == args["mcast_group_address"]:
                    mcast_group_address_found = line.split()[1]
                    if mcast_group_address_found == args["mcast_group_address"]:
                        result = True
                        break

        return result, {"ret_mcast_group_address": mcast_group_address_found}
