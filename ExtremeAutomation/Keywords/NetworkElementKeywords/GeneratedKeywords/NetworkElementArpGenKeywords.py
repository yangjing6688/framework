"""
Keyword class for all arp cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.ArpConstants import \
    ArpConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.ArpConstants import \
    ArpConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementArpGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementArpGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "arp"

    def arp_create_entry(self, device_name, ip_address='', mac='', **kwargs):
        """
        Description: Configures a static ARP entry.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "ip_address": ip_address,
            "mac": mac
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ENTRY,
                                    **kwargs)

    def arp_create_entry_interface(self, device_name, ip_address='', mac='', interface='', **kwargs):
        """
        Description: Configures a static ARP entry with port.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "interface": interface,
            "ip_address": ip_address,
            "mac": mac
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ENTRY_INTERFACE,
                                    **kwargs)

    def arp_delete_entry(self, device_name, ip_address='', **kwargs):
        """
        Description: Deletes an ARP entry.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS
        """
        args = {
            "ip_address": ip_address
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_ENTRY,
                                    **kwargs)

    def arp_clear_all_entries(self, device_name, **kwargs):
        """
        Description: Clears all ARP entries (dynamic-only on EXOS).

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_ENTRIES,
                                    **kwargs)

    def arp_create_entry_port(self, device_name, ip_address='', mac='', port='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_address": ip_address,
            "mac": mac,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ENTRY_PORT,
                                    **kwargs)

    def arp_create_entry_port_vlan(self, device_name, ip_address='', mac='', port='', vlan='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip_address": ip_address,
            "mac": mac,
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ENTRY_PORT_VLAN,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def arp_verify_entry_exists(self, device_name, ip_address='', macaddr='', intf='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [ip_address]  - The IP address under inspection.
        [macaddr]     - The MAC Address under inspection.
        [intf]        - The interface the entry should exist on.
        [static]      - A boolean flag identifying the ARP entry as static or dynamic.

        Verifies the specified route exists.
        """
        args = {"ip_address": ip_address,
                "macaddr": macaddr,
                "intf": intf}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ENTRY,
                                           self.parse_const.VERIFY_ARP_ENTRY_EXISTS, True,
                                           "ARP Entry for {ip_address} exists on {device_name}.",
                                           "ARP Entry for {ip_address} has incorrect values: \n{ret_dict}!",
                                           **kwargs)

    def arp_verify_entry_does_not_exist(self, device_name, ip_address='', macaddr='', intf='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [ip_address]  - The IP address under inspection.
        [macaddr]     - The MAC Address under inspection.
        [intf]        - The interface the entry should exist on.
        [static]      - A boolean flag identifying the ARP entry as static or dynamic.

        Verifies the specified ARP entry does not exist.
        """
        args = {"ip_address": ip_address,
                "macaddr": macaddr,
                "intf": intf}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ENTRY,
                                           self.parse_const.VERIFY_ARP_ENTRY_EXISTS, False,
                                           "ARP Entry for {ip_address} does not exist on {device_name}.",
                                           "ARP Entry for {ip_address} has values: \n{ret_dict}!",
                                           **kwargs)

    def arp_verify_entry_exists_vrf(self, device_name, vrf_name='', ip_address='', macaddr='', intf='',
                                    **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The VRF Name to verify.
        [ip_address]  - The IP address under inspection.
        [macaddr]     - The MAC Address under inspection.
        [intf]        - The interface the entry should exist on.
        [static]      - A boolean flag identifying the ARP entry as static or dynamic.

        Verifies an arp entry is present for given vrf.
        """
        args = {"vrf_name": vrf_name,
                "ip_address": ip_address,
                "macaddr": macaddr,
                "intf": intf}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VRF_ENTRY,
                                           self.parse_const.VERIFY_ARP_VRF_ENTRY_EXISTS, True,
                                           "ARP VRF Entry for {vrf_name} exists on {device_name}.",
                                           "ARP VRF Entry for {vrf_name} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def arp_verify_entry_does_not_exist_vrf(self, device_name, vrf_name='', ip_address='', macaddr='', intf='',
                                            **kwargs):
        """
        [device_name] - The device the keyword will be run against.
        [vrf_name]    - The VRF Name to verify.
        [ip_address]  - The IP address under inspection.
        [macaddr]     - The MAC Address under inspection.
        [intf]        - The interface the entry should exist on.
        [static]      - A boolean flag identifying the ARP entry as static or dynamic.

        Verifies an arp entry is NOT present for given vrf.
        """
        args = {"vrf_name": vrf_name,
                "ip_address": ip_address,
                "macaddr": macaddr,
                "intf": intf}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VRF_ENTRY,
                                           self.parse_const.VERIFY_ARP_VRF_ENTRY_EXISTS, False,
                                           "ARP VRF Entry for {vrf_name} does not exist on {device_name}.",
                                           "ARP VRF Entry for {vrf_name} EXISTS on {device_name}!",
                                           **kwargs)
