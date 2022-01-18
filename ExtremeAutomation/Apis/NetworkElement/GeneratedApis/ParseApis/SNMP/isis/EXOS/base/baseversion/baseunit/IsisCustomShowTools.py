from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.isis.base.IsisBaseCustomShowTools import \
    IsisBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class IsisCustomShowTools(IsisBaseCustomShowTools):
    def __init__(self, device):
        super(IsisCustomShowTools, self).__init__(device)

    def verify_isis_globally_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_globally_disabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
