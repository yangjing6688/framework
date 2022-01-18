"""
All ssh supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.ssh.base.sshbase import SshBase


class Ssh(DeviceApi, SshBase):
    def __init__(self, device_input):
        super(Ssh, self).__init__(device_input)

    def enable_client(self, arg_dictionary, **kwargs):
        uuid = "c4691b4a-c544-47bf-b72f-ec34e9743aab"
        cmd = "ssh client enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_client(self, arg_dictionary, **kwargs):
        uuid = "efcc8ea4-695d-4272-b325-fb416a42f991"
        cmd = "no ssh client enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_version(self, arg_dictionary, **kwargs):
        uuid = "ce297f32-03ea-4a22-8288-8e4b3262bcd0"
        cmd = "ssh version {0}".format(arg_dictionary['version'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tcp_port(self, arg_dictionary, **kwargs):
        uuid = "f1650dc0-93b2-43f3-a95d-62d0e6c8cab8"
        cmd = "ssh port {0}".format(arg_dictionary['tcp_port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show(self, arg_dictionary, **kwargs):
        uuid = "823e42ad-344c-4a2a-8d19-0ef08d30551c"
        cmd = "show ssh global"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_session(self, arg_dictionary, **kwargs):
        uuid = "97c26e4e-1ed6-43a1-bed7-62b2c986b62c"
        cmd = "show ssh session"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_rekey(self, arg_dictionary, **kwargs):
        uuid = "afe63ae6-664e-4e8f-b386-9c6d3da7c584"
        cmd = "show ssh rekey"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
