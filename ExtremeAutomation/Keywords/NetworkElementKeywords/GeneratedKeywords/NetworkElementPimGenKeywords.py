"""
Keyword class for all pim cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.PimConstants import \
    PimConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.PimConstants import \
    PimConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementPimGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementPimGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "pim"

    def pim_enable(self, device_name, **kwargs):
        """
        Description: Enable PIM.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE,
                                    **kwargs)

    def pim_disable(self, device_name, **kwargs):
        """
        Description: Disable PIM.

        Supported Agents and OS:
            CLI: EXOS, VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE,
                                    **kwargs)

    def pim_enable_sparse(self, device_name, exos_mode='', interface='', ip_ver='', mode='', vlan='', **kwargs):
        """
        Description: Enable PIM Sparse Mode.

        Supported Agents and OS:
            CLI: EXOS, VOSS, EOS
        """
        args = {
            "exos_mode": exos_mode,
            "interface": interface,
            "ip_ver": ip_ver,
            "mode": mode,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SPARSE,
                                    **kwargs)

    def pim_disable_sparse(self, device_name, interface='', ip_ver='', mode='', vlan='', **kwargs):
        """
        Description: Disable PIM Sparse Mode.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "interface": interface,
            "ip_ver": ip_ver,
            "mode": mode,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_SPARSE,
                                    **kwargs)

    def pim_set_rp(self, device_name, mcast_group_address='', mask='', ip='', interface='', acl='', **kwargs):
        """
        Description: Configures a given device to be a candidate Rendezvous Point.

        Supported Agents and OS:
            CLI: EXOS, VOSS, EOS
        """
        args = {
            "acl": acl,
            "interface": interface,
            "ip": ip,
            "mask": mask,
            "mcast_group_address": mcast_group_address
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RP,
                                    **kwargs)

    def pim_set_bsr_priority(self, device_name, priority='', interface='', ip='', **kwargs):
        """
        Description: Configures a candidate bootstrap router priority on an interface.

        Supported Agents and OS:
            CLI: EXOS, VOSS, EOS
        """
        args = {
            "interface": interface,
            "ip": ip,
            "priority": priority
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_BSR_PRIORITY,
                                    **kwargs)

    def pim_clear_cache(self, device_name, mcast_group_address='', **kwargs):
        """
        Description: Clears the PIM cache.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "mcast_group_address": mcast_group_address
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_CACHE,
                                    **kwargs)

    def pim_enable_interface(self, device_name, port='', **kwargs):
        """
        Description: Enable PIM on a given interface type.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_INTERFACE,
                                    **kwargs)

    def pim_enable_interface_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enable PIM on a given vlan.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_INTERFACE_VLAN,
                                    **kwargs)

    def pim_enable_ssm(self, device_name, answer='', **kwargs):
        """
        Description: Enable PIM SSM.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "answer": answer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_SSM,
                                    **kwargs)

    def pim_disable_interface(self, device_name, port='', **kwargs):
        """
        Description: Disables PIM on a given interface type.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_INTERFACE,
                                    **kwargs)

    def pim_disable_interface_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disables PIM on a given vlan.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_INTERFACE_VLAN,
                                    **kwargs)

    def pim_set_bsr_priority_vlan(self, device_name, vlan='', priority='', **kwargs):
        """
        Description: Configures a candidate bootstrap router priority on a vlan.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "priority": priority,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_BSR_PRIORITY_VLAN,
                                    **kwargs)

    def pim_set_rp_static(self, device_name, answer='', **kwargs):
        """
        Description: Sets the device to be a static RP which ignores the Boot Strap Router mechanism.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "answer": answer
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RP_STATIC,
                                    **kwargs)

    def pim_set_interface_active(self, device_name, port='', **kwargs):
        """
        Description: Set's the PIM interface to active.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INTERFACE_ACTIVE,
                                    **kwargs)

    def pim_set_interface_passive(self, device_name, port='', **kwargs):
        """
        Description: Set's the PIM interface to passive.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INTERFACE_PASSIVE,
                                    **kwargs)

    def pim_set_vlan_active(self, device_name, vlan='', **kwargs):
        """
        Description: Set's the PIM vlan to active.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VLAN_ACTIVE,
                                    **kwargs)

    def pim_set_vlan_passive(self, device_name, vlan='', **kwargs):
        """
        Description: Set's the PIM vlan to passive.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VLAN_PASSIVE,
                                    **kwargs)

    def pim_clear_rp(self, device_name, ip='', mask='', **kwargs):
        """
        Description: Clears the PIM RP.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {
            "ip": ip,
            "mask": mask
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RP,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def pim_verify_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Verifies that PIM is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_PIM_STATE, True,
                                           "PIM is enabled on {device_name}.",
                                           "PIM is DISABLED on on {device_name}!",
                                           **kwargs)

    def pim_verify_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Verifies that PIM is Disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_PIM_STATE, False,
                                           "PIM is Disabled on {device_name}.",
                                           "PIM is ENABLED on interface on {device_name}!",
                                           **kwargs)

    def pim_verify_enabled_on_interface(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [interface]    - The interface(s) that PIM should be enabled on.
        [ip_version]   - The IP version of PIM that should be enabled.
                         NOTE: ip_version is used only by EOS.
        [port_type]    - The interface type (ie. GigabitEthernet, Loopback, etc.)
        [port_num]     - The interface number (ie. 1/5)
                         NOTE: port_type and port_num are used only for VOSS.

        Verifies that PIM is enabled on a given interface.
        """
        args = {"interface": interface}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_PIM_INTERFACE_STATE, True,
                                           "PIM was enabled on interface {interface} on {device_name}.",
                                           "PIM was DISABLED on interface {interface} on {device_name}!",
                                           **kwargs)

    def pim_verify_disabled_on_interface(self, device_name, interface='', ip_version="ipv4", **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [interface]    - The interface(s) that PIM should be disabled on.
        [ip_version]   - The IP version of PIM that should be disabled.
                         NOTE: ip_version is used only for EOS.
        [port_type]    - The interface type (ie. GigabitEthernet, Loopback, etc.)
        [port_num]     - The interface number (ie. 1/5)
                         NOTE: port_type and port_num are only for VOSS.

        Verifies that PIM is disabled on a given interface.
        """
        ipv6_options = ["6", "ipv6", "v6"]

        if ip_version.lower() in ipv6_options:
            ip_version = "ipv6"
        else:
            ip_version = "ip"

        args = {"ip_ver": ip_version,
                "interface": interface}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_PIM_INTERFACE_STATE, False,
                                           "PIM was disabled on interface {interface} on {device_name}.",
                                           "PIM was ENABLED on interface {interface} on {device_name}!",
                                           **kwargs)

    def pim_verify_enabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [vlan]         - The interface vlan that PIM should be enabled on.
        NOTE: This keyword is used only for VOSS.

        Verifies that PIM is enabled on a given vlan.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_PIM_VLAN_STATE, True,
                                           "PIM is enabled on vlan {vlan} on {device_name}.",
                                           "PIM is DISABLED on vlan {vlan} on {device_name}!",
                                           **kwargs)

    def pim_verify_disabled_on_vlan(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [vlan]         - The interface vlan that PIM should be enabled on.
        NOTE: This keyword is used only for VOSS.

        Verifies that PIM is disabled on a given vlan.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_PIM_VLAN_STATE, False,
                                           "PIM is disabled on vlan {vlan} on {device_name}.",
                                           "PIM is ENABLED on vlan {vlan} on {device_name}!",
                                           **kwargs)

    def pim_verify_sparse_mode_enabled(self, device_name, interface='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Verifies that PIM SPARSE MODE is enabled.
        """
        args = {"interface": interface}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_PIM_TYPE_SPARSE, True,
                                           "PIM SPARSE MODE is enabled on {device_name}.",
                                           "PIM SPARSE MODE is DISABLED on on {device_name}!",
                                           **kwargs)

    def pim_verify_ssm_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.

        Verifies that PIM SSM is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_PIM_TYPE_SSM, True,
                                           "PIM SSM is enabled on {device_name}.",
                                           "PIM SSM is DISABLED on on {device_name}!",
                                           **kwargs)

    def pim_verify_expected_bsr_ip(self, device_name, expected_bsr_ip='', **kwargs):
        """
        Keyword Arguments:
        [device_names]     - The device(s) the keyword should be run against.
        [expected_bsr_ip]  - The Expected BSR IP address to verify.

        Verifies that the expected BSR IP Address is present on the device .
        """
        args = {"expected_bsr_ip": expected_bsr_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_PIM_EXPECTED_BSR, True,
                                           "The expected BSR IP Address {expected_bsr_ip} is present on {device_name}.",
                                           "The expected BSR IP Address {expected_bsr_ip} is NOT present on "
                                           "{device_name}!",
                                           **kwargs)

    def pim_verify_expected_bsr_ip_is_not_present(self, device_name, expected_bsr_ip='', **kwargs):
        """
        Keyword Arguments:
        [device_names]    - The device(s) the keyword should be run against.
        [expected_bsr_ip] - The expected BSR IP address that should not be set.

        Verify that the expected BSR IP Address is not present on the device.
        """
        args = {"expected_bsr_ip": expected_bsr_ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.VERIFY_PIM_EXPECTED_BSR, False,
                                           "The expected BSR IP Address {expected_bsr_ip} is not present on "
                                           "{device_name}.",
                                           "The expected BSR IP Address {expected_bsr_ip} IS present on {device_name}!",
                                           **kwargs)

    def pim_verify_candidate_bsr_ip(self, device_name, interface='', ip_address='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [interface]    - The interface that should be set as a candidate BSR.
        [ip_address]   - The IP address that should be set as a candidate BSR.

        Verify that a given IP address is configured as a candidate BSR.
        """
        args = {"ip_address": ip_address,
                "interface": interface}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BSR,
                                           self.parse_const.CHECK_PIM_BSR, True,
                                           "IP Address {ip_address} is set as a candidate BSR on {device_name}.",
                                           "IP Address {ip_address} is NOT set as a candidate BSR on {device_name}!",
                                           **kwargs)

    def pim_verify_candidate_bsr_ip_not_present(self, device_name, interface='', ip_address='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [interface]    - The interface to be checked.
        [ip_address]   - The IP address that should not be set as a candidate BSR..

        Verify that a given IP address is not configured as a candidate BSR.
        """
        args = {"ip_address": ip_address,
                "interface": interface}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BSR,
                                           self.parse_const.CHECK_PIM_BSR, False,
                                           "IP Address {ip_address} is not a candidate BSR on {device_name}.",
                                           "IP Address {ip_address} IS a candidate BSR on {device_name}!",
                                           **kwargs)

    def pim_verify_candidate_rp_ip(self, device_name, ip='', group='', mask='', interface='', acl='',
                                   **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device(s) the keyword should run against.
        [interface]    - The interface that should the candidate RP should be set on.
        [ip_address]   - The IP address that should be set as a candidate RP.
        [acl]          - The ACL applied to the candidate RP.

        Verifies that a given IP address is configured as a candidate Rendezvous Point.
        """
        args = {"interface": interface,
                "mcast_group_address": group,
                "mask": mask,
                "ip": ip,
                "acl": acl}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RP,
                                           self.parse_const.CHECK_PIM_CANDIDATE_RP_IP, True,
                                           "{ip} is set as a candidate RP on {device_name}.",
                                           "{ip} IS NOT set as a candidate RP on {device_name}!",
                                           **kwargs)

    def pim_verify_candidate_rp_ip_group_mask(self, device_name, ip='', group='', mask='', interface='', acl='',
                                              **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device(s) the keyword should run against.
        [interface]    - The interface that should the candidate RP should be set on.
        [ip_address]   - The IP address that should be set as a candidate RP.
        [acl]          - The ACL applied to the candidate RP.

        Verifies that a given IP address is configured as a candidate Rendezvous Point.
        """
        args = {"interface": interface,
                "mcast_group_address": group,
                "mask": mask,
                "ip": ip,
                "acl": acl}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RP,
                                           self.parse_const.CHECK_PIM_CANDIDATE_RP_IP_GROUP_MASK, True,
                                           "The Group Multicast Address {mcast_group_address} and Mask {mask} is "
                                           "properly set for Candidate RP {ip} on {device_name}.",
                                           "The Group Multicast Address and Mask for Candidate RP {ip} IS NOT properly "
                                           "set on {device_name}!",
                                           **kwargs)

    def pim_verify_rp_set(self, device_name, mcast_group_address='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]          - The device(s) the keyword should run against.
        [mcast_group_address]  - The Multicast Group IP Address to verify.
        [ip]                   - The Rendesvous Point IP address to verify.

        Verifies that a given Multicast Group and RP IP address set is present on the device.
        """
        args = {"mcast_group_address": mcast_group_address,
                "ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RP_SET,
                                           self.parse_const.VERIFY_PIM_RP_SET, True,
                                           "The Group Multicast Address {mcast_group_address} is set for RP {ip} on "
                                           "{device_name}.",
                                           "The Group Multicast Address {mcast_group_address} is NOT set for RP {ip} "
                                           "on {device_name}!",
                                           **kwargs)

    def pim_verify_rp_set_is_not_present(self, device_name, mcast_group_address='', ip='', **kwargs):
        """
        Keyword Arguments:
        [device_name]          - The device(s) the keyword should run against.
        [mcast_group_address]  - The Multicast Group IP Address to verify.
        [ip_address]           - The Rendesvous Point IP address to verify.

        Verifies that a given Multicast Group and RP IP address set is not present on the device.
        """
        args = {"mcast_group_address": mcast_group_address,
                "ip": ip}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RP_SET,
                                           self.parse_const.VERIFY_PIM_RP_SET, False,
                                           "The Group Multicast Address {mcast_group_address} is not set for RP {ip} "
                                           "on {device_name}.",
                                           "The Group Multicast Address {mcast_group_address} IS set for RP {ip} on "
                                           "{device_name}!",
                                           **kwargs)

    def pim_verify_candidate_rp_ip_not_present(self, device_name, interface='', ip_address='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [interface]    - The interface that should checked.
        [ip_address]   - The IP that should not be set as a candidate RP.

        Verifies that a given IP address is not configured as a candidate RP.
        """
        args = {"interface": interface,
                "ip_address": ip_address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RP,
                                           self.parse_const.CHECK_PIM_RP, False,
                                           "IP Address {ip_address} is not configured as a candidate RP on "
                                           "{device_name}.",
                                           "IP Address {ip_address} IS configured as a candidate RP on {device_name}!",
                                           **kwargs)

    def pim_verify_candidate_rp_static(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        NOTE:  This keyword is used on VOSS only.

        Verifies that the candidate rp is set to static.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RP,
                                           self.parse_const.CHECK_PIM_STATIC_RP, True,
                                           "PIM candidate RP is set to STATIC on {device_name}.",
                                           "PIM candidate RP IS NOT set to STATIC on {device_name}!",
                                           **kwargs)

    def pim_verify_current_bsr_priority(self, device_name, priority='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [priority]    - The candidate bootstrap priority value.

        Verifies the current Boot Strap Router's priority.
        """
        args = {"priority": priority}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_BSR,
                                           self.parse_const.CHECK_PIM_BSR_PRIORITY, True,
                                           "The Current PIM Bootstrap Router's Priority is set to {priority}.",
                                           "The Current PIM Bootstrap Router's Priority IS NOT set to {priority}",
                                           **kwargs)

    def pim_verify_current_mode(self, device_name, pim_mode='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [pim_mode]    - The current PIM Mode that is set.

        Verifies the current PIM Mode (ie. Sparse, SSM, etc.).
        """
        args = {"pim_mode": pim_mode}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_PIM_MODE, True,
                                           "The Current PIM MODE is set to {pim_mode}.",
                                           "The Current PIM MODE IS NOT set to {pim_mode}",
                                           **kwargs)

    def pim_verify_candidate_bsr_priority_interface(self, device_name, interface='', priority='', interface_ip='',
                                                    **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [interface]   - The interface or port to set the candidate bootstrap priority on.
        [priority]    - The candidate bootstrap priority value.

        Checks that a given interface is set to a specified bootstrap router priority.
        """
        args = {"interface": interface,
                "ip": interface_ip,
                "priority": priority}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INTERFACE,
                                           self.parse_const.CHECK_PIM_CANDIDATE_BSR_PRIORITY_ON_INTERFACE, True,
                                           "PIM candidate bootstrap router priority for {interface} is properly "
                                           "set to {priority}.",
                                           "PIM candidate bootstrap router priority for {interface} IS NOT set "
                                           "to {priority}!",
                                           **kwargs)

    def pim_verify_candidate_bsr_priority_vlan(self, device_name, vlan='', priority='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN that should be checked for the specified bootstrap router priority.
        [priority]    - The candidate bootstrap priority value.

        Checks that a given VLAN is set to a specified bootstrap router priority.
        """
        args = {"vlan": vlan,
                "priority": priority}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLAN,
                                           self.parse_const.CHECK_PIM_CANDIDATE_BSR_PRIORITY_ON_VLAN, True,
                                           "PIM candidate bootstrap router priority for vlan {vlan} is properly "
                                           "set to {priority}.",
                                           "PIM candidate bootstrap router priority for vlan {vlan} IS NOT set "
                                           "to {priority}!.",
                                           **kwargs)

    def pim_verify_any_source_group_entry(self, device_name, dest_group='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device(s) the keyword should run against.
        [dest_group]   - The multicast destination group ip address to verify.

        Verifies that a given PIM (*,G) entry is present in the PIM cache table for the device.
        """
        args = {"dest_group": dest_group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CACHE,
                                           self.parse_const.VERIFY_PIM_ANY_SOURCE_GROUP, True,
                                           "A *,G entry for the multicast destination address {dest_group} is present "
                                           "on {device_name}.",
                                           "A *,G entry for the multicast destination address {dest_group} is NOT "
                                           "present on {device_name}!",
                                           **kwargs)

    def pim_verify_any_source_group_entry_is_not_present(self, device_name, dest_group='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device(s) the keyword should run against.
        [dest_group]   - The multicast destination group ip address to verify.

        Verifies that a given PIM (*,G) entry is not present in the PIM cache table for the device.
        """
        args = {"dest_group": dest_group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CACHE,
                                           self.parse_const.VERIFY_PIM_ANY_SOURCE_GROUP, False,
                                           "A *,G entry for the multicast destination address {dest_group} is not "
                                           "present on {device_name}.",
                                           "A *,G entry for the multicast destination address {dest_group} IS present "
                                           "on {device_name}!",
                                           **kwargs)

    def pim_verify_source_group_entry(self, device_name, source_ip='', dest_group='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device(s) the keyword should run against.
        [source_ip]    - The source ip address to verify.
        [dest_group]   - The multicast destination group ip address to verify.

        Verifies that a given PIM (S,G) entry is present in the PIM cache table for the device.
        """
        args = {"source_ip": source_ip,
                "dest_group": dest_group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CACHE,
                                           self.parse_const.VERIFY_PIM_SOURCE_GROUP, True,
                                           "A Source Group(S,G) entry for source {source_ip} and multicast destination "
                                           "address {dest_group} is present on {device_name}.",
                                           "A Source Group(S,G) entry for source {source_ip} and multicast destination "
                                           "address {dest_group} is NOT present on {device_name}!",
                                           **kwargs)

    def pim_verify_source_group_entry_is_not_present(self, device_name, source_ip='', dest_group='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device(s) the keyword should run against.
        [source_ip]    - The source ip address to verify.
        [dest_group]   - The multicast destination group ip address to verify.

        Verifies that a given PIM (S,G) entry is present in the PIM cache table for the device.
        """
        args = {"source_ip": source_ip,
                "dest_group": dest_group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CACHE,
                                           self.parse_const.VERIFY_PIM_SOURCE_GROUP, False,
                                           "A Source Group(S,G) entry for source {source_ip} and multicast destination "
                                           "address {dest_group} is not present on {device_name}.",
                                           "A Source Group(S,G) entry for source {source_ip} and multicast destination "
                                           "address {dest_group} IS present on {device_name}!",
                                           **kwargs)

    def pim_verify_cache_entry(self, device_name, mcast_group_address='', **kwargs):
        """
        Keyword Arguments:
        [device_name]          - The device(s) the keyword should run against.
        [mcast_group_address]  - The multicast group address to verify.

        Verifies a given multicast group address is present in the PIM cache table for the device.
        """
        args = {"mcast_group_address": mcast_group_address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CACHE,
                                           self.parse_const.CHECK_PIM_CACHE, True,
                                           "The multicast group address {mcast_group_address} is present "
                                           "in the pim cache on {device_name}.",
                                           "The multicast group address {mcast_group_address} is NOT present "
                                           "in the pim cache on {device_name}!",
                                           **kwargs)

    def pim_verify_cache_entry_is_not_present(self, device_name, mcast_group_address='', **kwargs):
        """
        Keyword Arguments:
        [device_name]          - The device(s) the keyword should run against.
        [mcast_group_address]  - The multicast group address to verify.

        Verifies a given multicast group address is not present in the PIM cache table for the device.
        """
        args = {"mcast_group_address": mcast_group_address}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CACHE,
                                           self.parse_const.CHECK_PIM_CACHE, False,
                                           "The multicast group address {mcast_group_address} is not "
                                           "present in the pim cache on {device_name}.",
                                           "The multicast group address {mcast_group_address} IS present "
                                           "in the pim cache on {device_name}!",
                                           **kwargs)
