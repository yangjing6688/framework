"""
Base class for all bgp commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class BgpBase(CliBaseApi):
    def __init__(self, device):
        super(BgpBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def create_as(self, *args, **kwargs):
        return self.base_function()

    def delete_as(self, *args, **kwargs):
        return self.base_function()

    def set_router_id(self, *args, **kwargs):
        return self.base_function()

    def clear_router_id(self, *args, **kwargs):
        return self.base_function()

    def create_neighbor(self, *args, **kwargs):
        return self.base_function()

    def create_neighbor_link_local(self, *args, **kwargs):
        return self.base_function()

    def delete_neighbor(self, *args, **kwargs):
        return self.base_function()

    def delete_neighbor_link_local(self, *args, **kwargs):
        return self.base_function()

    def enable_neighbor(self, *args, **kwargs):
        return self.base_function()

    def enable_neighbor_link_local(self, *args, **kwargs):
        return self.base_function()

    def disable_neighbor(self, *args, **kwargs):
        return self.base_function()

    def disable_neighbor_link_local(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute(self, *args, **kwargs):
        return self.base_function()

    def clear_redistribute(self, *args, **kwargs):
        return self.base_function()

    def set_neighbor_password(self, *args, **kwargs):
        return self.base_function()

    def show_all_routes(self, *args, **kwargs):
        return self.base_function()

    def show_neighbors(self, *args, **kwargs):
        return self.base_function()

    def show_status(self, *args, **kwargs):
        return self.base_function()

    def clear_neighbor(self, *args, **kwargs):
        return self.base_function()

    def clear_neighbor_all(self, *args, **kwargs):
        return self.base_function()

    def enable_neighbor_capability(self, *args, **kwargs):
        return self.base_function()

    def disable_neighbor_capability(self, *args, **kwargs):
        return self.base_function()

    def set_auto_peering(self, *args, **kwargs):
        return self.base_function()

    def clear_auto_peering(self, *args, **kwargs):
        return self.base_function()

    def show_route_ip(self, *args, **kwargs):
        return self.base_function()

    def show_redistributed_routes(self, *args, **kwargs):
        return self.base_function()

    def show_networks(self, *args, **kwargs):
        return self.base_function()

    def show_peer_group(self, *args, **kwargs):
        return self.base_function()

    def show_stats(self, *args, **kwargs):
        return self.base_function()

    def show_summary(self, *args, **kwargs):
        return self.base_function()
