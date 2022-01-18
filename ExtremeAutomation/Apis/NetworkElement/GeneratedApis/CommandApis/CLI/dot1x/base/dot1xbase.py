"""
Base class for all dot1x commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class Dot1xBase(CliBaseApi):
    def __init__(self, device):
        super(Dot1xBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def enable_port(self, *args, **kwargs):
        return self.base_function()

    def disable_port(self, *args, **kwargs):
        return self.base_function()

    def enable_accounting(self, *args, **kwargs):
        return self.base_function()

    def disable_accounting(self, *args, **kwargs):
        return self.base_function()

    def enable_port_reauth(self, *args, **kwargs):
        return self.base_function()

    def disable_port_reauth(self, *args, **kwargs):
        return self.base_function()

    def set_global_idle_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_global_session_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_port_quietperiod(self, *args, **kwargs):
        return self.base_function()

    def set_port_reauthperiod(self, *args, **kwargs):
        return self.base_function()

    def set_port_servertimeout(self, *args, **kwargs):
        return self.base_function()

    def set_port_supp_resptimeout(self, *args, **kwargs):
        return self.base_function()

    def clear_global_idle_timeout(self, *args, **kwargs):
        return self.base_function()

    def clear_global_session_timeout(self, *args, **kwargs):
        return self.base_function()

    def clear_state_mac(self, *args, **kwargs):
        return self.base_function()

    def clear_port_state(self, *args, **kwargs):
        return self.base_function()

    def clear_port_state_mac(self, *args, **kwargs):
        return self.base_function()

    def clear_port_reauthperiod(self, *args, **kwargs):
        return self.base_function()

    def show_session(self, *args, **kwargs):
        return self.base_function()

    def show_global_idle_timeout(self, *args, **kwargs):
        return self.base_function()

    def show_global_session_timeout(self, *args, **kwargs):
        return self.base_function()

    def show_auth_cfg(self, *args, **kwargs):
        return self.base_function()

    def show_auth_cfg_port(self, *args, **kwargs):
        return self.base_function()

    def show_session_by_port(self, *args, **kwargs):
        return self.base_function()
