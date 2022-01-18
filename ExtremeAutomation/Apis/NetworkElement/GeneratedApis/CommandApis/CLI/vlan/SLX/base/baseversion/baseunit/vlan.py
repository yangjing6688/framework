"""
All vlan supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.vlan.base.vlanbase import VlanBase


class Vlan(DeviceApi, VlanBase):
    def __init__(self, device_input):
        super(Vlan, self).__init__(device_input)

    def create_vlan(self, arg_dictionary, **kwargs):
        uuid = "2e07dc6a-2f52-4bdd-b814-6a3fd6afc666"
        cmd = "vlan {0}||exit".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_vlan(self, arg_dictionary, **kwargs):
        uuid = "eaccd886-b51c-409d-9daa-703133a964e5"
        cmd = "no vlan {0}".format(arg_dictionary['vlan'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_egress_untagged(self, arg_dictionary, **kwargs):
        uuid = "1455236d-3899-476e-a333-93fcff7ed6ad"
        cmd = "switchport||switchport mode trunk||switchport trunk allowed vlan add {0}||switchport trunk native-vlan {1}||no switchport trunk tag native-vlan".format(arg_dictionary['vlan'],
                                                                                                                                                                       arg_dictionary['vlan'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_egress_tagged(self, arg_dictionary, **kwargs):
        uuid = "8fb45945-51d5-43b8-b469-84d4cfc3f546"
        cmd = "switchport||switchport mode trunk||switchport trunk allowed vlan add {0}".format(arg_dictionary['vlan'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_egress(self, arg_dictionary, **kwargs):
        uuid = "aaca0f2c-01a7-48d1-8b68-f113d9711a23"
        cmd = "switchport trunk allowed vlan remove {0}".format(arg_dictionary['vlan'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_description(self, arg_dictionary, **kwargs):
        uuid = "5e31f606-0a42-473b-906e-651b1fdabebc"
        cmd = "vlan {0}||description \"{1}\"||exit".format(arg_dictionary['vlan'],
                                                           arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_name(self, arg_dictionary, **kwargs):
        uuid = "b5132db1-ed57-4b19-a129-13bf3cf6efbe"
        cmd = "vlan {0}||name \"{1}\"||exit".format(arg_dictionary['vlan'],
                                                    arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_pvid(self, arg_dictionary, **kwargs):
        uuid = "b4477fa8-5f9e-449e-bc9f-c88a87add7b6"
        cmd = "switchport trunk native-vlan {0}".format(arg_dictionary['vlan'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_pvid(self, arg_dictionary, **kwargs):
        uuid = "04479df7-6ad7-4db6-8410-9bda5e8458d9"
        cmd = "no switchport trunk native-vlan {0}".format(arg_dictionary['vlan'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_all_info(self, arg_dictionary, **kwargs):
        uuid = "665c60ed-ab31-4ccd-9b85-7946db3c01a3"
        cmd = "show vlan brief"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "62cb48f8-848b-4604-a67b-5e135a96d45a"
        cmd = "show vlan detail {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_name(self, arg_dictionary, **kwargs):
        uuid = "48cf27a1-71fd-4212-85a3-12db4d2f899d"
        cmd = "show vlan detail {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
