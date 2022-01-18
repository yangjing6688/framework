"""
Keyword class for all sitetree northbound commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.SitetreeConstants import \
    SitetreeConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.SitetreeConstants import \
    SitetreeConstants as CommandConstants


class EndsystemSitetreeKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemSitetreeKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "sitetree"

    def verify_placeholder(self, device_name, **kwargs):
        """Verifies the output from placeholder."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.PLACEHOLDER,
                                           self.parse_const.PLACEHOLDER,
                                           True, "PASSED", "FAILED", **kwargs)
