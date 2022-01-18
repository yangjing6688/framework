"""
All unittest supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.base.unittestbase import UnittestBase


class Unittest(DeviceApi, UnittestBase):
    def __init__(self, device_input):
        super(Unittest, self).__init__(device_input)

    def function(self, arg_dictionary, **kwargs):
        uuid = "ba47070e-d7dc-46ce-8cda-9664032f3761"
        cmd = "command"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
