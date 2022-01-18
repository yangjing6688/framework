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
        cmd = "ntp"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_client(self, arg_dictionary, **kwargs):
        uuid = "8b787f31-3f32-46e8-b6ec-071b9f070e62"
        cmd = "no ntp"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server(self, arg_dictionary, **kwargs):
        uuid = "bffe6b2a-5f63-4e1e-b46e-29c6e2418d0a"
        cmd = "ntp server {0}".format(arg_dictionary['server'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server_key(self, arg_dictionary, **kwargs):
        uuid = "09065f5d-a15f-4409-ba1d-7b22d7b644fe"
        cmd = "ntp server {0} authentication-key {1}".format(arg_dictionary['server'],
                                                             arg_dictionary['key'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_server(self, arg_dictionary, **kwargs):
        uuid = "39122ed4-91c1-4a3d-b925-13bb8a5cb81b"
        cmd = "no ntp server {0}".format(arg_dictionary['server'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_server(self, arg_dictionary, **kwargs):
        uuid = "493921dc-3a05-4340-a0b5-a767118a45c0"
        cmd = "ntp server {0} enable".format(arg_dictionary['server'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_server(self, arg_dictionary, **kwargs):
        uuid = "e9558c48-66e2-4a27-bb5e-f6d8f78b768b"
        cmd = "no ntp server {0} enable".format(arg_dictionary['server'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_server_auth(self, arg_dictionary, **kwargs):
        uuid = "5c286cbc-5c61-4651-b747-ab06a3dff560"
        cmd = "ntp server {0} auth-enable".format(arg_dictionary['server'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_server_auth(self, arg_dictionary, **kwargs):
        uuid = "30b347ad-6d8a-4724-9669-d6726c8945b3"
        cmd = "no ntp server {0} auth-enable".format(arg_dictionary['server'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_global_interval(self, arg_dictionary, **kwargs):
        uuid = "e1e31ff7-1549-42f2-9cb0-6395e856e98f"
        cmd = "ntp interval {0}".format(arg_dictionary['interval'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_server_source_ip(self, arg_dictionary, **kwargs):
        uuid = "592e5f6e-0d5a-422e-ad6e-4d98cadb8c44"
        cmd = "ntp server {0} source-ip {1}".format(arg_dictionary['server'],
                                                    arg_dictionary['source_ip'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_auth(self, arg_dictionary, **kwargs):
        uuid = "e912bc13-d9f2-4bab-95c9-c662d9c0fd64"
        cmd = "ntp authentication-key {0} initialkey".format(arg_dictionary['index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_auth_key(self, arg_dictionary, **kwargs):
        uuid = "d3b91edb-83b0-4042-9502-6cf71d3d69d0"
        cmd = "ntp authentication-key {0} {1}".format(arg_dictionary['index'],
                                                      arg_dictionary['secret'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_auth_md5(self, arg_dictionary, **kwargs):
        uuid = "3f78af7e-6736-41e5-ab21-cdfce7790768"
        cmd = "ntp authentication-key {0} type md5".format(arg_dictionary['index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_auth_sha1(self, arg_dictionary, **kwargs):
        uuid = "d4ff46c2-5137-4053-9137-f4be9669b086"
        cmd = "ntp authentication-key {0} type sha1".format(arg_dictionary['index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_auth_key(self, arg_dictionary, **kwargs):
        uuid = "0c8daefc-7345-4f9a-b77d-115e6eebac6b"
        cmd = "no ntp authentication-key {0}".format(arg_dictionary['index'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "631a00eb-4564-415a-ab79-47363713be48"
        cmd = "show ntp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_servers(self, arg_dictionary, **kwargs):
        uuid = "6d62bc6f-e817-482f-a755-be026d8b43f8"
        cmd = "show ntp server"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_key(self, arg_dictionary, **kwargs):
        uuid = "0cab21c8-f88d-4bba-aa60-45b1edfa9f8c"
        cmd = "show ntp key"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_statistics(self, arg_dictionary, **kwargs):
        uuid = "a67a4bf0-9652-4b7d-b5ba-c2005fa802db"
        cmd = "show ntp statistics"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
