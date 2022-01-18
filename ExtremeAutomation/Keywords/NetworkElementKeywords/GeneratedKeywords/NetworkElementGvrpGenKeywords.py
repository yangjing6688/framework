"""
Keyword class for all gvrp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.GvrpConstants import \
    GvrpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.GvrpConstants import \
    GvrpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementGvrpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementGvrpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "gvrp"

    def gvrp_enable_global(self, device_name, **kwargs):
        """
        Description: Enable GVRP on a given device.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def gvrp_disable_global(self, device_name, **kwargs):
        """
        Description: Disable GVRP on a given device.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def gvrp_enable_port(self, device_name, port='', **kwargs):
        """
        Description: Enables GVRP on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT,
                                    **kwargs)

    def gvrp_disable_port(self, device_name, port='', **kwargs):
        """
        Description: Disables GVRP on a given port.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def gvrp_verify_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Verifies that GVRP is enabled on a given device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_GVRP_STATE, True,
                                           "Global GVRP state was enabled on {device_name}.",
                                           "Global GVRP state was DISABLED on {device_name}.",
                                           **kwargs)

    def gvrp_verify_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Verifies that GVRP is disabled on a given device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_GVRP_STATE, False,
                                           "Global GVRP state was disabled on {device_name}.",
                                           "Global GVRP state was ENABLED on {device_name}.",
                                           **kwargs)

    def gvrp_verify_port_enabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Verifies that GVRP is enabled on a given device.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE_PORT,
                                           self.parse_const.CHECK_GVRP_STATE_PORT, True,
                                           "GVRP was enabled on port {port} on {device_name}.",
                                           "GVRP was DISABLED on port {port} on {device_name}.",
                                           **kwargs)

    def gvrp_verify_port_disabled(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Verifies that GVRP is disabled on a given device.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE_PORT,
                                           self.parse_const.CHECK_GVRP_STATE_PORT, False,
                                           "GVRP was disabled on port {port} on {device_name}.",
                                           "GVRP was ENABLED on port {port} on {device_name}.",
                                           **kwargs)
