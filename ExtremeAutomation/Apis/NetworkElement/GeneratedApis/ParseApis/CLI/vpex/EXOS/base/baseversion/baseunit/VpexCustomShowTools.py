from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vpex.base.VpexBaseCustomShowTools import \
    VpexBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class VpexCustomShowTools(VpexBaseCustomShowTools):
    def __init__(self, device):
        super(VpexCustomShowTools, self).__init__(device)

    def verify_vpex_enabled(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output.lower(), "extender", 3)

        result = True if state.lower() == "enabled" else False
        return result, {"ret_state": state}

    def verify_vpex_auto_configuration_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vpex_ring_rebalancing_set_to_auto(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vpex_set_on_port(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_all_cascade_ports(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_vpex_topology_on_port(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
