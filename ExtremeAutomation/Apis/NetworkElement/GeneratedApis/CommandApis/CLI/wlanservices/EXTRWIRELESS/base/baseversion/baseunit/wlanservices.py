"""
All wlanservices supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.wlanservices.base.wlanservicesbase import \
    WlanservicesBase


class Wlanservices(DeviceApi, WlanservicesBase):
    def __init__(self, device_input):
        super(Wlanservices, self).__init__(device_input)

    def show_all(self, arg_dictionary, **kwargs):
        uuid = "3b504f20-a9fe-4d6e-b8fc-1d6480f59dea"
        cmd = "show wlans"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_detail(self, arg_dictionary, **kwargs):
        uuid = "99808fc2-1b5d-4693-ada6-523765211ee2"
        cmd = "show wlans \"{0}\"".format(arg_dictionary['wlan_service_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
