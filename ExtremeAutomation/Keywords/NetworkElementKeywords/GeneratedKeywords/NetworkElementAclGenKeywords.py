"""
Keyword class for all acl cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.AclConstants import \
    AclConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.AclConstants import \
    AclConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils \
    import NetworkElementSnmpUtils as SnmpUtils


class NetworkElementAclGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementAclGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "acl"

    def acl_create_ipv4(self, device_name, name='', acl_id='', acl_type='', voss_acl_type='', **kwargs):
        """
        Description: Creates an IPv4 ACL of the given type on a device.

        Supported Agents and OS:
            CLI: EOS, VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id,
            "acl_type": acl_type,
            "name": name,
            "voss_acl_type": voss_acl_type
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_IPV4,
                                    **kwargs)

    def acl_create_ipv6(self, device_name, name='', acl_id='', acl_type='', voss_acl_type='', **kwargs):
        """
        Description: Creates an IPv6 ACL of the given type on a device.

        Supported Agents and OS:
            CLI: EOS, VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id,
            "acl_type": acl_type,
            "name": name,
            "voss_acl_type": voss_acl_type
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_IPV6,
                                    **kwargs)

    def acl_delete_list(self, device_name, name='', acl_id='', acl_type='', ip_ver='', **kwargs):
        """
        Description: Removes an ACL on a given device.

        Supported Agents and OS:
            CLI: EOS, VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id,
            "acl_type": acl_type,
            "ip_ver": ip_ver,
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_LIST,
                                    **kwargs)

    def acl_set_standard_rule(self, device_name, acl_type='', ip_ver='', name='', rule_info='', rule_type='', **kwargs):
        """
        Description: Adds a rule entry of the given types to an existing ACL.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "acl_type": acl_type,
            "ip_ver": ip_ver,
            "name": name,
            "rule_info": rule_info,
            "rule_type": rule_type
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_STANDARD_RULE,
                                    **kwargs)

    def acl_create_ace_index(self, device_name, ace_name='', acl_id='', ace_index='', **kwargs):
        """
        Description: Creates an access control entry (ACE) index ID under a designated ACL.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ace_index": ace_index,
            "ace_name": ace_name,
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_ACE_INDEX,
                                    **kwargs)

    def acl_delete_ace_index(self, device_name, acl_id='', ace_index='', **kwargs):
        """
        Description: Removes an access control entry (ACE) index ID under a designated ACL.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ace_index": ace_index,
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_ACE_INDEX,
                                    **kwargs)

    def acl_enable_list(self, device_name, acl_id='', **kwargs):
        """
        Description: Enables the state of the ACL (and all ACEs in the ACL).

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_LIST,
                                    **kwargs)

    def acl_disable_list(self, device_name, acl_id='', **kwargs):
        """
        Description: Disables the state of the ACL (and all ACEs in the ACL).

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_LIST,
                                    **kwargs)

    def acl_enable_ace(self, device_name, acl_id='', ace_index='', **kwargs):
        """
        Description: Enables the ACE. An ACE can only be modified if it is disabled.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ace_index": ace_index,
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_ACE,
                                    **kwargs)

    def acl_disable_ace(self, device_name, acl_id='', ace_index='', **kwargs):
        """
        Description: Disables the ACE. An ACE can only be modified if it is disabled.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ace_index": ace_index,
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_ACE,
                                    **kwargs)

    def acl_set_name(self, device_name, name='', acl_id='', **kwargs):
        """
        Description: Changes the ACL name of an existing ACL.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id,
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_NAME,
                                    **kwargs)

    def acl_set_default_action(self, device_name, acl_id='', action='', **kwargs):
        """
        Description: Changes the default action the ACL should take when none of the Aces in the Acl match.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id,
            "action": action
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DEFAULT_ACTION,
                                    **kwargs)

    def acl_set_port(self, device_name, acl_id='', port='', **kwargs):
        """
        Description: Adds ports to the designated ACL.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT,
                                    **kwargs)

    def acl_clear_port(self, device_name, acl_id='', port='', **kwargs):
        """
        Description: Removes ports on the designated ACL.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT,
                                    **kwargs)

    def acl_set_vlan(self, device_name, acl_id='', vlan='', **kwargs):
        """
        Description: Adds VLANS to the designated ACL.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VLAN,
                                    **kwargs)

    def acl_clear_vlan(self, device_name, acl_id='', vlan='', **kwargs):
        """
        Description: Removes vlans on the designated ACL.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "acl_id": acl_id,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_VLAN,
                                    **kwargs)

    def acl_set_ace_action(self, device_name, acl_id='', ace_index='', ace_action='', **kwargs):
        """
        Description: Operational mode associated with the Ace that takes effect on the packets matching this Ace.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ace_action": ace_action,
            "ace_index": ace_index,
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACE_ACTION,
                                    **kwargs)

    def acl_set_ace_name(self, device_name, acl_id='', ace_index='', ace_name='', **kwargs):
        """
        Description: Configures the name to be associated with the Ace.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ace_index": ace_index,
            "ace_name": ace_name,
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACE_NAME,
                                    **kwargs)

    def acl_set_ace_ethernet_ethertype(self, device_name, acl_id='', ace_index='', ace_ethertype='', **kwargs):
        """
        Description: Configures the EtherType value from the ethernet header for the ACE under the ACL.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ace_ethertype": ace_ethertype,
            "ace_index": ace_index,
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACE_ETHERNET_ETHERTYPE,
                                    **kwargs)

    def acl_clear_ace_ethernet_ethertype(self, device_name, acl_id='', ace_index='', **kwargs):
        """
        Description: Removes the EtherType value from the ethernet header for the ACE under the ACL.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "ace_index": ace_index,
            "acl_id": acl_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ACE_ETHERNET_ETHERTYPE,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def acl_verify_ipv4_standard_list_exists(self, device_name, acl_name='', acl_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_name]    - The ACL(s) that should exist on the device.
        [acl_id]      - The unique numeric identifier representing the ACL (VOSS Only).

        Verifies that an IPv4 standard ACL exists on a given device.
        """
        args = {"acl_name": acl_name,
                "acl_id": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_IPV4,
                                           self.parse_const.CHECK_IPV4_ACL_EXISTS, True,
                                           "IPv4 standard ACL {acl_name} exists on {device_name}.",
                                           "IPv4 standard ACL {acl_name} does NOT exist on {device_name}!",
                                           **kwargs)

    def acl_verify_ipv4_standard_list_does_not_exist(self, device_name, acl_name='', acl_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_name]    - The ACL(s) that should exist on the device.
        [acl_id]      - The unique numeric identifier representing the ACL (VOSS Only).

        Verifies that an IPv4 standard ACL does not exist on a given device.
        """
        args = {"acl_name": acl_name,
                "acl_id": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_IPV4,
                                           self.parse_const.CHECK_IPV4_ACL_EXISTS, False,
                                           "IPv4 standard ACL {acl_name} does not exist on {device_name}.",
                                           "IPv4 standard ACL {acl_name} DOES exist on {device_name}!",
                                           **kwargs)

    def acl_verify_ipv6_standard_list_exists(self, device_name, acl_name='', acl_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_name]    - The ACL(s) that should exist on the device.
        [acl_id]      - The unique numeric identifier representing the ACL (VOSS Only).

        Verifies that an IPv6 standard ACL exists on a given device.
        """
        args = {"acl_name": acl_name,
                "acl_id": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_IPV6,
                                           self.parse_const.CHECK_IPV6_ACL_EXISTS, True,
                                           "IPv6 standard ACL {acl_name} exists on {device_name}.",
                                           "IPv6 standard ACL {acl_name} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def acl_verify_ipv6_standard_list_does_not_exist(self, device_name, acl_name='', acl_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_name]    - The ACL(s) that should exist on the device.
        [acl_id]      - The unique numeric identifier representing the ACL (VOSS Only).

        Verifies that an IPv6 standard ACL does not exist on a given device.
        """
        args = {"acl_name": acl_name,
                "acl_id": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_IPV6,
                                           self.parse_const.CHECK_IPV6_ACL_EXISTS, False,
                                           "IPv6 standard ACL {acl_name} does not exist on {device_name}.",
                                           "IPv6 standard ACL {acl_name} DOES exist on {device_name}!",
                                           **kwargs)

    def acl_verify_enabled(self, device_name, acl_name='', acl_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_id]      - The unique numeric identifier representing the ACL(s) (VOSS Only).
        [acl_name]    - The ACL name(s) that should exist on the device.

        Verifies the ACL and ACEs in the ACL are enabled.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id,
                "acl_name": acl_name,
                "oid_index": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_ACL_ENABLE, True,
                                           "ACL id {acl_id} name {acl_name} is enabled on {device_name}.",
                                           "ACL id {acl_id} name {acl_name} is NOT enabled on {device_name}!",
                                           **kwargs)

    def acl_verify_disabled(self, device_name, acl_name='', acl_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_id]      - The unique numeric identifier representing the ACL(s) (VOSS Only).
        [acl_name]    - The ACL(s) name that should exist on the device.

        Verifies the ACL and ACEs in the ACL are disabled
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id,
                "acl_name": acl_name,
                "oid_index": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_ACL_ENABLE, False,
                                           "ACL id {acl_id} name {acl_name} is disabled on {device_name}.",
                                           "ACL id {acl_id} name {acl_name} is enabled on {device_name}!",
                                           **kwargs)

    def acl_verify_name(self, device_name, acl_name='', acl_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_id]      - The unique numeric identifier representing the ACL(s) (VOSS Only).
        [acl_name]    - The ACL name(s) that should exist on the device.

        Verifies the ACL name.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id,
                "acl_name": acl_name,
                "oid_index": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_ACL_NAME, True,
                                           "ACL id {acl_id} name is {acl_name}.",
                                           "ACL id {acl_id} name is NOT {acl_name}!",
                                           **kwargs)

    def acl_verify_default_action(self, device_name, acl_name='', acl_id='', action='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_id]      - The unique numeric identifier representing the ACL (VOSS Only).
        [acl_name]    - The ACL name of the acl_id.
        [action]      - The expected default action the ACL should take.
                        Values are either permit or deny.

        Verifies the  action to be taken when none of the Aces in the Acl match.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id,
                "acl_name": acl_name,
                "oid_index": acl_id,
                "action": action,
                "action_snmp": SnmpUtils().get_voss_acl_action(action)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_ACL_ACTION, True,
                                           "ACL id {acl_id} name {acl_name} default action is {action}.",
                                           "ACL id {acl_id} name {acl_name} default action is NOT {action}!",
                                           **kwargs)

    def acl_verify_port_exists(self, device_name, acl_id='', acl_name='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_name]    - The ACL(s) that should exist on the device.
        [acl_id]      - The unique numeric identifier representing the ACL(s) (VOSS Only).
        [ports]       - The port(s) to be checked on the acl.

        Verifies ports on the designated ACL exist.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id,
                "acl_name": acl_name,
                "port": ports,
                "port_index": SnmpUtils().get_port_index_from_name(device_name, ports),
                "oid_index": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_ACL_PORT, True,
                                           "Port {port} is assigned on ACL {acl_id} {acl_name}.",
                                           "Port {port} is NOT assigned on ACL {acl_id} {acl_name}!",
                                           **kwargs)

    def acl_verify_port_does_not_exist(self, device_name, acl_id='', acl_name='', ports='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_name]    - The ACL(s) that should not exist on the device.
        [acl_id]      - The unique numeric identifier representing the ACL(s) (VOSS Only).
        [ports]       - The port(s) to be checked on the acl.

        Verifies port is not assigned on the designated ACL.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id,
                "acl_name": acl_name,
                "port": ports,
                "port_index": SnmpUtils().get_port_index_from_name(device_name, ports),
                "oid_index": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_ACL_PORT, False,
                                           "Port {port} is not assigned on ACL {acl_id} {acl_name}.",
                                           "Port {port} is assigned on ACL {acl_id} {acl_name}!",
                                           **kwargs)

    def acl_verify_vlan_exists(self, device_name, acl_id='', acl_name='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_name]    - The ACL(s) that should exist on the device.
        [acl_id]      - The unique numeric identifier representing the ACL(s) (VOSS Only).
        [vlan]        - The vlan(s) to be checked on the acl.

        Verifies VLANs on the designated ACL exist.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id,
                "acl_name": acl_name,
                "vlan": vlan,
                "oid_index": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_ACL_VLAN, True,
                                           "VLAN {vlan} is assigned on ACL {acl_id} {acl_name}.",
                                           "VLAN {vlan} is NOT assigned on ACL {acl_id} {acl_name}!",
                                           **kwargs)

    def acl_verify_vlan_does_not_exist(self, device_name, acl_id='', acl_name='', vlan='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [acl_name]    - The ACL(s) that should not exist on the device.
        [acl_id]      - The unique numeric identifier representing the ACL(s) (VOSS Only).
        [vlan]        - The vlan(s) to be checked on the acl.

        Verifies vlan is not assigned on the designated ACL.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id,
                "acl_name": acl_name,
                "vlan": vlan,
                "oid_index": acl_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ID,
                                           self.parse_const.CHECK_ACL_VLAN, False,
                                           "VLAN {vlan} is not assigned on ACL {acl_id} {acl_name}.",
                                           "VLAN {vlan} is assigned on ACL {acl_id} {acl_name}!",
                                           **kwargs)

    def acl_verify_ace_exists(self, device_name, ace_name='', acl_id='', ace_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ace_name]    - The name of the ACE entry under the ACL.
        [acl_id]      - The numeric identifier of the ACL e.g. 1,2,3,...
        [ace_index]   - The numeric index representing the Access Control Entry.

        Verifies an access control entry (ACE) exists under a designated ACL.
        This keyword only applies to VOSS.
        """
        args = {"ace_name": ace_name,
                "acl_id": acl_id,
                "ace_index": ace_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_ACES,
                                           self.parse_const.CHECK_ACE_EXISTS, True,
                                           "ACE {ace_index} name {ace_name} exists under ACL {acl_id}",
                                           "ACE {ace_index} name {ace_name} does NOT exist under ACL {acl_id}!",
                                           **kwargs)

    def acl_verify_ace_does_not_exist(self, device_name, ace_name='', acl_id='', ace_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ace_name]    - The name of the ACE entry under the ACL.
        [acl_id]      - The numeric identifier of the ACL e.g. 1,2,3,...
        [ace_index]   - The numeric index representing the Access Control Entry.

        Verifies an access control entry (ACE) does not exist under a designated ACL.
        This keyword only applies to VOSS.
        """
        args = {"ace_name": ace_name,
                "acl_id": acl_id,
                "ace_index": ace_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_ACES,
                                           self.parse_const.CHECK_ACE_EXISTS, False,
                                           "ACE {ace_index} name {ace_name} does not exist under ACL {acl_id}.",
                                           "ACE {ace_index} name {ace_name} exists under ACL {acl_id}!",
                                           **kwargs)

    def acl_verify_ace_oper_up(self, device_name, ace_name='', acl_id='', ace_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ace_name]    - The name of the ACE entry under the ACL.
        [acl_id]      - The numeric identifier of the ACL e.g. 1,2,3,...
        [ace_index]   - The numeric index representing the Access Control Entry.
                        The lower the number, the higher the priority.

        Verifies an access control entry (ACE) is operational under a designated ACL.
        This keyword only applies to VOSS.
        """
        args = {"ace_name": ace_name,
                "acl_id": acl_id,
                "ace_index": ace_index,
                "oid_index": acl_id + "." + ace_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACE_INDEX_OPER_STATE,
                                           self.parse_const.CHECK_ACE_INDEX_OPER_STATE, True,
                                           "ACE {ace_index} name {ace_name} under ACL{acl_id} is up.",
                                           "ACE {ace_index} name {ace_name} under ACL {acl_id} is DOWN!",
                                           **kwargs)

    def acl_verify_ace_oper_down(self, device_name, ace_name='', acl_id='', ace_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ace_name]    - The name of the ACE entry under the ACL.
        [acl_id]      - The numeric identifier of the ACL e.g. 1,2,3,...
        [ace_index]   - The numeric index representing the Access Control Entry.
                        The lower the number, the higher the priority.

        Verifies an access control entry (ACE) is not operational under a designated ACL.
        This keyword only applies to VOSS.
        """
        args = {"ace_name": ace_name,
                "acl_id": acl_id,
                "ace_index": ace_index,
                "oid_index": acl_id + "." + ace_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACE_INDEX_OPER_STATE,
                                           self.parse_const.CHECK_ACE_INDEX_OPER_STATE, False,
                                           "ACE {ace_index} name {ace_name} under ACL{acl_id} is down.",
                                           "ACE {ace_index} name {ace_name} under ACL {acl_id} is UP!",
                                           **kwargs)

    def acl_verify_ace_name(self, device_name, acl_id='', ace_index='', ace_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ace_name]    - The name of the ACE entry under the ACL.
        [acl_id]      - The numeric identifier of the ACL e.g. 1,2,3,...
        [ace_index]   - The numeric index representing the Access Control Entry.
                        The lower the number, the higher the priority.

        Verifies an access control entry (ACE) name is configured as expected.
        This keyword only applies to VOSS.
        """
        args = {"acl_id": acl_id,
                "ace_index": ace_index,
                "oid_index": acl_id + "." + ace_index,
                "ace_name": ace_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACE_INDEX_NAME,
                                           self.parse_const.CHECK_ACE_INDEX_NAME, True,
                                           "ACE {ace_index} under ACL {acl_id} is named {ace_name}.",
                                           "ACE {ace_index} under ACL {acl_id} is NOT named {ace_name}!",
                                           **kwargs)

    def acl_verify_ace_action(self, device_name, ace_name='', acl_id='', ace_index='', ace_action='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [ace_name]    - The name of the ACE entry under the ACL.
        [acl_id]      - The numeric identifier of the ACL e.g. 1,2,3,...
        [ace_index]   - The numeric index representing the Access Control Entry.
                        The lower the number, the higher the priority.
        [ace_action]  - The action the ACE should take.
                        Values are either permit or deny.

        Verifies the operational mode associated with the Ace that takes effect on matching packets.
        This keyword only applies to VOSS.
        """
        args = {"ace_name": ace_name,
                "acl_id": acl_id,
                "ace_index": ace_index,
                "oid_index": acl_id + "." + ace_index,
                "ace_action": ace_action,
                "ace_action_snmp": SnmpUtils().get_voss_acl_action(ace_action)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACE_INDEX_ACTION,
                                           self.parse_const.CHECK_ACE_INDEX_ACTION, True,
                                           "ACE {ace_index} under ACL {acl_id} action is {ace_action}.",
                                           "ACE {ace_index} under ACL {acl_id} action is NOT {ace_action}!",
                                           **kwargs)

    def acl_verify_ace_ethernet_ethertype_exists(self, device_name, ace_name='', acl_id='', ace_index='',
                                                 ace_ethertype='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ace_name]       - The name of the ACE entry under the ACL.
        [acl_id]         - The numeric identifier of the ACL e.g. 1,2,3,...
        [ace_index]      - The numeric index representing the Access Control Entry.
                           The lower the number, the higher the priority.
        [ace_ethertype]  - The EtherType value from ethernet header.
                           Values are:  Ethertype name {0x0-0xffff} or {ip | arp| ipx802dot3 | ipx802dot2 | ipxSnap |
                           ipxEthernet2 | appleTalk | AppleTalk-ARP | sna802dot2 | snaEthernet2 | netBios | xns
                           | vines | ipv6 | rarp | PPPoE-discovery | PPPoE-session.

        Verifies the EtherType value from the ethernet header for the ACE under the ACL exists.
        This keyword only applies to VOSS.
        """
        args = {"ace_name": ace_name,
                "acl_id": acl_id,
                "ace_index": ace_index,
                "oid_index": acl_id + "." + ace_index,
                "ace_ethertype": ace_ethertype}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACE_INDEX_ETHERNET_ETHERTYPE,
                                           self.parse_const.CHECK_ACE_INDEX_ETHERNET_ETHERTYPE, True,
                                           "ACE {ace_index} under ACL {acl_id} ethertype {ace_ethertype} exists.",
                                           "ACE {ace_index} under ACL {acl_id} ethertype {ace_ethertype}"
                                           " does not NOT exist!",
                                           **kwargs)

    def acl_verify_ace_ethernet_ethertype_does_not_exist(self, device_name, ace_name='', acl_id='', ace_index='',
                                                         ace_ethertype='', **kwargs):
        """
        Keyword Arguments:
        [device_name]    - The device the keyword should be run against.
        [ace_name]       - The name of the ACE entry under the ACL.
        [acl_id]         - The numeric identifier of the ACL e.g. 1,2,3,...
        [ace_index]      - The numeric index representing the Access Control Entry.
                           The lower the number, the higher the priority.
        [ace_ethertype]  - The EtherType value from ethernet header.
                           Values are:  Ethertype name {0x0-0xffff} or {ip | arp| ipx802dot3 | ipx802dot2 | ipxSnap |
                           ipxEthernet2 | appleTalk | AppleTalk-ARP | sna802dot2 | snaEthernet2 | netBios | xns
                           | vines | ipv6 | rarp | PPPoE-discovery | PPPoE-session.

        Verifies the EtherType value from the ethernet header for the ACE under the ACL does not exist.
        This keyword only applies to VOSS.
        """
        args = {"ace_name": ace_name,
                "acl_id": acl_id,
                "ace_index": ace_index,
                "oid_index": acl_id + "." + ace_index,
                "ace_ethertype": ace_ethertype}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACE_INDEX_ETHERNET_ETHERTYPE,
                                           self.parse_const.CHECK_ACE_INDEX_ETHERNET_ETHERTYPE, False,
                                           "ACE {ace_index} under ACL {acl_id} ethertype {ace_ethertype}"
                                           " does not exist.",
                                           "ACE {ace_index} under ACL {acl_id} ethertype {ace_ethertype}"
                                           " exists!",
                                           **kwargs)
