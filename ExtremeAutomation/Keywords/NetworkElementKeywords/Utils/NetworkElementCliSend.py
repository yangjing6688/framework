import re
import time
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult
from ExtremeAutomation.Library.ParsingHelper.ParserWrapper import ParserWrapper
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass \
    import NetworkElementKeywordBaseClass


class NetworkElementCliSend(NetworkElementKeywordBaseClass):
    # +-------------------+
    # | CLI Send Keywords |
    # +-------------------+
    def send_cmd(self, device_name, command, **kwargs):
        """
        Keyword Arguments:
            device_name - The name of the device the keyword should be run against.
            command - The command that should be sent to the device.

        Sends the given command to a device and logs the output.
        """
        
        dev, _, _ = self._init_keyword(device_name, **kwargs)
        cmd_obj = self.__send_command(dev, command, **kwargs)
        kw_result = self._determine_result(dev, cmd_obj, **kwargs)
        return self._keyword_cleanup([kw_result])

    def send_cmd_verify_output(self, device_name, command, expected_output, ignore_whitespace=True, ignore_case=True,
                               **kwargs):
        """
        Keyword Arguments:
            device_name - The name of the device the keyword should be run against.
            command - The command that should be sent to the device.
            expected_output - The string that must be present in the output for the keyword to pass.
            ignore_whitespace - A boolean flag indicating whether or not white space should be ignored.
            ignore_case - A boolean flag indicating whether or not case should be ignored.

        Optional Arguments:
            exists - [Default True] - This is a boolean flag that indicates whether the output should exist or not.
            max_wait - [Default 0] - This is an integer that indicates how long the keyword should wait before
                                     failing.
            interval - [Default 1] - This is the sleep duration between retry attempts while waiting for the expected
                                     output.

        Sends the given command to a device and then verifies that <expected_output> is
        in the command's output.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)
        cmd_obj = self.__send_command(dev, command, **kwargs)
        result = self.__check_output(cmd_obj, expected_output, ignore_whitespace, ignore_case, **kwargs)

        start = time.time()
        max_wait = self.get_max_wait(**kwargs)
        interval = self.get_interval(**kwargs)

        while time.time() - start < max_wait and not result:
            cmd_obj = self.__send_command(dev, command, **kwargs)
            result = self.__check_output(cmd_obj, expected_output, ignore_whitespace, ignore_case, **kwargs)
            if not result:
                time.sleep(interval)

        kw_result = self._determine_result(dev, cmd_obj, result, True, "CLI send passed.", "CLI send failed.", **kwargs)
        return self._keyword_cleanup([kw_result])

    def send_cmd_verify_output_regex(self, device_name, command, regex, **kwargs):
        """
        Keyword Arguments:
            device_name - The name of the device the keyword should be run against.
            command - The command that should be sent to the device.
            regex - The regular expression that will be run against the output. The keyword
                    will pass if any matches are returned, otherwise it will fail.

        Optional Arguments:
            exists - [Default True] - This is a boolean flag that indicates whether the output should exist or not.
            max_wait - [Default 0] - This is an integer that indicates how long the keyword should wait before
                                     failing.
            interval - [Default 1] - This is the sleep duration between retry attempts while waiting for the expected
                                     output.

        Sends the given command to a device and then verifies that <regex> returns at least 1 match
        when run against the command's output.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)
        valid_regex, compiled_regex = self.__check_regex(regex)

        if valid_regex:
            cmd_obj = self.__send_command(dev, command, **kwargs)
            result = self.__check_output(cmd_obj, compiled_regex, False, False, regex=True, **kwargs)

            start = time.time()
            max_wait = self.get_max_wait(**kwargs)
            interval = self.get_interval(**kwargs)

            while time.time() - start < max_wait and not result:
                cmd_obj = self.__send_command(dev, command, **kwargs)
                result = self.__check_output(cmd_obj, compiled_regex, False, False, regex=True, **kwargs)
                if not result:
                    time.sleep(interval)

            kw_result = self._determine_result(dev, cmd_obj, result, True, "CLI send passed.", "CLI send failed.",
                                               **kwargs)
        else:
            kw_result = KeywordResult(device_name, valid_regex, "CLI send passed.", regex + " is not valid regex.",
                                      None)
        return self._keyword_cleanup([kw_result])

    def send_cmd_verify_output_table(self, device_name, command, row, column, expected_value, ignore_case=False,
                                     **kwargs):
        """
        Keyword Arguments:
            device_name - The name of the device the keyword should be run against.
            command - The command that should be sent to the device.
            row - An integer value indicating which row in the output to check.
            column - An integer value indicating which column in the output to check.
            expected_value - The string that must be present at <column>:<row> in order for the
                             keyword to pass.
            ignore_case - A boolean flag indicating whether or not case should be ignored.

        Optional Arguments:
            exists - [Default True] - This is a boolean flag that indicates whether the output should exist or not.
            max_wait - [Default 0] - This is an integer that indicates how long the keyword should wait before
                                     failing.
            interval - [Default 1] - This is the sleep duration between retry attempts while waiting for the expected
                                     output.

        Sends the given command to a device and then it splits the output into a table. Each string
        in the output is split on whitespace to create the columns, and then newlines to create the rows.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)
        cmd_obj = self.__send_command(dev, command, **kwargs)
        result = self.__check_output(cmd_obj, expected_value, False, ignore_case, table=True, column=column, row=row,
                                     **kwargs)

        start = time.time()
        max_wait = self.get_max_wait(**kwargs)
        interval = self.get_interval(**kwargs)

        while time.time() - start < max_wait and not result:
            cmd_obj = self.__send_command(dev, command, **kwargs)
            result = self.__check_output(cmd_obj, expected_value, False, ignore_case, table=True, column=column,
                                         row=row, **kwargs)
            if not result:
                time.sleep(interval)

        kw_result = self._determine_result(dev, cmd_obj, result, True, "CLI send passed.", "CLI send failed.", **kwargs)
        return self._keyword_cleanup([kw_result])

    # +------------------------------+
    # | Non-Keyword Helper Functions |
    # +------------------------------+
    @staticmethod
    def __send_command(dev, command, **kwargs):
        """
        This functions creates a CLI command object and sends it to the given device.
        This function also supports a number of keyword arguments to set optional values
        within the command object.

        Optional Kwargs:
            prompt - This accepts a prompt constant (which can be found in NetworkElementConstants).
                     It tells the device which prompt it should sent the command from.
            prompt_args - This accepts either a string or list of strings which should contain
                          any arguments required by the prompt handler to change prompt.
            confirmation_phrases - This accepts either a string or list of strings which contain any
                                   outputs that require a response.
            confirmation_args - This accepts a string or list of strings to send in response to the
                                received confirmation phrase.
        """
        cmd_obj = CliCommandObject()
        cmd_obj.command = command
        cmd_obj.prompt = kwargs.get("prompt", "userPrompt")
        cmd_obj.prompt_args = kwargs.get("prompt_args", None)
        cmd_obj.confirmation_phrases = kwargs.get("confirmation_phrases", None)
        cmd_obj.confirmation_args = kwargs.get("confirmation_args", None)
        return dev.send_command_object(cmd_obj)

    def __check_output(self, cmd_obj, expected_output, ignore_whitespace, ignore_case, **kwargs):
        """
        This function checks a commands output and verifies it exists or does not exist.

        """
        result = True
        exists = StringUtils.string_to_boolean(kwargs.get("exists", True))
        result_string = ["\nExpected Outputs:"] if exists else ["\nUnexpected Outputs:"]
        format_output, format_expected_output = self.__format_verify_data(cmd_obj, expected_output, ignore_whitespace,
                                                                          ignore_case)
        if kwargs.get("table", False):
            pw = ParserWrapper()
            col = kwargs.get("column", 0)
            row = kwargs.get("row", 0)
            val = pw.get_value_at_location(format_output, col, expected_output, row)
            search_result = False if val == pw.constants.VALUE_NOT_PRESENT else True
        elif kwargs.get("regex", False):
            search_result = len(re.findall(expected_output, format_output)) > 0
            expected_output = expected_output.pattern
        else:
            search_result = format_expected_output in format_output

        if search_result:
            result_string.append("Found: " + expected_output)
            if not exists:
                result = False
        else:
            result_string.append("Not Found: " + expected_output)
            if exists:
                result = False

        self.logger.log_info("\n".join(result_string))

        return result

    @staticmethod
    def __format_verify_data(cmd_obj, expected_output, ignore_whitespace, ignore_case):
        """
        This function formats the command output and expected output.

        [expected_output] - The output the user expects to be within the command's output.
        [ignore_whitespace] - A boolean value that indicates whether or not whitespace should be ignored.
                              If enabled all whitespace characters will be stripped from the command
                              output and expected output.
        [ignore_case] - A boolean value that indicates whether or not case should be ignored. If enabled
                        the command output and expected output will be converted to all lower case characters.
        """
        format_output = cmd_obj.return_text
        format_expected_output = expected_output

        if StringUtils.string_to_boolean(ignore_whitespace, True):
            format_output = format_output.replace(" ", "")
            format_output = format_output.replace("\t", "")
            format_output = format_output.replace("\n", "")
            format_output = format_output.replace("\r", "")
            format_expected_output = format_expected_output.replace(" ", "")
            format_expected_output = format_expected_output.replace("\t", "")
            format_expected_output = format_expected_output.replace("\n", "")
            format_expected_output = format_expected_output.replace("\r", "")
        if StringUtils.string_to_boolean(ignore_case, True):
            format_output = format_output.lower()
            format_expected_output = format_expected_output.lower()

        return format_output, format_expected_output

    @staticmethod
    def __check_regex(regex_string):
        """
        This function verifies that the passed regex string is valid.
        """
        try:
            return True, re.compile(regex_string, re.DOTALL)
        except re.error:
            return False, None

    # +-----------------------------+
    # | Deprecated Helper Functions |
    # +-----------------------------+
    def __send_command_deprecated(self, dev, command, **kwargs):
        """
        Support kwargs:
         - prompt
         - prompt_args
         - confirmation_phrases
         - confirmation_args

        Creates the command object and sends it to the device. It also checks the kwargs for any optional arguments.
        """
        cmd_obj = CliCommandObject()
        cmd_obj.command = command
        cmd_obj.prompt = kwargs.get("prompt", "userPrompt")
        cmd_obj.prompt_args = kwargs.get("prompt_args", None)
        cmd_obj.confirmation_phrases = kwargs.get("confirmation_phrases", None)
        cmd_obj.confirmation_args = kwargs.get("confirmation_args", None)
        dev.send_command_object(cmd_obj)

        output = cmd_obj.return_text
        self.logger.log_info(output)

        return cmd_obj

    @staticmethod
    def __output_verify_deprecated(exists, output, search_list, ignore_whitespace, ignore_case, regex):
        """
        [exists]            - A boolean indicating whether the given string(s) should be present in the output.
        [output]            - The output to inspect.
        [search_list]       - A list of strings to check the existence of.
        [ignore_whitespace] - A boolean indicating whether or not whitespace should be ignored.
        [ignore_case]       - A boolean indicating whether or not case should be ignored.
        [regex]             - A boolean indicating whether or not the search list strings should be treated as regex.
        """
        result = True
        result_output = list()

        original_search_list = list(search_list)
        search_list = ListUtils.convert_to_list(search_list)
        ignore_whitespace = StringUtils.string_to_boolean(ignore_whitespace)
        ignore_case = StringUtils.string_to_boolean(ignore_case)
        regex = StringUtils.string_to_boolean(regex)

        if ignore_whitespace:
            output = output.replace(" ", "")
            search_list = [i.replace(" ", "") for i in search_list]
        if ignore_case:
            output = output.lower()
            search_list = [i.lower() for i in search_list]
        output = output.split("\r\n")

        if exists:
            result_output.append("\nExpected Outputs:")
        if not exists:
            result_output.append("\nUnexpected Outputs:")

        for i, search in enumerate(search_list):
            for j, line in enumerate(output):
                search_result = search in line if not regex else len(re.findall(re.compile(search), line)) > 0

                if search_result:
                    result_output.append("Found: " + original_search_list[i])
                    if not exists:
                        result = False
                    break
                if j == len(output) - 1:
                    result_output.append("Not Found: " + original_search_list[i])
                    if exists:
                        result = False

        return result, result_output

    @staticmethod
    def get_max_wait(**kwargs):
        """
        Attempts to get the max_wait time for the wait_for function.
        Note: Defaults to 0 if not defined in kwargs.
        """
        max_wait = kwargs.get("max_wait", 0)

        try:
            return int(max_wait)
        except ValueError:
            return 0

    @staticmethod
    def get_interval(**kwargs):
        """
        Attempts to get the retry interval for the wait_for function.
        Note: Defaults to 1 if not defined in kwargs.
        """
        interval = kwargs.get("interval", '1')

        try:
            return int(interval)
        except ValueError:
            return 1
