from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.cfm.base.CfmBaseCustomShowTools import \
    CfmBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return CfmCustomShowTools(device)


class CfmCustomShowTools(CfmBaseCustomShowTools):
    def __init__(self, device):
        super(CfmCustomShowTools, self).__init__(device)

    def check_cfm_state(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_domain(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_group(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_cfm_segment(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
