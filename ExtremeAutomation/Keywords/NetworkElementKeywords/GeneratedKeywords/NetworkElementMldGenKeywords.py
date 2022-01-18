"""
Keyword class for all mld cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.MldConstants import \
    MldConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.MldConstants import \
    MldConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementMldGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementMldGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "mld"

    def mld_enable_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Description: Enables MLD on a given VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_VLAN,
                                    **kwargs)

    def mld_disable_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Description: Disables MLD on a given VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_VLAN,
                                    **kwargs)

    def mld_set_version(self, device_name, version='', vlan='', vlan_name='', **kwargs):
        """
        Description: Configures the MLD version of a given VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "version": version,
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VERSION,
                                    **kwargs)

    def mld_enable_snooping(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Description: Enables MLD snooping on a given VLAN.

        Supported Agents and OS:
            CLI: EXOS, SLX
        """
        args = {
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SNOOPING,
                                    **kwargs)

    def mld_disable_snooping(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Description: Disables MLD snooping on a given VLAN.

        Supported Agents and OS:
            CLI: EXOS, SLX
        """
        args = {
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SNOOPING,
                                    **kwargs)

    def mld_enable_snooping_querier(self, device_name, vlan='', **kwargs):
        """
        Description: Enables the MLDv1 snooping querier function on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SNOOPING_QUERIER,
                                    **kwargs)

    def mld_disable_snooping_querier(self, device_name, vlan='', **kwargs):
        """
        Description: Disables the MLDv1 snooping querier function on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SNOOPING_QUERIER,
                                    **kwargs)

    def mld_set_snooping_fast_leave(self, device_name, vlan='', **kwargs):
        """
        Description: Configures the MLD snooping immediate-leave feature on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_FAST_LEAVE,
                                    **kwargs)

    def mld_clear_snooping_fast_leave(self, device_name, vlan='', **kwargs):
        """
        Description: Clears the MLD snooping immediate-leave feature on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SNOOPING_FAST_LEAVE,
                                    **kwargs)

    def mld_set_snooping_last_member_query_count(self, device_name, value='', vlan='', **kwargs):
        """
        Description: Configures the MLDv1 snooping last-member query count on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "value": value,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_LAST_MEMBER_QUERY_COUNT,
                                    **kwargs)

    def mld_clear_snooping_last_member_query_count(self, device_name, vlan='', **kwargs):
        """
        Description: Sets the MLDv1 snooping last-member query count to default on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SNOOPING_LAST_MEMBER_QUERY_COUNT,
                                    **kwargs)

    def mld_set_snooping_last_member_query_interval(self, device_name, value='', vlan='', **kwargs):
        """
        Description: Configures the MLDv1 snooping last-member query interval on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "value": value,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_LAST_MEMBER_QUERY_INTERVAL,
                                    **kwargs)

    def mld_clear_snooping_last_member_query_interval(self, device_name, vlan='', **kwargs):
        """
        Description: Sets the MLDv1 snooping last-member query interval to default on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SNOOPING_LAST_MEMBER_QUERY_INTERVAL,
                                    **kwargs)

    def mld_set_snooping_robustness_variable(self, device_name, value='', vlan='', **kwargs):
        """
        Description: Configures the MLDv1 snooping robustness-variable value on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "value": value,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_ROBUSTNESS_VARIABLE,
                                    **kwargs)

    def mld_clear_snooping_robustness_variable(self, device_name, vlan='', **kwargs):
        """
        Description: Sets the MLDv1 snooping robustness-variable value to default for a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SNOOPING_ROBUSTNESS_VARIABLE,
                                    **kwargs)

    def mld_set_snooping_startup_query_count(self, device_name, value='', vlan='', **kwargs):
        """
        Description: Configures the MLDv1 snooping startup-query-count value on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "value": value,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_STARTUP_QUERY_COUNT,
                                    **kwargs)

    def mld_clear_snooping_startup_query_count(self, device_name, vlan='', **kwargs):
        """
        Description: Sets the MLDv1 snooping startup-query-count value to default for a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SNOOPING_STARTUP_QUERY_COUNT,
                                    **kwargs)

    def mld_set_snooping_startup_query_interval(self, device_name, value='', vlan='', **kwargs):
        """
        Description: Configures the MLDv1 snooping startup-query-interval value on a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "value": value,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_STARTUP_QUERY_INTERVAL,
                                    **kwargs)

    def mld_clear_snooping_startup_query_interval(self, device_name, vlan='', **kwargs):
        """
        Description: Sets the MLDv1 snooping startup-query-interval value to default for a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SNOOPING_STARTUP_QUERY_INTERVAL,
                                    **kwargs)

    def mld_set_snooping_mrouter(self, device_name, port='', vlan='', **kwargs):
        """
        Description: Configures a VLAN port member to be a MLDv1 multicast router (mrouter)port.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_MROUTER,
                                    **kwargs)

    def mld_clear_snooping_mrouter(self, device_name, vlan='', **kwargs):
        """
        Description: Unconfigures the specified multicast router port for a given VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SNOOPING_MROUTER,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def mld_verify_enabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) MLD should be enabled on.

        Verifies MLD is enabled on a given VLAN.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_MLD_STATE, True,
                                           "MLD was enabled on VLAN {vlan} on {device_name}.",
                                           "MLD was DISABLED on VLAN {vlan} on {device_name}.",
                                           **kwargs)

    def mld_verify_disabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) MLD should be disabled on.

        Verifies MLD is disabled on a given VLAN.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_MLD_STATE, False,
                                           "MLD was disabled on VLAN {vlan} on {device_name}.",
                                           "MLD was ENABLED on VLAN {vlan} on {device_name}.",
                                           **kwargs)

    def mld_verify_snooping_enabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that MLD snooping should be enabled on.

        Verifies MLD snooping is enabled on a given VLAN.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_MLD_SNOOPING_STATE, True,
                                           "MLD snooping was enabled on VLAN {vlan} on {device_name}.",
                                           "MLD snooping was DISABLED on VLAN {vlan} on {device_name}.",
                                           **kwargs)

    def mld_verify_snooping_disabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that MLD snooping should be disabled on.

        Verifies MLD snooping is disabled on a given VLAN.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_MLD_SNOOPING_STATE, False,
                                           "MLD snooping was disabled on VLAN {vlan} on {device_name}.",
                                           "MLD snooping was ENABLED on VLAN {vlan} on {device_name}.",
                                           **kwargs)

    def mld_verify_version(self, device_name, vlan='', version='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) whose MLD version should be inspected.
        [version]     - The MLD version that should be configured.

        Verifies the MLD version configured to a given VLAN.
        """
        args = {"vlan": vlan,
                "version": version}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VERSION,
                                           self.parse_const.CHECK_MLD_VERSION, True,
                                           "MLD version was equal to {version} on {device_name}.",
                                           "MLD version was NOT equal to {version} on {device_name}.",
                                           **kwargs)
