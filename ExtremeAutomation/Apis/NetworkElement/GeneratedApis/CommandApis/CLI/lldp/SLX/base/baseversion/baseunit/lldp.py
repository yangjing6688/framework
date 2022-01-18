"""
All lldp supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.lldp.base.lldpbase import LldpBase


class Lldp(DeviceApi, LldpBase):
    def __init__(self, device_input):
        super(Lldp, self).__init__(device_input)

    def enable(self, arg_dictionary, **kwargs):
        uuid = "67f68e1a-af05-4d32-88a4-cc8e0f989c1d"
        cmd = "protocol lldp||no disable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable(self, arg_dictionary, **kwargs):
        uuid = "aeb4b061-2335-490b-8db6-3006da23f70c"
        cmd = "protocol lldp||disable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_tx(self, arg_dictionary, **kwargs):
        uuid = "f8731a63-99ec-43da-8014-df6422405b96"
        cmd = "protocol lldp||mode tx"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_rx(self, arg_dictionary, **kwargs):
        uuid = "be159c63-7f03-4bb2-b299-78ecf619481f"
        cmd = "protocol lldp||mode rx"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port_both(self, arg_dictionary, **kwargs):
        uuid = "b674aaf4-2510-4811-9f2e-e11b1bc7a612"
        cmd = "no lldp disable "
        prompt = "intfPrompt"
        prompt_args = "interface ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "9e2d8119-4960-41d5-9bc6-252c40fc311b"
        cmd = "lldp disable"
        prompt = "intfPrompt"
        prompt_args = "interface ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_tx_interval(self, arg_dictionary, **kwargs):
        uuid = "6d9bd153-8795-4c40-95f3-2a06039393b9"
        cmd = "protocol lldp||hello {0}".format(arg_dictionary['interval'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_sys_name(self, arg_dictionary, **kwargs):
        uuid = "fe626814-f3f4-42ac-944c-40400ddaa99f"
        cmd = "protocol lldp||system-name}"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_sys_name(self, arg_dictionary, **kwargs):
        uuid = "93ea05f4-ff67-417c-a8a9-4a783a235148"
        cmd = "protocol lldp||no system-name {0}".format(arg_dictionary['name'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile(self, arg_dictionary, **kwargs):
        uuid = "a64f240a-088e-441c-84ce-af505854e62e"
        cmd = "protocol lldp||profile {0}".format(arg_dictionary['profile'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile_interface(self, arg_dictionary, **kwargs):
        uuid = "31de4be9-c656-4bd9-a8d0-6a0aa35b9827"
        cmd = "lldp profile {0}".format(arg_dictionary['profile'])
        prompt = "intfPrompt"
        prompt_args = "interface ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_tx_hold_multiplier(self, arg_dictionary, **kwargs):
        uuid = "66eb3cef-0c24-4f81-b8f4-123be3838a24"
        cmd = "protocol lldp||multiplier {0}".format(arg_dictionary['multiplier'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "62450147-99e0-443c-aaad-b21b4c9925d1"
        cmd = "show lldp"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_status(self, arg_dictionary, **kwargs):
        uuid = "48a749d4-bcb4-4e9c-8f11-c3922d86b571"
        cmd = "show lldp interface ethernet {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_neighbors(self, arg_dictionary, **kwargs):
        uuid = "1699e38a-323c-4bfc-84c1-6da0e3d38c26"
        cmd = "show lldp neighbors"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_neighbors_detail(self, arg_dictionary, **kwargs):
        uuid = "b1129059-c017-4c0c-8a72-c504643e9225"
        cmd = "show lldp neighbors detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_neighbors_port(self, arg_dictionary, **kwargs):
        uuid = "47393c00-d263-482f-a18f-c55e07a57da9"
        cmd = "show lldp neighbors interface ethernet {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_neighbors_port_detail(self, arg_dictionary, **kwargs):
        uuid = "bb1be6ca-c87d-41ea-8120-029d9437c3f8"
        cmd = "show lldp neighbors interface ethernet {0} detail".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_statistics(self, arg_dictionary, **kwargs):
        uuid = "98be780a-6dc7-4681-a41b-c22ab3472db8"
        cmd = "show lldp statistics"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_statistics_port(self, arg_dictionary, **kwargs):
        uuid = "7e12d9d4-a6cd-418e-a4b8-e54a245fb542"
        cmd = "show lldp statistics interface ethernet {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
