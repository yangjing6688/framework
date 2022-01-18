"""
All logging supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.logging.base.loggingbase import LoggingBase


class Logging(DeviceApi, LoggingBase):
    def __init__(self, device_input):
        super(Logging, self).__init__(device_input)

    def clear_log(self, arg_dictionary, **kwargs):
        uuid = "e98e0e13-4086-463d-8b5c-736ca7d20db5"
        cmd = "clear log static"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_log(self, arg_dictionary, **kwargs):
        uuid = "1f9fa5cb-7b28-4235-89ac-e210f06a48be"
        cmd = "show log"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
