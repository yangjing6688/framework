"""
Base class for all vrf commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class VrfBase(CliBaseApi):
    def __init__(self, device):
        super(VrfBase, self).__init__()
        self.device = device

    def create_router(self, *args, **kwargs):
        return self.base_function()

    def create_router_with_vrfid(self, *args, **kwargs):
        return self.base_function()

    def delete_router(self, *args, **kwargs):
        return self.base_function()

    def enable_trap(self, *args, **kwargs):
        return self.base_function()

    def disable_trap(self, *args, **kwargs):
        return self.base_function()

    def enable_max_routes_trap(self, *args, **kwargs):
        return self.base_function()

    def disable_max_routes_trap(self, *args, **kwargs):
        return self.base_function()

    def enable_mvpn(self, *args, **kwargs):
        return self.base_function()

    def disable_mvpn(self, *args, **kwargs):
        return self.base_function()

    def enable_ipv6_max_routes_trap(self, *args, **kwargs):
        return self.base_function()

    def disable_ipv6_max_routes_trap(self, *args, **kwargs):
        return self.base_function()

    def enable_ipvpn(self, *args, **kwargs):
        return self.base_function()

    def disable_ipvpn(self, *args, **kwargs):
        return self.base_function()

    def enable_isis_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def disable_isis_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def set_mvpn_fwd_cache_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_max_routes(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_max_routes(self, *args, **kwargs):
        return self.base_function()

    def set_name(self, *args, **kwargs):
        return self.base_function()

    def set_vrfid(self, *args, **kwargs):
        return self.base_function()

    def set_interface_vlan(self, *args, **kwargs):
        return self.base_function()

    def clear_interface_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_ipvpn(self, *args, **kwargs):
        return self.base_function()

    def set_isid(self, *args, **kwargs):
        return self.base_function()

    def set_isis_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def clear_isis_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def set_isis_redistribute_direct_apply(self, *args, **kwargs):
        return self.base_function()

    def show_all(self, *args, **kwargs):
        return self.base_function()

    def show_max_routes(self, *args, **kwargs):
        return self.base_function()

    def show_max_routes_all(self, *args, **kwargs):
        return self.base_function()

    def show_max_routes_name(self, *args, **kwargs):
        return self.base_function()

    def show_ipv6_max_routes(self, *args, **kwargs):
        return self.base_function()

    def show_ipv6_max_routes_all(self, *args, **kwargs):
        return self.base_function()

    def show_ipv6_max_routes_name(self, *args, **kwargs):
        return self.base_function()

    def show_mvpn(self, *args, **kwargs):
        return self.base_function()

    def show_vrfids(self, *args, **kwargs):
        return self.base_function()

    def show_name(self, *args, **kwargs):
        return self.base_function()

    def show_ip_route(self, *args, **kwargs):
        return self.base_function()

    def show_ip_routing(self, *args, **kwargs):
        return self.base_function()

    def show_vrfid_ip_routing(self, *args, **kwargs):
        return self.base_function()

    def show_isid_list(self, *args, **kwargs):
        return self.base_function()

    def show_interface_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_ipvpn(self, *args, **kwargs):
        return self.base_function()

    def show_isis_redistribute_direct(self, *args, **kwargs):
        return self.base_function()
