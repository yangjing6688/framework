"""
Base class for all unit commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class UnitBase(CliBaseApi):
    def __init__(self, device):
        super(UnitBase, self).__init__()
        self.device = device

    def change_current_slot(self, *args, **kwargs):
        return self.base_function()

    def exit_current_slot(self, *args, **kwargs):
        return self.base_function()
