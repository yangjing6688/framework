from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.fdb.base.FdbBaseCustomShowTools import \
    FdbBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return FdbCustomShowTools(device)


class FdbCustomShowTools(FdbBaseCustomShowTools):
    def __init__(self, device):
        super(FdbCustomShowTools, self).__init__(device)

    def check_fdb_entry_exists(self, output, args, **kwargs):
        output = output.replace("SNMPv2-SMI::mib-2.17.7.1.2.2.1.2.", "")
        new_mac = StringUtils().mac_to_dec(args["mac_address"])
        item = args["vlan"] + "." + new_mac
        result = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if result == args["port_if_index"] else False
        return result, result

    def check_fdb_entry_only_exists_once(self, output, args, **kwargs):
        """
        If a mac entry exists in the mac address table more than once, this function returns False.
        """
        output = output.replace("SNMPv2-SMI::mib-2.17.7.1.2.2.1.2.", "")
        new_mac = StringUtils().mac_to_dec(args["mac_address"])
        mac_list = self.pw.get_value_by_offset(output, new_mac, 0)

        mac_list = mac_list.split()

        result = True if len(mac_list) == 1 else False
        return result, {"ret_mac_count": str(len(mac_list))}

    def check_fdb_entry_exists_twice(self, output, args, **kwargs):
        """
        Mac entry should exist in the mac address table two times in the case of 2 SPBM VLANS.
        """
        output = output.replace("SNMPv2-SMI::mib-2.17.7.1.2.2.1.2.", "")
        new_mac = StringUtils().mac_to_dec(args["mac_address"])
        mac_list = self.pw.get_value_by_offset(output, new_mac, 0)

        mac_list = mac_list.split()

        result = True if len(mac_list) == 2 else False
        return result, {"ret_mac_count": str(len(mac_list))}
