"""
Base class for all bridgemode commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class BridgemodeBase(CliBaseApi):
    def __init__(self, device):
        super(BridgemodeBase, self).__init__()
        self.device = device

    def set_mode(self, *args, **kwargs):
        return self.base_function()

    def show_mode(self, *args, **kwargs):
        return self.base_function()
