"""
All hostmonitor supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.hostmonitor.base.hostmonitorbase import \
    HostmonitorBase


class Hostmonitor(DeviceApi, HostmonitorBase):
    def __init__(self, device_input):
        super(Hostmonitor, self).__init__(device_input)

    def show_slot(self, arg_dictionary, **kwargs):
        uuid = "9cebe644-cb38-4cf6-a727-276929580b72"
        cmd = "show slot"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
