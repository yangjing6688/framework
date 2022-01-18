"""
Base class for all ssh commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class SshBase(CliBaseApi):
    def __init__(self, device):
        super(SshBase, self).__init__()
        self.device = device

    def enable(self, *args, **kwargs):
        return self.base_function()

    def disable(self, *args, **kwargs):
        return self.base_function()

    def show(self, *args, **kwargs):
        return self.base_function()

    def enable_client(self, *args, **kwargs):
        return self.base_function()

    def disable_client(self, *args, **kwargs):
        return self.base_function()

    def set_version(self, *args, **kwargs):
        return self.base_function()

    def set_tcp_port(self, *args, **kwargs):
        return self.base_function()

    def show_session(self, *args, **kwargs):
        return self.base_function()

    def show_rekey(self, *args, **kwargs):
        return self.base_function()

    def set_client_source_interface(self, *args, **kwargs):
        return self.base_function()

    def clear_client_source_interface(self, *args, **kwargs):
        return self.base_function()

    def show_client_status(self, *args, **kwargs):
        return self.base_function()

    def show_server_status(self, *args, **kwargs):
        return self.base_function()
