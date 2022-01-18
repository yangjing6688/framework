from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.igmp.base.IgmpBaseCustomShowTools import \
    IgmpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class IgmpCustomShowTools(IgmpBaseCustomShowTools):
    def __init__(self, device):
        super(IgmpCustomShowTools, self).__init__(device)

    def check_igmp_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_igmp_version(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_igmp_vlan_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_igmp_group(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_igmp_snooping_vlan_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_igmp_snooping_proxy_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_igmp_snooping_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_igmp_snooping_querier_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
