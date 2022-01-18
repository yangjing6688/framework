"""
All hostutils supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.hostutils.base.hostutilsbase import \
    HostutilsBase


class Hostutils(DeviceApi, HostutilsBase):
    def __init__(self, device_input):
        super(Hostutils, self).__init__(device_input)

    def ping_host(self, arg_dictionary, **kwargs):
        uuid = "57c52793-0d02-4f7f-b5b2-53bcd3024df4"
        cmd = "ping -c {0} -i {1} {2}".format(arg_dictionary['count'],
                                              arg_dictionary['timeout'],
                                              arg_dictionary['host_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
