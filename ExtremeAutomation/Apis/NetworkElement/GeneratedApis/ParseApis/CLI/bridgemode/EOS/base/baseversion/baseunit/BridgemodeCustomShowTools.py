from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.bridgemode.base.BridgemodeBaseCustomShowTools \
    import BridgemodeBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return BridgemodeCustomShowTools(device)


class BridgemodeCustomShowTools(BridgemodeBaseCustomShowTools):
    def __init__(self, device):
        super(BridgemodeCustomShowTools, self).__init__(device)

    def check_bridge_mode(self, output, args, **kwargs):
        """
        Valid bridge modes are 0 and 1.
        0 = Customer Bridge
        1 = Provider Bridge
        """
        valid_modes = {0: "customer",
                       1: "provider"
                       }

        output = output.lower()

        dev_mode = self.pw.get_value_by_offset(output, "current bridge", 5)

        result = True if dev_mode == valid_modes[args["bridge_mode"]] else False
        return result, {"ret_bridge_mode": dev_mode}
