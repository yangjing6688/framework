"""
All gvrp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.gvrp.base.gvrpbase import GvrpBase


class Gvrp(DeviceApi, GvrpBase):
    def __init__(self, device_input):
        super(Gvrp, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "437c86c5-9308-4907-9309-0d6ff78d3aa3"
        cmd = "set gvrp enable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "95e010f0-7318-4337-a1bf-e683fe046832"
        cmd = "set gvrp disable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port(self, arg_dictionary, **kwargs):
        uuid = "35afdcac-f547-4240-a938-78a57d4cc55c"
        cmd = "set gvrp enable {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "d0e8f204-ea0e-4e76-94e2-9180ad6c9850"
        cmd = "set gvrp disable {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "8f8e7f0f-2543-4b4a-b6fa-4bbdffd9df83"
        cmd = "show gvrp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state_port(self, arg_dictionary, **kwargs):
        uuid = "b115f617-3eaf-4b74-b74a-5b29e4b8d7bf"
        cmd = "show gvrp {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
