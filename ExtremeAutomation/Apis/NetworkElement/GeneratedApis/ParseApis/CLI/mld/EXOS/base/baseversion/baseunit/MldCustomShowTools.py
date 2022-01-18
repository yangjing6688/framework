from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.mld.base.MldBaseCustomShowTools import \
    MldBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return MldCustomShowTools(device)


class MldCustomShowTools(MldBaseCustomShowTools):
    def __init__(self, device):
        super(MldCustomShowTools, self).__init__(device)

    def check_mld_state(self, output, args, **kwargs):
        if args["vlan"].isdigit():
            vlan = StringUtils.exos_vlan_string(args["vlan"])
        else:
            vlan = args["vlan"]

        mld_enabled_vlans = self.pw.get_value_by_offset(output, vlan, 0).split()

        result = True if vlan in mld_enabled_vlans else False
        return result, {"ret_enabled_vlans": str(mld_enabled_vlans)}

    def check_mld_snooping_state(self, output, args, **kwargs):
        if args["vlan"].isdigit():
            vlan = StringUtils.exos_vlan_string(args["vlan"])
        else:
            vlan = args["vlan"]

        snooping_status = self.pw.get_value_by_offset(output, vlan, 2)

        result = True if snooping_status.find("z") != -1 else False
        return result, {"ret_snooping_state": snooping_status}

    def check_mld_version(self, output, args, **kwargs):
        if args["vlan"].isdigit():
            vlan = StringUtils.exos_vlan_string(args["vlan"])
        else:
            vlan = args["vlan"]

        mld_version = self.pw.get_value_by_offset(output, vlan, 5)

        result = True if mld_version == args["version"] else False
        return result, {"ret_version": mld_version}
