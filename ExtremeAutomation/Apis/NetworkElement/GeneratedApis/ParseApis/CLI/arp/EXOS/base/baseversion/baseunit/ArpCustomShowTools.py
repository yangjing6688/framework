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
        output = output.replace("show iparp " + args["ip_address"], "")

        ipaddr = self.pw.get_value_by_offset(output, args["ip_address"], 1)
        macaddr = self.pw.get_value_by_offset(output, args["ip_address"], 2)
        intf = self.pw.get_value_by_offset(output, args["ip_address"], 5)

        if ipaddr == self.constants.VALUE_NOT_PRESENT:
            return False, {"ret_mac": None, "ret_interface": None}

        macaddr = StringUtils.normalize_mac(macaddr)
        mac_arg = StringUtils.normalize_mac(args["macaddr"])

        if args["intf"] is None:
            result = ipaddr == args["ip_address"] and macaddr == mac_arg
        else:
            int_arg = StringUtils.exos_vlan_string(args["intf"])
            result = ipaddr == args["ip_address"] and macaddr == mac_arg and intf == int_arg

        return result, {"ret_mac": macaddr,
                        "ret_interface": intf}
