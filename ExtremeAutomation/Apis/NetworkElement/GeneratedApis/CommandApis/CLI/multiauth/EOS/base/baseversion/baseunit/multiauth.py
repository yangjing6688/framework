"""
All multiauth supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.multiauth.base.multiauthbase import \
    MultiauthBase


class Multiauth(DeviceApi, MultiauthBase):
    def __init__(self, device_input):
        super(Multiauth, self).__init__(device_input)

    def set_session_timeout(self, arg_dictionary, **kwargs):
        uuid = "ad2d1a2b-1c05-46ca-9fb5-fe6ce27806b8"
        cmd = "set multiauth session-timeout {0}".format(arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_session_type_timeout(self, arg_dictionary, **kwargs):
        uuid = "3acfba85-52e1-4d2c-9959-88fdd081a2e6"
        cmd = "set multiauth session-timeout {0} {1}".format(self.api_utils.eos_ma_mode(arg_dictionary['mode']),
                                                             arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_idle_timeout(self, arg_dictionary, **kwargs):
        uuid = "796e0685-e341-454b-9f48-4e69b3008fe7"
        cmd = "set multiauth idle-timeout {0}".format(arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_idle_type_timeout(self, arg_dictionary, **kwargs):
        uuid = "6af1773b-18c7-4bfa-ac39-fda93afa3608"
        cmd = "set multiauth idle-timeout {0} {1}".format(self.api_utils.eos_ma_mode(arg_dictionary['mode']),
                                                          arg_dictionary['timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_mode(self, arg_dictionary, **kwargs):
        uuid = "0cdfcb1c-ff0d-454e-904e-843d68779832"
        cmd = "set multiauth port mode {0} {1}".format(self.api_utils.eos_ma_mode(arg_dictionary['mode']),
                                                       arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_numusers(self, arg_dictionary, **kwargs):
        uuid = "affaa376-34fb-4b1e-a6b9-83a4a41a77b1"
        cmd = "set multiauth port numusers {0} {1}".format(arg_dictionary['num_users'],
                                                           arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_station_mac_port(self, arg_dictionary, **kwargs):
        uuid = "395038b8-7e83-43ae-9ef4-789be298fad1"
        cmd = "clear multiauth station mac {0} port {1}".format(arg_dictionary['mac'],
                                                                arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_station_port(self, arg_dictionary, **kwargs):
        uuid = "4c0206d2-7df7-4c17-bf25-b630cb366e01"
        cmd = "clear multiauth station port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_station_mac(self, arg_dictionary, **kwargs):
        uuid = "146f1262-e1c3-4df0-85b5-a2c31b423fde"
        cmd = "clear multiauth station mac {0} port *.*.*".format(arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_station_agent(self, arg_dictionary, **kwargs):
        uuid = "a98b62da-73b5-4a30-a12d-547a9a970f71"
        cmd = "clear multiauth session {0} *.*.* {1}".format(arg_dictionary['mac'],
                                                             self.api_utils.eos_ma_agent(arg_dictionary['agent']))
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_mode(self, arg_dictionary, **kwargs):
        uuid = "e059d40a-d336-440e-8fa0-37bbc37f7de8"
        cmd = "set multiauth mode {0}".format(arg_dictionary['mode'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_port_force_auth(self, arg_dictionary, **kwargs):
        uuid = "62f29872-ded8-4e28-9eef-50da69f83dea"
        cmd = "set multiauth port mode force-auth {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_session_timeout(self, arg_dictionary, **kwargs):
        uuid = "8bcf7706-aa82-413c-855a-c857cf38c1d5"
        cmd = "show multiauth session-timeout"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_idle_timeout(self, arg_dictionary, **kwargs):
        uuid = "45039e37-9b00-46ce-aa89-4200cbd456a9"
        cmd = "show multiauth idle-timeout"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "13a2b82c-e007-4ede-8c21-645b7862308b"
        cmd = "show multiauth"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_session_all(self, arg_dictionary, **kwargs):
        uuid = "73dbfaa0-d576-4855-b148-05640ab7eafe"
        cmd = "show multiauth session all"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_session_mac(self, arg_dictionary, **kwargs):
        uuid = "41e1c599-622f-4338-8a86-2de304ba5c52"
        cmd = "show multiauth session mac {0}".format(arg_dictionary['station_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
