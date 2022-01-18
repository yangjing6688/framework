"""
Keyword class for all administration northbound commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.AdministrationConstants import \
    AdministrationConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.AdministrationConstants import \
    AdministrationConstants as CommandConstants


class EndsystemAdministrationKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemAdministrationKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "administration"

    def verify_show_administration_server_info(self, device_name, **kwargs):
        """Verifies the output from show_administration_server_info."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ADMINISTRATION_SERVER_INFO,
                                           self.parse_const.SHOW_ADMINISTRATION_SERVER_INFO,
                                           True, "PASSED", "FAILED", **kwargs)
