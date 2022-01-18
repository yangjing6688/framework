from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.lldp.base.LldpBaseCustomShowTools import \
    LldpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return LldpCustomShowTools(device)


class LldpCustomShowTools(LldpBaseCustomShowTools):
    def __init__(self, device):
        super(LldpCustomShowTools, self).__init__(device)

    def check_lldp_tx_interval(self, output, args, **kwargs):
        item = "SNMPv2-SMI::iso.0.8802.1.1.2.1.1.1." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == args["interval"] else False
        return result, {"ret_interval": result_item}

    def check_lldp_tx_hold_multiplier(self, output, args, **kwargs):
        item = "SNMPv2-SMI::iso.0.8802.1.1.2.1.1.2." + args["oid_index"]
        result_item = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_item == args["multiplier"] else False
        return result, {"ret_hold_multiplier": result_item}
