from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.tunnel.base.TunnelBaseCustomShowTools import \
    TunnelBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return TunnelCustomShowTools(device)


class TunnelCustomShowTools(TunnelBaseCustomShowTools):
    def __init__(self, device):
        super(TunnelCustomShowTools, self).__init__(device)

    def check_tunnel_exists(self, output, args, **kwargs):
        tunnel_eos = StringUtils.eos_interface(args["tunnel"], "tun")

        tunnels = self.pw.get_value_by_offset(output, "Operationally", 0).split()

        result = True if tunnel_eos in tunnels else False

        return result, {"ret_tunnel": ', '.join(tunnels)}

    def check_tunnel_mode(self, output, args, **kwargs):
        tunnel_eos = StringUtils.eos_interface(args["tunnel"], "tun")
        tunnel_mode = self.pw.get_value_by_offset(output, tunnel_eos, 1)

        result = True if args["mode"].lower() in tunnel_mode.lower() else False

        return result, {"ret_tunnel": tunnel_mode}

    def check_tunnel_l2tb_port(self, output, args, **kwargs):
        tunnel_eos = StringUtils.eos_interface(args["tunnel"], "tun")
        tunnel_mode = self.pw.get_value_by_offset(output, tunnel_eos, 1)

        result = True if args["port"].lower() in tunnel_mode.lower() else False

        return result, {"ret_tunnel": tunnel_mode}
