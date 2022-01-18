"""
Base class for all unittest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class UnittestBase(CliBaseApi):
    def __init__(self, device):
        super(UnittestBase, self).__init__()
        self.device = device

    def function(self, *args, **kwargs):
        return self.base_function()
