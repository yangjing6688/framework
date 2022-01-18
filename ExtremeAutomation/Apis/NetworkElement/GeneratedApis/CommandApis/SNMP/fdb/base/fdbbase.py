"""
Base class for all fdb SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class FdbBase(SnmpBaseApi):
    def __init__(self, device):
        super(FdbBase, self).__init__()
        self.device = device

    def show_all_entries(self, *args, **kwargs):
        return self.base_function()

    def show_entry(self, *args, **kwargs):
        return self.base_function()

    def show_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_port(self, *args, **kwargs):
        return self.base_function()
