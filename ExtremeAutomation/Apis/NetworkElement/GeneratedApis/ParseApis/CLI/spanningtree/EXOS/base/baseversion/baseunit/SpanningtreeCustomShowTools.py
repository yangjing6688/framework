from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.spanningtree.base.\
    SpanningtreeBaseCustomShowTools import SpanningtreeBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return SpanningtreeCustomShowTools(device)


class SpanningtreeCustomShowTools(SpanningtreeBaseCustomShowTools):
    def __init__(self, device):
        super(SpanningtreeCustomShowTools, self).__init__(device)

    def check_spanning_tree_enabled(self, output, args, **kwargs):
        spanning_tree_output = self.pw.get_value_by_offset(output, "Stp:", 3)
        spanning_tree_output = spanning_tree_output.split(" ")[0]

        result = True if spanning_tree_output.lower() == "enabled" else False
        return result, {"ret_spanning_tree_output", spanning_tree_output}

    def check_spanning_tree_version(self, output, args, **kwargs):
        spanning_tree_output = self.pw.get_value_by_offset(output, "Operational Mode:", 2)

        result = True if spanning_tree_output == args["version"] else False
        return result, {"ret_spanning_tree_output": spanning_tree_output}

    def check_spanning_tree_bridge_priority(self, output, args, **kwargs):
        bp_result = self.pw.get_value_by_offset(output, "Bridge Priority            : ", 3)

        result = True if bp_result == args["priority"] else False
        return result, {"ret_bp_result": bp_result}

    def check_spanning_tree_loop_protect_enabled(self, output, args, **kwargs):
        lp_result = self.pw.get_value_by_offset(output, "Loop Protect            : ", 3)

        result = True if lp_result == "On" else False
        return result, {"ret_lp_result": lp_result}

    def check_spanning_tree_span_guard_enabled(self, output, args, **kwargs):
        sg_result = self.pw.get_value_by_offset(output, "Edge Port Safe Guard    : ", 5)

        result = True if sg_result == "Enabled" else False
        return result, {"ret_sg_result": sg_result}

    def store_spanning_tree_tc_counter(self, output, args, **kwargs):
        tc_count = self.pw.get_value_by_offset(output, "Number of Topology Changes", 5)
        self.value_storage.add_value(self.device.name, "tc_count", tc_count)
        self.logger.log_info("Topology Change counter: " + tc_count)

        result = True if tc_count else False
        return result, {"ret_tc_count": tc_count}

    def check_spanning_tree_tc_incremented(self, output, args, **kwargs):
        tc_count_new = self.pw.get_value_by_offset(output, "Number of Topology Changes", 5)
        tc_count_old = self.value_storage.get_value(self.device.name, "tc_count")
        self.logger.log_info("Topology Change counter: " + tc_count_new)
        if tc_count_new.isdigit() and tc_count_old.isdigit():
            incr_offset = int(tc_count_new) - int(tc_count_old)
        else:
            return False, {"tc_increment": tc_count_new}

        if int(incr_offset) == int(args["increment"]):
            return True, True
        self.logger.log_info("Topology Change Increment: " + str(incr_offset))
        return False, False

    def check_spanning_tree_tc_same(self, output, args, **kwargs):
        tc_count_new = self.pw.get_value_by_offset(output, "Number of Topology Changes", 5)
        tc_count_old = self.value_storage.get_value(self.device.name, "tc_count")
        self.logger.log_info("Topology Change counter: " + tc_count_new)

        ret_tc_count = {"ret_tc_new": tc_count_new,
                        "ret_tc_old": tc_count_old}

        result = True if tc_count_old == tc_count_new else False
        return result, ret_tc_count

    def check_spanning_tree_root(self, output, args, **kwargs):
        reg_root = StringUtils.normalize_mac(args["root_id"])
        reg_root = reg_root.replace(":", "")
        instance = "s" + str(args["sid"]) + " "
        current_reg_root = self.pw.get_value_by_offset(output, instance, 5)

        result = True if reg_root.lower() in current_reg_root.lower() else False
        return result, {"ret_current_reg_root": current_reg_root}

    def check_instance_root_port(self, output, args, **kwargs):
        current_root_port = self.pw.get_value_by_offset(output, "Root Port", 3)
        port = "----" if args["port"] == "0" else args["port"]

        result = True if str(current_root_port) == str(port) else False
        return result, {"ret_current_root_port": current_root_port}

    def check_instance_regional_root(self, output, args, **kwargs):
        reg_root = StringUtils.normalize_mac(args["reg_root"])
        reg_root = reg_root.replace(":", "")

        current_reg_root = self.pw.get_value_by_offset(output, "MSTI Regional Root", 4)
        current_reg_root = current_reg_root.replace(":", "")

        ret_reg_root = {"ret_reg_root": reg_root,
                        "ret_current_reg_root": current_reg_root}

        result = True if reg_root.lower() in current_reg_root.lower() else False
        return result, ret_reg_root

    def check_spanning_tree_cist_root(self, output, args, **kwargs):
        cist_root = StringUtils.normalize_mac(args["root_id"])
        current_cist_root = self.pw.get_value_by_offset(output, "CIST Root", 3)
        current_cist_root = current_cist_root.replace("-", ":")

        result = True if cist_root.lower() in current_cist_root.lower() else False
        return result, {"ret_current_cist_root": current_cist_root}

    def check_cist_regional_root(self, output, args, **kwargs):
        reg_root = StringUtils.normalize_mac(args["root_id"])
        reg_root = reg_root.replace(":", "")

        current_reg_root = self.pw.get_value_by_offset(output, "CIST Regional Root", 4)
        current_reg_root = current_reg_root.replace(":", "")

        ret_reg_root = {"ret_reg_root": reg_root,
                        "ret_current_reg_root": current_reg_root}

        result = True if reg_root.lower() in current_reg_root.lower() else False
        return result, ret_reg_root

    def check_stp_port_role(self, output, args, **kwargs):
        state = args["state"].lower()
        current_state = self.pw.get_value_by_offset(output, args["port"], 4)

        if state == "designated":
            result = True if current_state[1] == "D" else False
            return result, {"ret_current_state": current_state}
        elif state == "root":
            result = True if current_state[1] == "R" else False
            return result, {"ret_current_state": current_state}
        elif state == "alternate":
            result = True if current_state[1] == "A" else False
            return result, {"ret_current_state": current_state}
        elif state == "backup":
            result = True if current_state[1] == "B" else False
            return result, {"ret_current_state": current_state}
        elif state == "master":
            result = True if current_state[1] == "M" else False
            return result, {"ret_current_state": current_state}
        else:
            self.logger.log_info("Unknown STP port state: " + state)
            return False, False

    def check_stp_port_config_type(self, output, args, **kwargs):
        config_type = args["config_type"].lower()
        current_config_type = self.pw.get_value_by_offset(output, args["port"], 4)

        if config_type == "broadcast":
            result = True if current_config_type[1] == "b" else False
            return result, {"ret_current_config_type": current_config_type}
        elif config_type == "point-to-point":
            result = True if current_config_type[1] == "p" else False
            return result, {"ret_current_config_type": current_config_type}
        elif config_type == "edge":
            result = True if current_config_type[1] == "e" else False
            return result, {"ret_current_config_type": current_config_type}
        elif config_type == "auto":
            result = True if current_config_type[1] == "a" else False
            return result, {"ret_current_config_type": current_config_type}
        else:
            self.logger.log_info("Unknown STP config type: " + config_type)
            return False, False

    def check_stp_port_restricted(self, output, args, **kwargs):
        current_state = self.pw.get_value_by_offset(output, args["port"], 4)

        result = True if current_state[1] == "B" or current_state[1] == "A" else False
        return result, {"ret_current_state": current_state}

    def check_stp_port_autoedge(self, output, args, **kwargs):
        current_port_autoedge = self.pw.get_value_by_offset(output, "Auto Edge", 3)

        result = True if current_port_autoedge == "On" else False
        return result, {"ret_current_port_autoedge": current_port_autoedge}

    def check_stp_portadmin(self, output, args, **kwargs):
        instance = "s" + args["sid"]
        current_portadmin = self.pw.get_value_by_offset(output, "Stpd: " + instance, 7)

        result = True if current_portadmin == "ENABLED" else False
        return result, {"ret_current_portadmin": current_portadmin}

    def check_stp_portadmin_oper(self, output, args, **kwargs):
        oper_portadmin = self.pw.get_value_by_offset(output, "Port Role", 7)

        result = False if oper_portadmin.lower() == "----" else True
        return result, {"ret_oper_portadmin": oper_portadmin}

    def check_stp_port_state(self, output, args, **kwargs):
        state = args["state"].lower()
        current_state = self.pw.get_value_by_offset(output, args["port"], 2)
        current_state = current_state.lower().split()

        if state in current_state:
            result = True
            self.logger.log_info("Current STP port state was NOT " + state)
        else:
            result = False

        return result, {"ret_current_state": current_state}

    def check_stp_bridge_hello_time(self, output, args, **kwargs):
        bridge_hello = self.pw.get_value_by_offset(output, "CfgBrHelloTime", 4)
        bridge_hello.replace("s", "")

        result = True if bridge_hello == args["hello_time"] else False
        return result, {"ret_bridge_hello": bridge_hello}

    def check_stp_bridge_fwd_delay(self, output, args, **kwargs):
        bridge_fwd_delay = self.pw.get_value_by_offset(output, "CfgBrForwardDelay", 6)
        bridge_fwd_delay.replace("s", "")

        result = True if bridge_fwd_delay == args["fwd_delay"] else False
        return result, {"ret_bridge_fwd_delay": bridge_fwd_delay}

    def check_stp_bridge_max_age(self, output, args, **kwargs):
        bridge_max_age = self.pw.get_value_by_offset(output, "CfgBrMaxAge", 2)
        bridge_max_age.replace("s", "")

        result = True if bridge_max_age == args["max_age"] else False
        return result, {"ret_bridge_max_age": bridge_max_age}

    def check_stp_root_hello_time(self, output, args, **kwargs):
        root_hello = self.pw.get_value_by_offset(output, "HelloTime", 5)
        root_hello.replace("s", "")

        result = True if root_hello == args["hello_time"] else False
        return result, {"ret_root_hello": root_hello}

    def check_stp_root_fwd_delay(self, output, args, **kwargs):
        root_fwd_delay = self.pw.get_value_by_offset(output, "ForwardDelay", 8)
        root_fwd_delay.replace("s", "")

        result = True if root_fwd_delay == args["fwd_delay"] else False
        return result, {"ret_root_fwd_delay": root_fwd_delay}

    def check_stp_root_max_age(self, output, args, **kwargs):
        root_max_age = self.pw.get_value_by_offset(output, "MaxAge", 2)
        root_max_age.replace("s", "")

        result = True if root_max_age == args["max_age"] else False
        return result, {"ret_root_max_age": root_max_age}

    def return_spanning_tree_config_digest(self, output, args, **kwargs):
        try:
            config_digest = self.pw.get_value_by_offset(output, "MSTP Digest", 3)
            self.logger.log_info("Config Digest: " + config_digest)
            result = True

        except ValueError:
            self.logger.log_info("Config Digest not found")
            config_digest = None
            result = False

        return result, {"ret_config_digest": config_digest}

    def check_stp_ports_link_type_is_point_to_point(self, output, args, **kwargs):
        link_type = args["link_type"].lower()
        current_link_type = self.pw.get_value_by_offset(output, args["port"], 4)

        if link_type == "point-to-point":
            if current_link_type[1] == "p":
                result = True
                return result, {"ret_current_link_type": current_link_type}

        else:
            self.logger.log_info("Unknown STP config type: " + link_type)
            result = False
            return result, {"ret_current_link_type": current_link_type}

    def check_stp_ports_link_type_is_edge(self, output, args, **kwargs):
        link_type = args["link_type"].lower()
        current_link_type = self.pw.get_value_by_offset(output, args["port"], 4)

        if link_type == "edge":
            if current_link_type[1] == "e":
                result = True
                return result, {"ret_current_link_type"}
        else:
            self.logger.log_info("Unknown STP config type: " + link_type)
            result = False
            return result, {"ret_current_link_type"}
