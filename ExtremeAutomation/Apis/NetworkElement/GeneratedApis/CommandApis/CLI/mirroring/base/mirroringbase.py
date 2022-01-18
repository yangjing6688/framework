"""
Base class for all mirroring commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class MirroringBase(CliBaseApi):
    def __init__(self, device):
        super(MirroringBase, self).__init__()
        self.device = device

    def create_both(self, *args, **kwargs):
        return self.base_function()

    def create_ingress(self, *args, **kwargs):
        return self.base_function()

    def create_egress(self, *args, **kwargs):
        return self.base_function()

    def delete_port_mirror(self, *args, **kwargs):
        return self.base_function()

    def enable_port(self, *args, **kwargs):
        return self.base_function()

    def disable_port(self, *args, **kwargs):
        return self.base_function()

    def show_port_mirror(self, *args, **kwargs):
        return self.base_function()

    def show_port_mirror_all(self, *args, **kwargs):
        return self.base_function()

    def create_remote_both(self, *args, **kwargs):
        return self.base_function()

    def create_portlist(self, *args, **kwargs):
        return self.base_function()

    def set_source_port_both(self, *args, **kwargs):
        return self.base_function()

    def set_source_port_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_source_port_ingress(self, *args, **kwargs):
        return self.base_function()

    def set_source_port_egress(self, *args, **kwargs):
        return self.base_function()

    def clear_source_port(self, *args, **kwargs):
        return self.base_function()

    def enable_remote_ping_check(self, *args, **kwargs):
        return self.base_function()

    def disable_remote_ping_check(self, *args, **kwargs):
        return self.base_function()

    def set_description(self, *args, **kwargs):
        return self.base_function()
