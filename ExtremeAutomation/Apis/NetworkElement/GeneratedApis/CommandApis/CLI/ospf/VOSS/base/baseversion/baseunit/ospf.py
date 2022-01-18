"""
All ospf supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.ospf.base.ospfbase import OspfBase


class Ospf(DeviceApi, OspfBase):
    def __init__(self, device_input):
        super(Ospf, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "aad90010-4be0-4857-b591-ff4a17af18be"
        cmd = "router ospf enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "f38e1877-724f-4c29-a5c7-1a2dfc41aa2b"
        cmd = "no router ospf"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_router_id(self, arg_dictionary, **kwargs):
        uuid = "6548157c-4534-476f-89fb-ae4539384372"
        cmd = "router ospf||router-id {0}".format(arg_dictionary['router_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_router_id(self, arg_dictionary, **kwargs):
        uuid = "43074a74-1bf6-4d37-af45-3339a6a9228f"
        cmd = "router ospf||no router-id"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_interface(self, arg_dictionary, **kwargs):
        uuid = "efe8461c-4ad1-4918-9900-d97c63061910"
        cmd = "ip ospf enable"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['interface'])
        conf = "(y/n)"
        conf_args = "y"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args, conf=conf, conf_args=conf_args)

    def disable_interface(self, arg_dictionary, **kwargs):
        uuid = "37fb3e9a-06f3-42e2-99a3-0e5759a2fa50"
        cmd = "no ip ospf"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "c067043c-05db-4e0c-9958-1e75285b0ae1"
        cmd = "ip ospf enable"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['vlan'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "4856dfed-abcb-49a8-97f2-e8b9cc659943"
        cmd = "no ip ospf enable"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['vlan'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "7cb9490c-58e2-4982-a677-dffd12962348"
        cmd = "show ip ospf"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan_interface(self, arg_dictionary, **kwargs):
        uuid = "35b16b05-2cb2-42d9-bcff-849392b7a49b"
        cmd = "show ip ospf interface vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interface(self, arg_dictionary, **kwargs):
        uuid = "533ab02d-5999-4a75-bf9a-1211d4db7905"
        cmd = "show interfaces GigabitEthernet ospf {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
