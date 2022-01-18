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
        cmd = "shutdown"
        prompt = "intfPrompt"
        prompt_args = "tun.0.{0}".format(arg_dictionary['tunnel'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def delete_interface(self, arg_dictionary, **kwargs):
        uuid = "e8a1c3ea-06bf-4bc3-809f-477f1da53742"
        cmd = "no interface tunnel tun.0.{0}".format(arg_dictionary['tunnel'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_interface(self, arg_dictionary, **kwargs):
        uuid = "3fcc3372-4257-4c27-ba06-9bd2f92bb76e"
        cmd = "no shutdown"
        prompt = "intfPrompt"
        prompt_args = "tun.0.{0}".format(arg_dictionary['tunnel'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_interface(self, arg_dictionary, **kwargs):
        uuid = "75d9f71a-0d75-4b0b-b23c-644e421c6280"
        cmd = "shutdown"
        prompt = "intfPrompt"
        prompt_args = "tun.0.{0}".format(arg_dictionary['tunnel'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mode_gre(self, arg_dictionary, **kwargs):
        uuid = "7189ce0d-7a04-4abb-84c9-7d1f6a6f21b4"
        cmd = "tunnel mode gre"
        prompt = "intfPrompt"
        prompt_args = "tun.0.{0}".format(arg_dictionary['tunnel'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mode_vxlan(self, arg_dictionary, **kwargs):
        uuid = "b0e26563-c285-4f8b-b979-a8fefbd19217"
        cmd = "tunnel mode vxlan"
        prompt = "intfPrompt"
        prompt_args = "tun.0.{0}".format(arg_dictionary['tunnel'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mode_vxlan_l2tb_port(self, arg_dictionary, **kwargs):
        uuid = "b097d007-1522-42d1-9dc3-2539e52177fe"
        cmd = "tunnel mode vxlan l2 {0}".format(arg_dictionary['port'])
        prompt = "intfPrompt"
        prompt_args = "tun.0.{0}".format(arg_dictionary['tunnel'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_mode_gre_l2_port(self, arg_dictionary, **kwargs):
        uuid = "944976e1-5c22-4144-8891-1364fe6b4d37"
        cmd = "tunnel mode gre l2 {0}".format(arg_dictionary['port'])
        prompt = "intfPrompt"
        prompt_args = "tun.0.{0}".format(arg_dictionary['tunnel'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_source_ip(self, arg_dictionary, **kwargs):
        uuid = "ed130690-92dc-4748-8729-259d5b8c2858"
        cmd = "tunnel source {0}".format(arg_dictionary['ip_address'])
        prompt = "intfPrompt"
        prompt_args = "tun.0.{0}".format(arg_dictionary['tunnel'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_dest_ip(self, arg_dictionary, **kwargs):
        uuid = "9eba98f9-cb29-45b6-aace-101b08753f60"
        cmd = "tunnel destination {0}".format(arg_dictionary['ip_address'])
        prompt = "intfPrompt"
        prompt_args = "tun.0.{0}".format(arg_dictionary['tunnel'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_all(self, arg_dictionary, **kwargs):
        uuid = "51405cc7-f7f3-4911-8061-66bf00c1f0a4"
        cmd = "show tunnel"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
