"""
All tunnel supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.tunnel.base.tunnelbase import TunnelBase


class Tunnel(DeviceApi, TunnelBase):
    def __init__(self, device_input):
        super(Tunnel, self).__init__(device_input)

    def create_interface(self, arg_dictionary, **kwargs):
        uuid = "5e4d2dce-a324-4288-85fa-b3986c94a5ec"
        cmd = "create tunnel {0}".format(self.str_utils.exos_tunnel_interface(arg_dictionary['tunnel']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_interface(self, arg_dictionary, **kwargs):
        uuid = "e8a1c3ea-06bf-4bc3-809f-477f1da53742"
        cmd = "delete tunnel {0}".format(self.str_utils.exos_tunnel_interface(arg_dictionary['tunnel']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_interface(self, arg_dictionary, **kwargs):
        uuid = "3fcc3372-4257-4c27-ba06-9bd2f92bb76e"
        cmd = "enable tunnel {0}".format(self.str_utils.exos_tunnel_interface(arg_dictionary['tunnel']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_interface(self, arg_dictionary, **kwargs):
        uuid = "75d9f71a-0d75-4b0b-b23c-644e421c6280"
        cmd = "disable tunnel {0}".format(self.str_utils.exos_tunnel_interface(arg_dictionary['tunnel']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all(self, arg_dictionary, **kwargs):
        uuid = "51405cc7-f7f3-4911-8061-66bf00c1f0a4"
        cmd = "show tunnel"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
