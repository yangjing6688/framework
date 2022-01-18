from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.spanningtree.base.\
    SpanningtreeBaseCustomShowTools import SpanningtreeBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return SpanningtreeCustomShowTools(device)


class SpanningtreeCustomShowTools(SpanningtreeBaseCustomShowTools):
    def __init__(self, device):
        super(SpanningtreeCustomShowTools, self).__init__(device)

    def check_spanning_tree_enabled(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        status = self.pw.get_value_at_location(output, column=5, name=None, row=7)

        result = True if instance == args["sid"] and status == "Enabled" else False
        return result, {"ret_spanning_tree_status", status}

    def check_spanning_tree_version(self, output, args, **kwargs):
        version = args["version"]
        result = []
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["sid"]:
                    result.append(line.split()[2])
        result = True if version in result else False
        return result, {"ret_stp_version": version}

    def check_spanning_tree_bridge_priority(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        priority = self.pw.get_value_at_location(output, column=1, name=None, row=7)

        result = True if instance == args["sid"] and priority == args["priority"] else False
        return result, {"ret_bridge_priority": priority}

    def check_spanning_tree_root(self, output, args, **kwargs):
        root = args["root_id"]
        result = []
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["sid"]:
                    result.append(line.split()[1])
        result = True if root in result else False
        return result, {"ret_stp_root": root}

    def check_stp_boot_flag_is_rstp(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        stp_flag = self.pw.get_value_by_offset(output, "flags spanning-tree-mode", 2)

        if stp_flag == "rstp":
            result = True
            return result, {"ret_stp_flag": stp_flag}
        else:
            result = False
            return result, {"ret_stp_flag": stp_flag}

    def check_stp_boot_flag_is_mstp(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        stp_flag = self.pw.get_value_by_offset(output, "flags spanning-tree-mode", 2)

        if stp_flag == "mstp":
            result = True
            return result, {"ret_stp_flag": stp_flag}
        else:
            result = False
            return result, {"ret_stp_flag": stp_flag}

    def check_stp_ports_link_type_is_point_to_point(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        port = self.pw.get_value_by_offset(output, "Port Number", 3)
        port_status = self.pw.get_value_by_offset(output, "Port Oper  P2P Status", 5)

        if port == args["port"] and port_status == "True":
            result = True
            return result, {"ret_port_status": port_status}
        else:
            result = False
            return result, {"ret_port_status": port_status}

    def check_stp_ports_link_type_is_edge(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        port = self.pw.get_value_by_offset(output, "Port Number", 3)
        port_status = self.pw.get_value_by_offset(output, "Port Oper Edge Status", 5)

        if port == args["port"] and port_status == "True":
            result = True
            return result, {"ret_port_status": port_status}
        else:
            result = False
            return result, {"ret_port_status": port_status}

    def check_stp_bpduguard(self, output, args, **kwargs):
        result = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["port"]:
                    result = line.split()[5]
                    break
        result = True if result == "Enabled" else False
        return result, {"ret_bpduguard": args["port"]}

    def check_stp_hello_time(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        hello_time = self.pw.get_value_at_location(output, column=3, name=None, row=7)

        result = True if instance == args["sid"] and hello_time == args["hello_time"] else False
        return result, {"ret_hello_time": hello_time}

    def check_stp_fwd_delay(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        fwd_delay = self.pw.get_value_at_location(output, column=4, name=None, row=7)

        result = True if instance == args["sid"] and fwd_delay == args["fwd_delay"] else False
        return result, {"ret_fwd_delay": fwd_delay}

    def check_stp_max_age(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        max_age = self.pw.get_value_at_location(output, column=2, name=None, row=7)

        result = True if instance == args["sid"] and max_age == args["max_age"] else False
        return result, {"ret_max_age": max_age}

    def check_stp_bridge_hello_time(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        hello_time = self.pw.get_value_at_location(output, column=3, name=None, row=7)

        result = True if instance == args["sid"] and hello_time == args["hello_time"] else False
        return result, {"ret_bridge_hello_time": hello_time}

    def check_stp_bridge_fwd_delay(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        fwd_delay = self.pw.get_value_at_location(output, column=4, name=None, row=7)

        result = True if instance == args["sid"] and fwd_delay == args["fwd_delay"] else False
        return result, {"ret_bridge_fwd_delay": fwd_delay}

    def check_stp_bridge_max_age(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        max_age = self.pw.get_value_at_location(output, column=2, name=None, row=7)

        result = True if instance == args["sid"] and max_age == args["max_age"] else False
        return result, {"ret_bridge_max_age": max_age}

    def check_stp_root_hello_time(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        hello_time = self.pw.get_value_at_location(output, column=3, name=None, row=7)

        result = True if instance == args["sid"] and hello_time == args["hello_time"] else False
        return result, {"ret_root_hello_time": hello_time}

    def check_stp_root_fwd_delay(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        fwd_delay = self.pw.get_value_at_location(output, column=4, name=None, row=7)

        result = True if instance == args["sid"] and fwd_delay == args["fwd_delay"] else False
        return result, {"ret_fwd_delay": fwd_delay}

    def check_stp_root_max_age(self, output, args, **kwargs):
        instance = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        max_age = self.pw.get_value_at_location(output, column=2, name=None, row=7)

        result = True if instance == args["sid"] and max_age == args["max_age"] else False
        return result, {"ret_root_max_age": max_age}

    def check_spanning_tree_cist_root(self, output, args, **kwargs):
        cist_root_found = self.pw.get_value_at_location(output, column=3, name=None, row=6)

        result = True if cist_root_found == args["root_id"] else False
        return result, {"ret_cist_root": cist_root_found}

    def check_regional_name(self, output, args, **kwargs):
        regional_name_found = self.pw.get_value_at_location(output, column=4, name=None, row=14)

        result = True if regional_name_found == args["region_name"] else False
        return result, {"ret_reg_name": regional_name_found}

    def check_revision_level(self, output, args, **kwargs):
        revision_level_found = self.pw.get_value_at_location(output, column=4, name=None, row=15)

        result = True if revision_level_found == args["revision_level"] else False
        return result, {"ret_rev_lvl": revision_level_found}

    def check_mstp_cist_max_age(self, output, args, **kwargs):
        max_age_found = self.pw.get_value_at_location(output, column=4, name=None, row=15)

        result = True if max_age_found == args["revision_level"] else False
        return result, {"ret_max_age": max_age_found}

    def check_cist_regional_root(self, output, args, **kwargs):
        cist_regional_root_found = self.pw.get_value_at_location(output, column=4, name=None, row=7)

        result = True if cist_regional_root_found == args["cist_regional_root"] else False
        return result, {"ret_reg_root": cist_regional_root_found}

    def check_mstp_bridge_address(self, output, args, **kwargs):
        bridge_address_found = self.pw.get_value_at_location(output, column=3, name=None, row=5)

        result = True if bridge_address_found == args["bridge_address"] else False
        return result, {"ret_bridge_address": bridge_address_found}

    def check_mstp_cist_root(self, output, args, **kwargs):
        cist_root_found = self.pw.get_value_at_location(output, column=3, name=None, row=6)

        result = True if cist_root_found == args["cist_root"] else False
        return result, {"ret_cist_root": cist_root_found}

    def check_mstp_cist_regional_root(self, output, args, **kwargs):
        cist_regional_root_found = self.pw.get_value_at_location(output, column=4, name=None, row=7)

        result = True if cist_regional_root_found == args["cist_regional_root"] else False
        return result, {"ret_cist_reg_root": cist_regional_root_found}

    def check_mstp_cist_root_port(self, output, args, **kwargs):
        cist_root_port_found = self.pw.get_value_at_location(output, column=4, name=None, row=8)

        result = True if cist_root_port_found == args["cist_root_port"] else False
        return result, {"ret_cist_root_port": cist_root_port_found}

    def check_mstp_cist_root_cost(self, output, args, **kwargs):
        cist_root_cost_found = self.pw.get_value_at_location(output, column=4, name=None, row=9)

        result = True if cist_root_cost_found == args["cist_root_cost"] else False
        return result, {"ret_cist_root_cost": cist_root_cost_found}

    def check_mstp_cist_regional_root_cost(self, output, args, **kwargs):
        cist_regional_root_cost_found = self.pw.get_value_at_location(output, column=5, name=None, row=10)

        result = True if cist_regional_root_cost_found == args["cist_regional_root_cost"] else False
        return result, {"ret_cist_reg_root_cost": cist_regional_root_cost_found}

    def check_mstp_cist_forward_delay(self, output, args, **kwargs):
        cist_forward_delay_found = self.pw.get_value_at_location(output, column=4, name=None, row=16)

        result = True if cist_forward_delay_found == args["cist_forward_delay"] else False
        return result, {"ret_cist_fwd_delay": cist_forward_delay_found}

    def check_mstp_enabled_on_interface(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        port = self.pw.get_value_by_offset(output.lower(), "port number", 3)
        port_status = self.pw.get_value_by_offset(output.lower(), "force-port-state", 4)

        if port == args["port"] and port_status == "enable":
            return True, True

        else:
            return False, False

    def check_stp_port_role(self, output, args, **kwargs):
        state = args["state"].lower()
        current_state = self.pw.get_value_by_offset(output, args["port"], 2)

        if state == current_state.lower():
            result = True
            return result, {"ret_current_state": current_state}
        else:
            self.logger.log_info("STP port state: " + state)
            return False, False
