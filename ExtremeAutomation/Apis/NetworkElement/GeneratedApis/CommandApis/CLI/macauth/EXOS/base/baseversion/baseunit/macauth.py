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
        cmd = "enable netlogin mac"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable(self, arg_dictionary, **kwargs):
        uuid = "d9ddd942-7c57-4736-b409-553c04fc2b41"
        cmd = "disable netlogin mac"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port_reauthentication(self, arg_dictionary, **kwargs):
        uuid = "395b1bb6-11c5-4d30-a119-7a0b3eee5a9f"
        cmd = "configure netlogin mac ports {0} timers reauthentication on".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port_reauthentication(self, arg_dictionary, **kwargs):
        uuid = "d37a9da1-aa27-4025-949f-2b129c472ae1"
        cmd = "configure netlogin mac ports {0} timers reauthentication off".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_password(self, arg_dictionary, **kwargs):
        uuid = "d0055eb3-42e5-4708-a5d5-54f1aa980922"
        cmd = "configure netlogin add mac-list default password {0}".format(arg_dictionary['password'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_state(self, arg_dictionary, **kwargs):
        uuid = "ab8fafa9-3f90-4174-9b16-3a3e7fd83a6f"
        cmd = "{0} netlogin port {1} mac".format(self.api_utils.state_enable_disable(arg_dictionary['state']),
                                                 arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "fd91672c-7db0-488e-9ce6-2e7ae0e5b96d"
        cmd = "configure netlogin mac ports {0} timers reauth-period {1}".format(arg_dictionary['port'],
                                                                                 arg_dictionary['interval'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_quietperiod(self, arg_dictionary, **kwargs):
        uuid = "786b6a37-d736-4d98-bd54-0b57bd046e9e"
        cmd = "configure netlogin mac ports {0} timers delay {1}".format(arg_dictionary['port'],
                                                                         arg_dictionary['sec'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_password(self, arg_dictionary, **kwargs):
        uuid = "135bdb30-0b17-4c8d-a2e7-7984dce2336d"
        cmd = "configure netlogin delete mac-list default"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "9dd7a148-6bb3-43f1-b332-673a0737ea8a"
        cmd = "configure netlogin mac ports {0} timers reauth-period 3600".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port_quietperiod(self, arg_dictionary, **kwargs):
        uuid = "5f084e54-30c8-49e8-ae95-8bc4532991da"
        cmd = "configure netlogin mac ports {0} timers delay 0".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mac_format_type(self, arg_dictionary, **kwargs):
        uuid = "da655f5c-3d52-4885-a016-8b5c84d5a3b4"
        cmd = "configure netlogin mac username format_type {0}".format(arg_dictionary['format_type'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mac_user(self, arg_dictionary, **kwargs):
        uuid = "723f1833-4212-484a-a564-59ab7230c267"
        cmd = "configure netlogin add mac-list {0} {1} password {2}".format(self.str_utils.normalize_mac(arg_dictionary['mac_addr']),
                                                                            arg_dictionary['mask'],
                                                                            arg_dictionary['password'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mac_user_nopass(self, arg_dictionary, **kwargs):
        uuid = "b4508d75-bc40-4a1a-8d53-8506c8db5abc"
        cmd = "configure netlogin add mac-list {0} {1}".format(self.str_utils.normalize_mac(arg_dictionary['mac_addr']),
                                                               arg_dictionary['mask'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "75dc4abd-f611-4221-982d-f7f16c7c70d6"
        cmd = "configure netlogin mac timers reauth-period {0}".format(arg_dictionary['interval'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_mac_user(self, arg_dictionary, **kwargs):
        uuid = "7cc9a61d-9629-486e-abaf-2c2d4e076b0b"
        cmd = "configure netlogin delete mac-list {0} {1}".format(self.str_utils.normalize_mac(arg_dictionary['mac_addr']),
                                                                  arg_dictionary['mask'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show(self, arg_dictionary, **kwargs):
        uuid = "2e73c468-f660-4e8b-9098-ddcafd5eb76d"
        cmd = "show netlogin mac"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "9fff3204-4fa6-40c2-871e-a9d512f451bc"
        cmd = "show config netlogin"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_mac_list(self, arg_dictionary, **kwargs):
        uuid = "eb354c10-8a72-4050-9084-f62e5361a144"
        cmd = "show netlogin mac-list"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
