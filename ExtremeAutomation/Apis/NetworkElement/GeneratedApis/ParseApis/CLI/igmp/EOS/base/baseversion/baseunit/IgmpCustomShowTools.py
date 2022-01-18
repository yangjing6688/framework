from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.igmp.base.IgmpBaseCustomShowTools import \
    IgmpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return IgmpCustomShowTools(device)


class IgmpCustomShowTools(IgmpBaseCustomShowTools):
    def __init__(self, device):
        IgmpBaseCustomShowTools.__init__(self, device)

    def check_igmp_state(self, output, args, **kwargs):
        igmp_enabled_vlans = self.pw.get_value_by_offset(output, "IGMP config for vlan", 4).split()

        result = True if args["vlan"] in igmp_enabled_vlans else False

        return result, {"ret_igmp_vlans": igmp_enabled_vlans}

    def check_igmp_version(self, output, args, **kwargs):
        igmp_version = self.pw.get_value_by_offset(output, "Version", 2)

        result = True if args["igmp_ver"] == igmp_version else False
        return result, {"ret_igmp_version": igmp_version}
