from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.port.base.PortBaseCustomShowTools import \
    PortBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return PortCustomShowTools(device)


class PortCustomShowTools(PortBaseCustomShowTools):
    def __init__(self, device):
        super(PortCustomShowTools, self).__init__(device)

    def verify_port_enabled(self, output, *args):
        try:
            result = output["Object"]["AdminState"].upper() == "UP"
            return result, {"ret_state": output["Object"]["AdminState"]}
        except KeyError:
            return False, None

    def verify_port_disabled(self, output, *args):
        try:
            result = output["Object"]["AdminState"].upper() == "DOWN"
            return result, {"ret_state": output["Object"]["AdminState"]}
        except KeyError:
            return False, None
