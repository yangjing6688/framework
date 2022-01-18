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
        cmd = "copy {0}:{1} {2}".format(arg_dictionary['server'],
                                        arg_dictionary['filename'],
                                        arg_dictionary['new_filename'])
        prompt = "userPrompt"
        conf = "(y/n)"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def copy_file(self, arg_dictionary, **kwargs):
        uuid = "d8c0926c-e385-48a9-bce8-6f01b5e3a2a9"
        cmd = "copy /intflash/{0} /intflash/{1}".format(arg_dictionary['filename'],
                                                        arg_dictionary['new_filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_system_config(self, arg_dictionary, **kwargs):
        uuid = "6d59a8fd-ed51-4dec-8f4d-b9cf16610e10"
        cmd = "boot config choice primary config-file {0}".format(arg_dictionary['config'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_file(self, arg_dictionary, **kwargs):
        uuid = "0a78ddba-71a3-42c3-868e-11164c7f7add"
        cmd = "del {0}".format(arg_dictionary['file_name'])
        prompt = "userPrompt"
        conf = "Are you sure (y/n) ?"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def save_current_config(self, arg_dictionary, **kwargs):
        uuid = "02c67e7a-a247-43ab-b12f-f539a8c5bd64"
        cmd = "save config"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def save_config_to_file(self, arg_dictionary, **kwargs):
        uuid = "3d8e0f5e-997b-4038-8062-b9366bb4e9e4"
        cmd = "save config file {0}".format(arg_dictionary['config'])
        prompt = "routerConfigPrompt"
        conf = "(y/n)"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_system_to_primary_config(self, arg_dictionary, **kwargs):
        uuid = "0ef03d4d-a041-4230-88fe-85fed45c6bf3"
        cmd = "boot config choice primary config-file {0}".format(arg_dictionary['config'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_system_to_backup_config(self, arg_dictionary, **kwargs):
        uuid = "7d52a3ff-1183-4201-b0dc-777c123ce03f"
        cmd = "boot config choice primary backup-config-file {0}".format(arg_dictionary['config'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_config_files(self, arg_dictionary, **kwargs):
        uuid = "c891f497-15b8-430c-b7dd-a277279e5798"
        cmd = "ls"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_config_files_per_slot(self, arg_dictionary, **kwargs):
        uuid = "c5c51f3b-2e17-4c39-9c1d-31ac19f06ef8"
        cmd = "ls"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_default_boot_config_file(self, arg_dictionary, **kwargs):
        uuid = "e7e549e2-f594-4a6f-80c1-c09ca93f5e42"
        cmd = "show boot config choice"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
