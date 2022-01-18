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
        cmd = "enable ntp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_client(self, arg_dictionary, **kwargs):
        uuid = "8b787f31-3f32-46e8-b6ec-071b9f070e62"
        cmd = "disable ntp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server(self, arg_dictionary, **kwargs):
        uuid = "bffe6b2a-5f63-4e1e-b46e-29c6e2418d0a"
        cmd = "configure ntp server add {0}".format(arg_dictionary['server'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_server_key(self, arg_dictionary, **kwargs):
        uuid = "09065f5d-a15f-4409-ba1d-7b22d7b644fe"
        cmd = "configure ntp server add {0} key {1}".format(arg_dictionary['server'],
                                                            arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_server(self, arg_dictionary, **kwargs):
        uuid = "39122ed4-91c1-4a3d-b925-13bb8a5cb81b"
        cmd = "configure ntp server delete {0}".format(arg_dictionary['server'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_client_vlan(self, arg_dictionary, **kwargs):
        uuid = "1c3cca62-fb25-4aa7-8623-e7b487b7089c"
        cmd = "enable ntp {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_client_vlan(self, arg_dictionary, **kwargs):
        uuid = "07ac70d6-40b1-4f3e-abb9-0159a7eb83b9"
        cmd = "disable ntp {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "631a00eb-4564-415a-ab79-47363713be48"
        cmd = "show ntp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_association(self, arg_dictionary, **kwargs):
        uuid = "ce8c3fe3-eebb-43cf-8745-de5f5bd5b14c"
        cmd = "show ntp association"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_servers(self, arg_dictionary, **kwargs):
        uuid = "6d62bc6f-e817-482f-a755-be026d8b43f8"
        cmd = "show ntp server"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
