"""
All igmp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.igmp.base.igmpbase import IgmpBase


class Igmp(DeviceApi, IgmpBase):
    def __init__(self, device_input):
        super(Igmp, self).__init__(device_input)

    def set_version(self, arg_dictionary, **kwargs):
        uuid = "0aadf5bd-92a0-4eb4-808e-41d4b8cac082"
        cmd = "enable igmp vlan {0} {1}".format(arg_dictionary['vlan_name'],
                                                arg_dictionary['igmp_ver'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "641501ff-2725-4c7b-bd1b-d2712089faef"
        cmd = "enable igmp vlan {0}".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "8cf98d6c-2531-4707-8e13-610bbbe5b015"
        cmd = "disable igmp vlan {0}".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping(self, arg_dictionary, **kwargs):
        uuid = "ad3dcd6a-80e3-4722-987c-c0cfe19a9cf0"
        cmd = "enable igmp snooping"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping(self, arg_dictionary, **kwargs):
        uuid = "33b24c3b-bf5b-4bc3-ae3b-b40feeb4dd32"
        cmd = "disable igmp snooping"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_vlan(self, arg_dictionary, **kwargs):
        uuid = "60d3ecc1-10ff-48e2-ae92-69fa5da82b0c"
        cmd = "enable igmp snooping vlan {0}".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_vlan(self, arg_dictionary, **kwargs):
        uuid = "1631f48a-be31-4588-974f-c24c337c12f5"
        cmd = "disable igmp snooping vlan {0}".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_snooping_proxy(self, arg_dictionary, **kwargs):
        uuid = "0196a404-68d8-4b0f-83f1-433fc6432474"
        cmd = "enable igmp snooping with-proxy"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_snooping_proxy(self, arg_dictionary, **kwargs):
        uuid = "76d57f2c-571e-45b2-b5c0-0a207ba0d9dc"
        cmd = "disable igmp snooping with-proxy"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_version(self, arg_dictionary, **kwargs):
        uuid = "b4ec33ba-8bd1-4b3c-91c8-9d60afeb97ba"
        cmd = "show igmp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "7b779ef2-9d5c-4543-ac6d-dfb5b7740cd9"
        cmd = "show igmp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan(self, arg_dictionary, **kwargs):
        uuid = "cba4b245-18c5-44fe-ab3c-28a8cdd281bf"
        cmd = "show igmp vlan {0}".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_group(self, arg_dictionary, **kwargs):
        uuid = "7f377619-0c96-4bad-b335-662383a5e945"
        cmd = "show igmp group"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
