"""
All radius supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.radius.base.radiusbase import RadiusBase


class Radius(DeviceApi, RadiusBase):
    def __init__(self, device_input):
        super(Radius, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "6a794411-17ce-44a1-b80f-5f467d25a8d6"
        cmd = "set radius enable "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_acct(self, arg_dictionary, **kwargs):
        uuid = "d2154d3e-5129-4551-8e84-21fe67976ba5"
        cmd = "set radius accounting enable "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "9f41adce-7e97-45c2-addc-1b3b23dcdd4c"
        cmd = "set radius disable "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_acct(self, arg_dictionary, **kwargs):
        uuid = "55596503-345c-4584-9438-65aff18f58ea"
        cmd = "set radius accounting disable "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_server(self, arg_dictionary, **kwargs):
        uuid = "714d2b1e-d4bc-436a-8691-dbd3ac8209b6"
        cmd = "set radius server {0} {1} {2} {3}".format(arg_dictionary['index'],
                                                         arg_dictionary['addr'],
                                                         arg_dictionary['port'],
                                                         arg_dictionary['secret'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_acct_server(self, arg_dictionary, **kwargs):
        uuid = "c26d9e66-84f7-43c4-b51c-6b4a215fac5d"
        cmd = "set radius accounting server {0} {1} {2} {3}".format(arg_dictionary['index'],
                                                                    arg_dictionary['addr'],
                                                                    arg_dictionary['port'],
                                                                    arg_dictionary['secret'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_retries_global(self, arg_dictionary, **kwargs):
        uuid = "37ec7b4e-7453-456d-8567-6dc1c07c3813"
        cmd = "set radius retries {0}".format(arg_dictionary['num'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_timeout_global(self, arg_dictionary, **kwargs):
        uuid = "3c29d965-525b-4e5b-82c0-ae90f35ac1d1"
        cmd = "set radius timeout {0}".format(arg_dictionary['sec'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_algorithm_global_std(self, arg_dictionary, **kwargs):
        uuid = "9bc592d8-0738-4dc3-8ac2-0ad11d54feec"
        cmd = "set radius algorithm standard "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_algorithm_global_rr(self, arg_dictionary, **kwargs):
        uuid = "9236cb3d-b0ef-46c2-9813-d3d209c31920"
        cmd = "set radius algorithm round-robin "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_algorithm_global_srr(self, arg_dictionary, **kwargs):
        uuid = "cceb1fc6-b521-41dc-ae71-702da2578716"
        cmd = "set radius algorithm sticky-round-robin "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_accounting_retries_global(self, arg_dictionary, **kwargs):
        uuid = "6b4efe4d-560b-478d-a8fd-3ded6d09ffbd"
        cmd = "set radius accounting retries {0} all".format(arg_dictionary['num'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_accounting_timeout_global(self, arg_dictionary, **kwargs):
        uuid = "920d5343-c390-4865-b011-2a89384d6301"
        cmd = "set radius accounting timeout {0} all".format(arg_dictionary['sec'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_server(self, arg_dictionary, **kwargs):
        uuid = "51c0947e-5037-40a8-b4da-20d97ff27f12"
        cmd = "clear radius server {0}".format(arg_dictionary['index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_acct_server(self, arg_dictionary, **kwargs):
        uuid = "c1229a43-8988-4884-88a3-59da0add71a3"
        cmd = "clear radius accounting server {0}".format(arg_dictionary['index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_acct_server_global(self, arg_dictionary, **kwargs):
        uuid = "605ebf72-b989-4a7e-bb47-5a3c5f477542"
        cmd = "clear radius accounting server all"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_algorithm_global(self, arg_dictionary, **kwargs):
        uuid = "89723391-2765-4306-872f-e3007199182e"
        cmd = "clear radius algorithm "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_retries_global(self, arg_dictionary, **kwargs):
        uuid = "f9a7b472-ee89-45b6-8260-e890d5a8b4c5"
        cmd = "clear radius retries "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_timeout_global(self, arg_dictionary, **kwargs):
        uuid = "2a17d732-4379-4e7c-83b7-7d1b6a4189c2"
        cmd = "clear radius timeout "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_state(self, arg_dictionary, **kwargs):
        uuid = "a6ad0a18-a989-4afc-a647-2188555afbd7"
        cmd = "clear radius state "
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_global(self, arg_dictionary, **kwargs):
        uuid = "dc7a3e85-b914-4749-9bf6-145d7123d568"
        cmd = "show radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "e4f281eb-c13f-4aaa-a1d7-a1e9a7295195"
        cmd = "show radius state"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_acct_state(self, arg_dictionary, **kwargs):
        uuid = "0c4f711c-7595-43eb-921d-9d1864619ac6"
        cmd = "show radius accounting state"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_acct_global(self, arg_dictionary, **kwargs):
        uuid = "e6d35d83-9e33-4903-9aad-65391638b386"
        cmd = "show radius accounting"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_retries_global(self, arg_dictionary, **kwargs):
        uuid = "d69e3d97-db6c-49ed-8a28-849bf0694f5a"
        cmd = "show radius retries"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_timeout_global(self, arg_dictionary, **kwargs):
        uuid = "24bfdc5f-8fac-442c-b6b6-8cbccc2944d1"
        cmd = "show radius timeout"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_algorithm(self, arg_dictionary, **kwargs):
        uuid = "f45aa084-6873-4729-add8-568ef037dc4f"
        cmd = "show radius algorithm"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
