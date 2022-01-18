"""
All filemanagement supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.filemanagement.base.filemanagementbase import \
    FilemanagementBase


class Filemanagement(DeviceApi, FilemanagementBase):
    def __init__(self, device_input):
        super(Filemanagement, self).__init__(device_input)

    def copy_file_from_server(self, arg_dictionary, **kwargs):
        uuid = "41ef4888-d04f-439b-ab59-d5eeb9589bcd"
        cmd = "copy {0} {1}".format(arg_dictionary['filename'],
                                    arg_dictionary['new_filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def copy_file(self, arg_dictionary, **kwargs):
        uuid = "d8c0926c-e385-48a9-bce8-6f01b5e3a2a9"
        cmd = "copy {0} {1}".format(arg_dictionary['filename'],
                                    arg_dictionary['new_filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_config_files(self, arg_dictionary, **kwargs):
        uuid = "c891f497-15b8-430c-b7dd-a277279e5798"
        cmd = "dir"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
