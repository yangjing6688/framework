from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.ssh.base.SshBaseCustomShowTools import \
    SshBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class SshCustomShowTools(SshBaseCustomShowTools):
    def __init__(self, device):
        super(SshCustomShowTools, self).__init__(device)

    def verify_enabled(self, output, args, **kwargs):
        state_found = self.pw.get_value_by_offset(output, "SSH Access", 3)
        result = True if state_found == "Enabled" else False
        return result, {"ret_state": state_found}

    def verify_disabled(self, output, args, **kwargs):
        state_found = self.pw.get_value_by_offset(output, "SSH Access", 3)
        result = True if state_found == "Disabled" else False
        return result, {"ret_state": state_found}
