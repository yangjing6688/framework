"""
Base class for all dns commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class DnsBase(CliBaseApi):
    def __init__(self, device):
        super(DnsBase, self).__init__()
        self.device = device

    def create_domain_name(self, *args, **kwargs):
        return self.base_function()

    def delete_domain_name(self, *args, **kwargs):
        return self.base_function()

    def set_primary_server_ip(self, *args, **kwargs):
        return self.base_function()

    def set_secondary_server_ip(self, *args, **kwargs):
        return self.base_function()

    def set_tertiary_server_ip(self, *args, **kwargs):
        return self.base_function()

    def clear_primary_server_ip(self, *args, **kwargs):
        return self.base_function()

    def clear_secondary_server_ip(self, *args, **kwargs):
        return self.base_function()

    def clear_tertiary_server_ip(self, *args, **kwargs):
        return self.base_function()

    def show_domain_name(self, *args, **kwargs):
        return self.base_function()

    def show_servers(self, *args, **kwargs):
        return self.base_function()

    def show_host_by_name(self, *args, **kwargs):
        return self.base_function()

    def show_host_by_ip(self, *args, **kwargs):
        return self.base_function()
