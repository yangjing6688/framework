from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.hostutils.base.HostutilsBaseCustomShowTools \
    import HostutilsBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.Constants.LicenseServerConstants import LicenseServerConstants
from ExtremeAutomation.Library.Device.Common.Agents.RestAgent import RestAgent
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Library.Device.EndsystemElement.EndsystemElement import EndsystemElement
import re


class HostutilsCustomShowTools(HostutilsBaseCustomShowTools):
    def __init__(self, device):
        super(HostutilsCustomShowTools, self).__init__(device)

    def check_ping_result(self, output, args, **kwargs):
        host = self.pw.get_value_by_offset(output, args["host_address"], 3)

        result = True if args["host_address"] in host else False
        return result, result

    def check_debug_login(self, output, args, **kwargs):
        challenge = "EXOS version" + self.pw.get_value_range(output, "EXOS version", "==") + "=="
        challenge_dict = {"mode": "debug",
                          "challenge": challenge.replace("\r", "").replace("\n", "")}

        rest_server = EndsystemElement(self.constants.OS_LINUX, self.constants.PLATFORM_BASE,
                                       self.constants.UNIT_BASE, self.constants.VERSION_BASE)
        rest_server.hostname = LicenseServerConstants.CHALLENGE_SERVER
        rest_server.port = LicenseServerConstants.CHALLENGE_SERVER_PORT
        rest = RestAgent(rest_server)
        rest_cmd = RestCommandObject()
        rest_cmd.request_type = "post"
        rest_cmd.uri = LicenseServerConstants.CHALLENGE_URI
        rest_cmd.data = challenge_dict
        rest_response = rest.send_command_object(rest_cmd)
        response = rest_response.return_text["key"]

        return (True, response) if challenge != "valuenotpresent" else (False, None)

    def check_debug_login_enabled(self, output, args, **kwargs):
        result = "debug" in output
        return result, result

    def check_failed_login_attempts(self, output, args, **kwargs):
        expected_fails = args["login_attempts"]
        check_string = "and " + expected_fails + " failed logins since"
        response_string = self.pw.get_value_by_offset(output, "failed logins since", 10)
        result = check_string in output
        return result, response_string

    def check_last_login_date(self, output, args, **kwargs):
        expected_date_regex = r"[a-zA-Z]+ [a-zA-Z]+\s*\d+ \d\d:\d\d:\d\d \d{4}"
        response_string = self.pw.get_value_by_offset(output, "Last Successful Login was", 5)
        response_string += " " + self.pw.get_value_by_offset(output, "Last Successful Login was", 6)
        response_string += " " + self.pw.get_value_by_offset(output, "Last Successful Login was", 7)
        response_string += " " + self.pw.get_value_by_offset(output, "Last Successful Login was", 8)
        response_string += " " + self.pw.get_value_by_offset(output, "Last Successful Login was", 9)
        result = bool(re.search(expected_date_regex, output))
        return result, response_string

    def check_logout_message_exists(self, output, args, **kwargs):
        result = True if "Session has been terminated" in output else False
        return result, output

    def check_successful_login_attempts(self, output, args, **kwargs):
        expected_successes = args["login_attempts"]
        check_string = "There have been " + expected_successes + " successful logins since last reboot"
        response_string = self.pw.get_value_by_offset(output, "failed logins since", 3)
        result = check_string in output
        return result, response_string
