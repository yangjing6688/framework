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
        output = output.splitlines()
        result = None
        table_start = None
        table_end = None

        ipv6_addr = StringUtils.collapse_ipv6_address(args["ipv6_addr"])

        for index, line in enumerate(output):
            if line.find("VR") == 0 and table_start is None:
                table_start = index + 2
            if line.find("Total Entries") > 0:
                table_end = index
                break

        nd_table = output[table_start:table_end]

        for i in range(len(nd_table)):
            nd_table[i] = nd_table[i].replace("\n", "")
            nd_table[i] = nd_table[i].replace("\r", "")
            if i % 2 == 1:
                nd_table[i] += "\r\n"

        nd_table = "".join(nd_table)

        dev_ipv6_entries = self.pw.get_value_by_offset(nd_table, ipv6_addr, 1).split()
        dev_mac_entries = self.pw.get_value_by_offset(nd_table, ipv6_addr, 2).split()
        dev_interface_entries = self.pw.get_value_by_offset(nd_table, ipv6_addr, 5).split()
        ret_dict = {"ret_ipv6_entries": ', '.join(dev_ipv6_entries),
                    "ret_mac_entries": ', '.join(dev_mac_entries),
                    "ret_interfaces": ', '.join(dev_interface_entries)}
        if self.constants.VALUE_NOT_PRESENT not in dev_ipv6_entries:
            for i in range(len(dev_ipv6_entries)):
                if dev_ipv6_entries[i].find("%") > 0:
                    dev_ipv6_entry = dev_ipv6_entries[i][:dev_ipv6_entries[i].find("%")]
                else:
                    dev_ipv6_entry = dev_ipv6_entries[i]

                if dev_ipv6_entry == ipv6_addr:
                    result = True
                if StringUtils.normalize_mac(dev_mac_entries[i]) != StringUtils.normalize_mac(args["hw_addr"]):
                    result = False
                if args["interface"] is not None:
                    if dev_interface_entries[i] != StringUtils.exos_vlan_string(args["interface"]):
                        result = False
                if result:
                    return True, ret_dict
        return False, ret_dict
