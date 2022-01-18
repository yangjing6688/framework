import re
import inspect
from ExtremeAutomation.Library.Logger.Logger import Logger


class KeywordUtils:
    @staticmethod
    def log_running_keyword(message="", log_level=Logger.INFO, device_name=None):
        """
        This function returns the name of the function that called the log_running_keyword function, which in
        this case is the keyword name. It then changes the format of the keyword name from "this_is_a_keyword"
        to "This Is A Keyword". Finally it is printed to the log.
        """
        keyword_logger = Logger()
        keyword = inspect.currentframe().f_back

        while keyword.f_code.co_name.lower() == "_init_keyword":
            keyword = keyword.f_back

        if len(re.findall("^execute_.*keyword$", keyword.f_code.co_name.lower())) == 1:
            keyword = keyword.f_back

        keyword = keyword.f_code.co_name.replace("_", " ").title()

        if device_name is None:
            if message == "":
                keyword_logger.log_message("\n" + "Running keyword: " + keyword, log_level)
            else:
                keyword_logger.log_message("\n" + "Running keyword: " + keyword + " " + message, log_level)
        else:
            if message == "":
                keyword_logger.log_message("\n" + "Running keyword: " + keyword + " on " + str(device_name), log_level)
            else:
                keyword_logger.log_message("\n" + "Running keyword: " + keyword + " on " + str(device_name) + " " +
                                           message, log_level)

    @staticmethod
    def _check_regex(regex_string):
        """
        This function verifies that the passed regex string is valid.
        """
        try:
            return True, re.compile(regex_string, re.DOTALL)
        except re.error:
            return False, None
