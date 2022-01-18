"""
All dot1x supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.dot1x.base.dot1xbase import Dot1xBase


class Dot1x(DeviceApi, Dot1xBase):
    def __init__(self, device_input):
        super(Dot1x, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "7b0b9598-8ab6-4fb1-9a1a-2a70d2d7b84d"
        cmd = "set dot1x enable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "f5a6aba6-a97a-49b6-897b-184fe1413559"
        cmd = "set dot1x disable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port(self, arg_dictionary, **kwargs):
        uuid = "0b6ac4b0-e68f-41fb-83d0-61b5efad8298"
        cmd = "set dot1x auth-config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "2fc45446-9678-4cef-a9d5-d85bcb6c6f50"
        cmd = "set dot1x auth-config {0} dot1x".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_accounting(self, arg_dictionary, **kwargs):
        uuid = "b2670baa-5592-40ed-8e79-763d10c67409"
        cmd = "set dot1x accounting enable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_accounting(self, arg_dictionary, **kwargs):
        uuid = "f01a6ac2-535a-4078-a1b8-9fae0ee50d1e"
        cmd = "set dot1x accounting disable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_global_idle_timeout(self, arg_dictionary, **kwargs):
        uuid = "62596a7e-b3ae-4286-b634-039363c01ea4"
        cmd = "set multiauth idle-timeout dot1x {0}".format(arg_dictionary['idle_timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_global_session_timeout(self, arg_dictionary, **kwargs):
        uuid = "131894fa-f305-46af-a606-741c3a67f0ca"
        cmd = "set multiauth session-timeout dot1x {0}".format(arg_dictionary['session_timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_quietperiod(self, arg_dictionary, **kwargs):
        uuid = "21a6cf1d-694e-4f9f-a587-0cb643127371"
        cmd = "set dot1x auth-config quietperiod {0} {1}".format(arg_dictionary['quiet_period'],
                                                                 arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "f9c6bfc2-485e-4aa9-8ea0-ba3be2051102"
        cmd = "set dot1x auth-config reauthperiod {0} {1}".format(arg_dictionary['reauth_period'],
                                                                  arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_servertimeout(self, arg_dictionary, **kwargs):
        uuid = "66d31349-846e-4db2-9ee6-d4a3e81620ee"
        cmd = "set dot1x auth-config servertimeout {0} {1}".format(arg_dictionary['server_timeout'],
                                                                   arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_supp_resptimeout(self, arg_dictionary, **kwargs):
        uuid = "65a2913f-e3ba-4e5f-bf2e-9e865e801a57"
        cmd = "set dot1x auth-config supptimeout {0} {1}".format(arg_dictionary['supp_resp_timeout'],
                                                                 arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_global_idle_timeout(self, arg_dictionary, **kwargs):
        uuid = "132be284-138d-4b85-b45c-fcf91b942d5e"
        cmd = "clear multiauth idle-timeout dot1x"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_global_session_timeout(self, arg_dictionary, **kwargs):
        uuid = "9bd13fd4-6635-4a21-b02f-5bb000a753d6"
        cmd = "clear multiauth session-timeout dot1x"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port_state(self, arg_dictionary, **kwargs):
        uuid = "621a3d31-11ee-4625-a7e3-8d76719ed9e2"
        cmd = "clear dot1x auth-config {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "5d0e205f-703d-4c13-92da-28a54ae522a7"
        cmd = "clear dot1x auth-config reauthperiod {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
