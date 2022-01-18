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
        src_mac = StringUtils.normalize_mac(args["mac"], "-")
        mac_list = self.pw.get_value_by_offset(output, src_mac, 0).split()
        vlan_list = self.pw.get_value_by_offset(output, src_mac, 1).split()
        port_list = self.pw.get_value_by_offset(output, src_mac, 2).split()

        if port_list[0] == "any":
            port_list = self.pw.get_value_by_offset(output, src_mac, 5).split()
        ret_dict = {"ret_vlan": None,
                    "ret_port": None}
        if mac_list[0] == "valueNotPresent":
            return False, ret_dict
        else:
            for i, mac in enumerate(mac_list):
                if mac == src_mac:
                    ret_dict["ret_vlan"] = vlan_list[i]
                    ret_dict["ret_port"] = port_list[i]
                    if vlan_list[i] == args["vlan"]:
                        port_block = self.it.get_port_parser_obj(port_list[i])
                        if port_block.is_port_on_list(args["port"]):
                            return True, ret_dict
        return False, ret_dict

    def check_fdb_entry_only_exists_once(self, output, args, **kwargs):
        """
        If a mac entry exists in the mac address table more than once, this function returns False.
        """
        mac_list = self.pw.get_value_by_offset(output, args["mac"], 0).split()

        result = True if len(mac_list) == 1 else False
        return result, {"ret_mac_count": str(len(mac_list))}

    def check_fdb_agetime(self, output, args, **kwargs):
        output_agetime = self.pw.get_value_by_offset(output, "Aging time:", 2)

        result = True if args["agetime"] == output_agetime else False
        return result, {"ret_agetime": output_agetime}
