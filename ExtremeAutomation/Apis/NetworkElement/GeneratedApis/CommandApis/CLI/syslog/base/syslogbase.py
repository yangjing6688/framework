"""
Base class for all syslog commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class SyslogBase(CliBaseApi):
    def __init__(self, device):
        super(SyslogBase, self).__init__()
        self.device = device

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_target_info(self, *args, **kwargs):
        return self.base_function()
