"""
All sysinfo supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.sysinfo.base.sysinfobase import SysinfoBase


class Sysinfo(DeviceApi, SysinfoBase):
    def __init__(self, device_input):
        super(Sysinfo, self).__init__(device_input)

    def show_system_info(self, arg_dictionary, **kwargs):
        uuid = "9992c6bd-2b22-4727-ad19-cfbd352a6ca1"
        cmd = "show sys-info"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
