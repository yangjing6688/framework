from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vlan.EOS.base.baseversion.baseunit.\
    VlanCustomShowTools import VlanCustomShowTools as VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return VlanCustomShowTools(device)


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_exists(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
