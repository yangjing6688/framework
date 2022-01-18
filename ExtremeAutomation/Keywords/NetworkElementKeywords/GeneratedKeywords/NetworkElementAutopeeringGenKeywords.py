"""
Keyword class for all autopeering cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.AutopeeringConstants import \
    AutopeeringConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.AutopeeringConstants import \
    AutopeeringConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementAutopeeringGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementAutopeeringGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "autopeering"

    def autopeering_set_anycast_mac(self, device_name, anycast_mac='', **kwargs):
        """
        Description: Sets anycast mac.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "anycast_mac": anycast_mac
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ANYCAST_MAC,
                                    **kwargs)

    def autopeering_set_anycast_mac_and_id(self, device_name, anycast_mac='', peer_id='', **kwargs):
        """
        Description: Sets anycast mac and id.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "anycast_mac": anycast_mac,
            "peer_id": peer_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ANYCAST_MAC_AND_ID,
                                    **kwargs)

    def autopeering_set_anycast_mac_and_route_target(self, device_name, anycast_mac='', route_target='', **kwargs):
        """
        Description: Sets anycast mac and route target.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "anycast_mac": anycast_mac,
            "route_target": route_target
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ANYCAST_MAC_AND_ROUTE_TARGET,
                                    **kwargs)

    def autopeering_clear_anycast_mac(self, device_name, **kwargs):
        """
        Description: Clears anycast mac.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ANYCAST_MAC,
                                    **kwargs)

    def autopeering_clear_anycast_mac_and_id(self, device_name, **kwargs):
        """
        Description: Clears anycast mac and id.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ANYCAST_MAC_AND_ID,
                                    **kwargs)

    def autopeering_clear_anycast_mac_and_route_target(self, device_name, **kwargs):
        """
        Description: Clears anycast mac and route target.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ANYCAST_MAC_AND_ROUTE_TARGET,
                                    **kwargs)

    def autopeering_set_host_address_host_vrf_static_route_network_static_route_next_hop(self, device_name,
                                                                                         host_address='', host_vrf='',
                                                                                         network='', next_hop='',
                                                                                         **kwargs):
        """
        Description: Configures host.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "host_address": host_address,
            "host_vrf": host_vrf,
            "network": network,
            "next_hop": next_hop
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_HOST_ADDRESS_HOST_VRF_STATIC_ROUTE_NETWORK_STATIC_ROUTE_NEXT_HOP,
                                    **kwargs)

    def autopeering_clear_all_hosts(self, device_name, **kwargs):
        """
        Description: Clears all hosts.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_HOSTS,
                                    **kwargs)

    def autopeering_clear_host(self, device_name, host_address='', host_vrf='', **kwargs):
        """
        Description: Clears a single host.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "host_address": host_address,
            "host_vrf": host_vrf
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_HOST,
                                    **kwargs)

    def autopeering_clear_static_route_from_host(self, device_name, host_address='', host_vrf='', mask_value='',
                                                 static_route_ip='', **kwargs):
        """
        Description: Clears a single static routes from host.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "host_address": host_address,
            "host_vrf": host_vrf,
            "mask_value": mask_value,
            "static_route_ip": static_route_ip
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_STATIC_ROUTE_FROM_HOST,
                                    **kwargs)

    def autopeering_set_service_nsi_nsi_type_vrf_address_ip_address_prefix_length(self, device_name, address_ip='',
                                                                                  address_prefix_length='', nsi='',
                                                                                  nsi_type='', vrf='', **kwargs):
        """
        Description: Configures Service.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "address_ip": address_ip,
            "address_prefix_length": address_prefix_length,
            "nsi": nsi,
            "nsi_type": nsi_type,
            "vrf": vrf
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_SERVICE_NSI_NSI_TYPE_VRF_ADDRESS_IP_ADDRESS_PREFIX_LENGTH,
                                    **kwargs)

    def autopeering_set_host_static_route(self, device_name, host_address='', host_vrf='', network_address='',
                                          nexthop_address='', **kwargs):
        """
        Description: Sets static route for host.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "host_address": host_address,
            "host_vrf": host_vrf,
            "network_address": network_address,
            "nexthop_address": nexthop_address
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_HOST_STATIC_ROUTE,
                                    **kwargs)

    def autopeering_clear_all_services(self, device_name, **kwargs):
        """
        Description: Clears all services.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_SERVICES,
                                    **kwargs)

    def autopeering_clear_service(self, device_name, nsi='', **kwargs):
        """
        Description: Clears a single services.

        Supported Agents and OS:
            REST: EXOS
        """
        args = {
            "nsi": nsi
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_SERVICE,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def autopeering_verify_anycast_mac(self, device_name, anycast_mac, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [anycast_mac] - The anycast mac to verify.

        Verifies the current anycast mac
        """
        args = {"anycast_mac": anycast_mac}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_AUTOPEERING_ANYCAST_MAC, True,
                                           "Anycast Mac is {anycast_mac} on {device_name}.",
                                           "Anycast Mac is NOT {anycast_mac} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_id(self, device_name, peer_id, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [peer_id] - The peer-id to verify.

        Verifies the current peer id
        """
        args = {"peer_id": peer_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_AUTOPEERING_ID, True,
                                           "Autopeering ID is {id} on {device_name}.",
                                           "Autopeering ID is NOT {id} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_route_target(self, device_name, route_target, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [route_target] - The route_target to verify.

        Verifies the current route_target
        """
        args = {"route_target": route_target}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_GLOBAL,
                                           self.parse_const.CHECK_AUTOPEERING_ROUTE_TARGET, True,
                                           "Route Target is {route_target} on {device_name}.",
                                           "Route Target is NOT {route_target} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_host_exists(self, device_name, host_address, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [host_address] - The host_address to verify.

        Verifies the host_address exists
        """
        args = {"host_address": host_address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOSTS,
                                           self.parse_const.CHECK_AUTOPEERING_HOST_EXISTS, True,
                                           "Route Target is {host_address} on {device_name}.",
                                           "Route Target is NOT {host_address} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_host_does_not_exist(self, device_name, host_address, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [host_address] - The host_address to verify.

        Verifies the host_address does not exist
        """
        args = {"host_address": host_address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOSTS,
                                           self.parse_const.CHECK_AUTOPEERING_HOST_DOES_NOT_EXIST, True,
                                           "Route Target is {host_address} on {device_name}.",
                                           "Route Target is NOT {host_address} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_host_static_route_network_address(self, device_name, host_address, host_vrf,
                                                             network_address,
                                                             **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [host_address] - The host_address to verify.
        [host_vrf] - The host_vrf to verify
        [network_address] - The network_address to verify

        Verifies the host_address with static route and network address exists
        """
        args = {"host_address": host_address,
                "host_vrf": host_vrf,
                "network_address": network_address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOST_STATIC_ROUTES,
                                           self.parse_const.CHECK_AUTOPEERING_HOSTS_STATIC_ROUTE_NETWORK_ADDRESS_EXISTS,
                                           True,
                                           "Route Target is {host_address} on {device_name}.",
                                           "Route Target is NOT {host_address} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_host_static_route_network_address_does_not_exist(self, device_name, host_address, host_vrf,
                                                                            network_address, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [host_address] - The host_address to verify.
        [host_vrf] - The host_vrf to verify
        [network_address] - The network_address to verify

        Verifies the host_address with static route and network address does notexists
        """
        args = {"host_address": host_address,
                "host_vrf": host_vrf,
                "network_address": network_address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOST_STATIC_ROUTES,
                                           self.parse_const.
                                           CHECK_AUTOPEERING_HOSTS_STATIC_ROUTE_NETWORK_ADDRESS_DOES_NOT_EXIST, True,
                                           "Route Target is {host_address} on {device_name}.",
                                           "Route Target is NOT {host_address} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_host_static_route_nexthop(self, device_name, host_address, host_vrf, nexthop, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [host_address] - The host_address to verify.
        [host_vrf] - The host_vrf to verify
        [nexthop] - The nexthop to verify

        Verifies the host_address with static route and nexthop exists
        """
        args = {"host_address": host_address,
                "host_vrf": host_vrf,
                "nexthop": nexthop}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOST_STATIC_ROUTES,
                                           self.parse_const.CHECK_AUTOPEERING_HOSTS_STATIC_ROUTE_NEXTHOP_ADDRESS_EXISTS,
                                           True,
                                           "Route Target is {host_address} on {device_name}.",
                                           "Route Target is NOT {host_address} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_host_vrf(self, device_name, host_address, host_vrf, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [host_address] - The host_address to verify.
        [host_vrf] - The host_vrf to verify

        Verifies the host_address with vrf exists
        """
        args = {"host_address": host_address,
                "host_vrf": host_vrf}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOSTS,
                                           self.parse_const.CHECK_AUTOPEERING_HOSTS_VRF, True,
                                           "Route Target is {host_address} on {device_name}.",
                                           "Route Target is NOT {host_address} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_host_vrf_does_not_exist(self, device_name, host_address, host_vrf, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [host_address] - The host_address to verify.
        [host_vrf] - The host_vrf to verify

        Verifies the host_address with vrf does not exist
        """
        args = {"host_address": host_address,
                "host_vrf": host_vrf}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOSTS,
                                           self.parse_const.CHECK_AUTOPEERING_HOSTS_VRF_DOES_NOT_EXIST, True,
                                           "Route Target is {host_address} on {device_name}.",
                                           "Route Target is NOT {host_address} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_service(self, device_name, address_ip, address_prefix_length, nsi, nsi_type, vrf, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [address_ip] - The address_ip to verify.
        [address_prefix_length] - The address_prefix_length to verify.
        [nsi] - The nsi to verify.
        [nsi_type] - The nsi_type to verify.
        [vrf] - The vrf to verify.

        Verifies the service exists
        """
        args = {"address_ip": address_ip,
                "address_prefix_length": address_prefix_length,
                "nsi": nsi,
                "nsi_type": nsi_type,
                "vrf": vrf}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SERVICE,
                                           self.parse_const.CHECK_AUTOPEERING_SERVICE_EXISTS, True,
                                           "Service matches {nsi} on {device_name}.",
                                           "Service does NOT match {nsi} on {device_name}!",
                                           **kwargs)

    def autopeering_verify_service_does_not_exist(self, device_name, nsi, **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [nsi] - The nsi to verify.

        Verifies the nsi does not exist
        """
        args = {"nsi": nsi}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_SERVICES,
                                           self.parse_const.CHECK_AUTOPEERING_SERVICE_DOES_NOT_EXIST, True,
                                           "Service matches {nsi} on {device_name}.",
                                           "Service does NOT match {nsi} on {device_name}!",
                                           **kwargs)
