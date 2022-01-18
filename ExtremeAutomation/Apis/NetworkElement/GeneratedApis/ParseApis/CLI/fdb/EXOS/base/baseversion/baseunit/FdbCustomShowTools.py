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
        src_mac = StringUtils.normalize_mac_lowercase(args["mac"])
        src_vlan = args["vlan"]
        formatted_vlan = ""
        if src_vlan.isdigit():
            if len(src_vlan) < 4:
                i = 4
                while i > len(src_vlan):
                    formatted_vlan += "0"
                    i -= 1
                formatted_vlan += src_vlan
                src_vlan = formatted_vlan

        mac_list = self.pw.get_value_by_offset(output, src_mac, 0).split()
        raw_vlan_list = self.pw.get_value_by_offset(output, src_mac, 1).split()

        # Flags can have spaces. Go to end of row, then index -1 to get accurate port list.
        viable_vlan_list = []
        for vlan in raw_vlan_list:
            alpha_vlan = vlan.split("(")[0]
            if len(vlan.split("(")) > 1:
                numeric_vlan = vlan.split("(")[1].rstrip(")")
                if src_vlan == alpha_vlan or src_vlan == numeric_vlan:
                    viable_vlan_list.append(vlan)
        raw_vlan_list = viable_vlan_list
        if len(viable_vlan_list) < 1:
            return False, None

        modified_output = output
        digit_port_list = []
        i = 0
        while i < len(raw_vlan_list):
            test_first_line = self.pw.get_value_from_string_to_eol(modified_output, raw_vlan_list[0])
            line_to_remove = raw_vlan_list[0] + " " + test_first_line + "\n"
            newlist = test_first_line.split()
            val_to_append = newlist[len(newlist) - 1]
            digit_port_list.append(val_to_append)
            modified_output = modified_output.replace(line_to_remove, "")
            i += 1

        port_list = digit_port_list

        ret_dict = {"ret_vlan": None,
                    "ret_port": None}
        if mac_list[0] == "valueNotPresent":
            return False, ret_dict
        else:
            # Normalize EXOS vlan output into VLAN IDs.
            vlan_list = []
            for vlan in raw_vlan_list:
                if src_vlan.isdigit():
                    vlan_list.append(vlan[vlan.index("(") + 1:vlan.rindex(")")])
                else:
                    vlan_list.append(vlan[0:vlan.index("(")])

            for i, vlan in enumerate(vlan_list):
                ret_dict["ret_vlan"] = vlan_list[i]
                ret_dict["ret_port"] = port_list[i]
                port_block = self.it.get_port_parser_obj(port_list[i])
                if port_block.is_port_on_list(args["port"]):
                    return True, ret_dict

        return False, ret_dict

    def check_fdb_agetime(self, output, args, **kwargs):
        output_agetime = self.pw.get_value_by_offset(output, "FDB Aging time:", 3)

        result = True if args["agetime"] == output_agetime else False
        return result, {"ret_agetime": output_agetime}

    def check_fdb_stats_total_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_offset(output, "Total:", 1)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_total_entries": total}

    def check_fdb_stats_static_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_offset(output, "Static:", 3)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_static_entires": total}

    def check_fdb_stats_perm_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_offset(output, "Perm:", 5)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_permanent_entries": total}

    def check_fdb_stats_dynamic_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_offset(output, "Dyn:", 7)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_dynamic_entries": total}

    def check_fdb_stats_dropped_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_offset(output, "Dropped:", 9)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_dropped_count": total}

    def check_fdb_stats_locked_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_offset(output, "Locked:", 11)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_locked_count": total}

    def check_fdb_stats_locked_with_timeout_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_offset(output, "Locked with Timeout:", 15)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_locked_with_timeout_count": total}

    def check_fdb_stats_total_port_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_index(output, 18)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_total_port_count": total}

    def check_fdb_stats_dynamic_port_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_index(output, 19)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_dynamic_port_count": total}

    def check_fdb_stats_static_port_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_index(output, 20)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_static_port_count": total}

    def check_fdb_stats_dropped_port_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_index(output, 21)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_dropped_port_count": total}

    def check_fdb_stats_total_vlan_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_index(output, 15)

        result = True if args["expected_stats"] == total else False
        return result,

    def check_fdb_stats_dynamic_vlan_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_index(output, 16)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_dynamic_vlan_count": total}

    def check_fdb_stats_static_vlan_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_index(output, 17)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_static_vlan_count": total}

    def check_fdb_stats_dropped_vlan_equal(self, output, args, **kwargs):
        total = self.pw.get_value_by_index(output, 18)

        result = True if args["expected_stats"] == total else False
        return result, {"ret_dropped_vlan_count": total}

    def check_fdb_entry_only_exists_once(self, output, args, **kwargs):
        """
        If a mac entry exists in the mac address table more than once, this function returns False.
        """
        mac_in_table = self.pw.get_value_by_offset(output, args["mac"], 0)
        mac_list = mac_in_table.split()

        result = True if len(mac_list) == 1 else False
        return result, {"ret_mac_count": str(len(mac_list))}
