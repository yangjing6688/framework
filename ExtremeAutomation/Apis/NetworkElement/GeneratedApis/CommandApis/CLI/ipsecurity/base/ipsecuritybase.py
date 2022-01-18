"""
Base class for all ipsecurity commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class IpsecurityBase(CliBaseApi):
    def __init__(self, device):
        super(IpsecurityBase, self).__init__()
        self.device = device

    def set_trusted_port(self, *args, **kwargs):
        return self.base_function()

    def enable_dhcp_snooping(self, *args, **kwargs):
        return self.base_function()

    def disable_dhcp_snooping(self, *args, **kwargs):
        return self.base_function()

    def show_snooping_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_snooping_vlan_entries(self, *args, **kwargs):
        return self.base_function()

    def show_snooping_vlan_violations(self, *args, **kwargs):
        return self.base_function()

    def show_trusted_ports(self, *args, **kwargs):
        return self.base_function()
