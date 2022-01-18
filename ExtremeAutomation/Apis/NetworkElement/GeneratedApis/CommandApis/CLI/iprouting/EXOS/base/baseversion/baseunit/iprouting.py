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
        cmd = "configure iproute add {0} {1}".format(arg_dictionary['route'],
                                                     arg_dictionary['nexthop'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_static_route(self, arg_dictionary, **kwargs):
        uuid = "cbc5ea79-a20b-4553-ac1f-60b32d1516d5"
        cmd = "configure iproute delete {0} {1}".format(arg_dictionary['route'],
                                                        arg_dictionary['nexthop'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipmcforwarding_global(self, arg_dictionary, **kwargs):
        uuid = "f69ae499-5b57-4e24-8987-a14d44cd3481"
        cmd = "enable ipmcforwarding"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipmcforwarding_ipv4_global(self, arg_dictionary, **kwargs):
        uuid = "32e171b5-6551-4db1-8ee2-0f6a864d50fc"
        cmd = "enable ipmcforwarding ipv4"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipmcforwarding_ipv6_global(self, arg_dictionary, **kwargs):
        uuid = "392d0585-b01e-4d9f-8142-02372f1cc973"
        cmd = "enable ipmcforwarding ipv6"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipmcforwarding_ipv4_vlan(self, arg_dictionary, **kwargs):
        uuid = "0ae7168d-3108-4462-b0e7-94f3b8f38310"
        cmd = "enable ipmcforwarding ipv4 vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_ipmcforwarding_ipv6_vlan(self, arg_dictionary, **kwargs):
        uuid = "16e0d041-734c-4eb9-a721-9a4ba9ff1279"
        cmd = "enable ipmcforwarding ipv6 vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipmcforwarding_global(self, arg_dictionary, **kwargs):
        uuid = "debea284-1bd3-4f2f-995e-9a4b3763b3b1"
        cmd = "disable ipmcforwarding"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipmcforwarding_ipv4_global(self, arg_dictionary, **kwargs):
        uuid = "b82960d4-7270-4d1c-b212-0cefcaa26d93"
        cmd = "disable ipmcforwarding ipv4"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipmcforwarding_ipv6_global(self, arg_dictionary, **kwargs):
        uuid = "e9b994c9-9b5e-4f22-88b3-014c36d5a7d8"
        cmd = "disable ipmcforwarding ipv6"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipmcforwarding_ipv4_vlan(self, arg_dictionary, **kwargs):
        uuid = "8a8946e9-5ac9-433a-be25-b5a9bdd8d02a"
        cmd = "disable ipmcforwarding ipv4 vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_ipmcforwarding_ipv6_vlan(self, arg_dictionary, **kwargs):
        uuid = "545b5ccb-1043-46e1-925a-35a934e7dae1"
        cmd = "disable ipmcforwarding ipv6 vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_static_route(self, arg_dictionary, **kwargs):
        uuid = "5b410683-0304-4499-b01e-1e45e72be629"
        cmd = "show iproute origin static"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_all_routes(self, arg_dictionary, **kwargs):
        uuid = "6c9cabb5-a09c-4778-b656-f394027fed95"
        cmd = "show iproute"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
