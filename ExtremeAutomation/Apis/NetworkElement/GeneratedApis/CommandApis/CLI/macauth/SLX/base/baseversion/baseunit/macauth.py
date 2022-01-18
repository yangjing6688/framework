"""
All macauth supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.macauth.base.macauthbase import MacauthBase


class Macauth(DeviceApi, MacauthBase):
    def __init__(self, device_input):
        super(Macauth, self).__init__(device_input)

    def set_port_state(self, arg_dictionary, **kwargs):
        uuid = "ab8fafa9-3f90-4174-9b16-3a3e7fd83a6f"
        cmd = "{0} endpoint-tracking enable".format(self.api_utils.state_no_empty(arg_dictionary['state']))
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "fd91672c-7db0-488e-9ce6-2e7ae0e5b96d"
        cmd = "endpoint-tracking timeout reauth-period {0}".format(arg_dictionary['interval'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "9dd7a148-6bb3-43f1-b332-673a0737ea8a"
        cmd = "no endpoint-tracking timeout reauth-period"
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "9fff3204-4fa6-40c2-871e-a9d512f451bc"
        cmd = "show running-config interface ethernet {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port_authentication(self, arg_dictionary, **kwargs):
        uuid = "373e5598-b4ba-4214-aa38-e55ccee04966"
        cmd = "show mac-address-table endpoint-tracking authenticated interface ethernet {0}||show mac-address-table endpoint-tracking authentication-failed interface ethernet {1}".format(arg_dictionary['port'],
                                                                                                                                                                                            arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
