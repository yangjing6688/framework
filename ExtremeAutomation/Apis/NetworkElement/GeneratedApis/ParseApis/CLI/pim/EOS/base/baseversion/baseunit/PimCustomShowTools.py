from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.pim.base.PimBaseCustomShowTools import \
    PimBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return PimCustomShowTools(device)


class PimCustomShowTools(PimBaseCustomShowTools):
    def __init__(self, device):
        super(PimCustomShowTools, self).__init__(device)

    def check_pim_interface_state(self, output, args, **kwargs):
        interface = args["interface"]
        if interface.isdigit():
            interface = StringUtils.eos_interface(interface)

        pim_enabled_ifaces = self.pw.get_value_by_offset(output, interface, 0).split()

        result = True if interface in pim_enabled_ifaces else False
        return result, {"ret_enabled_interfaces": str(pim_enabled_ifaces)}

    def check_pim_bsr(self, output, args, **kwargs):
        interface = args["interface"]
        if interface.isdigit():
            interface = StringUtils.eos_interface(interface)

        bsr_interfaces = self.pw.get_value_by_offset(output, interface, 0).split()

        result = True if interface in bsr_interfaces else False
        return result, {"ret_bsr_interfaces": str(bsr_interfaces)}

    def check_pim_rp(self, output, args, **kwargs):
        rp_ip = self.pw.get_value_by_offset(output, "ip pim rp-candidate", 3)
        rp_acl = self.pw.get_value_by_offset(output, "ip pim rp-candidate", 5)

        result = True if args["ip_address"] == rp_ip and args["acl"] == rp_acl else False
        return result, {"ret_ip": rp_ip, "ret_acl": rp_acl}
