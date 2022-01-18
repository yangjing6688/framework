"""
Keyword class for all vrf cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.VrfConstants import \
    VrfConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.VrfConstants import \
    VrfConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementVrfGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementVrfGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "vrf"

    def vrf_create_router(self, device_name, vrf_name='', **kwargs):
        """
        Description: Creates an IP VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ROUTER,
                                    **kwargs)

    def vrf_create_router_with_vrfid(self, device_name, vrf_name='', vrfid='', **kwargs):
        """
        Description: Creates an IP VRF with a specified VRF ID.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name,
            "vrfid": vrfid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ROUTER_WITH_VRFID,
                                    **kwargs)

    def vrf_delete_router(self, device_name, vrf_name='', **kwargs):
        """
        Description: Removes an IP VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_ROUTER,
                                    **kwargs)

    def vrf_enable_trap(self, device_name, vrf_name='', **kwargs):
        """
        Description: Enables VRF Traps.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_TRAP,
                                    **kwargs)

    def vrf_disable_trap(self, device_name, vrf_name='', **kwargs):
        """
        Description: Disables VRF Traps.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_TRAP,
                                    **kwargs)

    def vrf_enable_max_routes_trap(self, device_name, vrf_name='', **kwargs):
        """
        Description: Enables VRF Max-Routes Trap.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_MAX_ROUTES_TRAP,
                                    **kwargs)

    def vrf_disable_max_routes_trap(self, device_name, vrf_name='', **kwargs):
        """
        Description: Disables VRF Max-Routes Trap.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_MAX_ROUTES_TRAP,
                                    **kwargs)

    def vrf_enable_mvpn(self, device_name, vrf_name='', **kwargs):
        """
        Description: Enables multicast (MVPN) on the specified VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_MVPN,
                                    **kwargs)

    def vrf_disable_mvpn(self, device_name, vrf_name='', **kwargs):
        """
        Description: Disables multicast (MVPN) on the specified VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_MVPN,
                                    **kwargs)

    def vrf_enable_ipv6_max_routes_trap(self, device_name, vrf_name='', **kwargs):
        """
        Description: Enables VRF IPv6-Max-Routes Trap.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPV6_MAX_ROUTES_TRAP,
                                    **kwargs)

    def vrf_disable_ipv6_max_routes_trap(self, device_name, vrf_name='', **kwargs):
        """
        Description: Disables VRF IPv6-Max-Routes Trap.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPV6_MAX_ROUTES_TRAP,
                                    **kwargs)

    def vrf_enable_ipvpn(self, device_name, vrf_name='', **kwargs):
        """
        Description: Enables Ipvpn on the specified Router VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPVPN,
                                    **kwargs)

    def vrf_disable_ipvpn(self, device_name, vrf_name='', **kwargs):
        """
        Description: Disables Ipvpn on the specified Router VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPVPN,
                                    **kwargs)

    def vrf_enable_isis_redistribute_direct(self, device_name, vrf_name='', **kwargs):
        """
        Description: Enables the specified router VRF for redistribute isis direct routes.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ISIS_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def vrf_disable_isis_redistribute_direct(self, device_name, vrf_name='', **kwargs):
        """
        Description: Disables the specified router VRF forr redistribute isis direct routes.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ISIS_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def vrf_set_mvpn_fwd_cache_timeout(self, device_name, vrf_name='', timeout='', **kwargs):
        """
        Description: Sets the mvpn forwarding cache timout for the specified VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "timeout": timeout,
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MVPN_FWD_CACHE_TIMEOUT,
                                    **kwargs)

    def vrf_set_max_routes(self, device_name, vrf_name='', num_max_routes='', **kwargs):
        """
        Description: Sets the maximum number of routes for an IP VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "num_max_routes": num_max_routes,
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAX_ROUTES,
                                    **kwargs)

    def vrf_set_ipv6_max_routes(self, device_name, vrf_name='', num_max_routes='', **kwargs):
        """
        Description: Sets the maximum number of routes for an IPv6 VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "num_max_routes": num_max_routes,
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV6_MAX_ROUTES,
                                    **kwargs)

    def vrf_set_name(self, device_name, new_vrf_name='', vrf_name='', **kwargs):
        """
        Description: Renames and existing IP VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "new_vrf_name": new_vrf_name,
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NAME,
                                    **kwargs)

    def vrf_set_vrfid(self, device_name, vrf_name='', vrfid='', **kwargs):
        """
        Description: Re-assigns a new VRF ID to an existing VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name,
            "vrfid": vrfid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VRFID,
                                    **kwargs)

    def vrf_set_interface_vlan(self, device_name, vrf_name='', interface='', **kwargs):
        """
        Description: Assigns a VRF to an Interface Vlan.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface,
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INTERFACE_VLAN,
                                    **kwargs)

    def vrf_clear_interface_vlan(self, device_name, vrf_name='', interface='', **kwargs):
        """
        Description: Removes a VRF from an Interface Vlan.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface,
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_INTERFACE_VLAN,
                                    **kwargs)

    def vrf_set_ipvpn(self, device_name, vrf_name='', **kwargs):
        """
        Description: Creates an IP VPN instance on a VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPVPN,
                                    **kwargs)

    def vrf_set_isid(self, device_name, vrf_name='', i_sid='', **kwargs):
        """
        Description: Sets an i-sid for the specified Vrf.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "i_sid": i_sid,
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISID,
                                    **kwargs)

    def vrf_set_isis_redistribute_direct(self, device_name, vrf_name='', **kwargs):
        """
        Description: Sets the specified router VRF to redistribute isis direct routes.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISIS_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def vrf_clear_isis_redistribute_direct(self, device_name, vrf_name='', **kwargs):
        """
        Description: Clears the specified router VRF from redistributing isis direct routes.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ISIS_REDISTRIBUTE_DIRECT,
                                    **kwargs)

    def vrf_set_isis_redistribute_direct_apply(self, device_name, vrf_name='', **kwargs):
        """
        Description: Applies redistribute isis direct routes to the VRF.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vrf_name": vrf_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISIS_REDISTRIBUTE_DIRECT_APPLY,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def vrf_verify_name(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name to verify.

        Verifies the IP VRF name.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NAME,
                                           self.parse_const.VERIFY_VRF_NAME, True,
                                           "The IP VRF name is {vrf_name}.",
                                           "The IP VRF name is NOT {vrf_name}.!",
                                           **kwargs)

    def vrf_verify_vrfid(self, device_name, vrf_name='', vrfid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.
        [vrfid]       - The IP VRF VRFID to verify.

        Verifies the IP VRF VRFID.
        """
        args = {"vrf_name": vrf_name,
                "vrfid": vrfid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NAME,
                                           self.parse_const.VERIFY_VRF_VRFID, True,
                                           "The VRF ID for IP VRF {vrf_name} is correctly set to {vrfid}.",
                                           "The VRF ID for IP VRF {vrf_name} IS NOT set to {vrfid}.!",
                                           **kwargs)

    def vrf_verify_mvpn_fwd_cache_timeout(self, device_name, vrf_name='', timeout='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.
        [timeout]     - The router vrf mvpn forwarding cache timeout value to verify.

        Verifies the router vrf mvpn forwarding cache timeout value for the specified VRF.
        """
        args = {"vrf_name": vrf_name,
                "timeout": timeout}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MVPN,
                                           self.parse_const.VERIFY_VRF_MVPN_FWD_CACHE_TIMEOUT, True,
                                           "The mvpn forwarding cache timeout value for router VRF {vrf_name} is "
                                           "correctly set to {timeout}.",
                                           "The mvpn forwarding cache timeout value for router VRF {vrf_name} IS NOT "
                                           "correctly set to {timeout}.!",
                                           **kwargs)

    def vrf_verify_name_and_vrfid(self, device_name, vrf_name='', vrfid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name to verify.
        [vrfid]       - The IP VRF VRF ID to verify.

        Verifies the IP VRF NAME and VRFID.
        """
        args = {"vrf_name": vrf_name,
                "vrfid": vrfid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NAME,
                                           self.parse_const.VERIFY_VRF_NAME_AND_VRFID, True,
                                           "The IP VRF name {vrf_name} and VRF ID {vrfid} is correctly "
                                           "set on {device_name}.",
                                           "The IP VRF name {vrf_name} and VRF ID {vrfid} IS NOT correctly "
                                           "set on {device_name}!",
                                           **kwargs)

    def vrf_verify_name_does_not_exist(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.

        Verifies the specified VRF does not exist on the device.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.VERIFY_VRF_NAME, False,
                                           "VRF {vrf_name} does not exist on {device_name}.",
                                           "VRF {vrf_name} Exists on {device_name}!",
                                           **kwargs)

    def vrf_verify_vrfid_does_not_exist(self, device_name, vrf_name='', vrfid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrfid]       - The IP VRF VRFID to verify.

        Verifies the specified VRF ID does not exist on the device.
        """
        args = {"vrf_name": vrf_name,
                "vrfid": vrfid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VRFIDS,
                                           self.parse_const.VERIFY_VRF_VRFID, False,
                                           "VRF ID {vrfid} does not exist on {device_name}.",
                                           "VRF ID {vrfid} IS present on {device_name}!",
                                           **kwargs)

    def vrf_verify_trap_enabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.

        Verifies that VRF Trap is enabled for the specified VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAX_ROUTES_NAME,
                                           self.parse_const.VERIFY_VRF_TRAP_ENABLED, True,
                                           "VRF Trap is enabled for IP VRF {vrf_name} on {device_name}.",
                                           "VRF Trap is NOT enabled for IP VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_trap_disabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.

        Verifies that VRF Trap is disabled for the specified VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAX_ROUTES_NAME,
                                           self.parse_const.VERIFY_VRF_TRAP_ENABLED, False,
                                           "VRF Trap is not enabled for IP VRF {vrf_name} on {device_name}",
                                           "VRF Trap IS enabled for IP VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_mvpn_enabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.

        Verifies that multicast (mvpn) is enabled on the specified IP VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MVPN,
                                           self.parse_const.VERIFY_VRF_MVPN_ENABLED, True,
                                           "Mvpn is enabled on IP VRF {vrf_name} on {device_name}.",
                                           "Mvpn IS NOT enabled on IP VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_mvpn_disabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.

        Verifies that multicast (mvpn) is disabled on the specified IP VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MVPN,
                                           self.parse_const.VERIFY_VRF_MVPN_DISABLED, False,
                                           "Mvpn is disabled on IP VRF {vrf_name} on {device_name}.",
                                           "Mvpn IS NOT disabled on IP VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_max_routes_trap_enabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.

        Verifies that VRF Max-Routes Trap is enabled for the specified VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAX_ROUTES_NAME,
                                           self.parse_const.VERIFY_VRF_MAX_ROUTES_TRAP_ENABLED, True,
                                           "VRF Max-Routes Trap is enabled for IP VRF {vrf_name} on {device_name}.",
                                           "VRF Max-Routes Trap is NOT enabled for IP VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_max_routes_trap_disabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.

        Verifies that VRF Max-Routes Trap is disabled for the specified VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAX_ROUTES_NAME,
                                           self.parse_const.VERIFY_VRF_MAX_ROUTES_TRAP_ENABLED, False,
                                           "VRF Max-Routes Trap is not enabled for IP VRF {vrf_name} on {device_name}",
                                           "VRF Max-Routes Trap IS enabled for IP VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_ipv6_max_routes_trap_enabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.

        Verifies that the VRF IPv6 Max-Routes Trap is enabled for the specified VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_MAX_ROUTES_NAME,
                                           self.parse_const.VERIFY_VRF_IPV6_MAX_ROUTES_TRAP_ENABLED, True,
                                           "The VRF IPv6 Max-Routes Trap is enabled for IP VRF {vrf_name} "
                                           "on {device_name}.",
                                           "The VRF IPv6 Max-Routes Trap is NOT enabled for IP VRF {vrf_name} "
                                           "on {device_name}!",
                                           **kwargs)

    def vrf_verify_ipv6_max_routes_trap_disabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The IP VRF name.

        Verifies that VRF IPv6 Max-Routes Trap is disabled for the specified VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_MAX_ROUTES_NAME,
                                           self.parse_const.VERIFY_VRF_IPV6_MAX_ROUTES_TRAP_ENABLED, False,
                                           "The VRF IPv6 Max-Routes Trap is not enabled for IP VRF {vrf_name} "
                                           "on {device_name}",
                                           "The VRF IPv6 Max-Routes Trap IS enabled for IP VRF {vrf_name} "
                                           "on {device_name}!",
                                           **kwargs)

    def vrf_verify_max_routes(self, device_name, vrf_name='', num_max_routes='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.
        [num_max_routes]  - The IP VRF Max-Routes to verify.

        Verifies the IP VRF Max-Routes value is correctly set for the specified VRF Name.
        """
        args = {"vrf_name": vrf_name,
                "num_max_routes": num_max_routes}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAX_ROUTES_NAME,
                                           self.parse_const.VERIFY_VRF_MAX_ROUTES, True,
                                           "The VRF Max-Routes for IP VRF {vrf_name} is correctly set to "
                                           "{num_max_routes} on {device_name}.",
                                           "The VRF Max-Routes for IP VRF {vrf_name} IS NOT correctly set to "
                                           "{num_max_routes} on {device_name}!",
                                           **kwargs)

    def vrf_verify_ipv6_max_routes(self, device_name, vrf_name='', num_max_routes='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.
        [num_max_routes]  - The IP VRF Max-Routes to verify.

        Verifies the IP VRF IPv6 Max-Routes value is correctly set for the specified VRF Name.
        """
        args = {"vrf_name": vrf_name,
                "num_max_routes": num_max_routes}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_MAX_ROUTES_NAME,
                                           self.parse_const.VERIFY_VRF_IPV6_MAX_ROUTES, True,
                                           "The VRF IPv6 Max-Routes for IP VRF {vrf_name} is correctly set to "
                                           "{num_max_routes} on {device_name}.",
                                           "The VRF IPv6 Max-Routes for IP VRF {vrf_name} IS NOT correctly set to "
                                           "{num_max_routes} on {device_name}!",
                                           **kwargs)

    def vrf_verify_interface_vlan_assigned(self, device_name, vrf_name='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.
        [vlan]            - The Interface Vlan to verify.

        Verifies the IP VRF is assigned to the specified Interface Vlan.
        """
        args = {"vrf_name": vrf_name,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_VLAN,
                                           self.parse_const.VERIFY_VRF_IS_ASSIGNED_TO_INTERFACE_VLAN, True,
                                           "VRF {vrf_name} is correctly assigned to vlan {vlan} on {device_name}.",
                                           "VRF {vrf_name} IS NOT correctly set to vlan {vlan} on {device_name}!",
                                           **kwargs)

    def vrf_verify_interface_vlan_not_assigned(self, device_name, vrf_name='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.
        [vlan]            - The Interface Vlan to verify.

        Verifies the IP VRF is not assigned to the specified Interface Vlan.
        """
        args = {"vrf_name": vrf_name,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE_VLAN,
                                           self.parse_const.VERIFY_VRF_IS_ASSIGNED_TO_INTERFACE_VLAN, False,
                                           "VRF {vrf_name} is not assigned to vlan {vlan} on {device_name}.",
                                           "VRF {vrf_name} IS assigned to vlan {vlan} on {device_name}!",
                                           **kwargs)

    def vrf_verify_ipvpn(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.

        Verifies Ipvpn is set for a specified Router VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPVPN,
                                           self.parse_const.VERIFY_ROUTER_VRF_IPVPN_IS_SET, True,
                                           "IPVPN is set for VRF {vrf_name} on {device_name}.",
                                           "IPVPN IS NOT set for VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_isid(self, device_name, vrf_name='', i_sid='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.
        [i_sid]           - The i-sid that should be set for the specified VRF.

        Verifies the specified i-sid is set for the VRF.
        """
        args = {"vrf_name": vrf_name,
                "i_sid": i_sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPVPN,
                                           self.parse_const.VERIFY_ROUTER_VRF_ISID_IS_SET, True,
                                           "I-SID {i_sid} is correctly set for VRF {vrf_name} on {device_name}.",
                                           "I-SID {i_sid} IS NOT correctly set for VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_ipvpn_enabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.

        Verifies Ipvpn is Enabled on the specified Router VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPVPN,
                                           self.parse_const.VERIFY_ROUTER_VRF_IPVPN_IS_ENABLED, True,
                                           "IPVPN is Enabled for VRF {vrf_name} on {device_name}.",
                                           "IPVPN IS NOT Enabled for VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_ipvpn_disabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.

        Verifies Ipvpn is Disabled on the specified Router VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPVPN,
                                           self.parse_const.VERIFY_ROUTER_VRF_IPVPN_IS_ENABLED, False,
                                           "IPVPN is Disabled for VRF {vrf_name} on {device_name}.",
                                           "IPVPN IS NOT Disabled for VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_isis_redistribute_direct(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.

        Verifies redistribute isis direct routes is set on the specified router VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_REDISTRIBUTE_DIRECT,
                                           self.parse_const.VERIFY_ROUTER_VRF_ISIS_REDISTRIBUTE_DIRECT, True,
                                           "ISIS Redistribute Direct is set for Router VRF {vrf_name} on "
                                           "{device_name}.",
                                           "ISIS Redistribute Direct is NOT set for VRF {vrf_name} on {device_name}!",
                                           **kwargs)

    def vrf_verify_isis_redistribute_direct_cleared(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.

        Verifies redistribute isis direct routes is NOT set on the specified router VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_REDISTRIBUTE_DIRECT,
                                           self.parse_const.VERIFY_ROUTER_VRF_ISIS_REDISTRIBUTE_DIRECT, False,
                                           "ISIS Redistribute Direct is not set for Router VRF {vrf_name} on "
                                           "{device_name}.",
                                           "ISIS Redistribute Direct IS set for Router VRF {vrf_name} on "
                                           "{device_name}!",
                                           **kwargs)

    def vrf_verify_isis_redistribute_direct_enabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.

        Verifies redistribute isis direct routes is Enabled on the specified router VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_REDISTRIBUTE_DIRECT,
                                           self.parse_const.VERIFY_ROUTER_VRF_ISIS_REDISTRIBUTE_DIRECT_ENABLED, True,
                                           "ISIS Redistribute Direct is enabled for Router VRF {vrf_name} on "
                                           "{device_name}.",
                                           "ISIS Redistribute Direct is NOT enabled for VRF {vrf_name} on "
                                           "{device_name}!",
                                           **kwargs)

    def vrf_verify_isis_redistribute_direct_disabled(self, device_name, vrf_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [vrf_name]        - The IP VRF name.

        Verifies redistribute isis direct routes is Enabled on the specified router VRF.
        """
        args = {"vrf_name": vrf_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISIS_REDISTRIBUTE_DIRECT,
                                           self.parse_const.VERIFY_ROUTER_VRF_ISIS_REDISTRIBUTE_DIRECT_ENABLED, False,
                                           "ISIS Redistribute Direct is disabled for Router VRF {vrf_name} on "
                                           "{device_name}.",
                                           "ISIS Redistribute Direct is NOT disabled for VRF {vrf_name} on "
                                           "{device_name}!",
                                           **kwargs)
