"""
Keyword class for all dhcp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.DhcpConstants import \
    DhcpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.DhcpConstants import \
    DhcpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementDhcpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementDhcpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "dhcp"

    def dhcp_enable_vlan(self, device_name, vlan_name='', **kwargs):
        """
        Description: Enables the DHCP client on a given VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_VLAN,
                                    **kwargs)

    def dhcp_disable_vlan(self, device_name, vlan_name='', **kwargs):
        """
        Description: Disables the DHCP client on a given VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_VLAN,
                                    **kwargs)

    def dhcp_enable_port(self, device_name, vlan_name='', port='', **kwargs):
        """
        Description: Enables the DHCP client on ports belonging to a given VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_PORT,
                                    **kwargs)

    def dhcp_disable_port(self, device_name, vlan_name='', port='', **kwargs):
        """
        Description: Disables the DHCP client on ports belonging to a given VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_PORT,
                                    **kwargs)

    def dhcp_enable_bootprelay_vlan(self, device_name, vlan_name='', **kwargs):
        """
        Description: Enables bootprelay on the provided vlan.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_BOOTPRELAY_VLAN,
                                    **kwargs)

    def dhcp_set_address_range(self, device_name, vlan_name='', start_addr='', end_addr='', **kwargs):
        """
        Description: Creates the IP DHCP address range for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "end_addr": end_addr,
            "start_addr": start_addr,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ADDRESS_RANGE,
                                    **kwargs)

    def dhcp_set_lease_time(self, device_name, vlan_name='', seconds='', **kwargs):
        """
        Description: Sets the IP DHCP lease time for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "seconds": seconds,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_LEASE_TIME,
                                    **kwargs)

    def dhcp_set_netlogin_lease_time(self, device_name, vlan_name='', seconds='', **kwargs):
        """
        Description: Configures the timer value returned as part of the DHCP response for clients.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "seconds": seconds,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NETLOGIN_LEASE_TIME,
                                    **kwargs)

    def dhcp_set_options_gateway(self, device_name, vlan_name='', gateway_addr='', **kwargs):
        """
        Description: Sets the default gateway in the DHCP scope for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "gateway_addr": gateway_addr,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_OPTIONS_GATEWAY,
                                    **kwargs)

    def dhcp_set_options_dns(self, device_name, vlan_name='', dns_addr='', **kwargs):
        """
        Description: Sets the DNS server in the DHCP scope for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "dns_addr": dns_addr,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_OPTIONS_DNS,
                                    **kwargs)

    def dhcp_set_options_dns_pri(self, device_name, vlan_name='', dns_addr='', **kwargs):
        """
        Description: Sets the primary DNS server in the DHCP scope for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "dns_addr": dns_addr,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_OPTIONS_DNS_PRI,
                                    **kwargs)

    def dhcp_set_options_dns_sec(self, device_name, vlan_name='', dns_addr='', **kwargs):
        """
        Description: Sets the secondary DNS server in the DHCP scope for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "dns_addr": dns_addr,
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_OPTIONS_DNS_SEC,
                                    **kwargs)

    def dhcp_set_bootprelay_ip(self, device_name, ip='', vr='', **kwargs):
        """
        Description: Adds the provided IP to bootprelay on the provided vr.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ip": ip,
            "vr": vr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_BOOTPRELAY_IP,
                                    **kwargs)

    def dhcp_clear_address_range(self, device_name, vlan_name='', **kwargs):
        """
        Description: Removes the IP DHCP address range for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ADDRESS_RANGE,
                                    **kwargs)

    def dhcp_clear_lease_time(self, device_name, vlan_name='', **kwargs):
        """
        Description: Sets the IP DHCP lease time for the VLAN back to the default of 300 seconds.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_LEASE_TIME,
                                    **kwargs)

    def dhcp_clear_netlogin_lease_time(self, device_name, vlan_name='', **kwargs):
        """
        Description: Sets the IP DHCP netlogin lease time for the VLAN back to the default of 10 seconds.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_NETLOGIN_LEASE_TIME,
                                    **kwargs)

    def dhcp_clear_global(self, device_name, vlan_name='', **kwargs):
        """
        Description: Removes the entire IP DHCP configuration for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_GLOBAL,
                                    **kwargs)

    def dhcp_clear_options_gateway(self, device_name, vlan_name='', **kwargs):
        """
        Description: Removes the default gateway in the DHCP scope for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_OPTIONS_GATEWAY,
                                    **kwargs)

    def dhcp_clear_options_dns(self, device_name, vlan_name='', **kwargs):
        """
        Description: Removes the DNS Sever in the DHCP scope for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_OPTIONS_DNS,
                                    **kwargs)

    def dhcp_clear_options_dns_pri(self, device_name, vlan_name='', **kwargs):
        """
        Description: Removes the primary DNS Sever in the DHCP scope for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_OPTIONS_DNS_PRI,
                                    **kwargs)

    def dhcp_clear_options_dns_sec(self, device_name, vlan_name='', **kwargs):
        """
        Description: Removes the secondary DNS Sever in the DHCP scope for the VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "vlan_name": vlan_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_OPTIONS_DNS_SEC,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def dhcp_verify_address_range(self, device_name, vlan='', vlan_name='', start_addr='', end_addr='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the lease time is set on.
        [start_addr]  - The start of the dhcp address range.
        [end_addr]    - The end of the dhcp address range.

        Verifies that the dhcp address range for the vlan is correct.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "start_addr": start_addr,
                "end_addr": end_addr}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_DHCP_VLAN_ADDRESS_RANGE, True,
                                           "DHCP address range for the vlan is correct.",
                                           "DHCP address range for the vlan is NOT correct!",
                                           **kwargs)

    def dhcp_verify_multiauth_lease_timer(self, device_name, vlan='', vlan_name='', seconds='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the netlogin lease time is set on.
        [seconds]     - The expected netlogin lease time in seconds.

        Verifies that the dhcp netlogin lease time for the vlan is correct.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "seconds": seconds}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_DHCP_VLAN_NETLOGIN_LEASE_TIMER, True,
                                           "DHCP netlogin lease time for the vlan is correct.",
                                           "DHCP netlogin lease time for the vlan is NOT correct!",
                                           **kwargs)

    def dhcp_verify_lease_timer(self, device_name, vlan='', vlan_name='', seconds='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the lease time is set on.
        [seconds]     - The expected lease time in seconds.

        Verifies that the dhcp lease time for the vlan is set correctly.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "seconds": seconds}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_DHCP_CONFIG,
                                           self.parse_const.CHECK_DHCP_VLAN_LEASE_TIMER, True,
                                           "DHCP lease time for the vlan is correct.",
                                           "DHCP lease time for the vlan is NOT correct!",
                                           **kwargs)

    def dhcp_verify_ports_enabled(self, device_name, vlan='', vlan_name='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the ports are members of.
        [ports]       - The expected port(s) that are enabled on the vlan for DHCP.

        Verifies that the port(s) on the vlan are enabled for DHCP.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "port": ports}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_DHCP_CONFIG,
                                           self.parse_const.CHECK_DHCP_VLAN_ENABLED_PORTS, True,
                                           "DHCP is enabled for the ports on the vlan.",
                                           "DHCP is NOT enabled for the ports on the vlan!",
                                           **kwargs)

    def dhcp_verify_default_gateway(self, device_name, vlan='', vlan_name='', gateway_ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the default gateway is assigned in the DHCP scope.
        [gateway_ip]  - The expected default gateway for the DHCP scope.

        Verifies that the default gateway is correct for the DHCP scope on the VLAN.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "gateway_ip": gateway_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_DHCP_CONFIG,
                                           self.parse_const.CHECK_DHCP_VLAN_DEFAULT_GATEWAY, True,
                                           "The default gateway is correct for the DHCP scope.",
                                           "The default gateway is NOT correct for the DHCP scope!",
                                           **kwargs)

    def dhcp_verify_primary_dns(self, device_name, vlan='', vlan_name='', dns1_ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the DNS server is assigned on in the DHCP scope.
        [dns1_ip]     - The expected primary dns server for the DHCP scope.

        Verifies that the primary DNSserver is correct for the DHCP scope on the VLAN.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "dns1_ip": dns1_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_DHCP_CONFIG,
                                           self.parse_const.CHECK_DHCP_VLAN_PRIMARY_DNS, True,
                                           "The primary DNS is correct for the DHCP scope.",
                                           "The primary DNS is NOT correct for the DHCP scope!",
                                           **kwargs)

    def dhcp_verify_secondary_dns(self, device_name, vlan='', vlan_name='', dns2_ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the dns server is defined on in the dhcp scope.
        [dns2_ip]     - The expected secondary dns server for the DHCP scope.

        Verifies that the secondary DNS server is correct for the DHCP scope on the VLAN.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "dns2_ip": dns2_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_DHCP_CONFIG,
                                           self.parse_const.CHECK_DHCP_VLAN_SECONDARY_DNS, True,
                                           "The secondary DNS is correct for the DHCP scope.",
                                           "The secondary DNS is NOT correct for the DHCP scope!",
                                           **kwargs)

    def dhcp_verify_ip_address(self, device_name, vlan='', vlan_name='', ip_address='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the IP address is assigned on in the DHCP scope..
        [ip_address]  - The  IP address that is expected to be allocated.

        Verifies that the IP address is assigned within the DHCP scope on the VLAN.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "ip_address": ip_address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_DHCP_ADDRESS_ALLOCATION,
                                           self.parse_const.CHECK_DHCP_VLAN_ASSIGNED_IP_ADDRESS_ALLOCATION, True,
                                           "The IP address is assigned in the DHCP scope.",
                                           "The IP address is NOT assigned in the DHCP scope!",
                                           **kwargs)

    def dhcp_verify_mac_address(self, device_name, vlan='', vlan_name='', mac='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that the IP address is assigned on in the DHCP scope..
        [mac]         - The  mac address of the station that is expected to be allocated for an ip address.

        Verifies that an address is assigned within the DHCP scope on the VLAN for a particular MAC address.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name,
                "mac": mac}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN_DHCP_ADDRESS_ALLOCATION,
                                           self.parse_const.CHECK_DHCP_VLAN_ASSIGNED_MAC_ADDRESS_ALLOCATION, True,
                                           "The MAC address is assigned an address in the DHCP scope.",
                                           "The MAC address is NOT assigned an address in the DHCP scope!",
                                           **kwargs)

    def dhcp_verify_bootprelay_server(self, device_name, ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [ip]          - The ip address to verify is listed in the bootp relay servers list .

        Verifies that an address is listed in the BOOTP Relay Servers list on EXOS.
        """
        args = {"ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BOOTPRELAY_INFO,
                                           self.parse_const.CHECK_BOOTPRELAY_SERVERS, True,
                                           "The IP address is listed in the BOOTP Relay Servers list.",
                                           "The IP address is NOT listed in the BOOTP Relay Servers list!",
                                           **kwargs)

    def dhcp_verify_bootprelay_interface_enabled(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that should be set to Enabled in the BOOTP Relay list.

        Verifies BOOTP Relay is Enabled on given vlan on EXOS.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BOOTPRELAY_INFO,
                                           self.parse_const.CHECK_BOOTPRELAY_INTERFACE_ENABLED, True,
                                           "The vlan {vlan} BOOTP Relay is Enabled.",
                                           "The vlan {vlan} BOOTP Relay is NOT Enabled!",
                                           **kwargs)

    def dhcp_verify_bootprelay_interface_disabled(self, device_name, vlan='', vlan_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan that should be set to Disabled in the BOOTP Relay list.

        Verifies BOOTP Relay is Disabled on given vlan on EXOS.
        """
        args = {"vlan": vlan,
                "vlan_name": vlan_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BOOTPRELAY_INFO,
                                           self.parse_const.CHECK_BOOTPRELAY_INTERFACE_DISABLED, True,
                                           "The vlan {vlan} BOOTP Relay is Disabled.",
                                           "The vlan {vlan} BOOTP Relay is NOT Disabled!",
                                           **kwargs)
