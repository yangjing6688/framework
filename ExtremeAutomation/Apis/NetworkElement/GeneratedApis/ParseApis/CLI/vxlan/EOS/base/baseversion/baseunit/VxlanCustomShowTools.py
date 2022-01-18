from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vxlan.base.VxlanBaseCustomShowTools import \
    VxlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return VxlanCustomShowTools(device)


class VxlanCustomShowTools(VxlanBaseCustomShowTools):
    def __init__(self, device):
        super(VxlanCustomShowTools, self).__init__(device)

    def check_logical_switch_exists(self, output, args, **kwargs):

        result = True if args["name"] in output else False
        return result, {"ret_check_exists": args["name"]}
