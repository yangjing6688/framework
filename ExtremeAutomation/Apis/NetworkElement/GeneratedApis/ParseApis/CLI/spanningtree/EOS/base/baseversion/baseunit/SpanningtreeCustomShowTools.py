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
        spanning_tree_output = self.pw.get_value_by_offset(output, "Spanning tree status", 4)
        spanning_tree_output = spanning_tree_output.split(" ")[0]

        result = True if spanning_tree_output.lower() == "enabled" else False
        return result, {"ret_spanning_tree_output", spanning_tree_output}

    def check_spanning_tree_version(self, output, args, **kwargs):
        spanning_tree_output = self.pw.get_value_by_offset(output, "Force Version", 3)

        if args["version"] == "802.1D":
            result = True if spanning_tree_output == "stpCompatible" else False
            return result, {"ret_spanning_tree_output": spanning_tree_output}
        elif args["version"] == "802.1W":
            result = True if spanning_tree_output == "rstp" else False
            return result, {"ret_spanning_tree_output": spanning_tree_output}
        elif args["version"] == "MSTP":
            result = True if spanning_tree_output == "mstp" else False
            return result, {"ret_spanning_tree_output": spanning_tree_output}

    def check_spanning_tree_bridge_priority(self, output, args, **kwargs):
        pri_result = self.pw.get_value_by_offset(output, "Designated Root Priority", 4)

        result = True if pri_result == args["priority"] else False
        return result, {"ret_pri_result": pri_result}

    def check_spanning_tree_loop_protect_enabled(self, output, args, **kwargs):
        lp_result = self.pw.get_value_by_offset(output, "Loop Protect            : ", 3)

        result = True if lp_result == "On" else False
        return result, {"ret_lp_result": lp_result}

    def check_spanning_tree_span_guard_enabled(self, output, args, **kwargs):
        sg_result = self.pw.get_value_by_offset(output, "Edge Port Safe Guard    : ", 5)

        result = True if sg_result == "Enabled" else False
        return result, {"ret_sg_result": sg_result}

    def store_spanning_tree_tc_counter(self, output, args, **kwargs):
        tc_count = self.pw.get_value_by_offset(output, "Topology Change Count", 4)
        self.value_storage.add_value(self.device.name, "tc_count", tc_count)
        self.logger.log_info("Topology Change count: " + tc_count)

        result = True if tc_count != self.constants.VALUE_NOT_PRESENT else False
        return result, {"ret_tc_count": tc_count}

    def check_spanning_tree_tc_incremented(self, output, args, **kwargs):
        tc_count_new = self.pw.get_value_by_offset(output, "Topology Change Count", 4)
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
        tc_count_new = self.pw.get_value_by_offset(output, "Topology Change Count", 4)
        tc_count_old = self.value_storage.get_value(self.device.name, "tc_count")
        self.logger.log_info("Topology Change counter: " + tc_count_new)

        ret_tc_count = {"ret_tc_new": tc_count_new,
                        "ret_tc_old": tc_count_old}

        result = True if tc_count_old == tc_count_new else False
        return result, ret_tc_count

    def check_spanning_tree_root(self, output, args, **kwargs):
        reg_root = StringUtils.normalize_mac(args["root_id"])
        current_reg_root = self.pw.get_value_by_offset(output, "Designated Root MacAddr", 4)
        current_reg_root = StringUtils.normalize_mac(current_reg_root)

        result = True if reg_root.lower() in current_reg_root.lower() else False
        return result, {"ret_current_reg_root": current_reg_root}

    def check_spanning_tree_cist_root(self, output, args, **kwargs):
        cist_root = StringUtils.normalize_mac(args["root_id"])
        current_cist_root = self.pw.get_value_by_offset(output, "Root ID", 3)
        current_cist_root = current_cist_root.replace("-", ":")

        result = True if cist_root.lower() in current_cist_root.lower() else False
        return result, {"ret_current_cist_root": current_cist_root}

    def check_cist_regional_root(self, output, args, **kwargs):
        reg_root = StringUtils.normalize_mac(args["root_id"])
        reg_root = reg_root.replace(":", "")
        current_reg_root = self.pw.get_value_by_offset(output, "Regional Root ID", 4)
        current_reg_root = current_reg_root.replace("-", "")

        ret_reg_root = {"ret_reg_root": reg_root,
                        "ret_current_reg_root": current_reg_root}

        result = True if reg_root.lower() in current_reg_root.lower() else False
        return result, ret_reg_root

    def check_instance_regional_root(self, output, args, **kwargs):
        reg_root = StringUtils.normalize_mac(args["reg_root"])
        reg_root = reg_root.replace(":", "")
        current_reg_root = self.pw.get_value_by_offset(output, "Regional Root ID", 4)
        current_reg_root = current_reg_root.replace("-", "")

        ret_reg_root = {"ret_reg_root": reg_root,
                        "ret_current_reg_root": current_reg_root}

        result = True if reg_root.lower() in current_reg_root.lower() else False
        return result, ret_reg_root

    def check_instance_root_port(self, output, args, **kwargs):
        current_root_port = self.pw.get_value_by_offset(output, "Designated Root Port", 4)

        result = True if str(current_root_port) == str(args["port"]) else False
        return result, {"ret_current_root_port": current_root_port}

    def check_stp_port_role(self, output, args, **kwargs):
        role = args["state"].lower()
        current_role = self.pw.get_value_by_offset(output, args["port"], 3)

        if role == "designated":
            result = True if current_role == "Designated" else False
            return result, {"ret_current_role": current_role}
        elif role == "root":
            current_role = self.pw.get_value_by_offset(output, "Forwarding", 3)
            result = True if current_role == "Root" else False
            return result, {"ret_current_role": current_role}
        elif role == "alternate":
            result = True if current_role == "Alternate" else False
            return result, {"ret_current_role": current_role}
        elif role == "backup":
            result = True if current_role == "Backup" else False
            return result, {"ret_current_role": current_role}
        elif role == "master":
            result = True if current_role == "Master" else False
            return result, {"ret_current_role": current_role}
        else:
            self.logger.log_info("Unknown STP port role: " + role)
            return False, False

    def check_stp_port_restricted(self, output, args, **kwargs):
        current_state = self.pw.get_value_by_offset(output, args["port"], 3)

        result = True if current_state == "Backup" or current_state == "Alternate" else False
        return result, {"ret_current_state": current_state}

    def check_stp_port_autoedge(self, output, args, **kwargs):
        current_port_autoedge = self.pw.get_value_by_offset(output, "Auto Edge", 5)

        result = True if current_port_autoedge == "enable" else False
        return result, {"ret_current_port_autoedge": current_port_autoedge}

    def check_stp_portadmin(self, output, args, **kwargs):
        current_portadmin = self.pw.get_value_by_offset(output, args["port"], 6)

        result = True if current_portadmin == "enable" else False
        return result, {"ret_current_portadmin": current_portadmin}

    def check_stp_portadmin_oper(self, output, args, **kwargs):
        oper_portadmin = self.pw.get_value_by_offset(output, "Role", 2)

        result = False if oper_portadmin == "designated" else True
        return result, {"ret_oper_portadmin": oper_portadmin}

    def check_stp_port_state(self, output, args, **kwargs):
        state = args["state"].lower()
        current_state = self.pw.get_value_by_offset(output, args["port"], 2)
        current_state = current_state.lower().split()

        if state in current_state:
            return True, True
        self.logger.log_info("Current STP port state was NOT " + state)
        return False, False

    def check_stp_bridge_hello_time(self, output, args, **kwargs):
        bridge_hello = self.pw.get_value_by_offset(output, "Bridge Hello Time", 4)

        result = True if bridge_hello == args["hello_time"] else False
        return result, {"ret_bridge_hello": bridge_hello}

    def check_stp_bridge_fwd_delay(self, output, args, **kwargs):
        bridge_fwd_delay = self.pw.get_value_by_offset(output, "Bridge Forward Delay", 4)

        result = True if bridge_fwd_delay == args["fwd_delay"] else False
        return result, {"ret_bridge_fwd_delay": bridge_fwd_delay}

    def check_stp_bridge_max_age(self, output, args, **kwargs):
        bridge_max_age = self.pw.get_value_by_offset(output, "Bridge Max Age", 4)

        result = True if bridge_max_age == args["max_age"] else False
        return result, {"ret_bridge_max_age": bridge_max_age}

    def check_stp_root_hello_time(self, output, args, **kwargs):
        root_hello = self.pw.get_value_by_offset(output, "Root Hello Time", 4)

        result = True if root_hello == args["hello_time"] else False
        return result, {"ret_root_hello": root_hello}

    def check_stp_root_fwd_delay(self, output, args, **kwargs):
        root_fwd_delay = self.pw.get_value_by_offset(output, "Root Forward Delay", 4)

        result = True if root_fwd_delay == args["fwd_delay"] else False
        return result, {"ret_root_fwd_delay": root_fwd_delay}

    def check_stp_root_max_age(self, output, args, **kwargs):
        root_max_age = self.pw.get_value_by_offset(output, "Root Max Age", 4)

        result = True if root_max_age == args["max_age"] else False
        return result, {"ret_root_max_age": root_max_age}

    def return_spanning_tree_config_digest(self, output, args, **kwargs):
        try:
            config_digest = self.pw.get_value_by_offset(output, "Configuration Digest:", 2)
            self.logger.log_info("Config Digest: " + config_digest)
            result = config_digest
            return result, {"ret_config_digest": config_digest}
        except ValueError:
            result = None
            return result, self.logger.log_info("Config Digest not found")

    def check_regional_name(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_revision_level(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
