"""
Base class for all arp SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class ArpBase(SnmpBaseApi):
    def __init__(self, device):
        super(ArpBase, self).__init__()
        self.device = device

    def show_all_entries(self, *args, **kwargs):
        return self.base_function()

    def show_entry(self, *args, **kwargs):
        return self.base_function()
