"""
All vlan supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.vlan.base.vlanbase import VlanBase


class Vlan(DeviceApi, VlanBase):
    def __init__(self, device_input):
        super(Vlan, self).__init__(device_input)

    def delete_vlan(self, arg_dictionary, **kwargs):
        uuid = "eaccd886-b51c-409d-9daa-703133a964e5"
        cmd = "delete {0}".format(arg_dictionary['topology_name'])
        prompt = "topologyPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_vlan_with_name(self, arg_dictionary, **kwargs):
        uuid = "b86d2d18-f68a-4a9a-8ad1-1cdb08fe5b12"
        cmd = "create {0} {1} {2} {3}".format(arg_dictionary['topology_name'],
                                              arg_dictionary['mode'],
                                              arg_dictionary['vlan'],
                                              arg_dictionary['tag'])
        prompt = "topologyPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
