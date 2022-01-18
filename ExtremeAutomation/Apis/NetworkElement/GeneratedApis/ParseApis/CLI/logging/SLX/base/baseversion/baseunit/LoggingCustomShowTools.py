from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.logging.base.LoggingBaseCustomShowTools import \
    LoggingBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class LoggingCustomShowTools(LoggingBaseCustomShowTools):
    def __init__(self, device):
        super(LoggingCustomShowTools, self).__init__(device)

    def check_string_in_output(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_regex_in_output(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
