from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.arp.base.ArpBaseCustomShowTools import \
    ArpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return ArpCustomShowTools(device)


class ArpCustomShowTools(ArpBaseCustomShowTools):
    def __init__(self, device):
        super(ArpCustomShowTools, self).__init__(device)

    def verify_arp_entry_exists(self, output, args, **kwargs):
        ip_arg = args["ip_address"]
        ipaddr = self.pw.get_value_by_offset(output, ip_arg, 0)
        macaddr = self.pw.get_value_by_offset(output, ip_arg, 1)
        intf = self.pw.get_value_by_offset(output, ip_arg, 2)

        if ipaddr == self.constants.VALUE_NOT_PRESENT:
            return False, {"ret_mac": macaddr,
                           "ret_interface": intf}

        macaddr = StringUtils.normalize_mac(macaddr)
        mac_arg = StringUtils.normalize_mac(args["macaddr"])

        if args["intf"] is None:
            result = macaddr == mac_arg
        else:
            result = macaddr == mac_arg and intf == args["intf"]

        return result, {"ret_mac": macaddr,
                        "ret_interface": intf}

    def verify_arp_vrf_entry_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
