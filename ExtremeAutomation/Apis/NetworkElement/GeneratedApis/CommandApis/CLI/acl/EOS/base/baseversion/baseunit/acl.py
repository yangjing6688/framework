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
        cmd = "ip access-list {0} {1}|| exit".format(arg_dictionary['acl_type'],
                                                     arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_ipv6(self, arg_dictionary, **kwargs):
        uuid = "8d98c3b6-3c38-41de-bbb9-7665d4fac2b0"
        cmd = "ipv6 access-list {0} {1}|| exit".format(arg_dictionary['acl_type'],
                                                       arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_list(self, arg_dictionary, **kwargs):
        uuid = "3d235e88-a2c4-4f09-961c-98f0600ef260"
        cmd = "no {0} access-list {1} {2}".format(arg_dictionary['ip_ver'],
                                                  arg_dictionary['acl_type'],
                                                  arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_standard_rule(self, arg_dictionary, **kwargs):
        uuid = "fda50222-0089-4331-b760-a0be89989052"
        cmd = "{0} access-list {1} {2}|| {3} {4}|| exit".format(arg_dictionary['ip_ver'],
                                                                arg_dictionary['acl_type'],
                                                                arg_dictionary['name'],
                                                                arg_dictionary['rule_type'],
                                                                arg_dictionary['rule_info'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_ipv4(self, arg_dictionary, **kwargs):
        uuid = "3bf3b522-5128-49dc-b9e0-1f8c898a6997"
        cmd = "show access-lists ipv4"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_ipv6(self, arg_dictionary, **kwargs):
        uuid = "3a10087e-a30e-4768-9451-07ae5f5c4a5d"
        cmd = "show access-lists ipv6"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
