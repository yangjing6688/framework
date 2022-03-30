"""
Keyword class for all sysconfig cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.SysinfoConstants import \
    SysinfoConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.SysinfoConstants import \
    SysinfoConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementSysinfoGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementSysinfoGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "sysinfo"

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def sysinfo_verify_switch_type(self, device_name, type, **kwargs):
        """
        Keyword Arguments:
        [version]              - The fireware version to be checked.

        Verifies that the firmware version on the device is the same as the one passed into this method.
        """
        args = {"type": type}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_INFO,
                                           self.parse_const.CHECK_FOR_SYSTEM_TYPE, True,
                                           "Sysinfo type is {type}.",
                                           "Sysinfo type is not {type}. ",
                                           **kwargs)

