"""
Keyword class for all rsmlt cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.RsmltConstants import \
    RsmltConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.RsmltConstants import \
    RsmltConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementRsmltGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementRsmltGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "rsmlt"

    def rsmlt_enable_edge_support(self, device_name, **kwargs):
        """
        Description: Enables RSMLT Edge Support.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_EDGE_SUPPORT,
                                    **kwargs)

    def rsmlt_disable_edge_support(self, device_name, **kwargs):
        """
        Description: Disables RSMLT Edge Support.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_EDGE_SUPPORT,
                                    **kwargs)

    def rsmlt_enable_vlan_interface(self, device_name, interface='', **kwargs):
        """
        Description: Enables RSMLT on a vlan interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_VLAN_INTERFACE,
                                    **kwargs)

    def rsmlt_disable_vlan_interface(self, device_name, interface='', **kwargs):
        """
        Description: Disables RSMLT on a vlan interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_VLAN_INTERFACE,
                                    **kwargs)

    def rsmlt_set_interface_holddown_timer(self, device_name, interface='', timer='', **kwargs):
        """
        Description: Sets the RSMLT holddown timer on the specified vlan interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface,
            "timer": timer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INTERFACE_HOLDDOWN_TIMER,
                                    **kwargs)

    def rsmlt_set_interface_holdup_timer(self, device_name, interface='', timer='', **kwargs):
        """
        Description: Sets the RSMLT holdup timer on the specified vlan interface.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface,
            "timer": timer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INTERFACE_HOLDUP_TIMER,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def rsmlt_verify_edge_support_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies RSMLT Edge Support is Enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_EDGE_SUPPORT,
                                           self.parse_const.VERIFY_RSMLT_EDGE_SUPPORT_ENABLED, True,
                                           "RSMLT Edge Support is enabled on {device_name}.",
                                           "RSMLT Edge Support is NOT enabled on {device_name}!",
                                           **kwargs)

    def rsmlt_verify_edge_support_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies RSMLT Edge Support is Disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_EDGE_SUPPORT,
                                           self.parse_const.VERIFY_RSMLT_EDGE_SUPPORT_DISABLED, True,
                                           "RSMLT Edge Support is disabled on {device_name}.",
                                           "RSMLT Edge Support IS enabled on {device_name}!",
                                           **kwargs)

    def rsmlt_verify_vlan_interface_enabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [interface]       - The Interface Vlan.

        Verifies RSMLT is enabled on the specified interface vlan.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOCAL,
                                           self.parse_const.VERIFY_RSMLT_ENABLED_ON_INTERFACE_VLAN, True,
                                           "RSMLT is enabled on vlan {interface} on {device_name}.",
                                           "RSMLT is NOT enabled on vlan {interface} on {device_name}!",
                                           **kwargs)

    def rsmlt_verify_vlan_interface_disabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [interface]       - The Interface Vlan.

        Verifies RSMLT is disabled on the specified interface vlan.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOCAL,
                                           self.parse_const.VERIFY_RSMLT_DISABLED_ON_INTERFACE_VLAN, True,
                                           "RSMLT is disabled on vlan {interface} on {device_name}.",
                                           "RSMLT is NOT disabled on vlan {interface} on {device_name}!",
                                           **kwargs)

    def rsmlt_verify_intf_holddown_timer(self, device_name, interface='', timer='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [interface]       - The Interface Vlan.
        [timer]           - The RSMLT holddown timer value to verify.

        Verifies the RSMLT Holddown Timer value is set for the specified interface vlan.
        """
        args = {"interface": interface,
                "intf": "vlan",
                "timer": timer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOCAL,
                                           self.parse_const.VERIFY_RSMLT_HOLDDOWN_TIMER_IS_SET, True,
                                           "RSMLT Holddown Timer value {timer} on vlan {interface} is correctly set.",
                                           "RSMLT Holddown Timer value {timer} on vlan {interface} is NOT correctly "
                                           "set!",
                                           **kwargs)

    def rsmlt_verify_intf_holdup_timer(self, device_name, interface='', timer='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [interface]       - The Interface Vlan.
        [timer]           - The RSMLT holdup timer value to verify.

        Verifies the RSMLT Holdup Timer value is set for the specified interface vlan.
        """
        args = {"interface": interface,
                "intf": "vlan",
                "timer": timer}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOCAL,
                                           self.parse_const.VERIFY_RSMLT_HOLDUP_TIMER_IS_SET, True,
                                           "RSMLT Holdup Timer value {timer} on vlan {interface} is correctly set.",
                                           "RSMLT Holdup Timer value {timer} on vlan {interface} is NOT correctly set!",
                                           **kwargs)
