from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.tunnel.base.TunnelBaseCustomShowTools import \
    TunnelBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return TunnelCustomShowTools(device)


class TunnelCustomShowTools(TunnelBaseCustomShowTools):
    def __init__(self, device):
        super(TunnelCustomShowTools, self).__init__(device)

    def check_tunnel_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
