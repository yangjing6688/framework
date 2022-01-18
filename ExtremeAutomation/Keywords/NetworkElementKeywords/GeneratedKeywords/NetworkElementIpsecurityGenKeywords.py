"""
Keyword class for all ipsecurity cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.IpsecurityConstants import \
    IpsecurityConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.IpsecurityConstants import \
    IpsecurityConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementIpsecurityGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementIpsecurityGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "ipsecurity"

    def ipsecurity_set_trusted_port(self, device_name, port='', **kwargs):
        """
        Description: Configures the given port as a trusted port.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TRUSTED_PORT,
                                    **kwargs)

    def ipsecurity_enable_dhcp_snooping(self, device_name, vlan='', ports='', violation_action='', snmp_trap='',
                                        block='', duration='', **kwargs):
        """
        Description: Enables ip security dhcp snooping in various ways on the given vlan/port.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "block": block,
            "duration": duration,
            "ports": ports,
            "snmp_trap": snmp_trap,
            "violation_action": violation_action,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_DHCP_SNOOPING,
                                    **kwargs)

    def ipsecurity_disable_dhcp_snooping(self, device_name, vlan='', ports='', **kwargs):
        """
        Description: Disables ip security dhcp snooping on the given vlan/port.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "ports": ports,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_DHCP_SNOOPING,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def ipsecurity_verify_trusted_port(self, device_name, port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port that should be in the Trusted list.

        Verifies that the given port is in the Trusted Port config.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TRUSTED_PORTS,
                                           self.parse_const.CHECK_TRUSTED_PORT_GLOBAL, True,
                                           "The port {port} is listed in the global Trusted list.",
                                           "The port {port} is NOT listed in the global Trusted list!",
                                           **kwargs)

    def ipsecurity_verify_dhcp_snooping_port(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan used in showing the dhcp-snooping table.
        [port]        - The port that should be listed in the vlans dhcp-snooping table.

        Verifies that the given port is listed in the dhcp-snooping table for the given vlan.
        """
        args = {"port": port,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNOOPING_VLAN,
                                           self.parse_const.CHECK_DHCP_SNOOPING_VLAN, True,
                                           "The port {port} is listed in the vlans snooping table.",
                                           "The port {port} is NOT listed in the vlans snooping table!",
                                           **kwargs)

    def ipsecurity_verify_dhcp_snooping_port_disabled(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan used in showing the dhcp-snooping table.
        [port]        - The port that should NOT be listed in the vlans dhcp-snooping table.

        Verifies that the given port is NOT listed in the dhcp-snooping table for the given vlan.
        """
        args = {"port": port,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNOOPING_VLAN,
                                           self.parse_const.CHECK_DHCP_SNOOPING_VLAN, False,
                                           "The port {port} is NOT listed in the vlans snooping table.",
                                           "The port {port} IS LISTED in the vlans snooping table!",
                                           **kwargs)

    def ipsecurity_verify_dhcp_snooping_entry(self, device_name, vlan='', mac='', subnet='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan used in showing the dhcp-snooping table.
        [mac]         - The mac address used to find the correct entry in the dhcp-snooping table.
        [subnet]      - The subnet in which the IP address listed in the table should be within.

        Verifies that the given ip is listed in the dhcp-snooping entries table for the given vlan.
        The verification is done via checking that the IP is within the provided subnet.  This is due to the fact
        that dhcp assigns IPs, so you may not know what it is.
        """
        args = {"mac": mac,
                "vlan": vlan,
                "subnet": subnet}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNOOPING_VLAN_ENTRIES,
                                           self.parse_const.CHECK_DHCP_SNOOPING_VLAN_ENTRIES, True,
                                           "The entry's ip is within the subnet in the vlans snooping entries table.",
                                           "The entry's ip is NOT within the subnet " +
                                           "in the vlans snooping entries table!",
                                           **kwargs)

    def ipsecurity_verify_dhcp_snooping_violations(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The vlan used in showing the dhcp-snooping table.
        [port]        - The port that should be listed in the vlans dhcp-snooping violations table.

        Verifies that the given port is listed in the dhcp-snooping violations table for the given vlan.
        """
        args = {"port": port,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SNOOPING_VLAN_VIOLATIONS,
                                           self.parse_const.CHECK_DHCP_SNOOPING_VLAN_VIOLATIONS, True,
                                           "The port {port} is listed in the vlans snooping violations table.",
                                           "The port {port} is NOT listed in the vlans snooping violations table!",
                                           **kwargs)
