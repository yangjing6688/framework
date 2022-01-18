"""
All iprouting supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.iprouting.base.iproutingbase import \
    IproutingBase


class Iprouting(DeviceApi, IproutingBase):
    def __init__(self, device_input):
        super(Iprouting, self).__init__(device_input)

    def show_static_route(self, arg_dictionary, **kwargs):
        uuid = "5b410683-0304-4499-b01e-1e45e72be629"
        cmd = "sudo ip netns exec swns bash||sudo route"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
