"""
All vxlan supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.vxlan.base.vxlanbase import VxlanBase


class Vxlan(DeviceApi, VxlanBase):
    def __init__(self, device_input):
        super(Vxlan, self).__init__(device_input)

    def create_logical_switch(self, arg_dictionary, **kwargs):
        uuid = "49ef7ff1-d0e9-413e-94e5-b70d34b9fb39"
        cmd = "set tunnel logical-switch create name {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_logical_switch(self, arg_dictionary, **kwargs):
        uuid = "54da38b2-c9e7-4491-9394-2b20965d3a25"
        cmd = "clear tunnel logical-switch name {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_logical_switch_to_vni_map(self, arg_dictionary, **kwargs):
        uuid = "9314a29d-4bc0-467a-a64e-be6a87d2314d"
        cmd = "set tunnel map logical-switch {0} keyword {1}".format(arg_dictionary['name'],
                                                                     arg_dictionary['vni'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_logical_switch_to_vlan_map(self, arg_dictionary, **kwargs):
        uuid = "cccd83dc-7199-466c-9d60-b2dfcc80bc2e"
        cmd = "set tunnel map logical-switch {0} vlan {1}".format(arg_dictionary['name'],
                                                                  arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_logical_switch_vni_vlan_map(self, arg_dictionary, **kwargs):
        uuid = "68836667-af69-476d-b61c-9b89159eb618"
        cmd = "set tunnel map logical-switch {0} keyword {1} vlan {2}".format(arg_dictionary['name'],
                                                                              arg_dictionary['vni'],
                                                                              arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_remote_vtep(self, arg_dictionary, **kwargs):
        uuid = "103d42de-427b-4ab8-9ceb-efba0c3080df"
        cmd = "set tunnel remote-vtep logical-switch {0} ip-address {1}".format(arg_dictionary['name'],
                                                                                arg_dictionary['ip_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_remote_vtep(self, arg_dictionary, **kwargs):
        uuid = "c3a92a89-a07e-4647-8249-c73cf068ea7a"
        cmd = "clear tunnel remote-vtep logical-switch {0}".format(arg_dictionary['name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_logical_switch(self, arg_dictionary, **kwargs):
        uuid = "72f20dde-4018-43bc-96da-b490c6f11605"
        cmd = "show tunnel logical-switch"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
