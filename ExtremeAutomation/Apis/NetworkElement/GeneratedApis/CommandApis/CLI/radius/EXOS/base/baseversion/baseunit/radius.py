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
        cmd = "enable radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_acct(self, arg_dictionary, **kwargs):
        uuid = "d2154d3e-5129-4551-8e84-21fe67976ba5"
        cmd = "enable radius-accounting"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "9f41adce-7e97-45c2-addc-1b3b23dcdd4c"
        cmd = "disable radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_acct(self, arg_dictionary, **kwargs):
        uuid = "55596503-345c-4584-9438-65aff18f58ea"
        cmd = "disable radius-accounting"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_server(self, arg_dictionary, **kwargs):
        uuid = "714d2b1e-d4bc-436a-8691-dbd3ac8209b6"
        cmd = "configure radius {0} server {1} {2} client-ip {3} shared-secret {4} vr {5}".format(arg_dictionary['index'],
                                                                                                  arg_dictionary['addr'],
                                                                                                  arg_dictionary['port'],
                                                                                                  arg_dictionary['client_ip'],
                                                                                                  arg_dictionary['secret'],
                                                                                                  arg_dictionary['vr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_acct_server(self, arg_dictionary, **kwargs):
        uuid = "c26d9e66-84f7-43c4-b51c-6b4a215fac5d"
        cmd = "configure radius-accounting {0} server {1} {2} client-ip {3} shared-secret {4} vr {5}".format(arg_dictionary['index'],
                                                                                                             arg_dictionary['addr'],
                                                                                                             arg_dictionary['port'],
                                                                                                             arg_dictionary['client_ip'],
                                                                                                             arg_dictionary['secret'],
                                                                                                             arg_dictionary['vr'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_retries_global(self, arg_dictionary, **kwargs):
        uuid = "37ec7b4e-7453-456d-8567-6dc1c07c3813"
        cmd = "configure radius retries {0}".format(arg_dictionary['num'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_timeout_global(self, arg_dictionary, **kwargs):
        uuid = "3c29d965-525b-4e5b-82c0-ae90f35ac1d1"
        cmd = "configure radius timeout {0}".format(arg_dictionary['sec'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_algorithm_global_std(self, arg_dictionary, **kwargs):
        uuid = "9bc592d8-0738-4dc3-8ac2-0ad11d54feec"
        cmd = "configure radius algorithm standard"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_algorithm_global_rr(self, arg_dictionary, **kwargs):
        uuid = "9236cb3d-b0ef-46c2-9813-d3d209c31920"
        cmd = "configure radius algorithm round-robin"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_server(self, arg_dictionary, **kwargs):
        uuid = "51c0947e-5037-40a8-b4da-20d97ff27f12"
        cmd = "unconfigure radius server {0}".format(arg_dictionary['index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_acct_server(self, arg_dictionary, **kwargs):
        uuid = "c1229a43-8988-4884-88a3-59da0add71a3"
        cmd = "unconfigure radius-accounting server {0}".format(arg_dictionary['index'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_acct_server_global(self, arg_dictionary, **kwargs):
        uuid = "605ebf72-b989-4a7e-bb47-5a3c5f477542"
        cmd = "unconfigure radius-accounting"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_algorithm_global(self, arg_dictionary, **kwargs):
        uuid = "89723391-2765-4306-872f-e3007199182e"
        cmd = "configure radius algorithm standard"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_retries_global(self, arg_dictionary, **kwargs):
        uuid = "f9a7b472-ee89-45b6-8260-e890d5a8b4c5"
        cmd = "configure radius retries 3"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_timeout_global(self, arg_dictionary, **kwargs):
        uuid = "2a17d732-4379-4e7c-83b7-7d1b6a4189c2"
        cmd = "configure radius timeout 3"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_mgmt(self, arg_dictionary, **kwargs):
        uuid = "9057e14d-ac0c-4761-b94b-f3a2b910e18a"
        cmd = "enable radius mgmt-access"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_netlogin(self, arg_dictionary, **kwargs):
        uuid = "aee135e5-1ef4-44a7-9aa7-f08e6e866480"
        cmd = "enable radius netlogin"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_mgmt(self, arg_dictionary, **kwargs):
        uuid = "8c1a1e0b-4474-4ed2-b0ba-5ca0719b65e1"
        cmd = "disable radius mgmt-access"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_netlogin(self, arg_dictionary, **kwargs):
        uuid = "614343be-6e31-45ba-8e49-95f100ad7dde"
        cmd = "disable radius netlogin"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_global(self, arg_dictionary, **kwargs):
        uuid = "dc7a3e85-b914-4749-9bf6-145d7123d568"
        cmd = "show radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_state(self, arg_dictionary, **kwargs):
        uuid = "e4f281eb-c13f-4aaa-a1d7-a1e9a7295195"
        cmd = "show radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_acct_state(self, arg_dictionary, **kwargs):
        uuid = "0c4f711c-7595-43eb-921d-9d1864619ac6"
        cmd = "show radius-accounting"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_acct_global(self, arg_dictionary, **kwargs):
        uuid = "e6d35d83-9e33-4903-9aad-65391638b386"
        cmd = "show radius-accounting"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_retries_global(self, arg_dictionary, **kwargs):
        uuid = "d69e3d97-db6c-49ed-8a28-849bf0694f5a"
        cmd = "show radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_timeout_global(self, arg_dictionary, **kwargs):
        uuid = "24bfdc5f-8fac-442c-b6b6-8cbccc2944d1"
        cmd = "show radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_algorithm(self, arg_dictionary, **kwargs):
        uuid = "f45aa084-6873-4729-add8-568ef037dc4f"
        cmd = "show radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
