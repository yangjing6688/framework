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
        cmd = "copy tftp://{0}/{1} slot{2}/{3}".format(arg_dictionary['server'],
                                                       arg_dictionary['filename'],
                                                       arg_dictionary['slot'],
                                                       arg_dictionary['new_filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def copy_file(self, arg_dictionary, **kwargs):
        uuid = "d8c0926c-e385-48a9-bce8-6f01b5e3a2a9"
        cmd = "copy slot{0}/{1} slot{2}/{3}".format(arg_dictionary['slot_a'],
                                                    arg_dictionary['filename'],
                                                    arg_dictionary['slot_b'],
                                                    arg_dictionary['new_filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_system_config(self, arg_dictionary, **kwargs):
        uuid = "6d59a8fd-ed51-4dec-8f4d-b9cf16610e10"
        cmd = "configure {0}".format(arg_dictionary['config'])
        prompt = "userPrompt"
        conf = "Are you sure you want to continue (y/n) [n]?"
        conf_args = "{0}".format(arg_dictionary['reboot_answer'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def upload_core_file(self, arg_dictionary, **kwargs):
        uuid = "1508165a-6f09-4f0c-8fd4-04000634f9d7"
        cmd = "copy slot{0}/cores/{1} tftp://{2}/{3}".format(arg_dictionary['slot'],
                                                             arg_dictionary['file_name'],
                                                             arg_dictionary['server_ip'],
                                                             arg_dictionary['remote_file'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def upload_file(self, arg_dictionary, **kwargs):
        uuid = "094ebcea-37ec-400f-a107-46981bff8ea1"
        cmd = "copy {0} tftp://{1}/{2}".format(arg_dictionary['local_file'],
                                               arg_dictionary['server_ip'],
                                               arg_dictionary['remote_file'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def generate_support_file(self, arg_dictionary, **kwargs):
        uuid = "9eda0ea2-639e-4499-af1d-d7642c9598eb"
        cmd = "show support outfile slot{0}/{1}.log".format(arg_dictionary['slot'],
                                                            arg_dictionary['filename'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_file_on_slot(self, arg_dictionary, **kwargs):
        uuid = "e9b4d9b3-22fe-4674-b0da-0fee0b344593"
        cmd = "del slot{0}/{1}".format(arg_dictionary['slot'],
                                       arg_dictionary['file_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_logging_files(self, arg_dictionary, **kwargs):
        uuid = "e2ce6548-0a30-4225-9137-743bb2742c05"
        cmd = "dir slot{0}/logs/".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_config_files(self, arg_dictionary, **kwargs):
        uuid = "c891f497-15b8-430c-b7dd-a277279e5798"
        cmd = "dir"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_config_files_per_slot(self, arg_dictionary, **kwargs):
        uuid = "c5c51f3b-2e17-4c39-9c1d-31ac19f06ef8"
        cmd = "dir slot{0}".format(arg_dictionary['slot'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
