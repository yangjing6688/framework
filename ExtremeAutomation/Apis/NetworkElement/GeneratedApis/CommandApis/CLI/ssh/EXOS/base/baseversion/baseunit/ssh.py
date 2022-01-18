"""
All ssh supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.ssh.base.sshbase import SshBase


class Ssh(DeviceApi, SshBase):
    def __init__(self, device_input):
        super(Ssh, self).__init__(device_input)

    def enable(self, arg_dictionary, **kwargs):
        uuid = "19268327-5b64-4b96-ae69-92538ef45c4f"
        cmd = "enable ssh2"
        prompt = "userPrompt"
        conf = "Continue?"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def disable(self, arg_dictionary, **kwargs):
        uuid = "3a8fb625-5da1-4534-a716-32896dd5b63d"
        cmd = "disable ssh2"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show(self, arg_dictionary, **kwargs):
        uuid = "823e42ad-344c-4a2a-8d19-0ef08d30551c"
        cmd = "show ssh2"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
