from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.JsonUtils import JsonUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.ParsingHelper.ParserWrapper import ParserWrapper
from ExtremeAutomation.Keywords.Utils.DeviceValueStorage import DeviceValueStorage
from ExtremeAutomation.Library.ParsingHelper.InspectionConstants import InspectionConstants
from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class BaseShowApi(object):
    def __init__(self):
        self.value_storage = DeviceValueStorage()
        self.logger = Logger()
        self.cmd_obj_constants = CommandObjectConstants()
        self.constants = NetworkElementConstants()
        self.inspect_constants = InspectionConstants()
        self.pw = ParserWrapper()
        self.str_utils = StringUtils()

    def _validate_json_output(self, rest_return_text, expected_values, exact_match):
        result = None

        if isinstance(expected_values, str):
            expected_values = StringUtils.format_json_output(expected_values)

        for key in expected_values.keys():
            if JsonUtils.search_json(rest_return_text, key, expected_values[key], exact_match):
                self.logger.log_info("Found: {" + str(key) + ": " + str(expected_values[key]) + "}")

                if result is None:
                    result = True
            else:
                self.logger.log_info("Not found: {" + str(key) + ": " + str(expected_values[key]) + "}")
                result = False
        return result

    def _regex_validate_json_output(self, rest_return_text, expected_values):
        result = None

        if isinstance(expected_values, str):
            expected_values = StringUtils.format_json_output(expected_values)

        for key in expected_values.keys():
            if JsonUtils.search_json_regex(rest_return_text, key, expected_values[key]):
                self.logger.log_info("Found: {" + str(key) + ": " + str(expected_values[key]) + "}")

                if result is None:
                    result = True
            else:
                self.logger.log_info("Not found: {" + str(key) + ": " + str(expected_values[key]) + "}")
                result = False
        return result


class NorthboundResults(object):
    def __init__(self):
        self.result_list = []
        self.result = True
        self.logger = Logger()

    def add_result(self, received, expected):
        """
        This function adds a new result to the result_list.

        It checks the received value against the expected value and adds an appropriate message.
        If they two values do not match it sets the result flag to False.
        """
        if received is None:
            received = 'None'

        if received == expected:
            self.result_list.append("Received: " + str(received) + " == Expected: " + expected)
        else:
            self.result_list.append("Received: " + str(received) + " != Expected: " + expected)
            if self.result:
                self.result = False

    def return_result(self):
        """
        This function logs all results in the result_list and returns the value of result.
        """
        self.log_results()
        return self.result

    def log_results(self):
        """
        This function logs the result list with a new line between each item.
        """
        self.logger.log_info("\n".join(self.result_list))
