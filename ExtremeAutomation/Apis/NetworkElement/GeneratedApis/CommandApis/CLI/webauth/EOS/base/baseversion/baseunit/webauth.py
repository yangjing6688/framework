"""
All webauth supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.webauth.base.webauthbase import WebauthBase


class Webauth(DeviceApi, WebauthBase):
    def __init__(self, device_input):
        super(Webauth, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "8605577b-fe15-4664-baa7-6e84ac4421c1"
        cmd = "set pwa enable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "58c01afb-4532-4b08-bbe8-f44f0e54bda6"
        cmd = "set pwa disable"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_control_port(self, arg_dictionary, **kwargs):
        uuid = "475f2a85-c938-46de-b2b1-da36b8114e43"
        cmd = "set pwa portcontrol enable {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_control_port(self, arg_dictionary, **kwargs):
        uuid = "93383c86-d287-4126-b217-16b639fa2b52"
        cmd = "set pwa portcontrol disable {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_hostname(self, arg_dictionary, **kwargs):
        uuid = "d8f21304-c087-4894-ab2f-8b00b90f21a6"
        cmd = "set pwa hostname {0}".format(arg_dictionary['url_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_init_port(self, arg_dictionary, **kwargs):
        uuid = "9155b2cb-6093-4f7d-b82b-32858ddf63b5"
        cmd = "set pwa initialize {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redirect_page(self, arg_dictionary, **kwargs):
        uuid = "ee1a4441-587d-48da-aa1e-edb66bc1dd88"
        cmd = "set pwa ipaddress {0}".format(arg_dictionary['redirect_page'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_hostname(self, arg_dictionary, **kwargs):
        uuid = "dba32dfa-85b2-4888-b3b4-ef9e48548c64"
        cmd = "clear pwa hostname"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redirect_page(self, arg_dictionary, **kwargs):
        uuid = "671068c9-e516-4210-a488-8a63011c75d5"
        cmd = "clear pwa ipaddress"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_summary_snapshot(self, arg_dictionary, **kwargs):
        uuid = "8db45701-652b-4f75-98ca-7b54283fe547"
        cmd = "show pwa summary"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "3766b43d-58cc-40f6-9aaf-047508966934"
        cmd = "show pwa {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
