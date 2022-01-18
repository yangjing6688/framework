"""
Keyword class for all policy cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.PolicyConstants import \
    PolicyConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.PolicyConstants import \
    PolicyConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ast import literal_eval
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class NetworkElementPolicyGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementPolicyGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "policy"

    def policy_set_invalid(self, device_name, action='', **kwargs):
        """
        Description: Configures the invalid action for the policy..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "action": action
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_INVALID,
                                    **kwargs)

    def policy_clear_invalid(self, device_name, **kwargs):
        """
        Description: Removes the invalid action for the policy..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_INVALID,
                                    **kwargs)

    def policy_set_port_admin_profile(self, device_name, port='', admin_id='', **kwargs):
        """
        Description: Creates a policy port admin profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "admin_id": admin_id,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_ADMIN_PROFILE,
                                    **kwargs)

    def policy_clear_port_admin_profile(self, device_name, port='', **kwargs):
        """
        Description: Deletes a policy port admin profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PORT_ADMIN_PROFILE,
                                    **kwargs)

    def policy_set_mac_source_admin_profile(self, device_name, mac_source='', port='', profile_id='', mask='',
                                            **kwargs):
        """
        Description: Creates a policy admin rule to apply to traffic with a specific mac source..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mac_source": mac_source,
            "mask": mask,
            "port": port,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAC_SOURCE_ADMIN_PROFILE,
                                    **kwargs)

    def policy_clear_mac_source_admin_profile(self, device_name, mac_source='', port='', mask='', **kwargs):
        """
        Description: Deletes a policy admin rule to apply to traffic with a specific mac source..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mac_source": mac_source,
            "mask": mask,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MAC_SOURCE_ADMIN_PROFILE,
                                    **kwargs)

    def policy_set_profile(self, device_name, profile_id='', **kwargs):
        """
        Description: Creates a policy profile with the given ID..

        Supported Agents and OS:
            CLI: EXOS, EOS, EXTRWIRELESS
        """
        args = {
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE,
                                    **kwargs)

    def policy_set_profile_with_name(self, device_name, profile_id='', name='', **kwargs):
        """
        Description: Creates a policy profile with the given ID and name..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "name": name,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_WITH_NAME,
                                    **kwargs)

    def policy_clear_profile(self, device_name, profile_id='', **kwargs):
        """
        Description: Deletes a policy profile with the given ID and name (if provided)..

        Supported Agents and OS:
            CLI: EXOS, EOS, EXTRWIRELESS
        """
        args = {
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PROFILE,
                                    **kwargs)

    def policy_set_profile_name(self, device_name, profile_id='', name='', **kwargs):
        """
        Description: Configures the supplied profile with the supplied profile name..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "name": name,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_NAME,
                                    **kwargs)

    def policy_set_profile_pvid_status(self, device_name, profile_id='', status='', **kwargs):
        """
        Description: Enables a given policy profile for pvid override..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "profile_id": profile_id,
            "status": status
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_PVID_STATUS,
                                    **kwargs)

    def policy_set_profile_pvid(self, device_name, profile_id='', pvid='', **kwargs):
        """
        Description: Configures the PVID value of a given policy rule..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "profile_id": profile_id,
            "pvid": pvid
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_PVID,
                                    **kwargs)

    def policy_set_profile_cos_status(self, device_name, profile_id='', status='', **kwargs):
        """
        Description: Enables COS status on a given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "profile_id": profile_id,
            "status": status
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_COS_STATUS,
                                    **kwargs)

    def policy_set_profile_cos(self, device_name, profile_id='', cos_value='', cos_name='', **kwargs):
        """
        Description: Configures a COS value to a given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS, EXTRWIRELESS
        """
        args = {
            "cos_name": cos_name,
            "cos_value": cos_value,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_COS,
                                    **kwargs)

    def policy_set_profile_egress_vlan(self, device_name, profile_id='', vlan='', append='', **kwargs):
        """
        Description: Adds a vlan or list of vlans to a policy profile's egress vlan list..

        Supported Agents and OS:
            CLI: EXOS, EOS, EXTRWIRELESS
        """
        args = {
            "append": append,
            "profile_id": profile_id,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_EGRESS_VLAN,
                                    **kwargs)

    def policy_set_profile_untagged_vlan(self, device_name, profile_id='', vlan='', append='', **kwargs):
        """
        Description: Adds a vlan or list of vlans to a policy profile's untagged vlan list..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "append": append,
            "profile_id": profile_id,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_UNTAGGED_VLAN,
                                    **kwargs)

    def policy_set_profile_forbidden_vlan(self, device_name, profile_id='', vlan='', append='', **kwargs):
        """
        Description: Adds a vlan or list of vlans to policy profile's forbidden vlan list..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "append": append,
            "profile_id": profile_id,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_FORBIDDEN_VLAN,
                                    **kwargs)

    def policy_set_profile_tci_overwrite(self, device_name, profile_id='', status='', **kwargs):
        """
        Description: Enables TCI overwrite on a given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "profile_id": profile_id,
            "status": status
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_TCI_OVERWRITE,
                                    **kwargs)

    def policy_set_profile_pvid_pvid_status(self, device_name, profile_id='', pvid='', pvid_status='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "profile_id": profile_id,
            "pvid": pvid,
            "pvid_status": pvid_status
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_PVID_PVID_STATUS,
                                    **kwargs)

    def policy_set_profile_untagged_pvid(self, device_name, profile_id='', name='', pvid='', vlan='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "name": name,
            "profile_id": profile_id,
            "pvid": pvid,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_UNTAGGED_PVID,
                                    **kwargs)

    def policy_set_rule(self, device_name, profile_id='', options='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "options": options,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE,
                                    **kwargs)

    def policy_clear_profile_rules(self, device_name, profile_id='', options='', **kwargs):
        """
        Description: Removes the given policy rules from a device..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "options": options,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PROFILE_RULES,
                                    **kwargs)

    def policy_set_rule_ether(self, device_name, profile_id='', ether_type='', mask='', port_string='',
                              storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                              mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                              **kwargs):
        """
        Description: Creates an ether type policy rule for the given policy profile. Available keys for the options
                     dictionary: {mask, port_string, storage_type, vlan, forward, drop, cos, tci_overwrite,
                     mirror_destination, syslog, trap, disable_port, quarantine_profile}.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "ether_type": ether_type,
            "forward": forward,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_ETHER,
                                    **kwargs)

    def policy_clear_rule_ether(self, device_name, profile_id='', ether_type='', mask='', port_string='', **kwargs):
        """
        Description: Deletes an ether type policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ether_type": ether_type,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_ETHER,
                                    **kwargs)

    def policy_set_rule_ip6dest(self, device_name, profile_id='', ipv6_addr='', l4_port='', mask='', port_string='',
                                storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                **kwargs):
        """
        Description: Creates an ip6 dest policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ipv6_addr": ipv6_addr,
            "l4_port": l4_port,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IP6DEST,
                                    **kwargs)

    def policy_clear_rule_ip6dest(self, device_name, profile_id='', ipv6_addr='', l4_port='', mask='', port_string='',
                                  **kwargs):
        """
        Description: Delete an ip6 dest policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ipv6_addr": ipv6_addr,
            "l4_port": l4_port,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IP6DEST,
                                    **kwargs)

    def policy_set_rule_ipdestsocket(self, device_name, profile_id='', ip_addr='', l4_port='', mask='', port_string='',
                                     storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                     mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                     **kwargs):
        """
        Description: Creates an ip destination socket policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ip_addr": ip_addr,
            "l4_port": l4_port,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPDESTSOCKET,
                                    **kwargs)

    def policy_clear_rule_ipdestsocket(self, device_name, profile_id='', ip_addr='', l4_port='', mask='',
                                       port_string='', **kwargs):
        """
        Description: Deletes an ip destination socket policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_addr": ip_addr,
            "l4_port": l4_port,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPDESTSOCKET,
                                    **kwargs)

    def policy_set_rule_ipfrag(self, device_name, profile_id='', mask='', port_string='', storage_type='', vlan='',
                               forward='', drop='', cos='', tci_overwrite='', mirror_destination='', syslog='',
                               trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Description: Creates an IP fragment policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPFRAG,
                                    **kwargs)

    def policy_clear_rule_ipfrag(self, device_name, profile_id='', mask='', port_string='', **kwargs):
        """
        Description: Deletes an IP fragment policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPFRAG,
                                    **kwargs)

    def policy_set_rule_ipproto(self, device_name, profile_id='', ipproto='', mask='', port_string='', storage_type='',
                                vlan='', forward='', drop='', cos='', tci_overwrite='', mirror_destination='',
                                syslog='', trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Description: Creates an IP protocol policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ipproto": ipproto,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPPROTO,
                                    **kwargs)

    def policy_clear_rule_ipproto(self, device_name, profile_id='', ip_proto='', mask='', port_string='', **kwargs):
        """
        Description: Deletes an IP protocol policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_proto": ip_proto,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPPROTO,
                                    **kwargs)

    def policy_set_rule_ipsourcesocket(self, device_name, profile_id='', ip_addr='', l4_port='', mask='',
                                       port_string='', storage_type='', vlan='', forward='', drop='', cos='',
                                       tci_overwrite='', mirror_destination='', syslog='', trap='', disable_port='',
                                       quarantine_profile='', **kwargs):
        """
        Description: Creates an IP source socket policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ip_addr": ip_addr,
            "l4_port": l4_port,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPSOURCESOCKET,
                                    **kwargs)

    def policy_clear_rule_ipsourcesocket(self, device_name, profile_id='', ip_addr='', l4_port='', mask='',
                                         port_string='', **kwargs):
        """
        Description: Deletes an IP source socket policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_addr": ip_addr,
            "l4_port": l4_port,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPSOURCESOCKET,
                                    **kwargs)

    def policy_set_rule_iptos(self, device_name, profile_id='', ip_tos='', mask='', port_string='', storage_type='',
                              vlan='', forward='', drop='', cos='', tci_overwrite='', mirror_destination='', syslog='',
                              trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Description: Creates an IP TOS policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ip_tos": ip_tos,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPTOS,
                                    **kwargs)

    def policy_clear_rule_iptos(self, device_name, profile_id='', ip_tos='', mask='', port_string='', **kwargs):
        """
        Description: Deletes an IP TOS policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_tos": ip_tos,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPTOS,
                                    **kwargs)

    def policy_set_rule_ipttl(self, device_name, profile_id='', ip_ttl='', mask='', port_string='', storage_type='',
                              vlan='', forward='', drop='', cos='', tci_overwrite='', mirror_destination='', syslog='',
                              trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Description: Creates an IP TTL policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ip_ttl": ip_ttl,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPTTL,
                                    **kwargs)

    def policy_clear_rule_ipttl(self, device_name, profile_id='', ip_ttl='', mask='', port_string='', **kwargs):
        """
        Description: Deletes an IP TTL policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_ttl": ip_ttl,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPTTL,
                                    **kwargs)

    def policy_set_rule_macdest(self, device_name, profile_id='', mac_addr='', mask='', port_string='',
                                storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                **kwargs):
        """
        Description: Creates a MAC destination policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "mac_addr": mac_addr,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_MACDEST,
                                    **kwargs)

    def policy_clear_rule_macdest(self, device_name, profile_id='', mac_addr='', mask='', port_string='', **kwargs):
        """
        Description: Deletes a MAC destination policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mac_addr": mac_addr,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_MACDEST,
                                    **kwargs)

    def policy_set_rule_macsource(self, device_name, profile_id='', mac_addr='', mask='', port_string='',
                                  storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                  mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                  **kwargs):
        """
        Description: Creates a MAC source policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "mac_addr": mac_addr,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_MACSOURCE,
                                    **kwargs)

    def policy_clear_rule_macsource(self, device_name, profile_id='', mac_addr='', mask='', port_string='', **kwargs):
        """
        Description: Deletes a MAC source policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mac_addr": mac_addr,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_MACSOURCE,
                                    **kwargs)

    def policy_set_rule_port(self, device_name, profile_id='', port='', mask='', port_string='', storage_type='',
                             vlan='', forward='', drop='', cos='', tci_overwrite='', mirror_destination='', syslog='',
                             trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Description: Creates a port policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port": port,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_PORT,
                                    **kwargs)

    def policy_clear_rule_port(self, device_name, profile_id='', port='', mask='', port_string='', **kwargs):
        """
        Description: Deletes a port policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "mask": mask,
            "port": port,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_PORT,
                                    **kwargs)

    def policy_set_rule_tcpdestportip(self, device_name, profile_id='', tcp_port='', ip_addr='', mask='',
                                      port_string='', storage_type='', vlan='', forward='', drop='', cos='',
                                      tci_overwrite='', mirror_destination='', syslog='', trap='', disable_port='',
                                      quarantine_profile='', **kwargs):
        """
        Description: Creates a TCP destination port IP rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ip_addr": ip_addr,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "tcp_port": tcp_port,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_TCPDESTPORTIP,
                                    **kwargs)

    def policy_clear_rule_tcpdestportip(self, device_name, profile_id='', tcp_port='', ip_addr='', mask='',
                                        port_string='', **kwargs):
        """
        Description: Deletes a TCP destination port IP rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_addr": ip_addr,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id,
            "tcp_port": tcp_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_TCPDESTPORTIP,
                                    **kwargs)

    def policy_set_rule_tcpsourceportip(self, device_name, profile_id='', tcp_port='', ip_addr='', mask='',
                                        port_string='', storage_type='', vlan='', forward='', drop='', cos='',
                                        tci_overwrite='', mirror_destination='', syslog='', trap='', disable_port='',
                                        quarantine_profile='', **kwargs):
        """
        Description: Creates a TCP source port IP rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ip_addr": ip_addr,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "tcp_port": tcp_port,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_TCPSOURCEPORTIP,
                                    **kwargs)

    def policy_clear_rule_tcpsourceportip(self, device_name, profile_id='', tcp_port='', ip_addr='', mask='',
                                          port_string='', **kwargs):
        """
        Description: Deletes a TCP source port IP rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_addr": ip_addr,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id,
            "tcp_port": tcp_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_TCPSOURCEPORTIP,
                                    **kwargs)

    def policy_set_rule_udpdestportip(self, device_name, profile_id='', udp_port='', ip_addr='', mask='',
                                      port_string='', storage_type='', vlan='', forward='', drop='', cos='',
                                      tci_overwrite='', mirror_destination='', syslog='', trap='', disable_port='',
                                      quarantine_profile='', **kwargs):
        """
        Description: Creates a UDP destination port IP rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ip_addr": ip_addr,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "udp_port": udp_port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_UDPDESTPORTIP,
                                    **kwargs)

    def policy_clear_rule_udpdestportip(self, device_name, profile_id='', udp_port='', ip_addr='', mask='',
                                        port_string='', **kwargs):
        """
        Description: Deletes a UDP destination port IP rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_addr": ip_addr,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id,
            "udp_port": udp_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_UDPDESTPORTIP,
                                    **kwargs)

    def policy_set_rule_udpsourceportip(self, device_name, profile_id='', udp_port='', ip_addr='', mask='',
                                        port_string='', storage_type='', vlan='', forward='', drop='', cos='',
                                        tci_overwrite='', mirror_destination='', syslog='', trap='', disable_port='',
                                        quarantine_profile='', **kwargs):
        """
        Description: Creates a UDP source port IP rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ip_addr": ip_addr,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "udp_port": udp_port,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_UDPSOURCEPORTIP,
                                    **kwargs)

    def policy_clear_rule_udpsourceportip(self, device_name, profile_id='', udp_port='', ip_addr='', mask='',
                                          port_string='', **kwargs):
        """
        Description: Deletes a UDP source port IP rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "ip_addr": ip_addr,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id,
            "udp_port": udp_port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_UDPSOURCEPORTIP,
                                    **kwargs)

    def policy_set_maptable_response(self, device_name, _type='', **kwargs):
        """
        Description: Configures the maptable RADIUS response for the policy..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "type": _type
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_MAPTABLE_RESPONSE,
                                    **kwargs)

    def policy_clear_maptable_response(self, device_name, **kwargs):
        """
        Description: Deletes the maptable RADIUS response for the policy..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_MAPTABLE_RESPONSE,
                                    **kwargs)

    def policy_enable(self, device_name, **kwargs):
        """
        Description: Enables policy on the given device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE,
                                    **kwargs)

    def policy_disable(self, device_name, **kwargs):
        """
        Description: Disables policy on the given device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE,
                                    **kwargs)

    def policy_set_vlanauthorization_state(self, device_name, state='', **kwargs):
        """
        Description: Configures the global policy vlan authorization state to be either enabled or disabled(default)..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_VLANAUTHORIZATION_STATE,
                                    **kwargs)

    def policy_set_rule_model_access_list(self, device_name, **kwargs):
        """
        Description: Configures the policy rule model to access-list..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_MODEL_ACCESS_LIST,
                                    **kwargs)

    def policy_set_rule_model_hierarchical(self, device_name, **kwargs):
        """
        Description: Configures the policy rule model to hierarchical..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_MODEL_HIERARCHICAL,
                                    **kwargs)

    def policy_set_access_list_profile_index(self, device_name, profile_index='', list_name='', **kwargs):
        """
        Description: Configures the profile index of the given access list..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "list_name": list_name,
            "profile_index": profile_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST_PROFILE_INDEX,
                                    **kwargs)

    def policy_set_access_list_profile_none(self, device_name, profile_index='', **kwargs):
        """
        Description: Configures profile state 'none' on given access list..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "profile_index": profile_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST_PROFILE_NONE,
                                    **kwargs)

    def policy_set_access_list_profile_highest(self, device_name, list_name='', rule='', **kwargs):
        """
        Description: Configures profile state 'highest-priority' on given access list..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "list_name": list_name,
            "rule": rule
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST_PROFILE_HIGHEST,
                                    **kwargs)

    def policy_set_access_list_profile_lowest(self, device_name, list_name='', rule='', **kwargs):
        """
        Description: Configures profile state 'lowest-priority' on given access list..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "list_name": list_name,
            "rule": rule
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST_PROFILE_LOWEST,
                                    **kwargs)

    def policy_set_access_list_rule_precedence_first(self, device_name, list_name='', rule='', **kwargs):
        """
        Description: Configures rule precedence 'first' on given access list..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "list_name": list_name,
            "rule": rule
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST_RULE_PRECEDENCE_FIRST,
                                    **kwargs)

    def policy_set_access_list_rule_precedence_last(self, device_name, list_name='', rule='', **kwargs):
        """
        Description: Configures rule precedence 'last' on given access list..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "list_name": list_name,
            "rule": rule
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST_RULE_PRECEDENCE_LAST,
                                    **kwargs)

    def policy_set_access_list_rule_precedence_before(self, device_name, list1='', rule1='', list2='', rule2='',
                                                      **kwargs):
        """
        Description: Configures rule precedence 'before' on given access list.  Format is: 'list1, rule1 before list2,
                     rule2'.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "list1": list1,
            "list2": list2,
            "rule1": rule1,
            "rule2": rule2
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST_RULE_PRECEDENCE_BEFORE,
                                    **kwargs)

    def policy_set_access_list_rule_precedence_after(self, device_name, list1='', rule1='', list2='', rule2='',
                                                     **kwargs):
        """
        Description: Configures rule precedence 'after' on given access list.  Format is: 'list1, rule1 before list2,
                     rule2'.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "list1": list1,
            "list2": list2,
            "rule1": rule1,
            "rule2": rule2
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST_RULE_PRECEDENCE_AFTER,
                                    **kwargs)

    def policy_set_access_list(self, device_name, list_name='', rule='', match_string='', action_string='', **kwargs):
        """
        Description: Creates a policy access-list named {list_name}.{rule} with up to 5 match conditions, listed in
                     {match_string}. All match conditions must be listed along with their corresponding arguments.
                     Followed by action_string..

        Supported Agents and OS:
            CLI: EXOS
            REST: EXOS
        """
        args = {
            "action_string": action_string,
            "list_name": list_name,
            "match_string": match_string,
            "rule": rule
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST,
                                    **kwargs)

    def policy_set_access_list_action_set(self, device_name, set_id='', action_string='', **kwargs):
        """
        Description: Creates a policy access-list action-set with set-id {set_id} and provided actions. All match
                     conditions must be listed along with their corresponding arguments..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "action_string": action_string,
            "set_id": set_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ACCESS_LIST_ACTION_SET,
                                    **kwargs)

    def policy_clear_all_rules(self, device_name, **kwargs):
        """
        Description: Removes all policy rules from the given device..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_RULES,
                                    **kwargs)

    def policy_clear_access_list_all(self, device_name, **kwargs):
        """
        Description: Deletes all policy access-lists and their associated rules..

        Supported Agents and OS:
            CLI: EXOS
            REST: EXOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ACCESS_LIST_ALL,
                                    **kwargs)

    def policy_clear_access_list(self, device_name, list_name='', **kwargs):
        """
        Description: Deletes the provided policy access-list..

        Supported Agents and OS:
            CLI: EXOS
            REST: EXOS
        """
        args = {
            "list_name": list_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ACCESS_LIST,
                                    **kwargs)

    def policy_clear_access_list_rule(self, device_name, list_name='', rule='', **kwargs):
        """
        Description: Deletes the provided policy access-list rule..

        Supported Agents and OS:
            CLI: EXOS
            REST: EXOS
        """
        args = {
            "list_name": list_name,
            "rule": rule
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ACCESS_LIST_RULE,
                                    **kwargs)

    def policy_clear_access_list_action_set(self, device_name, set_id='', **kwargs):
        """
        Description: Deletes the provided policy access-list action-set..

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "set_id": set_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ACCESS_LIST_ACTION_SET,
                                    **kwargs)

    def policy_set_profile_precedence(self, device_name, profile_id='', precedence='', **kwargs):
        """
        Description: Configures the rule precedence for a give policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "precedence": precedence,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_PRECEDENCE,
                                    **kwargs)

    def policy_set_profile_mirror_dest(self, device_name, profile_id='', index='', **kwargs):
        """
        Description: Configures a policy profile's mirror destination index..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "index": index,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_MIRROR_DEST,
                                    **kwargs)

    def policy_set_profile_syslog(self, device_name, profile_id='', state='', **kwargs):
        """
        Description: Enables syslog on the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "profile_id": profile_id,
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_SYSLOG,
                                    **kwargs)

    def policy_set_profile_trap(self, device_name, profile_id='', state='', **kwargs):
        """
        Description: Enables traps on the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "profile_id": profile_id,
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_TRAP,
                                    **kwargs)

    def policy_set_profile_disable_port(self, device_name, profile_id='', state='', **kwargs):
        """
        Description: Disables disable port on the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "profile_id": profile_id,
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_DISABLE_PORT,
                                    **kwargs)

    def policy_set_profile_fst(self, device_name, profile_id='', index='', **kwargs):
        """
        Description: Configures the FST index of the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "index": index,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_FST,
                                    **kwargs)

    def policy_set_profile_web_redirect(self, device_name, profile_id='', index='', **kwargs):
        """
        Description: Configures the web redirect index of the givne policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "index": index,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_WEB_REDIRECT,
                                    **kwargs)

    def policy_set_rule_application(self, device_name, profile_id='', application='', application_type='', mask='',
                                    port_string='', storage_type='', vlan='', forward='', drop='', cos='',
                                    tci_overwrite='', mirror_destination='', syslog='', trap='', disable_port='',
                                    quarantine_profile='', **kwargs):
        """
        Description: Creates an application policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "application": application,
            "application_type": application_type,
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_APPLICATION,
                                    **kwargs)

    def policy_clear_rule_application(self, device_name, profile_id='', application='', application_type='', mask='',
                                      port_string='', **kwargs):
        """
        Description: Delete an application policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "application": application,
            "application_type": application_type,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_APPLICATION,
                                    **kwargs)

    def policy_set_rule_icmp6type(self, device_name, profile_id='', icmp6type='', icmp6code='', mask='',
                                  port_string='', storage_type='', vlan='', forward='', drop='', cos='',
                                  tci_overwrite='', mirror_destination='', syslog='', trap='', disable_port='',
                                  quarantine_profile='', **kwargs):
        """
        Description: Creates an icmp6 type policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "icmp6code": icmp6code,
            "icmp6type": icmp6type,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_ICMP6TYPE,
                                    **kwargs)

    def policy_clear_rule_icmp6type(self, device_name, profile_id='', icmp6_type='', icmp6_code='', mask='',
                                    port_string='', **kwargs):
        """
        Description: Deletes an icmp6 type policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "icmp6_code": icmp6_code,
            "icmp6_type": icmp6_type,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_ICMP6TYPE,
                                    **kwargs)

    def policy_set_rule_icmptype(self, device_name, profile_id='', icmptype='', icmpcode='', mask='', port_string='',
                                 storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                 mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                 **kwargs):
        """
        Description: Creates an icmp type policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "icmpcode": icmpcode,
            "icmptype": icmptype,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_ICMPTYPE,
                                    **kwargs)

    def policy_clear_rule_icmptype(self, device_name, profile_id='', icmp_type='', icmp_code='', mask='',
                                   port_string='', **kwargs):
        """
        Description: Deletes an icmp type policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "icmp_code": icmp_code,
            "icmp_type": icmp_type,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_ICMPTYPE,
                                    **kwargs)

    def policy_set_rule_ip6flowlabel(self, device_name, profile_id='', ip6_flow_label='', mask='', port_string='',
                                     storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                     mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                     **kwargs):
        """
        Description: Creates an ip6 flow label policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ip6_flow_label": ip6_flow_label,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IP6FLOWLABEL,
                                    **kwargs)

    def policy_clear_rule_ip6flowlabel(self, device_name, profile_id='', ip6_flow_label='', mask='', port_string='',
                                       **kwargs):
        """
        Description: Deletes an ip6 flow label policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "ip6_flow_label": ip6_flow_label,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IP6FLOWLABEL,
                                    **kwargs)

    def policy_set_rule_ip6source(self, device_name, profile_id='', ipv6_addr='', l4_port='', mask='', port_string='',
                                  storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                  mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                  **kwargs):
        """
        Description: Creates an ip6 source policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ipv6_addr": ipv6_addr,
            "l4_port": l4_port,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IP6SOURCE,
                                    **kwargs)

    def policy_clear_rule_ip6source(self, device_name, profile_id='', ipv6_addr='', l4_port='', mask='',
                                    port_string='', **kwargs):
        """
        Description: Deletes an ip6 source policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "ipv6_addr": ipv6_addr,
            "l4_port": l4_port,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IP6SOURCE,
                                    **kwargs)

    def policy_set_rule_ipxclass(self, device_name, profile_id='', ipx_class='', mask='', port_string='',
                                 storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                 mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                 **kwargs):
        """
        Description: Creates an IPX class policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ipx_class": ipx_class,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPXCLASS,
                                    **kwargs)

    def policy_clear_rule_ipxclass(self, device_name, profile_id='', ipx_class='', mask='', port_string='', **kwargs):
        """
        Description: Deletes an IPX class policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "ipx_class": ipx_class,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPXCLASS,
                                    **kwargs)

    def policy_set_rule_ipxdest(self, device_name, profile_id='', ipx_addr='', mask='', port_string='',
                                storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                **kwargs):
        """
        Description: Creates an IPX destination policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ipx_addr": ipx_addr,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPXDEST,
                                    **kwargs)

    def policy_clear_rule_ipxdest(self, device_name, profile_id='', ipx_addr='', mask='', port_string='', **kwargs):
        """
        Description: Deletes an IPX destination policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "ipx_addr": ipx_addr,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPXDEST,
                                    **kwargs)

    def policy_set_rule_ipxdestsocket(self, device_name, profile_id='', ipx_socket='', mask='', port_string='',
                                      storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                      mirror_destination='', syslog='', trap='', disable_port='',
                                      quarantine_profile='', **kwargs):
        """
        Description: Creates an IPX destination socket policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ipx_socket": ipx_socket,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPXDESTSOCKET,
                                    **kwargs)

    def policy_clear_rule_ipxdestsocket(self, device_name, profile_id='', ipx_socket='', mask='', port_string='',
                                        **kwargs):
        """
        Description: Deletes an IPX destination socket policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "ipx_socket": ipx_socket,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPXDESTSOCKET,
                                    **kwargs)

    def policy_set_rule_ipxsource(self, device_name, profile_id='', ipx_addr='', mask='', port_string='',
                                  storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                  mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                  **kwargs):
        """
        Description: Creates an IPX source policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ipx_addr": ipx_addr,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPXSOURCE,
                                    **kwargs)

    def policy_clear_rule_ipxsource(self, device_name, profile_id='', ipx_addr='', mask='', port_string='', **kwargs):
        """
        Description: Deletes an IPX source policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "ipx_addr": ipx_addr,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPXSOURCE,
                                    **kwargs)

    def policy_set_rule_ipxsourcesocket(self, device_name, profile_id='', ipx_socket='', mask='', port_string='',
                                        storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                        mirror_destination='', syslog='', trap='', disable_port='',
                                        quarantine_profile='', **kwargs):
        """
        Description: Creates an IPX source socket policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ipx_socket": ipx_socket,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPXSOURCESOCKET,
                                    **kwargs)

    def policy_clear_rule_ipxsourcesocket(self, device_name, profile_id='', ipx_socket='', mask='', port_string='',
                                          **kwargs):
        """
        Description: Deletes an IPX source socket policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "ipx_socket": ipx_socket,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPXSOURCESOCKET,
                                    **kwargs)

    def policy_set_rule_ipxtype(self, device_name, profile_id='', ipx_type='', mask='', port_string='',
                                storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                **kwargs):
        """
        Description: Creates an IPX type policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "ipx_type": ipx_type,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_IPXTYPE,
                                    **kwargs)

    def policy_clear_rule_ipxtype(self, device_name, profile_id='', ipx_type='', mask='', port_string='', **kwargs):
        """
        Description: Deletes an IPX type policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "ipx_type": ipx_type,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_IPXTYPE,
                                    **kwargs)

    def policy_set_rule_llcdsapssap(self, device_name, profile_id='', llc_dsap_ssap='', mask='', port_string='',
                                    storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                    mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                    **kwargs):
        """
        Description: Creates an LLC DSAP SSAP policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "llc_dsap_ssap": llc_dsap_ssap,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_LLCDSAPSSAP,
                                    **kwargs)

    def policy_clear_rule_llcdsapssap(self, device_name, profile_id='', llc_dsap_ssap='', mask='', port_string='',
                                      **kwargs):
        """
        Description: Deletes an LLC DSAP SSAP policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "llc_dsap_ssap": llc_dsap_ssap,
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_LLCDSAPSSAP,
                                    **kwargs)

    def policy_set_rule_tci(self, device_name, profile_id='', tci_value='', mask='', port_string='', storage_type='',
                            vlan='', forward='', drop='', cos='', tci_overwrite='', mirror_destination='', syslog='',
                            trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Description: Creates a port policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "tci_value": tci_value,
            "trap": trap,
            "vlan": vlan
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_TCI,
                                    **kwargs)

    def policy_clear_rule_tci(self, device_name, profile_id='', tci_value='', mask='', port_string='', **kwargs):
        """
        Description: Deletes a port policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id,
            "tci_value": tci_value
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_TCI,
                                    **kwargs)

    def policy_set_rule_vlantag(self, device_name, profile_id='', vlan_tag='', mask='', port_string='',
                                storage_type='', vlan='', forward='', drop='', cos='', tci_overwrite='',
                                mirror_destination='', syslog='', trap='', disable_port='', quarantine_profile='',
                                **kwargs):
        """
        Description: Creates a VLAN tag rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos": cos,
            "disable_port": disable_port,
            "drop": drop,
            "forward": forward,
            "mask": mask,
            "mirror_destination": mirror_destination,
            "port_string": port_string,
            "profile_id": profile_id,
            "quarantine_profile": quarantine_profile,
            "storage_type": storage_type,
            "syslog": syslog,
            "tci_overwrite": tci_overwrite,
            "trap": trap,
            "vlan": vlan,
            "vlan_tag": vlan_tag
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_VLANTAG,
                                    **kwargs)

    def policy_clear_rule_vlantag(self, device_name, profile_id='', vlan_tag='', mask='', port_string='', **kwargs):
        """
        Description: Deletes a VLAN tag rule for the given policy profile..

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "mask": mask,
            "port_string": port_string,
            "profile_id": profile_id,
            "vlan_tag": vlan_tag
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_VLANTAG,
                                    **kwargs)

    def policy_set_profile_access_control(self, device_name, state='', **kwargs):
        """
        Description: Configures the invalid action for the policy..

        Supported Agents and OS:
            CLI: EXTRWIRELESS
        """
        args = {
            "state": state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_ACCESS_CONTROL,
                                    **kwargs)

    def policy_set_profile_traffic_mirror(self, device_name, mirror_state='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXTRWIRELESS
        """
        args = {
            "mirror_state": mirror_state
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROFILE_TRAFFIC_MIRROR,
                                    **kwargs)

    def policy_set_rule_l7(self, device_name, profile_name='', rule_id='', group_name='', app_name='',
                           in_filter_action='', out_filter_action='', access_control='', cos_name='', mirror_state='',
                           **kwargs):
        """
        Description: Creates a Layer 7 policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXTRWIRELESS
        """
        args = {
            "access_control": access_control,
            "app_name": app_name,
            "cos_name": cos_name,
            "group_name": group_name,
            "in_filter_action": in_filter_action,
            "mirror_state": mirror_state,
            "out_filter_action": out_filter_action,
            "profile_name": profile_name,
            "rule_id": rule_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_L7,
                                    **kwargs)

    def policy_clear_rule_l7(self, device_name, profile_name='', rule_id='', **kwargs):
        """
        Description: Deletes a Layer 7 policy rule for the given policy profile..

        Supported Agents and OS:
            CLI: EXTRWIRELESS
        """
        args = {
            "profile_name": profile_name,
            "rule_id": rule_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_RULE_L7,
                                    **kwargs)

    def policy_set_rule_l7_configure(self, device_name, access_control='', app_name='', cos_name='', group_name='',
                                     in_filter_action='', mirror_state='', out_filter_action='', rule_id='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXTRWIRELESS
        """
        args = {
            "access_control": access_control,
            "app_name": app_name,
            "cos_name": cos_name,
            "group_name": group_name,
            "in_filter_action": in_filter_action,
            "mirror_state": mirror_state,
            "out_filter_action": out_filter_action,
            "rule_id": rule_id
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_L7_CONFIGURE,
                                    **kwargs)

    def policy_set_rule_apply(self, device_name, profile_name='', **kwargs):
        """
        Description: Applies policy rules to a given policy profile..

        Supported Agents and OS:
            CLI: EXTRWIRELESS
        """
        args = {
            "profile_name": profile_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_RULE_APPLY,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def policy_verify_state_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the policy state is enabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_POLICY_STATE, True,
                                           "Policy state is enabled.", "Policy state is NOT enabled!",
                                           **kwargs)

    def policy_verify_port_admin_profile_exists(self, device_name, port='', profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port that should be applied to the admin profile.
        [profile_id]  - The profile ID that should be applied to the admin profile.
        """
        args = {"profile_id": profile_id,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADMIN_PROFILES,
                                           self.parse_const.CHECK_PORT_ADMIN_PROFILE, True,
                                           "The specified port admin-profile was configured on {device_name}.",
                                           "The specified port admin-profile was NOT configured on "
                                           "{device_name}!", **kwargs)

    def policy_verify_mac_source_admin_profile_exists(self, device_name, mac_addr='', port='', profile_id='', mask="48",
                                                      **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mac_addr]    - The MAC address that should be applied to the admin profile.
        [port]        - The port that should be applied to the admin profile.
        [profile_id]  - The profile ID that should be applied to the admin profile.
        """
        args = {"profile_id": profile_id,
                "mac_addr": mac_addr,
                "port": port,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADMIN_PROFILES,
                                           self.parse_const.CHECK_MAC_SOURCE_ADMIN_PROFILE, True,
                                           "The specified MAC source admin-profile was configured on "
                                           "{device_name}.",
                                           "The specified MAC source admin-profile was NOT configured on "
                                           "{device_name}!", **kwargs)

    def policy_verify_profile_exists(self, device_name, profile_ids='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_ids] - The policy profile ID(s) that should exist on the device.

        Verifies that the given policy profile ID is configured on the device.
        """
        args = {"profile_id": profile_ids}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_EXISTS, True,
                                           "Policy Profile: {profile_id} exists on {device_name}.",
                                           "Policy Profile: {profile_id} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_profile_name(self, device_name, profile_id='', profile_name='', **kwargs):
        """
        Keyword arguments:
        [device_name] - The devices the keyword will be run against.
        [profile_id]  - The policy id who's name will be verified.
        [policy_name] - The name of that is being verified for the profile.

        Verifies the name of the given policy profile.
        """
        args = {"profile_id": profile_id,
                "profile_name": profile_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_NAME, True,
                                           "The name for policy profile id: {profile_id} is {profile_name}.",
                                           "The name for policy profile id: {profile_id} is NOT {profile_name}!",
                                           **kwargs)

    def policy_verify_profile_pvid_status_enabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that pvid status is enabled for the given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_PVID_STATUS, True,
                                           "Policy profile {profile_id} pvid status was enabled.",
                                           "Policy profile {profile_id} pvid status was DISABLED!",
                                           **kwargs)

    def policy_verify_profile_pvid_status_disabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that pvid status is disabled for the given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_PVID_STATUS, False,
                                           "Policy profile {profile_id} pvid status was disabled.",
                                           "Policy profile {profile_id} pvid status was ENABLED!",
                                           **kwargs)

    def policy_verify_profile_pvid(self, device_name, profile_id='', pvid='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.
        [pvid]        - The pvid value that should be configured to the profile.

        Verifies that a policy profile is configured with the given pvid value.
        """
        args = {"profile_id": profile_id,
                "pvid": pvid}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_PVID, True,
                                           "Policy profile {profile_id} was configured with pvid {pvid}.",
                                           "Policy profile {profile_id} was NOT configured with pvid {pvid}!",
                                           **kwargs)

    def policy_verify_profile_cos_status_enabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that COS status is enabled for the given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_COS_STATUS, True,
                                           "COS status was enabled on policy profile {profile_id}.",
                                           "COS status was DISABLED on policy profile {profile_id}!",
                                           **kwargs)

    def policy_verify_profile_cos_status_should_be_disabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that COS status is disabled for the given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_COS_STATUS, False,
                                           "COS status was disabled on policy profile {profile_id}.",
                                           "COS status was ENABLED on policy profile {profile_id}!",
                                           **kwargs)

    def policy_verify_profile_cos(self, device_name, profile_id='', cos_value='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.
        [cos_value]   - The cos value that should be configured to the profile.

        Verifies that a policy profile is configured with the given cos value.
        """
        args = {"profile_id": profile_id,
                "cos_value": cos_value}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_COS, True,
                                           "Policy profile {profile_id} was configured with COS value "
                                           "{cos_value}.",
                                           "Policy profile {profile_id} was NOT configured with COS value "
                                           "{cos_value}!", **kwargs)

    def policy_verify_profile_egress_vlan_exists(self, device_name, profile_id='', vlans='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should run against.
        [profile_id]  - The policy profile to inspect.
        [vlans]       - The vlan(s) that is expected to be configured on the profile.

        Verifies that a given vlan exists on a policy profile's egress vlan list.
        """
        args = {"profile_id": profile_id,
                "vlan": vlans}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_EGRESS_VLAN, True,
                                           "VLAN {vlan} was on profile {profile_id}'s egress vlan list.",
                                           "VLAN {vlan} was NOT on profile {profile_id}'s egress vlan list!",
                                           **kwargs)

    def policy_verify_profile_untagged_vlan_exists(self, device_name, profile_id='', vlans='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should run against.
        [profile_id]  - The policy profile to inspect.
        [vlans]       - The vlan(s) that is expected to be configured on the profile.

        Verifies that a given vlan exists on a policy profile's untagged vlan list.
        """
        args = {"profile_id": profile_id,
                "vlan": vlans}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_UNTAGGED_VLAN, True,
                                           "VLAN {vlan} was on profile {profile_id}'s untagged vlan list.",
                                           "VLAN {vlan} was NOT on profile {profile_id}'s untagged vlan list!",
                                           **kwargs)

    def policy_verify_profile_forbidden_vlan_exists(self, device_name, profile_id='', vlans='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.
        [vlans]       - The vlan(s) that is expected to be configured on the profile.

        Verifies that a given vlan exists on a policy profile's forbidden vlan list.
        """
        args = {"profile_id": profile_id,
                "vlan": vlans}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_FORBIDDEN_VLAN, True,
                                           "VLAN {vlan} was on profile {profile_id}'s forbidden vlan list.",
                                           "VLAN {vlan} was NOT on profile {profile_id}'s forbidden vlan list!",
                                           **kwargs)

    def policy_verify_profile_tci_overwrite_enabled(self, device_name, profile_ids='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_ids] - The policy profile ID(s) to inspect.

        Verifies that TCI overwrite is enabled on a given policy profile.
        """
        args = {"profile_id": profile_ids}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_TCI_OVERWRITE, True,
                                           "TCI status is enabled for Profile: {profile_id} on {device_name}.",
                                           "TCI status is INCORRECTLY DISABLED for Profile: {profile_id} on "
                                           "{device_name}!",
                                           **kwargs)

    def policy_verify_profile_tci_overwrite_disabled(self, device_name, profile_ids='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_ids] - The policy profile ID(s) to inspect.

        Verifies that TCI overwrite is disabled on a given policy profile.
        """
        args = {"profile_id": profile_ids}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_TCI_OVERWRITE, False,
                                           "TCI status is disabled for Profile: {profile_id} on {device_name}.",
                                           "TCI status is INCORRECTLY ENABLED for Profile: {profile_id} on "
                                           "{device_name}!",
                                           **kwargs)

    def policy_verify_profile_precedence(self, device_name, profile_id='', precedence_string='', **kwargs):
        """
        Keyword Arguments:
        [device_name]       - The device the keyword should be run against.
        [profile_ids]       - The policy profile to inspect.
        [precedence_string] - The precedence order for the profile's rules. The passed string will be
                              expanded to a list of ints, so it can be passed in the same format it is
                              displayed on the device. For example "1,2-4,5" would be expanded to "1,2,3,4,5".

        Verifies the rule precedence order for a given policy profile.
        """
        args = {"profile_id": profile_id,
                "precedence_string": precedence_string}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_PRECEDENCE, True,
                                           "Policy profile {profile_id} was configured with precedence list "
                                           "{precedence_string}.",
                                           "Policy profile {profile_id} was NOT configured with precedence list "
                                           "{precedence_string}!",
                                           **kwargs)

    def policy_verify_profile_mirror_destination(self, device_name, profile_id='', mirror_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword should be run against.
        [profile_id]   - The policy profile to inspect.
        [mirror_index] - The mirror index the profile should be configured with.

        Verifies the mirror index of the given policy profile.
        """
        args = {"profile_id": profile_id,
                "mirror_index": mirror_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_MIRROR_DEST, True,
                                           "Policy profile {profile_id} was configured with mirror index "
                                           "{mirror_index}.",
                                           "Policy profile {profile_id} was NOT configured with mirror index "
                                           "{mirror_index}!",
                                           **kwargs)

    def policy_verify_profile_syslog_state_enabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that syslog is enabled on a given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_SYSLOG, True,
                                           "Syslog was enabled on policy profile {profile_id}.",
                                           "Syslog was DISABLED on policy profile {profile_id}!",
                                           **kwargs)

    def policy_verify_profile_syslog_state_disabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that syslog is disabled on a given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_SYSLOG, False,
                                           "Syslog was disabled on policy profile {profile_id}.",
                                           "Syslog was ENABLED on policy profile {profile_id}!",
                                           **kwargs)

    def policy_verify_profile_trap_state_enabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that traps are enabled on a given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_TRAP, True,
                                           "Traps are enabled on policy profile {profile_id}.",
                                           "Traps are DISABLED on policy profile {profile_id}!",
                                           **kwargs)

    def policy_verify_profile_trap_state_disabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that traps are disabled on a given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_TRAP, False,
                                           "Traps are disabled on policy profile {profile_id}.",
                                           "Traps are ENABLED on policy profile {profile_id}!",
                                           **kwargs)

    def policy_verify_profile_disable_port_enabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that disable port is enabled on a given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_DISABLE_PORT, True,
                                           "Disable port was enabled on policy profile {profile_id}.",
                                           "Disable port was DISABLED on policy profile {profile_id}!",
                                           **kwargs)

    def policy_verify_profile_disable_port_disabled(self, device_name, profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.

        Verifies that disable port is disabled on a given policy profile.
        """
        args = {"profile_id": profile_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_DISABLE_PORT, False,
                                           "Disable port was disabled on policy profile {profile_id}.",
                                           "Disable port was ENABLED on policy profile {profile_id}!",
                                           **kwargs)

    def policy_verify_profile_fst_index(self, device_name, profile_id='', fst_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_id]  - The policy profile to inspect.
        [fst_index]   - The fst index the profile should be configured with.

        Verifies the fst index of the given policy profile.
        """
        args = {"profile_id": profile_id,
                "fst_index": fst_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_FST, True,
                                           "Policy profile {profile_id} was configured with fst index "
                                           "{fst_index}.",
                                           "Policy profile {profile_id} was NOT configured with fst index "
                                           "{fst_index}!",
                                           **kwargs)

    def policy_verify_profile_web_redirect_index(self, device_name, profile_id='', web_redirect_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name]        - The device the keyword should be run against.
        [profile_id]         - The policy profile to inspect.
        [web_redirect_index] - The fst index the profile should be configured with.

        Verifies the web redirect index of the given policy profile.
        """
        args = {"profile_id": profile_id,
                "web_redirect_index": web_redirect_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_WEB_REDIRECT, True,
                                           "Policy profile {profile_id} was configured with web redirect index "
                                           "{web_redirect_index}.",
                                           "Policy profile {profile_id} was NOT configured with web redirect "
                                           "index {web_redirect_index}!",
                                           **kwargs)

    def policy_verify_rule_application_exists(self, device_name, profile_id='', application='', application_type='',
                                              mask='', port_string='', storage_type='', vlan='', cos='',
                                              tci_overwrite='', mirror_destination='', syslog='', trap='',
                                              disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [application]         - The application the rule should be configure with.
        [application_type]    - The application type the rule should be configured with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "application": application,
                "application_type": application_type,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_APPLICATION, True,
                                           "Specified application policy rule exists on {device_name}.",
                                           "Specified application policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ethertype_exists(self, device_name, profile_id='', ether_type='', mask='', port_string='',
                                            storage_type='', vlan='', cos='', tci_overwrite='',
                                            mirror_destination='', syslog='', trap='', disable_port='',
                                            quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ether_type]          - The ether type the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ether_type": ether_type,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_ETHER, True,
                                           "Specified ether policy rule exists on {device_name}.",
                                           "Specified ether policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_icmp6type_exists(self, device_name, profile_id='', icmp6_type='', icmp6_code='', mask='',
                                            port_string='', storage_type='', vlan='', cos='',
                                            tci_overwrite='', mirror_destination='', syslog='', trap='',
                                            disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [icmp6_type]          - The ICMPv6 type the rule should be configure with.
        [icmp6_code]          - The ICMPv6 code the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "icmp6_type": icmp6_type,
                "icmp6_code": icmp6_code,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_ICMP6TYPE, True,
                                           "Specified icmp6type policy rule exists on {device_name}.",
                                           "Specified icmp6type policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_icmptype_exists(self, device_name, profile_id='', icmp_type='', icmp_code='', mask='',
                                           port_string='', storage_type='', vlan='', cos='', tci_overwrite='',
                                           mirror_destination='', syslog='', trap='', disable_port='',
                                           quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [icmp_type]           - The ICMP type the rule should be configure with.
        [icmp_code]           - The ICMP code the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "icmp_type": icmp_type,
                "icmp_code": icmp_code,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_ICMPTYPE, True,
                                           "Specified icmptype policy rule exists on {device_name}.",
                                           "Specified icmptype policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ip6dest_exists(self, device_name, profile_id='', ipv6_addr='', l4_port='', mask='',
                                          port_string='', storage_type='', vlan='', cos='', tci_overwrite='',
                                          mirror_destination='', syslog='', trap='', disable_port='',
                                          quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipv6_addr]           - The IPv6 address the rule should be configure with.
        *[l4_port]            - The TCP/UDP port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipv6_addr": ipv6_addr,
                "l4_port": l4_port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IP6DEST, True,
                                           "Specified ip6dest policy rule exists on {device_name}.",
                                           "Specified ip6dest policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ip6flowlabel_exists(self, device_name, profile_id='', ipv6_flow_label='', mask='',
                                               port_string='', storage_type='', vlan='', cos='',
                                               tci_overwrite='', mirror_destination='', syslog='', trap='',
                                               disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipv6_flow_label]     - The IPv6 flow label the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipv6_flow_label": ipv6_flow_label,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IP6FLOWLABEL, True,
                                           "Specified ip6flowlabel policy rule exists on {device_name}.",
                                           "Specified ip6flowlabel policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ip6source_exists(self, device_name, profile_id='', ipv6_addr='', l4_port='', mask='',
                                            port_string='', storage_type='', vlan='', cos='',
                                            tci_overwrite='', mirror_destination='', syslog='', trap='',
                                            disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipv6_addr]           - The IPv6 address the rule should be configure with.
        *[l4_port]            - The TCP/UDP port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipv6_addr": ipv6_addr,
                "l4_port": l4_port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IP6SOURCE, True,
                                           "Specified ip6source policy rule exists on {device_name}.",
                                           "Specified ip6source policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipdestsocket_exists(self, device_name, profile_id='', ip_addr='', l4_port='', mask='',
                                               port_string='', storage_type='', vlan='', cos='',
                                               tci_overwrite='', mirror_destination='', syslog='', trap='',
                                               disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_addr]             - The IP address the rule should be configure with.
        *[l4_port]            - The TCP/UDP port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_addr": ip_addr,
                "l4_port": l4_port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPDESTSOCKET, True,
                                           "Specified ipdestsocket policy rule exists on {device_name}.",
                                           "Specified ipdestsocket policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipfrag_exists(self, device_name, profile_id='', mask='', port_string='', storage_type='',
                                         vlan='', cos='', tci_overwrite='', mirror_destination='', syslog='',
                                         trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPFRAG, True,
                                           "Specified ipfrag policy rule exists on {device_name}.",
                                           "Specified ipfrag policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipproto_exists(self, device_name, profile_id='', ip_proto='', mask='', port_string='',
                                          storage_type='', vlan='', cos='', tci_overwrite='',
                                          mirror_destination='', syslog='', trap='', disable_port='',
                                          quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_proto]            - The IP protocol value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_proto": ip_proto,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPPROTO, True,
                                           "Specified ipproto policy rule exists on {device_name}.",
                                           "Specified ipproto policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipsourcesocket_exists(self, device_name, profile_id='', ip_addr='', l4_port='', mask='',
                                                 port_string='', storage_type='', vlan='', cos='',
                                                 tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                 disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_addr]             - The IP address the rule should be configure with.
        *[l4_port]            - The TCP/UDP port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_addr": ip_addr,
                "l4_port": l4_port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPSOURCESOCKET, True,
                                           "Specified ipsourcesocket policy rule exists on {device_name}.",
                                           "Specified ipsourcesocket policy rule DOES NOT exist on "
                                           "{device_name}!",
                                           **kwargs)

    def policy_verify_rule_iptos_exists(self, device_name, profile_id='', ip_tos='', mask='', port_string='',
                                        storage_type='', vlan='', cos='', tci_overwrite='',
                                        mirror_destination='', syslog='', trap='', disable_port='',
                                        quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_names]        - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_tos]              - The IP TOS value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_tos": ip_tos,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPTOS, True,
                                           "Specified iptos policy rule exists on {device_name}.",
                                           "Specified iptos policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipttl_exists(self, device_name, profile_id='', ip_ttl='', mask='', port_string='',
                                        storage_type='', vlan='', cos='', tci_overwrite='',
                                        mirror_destination='', syslog='', trap='', disable_port='',
                                        quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_ttl]              - The IP TTL value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_ttl": ip_ttl,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPTTL, True,
                                           "Specified ipttl policy rule exists on {device_name}.",
                                           "Specified ipttl policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxclass_exists(self, device_name, profile_id='', ipx_class='', mask='', port_string='',
                                           storage_type='', vlan='', cos='', tci_overwrite='',
                                           mirror_destination='', syslog='', trap='', disable_port='',
                                           quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_class]           - The IPX class value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_class": ipx_class,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXCLASS, True,
                                           "Specified ipxclass policy rule exists on {device_name}.",
                                           "Specified ipxclass policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxdest_exists(self, device_name, profile_id='', ipx_dest='', mask='', port_string='',
                                          storage_type='', vlan='', cos='', tci_overwrite='',
                                          mirror_destination='', syslog='', trap='', disable_port='',
                                          quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_dest]            - The IPX destination address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_dest": ipx_dest,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXDEST, True,
                                           "Specified ipxdest policy rule exists on {device_name}.",
                                           "Specified ipxdest policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxdestsocket_exists(self, device_name, profile_id='', ipx_dest_socket='', mask='',
                                                port_string='', storage_type='', vlan='', cos='',
                                                tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_dest_socket]     - The IPX destination socket the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_dest_socket": ipx_dest_socket,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXDESTSOCKET, True,
                                           "Specified ipxdestsocket policy rule exists on {device_name}.",
                                           "Specified ipxdestsocket policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxsource_exists(self, device_name, profile_id='', ipx_source='', mask='', port_string='',
                                            storage_type='', vlan='', cos='', tci_overwrite='',
                                            mirror_destination='', syslog='', trap='', disable_port='',
                                            quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_source]          - The IPX source address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_source": ipx_source,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXSOURCE, True,
                                           "Specified ipxsource policy rule exists on {device_name}.",
                                           "Specified ipxsource policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxsourcesocket_exists(self, device_name, profile_id='', ipx_source_socket='', mask='',
                                                  port_string='', storage_type='', vlan='', cos='',
                                                  tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                  disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_source_socket]   - The IPX source socket the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_source_socket": ipx_source_socket,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXSOURCESOCKET, True,
                                           "Specified ipxsourcesocket policy rule exists on {device_name}.",
                                           "Specified ipxsourcesocket policy rule DOES NOT exist on "
                                           "{device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxtype_exists(self, device_name, profile_id='', ipx_type='', mask='', port_string='',
                                          storage_type='', vlan='', cos='', tci_overwrite='',
                                          mirror_destination='', syslog='', trap='', disable_port='',
                                          quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_type]            - The IPX type value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_type": ipx_type,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXTYPE, True,
                                           "Specified ipxtype policy rule exists on {device_name}.",
                                           "Specified ipxtype policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_llcdsapssap_exists(self, device_name, profile_id='', llc_dsap_ssap='', mask='',
                                              port_string='', storage_type='', vlan='', cos='', tci_overwrite='',
                                              mirror_destination='', syslog='', trap='', disable_port='',
                                              quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [llc_dsap_ssap]       - The LLC DSAP SSAP value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "llc_dsap_ssap": llc_dsap_ssap,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_LLCDSAPSSAP, True,
                                           "Specified llcdsapssap policy rule exists on {device_name}.",
                                           "Specified llcdsapssap policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_macdest_exists(self, device_name, profile_id='', mac_addr='', mask='', port_string='',
                                          storage_type='', vlan='', cos='', tci_overwrite='',
                                          mirror_destination='', syslog='', trap='', disable_port='',
                                          quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_names]        - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [mac_addr]            - The MAC address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "mac_addr": mac_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_MACDEST, True,
                                           "Specified macdest policy rule exists on {device_name}.",
                                           "Specified macdest policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_macsource_exists(self, device_name, profile_id='', mac_addr='', mask='', port_string='',
                                            storage_type='', vlan='', cos='', tci_overwrite='',
                                            mirror_destination='', syslog='', trap='', disable_port='',
                                            quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [mac_addr]            - The MAC address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "mac_addr": mac_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_MACSOURCE, True,
                                           "Specified macsource policy rule exists on {device_name}.",
                                           "Specified macsource policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_port_exists(self, device_name, profile_id='', port='', mask='', port_string='',
                                       storage_type='', vlan='', cos='', tci_overwrite='',
                                       mirror_destination='', syslog='', trap='', disable_port='',
                                       quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [port]                - The port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "port": port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_PORT, True,
                                           "Specified port policy rule exists on {device_name}.",
                                           "Specified port policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_tci_exists(self, device_name, profile_id='', tci_value='', mask='', port_string='',
                                      storage_type='', vlan='', cos='', tci_overwrite='',
                                      mirror_destination='', syslog='', trap='', disable_port='',
                                      quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [tci_value]           - The tci value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "tci_value": tci_value,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_TCI, True,
                                           "Specified tci policy rule exists on {device_name}.",
                                           "Specified tci policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_tcpdestportip_exists(self, device_name, profile_id='', tcp_port='', ip_addr='', mask='',
                                                port_string='', storage_type='', vlan='', cos='',
                                                tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [tcp_port]            - The TCP destination port the rule should be configure with.
        *[ip_addr]            - The IPv4/IPv6 address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "tcp_port": tcp_port,
                "ip_addr": ip_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_TCPDESTPORTIP, True,
                                           "Specified tcpdestportIP policy rule exists on {device_name}.",
                                           "Specified tcpdestportIP policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_tcpsourceportip_exists(self, device_name, profile_id='', tcp_port='', ip_addr='', mask='',
                                                  port_string='', storage_type='', vlan='', cos='',
                                                  tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                  disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [tcp_port]            - The TCP destination port the rule should be configure with.
        *[ip_addr]            - The IPv4/IPv6 address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "tcp_port": tcp_port,
                "ip_addr": ip_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_TCPSOURCEPORTIP, True,
                                           "Specified tcpsourceportIP policy rule exists on {device_name}.",
                                           "Specified tcpsourceportIP policy rule DOES NOT exist on "
                                           "{device_name}!",
                                           **kwargs)

    def policy_verify_rule_udpdestportip_exists(self, device_name, profile_id='', udp_port='', ip_addr='', mask='',
                                                port_string='', storage_type='', vlan='', cos='',
                                                tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [udp_port]            - The UDP destination port the rule should be configure with.
        *[ip_addr]            - The IPv4/IPv6 address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "udp_port": udp_port,
                "ip_addr": ip_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_UDPDESTPORTIP, True,
                                           "Specified udpdestportIP policy rule exists on {device_name}.",
                                           "Specified udpdestportIP policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_udpsourceportip_exists(self, device_name, profile_id='', udp_port='', ip_addr='', mask='',
                                                  port_string='', storage_type='', vlan='', cos='',
                                                  tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                  disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [udp_port]            - The TCP destination port the rule should be configure with.
        *[ip_addr]            - The IPv4/IPv6 address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "udp_port": udp_port,
                "ip_addr": ip_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_UDPSOURCEPORTIP, True,
                                           "Specified udpsourceportIP policy rule exists on {device_name}.",
                                           "Specified udpsourceportIP policy rule DOES NOT exist on "
                                           "{device_name}!",
                                           **kwargs)

    def policy_verify_rule_vlantag_exists(self, device_name, profile_id='', vlan_tag='', mask='', port_string='',
                                          storage_type='', vlan='', cos='', tci_overwrite='',
                                          mirror_destination='', syslog='', trap='', disable_port='',
                                          quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [vlan_tag]            - The tci value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "vlan_tag": vlan_tag,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_VLANTAG, True,
                                           "Specified vlantag policy rule exists on {device_name}.",
                                           "Specified vlantag policy rule DOES NOT exist on {device_name}!",
                                           **kwargs)

    def policy_verify_allow_types(self, device_name, port='', allow_type_list='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword should run against.
        [device_ports]    - The port(s) that should be inspected.
        [allow_type_list] - A list with length of 29 that corresponds to the output of
                            "show policy allowed-type <port>". Each entry should be a 1
                            or a 0. 1 indicates enabled 0 indicates disabled.

            Ex.
            allowed_types = "[1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
                              0, 1, 1, 1, 1, 1, 1, 1, 0, 1,
                              1, 1, 0, 1, 0, 0, 0, 0, 1]"

        Verifies the correct policy rule types are supported on a given port.
        """
        if "[" in allow_type_list and "]" in allow_type_list:
            allow_type_list = literal_eval(allow_type_list)

        if not isinstance(allow_type_list, list) or len(allow_type_list) != 29:
            self.logger.log_error("Length of allow_type_list must be exactly 29.")

        all_types = []
        for entry in allow_type_list:
            if entry == 1:
                all_types.append(True)
            else:
                all_types.append(False)

        args = {"port": port,
                "all_types": str(all_types)}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALLOW_TYPE,
                                           self.parse_const.CHECK_POLICY_ALLOWED_TYPES, True,
                                           "All expected allowed types were supported.",
                                           "An expected allowed type was is NOT supported!",
                                           **kwargs)

    def policy_verify_invalid_action(self, device_name, action='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [action]      - default, drop, or forward

        Verifies that the policy invalid action is correct.
        """
        args = {"action": action}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INVALID_ACTION,
                                           self.parse_const.CHECK_POLICY_INVALID_ACTION, True,
                                           "Policy invalid action is {action}.",
                                           "Policy invalid action is NOT {action}!",
                                           **kwargs)

    def policy_verify_maptable_response(self, device_name, attribute='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [attribute]   - both, policy, or tunnel.

        Verifies that the policy map response attribute type is correct.
        """
        args = {"attribute": attribute}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MAP_RESPONSE,
                                           self.parse_const.CHECK_POLICY_MAP_RESPONSE, True,
                                           "Policy map response is {attribute}.",
                                           "Policy map response is NOT {attribute}!",
                                           **kwargs)

    def policy_verify_global_vlan_authorization(self, device_name, state='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [state]       - enabled or disabled.

        Verifies that the global policy vlan authorization setting is correct.
        """
        args = {"state": state}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_VLANAUTHORIZATION,
                                           self.parse_const.CHECK_POLICY_GLOBAL_VLAN_AUTHORIZATION_STATE, True,
                                           "Policy global vlan authorization state is {state}.",
                                           "Policy global vlan authorization state is NOT {state}!",
                                           **kwargs)

    def policy_verify_invalid_count(self, device_name, count='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [count]       - The number of invalid/unknown profiles detected.
        Verifies that the policy invalid count is correct.
        """
        args = {"count": count}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INVALID_COUNT,
                                           self.parse_const.CHECK_POLICY_INVALID_COUNT, True,
                                           "Policy invalid count is {count}.",
                                           "Policy invalid count is NOT {count}!",
                                           **kwargs)

    def policy_verify_invalid_counter_should_increment(self, device_name, increment='', **kwargs):
        """
        Keyword Arguments
        [device_name] - The device the keyword will be run against.
        [increment]   - The amount that the Policy Invalid counter should increment.

        Verifies that the Policy Invalid counter incremented by the specified amount.
        """
        args = {"increment": increment}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_INVALID_COUNT,
                                           self.parse_const.VERIFY_POLICY_INVALID_COUNT_INCREMENTED, True,
                                           "The Policy Invalid count incremented by {increment}.",
                                           "The Policy Invalid count did not increment by the expected value!",
                                           **kwargs)

    def policy_verify_rule_model_access_list(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the rule-model is set to access-list.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_POLICY_RULE_MODEL_ACCESS_LIST, True,
                                           "Policy model is access-list.",
                                           "Policy model is NOT access-list!",
                                           **kwargs)

    def policy_verify_rule_model_hierarchical(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the rule-model is set to hierarchical.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_POLICY_RULE_MODEL_HIERARCHICAL, True,
                                           "Policy model is hierarchical.",
                                           "Policy model is NOT hierarchical!",
                                           **kwargs)

    def policy_verify_acl_ipttl(self, device_name, list_name='', rule='', ttl='', mask='', **kwargs):
        """
        Keyword Arguments:
        [device_name]     - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [ttl]             - The TTL that should be present in the rule.
        [mask]            - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given ttl and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "ttl": ttl,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_IPTTL, True,
                                           "The given TTL and MASK values are present for access-list "
                                           "{list_name}.{rule}.",
                                           "The given TTL and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_ether(self, device_name, list_name='', rule='', ether='', mask='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [ether] - The ether that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given ether and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "ether": ether,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ETHER, True,
                                           "The given Ether and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given Ether and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_icmp6type(self, device_name, list_name='', rule='', icmp6type='', mask='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [icmp6type] - The icmp6type that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given icmp6type and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "icmp6type": icmp6type,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ICMP6TYPE, True,
                                           "The given icmp6type and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given icmp6type and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_icmptype(self, device_name, list_name='', rule='', icmptype='', mask='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [icmptype] - The icmptype that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given icmptype and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "icmptype": icmptype,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ICMPTYPE, True,
                                           "The given icmptype and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given icmptype and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_ipdestsocket(self, device_name, list_name='', rule='', ipdestsocket='', mask='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [ipdestsocket] - The ipdestsocket that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given ipdestsocket and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "ipdestsocket": ipdestsocket,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_IPDESTSOCKET, True,
                                           "The given ipdestsocket and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given ipdestsocket and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_ipfrag(self, device_name, list_name='', rule='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>

        Verifies that the given acl {list_name}.{rule} is configured with ipfrag.
        """
        args = {"list_name": list_name,
                "rule": rule}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_IPFRAG, True,
                                           "IPFrag is present for " +
                                           "access-list {list_name}.{rule}.",
                                           "IPFrag is NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_ipproto(self, device_name, list_name='', rule='', ipproto='', mask='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [ipproto] - The ipproto that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given ipproto and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "ipproto": ipproto,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_IPPROTO, True,
                                           "The given ipproto and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given ipproto and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_ipsourcesocket(self, device_name, list_name='', rule='', ipsourcesocket='', mask='',
                                         **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [ipsourcesocket] - The ipsourcesocket that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given ipsourcesocket and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "ipsourcesocket": ipsourcesocket,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_IPSOURCESOCKET, True,
                                           "The given ipsourcesocket and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given ipsourcesocket and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_iptos(self, device_name, list_name='', rule='', iptos='', mask='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [iptos] - The iptos that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given iptos and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "iptos": iptos,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_IPTOS, True,
                                           "The given iptos and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given iptos and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_tcpdestportip(self, device_name, list_name='', rule='', tcpdestportip='', mask='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [tcpdestportip] - The tcpdestportip that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given tcpdestportip and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "tcpdestportip": tcpdestportip,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_TCPDESTPORTIP, True,
                                           "The given tcpdestportip and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given tcpdestportip and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_tcpsourceportip(self, device_name, list_name='', rule='', tcpsourceportip='', mask='',
                                          **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [tcpsourceportip] - The tcpsourceportip that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given tcpsourceportip and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "tcpsourceportip": tcpsourceportip,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_TCPSOURCEPORTIP, True,
                                           "The given tcpsourceportip and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given tcpsourceportip and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_udpdestportip(self, device_name, list_name='', rule='', udpdestportip='', mask='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [udpdestportip] - The udpdestportip that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given udpdestportip and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "udpdestportip": udpdestportip,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_UDPDESTPORTIP, True,
                                           "The given udpdestportip and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given udpdestportip and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_udpsourceportip(self, device_name, list_name='', rule='', udpsourceportip='', mask='',
                                          **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [udpsourceportip] - The udpsourceportip that should be present in the rule.
        [mask] - The mask value that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given udpsourceportip and mask data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "udpsourceportip": udpsourceportip,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_UDPSOURCEPORTIP, True,
                                           "The given udpsourceportip and MASK values are present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given udpsourceportip and MASK values are NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_action_cos(self, device_name, list_name='', rule='', cos='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [cos] - The cos that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given cos data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "cos": cos}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_COS, True,
                                           "The given cos value is present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given cos value is NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_action_mirror(self, device_name, list_name='', rule='', mirror_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [mirror_index] - The mirror index that should be present in the rule.

        Verifies that the given acl {list_name}.{rule} is configured with the given mirror data.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "mirror_index": mirror_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_MIRROR, True,
                                           "The given mirror value is present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given mirror value is NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_action_drop(self, device_name, list_name='', rule='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>

        Verifies that the given acl {list_name}.{rule} is configured with the drop flag.
        """
        args = {"list_name": list_name,
                "rule": rule}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_DROP, True,
                                           "The given drop flag is present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given drop flag is NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_action_forward(self, device_name, list_name='', rule='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>

        Verifies that the given acl {list_name}.{rule} is configured with the forward flag.
        """
        args = {"list_name": list_name,
                "rule": rule}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_FORWARD, True,
                                           "The given forward flag is present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The given forward flag is NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_action_trap_enabled(self, device_name, list_name='', rule='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>

        Verifies that the given acl {list_name}.{rule} is configured with the trap flag.
        """
        args = {"list_name": list_name,
                "rule": rule}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_TRAP_ENABLED, True,
                                           "The trap flag is present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The trap flag is NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_action_syslog_enabled(self, device_name, list_name='', rule='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>

        Verifies that the given acl {list_name}.{rule} is configured with the syslog flag.
        """
        args = {"list_name": list_name,
                "rule": rule}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_SYSLOG_ENABLED, True,
                                           "The syslog flag is present for " +
                                           "access-list {list_name}.{rule}.",
                                           "The syslog flag is NOT present for " +
                                           "access-list {list_name}.{rule}!",
                                           **kwargs)

    def policy_verify_acl_action_all(self, device_name, list_name='', rule='', volatile='', trap_syslog_flag='',
                                     drop_fwrd='', cos='', mirror='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name, rule] - The access list naming format of <list_name>.<rule>
        [volatile] - The flag that should be set in the table. Either "V" or "NV"
        [trap_syslog_flag] - The Trap or Syslog flags that should be set in the table.
        [drop_fwrd] - The vlan action state. Either "drop" or "fwrd".
        [cos] - The cos value that should be in the table.
        [mirror] - The mirror index that should be in the table.

        Verifies that the given acl {list_name}.{rule} is configured with the provided action values.
        5 action values may be verified.  Each value defaults to None.  Pass ${EMPTY} to verify table value is empty.
        """
        args = {"list_name": list_name,
                "rule": rule,
                "st": volatile,
                "ts": trap_syslog_flag,
                "vlan": drop_fwrd,
                "cos": cos,
                "mir": mirror}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_ALL, True,
                                           "The action items present for access-list {list_name}.{rule} " +
                                           "match the provided values.",
                                           "The action items present for access-list {list_name}.{rule} " +
                                           "do NOT match the provided values!",
                                           **kwargs)

    def policy_verify_acl_action_set_cos(self, device_name, set_id='', cos='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [set_id] - The access list action-set id
        [cos] - The cos that should be present in the rule.

        Verifies that the given action-set {set_id} is configured with the given cos data.
        """
        args = {"set_id": set_id,
                "cos": cos}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_ACTION_SET,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_SET_COS, True,
                                           "The given cos value is present for " +
                                           "action-set {set_id}.",
                                           "The given cos value is NOT present for " +
                                           "action-set {set_id}!",
                                           **kwargs)

    def policy_verify_acl_action_set_mirror(self, device_name, set_id='', mirror_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [set_id] - The access list action-set id.
        [mirror_index] - The mirror index that should be present in the rule.

        Verifies that the given action-set {set_id} is configured with the given mirror data.
        """
        args = {"set_id": set_id,
                "mirror_index": mirror_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_ACTION_SET,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_SET_MIRROR, True,
                                           "The given mirror value is present for " +
                                           "action-set {set_id}.",
                                           "The given mirror value is NOT present for " +
                                           "action-set {set_id}!",
                                           **kwargs)

    def policy_verify_acl_action_set_drop(self, device_name, set_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [set_id] - The access list action-set id.

        Verifies that the given action-set {set_id} is configured with the drop flag.
        """
        args = {"set_id": set_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_ACTION_SET,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_SET_DROP, True,
                                           "The given drop flag is present for " +
                                           "action-set {set_id}.",
                                           "The given drop flag is NOT present for " +
                                           "action-set {set_id}!",
                                           **kwargs)

    def policy_verify_acl_action_set_forward(self, device_name, set_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [set_id] - The access list action-set id.

        Verifies that the given action-set {set_id} is configured with the forward flag.
        """
        args = {"set_id": set_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_ACTION_SET,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_SET_FORWARD, True,
                                           "The given forward flag is present for " +
                                           "action-set {set_id}.",
                                           "The given forward flag is NOT present for " +
                                           "action-set {set_id}!",
                                           **kwargs)

    def policy_verify_acl_action_set_trap_enabled(self, device_name, set_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [set_id] - The access list action-set id.

        Verifies that the given action-set {set_id} is configured with the trap flag.
        """
        args = {"set_id": set_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_ACTION_SET,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_SET_TRAP_ENABLED, True,
                                           "The trap flag is present for " +
                                           "action-set {set_id}.",
                                           "The trap flag is NOT present for " +
                                           "action-set {set_id}!",
                                           **kwargs)

    def policy_verify_acl_action_set_syslog_enabled(self, device_name, set_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [set_id] - The access list action-set id.

        Verifies that the given action-set {set_id} is configured with the syslog flag.
        """
        args = {"set_id": set_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_ACTION_SET,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_SET_SYSLOG_ENABLED, True,
                                           "The syslog flag is present for " +
                                           "action-set {set_id}.",
                                           "The syslog flag is NOT present for " +
                                           "action-set {set_id}!",
                                           **kwargs)

    def policy_verify_acl_action_set_all(self, device_name, set_id='', volatile='', trap_syslog_flag='',
                                         drop_fwrd='', cos='', mirror='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [set_id] - The access list action-set id.
        [volatile] - The flag that should be set in the table. Either "V" or "NV"
        [trap_syslog_flag] - The Trap or Syslog flags that should be set in the table.
        [drop_fwrd] - The vlan action state. Either "drop" or "fwrd".
        [cos] - The cos value that should be in the table.
        [mirror] - The mirror index that should be in the table.

        Verifies that the given action-set {set_id} is configured with the provided action values.
        Each value defaults to None.  Pass ${EMPTY} to verify table value is empty.
        """
        args = {"set_id": set_id,
                "st": volatile,
                "ts": trap_syslog_flag,
                "vlan": drop_fwrd,
                "cos": cos,
                "mir": mirror}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_ACTION_SET,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_SET_ALL, True,
                                           "The action items present for action-set {set_id} " +
                                           "match the provided values.",
                                           "The action items present for action-set {set_id} " +
                                           "do NOT match the provided values!",
                                           **kwargs)

    def policy_verify_acl_profile_index(self, device_name, list_name='', profile_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name] - The access list name
        [index] - The PID that should be present in the table for the list.

        Verifies that the given access-list is configured with the given index PID value.
        """
        args = {"list_name": list_name,
                "profile_index": profile_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PROFILE,
                                           self.parse_const.CHECK_POLICY_ACL_PROFILE_INDEX, True,
                                           "The given PID value is present for " +
                                           "access-list {list_name}.",
                                           "The given PID value is NOT present for " +
                                           "access-list {list_name}!",
                                           **kwargs)

    def policy_verify_state_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Verifies that the policy state is disabled.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_POLICY_STATE, False,
                                           "Policy state is disabled.",
                                           "Policy state is NOT disabled!",
                                           **kwargs)

    def policy_verify_port_admin_profile_does_not_exist(self, device_name, port='', profile_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [port]        - The port that should be applied to the admin profile.
        [profile_id]  - The profile ID that should be applied to the admin profile.
        """
        args = {"profile_id": profile_id,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADMIN_PROFILES,
                                           self.parse_const.CHECK_PORT_ADMIN_PROFILE, False,
                                           "The specified port admin-profile is not configured on {device_name}.",
                                           "The specified port admin-profile IS STILL configured on "
                                           "{device_name}!",
                                           **kwargs)

    def policy_verify_mac_source_admin_profile_does_not_exist(self, device_name, mac_addr='', port='', profile_id='',
                                                              mask="48", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [mac_addr]    - The MAC address that should be applied to the admin profile.
        [port]        - The port that should be applied to the admin profile.
        [profile_id]  - The profile ID that should be applied to the admin profile.
        """
        args = {"profile_id": profile_id,
                "mac_addr": mac_addr,
                "port": port,
                "mask": mask}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ADMIN_PROFILES,
                                           self.parse_const.CHECK_MAC_SOURCE_ADMIN_PROFILE, False,
                                           "The specified MAC source admin-profile is not configured on "
                                           "{device_name}.",
                                           "The specified MAC source admin-profile IS STILL configured on "
                                           "{device_name}!",
                                           **kwargs)

    def policy_verify_profile_does_not_exist(self, device_name, profile_ids='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [profile_ids] - The policy profile ID(s) that should not exist on the device.

        Verifies that the given policy profile ID is not configured on the device.
        """
        args = {"profile_id": profile_ids}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL_PROFILES,
                                           self.parse_const.CHECK_POLICY_PROFILE_EXISTS, False,
                                           "Policy Profile: {profile_id} does not exist on {device_name}.",
                                           "Policy Profile: {profile_id} EXISTS on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_application_does_not_exist(self, device_name, profile_id='', application='',
                                                      application_type='', mask='', port_string='', storage_type='',
                                                      vlan='', cos='', tci_overwrite='', mirror_destination='',
                                                      syslog='', trap='', disable_port='',
                                                      quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [application]         - The application the rule should be configure with.
        [application_type]    - The application type the rule should be configured with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "application": application,
                "application_type": application_type,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_APPLICATION, False,
                                           "Specified application policy rule does not exist on {device_name}.",
                                           "Specified application policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ethertype_does_not_exist(self, device_name, profile_id='', ether_type='', mask='',
                                                    port_string='', storage_type='', vlan='', cos='',
                                                    tci_overwrite='', mirror_destination='', syslog='',
                                                    trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ether_type]          - The ether type the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ether_type": ether_type,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_ETHER, False,
                                           "Specified ether policy rule does not exist on {device_name}.",
                                           "Specified ether policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_icmp6type_does_not_exist(self, device_name, profile_id='', icmp6_type='', icmp6_code='',
                                                    mask='', port_string='', storage_type='', vlan='', cos='',
                                                    tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                    disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [icmp6_type]          - The ICMPv6 type the rule should be configure with.
        [icmp6_code]          - The ICMPv6 code the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "icmp6_type": icmp6_type,
                "icmp6_code": icmp6_code,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_ICMP6TYPE, False,
                                           "Specified icmp6type policy rule does not exist on {device_name}.",
                                           "Specified icmp6type policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_icmptype_does_not_exist(self, device_name, profile_id='', icmp_type='', icmp_code='',
                                                   mask='', port_string='', storage_type='', vlan='', cos='',
                                                   tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                   disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [icmp_type]           - The ICMP type the rule should be configure with.
        [icmp_code]           - The ICMP code the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "icmp_type": icmp_type,
                "icmp_code": icmp_code,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_ICMPTYPE, True,
                                           "Specified icmptype policy rule does not exist on {device_name}.",
                                           "Specified icmptype policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ip6dest_does_not_exist(self, device_name, profile_id='', ipv6_addr='', l4_port='', mask='',
                                                  port_string='', storage_type='', vlan='', cos='',
                                                  tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                  disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipv6_addr]           - The IPv6 address the rule should be configure with.
        *[l4_port]            - The TCP/UDP port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipv6_addr": ipv6_addr,
                "l4_port": l4_port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IP6DEST, False,
                                           "Specified ip6dest policy rule does not exist on {device_name}.",
                                           "Specified ip6dest policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ip6flowlabel_does_not_exist(self, device_name, profile_id='', ipv6_flow_label='', mask='',
                                                       port_string='', storage_type='', vlan='', cos='',
                                                       tci_overwrite='', mirror_destination='', syslog='',
                                                       trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipv6_flow_label]     - The IPv6 flow label the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipv6_flow_label": ipv6_flow_label,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IP6FLOWLABEL, False,
                                           "Specified ip6flowlabel policy rule does not exist on {device_name}.",
                                           "Specified ip6flowlabel policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ip6source_does_not_exist(self, device_name, profile_id='', ipv6_addr='', l4_port='', mask='',
                                                    port_string='', storage_type='', vlan='', cos='',
                                                    tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                    disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipv6_addr]           - The IPv6 address the rule should be configure with.
        *[l4_port]            - The TCP/UDP port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipv6_addr": ipv6_addr,
                "l4_port": l4_port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IP6SOURCE, False,
                                           "Specified ip6source policy rule does not exist on {device_name}.",
                                           "Specified ip6source policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipdestsocket_does_not_exist(self, device_name, profile_id='', ip_addr='', l4_port='',
                                                       mask='', port_string='', storage_type='', vlan='', cos='',
                                                       tci_overwrite='', mirror_destination='', syslog='',
                                                       trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_addr]             - The IP address the rule should be configure with.
        *[l4_port]            - The TCP/UDP port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_addr": ip_addr,
                "l4_port": l4_port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPDESTSOCKET, False,
                                           "Specified ipdestsocket policy rule does not exist on {device_name}.",
                                           "Specified ipdestsocket policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipfrag_does_not_exist(self, device_name, profile_id='', mask='', port_string='',
                                                 storage_type='', vlan='', cos='', tci_overwrite='',
                                                 mirror_destination='', syslog='', trap='', disable_port='',
                                                 quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPFRAG, False,
                                           "Specified ipfrag policy rule does not exist on {device_name}.",
                                           "Specified ipfrag policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipproto_does_not_exist(self, device_name, profile_id='', ip_proto='', mask='',
                                                  port_string='', storage_type='', vlan='', cos='', tci_overwrite='',
                                                  mirror_destination='', syslog='', trap='', disable_port='',
                                                  quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_proto]            - The IP protocol value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_proto": ip_proto,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPPROTO, False,
                                           "Specified ipproto policy rule does not exist on {device_name}.",
                                           "Specified ipproto policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipsourcesocket_does_not_exist(self, device_name, profile_id='', ip_addr='', l4_port='',
                                                         mask='', port_string='', storage_type='', vlan='',
                                                         cos='', tci_overwrite='', mirror_destination='',
                                                         syslog='', trap='', disable_port='',
                                                         quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_addr]             - The IP address the rule should be configure with.
        *[l4_port]            - The TCP/UDP port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_addr": ip_addr,
                "l4_port": l4_port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPSOURCESOCKET, False,
                                           "Specified ipsourcesocket policy rule does not exist on "
                                           "{device_name}.",
                                           "Specified ipsourcesocket policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_iptos_does_not_exist(self, device_name, profile_id='', ip_tos='', mask='', port_string='',
                                                storage_type='', vlan='', cos='', tci_overwrite='',
                                                mirror_destination='', syslog='', trap='', disable_port='',
                                                quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_names]        - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_tos]              - The IP TOS value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_tos": ip_tos,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPTOS, False,
                                           "Specified iptos policy rule does not exist on {device_name}.",
                                           "Specified iptos policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipttl_does_not_exist(self, device_name, profile_id='', ip_ttl='', mask='', port_string='',
                                                storage_type='', vlan='', cos='', tci_overwrite='',
                                                mirror_destination='', syslog='', trap='', disable_port='',
                                                quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ip_ttl]              - The IP TTL value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ip_ttl": ip_ttl,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPTTL, False,
                                           "Specified ipttl policy rule does not exist on {device_name}.",
                                           "Specified ipttl policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxclass_does_not_exist(self, device_name, profile_id='', ipx_class='', mask='',
                                                   port_string='', storage_type='', vlan='', cos='',
                                                   tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                   disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_class]           - The IPX class value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_class": ipx_class,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXCLASS, False,
                                           "Specified ipxclass policy rule does not exist on {device_name}.",
                                           "Specified ipxclass policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxdest_does_not_exist(self, device_name, profile_id='', ipx_dest='', mask='',
                                                  port_string='', storage_type='', vlan='', cos='', tci_overwrite='',
                                                  mirror_destination='', syslog='', trap='', disable_port='',
                                                  quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_dest]            - The IPX destination address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_dest": ipx_dest,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXDEST, False,
                                           "Specified ipxdest policy rule does not exist on {device_name}.",
                                           "Specified ipxdest policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxdestsocket_does_not_exist(self, device_name, profile_id='', ipx_dest_socket='', mask='',
                                                        port_string='', storage_type='', vlan='', cos='',
                                                        tci_overwrite='', mirror_destination='', syslog='',
                                                        trap='', disable_port='', quarantine_profile='',
                                                        **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_dest_socket]     - The IPX destination socket the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_dest_socket": ipx_dest_socket,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXDESTSOCKET, False,
                                           "Specified ipxdestsocket policy rule does not exist on {device_name}.",
                                           "Specified ipxdestsocket policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxsource_does_not_exist(self, device_name, profile_id='', ipx_source='', mask='',
                                                    port_string='', storage_type='', vlan='', cos='',
                                                    tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                    disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_source]          - The IPX source address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_source": ipx_source,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXSOURCE, False,
                                           "Specified ipxsource policy rule does not exist on {device_name}.",
                                           "Specified ipxsource policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxsourcesocket_does_not_exist(self, device_name, profile_id='', ipx_source_socket='',
                                                          mask='', port_string='', storage_type='', vlan='', cos='',
                                                          tci_overwrite='', mirror_destination='', syslog='',
                                                          trap='', disable_port='', quarantine_profile='',
                                                          **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_source_socket]   - The IPX source socket the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_source_socket": ipx_source_socket,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXSOURCESOCKET, False,
                                           "Specified ipxsourcesocket policy rule does not exist on "
                                           "{device_name}.",
                                           "Specified ipxsourcesocket policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_ipxtype_does_not_exist(self, device_name, profile_id='', ipx_type='', mask='',
                                                  port_string='', storage_type='', vlan='', cos='', tci_overwrite='',
                                                  mirror_destination='', syslog='', trap='', disable_port='',
                                                  quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [ipx_type]            - The IPX type value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "ipx_type": ipx_type,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_IPXTYPE, False,
                                           "Specified ipxtype policy rule does not exist on {device_name}.",
                                           "Specified ipxtype policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_llcdsapssap_does_not_exist(self, device_name, profile_id='', llc_dsap_ssap='', mask='',
                                                      port_string='', storage_type='', vlan='', cos='',
                                                      tci_overwrite='', mirror_destination='', syslog='',
                                                      trap='', disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [llc_dsap_ssap]       - The LLC DSAP SSAP value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "llc_dsap_ssap": llc_dsap_ssap,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_LLCDSAPSSAP, False,
                                           "Specified llcdsapssap policy rule does not exist on {device_name}.",
                                           "Specified llcdsapssap policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_macdest_does_not_exist(self, device_name, profile_id='', mac_addr='', mask='',
                                                  port_string='', storage_type='', vlan='', cos='',
                                                  tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                  disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_names]        - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [mac_addr]            - The MAC address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "mac_addr": mac_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_MACDEST, False,
                                           "Specified macdest policy rule does not exist on {device_name}.",
                                           "Specified macdest policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_macsource_does_not_exist(self, device_name, profile_id='', mac_addr='', mask='',
                                                    port_string='', storage_type='', vlan='', cos='',
                                                    tci_overwrite='', mirror_destination='', syslog='', trap='',
                                                    disable_port='', quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [mac_addr]            - The MAC address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "mac_addr": mac_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_MACSOURCE, False,
                                           "Specified macsource policy rule does not exist on {device_name}.",
                                           "Specified macsource policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_port_does_not_exist(self, device_name, profile_id='', port='', mask='', port_string='',
                                               storage_type='', vlan='', cos='', tci_overwrite='',
                                               mirror_destination='', syslog='', trap='', disable_port='',
                                               quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [port]                - The port the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "port": port,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_PORT, False,
                                           "Specified port policy rule does not exist on {device_name}.",
                                           "Specified port policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_tci_does_not_exist(self, device_name, profile_id='', tci_value='', mask='', port_string='',
                                              storage_type='', vlan='', cos='', tci_overwrite='',
                                              mirror_destination='', syslog='', trap='', disable_port='',
                                              quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [tci_value]           - The tci value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "tci_value": tci_value,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_TCI, False,
                                           "Specified tci policy rule does not exist on {device_name}.",
                                           "Specified tci policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_tcpdestportip_does_not_exist(self, device_name, profile_id='', tcp_port='', ip_addr='',
                                                        mask='', port_string='', storage_type='', vlan='',
                                                        cos='', tci_overwrite='', mirror_destination='',
                                                        syslog='', trap='', disable_port='',
                                                        quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [tcp_port]            - The TCP destination port the rule should be configure with.
        *[ip_addr]            - The IPv4/IPv6 address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "tcp_port": tcp_port,
                "ip_addr": ip_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_TCPDESTPORTIP, False,
                                           "Specified tcpdestportIP policy rule does not exist on {device_name}.",
                                           "Specified tcpdestportIP policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_tcpsourceportip_does_not_exist(self, device_name, profile_id='', tcp_port='', ip_addr='',
                                                          mask='', port_string='', storage_type='', vlan='',
                                                          cos='', tci_overwrite='', mirror_destination='',
                                                          syslog='', trap='', disable_port='',
                                                          quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [tcp_port]            - The TCP destination port the rule should be configure with.
        *[ip_addr]            - The IPv4/IPv6 address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "tcp_port": tcp_port,
                "ip_addr": ip_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_TCPSOURCEPORTIP, False,
                                           "Specified tcpsourceportIP policy rule does not exist on "
                                           "{device_name}.",
                                           "Specified tcpsourceportIP policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_udpdestportip_does_not_exist(self, device_name, profile_id='', udp_port='', ip_addr='',
                                                        mask='', port_string='', storage_type='', vlan='',
                                                        cos='', tci_overwrite='', mirror_destination='',
                                                        syslog='', trap='', disable_port='',
                                                        quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [udp_port]            - The UDP destination port the rule should be configure with.
        *[ip_addr]            - The IPv4/IPv6 address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "udp_port": udp_port,
                "ip_addr": ip_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_UDPDESTPORTIP, False,
                                           "Specified udpdestportIP policy rule does not exist on {device_name}.",
                                           "Specified udpdestportIP policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_udpsourceportip_does_not_exist(self, device_name, profile_id='', udp_port='', ip_addr='',
                                                          mask='', port_string='', storage_type='', vlan='',
                                                          cos='', tci_overwrite='', mirror_destination='',
                                                          syslog='', trap='', disable_port='',
                                                          quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [udp_port]            - The TCP destination port the rule should be configure with.
        *[ip_addr]            - The IPv4/IPv6 address the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "udp_port": udp_port,
                "ip_addr": ip_addr,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_UDPSOURCEPORTIP, False,
                                           "Specified udpsourceportIP policy rule does not exist on "
                                           "{device_name}.",
                                           "Specified udpsourceportIP policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_rule_vlantag_does_not_exist(self, device_name, profile_id='', vlan_tag='', mask='',
                                                  port_string='', storage_type='', vlan='', cos='', tci_overwrite='',
                                                  mirror_destination='', syslog='', trap='', disable_port='',
                                                  quarantine_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name]         - The device the keyword should be run against.
        [profile_id]^         - The profile ID the rule should be configured on.
        [vlan_tag]            - The tci value the rule should be configure with.
        *[mask]               - The mask that should be applied to the rule.
        *[port_string]        - The port string that should be applied to the rule.
        *[storage_type]       - Where the rule should be stored. Valid options are "volatile" and "non-volatile".
        *[vlan]               - The vlan the rule should be configured with.
        *[cos]                - The COS value the rule should be configured with.
        *[tci_overwrite]      - The state tci overwrite should be configured with. Valid options are "enable",
                                "disable", and "prohibit".
        *[mirror_destination] - The mirror index that should be applied to the rule.
        *[syslog]             - The state syslog should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[trap]               - The state trap should be configured with. Valid options are "enable", "disable", and
                                "prohibit".
        *[disable_port]       - The state disable-port should be configured with. Valid options are "enable", "disable",
                                and "prohibit".
        *[quarantine_profile] - The quarantine profile index the rule should be configured with.

        * = Optional arguments.
        ^ = If <profile_id> is actually the profile name an additional argument, "profile_name=True" must be
        passed to the keyword

        Verifies that a rule with the specified configuration exists on the given policy profile.
        """
        args = {"profile_id": self.__get_profile_id_from_name(device_name, profile_id, kwargs),
                "vlan_tag": vlan_tag,
                "mask": mask,
                "port_string": port_string,
                "storage_type": storage_type,
                "vlan": vlan,
                "cos": cos,
                "tci_overwrite": tci_overwrite,
                "mirror_destination": mirror_destination,
                "syslog": syslog,
                "trap": trap,
                "disable_port": disable_port,
                "quarantine_profile": quarantine_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_RULES_PROFILE,
                                           self.parse_const.CHECK_POLICY_RULE_VLANTAG, False,
                                           "Specified vlantag policy rule does not exist on {device_name}.",
                                           "Specified vlantag policy rule DOES exist on {device_name}!",
                                           **kwargs)

    def policy_verify_acl_does_not_exist(self, device_name, list_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name] - The access list naming format of <list_name>

        Verifies that the given acl {list_name} does not exist.
        """
        args = {"list_name": list_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_LIST_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_DOES_NOT_EXIST, False,
                                           "The policy access list {list_name}" +
                                           "correctly does not exist.",
                                           "The policy access list {list_name}" +
                                           "INCORRECTLY EXISTS!", expect_error=True,
                                           **kwargs)

    def policy_verify_acl_rule_does_not_exist(self, device_name, list_name='', rule='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name] - The access list naming format of <list_name>
        [rule] - The access list specific rule

        Verifies that the given acl {list_name}.{rule} does not exist.
        """
        args = {"list_name": list_name,
                "rule": rule}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_RULE_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_RULE_DOES_NOT_EXIST, False,
                                           "The policy access list {list_name}.{rule} " +
                                           "correctly does not exist.",
                                           "The policy access list {list_name}.{rule} " +
                                           "INCORRECTLY EXISTS!", expect_error=True,
                                           **kwargs)

    def policy_verify_acl_action_set_does_not_exist(self, device_name, set_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [set_id] - The access list action-set id.

        Verifies that the given action-set {set_id} does not exist.
        """
        args = {"set_id": set_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_ACTION_SET,
                                           self.parse_const.CHECK_POLICY_ACL_ACTION_SET_DOES_NOT_EXIST, True,
                                           "The policy action-set {set_id} " +
                                           "correctly does not exist.",
                                           "The policy action-set {set_id} " +
                                           "INCORRECTLY EXISTS!", expect_error=True,
                                           **kwargs)

    def policy_verify_acl_profile_index_none(self, device_name, list_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [list_name] - The access list name

        Verifies that the given access-list does not have a PID value.
        """
        args = {"list_name": list_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ACCESS_LIST_LIST_NAME,
                                           self.parse_const.CHECK_POLICY_ACL_PROFILE_INDEX_NONE, True,
                                           "A PID value is not present for " +
                                           "access-list {list_name}.",
                                           "A PID value IS INCORRECTLY present for " +
                                           "access-list {list_name}!",
                                           **kwargs)

    def policy_verify_and_store_invalid_counter(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.

        Stores the policy invalid count.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_POLICY_INVALID_COUNT,
                                           self.parse_const.STORE_POLICY_INVALID_COUNTER, True,
                                           "Policy Invalid Count Stored.",
                                           "Could not resolve Policy Invalid Count!",
                                           **kwargs)

    # ##################################################################################################################
    #   Non-keyword helper functions   #################################################################################
    # ##################################################################################################################
    def __get_profile_id_from_name(self, device_name, profile_ids, kw_args):
        if StringUtils.string_to_boolean(kw_args.get("profile_name", False)):
            profile_ids = ListUtils.convert_to_list(profile_ids)

            profile_id_list = []
            for profile_id in profile_ids:
                dev, cmd_api, parse_api = self._init_keyword(device_name, self.api_const, self.api_const)
                cmd_obj = dev.send_command_object(cmd_api.show_all_policy_profiles(None))
                output = cmd_obj.return_text

                profile_id_list.append(parse_api.get_profile_id_from_name(output, profile_id))
            return profile_id_list
        else:
            return profile_ids
