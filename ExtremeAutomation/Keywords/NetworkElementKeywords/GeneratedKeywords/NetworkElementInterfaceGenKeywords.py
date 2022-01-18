"""
Keyword class for all interface cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.InterfaceConstants import \
    InterfaceConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.InterfaceConstants import \
    InterfaceConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils \
    import NetworkElementSnmpUtils as SnmpUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class NetworkElementInterfaceGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementInterfaceGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "interface"

    def interface_create_interface(self, device_name, interface='', **kwargs):
        """
        Description: Creates an interface on a given device.

        Supported Agents and OS:
            CLI: EOS, VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_INTERFACE,
                                    **kwargs)

    def interface_delete_interface(self, device_name, interface='', **kwargs):
        """
        Description: Removes an interface on a given device.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
            REST: SNAPROUTE
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_INTERFACE,
                                    **kwargs)

    def interface_create_loopback(self, device_name, interface='', **kwargs):
        """
        Description: Creates a loopback-mode interface/VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_LOOPBACK,
                                    **kwargs)

    def interface_delete_loopback(self, device_name, interface='', **kwargs):
        """
        Description: Removes a loopback-mode interface/VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_LOOPBACK,
                                    **kwargs)

    def interface_enable_interface(self, device_name, interface='', **kwargs):
        """
        Description: Enable an interface on a given device.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_INTERFACE,
                                    **kwargs)

    def interface_disable_interface(self, device_name, interface='', **kwargs):
        """
        Description: Disable an interface on a given device.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_INTERFACE,
                                    **kwargs)

    def interface_enable_ip_forwarding(self, device_name, interface='', **kwargs):
        """
        Description: Enables the forwarding of IPv4 routed traffic on the interface.

        Supported Agents and OS:
            CLI: EOS, EXOS
            SNMP: EOS, EXOS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IP_FORWARDING,
                                    **kwargs)

    def interface_disable_ip_forwarding(self, device_name, interface='', **kwargs):
        """
        Description: Disables the forwarding of IPv4 routed traffic on the interface.

        Supported Agents and OS:
            CLI: EOS, EXOS
            SNMP: EOS, EXOS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IP_FORWARDING,
                                    **kwargs)

    def interface_enable_ipv6_forwarding(self, device_name, interface='', **kwargs):
        """
        Description: Enables the forwarding of IPv6 routed traffic on the interface.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
            SNMP: EOS, VOSS, EXOS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPV6_FORWARDING,
                                    **kwargs)

    def interface_disable_ipv6_forwarding(self, device_name, interface='', **kwargs):
        """
        Description: Disables the forwarding of IPv6 routed traffic on the interface.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
            SNMP: EOS, VOSS, EXOS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPV6_FORWARDING,
                                    **kwargs)

    def interface_enable_loopback(self, device_name, interface='', **kwargs):
        """
        Description: Enables loopback-mode on the interface/VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_LOOPBACK,
                                    **kwargs)

    def interface_disable_loopback(self, device_name, interface='', **kwargs):
        """
        Description: Disables loopback-mode on the interface/VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_LOOPBACK,
                                    **kwargs)

    def interface_set_ipv4_primary_addr_prefix(self, device_name, interface='', ip='', prefix='', **kwargs):
        """
        Description: Configure a primary IPv4 address on a given interface.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
            SNMP: VOSS
            REST: SNAPROUTE
        """
        args = {
            "interface": interface,
            "ip": ip,
            "prefix": prefix
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_PRIMARY_ADDR_PREFIX,
                                    **kwargs)

    def interface_set_ipv4_primary_addr_netmask(self, device_name, interface='', ip='', netmask='', **kwargs):
        """
        Description: Configure a primary IPv4 address on a given interface.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
            SNMP: VOSS
            REST: SNAPROUTE
        """
        args = {
            "interface": interface,
            "ip": ip,
            "netmask": netmask
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_PRIMARY_ADDR_NETMASK,
                                    **kwargs)

    def interface_set_ipv4_loopback_addr_prefix(self, device_name, interface='', ip='', prefix='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS, SLX
        """
        args = {
            "interface": interface,
            "ip": ip,
            "prefix": prefix
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_LOOPBACK_ADDR_PREFIX,
                                    **kwargs)

    def interface_set_ipv4_loopback_addr_netmask(self, device_name, interface='', ip='', netmask='', **kwargs):
        """
        Description: Configures an IPv4 loop back address on a given interface.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
            SNMP: VOSS
        """
        args = {
            "interface": interface,
            "ip": ip,
            "netmask": netmask
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_LOOPBACK_ADDR_NETMASK,
                                    **kwargs)

    def interface_set_ipv4_secondary_addr_prefix(self, device_name, interface='', ip='', prefix='', **kwargs):
        """
        Description: Configure a secondary IPv4 address on a given interface.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "interface": interface,
            "ip": ip,
            "prefix": prefix
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_SECONDARY_ADDR_PREFIX,
                                    **kwargs)

    def interface_set_ipv4_secondary_addr_netmask(self, device_name, interface='', ip='', netmask='', **kwargs):
        """
        Description: Configure a secondary IPv4 address on a given interface.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "interface": interface,
            "ip": ip,
            "netmask": netmask
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_SECONDARY_ADDR_NETMASK,
                                    **kwargs)

    def interface_set_ipv6_address(self, device_name, interface='', ipv6_addr='', prefix='', **kwargs):
        """
        Description: Configures an IPv6 address on a given interface.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
        """
        args = {
            "interface": interface,
            "ipv6_addr": ipv6_addr,
            "prefix": prefix
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV6_ADDRESS,
                                    **kwargs)

    def interface_set_ipv6_link_local_addr(self, device_name, interface='', ipv6_addr='', prefix='', **kwargs):
        """
        Description: Configures an IPv6 address on a given interface.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
        """
        args = {
            "interface": interface,
            "ipv6_addr": ipv6_addr,
            "prefix": prefix
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV6_LINK_LOCAL_ADDR,
                                    **kwargs)

    def interface_set_ipv6_eui64_address(self, device_name, interface='', prefix='', prefix_len='', **kwargs):
        """
        Description: Configures an EUI-64 IPv6 address on a given interface.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "interface": interface,
            "prefix": prefix,
            "prefix_len": prefix_len
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV6_EUI64_ADDRESS,
                                    **kwargs)

    def interface_set_ipv6_loopback_address(self, device_name, interface='', ipv6_addr='', prefix='',
                                            voss_oid_index='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS, SLX
            SNMP: VOSS
        """
        args = {
            "interface": interface,
            "ipv6_addr": ipv6_addr,
            "prefix": prefix,
            "voss_oid_index": voss_oid_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV6_LOOPBACK_ADDRESS,
                                    **kwargs)

    def interface_clear_ipv4_addr_prefix(self, device_name, interface='', ip='', prefix='', **kwargs):
        """
        Description: Removes the specified IP address from a given interface.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
            SNMP: VOSS
        """
        args = {
            "interface": interface,
            "ip": ip,
            "prefix": prefix
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV4_ADDR_PREFIX,
                                    **kwargs)

    def interface_clear_ipv4_loopback_addr_netmask(self, device_name, interface='', ip='', netmask='', **kwargs):
        """
        Description: Removes a loop back IPv4 address on a given interface.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
            SNMP: VOSS
        """
        args = {
            "interface": interface,
            "ip": ip,
            "netmask": netmask
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV4_LOOPBACK_ADDR_NETMASK,
                                    **kwargs)

    def interface_clear_ipv6_address(self, device_name, interface='', ipv6_addr='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS
        """
        args = {
            "interface": interface,
            "ipv6_addr": ipv6_addr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV6_ADDRESS,
                                    **kwargs)

    def interface_clear_ipv6_loopback_address(self, device_name, interface='', ipv6_addr='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EOS, VOSS, EXOS, SLX
            SNMP: VOSS
        """
        args = {
            "interface": interface,
            "ipv6_addr": ipv6_addr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV6_LOOPBACK_ADDRESS,
                                    **kwargs)

    def interface_set_mac_address(self, device_name, interface='', mac='', **kwargs):
        """
        Description: Configured a new MAC address on a given interface.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "interface": interface,
            "mac": mac
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAC_ADDRESS,
                                    **kwargs)

    def interface_enable_ipv6_forwarding_global(self, device_name, **kwargs):
        """
        Description: Enables the forwarding of IPv6 routed traffic globally.

        Supported Agents and OS:
            SNMP: EOS, VOSS, EXOS
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPV6_FORWARDING_GLOBAL,
                                    **kwargs)

    def interface_disable_ipv6_forwarding_global(self, device_name, **kwargs):
        """
        Description: Disables the forwarding of IPv6 routed traffic globally.

        Supported Agents and OS:
            SNMP: EOS, VOSS, EXOS
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPV6_FORWARDING_GLOBAL,
                                    **kwargs)

    def interface_enable_ipv6_vlan(self, device_name, interface='', **kwargs):
        """
        Description: Enables IPv6 on an Interface Vlan for a given device.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IPV6_VLAN,
                                    **kwargs)

    def interface_disable_ipv6_vlan(self, device_name, interface='', **kwargs):
        """
        Description: Disables IPv6 on an Interface Vlan for a given device.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IPV6_VLAN,
                                    **kwargs)

    def interface_enable_ip_forwarding_global(self, device_name, **kwargs):
        """
        Description: Enables the forwarding of IPv4 traffic globally.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_IP_FORWARDING_GLOBAL,
                                    **kwargs)

    def interface_disable_ip_forwarding_global(self, device_name, **kwargs):
        """
        Description: Disables the forwarding of IPv4 traffic globally.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_IP_FORWARDING_GLOBAL,
                                    **kwargs)

    def interface_enable_vlan_spb_multicast(self, device_name, interface='', **kwargs):
        """
        Description: Enable Spb multicast on an interface vlan.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_VLAN_SPB_MULTICAST,
                                    **kwargs)

    def interface_disable_vlan_spb_multicast(self, device_name, interface='', **kwargs):
        """
        Description: Disable Spb multicast on an interface vlan.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_VLAN_SPB_MULTICAST,
                                    **kwargs)

    def interface_enable_chassis_force_topology_ip_flag(self, device_name, **kwargs):
        """
        Description: Enables the flag which is used to set the CLIP-IP (circuit-less IP) as topology IP.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_CHASSIS_FORCE_TOPOLOGY_IP_FLAG,
                                    **kwargs)

    def interface_disable_chassis_force_topology_ip_flag(self, device_name, **kwargs):
        """
        Description: Disables the flag which is used to set the CLIP-IP (circuit-less IP) as topology IP.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_CHASSIS_FORCE_TOPOLOGY_IP_FLAG,
                                    **kwargs)

    def interface_set_ipv4_brouter_port(self, device_name, port='', ip='', netmask='', vlan='', mac_offset='',
                                        **kwargs):
        """
        Description: Configures a brouter entry on a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ip": ip,
            "mac_offset": mac_offset,
            "netmask": netmask,
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_BROUTER_PORT,
                                    **kwargs)

    def interface_clear_ipv4_brouter_port(self, device_name, port='', **kwargs):
        """
        Description: Removes a brouter configuration on a port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV4_BROUTER_PORT,
                                    **kwargs)

    def interface_set_ipv4_primary_addr_prefix_on_port(self, device_name, interface='', ip='', prefix='', **kwargs):
        """
        Description: Configure a primary IPv4 address on a given physical interface.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interface": interface,
            "ip": ip,
            "prefix": prefix
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_PRIMARY_ADDR_PREFIX_ON_PORT,
                                    **kwargs)

    def interface_set_ipv4_secondary_addr_prefix_on_port(self, device_name, interface='', ip='', prefix='', **kwargs):
        """
        Description: Configure a secondary IPv4 address on a given physical interface.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interface": interface,
            "ip": ip,
            "prefix": prefix
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV4_SECONDARY_ADDR_PREFIX_ON_PORT,
                                    **kwargs)

    def interface_set_ipv6_address_on_port(self, device_name, interface='', ipv6_addr='', prefix='', **kwargs):
        """
        Description: Configures an IPv6 address on a given physical interface.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interface": interface,
            "ipv6_addr": ipv6_addr,
            "prefix": prefix
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV6_ADDRESS_ON_PORT,
                                    **kwargs)

    def interface_set_ipv6_link_local_addr_on_port(self, device_name, interface='', **kwargs):
        """
        Description: Configures an IPv6 address on a given physical interface.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV6_LINK_LOCAL_ADDR_ON_PORT,
                                    **kwargs)

    def interface_set_ipv6_eui64_address_on_port(self, device_name, interface='', prefix='', prefix_len='', **kwargs):
        """
        Description: Configures an EUI-64 IPv6 address on a given physical interface.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interface": interface,
            "prefix": prefix,
            "prefix_len": prefix_len
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IPV6_EUI64_ADDRESS_ON_PORT,
                                    **kwargs)

    def interface_clear_ipv4_addr_prefix_on_port(self, device_name, interface='', **kwargs):
        """
        Description: Removes the specified IP address from a given physical interface.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV4_ADDR_PREFIX_ON_PORT,
                                    **kwargs)

    def interface_clear_ipv6_address_on_port(self, device_name, interface='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: SLX
        """
        args = {
            "interface": interface
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IPV6_ADDRESS_ON_PORT,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def interface_verify_exists(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]   - The interface to check the existence of.

        Verify a given interface exists.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_INTERFACE_EXISTS, True,
                                           "Interface {interface} exists on {device_name}.",
                                           "Interface {interface} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def interface_verify_does_not_exist(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]  - The interface(s) to check the existence of.

        Verify a given interface does not exist.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_INTERFACE_EXISTS, False,
                                           "Interface {interface} does not exist on {device_name}.",
                                           "Interface {interface} EXISTS on {device_name}!",
                                           **kwargs)

    def interface_verify_enabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]   - The interface to check the existence of.

        Verify a given interface exists.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_INTERFACE_ENABLED, True,
                                           "Interface {interface} is enabled on {device_name}.",
                                           "Interface {interface} IS NOT enabled on {device_name}!",
                                           **kwargs)

    def interface_verify_disabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]   - The interface to check the existence of.

        Verify a given interface exists.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_INTERFACE_ENABLED, False,
                                           "Interface {interface} is disabled on {device_name}.",
                                           "Interface {interface} IS NOT disabled on {device_name}!",
                                           **kwargs)

    def interface_verify_spb_multicast_enabled(self, device_name, interface='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]   - The interface to check the existence of.
        [vlan]        - The interface vlan.
        NOTE:  Must provide either the vlan id or interface type
        Verify spb multicast is enabled on a given interface vlan.
        """
        args = {"interface": interface,
                "vlan": vlan,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_SPB,
                                           self.parse_const.CHECK_INTERFACE_VLAN_SPB_MULTICAST_ENABLED, True,
                                           "Spb Multicast is enabled on interface {interface} on {device_name}.",
                                           "Spb Multicast is NOT enabled on interface {interface} on {device_name}!",
                                           **kwargs)

    def interface_verify_spb_multicast_disabled(self, device_name, interface='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]   - The interface to check the existence of.
        [vlan]        - The interface vlan.
        NOTE:  Must provide either the vlan id or interface type
        Verify spb multicast is disabled on a given interface vlan.
        """
        args = {"interface": interface,
                "vlan": vlan,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_SPB,
                                           self.parse_const.CHECK_INTERFACE_VLAN_SPB_MULTICAST_ENABLED, False,
                                           "Spb Multicast is disabled on interface {interface} on {device_name}.",
                                           "Spb Multicast IS enabled on interface {interface} on {device_name}!",
                                           **kwargs)

    def interface_verify_vrf_spb_multicast_enabled(self, device_name, vrf_name='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [vrf_name]     - The vrf interface name to verify.
        [vlan]         - The vlan to verify ip spb-multicast is enabled on.

        Verifies that ip spb-multicast is enabled on a given vlan for the specified vrf interface.
        """
        args = {"vrf_name": vrf_name,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_VRF_SPB,
                                           self.parse_const.CHECK_INTERFACE_VLAN_VRF_SPB_MULTICAST_ENABLED, True,
                                           "Spb Multicast is enabled for vlan {vlan} on interface VRF {vrf_name}.",
                                           "Spb Multicast is NOT enabled for vlan {vlan} on interface VRF {vrf_name}!",
                                           **kwargs)

    def interface_verify_vrf_spb_multicast_disabled(self, device_name, vrf_name='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [vrf_name]     - The vrf interface name to verify.
        [vlan]         - The vlan to verify ip spb-multicast is enabled on.

        Verifies that ip spb-multicast is disabled on a given vlan for the specified vrf interface.
        """
        args = {"vrf_name": vrf_name,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_VRF_SPB,
                                           self.parse_const.CHECK_INTERFACE_VLAN_VRF_SPB_MULTICAST_ENABLED, False,
                                           "Spb Multicast is not enabled for vlan {vlan} on interface VRF {vrf_name}.",
                                           "Spb Multicast IS enabled for vlan {vlan} on interface VRF {vrf_name}!",
                                           **kwargs)

    def interface_verify_loopback_exists(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]  - The interface(s) to check the existence of.

        Verify a given interface does not exist.
        """
        args = {"interface": interface,
                "intf": "loopback"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_LOOPBACK_EXISTS, True,
                                           "Loopback {interface} exists on {device_name}.",
                                           "Loopback {interface} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def interface_verify_loopback_does_not_exist(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]  - The interface(s) to check the existence of.

        Verify a given interface does not exist.
        """
        args = {"interface": interface,
                "intf": "loopback"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_LOOPBACK_EXISTS, False,
                                           "Loopback {interface} does not exist on {device_name}.",
                                           "Loopback {interface} EXISTS on {device_name}!",
                                           **kwargs)

    def interface_verify_ip_address(self, device_name, interface='', ipaddr='', prefix_or_subnet='', **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword will be run against.
        [interface]        - The interface to check the existence of.
        [ipaddr]           - The IP Address to verify.
        [prefix_or_subnet] - The prefix length or subnet mask of the IP.

        Verify a given interface exists.
        """
        args = {"interface": interface,
                "prefix_or_subnet": prefix_or_subnet,
                "ipaddr": ipaddr,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_IP_ADDRESS_EXISTS, True,
                                           "Interface {interface} exists on {device_name} with IP {ipaddr}.",
                                           "Interface {interface} DOES NOT exist on {device_name} with IP {ipaddr}!",
                                           **kwargs)

    def interface_verify_ip_address_does_not_exist(self, device_name, interface='', ipaddr='', prefix_or_subnet='',
                                                   **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword will be run against.
        [interface]        - The interface to check the existence of.
        [ipaddr]           - The IP Address to verify.
        [prefix_or_subnet] - The prefix length or subnet mask of the IP.

        Verify a given ip address does not exist on a specified interface.
        """
        args = {"interface": interface,
                "prefix_or_subnet": prefix_or_subnet,
                "ipaddr": ipaddr,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_IP_ADDRESS_EXISTS, False,
                                           "Interface {interface} does not exist on {device_name} with IP {ipaddr}.",
                                           "Interface {interface} Exists on {device_name} with IP {ipaddr}!",
                                           **kwargs)

    def interface_verify_ipv6_address(self, device_name, interface='', ipaddr='', prefix_len='', **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword will be run against.
        [interface]        - The interface to check the existence of.
        [ipaddr]           - The IP Address to verify.
        [prefix_or_subnet] - The prefix length or subnet mask of the IP.

        Verify a given interface exists.
        """
        args = {"interface": interface,
                "prefix_len": prefix_len,
                "ipaddr": ipaddr,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_INFO,
                                           self.parse_const.CHECK_IPV6_ADDRESS_EXISTS, True,
                                           "Interface {interface} exists on {device_name} with "
                                           "IP {ipaddr}/{prefix_len}.",
                                           "Interface {interface} on {device_name} DOES NOT have "
                                           "IP {ipaddr}/{prefix_len}!",
                                           **kwargs)

    def interface_verify_ipv6_address_does_not_exist(self, device_name, interface='', ipaddr='', prefix_len='',
                                                     **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword will be run against.
        [interface]        - The interface to check the existence of.
        [ipaddr]           - The IP Address to verify.
        [prefix_or_subnet] - The prefix length or subnet mask of the IP.

        Verifies that a given Ipv6 interface address does not exist.
        """
        args = {"interface": interface,
                "ipaddr": ipaddr,
                "prefix_len": prefix_len,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_INFO,
                                           self.parse_const.CHECK_IPV6_ADDRESS_EXISTS, False,
                                           "Interface {interface} does not exist on {device_name} with "
                                           "IP {ipaddr}.",
                                           "Interface {interface} Exists on {device_name} with "
                                           "IP {ipaddr}!",
                                           **kwargs)

    def interface_verify_linklocal_ipv6_address(self, device_name, interface='', ipaddr='', prefix_len='64', **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword will be run against.
        [interface]        - The interface to check the existence of.
        [ipaddr]           - The IP Address to verify.
        [prefix_or_subnet] - The prefix length or subnet mask of the IP.

        Verify a given interface exists.
        """
        args = {"interface": interface,
                "prefix_len": prefix_len,
                "ipaddr": ipaddr,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_INFO,
                                           self.parse_const.CHECK_IPV6_LINKLOCAL_EXISTS, True,
                                           "Interface {interface} exists on {device_name} with IP {ipaddr}.",
                                           "Interface {interface} on {device_name} DOES NOT have IP {ipaddr}!",
                                           **kwargs)

    def interface_verify_mac_address(self, device_name, interface='', mac='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [interface]    - The interface to check the existence of.
        [mac]          - The MAC Address to verify.

        Verify a given interface's MAC address.
        """
        args = {"interface": interface,
                "mac": mac,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO_BASIC,
                                           self.parse_const.CHECK_MAC_ADDRESS, True,
                                           "Interface {interface} exists on {device_name} with MAC {mac}.",
                                           "Interface {interface} DOES NOT exist on {device_name} with MAC {mac}!",
                                           **kwargs)

    def interface_verify_loopback_id(self, device_name, loopback_id='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [loopback_id]  - The The numeric identifier of the loopback interface.  e.g. loopback 1 will be "1".
        [ip]           - The IPv4 Address to verify.

        Verifies that the loopback_id matches the specified IPv4 address.
        """
        args = {"loopback_id": loopback_id,
                "ip": ip,
                "voss_oid_index": SnmpUtils().get_loopback_index(loopback_id) + "." + ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOOPBACK,
                                           self.parse_const.CHECK_LOOPBACK_ID, True,
                                           "Loopback {loopback_id} IPv4 address is {ip}.",
                                           "Loopback {loopback_id} IPv4 address is NOT {ip}!",
                                           **kwargs)

    def interface_verify_loopback_ipv4_address(self, device_name, interface='', ipaddr='', prefix_or_subnet='',
                                               **kwargs):
        """
        Keyword Arguments:
        [device_name]      - The device the keyword will be run against.
        [interface]        - The interface to check the existence of.
        [ipaddr]           - The IP Address to verify.
        [prefix_or_subnet] - The prefix length or subnet mask of the IP.

        Verify a given interface exists.
        """
        args = {"interface": interface,
                "prefix_or_subnet": prefix_or_subnet,
                "ipaddr": ipaddr,
                "intf": "loopback"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOOPBACK_INFO,
                                           self.parse_const.CHECK_IP_ADDRESS_EXISTS, True,
                                           "Loopback {interface} exists on {device_name} with IP {ipaddr}.",
                                           "Loopback {interface} on {device_name} does NOT have IP {ipaddr}!",
                                           **kwargs)

    def interface_verify_loopback_ipv4_address_does_not_exist(self, device_name, loopback_id='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [loopback_id]  - The The numeric identifier of the loopback interface.  e.g. loopback 1 will be "1".
        [ip]           - The IPv4 Address to verify.

        Verify the IPv4 loopback interface does not exist.
        """
        args = {"loopback_id": loopback_id,
                "ip": ip,
                "voss_oid_index": SnmpUtils().get_loopback_index(loopback_id) + "." + ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOOPBACK,
                                           self.parse_const.CHECK_LOOPBACK_IPV4_ADDRESS, False,
                                           "Loopback {loopback_id} IPv4 address {ip} does not exist.",
                                           "Loopback {loopback_id} IPv4 address {ip} EXISTS!",
                                           **kwargs)

    def interface_verify_loopback_ipv6_address(self, device_name, loopback_id='', ipv6_addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [loopback_id]  - The The numeric identifier of the loopback interface.  e.g. loopback 1 will be "1".
        [ipv6_addr]    - The IPv6 Address to verify.

        Verify the IPv6 address of a loopback interface.
        """
        args = {"loopback_id": loopback_id,
                "ipv6_addr": ipv6_addr,
                "voss_oid_index":
                    SnmpUtils().get_loopback_index(loopback_id) + "." + StringUtils().ipv6_to_dec(ipv6_addr)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOOPBACK,
                                           self.parse_const.CHECK_LOOPBACK_IPV6_ADDRESS_EXISTS, True,
                                           "Loopback {loopback_id} IPv6 address is {ipv6_addr}.",
                                           "Loopback {loopback_id} IPv6 address is NOT {ipv6_addr}!",
                                           **kwargs)

    def interface_verify_loopback_ipv6_prefix(self, device_name, loopback_id='', ipv6_addr='', prefix_len='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [loopback_id]  - The The numeric identifier of the loopback interface.  e.g. loopback 1 will be "1".
        [ipv6_addr]    - The IPv6 Address to verify.
        [prefix_len]   - The IPv6 Address prefix prefix length to verify.

        Verify the IPv6 address and prefix length of a loopback interface.
        """
        args = {"loopback_id": loopback_id,
                "ipv6_addr": ipv6_addr,
                "prefix_len": prefix_len,
                "voss_oid_index":
                    SnmpUtils().get_loopback_index(loopback_id) + "." + StringUtils().ipv6_to_dec(ipv6_addr)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOOPBACK,
                                           self.parse_const.CHECK_LOOPBACK_IPV6_ADDRESS_EXISTS, True,
                                           "Loopback {loopback_id} with IPv6 address {ipv6_addr} and prefix"
                                           " {prefix_len} is correctly set to {ipv6_addr}/{prefix_len}.",
                                           "Loopback {loopback_id} with IPv6 address {ipv6_addr} and prefix"
                                           " {prefix_len} is NOT correctly set to {ipv6_addr}/{prefix_len}!",
                                           **kwargs)

    def interface_verify_loopback_ipv6_address_does_not_exist(self, device_name, loopback_id='', ipv6_addr='',
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [loopback_id]  - The The numeric identifier of the loopback interface.  e.g. loopback 1 will be "1".
        [ipv6_addr]    - The IPv6 Address to verify.

        Verify the IPv6 loopback interface does not exist.
        """
        args = {"loopback_id": loopback_id,
                "ipv6_addr": ipv6_addr,
                "voss_oid_index":
                    SnmpUtils().get_loopback_index(loopback_id) + "." + StringUtils().ipv6_to_dec(ipv6_addr)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_LOOPBACK,
                                           self.parse_const.CHECK_LOOPBACK_IPV6_ADDRESS, False,
                                           "Loopback {loopback_id} IPv6 address {ipv6_addr} does not exist.",
                                           "Loopback {loopback_id} IPv6 address {ipv6_addr} EXISTS!",
                                           **kwargs)

    def interface_verify_brouter_port_ipv4_address(self, device_name, port='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port that the Brouter is configured on.
        [ip]           - The IPv4 address to verify.

        Verify the IPv4 address is assigned to a Brouter port.
        This keyword is VOSS specific.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port) + "." + ip,
                "ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BROUTER_PORT_IPV4,
                                           self.parse_const.CHECK_BROUTER_PORT_IPV4, True,
                                           "Brouter port {port} IPV4 address is {ip}.",
                                           "Brouter port {port} IPV4 address is NOT {ip}!",
                                           **kwargs)

    def interface_verify_brouter_port_ipv4_address_does_not_exist(self, device_name, port='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port that the Brouter is configured on.
        [ip]           - The IPv4 address to verify.

        Verify the Brouter port and it's IPv4 address assignment does not exist.
        This keyword is VOSS specific.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port) + "." + ip,
                "ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BROUTER_PORT_IPV4,
                                           self.parse_const.CHECK_BROUTER_PORT_IPV4, False,
                                           "Brouter port {port} IPV4 address is not {ip}.",
                                           "Brouter port {port} IPV4 address ID {IP}!",
                                           **kwargs)

    def interface_verify_brouter_port_vlan(self, device_name, port='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port that the Brouter is configured on.
        [vlan]         - The VLAN ID to verify.

        Verify the VLAN is assigned to a Brouter port.
        This keyword is VOSS specific.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BROUTER_PORT_VLAN,
                                           self.parse_const.CHECK_BROUTER_PORT_VLAN, True,
                                           "Brouter port {port} VLAN is {vlan}.",
                                           "Brouter port {port} VLAN is NOT {vlan}!",
                                           **kwargs)

    def interface_verify_brouter_port_vlan_does_not_exist(self, device_name, port='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [port]         - The port that the Brouter is configured on.
        [vlan]         - The VLAN ID to verify.

        Verify the Brouter port and it's VLAN assignment does not exist.
        This keyword is VOSS specific.
        """
        args = {"port": port,
                "oid_index": SnmpUtils().get_port_index_from_name(device_name, port),
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BROUTER_PORT_VLAN,
                                           self.parse_const.CHECK_BROUTER_PORT_VLAN, False,
                                           "Brouter port {port} VLAN is not {vlan}.",
                                           "Brouter port {port} VLAN ID {vlan}!",
                                           **kwargs)

    def interface_verify_chassis_force_topology_ip_flag_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verify the flag which is used to  set the  CLIP-IP as topology IP is enabled.
        This keyword is VOSS specific.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CHASSIS_FORCE_TOPOLOGY_IP_FLAG,
                                           self.parse_const.CHECK_CHASSIS_FORCE_TOPOLOGY_IP_FLAG, True,
                                           "Chassis force-topology IP flag is enabled.",
                                           "Chassis force-topology IP flag is NOT enabled!",
                                           **kwargs)

    def interface_verify_chassis_force_topology_ip_flag_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.

        Verify the flag which is used to  set the  CLIP-IP as topology IP is disabled.
        This keyword is VOSS specific.
        """
        args = {"oid_index": "0"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CHASSIS_FORCE_TOPOLOGY_IP_FLAG,
                                           self.parse_const.CHECK_CHASSIS_FORCE_TOPOLOGY_IP_FLAG, False,
                                           "Chassis force-topology IP flag is disabled.",
                                           "Chassis force-topology IP flag is ENABLED!",
                                           **kwargs)

    def interface_verify_ipv6_vlan_enabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]   - The interface to check the existence of.

        Verify the IPv6 Interface Vlan is Enabled.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_VLAN,
                                           self.parse_const.CHECK_IPV6_INTERFACE_VLAN_IS_ENABLED, True,
                                           "IPv6 Interface Vlan {interface} is enabled on {device_name}.",
                                           "IPv6 Interface Vlan {interface} IS NOT enabled on {device_name}!",
                                           **kwargs)

    def interface_verify_ipv6_vlan_disabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]   - The interface to check the existence of.

        Verify the IPv6 Interface Vlan is Disabled.
        """
        args = {"interface": interface,
                "intf": "vlan"}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IPV6_VLAN,
                                           self.parse_const.CHECK_IPV6_INTERFACE_VLAN_IS_ENABLED, False,
                                           "IPv6 Interface Vlan {interface} is disabled on {device_name}.",
                                           "IPv6 Interface Vlan {interface} IS NOT disabled on {device_name}!",
                                           **kwargs)
