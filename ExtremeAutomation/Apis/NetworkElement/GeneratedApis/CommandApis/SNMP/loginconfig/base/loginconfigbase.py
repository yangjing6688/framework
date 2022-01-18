"""
Base class for all loginconfig SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class LoginconfigBase(SnmpBaseApi):
    def __init__(self, device):
        super(LoginconfigBase, self).__init__()
        self.device = device

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

    def show_cli_num_access_violations(self, *args, **kwargs):
        return self.base_function()
