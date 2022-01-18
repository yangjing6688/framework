"""
Keyword class for all archives northbound commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.ArchivesConstants import \
    ArchivesConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.ArchivesConstants import \
    ArchivesConstants as CommandConstants


class EndsystemArchivesKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemArchivesKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "archives"

    def verify_show_archives(self, device_name, **kwargs):
        """Verifies the output from show_archives."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ARCHIVES,
                                           self.parse_const.SHOW_ARCHIVES,
                                           True, "PASSED", "FAILED", **kwargs)
