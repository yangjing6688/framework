from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.lldp.base.LldpBaseCustomShowTools import \
    LldpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class LldpCustomShowTools(LldpBaseCustomShowTools):
    def __init__(self, device):
        super(LldpCustomShowTools, self).__init__(device)

    def determine_lldp_port_transmit_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def determine_lldp_port_receive_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_lldp_tx_interval(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_lldp_sys_name(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_lldp_tx_hold_multiplier(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
