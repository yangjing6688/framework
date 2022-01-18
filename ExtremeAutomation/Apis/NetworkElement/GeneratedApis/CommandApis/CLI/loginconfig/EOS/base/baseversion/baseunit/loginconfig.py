"""
All loginconfig supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.loginconfig.base.loginconfigbase import \
    LoginconfigBase


class Loginconfig(DeviceApi, LoginconfigBase):
    def __init__(self, device_input):
        super(Loginconfig, self).__init__(device_input)

    def create_admin_account(self, arg_dictionary, **kwargs):
        uuid = "b2d5d8b4-05ff-448e-bd9a-6c3128a46f72"
        cmd = "set system login {0} super-user enable password {1}".format(arg_dictionary['username'],
                                                                           arg_dictionary['passwd'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_account(self, arg_dictionary, **kwargs):
        uuid = "66d9fc62-de47-45e9-a80f-237df09d6830"
        cmd = "clear system login {0}".format(arg_dictionary['username'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_accounts(self, arg_dictionary, **kwargs):
        uuid = "da0f6bef-fcb4-4509-bc9c-6262c01d3079"
        cmd = "show system login"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
