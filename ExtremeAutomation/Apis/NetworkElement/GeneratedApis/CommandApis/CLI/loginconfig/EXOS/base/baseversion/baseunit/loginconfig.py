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
        cmd = "create account admin {0} {1}".format(arg_dictionary['username'],
                                                    arg_dictionary['passwd'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def delete_account(self, arg_dictionary, **kwargs):
        uuid = "66d9fc62-de47-45e9-a80f-237df09d6830"
        cmd = "delete account {0}".format(arg_dictionary['username'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_account_password_policy_min_length(self, arg_dictionary, **kwargs):
        uuid = "7b2711f4-0fc4-48a3-986d-9dd6cb6c9474"
        cmd = "configure account {0} password-policy min-length {1}".format(arg_dictionary['username'],
                                                                            arg_dictionary['min_length'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_account_password_policy_min_different_chars(self, arg_dictionary, **kwargs):
        uuid = "769542b5-1b16-4127-901f-cdcf3bef674c"
        cmd = "configure account {0} password-policy min-different-characters {1}".format(arg_dictionary['username'],
                                                                                          arg_dictionary['min_chars'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_account_password_policy_min_age(self, arg_dictionary, **kwargs):
        uuid = "e4fddf5a-e021-489a-b30c-f8f928150e9b"
        cmd = "configure account {0} password-policy min-age {1}".format(arg_dictionary['username'],
                                                                         arg_dictionary['age'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_account_password_policy_max_age(self, arg_dictionary, **kwargs):
        uuid = "3c77851e-1dab-44cb-8076-4378392760be"
        cmd = "configure account {0} password-policy max-age {1}".format(arg_dictionary['username'],
                                                                         arg_dictionary['age'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_account_password(self, arg_dictionary, **kwargs):
        uuid = "d4003c0a-2fad-4069-bd4c-1280e018bc1b"
        cmd = "configure account {0} password".format(arg_dictionary['username'])
        prompt = "userPrompt"
        conf = "Current user's password:||New password:||Reenter password:"
        conf_args = "{0}||{1}||{2}".format(arg_dictionary['old_password'],
                                           arg_dictionary['new_password'],
                                           arg_dictionary['new_password'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def show_accounts(self, arg_dictionary, **kwargs):
        uuid = "da0f6bef-fcb4-4509-bc9c-6262c01d3079"
        cmd = "show accounts"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_logged_in_users(self, arg_dictionary, **kwargs):
        uuid = "8ecd0acd-9ccd-42af-8c97-acc46413408b"
        cmd = "show session"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_logged_in_users_detail(self, arg_dictionary, **kwargs):
        uuid = "eb712e6f-91c6-4889-9864-a79c70318f94"
        cmd = "show session detail"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_accounts_password_policy(self, arg_dictionary, **kwargs):
        uuid = "b9453801-62eb-4f8c-8a14-4254f921eb95"
        cmd = "show accounts password-policy"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
