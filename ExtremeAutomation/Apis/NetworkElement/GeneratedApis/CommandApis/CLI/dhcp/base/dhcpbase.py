"""
Base class for all dhcp commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class DhcpBase(CliBaseApi):
    def __init__(self, device):
        super(DhcpBase, self).__init__()
        self.device = device

    def enable_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_port(self, *args, **kwargs):
        return self.base_function()

    def disable_port(self, *args, **kwargs):
        return self.base_function()

    def enable_bootprelay_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_address_range(self, *args, **kwargs):
        return self.base_function()

    def set_lease_time(self, *args, **kwargs):
        return self.base_function()

    def set_netlogin_lease_time(self, *args, **kwargs):
        return self.base_function()

    def set_options_gateway(self, *args, **kwargs):
        return self.base_function()

    def set_options_dns(self, *args, **kwargs):
        return self.base_function()

    def set_options_dns_pri(self, *args, **kwargs):
        return self.base_function()

    def set_options_dns_sec(self, *args, **kwargs):
        return self.base_function()

    def set_bootprelay_ip(self, *args, **kwargs):
        return self.base_function()

    def clear_address_range(self, *args, **kwargs):
        return self.base_function()

    def clear_lease_time(self, *args, **kwargs):
        return self.base_function()

    def clear_netlogin_lease_time(self, *args, **kwargs):
        return self.base_function()

    def clear_global(self, *args, **kwargs):
        return self.base_function()

    def clear_options_gateway(self, *args, **kwargs):
        return self.base_function()

    def clear_options_dns(self, *args, **kwargs):
        return self.base_function()

    def clear_options_dns_pri(self, *args, **kwargs):
        return self.base_function()

    def clear_options_dns_sec(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_address_allocation(self, *args, **kwargs):
        return self.base_function()

    def show_bootprelay_info(self, *args, **kwargs):
        return self.base_function()
