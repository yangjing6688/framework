"""
Base class for all vxlan commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class VxlanBase(CliBaseApi):
    def __init__(self, device):
        super(VxlanBase, self).__init__()
        self.device = device

    def create_logical_switch(self, *args, **kwargs):
        return self.base_function()

    def delete_logical_switch(self, *args, **kwargs):
        return self.base_function()

    def create_logical_switch_to_vni_map(self, *args, **kwargs):
        return self.base_function()

    def create_logical_switch_to_vlan_map(self, *args, **kwargs):
        return self.base_function()

    def create_logical_switch_vni_vlan_map(self, *args, **kwargs):
        return self.base_function()

    def set_remote_vtep(self, *args, **kwargs):
        return self.base_function()

    def clear_remote_vtep(self, *args, **kwargs):
        return self.base_function()

    def show_logical_switch(self, *args, **kwargs):
        return self.base_function()
