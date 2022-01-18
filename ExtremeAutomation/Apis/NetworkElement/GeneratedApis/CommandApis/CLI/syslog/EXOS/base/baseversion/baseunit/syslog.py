"""
All syslog supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.syslog.base.syslogbase import SyslogBase


class Syslog(DeviceApi, SyslogBase):
    def __init__(self, device_input):
        super(Syslog, self).__init__(device_input)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "c7bf4eb2-f6c7-4a44-9ce3-481f7dee8a91"
        cmd = "show log configuration"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_target_info(self, arg_dictionary, **kwargs):
        uuid = "7624468f-99b7-4115-9a4e-498853e1787e"
        cmd = "show log configuration target syslog"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
