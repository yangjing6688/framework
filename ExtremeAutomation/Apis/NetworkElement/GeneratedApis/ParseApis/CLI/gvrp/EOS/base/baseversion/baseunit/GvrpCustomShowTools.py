from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.gvrp.base.GvrpBaseCustomShowTools import \
    GvrpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return GvrpCustomShowTools(device)


class GvrpCustomShowTools(GvrpBaseCustomShowTools):
    def __init__(self, device):
        super(GvrpCustomShowTools, self).__init__(device)

    def check_gvrp_state(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output.lower(), "global gvrp status", 4).replace(".", "")

        result = True if state == "enabled" else False

        return result, {"ret_grvp_state": state}

    def check_gvrp_state_port(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output, args["port"], 1).lower()

        result = True if state == "enabled" else False

        return result, {"ret_gvrp_state": state}
