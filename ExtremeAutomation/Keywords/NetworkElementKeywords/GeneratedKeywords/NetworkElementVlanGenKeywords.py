"""
Keyword class for all vlan cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.VlanConstants import \
    VlanConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.VlanConstants import \
    VlanConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementVlanGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementVlanGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "vlan"

    def vlan_create_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Creates the specified VLAN ID.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            REST: EXOS, SNAPROUTE
            SNMP: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_VLAN,
                                    **kwargs)

    def vlan_delete_vlan(self, device_name, vlan='', topology_name='', **kwargs):
        """
        Description: Removes the specified VLAN on a given device.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX, EXTRWIRELESS
            REST: EXOS, SNAPROUTE
            SNMP: VOSS
        """
        args = {
            "topology_name": topology_name,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_VLAN,
                                    **kwargs)

    def vlan_create_vman(self, device_name, vman='', **kwargs):
        """
        Description: Creates the specified VMAN ID.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "vman": vman
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_VMAN,
                                    **kwargs)

    def vlan_delete_vman(self, device_name, vman='', **kwargs):
        """
        Description: Removes a VMAN on a given device.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "vman": vman
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_VMAN,
                                    **kwargs)

    def vlan_enable_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Enables a given VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_VLAN,
                                    **kwargs)

    def vlan_disable_vlan(self, device_name, vlan='', **kwargs):
        """
        Description: Disabled a given VLAN.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_VLAN,
                                    **kwargs)

    def vlan_enable_dynamic_egress(self, device_name, vlan='', **kwargs):
        """
        Description: Sets dynamic egress on VLAN enabled or disabled.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_DYNAMIC_EGRESS,
                                    **kwargs)

    def vlan_disable_dynamic_egress(self, device_name, vlan='', **kwargs):
        """
        Description: Sets dynamic egress on VLAN enabled or disabled.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_DYNAMIC_EGRESS,
                                    **kwargs)

    def vlan_set_egress_untagged(self, device_name, vlan='', port='', **kwargs):
        """
        Description: Adds [ports] to [vlan]'s untagged egress list.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            REST: SNAPROUTE
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_EGRESS_UNTAGGED,
                                    **kwargs)

    def vlan_set_egress_tagged(self, device_name, vlan='', port='', **kwargs):
        """
        Description: Adds [ports] to [vlan]'s tagged egress list.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            REST: SNAPROUTE
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_EGRESS_TAGGED,
                                    **kwargs)

    def vlan_set_egress_forbidden(self, device_name, vlan='', port='', **kwargs):
        """
        Description: Adds [ports] to [vlan]'s forbidden egress list.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_EGRESS_FORBIDDEN,
                                    **kwargs)

    def vlan_clear_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Description: Removes [ports] from the [vlan]'s egress list.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_EGRESS,
                                    **kwargs)

    def vlan_clear_egress_type(self, device_name, egress_type='', port='', vlan='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "egress_type": egress_type,
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_EGRESS_TYPE,
                                    **kwargs)

    def vlan_set_description(self, device_name, vlan='', name='', **kwargs):
        """
        Description: Set VLAN name to specified name.

        Supported Agents and OS:
            CLI: EOS, EXOS, SLX
        """
        args = {
            "name": name,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DESCRIPTION,
                                    **kwargs)

    def vlan_clear_description(self, device_name, vlan='', **kwargs):
        """
        Description: Clears the  VLAN description.

        Supported Agents and OS:
            CLI: EOS, EXOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_DESCRIPTION,
                                    **kwargs)

    def vlan_set_name(self, device_name, vlan='', name='', **kwargs):
        """
        Description: Set VLAN name to specified name.

        Supported Agents and OS:
            CLI: EOS, EXOS, VOSS, SLX
            SNMP: VOSS
        """
        args = {
            "name": name,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NAME,
                                    **kwargs)

    def vlan_clear_name(self, device_name, vlan='', **kwargs):
        """
        Description: Clear specified VLAN's name.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_NAME,
                                    **kwargs)

    def vlan_set_pvid(self, device_name, port='', vlan='', modify_egress='', **kwargs):
        """
        Description: Applies the given PVID value to a port.

        Supported Agents and OS:
            CLI: EOS, VOSS, SLX
        """
        args = {
            "modify_egress": modify_egress,
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PVID,
                                    **kwargs)

    def vlan_clear_pvid(self, device_name, port='', vlan='', **kwargs):
        """
        Description: Clears the PVID on the given <api_utils.port>.

        Supported Agents and OS:
            CLI: EOS, VOSS, SLX
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PVID,
                                    **kwargs)

    def vlan_create_vlan_with_name(self, device_name, vlan='', tag='', topology_name='', mode='', **kwargs):
        """
        Description: Creates a VLAN by name with a tag value.

        Supported Agents and OS:
            CLI: EXOS, EXTRWIRELESS
        """
        args = {
            "mode": mode,
            "tag": tag,
            "topology_name": topology_name,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_VLAN_WITH_NAME,
                                    **kwargs)

    def vlan_set_vman_egress_untagged(self, device_name, vman='', port='', **kwargs):
        """
        Description: Adds [ports] to [vman]'s untagged port list.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "vman": vman
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VMAN_EGRESS_UNTAGGED,
                                    **kwargs)

    def vlan_set_vman_egress_tagged(self, device_name, vman='', port='', **kwargs):
        """
        Description: Adds [ports] to [vman]'s tagged port list.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "vman": vman
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VMAN_EGRESS_TAGGED,
                                    **kwargs)

    def vlan_clear_vman_egress(self, device_name, vman='', port='', **kwargs):
        """
        Description: Removes [ports] from the [vman]'s port list.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "vman": vman
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_VMAN_EGRESS,
                                    **kwargs)

    def vlan_set_nsi(self, device_name, vlan='', nsi='', **kwargs):
        """
        Description: Configures the NSI (Network Service Identifier) for a specified VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "nsi": nsi,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NSI,
                                    **kwargs)

    def vlan_clear_nsi(self, device_name, vlan='', nsi='', **kwargs):
        """
        Description: Removes the NSI (Network Service Identifier) for a specified VLAN.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "nsi": nsi,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_NSI,
                                    **kwargs)

    def vlan_set_isid(self, device_name, vlan='', i_sid='', **kwargs):
        """
        Description: Configures a VLAN I-SID for a specified VLAN.

        Supported Agents and OS:
            CLI: EXOS, VOSS
            SNMP: VOSS
        """
        args = {
            "i_sid": i_sid,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ISID,
                                    **kwargs)

    def vlan_clear_isid(self, device_name, vlan='', i_sid='', **kwargs):
        """
        Description: Removes a VLAN I-SID for a specified VLAN.

        Supported Agents and OS:
            CLI: EXOS, VOSS
            SNMP: VOSS
        """
        args = {
            "i_sid": i_sid,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ISID,
                                    **kwargs)

    def vlan_create_spbm(self, device_name, vlan='', **kwargs):
        """
        Description: Creates the specified SPBM VLAN on the VOSS platform.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_SPBM,
                                    **kwargs)

    def vlan_set_member(self, device_name, port='', vlan='', **kwargs):
        """
        Description: Adds a port to a vlan (Makes a port a member of a vlan).

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MEMBER,
                                    **kwargs)

    def vlan_clear_member(self, device_name, port='', vlan='', **kwargs):
        """
        Description: Removes a port from a specified vlan.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MEMBER,
                                    **kwargs)

    def vlan_set_port_encapsulation_dot1q(self, device_name, port='', **kwargs):
        """
        Description: Configures encapsulation dot1q on a given port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_ENCAPSULATION_DOT1Q,
                                    **kwargs)

    def vlan_clear_port_encapsulation_dot1q(self, device_name, port='', **kwargs):
        """
        Description: Removes encapsulation dot1q on a given port.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_ENCAPSULATION_DOT1Q,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def vlan_verify_exists(self, device_name, vlans='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [vlan] - The VLAN to check the existence of.

        Verifies the specified VLAN exists on the given device.
        """
        args = {"vlan": vlans,
                "oid_index": vlans}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_INFO,
                                           self.parse_const.CHECK_VLAN_EXISTS, True,
                                           "VLAN {vlan} exists on {device_name}.",
                                           "VLAN {vlan} DOES NOT exist on {device_name}.",
                                           **kwargs)

    def vlan_verify_does_not_exist(self, device_name, vlans='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [vlan] - The VLAN to check the existence of.

        Verifies the specified VLAN does not exist on the given device.
        """
        args = {"vlan": vlans,
                "oid_index": vlans}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_INFO,
                                           self.parse_const.CHECK_VLAN_EXISTS, False,
                                           "VLAN {vlan} DOES NOT exist on {device_name}.",
                                           "VLAN {vlan} exists on {device_name}.",
                                           **kwargs)

    def vlan_verify_vman_exists(self, device_name, vman='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vman]        - The VMAN(s) that should exist on the device.

        Verifies that a VMAN exists on a given device.
        """
        args = {"vman": vman}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_VMAN_INFO,
                                           self.parse_const.CHECK_VMAN_EXISTS, True,
                                           "VMAN {vman} exists on {device_name}.",
                                           "VMAN {vman} DOES NOT exist on {device_name}.",
                                           **kwargs)

    def vlan_verify_vman_does_not_exist(self, device_name, vman='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [vman]        - The VMAN(s) that should exist on the device.

        Verifies that a VMAN exists on a given device.
        """
        args = {"vman": vman}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_VMAN_INFO,
                                           self.parse_const.CHECK_VMAN_EXISTS, False,
                                           "VMAN {vman} does not exist on {device_name}.",
                                           "VMAN {vman} EXISTS on {device_name}.",
                                           **kwargs)

    def vlan_verify_port_on_untagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should be on the untagged egress list.

        Checks if a port is on the untagged egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_UNTAGGED_PORTS, True,
                                           "Port {port} is on the untagged egress list of {vlan}.",
                                           "Port {port} is NOT on the untagged egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_not_on_untagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should not be on the untagged egress list.

        Checks if a port is not on the untagged egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_UNTAGGED_PORTS, False,
                                           "Port {port} is not on the untagged egress list of {vlan}.",
                                           "Port {port} IS on the untagged egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_not_on_operational_untagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should not be on the untagged egress list.

        Checks if a port is not on the untagged egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_UNTAGGED_OPERATIONAL_PORTS, False,
                                           "Port {port} is NOT on the untagged egress list of {vlan}.",
                                           "Port {port} is on the untagged egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_on_tagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should be on the tagged egress list.

        Checks if a port is on the tagged egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_TAGGED_PORTS, True,
                                           "Port {port} is on the tagged egress list of {vlan}.",
                                           "Port {port} is NOT on the tagged egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_not_on_tagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The ports that should not be on the tagged egress list.

        Checks if a port is not on the tagged egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_TAGGED_PORTS, False,
                                           "Port {port} is not on the tagged egress list of {vlan}.",
                                           "Port {port} IS on the tagged egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_not_on_operational_tagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should not be on the tagged egress list.

        Checks if a port is not on the operational tagged egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_TAGGED_OPERATIONAL_PORTS, False,
                                           "Port {port} is not on the tagged egress list of {vlan}.",
                                           "Port {port} IS on the tagged egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_on_forbidden_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should be on the forbidden egress list.

        Checks if a port is on the forbidden egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_FORBIDDEN_PORTS, True,
                                           "Port {port} is on the forbidden egress list of {vlan}.",
                                           "Port {port} is NOT on the forbidden egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_on_static_forbidden_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should be on the static forbidden egress list.

        Checks if a port is on the static forbidden egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATIC,
                                           self.parse_const.CHECK_FORBIDDEN_PORTS, True,
                                           "Port {port} is on the forbidden egress list of {vlan}.",
                                           "Port {port} is NOT on the forbidden egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_on_static_untagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan] - The VLAN egress list to check.
        [port] - The port(s) that should be on the static untagged egress list.

        Checks if a port is on the static untagged egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATIC,
                                           self.parse_const.CHECK_UNTAGGED_PORTS, True,
                                           "Port {port} is on the static untagged egress list of {vlan}.",
                                           "Port {port} is NOT on the static untagged egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_on_static_tagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should be on the static tagged egress list.

        Checks if a port is on the static tagged egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATIC,
                                           self.parse_const.CHECK_TAGGED_PORTS, False,
                                           "Port {port} is on the static tagged egress list of {vlan}",
                                           "Port {port} is NOT on the static tagged egress list of {vlan}",
                                           **kwargs)

    def vlan_verify_port_not_on_static_tagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should be on the static tagged egress list.

        Checks if a port is on the static tagged egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATIC,
                                           self.parse_const.CHECK_TAGGED_PORTS, False,
                                           "Port {port} is on the static tagged egress list of {vlan}",
                                           "Port {port} is NOT on the static tagged egress list of {vlan}",
                                           **kwargs)

    def vlan_verify_port_not_on_forbidden_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN egress list to check.
        [port]        - The port(s) that should not be on the forbidden egress list.

        Checks if a port is not on the forbidden egress list of a given VLAN.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.CHECK_FORBIDDEN_PORTS, False,
                                           "Port {port} is not on the forbidden egress list of {vlan}.",
                                           "Port {port} IS on the forbidden egress list of {vlan}.",
                                           **kwargs)

    def vlan_verify_port_on_vman_untagged(self, device_name, vman='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vman]        - The VMAN portmember list to check.
        [port]        - The port(s) that should be on the untagged member list.

        Checks if a port is on the untagged member list of a given VMAN.
        """
        args = {"vman": vman,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VMAN_INFO,
                                           self.parse_const.CHECK_VMAN_UNTAGGED_PORTS, True,
                                           "Port {port} is on the untagged member list of {vman}.",
                                           "Port {port} is NOT on the untagged member list of {vman}.",
                                           **kwargs)

    def vlan_verify_port_not_on_vman_untagged(self, device_name, vman='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vman]        - The VMAN egress list to check.
        [port]        - The port(s) that should not be on the untagged member list.

        Checks if a port is not on the untagged member list of a given VMAN.
        """
        args = {"vman": vman,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VMAN_INFO,
                                           self.parse_const.CHECK_VMAN_UNTAGGED_PORTS, False,
                                           "Port {port} is not on the untagged member list of {vman}.",
                                           "Port {port} IS on the untagged member list of {vman}.",
                                           **kwargs)

    def vlan_verify_port_on_vman_tagged(self, device_name, vman='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vman]        - The VMAN portmember list to check.
        [port]        - The port(s) that should be on the tagged member list.

        Checks if a port is on the tagged member list of a given VMAN.
        """
        args = {"vman": vman,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VMAN_INFO,
                                           self.parse_const.CHECK_VMAN_TAGGED_PORTS, True,
                                           "Port {port} is on the tagged member list of {vman}.",
                                           "Port {port} is NOT on the tagged member list of {vman}.",
                                           **kwargs)

    def vlan_verify_port_not_on_vman_tagged(self, device_name, vman='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vman]        - The VMAN portmember list to check.
        [port]        - The port(s) that should not be on the tagged member list.

        Checks if a port is not on the tagged member list of a given VLAN.
        """
        args = {"vman": vman,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VMAN_INFO,
                                           self.parse_const.CHECK_VMAN_TAGGED_PORTS, False,
                                           "Port {port} is not on the tagged member list of {vman}.",
                                           "Port {port} IS on the tagged member list of {vman}.",
                                           **kwargs)

    def vlan_verify_enabled(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN that should be enabled.

        Checks if a VLAN is enabled on a given device.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_VLAN_STATE, True,
                                           "VLAN {vlan} is enabled on {device_name}.",
                                           "VLAN {vlan} is DISABLED on {device_name}.",
                                           **kwargs)

    def vlan_verify_disabled(self, device_name, vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN that should be enabled.

        Checks if a VLAN is disabled on a given device.
        """
        args = {"vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATUS,
                                           self.parse_const.CHECK_VLAN_STATE, False,
                                           "VLAN {vlan} is disabled on {device_name}.",
                                           "VLAN {vlan} is ENABLED on {device_name}.",
                                           **kwargs)

    def vlan_verify_port_pvid(self, device_name, port='', pvid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) whose PVID should be examined.
        [pvid]        - The PVID value the port should have configured.

        Checks if a ports PVID is set to a given value.
        """
        args = {"port": port,
                "pvid": pvid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PVID,
                                           self.parse_const.CHECK_PORT_PVID, True,
                                           "Port {port}'s PVID value was equal to {pvid}.",
                                           "Port {port}'s PVID value was NOT equal to {pvid}.",
                                           **kwargs)

    def vlan_verify_port_does_not_have_pvid(self, device_name, port='', pvid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) whose PVID should be examined.
        [pvid]        - The PVID value the port should have configured.

        Checks if a ports PVID is not set to a given value.
        """
        args = {"port": port,
                "pvid": pvid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PVID,
                                           self.parse_const.CHECK_PORT_PVID, False,
                                           "Port {port}'s PVID value was not equal to {pvid}.",
                                           "Port {port}'s PVID value was EQUAL to {pvid}.",
                                           **kwargs)

    def vlan_verify_tag(self, device_name, vlan='', tag='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN whose tag should be checked.
        [tag]         - The tag that <vlan> should be set to.

        Checks that a given VLAN is configured with the specified tag.
        """
        args = {"vlan": vlan,
                "tag": tag}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.GET_VLAN_TAG, True,
                                           "VLAN {vlan} was configured with tag {tag}.",
                                           "VLAN {vlan} was NOT configured with tag {tag}.",
                                           **kwargs)

    def vlan_verify_tag_not_equal(self, device_name, vlan='', tag='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The name of the vlan whose tag should be checked.
        [tag]         - The tag that <vlan> should be set to.

        Checks that a given VLAN is not configured with the specified tag.
        """
        args = {"vlan": vlan,
                "tag": tag}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INFO,
                                           self.parse_const.GET_VLAN_TAG, False,
                                           "VLAN {vlan} was notconfigured with tag {tag}.",
                                           "VLAN {vlan} WAS configured with tag {tag}.",
                                           **kwargs)

    def vlan_verify_name(self, device_name, vlan='', name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN whose name should exist.
        [name]        - The name that should exist on the VLAN.

        Checks that a VLAN is set to have the given name.
        """
        args = {"vlan": vlan,
                "oid_index": vlan,
                "name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NAME,
                                           self.parse_const.CHECK_VLAN_NAME, True,
                                           "VLAN {vlan} is named {name}.",
                                           "VLAN {vlan} is NOT named {name}.",
                                           **kwargs)

    def vlan_verify_name_is_not(self, device_name, vlan='', name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN whose name should exist.
        [name]        - The name that should exist on the VLAN.

        Checks that a VLAN is set to have the given name.
        """
        args = {"vlan": vlan,
                "name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NAME,
                                           self.parse_const.CHECK_VLAN_NAME, False,
                                           "VLAN {vlan} is not named {name}.",
                                           "VLAN {vlan} IS named {name}.",
                                           **kwargs)

    def vlan_verify_name_and_id(self, device_name, vlan_name='', vlan_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan_name]   - The vlan name that should be present on the device.
        [vlan_id}     - The vlan id that should be present on the device.

        Checks that a given VLAN name and VLAN id is present on the device.
        """
        args = {"vlan_name": vlan_name,
                "vlan_id": vlan_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_INFO,
                                           self.parse_const.CHECK_VLAN_NAME_ID, True,
                                           "VLAN {vlan_id} with name {vlan_name} is present on {device_name}.",
                                           "VLAN {vlan_id} with name {vlan_name} IS NOT present on "
                                           "{device_name}!",
                                           **kwargs)

    def vlan_verify_description(self, device_name, vlan='', description='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan] - The VLAN whose name should exist.
        [description] - The description the VLAN should be configured with.

        Checks that a VLAN is set to have the given name.
        """
        args = {"vlan": vlan,
                "description": description}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DESCRIPTION,
                                           self.parse_const.CHECK_VLAN_DESCRIPTION, True,
                                           "VLAN {vlan} is configured with description {description}.",
                                           "VLAN {vlan} is NOT configured with description {description}.",
                                           **kwargs)

    def vlan_verify_description_is_not(self, device_name, vlan='', description='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN whose name should exist.
        [description] - The description that should not exist on the VLAN.

        Checks that a VLAN is set to have the given description.
        """
        args = {"vlan": vlan,
                "description": description}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DESCRIPTION,
                                           self.parse_const.CHECK_VLAN_DESCRIPTION, False,
                                           "VLAN {vlan} is not configured with description {description}.",
                                           "VLAN {vlan} IS configured with description {description}.",
                                           **kwargs)

    def vlan_verify_port_tagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN whose name should exist.

        Checks that a VLAN is on the given port egress.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_EGRESS,
                                           self.parse_const.CHECK_VLAN_ON_PORT_TAGGED_EGRESS, True,
                                           "VLAN {vlan} is on port {port}'s tagged egress.",
                                           "VLAN {vlan} is NOT on port {port}'s tagged egress.",
                                           **kwargs)

    def vlan_verify_port_untagged_egress(self, device_name, vlan='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN whose name should exist.

        Checks that a VLAN is on the given port egress.
        """
        args = {"vlan": vlan,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_EGRESS,
                                           self.parse_const.CHECK_VLAN_ON_PORT_UNTAGGED_EGRESS, True,
                                           "VLAN {vlan} is on port {port}'s untagged egress.",
                                           "VLAN {vlan} is NOT on port {port}'s untagged egress.",
                                           **kwargs)

    def vlan_verify_isid_exists(self, device_name, vlan='', i_sid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN where the i-sid should be associated with.
        [i_sid]       - The i-sid that is expected to be associated with the VLAN.

        Checks that a given i-sid is set to a given VLAN.
        """
        args = {"vlan": vlan,
                "oid_index": vlan,
                "i_sid": i_sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_VLAN_ISID, True,
                                           "I-sid {i_sid} is set to VLAN {vlan}.",
                                           "I-sid {i_sid} is NOT set to VLAN {vlan}!",
                                           **kwargs)

    def vlan_verify_isid_does_not_exist(self, device_name, vlan='', i_sid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN where the i-sid should be associated with.
        [i_sid]       - The i-sid that is expected to be associated with the VLAN.

        Checks that a given i-sid is NOT set to a given VLAN.
        """
        args = {"vlan": vlan,
                "oid_index": vlan,
                "i_sid": i_sid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ISID,
                                           self.parse_const.CHECK_VLAN_ISID, False,
                                           "I-sid {i_sid} is not set to VLAN {vlan}.",
                                           "I-sid {i_sid} IS set to VLAN {vlan}!",
                                           **kwargs)

    def vlan_verify_nsi_exists(self, device_name, vlan='', nsi='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN where the i-sid should be associated with.
        [nsi]         - The i-sid that is expected to be associated with the VLAN.

        Checks that a given nsi is set to a given VLAN.
        """
        args = {"vlan": vlan,
                "oid_index": vlan,
                "nsi": nsi}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NSI,
                                           self.parse_const.CHECK_VLAN_NSI, True,
                                           "Nsi {nsi} is set to VLAN {vlan}.",
                                           "Nsi {nsi} is NOT set to VLAN {vlan}!",
                                           **kwargs)

    def vlan_verify_nsi_does_not_exist(self, device_name, vlan='', nsi='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [vlan]        - The VLAN where the i-sid should be associated with.
        [nsi]         - The i-sid that is expected to be associated with the VLAN.

        Checks that a given nsi is not set to a given VLAN.
        """
        args = {"vlan": vlan,
                "oid_index": vlan,
                "nsi": nsi}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NSI,
                                           self.parse_const.CHECK_VLAN_NSI, False,
                                           "Nsi {nsi} is not set to VLAN {vlan}.",
                                           "Nsi {nsi} IS set to VLAN {vlan}!",
                                           **kwargs)

    def vlan_verify_port_encapsulation_dot1q(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify.

        Verifies that encapsulation dot1q is set on a given port.
        NOTE:  This keyword applies to VOSS only.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_PORT_ENCAPSULATION_DOT1Q_IS_SET, True,
                                           "Encapsulation dot1q is set on {port}.",
                                           "Encapsulation dot1q IS NOT set on {port}!",
                                           **kwargs)

    def vlan_verify_port_encapsulation_not_dot1q(self, device_name, port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port]        - The port(s) to verify.

        Verifies that encapsulation dot1q is not set on a given port.
        NOTE:  This keyword applies to VOSS only.
        """
        args = {"port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT,
                                           self.parse_const.VERIFY_PORT_ENCAPSULATION_DOT1Q_IS_SET, False,
                                           "Encapsulation dot1q is not set on {port}.",
                                           "Encapsulation dot1q IS SET on {port}!",
                                           **kwargs)

    def vlan_verify_port_is_member_of_vlan(self, device_name, port='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [ports]       - The port to verify.
        [vlan]        - The vlan to verify.

        Verifies that a given port is a member of a vlan.
        NOTE:  This keyword applies to VOSS only.  Use the cli command "show vlan members port" for verification.
        """
        args = {"port": port,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MEMBERS_PORT,
                                           self.parse_const.CHECK_PORT_IS_MEMBER_OF_VLAN, True,
                                           "{port} is a member of vlan {vlan}.",
                                           "{port} IS NOT a member of vlan {vlan}!",
                                           **kwargs)

    def vlan_verify_port_is_not_member_of_vlan(self, device_name, port='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [ports]       - The port to verify.
        [vlan]        - The vlan to verify.

        Verifies that a given port is not a member of a vlan.
        NOTE:  This keyword applies to VOSS only.   Use the cli command "show vlan members port" for verification.
        """
        args = {"port": port,
                "vlan": vlan}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MEMBERS_PORT,
                                           self.parse_const.CHECK_PORT_IS_MEMBER_OF_VLAN, False,
                                           "{port} is not a member of vlan {vlan}.",
                                           "{port} IS a member of vlan {vlan}!",
                                           **kwargs)
