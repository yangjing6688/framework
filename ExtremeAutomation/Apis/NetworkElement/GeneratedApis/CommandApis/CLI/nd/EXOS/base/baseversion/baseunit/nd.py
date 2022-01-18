"""
All nd supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.nd.base.ndbase import NdBase


class Nd(DeviceApi, NdBase):
    def __init__(self, device_input):
        super(Nd, self).__init__(device_input)

    def set_v6_neighbor(self, arg_dictionary, **kwargs):
        uuid = "ebb0dced-7ea7-47c8-b14b-40d357f3ec6a"
        cmd = "configure neighbor-discovery add {0} {1}".format(arg_dictionary['ipv6_addr'],
                                                                arg_dictionary['hw_addr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_v6_neighbor(self, arg_dictionary, **kwargs):
        uuid = "79d7c87e-effc-42e0-a1e0-70e0313bbbf7"
        cmd = "configure neighbor-discovery delete {0}".format(arg_dictionary['ipv6_addr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_table(self, arg_dictionary, **kwargs):
        uuid = "f054d52a-5be0-4259-9249-bf718dd595a0"
        cmd = "show neighbor-discovery cache"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
