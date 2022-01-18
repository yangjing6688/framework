"""
All poe supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.poe.base.poebase import PoeBase


class Poe(DeviceApi, PoeBase):
    def __init__(self, device_input):
        super(Poe, self).__init__(device_input)

    def enable_port(self, arg_dictionary, **kwargs):
        uuid = "d85ded5e-243f-4062-bd8d-ac66eb95dda9"
        cmd = "no poe-shutdown"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "5147e9d2-fd97-4272-b558-aa5299f90122"
        cmd = "poe poe-shutdown"
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_power_usage_threshold(self, arg_dictionary, **kwargs):
        uuid = "142af738-8794-4d20-ab2d-9786dbeeda98"
        cmd = "poe poe-power-usage-threshold {0}".format(arg_dictionary['threshold'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_power_limit(self, arg_dictionary, **kwargs):
        uuid = "d7b94cad-7944-4f3e-8d18-13f8fb4588f1"
        cmd = "poe poe-limit {0}".format(arg_dictionary['power_limit'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_power_priority(self, arg_dictionary, **kwargs):
        uuid = "c1d24df9-00f0-496a-b3f8-29e7b1e5ff8f"
        cmd = "poe poe-priority {0}".format(arg_dictionary['power_priority'])
        prompt = "intfPrompt"
        prompt_args = "GigabitEthernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_power_usage_threshold(self, arg_dictionary, **kwargs):
        uuid = "72e7d69c-ce86-4112-b797-752234b16114"
        cmd = "show poe-main-status"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_status(self, arg_dictionary, **kwargs):
        uuid = "4251b8a5-a8e8-4721-b7e3-4ac80ca6c683"
        cmd = "show poe-port-status {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_measurements(self, arg_dictionary, **kwargs):
        uuid = "83d03a4d-fbda-4712-9821-add3bd61075a"
        cmd = "show poe-power-measurement {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_power_limit(self, arg_dictionary, **kwargs):
        uuid = "9739e6ed-4d06-474c-b10e-6b2ce08243e0"
        cmd = "show poe-port-status {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_power_priority(self, arg_dictionary, **kwargs):
        uuid = "f6e29478-e3f0-44c1-bca7-7759b689b892"
        cmd = "show poe-port-status {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_detection_status(self, arg_dictionary, **kwargs):
        uuid = "b1a45e73-1513-495c-bd1e-8736af39962b"
        cmd = "show poe-port-status {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_power_classification(self, arg_dictionary, **kwargs):
        uuid = "c4ec8d10-3227-4f12-b170-cac9f3dc6101"
        cmd = "show poe-port-status {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_global_status(self, arg_dictionary, **kwargs):
        uuid = "cc6195c1-c167-4510-80eb-f5be4c095563"
        cmd = "show poe-main-status"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
