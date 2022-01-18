"""
All isis supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.isis.base.isisbase import IsisBase


class Isis(DeviceApi, IsisBase):
    def __init__(self, device_input):
        super(Isis, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "5e8b2b77-f570-4a1c-b139-c933c7547bd6"
        cmd = "enable isis"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "695b2829-e1be-4156-878a-46a23c9ee9b9"
        cmd = "disable isis"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
