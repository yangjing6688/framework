from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.upm.base.UpmBaseCustomShowTools import \
    UpmBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class UpmCustomShowTools(UpmBaseCustomShowTools):
    def __init__(self, device):
        super(UpmCustomShowTools, self).__init__(device)

    def check_upm_authenticate_profile_ports(self, output, args, **kwargs):
        ports = self.pw.get_value_by_offset(output, args["auth_profile"], 1)
        result = self.it.compare_port_values(ports, args["ports"], self.inspect_constants.FOUNDIN)

        return result, {"ret_ports": ports}

    def check_upm_unauthenticated_profile_ports(self, output, args, **kwargs):
        ports = self.pw.get_value_by_offset(output, args["auth_profile"], 1)
        result = self.it.compare_port_values(ports, args["ports"], self.inspect_constants.FOUNDIN)

        return result, {"ret_ports": ports}
