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
        cmd = "set sntp client unicast"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_client(self, arg_dictionary, **kwargs):
        uuid = "8b787f31-3f32-46e8-b6ec-071b9f070e62"
        cmd = "set sntp client disable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server(self, arg_dictionary, **kwargs):
        uuid = "bffe6b2a-5f63-4e1e-b46e-29c6e2418d0a"
        cmd = "set sntp server {0}".format(arg_dictionary['server'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server_key(self, arg_dictionary, **kwargs):
        uuid = "09065f5d-a15f-4409-ba1d-7b22d7b644fe"
        cmd = "set sntp server {0} key {1}".format(arg_dictionary['server'],
                                                   arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server_precedence(self, arg_dictionary, **kwargs):
        uuid = "5108c32c-76ba-48c8-9c09-ee2711295567"
        cmd = "set sntp server {0} precedence {1}".format(arg_dictionary['server'],
                                                          arg_dictionary['precedence'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server_precedence_key(self, arg_dictionary, **kwargs):
        uuid = "6d14787c-7afc-4907-9567-568b4b76228f"
        cmd = "set sntp server {0} key {1} precedence {2}".format(arg_dictionary['server'],
                                                                  arg_dictionary['key'],
                                                                  arg_dictionary['precedence'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_server(self, arg_dictionary, **kwargs):
        uuid = "39122ed4-91c1-4a3d-b925-13bb8a5cb81b"
        cmd = "clear sntp server {0}".format(arg_dictionary['server'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "631a00eb-4564-415a-ab79-47363713be48"
        cmd = "show sntp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_servers(self, arg_dictionary, **kwargs):
        uuid = "6d62bc6f-e817-482f-a755-be026d8b43f8"
        cmd = "show sntp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
