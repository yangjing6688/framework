from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.macauth.base.MacauthBaseCustomShowTools import \
    MacauthBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return MacauthCustomShowTools(device)


class MacauthCustomShowTools(MacauthBaseCustomShowTools):
    def __init__(self, device):
        super(MacauthCustomShowTools, self).__init__(device)

    def verify_macauth_state(self, output, args, **kwargs):
        output = output.replace(";", "")
        mac_state = self.pw.get_value_by_offset(output, "NetLogin Authentication Mode", 9)

        result = True if mac_state == "ENABLED" else False
        return result, {"ret_state": mac_state}

    def verify_macauth_port_state(self, output, args, **kwargs):
        port_state = self.pw.get_value_by_offset(output, "enable netlogin ports", 3).split(" ")
        port_modes = self.pw.get_value_by_offset(output, "enable netlogin ports", 4).split(" ")

        result = False
        ret_state = None

        for i, mode in enumerate(port_modes):
            if mode == "mac":
                ret_state = port_state[i]
                result = self.it.compare_port_values(port_state[i], args["port"], self.inspect_constants.CONTAINS)

        return result, {"ret_port_state": ret_state}

    def verify_macauth_reauth_period(self, output, args, **kwargs):
        current_period = self.pw.get_value_by_offset(output, "Re-authentication period", 3)

        result = True if args["interval"] == current_period else False
        return result, {"ret_reauth_period": current_period}

    def verify_macauth_port_reauth_period(self, output, args, **kwargs):
        config_line = "netlogin mac ports " + args["port"] + " timers reauth-period"
        found_interval = self.pw.get_value_by_offset(output, config_line, 7)

        result = True if found_interval == args["interval"] else False
        return result, {"ret_port_reauth_period": found_interval}

    def verify_macauth_port_reauth_state(self, output, args, **kwargs):
        config_line = "netlogin mac ports " + args["port"] + " timers reauthentication"
        found_state = self.pw.get_value_by_offset(output, config_line, 7)

        result = True if found_state == "on" else False
        return result, {"ret_port_reauth_state": found_state}

    def verify_macauth_port_reauth_delay(self, output, args, **kwargs):
        config_line = "netlogin mac ports " + args["port"] + " timers delay"
        found_delay = self.pw.get_value_by_offset(output, config_line, 7)

        result = True if found_delay == args["interval"] else False
        return result, {"ret_port_reauth_delay": found_delay}

    def verify_macauth_mac_list_members(self, output, args, **kwargs):
        result = self.pw.is_exact_string_present_in_output(output, args["mac_addr"] + "/" + args["mask"])
        return result, result
