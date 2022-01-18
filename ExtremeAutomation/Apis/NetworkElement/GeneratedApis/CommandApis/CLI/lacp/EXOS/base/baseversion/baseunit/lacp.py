"""
All lacp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.lacp.base.lacpbase import LacpBase


class Lacp(DeviceApi, LacpBase):
    def __init__(self, device_input):
        super(Lacp, self).__init__(device_input)

    def create_lag(self, arg_dictionary, **kwargs):
        uuid = "6733e1f6-de56-41fd-ac2c-11de35c9a645"
        cmd = "enable sharing {0} grouping {1} lacp".format(arg_dictionary['main_lag_port'],
                                                            arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_lag(self, arg_dictionary, **kwargs):
        uuid = "1b7b971a-1b19-44a3-939a-cf482658c94b"
        cmd = "disable sharing {0}".format(arg_dictionary['main_lag_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_lag_port(self, arg_dictionary, **kwargs):
        uuid = "f8f70a5c-2f8b-4c22-9086-818a010990a2"
        cmd = "configure sharing {0} add ports {1}".format(arg_dictionary['main_lag_port'],
                                                           arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_lag_port(self, arg_dictionary, **kwargs):
        uuid = "e96bb2e6-e508-437f-92d3-9b5ce6b1c3f0"
        cmd = "unconfigure sharing {0} delete ports {1}".format(arg_dictionary['main_lag_port'],
                                                                arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "8fce70a1-95e7-48ef-ad00-c5980b9c5025"
        cmd = "show lacp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_lag_info(self, arg_dictionary, **kwargs):
        uuid = "54ab7d26-c328-4646-a763-c0745b816128"
        cmd = "show lacp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_lag(self, arg_dictionary, **kwargs):
        uuid = "aa67c54a-05ba-4169-a0e0-2b30a5e136c4"
        cmd = "show ports {0} sharing detail".format(arg_dictionary['main_lag_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
