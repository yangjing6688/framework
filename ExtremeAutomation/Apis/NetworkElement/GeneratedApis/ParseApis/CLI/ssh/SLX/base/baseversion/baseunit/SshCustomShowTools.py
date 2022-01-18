from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.ssh.base.SshBaseCustomShowTools import \
    SshBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class SshCustomShowTools(SshBaseCustomShowTools):
    def __init__(self, device):
        super(SshCustomShowTools, self).__init__(device)

    def verify_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_disabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_client_source_interface(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_tcp_port(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
