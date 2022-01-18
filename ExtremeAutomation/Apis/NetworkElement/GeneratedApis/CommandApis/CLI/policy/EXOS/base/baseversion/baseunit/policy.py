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
        cmd = "configure policy invalid action {0}".format(arg_dictionary['action'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_invalid(self, arg_dictionary, **kwargs):
        uuid = "c0534d4e-6503-4a62-92c8-60982adfafc0"
        cmd = "unconfigure policy invalid action"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_admin_profile(self, arg_dictionary, **kwargs):
        uuid = "7cc7e155-0479-484c-96ec-a8588b67f12b"
        cmd = "configure policy port {0} admin-id {1}".format(arg_dictionary['port'],
                                                              arg_dictionary['admin_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port_admin_profile(self, arg_dictionary, **kwargs):
        uuid = "05bc86ba-7e7e-46e7-ad5d-01e6eb12d87a"
        cmd = "unconfigure policy rule admin-profile port {0} port-string {1}".format(arg_dictionary['port'],
                                                                                      arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mac_source_admin_profile(self, arg_dictionary, **kwargs):
        uuid = "1149cd7c-a45b-4d67-9a92-9b766b3be7a4"
        cmd = "configure policy rule admin-profile macsource {0} mask {1} port-string {2} admin-pid {3}".format(arg_dictionary['mac_source'],
                                                                                                                arg_dictionary['mask'],
                                                                                                                arg_dictionary['port'],
                                                                                                                arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_mac_source_admin_profile(self, arg_dictionary, **kwargs):
        uuid = "4a52d2b0-4aa9-413e-81f8-8b5259a52e76"
        cmd = "unconfigure policy rule admin-profile macsource {0} mask {1} port-string {2}".format(arg_dictionary['mac_source'],
                                                                                                    arg_dictionary['mask'],
                                                                                                    arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile(self, arg_dictionary, **kwargs):
        uuid = "186cd3f0-1c59-4c01-8d30-3469e618861d"
        cmd = "configure policy profile {0}".format(arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_with_name(self, arg_dictionary, **kwargs):
        uuid = "a71c0e31-e2b3-4feb-b96e-409c4b70e2a8"
        cmd = "configure policy profile {0} name {1}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_profile(self, arg_dictionary, **kwargs):
        uuid = "1b24bfee-47d4-4044-9312-3a5f8306faf2"
        cmd = "unconfigure policy profile {0}".format(arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_name(self, arg_dictionary, **kwargs):
        uuid = "8d888968-eb15-4d19-8b95-f841a428a8c0"
        cmd = "configure policy profile {0} name {1}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_pvid_status(self, arg_dictionary, **kwargs):
        uuid = "1fd26716-ee6f-4975-8341-0f128761bb42"
        cmd = "configure policy profile {0} pvid-status {1}".format(arg_dictionary['profile_id'],
                                                                    arg_dictionary['status'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_pvid(self, arg_dictionary, **kwargs):
        uuid = "8158885c-d39e-4179-8e32-fe37aaef85da"
        cmd = "configure policy profile {0} pvid {1}".format(arg_dictionary['profile_id'],
                                                             arg_dictionary['pvid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_cos_status(self, arg_dictionary, **kwargs):
        uuid = "0e7ef673-36cd-4430-b44e-cef0ca3cfe5d"
        cmd = "configure policy profile {0} cos-status {1}".format(arg_dictionary['profile_id'],
                                                                   arg_dictionary['status'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_cos(self, arg_dictionary, **kwargs):
        uuid = "7ed1047d-4e70-4bf1-b876-8a528ae2d8ff"
        cmd = "configure policy profile {0} cos {1}".format(arg_dictionary['profile_id'],
                                                            arg_dictionary['cos_value'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_egress_vlan(self, arg_dictionary, **kwargs):
        uuid = "2df5030d-a802-4114-afd5-9a8438b02dc5"
        cmd = "configure policy profile {0} {1} egress-vlans {2}".format(arg_dictionary['profile_id'],
                                                                         self.api_utils.policy_vlan_append(arg_dictionary['append']),
                                                                         arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_untagged_vlan(self, arg_dictionary, **kwargs):
        uuid = "37000051-e9e9-413a-8181-77f833f36cef"
        cmd = "configure policy profile {0} {1} untagged-vlans {2}".format(arg_dictionary['profile_id'],
                                                                           self.api_utils.policy_vlan_append(arg_dictionary['append']),
                                                                           arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_forbidden_vlan(self, arg_dictionary, **kwargs):
        uuid = "89b900e8-d445-4b48-8b0a-eb437c6cd184"
        cmd = "configure policy profile {0} {1} forbidden-vlans {2}".format(arg_dictionary['profile_id'],
                                                                            self.api_utils.policy_vlan_append(arg_dictionary['append']),
                                                                            arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_tci_overwrite(self, arg_dictionary, **kwargs):
        uuid = "e5cc7a53-165c-4f27-83ba-f246fecb1a5e"
        cmd = "configure policy profile {0} tci-overwrite {1}".format(arg_dictionary['profile_id'],
                                                                      arg_dictionary['status'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_pvid_pvid_status(self, arg_dictionary, **kwargs):
        uuid = "53b7e3fe-5a56-4317-abfe-e0a3c34818e7"
        cmd = "configure policy profile {0} pvid {1} pvid-status {2}".format(arg_dictionary['profile_id'],
                                                                             arg_dictionary['pvid'],
                                                                             arg_dictionary['pvid_status'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_untagged_pvid(self, arg_dictionary, **kwargs):
        uuid = "9dcd19b0-ae53-4265-9de1-b3969bc333b6"
        cmd = "configure policy profile {0} pvid {1} pvid-status enable name {2} untagged-vlans {3}".format(arg_dictionary['profile_id'],
                                                                                                            arg_dictionary['pvid'],
                                                                                                            arg_dictionary['name'],
                                                                                                            arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule(self, arg_dictionary, **kwargs):
        uuid = "b6f4e66e-1598-4bf3-ad42-b0bf814bf9bd"
        cmd = "configure policy rule {0} {1}".format(arg_dictionary['profile_id'],
                                                     arg_dictionary['options'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_profile_rules(self, arg_dictionary, **kwargs):
        uuid = "197a5c36-bac9-44be-a484-be9ecb69bbdc"
        cmd = "unconfigure policy rule {0} {1}".format(arg_dictionary['profile_id'],
                                                       arg_dictionary['options'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ether(self, arg_dictionary, **kwargs):
        uuid = "00dc62ac-48ee-43d1-9f2d-e641269cebb5"
        cmd = "configure policy rule {0} ether {1} {2}".format(arg_dictionary['profile_id'],
                                                               arg_dictionary['ether_type'],
                                                               self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ether(self, arg_dictionary, **kwargs):
        uuid = "a3ed88d2-6bfe-4a37-ae66-9c6bc359d155"
        cmd = "unconfigure policy rule {0} ether {1} {2}".format(arg_dictionary['profile_id'],
                                                                 arg_dictionary['ether_type'],
                                                                 self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ip6dest(self, arg_dictionary, **kwargs):
        uuid = "b5a88d8d-6553-49ca-a2cc-44f8bc78d0fa"
        cmd = "configure policy rule {0} ip6dest {1} {2}".format(arg_dictionary['profile_id'],
                                                                 self.api_utils.policy_gen_ip6dest(arg_dictionary['ipv6_addr'], arg_dictionary['l4_port']),
                                                                 self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ip6dest(self, arg_dictionary, **kwargs):
        uuid = "3d40333e-8cd9-4412-877a-b1c6beca869a"
        cmd = "unconfigure policy rule {0} ip6dest {1} {2}".format(arg_dictionary['profile_id'],
                                                                   self.api_utils.policy_gen_ip6dest(arg_dictionary['ipv6_addr'], arg_dictionary['l4_port']),
                                                                   self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipdestsocket(self, arg_dictionary, **kwargs):
        uuid = "5b33c2df-1b7a-45d1-a4b9-36dd408479b8"
        cmd = "configure policy rule {0} ipdestsocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                      self.api_utils.policy_gen_ipaddr(arg_dictionary['ip_addr'], arg_dictionary['l4_port']),
                                                                      self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipdestsocket(self, arg_dictionary, **kwargs):
        uuid = "95004a55-e1c8-4123-8a49-ea9da45ffabb"
        cmd = "unconfigure policy rule {0} ipdestsocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                        self.api_utils.policy_gen_ipaddr(arg_dictionary['ip_addr'], arg_dictionary['l4_port']),
                                                                        self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipfrag(self, arg_dictionary, **kwargs):
        uuid = "df5ee88d-f686-4f49-8e83-20717c03414d"
        cmd = "configure policy rule {0} ipfrag {1}".format(arg_dictionary['profile_id'],
                                                            self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipfrag(self, arg_dictionary, **kwargs):
        uuid = "fb57fc23-5306-453b-89ec-d01784c26e26"
        cmd = "unconfigure policy rule {0} ipfrag {1}".format(arg_dictionary['profile_id'],
                                                              self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipproto(self, arg_dictionary, **kwargs):
        uuid = "b121e22f-f39a-4d29-9f27-24e52b0a34b0"
        cmd = "configure policy rule {0} ipproto {1} {2}".format(arg_dictionary['profile_id'],
                                                                 arg_dictionary['ipproto'],
                                                                 self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipproto(self, arg_dictionary, **kwargs):
        uuid = "21ef32cc-449c-4473-9393-c90bf90fd5df"
        cmd = "unconfigure policy rule {0} ipproto {1} {2}".format(arg_dictionary['profile_id'],
                                                                   arg_dictionary['ip_proto'],
                                                                   self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipsourcesocket(self, arg_dictionary, **kwargs):
        uuid = "47f84da2-31b0-4995-93cd-719fd56f9d95"
        cmd = "configure policy rule {0} ipsourcesocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                        self.api_utils.policy_gen_ipaddr(arg_dictionary['ip_addr'], arg_dictionary['l4_port']),
                                                                        self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipsourcesocket(self, arg_dictionary, **kwargs):
        uuid = "241d9ba8-b923-4685-bd9f-505489d1e170"
        cmd = "unconfigure policy rule {0} ipsourcesocket {1} {2}".format(arg_dictionary['profile_id'],
                                                                          self.api_utils.policy_gen_ipaddr(arg_dictionary['ip_addr'], arg_dictionary['l4_port']),
                                                                          self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_iptos(self, arg_dictionary, **kwargs):
        uuid = "498b751e-4e40-4fcf-9244-b62c85106bad"
        cmd = "configure policy rule {0} iptos {1} {2}".format(arg_dictionary['profile_id'],
                                                               arg_dictionary['ip_tos'],
                                                               self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_iptos(self, arg_dictionary, **kwargs):
        uuid = "7ea42f76-f9d4-4eac-9f7d-c802d411dbde"
        cmd = "unconfigure policy rule {0} iptos {1} {2}".format(arg_dictionary['profile_id'],
                                                                 arg_dictionary['ip_tos'],
                                                                 self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_ipttl(self, arg_dictionary, **kwargs):
        uuid = "15845486-fd51-4719-9681-962616403401"
        cmd = "configure policy rule {0} ipttl {1} {2}".format(arg_dictionary['profile_id'],
                                                               arg_dictionary['ip_ttl'],
                                                               self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_ipttl(self, arg_dictionary, **kwargs):
        uuid = "4565ecf5-cca2-4804-9135-f7c13485cb58"
        cmd = "unconfigure policy rule {0} ipttl {1} {2}".format(arg_dictionary['profile_id'],
                                                                 arg_dictionary['ip_ttl'],
                                                                 self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_macdest(self, arg_dictionary, **kwargs):
        uuid = "fcf4e5b4-cb65-4e83-96b1-652749767595"
        cmd = "configure policy rule {0} macdest {1} {2}".format(arg_dictionary['profile_id'],
                                                                 arg_dictionary['mac_addr'],
                                                                 self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_macdest(self, arg_dictionary, **kwargs):
        uuid = "48e3bcd5-d239-444a-b804-0e1a80a99d08"
        cmd = "unconfigure policy rule {0} macdest {1} {2}".format(arg_dictionary['profile_id'],
                                                                   arg_dictionary['mac_addr'],
                                                                   self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_macsource(self, arg_dictionary, **kwargs):
        uuid = "05ed08cb-7843-4ce5-9402-e291469a6dac"
        cmd = "configure policy rule {0} macsource {1} {2}".format(arg_dictionary['profile_id'],
                                                                   arg_dictionary['mac_addr'],
                                                                   self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_macsource(self, arg_dictionary, **kwargs):
        uuid = "6fa3f836-0f78-45c2-8f62-389d722b0ec5"
        cmd = "unconfigure policy rule {0} macsource {1} {2}".format(arg_dictionary['profile_id'],
                                                                     arg_dictionary['mac_addr'],
                                                                     self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_port(self, arg_dictionary, **kwargs):
        uuid = "c6d16f77-2d5a-4ccb-9f92-5c4ae88b1202"
        cmd = "configure policy rule {0} port {1} {2}".format(arg_dictionary['profile_id'],
                                                              arg_dictionary['port'],
                                                              self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_port(self, arg_dictionary, **kwargs):
        uuid = "a3327bbf-b5a3-4f1e-9325-2a1ddb65138f"
        cmd = "unconfigure policy rule {0} port {1} {2}".format(arg_dictionary['profile_id'],
                                                                arg_dictionary['port'],
                                                                self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_tcpdestportip(self, arg_dictionary, **kwargs):
        uuid = "a3e4238e-1a35-4ce9-88cb-85e04170e482"
        cmd = "configure policy rule {0} tcpdestportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                       self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['tcp_port']),
                                                                       self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_tcpdestportip(self, arg_dictionary, **kwargs):
        uuid = "6e3721c8-8645-4899-b746-0e1d5f802195"
        cmd = "unconfigure policy rule {0} tcpdestportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                         self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['tcp_port']),
                                                                         self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_tcpsourceportip(self, arg_dictionary, **kwargs):
        uuid = "a6f55f48-6dc0-4d77-97b4-172bf186e911"
        cmd = "configure policy rule {0} tcpsourceportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                         self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['tcp_port']),
                                                                         self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_tcpsourceportip(self, arg_dictionary, **kwargs):
        uuid = "3b1c1584-9a85-4269-9e55-efac096723c4"
        cmd = "unconfigure policy rule {0} tcpsourceportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                           self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['tcp_port']),
                                                                           self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_udpdestportip(self, arg_dictionary, **kwargs):
        uuid = "4449ead8-29c0-42bc-9634-4892b72c5fcd"
        cmd = "configure policy rule {0} udpdestportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                       self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['udp_port']),
                                                                       self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_udpdestportip(self, arg_dictionary, **kwargs):
        uuid = "9c0a29d3-d851-4261-bbf7-4a81135446e8"
        cmd = "unconfigure policy rule {0} udpdestportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                         self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['udp_port']),
                                                                         self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_udpsourceportip(self, arg_dictionary, **kwargs):
        uuid = "35f5ab4b-f5d1-4bc4-be7a-7117ab47c080"
        cmd = "configure policy rule {0} udpsourceportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                         self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['udp_port']),
                                                                         self.api_utils.policy_gen_rule(arg_dictionary['mask'], arg_dictionary['port_string'], arg_dictionary['storage_type'], arg_dictionary['vlan'], arg_dictionary['forward'], arg_dictionary['drop'], arg_dictionary['cos'], arg_dictionary['tci_overwrite'], arg_dictionary['mirror_destination'], arg_dictionary['syslog'], arg_dictionary['trap'], arg_dictionary['disable_port'], arg_dictionary['quarantine_profile']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_rule_udpsourceportip(self, arg_dictionary, **kwargs):
        uuid = "0ecb0b61-132c-412d-8321-0e15d66aec58"
        cmd = "unconfigure policy rule {0} udpsourceportip {1} {2}".format(arg_dictionary['profile_id'],
                                                                           self.api_utils.policy_gen_tcpip(arg_dictionary['ip_addr'], arg_dictionary['udp_port']),
                                                                           self.api_utils.policy_gen_rule_del(arg_dictionary['mask'], arg_dictionary['port_string']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_maptable_response(self, arg_dictionary, **kwargs):
        uuid = "efe56dda-2ecc-4a1c-a6d3-27254842e983"
        cmd = "configure policy maptable response {0}".format(arg_dictionary['type'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_maptable_response(self, arg_dictionary, **kwargs):
        uuid = "68d2ad8d-f98f-4aa4-a719-6ca6c8774171"
        cmd = "unconfigure policy maptable response"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable(self, arg_dictionary, **kwargs):
        uuid = "cda4d3d3-1e02-414c-8393-c8c81595f704"
        cmd = "enable policy"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable(self, arg_dictionary, **kwargs):
        uuid = "14033106-dd6a-4742-be0f-95de4284cf08"
        cmd = "disable policy"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vlanauthorization_state(self, arg_dictionary, **kwargs):
        uuid = "448045af-54a7-4217-8f8a-4aa53175f84e"
        cmd = "configure policy vlanauthorization {0}".format(arg_dictionary['state'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_rule_model_access_list(self, arg_dictionary, **kwargs):
        uuid = "e2a1fab3-273f-42d2-b308-281ce103a7f9"
        cmd = "configure policy rule-model access-list"
        prompt = "userPrompt"
        conf = "Do you really want to delete these rules?"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_rule_model_hierarchical(self, arg_dictionary, **kwargs):
        uuid = "20b65c48-acde-4718-b040-58a11ba07cf5"
        cmd = "configure policy rule-model hierarchical"
        prompt = "userPrompt"
        conf = "Do you really want to delete these rules?"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_access_list_profile_index(self, arg_dictionary, **kwargs):
        uuid = "96c9961e-89b9-453c-87a6-9c9a004605e6"
        cmd = "configure policy profile {0} access-list {1}".format(arg_dictionary['profile_index'],
                                                                    arg_dictionary['list_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_list_profile_none(self, arg_dictionary, **kwargs):
        uuid = "71c4267e-2880-4fc4-bf2c-ea659db1fd3f"
        cmd = "configure policy profile {0} access-list unassigned".format(arg_dictionary['profile_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_list_profile_highest(self, arg_dictionary, **kwargs):
        uuid = "30f0c730-1e43-4881-826a-2747adf81774"
        cmd = "configure policy access-list profile highest-priority {0}.{1}".format(arg_dictionary['list_name'],
                                                                                     arg_dictionary['rule'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_list_profile_lowest(self, arg_dictionary, **kwargs):
        uuid = "72a0ee34-e3ba-4769-81bd-9c6033ca4cc1"
        cmd = "configure policy access-list profile lowest-priority {0}.{1}".format(arg_dictionary['list_name'],
                                                                                    arg_dictionary['rule'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_list_rule_precedence_first(self, arg_dictionary, **kwargs):
        uuid = "e8082c13-8eca-4c72-89e9-0384ddd5e305"
        cmd = "configure policy access-list rule-precedence {0}.{1} first".format(arg_dictionary['list_name'],
                                                                                  arg_dictionary['rule'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_list_rule_precedence_last(self, arg_dictionary, **kwargs):
        uuid = "1c35d07c-08f3-4c16-8019-9c3faf18127c"
        cmd = "configure policy access-list rule-precedence {0}.{1} last".format(arg_dictionary['list_name'],
                                                                                 arg_dictionary['rule'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_list_rule_precedence_before(self, arg_dictionary, **kwargs):
        uuid = "5d2737f3-d279-48bf-b6c4-410c40864a09"
        cmd = "configure policy access-list rule-precedence {0}.{1} before {2}.{3}".format(arg_dictionary['list1'],
                                                                                           arg_dictionary['rule1'],
                                                                                           arg_dictionary['list2'],
                                                                                           arg_dictionary['rule2'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_list_rule_precedence_after(self, arg_dictionary, **kwargs):
        uuid = "9026dadf-fad9-4e16-894f-e55ad622d846"
        cmd = "configure policy access-list rule-precedence {0}.{1} after {2}.{3}".format(arg_dictionary['list1'],
                                                                                          arg_dictionary['rule1'],
                                                                                          arg_dictionary['list2'],
                                                                                          arg_dictionary['rule2'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_list(self, arg_dictionary, **kwargs):
        uuid = "1600e48f-bf9d-41cc-8168-6d1ba5587828"
        cmd = "create policy access-list {0}.{1} matches {2} actions {3}".format(arg_dictionary['list_name'],
                                                                                 arg_dictionary['rule'],
                                                                                 arg_dictionary['match_string'],
                                                                                 arg_dictionary['action_string'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_access_list_action_set(self, arg_dictionary, **kwargs):
        uuid = "efe6da8e-03d5-4654-8f8e-977a977510a8"
        cmd = "create policy access-list action-set {0} {1}".format(arg_dictionary['set_id'],
                                                                    arg_dictionary['action_string'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_rules(self, arg_dictionary, **kwargs):
        uuid = "538e5ddc-e2c8-4bd3-86bc-a1fb99a3af21"
        cmd = "unconfigure policy all-rules"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_access_list_all(self, arg_dictionary, **kwargs):
        uuid = "f16dcda3-7d22-4283-b09b-7402f8d1a03f"
        cmd = "delete policy access-list all-rules"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_access_list(self, arg_dictionary, **kwargs):
        uuid = "303ccc7d-9d3a-4fde-9337-319683debd11"
        cmd = "delete policy access-list {0}".format(arg_dictionary['list_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_access_list_rule(self, arg_dictionary, **kwargs):
        uuid = "b7e80862-0e5e-4b80-b36e-8d276741a77f"
        cmd = "delete policy access-list {0}.{1}".format(arg_dictionary['list_name'],
                                                         arg_dictionary['rule'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_access_list_action_set(self, arg_dictionary, **kwargs):
        uuid = "ea3a4263-84d0-4e40-bff2-5cd51b294741"
        cmd = "delete policy access-list action-set {0}".format(arg_dictionary['set_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "871fd84a-db46-4ea5-931c-e4f4859c97d6"
        cmd = "show policy state"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_map_response(self, arg_dictionary, **kwargs):
        uuid = "81343f8f-b126-4181-9d3e-53dfc8070538"
        cmd = "show policy maptable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_profiles(self, arg_dictionary, **kwargs):
        uuid = "ee409148-6d7f-40cc-9ad6-33c490e4744b"
        cmd = "show policy profile detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_profile(self, arg_dictionary, **kwargs):
        uuid = "f4cc3445-c7d6-4131-9f3f-58f5aceb62c8"
        cmd = "show policy profile {0}".format(arg_dictionary['profile_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rules(self, arg_dictionary, **kwargs):
        uuid = "e6c422c4-8307-4b49-800c-693b86ad4819"
        cmd = "show policy rule {0} detail".format(arg_dictionary['rule_type'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_invalid_action(self, arg_dictionary, **kwargs):
        uuid = "fb37f6cd-aa15-400c-b47b-6f1cf02e71c1"
        cmd = "show policy invalid action"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlanauthorization(self, arg_dictionary, **kwargs):
        uuid = "fc6bd614-b5b7-4624-ad95-62e32311bdee"
        cmd = "show policy vlanauthorization"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_allow_type(self, arg_dictionary, **kwargs):
        uuid = "f09ee2b9-6d5c-40bd-8d6d-a2cb1ca2940f"
        cmd = "show policy allowed-type {0} detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_rules(self, arg_dictionary, **kwargs):
        uuid = "1fbc44c3-7b05-4234-b056-fc3bc876feeb"
        cmd = "show policy rule detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_profiles(self, arg_dictionary, **kwargs):
        uuid = "4cc7973d-623a-4ba9-a48a-3963adc44854"
        cmd = "show policy profile detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rules_profile(self, arg_dictionary, **kwargs):
        uuid = "5e757112-dbf2-46f6-98d3-c97d3966fcbe"
        cmd = "show policy rule profile-index {0} detail".format(arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_invalid_count(self, arg_dictionary, **kwargs):
        uuid = "4042d414-f795-40fe-ba31-5215c68b748b"
        cmd = "show policy invalid count"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_admin_profiles(self, arg_dictionary, **kwargs):
        uuid = "35c5144b-815e-46b3-a13f-f07fee9e3557"
        cmd = "show policy rule admin-pid {0} detail".format(arg_dictionary['profile_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_access_list_rule_name(self, arg_dictionary, **kwargs):
        uuid = "352acacf-6fdb-4070-a7e3-0ef8baef9294"
        cmd = "show policy access-list {0}.{1}".format(arg_dictionary['list_name'],
                                                       arg_dictionary['rule'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_access_list_list_name(self, arg_dictionary, **kwargs):
        uuid = "e5d08279-b58c-4b2f-9941-bec2c5f6bb66"
        cmd = "show policy access-list {0}".format(arg_dictionary['list_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_access_list_action_set(self, arg_dictionary, **kwargs):
        uuid = "7d55818b-8301-4ef1-9574-0e6626056b81"
        cmd = "show policy access-list action-set {0}".format(arg_dictionary['set_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
