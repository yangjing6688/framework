"""
All upm supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.upm.base.upmbase import UpmBase


class Upm(DeviceApi, UpmBase):
    def __init__(self, device_input):
        super(Upm, self).__init__(device_input)

    def set_auth(self, arg_dictionary, **kwargs):
        uuid = "c6cbce2b-2f91-4a4a-931a-6042c77eb9fe"
        cmd = "configure upm event user-authenticate profile {0} ports {1}".format(arg_dictionary['auth_profile'],
                                                                                   arg_dictionary['ports'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_unauth(self, arg_dictionary, **kwargs):
        uuid = "e7482fb1-174d-420b-a7b5-3a36763cf8e9"
        cmd = "configure upm event user-unauthenticated profile {0} ports {1}".format(arg_dictionary['auth_profile'],
                                                                                      arg_dictionary['ports'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_profile(self, arg_dictionary, **kwargs):
        uuid = "bd69c272-33e8-431b-9be4-16d635825744"
        cmd = "create upm profile {0}||{1}".format(arg_dictionary['profile'],
                                                   self.api_utils.exos_upm_profile(arg_dictionary['lines']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_auth(self, arg_dictionary, **kwargs):
        uuid = "95f379bd-be9f-4ae1-83ac-c23737a2b94c"
        cmd = "unconfigure upm event user-authenticate profile {0} ports {1}".format(arg_dictionary['auth_profile'],
                                                                                     arg_dictionary['ports'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_unauth(self, arg_dictionary, **kwargs):
        uuid = "939cd1ba-fbc5-40f5-90dd-c6044e80764f"
        cmd = "unconfigure upm event user-unauthenticated profile {0} ports {1}".format(arg_dictionary['auth_profile'],
                                                                                        arg_dictionary['ports'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_auth_all_ports(self, arg_dictionary, **kwargs):
        uuid = "c3c20c34-ed79-4c78-83cf-5b65455c5ec1"
        cmd = "unconfigure upm event user-authenticate profile {0}".format(arg_dictionary['auth_profile'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_unauth_all_ports(self, arg_dictionary, **kwargs):
        uuid = "002a0aa5-e20f-451e-8554-5e49c875255f"
        cmd = "unconfigure upm event user-unauthenticated profile {0}".format(arg_dictionary['auth_profile'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_profile(self, arg_dictionary, **kwargs):
        uuid = "0d164f68-612b-4ecc-be4e-983749106921"
        cmd = "delete upm profile {0}".format(arg_dictionary['profile'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_event_authenticate(self, arg_dictionary, **kwargs):
        uuid = "4470ffb8-a43f-46ef-adf3-c92df8012cc6"
        cmd = "show upm event user-authenticate"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_event_unauthenticated(self, arg_dictionary, **kwargs):
        uuid = "32c36576-7b50-4278-9f26-588024d10204"
        cmd = "show upm event user-unauthenticated"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
