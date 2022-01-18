"""
Base class for all rsmlt commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class RsmltBase(CliBaseApi):
    def __init__(self, device):
        super(RsmltBase, self).__init__()
        self.device = device

    def enable_edge_support(self, *args, **kwargs):
        return self.base_function()

    def disable_edge_support(self, *args, **kwargs):
        return self.base_function()

    def enable_vlan_interface(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan_interface(self, *args, **kwargs):
        return self.base_function()

    def set_interface_holddown_timer(self, *args, **kwargs):
        return self.base_function()

    def set_interface_holdup_timer(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_edge_support(self, *args, **kwargs):
        return self.base_function()

    def show_vrf(self, *args, **kwargs):
        return self.base_function()

    def show_vrfid(self, *args, **kwargs):
        return self.base_function()

    def show_local(self, *args, **kwargs):
        return self.base_function()

    def show_local_vrf(self, *args, **kwargs):
        return self.base_function()

    def show_local_vrfid(self, *args, **kwargs):
        return self.base_function()

    def show_peer(self, *args, **kwargs):
        return self.base_function()

    def show_peer_vrf(self, *args, **kwargs):
        return self.base_function()

    def show_peer_vrfid(self, *args, **kwargs):
        return self.base_function()
