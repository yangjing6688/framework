"""
Keyword class for all devicevlans northbound commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.DevicevlansConstants import \
    DevicevlansConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.DevicevlansConstants import \
    DevicevlansConstants as CommandConstants


class EndsystemDevicevlansKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemDevicevlansKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "devicevlans"

    def verify_placeholder(self, device_name, **kwargs):
        """Verifies the output from placeholder."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.PLACEHOLDER,
                                           self.parse_const.PLACEHOLDER,
                                           True, "PASSED", "FAILED", **kwargs)
