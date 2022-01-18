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
        cmd = "interface tunnel {0}".format(arg_dictionary['tunnel'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_interface(self, arg_dictionary, **kwargs):
        uuid = "e8a1c3ea-06bf-4bc3-809f-477f1da53742"
        cmd = "no interface tunnel {0}".format(arg_dictionary['tunnel'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mode_gre(self, arg_dictionary, **kwargs):
        uuid = "7189ce0d-7a04-4abb-84c9-7d1f6a6f21b4"
        cmd = "mode gre ip"
        prompt = "intfPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_source_ip(self, arg_dictionary, **kwargs):
        uuid = "ed130690-92dc-4748-8729-259d5b8c2858"
        cmd = "source {0}".format(arg_dictionary['ip_address'])
        prompt = "intfPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_dest_ip(self, arg_dictionary, **kwargs):
        uuid = "9eba98f9-cb29-45b6-aace-101b08753f60"
        cmd = "destination {0}".format(arg_dictionary['ip_address'])
        prompt = "intfPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_source_ip(self, arg_dictionary, **kwargs):
        uuid = "2feabea2-ad4d-4d86-89e8-d3bc5c44d8e6"
        cmd = "no source"
        prompt = "intfPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_dest_ip(self, arg_dictionary, **kwargs):
        uuid = "fc21d27d-a6e4-49f3-9887-3e6c2330fd7c"
        cmd = "no destination"
        prompt = "intfPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_mode_gre(self, arg_dictionary, **kwargs):
        uuid = "5efab2db-71ff-4999-bee6-0ee3c80407ea"
        cmd = "no tunnel mode gre ip"
        prompt = "intfPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_tunnel(self, arg_dictionary, **kwargs):
        uuid = "bb5a6d27-f8bd-4338-afa2-e97330929747"
        cmd = "show tunnel {0}".format(arg_dictionary['tunnel'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all(self, arg_dictionary, **kwargs):
        uuid = "51405cc7-f7f3-4911-8061-66bf00c1f0a4"
        cmd = "show tunnel brief"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
