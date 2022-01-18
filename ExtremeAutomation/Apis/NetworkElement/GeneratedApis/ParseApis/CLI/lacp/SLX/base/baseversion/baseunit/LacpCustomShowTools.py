from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.lacp.base.LacpBaseCustomShowTools import \
    LacpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class LacpCustomShowTools(LacpBaseCustomShowTools):
    def __init__(self, device):
        super(LacpCustomShowTools, self).__init__(device)

    def verify_lacp_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_is_in_lag(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
