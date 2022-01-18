from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.lldp.base.LldpBaseCustomShowTools import \
    LldpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return LldpCustomShowTools(device)


class LldpCustomShowTools(LldpBaseCustomShowTools):
    def __init__(self, device):
        super(LldpCustomShowTools, self).__init__(device)

    def check_tlv_status(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_lldp_tx_interval(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        tx_interval = output['openconfig-lldp:config']['hello-timer']

        result = True if str(tx_interval) == args["interval"] else False
        return result, {"ret_interval": str(tx_interval)}

    def check_lldp_remote_port(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_lldp_neighbor_sysname(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
