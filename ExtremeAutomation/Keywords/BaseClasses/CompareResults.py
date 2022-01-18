from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants


class CompareResults(object):
    def __init__(self, command_obj=None):
        self.logger = Logger()

        if command_obj is not None:
            self.command = command_obj.command
            self.output = command_obj.return_text
            self.cli_error_code = command_obj.error_state
            self.cli_error_output = command_obj.error_text

    def compare_results(self, result, expected_result):
        """
        This function first checks if the result is not supported, if it is a message is logged.
        Then we compare the results and return a boolean.
        """
        if result == CommandObjectConstants.METHOD_NOT_SUPPORTED:
            self.logger.log_info("Keyword not supported.")
        return result == expected_result
