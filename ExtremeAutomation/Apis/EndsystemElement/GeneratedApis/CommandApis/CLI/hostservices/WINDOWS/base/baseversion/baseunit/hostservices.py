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
        cmd = "ping -n {0} {1}".format(arg_dictionary['count'],
                                       arg_dictionary['host_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)

    def download_file_via_ftp(self, arg_dictionary, **kwargs):
        cmd = "del __ftp.txt|| echo open {0}> __ftp.txt || echo {1}>> __ftp.txt || echo {2}>> __ftp.txt || echo get {3}>> __ftp.txt || echo quit>> __ftp.txt || ftp -s:__ftp.txt || del __ftp.txt".format(arg_dictionary['host'],
                                                                                                                                                                                                          arg_dictionary['user'],
                                                                                                                                                                                                          arg_dictionary['password'],
                                                                                                                                                                                                          arg_dictionary['file_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)
