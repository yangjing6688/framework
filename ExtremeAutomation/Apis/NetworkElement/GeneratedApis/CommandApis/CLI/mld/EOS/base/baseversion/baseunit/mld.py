"""
All mld supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.mld.base.mldbase import MldBase


class Mld(DeviceApi, MldBase):
    def __init__(self, device_input):
        super(Mld, self).__init__(device_input)

    def enable_vlan(self, arg_dictionary, **kwargs):
        uuid = "fdf9ef13-b6e0-4e40-9778-b37009e57b73"
        cmd = "set mld enable {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_vlan(self, arg_dictionary, **kwargs):
        uuid = "ac01e9f9-216e-4148-b8d9-9c814f561fca"
        cmd = "set mld disable {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_version(self, arg_dictionary, **kwargs):
        uuid = "c5dafbcc-5015-4322-9fd1-6a56cadbedde"
        cmd = "set mld config {0} mld-version {1}".format(arg_dictionary['vlan'],
                                                          arg_dictionary['version'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan(self, arg_dictionary, **kwargs):
        uuid = "5a011cd7-4ac2-4c80-83a3-77739dfe7063"
        cmd = "show mld config"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_version(self, arg_dictionary, **kwargs):
        uuid = "f2376d5c-ee82-4fb3-83a4-00b9492c2c03"
        cmd = "show mld config {0}".format(arg_dictionary['vlan'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
