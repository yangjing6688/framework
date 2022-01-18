"""
Base class for all vrrp commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class VrrpBase(CliBaseApi):
    def __init__(self, device):
        super(VrrpBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def enable_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_vlan_fabric_routing(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan_fabric_routing(self, *args, **kwargs):
        return self.base_function()

    def create_vlan(self, *args, **kwargs):
        return self.base_function()

    def clear_vlan(self, *args, **kwargs):
        return self.base_function()

    def create_group(self, *args, **kwargs):
        return self.base_function()

    def clear_group(self, *args, **kwargs):
        return self.base_function()

    def set_vlan_priority(self, *args, **kwargs):
        return self.base_function()

    def set_vlan_ipaddress(self, *args, **kwargs):
        return self.base_function()

    def show_all(self, *args, **kwargs):
        return self.base_function()

    def show_detail(self, *args, **kwargs):
        return self.base_function()

    def show_group(self, *args, **kwargs):
        return self.base_function()

    def show_group_all(self, *args, **kwargs):
        return self.base_function()

    def show_virtual_router(self, *args, **kwargs):
        return self.base_function()

    def show_virtual_router_all(self, *args, **kwargs):
        return self.base_function()

    def show_vr(self, *args, **kwargs):
        return self.base_function()

    def show_vr_all(self, *args, **kwargs):
        return self.base_function()

    def show_vlan(self, *args, **kwargs):
        return self.base_function()
