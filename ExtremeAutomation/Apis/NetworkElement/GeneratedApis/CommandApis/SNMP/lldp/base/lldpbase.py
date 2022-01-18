"""
Base class for all lldp SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class LldpBase(SnmpBaseApi):
    def __init__(self, device):
        super(LldpBase, self).__init__()
        self.device = device

    def set_tx_interval(self, *args, **kwargs):
        return self.base_function()

    def set_tx_hold_multiplier(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()
