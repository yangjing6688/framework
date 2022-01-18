"""
Keyword class for all wlanservices cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.WlanservicesConstants import \
    WlanservicesConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.WlanservicesConstants import \
    WlanservicesConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementWlanservicesGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementWlanservicesGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "wlanservices"

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def wlanservices_verify_exists(self, device_name, wlan_service_names='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [wlan_service_name] - The wlan service name that should exist on the device.

        Verifies that the given wlan service is configured on the device.
        """
        args = {"wlan_service_name": wlan_service_names}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_WLAN_SERVICE_EXISTS, True,
                                           "WLAN Service: {wlan_service_name} exists on {device_name}.",
                                           "WLAN Service: {wlan_service_name DOES NOT exist on {device_name}!",
                                           **kwargs)

    def wlanservices_verify_does_not_exist(self, device_name, wlan_service_names='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [wlan_service_name] - The wlan service name that should not exist on the device.

        Verifies that the given wlan service is not configured on the device.
        """
        args = {"wlan_service_name": wlan_service_names}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_WLAN_SERVICE_EXISTS, False,
                                           "WLAN Service: {wlan_service_name} correctly does not exist on "
                                           "{device_name}.",
                                           "WLAN Service: {wlan_service_name} incorrectly exists on "
                                           "{device_name}!",
                                           **kwargs)
