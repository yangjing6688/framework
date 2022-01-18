"""
Base class for all site commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class SiteBase(CliBaseApi):
    def __init__(self, device):
        super(SiteBase, self).__init__()
        self.device = device

    def show_all(self, *args, **kwargs):
        return self.base_function()

    def show_detail(self, *args, **kwargs):
        return self.base_function()
