"""
All ssh supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.ssh.base.sshbase import SshBase


class Ssh(DeviceApi, SshBase):
    def __init__(self, device_input):
        super(Ssh, self).__init__(device_input)

    def set_client_source_interface(self, arg_dictionary, **kwargs):
        uuid = "a640fe7f-d4c0-4ae8-8d09-8d44e8a07d4e"
        cmd = "ssh client source-interface {0}".format(arg_dictionary['interface'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_tcp_port(self, arg_dictionary, **kwargs):
        uuid = "f1650dc0-93b2-43f3-a95d-62d0e6c8cab8"
        cmd = "ssh server port {0}".format(arg_dictionary['tcp_port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_client_source_interface(self, arg_dictionary, **kwargs):
        uuid = "b3492f28-5da3-4aef-bc73-e95016a55d23"
        cmd = "no ssh client source-interface {0}".format(arg_dictionary['interface'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_client_status(self, arg_dictionary, **kwargs):
        uuid = "29b3463d-2b88-4f75-b3dc-74df4fce2bfb"
        cmd = "show ssh client status"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_server_status(self, arg_dictionary, **kwargs):
        uuid = "5c6f721d-5043-41e0-976c-ef92fc3d3a7f"
        cmd = "show ssh server status"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
