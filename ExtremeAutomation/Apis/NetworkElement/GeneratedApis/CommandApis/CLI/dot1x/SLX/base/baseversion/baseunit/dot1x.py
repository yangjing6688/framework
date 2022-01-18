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
        cmd = "dot1x enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "f5a6aba6-a97a-49b6-897b-184fe1413559"
        cmd = "no dot1x enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_port(self, arg_dictionary, **kwargs):
        uuid = "0b6ac4b0-e68f-41fb-83d0-61b5efad8298"
        cmd = "no shutdown||dot1x authentication"
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_port(self, arg_dictionary, **kwargs):
        uuid = "2fc45446-9678-4cef-a9d5-d85bcb6c6f50"
        cmd = "no dot1x authentication"
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_port_reauth(self, arg_dictionary, **kwargs):
        uuid = "b857f372-423f-4548-9498-9798911bdfe4"
        cmd = "dot1x reauthentication"
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_port_reauth(self, arg_dictionary, **kwargs):
        uuid = "e3b49964-7ea8-4560-9702-389527bbb438"
        cmd = "no dot1x reauthentication"
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_quietperiod(self, arg_dictionary, **kwargs):
        uuid = "21a6cf1d-694e-4f9f-a587-0cb643127371"
        cmd = "dot1x quiet-period {0}".format(arg_dictionary['quiet_period'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "f9c6bfc2-485e-4aa9-8ea0-ba3be2051102"
        cmd = "dot1x timeout re-authperiod {0}".format(arg_dictionary['reauth_period'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_servertimeout(self, arg_dictionary, **kwargs):
        uuid = "66d31349-846e-4db2-9ee6-d4a3e81620ee"
        cmd = "dot1x timeout tx-period {0}".format(arg_dictionary['server_timeout'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_port_supp_resptimeout(self, arg_dictionary, **kwargs):
        uuid = "65a2913f-e3ba-4e5f-bf2e-9e865e801a57"
        cmd = "dot1x timeout supp-timeout {0}".format(arg_dictionary['supp_resp_timeout'])
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_port_reauthperiod(self, arg_dictionary, **kwargs):
        uuid = "5d0e205f-703d-4c13-92da-28a54ae522a7"
        cmd = "no dot1x timeout re-authperiod"
        prompt = "intfPrompt"
        prompt_args = "ethernet {0}".format(arg_dictionary['port'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def show_session_by_port(self, arg_dictionary, **kwargs):
        uuid = "70edc6d7-118e-4f77-bd17-e36a3d4a2f48"
        cmd = "show dot1x session-info interface ethernet {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_auth_cfg(self, arg_dictionary, **kwargs):
        uuid = "32cba31a-69dc-494b-af45-5af8bdce12cc"
        cmd = "show dot1x"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_auth_cfg_port(self, arg_dictionary, **kwargs):
        uuid = "9d54fa2e-011d-462e-9b63-80dc32f7b9a7"
        cmd = "show dot1x all"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
