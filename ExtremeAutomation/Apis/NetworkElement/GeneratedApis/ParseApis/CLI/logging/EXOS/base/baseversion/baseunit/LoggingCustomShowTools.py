from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.logging.base.LoggingBaseCustomShowTools import \
    LoggingBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.Utils.KeywordUtils import KeywordUtils
import re


class LoggingCustomShowTools(LoggingBaseCustomShowTools):
    def __init__(self, device):
        super(LoggingCustomShowTools, self).__init__(device)

    def check_string_in_output(self, output, args, **kwargs):
        string = args["string"].replace("(", r"\(").replace(")", r"\)")
        string = string.replace(".", r"\.")
        result = self.pw.is_exact_string_present_in_output(output, string)
        return result, result

    def check_regex_in_output(self, output, args, **kwargs):
        good, comp_re = KeywordUtils()._check_regex(args["regex"])
        if good:
            if re.search(comp_re, output) is not None:
                return True, output
        return False, False
