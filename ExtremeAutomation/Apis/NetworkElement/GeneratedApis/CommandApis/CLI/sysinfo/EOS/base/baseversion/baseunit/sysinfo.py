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
        cmd = "show system hardware brief"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_core_files(self, arg_dictionary, **kwargs):
        uuid = "3c5089f2-d362-4999-9b75-6602db32b8e1"
        cmd = "dir slot{0}/cores".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_system_cpu_usage(self, arg_dictionary, **kwargs):
        uuid = "1896061d-31fa-4171-9668-f344caf212d7"
        cmd = "show system utilization cpu"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_system_slot_info(self, arg_dictionary, **kwargs):
        uuid = "603a68dd-444a-40cd-b052-10bd801852b3"
        cmd = "debug messageLog message|| i|| x"
        prompt = "debugPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_slot_files(self, arg_dictionary, **kwargs):
        uuid = "0f34134f-4468-4907-9d7f-53e5008f6880"
        cmd = "dir slot{0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
