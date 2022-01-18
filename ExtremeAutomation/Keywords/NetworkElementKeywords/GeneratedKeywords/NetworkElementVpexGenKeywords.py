"""
Keyword class for all vpex cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.VpexConstants import \
    VpexConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.VpexConstants import \
    VpexConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementVpexGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementVpexGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "vpex"

    def vpex_enable_global(self, device_name, **kwargs):
        """
        Description: Enables VPEX globally on the device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def vpex_disable_global(self, device_name, **kwargs):
        """
        Description: Disables VPEX globally on the device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def vpex_enable_auto_configuration(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_AUTO_CONFIGURATION,
                                    **kwargs)

    def vpex_disable_auto_configuration(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_AUTO_CONFIGURATION,
                                    **kwargs)

    def vpex_set_ports(self, device_name, port='', slot='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "slot": slot
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORTS,
                                    **kwargs)

    def vpex_clear_ports(self, device_name, port='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORTS,
                                    **kwargs)

    def vpex_set_ring_rebalancing_auto(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RING_REBALANCING_AUTO,
                                    **kwargs)

    def vpex_set_ring_rebalancing_off(self, device_name, **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RING_REBALANCING_OFF,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def vpex_verify_enabled(self, device_name, name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.

        Verifies VPEX is enabled globally on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_VPEX_ENABLED, True,
                                           "VPEX is globally enabled on {device_name}.",
                                           "VPEX is NOT globally enabled on {device_name}.",
                                           **kwargs)

    def vpex_verify_disabled(self, device_name, name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.

        Verifies VPEX is disabled globally on the device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_VPEX_ENABLED, False,
                                           "VPEX is globally disabled on {device_name}.",
                                           "VPEX is NOT globally disabled on {device_name}.",
                                           **kwargs)
