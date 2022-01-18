from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.igmp.base.IgmpBaseCustomShowTools import \
    IgmpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return IgmpCustomShowTools(device)


class IgmpCustomShowTools(IgmpBaseCustomShowTools):
    def __init__(self, device):
        IgmpBaseCustomShowTools.__init__(self, device)

    def check_igmp_state(self, output, args, **kwargs):
        vlan = StringUtils.exos_vlan_string(args["vlan"]) if args["vlan"].isdigit() else args["vlan"]

        igmp_enabled_vlans = self.pw.get_value_by_offset(output, vlan, 0).split()

        result = True if vlan in igmp_enabled_vlans else False

        return result, {"ret_igmp_vlans": igmp_enabled_vlans}

    def check_igmp_version(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        igmp_version = self.pw.get_value_by_offset(output, args["vlan_name"], 6)

        result = True if args["igmp_ver"] == igmp_version else False

        return result, {"ret_igmp_version": igmp_version}

    def check_igmp_vlan_state(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        vlan_found = self.pw.get_value_by_offset(output, "Interface on VLAN", 3)
        igmp_vlan_state = self.pw.get_value_by_offset(output, "IPmc", 7)

        result = True if vlan_found == args["vlan"] and igmp_vlan_state == args["igmp_vlan_state"] else False

        return result, {"ret_vlan_found": vlan_found, "ret_igmp_vlan_state": igmp_vlan_state}

    def check_igmp_snooping_vlan_state(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        vlan_found = self.pw.get_value_by_offset(output, "Interface on VLAN", 3)
        igmp_snooping_vlan_state = self.pw.get_value_by_offset(output, "Snooping", 4)

        result = True if vlan_found == args["vlan_name"] and igmp_snooping_vlan_state == "YES" else False

        return result, {"ret_vlan_found": vlan_found, "ret_igmp_snooping_vlan_state": igmp_snooping_vlan_state}

    def check_igmp_snooping_proxy_state(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        vlan_found = self.pw.get_value_by_offset(output, "Interface on VLAN", 3)
        snooping_proxy_state = self.pw.get_value_by_offset(output, "Snooping", 7)

        result = True if vlan_found == args["vlan_name"] and snooping_proxy_state == "YES" else False

        return result, {"ret_vlan_found": vlan_found, "ret_snooping_proxy_state": snooping_proxy_state}

    def verify_igmp_group(self, output, args, **kwargs):
        match = "no"
        ret_dict = {"ret_vlan": None,
                    "ret_port": None}
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["group"]:
                    vlan_found = line.split()[2]
                    port_found = line.split()[3]
                    ret_dict["ret_vlan"] = vlan_found
                    ret_dict["ret_port"] = port_found
                    if "vlan" in args and "port" in args:
                        if vlan_found == args["vlan"] \
                                and port_found == args["port"]:
                            match = "yes"
                            break
                    elif "vlan" in args:
                        if vlan_found == args["vlan"] \
                                and port_found == args["port"]:
                            match = "yes"
                            break
                    elif "port" in args:
                        if vlan_found == args["vlan"] \
                                and port_found == args["port"]:
                            match = "yes"
                            break
                    else:
                        match = "yes"
                        break

        result = True if match == "yes" else False

        return result, ret_dict
