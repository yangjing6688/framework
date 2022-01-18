"""
Keyword class for all igmp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.IgmpConstants import \
    IgmpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.IgmpConstants import \
    IgmpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementIgmpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementIgmpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "igmp"

    def igmp_set_version(self, device_name, igmp_ver='', vlan='', vlan_name='', **kwargs):
        """
        Description: Sets the IGMP version on a given VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
        """
        args = {
            "igmp_ver": igmp_ver,
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VERSION,
                                    **kwargs)

    def igmp_enable_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Description: Enables IGMP on the specified VLAN.

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

    def igmp_disable_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Description: Disables IGMP on the specified VLAN.

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

    def igmp_enable_snooping(self, device_name, **kwargs):
        """
        Description: Globally enables IGMP snooping.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SNOOPING,
                                    **kwargs)

    def igmp_disable_snooping(self, device_name, **kwargs):
        """
        Description: Globally disables IGMP snooping.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SNOOPING,
                                    **kwargs)

    def igmp_enable_snooping_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Description: Enables IGMP snooping on the specified VLAN.

        Supported Agents and OS:
            CLI: EXOS, VOSS, SLX
        """
        args = {
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SNOOPING_VLAN,
                                    **kwargs)

    def igmp_disable_snooping_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Description: Disables IGMP snooping on the specified VLAN.

        Supported Agents and OS:
            CLI: EXOS, VOSS, SLX
        """
        args = {
            "vlan": vlan,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SNOOPING_VLAN,
                                    **kwargs)

    def igmp_enable_snooping_proxy(self, device_name, port='', vlan='', **kwargs):
        """
        Description: Enables IGMP snooping proxy on the specified VLAN.

        Supported Agents and OS:
            CLI: EXOS, VOSS, SLX
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SNOOPING_PROXY,
                                    **kwargs)

    def igmp_disable_snooping_proxy(self, device_name, port='', vlan='', **kwargs):
        """
        Description: Disables IGMP snooping proxy on the specified VLAN.

        Supported Agents and OS:
            CLI: EXOS, VOSS, SLX
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SNOOPING_PROXY,
                                    **kwargs)

    def igmp_set_snooping_querier(self, device_name, vlan='', **kwargs):
        """
        Description: Enables the IGMP snooping querier on the specified VLAN.

        Supported Agents and OS:
            CLI: VOSS, SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_QUERIER,
                                    **kwargs)

    def igmp_clear_snooping_querier(self, device_name, vlan='', **kwargs):
        """
        Description: Disables the IGMP snooping querier on the specified VLAN.

        Supported Agents and OS:
            CLI: VOSS, SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SNOOPING_QUERIER,
                                    **kwargs)

    def igmp_set_snooping_querier_address(self, device_name, vlan='', ip='', **kwargs):
        """
        Description: Sets the IGMP snooping querier IP Address on a given VLAN.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip": ip,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_QUERIER_ADDRESS,
                                    **kwargs)

    def igmp_clear_snooping_querier_address(self, device_name, vlan='', **kwargs):
        """
        Description: Removes the IGMP snooping querier IP Address on a given VLAN.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SNOOPING_QUERIER_ADDRESS,
                                    **kwargs)

    def igmp_enable_snooping_compatibility_mode_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enables IGMP snooping Compatibility Mode on the specified VLAN.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SNOOPING_COMPATIBILITY_MODE_VLAN,
                                    **kwargs)

    def igmp_disable_snooping_compatibility_mode_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disables IGMP snooping Compatibility Mode on the specified VLAN.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SNOOPING_COMPATIBILITY_MODE_VLAN,
                                    **kwargs)

    def igmp_enable_snooping_dynamic_downgrade_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enables IGMP snooping Dynamic Downgrade on the specified VLAN.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SNOOPING_DYNAMIC_DOWNGRADE_VLAN,
                                    **kwargs)

    def igmp_disable_snooping_dynamic_downgrade_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disables IGMP snooping Dynamic Downgrade on the specified VLAN.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SNOOPING_DYNAMIC_DOWNGRADE_VLAN,
                                    **kwargs)

    def igmp_enable_snooping_explicit_host_tracking_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enables IGMP snooping Explicit Host Tracking on the specified VLAN.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SNOOPING_EXPLICIT_HOST_TRACKING_VLAN,
                                    **kwargs)

    def igmp_disable_snooping_explicit_host_tracking_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disables IGMP snooping Explicit Host Tracking on the specified VLAN.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SNOOPING_EXPLICIT_HOST_TRACKING_VLAN,
                                    **kwargs)

    def igmp_set_version_interface(self, device_name, igmp_ver='', port='', **kwargs):
        """
        Description: Sets the IGMP version for a given interface.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "igmp_ver": igmp_ver,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VERSION_INTERFACE,
                                    **kwargs)

    def igmp_enable_snooping_fast_leave(self, device_name, vlan='', **kwargs):
        """
        Description: Enables IGMP snooping fast leave on the specified VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SNOOPING_FAST_LEAVE,
                                    **kwargs)

    def igmp_disable_snooping_fast_leave(self, device_name, vlan='', **kwargs):
        """
        Description: Disables IGMP snooping fast leave on the specified VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SNOOPING_FAST_LEAVE,
                                    **kwargs)

    def igmp_set_snooping_last_member_query_interval(self, device_name, interval='', vlan='', **kwargs):
        """
        Description: Sets the IGMP snooping last member query interval value for the specified VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interval": interval,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_LAST_MEMBER_QUERY_INTERVAL,
                                    **kwargs)

    def igmp_set_snooping_last_member_query_count(self, device_name, value='', vlan='', **kwargs):
        """
        Description: Sets the IGMP snooping last member query count value for the specified VLAN.

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

    def igmp_set_snooping_query_interval(self, device_name, interval='', vlan='', **kwargs):
        """
        Description: Sets the IGMP snooping query interval value for the specified VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interval": interval,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_QUERY_INTERVAL,
                                    **kwargs)

    def igmp_set_snooping_query_max_response_time(self, device_name, time='', vlan='', **kwargs):
        """
        Description: Sets the IGMP snooping query max response time for the specified VLAN.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "time": time,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SNOOPING_QUERY_MAX_RESPONSE_TIME,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def igmp_verify_enabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that IGMP should be enabled on.

        Verifies that IGMP is enabled on a given VLAN.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_IGMP_STATE, True,
                                           "IGMP is enabled on vlan {vlan} on {device_name}.",
                                           "IGMP is DISABLED on vlan {vlan} on {device_name}.",
                                           **kwargs)

    def igmp_verify_disabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that IGMP should be disabled on.

        Verifies that IGMP is disabled on a given VLAN.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_IGMP_STATE, False,
                                           "IGMP is disabled on vlan {vlan} on {device_name}.",
                                           "IGMP is ENABLED on vlan {vlan} on {device_name}.",
                                           **kwargs)

    def igmp_verify_version(self, device_name, vlan='', vlan_name='', version='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) whose IGMP version should be inspected.
        [version]     - The IGMP version the VLAN should be configured with.

        Verifies the IGMP version configured to a given VLAN.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "igmp_ver": version}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VERSION,
                                           self.parse_const.CHECK_IGMP_VERSION, True,
                                           "IGMP version is equal to {igmp_ver} on {device_name}.",
                                           "IGMP version is NOT equal to {igmp_ver} on {device_name}.",
                                           **kwargs)

    def igmp_verify_snooping_enabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that IGMP should be enabled on.

        Verifies that IGMP snooping is enabled on a given VLAN.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_VLAN_STATE, True,
                                           "IGMP Snooping is enabled on vlan {vlan} on {device_name}.",
                                           "IGMP Snooping is DISABLED on vlan {vlan} on {device_name}.",
                                           **kwargs)

    def igmp_verify_snooping_disabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that IGMP should be disabled on.

        Verifies that IGMP snooping is disabled on a given VLAN.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_VLAN_STATE, False,
                                           "IGMP Snooping is disabled on vlan {vlan} on {device_name}.",
                                           "IGMP Snooping is ENABLED on vlan {vlan} on {device_name}.",
                                           **kwargs)

    def igmp_verify_snooping_querier_enabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that IGMP should be enabled on.

        Verifies that IGMP snooping querier is enabled on a given VLAN.
        NOTE: Currently only supported on VOSS
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_VLAN_STATE, True,
                                           "IGMP Snooping Querier is enabled on vlan {vlan} on {device_name}.",
                                           "IGMP Snooping Querier is DISABLED on vlan {vlan} on {device_name}.",
                                           **kwargs)

    def igmp_verify_snooping_querier_disabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that IGMP should be disabled on.

        Verifies that IGMP snooping querier is disabled on a given VLAN.
        NOTE: Currently only supported on VOSS
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_QUERIER_STATE, False,
                                           "IGMP Snooping Querier is disabled on vlan {vlan} on {device_name}.",
                                           "IGMP Snooping Querier is ENABLED on vlan {vlan} on {device_name}.",
                                           **kwargs)

    def igmp_verify_snooping_querier_address(self, device_name, vlan='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) whose IGMP version should be inspected.
        [ip]          - The IP Address for the IGMP Snooping Querier.

        Verifies the IGMP snooping querier IP Address configured to a given VLAN.
        NOTE: Currently only supported on VOSS
        """
        args = {"vlan": vlan,
                "ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNOOPING_QUERIER_ADDRESS,
                                           self.parse_const.CHECK_IGMP_SNOOPING_QUERIER_ADDRESS, True,
                                           "IGMP Snooping Querier Address was {ip} on {device_name}.",
                                           "IGMP Snooping Querier Address was NOT {ip} on {device_name}!",
                                           **kwargs)

    def igmp_verify_snooping_querier_address_removed(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) whose IGMP version should be inspected.

        Verifies the IGMP snooping querier IP Address has been removed on the given VLAN.
        NOTE: Currently only supported on VOSS
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNOOPING_QUERIER_ADDRESS,
                                           self.parse_const.CHECK_IGMP_SNOOPING_QUERIER_ADDRESS_IS_REMOVED, True,
                                           "IGMP Snooping Querier Address has been removed on {device_name}.",
                                           "IGMP Snooping Querier Address was NOT removed on {device_name}.",
                                           **kwargs)

    def igmp_verify_snooping_proxy_enabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that IGMP should be enabled on.

        Verifies that IGMP snooping proxy is enabled on a given VLAN.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_PROXY_STATE, True,
                                           "IGMP Snooping Proxy is enabled on vlan {vlan} on {device_name}.",
                                           "IGMP Snooping Proxy IS NOT enabled on vlan {vlan} on {device_name}!",
                                           **kwargs)

    def igmp_verify_snooping_proxy_disabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vlan]        - The VLAN(s) that IGMP should be disabled on.

        Verifies that IGMP snooping proxy is disabled on a given VLAN.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_PROXY_STATE, False,
                                           "IGMP Snooping Proxy is disabled on vlan {vlan} on {device_name}.",
                                           "IGMP Snooping Proxy IS ENABLED on vlan {vlan} on {device_name}!",
                                           **kwargs)

    def igmp_verify_snooping_dynamic_downgrade_enabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan on which IGMP snooping is being enabled.

        Verifies that IGMP snooping Dynamic Downgrade is enabled on a given VLAN.
        NOTE:  Supported on VOSS only.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_DYNAMIC_DOWNGRADE_STATE, True,
                                           "IGMP Snooping Dynamic Downgrade is enabled on vlan {vlan} on "
                                           "{device_name}.",
                                           "IGMP Snooping Dynamic Downgrade IS NOT enabled on vlan {vlan} on "
                                           "{device_name}!",
                                           **kwargs)

    def igmp_verify_snooping_dynamic_downgrade_disabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan on which IGMP snooping is being enabled.

        Verifies that IGMP snooping Dynamic Downgrade is disabled on a given VLAN.
        NOTE:  Supported on VOSS only.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_DYNAMIC_DOWNGRADE_STATE, False,
                                           "IGMP Snooping Dynamic Downgrade is disabled on vlan {vlan} on "
                                           "{device_name}.",
                                           "IGMP Snooping Dynamic Downgrade IS NOT disabled on vlan {vlan} on "
                                           "{device_name}!",
                                           **kwargs)

    def igmp_verify_snooping_compatibility_mode_enabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan on which IGMP snooping is being enabled.

        Verifies that IGMP snooping Compatibility Mode is enabled on a given VLAN.
        NOTE:  Supported on VOSS only.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_COMPATIBILITY_MODE_STATE, True,
                                           "IGMP Snooping Compatibility Mode is enabled on vlan {vlan} on "
                                           "{device_name}.",
                                           "IGMP Snooping Compatibility Mode IS NOT enabled on vlan {vlan} on "
                                           "{device_name}!",
                                           **kwargs)

    def igmp_verify_snooping_compatibility_mode_disabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan on which IGMP snooping is being enabled.

        Verifies that IGMP snooping Compatibility Mode is disabled on a given VLAN.
        NOTE:  Supported on VOSS only.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_COMPATIBILITY_MODE_STATE, False,
                                           "IGMP Snooping Compatibility Mode is disabled on vlan {vlan} on "
                                           "{device_name}.",
                                           "IGMP Snooping Compatibility Mode IS NOT disabled on vlan {vlan} on "
                                           "{device_name}!",
                                           **kwargs)

    def igmp_verify_snooping_explicit_host_tracking_enabled_on_vlan(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan on which IGMP snooping is being enabled.

        Verifies that IGMP snooping Explicit Host Tracking is enabled on a given VLAN.
        NOTE:  Supported on VOSS only.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_EXPLICIT_HOST_TRACKING_STATE,
                                           True, "IGMP Snooping Explicit Host Tracking is enabled on vlan {vlan} "
                                                 "on {device_name}.",
                                           "IGMP Snooping Explicit Host Tracking IS NOT enabled on vlan {vlan} "
                                           "on {device_name}!",
                                           **kwargs)

    def igmp_verify_snooping_explicit_host_tracking_disabled_on_vlan(self, device_name, vlan='', vlan_name='',
                                                                     **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan on which IGMP snooping is being enabled.

        Verifies that IGMP snooping Explicit Host Tracking is disabled on a given VLAN.
        NOTE:  Supported on VOSS only.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_IGMP_SNOOPING_EXPLICIT_HOST_TRACKING_STATE,
                                           False, "IGMP Snooping Explicit Host Tracking is disabled on vlan "
                                                  "{vlan} on {device_name}.",
                                           "IGMP Snooping Explicit Host Tracking IS NOT disabled on vlan {vlan} "
                                           "on {device_name}!",
                                           **kwargs)

    def igmp_verify_group_exists(self, device_name, group='', vlan='', vlan_name='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [group]       - The IGMP group to verify.
        [vlan]        - The vlan on which the IGMP group should exist on.
        [port]        - The port on which IGMP group should exist on.
        Verifies that an IGMP group exists on a given vlan and port.
        """
        args = {"group": group,
                "vlan": vlan,
                "vlan_name": vlan_name,
                "port": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GROUP,
                                           self.parse_const.VERIFY_IGMP_GROUP, True,
                                           "IGMP Group {group} exists on vlan {vlan} port {port} on {device_name}.",
                                           "IGMP Group {group} does NOT exist on vlan {vlan} port {port} on "
                                           "{device_name}!",
                                           **kwargs)

    def igmp_verify_group_does_not_exist(self, device_name, group='', vlan='', vlan_name='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [group]       - The IGMP group to verify.
        [vlan]        - The vlan on which the IGMP group should exist on.
        [port]        - The port on which IGMP group should exist on.
        Verifies that an IGMP group does not exist on a given vlan and port.
        """
        args = {"group": group,
                "vlan": vlan,
                "vlan_name": vlan_name,
                "port": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GROUP,
                                           self.parse_const.VERIFY_IGMP_GROUP, False,
                                           "IGMP Group {group} does not exist on vlan {vlan} port {port} on "
                                           "{device_name}.",
                                           "IGMP Group {group} EXISTS on vlan {vlan} port {port} on {device_name}!",
                                           **kwargs)
