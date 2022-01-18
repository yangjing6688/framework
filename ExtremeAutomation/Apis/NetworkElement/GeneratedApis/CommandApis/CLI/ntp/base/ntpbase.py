"""
Base class for all ntp commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class NtpBase(CliBaseApi):
    def __init__(self, device):
        super(NtpBase, self).__init__()
        self.device = device

    def enable_client(self, *args, **kwargs):
        return self.base_function()

    def disable_client(self, *args, **kwargs):
        return self.base_function()

    def create_server(self, *args, **kwargs):
        return self.base_function()

    def create_server_key(self, *args, **kwargs):
        return self.base_function()

    def create_server_precedence(self, *args, **kwargs):
        return self.base_function()

    def create_server_precedence_key(self, *args, **kwargs):
        return self.base_function()

    def delete_server(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_servers(self, *args, **kwargs):
        return self.base_function()

    def enable_client_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_client_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_association(self, *args, **kwargs):
        return self.base_function()

    def enable_server(self, *args, **kwargs):
        return self.base_function()

    def disable_server(self, *args, **kwargs):
        return self.base_function()

    def enable_server_auth(self, *args, **kwargs):
        return self.base_function()

    def disable_server_auth(self, *args, **kwargs):
        return self.base_function()

    def set_global_interval(self, *args, **kwargs):
        return self.base_function()

    def set_server_source_ip(self, *args, **kwargs):
        return self.base_function()

    def set_auth(self, *args, **kwargs):
        return self.base_function()

    def set_auth_key(self, *args, **kwargs):
        return self.base_function()

    def set_auth_md5(self, *args, **kwargs):
        return self.base_function()

    def set_auth_sha1(self, *args, **kwargs):
        return self.base_function()

    def clear_auth_key(self, *args, **kwargs):
        return self.base_function()

    def show_key(self, *args, **kwargs):
        return self.base_function()

    def show_statistics(self, *args, **kwargs):
        return self.base_function()

    def set_source_ip_mm(self, *args, **kwargs):
        return self.base_function()

    def set_source_ip_chassis(self, *args, **kwargs):
        return self.base_function()

    def show_association_detail(self, *args, **kwargs):
        return self.base_function()
