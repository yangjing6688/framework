"""
All vrrp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.vrrp.base.vrrpbase import VrrpBase


class Vrrp(DeviceApi, VrrpBase):
    def __init__(self, device_input):
        super(Vrrp, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "c223e23c-297b-49fe-9326-77ddc3aa2697"
        cmd = "enable vrrp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "a5e2343b-bd31-4eb9-ad6d-4859df19b1ed"
        cmd = "disable vrrp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "ebb63174-a777-4bf0-81ba-feaee1d47d0a"
        cmd = "enable vrrp vlan {0} vrid {1}".format(arg_dictionary['vlan'],
                                                     arg_dictionary['vrid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "ef0bb4d4-408a-4fdd-a5f8-70749a0f4f6e"
        cmd = "disable vrrp vlan {0} vrid {1}".format(arg_dictionary['vlan'],
                                                      arg_dictionary['vrid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_vlan_fabric_routing(self, arg_dictionary, **kwargs):
        uuid = "1aea17a3-64f3-4174-9c57-46944575a884"
        cmd = "configure vrrp vlan {0} vrid {1} fabric-routing on".format(arg_dictionary['vlan'],
                                                                          arg_dictionary['vrid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan_fabric_routing(self, arg_dictionary, **kwargs):
        uuid = "cd972247-68b0-4348-8f34-fa286fd19cc5"
        cmd = "configure vrrp vlan {0} vrid {1} fabric-routing off".format(arg_dictionary['vlan'],
                                                                           arg_dictionary['vrid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_vlan(self, arg_dictionary, **kwargs):
        uuid = "95df1aca-795a-4b87-b1d4-a6bd1fafd49b"
        cmd = "create vrrp vlan {0} vrid {1}".format(arg_dictionary['vlan'],
                                                     arg_dictionary['vrid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_vlan(self, arg_dictionary, **kwargs):
        uuid = "0d2169e2-7c17-4e23-ae3e-127676e1370e"
        cmd = "delete vrrp vlan {0} vrid {1}".format(arg_dictionary['vlan'],
                                                     arg_dictionary['vrid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_group(self, arg_dictionary, **kwargs):
        uuid = "5a97b9ae-459b-4920-ad52-0e0022067e98"
        cmd = "create vrrp group {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_group(self, arg_dictionary, **kwargs):
        uuid = "5aaeb0e1-bfbf-47fd-b007-34a5ba7abb4c"
        cmd = "delete vrrp group {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vlan_priority(self, arg_dictionary, **kwargs):
        uuid = "6eba5c94-5f6a-4618-b15b-b1fd8780050d"
        cmd = "configure vrrp vlan {0} vrid {1} priority {2}".format(arg_dictionary['vlan'],
                                                                     arg_dictionary['vrid'],
                                                                     arg_dictionary['priority'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vlan_ipaddress(self, arg_dictionary, **kwargs):
        uuid = "059235e6-51ad-4ccf-a7c8-6d9d704244ef"
        cmd = "configure vrrp vlan {0} vrid {1} add {2}".format(arg_dictionary['vlan'],
                                                                arg_dictionary['vrid'],
                                                                arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all(self, arg_dictionary, **kwargs):
        uuid = "2fbb4647-b867-4879-bf9f-2396a31f2f26"
        cmd = "show vrrp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_detail(self, arg_dictionary, **kwargs):
        uuid = "e0e5da77-7d20-4f32-bcb0-098d7d8738d1"
        cmd = "show vrrp detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_group(self, arg_dictionary, **kwargs):
        uuid = "30b95afc-6bb0-4b95-a010-98512a2f240f"
        cmd = "show vrrp group {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_group_all(self, arg_dictionary, **kwargs):
        uuid = "d6566d08-8827-4deb-9854-b0385e36eb25"
        cmd = "show vrrp group"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_virtual_router(self, arg_dictionary, **kwargs):
        uuid = "e7fa2cb7-bf6a-4545-9f3e-7ff0213ef03b"
        cmd = "show vrrp virtual-router {0}".format(arg_dictionary['vr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_virtual_router_all(self, arg_dictionary, **kwargs):
        uuid = "6b1813fa-e46c-41a6-b598-3e95b2843322"
        cmd = "show vrrp virtual-router"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vr(self, arg_dictionary, **kwargs):
        uuid = "f4a84284-c695-4d6f-ac5e-6ec621e73fa9"
        cmd = "show vrrp vr {0}".format(arg_dictionary['vr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vr_all(self, arg_dictionary, **kwargs):
        uuid = "8c5cfc15-1800-42e6-8b4d-ffd299d703f8"
        cmd = "show vrrp vr"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan(self, arg_dictionary, **kwargs):
        uuid = "4940f28d-6bef-432d-9160-a29a28c80b07"
        cmd = "show vrrp vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
