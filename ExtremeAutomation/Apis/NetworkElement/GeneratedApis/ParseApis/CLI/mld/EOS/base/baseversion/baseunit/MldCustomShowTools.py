from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.mld.base.MldBaseCustomShowTools import \
    MldBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return MldCustomShowTools(device)


class MldCustomShowTools(MldBaseCustomShowTools):
    def __init__(self, device):
        super(MldCustomShowTools, self).__init__(device)

    def check_mld_state(self, output, args, **kwargs):
        mld_enabled_vlans = self.pw.get_value_by_offset(output, "MLD config for vlan", 4).split()

        result = True if args["vlan"] in mld_enabled_vlans else False
        return result, {"ret_enabled_vlans": str(mld_enabled_vlans)}

    def check_mld_version(self, output, args, **kwargs):
        mld_version = self.pw.get_value_by_offset(output, "Version", 2)

        result = True if mld_version == args["version"] else False
        return result, {"ret_version": mld_version}
