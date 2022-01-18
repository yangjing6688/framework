"""
All lacp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.lacp.base.lacpbase import LacpBase


class Lacp(DeviceApi, LacpBase):
    def __init__(self, device_input):
        super(Lacp, self).__init__(device_input)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "257a08f4-5e78-4a35-a853-35372913ec5c"
        cmd = "interface ethernet {0}||channel-group {1} mode passive".format(arg_dictionary['main_lag_port'],
                                                                              arg_dictionary['key'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port(self, arg_dictionary, **kwargs):
        uuid = "8ce4b9f2-e3f0-4fde-8d60-204af927bfa9"
        cmd = "interface ethernet {0}||channel-group {1} mode active".format(arg_dictionary['main_lag_port'],
                                                                             arg_dictionary['key'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_lag(self, arg_dictionary, **kwargs):
        uuid = "6733e1f6-de56-41fd-ac2c-11de35c9a645"
        cmd = "interface ethernet {0}||channel-group {1} mode on".format(arg_dictionary['main_lag_port'],
                                                                         arg_dictionary['key'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_lag(self, arg_dictionary, **kwargs):
        uuid = "1b7b971a-1b19-44a3-939a-cf482658c94b"
        cmd = "interface ethernet {0}||no channel-group {1}".format(arg_dictionary['main_lag_port'],
                                                                    arg_dictionary['key'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_priority(self, arg_dictionary, **kwargs):
        uuid = "52f86761-45c0-4eac-9760-5ae60331f9ad"
        cmd = "interface ethernet {0}||lacp port-priority {1}".format(arg_dictionary['main_lag_port'],
                                                                      arg_dictionary['priority'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_system_priority(self, arg_dictionary, **kwargs):
        uuid = "375da013-e36e-427e-96f7-d3d1a93eae15"
        cmd = "lacp system-priority {0}".format(arg_dictionary['priority'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_lag_port(self, arg_dictionary, **kwargs):
        uuid = "f8f70a5c-2f8b-4c22-9086-818a010990a2"
        cmd = "interface ethernet {0}||channel-group {1} mode on".format(arg_dictionary['main_lag_port'],
                                                                         arg_dictionary['key'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_lag_port(self, arg_dictionary, **kwargs):
        uuid = "e96bb2e6-e508-437f-92d3-9b5ce6b1c3f0"
        cmd = "interface ethernet {0}||no channel-group {1}".format(arg_dictionary['main_lag_port'],
                                                                    arg_dictionary['key'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_counters(self, arg_dictionary, **kwargs):
        uuid = "6aa9f95c-0e55-4293-9a92-f434cade9f20"
        cmd = "clear lacp {0} counters".format(arg_dictionary['port_channel'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_all_counters(self, arg_dictionary, **kwargs):
        uuid = "5de1719c-872a-41d7-9013-8930edadad8d"
        cmd = "clear lacp counters"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_lag_info(self, arg_dictionary, **kwargs):
        uuid = "54ab7d26-c328-4646-a763-c0745b816128"
        cmd = "show interface port-channel {0}".format(arg_dictionary['main_lag_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_counter(self, arg_dictionary, **kwargs):
        uuid = "63358f3c-9b19-4554-96f2-5e6445c9e5d1"
        cmd = "show lacp counter {0}".format(arg_dictionary['interface'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_sysid(self, arg_dictionary, **kwargs):
        uuid = "97fa1e24-c39c-43ce-903f-6b1e363a968c"
        cmd = "show lacp sys-id"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
