"""
All common supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.CLI.common.base.commonbase import CommonBase


class Common(DeviceApi, CommonBase):
    def __init__(self, device_input):
        super(Common, self).__init__(device_input)

    def get_dir(self, arg_dictionary, **kwargs):
        cmd = "dir"
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)

    def remove_file(self, arg_dictionary, **kwargs):
        cmd = "del {0}".format(arg_dictionary['file_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(cmd, prompt=prompt)
