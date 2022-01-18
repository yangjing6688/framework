"""
All policy supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.policy.base.policybase import PolicyBase


class Policy(DeviceApi, PolicyBase):
    def __init__(self, device_input):
        super(Policy, self).__init__(device_input)

    def set_invalid(self, arg_dictionary, **kwargs):
        uuid = "cbba64d9-3e6c-4e38-a947-df6845f9dc8a"
        cmd = "set policy invalid action {0}".format(arg_dictionary['action'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_invalid(self, arg_dictionary, **kwargs):
        uuid = "c0534d4e-6503-4a62-92c8-60982adfafc0"
        cmd = "clear policy invalid action"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_admin_profile(self, arg_dictionary, **kwargs):
        uuid = "7cc7e155-0479-484c-96ec-a8588b67f12b"
        cmd = "set policy port {0} {1}".format(arg_dictionary['port'],
                                               arg_dictionary['admin_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port_admin_profile(self, arg_dictionary, **kwargs):
        uuid = "05bc86ba-7e7e-46e7-ad5d-01e6eb12d87a"
        cmd = "clear policy rule admin-profile port {0} port-string {1}".format(arg_dictionary['port'],
                                                                                arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mac_source_admin_profile(self, arg_dictionary, **kwargs):
        uuid = "1149cd7c-a45b-4d67-9a92-9b766b3be7a4"
        cmd = "set policy rule admin-profile macsource {0} mask {1} port-string {2} admin-pid {3}".format(arg_dictionary['mac_source'],
                                                                                                          arg_dictionary['mask'],
                                                                                                          arg_dictionary['port'],
                                                                                                          arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_mac_source_admin_profile(self, arg_dictionary, **kwargs):
        uuid = "4a52d2b0-4aa9-413e-81f8-8b5259a52e76"
        cmd = "clear policy rule admin-profile macsource {0} mask {1} port-string {2}".format(arg_dictionary['mac_source'],
                                                                                              arg_dictionary['mask'],
                                                                                              arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile(self, arg_dictionary, **kwargs):
        uuid = "186cd3f0-1c59-4c01-8d30-3469e618861d"
        cmd = "set policy profile {0}".format(arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_with_name(self, arg_dictionary, **kwargs):
        uuid = "a71c0e31-e2b3-4feb-b96e-409c4b70e2a8"
        cmd = "set policy profile {0} name {1}".format(arg_dictionary['profile_id'],
                                                       arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_profile(self, arg_dictionary, **kwargs):
        uuid = "1b24bfee-47d4-4044-9312-3a5f8306faf2"
        cmd = "clear policy profile {0}".format(arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_name(self, arg_dictionary, **kwargs):
        uuid = "8d888968-eb15-4d19-8b95-f841a428a8c0"
        cmd = "set policy profile {0} name {1}".format(arg_dictionary['profile_id'],
                                                       arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_pvid_status(self, arg_dictionary, **kwargs):
        uuid = "1fd26716-ee6f-4975-8341-0f128761bb42"
        cmd = "set policy profile {0} pvid-status {1}".format(arg_dictionary['profile_id'],
                                                              arg_dictionary['status'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_pvid(self, arg_dictionary, **kwargs):
        uuid = "8158885c-d39e-4179-8e32-fe37aaef85da"
        cmd = "set policy profile {0} pvid {1}".format(arg_dictionary['profile_id'],
                                                       arg_dictionary['pvid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_cos_status(self, arg_dictionary, **kwargs):
        uuid = "0e7ef673-36cd-4430-b44e-cef0ca3cfe5d"
        cmd = "set policy profile {0} cos-status {1}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['status'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_cos(self, arg_dictionary, **kwargs):
        uuid = "7ed1047d-4e70-4bf1-b876-8a528ae2d8ff"
        cmd = "set policy profile {0} cos {1}".format(arg_dictionary['profile_id'],
                                                      arg_dictionary['cos_value'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_egress_vlan(self, arg_dictionary, **kwargs):
        uuid = "2df5030d-a802-4114-afd5-9a8438b02dc5"
        cmd = "set policy profile {0} {1} egress-vlans {2}".format(arg_dictionary['profile_id'],
                                                                   self.api_utils.policy_vlan_append(arg_dictionary['append']),
                                                                   arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_untagged_vlan(self, arg_dictionary, **kwargs):
        uuid = "37000051-e9e9-413a-8181-77f833f36cef"
        cmd = "set policy profile {0} {1} untagged-vlans {2}".format(arg_dictionary['profile_id'],
                                                                     self.api_utils.policy_vlan_append(arg_dictionary['append']),
                                                                     arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_forbidden_vlan(self, arg_dictionary, **kwargs):
        uuid = "89b900e8-d445-4b48-8b0a-eb437c6cd184"
        cmd = "set policy profile {0} {1} forbidden-vlans {2}".format(arg_dictionary['profile_id'],
                                                                      self.api_utils.policy_vlan_append(arg_dictionary['append']),
                                                                      arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_tci_overwrite(self, arg_dictionary, **kwargs):
        uuid = "e5cc7a53-165c-4f27-83ba-f246fecb1a5e"
        cmd = "set policy profile {0} tci-overwrite {1}".format(arg_dictionary['profile_id'],
                                                                arg_dictionary['status'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_pvid_pvid_status(self, arg_dictionary, **kwargs):
        uuid = "53b7e3fe-5a56-4317-abfe-e0a3c34818e7"
        cmd = "set policy profile {0} pvid {1} pvid-status {2}".format(arg_dictionary['profile_id'],
                                                                       arg_dictionary['pvid'],
                                                                       arg_dictionary['pvid_status'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_untagged_pvid(self, arg_dictionary, **kwargs):
        uuid = "9dcd19b0-ae53-4265-9de1-b3969bc333b6"
        cmd = "set policy profile {0} pvid {1} pvid-status enable name {2} untagged-vlans {3}".format(arg_dictionary['profile_id'],
                                                                                                      arg_dictionary['pvid'],
                                                                                                      arg_dictionary['name'],
                                                                                                      arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule(self, arg_dictionary, **kwargs):
        uuid = "b6f4e66e-1598-4bf3-ad42-b0bf814bf9bd"
        cmd = "set policy rule {0} {1}".format(arg_dictionary['profile_id'],
                                               arg_dictionary['options'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_profile_rules(self, arg_dictionary, **kwargs):
        uuid = "197a5c36-bac9-44be-a484-be9ecb69bbdc"
        cmd = "clear policy rule {0} {1}".format(arg_dictionary['profile_id'],
                                                 arg_dictionary['options'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ether(self, arg_dictionary, **kwargs):
        uuid = "00dc62ac-48ee-43d1-9f2d-e641269cebb5"
        cmd = "set policy rule {0} ether {1} {2}".format(arg_dictionary['profile_id'],
                                                         arg_dictionary['ether_type'],
                                                         self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ether(self, arg_dictionary, **kwargs):
        uuid = "a3ed88d2-6bfe-4a37-ae66-9c6bc359d155"
        cmd = "clear policy rule {0} ether {1} {2}".format(arg_dictionary['profile_id'],
                                                           arg_dictionary['ether_type'],
                                                           self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ip6dest(self, arg_dictionary, **kwargs):
        uuid = "b5a88d8d-6553-49ca-a2cc-44f8bc78d0fa"
        cmd = "set policy rule {0} ip6dest {1} {2}".format(arg_dictionary['profile_id'],
                                                           self.api_utils.policy_gen_ip6dest(arg_dictionary['ipv6_addr'], arg_dictionary['l4_port']),
                                                           self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ip6dest(self, arg_dictionary, **kwargs):
        uuid = "3d40333e-8cd9-4412-877a-b1c6beca869a"
        cmd = "clear policy rule {0} ip6dest {1} {2}".format(arg_dictionary['profile_id'],
                                                             self.api_utils.policy_gen_ip6dest(arg_dictionary['ipv6_addr'], arg_dictionary['l4_port']),
                                                             self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipdestsocket(self, arg_dictionary, **kwargs):
        uuid = "5b33c2df-1b7a-45d1-a4b9-36dd408479b8"
        cmd = "set policy rule {0} ipdestsocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                self.api_utils.policy_gen_ipaddr(arg_dictionary['ip_addr'], arg_dictionary['l4_port']),
                                                                self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipdestsocket(self, arg_dictionary, **kwargs):
        uuid = "95004a55-e1c8-4123-8a49-ea9da45ffabb"
        cmd = "clear policy rule {0} ipdestsocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                  self.api_utils.policy_gen_ipaddr(arg_dictionary['ip_addr'], arg_dictionary['l4_port']),
                                                                  self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipfrag(self, arg_dictionary, **kwargs):
        uuid = "df5ee88d-f686-4f49-8e83-20717c03414d"
        cmd = "set policy rule {0} ipfrag {1}".format(arg_dictionary['profile_id'],
                                                      self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipfrag(self, arg_dictionary, **kwargs):
        uuid = "fb57fc23-5306-453b-89ec-d01784c26e26"
        cmd = "clear policy rule {0} ipfrag {1}".format(arg_dictionary['profile_id'],
                                                        self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipproto(self, arg_dictionary, **kwargs):
        uuid = "b121e22f-f39a-4d29-9f27-24e52b0a34b0"
        cmd = "set policy rule {0} ipproto {1} {2}".format(arg_dictionary['profile_id'],
                                                           arg_dictionary['ipproto'],
                                                           self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipproto(self, arg_dictionary, **kwargs):
        uuid = "21ef32cc-449c-4473-9393-c90bf90fd5df"
        cmd = "clear policy rule {0} ipproto {1} {2}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['ip_proto'],
                                                             self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipsourcesocket(self, arg_dictionary, **kwargs):
        uuid = "47f84da2-31b0-4995-93cd-719fd56f9d95"
        cmd = "set policy rule {0} ipsourcesocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                  self.api_utils.policy_gen_ipaddr(arg_dictionary['ip_addr'], arg_dictionary['l4_port']),
                                                                  self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipsourcesocket(self, arg_dictionary, **kwargs):
        uuid = "241d9ba8-b923-4685-bd9f-505489d1e170"
        cmd = "clear policy rule {0} ipsourcesocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                    self.api_utils.policy_gen_ipaddr(arg_dictionary['ip_addr'], arg_dictionary['l4_port']),
                                                                    self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_iptos(self, arg_dictionary, **kwargs):
        uuid = "498b751e-4e40-4fcf-9244-b62c85106bad"
        cmd = "set policy rule {0} iptos {1} {2}".format(arg_dictionary['profile_id'],
                                                         arg_dictionary['ip_tos'],
                                                         self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_iptos(self, arg_dictionary, **kwargs):
        uuid = "7ea42f76-f9d4-4eac-9f7d-c802d411dbde"
        cmd = "clear policy rule {0} iptos {1} {2}".format(arg_dictionary['profile_id'],
                                                           arg_dictionary['ip_tos'],
                                                           self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipttl(self, arg_dictionary, **kwargs):
        uuid = "15845486-fd51-4719-9681-962616403401"
        cmd = "set policy rule {0} ipttl {1} {2}".format(arg_dictionary['profile_id'],
                                                         arg_dictionary['ip_ttl'],
                                                         self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipttl(self, arg_dictionary, **kwargs):
        uuid = "4565ecf5-cca2-4804-9135-f7c13485cb58"
        cmd = "clear policy rule {0} ipttl {1} {2}".format(arg_dictionary['profile_id'],
                                                           arg_dictionary['ip_ttl'],
                                                           self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_macdest(self, arg_dictionary, **kwargs):
        uuid = "fcf4e5b4-cb65-4e83-96b1-652749767595"
        cmd = "set policy rule {0} macdest {1} {2}".format(arg_dictionary['profile_id'],
                                                           arg_dictionary['mac_addr'],
                                                           self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_macdest(self, arg_dictionary, **kwargs):
        uuid = "48e3bcd5-d239-444a-b804-0e1a80a99d08"
        cmd = "clear policy rule {0} macdest {1} {2}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['mac_addr'],
                                                             self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_macsource(self, arg_dictionary, **kwargs):
        uuid = "05ed08cb-7843-4ce5-9402-e291469a6dac"
        cmd = "set policy rule {0} macsource {1} {2}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['mac_addr'],
                                                             self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_macsource(self, arg_dictionary, **kwargs):
        uuid = "6fa3f836-0f78-45c2-8f62-389d722b0ec5"
        cmd = "clear policy rule {0} macsource {1} {2}".format(arg_dictionary['profile_id'],
                                                               arg_dictionary['mac_addr'],
                                                               self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_port(self, arg_dictionary, **kwargs):
        uuid = "c6d16f77-2d5a-4ccb-9f92-5c4ae88b1202"
        cmd = "set policy rule {0} port {1} {2}".format(arg_dictionary['profile_id'],
                                                        arg_dictionary['port'],
                                                        self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_port(self, arg_dictionary, **kwargs):
        uuid = "a3327bbf-b5a3-4f1e-9325-2a1ddb65138f"
        cmd = "clear policy rule {0} port {1} {2}".format(arg_dictionary['profile_id'],
                                                          arg_dictionary['port'],
                                                          self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_tcpdestportip(self, arg_dictionary, **kwargs):
        uuid = "a3e4238e-1a35-4ce9-88cb-85e04170e482"
        cmd = "set policy rule {0} tcpdestportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                 self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['tcp_port']),
                                                                 self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_tcpdestportip(self, arg_dictionary, **kwargs):
        uuid = "6e3721c8-8645-4899-b746-0e1d5f802195"
        cmd = "clear policy rule {0} tcpdestportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                   self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['tcp_port']),
                                                                   self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_tcpsourceportip(self, arg_dictionary, **kwargs):
        uuid = "a6f55f48-6dc0-4d77-97b4-172bf186e911"
        cmd = "set policy rule {0} tcpsourceportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                   self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['tcp_port']),
                                                                   self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_tcpsourceportip(self, arg_dictionary, **kwargs):
        uuid = "3b1c1584-9a85-4269-9e55-efac096723c4"
        cmd = "clear policy rule {0} tcpsourceportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                     self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['tcp_port']),
                                                                     self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_udpdestportip(self, arg_dictionary, **kwargs):
        uuid = "4449ead8-29c0-42bc-9634-4892b72c5fcd"
        cmd = "set policy rule {0} udpdestportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                 self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['udp_port']),
                                                                 self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_udpdestportip(self, arg_dictionary, **kwargs):
        uuid = "9c0a29d3-d851-4261-bbf7-4a81135446e8"
        cmd = "clear policy rule {0} udpdestportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                   self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['udp_port']),
                                                                   self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_udpsourceportip(self, arg_dictionary, **kwargs):
        uuid = "35f5ab4b-f5d1-4bc4-be7a-7117ab47c080"
        cmd = "set policy rule {0} udpsourceportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                   self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['udp_port']),
                                                                   self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_udpsourceportip(self, arg_dictionary, **kwargs):
        uuid = "0ecb0b61-132c-412d-8321-0e15d66aec58"
        cmd = "clear policy rule {0} udpsourceportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                     self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['udp_port']),
                                                                     self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_maptable_response(self, arg_dictionary, **kwargs):
        uuid = "efe56dda-2ecc-4a1c-a6d3-27254842e983"
        cmd = "set policy maptable response {0}".format(arg_dictionary['type'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_maptable_response(self, arg_dictionary, **kwargs):
        uuid = "68d2ad8d-f98f-4aa4-a719-6ca6c8774171"
        cmd = "clear policy maptable response"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_rules(self, arg_dictionary, **kwargs):
        uuid = "538e5ddc-e2c8-4bd3-86bc-a1fb99a3af21"
        cmd = "clear policy all-rules"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_precedence(self, arg_dictionary, **kwargs):
        uuid = "bfd3bd78-7c3e-41f2-8e26-c1fd2435d5a5"
        cmd = "set policy profile {0} precedence {1}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['precedence'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_mirror_dest(self, arg_dictionary, **kwargs):
        uuid = "07de7f4b-c431-4105-8da7-84a787c2bd12"
        cmd = "set policy profile {0} mirror-destination {1}".format(arg_dictionary['profile_id'],
                                                                     arg_dictionary['index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_syslog(self, arg_dictionary, **kwargs):
        uuid = "5a3fac57-847b-4e3a-9dee-0f86709ab8b7"
        cmd = "set policy profile {0} syslog {1}".format(arg_dictionary['profile_id'],
                                                         arg_dictionary['state'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_trap(self, arg_dictionary, **kwargs):
        uuid = "256457b7-0d33-4d4a-9fa1-592345de38f6"
        cmd = "set policy profile {0} trap {1}".format(arg_dictionary['profile_id'],
                                                       arg_dictionary['state'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_disable_port(self, arg_dictionary, **kwargs):
        uuid = "cf1aa1f0-1a6a-4a6f-bd64-eabb89fc654f"
        cmd = "set policy profile {0} disable-port {1}".format(arg_dictionary['profile_id'],
                                                               arg_dictionary['state'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_fst(self, arg_dictionary, **kwargs):
        uuid = "090f879d-7414-42f3-a552-27e15126c02f"
        cmd = "set policy profile {0} fst {1}".format(arg_dictionary['profile_id'],
                                                      arg_dictionary['index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_web_redirect(self, arg_dictionary, **kwargs):
        uuid = "d7557d56-5435-4ded-9d24-ca6fadbe08a2"
        cmd = "set policy profile {0} web-redirect {1}".format(arg_dictionary['profile_id'],
                                                               arg_dictionary['index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_application(self, arg_dictionary, **kwargs):
        uuid = "fa524d81-170b-44fc-9c88-9e8c378f7f52"
        cmd = "set policy rule {0} application {1} {2} {3}".format(arg_dictionary['profile_id'],
                                                                   arg_dictionary['application'],
                                                                   arg_dictionary['application_type'],
                                                                   self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_application(self, arg_dictionary, **kwargs):
        uuid = "fdcd9819-07d0-4da2-a8b2-d79c0ac2f0a8"
        cmd = "clear policy rule {0} application {1} {2} {3}".format(arg_dictionary['profile_id'],
                                                                     arg_dictionary['application'],
                                                                     arg_dictionary['application_type'],
                                                                     self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_icmp6type(self, arg_dictionary, **kwargs):
        uuid = "fcba0959-7643-460b-b132-16d2dde35319"
        cmd = "set policy rule {0} icmp6type {1} {2}".format(arg_dictionary['profile_id'],
                                                             self.api_utils.policy_gen_icmp6(arg_dictionary['icmp6type'], arg_dictionary['icmp6code']),
                                                             self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_icmp6type(self, arg_dictionary, **kwargs):
        uuid = "c239e306-7d15-4611-826a-7fd38a731cf5"
        cmd = "clear policy rule {0} icmp6type {1} {2}".format(arg_dictionary['profile_id'],
                                                               self.api_utils.policy_gen_icmp6(arg_dictionary['icmp6_type'], arg_dictionary['icmp6_code']),
                                                               self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_icmptype(self, arg_dictionary, **kwargs):
        uuid = "5e4ea557-4950-4b71-9c20-3a43a0e3849f"
        cmd = "set policy rule {0} icmptype {1} {2}".format(arg_dictionary['profile_id'],
                                                            self.api_utils.policy_gen_icmp(arg_dictionary['icmptype'], arg_dictionary['icmpcode']),
                                                            self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_icmptype(self, arg_dictionary, **kwargs):
        uuid = "af5fb0c8-8285-470a-a1ee-e5d6d440df6a"
        cmd = "clear policy rule {0} icmptype {1} {2}".format(arg_dictionary['profile_id'],
                                                              self.api_utils.policy_gen_icmp(arg_dictionary['icmp_type'], arg_dictionary['icmp_code']),
                                                              self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ip6flowlabel(self, arg_dictionary, **kwargs):
        uuid = "e5f1c36b-bcfe-4b13-b5f5-0d1a3308cbc2"
        cmd = "set policy rule {0} ip6flowlabel {1} {2}".format(arg_dictionary['profile_id'],
                                                                arg_dictionary['ip6_flow_label'],
                                                                self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ip6flowlabel(self, arg_dictionary, **kwargs):
        uuid = "a2174339-6b3a-4367-b2cd-2e5ba72fdfe1"
        cmd = "clear policy rule {0} ip6flowlabel {1} {2}".format(arg_dictionary['profile_id'],
                                                                  arg_dictionary['ip6_flow_label'],
                                                                  self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ip6source(self, arg_dictionary, **kwargs):
        uuid = "f4d89a0e-8b2e-4a07-862a-0238bd2febf5"
        cmd = "set policy rule {0} ip6source {1} {2}".format(arg_dictionary['profile_id'],
                                                             self.api_utils.policy_gen_ip6dest(arg_dictionary['ipv6_addr'], arg_dictionary['l4_port']),
                                                             self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ip6source(self, arg_dictionary, **kwargs):
        uuid = "16d20f97-556f-479d-8922-b363fc3cb3bc"
        cmd = "clear policy rule {0} ip6source {1} {2}".format(arg_dictionary['profile_id'],
                                                               self.api_utils.policy_gen_ip6dest(arg_dictionary['ipv6_addr'], arg_dictionary['l4_port']),
                                                               self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipxclass(self, arg_dictionary, **kwargs):
        uuid = "4b7cbdc4-4522-4214-886c-b1185512998b"
        cmd = "set policy rule {0} ipxclass {1} {2}".format(arg_dictionary['profile_id'],
                                                            arg_dictionary['ipx_class'],
                                                            self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipxclass(self, arg_dictionary, **kwargs):
        uuid = "fa631379-9c32-4060-9807-25ea93ab4e4b"
        cmd = "clear policy rule {0} ipxclass {1} {2}".format(arg_dictionary['profile_id'],
                                                              arg_dictionary['ipx_class'],
                                                              self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipxdest(self, arg_dictionary, **kwargs):
        uuid = "75179bad-bb77-4bdf-97ab-56fd5531dc77"
        cmd = "set policy rule {0} ipxdest {1} {2}".format(arg_dictionary['profile_id'],
                                                           arg_dictionary['ipx_addr'],
                                                           self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipxdest(self, arg_dictionary, **kwargs):
        uuid = "a2e72025-0ee1-41f2-a9ec-a30943fba1b0"
        cmd = "clear policy rule {0} ipxdest {1} {2}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['ipx_addr'],
                                                             self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipxdestsocket(self, arg_dictionary, **kwargs):
        uuid = "01db00e6-9b07-4690-97eb-596c4e92aab2"
        cmd = "set policy rule {0} ipxdestsocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                 arg_dictionary['ipx_socket'],
                                                                 self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipxdestsocket(self, arg_dictionary, **kwargs):
        uuid = "9d3118bd-1002-4b7e-a815-b28d4bc033cd"
        cmd = "clear policy rule {0} ipxdestsocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                   arg_dictionary['ipx_socket'],
                                                                   self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipxsource(self, arg_dictionary, **kwargs):
        uuid = "914b0351-2b35-4cc4-8c9a-dcbe13b583a9"
        cmd = "set policy rule {0} ipxsource {1} {2}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['ipx_addr'],
                                                             self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipxsource(self, arg_dictionary, **kwargs):
        uuid = "db18ee58-e235-491d-b8e0-af78803c07c4"
        cmd = "clear policy rule {0} ipxsource {1} {2}".format(arg_dictionary['profile_id'],
                                                               arg_dictionary['ipx_addr'],
                                                               self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipxsourcesocket(self, arg_dictionary, **kwargs):
        uuid = "32b8a6af-574e-4faf-940e-b9db30ea15cc"
        cmd = "set policy rule {0} ipxsourcesocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                   arg_dictionary['ipx_socket'],
                                                                   self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipxsourcesocket(self, arg_dictionary, **kwargs):
        uuid = "e1518406-93ab-4025-8efa-197939be68cb"
        cmd = "clear policy rule {0} ipxsourcesocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                     arg_dictionary['ipx_socket'],
                                                                     self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipxtype(self, arg_dictionary, **kwargs):
        uuid = "34f0dd2c-57f4-43b6-a197-73d41a65126a"
        cmd = "set policy rule {0} ipxtype {1} {2}".format(arg_dictionary['profile_id'],
                                                           arg_dictionary['ipx_type'],
                                                           self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipxtype(self, arg_dictionary, **kwargs):
        uuid = "c22d7e0a-2425-4f69-9db4-27ca2ae8cf1e"
        cmd = "clear policy rule {0} ipxtype {1} {2}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['ipx_type'],
                                                             self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_llcdsapssap(self, arg_dictionary, **kwargs):
        uuid = "82a219b6-f9e3-48e0-a2d8-1b3cafd60a7e"
        cmd = "set policy rule {0} llcdsapssap {1} {2}".format(arg_dictionary['profile_id'],
                                                               arg_dictionary['llc_dsap_ssap'],
                                                               self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_llcdsapssap(self, arg_dictionary, **kwargs):
        uuid = "a4d02d47-eb78-4854-89b0-16508161dc20"
        cmd = "clear policy rule {0} llcdsapssap {1} {2}".format(arg_dictionary['profile_id'],
                                                                 arg_dictionary['llc_dsap_ssap'],
                                                                 self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_tci(self, arg_dictionary, **kwargs):
        uuid = "b7bc6b10-59f5-4a0e-bafd-383c4d46e78b"
        cmd = "set policy rule {0} tci {1} {2}".format(arg_dictionary['profile_id'],
                                                       arg_dictionary['tci_value'],
                                                       self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_tci(self, arg_dictionary, **kwargs):
        uuid = "1ebdd8b3-53a0-4840-bfdd-908d8462d991"
        cmd = "clear policy rule {0} tci {1} {2}".format(arg_dictionary['profile_id'],
                                                         arg_dictionary['tci_value'],
                                                         self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_vlantag(self, arg_dictionary, **kwargs):
        uuid = "e9ea7542-fb2c-48d5-86b5-26f5a6f70e1f"
        cmd = "set policy rule {0} vlantag {1} {2}".format(arg_dictionary['profile_id'],
                                                           arg_dictionary['vlan_tag'],
                                                           self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_vlantag(self, arg_dictionary, **kwargs):
        uuid = "5b5e373a-6d75-4e62-87fc-99cdbe34b1d7"
        cmd = "clear policy rule {0} vlantag {1} {2}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['vlan_tag'],
                                                             self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_map_response(self, arg_dictionary, **kwargs):
        uuid = "81343f8f-b126-4181-9d3e-53dfc8070538"
        cmd = "show policy maptable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_profiles(self, arg_dictionary, **kwargs):
        uuid = "ee409148-6d7f-40cc-9ad6-33c490e4744b"
        cmd = "show policy profile -verbose"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rules(self, arg_dictionary, **kwargs):
        uuid = "e6c422c4-8307-4b49-800c-693b86ad4819"
        cmd = "show policy rule {0} -verbose".format(arg_dictionary['rule_type'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_invalid_action(self, arg_dictionary, **kwargs):
        uuid = "fb37f6cd-aa15-400c-b47b-6f1cf02e71c1"
        cmd = "show policy invalid action"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_allow_type(self, arg_dictionary, **kwargs):
        uuid = "f09ee2b9-6d5c-40bd-8d6d-a2cb1ca2940f"
        cmd = "show policy allowed-type {0} -verbose".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_rules(self, arg_dictionary, **kwargs):
        uuid = "1fbc44c3-7b05-4234-b056-fc3bc876feeb"
        cmd = "show policy rule -verbose"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_profiles(self, arg_dictionary, **kwargs):
        uuid = "4cc7973d-623a-4ba9-a48a-3963adc44854"
        cmd = "show policy profile -verbose"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rules_profile(self, arg_dictionary, **kwargs):
        uuid = "5e757112-dbf2-46f6-98d3-c97d3966fcbe"
        cmd = "show policy rule {0} -verbose".format(arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_admin_profiles(self, arg_dictionary, **kwargs):
        uuid = "35c5144b-815e-46b3-a13f-f07fee9e3557"
        cmd = "show policy rule admin-pid {0} -verbose".format(arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
