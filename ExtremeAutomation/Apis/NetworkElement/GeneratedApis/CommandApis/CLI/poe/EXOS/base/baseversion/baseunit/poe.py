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
        cmd = "enable inline-power ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "5147e9d2-fd97-4272-b558-aa5299f90122"
        cmd = "disable inline-power ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_power_usage_threshold(self, arg_dictionary, **kwargs):
        uuid = "142af738-8794-4d20-ab2d-9786dbeeda98"
        cmd = "configure inline-power usage-threshold {0}".format(arg_dictionary['threshold'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_power_limit(self, arg_dictionary, **kwargs):
        uuid = "d7b94cad-7944-4f3e-8d18-13f8fb4588f1"
        cmd = "configure inline-power operator-limit {0} port {1}".format(arg_dictionary['power_limit'],
                                                                          arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_power_priority(self, arg_dictionary, **kwargs):
        uuid = "c1d24df9-00f0-496a-b3f8-29e7b1e5ff8f"
        cmd = "configure inline-power priority {0} ports {1}".format(arg_dictionary['power_priority'],
                                                                     arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_detect_type(self, arg_dictionary, **kwargs):
        uuid = "a1bb7007-736f-4b7f-ae63-16df0afdc9a2"
        cmd = "configure inline-power detection {0} port {1}".format(arg_dictionary['detect_type'],
                                                                     arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_power_usage_threshold(self, arg_dictionary, **kwargs):
        uuid = "72e7d69c-ce86-4112-b797-752234b16114"
        cmd = "show inline-power"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_status(self, arg_dictionary, **kwargs):
        uuid = "4251b8a5-a8e8-4721-b7e3-4ac80ca6c683"
        cmd = "show inline-power stats ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_power_limit(self, arg_dictionary, **kwargs):
        uuid = "9739e6ed-4d06-474c-b10e-6b2ce08243e0"
        cmd = "show inline-power configuration ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_power_priority(self, arg_dictionary, **kwargs):
        uuid = "f6e29478-e3f0-44c1-bca7-7759b689b892"
        cmd = "show inline-power configuration ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_detection_status(self, arg_dictionary, **kwargs):
        uuid = "b1a45e73-1513-495c-bd1e-8736af39962b"
        cmd = "show inline-power configuration ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_power_classification(self, arg_dictionary, **kwargs):
        uuid = "c4ec8d10-3227-4f12-b170-cac9f3dc6101"
        cmd = "show inline-power configuration ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_global_status(self, arg_dictionary, **kwargs):
        uuid = "cc6195c1-c167-4510-80eb-f5be4c095563"
        cmd = "show inline-power stats"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_detect_type(self, arg_dictionary, **kwargs):
        uuid = "c1e39a8b-22b3-451b-a18b-1109612238dd"
        cmd = "show inline-power config port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_inline_power(self, arg_dictionary, **kwargs):
        uuid = "8ec88be4-58f4-4d2f-9fd5-9094f40fd3bb"
        cmd = "enable inline-power"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_inline_power(self, arg_dictionary, **kwargs):
        uuid = "9025539e-fe7f-4b90-b9bf-e4a958e6cf1b"
        cmd = "disable inline-power"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_inline_power(self, arg_dictionary, **kwargs):
        uuid = "81267391-6ee1-4eab-90ea-c230b48cb963"
        cmd = "show inline-power"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_inline_power_info_port(self, arg_dictionary, **kwargs):
        uuid = "38692552-cf69-451a-884b-5ecb0fac87e6"
        cmd = "show inline-power info ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_inline_power_legacy(self, arg_dictionary, **kwargs):
        uuid = "6da49954-b1d9-4dd8-b905-15fd0609d2b6"
        cmd = "enable inline-power legacy"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_inline_power_legacy(self, arg_dictionary, **kwargs):
        uuid = "249d5f97-4872-4bad-b56c-2b60459937b0"
        cmd = "disable inline-power legacy"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_inline_power_legacy(self, arg_dictionary, **kwargs):
        uuid = "960f6737-efc4-48cc-ac9d-8864296ec0a1"
        cmd = "show inline-power config port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_inline_power_disconnect_deny_port(self, arg_dictionary, **kwargs):
        uuid = "fa8aaf1d-1d6d-4282-b05d-2c793c090fa7"
        cmd = "configure inline-power disconnect deny-port"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_inline_power_disconnect_lowest_priority(self, arg_dictionary, **kwargs):
        uuid = "f9469e5c-858b-47d7-95a0-7e84b457c937"
        cmd = "configure inline-power disconnect lowest-priority"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_inline_power_disconnect(self, arg_dictionary, **kwargs):
        uuid = "a88c6ba4-5483-4c51-ba5b-7e5ac5a4bdac"
        cmd = "unconfigure inline-power disconnect"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_inline_power_label(self, arg_dictionary, **kwargs):
        uuid = "83510d13-fdc3-4f04-8fb4-2cdaaa20beb5"
        cmd = "configure inline-power label {0} port {1}".format(arg_dictionary['test_label'],
                                                                 arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_inline_power_label(self, arg_dictionary, **kwargs):
        uuid = "56218313-92c6-4165-aaf5-45f0c6398a50"
        cmd = "show inline-power config port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_inline_power_operator_limit(self, arg_dictionary, **kwargs):
        uuid = "e98c8e08-fe3e-45d7-94c5-faa84e171287"
        cmd = "show inline-power config port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
