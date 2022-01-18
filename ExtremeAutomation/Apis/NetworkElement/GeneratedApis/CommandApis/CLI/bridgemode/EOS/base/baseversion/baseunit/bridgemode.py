"""
All bridgemode supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.bridgemode.base.bridgemodebase import \
    BridgemodeBase


class Bridgemode(DeviceApi, BridgemodeBase):
    def __init__(self, device_input):
        super(Bridgemode, self).__init__(device_input)

    def set_mode(self, arg_dictionary, **kwargs):
        uuid = "0aedb73e-9436-4b17-b1c4-79440118b1c8"
        cmd = "set bridge mode {0}".format(arg_dictionary['mode'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mode(self, arg_dictionary, **kwargs):
        uuid = "a5db3a22-132e-404b-ab0b-9b49d8b16fac"
        cmd = "show bridge mode"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
