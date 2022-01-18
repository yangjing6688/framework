"""
All ntp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.ntp.base.ntpbase import NtpBase


class Ntp(DeviceApi, NtpBase):
    def __init__(self, device_input):
        super(Ntp, self).__init__(device_input)

    def enable_client(self, arg_dictionary, **kwargs):
        uuid = "c784a0f4-a409-49bd-83d9-4c11f8bcbeba"
        cmd = "ntp peer {0}".format(arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_client(self, arg_dictionary, **kwargs):
        uuid = "8b787f31-3f32-46e8-b6ec-071b9f070e62"
        cmd = "no ntp peer {0}".format(arg_dictionary['ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server(self, arg_dictionary, **kwargs):
        uuid = "bffe6b2a-5f63-4e1e-b46e-29c6e2418d0a"
        cmd = "ntp server {0}".format(arg_dictionary['server'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server_key(self, arg_dictionary, **kwargs):
        uuid = "09065f5d-a15f-4409-ba1d-7b22d7b644fe"
        cmd = "ntp server {0} key {1}".format(arg_dictionary['server'],
                                              arg_dictionary['key'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_server(self, arg_dictionary, **kwargs):
        uuid = "39122ed4-91c1-4a3d-b925-13bb8a5cb81b"
        cmd = "no ntp server {0}".format(arg_dictionary['server'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_server_auth(self, arg_dictionary, **kwargs):
        uuid = "5c286cbc-5c61-4651-b747-ab06a3dff560"
        cmd = "ntp authenticate"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_server_source_ip(self, arg_dictionary, **kwargs):
        uuid = "592e5f6e-0d5a-422e-ad6e-4d98cadb8c44"
        cmd = "ntp source-ip {0}".format(arg_dictionary['server'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_source_ip_mm(self, arg_dictionary, **kwargs):
        uuid = "fa3c7bce-bf26-4d16-8044-bcb5772be6c0"
        cmd = "ntp source-ip mm-ip"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_source_ip_chassis(self, arg_dictionary, **kwargs):
        uuid = "9ea639ea-782f-4e8a-bb8f-060bf4896694"
        cmd = "ntp source-ip chassis-ip"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_auth_md5(self, arg_dictionary, **kwargs):
        uuid = "3f78af7e-6736-41e5-ab21-cdfce7790768"
        cmd = "ntp authentication-key {0} md5 {1}".format(arg_dictionary['index'],
                                                          arg_dictionary['md5_string'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_auth_key(self, arg_dictionary, **kwargs):
        uuid = "0c8daefc-7345-4f9a-b77d-115e6eebac6b"
        cmd = "no ntp authentication-key {0}".format(arg_dictionary['index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "631a00eb-4564-415a-ab79-47363713be48"
        cmd = "show ntp status"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_association(self, arg_dictionary, **kwargs):
        uuid = "ce8c3fe3-eebb-43cf-8745-de5f5bd5b14c"
        cmd = "show ntp association"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_association_detail(self, arg_dictionary, **kwargs):
        uuid = "c7c5dde3-3aa1-4dca-9bca-fc6be13458ac"
        cmd = "show ntp association detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
