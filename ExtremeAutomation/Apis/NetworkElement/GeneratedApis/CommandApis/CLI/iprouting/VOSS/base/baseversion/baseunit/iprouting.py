"""
All iprouting supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.iprouting.base.iproutingbase import \
    IproutingBase


class Iprouting(DeviceApi, IproutingBase):
    def __init__(self, device_input):
        super(Iprouting, self).__init__(device_input)

    def show_all_routes(self, arg_dictionary, **kwargs):
        uuid = "6c9cabb5-a09c-4778-b656-f394027fed95"
        cmd = "show ip route"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_ipv6_routes(self, arg_dictionary, **kwargs):
        uuid = "7471f376-354e-48ab-a981-144ea27263b1"
        cmd = "show ipv6 route"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ip_route_vrf(self, arg_dictionary, **kwargs):
        uuid = "00fb4403-703a-48bb-bb0f-6e564c51941e"
        cmd = "show ip route vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_ipv6_route_vrf(self, arg_dictionary, **kwargs):
        uuid = "2bfa0750-2851-462b-b868-68abbbb5d26c"
        cmd = "show ipv6 route vrf {0}".format(arg_dictionary['vrf_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
