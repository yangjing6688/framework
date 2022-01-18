from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.webauth.base.WebauthBaseCustomShowTools import \
    WebauthBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
import time
import datetime


def create_instance(device):
    return WebauthCustomShowTools(device)


class WebauthCustomShowTools(WebauthBaseCustomShowTools):
    def __init__(self, device):
        super(WebauthCustomShowTools, self).__init__(device)

    def check_webauth_enabled(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'netlogin authentication mode', 5)

        result = res == "enabled"
        return result, {"ret_state": res}

    def verify_webauth_port_state(self, output, args, **kwargs):
        port_state = self.pw.get_value_by_offset(output, "enable netlogin ports", 3).split(" ")
        port_modes = self.pw.get_value_by_offset(output, "enable netlogin ports", 4).split(" ")

        result = False
        state = None
        for i, mode in enumerate(port_modes):
            if mode == "web-based":
                state = port_state[i]
                if self.it.compare_port_values(port_state[i], args["port"], self.inspect_constants.CONTAINS):
                    result = True
        return result, {"ret_port_state": state}

    def check_webauth_base_url_exists(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'base-url', 2)

        result = res == args["base_url"]
        return result, {"ret_url_name": res}

    def check_webauth_base_url_default(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'base-url', 2)

        result = res == "network-access.com"
        return result, {"ret_url_name": res}

    def check_webauth_lease_time(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'netlogin lease timer', 4)
        result = False
        if res.isdigit() and args["seconds"].isdigit():
            result = int(res) == int(args["seconds"])

        return result, {"ret_lease_time": res}

    def check_webauth_redirect_enabled(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'default-redirect-page', 2)

        result = res == "enabled"
        return result, {"ret_redirect_state": res}

    def check_webauth_session_timeout(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'web-based', 1)
        result = False
        if res.isdigit() and args["seconds"].isdigit():
            result = int(res) == int(args["seconds"])

        return result, {"ret_session_timeout": res}

    def check_webauth_idle_timeout(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'web-based', 2)
        result = False
        if res.isdigit() and args["seconds"].isdigit():
            result = int(res) == int(args["seconds"])

        return result, {"ret_idle_timeout": res}

    def check_webauth_session_timeout_default(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'web-based', 1)
        result = False
        if res.isdigit():
            result = int(res) == 0

        return result, {"ret_session_timeout": res}

    def check_webauth_idle_timeout_default(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'web-based', 2)
        result = False
        if res.isdigit():
            result = int(res) == 300

        return result, {"ret_idle_timeout": res}

    def check_webauth_user_authenticated(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), args["mac_or_ip_or_user"], 2)

        return res == "yes", {"ret_user_auth": res}

    def check_webauth_user_unauthenticated(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), args["mac_or_ip_or_user"], 2)

        return res == "no", {"ret_user_auth": res}

    def check_webauth_user_authenticated_radius(self, output, args, **kwargs):
        user_auth = self.pw.get_value_by_offset(output.lower(), args["mac_or_ip_or_user"], 2)
        auth_type = self.pw.get_value_by_offset(output.lower(), args["mac_or_ip_or_user"], 3)

        result = user_auth == "yes" and auth_type == "radius"
        return result, {"ret_user_auth": user_auth,
                        "ret_auth_type": auth_type}

    def check_webauth_user_login_name(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), args["mac_or_ip_or_user"], 6)

        return res == args["login_name"], {"ret_login_name": res}

    def check_webauth_user_ip(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), args["mac_or_ip_or_user"], 1)

        return res == args["ip"], {"ret_user_ip": res}

    def check_webauth_user_authenticated_auth_type(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), args["mac_or_ip_or_user"], 4)

        return res == args["auth_type"], {"ret_auth_type": res}

    def check_webauth_database_order_radius(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'authentication database', 3)

        return res == "radius", {"ret_db_order": res}

    def check_webauth_database_order_radius_local(self, output, args, **kwargs):
        type_radius = self.pw.get_value_by_offset(output.lower(), 'authentication database', 3)
        type_local = self.pw.get_value_by_offset(output.lower(), 'authentication database', 4)

        result = type_radius == "radius" and type_local == "local-user"
        return result, {"ret_db_order": type_radius + " " + type_local}

    def check_webauth_database_order_local(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'authentication database', 3)

        return res == "local-user", {"ret_db_order": res}

    def check_webauth_database_order_local_radius(self, output, args, **kwargs):
        type_local = self.pw.get_value_by_offset(output.lower(), 'authentication database', 3)
        type_radius = self.pw.get_value_by_offset(output.lower(), 'authentication database', 5)

        result = type_local == "local-user" and type_radius == "radius"
        return result, {"ret_db_order": type_local + " " + type_radius}

    def check_webauth_protocol_order(self, output, args, **kwargs):
        order = args["order"].split()

        order0 = self.pw.get_value_by_offset(output.lower(), 'authentication protocol order', 3)
        order1 = self.pw.get_value_by_offset(output.lower(), 'authentication protocol order', 4)
        order2 = self.pw.get_value_by_offset(output.lower(), 'authentication protocol order', 5)

        result = order0 == order[0] and order1 == order[1] and order2 == order[2]
        return result, {"ret_protocol_order": " ".join([order0, order1, order2])}

    def check_webauth_redirect_page_enabled(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'default-redirect-page', 2)

        return res == "enabled", {"ret_redirect_page_state": res}

    def check_webauth_redirect_page_disabled(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'default-redirect-page', 2)

        return res == "disabled", {"ret_redirect_page_state": res}

    def check_webauth_redirect_page(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'default-redirect-page', 3)

        return res == args["address"], {"ret_redirect_page": res}

    def check_webauth_reauthenticate_on_refresh_enabled(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'reauthenticate on refresh', 3)

        return res == "enabled", {"ret_reauthentication_state": res}

    def check_webauth_reauthenticate_on_refresh_disabled(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'reauthenticate on refresh', 3)

        return res == "disabled", {"ret_reauthentication_state": res}

    def check_webauth_redirect_page_default(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'default-redirect-page', 3)

        return res == "http://www.extremenetworks.com", {"ret_redirect_page": res}

    def check_webauth_session_refresh_interval(self, output, args, **kwargs):
        output = output.replace(";", "")
        minutes = self.pw.get_value_by_offset(output, "Netlogin Session-Refresh", 4)
        seconds = self.pw.get_value_by_offset(output, "Netlogin Session-Refresh", 6)

        result = False
        try:
            x_int = minutes + ":" + seconds
            x = time.strptime(x_int, "%M:%S")
            current = datetime.timedelta(minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

            if args["interval"].isdigit():
                result = int(current) == int(args["interval"])
        except ValueError:
            current = "valueNotPresent"
        return result, {"ret_session_refresh_interval": str(current)}

    def check_webauth_session_refresh_enabled(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'netlogin session-refresh', 3)

        return res == "enabled", {"ret_session_refresh": res}

    def check_webauth_session_refresh_disabled(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'netlogin session-refresh', 3)

        return res == "disabled", {"ret_session_refresh": res}

    def check_webauth_allowed_refresh_failures(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'refresh failures allowed', 4)

        return res == args["num_failures"], {"ret_allowed_failures": res}

    def check_webauth_session_refresh_default(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'netlogin session-refresh', 4)

        result = False
        if res.isdigit():
            result = int(res) == 3

        return result, {"ret_session_refresh": res}

    def check_webauth_allowed_refresh_failures_default(self, output, args, **kwargs):
        res = self.pw.get_value_by_offset(output.lower(), 'refresh failures allowed', 4)

        result = False
        if res.isdigit():
            result = int(res) == 0

        return result, {"ret_allowed_failures": res}
