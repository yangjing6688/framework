"""
All hostutils supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.hostutils.base.hostutilsbase import \
    HostutilsBase


class Hostutils(DeviceApi, HostutilsBase):
    def __init__(self, device_input):
        super(Hostutils, self).__init__(device_input)

    def ping_host(self, arg_dictionary, **kwargs):
        uuid = "57c52793-0d02-4f7f-b5b2-53bcd3024df4"
        cmd = "ping count {0} interval {1} {2}".format(arg_dictionary['count'],
                                                       arg_dictionary['timeout'],
                                                       arg_dictionary['host_address'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_debug_mode(self, arg_dictionary, **kwargs):
        uuid = "561a3b82-0d6e-456c-9c21-e8732fff4e8c"
        cmd = "enable debug-mode"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def return_debug_creds(self, arg_dictionary, **kwargs):
        uuid = "1151e4ca-cb54-4aed-b89c-d6d3cb64661e"
        cmd = "{0}".format(arg_dictionary['response'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_feature_license(self, arg_dictionary, **kwargs):
        uuid = "5c9acf86-b925-473a-b308-755ad8b516bb"
        cmd = "enable license {0}".format(arg_dictionary['key'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def telnet_to_ip(self, arg_dictionary, **kwargs):
        uuid = "653ec587-88c4-4a0f-bbb8-ff81c1990bb4"
        cmd = "telnet {0}".format(arg_dictionary['ip_address'])
        prompt = "userPrompt"
        conf = "login:||password:||Do you wish to save||Last Successful Login"
        conf_args = "{0}||{1}||n||exit".format(arg_dictionary['username'],
                                               arg_dictionary['password'])

        self.device.error_checker.add_error_to_ignore_list(*["Login timed out!"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def ssh_to_ip(self, arg_dictionary, **kwargs):
        uuid = "23546501-3087-40dd-a754-f9e6355e9a49"
        cmd = "ssh user {0} {1}".format(arg_dictionary['username'],
                                        arg_dictionary['ip_address'])
        prompt = "userPrompt"
        conf = "password:||Do you wish to save||Last Successful Login"
        conf_args = "{0}||n||exit".format(arg_dictionary['password'])

        self.device.error_checker.add_error_to_ignore_list(*["Login timed out!"])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)
