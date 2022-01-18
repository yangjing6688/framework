from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_exists(self, output, args, **kwargs):
        item = "SNMPv2-SMI::mib-2.17.7.1.4.3.1.1." + args["vlan"]

        return item in output, item in output
