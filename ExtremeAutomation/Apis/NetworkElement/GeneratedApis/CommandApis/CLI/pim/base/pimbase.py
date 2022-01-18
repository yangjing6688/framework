"""
Base class for all pim commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class PimBase(CliBaseApi):
    def __init__(self, device):
        super(PimBase, self).__init__()
        self.device = device

    def enable(self, *args, **kwargs):
        return self.base_function()

    def disable(self, *args, **kwargs):
        return self.base_function()

    def enable_sparse(self, *args, **kwargs):
        return self.base_function()

    def disable_sparse(self, *args, **kwargs):
        return self.base_function()

    def set_rp(self, *args, **kwargs):
        return self.base_function()

    def set_bsr_priority(self, *args, **kwargs):
        return self.base_function()

    def clear_cache(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_bsr(self, *args, **kwargs):
        return self.base_function()

    def show_rp(self, *args, **kwargs):
        return self.base_function()

    def show_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_cache(self, *args, **kwargs):
        return self.base_function()

    def show_cache_group(self, *args, **kwargs):
        return self.base_function()

    def show_rp_set(self, *args, **kwargs):
        return self.base_function()

    def show_rp_set_group(self, *args, **kwargs):
        return self.base_function()

    def enable_interface(self, *args, **kwargs):
        return self.base_function()

    def enable_interface_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_ssm(self, *args, **kwargs):
        return self.base_function()

    def disable_interface(self, *args, **kwargs):
        return self.base_function()

    def disable_interface_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_bsr_priority_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_rp_static(self, *args, **kwargs):
        return self.base_function()

    def set_interface_active(self, *args, **kwargs):
        return self.base_function()

    def set_interface_passive(self, *args, **kwargs):
        return self.base_function()

    def set_vlan_active(self, *args, **kwargs):
        return self.base_function()

    def set_vlan_passive(self, *args, **kwargs):
        return self.base_function()

    def clear_rp(self, *args, **kwargs):
        return self.base_function()

    def show_interface(self, *args, **kwargs):
        return self.base_function()
