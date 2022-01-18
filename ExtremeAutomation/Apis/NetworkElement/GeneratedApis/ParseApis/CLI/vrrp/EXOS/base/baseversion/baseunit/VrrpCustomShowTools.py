from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vrrp.base.VrrpBaseCustomShowTools import \
    VrrpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class VrrpCustomShowTools(VrrpBaseCustomShowTools):
    def __init__(self, device):
        super(VrrpCustomShowTools, self).__init__(device)

    def check_vrrp_globally_enabled(self, output, args, **kwargs):
        vlan_found = self.pw.get_value_by_offset(output.lower(), "vlan:", 1)
        state = self.pw.get_value_by_offset(output.lower(), "vrrp:", 5)

        vlan = args["vlan"]
        if vlan.isdigit():
            vlan = StringUtils.exos_vlan_string(vlan)

        result = True if vlan_found == vlan.lower() and state == "enabled" else False
        return result, {"ret_state": state,
                        "ret_vlan": vlan_found}

    def check_vrrp_globally_disabled(self, output, args, **kwargs):
        vlan_found = self.pw.get_value_by_offset(output.lower(), "vlan:", 1)
        state = self.pw.get_value_by_offset(output.lower(), "vrrp:", 5)

        vlan = args["vlan"]
        if vlan.isdigit():
            vlan = StringUtils.exos_vlan_string(vlan)

        result = True if vlan_found == vlan.lower() and state == "disabled" else False
        return result, {"ret_state": state,
                        "ret_vlan": vlan_found}

    def check_vrrp_vlan_exists(self, output, args, **kwargs):
        vlan_found = self.pw.get_value_by_offset(output.lower(), "vlan:", 1)
        vrid_found = self.pw.get_value_by_offset(output.lower(), "vrid:", 3)

        vlan = args["vlan"]
        if vlan.isdigit():
            vlan = StringUtils.exos_vlan_string(vlan)

        result = True if vlan_found == vlan.lower() and vrid_found == args["vrid"] else False
        return result, {"ret_vlan": vlan_found,
                        "ret_vrid": vrid_found}

    def check_vrrp_group_exists(self, output, args, **kwargs):
        group_found = self.pw.get_value_by_offset(output.lower(), "group name", 3)
        result = True if group_found == args["name"].lower() else False
        return result, {"ret_group": group_found}

    def check_vrrp_vlan_fabric_routing_is_set(self, output, args, **kwargs):
        vlan_found = self.pw.get_value_by_offset(output.lower(), "vlan:", 1)
        fabric_routing_state = self.pw.get_value_by_offset(output.lower(), "fabric routing:", 2)

        vlan = args["vlan"]
        if vlan.isdigit():
            vlan = StringUtils.exos_vlan_string(vlan)
        result = True if vlan_found == vlan.lower() and fabric_routing_state == "on" else False
        return result, {"ret_fabric_routing": fabric_routing_state,
                        "ret_vlan": vlan_found}

    def check_vrrp_vlan_priority_is_set(self, output, args, **kwargs):
        vlan_found = self.pw.get_value_by_offset(output.lower(), "vlan:", 1)
        priority = self.pw.get_value_by_offset(output.lower(), "priority:", 1)

        vlan = args["vlan"]
        if vlan.isdigit():
            vlan = StringUtils.exos_vlan_string(vlan)

        result = True if vlan_found == vlan.lower() and args["priority"] in priority else False
        return result, {"ret_priority": priority,
                        "ret_vlan": vlan_found}

    def check_vrrp_vlan_ip_address_is_set(self, output, args, **kwargs):
        vlan_found = self.pw.get_value_by_offset(output.lower(), "vlan:", 1)
        ip_found = self.pw.get_value_by_offset(output.lower(), args["ip"], 0)

        vlan = args["vlan"]
        if vlan.isdigit():
            vlan = StringUtils.exos_vlan_string(vlan)

        result = True if vlan_found == vlan.lower() and ip_found == args["ip"] else False
        return result, {"ret_ip": ip_found,
                        "ret_vlan": vlan_found}

    def check_vrrp_vlan_is_enabled(self, output, args, **kwargs):
        vlan_found = self.pw.get_value_by_offset(output.lower(), "vlan:", 1)
        state = self.pw.get_value_by_offset(output.lower(), "vrrp:", 5)

        vlan = args["vlan"]
        if vlan.isdigit():
            vlan = StringUtils.exos_vlan_string(vlan)

        result = True if vlan_found == vlan.lower() and state == "enabled" else False
        return result, {"ret_state": state}

    def check_vrrp_state_is_master(self, output, args, **kwargs):
        vlan_found = self.pw.get_value_by_offset(output, "VLAN:", 1)
        state = self.pw.get_value_by_offset(output, "State:", 7)

        vlan = args["vlan"]
        if vlan.isdigit():
            vlan = StringUtils.exos_vlan_string(vlan)

        result = True if vlan_found == vlan and state == "MASTER" else False
        return result, {"ret_state": state,
                        "ret_vlan": vlan_found}

    def check_vrrp_state_is_backup(self, output, args, **kwargs):
        vlan_found = self.pw.get_value_by_offset(output, "VLAN:", 1)
        state = self.pw.get_value_by_offset(output, "State:", 7)

        vlan = args["vlan"]
        if vlan.isdigit():
            vlan = StringUtils.exos_vlan_string(vlan)
        result = True if vlan_found == vlan and state == "BACKUP" else False
        return result, {"ret_state": state,
                        "ret_vlan": vlan_found}
