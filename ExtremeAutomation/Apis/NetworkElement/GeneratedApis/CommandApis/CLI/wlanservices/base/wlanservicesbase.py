"""
Base class for all wlanservices commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class WlanservicesBase(CliBaseApi):
    def __init__(self, device):
        super(WlanservicesBase, self).__init__()
        self.device = device

    def show_all(self, *args, **kwargs):
        return self.base_function()

    def show_detail(self, *args, **kwargs):
        return self.base_function()
