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
        cmd = "set igmp enable {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "641501ff-2725-4c7b-bd1b-d2712089faef"
        cmd = "set igmp enable {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "8cf98d6c-2531-4707-8e13-610bbbe5b015"
        cmd = "set igmp disable {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_version(self, arg_dictionary, **kwargs):
        uuid = "b4ec33ba-8bd1-4b3c-91c8-9d60afeb97ba"
        cmd = "show igmp config {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "7b779ef2-9d5c-4543-ac6d-dfb5b7740cd9"
        cmd = "show igmp config"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
