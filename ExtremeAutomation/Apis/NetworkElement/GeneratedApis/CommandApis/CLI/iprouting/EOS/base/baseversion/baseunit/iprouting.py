"""
All iprouting supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.iprouting.base.iproutingbase import \
    IproutingBase


class Iprouting(DeviceApi, IproutingBase):
    def __init__(self, device_input):
        super(Iprouting, self).__init__(device_input)

    def create_static_route(self, arg_dictionary, **kwargs):
        uuid = "ae2bcfeb-eb32-4a9c-a98c-10dd40a7527f"
        cmd = "ip route {0} {1}".format(arg_dictionary['route'],
                                        arg_dictionary['nexthop'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_static_route(self, arg_dictionary, **kwargs):
        uuid = "cbc5ea79-a20b-4553-ac1f-60b32d1516d5"
        cmd = "no ip route {0} {1}".format(arg_dictionary['route'],
                                           arg_dictionary['nexthop'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_static_route(self, arg_dictionary, **kwargs):
        uuid = "5b410683-0304-4499-b01e-1e45e72be629"
        cmd = "show ip route static"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_routes(self, arg_dictionary, **kwargs):
        uuid = "6c9cabb5-a09c-4778-b656-f394027fed95"
        cmd = "show ip route"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
