"""
All vlan supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.vlan.base.vlanbase import VlanBase


class Vlan(DeviceApi, VlanBase):
    def __init__(self, device_input):
        super(Vlan, self).__init__(device_input)

    def show_all_info(self, arg_dictionary, **kwargs):
        uuid = "665c60ed-ab31-4ccd-9b85-7946db3c01a3"
        cmd = "show vlan"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "62cb48f8-848b-4604-a67b-5e135a96d45a"
        cmd = "show vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_name(self, arg_dictionary, **kwargs):
        uuid = "48cf27a1-71fd-4212-85a3-12db4d2f899d"
        cmd = "show vlan {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_pvid(self, arg_dictionary, **kwargs):
        uuid = "49369c19-a5c0-4518-bd93-317d7ff99061"
        cmd = "show vlan port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
