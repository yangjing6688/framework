from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.hostutils.base.HostutilsBaseCustomShowTools \
    import HostutilsBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return HostutilsCustomShowTools(device)


class HostutilsCustomShowTools(HostutilsBaseCustomShowTools):
    def __init__(self, device):
        super(HostutilsCustomShowTools, self).__init__(device)

    def check_ping_result(self, output, args, **kwargs):
        host = self.pw.get_value_by_offset(output, args["host_address"], 3)

        result = True if args["host_address"] in host else False
        return result, result
