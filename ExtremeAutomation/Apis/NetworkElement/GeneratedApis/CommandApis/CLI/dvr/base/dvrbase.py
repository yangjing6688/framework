"""
Base class for all dvr commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class DvrBase(CliBaseApi):
    def __init__(self, device):
        super(DvrBase, self).__init__()
        self.device = device

    def set_domain_controller(self, *args, **kwargs):
        return self.base_function()

    def clear_domain_controller(self, *args, **kwargs):
        return self.base_function()

    def disable_domain_controller_inject_default_route_all(self, *args, **kwargs):
        return self.base_function()

    def disable_domain_controller_inject_default_route(self, *args, **kwargs):
        return self.base_function()

    def set_leaf_id(self, *args, **kwargs):
        return self.base_function()

    def set_leaf_virtual_ist(self, *args, **kwargs):
        return self.base_function()

    def clear_leaf_virtual_ist(self, *args, **kwargs):
        return self.base_function()

    def set_interface_gateway_ipv4(self, *args, **kwargs):
        return self.base_function()

    def clear_interface_gateway_ipv4(self, *args, **kwargs):
        return self.base_function()

    def enable_interface(self, *args, **kwargs):
        return self.base_function()

    def disable_interface(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_direct_metric(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_vrf(self, *args, **kwargs):
        return self.base_function()

    def clear_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def enable_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def disable_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_static(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_static_metric(self, *args, **kwargs):
        return self.base_function()

    def clear_redistribute_static(self, *args, **kwargs):
        return self.base_function()

    def enable_redistribute_static(self, *args, **kwargs):
        return self.base_function()

    def disable_redistribute_static(self, *args, **kwargs):
        return self.base_function()

    def clear_host_entries(self, *args, **kwargs):
        return self.base_function()

    def clear_host_entries_ipv4(self, *args, **kwargs):
        return self.base_function()

    def clear_host_entries_ipv4_l3isid(self, *args, **kwargs):
        return self.base_function()

    def clear_host_entries_l2isid(self, *args, **kwargs):
        return self.base_function()

    def clear_host_entries_l3isid(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_interfaces(self, *args, **kwargs):
        return self.base_function()

    def show_members(self, *args, **kwargs):
        return self.base_function()

    def show_backbone_entries(self, *args, **kwargs):
        return self.base_function()

    def show_backbone_members(self, *args, **kwargs):
        return self.base_function()

    def show_database(self, *args, **kwargs):
        return self.base_function()

    def show_host_entries(self, *args, **kwargs):
        return self.base_function()

    def show_l3vsn(self, *args, **kwargs):
        return self.base_function()

    def show_redistribute(self, *args, **kwargs):
        return self.base_function()

    def show_routes(self, *args, **kwargs):
        return self.base_function()
