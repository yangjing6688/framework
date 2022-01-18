from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.isis.base.IsisBaseCustomShowTools import \
    IsisBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return IsisCustomShowTools(device)


class IsisCustomShowTools(IsisBaseCustomShowTools):
    def __init__(self, device):
        super(IsisCustomShowTools, self).__init__(device)

    def verify_isis_globally_enabled(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_isis_globally_disabled(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
