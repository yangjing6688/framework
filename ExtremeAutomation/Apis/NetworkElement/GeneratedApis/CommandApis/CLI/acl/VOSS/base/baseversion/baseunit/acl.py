"""
All acl supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.acl.base.aclbase import AclBase


class Acl(DeviceApi, AclBase):
    def __init__(self, device_input):
        super(Acl, self).__init__(device_input)

    def create_ipv4(self, arg_dictionary, **kwargs):
        uuid = "46cc1e09-b77a-48f3-b471-b0460b965a05"
        cmd = "filter acl {0} type {1} name {2}".format(arg_dictionary['acl_id'],
                                                        arg_dictionary['voss_acl_type'],
                                                        arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_ipv6(self, arg_dictionary, **kwargs):
        uuid = "8d98c3b6-3c38-41de-bbb9-7665d4fac2b0"
        cmd = "filter acl {0} type {1} name {2} pktType ipv6".format(arg_dictionary['acl_id'],
                                                                     arg_dictionary['voss_acl_type'],
                                                                     arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_list(self, arg_dictionary, **kwargs):
        uuid = "3d235e88-a2c4-4f09-961c-98f0600ef260"
        cmd = "no filter acl {0}".format(arg_dictionary['acl_id'])
        prompt = "routerConfigPrompt"
        conf = "Do you wish to delete this ACL? (y/n) ?"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def create_ace_index(self, arg_dictionary, **kwargs):
        uuid = "91b19841-d175-4715-ad5e-762434c6dd5d"
        cmd = "filter acl ace {0} {1} name {2}".format(arg_dictionary['acl_id'],
                                                       arg_dictionary['ace_index'],
                                                       arg_dictionary['ace_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_ace_index(self, arg_dictionary, **kwargs):
        uuid = "ca55a68a-e092-4462-aaf9-42ce02793795"
        cmd = "no filter acl ace {0} {1}".format(arg_dictionary['acl_id'],
                                                 arg_dictionary['ace_index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_list(self, arg_dictionary, **kwargs):
        uuid = "57cd5339-9aa3-4b16-aa0d-a71ca66ace9b"
        cmd = "filter acl {0} enable".format(arg_dictionary['acl_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_list(self, arg_dictionary, **kwargs):
        uuid = "71c6c544-fa88-4dfa-be7b-4e87198e029b"
        cmd = "no filter acl {0} enable".format(arg_dictionary['acl_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ace(self, arg_dictionary, **kwargs):
        uuid = "40e17139-f478-436f-bd1f-e7b7e251d857"
        cmd = "filter acl ace {0} {1} enable".format(arg_dictionary['acl_id'],
                                                     arg_dictionary['ace_index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ace(self, arg_dictionary, **kwargs):
        uuid = "40e579c3-0a1b-4785-bb42-0f0a7930cf04"
        cmd = "no filter acl ace {0} {1} enable".format(arg_dictionary['acl_id'],
                                                        arg_dictionary['ace_index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_name(self, arg_dictionary, **kwargs):
        uuid = "aa86a026-8284-4fd1-97ce-9be9826d4c30"
        cmd = "filter acl {0} name {1}".format(arg_dictionary['acl_id'],
                                               arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_default_action(self, arg_dictionary, **kwargs):
        uuid = "54ea9fc0-1ca1-476f-94a2-dfa4525a4bf7"
        cmd = "filter acl set {0} default-action {1}".format(arg_dictionary['acl_id'],
                                                             arg_dictionary['action'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port(self, arg_dictionary, **kwargs):
        uuid = "0a1fae24-2a56-4607-ab8e-108277703e4f"
        cmd = "filter acl port {0} {1}".format(arg_dictionary['acl_id'],
                                               arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port(self, arg_dictionary, **kwargs):
        uuid = "ecc0cb15-cdbb-4731-84fd-f54bef2a7c4b"
        cmd = "no filter acl port {0} {1}".format(arg_dictionary['acl_id'],
                                                  arg_dictionary['port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vlan(self, arg_dictionary, **kwargs):
        uuid = "6c9f011e-c993-455b-a448-1fd505c3f1b0"
        cmd = "filter acl vlan {0} {1}".format(arg_dictionary['acl_id'],
                                               arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_vlan(self, arg_dictionary, **kwargs):
        uuid = "cf9d5686-2128-4a94-8eb8-d45aebd55127"
        cmd = "no filter acl vlan {0} {1}".format(arg_dictionary['acl_id'],
                                                  arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ace_action(self, arg_dictionary, **kwargs):
        uuid = "57b9120e-fe78-4259-803c-c5596a9e132e"
        cmd = "filter acl ace action {0} {1} {2}".format(arg_dictionary['acl_id'],
                                                         arg_dictionary['ace_index'],
                                                         arg_dictionary['ace_action'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ace_name(self, arg_dictionary, **kwargs):
        uuid = "60841625-fe68-45df-807c-962bac8724ac"
        cmd = "filter acl ace {0} {1} name {2}".format(arg_dictionary['acl_id'],
                                                       arg_dictionary['ace_index'],
                                                       arg_dictionary['ace_name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_ace_ethernet_ethertype(self, arg_dictionary, **kwargs):
        uuid = "ce925b7f-3e77-40cf-91de-6d09c99de6cd"
        cmd = "filter acl ace ethernet {0} {1} ether-type eq {2}".format(arg_dictionary['acl_id'],
                                                                         arg_dictionary['ace_index'],
                                                                         arg_dictionary['ace_ethertype'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_ace_ethernet_ethertype(self, arg_dictionary, **kwargs):
        uuid = "3505b71e-e11c-4f18-9560-077cbd35dac8"
        cmd = "no filter acl ace ethernet {0} {1} ether-type".format(arg_dictionary['acl_id'],
                                                                     arg_dictionary['ace_index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_ipv4(self, arg_dictionary, **kwargs):
        uuid = "3bf3b522-5128-49dc-b9e0-1f8c898a6997"
        cmd = "show filter acl"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_ipv6(self, arg_dictionary, **kwargs):
        uuid = "3a10087e-a30e-4768-9451-07ae5f5c4a5d"
        cmd = "show filter acl"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ports(self, arg_dictionary, **kwargs):
        uuid = "8ffd0e0a-27f8-4aae-aff8-988189718390"
        cmd = "show filter acl {0}".format(arg_dictionary['acl_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlans(self, arg_dictionary, **kwargs):
        uuid = "1b7c9dbf-948a-4482-9476-ab6e0b7620ae"
        cmd = "show filter acl {0}".format(arg_dictionary['acl_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_aces(self, arg_dictionary, **kwargs):
        uuid = "cc442231-d3ef-4813-8135-9b3528e5243e"
        cmd = "show filter acl ace"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_id(self, arg_dictionary, **kwargs):
        uuid = "86174dbc-da63-4687-8a6c-065231c22f52"
        cmd = "show filter acl {0}".format(arg_dictionary['acl_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ace_index_oper_state(self, arg_dictionary, **kwargs):
        uuid = "ed267470-b73c-4648-88f9-d9579132f515"
        cmd = "show filter acl action {0} {1}".format(arg_dictionary['acl_id'],
                                                      arg_dictionary['ace_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ace_index_name(self, arg_dictionary, **kwargs):
        uuid = "85617c4f-fd3c-4c2a-a0ec-9b7e8ff97a57"
        cmd = "show filter acl action {0} {1}".format(arg_dictionary['acl_id'],
                                                      arg_dictionary['ace_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ace_index_action(self, arg_dictionary, **kwargs):
        uuid = "afa282b5-06e2-4ef0-977e-855ae59cf46a"
        cmd = "show filter acl action {0} {1}".format(arg_dictionary['acl_id'],
                                                      arg_dictionary['ace_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ace_index_ethernet_ethertype(self, arg_dictionary, **kwargs):
        uuid = "9d06dd23-427d-4539-9ca9-589a7b72382f"
        cmd = "show filter acl ethernet {0} {1}".format(arg_dictionary['acl_id'],
                                                        arg_dictionary['ace_index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
