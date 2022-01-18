"""
Keyword class for all logging cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.LoggingConstants import \
    LoggingConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.LoggingConstants import \
    LoggingConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementLoggingGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementLoggingGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "logging"

    def logging_clear_log(self, device_name, **kwargs):
        """
        Description: Clears the logging buffer/file.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LOG,
                                    **kwargs)

    def logging_clear_log_auditlog(self, device_name, **kwargs):
        """
        Description: Clears the auditlog buffer/file.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LOG_AUDITLOG,
                                    **kwargs)

    def logging_clear_log_raslog(self, device_name, **kwargs):
        """
        Description: Clears the raslog buffer/file.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LOG_RASLOG,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def logging_verify_string_in_log(self, device_name, string='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [string]      - The string expected to be in the logging output.

        Verifies the given string(s) are present in the log output.
        """
        args = {"string": string}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOG,
                                           self.parse_const.CHECK_STRING_IN_OUTPUT, True,
                                           "The expected string: {string} was present in the log.",
                                           "The expected string: {string} was NOT present in the log!",
                                           **kwargs)

    def logging_verify_regex_in_log(self, device_name, regex='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [regex]       - The string expected to be in the logging output.

        Verifies the given string(s) are present in the log output.
        """
        args = {"regex": regex}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOG,
                                           self.parse_const.CHECK_REGEX_IN_OUTPUT, True,
                                           "The expected string: {regex} was present in the log.",
                                           "The expected string: {regex} was NOT present in the log!",
                                           **kwargs)
