"""
All loginconfig supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.loginconfig.base.loginconfigbase import \
    LoginconfigBase


class Loginconfig(DeviceApi, LoginconfigBase):
    def __init__(self, device_input):
        super(Loginconfig, self).__init__(device_input)

    def enable_cli_ro_user(self, arg_dictionary, **kwargs):
        uuid = "ea3d9fcc-d197-417e-a031-37b620fdd097"
        cmd = "password access-level ro"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_cli_ro_user(self, arg_dictionary, **kwargs):
        uuid = "c5e141ea-dc47-4717-84dd-bceb13094a74"
        cmd = "no password access-level ro"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_cli_rw_user(self, arg_dictionary, **kwargs):
        uuid = "c99b279a-18b8-42d3-b972-8d1d29003d32"
        cmd = "password access-level rw"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_cli_rw_user(self, arg_dictionary, **kwargs):
        uuid = "2ad7f9bb-ab1a-45df-b0b5-37fe61245c9c"
        cmd = "no password access-level rw"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_cli_l1_user(self, arg_dictionary, **kwargs):
        uuid = "207affc7-cf16-4e90-a775-4c144608e857"
        cmd = "password access-level l1"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_cli_l1_user(self, arg_dictionary, **kwargs):
        uuid = "744838ca-cac8-4e62-9be6-c6564643150d"
        cmd = "no password access-level l1"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_cli_l2_user(self, arg_dictionary, **kwargs):
        uuid = "2c4a60d8-111c-4957-9650-c41a77a7db18"
        cmd = "password access-level l2"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_cli_l2_user(self, arg_dictionary, **kwargs):
        uuid = "8193b82e-958e-4b6c-a1f7-8c2ae3e5f7f6"
        cmd = "no password access-level l2"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_cli_l3_user(self, arg_dictionary, **kwargs):
        uuid = "930c8b33-2eac-4e68-99dd-4e0b8e428282"
        cmd = "password access-level l3"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_cli_l3_user(self, arg_dictionary, **kwargs):
        uuid = "981eaa7e-cda5-4aff-b814-f67b62d3a228"
        cmd = "no password access-level l3"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_read_only_user(self, arg_dictionary, **kwargs):
        uuid = "4e834f1e-c3ea-4000-b985-d79bac2dd073"
        cmd = "username {0} level ro".format(arg_dictionary['username'])
        prompt = "routerConfigPrompt"
        conf = "Enter the old password :||Enter the New password :||Re-enter the New password :"
        conf_args = "{0}||{1}||{2}".format(arg_dictionary['old_passwd'],
                                           arg_dictionary['new_passwd'],
                                           arg_dictionary['new_passwd'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_read_write_user(self, arg_dictionary, **kwargs):
        uuid = "c447def2-3369-4b7b-80f4-714a37436ebd"
        cmd = "username {0} level rw".format(arg_dictionary['username'])
        prompt = "routerConfigPrompt"
        conf = "Enter the old password :||Enter the New password :||Re-enter the New password :"
        conf_args = "{0}||{1}||{2}".format(arg_dictionary['old_passwd'],
                                           arg_dictionary['new_passwd'],
                                           arg_dictionary['new_passwd'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_read_write_all_user(self, arg_dictionary, **kwargs):
        uuid = "2fc53e4e-3c43-4f6f-bbb6-64325f9fbcc9"
        cmd = "username {0} level rwa".format(arg_dictionary['username'])
        prompt = "routerConfigPrompt"
        conf = "Enter the old password :||Enter the New password :||Re-enter the New password :"
        conf_args = "{0}||{1}||{2}".format(arg_dictionary['old_passwd'],
                                           arg_dictionary['new_passwd'],
                                           arg_dictionary['new_passwd'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_max_telnet_sessions(self, arg_dictionary, **kwargs):
        uuid = "61e97777-e3ab-40f7-9a67-41fa1ab23e69"
        cmd = "telnet-access sessions {0}".format(arg_dictionary['max_sessions'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_max_rlogin_sessions(self, arg_dictionary, **kwargs):
        uuid = "facb657e-8872-4a8d-883a-2ca8b94ad3c8"
        cmd = "max-logins {0}".format(arg_dictionary['max_sessions'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_l1_user(self, arg_dictionary, **kwargs):
        uuid = "eb4fbd98-37be-40e4-b574-791f38b81926"
        cmd = "username {0} level l1".format(arg_dictionary['username'])
        prompt = "routerConfigPrompt"
        conf = "Enter the old password :||Enter the New password :||Re-enter the New password :"
        conf_args = "{0}||{1}||{2}".format(arg_dictionary['old_passwd'],
                                           arg_dictionary['new_passwd'],
                                           arg_dictionary['new_passwd'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_l2_user(self, arg_dictionary, **kwargs):
        uuid = "20a0224e-6eb4-42bd-9116-e4d6774b1b13"
        cmd = "username {0} level l2".format(arg_dictionary['username'])
        prompt = "routerConfigPrompt"
        conf = "Enter the old password :||Enter the New password :||Re-enter the New password :"
        conf_args = "{0}||{1}||{2}".format(arg_dictionary['old_passwd'],
                                           arg_dictionary['new_passwd'],
                                           arg_dictionary['new_passwd'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_l3_user(self, arg_dictionary, **kwargs):
        uuid = "a9865378-42fb-41e1-8785-69d0f34e00ad"
        cmd = "username {0} level l3".format(arg_dictionary['username'])
        prompt = "routerConfigPrompt"
        conf = "Enter the old password :||Enter the New password :||Re-enter the New password :"
        conf_args = "{0}||{1}||{2}".format(arg_dictionary['old_passwd'],
                                           arg_dictionary['new_passwd'],
                                           arg_dictionary['new_passwd'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, conf=conf, conf_args=conf_args)

    def set_cli_timeout(self, arg_dictionary, **kwargs):
        uuid = "5829f7a8-04b5-4b23-995f-7af584d3cba6"
        cmd = "cli timeout {0}".format(arg_dictionary['timeout'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_cli_info(self, arg_dictionary, **kwargs):
        uuid = "02896d84-dba9-446d-af14-81389cac1372"
        cmd = "show cli info"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_cli_users_state(self, arg_dictionary, **kwargs):
        uuid = "e92c8400-0654-4a65-ad92-bef8408ac5c3"
        cmd = "show cli password"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
