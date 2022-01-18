"""
Base class for all arp commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class ArpBase(CliBaseApi):
    def __init__(self, device):
        super(ArpBase, self).__init__()
        self.device = device

    def create_entry(self, *args, **kwargs):
        return self.base_function()

    def create_entry_interface(self, *args, **kwargs):
        return self.base_function()

    def delete_entry(self, *args, **kwargs):
        return self.base_function()

    def clear_all_entries(self, *args, **kwargs):
        return self.base_function()

    def show_all_entries(self, *args, **kwargs):
        return self.base_function()

    def show_entry(self, *args, **kwargs):
        return self.base_function()

    def create_entry_port(self, *args, **kwargs):
        return self.base_function()

    def create_entry_port_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_vrf_entry(self, *args, **kwargs):
        return self.base_function()
