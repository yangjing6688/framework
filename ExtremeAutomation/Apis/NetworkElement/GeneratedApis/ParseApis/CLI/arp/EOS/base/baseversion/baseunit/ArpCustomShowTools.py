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
        output = output.replace("arp " + args["ip_address"], "")

        macaddr = self.pw.get_value_by_offset(output, args["ip_address"], 1)
        intf = self.pw.get_value_by_offset(output, args["ip_address"], 4)

        # This checks if the first digit of intf is a digit or the character "-".
        # If it is assume flags were present and shift the intf index by 1.
        if intf[0].isdigit() or intf == "-":
            intf = self.pw.get_value_by_offset(output, args["ip_address"], 5)

        int_arg = StringUtils.eos_interface(args["intf"])
        mac_arg = StringUtils.normalize_mac(args["macaddr"])

        if macaddr != "valueNotPresent":
            macaddr = StringUtils.normalize_mac(macaddr)

        if int_arg is None:
            result = macaddr == mac_arg
        else:
            result = macaddr == mac_arg and intf == int_arg

        return result, {"ret_mac": macaddr,
                        "ret_interface": intf}
