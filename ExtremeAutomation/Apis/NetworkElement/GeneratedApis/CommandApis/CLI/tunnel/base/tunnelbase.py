"""
Base class for all tunnel commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class TunnelBase(CliBaseApi):
    def __init__(self, device):
        super(TunnelBase, self).__init__()
        self.device = device

    def create_interface(self, *args, **kwargs):
        return self.base_function()

    def delete_interface(self, *args, **kwargs):
        return self.base_function()

    def enable_interface(self, *args, **kwargs):
        return self.base_function()

    def disable_interface(self, *args, **kwargs):
        return self.base_function()

    def set_mode_gre(self, *args, **kwargs):
        return self.base_function()

    def set_mode_vxlan(self, *args, **kwargs):
        return self.base_function()

    def set_mode_vxlan_l2tb_port(self, *args, **kwargs):
        return self.base_function()

    def set_mode_gre_l2_port(self, *args, **kwargs):
        return self.base_function()

    def set_source_ip(self, *args, **kwargs):
        return self.base_function()

    def set_dest_ip(self, *args, **kwargs):
        return self.base_function()

    def show_all(self, *args, **kwargs):
        return self.base_function()

    def clear_source_ip(self, *args, **kwargs):
        return self.base_function()

    def clear_dest_ip(self, *args, **kwargs):
        return self.base_function()

    def clear_mode_gre(self, *args, **kwargs):
        return self.base_function()

    def show_tunnel(self, *args, **kwargs):
        return self.base_function()
