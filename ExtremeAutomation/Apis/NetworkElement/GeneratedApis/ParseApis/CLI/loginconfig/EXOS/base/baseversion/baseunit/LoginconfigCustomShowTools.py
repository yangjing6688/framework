from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.loginconfig.base.LoginconfigBaseCustomShowTools \
    import LoginconfigBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return LoginconfigCustomShowTools(device)


class LoginconfigCustomShowTools(LoginconfigBaseCustomShowTools):
    def __init__(self, device):
        super(LoginconfigCustomShowTools, self).__init__(device)

    def verify_login_exists(self, output, args, **kwargs):
        if args["access_level"] is None:
            return args["username"] in output
        else:
            login_access_level = self.pw.get_value_by_offset(output, args["username"], 1)

        if login_access_level.lower() == "r/w":
            login_access_level = ["read_write", "read/write", "r/w", "rw"]
        elif login_access_level.lower() == "ro":
            login_access_level = ["read_only", "read/only", "r/o", "ro"]

        result = True if args["access_level"].lower() in login_access_level else False

        return result, {"ret_access_lvl": login_access_level}

    def verify_admin_login_exists(self, output, args, **kwargs):
        result = self.pw.get_value_by_offset(output, 'R/W', 0)

        result1 = True if args["username"] in result else False

        return result1, {"ret_admin": result}

    def verify_admin_login_does_not_exist(self, output, args, **kwargs):
        result = self.pw.get_value_by_offset(output, 'R/W', 0)

        result1 = True if args["username"] in result else False

        return result1, {"ret_admin": result}

    def verify_login_user_authentication_method(self, output, args, **kwargs):
        result = self.pw.get_value_range(output, args["username"], "Cli Auth")

        result1 = True if args["auth_method"].lower() in result.lower() else False

        return result1, {"ret_admin": result}

    def check_total_failed_login_attempts(self, output, args, **kwargs):
        value = self.pw.get_value_by_offset(output.lower(), args["username"], 3)
        result = True if value == args["login_attempts"] else False
        return result, {"ret_logins": value}

    def check_failed_login_attempts_since_success(self, output, args, **kwargs):
        value = self.pw.get_value_by_offset(output.lower(), args["username"], 4)
        result = True if value == args["login_attempts"] else False
        return result, {"ret_logins": value}

    def check_successful_login_attempts(self, output, args, **kwargs):
        value = self.pw.get_value_by_offset(output.lower(), args["username"], 2)
        result = True if value == args["login_attempts"] else False
        return result, {"ret_logins": value}

    def check_password_max_age(self, output, args, **kwargs):
        if "-" in self.pw.get_value_by_offset(output, args["username"], 1):
            value = self.pw.get_value_by_offset(output, args["username"], 2)
        else:
            value = self.pw.get_value_by_offset(output, args["username"], 1)
        result = True if value == args["age"] else False
        return result, {"ret_age": value}

    def check_password_min_age(self, output, args, **kwargs):
        full_line = self.pw.get_value_from_string_to_eol(output, args["username"])
        full_line = full_line.strip().split()
        line_length = len(full_line)
        value = self.pw.get_value_by_offset(output, args["username"], line_length - 6)
        result = True if value == args["age"] else False
        return result, {"ret_age": value}

    def check_password_min_diff_char(self, output, args, **kwargs):
        full_line = self.pw.get_value_from_string_to_eol(output, args["username"])
        full_line = full_line.strip().split()
        line_length = len(full_line)
        value = self.pw.get_value_by_offset(output, args["username"], line_length - 4)
        result = True if value == args["min_diff_chars"] else False
        return result, {"ret_mindiffchar": value}

    def check_password_min_length(self, output, args, **kwargs):
        full_line = self.pw.get_value_from_string_to_eol(output, args["username"])
        full_line = full_line.strip().split()
        line_length = len(full_line)
        value = self.pw.get_value_by_offset(output, args["username"], line_length - 5)
        result = True if value == args["length"] else False
        return result, {"ret_length": value}
