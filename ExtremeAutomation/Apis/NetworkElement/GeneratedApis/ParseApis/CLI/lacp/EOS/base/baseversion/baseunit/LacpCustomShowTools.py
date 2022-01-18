from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.lacp.base.LacpBaseCustomShowTools import \
    LacpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return LacpCustomShowTools(device)


class LacpCustomShowTools(LacpBaseCustomShowTools):
    def __init__(self, device):
        super(LacpCustomShowTools, self).__init__(device)

    def check_port_is_in_lag(self, output, args, **kwargs):
        new_output = self.pw.get_eol_value(output, "Attached Ports: ")[0]
        attached_ports = new_output.replace("Attached Ports:  ", "")

        result = self.it.compare_port_values(attached_ports, args["lag_port"], self.inspect_constants.FOUNDIN)
        return result, {"ret_ports": attached_ports}

    def verify_lacp_enabled(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
