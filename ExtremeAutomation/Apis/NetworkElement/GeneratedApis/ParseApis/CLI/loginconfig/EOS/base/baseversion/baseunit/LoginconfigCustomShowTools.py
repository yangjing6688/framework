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
        result = args["username"] in output
        return result, result

    def verify_admin_login_exists(self, output, args, **kwargs):
        result = self.pw.get_value_by_offset(output, 'super-user', 0)

        result1 = True if args["username"] in result else False

        return result1, {"ret_admin": result}

    def verify_admin_login_does_not_exist(self, output, args, **kwargs):
        table = str.maketrans(dict.fromkeys('[]'))
        output = output.translate(table)
        result = self.pw.get_value_by_offset(output, 'super-user', 0)

        result1 = True if args["username"] in result else False

        return result1, {"ret_admin": result}
