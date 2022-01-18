"""
Base class for all logging commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class LoggingBase(CliBaseApi):
    def __init__(self, device):
        super(LoggingBase, self).__init__()
        self.device = device

    def clear_log(self, *args, **kwargs):
        return self.base_function()

    def show_log(self, *args, **kwargs):
        return self.base_function()

    def clear_log_auditlog(self, *args, **kwargs):
        return self.base_function()

    def clear_log_raslog(self, *args, **kwargs):
        return self.base_function()

    def show_log_auditlog(self, *args, **kwargs):
        return self.base_function()

    def show_log_raslog(self, *args, **kwargs):
        return self.base_function()
