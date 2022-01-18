from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.rsmlt.base.RsmltBaseCustomShowTools import \
    RsmltBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class RsmltCustomShowTools(RsmltBaseCustomShowTools):
    def __init__(self, device):
        super(RsmltCustomShowTools, self).__init__(device)

    def verify_rsmlt_edge_support_enabled(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output, "rsmlt-peer-forwarding", 2)

        result = True if state == "enable" else False
        return result, {"ret_edge_support_state": state}

    def verify_rsmlt_edge_support_disabled(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output, "rsmlt-peer-forwarding", 2)

        result = True if state == "disable" else False
        return result, {"ret_edge_support_state": state}

    def verify_rsmlt_enabled_on_interface_vlan(self, output, args, **kwargs):
        output = output.lower()
        enabled = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["interface"]:
                    enabled = line.split()[3]

                    break
        result = True if enabled == "enable" else False
        return result, {"ret_state": enabled}

    def verify_rsmlt_disabled_on_interface_vlan(self, output, args, **kwargs):
        output = output.lower()
        disabled = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["interface"]:
                    disabled = line.split()[3]
                    break
        result = True if disabled == "disable" else False
        return result, {"ret_state": disabled}

    def verify_rsmlt_holddown_timer_is_set(self, output, args, **kwargs):
        output = output.lower()
        timer = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["interface"]:
                    timer = line.split()[5]
                    break
        result = True if timer == args["timer"] else False
        return result, {"ret_holddown_timer": timer}

    def verify_rsmlt_holdup_timer_is_set(self, output, args, **kwargs):
        output = output.lower()
        timer = None
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == args["interface"]:
                    timer = line.split()[6]
                    break
        result = True if timer == args["timer"] else False
        return result, {"ret_holddown_timer": timer}
