"""
All lacp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.lacp.base.lacpbase import LacpBase


class Lacp(DeviceApi, LacpBase):
    def __init__(self, device_input):
        super(Lacp, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "a3aab87a-4811-4a23-b823-a24e6dd3edb0"
        cmd = "lacp enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "7893b72a-32d1-4372-beac-c5599e185374"
        cmd = "no lacp enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def create_lag(self, arg_dictionary, **kwargs):
        uuid = "6733e1f6-de56-41fd-ac2c-11de35c9a645"
        cmd = "interface {0}||lacp key {1} aggregation enable||lacp enable||exit".format(arg_dictionary['main_lag_port'],
                                                                                         arg_dictionary['key'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_lag(self, arg_dictionary, **kwargs):
        uuid = "1b7b971a-1b19-44a3-939a-cf482658c94b"
        cmd = "interface {0}||no lacp aggregation enable".format(arg_dictionary['main_lag_port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_lag_port(self, arg_dictionary, **kwargs):
        uuid = "f8f70a5c-2f8b-4c22-9086-818a010990a2"
        cmd = "interface {0}||lacp aggregation enable||lacp enable||exit".format(arg_dictionary['main_lag_port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_lag_port(self, arg_dictionary, **kwargs):
        uuid = "e96bb2e6-e508-437f-92d3-9b5ce6b1c3f0"
        cmd = "interface {0}||no lacp aggregation enable||no lacp enable".format(arg_dictionary['main_lag_port'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "8fce70a1-95e7-48ef-ad00-c5980b9c5025"
        cmd = "show lacp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_lag_info(self, arg_dictionary, **kwargs):
        uuid = "54ab7d26-c328-4646-a763-c0745b816128"
        cmd = "show lacp||show lacp interface gigabitethernet {0}".format(arg_dictionary['main_lag_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_all(self, arg_dictionary, **kwargs):
        uuid = "aac2b104-bf1d-441c-99ec-8767d1aa2699"
        cmd = "show lacp interface gigabitethernet {0}".format(arg_dictionary['main_lag_port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mlt_port(self, arg_dictionary, **kwargs):
        uuid = "13eb0ca6-2f5f-4abf-b877-3825fa9fa980"
        cmd = "show lacp interface mlt id {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mlt_id_logical_index(self, arg_dictionary, **kwargs):
        uuid = "5267dee0-dbe1-4295-9356-b54d56fb36b3"
        cmd = "show mlt {0}".format(arg_dictionary['mlt_id'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
