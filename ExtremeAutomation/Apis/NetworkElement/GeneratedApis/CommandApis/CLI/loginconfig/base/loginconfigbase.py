"""
Base class for all loginconfig commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class LoginconfigBase(CliBaseApi):
    def __init__(self, device):
        super(LoginconfigBase, self).__init__()
        self.device = device

    def create_admin_account(self, *args, **kwargs):
        return self.base_function()

    def delete_account(self, *args, **kwargs):
        return self.base_function()

    def show_accounts(self, *args, **kwargs):
        return self.base_function()

    def set_account_password_policy_min_length(self, *args, **kwargs):
        return self.base_function()

    def set_account_password_policy_min_different_chars(self, *args, **kwargs):
        return self.base_function()

    def set_account_password_policy_min_age(self, *args, **kwargs):
        return self.base_function()

    def set_account_password_policy_max_age(self, *args, **kwargs):
        return self.base_function()

    def set_account_password(self, *args, **kwargs):
        return self.base_function()

    def show_logged_in_users(self, *args, **kwargs):
        return self.base_function()

    def show_logged_in_users_detail(self, *args, **kwargs):
        return self.base_function()

    def show_accounts_password_policy(self, *args, **kwargs):
        return self.base_function()

    def enable_cli_ro_user(self, *args, **kwargs):
        return self.base_function()

    def disable_cli_ro_user(self, *args, **kwargs):
        return self.base_function()

    def enable_cli_rw_user(self, *args, **kwargs):
        return self.base_function()

    def disable_cli_rw_user(self, *args, **kwargs):
        return self.base_function()

    def enable_cli_l1_user(self, *args, **kwargs):
        return self.base_function()

    def disable_cli_l1_user(self, *args, **kwargs):
        return self.base_function()

    def enable_cli_l2_user(self, *args, **kwargs):
        return self.base_function()

    def disable_cli_l2_user(self, *args, **kwargs):
        return self.base_function()

    def enable_cli_l3_user(self, *args, **kwargs):
        return self.base_function()

    def disable_cli_l3_user(self, *args, **kwargs):
        return self.base_function()

    def set_read_only_user(self, *args, **kwargs):
        return self.base_function()

    def set_read_write_user(self, *args, **kwargs):
        return self.base_function()

    def set_read_write_all_user(self, *args, **kwargs):
        return self.base_function()

    def set_max_telnet_sessions(self, *args, **kwargs):
        return self.base_function()

    def set_max_rlogin_sessions(self, *args, **kwargs):
        return self.base_function()

    def set_l1_user(self, *args, **kwargs):
        return self.base_function()

    def set_l2_user(self, *args, **kwargs):
        return self.base_function()

    def set_l3_user(self, *args, **kwargs):
        return self.base_function()

    def set_cli_timeout(self, *args, **kwargs):
        return self.base_function()

    def show_cli_info(self, *args, **kwargs):
        return self.base_function()

    def show_cli_users_state(self, *args, **kwargs):
        return self.base_function()
