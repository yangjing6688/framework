"""
All logging supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.logging.base.loggingbase import LoggingBase


class Logging(DeviceApi, LoggingBase):
    def __init__(self, device_input):
        super(Logging, self).__init__(device_input)

    def clear_log_auditlog(self, arg_dictionary, **kwargs):
        uuid = "a09f2853-a6c2-484b-a3e2-8dc45402c9e1"
        cmd = "clear logging auditlog"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_log_raslog(self, arg_dictionary, **kwargs):
        uuid = "c79f61db-d7e3-4a79-b661-2d989ac2e7a7"
        cmd = "clear logging raslog"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_log_auditlog(self, arg_dictionary, **kwargs):
        uuid = "c72b3bc4-baa5-41a4-bd6e-ed5a2c8dc68b"
        cmd = "show logging auditlog"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_log_raslog(self, arg_dictionary, **kwargs):
        uuid = "5930a524-0499-4226-b71b-b2a2b511b579"
        cmd = "show logging raslog"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
