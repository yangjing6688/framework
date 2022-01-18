from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.dot1x.base.Dot1xBaseCustomShowTools import \
    Dot1xBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return Dot1xCustomShowTools(device)


class Dot1xCustomShowTools(Dot1xBaseCustomShowTools):
    def __init__(self, device):
        super(Dot1xCustomShowTools, self).__init__(device)

    def verify_dot1x_state(self, output, args, **kwargs):
        output = output.replace(";", "")
        dot1x_state = self.pw.get_value_by_offset(output, "NetLogin Authentication Mode", 7)

        result = True if dot1x_state == "ENABLED" else False
        return result, {"ret_dot1x_state": dot1x_state}

    def check_if_dot1x_is_enabled(self, output, args, **kwargs):
        expected_value = self.pw.get_value_by_offset(output, 'NetLogin Authentication Mode', 7)

        result = True if expected_value == "ENABLED" else False
        return result, {"ret_dot1x_enabled": expected_value}

    def verify_dot1x_accounting_state(self, output, args, **kwargs):
        output = output.replace(";", "")
        dot1x_acct_state = self.pw.get_value_by_offset(output, 'RADIUS Accounting', 3)

        result = True if dot1x_acct_state == "On" else False
        return result, {"ret_accounting_state": dot1x_acct_state}

    def check_if_dot1x_accounting_is_enabled(self, output, args, **kwargs):
        expected_value = self.pw.get_value_by_offset(output, 'RADIUS Accounting', 3)

        result = True if expected_value == "On" else False
        return result, {"ret_accounting_enabled": expected_value}

    def verify_dot1x_is_enabled_on_port(self, output, args, **kwargs):
        port_state = self.pw.get_value_by_offset(output, "enable netlogin ports", 3).split(" ")
        port_modes = self.pw.get_value_by_offset(output, "enable netlogin ports", 4).split(" ")

        result = False

        for i, mode in enumerate(port_modes):
            if mode == "dot1x":
                result = self.it.compare_port_values(port_state[i], args["port"], self.inspect_constants.CONTAINS)
        return result, {"ret_port_state": port_state,
                        "ret_port_modes": str(port_modes)}

    def verify_dot1x_quiet_period(self, output, args, **kwargs):
        quietperiod = self.pw.get_value_by_offset(output, "Quiet Period", 3)

        result = True if quietperiod == args["quiet_period"] else False
        return result, {"ret_quiet_period": quietperiod}

    def verify_dot1x_port_reauth_period(self, output, args, **kwargs):
        conf_interval = self.pw.get_value_by_offset(output, args["port"] + " timers reauth-period", 7)
        if conf_interval.lower() == "valuenotpresent":
            conf_interval = "3600"

        result = True if args["interval"] == conf_interval else False
        return result, {"ret_port_reauth_period": conf_interval}

    def verify_dot1x_reauth_period(self, output, args, **kwargs):
        reauthperiod = self.pw.get_value_by_offset(output, "Re-authentication period", 3)

        result = True if reauthperiod == args["reauth_period"] else False
        return result, {"ret_reauth_period": reauthperiod}

    def verify_dot1x_port_reauth_state(self, output, args, **kwargs):
        reauth_state = self.pw.get_value_by_offset(output, args["port"] + " timers reauthentication", 7)
        if reauth_state.lower() == "valuenotpresent":
            reauth_state = "off"

        result = True if reauth_state == "on" else False
        return result, {"ret_reauth_state": reauth_state}

    def verify_dot1x_supp_response_timeout(self, output, args, **kwargs):
        suppresptimeout = self.pw.get_value_by_offset(output, "Supplicant Response Timeout", 4)

        result = True if suppresptimeout == args["supp_resp_timeout"] else False
        return result, {"ret_supp_response_timeout": suppresptimeout}

    def verify_dot1x_server_timeout(self, output, args, **kwargs):
        servertimeout = self.pw.get_value_by_offset(output, "RADIUS server timeout", 4)

        result = True if servertimeout == args["server_timeout"] else False
        return result, {"ret_server_timeout": servertimeout}

    def verify_dot1x_idle_timeout(self, output, args, **kwargs):
        idletimeout = self.pw.get_value_by_offset(output, "Idle Timeout", 3)

        result = True if idletimeout == args["idle_timeout"] else False
        return result, {"ret_idle_timeout": idletimeout}

    def verify_global_dot1x_idle_timeout(self, output, args, **kwargs):
        idletimeout = self.pw.get_value_by_offset(output, "dot1x", 1)

        result = True if idletimeout == args["idle_timeout"] else False
        return result, {"ret_global_idle_timeout": idletimeout}

    def verify_dot1x_session_timeout(self, output, args, **kwargs):
        sessiontimeout = self.pw.get_value_by_offset(output, "Session Timeout", 3)

        result = True if sessiontimeout == args["session_timeout"] else False
        return result, {"ret_session_timeout": sessiontimeout}

    def verify_global_dot1x_session_timeout(self, output, args, **kwargs):
        sessiontimeout = self.pw.get_value_by_offset(output, "dot1x", 1)

        result = True if sessiontimeout == args["seconds"] else False
        return result, {"ret_global_session_timeout": sessiontimeout}

    def check_if_dot1x_user_is_authenticated(self, output, args, **kwargs):
        auth_status = self.pw.get_value_by_offset(output, args["mac_or_ip_or_user"], 2)

        result = True if auth_status == "yes" else False
        return result, {"ret_user_auth": auth_status}

    def check_if_dot1x_user_is_unauthenticated(self, output, args, **kwargs):
        auth_status = self.pw.get_value_by_offset(output, args["mac_or_ip_or_user"], 2)

        result = True if auth_status == "no" else False
        return result, {"ret_user_unauth": auth_status}

    def check_if_dot1x_user_is_authenticated_by_radius(self, output, args, **kwargs):
        auth_status = self.pw.get_value_by_offset(output, args["mac_or_ip_or_user"], 2)
        auth_agent = self.pw.get_value_by_offset(output, args["mac_or_ip_or_user"], 3)

        result = False
        if auth_status == "yes" and auth_agent == "radius":
            result = True
        return result, {"ret_auth_status": auth_status,
                        "ret_auth_agent": auth_agent}

    def check_if_dot1x_user_login_name_is_correct(self, output, args, **kwargs):
        username = self.pw.get_value_by_offset(output, args["mac_or_ip_or_user"], 6)

        result = True if username == args["login_name"] else False
        return result, {"ret_login_name": username}

    def check_if_dot1x_user_ip_is_correct(self, output, args, **kwargs):
        user_ip = self.pw.get_value_by_offset(output, args["mac_or_ip_or_user"], 1)

        result = True if user_ip == args["ip"] else False
        return result, {"ret_user_ip": user_ip}
