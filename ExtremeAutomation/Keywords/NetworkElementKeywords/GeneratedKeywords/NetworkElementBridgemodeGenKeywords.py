"""
Keyword class for all bridgemode cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.BridgemodeConstants import \
    BridgemodeConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.BridgemodeConstants import \
    BridgemodeConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementBridgemodeGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementBridgemodeGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "bridgemode"

    def bridgemode_set_mode(self, device_name, mode='', **kwargs):
        """
        Description: Sets a device's bridge mode to the specified value.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "mode": mode
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MODE,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def bridgemode_verify_customer_bridge(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.

        Verifies the bridge mode on a given device is set to customer bridge.
        """
        args = {"bridge_mode": 0}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MODE,
                                           self.parse_const.CHECK_BRIDGE_MODE, True,
                                           "Bridge mode was equal to customer bridge on {device_name}.",
                                           "Bridge mode was not equal to customer bridge on {device_name}.",
                                           **kwargs)

    def bridgemode_verify_provider_bridge(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.

        Verifies the bridge mode on a given device is set to provider bridge.
        """
        args = {"bridge_mode": 1}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MODE,
                                           self.parse_const.CHECK_BRIDGE_MODE, True,
                                           "Bridge mode was equal to provider bridge on {device_name}.",
                                           "Bridge mode was not equal to provider bridge on {device_name}.",
                                           **kwargs)
