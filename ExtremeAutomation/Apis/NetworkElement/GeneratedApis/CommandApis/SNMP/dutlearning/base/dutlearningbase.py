"""
Base class for all dutlearning SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class DutlearningBase(SnmpBaseApi):
    def __init__(self, device):
        super(DutlearningBase, self).__init__()
        self.device = device

    def getnext_system_location_dot_zero(self, *args, **kwargs):
        return self.base_function()

    def walk_system(self, *args, **kwargs):
        return self.base_function()

    def bulkwalk_system(self, *args, **kwargs):
        return self.base_function()
