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
        cmd = "tftp get {0} vr {1} {2} {3}".format(arg_dictionary['server'],
                                                   arg_dictionary['vr'],
                                                   arg_dictionary['filename'],
                                                   arg_dictionary['new_filename'])
        prompt = "userPrompt"
        conf = "(y/N)"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def copy_file(self, arg_dictionary, **kwargs):
        uuid = "d8c0926c-e385-48a9-bce8-6f01b5e3a2a9"
        cmd = "cp {0} {1}".format(arg_dictionary['filename'],
                                  arg_dictionary['new_filename'])
        prompt = "userPrompt"
        conf = "(y/N)"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_system_config(self, arg_dictionary, **kwargs):
        uuid = "6d59a8fd-ed51-4dec-8f4d-b9cf16610e10"
        cmd = "use configuration {0}".format(arg_dictionary['config'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def upload_core_file(self, arg_dictionary, **kwargs):
        uuid = "1508165a-6f09-4f0c-8fd4-04000634f9d7"
        cmd = "upload debug {0} vr {1}".format(arg_dictionary['server_ip'],
                                               arg_dictionary['vr'])
        prompt = "userPrompt"
        conf = "Do you want to run show tech-support logto file first? (y/N)"
        conf_args = "{0}".format(arg_dictionary['yes_no'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def upload_file(self, arg_dictionary, **kwargs):
        uuid = "094ebcea-37ec-400f-a107-46981bff8ea1"
        cmd = "upload {0} {1} vr {2} {3} chron".format(arg_dictionary['local_file'],
                                                       arg_dictionary['server_ip'],
                                                       arg_dictionary['vr'],
                                                       arg_dictionary['remote_file'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def generate_support_file(self, arg_dictionary, **kwargs):
        uuid = "9eda0ea2-639e-4499-af1d-d7642c9598eb"
        cmd = "show tech-support all logto file"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_file_on_slot(self, arg_dictionary, **kwargs):
        uuid = "e9b4d9b3-22fe-4674-b0da-0fee0b344593"
        cmd = "rm {0}".format(arg_dictionary['file_name'])
        prompt = "userPrompt"
        conf = "(y/n)"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def delete_file(self, arg_dictionary, **kwargs):
        uuid = "0a78ddba-71a3-42c3-868e-11164c7f7add"
        cmd = "rm {0}".format(arg_dictionary['file_name'])
        prompt = "userPrompt"
        conf = "(y/N)"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def save_current_config(self, arg_dictionary, **kwargs):
        uuid = "02c67e7a-a247-43ab-b12f-f539a8c5bd64"
        cmd = "save"
        prompt = "userPrompt"
        conf = "(y/N)"
        conf_args = "{0}".format(arg_dictionary['save_config'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def save_config_to_primary(self, arg_dictionary, **kwargs):
        uuid = "32c70c1b-1653-46ee-b81b-2e4196af5865"
        cmd = "save configuration primary"
        prompt = "userPrompt"
        conf = "(y/N)"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def save_config_to_secondary(self, arg_dictionary, **kwargs):
        uuid = "7de714fa-385e-4285-b0fd-5f5580a78586"
        cmd = "save configuration secondary"
        prompt = "userPrompt"
        conf = "(y/N)"
        conf_args = "{0}".format(arg_dictionary['answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def save_config_to_file(self, arg_dictionary, **kwargs):
        uuid = "3d8e0f5e-997b-4038-8062-b9366bb4e9e4"
        cmd = "save configuration {0}".format(arg_dictionary['config'])
        prompt = "userPrompt"
        conf = "overwrite it? (y/N)||save configuration to||default database? (y/N)"
        conf_args = "{0}||{1}||{2}".format(arg_dictionary['overwrite_answer'],
                                           arg_dictionary['standard_answer'],
                                           arg_dictionary['replace_default_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def show_logging_files(self, arg_dictionary, **kwargs):
        uuid = "e2ce6548-0a30-4225-9137-743bb2742c05"
        cmd = "ls internal-memory"
        prompt = "userPrompt"

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
