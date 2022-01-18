"""
Base class for all common commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class CommonBase(CliBaseApi):
    def __init__(self, device):
        super(CommonBase, self).__init__()
        self.device = device

    def get_dir(self, *args, **kwargs):
        return self.base_function()

    def remove_file(self, *args, **kwargs):
        return self.base_function()
