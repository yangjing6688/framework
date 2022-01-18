"""
Base class for all upm commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class UpmBase(CliBaseApi):
    def __init__(self, device):
        super(UpmBase, self).__init__()
        self.device = device

    def set_auth(self, *args, **kwargs):
        return self.base_function()

    def set_unauth(self, *args, **kwargs):
        return self.base_function()

    def set_profile(self, *args, **kwargs):
        return self.base_function()

    def clear_auth(self, *args, **kwargs):
        return self.base_function()

    def clear_unauth(self, *args, **kwargs):
        return self.base_function()

    def clear_auth_all_ports(self, *args, **kwargs):
        return self.base_function()

    def clear_unauth_all_ports(self, *args, **kwargs):
        return self.base_function()

    def clear_profile(self, *args, **kwargs):
        return self.base_function()

    def show_event_authenticate(self, *args, **kwargs):
        return self.base_function()

    def show_event_unauthenticated(self, *args, **kwargs):
        return self.base_function()
