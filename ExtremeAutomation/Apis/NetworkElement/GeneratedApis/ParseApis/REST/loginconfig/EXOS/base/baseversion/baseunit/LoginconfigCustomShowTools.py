from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.loginconfig.base.\
    LoginconfigBaseCustomShowTools import LoginconfigBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return LoginconfigCustomShowTools(device)


class LoginconfigCustomShowTools(LoginconfigBaseCustomShowTools):
    def __init__(self, device):
        super(LoginconfigCustomShowTools, self).__init__(device)

    def verify_login_exists(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)
        login_access_level = None
        found_level = None
        name = None

        for i in range(1, len(output["result"])):
            try:
                name = output["result"][i]["account"]["name"]

                if name == args["account_name"]:
                    login_access_level = output["result"][i]["account"]["readwrite"]

                    if login_access_level == 1:
                        login_access_level = "r/w"
                    else:
                        login_access_level = "ro"
                    found_level = login_access_level
                    break

            except AttributeError:
                pass

        if args["access_level"] is not None:
            if login_access_level.lower() == "r/w":
                login_access_level = ["read_write", "read/write", "r/w", "rw"]
            elif login_access_level.lower() == "ro":
                login_access_level = ["read_only", "read/only", "r/o", "ro"]

            result = True if args["access_level"].lower() in login_access_level else False
        else:
            if login_access_level is None:
                result = False
            else:
                result = True

        return result, {"ret_login": name,
                        "ret_level": found_level}
