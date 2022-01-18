"""
All macauth supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.macauth.base.macauthbase import MacauthBase


class Macauth(DeviceApi, MacauthBase):
    def __init__(self, device_input):
        super(Macauth, self).__init__(device_input)

    def enable(self, arg_dictionary, **kwargs):
        uuid = "f2f65c83-6b78-416f-9da0-ce91a8fdd90c"
        cmd = "set macauth enable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable(self, arg_dictionary, **kwargs):
        uuid = "d9ddd942-7c57-4736-b409-553c04fc2b41"
        cmd = "set macauth disable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port_reauthentication(self, arg_dictionary, **kwargs):
        uuid = "395b1bb6-11c5-4d30-a119-7a0b3eee5a9f"
        cmd = "set macauthentication reauthentication enable {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port_reauthentication(self, arg_dictionary, **kwargs):
        uuid = "d37a9da1-aa27-4025-949f-2b129c472ae1"
        cmd = "set macauthentication reauthentication disable {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_password(self, arg_dictionary, **kwargs):
        uuid = "d0055eb3-42e5-4708-a5d5-54f1aa980922"
        cmd = "set macauth password {0}".format(arg_dictionary['password'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_state(self, arg_dictionary, **kwargs):
        uuid = "ab8fafa9-3f90-4174-9b16-3a3e7fd83a6f"
        cmd = "set macauth port {0} {1}".format(self.api_utils.state_enable_disable(arg_dictionary['state']),
                                                arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "fd91672c-7db0-488e-9ce6-2e7ae0e5b96d"
        cmd = "set macauth reauthperiod {0} {1}".format(arg_dictionary['interval'],
                                                        arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_quietperiod(self, arg_dictionary, **kwargs):
        uuid = "786b6a37-d736-4d98-bd54-0b57bd046e9e"
        cmd = "set macauth quietperiod {0} {1}".format(arg_dictionary['sec'],
                                                       arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_password(self, arg_dictionary, **kwargs):
        uuid = "135bdb30-0b17-4c8d-a2e7-7984dce2336d"
        cmd = "clear macauth password "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "9dd7a148-6bb3-43f1-b332-673a0737ea8a"
        cmd = "clear macauth reauthperiod {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port_quietperiod(self, arg_dictionary, **kwargs):
        uuid = "5f084e54-30c8-49e8-ae95-8bc4532991da"
        cmd = "clear macauth quietperiod {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show(self, arg_dictionary, **kwargs):
        uuid = "2e73c468-f660-4e8b-9098-ddcafd5eb76d"
        cmd = "show macauthentication"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "9fff3204-4fa6-40c2-871e-a9d512f451bc"
        cmd = "show macauth {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
