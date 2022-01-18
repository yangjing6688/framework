"""
All multiauth supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.multiauth.base.multiauthbase import \
    MultiauthBase


class Multiauth(DeviceApi, MultiauthBase):
    def __init__(self, device_input):
        super(Multiauth, self).__init__(device_input)

    def enable_session_refresh(self, arg_dictionary, **kwargs):
        uuid = "f3eb09e3-5666-4313-ac3d-fbb864ea2476"
        cmd = "enable netlogin session-refresh"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_session_refresh(self, arg_dictionary, **kwargs):
        uuid = "bf5c7ddd-7ddb-4969-b73c-21f3a626cd4e"
        cmd = "disable netlogin session-refresh"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_session_timeout(self, arg_dictionary, **kwargs):
        uuid = "ad2d1a2b-1c05-46ca-9fb5-fe6ce27806b8"
        cmd = "configure netlogin session-timeout {0}".format(arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_session_type_timeout(self, arg_dictionary, **kwargs):
        uuid = "3acfba85-52e1-4d2c-9959-88fdd081a2e6"
        cmd = "configure netlogin session-timeout {0} {1}".format(self.api_utils.exos_ma_mode(arg_dictionary['mode']),
                                                                  arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_session_type_timeout(self, arg_dictionary, **kwargs):
        uuid = "25b27d24-41ba-408f-b670-d6a0a55918e5"
        cmd = "unconfigure netlogin session-timeout {0}".format(self.api_utils.exos_ma_mode(arg_dictionary['mode']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_session_refresh(self, arg_dictionary, **kwargs):
        uuid = "f26cfaa0-c900-4839-9d43-3f6f9a10709d"
        cmd = "configure netlogin session-refresh {0}".format(arg_dictionary['seconds'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_session_refresh(self, arg_dictionary, **kwargs):
        uuid = "a16c13f3-5825-484b-9a84-9b823ea8fe1a"
        cmd = "unconfigure netlogin session-refresh"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_vlan(self, arg_dictionary, **kwargs):
        uuid = "2b3308c0-27b9-48e0-9550-91d9af08dff1"
        cmd = "configure netlogin vlan {0}".format(arg_dictionary['multiauth_vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_vlan(self, arg_dictionary, **kwargs):
        uuid = "954d2698-9c1a-478e-888b-b4aea467b4a3"
        cmd = "unconfigure netlogin vlan"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_idle_timeout(self, arg_dictionary, **kwargs):
        uuid = "796e0685-e341-454b-9f48-4e69b3008fe7"
        cmd = "configure netlogin idle-timeout {0}".format(arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_idle_type_timeout(self, arg_dictionary, **kwargs):
        uuid = "6af1773b-18c7-4bfa-ac39-fda93afa3608"
        cmd = "configure netlogin idle-timeout {0} {1}".format(self.api_utils.exos_ma_mode(arg_dictionary['mode']),
                                                               arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_idle_type_timeout(self, arg_dictionary, **kwargs):
        uuid = "05becf3a-3ebb-4fec-a4be-cc1a44177e9d"
        cmd = "unconfigure netlogin idle-timeout {0}".format(self.api_utils.exos_ma_mode(arg_dictionary['mode']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_mode(self, arg_dictionary, **kwargs):
        uuid = "0cdfcb1c-ff0d-454e-904e-843d68779832"
        cmd = "configure netlogin port {0} authentication mode {1}".format(arg_dictionary['port'],
                                                                           self.api_utils.exos_ma_mode(arg_dictionary['mode']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_numusers(self, arg_dictionary, **kwargs):
        uuid = "affaa376-34fb-4b1e-a6b9-83a4a41a77b1"
        cmd = "configure netlogin ports {0} allowed-users {1}".format(arg_dictionary['port'],
                                                                      arg_dictionary['num_users'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_station_mac_port(self, arg_dictionary, **kwargs):
        uuid = "395038b8-7e83-43ae-9ef4-789be298fad1"
        cmd = "clear netlogin state mac-address {0} port {1}".format(arg_dictionary['mac'],
                                                                     arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_station_port(self, arg_dictionary, **kwargs):
        uuid = "4c0206d2-7df7-4c17-bf25-b630cb366e01"
        cmd = "clear netlogin state port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_station_mac(self, arg_dictionary, **kwargs):
        uuid = "146f1262-e1c3-4df0-85b5-a2c31b423fde"
        cmd = "clear netlogin state mac-address {0}".format(arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_station_agent(self, arg_dictionary, **kwargs):
        uuid = "a98b62da-73b5-4a30-a12d-547a9a970f71"
        cmd = "clear netlogin state agent {0}".format(self.api_utils.exos_ma_agent(arg_dictionary['agent']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_session_timeout(self, arg_dictionary, **kwargs):
        uuid = "8bcf7706-aa82-413c-855a-c857cf38c1d5"
        cmd = "show netlogin timeout"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_idle_timeout(self, arg_dictionary, **kwargs):
        uuid = "45039e37-9b00-46ce-aa89-4200cbd456a9"
        cmd = "show netlogin timeout"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_session(self, arg_dictionary, **kwargs):
        uuid = "a9b1d689-56ed-4730-827b-749683939450"
        cmd = "show netlogin session"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "13a2b82c-e007-4ede-8c21-645b7862308b"
        cmd = "show netlogin"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_session_all(self, arg_dictionary, **kwargs):
        uuid = "73dbfaa0-d576-4855-b148-05640ab7eafe"
        cmd = "show netlogin session all"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_session_mac(self, arg_dictionary, **kwargs):
        uuid = "41e1c599-622f-4338-8a86-2de304ba5c52"
        cmd = "show netlogin session mac-address {0}".format(arg_dictionary['station_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_session_port(self, arg_dictionary, **kwargs):
        uuid = "884857ec-cf3f-4075-be87-115f081d5f5b"
        cmd = "show netlogin session ports {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
