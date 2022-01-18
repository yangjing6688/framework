"""
Keyword class for all bgp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.BgpConstants import \
    BgpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.BgpConstants import \
    BgpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementBgpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementBgpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "bgp"

    def bgp_enable_global(self, device_name, asnum='', **kwargs):
        """
        Description: Enables the BGP protocol.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "asnum": asnum
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GLOBAL,
                                    **kwargs)

    def bgp_disable_global(self, device_name, asnum='', **kwargs):
        """
        Description: Disables the BGP protocol.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "asnum": asnum
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GLOBAL,
                                    **kwargs)

    def bgp_create_as(self, device_name, asnum='', **kwargs):
        """
        Description: Configures the BGP AS-number.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            REST: EXOS
        """
        args = {
            "asnum": asnum
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_AS,
                                    **kwargs)

    def bgp_delete_as(self, device_name, asnum='', **kwargs):
        """
        Description: Unconfigures the BGP AS-number.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            REST: EXOS
        """
        args = {
            "asnum": asnum
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_AS,
                                    **kwargs)

    def bgp_set_router_id(self, device_name, rtrid='', asnum='', **kwargs):
        """
        Description: Configures the Router-ID on the DUT.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            REST: EXOS
        """
        args = {
            "asnum": asnum,
            "rtrid": rtrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ROUTER_ID,
                                    **kwargs)

    def bgp_clear_router_id(self, device_name, answer='', asnum='', **kwargs):
        """
        Description: Clears the Router-ID on the DUT.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            REST: EXOS
        """
        args = {
            "answer": answer,
            "asnum": asnum
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ROUTER_ID,
                                    **kwargs)

    def bgp_create_neighbor(self, device_name, ip='', remoteas='', asnum='', **kwargs):
        """
        Description: Creates a BGP neighbor entry. The asnum or remote-as is required at the time of neighbor creation.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            REST: EXOS
        """
        args = {
            "asnum": asnum,
            "ip": ip,
            "remoteas": remoteas
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_NEIGHBOR,
                                    **kwargs)

    def bgp_create_neighbor_link_local(self, device_name, ip='', remoteas='', asnum='', vlan_eos='', vlan_exos='',
                                       **kwargs):
        """
        Description: Creates a link-local BGP neighbor entry. The remote-as is required at the time of neighbor
                     creation.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "asnum": asnum,
            "ip": ip,
            "remoteas": remoteas,
            "vlan_eos": vlan_eos,
            "vlan_exos": vlan_exos
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_NEIGHBOR_LINK_LOCAL,
                                    **kwargs)

    def bgp_delete_neighbor(self, device_name, ip='', asnum='', remoteas='', **kwargs):
        """
        Description: Removes a BGP neighbor entry.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            REST: EXOS
        """
        args = {
            "asnum": asnum,
            "ip": ip,
            "remoteas": remoteas
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_NEIGHBOR,
                                    **kwargs)

    def bgp_delete_neighbor_link_local(self, device_name, ip='', remoteas='', asnum='', vlan_eos='', vlan_exos='',
                                       **kwargs):
        """
        Description: Deletes a link-local BGP neighbor entry. The remote-as is required for EOS systems.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "asnum": asnum,
            "ip": ip,
            "remoteas": remoteas,
            "vlan_eos": vlan_eos,
            "vlan_exos": vlan_exos
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_NEIGHBOR_LINK_LOCAL,
                                    **kwargs)

    def bgp_enable_neighbor(self, device_name, ip='', asnum='', **kwargs):
        """
        Description: Enables the BGP Neighbor.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            REST: EXOS
        """
        args = {
            "asnum": asnum,
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_NEIGHBOR,
                                    **kwargs)

    def bgp_enable_neighbor_link_local(self, device_name, ip='', asnum='', vlan_eos='', vlan_exos='', **kwargs):
        """
        Description: Enables the link-local BGP Neighbor.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "asnum": asnum,
            "ip": ip,
            "vlan_eos": vlan_eos,
            "vlan_exos": vlan_exos
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_NEIGHBOR_LINK_LOCAL,
                                    **kwargs)

    def bgp_disable_neighbor(self, device_name, ip='', asnum='', **kwargs):
        """
        Description: Disables the BGP Neighbor.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
            REST: EXOS
        """
        args = {
            "asnum": asnum,
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_NEIGHBOR,
                                    **kwargs)

    def bgp_disable_neighbor_link_local(self, device_name, ip='', asnum='', vlan_eos='', vlan_exos='', **kwargs):
        """
        Description: Disables the link-local BGP Neighbor.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "asnum": asnum,
            "ip": ip,
            "vlan_eos": vlan_eos,
            "vlan_exos": vlan_exos
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_NEIGHBOR_LINK_LOCAL,
                                    **kwargs)

    def bgp_set_redistribute(self, device_name, protocol='', asnum='', **kwargs):
        """
        Description: Configures BGP to redistribute routes from another protocol.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "asnum": asnum,
            "protocol": protocol
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_REDISTRIBUTE,
                                    **kwargs)

    def bgp_clear_redistribute(self, device_name, protocol='', asnum='', **kwargs):
        """
        Description: Clears the BGP redistribution of routes from another protocol.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "asnum": asnum,
            "protocol": protocol
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_REDISTRIBUTE,
                                    **kwargs)

    def bgp_set_neighbor_password(self, device_name, ip='', password='', asnum='', **kwargs):
        """
        Description: Sets a password for the TCP session between the DUT and Neighbor.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "asnum": asnum,
            "ip": ip,
            "password": password
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NEIGHBOR_PASSWORD,
                                    **kwargs)

    def bgp_clear_neighbor(self, device_name, ip='', **kwargs):
        """
        Description: Clear the BGP peer relationship between the DUT and the Neighbor.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_NEIGHBOR,
                                    **kwargs)

    def bgp_clear_neighbor_all(self, device_name, **kwargs):
        """
        Description: Clears the BGP peer relationship for all neighbors.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_NEIGHBOR_ALL,
                                    **kwargs)

    def bgp_enable_neighbor_capability(self, device_name, ip='', capability='', family='', **kwargs):
        """
        Description: Enables the Address-family for the BGP Neighbor.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "capability": capability,
            "family": family,
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_NEIGHBOR_CAPABILITY,
                                    **kwargs)

    def bgp_disable_neighbor_capability(self, device_name, ip='', capability='', family='', **kwargs):
        """
        Description: Disables the Address-family for the BGP Neighbor.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {
            "capability": capability,
            "family": family,
            "ip": ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_NEIGHBOR_CAPABILITY,
                                    **kwargs)

    def bgp_set_auto_peering(self, device_name, asnum='', rtrid='', **kwargs):
        """
        Description: Configures the Auto-Peering feature.

        Supported Agents and OS:
            CLI: EXOS
            REST: EXOS
        """
        args = {
            "asnum": asnum,
            "rtrid": rtrid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_AUTO_PEERING,
                                    **kwargs)

    def bgp_clear_auto_peering(self, device_name, **kwargs):
        """
        Description: Un-configures the Auto-Peering feature.

        Supported Agents and OS:
            CLI: EXOS
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_AUTO_PEERING,
                                    **kwargs)

    def bgp_set_confederation_id(self, device_name, confed_id='', **kwargs):
        """
        Description: Configures confederation ID.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "confed_id": confed_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CONFEDERATION_ID,
                                    **kwargs)

    def bgp_clear_confederation_id(self, device_name, confed_id='', **kwargs):
        """
        Description: Clears confederation ID.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "confed_id": confed_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_CONFEDERATION_ID,
                                    **kwargs)

    def bgp_set_confederation_peer_member_as(self, device_name, member_as='', **kwargs):
        """
        Description: Sets confederation peer member AS.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "member_as": member_as
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_CONFEDERATION_PEER_MEMBER_AS,
                                    **kwargs)

    def bgp_clear_confederation_peer_member_as(self, device_name, member_as='', **kwargs):
        """
        Description: Clears confederation peer member AS.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "member_as": member_as
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_CONFEDERATION_PEER_MEMBER_AS,
                                    **kwargs)

    def bgp_set_graceful_restart_time(self, device_name, restart_time='', **kwargs):
        """
        Description: Sets graceful restart time.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "restart_time": restart_time
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_GRACEFUL_RESTART_TIME,
                                    **kwargs)

    def bgp_clear_graceful_restart_time(self, device_name, **kwargs):
        """
        Description: Clears graceful restart time.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_GRACEFUL_RESTART_TIME,
                                    **kwargs)

    def bgp_set_graceful_stale_route_time(self, device_name, stale_route_time='', **kwargs):
        """
        Description: Sets graceful stale route time.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "stale_route_time": stale_route_time
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_GRACEFUL_STALE_ROUTE_TIME,
                                    **kwargs)

    def bgp_clear_graceful_stale_route_time(self, device_name, **kwargs):
        """
        Description: Clears graceful stale route time.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_GRACEFUL_STALE_ROUTE_TIME,
                                    **kwargs)

    def bgp_set_maximum_paths(self, device_name, paths='', **kwargs):
        """
        Description: Sets maximum paths.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "paths": paths
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAXIMUM_PATHS,
                                    **kwargs)

    def bgp_clear_maximum_paths(self, device_name, **kwargs):
        """
        Description: Clears maximum paths.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MAXIMUM_PATHS,
                                    **kwargs)

    def bgp_set_neighbor_keep_alive_interval_and_hold_time(self, device_name, hold_time='', keep_alive_time='',
                                                           neighbor_ip='', **kwargs):
        """
        Description: set_neighbor_keep_alive_interval_and_hold_time.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "hold_time": hold_time,
            "keep_alive_time": keep_alive_time,
            "neighbor_ip": neighbor_ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NEIGHBOR_KEEP_ALIVE_INTERVAL_AND_HOLD_TIME,
                                    **kwargs)

    def bgp_set_neighbor_transport_address(self, device_name, local_address='', neighbor_ip='', **kwargs):
        """
        Description: set_neighbor_transport_address.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "local_address": local_address,
            "neighbor_ip": neighbor_ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NEIGHBOR_TRANSPORT_ADDRESS,
                                    **kwargs)

    def bgp_enable_graceful_restart(self, device_name, **kwargs):
        """
        Description: Enables graceful restart.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_GRACEFUL_RESTART,
                                    **kwargs)

    def bgp_disable_graceful_restart(self, device_name, **kwargs):
        """
        Description: Disables graceful restart.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_GRACEFUL_RESTART,
                                    **kwargs)

    def bgp_enable_allow_multiple_as(self, device_name, **kwargs):
        """
        Description: Enables allow multiple AS.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ALLOW_MULTIPLE_AS,
                                    **kwargs)

    def bgp_disable_allow_multiple_as(self, device_name, **kwargs):
        """
        Description: Disables allow multiple AS.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ALLOW_MULTIPLE_AS,
                                    **kwargs)

    def bgp_enable_always_compare_med(self, device_name, **kwargs):
        """
        Description: Enables always compare med.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ALWAYS_COMPARE_MED,
                                    **kwargs)

    def bgp_disable_always_compare_med(self, device_name, **kwargs):
        """
        Description: Disable always compare med.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ALWAYS_COMPARE_MED,
                                    **kwargs)

    def bgp_enable_advertise_inactive_routes_ipv4_unicast(self, device_name, **kwargs):
        """
        Description: Enables advertise inactive routes v4 unicast.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ADVERTISE_INACTIVE_ROUTES_IPV4_UNICAST,
                                    **kwargs)

    def bgp_disable_advertise_inactive_routes_ipv4_unicast(self, device_name, **kwargs):
        """
        Description: Disables advertise inactive routes v4 unicast.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ADVERTISE_INACTIVE_ROUTES_IPV4_UNICAST,
                                    **kwargs)

    def bgp_enable_advertise_inactive_routes_l3vpn_ipv4_unicast(self, device_name, **kwargs):
        """
        Description: Enables advertise inactive routes v4 l3vpn unicast.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ADVERTISE_INACTIVE_ROUTES_L3VPN_IPV4_UNICAST,
                                    **kwargs)

    def bgp_disable_advertise_inactive_routes_l3vpn_ipv4_unicast(self, device_name, **kwargs):
        """
        Description: Disables advertise inactive routes v4 l3vpn unicast.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ADVERTISE_INACTIVE_ROUTES_L3VPN_IPV4_UNICAST,
                                    **kwargs)

    def bgp_enable_advertise_inactive_routes_ipv6_unicast(self, device_name, **kwargs):
        """
        Description: Enables advertise inactive routes v6 unicast.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ADVERTISE_INACTIVE_ROUTES_IPV6_UNICAST,
                                    **kwargs)

    def bgp_disable_advertise_inactive_routes_ipv6_unicast(self, device_name, **kwargs):
        """
        Description: Disables advertise inactive routes v6 unicast.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ADVERTISE_INACTIVE_ROUTES_IPV6_UNICAST,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def bgp_verify_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.

        Verifies that BGP is Enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_BGP_ENABLED, True,
                                           "BGP is ENABLED on {device_name}.",
                                           "BGP is NOT Enabled on {device_name}!",
                                           **kwargs)

    def bgp_verify_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.

        Verifies that BGP is Disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_BGP_DISABLED, True,
                                           "BGP is DISABLED on {device_name}.",
                                           "BGP is NOT Disabled on {device_name}!",
                                           **kwargs)

    def bgp_verify_as(self, device_name, asnum='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [asnum]       - The AS-number for BGP.

        Verifies the BGP AS-number.
        """
        args = {"asnum": asnum}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_BGP_AS, True,
                                           "BGP AS is correctly set to {asnum} on {device_name}.",
                                           "BGP AS IS NOT properly set to {asnum} on {device_name}!",
                                           **kwargs)

    def bgp_verify_as_does_not_exist(self, device_name, asnum='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [asnum]       - The AS-number for BGP.

        Verifies that a BGP AS-number does not exist.
        """
        args = {"asnum": asnum}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_BGP_AS, False,
                                           "BGP AS {asnum} does not exist on {device_name}.",
                                           "BGP AS {asnum} EXISTS on {device_name}!",
                                           **kwargs)

    def bgp_verify_routerid(self, device_name, rtrid='', asnum='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [rtrid]       - Router ID.
        [asnum]       - The AS of the local BGP router.

        Verifies the BGP Router-ID on the DUT.
        """
        args = {"rtrid": rtrid,
                "asnum": asnum if asnum is not None else "none",
                "bgp": "bgp"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_BGP_ROUTER_ID, True,
                                           "The BGP Router-ID is correctly set to {rtrid} on {device_name}.",
                                           "The BGP Router-ID IS NOT properly set to {rtrid} on {device_name}!",
                                           **kwargs)

    def bgp_verify_routerid_does_not_exist(self, device_name, rtrid='', asnum='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [rtrid]       - Router ID.
        [asnum]       - The AS of the local BGP router.

        Verifies the specified BGP Router-ID does not exist on the DUT.
        """
        args = {"rtrid": rtrid,
                "asnum": asnum if asnum is not None else "none",
                "bgp": "bgp"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_BGP_ROUTER_ID, False,
                                           "The BGP Router-ID {rtrid} does not exist on {device_name}.",
                                           "The BGP Router-ID {rtrid} STILL EXISTS on {device_name}!",
                                           **kwargs)

    def bgp_verify_auto_peering(self, device_name, peering_value="1", **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [peering_value] - The auto-peering value. 1 enabled, 0 disabled.  default is properly set to 1.

        Verifies the BGP auto-peering value on the DUT.
        Peering_value is not statically set to 1 for future scenarios where 2,3,etc.. could be used.
        """
        args = {"peering_value": peering_value}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_BGP_AUTO_PEERING, True,
                                           "The BGP auto-peering value is correctly set to {peering_value} on "
                                           "{device_name}.",
                                           "The BGP auto-peering val IS NOT properly set to {peering_value} on "
                                           "{device_name}!",
                                           **kwargs)

    def bgp_verify_auto_peering_disabled(self, device_name, **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.

        Verifies the BGP auto-peering value is set to 0 on the DUT.
        """
        args = {"peering_value": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_BGP_AUTO_PEERING, True,
                                           "The BGP auto-peering value is correctly set to {peering_value} on "
                                           "{device_name}.",
                                           "The BGP auto-peering val IS NOT properly set to {peering_value} on "
                                           "{device_name}!",
                                           **kwargs)

    def bgp_verify_neighbor_exists(self, device_name, ip='', asnum='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [ip]          - The IP Address of the BGP Neighbor.
        [asnum]       - The AS of the BGP Neighbor.

        Verifies that the BGP Neighbor specified exists
        """
        args = {"ip": ip,
                "asnum": asnum}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBORS,
                                           self.parse_const.CHECK_NEIGHBOR_EXISTS, True,
                                           "Found BGP Neighbor {ip} on {device_name}.",
                                           "Error: Did NOT find BGP Neighbor {ip} on {device_name}!",
                                           **kwargs)

    def bgp_verify_neighbor_does_not_exist(self, device_name, ip='', asnum='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [ip]          - The IP Address of the BGP Neighbor.
        [asnum]       - The AS of the BGP Neighbor.

        Verifies that the BGP Neighbor specified does not exist on the DUT
        """
        args = {"ip": ip,
                "asnum": asnum}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBORS,
                                           self.parse_const.CHECK_NEIGHBOR_EXISTS, False,
                                           "BGP Neighbor {ip} does not exist on {device_name}.",
                                           "BGP Neighbor {ip} STILL EXISTS on {device_name}!",
                                           **kwargs)

    def bgp_verify_route_exists(self, device_name, route='', nexthop='', peer='', vlan='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [route]       - The route being looked for.
        [nexthop]     - The expected nexthop for the route.
        [intf]        - The interface the nexthop should be out.

        Verifies the specified route exists.
        """
        args = {"route": route,
                "nexthop": nexthop,
                "peer": peer,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_ROUTES,
                                           self.parse_const.CHECK_ROUTE_EXISTS, True,
                                           "Route {route} exists on {device_name}.",
                                           "Route {route} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def bgp_verify_route_does_not_exist(self, device_name, route='', nexthop='', peer='', vlan='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [route]       - The route being looked for.
        [nexthop]     - The expected nexthop for the route.
        [intf]        - The interface the nexthop should be out.

        Verifies the specified route does NOT exist.
        """
        args = {"route": route,
                "nexthop": nexthop,
                "peer": peer,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_ROUTES,
                                           self.parse_const.CHECK_ROUTE_EXISTS, False,
                                           "Route {route} does not exist on {device_name}.",
                                           "Route {route} STILL exists on {device_name}!",
                                           **kwargs)

    def bgp_verify_neighbor_state(self, device_name, neighbor='', state='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [neighbor]    - The Neighbor's state to inspect.
        [state]       - The expected state of the neighbor.

        Verifies the neighbor state of a specified peer.
        """
        args = {"neighbor": neighbor,
                "state": state}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBORS,
                                           self.parse_const.CHECK_NEIGHBOR_STATE, True,
                                           "Neighbor {neighbor} on {device_name} is {state}.",
                                           "Neighbor {neighbor} on {device_name} is NOT {state}!",
                                           **kwargs)

    def bgp_verify_linklocal_neighbor_state(self, device_name, neighbor='', vlan='', state='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [neighbor]    - The Neighbor's state to inspect.
        [vlan]     - The expected vlan.
        [state]       - The expected state of the neighbor.

        Waits for the link-local peer to enter the specified state.
        """
        args = {"neighbor": neighbor,
                "state": state,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BGP_NEIGHBORS,
                                           self.parse_const.CHECK_LINKLOCAL_NEIGHBOR_STATE, True,
                                           "Neighbor {neighbor} on {device_name} is {state}.",
                                           "Error: Timeout before neighbor reached {state}!",
                                           **kwargs)

    def bgp_verify_confederation_id(self, device_name, confed_id='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [confed_id]       - The confederation id to verify

        Verifies the specified confederation ID.
        """
        args = {"confed_id": confed_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CONFEDERATION,
                                           self.parse_const.CHECK_CONFEDERATION_ID, True,
                                           "Confederation ID {confed_id} exists on {device_name}.",
                                           "Confederation ID {confed_id} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def bgp_verify_confederation_peer_member_as_exists(self, device_name, peer='', exists='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [peer]       - The confederation peer to verify
        [exists]       - Does peer member exist

        Verifies the specified confederation peer iD.
        """
        args = {"peer": peer,
                'exists': exists}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CONFEDERATION,
                                           self.parse_const.CHECK_CONFEDERATION_PEER_MEMBER_AS, True,
                                           "Confederation ID {peer} exists on {device_name}.",
                                           "Confederation ID {peer} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def bgp_verify_graceful_restart(self, device_name, graceful_restart='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [graceful_restart]       - The value of graceful restart

        Verifies graceful restart value.
        """
        args = {"graceful_restart": graceful_restart}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GRACEFUL_RESTART,
                                           self.parse_const.CHECK_GRACEFUL_RESTART, True,
                                           "Graceful restart matches {graceful_restart} exists on {device_name}.",
                                           "Graceful restart DOES not match {graceful_restart} on {device_name}!",
                                           **kwargs)

    def bgp_verify_graceful_restart_time(self, device_name, restart_time='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [restart_time]       - The route being looked for.

        Verifies the restart_time.
        """
        args = {"restart_time": restart_time}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GRACEFUL_RESTART,
                                           self.parse_const.CHECK_GRACEFUL_RESTART_TIME, True,
                                           "Graceful restart matches {restart_time} exists on {device_name}.",
                                           "Graceful restart DOES not match {restart_time} on {device_name}!",
                                           **kwargs)

    def bgp_verify_graceful_stale_route_time(self, device_name, stale_route_time='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [stale_route_time]       - The stale route time to verify.

        Verifies the specified stale route time.
        """
        args = {"stale_route_time": stale_route_time}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GRACEFUL_RESTART,
                                           self.parse_const.CHECK_STALE_ROUTE_TIME, True,
                                           "Graceful restart matches {stale_route_time} exists on {device_name}.",
                                           "Graceful restart DOES not match {stale_route_time} on {device_name}!",
                                           **kwargs)

    def bgp_verify_allow_multiple_as(self, device_name, allow_multiple_as='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [allow_multiple_as]       - allow multiple as value.

        Verifies the specified allow multiple as value.
        """
        args = {"allow_multiple_as": allow_multiple_as}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_USE_MULTIPLE_PATHS,
                                           self.parse_const.CHECK_ALLOW_MULTIPLE_AS, True,
                                           "Graceful restart matches {allow_multiple_as} exists on {device_name}.",
                                           "Graceful restart DOES not match {allow_multiple_as} on {device_name}!",
                                           **kwargs)

    def bgp_verify_maximum_paths(self, device_name, maximum_paths='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [maximum_paths]       - The route being looked for.

        Verifies the value of maximum paths.
        """
        args = {"maximum_paths": maximum_paths}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_USE_MULTIPLE_PATHS,
                                           self.parse_const.CHECK_MAXIMUM_PATHS, True,
                                           "Graceful restart matches {maximum_paths} exists on {device_name}.",
                                           "Graceful restart DOES not match {maximum_paths} on {device_name}!",
                                           **kwargs)

    def bgp_verify_always_compare_med(self, device_name, always_compare_med='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [always_compare_med]       - always compare med

        Verifies the value of always compare med.
        """
        args = {"always_compare_med": always_compare_med}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALWAYS_COMPARE_MED,
                                           self.parse_const.CHECK_ALWAYS_COMPARE_MED, True,
                                           "always_compare_med matches {always_compare_med} exists on {device_name}.",
                                           "always_compare_med DOES not match {always_compare_med} on {device_name}!",
                                           **kwargs)

    def bgp_verify_advertise_inactive_routes_ipv4_unicast(self, device_name, advertise_inactive_routes='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [advertise_inactive_routes]       - Advertise inactive routes.

        Verifies the advertise inactive routes.
        """
        args = {"advertise_inactive_routes": advertise_inactive_routes}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ADVERTISE_INACTIVE_ROUTES_IPV4_UNICAST,
                                           self.parse_const.CHECK_ADVERTISE_INACTIVE_ROUTES, True,
                                           "Advertise inactive {advertise_inactive_routes} exists on {device_name}.",
                                           "Advertise inactive DOES not match {advertise_inactive_routes} on "
                                           "{device_name}!",
                                           **kwargs)

    def bgp_verify_advertise_inactive_routes_ipv6_unicast(self, device_name, advertise_inactive_routes='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [advertise_inactive_routes]       - Advertise inactive routes.

        Verifies the advertise inactive routes.
        """
        args = {"advertise_inactive_routes": advertise_inactive_routes}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ADVERTISE_INACTIVE_ROUTES_IPV6_UNICAST,
                                           self.parse_const.CHECK_ADVERTISE_INACTIVE_ROUTES, True,
                                           "Advertise inactive matches {advertise_inactive_routes} exists on "
                                           "{device_name}.",
                                           "Advertise inactive DOES not match {advertise_inactive_routes} on "
                                           "{device_name}!",
                                           **kwargs)

    def bgp_verify_advertise_inactive_routes_l3vpn_ipv4_unicast(self, device_name, advertise_inactive_routes='',
                                                                **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [advertise_inactive_routes]       - Advertise inactive routes.

        Verifies the advertise inactive routes..
        """
        args = {"advertise_inactive_routes": advertise_inactive_routes}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_ADVERTISE_INACTIVE_ROUTES_L3VPN_IPV4_UNICAST,
                                           self.parse_const.CHECK_ADVERTISE_INACTIVE_ROUTES, True,
                                           "Advertise inactive matches {advertise_inactive_routes} exists "
                                           "on {device_name}.",
                                           "Advertise inactive DOES not match {advertise_inactive_routes}"
                                           " on {device_name}!",
                                           **kwargs)

    def bgp_verify_neighbor_keep_alive_time(self, device_name, neighbor_ip='', keep_alive_interval='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [neighbor_ip]       - The neighbor ip.
        [keep_alive_interval]     - The keep_alive_interval.

        Verifies the specified keep alive time.
        """
        args = {"neighbor_ip": neighbor_ip,
                "keep_alive_interval": keep_alive_interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBOR_TIMERS,
                                           self.parse_const.CHECK_NEIGHBOR_KEEP_ALIVE_TIME, True,
                                           "keep_alive_interval matches {keep_alive_interval} exists on {device_name}.",
                                           "keep_alive_interval DOES not match {keep_alive_interval} on {device_name}!",
                                           **kwargs)

    def bgp_verify_neighbor_hold_time(self, device_name, neighbor_ip='', hold_time='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [neighbor_ip]       - The  neighbor ip.
        [hold_time]     - The hold time.

        Verifies the specified hold time for neighbor.
        """
        args = {"neighbor_ip": neighbor_ip,
                "hold_time": hold_time}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NEIGHBOR_TIMERS,
                                           self.parse_const.CHECK_NEIGHBOR_HOLD_TIME, True,
                                           "hold_time matches {hold_time} exists on {device_name}.",
                                           "hold_time DOES not match {hold_time} on {device_name}!",
                                           **kwargs)
