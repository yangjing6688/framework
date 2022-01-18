"""
Base class for all iprouting commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class IproutingBase(CliBaseApi):
    def __init__(self, device):
        super(IproutingBase, self).__init__()
        self.device = device

    def create_static_route(self, *args, **kwargs):
        return self.base_function()

    def delete_static_route(self, *args, **kwargs):
        return self.base_function()

    def show_static_route(self, *args, **kwargs):
        return self.base_function()

    def show_all_routes(self, *args, **kwargs):
        return self.base_function()

    def enable_ipmcforwarding_global(self, *args, **kwargs):
        return self.base_function()

    def enable_ipmcforwarding_ipv4_global(self, *args, **kwargs):
        return self.base_function()

    def enable_ipmcforwarding_ipv6_global(self, *args, **kwargs):
        return self.base_function()

    def enable_ipmcforwarding_ipv4_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_ipmcforwarding_ipv6_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_ipmcforwarding_global(self, *args, **kwargs):
        return self.base_function()

    def disable_ipmcforwarding_ipv4_global(self, *args, **kwargs):
        return self.base_function()

    def disable_ipmcforwarding_ipv6_global(self, *args, **kwargs):
        return self.base_function()

    def disable_ipmcforwarding_ipv4_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_ipmcforwarding_ipv6_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_all_ipv6_routes(self, *args, **kwargs):
        return self.base_function()

    def show_ip_route_vrf(self, *args, **kwargs):
        return self.base_function()

    def show_ipv6_route_vrf(self, *args, **kwargs):
        return self.base_function()
