"""
Keyword class for all nd cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.NdConstants import \
    NdConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.NdConstants import \
    NdConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementNdGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementNdGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "nd"

    def nd_set_v6_neighbor(self, device_name, ipv6_addr='', hw_addr='', interface='', port='', **kwargs):
        """
        Description: Creates a static Neighbor Discovery entry for the supplied IPv6 address/MAC.

        Supported Agents and OS:
            CLI: EXOS, EOS, VOSS
        """
        args = {
            "hw_addr": hw_addr,
            "interface": interface,
            "ipv6_addr": ipv6_addr,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_V6_NEIGHBOR,
                                    **kwargs)

    def nd_clear_v6_neighbor(self, device_name, ipv6_addr='', interface='', **kwargs):
        """
        Description: Deletes a Neighbor Discovery entry for the supplied IPv6 address.

        Supported Agents and OS:
            CLI: EXOS, EOS, VOSS
        """
        args = {
            "interface": interface,
            "ipv6_addr": ipv6_addr
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_V6_NEIGHBOR,
                                    **kwargs)

    def nd_clear_v6_neighbor_port(self, device_name, ipv6_addr='', port='', **kwargs):
        """
        Description: Deletes a Neighbor Discovery port for the supplied IPv6 address.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ipv6_addr": ipv6_addr,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_V6_NEIGHBOR_PORT,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def nd_verify_neighbor_entry(self, device_name, ipv6_addr='', hw_addr='', interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should run against.
        [ipv6_addr]   - The IPv6 address of the neighbor entry.
        [hw_addr]     - The MAC address of the neighbor entry.
        [interface]   - The interface the entry should be learned on. This information is not required.

        Verifies a give neighbor entry exists.
        """
        args = {"interface": interface,
                "ipv6_addr": ipv6_addr,
                "hw_addr": hw_addr}

        self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ND_TABLE,
                                    self.parse_const.CHECK_ND_ENTRY_EXISTS, True,
                                    "A neighbor entry for {ipv6_addr} at {hw_addr} exists on {device_name}.",
                                    "A neighbor entry for {ipv6_addr} at {hw_addr} DOES NOT exist on "
                                    "device_name!",
                                    **kwargs)

    def nd_verify_neighbor_entry_does_not_exist(self, device_name, ipv6_addr='', hw_addr='', interface='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should run against.
        [ipv6_addr]   - The IPv6 address of the neighbor entry.
        [hw_addr]     - The MAC address of the neighbor entry.
        [interface]   - The interface the entry should be learned on. This information is not required.

        Verifies a give neighbor entry exists.
        """
        args = {"interface": interface,
                "ipv6_addr": ipv6_addr,
                "hw_addr": hw_addr}

        self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ND_TABLE,
                                    self.parse_const.CHECK_ND_ENTRY_EXISTS, False,
                                    "A neighbor entry for {ipv6_addr} at {hw_addr} does not exist on "
                                    "{device_name}.",
                                    "A neighbor entry for {ipv6_addr} at {hw_addr} STILL exists on device_name!",
                                    **kwargs)
