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
        cmd = "copy tftp://@{0}/{1} flash://{2}".format(arg_dictionary['server'],
                                                        arg_dictionary['filename'],
                                                        arg_dictionary['new_filename'])
        prompt = "userPrompt"
        conf = "do you want to overwrite it? [y/n]"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def copy_file(self, arg_dictionary, **kwargs):
        uuid = "d8c0926c-e385-48a9-bce8-6f01b5e3a2a9"
        cmd = "copy flash://{0} flash://{1}".format(arg_dictionary['filename'],
                                                    arg_dictionary['new_filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_system_config(self, arg_dictionary, **kwargs):
        uuid = "6d59a8fd-ed51-4dec-8f4d-b9cf16610e10"
        cmd = "copy flash://{0} startup-config".format(arg_dictionary['filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def upload_file(self, arg_dictionary, **kwargs):
        uuid = "094ebcea-37ec-400f-a107-46981bff8ea1"
        cmd = "copy flash://{0} tftp://@{1}/{2}".format(arg_dictionary['local_file'],
                                                        arg_dictionary['server_ip'],
                                                        arg_dictionary['remote_file'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_file(self, arg_dictionary, **kwargs):
        uuid = "0a78ddba-71a3-42c3-868e-11164c7f7add"
        cmd = "delete flash://{0}".format(arg_dictionary['file_name'])
        prompt = "userPrompt"
        conf = "Do you want to continue:[y/n]"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def save_current_config(self, arg_dictionary, **kwargs):
        uuid = "02c67e7a-a247-43ab-b12f-f539a8c5bd64"
        cmd = "copy running-config startup-config"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def save_config_to_file(self, arg_dictionary, **kwargs):
        uuid = "3d8e0f5e-997b-4038-8062-b9366bb4e9e4"
        cmd = "copy running-config {0}".format(arg_dictionary['config'])
        prompt = "userPrompt"
        conf = "do you want to overwrite it? [y/n]"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def show_logging_files(self, arg_dictionary, **kwargs):
        uuid = "e2ce6548-0a30-4225-9137-743bb2742c05"
        cmd = "show logging raslog"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_config_files(self, arg_dictionary, **kwargs):
        uuid = "c891f497-15b8-430c-b7dd-a277279e5798"
        cmd = "dir"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
