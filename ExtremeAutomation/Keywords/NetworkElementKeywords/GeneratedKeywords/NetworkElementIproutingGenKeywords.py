"""
Keyword class for all iprouting cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.IproutingConstants import \
    IproutingConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.IproutingConstants import \
    IproutingConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementIproutingGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementIproutingGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "iprouting"

    def iprouting_create_static_route(self, device_name, route='', nexthop='', **kwargs):
        """
        Description: Creates a static route entry.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "nexthop": nexthop,
            "route": route
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_STATIC_ROUTE,
                                    **kwargs)

    def iprouting_delete_static_route(self, device_name, route='', nexthop='', **kwargs):
        """
        Description: Removes a static route entry.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "nexthop": nexthop,
            "route": route
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_STATIC_ROUTE,
                                    **kwargs)

    def iprouting_enable_ipmcforwarding_global(self, device_name, **kwargs):
        """
        Description: Enables ipmcforwarding globally.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPMCFORWARDING_GLOBAL,
                                    **kwargs)

    def iprouting_enable_ipmcforwarding_ipv4_global(self, device_name, **kwargs):
        """
        Description: Enables ipmcforwarding on ipv4 globally.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPMCFORWARDING_IPV4_GLOBAL,
                                    **kwargs)

    def iprouting_enable_ipmcforwarding_ipv6_global(self, device_name, **kwargs):
        """
        Description: Enables ipmcforwarding on ipv6 globally.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPMCFORWARDING_IPV6_GLOBAL,
                                    **kwargs)

    def iprouting_enable_ipmcforwarding_ipv4_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enables ipmcforwarding ipv4 on the given vlan.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPMCFORWARDING_IPV4_VLAN,
                                    **kwargs)

    def iprouting_enable_ipmcforwarding_ipv6_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enables ipmcforwarding ipv6 on the given vlan.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPMCFORWARDING_IPV6_VLAN,
                                    **kwargs)

    def iprouting_disable_ipmcforwarding_global(self, device_name, **kwargs):
        """
        Description: Disables ipmcforwarding globally.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPMCFORWARDING_GLOBAL,
                                    **kwargs)

    def iprouting_disable_ipmcforwarding_ipv4_global(self, device_name, **kwargs):
        """
        Description: Disables ipmcforwarding on ipv4 globally.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPMCFORWARDING_IPV4_GLOBAL,
                                    **kwargs)

    def iprouting_disable_ipmcforwarding_ipv6_global(self, device_name, **kwargs):
        """
        Description: Disables ipmcforwarding on ipv6 globally.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPMCFORWARDING_IPV6_GLOBAL,
                                    **kwargs)

    def iprouting_disable_ipmcforwarding_ipv4_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disables ipmcforwarding ipv4 on the given vlan.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPMCFORWARDING_IPV4_VLAN,
                                    **kwargs)

    def iprouting_disable_ipmcforwarding_ipv6_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disables ipmcforwarding ipv6 on the given vlan.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPMCFORWARDING_IPV6_VLAN,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def iprouting_verify_and_store_default_gateway_ip(self, device_name, gateway_name='', **kwargs):
        """
        Keyword Arguments
        [device_name]    - The device the keyword will be run against.
        [destination_ip] - The route or host destination.
        [gateway_name]   - The name of the stored gateway variable.

        Stores the gateway IP for a given destination.
        """
        args = {"gateway_name": gateway_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_ROUTES,
                                           self.parse_const.STORE_DEFAULT_GATEWAY, True,
                                           "Default gateway IP address stored.",
                                           "No route found for destination!",
                                           **kwargs)

    def iprouting_verify_route_interface(self, device_name, interface='', **kwargs):
        """
        *DEPRECATED!* Endsystem keywords instead. This is a Linux host keyword.
        Keyword Arguments:
        [device_name] - The Network Element to run the keyword against.
        [interface]   - The interface to check.

        Verifies the presence of an interface.
        """
        args = {"interface": interface}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATIC_ROUTE,
                                           self.parse_const.VALIDATE_STATIC_ROUTE_INT_EXISTS, True,
                                           "Route Interface {interface} exists on {device_name}.",
                                           "Route Interface {interface} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def iprouting_verify_route_exists(self, device_name, route='', nexthop='', mask='', vrf_name='', cost='',
                                      interface='', protocol='', age='', route_type='', preference='',
                                      **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [route]        - The route destination address to verify.              (Example:  10.2.201.0)
        [mask]         - The route destination subnet mask to verify.          (Example:  255.255.255.0)
        [nexthop]      - The route destination next hop gateway to verify.     (Example:  VSP4001 or 10.2.201.1)
        [vrf_name]     - The name of the VRF being verified.                   (Example:  vrf_red)
        [isid]         - The route destination I-SID being used.               (Example:  30001)
        [cost]         - The route cost to the destination.                    (Example:  225)
        [interface]    - The VLAN or BVLAN interface used for the route.       (Example:  4051)
        [protocol]     - The route protocol type.                              (Example:  ISIS)
        [age]          - The route age.                                        (Example:  0)
        [route_type]   - The route type.                                       (Example:  IBSV or DB)
        [preference]   - The route preference.                                 (Example:  7)

        Verifies route entries are present in the ip route table.
        """
        args = {"route": route,
                "mask": mask,
                "nexthop": nexthop,
                "vrf_name": vrf_name,
                "cost": cost,
                "interface": interface,
                "protocol": protocol,
                "age": age,
                "type": route_type,
                "preference": preference}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_ROUTES,
                                           self.parse_const.VALIDATE_ROUTE_ENTRY, True,
                                           "The route entries are present on {device_name}.",
                                           "The route entries are NOT present on {device_name}.!",
                                           **kwargs)

    def iprouting_verify_route_does_not_exist(self, device_name, route='', nexthop='', mask='', vrf_name='', cost='',
                                              interface='', protocol='', age='', route_type='', preference='',
                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [route]        - The route destination address to verify.              (Example:  10.2.201.0)
        [mask]         - The route destination subnet mask to verify.          (Example:  255.255.255.0)
        [nexthop]      - The route destination next hop gateway to verify.     (Example:  VSP4001 or 10.2.201.1)
        [vrf_name]     - The name of the VRF being verified.                   (Example:  vrf_red)
        [isid]         - The route destination I-SID being used.               (Example:  30001)
        [cost]         - The route cost to the destination.                    (Example:  225)
        [interface]    - The VLAN or BVLAN interface used for the route.       (Example:  4051)
        [protocol]     - The route protocol type.                              (Example:  ISIS)
        [age]          - The route age.                                        (Example:  0)
        [route_type]   - The route type.                                       (Example:  IBSV or DB)
        [preference]   - The route preference.                                 (Example:  7)

        Verifies route entries are present in the ip route table.
        """
        args = {"route": route,
                "mask": mask,
                "nexthop": nexthop,
                "vrf_name": vrf_name,
                "cost": cost,
                "interface": interface,
                "protocol": protocol,
                "age": age,
                "type": route_type,
                "preference": preference}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_ROUTES,
                                           self.parse_const.VALIDATE_ROUTE_ENTRY, False,
                                           "The route entries are not present on {device_name}.",
                                           "The route entries are INCORRECTLY present on {device_name}.!",
                                           **kwargs)

    def iprouting_verify_ipv6_route_exists(self, device_name, route='', nexthop='', interface='', protocol='', cost='',
                                           age='', route_type='', preference='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [route]        - The route destination address to verify.              (Example:  3000:10:0:0:0:0:0:0/64)
        [nexthop]      - The route destination next hop gateway to verify.     (Example:  VSP4001)
        [interface]    - The VLAN or BVLAN interface used for the route.       (Example:  4051)
        [protocol]     - The route protocol type.                              (Example:  ISIS)
        [cost]         - The route cost to the destination.                    (Example:  225)
        [age]          - The route age.                                        (Example:  0)
        [route_type]   - The route type.                                       (Example:  IBSV or DB)
        [preference]   - The route preference.                                 (Example:  7)

        Verifies IPv6 route entries are present in the ipv6 route table.
        """
        args = {"route": route,
                "nexthop": nexthop,
                "interface": interface,
                "protocol": protocol,
                "cost": cost,
                "age": age,
                "route_type": route_type,
                "preference": preference}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_IPV6_ROUTES,
                                           self.parse_const.VALIDATE_IPV6_ROUTE_ENTRY, True,
                                           "The route entries are present on {device_name}.",
                                           "The route entries are NOT present on {device_name}.!",
                                           **kwargs)

    def iprouting_verify_vrf_route_exists(self, device_name, route='', mask='', nexthop='', vrf_name='', cost='',
                                          interface='', protocol='', age='', route_type='', preference='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [route]        - The route destination address to verify.              (Example:  10.2.201.0)
        [mask]         - The route destination subnet mask to verify.          (Example:  255.255.255.0)
        [nexthop]      - The route destination next hop gateway to verify.     (Example:  VSP4001 or 10.2.201.1)
        [vrf_name]     - The name of the VRF being verified.                   (Example:  vrf_red)
        [cost]         - The route cost to the destination.                    (Example:  225)
        [interface]    - The VLAN or BVLAN interface used for the route.       (Example:  4051)
        [protocol]     - The route protocol type.                              (Example:  ISIS)
        [age]          - The route age.                                        (Example:  0)
        [route_type]   - The route type.                                       (Example:  IBSV or DB)
        [preference]   - The route preference.                                 (Example:  7)

        Verifies route entries exist for the specified VRF.  (VOSS Only)
        """
        args = {"route": route,
                "mask": mask,
                "nexthop": nexthop,
                "vrf_name": vrf_name,
                "cost": cost,
                "interface": interface,
                "protocol": protocol,
                "age": age,
                "type": route_type,
                "preference": preference}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IP_ROUTE_VRF,
                                           self.parse_const.VALIDATE_VRF_ROUTE_ENTRY, True,
                                           "The following route entries are present for VRF {vrf_name}: {route} "
                                           "{mask}, {nexthop}, {cost}, {interface}, {protocol}, {age}, "
                                           "{type}, and {preference} on {device_name}.",
                                           "The following route entries are NOT present for VRF {vrf_name}: {route} "
                                           "{mask}, {nexthop}, {cost}, {interface}, {protocol}, {age}, "
                                           "{type}, and {preference} on {device_name}.!",
                                           **kwargs)

    def iprouting_verify_vrf_ipv6_route_exists(self, device_name, route='', nexthop='', vrf_name='', cost='',
                                               interface='', protocol='', age='', route_type='', preference='',
                                               **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [route]        - The route destination address to verify.              (Example:  3000:10:0:0:0:0:0:0/64)
        [nexthop]      - The route destination next hop gateway to verify.     (Example:  VSP4001)
        [vrf_name]     - The name of the VRF being verified.                   (Example:  vrf_red)
        [isid]         - The route destination I-SID being used.               (Example:  30001)
        [cost]         - The route cost to the destination.                    (Example:  225)
        [interface]    - The VLAN or BVLAN interface used for the route.       (Example:  4051)
        [protocol]     - The route protocol type.                              (Example:  ISIS)
        [age]          - The route age.                                        (Example:  0)
        [route_type]   - The route type.                                       (Example:  IBSV or DB)
        [preference]   - The route preference.                                 (Example:  7)

        Verifies route entries exist for the specified VRF.  (VOSS Only)
        """
        args = {"route": route,
                "nexthop": nexthop,
                "vrf_name": vrf_name,
                "cost": cost,
                "interface": interface,
                "protocol": protocol,
                "age": age,
                "type": route_type,
                "preference": preference}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_ROUTE_VRF,
                                           self.parse_const.VALIDATE_IPV6_VRF_ROUTE_ENTRY, True,
                                           "The following route entries are present for VRF {vrf_name}:  {route}, "
                                           "{nexthop}, {cost}, {interface}, {protocol}, {age}, "
                                           "{type}, and {preference} on {device_name}.",
                                           "The following route entries are NOT present for VRF {vrf_name}:  {route}, "
                                           "{nexthop}, {cost}, {interface}, {protocol}, {age}, "
                                           "{type}, and {preference} on {device_name}.!",
                                           **kwargs)
