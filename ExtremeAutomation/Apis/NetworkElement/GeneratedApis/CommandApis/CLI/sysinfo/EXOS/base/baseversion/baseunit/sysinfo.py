"""
All sysinfo supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.sysinfo.base.sysinfobase import SysinfoBase


class Sysinfo(DeviceApi, SysinfoBase):
    def __init__(self, device_input):
        super(Sysinfo, self).__init__(device_input)

    def show_hardware_summary(self, arg_dictionary, **kwargs):
        uuid = "531d77b2-554f-4fbb-b5cd-e5519a1e1951"
        cmd = "show slot"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_core_files(self, arg_dictionary, **kwargs):
        uuid = "3c5089f2-d362-4999-9b75-6602db32b8e1"
        cmd = "ls internal-memory"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_system_cpu_usage(self, arg_dictionary, **kwargs):
        uuid = "1896061d-31fa-4171-9668-f344caf212d7"
        cmd = "show cpu-monitoring"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_system_info(self, arg_dictionary, **kwargs):
        uuid = "9992c6bd-2b22-4727-ad19-cfbd352a6ca1"
        cmd = "show switch"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
