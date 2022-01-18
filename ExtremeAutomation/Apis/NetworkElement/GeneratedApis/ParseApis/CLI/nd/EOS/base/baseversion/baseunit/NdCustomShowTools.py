from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.nd.base.NdBaseCustomShowTools import \
    NdBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return NdCustomShowTools(device)


class NdCustomShowTools(NdBaseCustomShowTools):
    def __init__(self, device):
        super(NdCustomShowTools, self).__init__(device)

    def check_nd_entry_exists(self, output, args, **kwargs):
        result = None

        ipv6_addr = StringUtils.expand_ipv6_address(args["ipv6_addr"], leading_zeroes=False)

        dev_ipv6_entries = self.pw.get_value_by_offset(output, ipv6_addr, 0).split()
        dev_mac_entries = self.pw.get_value_by_offset(output, ipv6_addr, 1).split()
        dev_interface_entries = self.pw.get_value_by_offset(output, ipv6_addr, 3).split()
        ret_dict = {"ret_ipv6_entries": ', '.join(dev_ipv6_entries),
                    "ret_mac_entries": ', '.join(dev_mac_entries),
                    "ret_interfaces": ', '.join(dev_interface_entries)}
        if self.constants.VALUE_NOT_PRESENT not in dev_ipv6_entries:
            for i in range(len(dev_ipv6_entries)):
                if dev_ipv6_entries[i] == ipv6_addr:
                    result = True
                if StringUtils.normalize_mac(dev_mac_entries[i]) != StringUtils.normalize_mac(args["mac_addr"]):
                    result = False
                if args["interface"] is not None:
                    if dev_interface_entries[i] != StringUtils.eos_interface(args["interface"]):
                        result = False
                if result:
                    return True, ret_dict
        return False, ret_dict
