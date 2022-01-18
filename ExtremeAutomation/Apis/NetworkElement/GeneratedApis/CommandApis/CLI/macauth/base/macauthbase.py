"""
Base class for all macauth commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class MacauthBase(CliBaseApi):
    def __init__(self, device):
        super(MacauthBase, self).__init__()
        self.device = device

    def enable(self, *args, **kwargs):
        return self.base_function()

    def disable(self, *args, **kwargs):
        return self.base_function()

    def enable_port_reauthentication(self, *args, **kwargs):
        return self.base_function()

    def disable_port_reauthentication(self, *args, **kwargs):
        return self.base_function()

    def set_password(self, *args, **kwargs):
        return self.base_function()

    def set_port_state(self, *args, **kwargs):
        return self.base_function()

    def set_port_reauthperiod(self, *args, **kwargs):
        return self.base_function()

    def set_port_quietperiod(self, *args, **kwargs):
        return self.base_function()

    def clear_password(self, *args, **kwargs):
        return self.base_function()

    def clear_port_reauthperiod(self, *args, **kwargs):
        return self.base_function()

    def clear_port_quietperiod(self, *args, **kwargs):
        return self.base_function()

    def show(self, *args, **kwargs):
        return self.base_function()

    def show_port(self, *args, **kwargs):
        return self.base_function()

    def set_mac_format_type(self, *args, **kwargs):
        return self.base_function()

    def set_mac_user(self, *args, **kwargs):
        return self.base_function()

    def set_mac_user_nopass(self, *args, **kwargs):
        return self.base_function()

    def set_reauthperiod(self, *args, **kwargs):
        return self.base_function()

    def clear_mac_user(self, *args, **kwargs):
        return self.base_function()

    def show_mac_list(self, *args, **kwargs):
        return self.base_function()

    def show_port_authentication(self, *args, **kwargs):
        return self.base_function()
