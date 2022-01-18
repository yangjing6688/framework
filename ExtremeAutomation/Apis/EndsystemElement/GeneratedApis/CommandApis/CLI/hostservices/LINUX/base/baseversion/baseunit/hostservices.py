"""
All hostservices supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.CLI.hostservices.base.hostservicesbase import \
    HostservicesBase


class Hostservices(DeviceApi, HostservicesBase):
    def __init__(self, device_input):
        super(Hostservices, self).__init__(device_input)

    def ping_host_from_endsys(self, arg_dictionary, **kwargs):
        cmd = "ping -c {0} {1}".format(arg_dictionary['count'],
                                       arg_dictionary['host_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)
