from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.iprouting.base.IproutingBaseCustomShowTools \
    import IproutingBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return IproutingCustomShowTools(device)


class IproutingCustomShowTools(IproutingBaseCustomShowTools):
    def __init__(self, device):
        super(IproutingCustomShowTools, self).__init__(device)

    def validate_route_entry(self, output, args, **kwargs):
        return args["route"] in output, None

    def validate_static_route_int_exists(self, output, args, **kwargs):
        return args["interface"] in output, None
