from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.lldp.base.LldpBaseCustomShowTools import \
    LldpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return LldpCustomShowTools(device)


class LldpCustomShowTools(LldpBaseCustomShowTools):
    def __init__(self, device):
        super(LldpCustomShowTools, self).__init__(device)

    def check_lldp_tx_interval(self, output, args, **kwargs):
        found_item = self.pw.get_value_by_offset(output.lower(), "txinterval:", 1)

        result = True if found_item == args["interval"] else False
        return result, {"ret_tx_interval": found_item}

    def check_lldp_tx_hold_multiplier(self, output, args, **kwargs):
        found_item = self.pw.get_value_by_offset(output.lower(), "txholdmultiplier:", 1)

        result = True if found_item == args["multiplier"] else False
        return result, {"ret_tx_hold_multiplier": found_item}
