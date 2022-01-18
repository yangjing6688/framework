from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.fdb.base.FdbBaseCustomShowTools import \
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
        output = output.replace("\n", "\r\n")

        found_vlans = self.pw.get_exact_value_by_offset(output, args["mac"], 0)
        found_ports = self.pw.get_exact_value_by_offset(output, args["mac"], 3)
        ret_dict = {"ret_vlan": None,
                    "ret_port": None}
        for i, vlan in enumerate(found_vlans):
            if vlan == args["vlan"]:
                ret_dict["ret_vlan"] = vlan
                ret_dict["ret_port"] = found_ports[i].replace("Port-", "")

        result = ret_dict["ret_vlan"] == args["vlan"] and ret_dict["ret_port"] == args["port"]
        return result, ret_dict

    def check_fdb_agetime(self, output, args, **kwargs):
        output_agetime = self.pw.get_value_by_offset(output, "Mac Address Table Aging Time:", 5)

        result = True if args["agetime"] == output_agetime else False
        return result, {"ret_agetime": output_agetime}

    def check_fdb_entry_only_exists_once(self, output, args, **kwargs):
        """
        If a mac entry exists in the mac address table more than once, this function returns False.
        """
        mac = StringUtils.normalize_mac_lowercase(args["mac"])
        mac_in_table = self.pw.get_value_by_offset(output, mac, 2)
        mac_list = mac_in_table.split()

        result = True if len(mac_list) == 1 else False
        return result, {"ret_mac_count": str(len(mac_list))}

    def check_fdb_entry_exists_twice(self, output, args, **kwargs):
        """
        Mac entry should exist in the mac address table two times in the case of 2 SPBM VLANS.
        """
        mac = StringUtils.normalize_mac_lowercase(args["mac"])
        mac_in_table = self.pw.get_value_by_offset(output, mac, 2)
        mac_list = mac_in_table.split()

        result = True if len(mac_list) == 2 else False
        return result, {"ret_mac_count": str(len(mac_list))}
