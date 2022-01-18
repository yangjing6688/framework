from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.acl.base.AclBaseCustomShowTools import \
    AclBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return AclCustomShowTools(device)


class AclCustomShowTools(AclBaseCustomShowTools):
    def __init__(self, device):
        super(AclCustomShowTools, self).__init__(device)

    def check_ipv4_acl_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_ipv6_acl_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
