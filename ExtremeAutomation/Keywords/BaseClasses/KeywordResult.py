from ExtremeAutomation.Library.Logger.Logger import Logger


class KeywordResult(object):
    def __init__(self, device_name, test_result, pass_string, fail_string, cmd_obj):
        self.device_name = device_name
        self.test_result = test_result
        self.pass_string = pass_string
        self.fail_string = fail_string
        self.logger = Logger()
        self.cmd_obj = cmd_obj
        try:
            self.return_text = self.cmd_obj._return_text
        except Exception:
            self.return_text = ""

        try:
            self.command = cmd_obj.command if cmd_obj.command else "N/A"
        except AttributeError:
            self.command = "N/A"

    def print_kw_result(self):
        """
        This function builds a log message based on a given keyword result and
        then writes it to the log.
        """
        if self.test_result:
            message = self.pass_string
            test_result = "Pass"
        else:
            if self.cmd_obj != None:
                message = self.fail_string + self.cmd_obj.return_text
            else:
                message = self.fail_string
            test_result = "Fail"
        kw_result = str("\n" + "Device Name: " + str(self.device_name) + "\n" +
                        "Command Sent: " + str(self.command) + "\n" +
                        "Result: " + test_result + "\n" +
                        "Message: " + message)

        self.logger.log_info(kw_result)
        return kw_result
